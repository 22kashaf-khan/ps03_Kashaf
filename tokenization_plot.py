# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vjovkeG34T-GQyvPin3ALIbNXXdgb_CT
"""


#!pip install nltk
#!pip install transformers

import nltk
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt

nltk.download('punkt')

text = "The ancient city of Babylon, located in present-day Iraq, was one of the most influential centers of Mesopotamian civilization. Known for its impressive architectural achievements, the city was home to the famous Hanging Gardens, one of the Seven Wonders of the Ancient World. Babylon was also significant for the development of early laws, as evidenced by the Code of Hammurabi, one of the oldest deciphered writings of significant length in the world. The city’s rich cultural and scientific advancements influenced many aspects of later civilizations, including mathematics, astronomy, and literature."

tokens = word_tokenize(text)

print("List of tokens:", tokens)

num_tokens = len(tokens)
print("\nNumber of tokens:", num_tokens)

freq_dist = FreqDist(tokens)
print("\nFrequency of each token:")
for word, frequency in freq_dist.items():
    print(f"{word}: {frequency}")

print("\nPlotting the frequency distribution:")
plt.figure(figsize=(12, 6))
freq_dist.plot(30, title="Token Frequency Distribution")  # Plot the top 30 tokens
plt.show()

