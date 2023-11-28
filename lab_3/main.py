import tkinter as tk

class RasterizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Растеризация: Отрезки и Окружности")
        self.root.resizable(False, False)  # Запрещаем изменение размера окна

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.pack()

        self.draw_axes_and_grid()

        # Примеры вызова растеризации
        self.draw_line(50, 50, 200, 200, "blue")
        self.draw_line_bresenham(50, 100, 200, 250, "green")
        self.draw_circle_bresenham(400, 150, 50, "red")

        # Добавляем возможность перемещения графика с помощью мыши
        self.canvas.bind("<B1-Motion>", self.drag)
        self.canvas.bind("<ButtonPress-1>", self.on_click)

        # Кнопки для масштабирования
        plus_button = tk.Button(root, text="+", command=self.zoom_in)
        plus_button.pack(side=tk.LEFT)
        minus_button = tk.Button(root, text="-", command=self.zoom_out)
        minus_button.pack(side=tk.LEFT)

        # Начальные координаты клика мыши
        self.start_x = 0
        self.start_y = 0

    def draw_axes_and_grid(self):
        for i in range(0, 600, 20):
            self.canvas.create_line(i, 0, i, 600, fill="lightgray")
            self.canvas.create_line(0, i, 600, i, fill="lightgray")

        self.canvas.create_line(300, 0, 300, 600, width=2)
        self.canvas.create_line(0, 300, 600, 300, width=2)

        # Подписываем оси
        self.canvas.create_text(310, 10, text="Y", anchor=tk.W)
        self.canvas.create_text(590, 310, text="X", anchor=tk.W)

        # Добавляем метки на осях
        for i in range(-15, 16):
            if i != 0:
                self.canvas.create_text(300 + i * 20, 310, text=str(i), anchor=tk.N)

            self.canvas.create_text(310, 300 - i * 20, text=str(i), anchor=tk.W)

    def draw_line(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))

        x_increment = dx / steps
        y_increment = dy / steps

        x, y = x1, y1
        for _ in range(steps + 1):
            print(f"Drawing rectangle at ({x}, {y}) with color {color}")
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color)
            x += x_increment
            y += y_increment

    def draw_line_bresenham(self, x1, y1, x2, y2, color):
        dx = x2 - x1
        dy = y2 - y1

        x, y = x1, y1
        d = 2 * dy - dx
        for _ in range(dx + 1):
            print(f"Drawing line (Bresenham) at ({x}, {y}) with color {color}")
            self.canvas.create_rectangle(x, y, x + 2, y + 2, fill=color)
            if d >= 0:
                y += 1
                d -= 2 * dx
            x += 1
            d += 2 * dy

    def draw_circle_bresenham(self, xc, yc, r, color):
        x = 0
        y = r
        d = 3 - 2 * r

        while x <= y:
            self.draw_circle_points(xc, yc, x, y, color)
            x += 1
            if d > 0:
                y -= 1
                d = d + 4 * (x - y) + 10
            else:
                d = d + 4 * x + 6
            self.draw_circle_points(xc, yc, x, y, color)

    def draw_circle_points(self, xc, yc, x, y, color):
        print(f"Drawing circle point at ({xc + x}, {yc + y}) with color {color}")
        self.canvas.create_rectangle(xc + x, yc + y, xc + x + 2, yc + y + 2, fill=color)
        print(f"Drawing circle point at ({xc - x}, {yc + y}) with color {color}")
        self.canvas.create_rectangle(xc - x, yc + y, xc - x + 2, yc + y + 2, fill=color)
        print(f"Drawing circle point at ({xc + x}, {yc - y}) with color {color}")
        self.canvas.create_rectangle(xc + x, yc - y, xc + x + 2, yc - y + 2, fill=color)
        print(f"Drawing circle point at ({xc - x}, {yc - y}) with color {color}")
        self.canvas.create_rectangle(xc - x, yc - y, xc - x + 2, yc - y + 2, fill=color)
        print(f"Drawing circle point at ({xc + y}, {yc + x}) with color {color}")
        self.canvas.create_rectangle(xc + y, yc + x, xc + y + 2, yc + x + 2, fill=color)
        print(f"Drawing circle point at ({xc - y}, {yc + x}) with color {color}")
        self.canvas.create_rectangle(xc - y, yc + x, xc - y + 2, yc + x + 2, fill=color)
        print(f"Drawing circle point at ({xc + y}, {yc - x}) with color {color}")
        self.canvas.create_rectangle(xc + y, yc - x, xc + y + 2, yc - x + 2, fill=color)
        print(f"Drawing circle point at ({xc - y}, {yc - x}) with color {color}")
        self.canvas.create_rectangle(xc - y, yc - x, xc - y + 2, yc - x + 2, fill=color)

    def zoom_in(self):
        self.canvas.scale(tk.ALL, 300, 300, 1.1, 1.1)

    def zoom_out(self):
        self.canvas.scale(tk.ALL, 300, 300, 0.9, 0.9)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def drag(self, event):
        dx = event.x - self.start_x
        dy = event.y - self.start_y
        self.canvas.move(tk.ALL, dx, dy)
        self.start_x = event.x
        self.start_y = event.y


if __name__ == "__main__":
    root = tk.Tk()
    app = RasterizationApp(root)
    root.mainloop()
