from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


def create_excel_file() -> Workbook:
    """Creates a new Excel file and returns a Workbook object.

    Returns:
        Workbook: A new Workbook object.
    """
    return Workbook()


def write_headers(sheet) -> None:
    """Writes headers to the Excel sheet.

    Args:
        sheet (Worksheet): The worksheet to write headers to.
    """
    sheet['A1'] = 'Employee ID'
    sheet['B1'] = 'Name'
    sheet.column_dimensions['A'].auto_size = True
    sheet.column_dimensions['B'].auto_size = True


def write_employees_data(sheet, employees: list) -> None:
    """Writes employee data to the Excel sheet.

    Args:
        sheet (Worksheet): The worksheet to write employee data to.
        employees (list): A list of dictionaries, each representing an employee.
    """
    for i, employee in enumerate(employees, start=2):
        sheet[f'A{i}'] = employee['employee_id']
        sheet[f'B{i}'] = employee['name']


def write_employees_to_excel(employees_data: list, file_path: str) -> None:
    """Writes employee data to an Excel file.

    Args:
        file_path (str): The path to the Excel file to write to.
        employees_data (list): A list of dictionaries, each representing
        an employee.
    """
    wb = create_excel_file()
    sheet = wb.active
    write_headers(sheet)
    write_employees_data(sheet, employees_data)
    wb.save(file_path)
    print(
        f'Employee data has been successfully written to an Excel file:'
        f'\n{file_path}'
    )
