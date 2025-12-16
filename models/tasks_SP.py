from playwright.async_api import Page, expect
from pathlib import Path

class TasksPage:
    def __init__(self, page:Page):
        self.page = page

        #Web elements present in Tasks feature
        self.tasks_link=self.page.get_by_role("link", name="Tasks")
        self.create_task_link=self.page.get_by_role("link", name="Create task")
        self.incomplete_btn=self.page.get_by_role("button",name="Incomplete")
        self.complete_btn=self.page.get_by_role("button",name="Completed")

        #Web elements in New Task form
        self.task_name=self.page.get_by_placeholder("Write a task")
        self.description=self.page.get_by_placeholder("Add task description")
        self.date_due=self.page.get_by_placeholder("mm/dd/yy")
        self.save_btn=self.page.get_by_role("button",name="Save")
        self.priority_btn=self.page.get_by_role("button",name="None")
        self.client=self.page.get_by_role("combobox",name="Select client")
        self.team_member=self.page.get_by_role("combobox",name="Add team members")

        #Web elements for Time Picker
        self.time_widget=self.page.locator("div.trigger-module_component__XNiIM")
        self.done_btn=self.page.get_by_role("button",name="Done", exact=True)

        #Web elements related to tasks verification
        self.task_check=self.page.locator("div.checkable-circle")
        self.edit_task_btn=self.page.get_by_label("Edit task")

        #Web element to attach file
        self.attach_btn=self.page.get_by_text("Choose file")


    #Methods for different actions
    #Navigating to Tasks page
    def navigate_to_tasks_page(self):
        self.tasks_link.click()

    #Creating a new task
    def open_new_task_form(self):
        self.create_task_link.click()

    #Select due date in widget calendar
    def select_date(self, day_number:int):
        self.date_due.click()
        self.page.get_by_role("cell",name=str(day_number)).click()

    #Select due hour, minute and AM/PM in widget hour
    def select_time(self, hour:str, minute:str, ampm:str):
        self.time_widget.click()
        self.page.get_by_role("option",name=hour, exact=True).click()
        self.page.get_by_role("option",name=minute, exact=True).click()
        self.page.get_by_role("option",name=ampm, exact=True).click()
        self.done_btn.click()

    #Defining task's priority
    def set_priority(self, priority:str):
        self.priority_btn.click()
        self.page.get_by_role("option",name=priority).click()

    #Defining task's client
    def assign_client(self, client:str):
        self.client.click()
        self.page.get_by_role("option",name=client).click()

    #Defining task's team member
    def assign_team_member(self, team_member:str):
        self.team_member.click()
        self.page.get_by_role("option",name=team_member).click()

    #Creating task
    def create_task(self, title:str, description:str, day_number:int, hour:str, minute:str, ampm:str,priority:str, client:str, team_member:str):
        self.task_name.fill(title)
        self.description.fill(description)
        self.select_date(day_number)
        self.select_time(hour, minute, ampm)
        self.set_priority(priority)
        self.assign_client(client)
        self.assign_team_member(team_member)
        self.save_btn.click()

    #Attaching a file
    def attaching_file(self,file_path:str):
        self.attach_btn.set_input_files(file_path)

    #Marking task created as Completed
    def mark_task_as_complete(self,task:str):
        task_complete=self.task_check.first
        task_complete.click()

    #Looking for all tasks Completed
    def filter_completed_tasks(self):
        self.incomplete_btn.click()
        self.complete_btn.click()

    #Reference for task completed
    def verify_task_complete_details(self, task:str):
        task_in_list=self.page.get_by_text(task).first
        task_in_list.click()