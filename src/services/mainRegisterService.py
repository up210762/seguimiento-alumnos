## Main of program where make the important logical

# Charge the necesary dependencies
from src.models.ModelStudent import Student
from src.models.ModelScore import Score
from src.models.ModelGroup import Group
from src.models.ModelSubject import Subject
from src.services.Students.registerStudentService import register_student
from src.services.Subject.registerSubjectService import register_subject
from src.services.Results.registerScoreService import register_score
from src.services.Groups.registerGroupService import register_group
from src.services.Groups.textCleanerGroupsService import clean_text
from src.services.Results.getResultService import get_tries
from src.utils.Logger import Logger
from dotenv import load_dotenv
import os, csv, traceback, time

# Charge the values of file .env
load_dotenv()

# Charge the path for save the files
UPLOAD_FOLDER = os.getenv('ROOT_PATH')

# Define the variable type array
reader_students = []
reader_subjects = []
reader_score = []
reader_group = []
relation_subject_group = []

# Function to register the students and qualifications that was recibe from csv file
def register_service(filename, date: str):
    try:
        # Se abre un contexto global para manejar el archivo CSV
        with open(f'{UPLOAD_FOLDER}/{filename}', newline='') as csvfile:
            counter = 0
            reader = csv.reader(csvfile)

            # Se realiza una primera iteración para llenar las tablas de registro que no necesitan de datos externos.
            for row in reader:
                if counter == 0:
                    counter=+1
                    pass
                else:
                    group = Group(clean_text(row[0]))
                    student = Student(row[5], row[6])
                    subject = Subject(row[1])

                    reader_students.append((student.enrollment, student.name))
                    reader_subjects.append((subject.subject))
                    reader_group.append((group.group))

            # Se realizan los registros
            register_student(reader_students)
            register_subject(reader_subjects)
            register_group(reader_group)

            # Se reinicia el contador del contexto global para permitir una segunda iteración
            csvfile.seek(0)
            counter = 0

            # Se realiza una segunda iteración para llenar las tablas de registro que dependen de datos externos.
            for row in reader:
                if row[1]:
                    if counter == 0:
                        counter=+1
                        pass
                    else:
                        if int(row[8])>=7:
                            status = 1
                        else:
                            status = 2
                        score = Score(row[5], row[1], clean_text(row[0]), row[8])
                        tries: int = get_tries([row[5], row[1]])
                        tries += 1
                        subject_id:int = score.search_subject()
                        if subject_id == None:
                            return "Hay un dato incorrecto"
                        group_id = score.search_group()
                        reader_score.append((score.enrollment, subject_id, group_id, score.score, tries, date, status))
                        time.sleep(0.01)
                else:
                    return "Asegurate que el archivo CSV esté separado por comas o tenga el formato correcto.", 409
            # Se realizan los registros
            res = register_score(reader_score)

            # Se devuelve como respuesta las filas afectadas
            return res, 200
        
    except Exception as ex:
        Logger.add_to_log('Error:', traceback.format_exc())

        return {
            'message': f"Error: {ex}",
            'success': False
        }, 500