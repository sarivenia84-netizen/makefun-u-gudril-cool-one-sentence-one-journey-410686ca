import os
from pathlib import Path

text = "I set off with a paper map and a heroic sense of direction, got mugged by eleven cities, then followed Mum's sizzling onions home and learned the shortest way back is the route you earn twice."
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "answer.txt").write_text(text, encoding="utf-8")
