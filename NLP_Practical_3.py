def edit_distance(word1, word2):

    rows = len(word1) + 1
    cols = len(word2) + 1

    dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        dp[i][0] = i

    for j in range(cols):
        dp[0][j] = j

    for i in range(1, rows):
        for j in range(1, cols):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[rows - 1][cols - 1]


dictionary = {
    "apple": 50,
    "banana": 40,
    "computer": 80,
    "college": 70,
    "student": 90,
    "machine": 60,
    "learning": 75,
    "python": 85,
    "science": 65,
    "language": 55
}


def correct_word(misspelled):

    best_word = None
    best_score = float("-inf")

    for word, frequency in dictionary.items():

        distance = edit_distance(misspelled, word)
        score = frequency / (distance + 1)

        if score > best_score:
            best_score = score
            best_word = word

    return best_word


word = input("Enter Misspelled Word: ")

print("\n------ EDIT DISTANCE ------")

for correct in dictionary:
    distance = edit_distance(word, correct)
    print(word, "->", correct, ":", distance)


correction = correct_word(word)

print("\n------ SPELLING CORRECTION ------")
print("Misspelled Word :", word)
print("Suggested Word  :", correction)


dataset = [
    ("aple", "apple"),
    ("bananna", "banana"),
    ("computr", "computer"),
    ("colleg", "college"),
    ("studnt", "student"),
    ("machin", "machine"),
    ("learnng", "learning"),
    ("pythn", "python"),
    ("scince", "science"),
    ("langage", "language")
]

correct_predictions = 0

print("\n------ DATASET EVALUATION ------")

for misspelled, actual in dataset:

    predicted = correct_word(misspelled)

    print(
        misspelled,
        "-> Predicted:",
        predicted,
        "| Actual:",
        actual
    )

    if predicted == actual:
        correct_predictions += 1


accuracy = (correct_predictions / len(dataset)) * 100

print("\nCorrect Predictions :", correct_predictions)
print("Total Words         :", len(dataset))
print("Accuracy            :", accuracy,
