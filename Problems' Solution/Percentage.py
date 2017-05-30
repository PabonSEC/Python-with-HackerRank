if __name__ == '__main__':

    student_marks = {}

    n = int(input())

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query = input()

    li = student_marks[query]

    avg = 0.0

    for i in li:
        avg += i

    print(format(avg/3, '.2f'))
