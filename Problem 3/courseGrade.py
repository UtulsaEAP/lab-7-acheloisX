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

def courseGrade():
    while True:
        try:
            file_name = input("Enter  tsv: ").strip()
            if file_name.lower() == 'quit':
                break
            
            midterm1_total = 0
            midterm2_total = 0
            final_total = 0
            student_count = 0

            with open(file_name, 'r') as file:
                lines = file.readlines()

            output_file_name = f'report_{file_name.split(".")[0]}.txt'

            with open(output_file_name, 'w') as report_file:
                for line in lines:
                    parts = line.split('\t')
                    last_name, first_name, midterm1, midterm2, final = parts
                    midterm1 = int(midterm1)
                    midterm2 = int(midterm2)
                    final = int(final)
                    
                    average_score = (midterm1 + midterm2 + final) / 3
                    
                    letter_grade = compute_grade(average_score)
                    
                    report_file.write(f'{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n')
                    
                    midterm1_total += midterm1
                    midterm2_total += midterm2
                    final_total += final
                    student_count += 1

           
            midterm1_avg = midterm1_total / student_count
            midterm2_avg = midterm2_total / student_count
            final_avg = final_total / student_count

            with open(output_file_name, 'a') as report_file:
                report_file.write(f'\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}')

            print(f'Report file "{output_file_name}" has been generated successfully.\n')
        
        except FileNotFoundError:
            print(f'Error: File "{file_name}" not found.\n')
        except Exception as e:
            print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    courseGrade()