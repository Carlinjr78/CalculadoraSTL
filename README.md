# 🧮 Calculadora STL — Beta v0.1

Uma ferramenta simples e prática para makers que trabalham com impressão 3D e querem **calcular automaticamente o custo de cada peça** com base no consumo de **PLA**, **energia elétrica** e **tempo de impressão**.

---

## ✅ Funcionalidades

- 🧱 Cálculo de custo com base em:
  - Peso do PLA usado (g)
  - Tempo de impressão (h)
  - Consumo da impressora (W)
  - Preço do PLA por kg
  - Preço da energia por kWh
- 💵 Estimativa de lucro em R$ e em %
- 🔄 Cálculo de autonomia (quantas peças cabem em 1kg de PLA)
- 📊 Salvamento automático em planilha `.xlsx`
- 💾 Configurações persistentes para PLA, energia e watts
- 🖱️ Interface gráfica leve, sem necessidade de terminal

---

## 🗂️ Planilha Gerada

Cada linha da planilha `relatorio_impressoes.xlsx` contém:

| Produto | PLA (g) | Tempo (h) | Custo PLA | Custo Energia | Custo Total | Preço | Lucro R$ | Lucro % |
|---------|---------|-----------|-----------|----------------|--------------|--------|-----------|----------|

---

## ⚙️ Requisitos

Para rodar o código-fonte:

- Python 3.10+
- Instalar a biblioteca necessária:
  ```bash
  pip install openpyxl
  ```

---

## 🖥️ Executável

Se preferir usar sem instalar nada, utilize o executável já compilado:

```
/dist/calculadora_stl.exe
```

---

## 💡 Observações

- Este projeto está em fase **Beta Test**.
- Feedbacks sobre usabilidade, bugs ou sugestões de melhoria são bem-vindos!
- Desenvolvido com ❤️ por **Carlos Alberto** para facilitar a vida dos makers brasileiros.

---

## 🚀 Próximas atualizações

- Interface mais amigável com `ttk` e modo escuro
- Abertura automática da planilha
- Controle de estoque de PLA
- Relatórios por período
- Backup automático da planilha

---

## 📬 Contato

Quer sugerir melhorias ou relatar problemas? Me encontre por aqui ou no GitHub! 😄
