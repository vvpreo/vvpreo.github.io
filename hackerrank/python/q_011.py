#! /usr/bin/python3
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]

    avg_score = sum(marks) / len(marks)
    avg_score = round(avg_score, 2)

    print(f'{avg_score:.2f}')
