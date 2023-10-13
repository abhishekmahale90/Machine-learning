#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Define the prior probabilities P(sunny) and P(rainy)
P_sunny = 0.7  # Example value
P_rainy = 0.3  # Example value

# Define the conditional probabilities P(word|category)
P_word_given_sunny = {
    'a': 0.4,  # Example values for each word
    'cone': 0.6,
    'of': 0.8,
    'ice': 0.3,
    'cream': 0.7
}

P_word_given_rainy = {
    'a': 0.5,  # Example values for each word
    'cup': 0.7,
    'of': 0.6,
    'hot': 0.4,
    'coffee': 0.8
}

# Define the input statements
statement_sunny = "a cone of ice cream"
statement_rainy = "a cup of hot coffee"

# Tokenize the input statements
words_sunny = statement_sunny.split()
words_rainy = statement_rainy.split()

# Initialize the probabilities
P_sunny_given_statement = P_sunny
P_rainy_given_statement = P_rainy

# Calculate the conditional probabilities for each word
for word in words_sunny:
    P_sunny_given_statement *= P_word_given_sunny.get(word, 1e-6)  # Use a small value for unknown words
    P_rainy_given_statement *= P_word_given_rainy.get(word, 1e-6)

# Normalize the probabilities
total_probability = P_sunny_given_statement + P_rainy_given_statement
P_sunny_given_statement /= total_probability
P_rainy_given_statement /= total_probability

# Output the results
print("P(sunny|a cone of ice cream) =", P_sunny_given_statement)
print("P(rainy|a cup of hot coffee) =", P_rainy_given_statement)


# In[ ]:




