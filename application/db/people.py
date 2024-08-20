def get_employee(employee_id: int) -> dict:
    """Retrieves a single employee by ID.

    Args:
        employee_id (int): The ID of the employee to retrieve.

    Returns:
        dict: A dictionary containing the employee's ID and name.
    """
    return {'employee_id': employee_id, 'name': 'John Doe'}


def get_employees() -> list[dict]:
    """Retrieves a list of employee dictionaries containing employee_id and name

    Returns:
        list: A list of dictionaries, each representing an employee.
    """
    return [
        {'employee_id': 1, 'name': 'John Doe'},
        {'employee_id': 2, 'name': 'Jane Doe'},
    ]


def get_employees_or_employee(employee_id: int = None) -> dict | list[dict]:
    """Retrieves either a list of all employees or a single employee by ID.

    If employee_id is provided, returns a dictionary representing the employee.
    Otherwise, returns a list of dictionaries, each representing an employee.

    Args:
        employee_id (int, optional): The ID of the employee to retrieve.
        Defaults to None.

    Returns:
        dict or list: A dictionary representing a single employee or a list of
        employee dictionaries.
    """
    return (
        get_employee(employee_id)
        if employee_id is not None
        else get_employees()
    )


def format_employees(employees: dict | list) -> str:
    """
    Format the employees data into a string.

    Args:
        employees (dict or list): The employees data returned by
        get_employees_or_employee.

    Returns:
        str: The formatted employees data.
    """
    if isinstance(employees, dict):
        return (f"Employee ID: {employees['employee_id']}, "
                f"Name: {employees['name']}")
    elif isinstance(employees, list):
        formatted_employees = [
            f"Employee ID: {employee['employee_id']}, Name: {employee['name']}"
            for employee in employees
        ]
        return "\n".join(formatted_employees)
    else:
        raise ValueError("Invalid employees data")
