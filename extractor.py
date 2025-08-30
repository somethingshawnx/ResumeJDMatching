def load_text(path):
    """Load plain text file and clean."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    return " ".join(text.split())

