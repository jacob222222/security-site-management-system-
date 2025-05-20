import csv
from datetime import datetime

def calculate_days(start, end):
    if not end:
        return "Open"
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    return (end_date - start_date).days

def generate_sla_report(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"{'Ticket':<8} {'Status':<12} {'Days Open':<10}")
        print("-" * 32)
        for row in reader:
            days_open = calculate_days(row['date_opened'], row['date_closed'] or '')
            print(f"{row['ticket_id']:<8} {row['status']:<12} {days_open:<10}")

if __name__ == "__main__":
    generate_sla_report('data/issues.csv')
