#######################################################################################################################################################
# 
# Name: Le, Thi Thu Huong
# SID: 740095180
# Exam Date: 28 Mar 2025
# Module: Programming for Business Analytics
# Github link for this assignment: https://github.com/UniversityExeterBusinessSchool/mock-test-2-tl686
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]
average_sales = sum(weekly_sales) / len(weekly_sales)
print ("The average sales is:",average_sales)
for i in weekly_sales:
    if i < average_sales:
        print (f"Week's sales {i} was below the average sales")
    elif i > average_sales:
        print (f"Week's sales {i} was above the average sales")
    else:
        continue
#OUT PUT:
# Week's sales 120 was above the average sales
# Week's sales 85 was below the average sales
# Week's sales 100 was below the average sales
# Week's sales 90 was below the average sales
# Week's sales 110 was above the average sales
# Week's sales 95 was below the average sales
# Week's sales 130 was above the average sales
# The average sales is: 104.28571428571429
#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""
start_1 = customer_feedback.find('good')
end_1 = start_1 + len ('good')
start_2 = customer_feedback.find('improved')
end_2 = start_2 + len ('improved')
position = [(start_1, end_1),(start_2, end_2)]
print ("Position of the words 'good' and 'improved' in the customer feedback is:",position)
#OUT PUT: Position of the words 'good' and 'improved' in the customer feedback is: [(16, 20), (34, 42)]
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.
def NPM (net_profit, revenue):
    return (net_profit / revenue) * 100
def CAC (total_marketing_cost, new_customers_acquired):
    return (total_marketing_cost / new_customers_acquired)
def NPC (promoters, detractors, total_respondents):
    return (promoters - detractors) / total_respondents * 100
def ROI (net_gain_from_investment, investment_cost):
    return (net_gain_from_investment / investment_cost) * 100
print ("Net Profit Margin:", NPM (7400,95180))
print ("Customer Acquisition Cost:", CAC (7400,95180))
print ("Net Promoter Score:", NPC (7400,95180,740095180))
print ("Return on Investment:", ROI (7400,95180))
#OUT PUT:
# Net Profit Margin: 7.774742592981719
# Customer Acquisition Cost: 0.07774742592981719
# Net Promoter Score: -0.011860636627845624
# Return on Investment: 7.774742592981719
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}

#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130

#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.

#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.

#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}

#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
#print("The average is" + average)

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

#######################################################################################################################################################
