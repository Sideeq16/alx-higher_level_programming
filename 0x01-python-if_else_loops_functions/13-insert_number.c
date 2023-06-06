#include <stdio.h>
#include <stdlib.h>
#include "main.h"

/**
 * insert_node - insert into a node
 * @head: head
 * @number: number to insert
 * Return: new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);  /* Failed to allocate memory for the new node */
	}

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
	new_node->next = *head;
	*head = new_node;
	return (new_node);
	}

	listint_t *current = *head;

	while (current->next != NULL && number > current->next->n)
	{
	current = current->next;
	}

	new_node->next = current->next;
	current->next = new_node;
	return (new_node);
}
