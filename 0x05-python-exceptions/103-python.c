#include <Python.h>

void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid PyListObject\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, type);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "Invalid PyBytesObject\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("        - Length: %zd\n", size);
	printf("        - Bytes: ");
	if (size > 10)
		size = 10;

	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i != size - 1)
			printf(" ");
	}
	printf("\n");
}

void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "Invalid PyFloatObject\n");
		return;
	}

	printf("[.] float object info\n");

	double value = PyFloat_AsDouble(p);
	printf("        - Value: %f\n", value);
}
