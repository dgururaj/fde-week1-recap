import csv

file_name = "data/homework_invoices.csv"

total_invoices = 0
high_value_invoices = 0
invalid_amount_invoices = 0

try:
    with open(file_name, mode="r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for invoice in reader:
            total_invoices += 1

            vendor = invoice["vendor"]
            amount = invoice["amount"]
            status = invoice["status"]

            print(f"Vendor: {vendor}")
            print(f"Amount: {amount}")
            print(f"Status: {status}")

            try:
                # Check for missing amount
                if not amount or amount.strip() == "":
                    raise ValueError("Missing amount")

                # Convert amount to number
                amount_value = float(amount)

                # Check amount greater than 100,000
                if amount_value > 100000:
                    high_value_invoices += 1
                    print(">>> Amount is greater than 100,000")

            except ValueError:
                invalid_amount_invoices += 1
                print(">>> Invalid or missing amount")

            print("-" * 40)

except FileNotFoundError:
    print(f"File not found: {file_name}")

# Final summary
print("\n========== SUMMARY ==========")
print(f"Total invoices read: {total_invoices}")
print(f"Invoices > 100,000: {high_value_invoices}")
print(f"Missing/invalid amount: {invalid_amount_invoices}")