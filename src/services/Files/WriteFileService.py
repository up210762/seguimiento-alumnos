from src.services.Subject.getSubjects import get_groups
from src.services.Score.getResultService import get_results

import csv

subjects = get_groups()

def write_results(filename, dataStudents: list):
    with open(f'src/output-files/{filename}', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        
        header = ['GRUPO', 'GRUPO NUEVO', 'Matrícula', 'Nombre']
        for subject in subjects:
            header.append(subject[0])
            
        writer.writerow(header)
        
        actual_student = ''
        files = None
        
        for data in dataStudents:
            if actual_student != data[1]:
                if actual_student == "":
                    files = [data[0], "", data[1], data[2]]
                    files.append(data[4])
                    actual_student = data[1]
                else:
                    writer.writerow(files)
                    files = [data[0], "", data[1], data[2]]
                    files.append(data[4])
                    actual_student = data[1]
            else:
                files.append(data[4])
        
def write_file_service(filename):
    try:
        data_students = get_results()
        write_results(filename, data_students)
    except Exception as ex:
        return 500