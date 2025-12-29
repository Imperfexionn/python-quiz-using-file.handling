# Basically a quiz thingy.
# Quiz data; add/modify questions/answers here.
quiz = [
    {"question": "What is 5 + 5?", "answer": "10"},
    {"question": "What is 12 + 3?", "answer": "15"},
    {"question": "What is 5 x 2?", "answer": "10"}
       ]
total_questions = len(quiz)
correct=0
# Clear previous scores.
score_file = open("scores.txt", "w")
score_file.write("")
score_file.close()

# Start quiz.
score_file = open("scores.txt", "a")  # open in append mode

for x in range(len(quiz)):
    q = quiz[x]
    user_answer=input(q["question"] + "\n").strip()
    if user_answer == q["answer"]:
        score_file.write(f"Question {x+1} was correct!\n")
        correct+=1
    else:
        score_file.write(f"Question {x + 1} was incorrect!\n")
score_file.close()

# Display results
score_file = open("scores.txt", "r")
result = score_file.read()
print("\nYour Results:")
print(result)
if correct <=1 and correct > 0:
    print(f"You got {correct} question correct out of {total_questions}!")
else:
    print(f"You got {correct} questions correct out of {total_questions}!")
score_file.close()

