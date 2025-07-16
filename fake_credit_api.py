from fastapi import FastAPI
from typing import List
from datetime import date

app = FastAPI(title="Fake Credit Detail API")

# Sample credit data (20 entries)
credit_data = [
    {
        "creditId": f"CRD{str(i).zfill(4)}",
        "customerName": name,
        "creditScore": score,
        "loanAmount": amount,
        "loanType": loan,
        "status": status,
        "issueDate": issue,
        "dueDate": due,
        "bankName": bank,
        "interestRate": rate
    }
    for i, (name, score, amount, loan, status, issue, due, bank, rate) in enumerate([
        ("Ravi Kumar", 720, 500000, "Home Loan", "Approved", "2023-01-10", "2033-01-10", "Bank of India", 7.5),
        ("Sneha Mehta", 680, 300000, "Car Loan", "Pending", "2024-05-20", "2029-05-20", "HDFC Bank", 9.0),
        ("Amit Sharma", 800, 200000, "Personal Loan", "Approved", "2022-07-15", "2027-07-15", "Axis Bank", 10.5),
        ("Neha Verma", 750, 450000, "Education Loan", "Approved", "2021-06-01", "2026-06-01", "SBI", 8.2),
        ("Raj Malhotra", 630, 150000, "Credit Card", "Rejected", "2024-02-11", "2029-02-11", "ICICI Bank", 12.0),
        ("Pooja Singh", 710, 600000, "Home Loan", "Approved", "2023-03-22", "2033-03-22", "PNB", 7.0),
        ("Ankit Jain", 670, 350000, "Car Loan", "Pending", "2023-11-05", "2028-11-05", "HDFC Bank", 9.5),
        ("Rakesh Yadav", 780, 800000, "Home Loan", "Approved", "2020-08-10", "2030-08-10", "SBI", 6.9),
        ("Priya Sharma", 745, 250000, "Personal Loan", "Approved", "2024-01-01", "2029-01-01", "Axis Bank", 10.0),
        ("Nikhil Rathi", 655, 120000, "Credit Card", "Rejected", "2022-10-10", "2027-10-10", "ICICI Bank", 11.5),
        ("Meena Gupta", 695, 400000, "Car Loan", "Approved", "2021-12-20", "2026-12-20", "Kotak Bank", 9.0),
        ("Vikas Dubey", 610, 100000, "Personal Loan", "Pending", "2023-05-01", "2028-05-01", "IDFC Bank", 13.0),
        ("Anjali Rai", 730, 550000, "Home Loan", "Approved", "2022-03-12", "2032-03-12", "SBI", 7.3),
        ("Suresh Kumar", 760, 150000, "Credit Card", "Approved", "2021-01-10", "2026-01-10", "Axis Bank", 12.5),
        ("Rina Das", 690, 300000, "Education Loan", "Pending", "2023-06-14", "2028-06-14", "Bank of Baroda", 8.8),
        ("Harish Rawat", 725, 700000, "Home Loan", "Approved", "2020-09-30", "2030-09-30", "Canara Bank", 6.5),
        ("Payal Mehra", 665, 250000, "Personal Loan", "Pending", "2022-02-22", "2027-02-22", "ICICI Bank", 10.9),
        ("Nitin Chauhan", 785, 800000, "Home Loan", "Approved", "2024-01-15", "2034-01-15", "HDFC Bank", 6.7),
        ("Sonal Jain", 700, 180000, "Car Loan", "Approved", "2023-04-18", "2028-04-18", "SBI", 9.1),
        ("Rohit Aggarwal", 640, 160000, "Credit Card", "Rejected", "2021-05-05", "2026-05-05", "Axis Bank", 11.2)
    ])
]

@app.get("/api/credit-details", summary="Get all credit details")
def get_credit_details():
    return credit_data
