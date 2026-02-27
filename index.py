

import ttkbootstrap as ttk
from tkinter import filedialog
import os
from Service.explorer_service import list_files
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

        # Pfad-
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

        self.canvas.create_window((0, 0), window=self.scrollable, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # ================================================

        """"
        # Beispiel-Cards
        for i in range(20):
            create_card(
                self.scrollable,
                f"example_{i}.txt",
                "… hier stehen 40 Zeichen vor dem Treffer und 40 Zeichen nach dem Treffer …"
            )
        """
        self.scrollable.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))


        self.root.bind_all("<MouseWheel>", self._on_mousewheel)      # Windows / macOS
        self.root.bind_all("<Button-4>", self._on_mousewheel)       # Linux
        self.root.bind_all("<Button-5>", self._on_mousewheel)




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
        """Wird bei Enter im Suchfeld ausgeführt"""
        keywords = self.keywords.get()
        
        # Prüfen ob ein Pfad ausgewählt wurde
        if not getattr(self, "basis_pfad", None):
            print("Kein Pfad ausgewählt")
            return
        
        if not keywords:
            print("Kein Suchbegriff eingegeben")
          
        
        # Alte Ergebnisse löschen
        self.clear_results()
        
        # Dateien mit ExplorerService auflisten
        dateien = list_files(self.basis_pfad, keywords, recursive=True)
        
        # Für jede Datei eine Card erstellen (vorerst nur Platzhalter-Text)
        for dateipfad in dateien[:50]:  # Erste 50 Dateien als Beispiel
            dateiname = os.path.basename(dateipfad)
            
            # Hier kommt später die Snippet-Logik rein
            platzhalter_text = f"Datei gefunden unter: {dateipfad}"
            
            # Card erstellen
            create_card(
                self.scrollable,
                dateiname,           # Title = Dateiname
                platzhalter_text     # Body = Platzhalter
            )
        
        # Info anzeigen wie viele Dateien gefunden wurden
        if hasattr(self, 'ergebnis_label'):
            self.ergebnis_label.configure(
                text=f"{len(dateien)} Dateien gefunden. Zeige erste 50.",
                bootstyle="info"
            )

    def _on_mousewheel(self, event):
        x, y = self.root.winfo_pointerxy()
        widget = self.root.winfo_containing(x, y)

        # nur scrollen, wenn Maus über Results-Bereich ist
        if widget is None or not str(widget).startswith(str(self.results_wrap)):
            return

        if event.delta:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

if __name__ == "__main__":
    MeineApp()