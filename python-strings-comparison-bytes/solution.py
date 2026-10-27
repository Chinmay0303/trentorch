def compare_strings(a: str, b: str) -> int:
    """
    Compare `a` and `b` lexicographically by code point, WITHOUT
    using the <, >, or == operators on the whole strings. Use a
    loop over positions with ord() on individual characters.

    Return -1 if a < b, 0 if a == b, 1 if a > b.
    A string that is a proper prefix of another is smaller.
    """
    for char_a,char_b in zip(a,b):
    # print(f"a: {char_a}, ord: {ord(char_a)}, b: {char_b}, ord: {ord(char_b)}")
        if(ord(char_a) > ord(char_b)):
            return 1
        elif(ord(char_a) < ord(char_b)):
            return -1

    if(len(a) > len(b)):
        return 1
    elif(len(a) < len(b)):
        return -1
        
    return 0


def compare_ignoring_case(a: str, b: str) -> int:
    """
    Same return convention as compare_strings, but the strings
    are compared after applying casefold() to both. You may use
    the built-in comparison operators here.
    """
    a = a.casefold()
    b = b.casefold()

    return compare_strings(a,b)


def caesar_shift(s: str, k: int) -> str:
    """
    Shift every ASCII letter in `s` forward by `k` positions in
    the alphabet, wrapping from "z" to "a" (and "Z" to "A").
    Case is preserved. Characters that are not ASCII letters are
    left unchanged. `k` may be negative or larger than 26.
    Use ord(), chr(), and %.

    Example: caesar_shift("Abc, xyz!", 3) -> "Def, abc!"
    """
    # print(ord("a"), ord("z"), ord("A"), ord("Z"))

    new_s = ""
    for char in s:
        val = ord(char)
        # print(char, val)
        if(val >= 65 and val <= 90):
            val += k%26
            if(val > 90):
                val = val - 26
            elif(val < 65):
                val = val + 26
        
        elif(val >= 97 and val <= 122):
            val += k%26
            if(val > 122):
                val = val - 26
            elif(val < 97):
                val = val + 26
            
        new_char = chr(val)
        # print(new_char, val)
        new_s += new_char
        
    return new_s


def utf8_byte_length(s: str) -> int:
    """
    Return the number of bytes needed to store `s` in UTF-8.
    Example: utf8_byte_length("café") -> 5
    """
    print(len(s))

    return len(s.encode("utf-8"))


def roundtrip(s: str, encoding: str) -> str:
    """
    Encode `s` using `encoding`, then decode the resulting bytes
    using the same encoding, and return the decoded text. Use
    errors="replace" when encoding so characters the encoding
    cannot represent do not cause an error.
    Example: roundtrip("naïve", "utf-8") -> "naïve"
    """
    enc_s = s.encode(encoding,errors = "replace")

    print(encoding, enc_s)

    dec_s = enc_s.decode(encoding)

    return dec_s


def is_ascii_only(s: str) -> bool:
    """
    Return True if every character of `s` is ASCII. Do this by
    comparing len(s) with the length of the UTF-8 encoded bytes;
    do not loop over characters.
    """
    if(len(s) == len(s.encode("utf-8"))):
        return True
    else:
        return False


def first_byte_values(s: str, count: int):
    """
    Return a list of the integer values of the first `count`
    bytes of `s` encoded in UTF-8 (fewer if the encoded data is
    shorter than `count`).
    Example: first_byte_values("Aé", 3) -> [65, 195, 169]
    """
    return list(s.encode("utf-8"))[:count]
