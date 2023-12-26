import streamlit as st
import Functions

todos = Functions.get_data()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    Functions.put_data(todos)


st.title("My To-Do App")
st.subheader("This app is to increase your Productivity")
st.write("List of Todos:")


for index, todo in enumerate(todos):
    checked_key = f"checked_{index}"
    checked = st.checkbox(todo, key=checked_key)
    if checked:
        complete = st.checkbox("Complete", key="complete")
        edit = st.checkbox("Edit", key="edit")
        if complete:
            todos.pop(index)
            Functions.put_data(todos)
            del st.session_state[checked_key]
            st.rerun()
        elif edit:
            st.text_input(label="",placeholder="Edit here..", key=f"edit_todo{index}", value=todo)
            edited_todo = st.session_state[f"edit_todo{index}"]
            todos[index] = edited_todo + "\n"
            Functions.put_data(todos)
            st.rerun()

st.text_input(label="", placeholder="Add a todo here..",
              on_change=add_todo, key="new_todo")
