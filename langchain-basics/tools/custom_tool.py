from langchain_community.tools import tool


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b


# Step 3 - add tool decorator


@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers a, b"""
    return a * b


result = multiply.invoke({"a": 2, "b": 5})
print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args)
print(multiply.args_schema.model_json_schema())  # this is how tool sent to LLM
