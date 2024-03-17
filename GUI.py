from tkinter import *
from dfs import dfs, visited, stack  # Make sure to import dfs, visited, and stack from the correct module
from collections import deque
from bfs import bfs 
import random
from random_search import random_search
from search_with_open_list import search_with_open_list
from search_with_closed_list import search_with_closed_list

def on_button_click(button_text):
    # Get the input values
    graph_input = {}
    lines = graph_entry.get("1.0", END).split("\n")  # Split input by lines
    for line in lines:
        if not line.strip():  # Skip empty lines
            continue
        parts = line.split(":")
        if len(parts) < 2:
            continue  # Skip lines that don't have the expected format
        vertex = int(parts[0].strip())
        neighbors = [int(node.strip()) for node in parts[1].split()]
        graph_input[vertex] = neighbors

    initial_node = int(initial_node_entry.get())
    target_node = int(target_node_entry.get())
    search_value = int(search_entry.get())

    # Call the search function based on the button clicked
    if button_text == "Random Search":
        result, path = random_search(graph_input, initial_node, target_node)
        display_result(result, path)
    elif button_text == "Search With Open List":
        result, path = search_with_open_list(graph_input, initial_node, target_node)
        display_result(result, path)
    elif button_text == "Search With Closed List":
        result, path = search_with_closed_list(graph_input, initial_node, target_node)
        display_result(result, path)
    elif button_text == "Depth First Search":
        result = dfs(search_value, visited, stack, graph_input)
        display_dfs_bfs_result(result,search_value)
    elif button_text == "Breadth First Search":
        result = bfs(search_value, graph_input)
        display_dfs_bfs_result(result,search_value)
    
    
    # Add more conditions for other search methods if needed...
def display_result(result, path):
    if result:
        result_label.config(text=f"Success! Path: {path}")
    else:
        result_label.config(text="Target node not reachable from the initial node.")

def display_dfs_bfs_result(result,search_value):
    if result:
        result_dfs_bfs_label.config(text=f"Value {search_value} found ")
    else:
        result_dfs_bfs_label.config(text=f" {search_value}  Not Found")
    
# Initialize Tkinter
root = Tk()
root.title("Search with Open List")
root.geometry("400x400")

# Create input fields
graph_label = Label(root, text="Enter graph (in the specified format):")
graph_label.pack()
graph_entry = Text(root, height=9, width=30)
graph_entry.pack()

initial_node_label = Label(root, text="Enter initial node:")
initial_node_label.pack()
initial_node_entry = Entry(root)
initial_node_entry.pack()

target_node_label = Label(root, text="Enter target node:")
target_node_label.pack()
target_node_entry = Entry(root)
target_node_entry.pack()

# Create buttons for different search methods
random_search_button = Button(root, text="Random Search", command=lambda: on_button_click("Random Search"))
random_search_button.pack()

search_with_open_list_button = Button(root, text="Search With Open List", command=lambda: on_button_click("Search With Open List"))
search_with_open_list_button.pack()

search_with_closed_list_button = Button(root, text="Search With Closed List", command=lambda: on_button_click("Search With Closed List"))
search_with_closed_list_button.pack()

# Label to display the result
result_label = Label(root, text="")
result_label.pack()



search_label = Label(root, text="Enter search value:")
search_label.pack()
search_entry = Entry(root)
search_entry.pack()

dfs_button = Button(root, text="Depth First Search", command=lambda: on_button_click("Depth First Search"))
dfs_button.pack()

bfs_button = Button(root, text="Breadth First Search", command=lambda: on_button_click("Breadth First Search"))
bfs_button.pack()

result_dfs_bfs_label = Label(root, text="")
result_dfs_bfs_label.pack()

# Run the Tkinter event loop
root.mainloop()
