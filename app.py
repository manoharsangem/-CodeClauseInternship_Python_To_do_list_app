from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks
tasks = []

# Home route - displays the to-do list
@app.route('/')
@app.route('/home')
def home():
    return render_template('front.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')  # Get the task from the form
    if task:
        tasks.append(task)  # Add the task to the list
    return redirect(url_for('home'))  # Redirect back to the home page

# Route to delete a task
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):  # Check if task_id is valid
        tasks.pop(task_id)  # Remove the task by its index
    return redirect(url_for('home'))  # Redirect back to the home page

# Route to edit a task
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'POST':
        updated_task = request.form.get('task')
        if updated_task and 0 <= task_id < len(tasks):  # Check if task_id is valid
            tasks[task_id] = updated_task  # Update the task
        return redirect(url_for('home'))
    return render_template('edit.html', task_id=task_id, task=tasks[task_id])

if __name__ == '__main__':
    app.run(debug=True)
