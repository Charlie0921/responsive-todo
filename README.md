# Responsive TodoList (without framework)

## Background
- During my time as a manager in the Airforce, responsible for monitoring flight schedules and managing munitions, I needed a reliable application to keep track of upcoming tasks.
- This project was created to fulfill that need by providing an easy-to-use task management tool.

## What it Does
- Allows users to create, edit, and store tasks with deadlines and categories.
- Displays the number of days left until each task’s deadline, helping users plan ahead effectively.
- Fully responsive design ensures compatibility across various devices, including phones and desktops.

## Challenges
- Building all functionality from scratch without using common libraries such as React meant manually creating UI components and managing state.
- Making schedules editable required dynamic modification capabilities:
  - Automatically inserting the task name into input fields for editing.
  - Using reusable form elements for multiple edits.

## Resolution
- Separated the editing functionality into modular parts for easier management and code clarity.
- Used `setAttribute` to update element values dynamically after changes.
- Employed `querySelector` with class selectors to accurately extract and manipulate original task information.

## Accomplishments
- Successfully built a practical application that contributed to operational efficiency in the Airforce.
- Responsiveness allowed me to access and update tasks from any device without limitation.

## What We Learned
- Building UI components manually reinforced the importance of understanding core web technologies and how modern frameworks abstract these complexities.
- Future plans include connecting to a back-end database to persist tasks securely and reliably.
