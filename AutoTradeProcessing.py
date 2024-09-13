import pandas as pd

# Sample trade data
trade_data = {
    'Trade_ID': [101, 102, 103, 104],
    'Asset_Type': ['Bond', 'Equity', 'Bond', 'Equity'],
    'Trade_Amount': [10000, 15000, 20000, 12000],
    'Income_Payment': [500, 0, 700, 0],
    'Corporate_Action': ['None', 'Stock Split', 'None', 'Dividend']
}

# Convert trade data to DataFrame
df_trades = pd.DataFrame(trade_data)

def process_trades(df):
    """
    Process trade data, and calculate total income and corporate actions.
    """
    print("Processing Trade Data...")
    
    # Process income payments
    df['Processed_Income'] = df['Income_Payment'].apply(lambda x: x if x > 0 else 0)
    
    # Process corporate actions
    df['Processed_Corporate_Action'] = df['Corporate_Action'].apply(lambda x: 'Processed' if x != 'None' else 'None')

    # Total Trade Summary
    total_income = df['Processed_Income'].sum()
    print(f"Total Income Processed: ${total_income}")
    
    print(f"Processed Data:\n{df[['Trade_ID', 'Processed_Income', 'Processed_Corporate_Action']]}")

# Run the trade processing function
process_trades(df_trades)
