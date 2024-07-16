# works for both numbers and character strings
integer = 121


def palindrome(integer):
    str_num = str(integer)
    reversed = str_num[::-1]
    if str_num == reversed:
        return True
    else:
        return False


print(palindrome(integer))
