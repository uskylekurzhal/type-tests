## Summary
This example is intended to show how we can achieve static/compile-time type checking in Python 2, which will also carry over when we switch our codebase to Python 3, by taking advantage of a Python library called [mypy](https://mypy.readthedocs.io/).

## How To Implement Type Checking
To implement the type checking in Python 2, you must:
* Install Python 3
* Install `mypy` with Python 3's pip
* Install the `typing` library with Python 2's pip (it is not included in the Python 2 standard library, unlike Python 3)

When performing type checking with mypy on Python 2 code, you must run `mypy --py2 <your-file>`.  However, you can remove the `--py2` argument to run type checking on Python 3 code.

To add types in Python 2, you simply add comments with the appropriate types (see the example or the [mypy website](https://mypy.readthedocs.io/en/stable/python2.html) for syntax).  These type comments work for both Python 3 *and* Python 2.

## How To Run This Code
By running the below example, you can see how mypy 

```
docker-compose up;
docker exec -ti type-test bash;

# mypy --py2 type_test.py;
# python2.7 type_test.py;
```

There is a line in the code that you can also edit in order to see how the type checker handles mismatching types.
