"""Structural index of SA's complete account (CA-I/II/III).

For every numbered statement (theorem, lemma, proposition, corollary) record file,
line, label, heading title and the status the account itself declares in its
heading or in the lines that follow it (CA-I L27-46 convention).
Output: TSV on stdout. A text index only; it reads, it proves nothing.
"""
import re
import sys

ENV = re.compile(r"\\begin\{(theorem|lemma|proposition|corollary)\}(\[(.*)\])?")
LABEL = re.compile(r"\\label\{([^}]*)\}")


def heading_title(lines, i):
    """Collect the optional [..] argument, which may span lines."""
    text = lines[i]
    j = i
    if "[" in text.split("}", 1)[1][:2]:
        depth = 0
        out = []
        started = False
        while j < len(lines) and j < i + 6:
            for ch in lines[j][(lines[j].index("[") if j == i else 0):]:
                if ch == "[":
                    depth += 1
                    started = True
                    if depth == 1:
                        continue
                if ch == "]":
                    depth -= 1
                    if started and depth == 0:
                        return " ".join("".join(out).split()), j
                out.append(ch)
            out.append(" ")
            j += 1
    return "", i


def status(title, follow):
    t = title.lower()
    f = follow.lower()
    if "proof outstanding" in f[:600] or "proof outstanding" in t:
        return "OUTSTANDING"
    if "proof incomplete" in f[:600] or "proof incomplete" in t:
        return "INCOMPLETE"
    if "printed without proof" in t or "printed without proof" in f[:400]:
        return "PRINTED"
    if t.startswith("model") or "(model)" in t or " model" in t[:12]:
        return "MODEL"
    if "\\cite" in title or "cited by statement" in t:
        return "CITED"
    return "PROVED"


def main(paths):
    print("file\tline\tkind\tlabel\tstatus\ttitle")
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = fh.readlines()
        for i, line in enumerate(lines):
            m = ENV.search(line)
            if not m:
                continue
            title, j = heading_title(lines, i)
            lab = ""
            for k in range(i, min(i + 8, len(lines))):
                lm = LABEL.search(lines[k])
                if lm:
                    lab = lm.group(1)
                    break
            follow = "".join(lines[j + 1:j + 25])
            st = status(title, follow)
            title = title.replace("\t", " ")[:220]
            print(f"{name}\t{i + 1}\t{m.group(1)}\t{lab}\t{st}\t{title}")


if __name__ == "__main__":
    main(sys.argv[1:])
