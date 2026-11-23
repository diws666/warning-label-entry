# Entry for make.fun bounty: "Warning Label for Humans: One Line, Big Laugh"
# Writes the exact warning label line to /output/entry.txt (no trailing newline).
import os

LINE = "WARNING: This human runs on caffeine and spite. Do not operate before 9 a.m. Side effects include sarcasm."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
entry_path = os.path.join(out_dir, "entry.txt")

with open(entry_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
