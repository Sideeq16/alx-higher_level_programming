#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - list python 
 * @py_list: python list
 * Return: list of python element
 */
void print_python_list_info(PyObject *py_list)
{
    Py_ssize_t list_size = PyList_Size(py_list);
    Py_ssize_t list_allocated = ((PyListObject *)py_list)->allocated;
    Py_ssize_t index;

    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", list_allocated);

    for (index = 0; index < list_size; index++)
    {
        PyObject *list_item = PyList_GetItem(py_list, index);
        printf("Element %ld: %s\n", index, Py_TYPE(list_item)->tp_name);
    }
}
