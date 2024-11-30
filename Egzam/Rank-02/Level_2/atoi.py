# /* ************************************************************************** */
# /*                                                                            */
# /*                                                        :::      ::::::::   */
# /*   ft_atoi.py                                         :+:      :+:    :+:   */
# /*                                                    +:+ +:+         +:+     */
# /*   By: mbany <mbany@student.42warsaw.pl>          +#+  +:+       +#+        */
# /*                                                +#+#+#+#+#+   +#+           */
# /*   Created: 2024/02/28 15:52:02 by mbany             #+#    #+#             */
# /*   Updated: 2024/03/15 10:21:18 by mbany            ###   ########.fr       */
# /*                                                                            */
# /* ************************************************************************** */

#include "libft.h"

def ft_atoi(s):
    result = 0
    sign = 1
    i = 0

    while i < len(s) and s[i].isspace():
        i += 1
        
    if i < len(s) and (s[i] == '-' or s[i] == '+'):
        if s[i] == '-':
            sign = -1
        i += 1

    while i < len(s) and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1

    return result * sign

str1 = "1654"
str2 = "98765"
str3 = "-852"
str4 = "852"
str5 = "159"
str6 = "357"


num1 = ft_atoi(str1)
num2 = ft_atoi(str2)
num3 = ft_atoi(str3)
num4 = ft_atoi(str4)
num5 = ft_atoi(str5)
num6 = ft_atoi(str6)

#  Testujemy wyniki
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)
