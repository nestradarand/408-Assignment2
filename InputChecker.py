'''
This class simply serves to ensure that a string is a pure string with no numerical values in it
Mainly to make sure valid Majors, Advisors and Names are being entered
'''

class Checker:

    def is_pure_text(to_check:str) -> bool:
        ###if a char is not alphabetic, a space, or a hyphen then we return false for that word
        for i in to_check:
            if not i.isalpha() and i != ' ' and i != '-':
                return False
        return True