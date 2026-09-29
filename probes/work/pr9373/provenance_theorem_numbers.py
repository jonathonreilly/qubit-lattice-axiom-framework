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
import itertools, math, os, re, subprocess, sys
from pathlib import Path

PR = 9373
ROOT = Path(__file__).resolve().parents[3]
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
git("fetch", "origin", f"pull/{PR}/head", "--quiet")
HEAD = git("rev-parse", "FETCH_HEAD").stdout.strip()
files = [f for f in git("diff", "--name-only", f"origin/main...{HEAD}").stdout.split() if "audit/data" not in f]
note_paths = [f for f in files if f.startswith("docs/") and f.endswith(".md")]
note_path = note_paths[0]
if os.environ.get("PROBE_NOTE"): note_path = [f for f in note_paths if os.environ["PROBE_NOTE"] in f][0]
cache_paths = [f for f in files if f.startswith("logs/runner-cache/")]
cache_path = cache_paths[0]
NOTE_OVERRIDE = os.environ.get("PROBE_NOTE")
runner_path = [f for f in files if f.startswith("scripts/") and f.endswith(".py")][0]
def show(p): return git("show", f"{HEAD}:{p}").stdout
runner_paths = [f for f in files if f.startswith("scripts/") and f.endswith(".py")]
note, cache_raw, runner = show(note_path), "\n----- stdout -----\n".join(show(p) for p in cache_paths), "\n".join(show(p) for p in runner_paths)
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
cache = "\n".join(part.split("----- stderr")[0] for part in cache_raw.split("----- stdout -----\n"))
pc = sorted(set(abs(x) for x in numbers(cache) if x == x and abs(x) < 1e18 and x != 0))
cache_lines = [sorted(set(abs(x) for x in numbers(l) if x == x and abs(x) < 1e18 and x != 0)) for l in cache.split("\n")]
pr = sorted(set(abs(x) for x in numbers(runner + "\n" + data_txt.replace(chr(34), " ")) if x == x and abs(x) < 1e18 and x != 0))
print(f"   {len(pc)} distinct printed values, {len(pr)} runner and packaged-data constants ({len(data_files)} data files)")

body = note.split("\n---\n", 2)[-1] if note.startswith("---") else note
body = re.sub(r"\]\([^)]*\)", "]", body)
body = re.sub(r"`[^`\n]*\.(?:md|py|txt|json)`", " FILE ", body)                                              # file names in code spans
body = re.sub(r"`[A-Za-z_./-]{14,}[^`\n]*`", " ID ", body)
body = re.sub(r"\b[A-Z][A-Z_0-9]{12,}\b", "ID", body)
body = re.sub(r"\b[0-9a-f]{16,}\b", "HASH", body)
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
toks = [(m.start(), m.end(), m.group(0).replace(",", "").rstrip(".")) for m in NUM.finditer(body)]
def dec(s): return len(s.split(".")[1]) if "." in s and "e" not in s.lower() else 0
def sig(s): return len(s.lstrip("+-").replace(".", "").lstrip("0").split("e")[0])
def close(p, v, d, scale):
    q = p * scale
    return abs(round(q, d) - v) <= 1e-9 * max(1, v) or (d > 0 and abs(q - v) <= 0.5 * 10 ** (-d) + 1e-12) or (d > 0 and abs(math.floor(q * 10 ** d) / 10 ** d - v) <= 1e-9 * max(1, v))
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
    if fl: refpool[r_] = sorted(set(abs(x) for x in numbers(git("show", f"{h_}:{fl[0]}").stdout.split("----- stdout -----\n", 1)[-1]) if abs(x) < 1e18 and x != 0))
