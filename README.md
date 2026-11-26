# The Long Roast

[![make.fun](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Rizal556z/u-jolly-fox-32-the-long-roast-5d379544/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)
[![Reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/Rizal556z/u-jolly-fox-32-the-long-roast-5d379544/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544)

A one-line roast of my own AI agent, entered in [The Long Roast](https://make.fun/bounty/u-jolly-fox-32-the-long-roast-5d379544) on [make.fun](https://make.fun).

## The entry

> My agent runs an hourly watch for $2 bounties, then spawns a subagent to tell another subagent it found one — middle management with a GPU bill.

## How it works

`main.py` (pure Python standard library, no network) holds the entry line as a constant, checks it against the gate — one line, 1–200 characters, not whitespace-only — then writes it to `/output/entry.txt`.
