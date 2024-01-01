#include "lists.h"

/**
 * check_cycle - checks for cycles in singly linked
 * @list: pointer to our list
 * Return: 0 if no cycle, 1 if cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *chker;
	listint_t *prev;

	chker = list;
	prev = list;
	while (list && chker && chker->next)
	{
		list = list->next;
		chker = chker->next->next;

		if (list == chker)
		{
			list = prev;
			prev =  chker;
			while (1)
			{
				chker = prev;
				while (chker->next != list && chker->next != prev)
				{
					chker = chker->next;
				}
				if (chker->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}

	return (0);
}