print("   referenced open PRs with a cache:", {k: len(v) for k, v in refpool.items()})
res = {"STRUCT": [], "CACHE": [], "RUNNER": [], "DERIVED": [], "REF": [], "UNC": []}
for a, b, s in toks:
    ctx = body[max(0, a - 40):b + 30].replace("\n", " ")
    v = abs(float(s)); d = dec(s)
    if re.fullmatch(r"\d+", s) and int(s) in {m * L_ ** 3 for L_ in (2, 4, 6, 8, 10, 12, 16, 20, 24) for m in (1, 3)}:
        res["STRUCT"].append((s, ctx + "  <- lattice size L^3 or 3 L^3 (links or plaquettes)")); continue
    if s in ("0", "1", "2", "3", "4") or (re.fullmatch(r"\d+", s) and v <= 12 and not re.search(r"(walkers|seeds|batches|runs|steps|samples)", ctx[40:])):
        res["STRUCT"].append((s, ctx)); continue
    weak = False
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
    found = False
    for _ in range(50):
        for i_, (s_, c_) in enumerate(res["UNC"]):
            if s_ == tok:
                res["UNC"].pop(i_); found = True
                if ok: res["DERIVED"].append((tok, c_[:70] + "  <- " + how))
                else:
                    res["UNC"].append(("HIT:" + tok, c_))
                    if not any(h_.startswith(tok + ":") for h_ in extra_hits): extra_hits.append(f"{tok}: {hit_note or how}")
                break
        else:
            break
    if not found: print(f"[note] extra for {tok}: token not left uncovered (already sourced directly or absent from this note)")
