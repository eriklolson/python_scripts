#!/usr/bin/env python3

from datetime import datetime, timedelta

def calculate_dates(meds_filled_date, meds_quantity, days_prior_fill):
    try:
        # Convert input date string to datetime object
        filled_date = datetime.strptime(meds_filled_date, "%Y-%m-%d")
        
        # Calculate the date when the meds will run out
        meds_run_out_date = filled_date + timedelta(days=meds_quantity)
        
        # Calculate the next fillable date
        fillable_date = meds_run_out_date - timedelta(days=days_prior_fill)
        
        # Calculate the order refill date (7 business days before meds run out)
        order_refill_date = subtract_business_days(meds_run_out_date, 7)

        return (
            meds_run_out_date.strftime("%Y-%m-%d"), 
            fillable_date.strftime("%Y-%m-%d"),
            order_refill_date.strftime("%Y-%m-%d")
        )
    
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD.", None, None

def subtract_business_days(from_date, num_days):
    """Subtracts a given number of business days (Mon-Fri) from a given date."""
    days_subtracted = 0
    while days_subtracted < num_days:
        from_date -= timedelta(days=1)
        if from_date.weekday() < 5:  # Monday to Friday (0-4)
            days_subtracted += 1
    return from_date

if __name__ == "__main__":
    # User input
    meds_filled_date = input("Enter meds filled date (YYYY-MM-DD): ")
    meds_quantity = int(input("Enter meds quantity: "))
    days_prior_fill = int(input("Enter number of days prior it can be filled: "))

    # Calculate and display the results
    meds_run_out_date, fillable_date, order_refill_date = calculate_dates(
        meds_filled_date, meds_quantity, days_prior_fill
    )

    if fillable_date:
        print(f"Meds run out date: {meds_run_out_date}")
        print(f"Next fillable date: {fillable_date}")
        print(f"Order refill date (7 business days before run out): {order_refill_date}")
    else:
        print(meds_run_out_date)
