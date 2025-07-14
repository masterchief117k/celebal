import pandas as pd
import pandas as pd

# Load the dataset
df = pd.read_csv("data/Training Dataset.csv")


# Define a function to convert each row to a text chunk
def tabular_to_text(row):
    gender = row.get("Gender", "Unknown")
    education = row.get("Education", "Unknown")
    income = row.get("ApplicantIncome", "N/A")
    loan_amount = row.get("LoanAmount", "N/A")
    credit = row.get("Credit_History", "Unknown")
    status = row.get("Loan_Status", "Unknown")

    return (
        f"The applicant is a {gender} with {education} education, earning ₹{income}, "
        f"requesting ₹{loan_amount}. Credit history: {credit}. Loan status: {status}."
    )


# Apply the transformation to each row
text_chunks = [tabular_to_text(row) for _, row in df.iterrows()]

# (Optional) Save to a text file or JSON for embedding
with open("loan_chunks.txt", "w", encoding="utf-8") as file:
    for chunk in text_chunks:
        file.write(chunk + "\n")

print(f"{len(text_chunks)} text chunks generated and saved to 'loan_chunks.txt'.")

#print(data)
