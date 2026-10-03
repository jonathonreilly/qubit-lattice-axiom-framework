import re, os
rep = open("FINAL_REPORT.md").read()
def reindent(md):
    out = []
    for line in md.split("\n"):
        stripped = line.lstrip(" ")
        s = len(line) - len(stripped)
        if s > 0 and stripped:
            level = (s + 1) // 2           # 2 or 3 spaces -> 1 level, 4-5 -> 2, ...
            line = " " * (4 * level) + stripped
        out.append(line)
    return "\n".join(out).strip() + "\n"
secs = {}
# summary
i = rep.index("## The night in one page"); j = rep.index("## How to read this")
secs["s1"] = rep[i:j]
k = rep.index("## What we found")
secs["s2"] = rep[j:k]
body = rep[k:]
parts = re.split(r"(?m)^### ", body)
# parts[0] = "## What we found\n\n", parts[1..] = sections "0. ...", ..., then trailing ## sections inside last part
for p in parts[1:]:
    num = p.split(".")[0].strip()
    head, rest = p.split("\n", 1)
    tail = ""
    m = re.search(r"(?m)^## ", rest)
    if m:
        tail = rest[m.start():]; rest = rest[:m.start()]
    secs[f"f{num}"] = "## " + head + "\n" + rest
    if tail:
        for q in re.split(r"(?m)^(?=## )", tail):
            if q.startswith("## Your menu decision"): secs["menu"] = q
            elif q.startswith("## The assembled model"): secs["a13"] = q.replace("## The assembled model (A13)", "## The assembled model of the earlier shape (A13)", 1)
            elif q.startswith("## Decisions this raises"): secs["dec"] = q.replace("## Decisions this raises (yours)", "## Decisions for you: the full list (0 to 27)", 1)
order = ["s1", "s2"] + [f"f{n}" for n in range(12)] + ["menu", "a13", "dec"]
for key in order:
    md = reindent(secs[key])
    md = re.sub(r"(?m)^\*(Final review round|Running now|Still running).*\*\s*$", "", md).rstrip() + "\n"
    open(f"docfill/{key}.md", "w").write(md)
    print(key, len(md), md.split("\n", 1)[0][:90])
