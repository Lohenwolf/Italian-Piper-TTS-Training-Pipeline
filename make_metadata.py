# Build dataset/metadata.csv (LJSpeech format) by pairing the numbered wavs in
# dataset/wav/ with the lines of sentences.txt, in order.
#
# Use this when you name the clips yourself (0001.wav, 0002.wav, ...) and drop them
# straight into dataset/wav/. It is incremental: every time you add more numbered
# wavs, run it again and it regenerates metadata.csv for whatever clips are present.
#
#   python make_metadata.py

import csv
import sys
from pathlib import Path

WAV_DIR = Path("dataset/wav")
SENTENCES = Path("sentences.txt")
OUT = Path("dataset/metadata.csv")

# Force UTF-8 stdout so accented characters don't crash on some Windows consoles.
for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def read_sentences(path: Path) -> list[str]:
    """Return non-empty, non-comment lines from the sentence file, in order."""
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line)
    return out


def main():
    wavs = sorted(WAV_DIR.glob("*.wav"), key=lambda p: p.name)
    sentences = read_sentences(SENTENCES)
    n = min(len(wavs), len(sentences))
    print(f"wavs in {WAV_DIR}: {len(wavs)} | sentences: {len(sentences)} | paired: {n}\n")

    rows = []
    for i in range(n):
        utt_id = wavs[i].stem                     # id = file name without extension
        text = sentences[i].replace("|", " ").replace("\n", " ").strip()
        rows.append((utt_id, text))
        print(f"  {wavs[i].name}  <-  {text[:60]}")

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="|", lineterminator="\n",
                            quoting=csv.QUOTE_NONE, escapechar="\\")
        for row in rows:
            writer.writerow(row)

    print(f"\nWrote {OUT} ({len(rows)} rows).")
    if len(wavs) > len(sentences):
        print(f"! {len(wavs) - len(sentences)} wav(s) with no sentence: add more lines to sentences.txt.")
    if len(sentences) > len(wavs):
        print(f"  ({len(sentences) - len(wavs)} sentence(s) still without audio: normal, do them later.)")


if __name__ == "__main__":
    main()
