# Note: 
#   Please save this as diagnostic_firstname.txt
#       (replace firstname w/ yours)
#   Do not edit lines that say: "# Last line in ____"
###############################################################################
# Imports  # there will only be one import added here.

import os

###############################################################################
# Write f01 that prints "Hello World!" and calls f02. (three lines)
def f01():
    print("Hello World!")
    f02()
###############################################################################
# Write f02 that sets the variables x, y, and z equal to the words 
# necessary to have the f03 print "i love python!" (five lines)
def f02():
    x = 'i'
    y = 'love'
    z = 'python'
    f03(x,y,z)  # Last line in f2()
###############################################################################
# Finish f03 (replace the ????). 
def f03(*words):
    truth = " ".join(words)  # This is broken.
    truth_emphasized = truth + "!"
    print truth_emphasized
    f04(truth)  # Last line in f03()
###############################################################################
# Write f04 that prints truth backwards (edit one line only)
# Ex. f4("Littlest Bear") prints "raeB tselttiL"
def f04(string):
    print string[::-1]
    f05(string)  # Last line in f04()
###############################################################################
# Write f05 that for each char in a word passed as a parameter, prints that 
# word on a new line, and for each consecutive print, prints it indented by one
# more char. (possibly a few lines)
# Ex. f05("Info")
# Info
#  Info
#   Info
#    Info
def f05(word):
    for i, char in enumerate(word):
        print (' '*i) + word
    f06("South Hall", "Python Rocks!")  # Last line in f05()
###############################################################################
# Write f06 that takes two strings:
# (1) prints: "'string' is longer than 'string' by x chars"
#   replace string and string w/ the actual strings, replace x w/ proper value
# (2) prints: "'string' has only xx.xx% the number of chars of 'string'"
#   replace string and string w/ the actual strings
#   replace xx.xx w/ proper value
# (several lines)
# Ex. f06("short_string", "longer_string")
# 'longer_string' is longer than 'short_string' by 1 chars
# 'short_string' has only 92.31% the number of chars of longer_string
def f06(string1, string2):
    #Step 1
    string_list = sorted([string1, string2], key = len)
    chars_diff = abs(len(string1)-len(string2))
    print ("'{0}' is longer than '{1}' by {2} chars".
            format(string_list[1], string_list[0], chars_diff))
    #Step 2
    percentage = float(len(string1))/len(string2)*100
    print ("'{0}' has only {1:.2f}% the number of chars of '{2}'".
            format(string_list[0], percentage, string_list[1]))
    various_solutions()  # Last line in f06()
###############################################################################
# Write f07, f08, f09, f10 to find the sum of all the multiples of 3 or 5 
# below 500 (starting at 1)
# f07 should demonstrate a while loop, returning the sum
# f08 should demonstrate a for loop, returning the sum
# f09 should demonstrate list comprehension, returning the sum
# f10 should demonstrate recursion, returning the sum
# check_solution_vals() will call the functions and check solutions.
# only edit the parameters in the function calls (if you want to)
###############################################################################
def various_solutions():
    """ This checks solutions. ONLY EDIT PARAMETERS PASSED TO FUNCTIONS. """
    while_ = f07()
    for_ = f08()
    list_comprehension = f09()
    recursion = f10()
    # DO NOT EDIT BELOW THIS LINE
    vals = [while_, for_, list_comprehension, recursion]
    for val in vals:
        print val
    if len(set(vals)) == 1:
        print("Not sure if it's right, but all your solutions agree!")
    else: print ("Oops...")
    f11_args = [1,"2", 3.0, '4', 5.0, 6]  # Last lines in various_solutions()
    for arg in f11_args:
        f11(arg)
    f12()
###############################################################################
def f07():
    '''Returns a sum of all the multiples of 3 or 5 below 500 (starting at 1), 
    using a while loop.
    '''
    number = 1
    total_sum = 0
    while number <= 500:
        if number%3 == 0 or number%5 == 0:
            total_sum += number
        number += 1
    return total_sum

###############################################################################
def f08():
    '''Returns a sum of all the multiples of 3 or 5 below 500 (starting at 1), 
    using a for loop.
    '''
    total_sum = 0
    for number in range(1, 501):
        if number%3 == 0 or number%5 == 0:
            total_sum += number
    return total_sum

###############################################################################
def f09():
    '''Returns a sum of all the multiples of 3 or 5 below 500 (starting at 1), 
    using list comprehension.
    '''
    multiples_list = ([number for number in range(1, 501) 
            if number%3 == 0 or number%5 == 0])
    return sum(multiples_list)


###############################################################################
def f10(number = 1, total_sum = 0):
    '''Returns a sum of all the multiples of 3 or 5 below 500 (starting at 1), 
    using recursion.
    '''
    # Recurssion is driving me crazy!!!
    # if number <= 10:
    #     total_sum = total_sum + f10((number + 1))
    # else:
    #     return total_sum
    pass
  


###############################################################################
# Write f11() to take arguments, printing them as floats if they started as
# strings, integers if they started as floats, and as the value 0 if they
# started as ints.
def f11(args):
    if type(args) == str:
        print float(args)
    if type(args) == float:
        print int(args)
    if type(args) == int:
        print 0


