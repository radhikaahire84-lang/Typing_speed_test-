import tkinter as tk
import random
import time

sentences = [
    "Typing speed is measured in words per minute.",
    "Python is a simpl programming language.",
    "Practice makes a person perfect in typing.",
    "Tkinter makes GUI development simple and fast.",
    "Artificial Intelligence is shaping the future."
]

start_time = 0
selected_sentence = ""

def start_test():
    global start_time, selected_sentence
    selected_sentence = random.choice(sentences)
    sentence_label.config(text=selected_sentence)
    entry.delete(0, tk.END)
    result_label.config(text="")
    start_time = time.time()

def check_speed():
    end_time = time.time()
    typed_text = entry.get()
    time_taken = end_time - start_time

    if typed_text.strip() == "":
        result_label.config(text="Please type something!")
        return

    word_count = len(typed_text.strip().split())
    wpm = round((word_count / time_taken) * 60)

    if typed_text.strip() == selected_sentence:
        result = f"Correct! Your typing speed is {wpm} WPM."
    else:
        result = f"Incorrect! You typed {wpm} WPM."

    result_label.config(text=result)

root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x300")
root.config(bg="white")


instruction = tk.Label(root, text="Click 'Start Test' and type the sentence as fast as you can.", bg="white")
instruction.pack(pady=10)

sentence_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, bg="white")
sentence_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=70)
entry.pack(pady=10)

start_btn = tk.Button(root, text="Start Test", command=start_test, bg="#4CAF50", fg="white")
start_btn.pack(pady=5)

check_btn = tk.Button(root, text="Check Speed", command=check_speed, bg="#2196F3", fg="white")
check_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="black", bg="white")
result_label.pack(pady=10)

root.mainloop()