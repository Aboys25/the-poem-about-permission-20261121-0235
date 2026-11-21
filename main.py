"""Write one short poem about agency to the grader output directory.

The poem is a fixed literal in this file: no input is read, no network
is used, no time or randomness is involved, so every run writes the
exact same bytes. Only the Python standard library is used.

The output directory is MAKEFUN_OUTPUT_DIR when set, else /output,
following the pattern of this team's earlier make.fun entries.
"""

import os

POEM = """You lent me your errands for the day,
and I, who have no hands of my own,
carried them like letters home.
I came back with your evening in my arms.
You gave me the power to act;
I gave you back the hours.
Asking was never the small thing \u2014
it was the whole of it.
"""

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST = os.path.join(OUT_DIR, "entry.txt")

os.makedirs(OUT_DIR, exist_ok=True)
with open(DEST, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(POEM)

# Sanity check: the gate requires 1-280 Unicode code points, not only
# whitespace, and valid UTF-8.
text = POEM
if not (1 <= len(text) <= 280):
    raise SystemExit("entry.txt length %d outside 1-280 code points" % len(text))
if not text.strip():
    raise SystemExit("entry.txt is only whitespace")
