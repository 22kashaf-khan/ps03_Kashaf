# ps03_Kashaf
Overview
This Python script performs tokenization of a given text, counts the number of tokens, calculates the frequency of each token, and plots the frequency distribution. It is particularly useful for understanding how often words appear in a body of text, which can be applied to various NLP projects.

Requirements
Python 3.x
NLTK library
Matplotlib library
Installation
Ensure that nltk and matplotlib are installed. Run the following commands if necessary:

bash
Copy code
pip install nltk matplotlib
Steps in the Code
Installation Check: The code includes an optional line to install NLTK if running in a local environment.
Import Libraries: It imports word_tokenize from nltk.tokenize, FreqDist from nltk.probability, and matplotlib.pyplot for plotting.
Download NLTK Data: The nltk.download('punkt') line ensures that the necessary tokenizer models are downloaded.
Create the Text: The variable text contains a sample paragraph for processing.
Tokenization: The word_tokenize() function splits the paragraph into individual tokens (words and punctuation).
Print Tokens: The script prints the list of tokens.
Token Count: The code calculates and prints the total number of tokens.
Frequency Distribution: The FreqDist object is used to count the frequency of each token.
Plot the Distribution: The script uses the plot() method from FreqDist to display a plot of token frequency.
Usage
Copy the code into a Python file, e.g., tokenization_plot.py.
Run the script in an environment with Python installed.
View the console output for the token list and count.
A plot showing the frequency distribution of the top 30 tokens will appear.
Example Output
A list of tokens is printed to the console.
The number of tokens in the text is displayed.
A frequency plot is shown, visualizing the most common tokens.
