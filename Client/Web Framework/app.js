console.log('hello world')

//selectors

//it selects an item from the html doc
const todoInput = document.querySelector('.todo-item');
const todoButton = document.querySelector('.add-button');
const todoList = document.querySelector('.todo-list');
 
//functions
function addTodo(event){
   
    //prevent default behaviour
    event.preventDefault();
   
    //create todo div with class todo
    const todoDiv =document.createElement('div');
    todoDiv.classList.add("todo");

    //check button
    const completeButton = document.createElement('button');
    completeButton.innerHTML = '<i class="fas fa-check"></i>';
    completeButton.classList.add("complete-btn");
    todoDiv.appendChild(completeButton);
   
    //create li with class todo-item and append it to todo div
    const newTodo =document.createElement('li');
    newTodo.innerText = todoInput.value;
    newTodo.classList.add('todo-item');
    todoDiv.appendChild(newTodo);
   
    //check del button
    const delButton = document.createElement('button');
    delButton.innerHTML = '<i class="fas fa-trash"></i>';
    delButton.classList.add("del-btn");
    todoDiv.appendChild(delButton);
    
    //append to list
    todoList.appendChild(todoDiv);

    //clear value
    todoInput.value = "";
}

function checkDelete(event){
    const item = event.target;

    //delete

    if ( item.classList[0] === "del-btn"){
        const todo = item.parentElement;
        todo.remove();
    }

    //check
    if ( item.classList[0] === "complete-btn"){
        const todo = item.parentElement;
        todo.classList.toggle('completed');
    }


}

//event listners

todoButton.addEventListener('click',addTodo)
todoList.addEventListener('click', checkDelete)