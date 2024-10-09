
# Task Management Web App

A task management application built with Python and Flask that allows users to manage tasks through a single-page web interface. You can add, mark as complete, and delete tasks, all from one page. The application uses SQLite for persistent storage and includes user authentication to support multiple users.

## Features

-   **User Authentication**: Secure login and registration system, ensuring only authorized users can access their task lists.
-   **Multi-User Functionality**: Each user has their own task list, so tasks are user-specific.
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
    pip install flask` 
    ```
    
3.  **Create a `.env` file** based on the `.env.example`:
    -   Copy `.env.example` to `.env` and update any necessary environment variables (e.g., secret keys).
4.  **Run `keygen.py`** to generate a secure key:
    ```
    `python keygen.py` 
    ```
5.  **Run the web application**:
    ```
    `python main.py` 
    ```
6.  **Access the app**: Open your browser and go to `http://127.0.0.1:5000` to manage tasks and user accounts through the web interface.

## Web Interface Overview

-   **Task List**: The homepage displays a list of tasks with options to add new tasks, delete tasks, or mark tasks as complete, all from one page.
    -   Example:
        -   `go shopping` [Mark Complete] [Delete]
        -   `go to gym` [Mark Complete] [Delete]
        -   `call madushani` [Mark Complete] [Delete]
-   **Add Task**: Add new tasks by filling out a form at the top of the page.
-   **Mark Complete**: Easily mark tasks as complete by clicking the "Mark Complete" button.
-   **Delete**: Remove a task from the list by clicking "Delete."
-   **User Authentication**: Only registered users can log in and manage their tasks.

## Database

The app uses an SQLite database (`database.db`) to store tasks and user credentials. The database schema includes fields for task descriptions, completion statuses, and user IDs. The `dbms.py` module handles all database operations, including creating tables, inserting, retrieving, and deleting tasks and users.

## Folder Structure

```

`├── static/           # Static files (CSS, JS)
│   ├── css/
│   └── js/
├── templates/        # HTML templates (login, register, task management)
│   ├── index.html
│   ├── login.html
│   └── register.html
├── app.py            # Backend logic for task management and authentication
├── main.py           # Flask app entry point
├── dbms.py           # Database management for SQLite
├── keygen.py         # Generates secure keys for authentication
├── database.db       # SQLite database file
├── .env              # Environment variables file
├── .env.example      # Example environment file
└── README.md         # Project documentation` 
```
## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

-   Inspired by various task management applications.
-   Special thanks to the open-source community for their contributions and support.