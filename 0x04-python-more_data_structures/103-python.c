#include <stdio.h>

struct timespec;

#include <Python.h>

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: our list
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, first, i;
	char *word;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	word = PyBytes_AsString(p);
	printf("  size: %ld\n  trying string: %s\n", size, word);
	if (size >= 10)
		first = 10;
	else
		first = size + 1;
	printf("  first %ld bytes:", size + 1);
	for (i = 0; i < first; i++)
	{
		if (word[i] >= 0)
			printf(" %02x", word[i]);
		else
			printf(" %02x", word[i] + 256);
	}
	printf("\n");
}
/**
 * print_python_list - prints some basic info about Python lists.
 * @p: our list
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len, i;
	PyObject *item;

	len = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %ld: %s\n", i, (item->ob_type)->tp_name);
		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
