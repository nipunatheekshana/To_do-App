
# Task Management Web App

A task management application built with Python and Flask that allows users to manage tasks through a single-page web interface. You can add, mark as complete, and delete tasks, all from one page. The application uses SQLite for persistent storage.

## Features

-   **Single-Page Web Interface**: Manage all tasks on a single page—add, mark tasks as complete, and delete tasks easily.
-   **Add Tasks**: Input new tasks through a form on the same page.
-   **Mark Complete**: Mark tasks as complete with a single click.
-   **Delete Tasks**: Remove tasks from the list directly.
-   **Persistent Storage**: Tasks are stored in an SQLite database to ensure they are saved across sessions.

## Requirements

-   Python 3.x
-   Flask
-   SQLite

## Installation and Setup

1.  **Clone the repository** or download the project files.
2.  **Install Flask**:
    ```
    pip install flask
    ```
3.  **Run the web application**
    ```
    python main.py
    ```
5.  **Access the app**: Open your browser and go to `http://127.0.0.1:5000` to manage tasks in the web interface.

## Web Interface Overview

-   **Task List**: The homepage displays a list of tasks with options to add new tasks, delete tasks, or mark tasks as complete, all from one page.
    -   Example:
        -   `go shopping` [Mark Complete] [Delete]
        -   `go to gym` [Mark Complete] [Delete]
        -   `call madushani` [Mark Complete] [Delete]
-   **Add Task**: Add new tasks by filling out a form at the top of the page.
-   **Mark Complete**: Easily mark tasks as complete by clicking the "Mark Complete" button.
-   **Delete**: Remove a task from the list by clicking "Delete."

## Database

The app uses an SQLite database (`database.db`) to store tasks. The database schema includes fields for task descriptions and completion statuses. The `dbms.py` module handles all database operations, including creating tables, inserting, retrieving, and deleting tasks.

## Folder Structure

```
├── static/           # Static files (CSS, JS)
│   ├── css/
│   └── js/
├── templates/        # HTML templates
│   └── index.html
├── app.py            # Backend logic for task management
├── main.py           # Flask app entry point
├── dbms.py           # Database management for SQLite
├── database.db       # SQLite database file
└── README.md         # Project documentation
```

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

-   Inspired by various task management applications.
-   Special thanks to the open-source community for their contributions and support.

----------

This README now removes the `requirements.txt` section and instead provides the command to install Flask manually. Let me know if you'd like any further adjustments!