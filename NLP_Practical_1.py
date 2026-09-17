import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

text = "Breaking Bad is the highest-rated television series."

print("Original Text:")
print(text)

tokens = word_tokenize(text)

print("\nTokens:")
print(tokens)

stop_words = set(stopwords.words("english"))
filtered_words = [word for word in tokens if word.lower() not in stop_words]

print("\nAfter Stop-word Removal:")
print(filtered_words)

stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print("\nStemmed Words:")
print(stemmed_words)

lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]

print("\nLemmatized Words:")
print(lemmatized_words)

pos_tags = pos_tag(filtered_words)

print("\nPOS Tags:")
print(pos_tags)