'''
/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   s_swap.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mbany <mbany@student.42warsaw.pl>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/04/24 13:23:30 by mbany             #+#    #+#             */
/*   Updated: 2024/05/24 11:05:29 by mbany            ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*
Assignment name  : ft_swap
Expected files   : ft_swap.c
Allowed functions:
--------------------------------------------------------------------------------

Write a function that swaps the contents of two integers the adresses of which
are passed as parameters.

Your function must be declared as follows:

void	ft_swap(int *a, int *b);
'''


#include <unistd.h>
#include <stdio.h>

def	ft_swap(a, b):
	return b,a

def main():

    a = 5
    b = 10
    
    print("before swapping")
    print("a:", a)
    print("b:", b)
    
    a,b = ft_swap(a, b)
    
    print("After swapping:")
    print("a:", a)
    print("b:", b)

if __name__ == "__main__":
    main()
