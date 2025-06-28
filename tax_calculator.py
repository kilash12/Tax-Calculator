def calculate_old_regime_tax(income):
    # Standard deductions and exemptions
    standard_deduction = 50000
    section_80C = 150000  # Max under 80C
    hra = 60000  # Assumed HRA
    total_deductions = standard_deduction + section_80C + hra

    taxable_income = max(0, income - total_deductions)
    
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.2
    else:
        tax = (250000 * 0.05) + (500000 * 0.2) + (taxable_income - 1000000) * 0.3
    
    return tax


def calculate_new_regime_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 750000:
        tax = (250000 * 0.05) + (income - 500000) * 0.1
    elif income <= 1000000:
        tax = (250000 * 0.05) + (250000 * 0.1) + (income - 750000) * 0.15
    elif income <= 1250000:
        tax = (250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (income - 1000000) * 0.2
    elif income <= 1500000:
        tax = (250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (income - 1250000) * 0.25
    else:
        tax = (250000 * 0.05) + (250000 * 0.1) + (250000 * 0.15) + (250000 * 0.2) + (250000 * 0.25) + (income - 1500000) * 0.3

    return tax


def main():
    print("---- Tax Deduction Calculator (Old vs New Regime) ----")
    try:
        ctc = float(input("Enter your Total CTC (₹): "))
        bonus = float(input("Enter your Bonus amount (₹): "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    total_income = ctc + bonus
    print(f"\nTotal Income (CTC + Bonus): ₹{total_income:.2f}")

    old_tax = calculate_old_regime_tax(total_income)
    new_tax = calculate_new_regime_tax(total_income)

    print("\n--- Tax Comparison ---")
    print(f"Old Regime Tax: ₹{old_tax:.2f}")
    print(f"New Regime Tax: ₹{new_tax:.2f}")

    if old_tax < new_tax:
        print("👉 You save more under the **Old Regime**.")
    elif new_tax < old_tax:
        print("👉 You save more under the **New Regime**.")
    else:
        print("👉 Both regimes result in the same tax.")

if __name__ == "__main__":
    main()
