def word_count(text: str) -> int:
    """
    Return the number of words in `text`, where words are
    separated by any run of whitespace. Leading and trailing
    whitespace does not create extra words.
    """
    text = text.strip()

    if(len(text) <= 0):
        return 0

    print(text.split())
    return len(text.split())


def reverse_word_order(text: str) -> str:
    """
    Split `text` on whitespace, reverse the order of the words
    (a list can be sliced with [::-1] like a string), and
    return them joined by single spaces.

    Example: reverse_word_order("  one  two three ") -> "three two one"
    """
    text = text.strip()

    if(len(text) <= 0):
        return 0

    text_list = text.split()

    print(text_list)

    new_list = []
    for i in range(len(text_list) - 1, -1, -1):
        word = text_list[i]
        new_list.append(word)

    print(new_list)

    rev_string = " ".join(new_list)

    return rev_string


def last_field(line: str, sep: str) -> str:
    """
    Return the text after the LAST occurrence of `sep` in
    `line`. If `sep` does not occur, return `line` unchanged.
    Use rsplit() with a maxsplit of 1 and the index -1.

    Example: last_field("a/b/c.txt", "/") -> "c.txt"
    """
    text = line.rsplit(sep,1)[-1]

    print(line.rsplit(sep,1))
    print(line.rsplit(sep))
    
    return text


def count_nonblank_lines(text: str) -> int:
    """
    Return how many lines in `text` (as split by splitlines())
    contain at least one character that is not whitespace.
    """
    lines = text.splitlines()

    count_lines = 0

    for i,line in enumerate(lines):
        print(line)
        has_char = 0
        for char in line:
            if(char != " "):
                count_lines += 1
                break

    return count_lines


def make_csv_line(fields) -> str:
    """
    `fields` is a list of strings. Return one string in which
    the fields are joined by ",". Any field that contains a
    comma is first wrapped in double quotes.

    Example: make_csv_line(["a", "b,c", "d"]) -> 'a,"b,c",d'
    """
    print(fields)

    field_list = []
    for field in fields:
        str = ""
        if("," in field):
            str = " "
            str += field
            str += " "
        else:
            str = field
            
        field_list.append(str)

    ans_string = ",".join(field_list)

    quote = '"'

    return ans_string.replace(" ", quote)
