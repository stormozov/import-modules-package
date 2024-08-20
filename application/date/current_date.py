def get_current_date(date_format: str = '%Y-%m-%d') -> str:
    """Get the current date in the format 'YYYY-MM-DD'.

    Returns:
        str: The current date in the format 'YYYY-MM-DD'.

    Example:
        >>> get_current_date()
        '2022-01-01'
    """
    from datetime import datetime
    return datetime.now().strftime(date_format)
