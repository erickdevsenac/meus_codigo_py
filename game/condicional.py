import tkinter as tk
from tkinter import messagebox
import random

# Função que cria a lógica do jogo
class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")
        
        # Inicia o número correto aleatório
        self.numero_correto = random.randint(1, 10)
        self.tentativas = 5

        # Adiciona os componentes da interface gráfica
        self.label = tk.Label(self.root, text="Tente adivinhar o número entre 1 e 10!😁", font=("Arial", 14))
        self.label.pack(pady=10)

        self.palpite_label = tk.Label(self.root, text="👀Digite seu palpite: ", font=("Arial", 12))
        self.palpite_label.pack(pady=5)

        self.palpite_entry = tk.Entry(self.root, font=("Arial", 12))
        self.palpite_entry.pack(pady=5)

        self.botao_adivinhar = tk.Button(self.root, text="Adivinhar", font=("Arial", 12), command=self.verificar_palpite)
        self.botao_adivinhar.pack(pady=10)

        self.feedback_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.feedback_label.pack(pady=10)

        self.tentativas_label = tk.Label(self.root, text=f"🤨Tentativas restantes: {self.tentativas}", font=("Arial", 12))
        self.tentativas_label.pack(pady=5)

    def verificar_palpite(self):
        try:
            palpite = int(self.palpite_entry.get())

            if palpite == self.numero_correto:
                self.feedback_label.config(text="😁Parabéns! Você acertou!", fg="green")
                self.finalizar_jogo(True)
            elif palpite < self.numero_correto:
                self.feedback_label.config(text="➕ O número é maior. Tente novamente!", fg="#E97451")
            else:
                self.feedback_label.config(text="➖ O número é menor. Tente novamente!", fg="#E97451")

            self.tentativas -= 1
            self.tentativas_label.config(text=f"😥Tentativas restantes: {self.tentativas}")

            if self.tentativas == 0:
                self.feedback_label.config(text="😒 Fim de jogo! Você não acertou.", fg="red")
                self.finalizar_jogo(False)

        except ValueError:
            messagebox.showerror("Entrada inválida", "Por favor, insira um número válido!")

    def finalizar_jogo(self, venceu):
        if venceu:
            messagebox.showinfo("🎇Vitória", "Você venceu! O número era " + str(self.numero_correto))
        else:
            messagebox.showinfo("😒Fim de jogo", f"O número era {self.numero_correto}. Tente novamente!")

        # Reseta o jogo
        self.numero_correto = random.randint(1, 10)
        self.tentativas = 5
        self.tentativas_label.config(text=f"Tentativas restantes: {self.tentativas}")
        self.feedback_label.config(text="")
        self.palpite_entry.delete(0, tk.END)

# Configura a interface gráfica
def main():
    root = tk.Tk()
    jogo = JogoAdivinhacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()
