import json
import csv
import argparse
import sys

# Import the get_customers function from Test7.py
try:
    from Test7 import get_customers
except Exception:
    # If running as a script where module import path differs, try relative import
    try:
        from .Test7 import get_customers
    except Exception as e:
        print("Failed to import get_customers from Test7.py:", e)
        sys.exit(1)


def save_json(customers, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(customers, fh, ensure_ascii=False, indent=2)


def save_csv(customers, path):
    if not customers:
        return
    keys = set()
    for c in customers:
        keys.update(c.keys())
    keys = list(keys)
    with open(path, "w", encoding="utf-8", newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        for c in customers:
            writer.writerow(c)


def main():
    parser = argparse.ArgumentParser(description="Run get_customers and save results")
    parser.add_argument("--output", "-o", type=str, default="customers.json",
                        help="Output file path for JSON (or CSV if --csv)")
    parser.add_argument("--csv", action="store_true", help="Also write CSV (output.csv)")
    parser.add_argument("--no-save", action="store_true", help="Do not save files, just print")
    args = parser.parse_args()

    customers = get_customers()

    # Print a pretty view
    print("Found {} customers:".format(len(customers)))
    for c in customers:
        print("- {}: {}".format(c.get("id"), c.get("name")))

    if not args.no_save:
        # Save JSON
        save_json(customers, args.output)
        print(f"Saved JSON -> {args.output}")
        if args.csv:
            csv_path = args.output.rsplit('.', 1)[0] + '.csv' if '.' in args.output else args.output + '.csv'
            save_csv(customers, csv_path)
            print(f"Saved CSV  -> {csv_path}")


if __name__ == '__main__':
    main()
