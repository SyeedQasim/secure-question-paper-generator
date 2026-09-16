import random
from questions import questions

TARGET_MARKS = 10


def generate_paper(question_bank, target_marks):
    shuffled = question_bank.copy()
    random.shuffle(shuffled)

    def find_combination(start, selected, current_marks):
        if current_marks == target_marks:
            return selected

        if current_marks > target_marks:
            return None

        for i in range(start, len(shuffled)):
            question = shuffled[i]

            result = find_combination(
                i + 1,
                selected + [question],
                current_marks + question["marks"]
            )

            if result is not None:
                return result

        return None

    return find_combination(0, [], 0)


paper = generate_paper(questions, TARGET_MARKS)

if paper is None:
    print("No paper with exactly", TARGET_MARKS, "marks can be created.")
else:
    print("QUESTION PAPER")
    print("================")

    total_marks = 0

    for number, q in enumerate(paper, 1):
        print(f"Q{number}. {q['question']} [{q['marks']} marks]")
        total_marks += q["marks"]

    print("================")
    print("Total Marks:", total_marks)
