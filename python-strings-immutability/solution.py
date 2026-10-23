def replace_char_at(s: str, index: int, ch: str) -> str:
    """
    Return a new string equal to `s` with the character at
    position `index` replaced by `ch`. `index` may be negative.
    `ch` may be any string, not necessarily one character long.

    If `index` is out of range (index >= len(s) or
    index < -len(s)), return `s` unchanged.
    Do not use the replace() method.

    Example: replace_char_at("hello", 0, "J") -> "Jello"
    """
    if(index >= len(s) or index < -len(s)):
        return s

    if(index < 0):
       index = len(s) + index
        
    new_string = s[:index]
    print(new_string)
    new_string += ch
    print(new_string)
    new_string += s[index+1:]
    print(new_string)
    
    return new_string

def insert_at(s: str, index: int, text: str) -> str:
    """
    Return a new string with `text` inserted before position
    `index`. Slice semantics apply: an `index` at or beyond
    len(s) appends, and a negative `index` counts from the end
    (clamped at the start of the string).

    Examples:
      insert_at("abc", 1, "X")   -> "aXbc"
      insert_at("abc", -1, "X")  -> "abXc"
      insert_at("abc", 99, "X")  -> "abcX"
    """
    if(index > 0):
        index = min(len(s),index)
    elif(index < 0):
        index = max(-len(s),index)

    print(index)

    new_s = s[:index]
    new_s += text
    new_s += s[index:]

    return new_s


def join_with_separator(parts, sep: str) -> str:
    """
    `parts` is a list of strings. Build and return one string
    containing every element of `parts`, with `sep` placed
    between consecutive elements (not before the first, not
    after the last). Use a for loop with + / += only. Do not
    use the join() method.

    An empty `parts` returns "".
    Example: join_with_separator(["a", "b", "c"], "-") -> "a-b-c"
    """

    new_s = ""
    for i in range(0,len(parts)):
        new_s += parts[i] + sep

    print(type(new_s))
    if(len(sep) >0):
        return new_s[:-1]
    else:
        return new_s

def repeat_text(s: str, n: int) -> str:
    """
    Return `s` repeated `n` times using the * operator.
    If n <= 0, return "".
    """
    return s*n


def total_chars_copied(n: int, piece_length: int) -> int:
    """
    Model of repeated concatenation. A string starts empty.
    For each of `n` steps, one piece of length `piece_length`
    is appended, and the step writes every character of the
    NEW string (previous content plus the piece).

    Return the total number of characters written across all
    n steps: piece_length * (1 + 2 + ... + n).
    If n <= 0, return 0.

    Example: total_chars_copied(3, 2) -> 2 + 4 + 6 = 12
    """
    if(n <= 0):
        return 0

    sum = 0
    for i in range(1,n+1):
        sum += i

    return sum*piece_length
