import random
from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

nltk.download('loanbot')
app = Flask(__name__)
@app.route
    
class LoanSupportChatbot:
    def __init__(self):
        self.user_profile = { }

    def start_chat(self):
        print("Welcome to Smart Bank's Loan Support Chatbot!!!")
        print("How can I assist you ?")

        while True:
            user_input = input("You: ").strip( ).lower( )

            if user_input == "exit":
                print("Thank you for using Smart Bank's Loan Support Chatbot. Goodbye!")
                break

            response = self.generate_response(user_input)
            print("Chatbot:", response)

    def generate_response(self, user_input):
        if "eligibility" in user_input:
            return self.check_loan_eligibility()
        elif "loan products" in user_input:
            return self.provide_loan_products_info()
        elif "application process" in user_input:
            return self.guide_loan_application_process()
        elif "faq" in user_input:
            return self.answer_faq()
        elif "recommendations" in user_input:
            return self.offer_personalized_recommendations()
        else:
            return "I'm sorry, I didn't understand that. How can I assist you?"

    def check_loan_eligibility(self):
        return "To check your eligibility, please provide details such as credit score, income level, employment status, and existing debts."

    def provide_loan_products_info(self):
        return "We offer various loan products including Overdraft Facilities, Housing Loans, Education Loans, Pensioners' Loans, and Personal Loans. Which one would you like to know more about?"

    def guide_loan_application_process(self):
        return "To apply for a loan, you can visit our branch or apply online. I can guide you through the process. Please specify which loan you're interested in."

    def answer_faq(self):
       
        return "For FAQs and troubleshooting, please visit our website or contact our customer support."

    def offer_personalized_recommendations(self):
       
        return "To provide personalized recommendations, I would need more information about your financial situation. Can you provide details such as your income, expenses, and financial goals?"


class HousingLoanSupport:
    def __init__(self):
        pass

    def generate_response(self, user_input):
        if "housing loan scheme" in user_input:
           
            return self.provide_housing_loan_scheme_info()
        
        elif "housing loan for university staff" in user_input:

            return self.provide_housing_loan_for_university_staff_info()
        
        elif "housing loan scheme for the permanent cadre employees" in user_input:

            return self.provide_housing_loan_for_permanent_cadre_employees_info()
        
        elif "apply online" in user_input:

            return self.guide_housing_loan_application_online()
        else:
            return "I'm sorry, I didn't understand that. How can I assist you with housing loans?"

    def provide_housing_loan_scheme_info(self):
        
        info = """
 Smart Bank's Housing Loan Scheme offers various options:
        - Purchase a land to construct a house later
        - Purchase a land and to construct a house
        - Construct a house in a land owned by the borrower/s
        - Purchase a house/ partly constructed house/ condominium unit
        - Complete construction/ renovation/ extension/ repair of an existing house/ condominium unit
        - Landscaping/ interior decoration of the house/ condominium unit
        - Construction of houses/ apartments for sale
        
        Quantum of the Loan: Maximum of Rs. 50 Million
        Repayment Period: 25 years
        Area of Operation: All Island
        
        Eligibility:
        - Sri Lankan Citizen/s above the age of 18 years
        - Resident of Sri Lanka
        - Not a defaulter of Smart Bank or any other financial institution
        - Professionals with fixed/non-fixed income, permanent employees of government, statutory bodies, private sector, self-employed, farmers, and cultivators etc.
        - In case of a joint housing loan, the co-borrowers should be close relatives or directly interested parties for purchasing/developing of property
        
        For more information, please contact the Manager at your nearest Smart Branch or call centre: 1234
        """
        return info
    
class Loan:

    def __init__(self, loan_type):

        self.loan_type = loan_type
        self.features = None
        self.loan_amount = None
        self.repayment_period = None
        self.security = None
        self.purpose = None
        self.eligibility = None
        self.required_documents = None

class EducationalLoan(Loan):

    def __init__(self):

        super().__init__("Educational Loan")

        self.features = ["Smart Bank Educational Loans provide the financial support you need to achieve your higher educational goals at local or foreign universities.",
                         "Option of paying only the interest until the degree is complete.",
                         "Receive the maximum loan amount necessary for your requirements.",
                         "Speedy service.",
                         "No hidden costs."]
        
        self.loan_amount = "Maximum Rs. 10.0 Million (or 80% of the course fee which is less)"

        self.repayment_period = "Maximum of 7 years with 04 years Grace period"

        self.security = "Mortgage of property for facilities over Rs. 500,000/-"

        self.purpose = ["Registration Fees",
                        "Course Fees",
                        "Examination Fees",
                        "Payments for Travel Expenses can be considered for Foreign Universities"]
        
        self.eligibility = ["Smart Bank Customers and Students",
                            "Should have a minimum of 3 passes at G.C.E. (A/L) to follow degree courses",
                            "Should follow Post Graduate Examinations and Diplomas relevant to current employment",
                            "Should obtain the approval of the University Grant Commission of Sri Lanka for local/foreign educational institute, university and course"]
        
        self.required_documents = ["Loan Application",
                                   "Letter from University",
                                   "Proof of identification (NIC/Passport)"]

class LaptopLoan(Loan):

    def __init__(self):

        super().__init__("Laptop Loan")

        self.loan_amount = "Up to a maximum of Rs. 75,000/-"

        self.rate_of_interest = "0% (* Conditions apply. During NPA, customer should pay monthly AWPLR+0.5 subject to floor rate of 8.5%)"

        self.repayment_period = "Up to a maximum of 3 years"

        self.collateral = "A Personal Guarantee"

        self.eligibility = ["Only for students in National Universities",
                            "Joint loan with a parent/guardian"]
        
        self.required_documents = ["Duly completed Application",
                                   "Student Record Book and Student ID",
                                   "NIC of Student, Parent/Guardian and Guarantor",
                                   "Recommendation Letter by an Authorized Person of the University"]


