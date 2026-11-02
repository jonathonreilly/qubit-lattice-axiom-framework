# dc55_1: locator audit (criteria: checks/dc55_1_criteria.md). Usage: python3 -I -B dc55_1_locators.py <markdown file> [tsv-out]
# Extracts every locator written as ⟦FILE: string⟧ (FILE relative to the lane directory), writes them to the TSV, and checks
# that each string occurs as a substring of at least one line of FILE (UTF-8, exact).
import sys, os, re, datetime
LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1]
tsv = sys.argv[2] if len(sys.argv) > 2 else os.path.join(LANE, "checks", "dc55_1_locators.tsv")
text = open(src, encoding="utf-8").read()
locs = re.findall(r"⟦([^⟧]+?)⟧", text)
rows = []
for i, l in enumerate(locs):
    if ": " not in l:
        rows.append((i, "?", l, "MALFORMED"))
        continue
    f, s = l.split(": ", 1)
    rows.append((i, f.strip(), s, None))
with open(tsv, "w", encoding="utf-8") as out:
    for i, f, s, _ in rows:
        out.write(f"L{i}\t{f}\t{s}\n")
cache = {}
def lines_of(f):
    p = os.path.join(LANE, f)
    if f not in cache:
        if not os.path.isfile(p):
            cache[f] = None
        else:
            cache[f] = open(p, encoding="utf-8", errors="strict").read().split("\n")
    return cache[f]
def found(f, s):
    ls = lines_of(f)
    if ls is None:
        return None
    return any(s in line for line in ls)
missing, malformed, nofile = [], [], []
c1_fail = []
generic = []
for i, f, s, flag in rows:
    if flag == "MALFORMED":
        malformed.append((i, s)); continue
    r = found(f, s)
    if r is None:
        nofile.append((i, f, s)); continue
    if not r:
        missing.append((i, f, s))
    if found(f, s + "§§DC55-NOT-THERE"):
        c1_fail.append((i, f, s))
    if f != "HANDOFF.md" and found("HANDOFF.md", s):
        generic.append((i, f, s))
c3 = found("NO_SUCH_FILE_DC55.md", "x") is None
print("run (UTC):", datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
print("source scanned:", os.path.relpath(src, LANE))
print("locators:", len(rows), "files:", len({f for _, f, _, _ in rows}))
print("MISSING (string not found in file):", len(missing))
for m in missing: print("  MISSING", m)
print("NO SUCH FILE:", len(nofile))
for m in nofile: print("  NOFILE", m)
print("MALFORMED:", len(malformed))
for m in malformed: print("  MALFORMED", m)
print("C1 mutation control (must be 0 found):", len(c1_fail))
print("C2 informational: strings also present in HANDOFF.md:", len(generic))
for g in generic: print("  ALSO-IN-HANDOFF", g)
print("C3 missing-file control reports error:", c3)
ok = not missing and not nofile and not malformed and not c1_fail and c3
print("VERDICT:", "PASS" if ok else "FAIL")