###############################################################################
# Write f12() to ask for raw_input from the user. Change the input to a float.
# Create log_file.txt to log the input that cannot be changed to a float. 
#   - write one faulty input per line
# Print, as a list, all converted input.
# Proceed to the last line, calling f13, when the user types done or "done"
# Ex. log_file.txt
#   TEST
#   123abc
#   python rules
# Ex. printing
#   [1.0, 1.3, 2.443]
def f12():
    with open('log_file.txt', 'w') as f:
        list_of_floats = []
        while True:
            user_input = raw_input('Please enter something:\n')
            if user_input == 'done' or user_input == '"done"':
                break
            
            try:
                user_input = float(user_input)
            except ValueError:
                f.write(user_input)
                f.write('\n')
            else:
                list_of_floats.append(user_input)

    print list_of_floats
    f13()  # Last line in f12()
###############################################################################
# Fix the error in f13:
def f13():
    for each in "string":
        print each
    f14()  # Last line in f13()
###############################################################################
# Write f14 to print the path and filename of this script. DO NOT HARD CODE.
# You must add an import statement. Please do so at the top of the file.
# Ex. /Users/dsg/Desktop/python-boot-camp/HW11/diagnostic.py
def f14():
    print os.getcwd()    
    f15()  # Last line in f14()
###############################################################################
# Write f15 to print the goal below. Do not print any strings.
# Do not take more than nine lines to code.
# Goal:
# [[0], [], [], [], [], [], [], [], [], []]
# [[], [0], [], [], [], [], [], [], [], []]
# [[], [], [0], [], [], [], [], [], [], []]
# [[], [], [], [0], [], [], [], [], [], []]
# [[], [], [], [], [0], [], [], [], [], []]
# [[], [], [], [], [], [0], [], [], [], []]
# [[], [], [], [], [], [], [0], [], [], []]
# [[], [], [], [], [], [], [], [0], [], []]
# [[], [], [], [], [], [], [], [], [0], []]
# [[], [], [], [], [], [], [], [], [], [0]]
def f15():
    for row in range(1, 11):
        row_list = []
        for column in range(1, 11):
            if row == column:
                row_list.append([0])
            else:
                row_list.append([])
        print row_list
    f16([1,2,3],[4,5,6])  # Last line in f15()
###############################################################################
# Write f16() that takes two lists and prints a list with the nth elements of 
# each list sharing a tuple.
# Ex.
# [1,2,3] and [4,5,6] would produce [(1, 4), (2, 5), (3, 6)]
def f16(list1, list2):
    print zip(list1, list2)
    f17()  # Last line in f16()
###############################################################################
# Write f17() to take the 2nd line from few_words.txt, and print a list
# with the index of the word in that line and the word, sharing tuples.
# Ex. [(0, 'To'), (1, 'be'), (2, 'or'), (3, 'not'), (4, 'to'), (5, 'be')]
def f17():
    with open('few_words.txt') as f:
        list_of_lines = f.read().split('\n')

    line_2 = list_of_lines[1].split()
    list_ = [(i, word) for i, word in enumerate(line_2)]
    print list_
    f18(list_)  # Last line in f17()
# Write f18 to take the list above and create a dictionary, use the words as
# keys and the numbers as values.
# Print the dictionary.
# Call the dictionary in f19()
def f18(list_):
    d = {item[1]:item[0] for item in list_}         ##Finished here at the end of class.
    print d
    f19(d)  # Last line in f18()
# Write f19 to update that dictionary by changing the values by adding the 
# number of chars in the word to the current value (if the resulting value
# would be even), otherwise change the value to the ascii number for the last
# char in the word. Print the new dictionary.
def f19(d):
    



    f22()  # Last line in f19()
# Write f21() to find if a word is capitalized. Return True/False.
# Ex.
# f21("Yes") = True, f21("NO") = False, 
# f21("nope") = False, f21("nADA") = False
def f21(word):
    pass





# Write f22() to use f21() to (1) print a list of all capitalized words in 
# few_words.txt sorted by length. Then (2) remove all duplicate words.
# (3) If our favorite word (Python) is in the list, move it to the front of the 
# list (because it deserves to be there). (4) Make Python all uppercase.
# (5) If magic is in the list. Delete it. 
# (6) Add an exlamation mark to Python.
# (7) To show how special Python is to us, put all the other words in a nested
# list so they don't contaminate Python.
# (8) This latest version (second print in this function)
# Ex. second print:
# ['PYTHON!', ['Other1', 'Other_2']]
def f22():
    








    f23([["o","o","x"],["x","o","x"],["o","","x"]])  # Last lines in f22()
    f23([["o","","o"],["x","o","x"],["o","x","x"]])
    f23([["o","o","x"],["x","x","x"],["o","","o"]])
# Write f23() that takes a list of three lists of len 3, and says who won in 
# tic-tac-toe (you can expect all moves to have been legal, made turn-by-turn)
# you can expect there is a winner. Print the x or o and the type of win:
# "col1", "col2", "row3", "falling_back_diag", "falling_front_diag" 
# Ex. of rows (not a finished game)
# row1 = ["o","",""]
# row2 = ["","x",""]
# row3 = ["","",""]
# Ex. of print: x, col2
def f23(lists_):
    pass













# Write main() that calls f01, then prints the The Zen of Python, by Tim Peters.
# (three lines)
def main():
    # f01()
    # import this

    
    f18(f17())





# Write the boilerplate code. (two lines)
if __name__ == "__main__":
    main()


