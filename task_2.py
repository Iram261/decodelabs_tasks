def main():
    print("=" * 40)
    print("      EXPENSE TRACKER      ")
    print("=" * 40)
    print("Instructions: Enter expense amounts one by one.")
    print("Type 'exit' or 'quit' to finish and see the total.\n")

    
    total_spent = 0.0

    while True:
        user_input = input("Enter expense amount (or 'exit'): ").strip().lower()

        
        if user_input in ['exit', 'quit']:
            break

        try:
            
            expense = float(user_input)

            if expense < 0:
                print("❌ Expense cannot be negative. Please enter a valid amount.")
                continue

            
            total_spent += expense
            print(add_success_message(expense, total_spent))

        except ValueError:
            
            print("❌ Invalid input. Please enter a valid numerical amount.")

    
    print("\n" + "=" * 40)
    print(f" TOTAL SPENT = ${total_spent:,.2f}")
    print("=" * 40)


def add_success_message(amount, current_total):
    """Helper function to keep the loop code clean and readable."""
    return f"✔️ Added ${amount:,.2f} | Current Total: ${current_total:,.2f}"


if __name__ == "__main__":
    main()