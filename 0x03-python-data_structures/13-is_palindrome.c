#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: the head od list
 * Return: Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, a[1024];

	temp = *head;
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (temp)
	{
		a[i] = temp->n;
		temp = temp->next;
		if (a[i] == temp->n && a[i - 1] == (temp->next)->n)
			break;
		if (a[i - 1] == temp->n&& a[i - 2] == (temp->next)->n)
			break;
		i++;
	}
	if (i <= 1 || (i == 3 && a[0] == a[2]) || (i == 2 && a[0] == a[1]))
		return (1);
	while (i >= 0 && temp)
	{
		if (a[i] != temp->n && a[i - 1] != temp->n)
			return (0);
		temp = temp->next;
		i--;
	}
	return (1);
}
