import tkinter as tk
from tkinter import messagebox
import json
import os
import openpyxl

# ---------- CONFIGURAÇÕES ----------
CONFIG_FILE = "config.json"
PLANILHA = "relatorio_impressoes.xlsx"

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"pla_kg": 65.0, "energia_kwh": 1.10, "consumo_watts": 120}

def salvar_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

config = carregar_config()

# ---------- CÁLCULO ----------
def calcular():
    try:
        peso = float(entry_peso.get())
        tempo = float(entry_tempo.get())
        preco = float(entry_preco.get())

        custo_pla = (peso / 1000) * config["pla_kg"]
        custo_energia = (config["consumo_watts"] * tempo / 1000) * config["energia_kwh"]
        custo_total = custo_pla + custo_energia
        lucro_reais = preco - custo_total
        lucro_percent = (lucro_reais / custo_total) * 100 if custo_total > 0 else 0
        qtd_possivel = 1000 / peso if peso > 0 else 0

        resultado.set(
            f"Custo PLA: R$ {custo_pla:.2f}\n"
            f"Custo Energia: R$ {custo_energia:.2f}\n"
            f"Custo Total: R$ {custo_total:.2f}\n"
            f"Lucro: R$ {lucro_reais:.2f} ({lucro_percent:.1f}%)\n"
            f"Autonomia: ~{qtd_possivel:.1f} peças por 1kg"
        )
        return custo_pla, custo_energia, custo_total, lucro_reais, lucro_percent
    except ValueError:
        messagebox.showerror("Erro", "Preencha todos os campos corretamente.")
        return None

# ---------- SALVAR PLANILHA ----------
def salvar_planilha():
    dados = calcular()
    if not dados: return
    nome = entry_nome.get()
    if not nome:
        messagebox.showwarning("Aviso", "Digite o nome do produto.")
        return

    if not os.path.exists(PLANILHA):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append([
            "Produto", "PLA (g)", "Tempo (h)", "Custo PLA", "Custo Energia",
            "Custo Total", "Preço", "Lucro R$", "Lucro %"
        ])
        wb.save(PLANILHA)

    wb = openpyxl.load_workbook(PLANILHA)
    ws = wb.active
    custo_pla, custo_energia, custo_total, lucro_r, lucro_p = dados

    ws.append([
        nome,
        float(entry_peso.get()),
        float(entry_tempo.get()),
        round(custo_pla, 2),
        round(custo_energia, 2),
        round(custo_total, 2),
        float(entry_preco.get()),
        round(lucro_r, 2),
        round(lucro_p, 1)
    ])
    wb.save(PLANILHA)
    messagebox.showinfo("Salvo", "Dados registrados com sucesso.")

# ---------- GUI ----------
janela = tk.Tk()
janela.title("Calculadora STL")

tk.Label(janela, text="Nome do Produto").grid(row=0, column=0, sticky='w')
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

tk.Label(janela, text="PLA usado (g)").grid(row=1, column=0, sticky='w')
entry_peso = tk.Entry(janela)
entry_peso.grid(row=1, column=1)

tk.Label(janela, text="Tempo (h)").grid(row=2, column=0, sticky='w')
entry_tempo = tk.Entry(janela)
entry_tempo.grid(row=2, column=1)

tk.Label(janela, text="Preço cobrado (R$)").grid(row=3, column=0, sticky='w')
entry_preco = tk.Entry(janela)
entry_preco.grid(row=3, column=1)

resultado = tk.StringVar()
tk.Label(janela, textvariable=resultado, justify='left', font=("Arial", 10, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(janela, text="Calcular", command=calcular).grid(row=4, column=0)
tk.Button(janela, text="Salvar na planilha", command=salvar_planilha).grid(row=4, column=1)

# Configurações editáveis
tk.Label(janela, text="PLA R$/kg").grid(row=6, column=0, sticky='w')
entry_pla = tk.Entry(janela)
entry_pla.insert(0, str(config["pla_kg"]))
entry_pla.grid(row=6, column=1)

tk.Label(janela, text="Energia R$/kWh").grid(row=7, column=0, sticky='w')
entry_energia = tk.Entry(janela)
entry_energia.insert(0, str(config["energia_kwh"]))
entry_energia.grid(row=7, column=1)

tk.Label(janela, text="Consumo da impressora (W)").grid(row=8, column=0, sticky='w')
entry_watts = tk.Entry(janela)
entry_watts.insert(0, str(config["consumo_watts"]))
entry_watts.grid(row=8, column=1)

def salvar_config_gui():
    try:
        config["pla_kg"] = float(entry_pla.get())
        config["energia_kwh"] = float(entry_energia.get())
        config["consumo_watts"] = float(entry_watts.get())
        salvar_config(config)
        messagebox.showinfo("Salvo", "Valores atualizados com sucesso.")
    except ValueError:
        messagebox.showerror("Erro", "Digite valores numéricos válidos.")

tk.Button(janela, text="Salvar Valores", command=salvar_config_gui).grid(row=9, column=0, columnspan=2, pady=10)

janela.mainloop()
