from pyscript import document, when
from pyodide.ffi.wrappers import add_event_listener

#Shows modals

#Import objects
modalBackground = document.querySelector("#modal-background")
projects = document.querySelectorAll(".project")
project_modals = document.querySelectorAll(".modal-project")

@when("click", "#modal-background")
def hide_modal():
    modalBackground.style.backgroundColor = "rgba(0,0,0,0)"
    modalBackground.style.zIndex = "-1"
    for modal in project_modals:
        modal.style.display = "none"

def show_modal(event):
    #project arg formatted as project-[Project]
    modalBackground.style.zIndex = "1"
    modalBackground.style.backgroundColor = "rgba(0,0,0,0.5)"
    shown_project = document.querySelector("#modal_"+ event.currentTarget.id)
    shown_project.style.display = "grid"

for p in projects:
    add_event_listener(p, "click", show_modal)

