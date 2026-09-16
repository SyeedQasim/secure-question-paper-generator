import random
from questions import questions

random.shuffle(questions)

paper = []
total_marks = 0

for q in questions:

    if total_marks + q["marks"] <= 10:
        paper.append(q)
        total_marks += q["marks"]

    if total_marks == 10:
        break

print("QUESTION PAPER")
print("================")

for number, q in enumerate(paper, 1):
    print(f"Q{number}. {q['question']} [{q['marks']} marks]")

print("================")
print("Total Marks:", total_marks)
