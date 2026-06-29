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
    # Block strings, booleans, and non-numeric types early
    if isinstance(node, ast.Constant):
        if type(node.value) not in (int, float):
            raise ValueError("Only literal numbers are allowed.")
        return node.value

    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)

        # Prevent CPU-melting operations (e.g., 9**9**9)
        if isinstance(node.op, ast.Pow):
            if right > 1000 or left > 10000:
                raise ValueError("Exponent or base too large to calculate safely.")

        op = OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported mathematical operator.")

        return op(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)

        op = OPERATORS.get(type(node.op))
        if op is None:
            raise ValueError("Unsupported unary operator.")

        return op(operand)

    raise ValueError("Invalid mathematical syntax.")


def calculator(expression: str) -> dict:
    if not expression or not expression.strip():
        return {
            "success": False,
            "error": { "message": "Expression cannot be empty." }
        }

    try:
        tree = ast.parse(expression.strip(), mode="eval")
        result = _evaluate(tree.body)

        return {
            "success": True,
            "data": { "result": result }
        }

    except ZeroDivisionError:
        return {
            "success": False,
            "error": { "message": "Division by zero." }
        }
    except Exception as e:
        error_msg = str(e) if str(e) else "Invalid mathematical expression."
        return {
            "success": False,
            "error": { "message": error_msg }
        }
