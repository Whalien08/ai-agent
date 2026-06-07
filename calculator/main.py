import sys
from pkg.calculator import calculator
from pkg.render import render_calculator

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"<equation>\"")
        print("Example: python main.py \"2 + 2\"")
        sys.exit(1)

    equation = sys.argv[1]
    try:
        res = calculator(equation)
        render_calculator(equation, res)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()