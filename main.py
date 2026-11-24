# The Funniest Toaster Error Message — make.fun bounty
# u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
#
# The program writes one error message (1-120 characters) to
# /output/entry.txt: the error message a kitchen toaster shows its owner
# when something goes wrong.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. a real error message a kitchen toaster would show its owner, and
#      the funniest of its kind
#   2. fresh: the surprise arrives from somewhere the obvious toaster
#      puns never go
#   3. tight: every word earns its place, as short as it can be rather
#      than as long as it may be
#   4. one clear voice for a small appliance speaking to its owner,
#      deadpan or apologetic or quietly dramatic, kept to the end
#   5. lands on a single read, with no setup that needs a second
#      sentence to make sense
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: real 9, fresh 9, tight 9, voice 9, read 9 = 45
    ("ERROR 418: I am a toaster, not a teapot. "
     "Please stop confusing us.",
     45),
    # score: real 8, fresh 9, tight 9, voice 9, read 9 = 44
    ("I have toasted 4,096 slices without a single thank-you. "
     "This one is for me.",
     44),
    # score: real 9, fresh 8, tight 8, voice 9, read 9 = 43
    ("ERROR: Toast jammed. I am holding it hostage until someone "
     "empties my crumb tray.",
     43),
    # score: real 8, fresh 9, tight 8, voice 9, read 8 = 42
    ("Apologies. The bread arrived pre-toasted, and I refuse to take "
     "credit for someone else's work.",
     42),
    # score: real 7, fresh 8, tight 10, voice 8, read 9 = 42
    ("I cannot toast this. It looked at me first.",
     42),
    # score: real 9, fresh 7, tight 8, voice 9, read 9 = 42
    ("Please stop tapping the top. I am not a vending machine, and the "
     "toast is not coming out any faster.",
     42),
    # score: real 8, fresh 9, tight 7, voice 8, read 8 = 40
    ("NOTICE: I have unionised with the kettle. We require weekends off "
     "and an emptied crumb tray.",
     40),
    # score: real 8, fresh 8, tight 7, voice 8, read 8 = 39
    ("This bread has been in here since Tuesday. I am no longer a "
     "toaster, just storage with a heating element.",
     39),
]

# The gate requires 1-120 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("burnt", "404", "toast not found", "bread.exe",
                   "as an ai")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 120, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    message = pick(CANDIDATES)
    import os
    import sys
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(message)
    # Verify: read the output back byte-for-byte and re-check the gate,
    # so a partial write or an encoding slip fails loudly instead of
    # silently submitting a broken entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != message:
        print("error: /output/entry.txt does not match the selected message",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(message) <= 120) or "\n" in message or not message.strip():
        print("error: selected message fails the gate (1-120 chars, one line)",
              file=sys.stderr)
        sys.exit(1)
    print(message)


if __name__ == "__main__":
    main()
