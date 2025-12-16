TASKS FEATURE
1. Create Task:
            - Add Task name (verify max length of characters available)
            - Add a Description
            - Select due date and due time
            - Select priority
            - Select client
            - Select assigned to (add and remove)
            - Load attachment (test max capacity(# of files and MB capacity))
            - Save 
            * Consider only one field to fill and save the task
            * Fill all the fields available and save the task
            * If any error present during task creation, verify the presence of Error or Warning message

2. Verify Task creation:
                     - Search task with name used for previous task
                     - Select 'All' from dropdown menu and verify task presence
                     - Select 'Incomplete' from dropdown menu and verify task presence
                     - Select 'Complete' from dropdown meny and verify task absence 

3. Verify correct task assignment:
                                  - If while creation the task was assigned to any team member, verify its presence in "Assigned to" correspondent team member
                                  - If while creation the task was not assigned to any member, verify presence in "Assigned to all" and "Assigned to you"
                                  - If while creation the task was assigned to multiple team members, verify its presence for all the involved

4. Custom view:
                - Test distribution according to selected view
                - When due date: verify that current tasks are in order according to their due date
                - When date created: verify the oldest tasks present at the top
                - When Priority is selected: verify more severe tasks are listed at the top (from critical to low)

5. Creation of quick task:
                          - For the name, write any character, don't leave blank the name as quick task won't be created
                          - Click on quick task and modify one or all fields, save it, verify the presence
                          - Save a quick task with a given priority, set the view as 'Priority' and verify the presence, change the priority and verify it's correctly modified

6. Complete task: - Complete task created amd verify the presence in Completed option view and absence in Incompleted option view
                  - Select Completed option view and then the Completed date view to sort them and the task should be at the top
                  - Click on this to verify the legend that specifies that task was completed on given date by given user

7. Uncheck task complete: - Task should not longer be available in Completed tasks, it should be back in Incompleted and available to modify

8. Delete the task: - Task should not be present considering all the options