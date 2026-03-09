import os
from typing import Optional

# externe Libraries

import fitz  # PyMuPDFcmd

class ReaderService:
    """
    Service zum Lesen von Text aus verschiedenen Dateiformaten.
    Nutzt pdfplumber oder PyMuPDF für PDFs, kann leicht erweitert werden.
    """

    def __init__(self):
        # Unterstützte Dateiformate
        self.supported_extensions = {
            '.pdf', '.txt', '.md', '.html', '.htm', '.docx', '.doc', '.odt', '.rtf',
            '.xlsx', '.xls', '.csv',
            '.pptx', '.ppt'
        }

    def extract_text(self, filepath: str, max_chars: Optional[int] = 1000) -> Optional[str]:
        """
        Zentrale Methode: erkennt Dateiformat und ruft passende Extraktionsmethode auf.
        """
        if not os.path.exists(filepath):
            print(f"❓ Datei nicht gefunden: {filepath}")
            return None

        ext = os.path.splitext(filepath)[1].lower()
        if ext not in self.supported_extensions:
            print(f"⚠️ Format nicht unterstützt: {filepath}")
            return None

        try:
            if ext == '.pdf':
                text = self._extract_pdf(filepath)
            elif ext in {'.txt', '.md', '.html', '.htm'}:
                text = self._extract_text_file(filepath)
            else:
                # Platzhalter für weitere Formate wie docx, xlsx etc.
                text = self._extract_generic(filepath)

            if not text:
                return None

            # Text bereinigen
            text = ' '.join(text.split())

            if max_chars and len(text) > max_chars:
                text = text[:max_chars] + "..."

            return text

        except Exception as e:
            print(f"❌ Fehler beim Lesen von {filepath}: {e}")
            return None


    def _extract_pdf(self, filepath: str) -> str:
        """PDF-Extraktion nur mit PyMuPDF."""
        doc = fitz.open(filepath)
        text = "\n".join([page.get_text() for page in doc])
        return text

    def _extract_text_file(self, filepath: str) -> str:
        """Textdateien (txt, md, html) auslesen."""
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

    def _extract_generic(self, filepath: str) -> str:
        """
        Platzhalter für Word, Excel, PPTX etc.
        Hier könnte z.B. python-docx, openpyxl, python-pptx genutzt werden.
        """
        print(f"ℹ️ Generische Extraktion noch nicht implementiert für {filepath}")
        return ""

    def get_snippet(self, filepath: str, keywords: str = "", context_chars: int = 200) -> Optional[str]:
        """Erste 500 Zeichen als Snippet."""
        text = self.extract_text(filepath, max_chars=None)
        if not text:
            return f"Path: {filepath}"
        return text[:500] + "..."

    def is_supported(self, filepath: str) -> bool:
        ext = os.path.splitext(filepath)[1].lower()
        return ext in self.supported_extensions