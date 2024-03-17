from tkinter import *
from uniform_cost_search import uniform_cost_search,stack,graph
def on_button_click(button_text):
    # user input of start node and to be searched node
    global stack
    stack = []
    start_value = int(start_entry_var.get())
    end_value = int(end_entry_var.get())

    if button_text == "Uniform_Cost Search":
        if not graph:
            print("Error: Graph is not built yet. Please submit the graph first.")
            return

        result = uniform_cost_search(graph, start_value, end_value, stack)
        if result:
            print(f"Uniform_Cost Search: {start_value} to {end_value} is found with distance {result}.")
        else:
            print(f"Uniform_Cost Search: {start_value} is not found.")

def build_graph_with_weight():
    vertex = value.get()
    neighbors_with_weights = value_neighbour.get().split() if value_neighbour.get() else []

    neighbors = {}
    for neighbor_with_weight in neighbors_with_weights:
        neighbor, weight = neighbor_with_weight.split(':')
        neighbors[int(neighbor)] = int(weight)

    graph[int(vertex)] = neighbors
    print(f"Vertex {vertex} with neighbors {neighbors} added to the graph")

# Initialize graph
graph = {}

root = Tk()
root.geometry("666x555")
root.minsize(200, 100)
root.maxsize(2000, 1000)
root.title("GUI for Uniformed Search")

# Entry for vertex value
vertex_label = Label(root, text="Enter vertex value")
vertex_label.grid(row=0, column=0)
value = StringVar()
value_entry = Entry(root, textvariable=value)
value_entry.grid(row=0, column=1)

# Entry for neighbor values
neighbors_label = Label(root, text="Enter neighbor values with weights (format:neighbor:weight  neighbor:weight ...)")
neighbors_label.grid(row=1, column=0)
value_neighbour = StringVar()
value_entry_n = Entry(root, textvariable=value_neighbour)
value_entry_n.grid(row=1, column=1)

# Button to submit
submit_button = Button(root,bg="pink", fg="black", text="Submit", command=build_graph_with_weight)
submit_button.grid(row=3, column=0, columnspan=2)

start_label = Label(text="Enter the start value:")
start_label.grid()
start_entry_var= StringVar()
start_entry = Entry(root, textvariable=start_entry_var)  # Corrected this line to use search_entry
start_entry.grid()

end_label = Label(text="Enter the end value:")
end_label.grid()
end_entry_var = StringVar()
end_entry = Entry(root, textvariable=end_entry_var)  # Corrected this line to use search_entry
end_entry.grid() 

ufs_button = Button(root,bg="pink", fg="black", text="Uniform_Cost Search", command=lambda: on_button_click("Uniform_Cost Search"))
ufs_button.grid(row=8, column=0, columnspan=2)

# Create a label to display the result

root.mainloop()
