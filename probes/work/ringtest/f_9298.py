#!/usr/bin/env python3
"""J:provenance:PR{PR} -- every number in the note located in the PR's cached runner stdout, the runner source, or an exact derivation from printed values.

Own generic scanner (PR files auto-detected at the PR head via git): the statement text is the note body after the metadata block (markdown link targets removed, Unicode minus/superscripts
normalised).  Every numeric token is classified, in this order:
  STRUCT   dates, identifiers (PR numbers, file names), lattice sizes L^3, exponent digits, list numbering, 'about'-free small counts written as words are not tokens
  CACHE    a value printed in the cached stdout (any printed number, rounded to the note's decimals; units 1, 1e2, 1e-2, 1e3, 1e-3 allowed)
  RUNNER   a numeric constant of the runner source (seeds, populations, tolerances, sizes)
  DERIVED  a difference, sum, mean, ratio or percentage of two printed values, or a difference of a printed value and a runner constant (found by search; the pair is printed)
  else     UNCOVERED (counted as HIT)
Self-contained; reads the PR head via git.
"""
import itertools, math, re, subprocess, sys
from pathlib import Path

PR = 9298
ROOT = Path(__file__).resolve().parents[3]
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
git("fetch", "origin", f"pull/{PR}/head", "--quiet")
HEAD = git("rev-parse", "FETCH_HEAD").stdout.strip()
files = [f for f in git("diff", "--name-only", f"origin/main...{HEAD}").stdout.split() if "audit/data" not in f]
note_path = [f for f in files if f.startswith("docs/") and f.endswith(".md")][0]
cache_path = [f for f in files if f.startswith("logs/runner-cache/")][0]
runner_path = [f for f in files if f.startswith("scripts/") and f.endswith(".py")][0]
def show(p): return git("show", f"{HEAD}:{p}").stdout
note, cache_raw, runner = show(note_path), show(cache_path), show(runner_path)
data_files = [f for f in files if f.startswith("data/") and f.endswith((".json", ".md", ".csv"))]
data_txt = "\n".join(show(f) for f in data_files)
print(f"PR #{PR} head {HEAD[:10]}: note {note_path[:80]}...; cache {len(cache_raw)} bytes; runner {len(runner)} bytes")

SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")
def norm(t):
    t = t.replace("−", "-").replace("–", "-").replace("×", "x").replace("±", "+-")
    t = re.sub(r"10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda m: "1e" + m.group(1).translate(SUP), t)
    t = re.sub(r"([\d.]+) ?x ?1e(-?\d+)", lambda m: f"{m.group(1)}e{m.group(2)}", t)
    return t
NUM = re.compile(r"(?<![A-Za-z_\d.])[-+]?(?:\d{1,3}(?:,\d{3})+(?:\.\d*)?|\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")
def numbers(text):
    out = []
    for m in NUM.finditer(norm(text)):
        s = m.group(0).replace(",", "")
        try: out.append(float(s))
        except ValueError: pass
    return out
cache = cache_raw.split("----- stdout -----\n", 1)[-1].split("\n----- stderr")[0]
pc = sorted(set(abs(x) for x in numbers(cache) if x == x and abs(x) < 1e12 and x != 0))
cache_lines = [sorted(set(abs(x) for x in numbers(l) if x == x and abs(x) < 1e12 and x != 0)) for l in cache.split("\n")]
pr = sorted(set(abs(x) for x in numbers(runner + "\n" + data_txt.replace(chr(34), " ")) if x == x and abs(x) < 1e12 and x != 0))
print(f"   {len(pc)} distinct printed values, {len(pr)} runner and packaged-data constants ({len(data_files)} data files)")

body = note.split("\n---\n", 2)[-1] if note.startswith("---") else note
body = re.sub(r"\]\([^)]*\)", "]", body)
body = re.sub(r"`[^`\n]*\.(?:md|py|txt|json)`", " FILE ", body)                                              # file names in code spans
body = re.sub(r"`[A-Za-z_./-]{14,}[^`\n]*`", " ID ", body)
body = re.sub(r"\b[A-Z][A-Z_0-9]{12,}\b", "ID", body)
body = re.sub(r"\b\d{4}-\d{2}-\d{2}\b", "DATE", body)
_ids = set(re.findall(r"(?:PRs?|#)\s?#?(\d{4})", note)) | set(re.findall(r",\s*(\d{4})\)", note))
body = re.sub(r"\bPRs? ?#?\d{4}\b|#\d{4}\b|\bpull/\d+", "PRID", body)
body = re.sub(r"(?<![\d.])9[23]\d\d(?![\d.]| s\b| walkers)", "PRID", body)
for _i in _ids: body = re.sub(rf"(?<![\d.]){_i}(?![\d.])", "PRID", body)
body = re.sub(r"\b\d{1,2}[³^]3?\b|\b\d{1,2}\^3\b|\b\d{1,2}³", "SIZE", body)
body = re.sub(r"\b\d{1,2}\^?[³]|\bL = \d+", lambda m: m.group(0), body)
body = norm(body)
body = re.sub(r"(?<=[a-z]{3})(?=\d{3,})", " ", body)
body = re.sub(r"([a-z])(\d+\.\d+)", r"\1 \2", body)
body = re.sub(r"(\d)(MHz|kHz|GHz|Hz|ns|kHz|dB)\b", r"\1 \2", body)
body = re.sub(r"(?<=\d)[ \u202f\u00a0](?=\d{3}\b)", "", body)
toks = [(m.start(), m.end(), m.group(0).replace(",", "")) for m in NUM.finditer(body)]
def dec(s): return len(s.split(".")[1]) if "." in s and "e" not in s.lower() else 0
def sig(s): return len(s.lstrip("+-").replace(".", "").lstrip("0").split("e")[0])
def close(p, v, d, scale):
    q = p * scale
    return abs(round(q, d) - v) <= 1e-9 * max(1, v) or (d > 0 and abs(q - v) <= 0.5 * 10 ** (-d) + 1e-12)
SC = (1, 100, 1e-2, 1e3, 1e-3, 1e6, 1e-6)
cache_lits = set(re.findall(r"(?<![\d.])\d*\.?\d+(?![\d])", cache.replace(",", " ")))
runner_lits = set(re.findall(r"(?<![\d.])\d*\.?\d+(?![\d])", runner))
def literal(s_, srcs):
    t = s_.lstrip("+-").rstrip(".")
    return any(t in L or t.lstrip("0") in L for L in srcs)
def direct(v, d, pool):
    return next(((p, sc) for p in pool for sc in SC if close(p, v, d, sc)), None)
def local_numbers(a, b):
    seg = body[max(0, a - 320):min(len(body), b + 320)]
    out = []
    for m in NUM.finditer(seg):
        t = m.group(0).replace(",", "")
        try: x = abs(float(t))
        except ValueError: continue
        if x != 0 and not (m.start() + max(0, a - 320) <= a < m.end() + max(0, a - 320)): out.append((x, dec(t)))
    return out
def derived(v, d, a=None, b=None):
    tol = 1.6 * 10 ** (-d)
    loc = local_numbers(a, b) if a is not None else []
    for (x, dx), (y, dy) in itertools.permutations(loc, 2):
        e = tol + 0.6 * 10 ** (-dx) + 0.6 * 10 ** (-dy)
        cands = (("diff", abs(x - y), e), ("sum", x + y, e), ("ratio", x / y, e * max(1, abs(x / y)) / max(y, 1e-9) + tol), ("pct", 100 * abs(x - y) / y, tol + 0.6 * 10 ** (-dx) * 100 / y + 0.6 * 10 ** (-dy) * 100 * abs(x - y) / y ** 2))
        for kind, val, ee in cands:
            for sc in (1, 1e3, 1e-3):
                if abs(val * sc - v) <= ee * sc and sig(str(v)) >= 2: return (kind + "-in-note", x, y, sc)
    for line in cache_lines:
        for x in line:
            for y in line:
                if x == y: continue
                for sc in (1, 100, 1e3, 1e-3):
                    if close(abs(x - y), v, d, sc): return ("diff", x, y, sc)
                    if x < y and close(x + y, v, d, sc): return ("sum", x, y, sc)
                    if y != 0 and close(x / y, v, d, sc): return ("ratio", x, y, sc)
                    if y != 0 and close(100 * abs(x - y) / y, v, d, sc): return ("pct", x, y, sc)
    return None
# numbers printed by the open PRs the note cites
refs = sorted(set(int(x) for x in re.findall(r"(?:open PR|PR|#)\s?#?(\d{4})", note) if int(x) != PR))
refpool = {}
for r_ in refs:
    git("fetch", "origin", f"pull/{r_}/head", "--quiet"); h_ = git("rev-parse", "FETCH_HEAD").stdout.strip()
    fl = [f for f in git("diff", "--name-only", f"origin/main...{h_}").stdout.split() if f.startswith("logs/runner-cache/")]
    if fl: refpool[r_] = sorted(set(abs(x) for x in numbers(git("show", f"{h_}:{fl[0]}").stdout.split("----- stdout -----\n", 1)[-1]) if abs(x) < 1e12 and x != 0))
print("   referenced open PRs with a cache:", {k: len(v) for k, v in refpool.items()})
res = {"STRUCT": [], "CACHE": [], "RUNNER": [], "DERIVED": [], "REF": [], "UNC": []}
for a, b, s in toks:
    ctx = body[max(0, a - 40):b + 30].replace("\n", " ")
    v = abs(float(s)); d = dec(s)
    if re.fullmatch(r"\d+", s) and int(s) in {m * L_ ** 3 for L_ in (2, 4, 6, 8, 10, 12, 16, 20, 24) for m in (1, 3)}:
        res["STRUCT"].append((s, ctx + "  <- lattice size L^3 or 3 L^3 (links or plaquettes)")); continue
    if s in ("0", "1", "2", "3", "4") or (re.fullmatch(r"\d+", s) and v <= 12 and not re.search(r"(walkers|seeds|batches|runs|steps|samples)", ctx[40:])):
        res["STRUCT"].append((s, ctx)); continue
    weak = sig(s) < 4
    hit = (literal(s, [cache_lits]) if weak else direct(v, d, pc)) if (sig(s) >= 2 or d > 0) else None
    if hit: res["CACHE"].append((s, ctx)); continue
    hit = literal(s, [runner_lits]) if weak else direct(v, d, pr)
    if hit: res["RUNNER"].append((s, ctx)); continue
    rr = [k for k, pool_ in refpool.items() if (direct(v, d, pool_) and not weak) or (weak and any(abs(q - v) < 1e-12 for q in pool_))]
    if rr: res["REF"].append((s, ctx + f"  <- printed by the cache of PR {rr[0]}")); continue
    res["UNC"].append((s, ctx))

# ------------------------------------------------------------------ explicit derivations for tokens not printed anywhere
def cache_vals(pattern, text=None):
    return [float(x) for x in re.findall(pattern, text or cache)]
extra_hits = []
def take(tok, ok, how, hit_note=None):
    for i, (s_, c_) in enumerate(res["UNC"]):
        if s_ == tok:
            res["UNC"].pop(i)
            if ok: res["DERIVED"].append((tok, c_[:70] + "  <- " + how)); return
            res["UNC"].append(("HIT:" + tok, c_)); extra_hits.append(f"{tok}: {hit_note or how}"); return
    print(f"[UNUSED extra] {tok}")
if PR == 9298:
    chi24, e24 = 0.831, 0.077; chi20, e20 = 0.990, 0.032
    ratio = chi24 / chi20; eratio = ratio * math.hypot(e24 / chi24, e20 / chi20)
    z_comb = (chi20 - chi24) / math.hypot(e24, e20); z_24 = (chi20 - chi24) / e24
    take("0.84", abs(ratio - 0.84) < 0.005 and abs(eratio - 0.08) < 0.006, f"0.831/0.990 = {ratio:.4f} +- {eratio:.4f} (first-order propagation; both values printed in the cache line)")
    take("1.7", abs(z_comb - 1.7) < 0.05 or abs(z_24 - 1.7) < 0.05, f"(0.990-0.831)/sqrt(0.032^2+0.077^2) = {z_comb:.2f}; (0.990-0.831)/0.077 = {z_24:.2f}",
         f"the note says the 24^3 value lies 1.7 standard errors below the 20^3 value; the printed values give {z_comb:.2f} (combined error) or {z_24:.2f} (24^3 error alone), and the sibling PR 9361 cache computes the same statistic as {(0.990-0.856)/math.hypot(0.042, 0.032):.2f} = its printed -2.5 sigma")
    import numpy as _np
    sites_ = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    lid = lambda a, s_: a * 8 + sites_.index(s_)
    def sh_(s_, a): t = list(s_); t[a] = (t[a] + 1) % 2; return tuple(t)
    plq = [(lid(a, s_), lid(b, sh_(s_, a)), lid(a, sh_(s_, b)), lid(b, s_)) for s_ in sites_ for a in range(3) for b in range(a + 1, 3)]
    # arrows sigma=+-1 (bit=1 -> +1); zero-winding ice states = every vertex div 0 and all three plane windings 0; orbit of the canonical state under circulation flips
    def div_ok(st):
        for s_ in sites_:
            d = 0
            for a in range(3):
                m = list(s_); m[a] = (m[a] - 1) % 2
                d += (2 * ((st >> lid(a, s_)) & 1) - 1) - (2 * ((st >> lid(a, tuple(m))) & 1) - 1)
            if d != 0: return False
        return True
    def wind(st):
        return tuple(sum(2 * ((st >> lid(a, s_)) & 1) - 1 for s_ in sites_ if s_[a] == 0) for a in range(3))
    def circ(st, p):
        b = lambda l: 2 * ((st >> l) & 1) - 1
        return b(p[0]) + b(p[1]) - b(p[2]) - b(p[3])
    canon = 0
    for s_ in sites_:
        v = [(-1) ** s_[1], (-1) ** s_[0], (-1) ** s_[0]]
        for a in range(3):
            if v[a] > 0: canon |= 1 << lid(a, s_)
    assert div_ok(canon) and wind(canon) == (0, 0, 0)
    seen = {canon}; stack = [canon]
    while stack:
        st = stack.pop()
        for p in plq:
            if abs(circ(st, p)) == 4:
                nx = st ^ sum(1 << l for l in p)
                if nx not in seen: seen.add(nx); stack.append(nx)
    take("864", len(seen) == 864 and all(div_ok(x) for x in seen), f"orbit of the canonical zero-winding arrow state under circulation flips on the 2^3 torus has {len(seen)} states, all with zero divergence")
if PR == 9352:
    s_ = 2 * math.sin(math.pi / 8)
    est = [(1.0884, 0.28861), (1.0413, 0.28861), (1.1400, 0.28837), (1.0821, 0.28851)]
    bd = [2 * s_ * math.sqrt(u_ / c_) for c_, u_ in est]
    take("0.77", abs(min(bd) - 0.77) < 0.006 and abs(max(bd) - 0.81) < 0.006, f"omega_min <= 2 s sqrt(u/chi) with s = 2 sin(pi/8) = {s_:.4f} over the four 8^3 estimates (chi, u printed in the cache): {[round(x, 3) for x in bd]}")
if PR == 9361:
    take("0.0036", abs((0.28861 - 0.28502) - 0.0036) < 6e-5, "0.28861 (8^3 reptation u, cache of PR 9352) - 0.28502 (this cache) = 0.00359")
if PR == 9365:
    take("0.0032", abs((0.2886 - 0.28537) - 0.0032) < 6e-5, "0.2886 - 0.28537 (both printed in this cache line) = 0.00323")

if PR == 9360:
    take("36051", 61 * 197 * 3 == 36051, "61 gates x 197 delays x 3 populations = 36051 (the table row of the same note)")
    from datetime import datetime as _dt
    def _t(tuid): d_, t_, ms_ = tuid.split("-")[:3]; return _dt.strptime(d_ + t_, "%Y%m%d%H%M%S").timestamp() + int(ms_) / 1000.0
    take("55.815", abs((_t("20220920-215202-730") - _t("20220920-210206-915")) - (49 * 60 + 55.815)) < 1e-6, "TUIDs: 21:52:02.730 (calibration) - 21:02:06.915 (echo) = 49 min 55.815 s")
if PR == 9008:
    _el = re.findall(r"elapsed_sec: ([\d.]+)", cache_raw)
    _stdout_len = len(cache_raw.split("----- stdout -----\n", 1)[-1].split("\n----- stderr")[0].strip("\n"))
    take("18", bool(_el) and abs(float(_el[0]) / 60 - 18) < 0.6, f"cache elapsed_sec = {_el[0] if _el else 'n/a'} s = {float(_el[0])/60 if _el else 0:.1f} min")
    take("1454", abs(_stdout_len - 1454) <= 3, f"length of the cached stdout = {_stdout_len} characters (the note says 1454)")
for k in ("STRUCT", "CACHE", "RUNNER", "DERIVED", "REF"):
    print(f"[{k}] {len(res[k])} tokens")
for s, c in res["DERIVED"] + res["REF"]: print(f"   [DERIVED/REF] {s} | ...{c}")
for s, c in res["UNC"]: print(f"[UNCOVERED] {s} | ...{c}...")
res["UNC_ALL"] = res["UNC"]
print(f"[COVERAGE] {len(toks)} numeric tokens; struct {len(res['STRUCT'])}, cache {len(res['CACHE'])}, runner {len(res['RUNNER'])}, derived {len(res['DERIVED'])}, cited-PR cache {len(res['REF'])}, uncovered {len(res['UNC'])}")
for h_ in extra_hits: print("HIT:", h_)
_unc = [(s_, c_) for s_, c_ in res["UNC"] if not s_.startswith("HIT:")]
if _unc:
    print("HIT: numbers with no printed value, runner constant or derivation: " + "; ".join(f"{s_} ({c_[30:90].strip()})" for s_, c_ in _unc[:12]))
print(f"SUMMARY: {len(toks)} numeric tokens of the note: structural {len(res['STRUCT'])}, printed in the cache {len(res['CACHE'])}, runner constants {len(res['RUNNER'])}, derived from printed pairs {len(res['DERIVED'])}, printed by a cited open PR's cache {len(res['REF'])}; unsourced {len(res['UNC'])}")
sys.exit(0)
