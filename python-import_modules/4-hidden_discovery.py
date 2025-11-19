#!/usr/bin/python3
import importlib.util


def main():
    """Print all names defined in hidden_4.pyc (excluding __ names)."""
    # Load the compiled module
    spec = importlib.util.spec_from_file_location("hidden_4", "/tmp/hidden_4.pyc")
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get names defined in the module (exclude names starting with __)
    names = [name for name in dir(hidden_4) if not name.startswith("__")]

    # Print names in alphabetical order
    for name in sorted(names):
        print(name)


if __name__ == "__main__":
    main()
