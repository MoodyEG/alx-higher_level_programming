#include "lists.h"

/**
 * insert_node - inserts a new node and sort it
 * @head: the head od list
 * @number: the data to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp, *prev;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	if (temp == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	while (temp != NULL)
	{
		if (number < temp->n)
			break;
		prev = temp;
		temp = temp->next;
	}
	new->next = temp;
	if (temp == *head)
		*head = new;
	else
		prev->next = new;

	return (new);
}
