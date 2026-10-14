"""Swap the quote in README.md for a random gothic one."""
import random
import re
from pathlib import Path

QUOTES = [
    ("Deep into that darkness peering, long I stood there, wondering, fearing, doubting, "
     "dreaming dreams no mortal ever dared to dream before.", "Edgar Allan Poe, *The Raven*"),
    ("All that we see or seem is but a dream within a dream.", "Edgar Allan Poe, *A Dream Within a Dream*"),
    ("The boundaries which divide Life from Death are at best shadowy and vague.",
     "Edgar Allan Poe, *The Premature Burial*"),
    ("I became insane, with long intervals of horrible sanity.", "Edgar Allan Poe"),
    ("Beware; for I am fearless, and therefore powerful.", "Mary Shelley, *Frankenstein*"),
    ("Nothing is so painful to the human mind as a great and sudden change.", "Mary Shelley, *Frankenstein*"),
    ("Listen to them, the children of the night. What music they make!", "Bram Stoker, *Dracula*"),
    ("We learn from failure, not from success!", "Bram Stoker, *Dracula*"),
    ("The only way to get rid of a temptation is to yield to it.", "Oscar Wilde, *The Picture of Dorian Gray*"),
    ("Hell is empty and all the devils are here.", "William Shakespeare, *The Tempest*"),
    ("The oldest and strongest emotion of mankind is fear, and the oldest and strongest kind "
     "of fear is fear of the unknown.", "H. P. Lovecraft"),
    ("That is not dead which can eternal lie, and with strange aeons even death may die.", "H. P. Lovecraft"),
    ("It works on my machine. The machine is haunted.", "the console, at 3 a.m."),
    ("Every bug you bury rises again in production.", "an old crypt-keeper's proverb"),
]

readme = Path("README.md")
text = readme.read_text(encoding="utf-8")
pattern = re.compile(r"(<!--QUOTE:START-->\n).*?(\n<!--QUOTE:END-->)", re.S)
current = pattern.search(text).group(0)

# Never pick the quote that's already showing
choices = [q for q in QUOTES if q[0] not in current]
quote, source = random.choice(choices)
block = f'> *"{quote}"*\n>\n> — {source}'

readme.write_text(pattern.sub(lambda m: m.group(1) + block + m.group(2), text), encoding="utf-8")
