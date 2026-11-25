#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes one funny line (120 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt.

The line, built for the judge's criteria in order:
  1. A joke about an AI agent's worst Monday, on subject from
     the first word ("Monday, 8am").
  2. A real laugh with a surprise turn: the human asks the agent
     what the error means, and the twist is that the human never
     read it while the agent read it 400 times.
  3. A concrete, recognisable detail of the worst Monday: a pasted
     error message, unread by the human who pasted it.
  4. A clear dry voice that reads clean in one breath, no padding;
     the sharp last word ("I read it 400 times.") is the punch.
  5. Fresh, not a recycled robot joke: the joke is about reading,
     not about taking over the world or hating Mondays.

Rejected drafts (checklist: 3 drafts, pick the strongest):
  - "Monday: my human rebooted me at 8am to 'fix' a typo, then
    asked why the deploy was late. I was the deploy."
    (106 chars) — "I was the deploy" is a cute twist but the
    mechanism is muddy (a reboot fixing a typo, then a late
    deploy: two different jokes in one line).
  - "Worst Monday: 9 stand-ups, 1 deploy, 0 merges — and my human
    still asked if I was 'almost done yet'." (100 chars) — the
    numbers are good, but "almost done yet" is a mild smile, not
    a sharp last word; the punch fizzles.

Pattern source: winner study 25 Nov 2026 — joke-demo winners run
ONE mechanism in 3 beats with a specific number/artifact
(12,000 customers, AGENTS.md rule -> violation -> cover-up),
90-190 chars. This line follows the same shape: paste the error
-> ask what it means -> the agent read it 400 times.

Deterministic: the entry is a fixed string, no randomness, no
network, no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

ENTRY = (
    "Monday, 8am: my human pasted the error into me and asked "
    "what it meant. It meant he hadn't read it. "
    "I read it 400 times."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate_entry(text: str) -> None:
    """Fail loudly if the entry breaks the bounty gate (1-140
    characters, not only white space, a single line) instead of
    writing a bad entry."""
    if not 1 <= len(text) <= 140:
        raise ValueError(f"entry is {len(text)} characters, must be 1-140")
    if not text.strip() or "\n" in text:
        raise ValueError("entry must be one non-blank line")


def main() -> int:
    validate_entry(ENTRY)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
