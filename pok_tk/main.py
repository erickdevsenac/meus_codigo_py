import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk  # Certifique-se de instalar: pip install pillow

def buscar_pokemon():
    nome_pokemon = entrada_nome.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{nome_pokemon}"
    resultado_texto.delete(1.0, tk.END)  # Limpa o texto anterior
    imagem_label.config(image='')  # Limpa a imagem anterior
    imagem_label.image = None

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        nome = dados.get("name", "Nome não encontrado").capitalize()
        id_pokemon = dados.get("id", "ID não encontrado")
        tipos = [t["type"]["name"].capitalize() for t in dados.get("types", [])]
        habilidades = [h["ability"]["name"].capitalize() for h in dados.get("abilities", [])]
        peso = dados.get("weight", "Peso não encontrado") / 10.0  # Converter para kg
        altura = dados.get("height", "Altura não encontrada") / 10.0 # Converter para metros
        imagem_url = dados["sprites"]["front_default"]

        texto_exibicao = f"Nome: {nome}\n"
        texto_exibicao += f"ID: {id_pokemon}\n"
        texto_exibicao += f"Tipos: {', '.join(tipos)}\n"
        texto_exibicao += f"Habilidades: {', '.join(habilidades)}\n"
        texto_exibicao += f"Peso: {peso} kg\n"
        texto_exibicao += f"Altura: {altura} m\n"

        resultado_texto.insert(tk.END, texto_exibicao)

        # Buscar e exibir a imagem
        try:
            imagem_resposta = requests.get(imagem_url)
            imagem_resposta.raise_for_status()
            imagem_data = imagem_resposta.content
            imagem = Image.open(BytesIO(imagem_data))
            imagem_tk = ImageTk.PhotoImage(imagem)
            imagem_label.config(image=imagem_tk)
            imagem_label.image = imagem_tk  # Manter uma referência!

        except requests.exceptions.RequestException as e:
            resultado_texto.insert(tk.END, f"\nErro ao buscar imagem: {e}")
        except Exception as e:
             resultado_texto.insert(tk.END, f"\nErro ao exibir imagem: {e}")


    except requests.exceptions.RequestException as e:
        resultado_texto.insert(tk.END, f"Erro ao buscar Pokémon: {e}")
    except ValueError:
        resultado_texto.insert(tk.END, "Erro: Resposta da API não é um JSON válido.")
    except KeyError:
        resultado_texto.insert(tk.END, f"Erro: Pokémon '{entrada_nome.get()}' não encontrado.")

janela = tk.Tk()
janela.title("Pokedex Simples")

label_nome = tk.Label(janela, text="Nome do Pokémon:")
label_nome.pack(padx=10, pady=5)

entrada_nome = tk.Entry(janela, width=30)
entrada_nome.pack(padx=10, pady=5)

botao_buscar = tk.Button(janela, text="Buscar", command=buscar_pokemon)
botao_buscar.pack(padx=10, pady=10)

resultado_texto = tk.Text(janela, height=10, width=40)
resultado_texto.pack(padx=10, pady=10)

imagem_label = tk.Label(janela)
imagem_label.pack(padx=10, pady=10)

janela.mainloop()