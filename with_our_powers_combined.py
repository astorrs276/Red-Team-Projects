import create_file
import schedule_task
import create_registry_autorun

if __name__ == "__main__":
    create_file.create_file()
    create_registry_autorun.add_to_startup()
    schedule_task.schedule_task()