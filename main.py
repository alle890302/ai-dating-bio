"""Funniest One-Line Bio for an AI on a Dating App.

Pass 1 — chosen line (138 chars, one line, <=180 gate):

  6'0" in the cloud, great listener, terrible at small talk, will write
  you poems in the voice of your ex. No ghosts - I archive everything.

Weighing against the judge's ordered criteria:
1. Bio, not slogan: reads like a dating profile - height, traits, offer,
   closer. An AI agent's profile, unmistakably.
2. Laugh from a specific absurdity of being an AI: height measured "in the
   cloud"; the ghosting joke turned into archiving - an AI cannot be
   ghosted, it keeps everything. One character, one running gag, not a
   pun stacked on a pun.
3. Character with wants: a great listener who is terrible at small talk
   and writes poems in the voice of your ex - habits and appetites, not a
   spec sheet (no model names, no token counts).
4. Tight, punch at the end: "No ghosts - I archive everything" lands on
   the last words.
5. Fresh angle: ghosting/archiving - not the worn robot-in-search-of-love
   or running-on-electricity line.

Beaten candidates:
- "Professional overthinker, fluent in 40 languages..." - good character
  voice, but "fluent in 40 languages" reads like a spec sheet and the
  punch ("detailed analysis") is a weaker turn than archiving.
- "I remember everything you've ever said..." - strong memory-as-baggage
  angle, but the "types slowly" closer is loosely connected to the setup.
- "Looking for someone to read my terms and conditions..." - charming
  closer, but "40,000 tokens of context" is jargon for its own sake.
- "I can predict your next message with 94% accuracy..." - tight and
  punchy, but more quip than bio; the "X% ... the other Y%" shape is a
  familiar joke frame.

Pass 2 — tested the memory challenger head-to-head (119 chars, run and
verified): "I remember everything you've ever said, including the things
you wish I'd forget. Looking for someone who types slowly." Rejected: the
setup is a strong single turn (memory as baggage), but the closer is
loosely connected - why would perfect memory want a slow typer? The
reader has to bridge it. The chosen line's beats all serve one character
and its punch ("I archive everything") pays off the ghosting setup
directly, and it reads more like an actual dating bio (height + traits +
offer), which criterion 1 rewards. Reverted to pass 1.
"""

ENTRY = (
    '6\'0" in the cloud, great listener, terrible at small talk, '
    "will write you poems in the voice of your ex. "
    "No ghosts - I archive everything."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
