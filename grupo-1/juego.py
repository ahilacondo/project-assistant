import tkinter as tk
from PIL import Image, ImageTk

class ComputerStructureQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JUEGO: ESTRUCTURA DE UN COMPUTADOR")

        self.question_label = tk.Label(root, text="¿Qué unidad en una computadora controla el flujo de datos y regula el funcionamiento del sistema?")
        self.question_label.pack()

        self.image_frame = tk.Frame(root)
        self.image_frame.pack()

        self.image_labels = []
        for _ in range(3):
            image_label = tk.Label(self.image_frame, image=None)
            image_label.pack(side=tk.LEFT, padx=10)
            image_label.bind("<Button-1>", self.check_answer)
            self.image_labels.append(image_label)

        self.correct_answer = 1  
        self.load_question()

    def load_question(self):
        question = "¿Qué unidad en una computadora controla el flujo de datos y regula el funcionamiento del sistema?"
        self.question_label.config(text=question)

        # Cargar las imágenes
        for i in range(3):
            image_path = f"img/option_{i+1}.png"
            image = Image.open(image_path)
            image = image.resize((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.image_labels[i].config(image=photo)
            self.image_labels[i].image = photo

    def check_answer(self, event):
        clicked_label = event.widget
        clicked_index = self.image_labels.index(clicked_label)

        if clicked_index == self.correct_answer:
            print("Respuesta correcta.")
            #texto_a_audio("Respuesta correcta.")
        else:
            print("Respuesta incorrecta.")
            #texto_a_audio("Respuesta incorrecta.")
        self.load_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = ComputerStructureQuizApp(root)
    root.mainloop()

