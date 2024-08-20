def calculate_annual_salary(salary: float, bonus: float = 1.1) -> float:
    """Calculate the annual salary based on the given monthly salary and bonus.

    Args:
        salary (float): The monthly salary.
        bonus (float, optional): The bonus factor. Defaults to 1.1.

    Returns:
        float: The annual salary.

    Example:
        >>> calculate_annual_salary(5_000)
        60000.0
        >>> calculate_annual_salary(5_000, 1.2)
        72000.0
    """
    annual_salary = salary * 12 * bonus
    return annual_salary
