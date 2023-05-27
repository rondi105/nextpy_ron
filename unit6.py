import tkinter as tk
from gtts import gTTS
import os
def read_aloud(sentence):
    tts = gTTS(text=sentence, lang='en')
    tts.save('output.mp3')
    os.system('output.mp3')

def create_window():
    def show_image():
        image_label.config(image=image)
        image_label.image = image

    window = tk.Tk()
    window.title("window")

    # Create the question label with custom font size and color
    question_label = tk.Label(window, text="What is your favorite video?", font=("Arial", 16), fg="pink")
    question_label.pack()

    button = tk.Button(window, text="Show Image", command=show_image)
    button.pack()

    image = tk.PhotoImage(file="sirton.png")
    image_label = tk.Label(window)
    image_label.pack()

    window.mainloop()


def main():
    create_window()
    read_aloud("first time i'm using a package in next.py course")

if __name__ == '__main__':
    main()
