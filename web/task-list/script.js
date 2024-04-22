// Constants for DOM elements
const taskInput = document.querySelector("#newtask input"); // Selects the input field for entering new tasks
const taskSection = document.querySelector('.tasks'); // Selects the section where tasks will be displayed

// Event listener for keyup event on taskInput (Enter key)
taskInput.addEventListener("keyup", (e) => {
    if (e.key === "Enter") {
        createTask(); // Calls createTask function if Enter key is pressed
    }
});

// Event listener for click event on the add button (identified by id 'push')
document.querySelector('#push').onclick = function() {
    createTask(); // Calls createTask function when add button is clicked
};

// Function to create a new task
function createTask() {
    const taskName = taskInput.value.trim(); // Gets the trimmed value of the task input field

    // Check if taskName is empty
    if (taskName.length === 0) {
        alert("The task field is empty. Enter a task name and try again."); // Displays an alert if task name is empty
        return; // Exits the function early if task name is empty
    }

    // Appends new task HTML to taskSection
    taskSection.innerHTML += `
        <div class="task">
            <label class="taskname">
                <input type="checkbox" onclick="updateTask(this)">
                <p>${taskName}</p>
            </label>
            <div class="delete">
                <i class="uil uil-trash"></i>
            </div>
        </div>`;

    taskInput.value = ''; // Clears the task input field after adding the task

    // Add click event listener to all delete icons (class 'delete')
    const deleteIcons = document.querySelectorAll(".delete");
    deleteIcons.forEach(icon => {
        icon.onclick = function() {
            this.parentNode.remove(); // Removes the task's parent element (the entire task) when delete icon is clicked
        };
    });

    // Check if taskSection height is >= 300px and apply CSS class accordingly
    if (taskSection.offsetHeight >= 300) {
        taskSection.classList.add("overflow"); // Adds 'overflow' class to taskSection if height exceeds 300px
    } else {
        taskSection.classList.remove("overflow"); // Removes 'overflow' class from taskSection if height is less than 300px
    }
}

// Function to update task status (checked/unchecked)
function updateTask(task) {
    const taskItem = task.parentElement.querySelector('p'); // Gets the <p> element (task name) within the task's <label>

    // Toggle 'checked' class based on checkbox state
    if (task.checked) {
        taskItem.classList.add("checked"); // Adds 'checked' class to task name if checkbox is checked
    } else {
        taskItem.classList.remove("checked"); // Removes 'checked' class from task name if checkbox is unchecked
    }
}
