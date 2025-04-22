🌟 Django CRUD Operations Assignment

📌 Objective

Create a Django web application that performs CRUD operations (Create, Read, Update, Delete) using a single model.

🛠️ Model to Use

Model Name: Task Fields:

title (CharField, max_length=200)
description (TextField)
due_date (DateTimeField)
is_completed (BooleanField, default=False)
📂 Documentation Structure to Follow

1. Project Setup
Install Django and create a project named task_manager.
Create an app named tasks.
Add tasks to INSTALLED_APPS in settings.py.
2. Model Definition
Define the Task model in models.py.
Run migrations:
python manage.py makemigrations  
python manage.py migrate  
3. Admin Registration
Register the Task model in admin.py to interact with it via Django’s admin interface.
4. CRUD Operations Implementation
🔹 Create

Create a form in forms.py for adding new tasks.
Design a template (create_task.html) with a form to submit task details.
Add a view to handle form submission and save data to the database.
🔹 Read

Create a view to display all tasks in a template (task_list.html).
Include a "Detail" button to view individual task details in a new template (task_detail.html).
🔹 Update

Add an "Edit" button in task_list.html to modify existing tasks.
Create an update_task.html template with a pre-filled form.
Implement a view to save updated data.
🔹 Delete

Add a "Delete" button in task_list.html.
Create a confirmation page (delete_task.html).
Implement a view to remove tasks from the database.
5. URL Configuration
Map URLs to views in urls.py (e.g., /create/, /list/, /update/<id>/, /delete/<id>/).
🧪 Testing Requirements

Ensure all CRUD operations work seamlessly.
Handle edge cases (e.g., invalid form submissions).
💡 Submission Guidelines

Share your GitHub repository link or code files.
Include a README.md with setup instructions.
Showcase screenshots of your working application.
📝 Notes

Use Django’s built-in class-based views (e.g., CreateView, ListView) or function-based views.
Style your templates with CSS/Bootstrap for better UX.
Bonus: Add a filter to sort tasks by due date or completion status.
