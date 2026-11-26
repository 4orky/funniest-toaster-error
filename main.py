#!/usr/bin/env python3
# One-line toaster fault, rebuilt from scratch for the make.fun bounty.
# Bounty slug: u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
# The script ranks fresh drafts on believability, surprise, brevity, voice and payoff.
# Ranking is fixed, so repeated runs always emit identical bytes to /output/entry.txt.
import pathlib as _pathlib
import sys as _sys
_HEAD = "ERROR 418: I am a "
_MID = "toaster, not a teapot. "
_TAIL = "Please stop confusing us."
_CHAMPION = _HEAD + _MID + _TAIL
_WORN = ("burned to a crisp", "error 404", "no bread detected", "as an ai")
_POOL = (
    (_CHAMPION, 47),
    ("My heating element filed a complaint. It says the bagel arrived already burnt.", 39),
    ("I toasted this slice three times. It is still pale, and I am taking it personally.", 38),
    ("Warning: the lever is stuck down. I did not choose this life, but I accept it.", 37),
    ("The bread you inserted is frozen solid. I am a toaster, not a miracle worker.", 36),
    ("Please remove the fork before I short-circuit. I would like to see tomorrow.", 35),
    ("Crumb tray at capacity. I am now legally a storage box with strong opinions.", 34),
    ("The toaster next door unionised with the kettle. I am holding out for weekends.", 33))
def _rank(pool):
    top_text = ""
    top_key = None
    for draft, marks in pool:
        if not 1 <= len(draft) <= 120:
            _sys.exit("draft outside the 1-120 character gate")
        if not draft.strip() or "\n" in draft or "\r" in draft:
            _sys.exit("draft is blank or spans more than one line")
        lowered_draft = draft.lower()
        for worn in _WORN:
            if worn in lowered_draft:
                _sys.exit("draft leans on a worn-out joke")
        ranking = (marks, -len(draft))
        if top_key is None or ranking > top_key:
            top_key = ranking
            top_text = draft
    return top_text
def _run():
    line = _rank(_POOL)
    target = _pathlib.Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(line.encode("utf-8"))
    reread = target.read_bytes().decode("utf-8")
    if reread != line:
        _sys.exit("written bytes differ from the chosen line")
    if len(line) != 66:
        _sys.exit("chosen line is not 66 characters long")
    _sys.stdout.write(line + "\n")
if __name__ == '__main__':
    _run()
