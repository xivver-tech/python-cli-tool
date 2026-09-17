#!/usr/bin/env python3
"""Simple command-line calculator."""

import sys

def main():
    print("Simple CLI Calculator")
    print("Enter expressions like: 2 + 3, 10 * 4, 15 / 3")
    print("Type 'quit' or 'exit' to leave.\n")

    while True:
        try:
            expr = input("> ").strip()
            if expr.lower() in ("quit", "exit", "q"):
                print("Bye!")
                break
            if not expr:
                continue
            # Safe-ish evaluation for basic arithmetic
            result = eval(expr, {"__builtins__": {}}, {})
            print(f"= {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
