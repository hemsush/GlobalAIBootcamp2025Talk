"""
AWS Billing CSV Generator

This script generates synthetic AWS billing data for multiple accounts and services,
including EC2, S3, Lambda, RDS, and more. The generated data includes usage metrics,
cost breakdowns, and account details for realistic financial analysis.

Author: Hema
Date: March 2025

Usage:
    Run this script to generate a CSV file containing AWS billing data.
    The output file can be used for cost optimization analysis, RAG-based LLM agent
    training, and dashboard visualizations.
"""



import os
import csv
import random
from datetime import datetime

# Output directory for CSV bills
output_dir = "aws_bills"
os.makedirs(output_dir, exist_ok=True)

# AWS Services & Pricing
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
        return random.randint(50, 500)
    elif service["Unit"] == "per GB":
        return random.randint(100, 5000)
    elif service["Unit"] in ["per request", "per message", "per query"]:
        return random.randint(100000, 10000000)
    return random.randint(1, 100)

# Generate AWS cost data for multiple accounts over 12 months
accounts = ["123456789012", "987654321098", "567890123456"]
months = [datetime(2024, m, 1).strftime("%b-%Y") for m in range(1, 13)]

for account in accounts:
    csv_filename = os.path.join(output_dir, f"aws_bill_{account}.csv")

    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Account ID", "Month", "Service", "Instance Type", "Usage", "Unit", "Cost"])

        for month in months:
            for service in AWS_SERVICES:
                usage = generate_usage(service)
                cost = round(usage * service["Rate"], 2)

                writer.writerow([account, month, service["Service"], service["Instance Type"], usage, service["Unit"], cost])

    print(f"CSV generated: {csv_filename}")

print(f" All AWS billing CSVs stored in '{output_dir}/' for analysis!")
