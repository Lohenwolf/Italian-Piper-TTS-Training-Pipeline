# Piper Italian Voice Trainer

**Complete toolkit** to build and fine-tune your own Italian voice from "scratch".

Fine-tuneing starts from the Spanish [`es_ES/davefx`](https://huggingface.co/datasets/rhasspy/piper-checkpoints/tree/main/es/es_ES/davefx)
checkpoint on an Italian dataset. Single speaker · 22.05 kHz · `medium` quality.

---

## Build / fine-tune your own voice

Everything is included.

1. **Phrases** — [`sentences.txt`](sentences.txt): put here your varied Italian sentences.
   One line = one clip. You can edit/extend it freely.
2. **Audio** — generate one clip per line with any TTS you like, as `.wav`. Number them
   `0001.wav, 0002.wav, …` in order.
3. **Dataset** — build the LJSpeech layout (`dataset/wav/` + `metadata.csv`):
   ```bash
   python make_metadata.py        # clips already numbered in dataset/wav/
   ```
4. **Train** — open [`piper_train_colab.ipynb`](piper_train_colab.ipynb) on Google Colab
   (free GPU): preprocess → fine-tune → export `model.onnx`.

## Repo contents

| File | What it is |
|------|------------|
| `sentences.txt` |Italian sentences used as the dataset script |
| `make_metadata.py` | builds `metadata.csv` from numbered wavs |
| `piper_train_colab.ipynb` | the full Colab training/export notebook |

## Credits

- **Base checkpoint:** `es_ES/davefx` (medium) — [rhasspy/piper-checkpoints](https://huggingface.co/datasets/rhasspy/piper-checkpoints).
- **[Piper](https://github.com/rhasspy/piper)** (MIT) and **espeak-ng** (GPL) for synthesis & phonemization.

## Notes & license

- Toolkit code: **MIT**. Please
  keep the davefx attribution if you build on it.
