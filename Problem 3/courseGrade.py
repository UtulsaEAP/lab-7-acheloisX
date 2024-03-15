def compute_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'      

def compute_average(scores):
    return sum(scores)/len(scores)

filename = input("Enter the tsv filename: ")
students = []
with open(filename, 'r') as f:
    for line in f:
        fields = line.strip().split('\t')
        last_name, first_name, midterm1, midterm2, final = fields
        midterm1 = int(midterm1)
        midterm2 = int(midterm2)
        final = int(final)
        students.append((last_name, first_name, midterm1, midterm2, final))

with open('report.txt', 'w') as f:
    for student in students:
        last_name, first_name, midterm1, midterm2, final = student
        avg_score = compute_average([midterm1, midterm2, final])
        letter_grade = compute_grade(avg_score)
        f.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")

exams = {'midterm1': [], 'midterm2': [], 'final': []}
for student in students:
    exams['midterm1'].append(student[2])
    exams['midterm2'].append(student[3])
    exams['final'].append(student[4])

f.write(f"\nAverages: midterm1 {avg1:.2f}, midterm2 {avg2:.2f}, final {avg3:.2f}")
