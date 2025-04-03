# 🧩 JSONEX — Conversor JSON para Excel

Um pequeno aplicativo com interface gráfica feito em **Python** 
usando [ttkbootstrap](https://ttkbootstrap.readthedocs.io/), 
que converte arquivos `.json` em planilhas `.xlsx` do Excel.

---

## ✅ Funcionalidades

- 📄 Converte arquivos `.json` para `.xlsx`
- 🧠 Detecta automaticamente:
  - Lista de dicionários (JSON simples)
  - Dicionário com múltiplas listas (cada chave vira uma **aba/sheet** separada)
- 🎨 Interface amigável com tema escuro (`superhero` do ttkbootstrap)

---

## 🚀 Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/CelsoJr85/jsonex.git
cd jsonex
Crie e ative um ambiente virtual (recomendado):

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
# ou
source venv/bin/activate  # Linux/macOS
Instale as dependências:

bash
Copy
Edit
pip install -r requirements.txt
🧠 Como Usar
Execute o app:

bash
Copy
Edit
python main.py
Na interface:

Clique em Selecionar JSON e escolha o arquivo .json

Clique em Converter e Salvar Excel

O arquivo .xlsx será salvo no local escolhido

🛠 Requisitos
Python 3.8 ou superior

Módulos usados:

ttkbootstrap

pandas

openpyxl

📂 Estrutura do Projeto
bash
Copy
Edit
jsonex/
├── main.py              # Código principal da aplicação
├── requirements.txt     # Dependências do projeto
├── .gitignore           # Ignora arquivos desnecessários no repositório
└── README.md            # Este arquivo
📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

👤 Autor
Feito com 💻 por Custódio
🔗 GitHub: CelsoJr85
📧 E-mail: celsocustodiojunior1985@gmail.com
