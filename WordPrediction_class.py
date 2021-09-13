'''
Program: Follow-along Lab - Week 2 Day 2

Date: July 15th, 2020
Authors: Keval Israni, Muskan Israni
Student ID: 017834282, 017537908
class: CECS 451- Artificial Intelligence
'''

from hashlib import new
import random
import string

target = list("Keval")


def generate_random_solutions(length=len(target)):
    # sytax description: [for-body for-statement] is a one line for loop
    return [random.choice(string.printable) for _ in range(length)]


def evaluate(solution):
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff


def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)


best = generate_random_solutions()
best_score = evaluate(best)

iterations = 0

while True:
    iterations += 1

    print(iterations, " iterations so far",
          best_score, "Solution", "".join(best))

    if(best_score == 0):
        break

    new_solution = list(best)
    mutate_solution(new_solution)
    score = evaluate(new_solution)

    if (score < best_score):
        best = new_solution
        best_score = score

# print(diff, best)
