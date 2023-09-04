'''
Affirm an individual or group honor code by replacing <name> or <names>.
`
For individual submissions: I, <name>, have neither given or recived inappropriate help with this homework assignment.

For group submissions: We, Charlene, Sanna, Leo, Dustin, have neither given or recived inappropriate help with this homework assignment. All group members participated in this work, and all concur with this submission.
'''


def L4(inString):
    # For lab #4, add code that  computes the counts of non-negative
    # ints equal to 0, 1 and 2 mod 3, and returns 'yes' if the 3
    # counts are the same; otherwise, L4 returns 'no'.
    #     
    numbers = inString.split()
    counts = {0: 0, 1: 0, 2: 0}

    for number in numbers:
        num = int(number)
        if num >= 0:
            remainder = num % 3
            counts[remainder] += 1

    if all(count == counts[0] for count in counts.values()):
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':

    def test_case(F,string,expected,num,comment=''):
        err = '** '
        result = F(string)
        func_name = str(F).split()[1]
        func_call = f'''{func_name}("{string}")'''
        if result == expected: err = ''
        e = expected
        print (f'{err}test #{num} {func_call}: expected "{e}", received "{result}"')
        print (f'test #{num} Explanation: {comment}\n')
        return num + 1

    num = 1

    s = '1 5 9 -2'
    exp = '#(%3 = 0) = #(%3 = 1) = #(%3 = 2) = 1, -2 ignored' 
    num = test_case(L4,s,'yes',num,exp)
    
    s = ' -2'
    exp = '#(%3 = 0) = #(%3 = 1) = #(%3 = 2) = 0, -2 ignored' 
    num = test_case(L4,s,'yes',num,exp)    

    s = '  -5 0 '
    exp = '#(%3 = 0) = 1, but #(%3 = 1) = #(%3 = 2) = 1, -5 ignored' 
    num = test_case(L4,s,'no',num,exp)    

    s = '1 5 9 11 -2'
    exp = '#(%3 = 0) = #(%3 = 1) = 1, but #(%3 = 2) = 2' 
    num = test_case(L4,s,'no',num,exp)

    
