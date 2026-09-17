import nltk
import math
from collections import Counter
from nltk.corpus import brown

nltk.download('brown')

sentences = [[word.lower() for word in sentence] for sentence in brown.sents()]

split = int(0.8 * len(sentences))
train_sentences = sentences[:split]
test_sentences = sentences[split:]

START = "<s>"
END = "</s>"

train_data = [[START] + sentence + [END] for sentence in train_sentences]
test_data = [[START] + sentence + [END] for sentence in test_sentences]

vocabulary = set(word for sentence in train_data for word in sentence)
V = len(vocabulary)

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()

for sentence in train_data:
    for word in sentence:
        unigram_counts[word] += 1
    for i in range(len(sentence) - 1):
        bigram_counts[(sentence[i], sentence[i + 1])] += 1
    for i in range(len(sentence) - 2):
        trigram_counts[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1

total_words = sum(unigram_counts.values())

def unigram_mle(word):
    return unigram_counts[word] / total_words

def bigram_mle(w1, w2):
    if unigram_counts[w1] == 0:
        return 0
    return bigram_counts[(w1, w2)] / unigram_counts[w1]

def trigram_mle(w1, w2, w3):
    if bigram_counts[(w1, w2)] == 0:
        return 0
    return trigram_counts[(w1, w2, w3)] / bigram_counts[(w1, w2)]

def unigram_laplace(word):
    return (unigram_counts[word] + 1) / (total_words + V)

def bigram_laplace(w1, w2):
    return (bigram_counts[(w1, w2)] + 1) / (unigram_counts[w1] + V)

def trigram_laplace(w1, w2, w3):
    return (trigram_counts[(w1, w2, w3)] + 1) / (bigram_counts[(w1, w2)] + V)

def unigram_perplexity(data, smoothing=False):
    log_probability = 0
    N = 0
    for sentence in data:
        for word in sentence:
            probability = unigram_laplace(word) if smoothing else unigram_mle(word)
            if probability == 0:
                return float("inf")
            log_probability += math.log(probability)
            N += 1
    return math.exp(-log_probability / N)

def bigram_perplexity(data, smoothing=False):
    log_probability = 0
    N = 0
    for sentence in data:
        for i in range(len(sentence) - 1):
            w1, w2 = sentence[i], sentence[i + 1]
            probability = bigram_laplace(w1, w2) if smoothing else bigram_mle(w1, w2)
            if probability == 0:
                return float("inf")
            log_probability += math.log(probability)
            N += 1
    return math.exp(-log_probability / N)

def trigram_perplexity(data, smoothing=False):
    log_probability = 0
    N = 0
    for sentence in data:
        for i in range(len(sentence) - 2):
            w1, w2, w3 = sentence[i], sentence[i + 1], sentence[i + 2]
            probability = trigram_laplace(w1, w2, w3) if smoothing else trigram_mle(w1, w2, w3)
            if probability == 0:
                return float("inf")
            log_probability += math.log(probability)
            N += 1
    return math.exp(-log_probability / N)

uni_mle_pp = unigram_perplexity(test_data)
bi_mle_pp = bigram_perplexity(test_data)
tri_mle_pp = trigram_perplexity(test_data)

uni_laplace_pp = unigram_perplexity(test_data, True)
bi_laplace_pp = bigram_perplexity(test_data, True)
tri_laplace_pp = trigram_perplexity(test_data, True)

print("Total Sentences:", len(sentences))
print("Training Sentences:", len(train_sentences))
print("Testing Sentences:", len(test_sentences))
print("Vocabulary Size:", V)

print("\nPERPLEXITY WITHOUT SMOOTHING")
print("Unigram:", uni_mle_pp)
print("Bigram:", bi_mle_pp)
print("Trigram:", tri_mle_pp)

print("\nPERPLEXITY WITH LAPLACE SMOOTHING")
print("Unigram:", uni_laplace_pp)
print("Bigram:", bi_laplace_pp)
print("Trigram:", tri_laplace_pp)

print("\nCOMPARISON")
print("Model\t\tMLE\t\tLaplace")
print("Unigram\t\t", uni_mle_pp, "\t", uni_laplace_pp)
print("Bigram\t\t", bi_mle_pp, "\t", bi_laplace_pp)
print("Trigram\t\t", tri_mle_pp, "\t", tri_laplace_pp)

print("\nEXAMPLE PROBABILITIES")

print("\nUnigram:")
print("P(the) MLE:", unigram_mle("the"))
print("P(the) Laplace:", unigram_laplace("the"))

print("\nBigram:")
print("P(the | in) MLE:", bigram_mle("in", "the"))
print("P(the | in) Laplace:", bigram_laplace("in", "the"))

print("\nTrigram:")
print("P(house | in,the) MLE:", trigram_mle("in", "the", "house"))
print("P(house | in,the) Laplace:", trigram_laplace("in", "the", "house"))