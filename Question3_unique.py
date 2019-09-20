def unique(s):
    """
    :param s: List[Any] -- list of values.
    :return: True if all values within s are unique.
             False otherwise.
    """
    if len(s) == 1:
        return True
    test = s[0]
    if test not in s[1:]:
        return unique(s[1:])
    return False

def main():
    print(unique([1,7,6,5,4,3,1]))   # False
    print(unique([9,4,3,2,1,8]))     # True
    print(unique(['9',[],4,3,2,1,8]))     # True

if __name__ == '__main__':
    main()

