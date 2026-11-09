# REST API Data Management

This project contains Python scripts designed to interact with a REST API ([JSONPlaceholder](https://jsonplaceholder.typicode.com)) to retrieve, process, and export employee task and TODO list data into multiple formats (CSV and JSON).

## Project Requirements

- **Environment**: All files are interpreted and compiled on Ubuntu 14.04 LTS using Python 3 (version 3.4.3).
- **Style**: Code adheres strictly to the PEP 8 style guide.
- **Shebang**: Every Python script begins with `#!/usr/bin/python3`.
- **Imports**: All imported libraries are organized in alphabetical order.
- **Safety**: Dictionary values are accessed safely using the `.get()` method.
- **Execution**: Scripts are non-executable when imported using the `if __name__ == "__main__":` guard.
- **File Endings**: All files end with a new line.

## Files Description

| File | Description |
| --- | --- |
| `0-gather_data_from_an_API.py` | Accepts an employee ID as a command-line argument and displays their TODO list progress on standard output. |
| `1-export_to_csv.py` | Extends Task #0 by exporting all tasks associated with a given employee ID into a CSV file (`USER_ID.csv`). |
| `2-export_to_JSON.py` | Extends Task #0 by exporting all tasks associated with a given employee ID into a structured JSON file (`USER_ID.json`). |
| `3-dictionary_of_list_of_dictionaries.py` | Fetches TODO list data for all employees and exports the combined dataset into a JSON file (`todo_all_employees.json`).|
