def append_all(lst: list, items: list) -> None:
    """
    Add every element of `items` to the end of `lst`, in place,
    so that each element becomes its own new element of `lst`.
    Use extend(). Return nothing.
    """
    # print(lst)
    # print(items)
    # for item in items:
    #     lst.append(item)
    # print(lst)
    # print()

    # print(lst)
    lst.extend(items)
    # print(lst)


def insert_sorted(lst: list, value) -> None:
    """
    `lst` is sorted in ascending order. Insert `value` in place
    so that the list stays sorted, placing it AFTER any existing
    elements equal to `value`. Use a loop to find the position
    and insert() to add it. Return nothing.

    Example: lst = [1, 3, 3, 5]; insert_sorted(lst, 3)
             -> lst is now [1, 3, 3, 3, 5]
    """
    # print(lst)
    target = len(lst)
    for i in range(0,len(lst)):
        if(lst[i] > value):
            target = i
            break

    # print(target)
    lst.append(0)
    for i in range(len(lst) - 1, target, -1):
        lst[i] = lst[i-1]

    # print(lst)
    lst[target] = value
    # print(lst)


def flatten_one_level(list_of_lists: list) -> list:
    """
    Return a NEW list made of the elements of each inner list,
    in order. Do not change `list_of_lists` or its inner lists.
    Use extend() on a fresh list.

    Example: flatten_one_level([[1, 2], [], [3]]) -> [1, 2, 3]
    """
    new_list = []

    for list in list_of_lists:
        for element in list:
            new_list.append(element)

    return new_list


def concat_identity_report(lst: list, extra: list) -> list:
    """
    Using the list `lst` given by the caller:
      1. Record id(lst). Perform `lst += extra`. Record whether
         id(lst) is unchanged (call this same_after_iadd).
      2. Record id(lst) again. Perform `lst = lst + extra`.
         Record whether id(lst) is unchanged (same_after_plus).
    Return a list [same_after_iadd, same_after_plus].
    (The caller's original list is changed by step 1 only.)
    """
    # print(lst)
    # print(extra)

    id_old = id(lst)
    lst += extra

    id_plus = id(lst)

    same_1 = (id_plus == id_old) 

    lst = lst + extra

    same_2 = (id(lst) == id_plus)

    return [same_1, same_2]


def remove_all(lst: list, value) -> None:
    """
    Remove EVERY element equal to `value` from `lst`, in place
    (the caller's list object must keep its id()). Consecutive
    duplicates must all be removed. Return nothing.

    Example: lst = [1, 1, 2, 1]; remove_all(lst, 1)
             -> lst is now [2]
    """
    # print(lst)   

    keep = [x for x in lst if x != value]

    lst[:] = keep

def pop_last_n(lst: list, n: int) -> list:
    """
    Remove the last `n` elements of `lst` in place and return
    them in their ORIGINAL order as a new list. If n <= 0,
    remove nothing and return []. If n >= len(lst), remove
    everything.

    Example: lst = [1, 2, 3, 4]; pop_last_n(lst, 2) -> [3, 4]
             and lst is now [1, 2]
    """
    if(n <= 0):
        return []
    if (n > len(lst)):
        n = len(lst)
        
    removed = lst[-n:]
    del lst[-n:]
    return removed


def delete_every_other(lst: list) -> None:
    """
    Remove the elements at positions 0, 2, 4, ... from `lst`,
    in place, using del with an extended slice. Return nothing.

    Example: lst = [1, 2, 3, 4, 5] -> lst is now [2, 4]
    """
    del lst[::2]


def remove_first_or_report(lst: list, value) -> bool:
    """
    If `value` is in `lst`, remove its first occurrence in place
    and return True. If it is not present, leave `lst` unchanged
    and return False. Check with `in` before removing; do not
    let remove() fail.
    """
    if(value in lst):
        lst.remove(value)
        return True
    return False
