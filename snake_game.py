import tkinter as tk
import random

WIDTH, HEIGHT = 400, 400
SEG_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game v1.0")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"
        self.food = self.create_food()
        self.running = True

        self.root.bind("<KeyPress>", self.change_direction)
        self.update()

    def create_food(self):
        while True:
            x = random.randint(0, (WIDTH - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT - SEG_SIZE) // SEG_SIZE) * SEG_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def change_direction(self, event):
        key = event.keysym
        opposites = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key in opposites and opposites[key] != self.direction:
            self.direction = key

    def update(self):
        if not self.running:
            return

        head_x, head_y = self.snake[0]
        if self.direction == "Up": head_y -= SEG_SIZE
        elif self.direction == "Down": head_y += SEG_SIZE
        elif self.direction == "Left": head_x -= SEG_SIZE
        elif self.direction == "Right": head_x += SEG_SIZE

        new_head = (head_x, head_y)

        if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or new_head in self.snake):
            self.running = False
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="white", font=("Arial", 24))
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.draw()
        self.root.after(150, self.update)

    def draw(self):
        self.canvas.delete("all")
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx + SEG_SIZE, fy + SEG_SIZE, fill="red")
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + SEG_SIZE, y + SEG_SIZE, fill="green")

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()