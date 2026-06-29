import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def _evaluate(node):
    if isinstance(node, ast.Constant):  # numbers
        return node.value

    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)

        op = OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported operator.")

        return op(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)

        op = OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported unary operator.")

        return op(operand)

    raise ValueError("Invalid expression.")


def calculator(expression: str) -> dict:
    if not expression or not expression.strip():
        return {
            "success": False,
            "error": {
                "message": "Expression cannot be empty."
            }
        }

    try:
        tree = ast.parse(expression, mode="eval")
        result = _evaluate(tree.body)

        return {
            "success": True,
            "data": {
                "result": result
            }
        }

    except ZeroDivisionError:
        return {
            "success": False,
            "error": {
                "message": "Division by zero."
            }
        }

    except Exception:
        return {
            "success": False,
            "error": {
                "message": "Invalid mathematical expression."
            }
        }