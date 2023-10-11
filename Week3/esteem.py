

""""

1. I feel that I am a person of worth, at least on an equal plane with others.
2. I feel that I have a number of good qualities.
3. All in all, I am inclined to feel that I am a failure.
4. I am able to do things as well as most other people.
5. I feel I do not have much to be proud of.
6. I take a positive attitude toward myself.
7. On the whole, I am satisfied with myself.
8. I wish I could have more respect for myself.
9. I certainly feel useless at times.
10. At times I think I am no good at all.

The person responds to each statement by choosing one of these four options: strongly disagree, disagree, agree, or strongly agree. The person’s response to each statement is worth 0–3 points, meaning the highest possible score is 10 * 3 = 30 points. If a person scores lower than 15 points, the person may have a problematic low self-esteem.

Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:

Choice	Points
Strongly Disagree	0
Disagree	1
Agree	2
Strongly Agree	3
The other five statements (numbers 3, 5, 8, 9, 10) are negative and are scored like this:

Choice	Points
Strongly Disagree	3
Disagree	2
Agree	1
Strongly Agree	0


"""

print("\nThis program is an implementation of the Rosenberg Self-Esteem Scale.")
print("This program will show you ten statements that you could possibly apply to yourself.")
print("\nPlease rate how much you agree with each of the")
print("statements by responding with one of these four letters:")

print("\nD means you strongly disagree with the statement.")
print("d means you disagree with the statement.")
print("a means you agree with the statement.")
print("A means you strongly agree with the statement.\n")


questions = [
    "I feel that I am a person of worth, at least on an equal plane with others.",
    "I feel that I have a number of good qualities.",
    "All in all, I am inclined to feel that I am a failure.",
    "I am able to do things as well as most other people.",
    "I feel I do not have much to be proud of.",
    "I take a positive attitude toward myself.",
    "On the whole, I am satisfied with myself.",
    "I wish I could have more respect for myself.",
    "I certainly feel useless at times.",
    "At times I think I am no good at all."]


def main():
    # for i, question in enumerate(questions):
    #     i+=1
    #     answer = input(f"{i}. {question}: (D/d/A/a): ")

    #score = 0

    answer1 = input(f" 1. {questions[0]} :  ")
    score += give_score_positive(answer1)

    answer2 = input(f" 2. {questions[1]} :  ")
    score += give_score_positive(answer2)

    answer3 = input(f" 3. {questions[2]} :  ")
    score += give_score_negative(answer3)

    answer4 = input(f" 4. {questions[3]} :  ")
    score += give_score_positive(answer4)

    answer5 = input(f" 5. {questions[4]} :  ")
    score += give_score_negative(answer5)

    answer6 = input(f" 6. {questions[5]} :  ")
    score += give_score_positive(answer6)

    answer7 = input(f" 7. {questions[6]} :  ")
    score += give_score_positive(answer7)

    answer8 = input(f" 8. {questions[7]} :  ")
    score += give_score_negative(answer8)

    answer9 = input(f" 9. {questions[8]} :  ")
    score += give_score_negative(answer9)

    answer10 = input(f" 10. {questions[9]} :  ")
    score += give_score_negative(answer10)

    print(f"\nTotal score: {score}. A score below 15 may indicate problematic low self-esteem.\n")


# Function for Scoring Positive Statements (numbers 1, 2, 4, 6, 7)
def give_score_positive(answer):
    if answer == "D":
        score = 0
    elif answer == "d":
        score = 1
    elif answer == "a":
        score = 2
    elif answer == "A":
        score = 3
    return score


# Function for Scoring Negative Statements (numbers 3, 5, 8, 9, 10)
def give_score_negative(answer):
    if answer == "D":
        score = 3
    elif answer == "d":
        score = 2
    elif answer == "a":
        score = 1
    elif answer == "A":
        score = 0
    return score


main()
