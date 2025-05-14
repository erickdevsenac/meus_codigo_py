import tkinter as tk
from tkinter import ttk, messagebox
from math import radians, sin, cos, sqrt, atan2

class CalculadoraViagem:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Viagem Interestadual e Internacional")
        self.root.geometry("600x500")
        
        # Dados iniciais (coordenadas aproximadas das capitais)
        self.estados = {
            "AC": {"nome": "Acre", "coords": (-9.97, -67.81)},
            "AL": {"nome": "Alagoas", "coords": (-9.67, -35.74)},
            "AM": {"nome": "Amazonas", "coords": (-3.10, -60.02)},
            "AP": {"nome": "Amapá", "coords": (0.03, -51.07)},
            "BA": {"nome": "Bahia", "coords": (-12.97, -38.50)},
            "CE": {"nome": "Ceará", "coords": (-3.73, -38.52)},
            "DF": {"nome": "Distrito Federal", "coords": (-15.79, -47.88)},
            "ES": {"nome": "Espírito Santo", "coords": (-20.32, -40.34)},
            "GO": {"nome": "Goiás", "coords": (-16.68, -49.25)},
            "MA": {"nome": "Maranhão", "coords": (-2.53, -44.30)},
            "MG": {"nome": "Minas Gerais", "coords": (-19.92, -43.94)},
            "MS": {"nome": "Mato Grosso do Sul", "coords": (-20.44, -54.65)},
            "MT": {"nome": "Mato Grosso", "coords": (-15.60, -56.10)},
            "PA": {"nome": "Pará", "coords": (-1.46, -48.50)},
            "PB": {"nome": "Paraíba", "coords": (-7.12, -34.88)},
            "PE": {"nome": "Pernambuco", "coords": (-8.05, -34.90)},
            "PI": {"nome": "Piauí", "coords": (-5.09, -42.80)},
            "PR": {"nome": "Paraná", "coords": (-25.42, -49.25)},
            "RJ": {"nome": "Rio de Janeiro", "coords": (-22.91, -43.20)},
            "RN": {"nome": "Rio Grande do Norte", "coords": (-5.79, -35.21)},
            "RO": {"nome": "Rondônia", "coords": (-8.76, -63.90)},
            "RR": {"nome": "Roraima", "coords": (2.82, -60.67)},
            "RS": {"nome": "Rio Grande do Sul", "coords": (-30.03, -51.23)},
            "SC": {"nome": "Santa Catarina", "coords": (-27.59, -48.55)},
            "SE": {"nome": "Sergipe", "coords": (-10.91, -37.07)},
            "SP": {"nome": "São Paulo", "coords": (-23.55, -46.63)},
            "TO": {"nome": "Tocantins", "coords": (-10.18, -48.33)}
        }
        
        self.paises = {
            "ARG": {"nome": "Argentina", "coords": (-34.60, -58.38)},
            "EUA": {"nome": "Estados Unidos", "coords": (38.90, -77.04)},
            "FRA": {"nome": "França", "coords": (48.86, 2.35)},
            "JPN": {"nome": "Japão", "coords": (35.68, 139.77)},
            "PRT": {"nome": "Portugal", "coords": (38.72, -9.14)}
        }
        
        # Variáveis
        self.origem_var = tk.StringVar()
        self.destino_var = tk.StringVar()
        self.tipo_destino_var = tk.StringVar(value="estado")
        self.velocidade_var = tk.IntVar(value=80)
        self.resultado_var = tk.StringVar()
        self.detalhes_var = tk.StringVar()
        
        # Interface
        self.criar_interface()
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        ttk.Label(main_frame, text="Calculadora de Viagem", 
                 font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Tipo de destino
        ttk.Label(main_frame, text="Tipo de Destino:").grid(row=1, column=0, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text="Estado", variable=self.tipo_destino_var, 
                       value="estado", command=self.atualizar_destinos).grid(row=1, column=1, sticky=tk.W)
        ttk.Radiobutton(main_frame, text="País", variable=self.tipo_destino_var, 
                       value="pais", command=self.atualizar_destinos).grid(row=1, column=2, sticky=tk.W)
        
        # Origem
        ttk.Label(main_frame, text="Origem (Estado Brasileiro):").grid(row=2, column=0, sticky=tk.W, pady=5)
        estados = sorted([f"{sigla} - {dados['nome']}" for sigla, dados in self.estados.items()])
        origem_cb = ttk.Combobox(main_frame, textvariable=self.origem_var, values=estados, state="readonly")
        origem_cb.grid(row=2, column=1, columnspan=2, sticky=tk.EW, pady=5)
        
        # Destino
        ttk.Label(main_frame, text="Destino:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.destino_cb = ttk.Combobox(main_frame, textvariable=self.destino_var, state="readonly")
        self.destino_cb.grid(row=3, column=1, columnspan=2, sticky=tk.EW, pady=5)
        self.atualizar_destinos()
        
        # Velocidade
        ttk.Label(main_frame, text="Velocidade Média (km/h):").grid(row=4, column=0, sticky=tk.W, pady=5)
        ttk.Entry(main_frame, textvariable=self.velocidade_var).grid(row=4, column=1, sticky=tk.EW, pady=5)
        
        # Botão de cálculo
        ttk.Button(main_frame, text="Calcular Viagem", 
                  command=self.calcular_viagem).grid(row=5, column=0, columnspan=3, pady=15)
        
        # Resultado
        ttk.Label(main_frame, text="Resultado:", font=('Helvetica', 10, 'bold')).grid(
            row=6, column=0, sticky=tk.W, pady=5)
        ttk.Label(main_frame, textvariable=self.resultado_var, wraplength=500).grid(
            row=6, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Detalhes do destino
        ttk.Label(main_frame, text="Detalhes do Destino:", font=('Helvetica', 10, 'bold')).grid(
            row=7, column=0, sticky=tk.W, pady=5)
        ttk.Label(main_frame, textvariable=self.detalhes_var, wraplength=500).grid(
            row=7, column=1, columnspan=2, sticky=tk.W, pady=5)
        
        # Configurar expansão
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(6, weight=1)
        main_frame.rowconfigure(7, weight=1)
    
    def atualizar_destinos(self):
        tipo = self.tipo_destino_var.get()
        if tipo == "estado":
            destinos = sorted([f"{sigla} - {dados['nome']}" for sigla, dados in self.estados.items()])
        else:
            destinos = sorted([f"{sigla} - {dados['nome']}" for sigla, dados in self.paises.items()])
        
        self.destino_cb['values'] = destinos
    
    def calcular_distancia(self, coord1, coord2):
        # Fórmula de Haversine para calcular distância entre coordenadas geográficas
        lat1, lon1 = radians(coord1[0]), radians(coord1[1])
        lat2, lon2 = radians(coord2[0]), radians(coord2[1])
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        
        return 6371 * c  # Raio da Terra em km
    
    def formatar_tempo(self, horas):
        if horas >= 24:
            dias = int(horas // 24)
            horas_rest = horas % 24
            return f"{dias} dias e {horas_rest:.1f} horas"
        return f"{horas:.1f} horas"
    
    def calcular_viagem(self):
        origem = self.origem_var.get().split(" - ")[0]
        destino = self.destino_var.get().split(" - ")[0]
        velocidade = self.velocidade_var.get()
        
        if not origem or not destino:
            messagebox.showerror("Erro", "Selecione origem e destino!")
            return
        
        try:
            # Obter coordenadas
            origem_coords = self.estados[origem]["coords"]
            
            if self.tipo_destino_var.get() == "estado":
                destino_coords = self.estados[destino]["coords"]
                destino_nome = self.estados[destino]["nome"]
                tipo_destino = "Estado"
            else:
                destino_coords = self.paises[destino]["coords"]
                destino_nome = self.paises[destino]["nome"]
                tipo_destino = "País"
            
            # Calcular distância
            distancia = self.calcular_distancia(origem_coords, destino_coords)
            horas = distancia / velocidade
            
            # Atualizar resultados
            self.resultado_var.set(
                f"Distância entre {self.estados[origem]['nome']} e {destino_nome}: {distancia:.0f} km\n"
                f"Tempo estimado de viagem ({velocidade} km/h): {self.formatar_tempo(horas)}"
            )
            
            self.detalhes_var.set(
                f"Destino Final: {destino_nome} ({tipo_destino})\n"
                f"Coordenadas: {destino_coords[0]:.2f}° N, {destino_coords[1]:.2f}° W"
            )
            
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraViagem(root)
    root.mainloop()