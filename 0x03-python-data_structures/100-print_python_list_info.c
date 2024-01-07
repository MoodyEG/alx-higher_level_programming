#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: our list
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{/*Used AI and a lot of outside help for this one*/
	Py_ssize_t len, i;
	PyObject *item;

	len = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (i = 0; i < len; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
