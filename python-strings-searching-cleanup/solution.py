def sentence_case(s: str) -> str:
    """
    Return `s` with its first character uppercase and every
    other character lowercase.
    Example: sentence_case("hELLO wORLD") -> "Hello world"
    """

    if(len(s) <= 0):
        return ""
    new_s = s[0].upper()
    
    for char in s[1:]:
        new_s += char.lower()

    return new_s


def swap_first_char_case(s: str) -> str:
    """
    Return `s` with ONLY its first character's case swapped;
    the rest of the string is unchanged. An empty string
    returns "". Use slicing together with swapcase().
    Example: swap_first_char_case("python") -> "Python"
             swap_first_char_case("PYthon") -> "pYthon"
    """
    if(len(s) <= 0):
        return ""
        
    new_s = s[0].swapcase()
    new_s += s[1:]

    return new_s

def equal_ignoring_case(a: str, b: str) -> bool:
    """
    Return True if `a` and `b` are the same text when case is
    ignored. Use casefold() on both sides.
    Example: equal_ignoring_case("Straße", "STRASSE") -> True
    """
    a = a.casefold()
    b = b.casefold()

    print(a,b)

    return (a == b)


def case_kind(s: str) -> str:
    """
    Classify `s` using isupper(), islower(), and istitle(),
    checked in this order. Return exactly one of:
      "upper", "lower", "title", "mixed"
    Return "mixed" if none of the three tests is True
    (including for the empty string).
    """
    if(s.isupper()):
        return "upper"
    elif(s.islower()):
        return "lower"
    elif(s.istitle()):
        return "title"
    else:
        return "mixed"


def find_all(s: str, sub: str):
    """
    Return a list of the starting indices of every occurrence
    of `sub` in `s`, in increasing order, INCLUDING overlapping
    occurrences. Use find() with a moving start position.
    If `sub` is empty, return an empty list.

    Example: find_all("aaaa", "aa") -> [0, 1, 2]
    """
    ans_list = []
    
    if(len(sub) <= 0):
        return ans_list
        
    i = 0
    while(i + len(sub) - 1 < len(s)):
        index = s.find(sub,i,i+len(sub))
        if(index >= 0):
            ans_list.append(index)
        i += 1

    return ans_list

def count_overlapping(s: str, sub: str) -> int:
    """
    Return the number of occurrences of `sub` in `s`, counting
    overlapping occurrences. If `sub` is empty, return 0.
    Example: count_overlapping("aaaa", "aa") -> 3
             (the built-in count() would give 2)
    """
    if(len(sub) <= 0):
        return 0
        
    i = 0
    count = 0
    while(i + len(sub) - 1 < len(s)):
        index = s.find(sub,i,i+len(sub))
        if(index >= 0):
            count += 1
        i += 1

    return count


def has_extension(filename: str, ext: str) -> bool:
    """
    Return True if `filename` ends with a dot followed by `ext`,
    ignoring case. `ext` is given WITHOUT the dot.
    Example: has_extension("Report.PDF", "pdf") -> True
             has_extension("pdf", "pdf")        -> False
    """
    filename = filename.casefold()
    ext = '.' + ext

    return filename.endswith(ext)


def classify_token(token: str) -> str:
    """
    Return exactly one of the following, checked in this order:
      "digits"  if every character is a digit
      "letters" if every character is a letter
      "alnum"   if every character is a letter or digit
      "space"   if every character is whitespace
      "other"   otherwise (including the empty string)
    """
    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ"

    count_letters = 0
    count_dights = 0
    count_spaces = 0

    if(len(token) == 0):
        return "other"

    for char in token:
        if(char in digits):
            count_dights += 1
        elif(char in letters):
            count_letters += 1
        elif(char == " "):
            count_spaces += 1

    if(count_dights == len(token)):
        return "digits"
    elif(count_letters == len(token)):
        return "letters"
    elif(count_dights + count_letters == len(token)):
        return "alnum"
    elif(count_spaces == len(token)):
        return "space"
    else:
        return "other"

def remove_leading(s:str, char:str):
    """
    remove leading occurences of char from s
    """

    if(len(s) == 0):
        return ""
    
    index = 0
    while(index < len(s) and (s[index] in char) ):
        index += 1
        
    new_s = s[index:]

    return new_s

def remove_trailing(s:str, char:str):
    """
    remove trailing occurences of char from s
    """

    if(len(s) == 0):
        return ""
        
    index = len(s) - 1
    while(index >= 0 and (s[index] in char)):
        index -= 1
        
    new_s = s[:index+1]

    return new_s


def clean_field(s: str) -> str:
    """
    Return `s` with, in this order:
      1. leading and trailing whitespace removed,
      2. any trailing characters from the set ".,;" removed,
      3. leading and trailing whitespace removed again.

    Example: clean_field("  total ; ")  -> "total"
             clean_field("  a b.. ")    -> "a b"
    """

    if(len(s) == 0):
        return ""

    s = remove_leading(s," ")
    s = remove_trailing(s, " ")

    pun_set = ".,;"

    s = remove_trailing(s,pun_set)

    s = remove_leading(s," ")
    s = remove_trailing(s, " ")

    return s

    

def remove_prefix_once(s: str, prefix: str) -> str:
    """
    If `s` begins with `prefix`, return `s` with that prefix
    removed exactly ONCE. Otherwise return `s` unchanged.
    Do not use lstrip(): it removes a set of characters, not a
    prefix.

    Example: remove_prefix_once("ababab", "ab") -> "abab"
    """

    len1 = len(s)
    len2 = len(prefix)
    
    if(len1 <= 0 ):
        return ""

    if(prefix not in s or len2 <= 0):
        return s

    if(s[:len2] == prefix):
        return s[len2:]

    


def replace_first_n(s: str, old: str, new: str, n: int) -> str:
    """
    Return `s` with the first `n` occurrences of `old` replaced
    by `new`. If n == 0, return `s` unchanged. If n < 0,
    replace every occurrence.
    """
    if(n == 0):
        return s
    if(len(s) <= 0):
        return ""

    s = s.replace(old, new, n)
    return s
