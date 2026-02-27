import ttkbootstrap as ttk
from tkinter import filedialog
import os
from card import create_card

class MeineApp:
    def __init__(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title("OSWalk")

        # Header
        self.header = ttk.Frame(self.root)
        self.header.pack(padx=(50,50), pady=(40, 10), fill="x")

        self.title_os = ttk.Label(self.header, text="OS", font=("", 32, "bold"), bootstyle="info")
        self.title_os.pack(side="left", padx=(0, 2))

        self.title_walk = ttk.Label(self.header, text="Walk", font=("", 32, "bold"), bootstyle="warning")
        self.title_walk.pack(side="left", padx=(0, 12))

        self.keywords = ttk.Entry(self.header, bootstyle="light", font=("", 16))
        self.keywords.pack(side="left", fill="x", expand=True)
        self.keywords.bind("<Return>", self.suchen)

        # Pfad
        self.pfad_label = ttk.Label(self.root, text="Kein Pfad gewählt", bootstyle="light")
        self.pfad_label.pack(pady=(10, 5))

        self.btn = ttk.Button(self.root, text="search-path", command=self.datei_oeffnen)
        self.btn.pack(pady=(0, 10))

        # ===== Results (Scroll-Container) =====
        self.results_wrap = ttk.Frame(self.root)
        self.results_wrap.pack(fill="both", expand=True, padx=50, pady=(10, 20))

        self.canvas = ttk.Canvas(self.results_wrap)
        self.scrollbar = ttk.Scrollbar(self.results_wrap, orient="vertical", command=self.canvas.yview)
        self.scrollable = ttk.Frame(self.canvas)

        self.scrollable.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        # ================================================


        # Beispiel-Cards
        for i in range(20):
            create_card(
                self.scrollable,
                f"example_{i}.txt",
                "… hier stehen 40 Zeichen vor dem Treffer und 40 Zeichen nach dem Treffer …"
            )

 
        self.root.mainloop()

    def clear_results(self):
        for w in self.scrollable.winfo_children():
            w.destroy()

    def add_result(self, filename, snippet, path):
        card = ttk.Frame(self.scrollable, bootstyle="secondary", padding=10)
        card.pack(fill="x", pady=6)

        title = ttk.Label(card, text=filename, font=("", 14, "bold"), bootstyle="light")
        title.pack(anchor="w")

        body = ttk.Label(card, text=snippet, wraplength=900, bootstyle="secondary")
        body.pack(anchor="w", pady=(4, 0))

        # Klick = Datei öffnen (macOS/Linux/Windows) TODO openFilePath
        def open_file(_=None):
            try:
                if os.name == "nt":
                    os.startfile(path)
                elif sys.platform == "darwin":
                    os.system(f'open "{path}"')
                else:
                    os.system(f'xdg-open "{path}"')
            except:
                pass

        card.bind("<Button-1>", open_file)
        title.bind("<Button-1>", open_file)
        body.bind("<Button-1>", open_file)

    def make_snippet(self, text, keyword, ctx=40): # 40 Wörter vorher und nachher anzeigen als description
        idx = text.lower().find(keyword.lower())
        if idx == -1:
            return None

        start = max(0, idx - ctx)
        end = min(len(text), idx + len(keyword) + ctx)
        return text[start:end].replace("\n", " ")

    def datei_oeffnen(self):
        pfad = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
        if pfad:
            self.pfad_label.configure(text=pfad)
            self.basis_pfad = pfad

    def suchen(self, event=None):
        keyword = self.keywords.get().strip()
        self.clear_results()

        if not getattr(self, "basis_pfad", None) or not keyword:
            return

        for root, _, files in os.walk(self.basis_pfad):
            for name in files:
                if not name.lower().endswith((".txt", ".md", ".py")):
                    continue

                pfad = os.path.join(root, name)
                try:
                    with open(pfad, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                except:
                    continue

                snippet = self.make_snippet(content, keyword, ctx=40)
                if snippet:
                    self.add_result(name, snippet, pfad)


if __name__ == "__main__":
    import sys
    MeineApp()