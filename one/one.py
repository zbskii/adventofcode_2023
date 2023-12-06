import sys

def sum_first_and_last_numbers(s):
    first = None
    last = None
    
    for i in range(len(s)):
        if s[i].isdigit():
            if first is None:
                first = s[i];
            else:
                last = s[i]
        enumber = has_english_number(s, i)
        if enumber:
            nume = convert_english_number_to_int(enumber)
            if first is None:
                first = nume
                print("enum first: %s" % nume)
                
            else:
                last = nume
                print("enum last: %s" % nume)
            i+=len(enumber)
            
            
    if first is None:
        raise Exception("No first number found on line %s" % s)
    if last is None:
        last = first

    print("first %s, last %s" % (first, last))
    return "%s%s" % (first, last)

def has_english_number(s, i):
    english_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for number in english_numbers:
        if s[i:].startswith(number):
            return number
    return None

def convert_english_number_to_int(word):
    number_dict = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    return number_dict.get(word.lower(), None)



def main():

    s = open(sys.argv[1]).readlines()
    sum = 0
    for l in s:
        print("current line: %s" % l)
        linesum = (sum_first_and_last_numbers(l))
        print("linesum: %s" % linesum)
        sum += int(linesum)
    print(sum)
    return 0



if __name__ == "__main__":
    exit(main())