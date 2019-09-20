def vc_count(word):
    """
    ### Friendly tip: This function can't solve the problem, 
    ### you need more parameters to pass information between recursive functions.
    ### So, define another function!! Return the result from your new function!!
    
    :param word: String -- the input string
    :return: List[Int] -- the first integer is the number of vowels, 
                          the second integer is the number of consonants.
    """
    def count(s, res):
        if len(s) == 1:
            if s in 'aeiou':
                res[0] += 1
            res[1] += 1
            return res
        else:
            if s[0] in 'aeiou':
                res[0] += 1
            else:
                res[1] += 1
            return count(s[1:], res)  
    i = [0, 0]
    word.lower()
    res = count(word, i)
    return res

def main():
    print(vc_count("GoodMorningShanghai"))   # [7, 12]
    print(vc_count("WhatsUpGuys"))           # [3, 8]
    print(vc_count("EnjoyNationalHoliday"))  # [9, 11]
    print(vc_count("aaaaaaaaaaaaaaaAAAAA"))  # [20, 0]
    print(vc_count("hmmmmmmmmmmmmmmm"))      # [0, 16]

if __name__ == '__main__':
    main()