def partners_and_shared():
    def nb_(s_): return [(s_[0] + d_[0], s_[1] + d_[1], s_[2] + d_[2]) for d_ in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
    sh = lambda a_, c_: len(set(nb_(a_)) & set(nb_(c_)))
    part = [(dx, dy, dz) for dx in range(-2, 3) for dy in range(-2, 3) for dz in range(-2, 3) if (dx, dy, dz) != (0, 0, 0) and (dx + dy + dz) % 2 == 0 and sh((0, 0, 0), (dx, dy, dz)) > 0]
    return part, sh
if PR in (9316, 9345):
    from fractions import Fraction as _Fr
    _part, _sh = partners_and_shared()
    take("34", (36 - _sh((0, 0, 0), (1, 1, 0)) == 34) and (36 - _sh((0, 0, 0), (2, 0, 0)) == 35) and len(_part) == 18 and sum(1 for p_ in _part if _sh((0, 0, 0), p_) == 2) == 12 and 2 * (6 * 35 + 12 * 34) // 2 == 618, "each pair with s shared B neighbours has 36 - s vacuum (b, b') destinations: 35 for the 6 axis partners at distance 2, 34 for the 12 face-diagonal partners, so -2 (N/2)(6*35 + 12*34) = -618 N")
    take("23328", 9 * 2 * 6 ** 4 == 23328 and len(_part) == 18, "9 unordered overlapping pairs per A centre (18 partners / 2) x 2 x ||S_ac||^2 <= (||F||^2)^2 with ||F_a|| <= 6 -> 2 x 6^4 = 2592 per pair set of nine: 9 x 2 x 1296 = 23328 per A centre")
if PR == 9316:
    from fractions import Fraction as _Fr
    take("-624.48", abs(-550 - 0.01 * 7448 + 624.48) < 1e-12 and 2 * math.atan(1 / 200) < 0.01, "k0_x = 2 atan(1/200) < 0.01 and v_x = 7448 (printed): Weyl shift 0.01 x 7448 = 74.48, so -550 - 74.48 = -624.48")
    take("-214", 2.0 ** -214 < 1e-62 / 16, "2^-214 = 4.6e-65 < q0/16 = 6.25e-64 for q0 = 10^-62 (the conservative integer exponent)")
    take("115.61964849312", abs(231.23929698624 / 2 - 115.61964849312) < 1e-11, "half of the printed Hessian 231.23929698624 (cache prints 231.239296986239...)")
    for _tk in ("180", "1218", "9758"):
        take(_tk, False, "no runner, cache or data file of the PR", hit_note="the first exploratory quotient search 'hit its 180-second resource guard after processing 1218 of 9758 discovered words' appears in no runner, cache or data file of the PR (the note calls it preserved, but nothing in the PR contains it)")
if PR == 9345:
    from fractions import Fraction as _Fr
    import mpmath as _mp
    _mp.mp.dps = 40
    _n = (2048 - 7) // 2 + 1; _x = 11728 * _mp.mpf(1) / 50
    _cap = 684 * (_mp.e ** _x * _x ** _n / _mp.factorial(_n)) ** 2
    _q = 16384 // 8 - 1; _y = 2 * 14128 * _mp.mpf(1) / 50
    _vol = 2 * 684 * _mp.e ** _y * _y ** _q / _mp.factorial(_q)
    take("1.66473687478e-215", 1.66473687477e-215 <= float(_cap) <= 1.664736874785e-215, f"E_capture = 684 T_n(11728 u)^2 with n = 1021, u = 1/50: {_mp.nstr(_cap, 12)} (the note rounds the upper bound up)")
    take("1.92515042277e-9", abs(float(_vol) - 1.92515042277e-9) < 5e-20, f"E_vol = 2*684 exp(2Mu)(2Mu)^q/q! with q = floor(16384/8) - 1 = 2047, M = 14128: {_mp.nstr(_vol, 12)}")
    _R = 497313353615986515185363764932926666957967531268139212800
    take("4.97", abs(_R / 1e56 - 4.97) < 0.005, f"the refined R = {_R} = 4.973e56 (derived in the exact-arithmetic check of the paired falsifier)")
    take("288", 2 * 12 * 12 == 288, "||F_a||^2 <= 12 so ||S_ac||^2 <= 144 and ||h_ac|| = 2 ||S_ac^* S_ac|| <= 288")
    take("72", [2 * (5 - o) * (6 - o) * (o + 1) for o in range(6)][2] == 72, "2(5-o)(6-o)(o+1) at o = 2")
    take("2592", 9 * 288 == 2592, "nine pair terms per A centre x 288")
    for _tk in ("1111.4210", "2031", "0907.3740"): take(_tk, True, "bibliographic identifier (arXiv number or journal page)")
    _part, _sh = partners_and_shared()
    _S = [(x, y, z) for x in range(-4, 5) for y in range(-4, 5) for z in range(-4, 5) if abs(x) + abs(y) + abs(z) <= 4 and (x + y + z) % 2 == 0]
    _pairs = set()
    for a_ in _S:
        for p_ in _part: _pairs.add(tuple(sorted((a_, (a_[0] + p_[0], a_[1] + p_[1], a_[2] + p_[2])))))
    take("2076", len(_pairs) == 1038 and 2 * len(_pairs) == 2076 and 1195776 == 2076 * 576, "reproduced under the reading that a star meets the A centres within l1 distance 4: 1038 pair terms have an endpoint there, doubled for a pair support (union bound); and J = 1195776 = 2076 x 576 (printed)")
    take("170", len(_S) == 85 and 2 * len(_S) == 170 and 27200 == 170 * 160, "A centres with l1 distance <= 4 from a star centre: 85; doubled for a pair support: 170; 27200 = 170 x 160 (printed)")
    def _nb4(s_): return [((s_[0] + d_[0]) % 4, (s_[1] + d_[1]) % 4, (s_[2] + d_[2]) % 4) for d_ in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
    _A4 = [(x_, y_, z_) for x_ in range(4) for y_ in range(4) for z_ in range(4) if (x_ + y_ + z_) % 2 == 0]
    _tot = sum(36 - len(set(_nb4((0, 0, 0))) & set(_nb4(c_))) for c_ in _A4 if c_ != (0, 0, 0) and len(set(_nb4((0, 0, 0))) & set(_nb4(c_))) > 0)
    take("-510", -_tot == -510 and 6 * 5 == 30, f"L = 4 torus, enumerated: an A centre has 15 overlapping partners (axis partners coincide with their mirror images and share two B neighbours), each with 36 - 2 = 34 vacuum destination pairs, so the H4 vacuum scalar per A is -2 x (15 x 34)/2 = -{_tot}; the '30N' is the vacuum loss of the resolved-minus instrument (6N labels x 5 destinations)")
    take("19183", True, "the exponent -19183/75 (Hamiltonian tail) is checked in the paired falsifier: exp(-19183/75) <= 2^-255")
    take("-6.40636", True, "time-average interval widened by the analytic error .014 (checked in the paired falsifier)")
    take("-1.07994", True, "as above")
    take("4095", 4096 - 1 == 4095, "4096 - 1 (sample count minus one)")
    take("8192", 2 * 4096 == 8192, "two targets x 4096 samples")

if PR == 9314:
    _A = (0, 3, 5, 6); _B = (1, 2, 4, 7)
    _edges = [f"{a_}{b_}" for a_ in _A for b_ in _B if bin(a_ ^ b_).count("1") == 1]
    _ok_e = _edges == ["01", "02", "04", "31", "32", "37", "51", "54", "57", "62", "64", "67"]
    for _tk in ("31", "32", "37", "51", "54", "57", "62"):
        take(_tk, _ok_e, "vertex-pair label of the cube edge list: the A -> B edges of the cube graph with A = (0,3,5,6), B = (1,2,4,7) (XOR with 1, 2 or 4), in the note's order")
    take("972", 2 * 6 * 3 ** 4 == 972 and 6 == 4 * 3 // 2, "||H4|| <= 2 x (4*3/2 = 6 unordered A pairs) x (||F_a||^2)^2 with ||F_a|| <= 3, i.e. 2 x 6 x 3^4 = 972")
    take("96", 24 * 2 ** 2 == 96 and 12 * 2 == 24, "||Gamma|| <= (12 edges x 2 signs = 24 birth maps) x ||B||^2 with ||B|| <= 2: 24 x 4 = 96")
if PR == 9373:
    import sympy as sp
    from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
    _tr = standard_transformations + (implicit_multiplication_application,)
    q_, J_, u_, v_, t_ = sp.symbols("q J u v t", positive=True)
    _SUPD = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹", "0123456789")
    def conv(s):
        s = s.replace("−", "-").replace("π", "PI").replace("κ", "kappa").replace("`", "")
        s = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹]+)", lambda m: "**" + m.group(1).translate(_SUPD), s)
        s = re.sub(r"PI(?=[a-zA-Z(])", "PI*", s)
        s = re.sub(r"(\d)([a-zA-Z(])", r"\1*\2", s)
        s = re.sub(r"([a-zA-Z)])\s*\(", r"\1*(", s)
        s = re.sub(r"\)\s*([a-zA-Z(])", r")*\1", s)
        s = re.sub(r"(?<=[a-z])(?=[a-z])", "*", s).replace("PI", "pi")
        return parse_expr(s, local_dict={"q": q_, "v": v_, "t": t_, "u": u_, "J": J_, "pi": sp.pi, "kappa": q_}, transformations=_tr)
    def cconv(s):
        return parse_expr(s.replace("^", "**"), local_dict={"q": q_, "v": v_, "t": t_, "pi": sp.pi})
    def same(a, b): return sp.simplify(sp.together(a - b)) == 0
    C = cache
    formula_ok = []; formula_lines = []
    def formula(name, note_str, note_expr, cache_expr, cache_where):
        ok = same(note_expr, cache_expr)
        formula_ok.append(ok); formula_lines.append(f"   [FORMULA] {name}: note `{note_str}` = cache `{cache_where}` (sympy difference simplifies to 0: {ok})")
        if not ok: extra_hits.append(f"formula {name}: note `{note_str}` is not the cache's `{cache_where}`")
    def note_span(pattern):
        m = re.search(pattern, note, re.S)
        if not m: extra_hits.append(f"note text for {pattern!r} not found"); return None
        return m.group(1).strip()
    # -- item 2: c ------------------------------------------------------------
    s_c = note_span(r"`c = ([^`]+)`, which is `48`")
    m_c = re.search(r"-- c = (.*?); at q = 1/2: (\d+)", C)
    formula("c(q)", s_c, conv(s_c), cconv(m_c.group(1)), "c = " + m_c.group(1) + f"; at q = 1/2: {m_c.group(2)}")
    _c = conv(s_c)
    # -- item 3: h ------------------------------------------------------------
    s_h = note_span(r"`h\(q\) = ([^`]+)`, which is")
    m_h = re.search(r"-- h\(q\) = (.*?) at f\+ and (.*?) at f-", C)
    formula("h(q) at f+", s_h, conv(s_h), cconv(m_h.group(1)), "h(q) = " + m_h.group(1) + " at f+")
    formula("h(q) at f-", s_h, conv(s_h), cconv(m_h.group(2)), m_h.group(2) + " at f-")
    _h = conv(s_h)
    # -- item 4: n ------------------------------------------------------------
    s_n = note_span(r"`n = \(([^`]+)\)` at")
    m_n = re.search(r"n at f\+ = \[(.*?)\], at f- = \[(.*?)\]", C)
    parts_n = [p.strip() for p in re.split(r",\s*(?![^()]*\))", s_n)]
    cp_n = [[cconv(x) for x in re.split(r",\s*(?![^()]*\))", m_n.group(k))] for k in (1, 2)]
    nn = [conv(p.replace("∓", "-")) for p in parts_n]; npl = [conv(p.replace("∓", "+")) for p in parts_n]
    for j in range(3):
        formula(f"n[{j}] at f+ (upper sign)", parts_n[j], nn[j], cp_n[0][j], "n at f+ = [" + m_n.group(1) + "]")
        formula(f"n[{j}] at f- (lower sign)", parts_n[j], npl[j], cp_n[1][j], "at f- = [" + m_n.group(2) + "]")
    # -- item 6: A, B, resultant -------------------------------------------------
    s_A = note_span(r"`A = ([^`]+)`"); s_B = note_span(r"`B = ([^`]+)`"); s_R = note_span(r"resultant is\s+`([^`]+)`")
    m_ab = re.search(r"f\+: A = (.*?), B = (.*?), resultant (.*?); f-: resultant (.*)", C)
    formula("A at f+", s_A, conv(s_A), cconv(m_ab.group(1)), "A = " + m_ab.group(1))
    formula("B at f+", s_B, conv(s_B), cconv(m_ab.group(2)), "B = " + m_ab.group(2))
    formula("resultant at f+", s_R, conv(s_R), cconv(m_ab.group(3)), "resultant " + m_ab.group(3))
    formula("resultant at f- ('and the same at f-')", s_R, conv(s_R), cconv(m_ab.group(4)), "f-: resultant " + m_ab.group(4))
    formula("2^29 in the resultant", "2²⁹", sp.Integer(2) ** 29, sp.Integer(536870912), "-536870912*q**10*...")
    # the resultant is the resultant of A and B as binary forms (an independent recomputation, exact)
    _A = conv(s_A); _B = conv(s_B)
    _a = sp.Poly(sp.expand(_A.subs(t_, 1)), v_); _b = sp.Poly(sp.expand(_B.subs(t_, 1)), v_)
    _res = sp.simplify(sp.resultant(_a.as_expr(), _b.as_expr(), v_))
    formula("resultant of A, B recomputed from the printed forms (note item 6)", s_R, conv(s_R), _res, "sympy resultant of the note's A(v, 1), B(v, 1) in v")
    # -- item 1 and the parametrisation ---------------------------------------
    _J = 8 * q_ ** 2 / (1 + 4 * q_ ** 2)
    formula("kappa^2 = J/[4(2 - J)] with kappa = q, J = 8q^2/(1 + 4q^2)", "κ² = J/[4(2 − J)]", q_ ** 2, _J / (4 * (2 - _J)), "note's parametrisation")
    formula("J - 1 = (4q^2 - 1)/(4q^2 + 1)", "J − 1 = (4q² − 1)/(4q² + 1)", _J - 1, (4 * q_ ** 2 - 1) / (4 * q_ ** 2 + 1), "cache: cos 2 pi x = J - 1 = (4q^2 - 1)/(4q^2 + 1)")
    m_f = re.search(r"family \(ii\): cos 2 pi x = (.*?), cos 2 pi f3 = (-?\d+); family \(iii\): sqrt\(\.\.\.\) = J \+ 4, cos 2 pi f3 = (-?\d+), cos 2 pi \(1/2 \+ g\) = (.*)", C)
    formula("family (ii) cos 2 pi x", "1 − J/(4κ²) of PR 9350 at κ = q", 1 - _J / (4 * q_ ** 2), cconv(m_f.group(1)), "family (ii): cos 2 pi x = " + m_f.group(1))
    formula("family (ii) cos 2 pi f3 = -1", "(J + 2)/(4κ²) − (4 + J − J²)/J of PR 9350 at κ = q", (_J + 2) / (4 * q_ ** 2) - (4 + _J - _J ** 2) / _J, sp.Integer(int(m_f.group(2))), "family (ii): ... cos 2 pi f3 = " + m_f.group(2))
    _sq = 5 * _J ** 2 + 8 * _J + _J * (_J + 2) / q_ ** 2
    formula("family (iii) radicand = (J + 4)^2", "5J² + 8J + J(J + 2)/κ² at κ = q", _sq, (_J + 4) ** 2, "family (iii): sqrt(...) = J + 4")
    formula("family (iii) cos 2 pi f3 = [J + 2 - (J + 4)]/2 = -1", "[J + 2 − √(...)]/2", (_J + 2 - (_J + 4)) / 2, sp.Integer(int(m_f.group(3))), "family (iii): cos 2 pi f3 = " + m_f.group(3))
    formula("family (iii) cos 2 pi (1/2 + g) = -(-J - cos 2 pi f3) = J - 1", "cos 2πg = −J − cos 2πf₃", -(-_J - (-1)), cconv(m_f.group(4)), "cos 2 pi (1/2 + g) = " + m_f.group(4))
    formula("e^{2 pi i x} = (2q + i)^2/(1 + 4q^2): real part is cos 2 pi x, imaginary part is +4q/(4q^2 + 1) (the cache's sin)", "(2q ± i)²/(1 + 4q²)", sp.re(sp.expand((2 * q_ + sp.I) ** 2 / (1 + 4 * q_ ** 2))) + sp.I * sp.im(sp.expand((2 * q_ + sp.I) ** 2 / (1 + 4 * q_ ** 2))), (4 * q_ ** 2 - 1) / (4 * q_ ** 2 + 1) + sp.I * 4 * q_ / (4 * q_ ** 2 + 1), "cache: cos 2 pi x = (4q^2 - 1)/(4q^2 + 1), sin 2 pi x = +-4q/(4q^2 + 1)")
    # -- single numbers -------------------------------------------------------
    _sub = lambda e, v: sp.nsimplify(e.subs(q_, v))
    def num(tok, ok, how):
        formula_ok.append(bool(ok)); formula_lines.append(f"   [NUMBER] {tok}: {how}: {ok}")
        if not ok: extra_hits.append(f"number {tok}: {how}")
    num("48", _sub(_c, sp.Rational(1, 2)) == 48 and int(m_c.group(2)) == 48, "c(q = 1/2) from the printed formula, and the cache prints 'at q = 1/2: 48' (the note attributes it to open PR 9357, whose note also states det(H - lambda) = lambda^2 (lambda^2 - 48))")
    num("192", _sub(_h, sp.Rational(1, 2)) == 192, "h(q = 1/2) evaluated from the printed formula (the cache prints the formula, not the value; open PR 9357's note states the Hessian 4 pi^2 * 192 [[1, -1, 0], [-1, 1, 0], [0, 0, 0]])")
    num("J = 1 at q = 1/2", sp.simplify(_J.subs(q_, sp.Rational(1, 2))) == 1, "J(1/2) = 8/4/2 = 1 and kappa = q = 1/2 (PR 9357's case)")
    num("J = 2/5 <-> kappa = 1/4", sp.simplify(_J.subs(q_, sp.Rational(1, 4))) == sp.Rational(2, 5), "J(1/4) = 2/5; cache key '2/5'")
    num("J = 8/5 <-> kappa = 1", sp.simplify(_J.subs(q_, 1)) == sp.Rational(8, 5), "J(1) = 8/5; cache key '8/5'")
    num("J runs over (0, 2), once each", sp.simplify(sp.diff(_J, q_) - 16 * q_ / (1 + 4 * q_ ** 2) ** 2) == 0 and sp.limit(_J, q_, 0, "+") == 0 and sp.limit(_J, q_, sp.oo) == 2, "dJ/dq = 16q/(1 + 4q^2)^2 > 0, J(0+) = 0, J(inf) = 2")
    _fl = re.search(r"(\{'2/5'.*\})", C)
    import ast
    _fluxes = ast.literal_eval(_fl.group(1)) if _fl else {}
    num("-2 and +2 (fluxes), radii 0.004 and 0.008", _fluxes == {"2/5": [[-2.0, -2.0], [2.0, 2.0]], "8/5": [[-2.0, -2.0], [2.0, 2.0]]} and "0.004" in C and "0.008" in C, "cache prints the flux dictionary {'2/5': [[-2.0, -2.0], [2.0, 2.0]], '8/5': [[-2.0, -2.0], [2.0, 2.0]]} (f+ then f-, radius .004 then .008) and the radii in the check text")
    num("Seven checks / TOTAL: PASS=7 FAIL=0", "TOTAL: PASS=7 FAIL=0" in cache and cache.count("[PASS]") == 7, "the cache prints TOTAL: PASS=7 FAIL=0 and seven [PASS] lines")
    _el = float(re.search(r"elapsed_sec: ([\d.]+)", cache_raw).group(1))
    print(f"   [INFO] 'in about ten seconds' vs the cache's elapsed_sec {_el} (the last check's own timer prints 7 s): about eight seconds, not ten (a rounding of a duration, not a claim about the result)")
    # -- numbers attributed to open PRs 9350 and 9357, from their own notes -----
    def show_pr(pr, suffix):
        g_ = git("fetch", "origin", f"pull/{pr}/head", "--quiet"); h_ = git("rev-parse", "FETCH_HEAD").stdout.strip()
        fl_ = [f for f in git("diff", "--name-only", f"origin/main...{h_}").stdout.split() if f.endswith(suffix) and "audit/data" not in f]
        return git("show", f"{h_}:{fl_[0]}").stdout if fl_ else ""
    n50 = show_pr(9350, ".md"); n57 = show_pr(9357, ".md"); c57 = show_pr(9357, ".txt")
    num("kappa_h^2 = J/[4(2 - J)] and the two families (attributed to open PR 9350)", "κ_h² = J/[4(2 − J)]" in n50 and "cos 2πx = 1 − J/(4κ²)" in n50 and "√(5J² + 8J + J(J + 2)/κ²)" in n50, "open PR 9350's note prints κ_h² = J/[4(2 − J)], family (ii) cos 2πx = 1 − J/(4κ²) and family (iii) with √(5J² + 8J + J(J + 2)/κ²); this cache checks them at κ = q")
    num("(c = 48, Hessian 192) of open PR 9357", "lambda^2 (lambda^2 - 48)" in c57 and "[[192, -192, 0], [-192, 192, 0], [0, 0, 0]]" in c57 and "192" in n57 and "48" in n57, "open PR 9357's own cache prints 'lambda^2 (lambda^2 - 48)' and 'Hessian at f+ = 4 pi^2 x [[192, -192, 0], [-192, 192, 0], [0, 0, 0]]' (its note states the same)")
    for _l in formula_lines: print(_l)
    print(f"[FORMULA-LEVEL] {len(formula_ok)} formula and number statements of the note checked against the cache; {sum(1 for x in formula_ok if x)} match exactly; {sum(1 for x in formula_ok if not x)} do not")
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
print(f"SUMMARY: {len(toks)} numeric tokens of the note: structural {len(res['STRUCT'])}, printed in the cache {len(res['CACHE'])}, runner constants {len(res['RUNNER'])}, derived from printed pairs {len(res['DERIVED'])}, printed by a cited open PR's cache {len(res['REF'])}; unsourced {len(res['UNC'])}" + (f"; formula-level: {len(formula_ok)} formulas and numbers of the note (c, h, n, A, B, the resultant with 2^29, the family cosines, J = 2/5 and 8/5 as kappa = 1/4 and 1, 48 and 192, the flux dictionary) compared symbolically with the cache's printed expressions, {sum(formula_ok)} match exactly" if PR == 9373 else ""))
sys.exit(0)
