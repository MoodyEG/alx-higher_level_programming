#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints Python strings.
 * @p: Our PyObject
 * Return: no return
 */
void print_python_string(PyObject *p)
{
	PyObject *str;

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}
