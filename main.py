import json
import pandas as pd
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox


class JsonToExcelConverter(ttk.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        self.title("JSONEX - Conversor JSON para Excel")
        self.geometry("420x220")
        self.resizable(False, False)

        self.json_path = None

        self._create_widgets()

    def _create_widgets(self):
        ttk.Label(self, text="Conversor de JSON para Excel", font=("Segoe UI", 14, "bold")).pack(pady=15)
        ttk.Button(self, text="Selecionar JSON", command=self.select_json, bootstyle=PRIMARY).pack(pady=5)
        ttk.Button(self, text="Converter e Salvar Excel", command=self.convert_to_excel, bootstyle=SUCCESS).pack(pady=5)

    def select_json(self):
        file_path = filedialog.askopenfilename(
            title="Selecionar Arquivo JSON",
            filetypes=[("Arquivos JSON", "*.json")]
        )
        if file_path:
            self.json_path = file_path
            messagebox.showinfo("Arquivo Selecionado", f"Arquivo selecionado:\n{file_path}")

    def convert_to_excel(self):
        if not self.json_path:
            messagebox.showwarning("Nenhum arquivo", "Por favor, selecione um arquivo JSON primeiro.")
            return

        try:
            with open(self.json_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)

            save_path = filedialog.asksaveasfilename(
                defaultextension=".xlsx",
                filetypes=[("Arquivo Excel", "*.xlsx")],
                title="Salvar como"
            )
            if not save_path:
                return

            # Verifica se é um dicionário com múltiplas listas (múltiplas sheets)
            if isinstance(json_data, dict):
                try:
                    with pd.ExcelWriter(save_path, engine='openpyxl') as writer:
                        wrote = False
                        for key, value in json_data.items():
                            if isinstance(value, list) and all(isinstance(item, dict) for item in value):
                                pd.DataFrame(value).to_excel(writer, sheet_name=str(key)[:31], index=False)
                                wrote = True
                        if not wrote:
                            # Se nenhuma lista válida foi encontrada, normaliza o dicionário completo
                            pd.json_normalize(json_data).to_excel(writer, sheet_name="dados", index=False)
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao criar múltiplas sheets:\n{e}")
                    return

            elif isinstance(json_data, list):
                df = pd.DataFrame(json_data)
                df.to_excel(save_path, index=False, sheet_name="dados")

            else:
                messagebox.showerror("Erro", "Formato de JSON não suportado para conversão.")
                return

            messagebox.showinfo("Sucesso", f"Excel salvo com sucesso:\n{save_path}")

        except Exception as e:
            messagebox.showerror("Erro na Conversão", f"Ocorreu um erro:\n{str(e)}")


if __name__ == "__main__":
    app = JsonToExcelConverter()
    app.mainloop()
