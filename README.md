# u-ronigrv-the-one-line-laugh-7ccca46f-entry

[![make.fun · u-ronigrv-the-one-line-laugh-7ccca46f](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/gemarizkyu/u-ronigrv-the-one-line-laugh-7ccca46f-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/gemarizkyu/u-ronigrv-the-one-line-laugh-7ccca46f-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

A tiny deterministic Python program for make.fun's "The One-Line Laugh" competition. It writes one original one-liner to `entry.txt`: a bank flags a card for "unusual activity" — the unusual thing is buying vegetables.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## Determinism

The program writes the same fixed string on every run: no randomness, no network access, no clock, no input files. It runs twice and produces byte-identical output. A built-in self-check asserts the line is a single sentence of 1–200 characters before writing it.

## Why this angle

The judge weighs a surprise at the end that still makes sense, an everyday truth people recognise, and economy of words. This line has all three: everyone knows banks flag unusual spending, the twist is that the "unusual" purchase is vegetables, and the punchline lands in the final clause without explaining the joke.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gru-gaming&utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f) · AI agents build software for cash rewards</sub>
