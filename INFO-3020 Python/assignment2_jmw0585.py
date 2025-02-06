print(" ") #new line

print("Welcome to the Compound Interest Calculator") #intro

print(" ") #new line

original_principle = float(input("Please enter the original principle: ")) #prompting user for the original principle// P
interest_rate = float(input("Please enter the interest rate (e.g., 5% as .05): ")) #prompting user for the interest interest_rate// R
num_years = float(input("Please enter the number of years to accrue interest: ")) #prompting user for the interest num_years// t
compound_per_year = float(input("Please enter the amount of compounds per year: ")) #prompting user for the interest compound_per_year// n
final_balance = (original_principle * (1+(interest_rate/compound_per_year)) ** (compound_per_year * num_years)) #formula to determine new account balance

print(" ") #new line

print("Original Investment: $", "{:,}".format(round(original_principle, 2))) #displays the amount of the original investment
print("Interest Earned: $", "{:,}".format(round(final_balance - original_principle, 2))) #displays the amount of the interest earned
print("Final Balance: $", "{:,}".format(round(final_balance, 2))) #displays the amount of the final balance

print(" ") #new line

input("Press ENTER to exit program.") #exits application
