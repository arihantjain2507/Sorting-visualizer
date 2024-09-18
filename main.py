import tkinter as tk
import random
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.canvas = tk.Canvas(root, width=800, height=400)
        self.canvas.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.generate_button = tk.Button(self.button_frame, text="Generate Random List", command=self.generate_random_list)
        self.generate_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.sort_button = tk.Button(self.button_frame, text="Sort", command=self.start_sorting)
        self.sort_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.algorithm_var = tk.StringVar()
        algorithms = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Selection Sort"]
        self.algorithm_dropdown = tk.OptionMenu(root, self.algorithm_var, *algorithms)
        self.algorithm_var.set("Bubble Sort")
        self.algorithm_dropdown.pack(pady=10)

        self.animation_speed_scale = tk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, label="Animation Speed")
        self.animation_speed_scale.pack()

        self.list = []
        self.rectangles = []

    def generate_random_list(self):
        self.list = [random.randint(10, 300) for _ in range(50)]  # Adjust the range and size as needed
        self.draw_rectangles()

    def draw_rectangles(self):
        self.canvas.delete("all")
        self.rectangles = []
        width = 800 / len(self.list)
        for i, num in enumerate(self.list):
            height = num
            x0 = i * width
            y0 = 400 - height
            x1 = (i + 1) * width
            y1 = 400
            rectangle = self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            self.rectangles.append(rectangle)

    def start_sorting(self):
        algorithm = self.algorithm_var.get()
        speed = 1 / self.animation_speed_scale.get()  # Inverse speed for smoother animation

        if algorithm == "Bubble Sort":
            self.bubble_sort(self.list, speed)
        elif algorithm == "Insertion Sort":
            self.insertion_sort(self.list, speed)
        elif algorithm == "Merge Sort":
            self.merge_sort(self.list, speed)
        elif algorithm == "Quick Sort":
            self.quick_sort(self.list, 0, len(self.list) - 1, speed)
        elif algorithm == "Selection Sort":
            self.selection_sort(self.list, speed)

    def bubble_sort(self, arr, speed):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    self.update_visualization()
                    time.sleep(speed)

    def insertion_sort(self, arr, speed):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
                self.update_visualization()
                time.sleep(speed)
            arr[j + 1] = key
            self.update_visualization()
            time.sleep(speed)

    def merge_sort(self, arr, speed):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half, speed)
            self.merge_sort(right_half, speed)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1
                self.update_visualization()
                time.sleep(speed)

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1
                self.update_visualization()
                time.sleep(speed)

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1
                self.update_visualization()
                time.sleep(speed)

    def quick_sort(self, arr, low, high, speed):
        if low < high:
            pi = self.partition(arr, low, high, speed)
            self.quick_sort(arr, low, pi - 1, speed)
            self.quick_sort(arr, pi + 1, high, speed)

    def partition(self, arr, low, high, speed):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.update_visualization()
                time.sleep(speed)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.update_visualization()
        time.sleep(speed)
        return i + 1

    def selection_sort(self, arr, speed):
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
                self.update_visualization()
                time.sleep(speed)
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.update_visualization()
            time.sleep(speed)

    def update_visualization(self):
        self.canvas.delete("all")
        width = 800 / len(self.list)
        for i, num in enumerate(self.list):
            height = num
            x0 = i * width
            y0 = 400 - height
            x1 = (i + 1) * width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="sky blue")
        self.root.update()
        time.sleep(0.01)

if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizer(root)
    root.mainloop()
