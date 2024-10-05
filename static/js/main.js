let tasks = [];


// Event listeners
$(document).ready(function () {
    loadTasks(); // Load tasks on page load

    // Add task button
    $('#addTaskBtn').click(function () {
        addTask();
    });

    // Handle task deletion using event delegation
    $(document).on('click', '.deleteTaskBtn', function () {
        let index = $(this).data('index');
        deleteTask(index);
    });

    // Handle task completion using event delegation
    $(document).on('click', '.markCompleteBtn', function () {
        let index = $(this).data('index');
        markComplete(index);
    });
});

// Load tasks from server using AJAX and jQuery
function loadTasks() {
    $.ajax({
        url: "/load-tasks",
        type: "GET",
        success: function (response) {
            console.log("Success:", response);
            // Loop through the response and push each task to the tasks array
            $.each(response.tasks, function (index, task) {
                tasks.push({ task: task[0], completed: task[1] });
            });
            renderTasks(); // Call render after loading
        },
        error: function (xhr, status, error) {
            console.log("Error:", error);
        },
    });
}
function saveTasks() {
    $.ajax({
        url: "/save-tasks",
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify({ tasks: tasks }),
        success: function (response) {
            console.log("Success:", response);
        },
        error: function (xhr, status, error) {
            console.log("Error:", error);
        },
    });
}

// Render tasks in the taskList
function renderTasks() {
    $('#taskList').empty(); // Clear the list

    // Loop through tasks array and append each task to the list
    $.each(tasks, function (index, task) {
        let taskItem = `
      <li class="flex justify-between items-center border border-gray-300 p-3 rounded">
        <span class="${task.completed ? 'line-through text-gray-500' : ''}">${task.task}</span>
        <div>
          <button class="text-green-500 mr-2 markCompleteBtn" data-index="${index}">${task.completed ? '✔' : 'Mark Complete'}</button>
          <button class="text-red-500 deleteTaskBtn" data-index="${index}">Delete</button>
        </div>
      </li>
    `;
        $('#taskList').append(taskItem);
    });
}

// Add a new task
function addTask() {
    let newTask = $('#taskInput').val().trim();
    if (newTask) {
        tasks.push({ task: newTask, completed: false });
        $('#taskInput').val(''); // Clear input field
        renderTasks(); // Update task list
        saveTasks();
    } else {
        alert('Please enter a task');
    }
}

// Delete a task based on its index
function deleteTask(index) {
    tasks.splice(index, 1); // Remove task from array
    renderTasks(); // Update the list
    saveTasks();
}

// Mark a task as complete or incomplete
function markComplete(index) {
    tasks[index].completed = !tasks[index].completed; // Toggle completed status
    renderTasks(); // Update the list
    saveTasks();
}

