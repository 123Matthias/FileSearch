import ttkbootstrap as ttk

def create_card(parent, title, body):
    # Card ohne eigenen Background (nimmt Parent-Farbe)
    card = ttk.Frame(parent, padding=10)
    card.pack(fill="x", pady=6)

    # Header: Info-Farbe (blau)
    title_label = ttk.Label(
        card,
        text=title,
        font=("", 14, "bold"),
        bootstyle="info"
    )
    title_label.pack(anchor="w")

    # Body: Weißer Text (echtes Weiß via Style)
    body_label = ttk.Label(
        card,
        text=body,
        wraplength=900,
        style="White.TLabel"   # aus deinem Style-Override
    )
    body_label.pack(anchor="w", pady=(4, 0))

    return card
