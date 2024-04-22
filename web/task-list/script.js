//declaring constants
const taskInput = document.querySelector("#newtask input");
const taskSection = document.querySelector('.tasks');
//listener for enter key
taskInput.addEventListener("keyup",(e) => {
    if(e.key == "Enter"){createTask();}});
//onclick event for the add button
document.querySelector(#push).onclick = function() {
    createTask();
}
//the task creation itself
function createTask() {
    if (taskInput.value.length == 0){
        alert("The task field is blanks. Enter a task name and try again.");
    }
    else{
        taskSection.innerHTML +=
        `<div class="task">
        <label id="taskname">
        <input onclick="updateTask(this)" type="checkbox" id="check-task">
        <p>${document.querySelector('#newtask input').value}</p>
        </label> 
        <div class="delete">
        <i class="uil uil-trash"></i></div></div>`;  
        var current_task = document.querySelectorAll(".delete");
        for (var i = 0; i < current_task.length; i++) {
        current_task[i].onclick = function () {
        this.parentNode.remove(); }}   
        taskSection.offsetHeight >= 300
        ? taskSection.classList.add("overflow")
        : taskSection.classList.remove("overflow";)
    }
}
function updateTask(task){
    let taskItem = task.parentElement.lastElementChild;
    if (task.checked){
        taskItem.classList.add("checked");}
    else {taskItem.classList.remove("checked");}
}
