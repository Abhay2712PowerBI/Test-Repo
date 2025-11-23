from typing import List, Optional, Tuple
import argparse
import json

# calculate_tax.py
"""
Simple progressive tax calculator.
Usage:
    python calculate_tax.py --income 85000 --deduction 12550
"""


Bracket = Tuple[Optional[float], float]  # (upper_limit, rate)

# Example progressive brackets (upper limits are cumulative). None means no upper bound.
DEFAULT_BRACKETS: List[Bracket] = [
        (10275, 0.10),
        (41775, 0.12),
        (89075, 0.22),
        (170050, 0.24),
        (215950, 0.32),
        (539900, 0.35),
        (None, 0.37),
]


def calculate_tax(income: float, brackets: List[Bracket]) -> float:
        """
        Calculate tax owed on taxable income using progressive brackets.

        income: taxable income (after deductions)
        brackets: list of (upper_limit, rate). upper_limit is cumulative; None means open-ended.
        """
        tax = 0.0
        prev_limit = 0.0
        remaining = income

        for upper, rate in brackets:
                if upper is None:
                        taxable = max(0.0, remaining)
                else:
                        bracket_size = max(0.0, upper - prev_limit)
                        taxable = min(bracket_size, max(0.0, remaining))

                tax += taxable * rate
                remaining -= taxable

                if upper is not None:
                        prev_limit = upper

                if remaining <= 0:
                        break

        return round(tax, 2)


def summary(gross_income: float, deduction: float = 0.0, brackets: List[Bracket] = DEFAULT_BRACKETS) -> dict:
        taxable_income = max(0.0, gross_income - deduction)
        tax = calculate_tax(taxable_income, brackets)
        after_tax = gross_income - tax
        effective_rate = (tax / gross_income) if gross_income > 0 else 0.0
        return {
                "gross_income": round(gross_income, 2),
                "deduction": round(deduction, 2),
                "taxable_income": round(taxable_income, 2),
                "tax": tax,
                "after_tax_income": round(after_tax, 2),
                "effective_rate": round(effective_rate, 4),
        }


def parse_args():
        parser = argparse.ArgumentParser(description="Progressive tax calculator")
        parser.add_argument("--income", type=float, required=True, help="Gross income")
        parser.add_argument("--deduction", type=float, default=0.0, help="Deduction (standard/itemized)")
        parser.add_argument("--brackets-file", type=str, help="Optional JSON file with brackets")
        return parser.parse_args()


if __name__ == "__main__":
        args = parse_args()
        result = summary(args.income, args.deduction)
        # Simple text output
        print(f"Gross income:       ${result['gross_income']:,}")
        print(f"Deduction:          ${result['deduction']:,}")
        print(f"Taxable income:     ${result['taxable_income']:,}")
        print(f"Tax owed:           ${result['tax']:,}")
        print(f"After-tax income:   ${result['after_tax_income']:,}")
        print(f"Effective tax rate: {result['effective_rate'] * 100:.2f}%")
        if args.brackets_file:
            try:
                with open(args.brackets_file, "r", encoding="utf-8") as fh:
                    data = json.load(fh)

                custom_brackets = []
                for item in data:
                    if isinstance(item, (list, tuple)):
                        upper, rate = item
                    elif isinstance(item, dict):
                        upper, rate = item.get("upper"), item.get("rate")
                    else:
                        raise ValueError("Invalid bracket entry; expected list/tuple or dict")

                    upper_val = None if upper is None else float(upper)
                    custom_brackets.append((upper_val, float(rate)))

                custom_result = summary(args.income, args.deduction, custom_brackets)
                print("\n[Using custom brackets]")
                print("Tax owed (custom):      ${:,.2f}".format(custom_result["tax"]))
                print("After-tax income (custom): ${:,.2f}".format(custom_result["after_tax_income"]))
            except Exception as e:
                print("Failed to load/parse brackets file:", e)        