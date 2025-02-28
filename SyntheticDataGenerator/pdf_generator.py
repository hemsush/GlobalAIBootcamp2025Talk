from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import random
from datetime import datetime

# Output directory for PDF bills
output_dir = "aws_bills"
os.makedirs(output_dir, exist_ok=True)

# AWS Services with Pricing Models
AWS_SERVICES = [
    {"Service": "EC2", "Instance Type": "t3.medium", "Rate": 0.0416, "Unit": "per hour"},
    {"Service": "S3", "Instance Type": "Standard Storage", "Rate": 0.023, "Unit": "per GB"},
    {"Service": "Lambda", "Instance Type": "Invocations", "Rate": 0.00001667, "Unit": "per request"},
    {"Service": "RDS", "Instance Type": "db.m5.large", "Rate": 0.10, "Unit": "per hour"},
    {"Service": "EKS", "Instance Type": "Cluster Management", "Rate": 0.10, "Unit": "per hour"},
    {"Service": "CloudFront", "Instance Type": "Data Transfer", "Rate": 0.085, "Unit": "per GB"},
    {"Service": "DynamoDB", "Instance Type": "Read/Write Units", "Rate": 0.00065, "Unit": "per request"},
    {"Service": "EBS", "Instance Type": "GP3 Storage", "Rate": 0.08, "Unit": "per GB"},
    {"Service": "VPC", "Instance Type": "VPN Connection", "Rate": 0.05, "Unit": "per hour"},
    {"Service": "CloudWatch", "Instance Type": "Logs & Metrics", "Rate": 0.30, "Unit": "per GB"},
    {"Service": "Route 53", "Instance Type": "DNS Queries", "Rate": 0.0005, "Unit": "per query"},
    {"Service": "SNS", "Instance Type": "Messages", "Rate": 0.0004, "Unit": "per message"},
    {"Service": "SQS", "Instance Type": "Queue Messages", "Rate": 0.0004, "Unit": "per message"},
    {"Service": "Glue", "Instance Type": "ETL Jobs", "Rate": 0.44, "Unit": "per hour"},
    {"Service": "Redshift", "Instance Type": "Compute Node", "Rate": 0.24, "Unit": "per hour"},
]

# Generate random AWS usage data
def generate_usage(service):
    if service["Unit"] == "per hour":
        return random.randint(50, 500)  # Simulated hours
    elif service["Unit"] == "per GB":
        return random.randint(100, 5000)  # Simulated storage usage
    elif service["Unit"] == "per request" or service["Unit"] == "per message" or service["Unit"] == "per query":
        return random.randint(100000, 10000000)  # Simulated API requests

# Generate AWS bills for multiple accounts over 12 months
accounts = ["123456789012", "987654321098", "567890123456"]
months = [datetime(2024, m, 1).strftime("%b-%Y") for m in range(1, 13)]

for account in accounts:
    for month in months:
        file_path = os.path.join(output_dir, f"aws_bill_{account}_{month}.pdf")

        c = canvas.Canvas(file_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        c.drawString(100, 750, f"AWS Billing Statement - {month}")
        c.drawString(100, 730, f"Account ID: {account}")
        c.drawString(100, 710, "----------------------------------")

        y = 680
        total_cost = 0

        for service in AWS_SERVICES:
            usage = generate_usage(service)
            cost = round(usage * service["Rate"], 2)
            total_cost += cost

            c.drawString(100, y, f"Service: {service['Service']}, Type: {service['Instance Type']}, Usage: {usage} {service['Unit']}, Cost: ${cost}")
            y -= 20

        # Total cost
        c.drawString(100, y - 20, f"Total Cost: ${round(total_cost, 2)}")

        # Ensure the PDF closes properly with an explicit EOF marker
        c.showPage()
        c.save()

        # Append EOF marker manually
        with open(file_path, "ab") as f:
            f.write(b"\n%%EOF")

print(f" Successfully generated AWS billing PDFs in '{output_dir}/' with proper EOF markers!")
