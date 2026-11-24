import os
# One-liner entry (92 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "Error 04: Bread inserted upside down. I toasted it anyway. We both know whose fault this is."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
