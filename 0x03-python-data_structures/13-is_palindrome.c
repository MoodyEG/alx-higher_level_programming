#include "lists.h"

/**
 * list_len - gets the length of the list
 * @head: the head of list
 * Return: length of the list
 */
int list_len(listint_t **head)
{
	listint_t *temp;
	int len = 0;

	temp = *head;
	while (temp)
	{
		temp = temp->next;
		len++;
	}
	return (len);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp, *lent;
	int i = 0, len = 0, a[1024];

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = lent = *head;
	len = list_len(&lent);
	while (temp)
	{
		a[i] = temp->n;
		temp = temp->next;
		if (temp)
			if (temp->next && i + 1 >= len / 2)
				{
					if (len % 2 == 0 && a[i] == temp->n && a[i - 1] == (temp->next)->n)
						break;
					if (len % 2 != 0 && a[i - 1] == temp->n && a[i - 2] == (temp->next)->n)
						break;
				}
		i++;
	}
	if (len >= 4 && !temp)
		return (0);
	while (i >= 0 && temp)
	{
		if (a[i] != temp->n && len % 2 == 0)
			return (0);
		if (a[i - 1] != temp->n && len % 2 != 0)
			return (0);
		temp = temp->next;
		i--;
	}

	return (1);
}
