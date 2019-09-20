def pascal(n):
    """
    :param n: Int -- Levels of pascal triangle

    :return: List[List[Int]] -- a list of sublists, which contains pascal values.
    """
    def new(lst1):
        if len(lst1) == 1:
            return [1]
        mid = lst1[0] + lst1[1]
        return new(lst1[1 : ]) + [mid]
    if n == 1:
        return [[1]]
    new = new(pascal(n - 1)[-1]) + [1]
    return pascal(n - 1) + [new]
    
        

def main():
    print(pascal(4))    # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]

if __name__ == '__main__':
    main()




