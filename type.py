import pyautogui import time import random import keyboard from pynput.mouse import Controller as MouseController from pynput.keyboard import Controller as KeyboardController import tkinter as tk from threading import Thread

mouse = MouseController() keyboard_controller = KeyboardController()

class AutoTyperGUI: def init(self, master): self.master = master master.title("Human-like AutoTyper")

self.label = tk.Label(master, text="Enter text to type:")
    self.label.pack()

    self.text_entry = tk.Text(master, height=5, width=50)
    self.text_entry.pack()

    self.duration_label = tk.Label(master, text="Typing Duration (seconds):")
    self.duration_label.pack()
    self.duration_entry = tk.Entry(master)
    self.duration_entry.pack()

    self.very_long_break_var = tk.BooleanVar()
    self.very_long_break_check = tk.Checkbutton(master, text="Enable Very Long Breaks", variable=self.very_long_break_var)
    self.very_long_break_check.pack()

    self.start_button = tk.Button(master, text="Start Typing", command=self.start_typing_thread)
    self.start_button.pack()

    self.status_label = tk.Label(master, text="Status: Waiting to start...")
    self.status_label.pack()

    self.active_time_label = tk.Label(master, text="Active Typing Time: 0.00 seconds")
    self.active_time_label.pack()

    self.active_time = 0

def update_active_time(self):
    self.active_time_label.config(text=f"Active Typing Time: {self.active_time:.2f} seconds")

def start_typing_thread(self):
    t = Thread(target=self.run_autotyper)
    t.daemon = True
    t.start()

def run_autotyper(self):
    text_to_type = self.text_entry.get("1.0", tk.END).strip()
    try:
        typing_duration = float(self.duration_entry.get())
    except:
        self.status_label.config(text="Invalid duration entered.")
        return

    ask_very_long = self.very_long_break_var.get()
    self.status_label.config(text="Typing will start in 5 seconds... Switch to input field!")
    time.sleep(5)
    auto_typer(text_to_type, typing_duration, ask_for_very_long=ask_very_long, gui=self)
    self.status_label.config(text="Typing completed.")

def simulate_mouse_movement(): try: x, y = pyautogui.position() dx = random.randint(-50, 50) dy = random.randint(-50, 50) mouse.move(dx, dy) except: pass

def simulate_navigation(): if random.random() < 0.1: key = random.choice(["up", "down"]) for _ in range(random.randint(1, 3)): pyautogui.press(key) time.sleep(0.1)

def simulate_typing_with_errors(text): result = [] for word in text.split(): if random.random() < 0.1: typo_index = random.randint(0, len(word)-1) typo_char = random.choice('abcdefghijklmnopqrstuvwxyz') word = word[:typo_index] + typo_char + word[typo_index + 1:] result.append(word) result.append("<BACKSPACE>" * len(word)) result.append(word.replace(typo_char, '')) else: result.append(word) return ' '.join(result)

def auto_typer(text, typing_duration, min_delay=0.05, max_delay=0.2, very_short_break_time=(1, 3), short_break_time=(34, 101), long_break_time=(1620, 7020), very_long_break_time=(15480, 25920), ask_for_very_long=True, gui=None):

def get_next_break(min_active, max_active, offset):
    return active_time + random.uniform(min_active, max_active) + random.uniform(-offset, offset)

active_time = 0
last_very_short = -float('inf')
last_short = -float('inf')
last_long = -float('inf')
last_very_long = -float('inf')

next_very_short_break = get_next_break(3, 7, 1)
next_short_break = get_next_break(120, 420, 10)
next_long_break = get_next_break(5400, 8280, 60)
next_very_long_break = get_next_break(15120, 23040, 120)

words = simulate_typing_with_errors(text).split()

while active_time < typing_duration:
    for word in words:
        if keyboard.is_pressed('pause'):
            print("\nTyping paused...")
            return

        for char in word + ' ':
            if "<BACKSPACE>" in char:
                keyboard_controller.press("\b")
                keyboard_controller.release("\b")
                time.sleep(0.05)
                continue
            char_start_time = time.time()
            pyautogui.write(char)
            time.sleep(random.uniform(min_delay, max_delay))
            elapsed = time.time() - char_start_time
            active_time += elapsed

            if gui:
                gui.active_time = active_time
                gui.update_active_time()

            if random.random() < 0.005:
                think_time = random.uniform(1.5, 5.5)
                print(f"\nThinking for {think_time:.2f} seconds...")
                time.sleep(think_time)

            if random.random() < 0.01:
                simulate_mouse_movement()

            if random.random() < 0.05:
                simulate_navigation()

            if active_time >= next_very_short_break and active_time - last_very_short >= 5:
                sleep_time = random.uniform(*very_short_break_time)
                print(f"\nTaking a very short break for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
                last_very_short = active_time
                next_very_short_break = get_next_break(3, 7, 1)

            if active_time >= next_short_break and active_time - last_short >= 300:
                sleep_time = random.uniform(*short_break_time)
                print(f"\nTaking a short break for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
                last_short = active_time
                next_short_break = get_next_break(120, 420, 10)

            if active_time >= next_long_break and active_time - last_long >= 3600:
                sleep_time = random.uniform(*long_break_time)
                print(f"\nTaking a long break for {sleep_time/60:.2f} minutes...")
                time.sleep(sleep_time)
                last_long = active_time
                next_long_break = get_next_break(5400, 8280, 60)

            if ask_for_very_long and active_time >= next_very_long_break and active_time - last_very_long >= 14400:
                response = input("\nDo you want to take a very long break now? (y/n): ").strip().lower()
                if response == 'y':
                    sleep_time = random.uniform(*very_long_break_time)
                    print(f"Taking a very long break for {sleep_time/3600:.2f} hours...")
                    time.sleep(sleep_time)
                    last_very_long = active_time
                    next_very_long_break = get_next_break(15120, 23040, 120)
                else:
                    next_very_long_break = get_next_break(15120, 23040, 120)

            if active_time >= typing_duration:
                print("\nTyping completed for the specified duration.")
                return

if name == "main": root = tk.Tk() gui = AutoTyperGUI(root) root.mainloop()