educational_loan = EducationalLoan()

laptop_loan = LaptopLoan()

print("Educational Loan Information:")
print("Features:", educational_loan.features)
print("Loan Amount:", educational_loan.loan_amount)
print("Repayment Period:", educational_loan.repayment_period)
print("Security:", educational_loan.security)
print("Purpose:", educational_loan.purpose)
print("Eligibility:", educational_loan.eligibility)
print("Required Documents:", educational_loan.required_documents)

print("\nLaptop Loan Information:")
print("Loan Amount:", laptop_loan.loan_amount)
print("Rate of Interest:", laptop_loan.rate_of_interest)
print("Repayment Period:", laptop_loan.repayment_period)
print("Collateral:", laptop_loan.collateral)
print("Eligibility:", laptop_loan.eligibility)
print("Required Documents:", laptop_loan.required_documents)

class GovernmentPensionersLoan(Loan):

    def __init__(self):
        super().__init__("Government Pensioner's Loan Scheme")
        self.purpose = ["To Start a Business",
                        "Educational Expenses of their children",
                        "To meet Medical Expenses",
                        "House Repairs",
                        "Any Other Purpose legally acceptable (to uplift the lifestyle of the pensioners)"]
        self.eligibility = ["Government Pensioners below 75 years of age",
                            "Pension should be remitted to Smart Bank Account (Joint accounts will not be permitted.)"]
        self.loan_amount = "No upper limit (Monthly installment of the loan should be below 70% of gross pension)"
        self.repayment_period = "Maximum 15 years"
        self.security = ["Pension should be remitted to Smart Bank Account.",
                         "Decreasing Term Assurance Policy (DTA Policy)"]

government_pensioners_loan = GovernmentPensionersLoan()

print("Government Pensioner's Loan Scheme Information:")

print("Purpose:", government_pensioners_loan.purpose)

print("Eligibility:", government_pensioners_loan.eligibility)

print("Loan Amount:", government_pensioners_loan.loan_amount)

print("Repayment Period:", government_pensioners_loan.repayment_period)

print("Security:", government_pensioners_loan.security)
   
class PersonalLoan(Loan):

    def __init__(self):

        super().__init__("Smart Bank Personal Loan")

        self.features = ["Simplified documentation",
                         "Competitive rates",
                         "Transparency",
                         "Availability of Personal Loans for a variety of needs"]
        
        self.how_to_apply = ["Click on the Apply Online button (or Visit any Smart Bank Branch)",
                             "Complete the online Application",
                             "Once completed click on Submit button (please remember the reference number given)",
                             "You will receive an email or telephone call to visit the branch with required documents"]
        
        self.eligibility = ["In the age group of 18-55 (Applicants over 55 can be entertained, but only under special circumstances)",
                            "A salaried employee belonging to the following categories:",
                            "- Permanent employees of Government Service/ Statutory Bodies with a take home salary of LKR 30,000 or more",
                            "- Employees of Private sector entities as listed by the bank (Refer List) with a take home salary of LKR 40,000 or more"]
       
        self.required_documents = ["Loan Application",
                                   "Letter from Employer confirming service, position & salary",
                                   "Form No.375",
                                   "Proof of Identification (NIC/ Passport)"]

class LoansForProfessionals(Loan):

    def __init__(self):

        super().__init__("Loans for Professionals")

        self.eligible_sectors = ["Health Sector",
                                 "SLASA/SLEASA/SLPSA/GICTPA",
                                 "Engineers (IESL, IIESL)",
                                 "Tri Forces (Army, Navy, Airforce), Sri Lanka Police",
                                 "Government Employees",
                                 "Accountants",
                                 "Professional Qualified Persons (MAAT, ACA, FCA, ACMA, CGMA, ACCA)",
                                 "Employees of the office of the President/ Prime Minister",
                                 "Permanent Employees of the Institute of Bankers of Sri Lanka (IBSL)",
                                 "Employees of Sri Lanka Insurance Corporation (SLIC)",
                                 "Academic/Non-Academic Staff of Sri Lanka Institute of Information Technology (SLIIT)",
                                 "Customs",
                                 "Valuers",
                                 "Members of the Government Surveyors Association",
                                 "Members of the Association of the Government Scientific Officers (AGSO)",
                                 "Employees of Airport and Aviation Services"]
        
        self.required_documents = ["Loan Application",
                                   "Letter from Employer confirming service, position & salary",
                                   "Form No. 375 (Permanent employees only)",
                                   "DTA Policy",
                                   "Any other documents if required"]
        
        self.security = "One/ two guarantors in the same/higher grade to the borrower based on the loan scheme."

personal_loan = PersonalLoan()

loans_for_professionals = LoansForProfessionals()

print("Smart Bank Personal Loan Information:")
print("Features:", personal_loan.features)
print("How to Apply:", personal_loan.how_to_apply)
print("Eligibility:", personal_loan.eligibility)
print("Required Documents:", personal_loan.required_documents)

print("\nLoans for Professionals Information:")
print("Eligible Sectors:", loans_for_professionals.eligible_sectors)
print("Required Documents:", loans_for_professionals.required_documents)
print("Security:", loans_for_professionals.security)


if __name__ == "__main__":
    chatbot = LoanSupportChatbot()
    chatbot.start_chat()