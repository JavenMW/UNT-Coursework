#prompting user for number to square root
user_number = int(input("Please enter a positive number: "))

#check to make sure number entered is positive
if user_number <= 0:
    while user_number <= 0:
        user_number = int(input("Your number must be positive. Please try again: "))
print("Thank you.")

#user number changed to original_estimate
#not necessary but the wording helped when creating my while loop
original_estimate = user_number

epsilon_check = abs((original_estimate/original_estimate-original_estimate))

#comparing estimate to episilon
if epsilon_check >= 0.0001:
    #calculating sqrt
    while epsilon_check >= 0.0001:
        new_estimate = ((original_estimate/epsilon_check+epsilon_check)/2)
        epsilon_check = abs(original_estimate/new_estimate-new_estimate)
#displaying sqrt
print("Square root of", user_number, end = '')
print(" is:", format(new_estimate, '.3f'))
