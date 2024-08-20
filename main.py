from application.art.print_art import print_art
from application.date.current_date import get_current_date
from application.db.people import format_employees, get_employees_or_employee
from application.excel_writer.writer import write_employees_to_excel
from application.fs_tools.absolute_path import get_absolute_path
from application.salary import calculate_annual_salary


if __name__ == '__main__':
    # Printing current date
    print(f'Current date: {get_current_date()}', end='\n\n')

    # Calculating annual salary and printing it
    print(
        f'Your current annual salary is {calculate_annual_salary(60_000.0)}',
        end='\n\n'
    )

    # Formatting employees data
    employees = get_employees_or_employee()
    formatted_employees = format_employees(employees)
    print(formatted_employees, end='\n\n')

    # Using ART library to print ASCII art
    print_art('STORMOZOV')

    # Writing employees data to Excel using openpyxl library
    excel_file_path = get_absolute_path(['employees.xlsx'])
    write_employees_to_excel(employees, excel_file_path)
