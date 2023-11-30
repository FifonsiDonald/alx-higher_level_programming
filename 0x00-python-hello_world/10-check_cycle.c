#include "lists.h"

/**
 * check_cycle - Function to check if there is cycle in list
 * @list: linked list to check
 * Return: 1 for cycle, 0 if none
 */

int check_cycle(listint_t *list)
{
	listint_t *h = list;
	listint_t *t = list;

	if (!list)
		return (0);

	while (1)
	{
		if (hare->next != NULL && hare->next->next != NULL)
		{
			h = h->next->next;
			t = t->next;

			if (h == t)
				return (1);
		}
		else
			return (0);
	}
}
