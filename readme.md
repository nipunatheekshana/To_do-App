# Task Management Script

A simple command-line task management application in Python that allows you to add, view, delete, and mark tasks as complete. This script stores tasks in a text file, making them persistent across sessions.

## Features

- **Add Tasks**: Input new tasks to your task list.
- **View Tasks**: Display all tasks with their completion status.
- **Delete Tasks**: Remove tasks from your list.
- **Mark Tasks as Complete**: Update the status of a task to completed.
- **Save Tasks**: Automatically saves tasks to a text file.
- **Help Command**: Provides a list of commands and their functions.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository** or download the script.
2. **Run the script** using Python:
   ```bash
   python app.py
   ```
3. Follow the on-screen prompts to manage your tasks.

## Commands

- `1`: Add task
- `2`: View tasks
- `3`: Delete task
- `4`: Mark task as complete
- `5`: Save tasks
- `6`: Exit the application (saves tasks automatically)
- `7`: Display help information

## File Storage

Tasks are stored in a text file named `tasks.txt`. Each task is saved in the format:
```
task_name%%%completed_status
```
Where `completed_status` is a boolean value (`True` or `False`).

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various task management applications.
- Thank you to the open-source community for their contributions and support.
```

### Instructions to Use:
- You can modify sections like "Contributing" or "License" based on your preferences or project's requirements.
- Make sure to adjust the filename in the usage section if your script has a different name.