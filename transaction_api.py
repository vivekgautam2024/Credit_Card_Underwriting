from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Full transaction data
transactions = [
    {"Date": "01-01-2025", "Description": "Opening Balance", "Deposit": 0, "Withdrawal": 0, "Balance": 5000},
    {"Date": "02-01-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7000},
    {"Date": "05-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6750},
    {"Date": "06-01-2025", "Description": "Online Purchase - Amazon Prime", "Deposit": 0, "Withdrawal": 20, "Balance": 6730},
    {"Date": "08-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 500, "Balance": 6230},
    {"Date": "10-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 6030},
    {"Date": "12-01-2025", "Description": "Transfer from Friend - John", "Deposit": 300, "Withdrawal": 0, "Balance": 6330},
    {"Date": "14-01-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 6315},
    {"Date": "15-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 6195},
    {"Date": "17-01-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 400, "Withdrawal": 0, "Balance": 6595},
    {"Date": "18-01-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 250, "Balance": 6345},
    {"Date": "20-01-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 6145},
    {"Date": "22-01-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 6015},
    {"Date": "25-01-2025", "Description": "Transfer to Savings", "Deposit": 0, "Withdrawal": 600, "Balance": 5415},
    {"Date": "28-01-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 5265},
    {"Date": "30-01-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 100, "Balance": 5165},
    {"Date": "01-02-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7165},
    {"Date": "03-02-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7145},
    {"Date": "04-02-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7245},
    {"Date": "05-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 300, "Balance": 6945},
    {"Date": "07-02-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 6445},
    {"Date": "10-02-2025", "Description": "Transfer from Friend - Lisa", "Deposit": 200, "Withdrawal": 0, "Balance": 6645},
    {"Date": "12-02-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 5945},
    {"Date": "13-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 5695},
    {"Date": "15-02-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 5565},
    {"Date": "18-02-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 500, "Withdrawal": 0, "Balance": 6065},
    {"Date": "20-02-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 5865},
    {"Date": "22-02-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 300, "Balance": 5565},
    {"Date": "25-02-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 5765},
    {"Date": "27-02-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 5415},
    {"Date": "01-03-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7415},
    {"Date": "03-03-2025", "Description": "Transfer from Friend - John", "Deposit": 100, "Withdrawal": 0, "Balance": 7515},
    {"Date": "05-03-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7495},
    {"Date": "07-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7345},
    {"Date": "08-03-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7445},
    {"Date": "10-03-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 7430},
    {"Date": "12-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7300},
    {"Date": "14-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 6800},
    {"Date": "17-03-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6550},
    {"Date": "18-03-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 6700},
    {"Date": "20-03-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 200, "Balance": 6500},
    {"Date": "22-03-2025", "Description": "Transfer from Friend - John", "Deposit": 250, "Withdrawal": 0, "Balance": 6750},
    {"Date": "25-03-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 350, "Balance": 6400},
    {"Date": "27-03-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 120, "Balance": 6280},
    {"Date": "30-03-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 5680},
    {"Date": "01-04-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7680},
    {"Date": "03-04-2025", "Description": "Online Purchase - Amazon Prime", "Deposit": 0, "Withdrawal": 20, "Balance": 7660},
    {"Date": "05-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7510},
    {"Date": "07-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 200, "Balance": 7310},
    {"Date": "10-04-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 200, "Withdrawal": 0, "Balance": 7510},
    {"Date": "12-04-2025", "Description": "Online Purchase - BestBuy", "Deposit": 0, "Withdrawal": 300, "Balance": 7210},
    {"Date": "14-04-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 7310},
    {"Date": "15-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7180},
    {"Date": "18-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 700, "Balance": 6480},
    {"Date": "20-04-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 250, "Balance": 6230},
    {"Date": "22-04-2025", "Description": "Online Purchase - eBay", "Deposit": 0, "Withdrawal": 100, "Balance": 6130},
    {"Date": "23-04-2025", "Description": "Transfer from Friend - Mike", "Deposit": 300, "Withdrawal": 0, "Balance": 6430},
    {"Date": "25-04-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 6250},
    {"Date": "27-04-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 125, "Balance": 6125},
    {"Date": "30-04-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5625},
    {"Date": "01-05-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7625},
    {"Date": "03-05-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 7125},
    {"Date": "05-05-2025", "Description": "Transfer from Friend - Paul", "Deposit": 200, "Withdrawal": 0, "Balance": 7325},
    {"Date": "07-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 7175},
    {"Date": "10-05-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7155},
    {"Date": "12-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 250, "Balance": 6905},
    {"Date": "14-05-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 250, "Withdrawal": 0, "Balance": 7155},
    {"Date": "15-05-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7025},
    {"Date": "18-05-2025", "Description": "Online Purchase - Netflix", "Deposit": 0, "Withdrawal": 15, "Balance": 7010},
    {"Date": "20-05-2025", "Description": "Transfer from Friend - Mike", "Deposit": 200, "Withdrawal": 0, "Balance": 7210},
    {"Date": "22-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 600, "Balance": 6610},
    {"Date": "25-05-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 220, "Balance": 6390},
    {"Date": "27-05-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 150, "Balance": 6240},
    {"Date": "30-05-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5740},
    {"Date": "01-06-2025", "Description": "Salary Deposit", "Deposit": 2000, "Withdrawal": 0, "Balance": 7740},
    {"Date": "03-06-2025", "Description": "Online Purchase - Spotify", "Deposit": 0, "Withdrawal": 20, "Balance": 7720},
    {"Date": "05-06-2025", "Description": "ATM Withdrawal", "Deposit": 0, "Withdrawal": 100, "Balance": 7620},
    {"Date": "07-06-2025", "Description": "Transfer from Friend - Mike", "Deposit": 100, "Withdrawal": 0, "Balance": 7720},
    {"Date": "10-06-2025", "Description": "Online Purchase - Apple Store", "Deposit": 0, "Withdrawal": 500, "Balance": 7220},
    {"Date": "12-06-2025", "Description": "Transfer from Friend - John", "Deposit": 200, "Withdrawal": 0, "Balance": 7420},
    {"Date": "15-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 180, "Balance": 7240},
    {"Date": "17-06-2025", "Description": "Utility Bill Payment", "Deposit": 0, "Withdrawal": 130, "Balance": 7110},
    {"Date": "18-06-2025", "Description": "Transfer from Friend - Sarah", "Deposit": 150, "Withdrawal": 0, "Balance": 7260},
    {"Date": "20-06-2025", "Description": "Online Purchase - Amazon", "Deposit": 0, "Withdrawal": 250, "Balance": 7010},
    {"Date": "22-06-2025", "Description": "Transfer from Friend - Anna", "Deposit": 100, "Withdrawal": 0, "Balance": 7110},
    {"Date": "25-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 1000, "Balance": 6110},
    {"Date": "27-06-2025", "Description": "Groceries", "Deposit": 0, "Withdrawal": 150, "Balance": 5960},
    {"Date": "30-06-2025", "Description": "Transfer to Savings Account", "Deposit": 0, "Withdrawal": 500, "Balance": 5460}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the Transaction API"}

@app.get("/transactions")
def get_transactions():
    return transactions

@app.get("/transactions/by-date/{date}")
def get_transaction_by_date(date: str):
    result = [t for t in transactions if t["Date"] == date]
    return result if result else {"message": "No transactions found on this date"}

@app.get("/transactions/search")
def search_transactions(description: Optional[str] = None):
    if description:
        result = [t for t in transactions if description.lower() in t["Description"].lower()]
        return result
    return transactions
