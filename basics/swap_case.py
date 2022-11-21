def swap_case(s):
    t = ""
    for i in range(len(s)):
        if s[i].islower():
            t += s[i].upper()
        else:
            t += s[i].lower()
    return t
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)