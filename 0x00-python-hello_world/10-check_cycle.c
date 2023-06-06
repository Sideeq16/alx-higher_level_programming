#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checker cycle if exists
 * @list: node
 * Return: integer value
 */
int check_cycle(listint_t *list)
{
	listint_t slw = list;
	listint_t *fst  = list;

	while (fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;

		if (slw == fst)
		{
			return (1);
		}
	}

	return (0);
}
