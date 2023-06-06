#include <stdio.h>
#include <stdlib.h>
#include "main.h"
listint_t* insert_node(listint_t** head, int number) {
    
    listint_t* new_node = (listint_t*)malloc(sizeof(listint_t));
    if (new_node == NULL) {
        /* Failed to allocate memory for the new node */
        return NULL;
    }
    new_node->data = number;
    new_node->next = NULL;

    /* If the list is empty or the new node should be inserted at the beginning */
    if (*head == NULL || number < (*head)->data) {
        new_node->next = *head;
        *head = new_node;
        return new_node;
    }

    /* Traverse the list to find the appropriate position to insert the new node */
    listint_t* current = *head;
    while (current->next != NULL && current->next->data < number) {
        current = current->next;
    }

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;
    return new_node;
}
