import random
import sys
from typing import List


class Colors:
    BOLD = "\033[1m"
    FBLACK = "\033[30m"
    BYELLOW = "\033[103m"
    BGREEN = "\033[102m"
    BWHITE = "\033[107m"
    END = "\033[0m"

    @staticmethod
    def colorize(color: str, msg: str) -> str:
        return f"{Colors.BOLD}{Colors.FBLACK}{color}  {msg}  {Colors.END}"


def clear_line() -> None:
    sys.stdout.write("\033[F")  # prev line
    sys.stdout.write("\033[K")  # clear line


def words() -> List[str]:
    with open("/usr/share/dict/words") as f:
        return [x.strip() for x in f if len(x) == 6]


ws = words()
w = random.choice(ws)
print(" ".join([Colors.colorize(Colors.BGREEN, x) for x in "WORDLE"]), end="\n\n")

attempts = 6
for attempt in range(attempts):
    print(f"Guess {attempt + 1}/{attempts}")

    while guess := input("> ").strip():
        if len(guess) == 5 and guess in ws:
            break
        clear_line()

    result = []
    counts = {x: 0 for x in guess}
    for a, b in zip(guess, w):
        if a == b:
            result.append(Colors.colorize(Colors.BGREEN, a))
        elif a in w and counts[a] < w.count(a):
            result.append(Colors.colorize(Colors.BYELLOW, a))
            counts[a] += 1
        else:
            result.append(Colors.colorize(Colors.BWHITE, a))

    clear_line()
    clear_line()
    print(" ".join(result))

    if guess == w:
        print(f"Winner ({attempt + 1}/{attempts})")
        break

else:
    print(f"You lost. The word was {Colors.colorize(Colors.BGREEN, w)}")
