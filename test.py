# Description: One Stop Insurance Company
# Author: Emily Warford
# Date: Mar. 24, 2024


# Imports:

import datetime
from datetime import timedelta, date
import FormatValues as FV


# Functions

   
def GreetingMessage():
   print("Welcome to One Stop Insurance Company invoice generator. Please enter requested information below.")


# Defaults:

f = open('Default.dat', 'r')

PolicyNumber = int(f.readline())
BasicPremium = float(f.readline())
CarsDiscount = float(f.readline())
LiabilityCost = float(f.readline())
GlassCost = float(f.readline())
LoanCost = float(f.readline())
TaxRate = float(f.readline())
ProcessingFee = float(f.readline())

f.close()


GreetingMessage()


# Inputs:

CustomerFirst = input("Please enter the customer first name: ").title()
CustomerLast = input("Please enter the customer last name: ").title()
StreetAddress = input("Please enter the customer street address: ")
City = input("Please enter the customer city: ").title()

ProvinceList = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "SK", "AB", "BC", "NT", "YT", "NV"]
while True:
    Province = input("Enter the customer province (XX): ")
    if Province not in ProvinceList:
        print("Data Entry Error - invalid province.")
    else:
        break

PostalCode = input("Please enter the customer postal code: ")
PhoneNumber = input("Please enter the customer preferred phone number: ")
NumberCars = input("Please number of cars being insured: ")
NumberCars = int(NumberCars)
ExtraLiability = input("Is extra liability required (Y/N)? ").upper()
GlassCoverage = input("Is glass coverage required (Y/N)? ").upper()
LoanCar = input("Is a loaner car required (Y/N)? ").upper()

PaymentList = ["Full", "Monthly", "Down Pay"]
while True:
    PaymentType = input("What payment type is preferred (Full, Monthly, or Down Pay)? ").title()
    if PaymentType not in PaymentList:
        print("Data Entry Error - invalid payment option")
        continue
    
    if PaymentType == "Down Pay":
        DownPayment = input("Please enter the down payment amount: ")
        DownPayment = float(DownPayment)
        break
    
    else:
        break

if PaymentType == "Full":
   DownPayment = 0

if PaymentType == "Monthly":
   DownPayment = 0

# Claims

while True:
    ClaimNumber = input("Please enter the claim number (Type 'END' to stop claim data input): ")
    if ClaimNumber == "END":
     break

    ClaimDate = input("Please enter the claim date: ")
    ClaimAmount = input("Please enter the claim amount: ")
    continue

ClaimOne = ["1", "2021-01-30", "10,000.00"]
ClaimTwo = ["2", "2022-02-28", "20,000.00"]
ClaimThree = ["3", "2023-03-26", "30,000.00"]

# Calculations

if NumberCars == 1:
 InsurancePremium = 869
else:
 InsurancePremium = 869 + ((NumberCars - 1) * (869 * 0.25))

if ExtraLiability == "Y":
    ExtraCost = 130 * NumberCars
else:
    ExtraCost = 0

if GlassCoverage == "Y":
    GlassCost = 86 * NumberCars
else:
    GlassCost = 0

if LoanCar == "Y":
    LoanCost = 58 * NumberCars
else: 
    LoanCost = 0

TotalExtra = ExtraCost + GlassCost + LoanCost

TotalPremium = InsurancePremium + TotalExtra

SalesTax = TaxRate * TotalPremium

TotalCost = SalesTax + TotalPremium
TotalCost = float(TotalCost)

MonthlyPayment = (float(39.99) + (TotalCost - DownPayment)) / 8

InvoiceDate = datetime.date.today()
PaymentDate = (InvoiceDate.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)


# Results

print(f"                                  ")
print(f"         1         2         3         4         5         6         7")
print(f"123456789012345678901234567890123456789012345678901234567890123456789012345678")
print(f"                                  ")
print(f"One Stop Insurance Company                   Invoice Date: {InvoiceDate}")
print(f"Invoice Information                          Policy No: {PolicyNumber}")
print(f"                                  ")
print(f"                                         ")
print(f"Customer Information:                                 ")
print(f"                                             ----------------------------------")
print(f"{CustomerFirst}. {CustomerLast}                        ")
print(f"{StreetAddress}                              Payment Type: {PaymentType}")
print(f"{City}, {Province} {PostalCode}              Number of Cars: {NumberCars}")
print(f"{PhoneNumber}")
print(f"                                             ----------------------------------")
print(f"Invoice Details:                             Insurance Premium: {FV.FDollar2(InsurancePremium)}")
print(f"                                             Extra Liability: {FV.FDollar2(ExtraCost)}")
print(f"                                             Glass Coverage: {FV.FDollar2(GlassCost)}")
print(f"                                             Loan Car Coverage: {FV.FDollar2(LoanCost)}")
print(f"                                             Total Extra Coverage: {FV.FDollar2(TotalExtra)}")
print(f"                                             Total Insurance Premium: {FV.FDollar2(TotalPremium)}")
print(f"                                             HST: {FV.FDollar2(SalesTax)}")
print(f"                                             Total Cost: {FV.FDollar2(TotalCost)}")
print(f"                                             ----------------------------------")
print(f"                                             Monthly Payment: {FV.FDollar2(MonthlyPayment)}")
print(f"                                             First Payment Date: {PaymentDate}")
print(f"-------------------------------------------------------------------------------")
print(f"                                  ")
print(f"Claim #   Claim Date   Amount")
print(f"----------------------------------")
print(f"{ClaimOne}")
print(f"{ClaimTwo}")
print(f"{ClaimThree}")
