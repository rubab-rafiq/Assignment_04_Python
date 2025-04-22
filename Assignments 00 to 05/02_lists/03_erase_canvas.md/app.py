# 03_erase_canvas.md
# Import the tkinter module for GUI
import tkinter as tk

# Set canvas size and cell size
CANVAS_WIDTH = 600      # Canvas width is 600 pixels
CANVAS_HEIGHT = 600     # Canvas height is 600 pixels
CELL_SIZE = 50          # Each grid cell will be 50x50 pixels

# Function to create a grid on the canvas
def create_grid(canvas):
    """Create a grid of rectangles on the canvas."""
    cells = []  # Store all the cell rectangles
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):  # Loop over rows
        row_cells = []  # List to store one row of cells
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):  # Loop over columns
            # Draw a blue rectangle (cell) with black border
            rect = canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")
            row_cells.append(rect)  # Add cell to row list
        cells.append(row_cells)  # Add row to main grid
    return cells  # Return full grid

# Function to erase a cell when mouse is clicked or dragged
def erase(event):
    x, y = event.x, event.y  # Get mouse x and y position
    row = y // CELL_SIZE     # Calculate which row was clicked
    col = x // CELL_SIZE     # Calculate which column was clicked

    # Check if click is inside the grid
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        # Change the cell color to white (erase effect)
        canvas.itemconfig(grid[row][col], fill="white")

# Main function to start the app
def main():
    global canvas, grid  # Make canvas and grid accessible in erase function

    # Create the main app window
    root = tk.Tk()
    root.title("Grid Erase Canvas")  # Set window title

    # Create a canvas area with white background
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT , bg="white")
    
    # Bind mouse left click and drag to erase function
    canvas.bind("<Button-1>", erase)      # When mouse is clicked
    canvas.bind("<B1-Motion>", erase)     # When mouse is dragged with button

    canvas.pack()  # Add canvas to the window

    # Draw the grid on the canvas
    grid = create_grid(canvas)

    # Start the event loop (keeps window open and interactive)
    root.mainloop()

# Run the program
if __name__ == "__main__":
    main()
