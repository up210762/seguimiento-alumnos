from src.services.Results.writeResults import write_results
from src.services.Results.getResultService import get_results


def write_file_service():
    try:
        data_students = get_results()
        write_results(data_students)
    except Exception as ex:
        return ex