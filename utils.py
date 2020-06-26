"""
Utility functions for ThotBank.
"""


def latinize_coptic(text):
    """
    Latinize Coptic characters in a text.

    This function is needed as a workaround for `unidecode` failing on most
    Coptic characters. In can be used in conjunction with `unidecode` itself.

    Note that the mapping is not inteded as a perfect phonological
    transcription, but as a way of obtaining strict-ASCII keys. Note, as
    well, that the mapping is case sensitive.

    Parameters
    ----------
    text : str
        The string to be mapped. Non-Coptic characters are left untouched.

    Returns
    -------
    latin : str
        Latinized version of the string.
    """

    # Build the mapping dictionary. If we ever create an inverse function,
    # such as for accepting data from the internet, it is better to
    # manually invert the dictionary than to create some complex global
    # variable holding the correspondence.
    mapper = {
        "ⲁ": "a",
        "ⲃ": "b",
        "ⲅ": "g",
        "ⲇ": "d",
        "ⲉ": "e",
        "ⲋ": "5",
        "ⲍ": "z",
        "ⲏ": "E",
        "ⲑ": "T",
        "ⲓ": "i",
        "ⲕ": "k",
        "ⲗ": "l",
        "ⲙ": "m",
        "ⲛ": "n",
        "ⲝ": "X",
        "ⲟ": "o",
        "ⲡ": "p",
        "ⲣ": "r",
        "ⲥ": "s",
        "ⲧ": "t",
        "ⲩ": "u",
        "ⲫ": "F",
        "ⲭ": "X",
        "ⲯ": "P",
        "ⲱ": "O",
        "ϣ": "S",
        "ϥ": "f",
        "ϧ": "H",
        "ϩ": "h",
        "ϫ": "j",
        "ϭ": "q",
        "ϯ": "7",
        "ⲵ": "3",
        "ⲹ": "K",
        "ⳉ": "2",
        "ⳋ": "9",
    }

    for source, target in mapper.items():
        text = text.replace(source, target)

    return text
