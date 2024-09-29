# Assignment name  : rostring
# Expected files   : rostring.c
# Allowed functions: write, malloc, free
# --------------------------------------------------------------------------------

# Write a program that takes a string and displays this string after rotating it
# one word to the left.

# Thus, the first word becomes the last, and others stay in the same order.

# A "word" is defined as a part of a string delimited either by spaces/tabs, or
# by the start/end of the string.

# Words will be separated by only one space in the output.

# If there's less than one argument, the program displays \n.

# Example:

# $>./rostring "abc   " | cat -e
# abc$
# $>
# $>./rostring "Que la      lumiere soit et la lumiere fut"
# la lumiere soit et la lumiere fut Que
# $>
# $>./rostring "     AkjhZ zLKIJz , 23y"
# zLKIJz , 23y AkjhZ
# $>
# $>./rostring "first" "2" "11000000"
# first
# $>
# $>./rostring | cat -e
# $
# $>


def first_word( s):
	i = 0

	while i < len(s) and (s[i] == ' ' or s[i] == '\t'):
		i += 1
	while s[i] != ' ' and s[i] != '\t' and s[i] != '\0':
		print(s[i], end = '')
		i += 1

def main(args):
	if len(args) > 1:
		s = args[1]
		i = 0
		while i < len(s) and s[i] == ' ' or s[i] == '\t':
			i += 1
		while i < len(s) and s[i] != ' ' and s[i] != '\t' and s[i] != '\0':
			i += 1
		while i < len(s) and s[i] == ' ' or s[i] == '\t':
			i += 1
		while i < len(s):
			if s[i] == ' ' or s[i] == '\t':
				while i < len(s) and s[i] == ' ' or s[i] == '\t':
					i += 1
				if i < len(s):
					print(' ', end='')
			else:
				print(s[i], end ='')
				i +=1
		print(' ',end = '')
		first_word(s)
	print()
if __name__ == "__main__":
    import sys
    main(sys.argv)
