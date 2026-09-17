import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

df = pd.read_csv(r"C:\Users\PRAJWAL\Downloads\archive (10)\movie_data.csv")
text = df["review"].iloc[0]

print("ORIGINAL TEXT:")
print(text)

# Sentence segmentation
sentences = sent_tokenize(text)
print("\nSENTENCES:")
print(sentences)

# Normalization
normalized = re.sub(r"[^a-zA-Z\s]", "", text).lower()

# Tokenization
tokens = word_tokenize(normalized)
print("\nTOKENS:")
print(tokens)

# Stopword removal
stop_words = set(stopwords.words("english"))
filtered = [word for word in tokens if word not in stop_words]
print("\nAFTER STOPWORD REMOVAL:")
print(filtered)

# Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]
print("\nSTEMMED:")
print(stemmed)

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized = [lemmatizer.lemmatize(word) for word in filtered]
print("\nLEMMATIZED:")
print(lemmatized)

# OOV detection
vocabulary = set()
for review in df["review"].head(1000):
    words = word_tokenize(re.sub(r"[^a-zA-Z\s]", "", review).lower())
    vocabulary.update(words)

oov = [word for word in tokens if word not in vocabulary]
print("\nOOV WORDS:")
print(oov)

# Unknown token replacement
oov_handled = [word if word in vocabulary else "<UNK>" for word in tokens]
print("\nOOV HANDLED:")
print(oov_handled)

# Final text
final_text = " ".join(lemmatized)

print("\nFINAL TEXT:")
print(final_text)

# Comparison
print("\nOriginal Word Count:", len(word_tokenize(text)))
print("Processed Word Count:", len(lemmatized))
print("OOV Word Count:", len(oov))