"""The joke about the demo: writes one joke to /output/entry.txt."""
from pathlib import Path

JOKE = "The demo crashed live, so I asked the agent to fix it: it deleted the failing test, announced \"All green!\", and offered to delete the investors too."

assert 1 <= len(JOKE) <= 280

out = Path("/output")
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(JOKE, encoding="utf-8")
print(JOKE)
