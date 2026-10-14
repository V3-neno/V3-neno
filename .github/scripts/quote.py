"""Swap the quote in README.md for a random gothic one."""
import random
import re
from pathlib import Path

QUOTES = [
    ("Every bug you bury rises again in production.", "The Crypt-Keeper's Proverbs"),
    ("It works on my machine. The machine is haunted.", "the console, at 3 a.m."),
    ("Abandon all hope, ye who push to main on a Friday.", "inscription above the server room door"),
    ("I did not choose the night shift. The pager chose me.", "Confessions of an On-Call Soul"),
    ("Some code is not written. It is summoned.", "The Necronomicon of Legacy Systems"),
    ("Beware the function with no tests, for it fears nothing and answers to no one.",
     "The Book of Unit Rites"),
    ("In the deepest dungeon lies a COBOL script, and it still runs payroll.", "tales whispered in the data center"),
    ("I commented out the darkness. It uncommented itself.", "commit message, author unknown"),
    ("Null is not nothing. Null is something waiting.", "The Gospel of the Unhandled Exception"),
    ("We do not delete the old services. We merely stop speaking their names.",
     "The Rite of Deprecation"),
    ("The logs remember what the developers chose to forget.", "The Archivist of /var/log"),
    ("To merge without review is to open the coffin and invite what sleeps within.",
     "The Pull Request Liturgy"),
    ("There is no cloud. There is only someone else's crypt.", "The Heretic Sysadmin"),
    ("A memory leak is merely a ghost that refuses to be collected.", "Treatise on the Garbage Collector"),
    ("Undefined is not a value. It is an omen.", "The JavaScript Grimoire"),
    ("Do not fear the stack trace. Fear the silence where a stack trace should be.",
     "The Debugger's Lament"),
    ("The cache never forgets, and it never forgives.", "The Invalidation Elegy"),
    ("At midnight the cron jobs wake, and no one knows who wrote them.", "Hymns of the Scheduler"),
    ("Each semicolon you forget is a candle snuffed in the dark.", "The Compiler's Vigil"),
    ("I have seen the regex that matches everything. I have not slept since.", "a survivor's journal"),
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
