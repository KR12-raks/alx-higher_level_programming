#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "lists.h"

/**
 * insert_node - insert a number into a sorted list
 *
 * @head: A linked list
 *
 * @number: number to be inserted
 *
 * Return: pointer to the new haed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);
	
	new = malloc(sizeof(listint_t))
	if (!new)
		return (NULL);

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < number)
		{
			temp->next = new;
			new->next = current;
		}

		temp->next = new;
		new->next = current;
	}
	return (new);
}
