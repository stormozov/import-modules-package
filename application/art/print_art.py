import art


def print_art(text: str, font: str = 'standard') -> None:
    """Print ASCII art of the given text using the specified font.

    Args:
        text (str): The text to be converted to ASCII art.
        font (str, optional): The font to use for the ASCII art.
        Defaults to 'standard'.

    Returns:
        None

    Raises:
        ValueError: If the font is not a valid font name.

    Note:
        The available fonts are:
        - standard
        - script
        - serifcap
        - block
        - bubble
        - digital
        - script
        - serifsym
        - slant
        - smblock
        - smmono9
        - smmono12
        - smscript
        - smserif9
        - smserif12
        - unicode
        - usaflag
    """
    result_art = art.text2art(text, font)
    print(result_art)
