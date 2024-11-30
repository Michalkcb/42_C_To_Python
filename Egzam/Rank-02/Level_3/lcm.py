# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lcm.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbany <mbany@student.42warsaw.pl>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/11/30 12:51:24 by mbany             #+#    #+#              #
#    Updated: 2024/11/30 12:56:35 by mbany            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""
Assignment name  : lcm
Expected files   : lcm.c
Allowed functions:
--------------------------------------------------------------------------------

Write a function who takes two unsigned int as parameters and returns the
computed LCM of those parameters.

LCM (Lowest Common Multiple) of two non-zero integers is the smallest postive
integer divisible by the both integers.

A LCM can be calculated in two ways:

- You can calculate every multiples of each integers until you have a common
multiple other than 0

- You can use the HCF (Highest Common Factor) of these two integers and
calculate as follows:

	LCM(x, y) = | x * y | / HCF(x, y)

  | x * y | means "Absolute value of the product of x by y"

If at least one integer is null, LCM is equal to 0.

Your function must be prototyped as follows:

  unsigned int    lcm(unsigned int a, unsigned int b);
"""
def    lcm(a, b):
	n = 0
	if a == 0 or b == 0:
		return 0
	if a > n:
		n = a
	else:
		n = b
	while 1:
		if n % a == 0 and n % b == 0:
			return (n)
		n += 1


a = int(input("podaj a: "))
b = int(input("podaj b: "))
result = lcm(a, b)
print(result)
