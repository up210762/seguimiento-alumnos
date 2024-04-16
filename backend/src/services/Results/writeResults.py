from src.services.Subject.getSubjects import get_groups
import csv

subjects = get_groups()

def write_results(dataStudents: list):
    with open('src/files/Seguimiento Alumnos.csv', 'w', newline='') as file:
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
        
            