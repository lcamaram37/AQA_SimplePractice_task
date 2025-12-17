import pytest
from models.login_SP import LoginPage
from models.tasks_SP import TasksPage
from playwright.sync_api import Page, expect

#Function that handles fixture task_data
def test_login_and_task_flow(page:Page, task_data):
    #Obtaining login data from fixture
    login_data=task_data["login"]
    task_data=task_data["task"]

    #Setup and login
    login_page=LoginPage(page)
    task_page=TasksPage(page)
    login_page.login(login_data["username"],login_data["password"])

    #Verification of successful login
    page.wait_for_url(f"{login_data['base_url']}/calendar/appointments")
    expect(page).to_have_url(f"{login_data['base_url']}/calendar/appointments")
    page.screenshot(path="SS_LoginOK.jpg")
    print("✅ 1. Successful login.")

    #Creating a new task
    task_page.navigate_to_tasks_page()
    expect(page).to_have_url("https://secure.simplepractice.com/tasks")
    page.wait_for_url("https://secure.simplepractice.com/tasks",timeout=10)
    page.screenshot(path="SS_TasksOK.jpg")
    task_page.open_new_task_form()
    expect(page).to_have_url("https://secure.simplepractice.com/tasks/new")
    page.wait_for_url("https://secure.simplepractice.com/tasks/new",timeout=50)

    task_page.create_task(
        title=task_data["title"],
        description=task_data["description"],
        day_number=task_data["date_day"],
        hour=task_data["time_hour"],
        minute=task_data["time_minute"],
        ampm=task_data["time_ampm"],
        priority=task_data["priority"],
        client=task_data["client_name"],
        team_member=task_data["team_member"]
    )
    page.screenshot(path="SS_NewTaskOK.jpg")
    task_page.attaching_file("CV.pdf")
    print("✅ File attached.")

    expect(page).to_have_url("https://secure.simplepractice.com/tasks/new")
    print("✅ Task created successfully.")

    #Verification point of new task created and visible
    task_page.search_bar.fill(task_data["title"])
    expect(page.get_by_text(task_data["title"]).first).to_be_visible()
    page.screenshot(path="SS_TaskVisible.jpg")
    print("✅ Task is visible in Incomplete list")

    #Complete task
    task_page.mark_task_as_complete(task_data["title"])
    print("✅ Task completed successfully.")

    #Verification point of task marked as completed
    task_page.filter_completed_tasks(task_data["title"])
    expect(page).to_have_url("https://secure.simplepractice.com/tasks?completed=true")
    task_title_locator=page.get_by_text(task_data["title"], exact=True)
    expect(task_title_locator).to_be_visible()
    page.screenshot(path="SS_TaskCompleted.jpg")
    print("✅ Task completed and visible in Complete list.")

    #Verification of task legend
    task_page.verify_task_complete_details(task_data["title"])
    completed_legend = page.locator("p.completed-at")
    expect(completed_legend.first).to_contain_text("Task marked as completed")
    print("✅ Task has legend 'Task marked as complete' visible.")

    print("✅ Flow completed successfully.")