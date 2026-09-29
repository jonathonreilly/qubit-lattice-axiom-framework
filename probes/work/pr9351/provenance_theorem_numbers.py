#!/usr/bin/env python3
"""J:provenance:PR9351 -- every number in the theorem statements of the square microscopic spectral certificate note, located in the runner's cached stdout, the runner source, or an exact derivation.

Statement text = the front-matter claim_scope + the target paragraph ("The target is ... six interval bounds") + the whole "Six finite-case error certificates" section (parameters, table)
+ the two displayed statements of the reduction, equation (1) with R_m(E), and of the first-order coefficients, equation (2).  Every numeric token of that text (integers, decimals, fractions a/b,
1e-9 forms, number words) must fall inside one listed item:
  CACHE       printed by the PR's cached runner output (logs/runner-cache/square_microscopic_spectral_certificate_2026_09_27.txt at the PR head), re-parsed here as exact rationals -> sourced
  RUNNER      a constant of the runner source (scripts/square_microscopic_spectral_certificate_2026_09_27.py at the PR head)                                                         -> sourced
  DERIVED     an exact derivation stated in the note, re-executed here (sympy / exact Fractions)                                                                                      -> sourced
  DEFINITION  a constant of a declared object                                                                                                                                         -> not a claim
  (else)      HIT: no runner line, no cache line, no derivation in the note.
Tokens covered by no item are printed as UNCOVERED; a number the note attributes to another block would be INFO when that block's cache prints it (none here). Self-contained; reads the PR head via git.
"""
import json
import math
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PR = 9351
BRANCH = "physics-loop/measured-corrections-20260927"
NOTE = "docs/SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27.md"
RUNNER = "scripts/square_microscopic_spectral_certificate_2026_09_27.py"
CACHE = "logs/runner-cache/square_microscopic_spectral_certificate_2026_09_27.txt"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def head():
    git("fetch", "origin", BRANCH, "--quiet")
    r = git("rev-parse", f"origin/{BRANCH}")
    if r.returncode != 0:
        raise SystemExit("cannot resolve the PR branch: " + r.stderr.strip())
    return r.stdout.strip()


HEAD = head()


def show(path):
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {HEAD}: {r.stderr.strip()}")
    return r.stdout


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    for a, b in (("−", "-"), ("≥", ">="), ("≤", "<="), ("·", "*"), ("²", "^2"), ("√", "sqrt")):
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


def statement_pieces(note):
    fm = note.split("\n---\n", 1)[0]
    cs = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M).group(1)
    secs = {s.split("\n", 1)[0].strip(): s for s in re.split(r"^## ", note, flags=re.M)[1:]}
    p = secs["Premises and exact target"]
    i = p.index("The target is"); target = p[i:p.index("\n\n", i)]
    cert = secs["Six finite-case error certificates"]
    red = secs["Exact reduction and global spectral indexing"]
    a = red.index("    E(1+4x-lambda)"); eq1 = red[a:red.index("(1)\n", a) + 3]
    fc = secs["First correction: formal coefficient with hypotheses retained"]
    b = fc.index("    H0(n,n)"); eq2 = fc[b:fc.index("(2)\n", b) + 3]
    out = [("claim_scope", cs), ("target paragraph", target), ("Six finite-case error certificates", cert), ("equation (1) and R_m(E)", eq1), ("equation (2)", eq2)]
    res = []
    for name, t in out:
        t = norm(re.sub(r"\s+", " ", t))
        t = re.sub(r"(?<=[a-z]{2})(?=\d)", " ", t)              # 'or15803623/500000', 'width2e-9' -> separate the glued number
        res.append((name, t))
    return res


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+e-\d+|\d+/\d+|\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|half|quarter|single|pair|first|second)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


# ------------------------------------------------------------------------------------------------ the cache, re-parsed
def load_cache():
    raw = show(CACHE)
    body = raw.split("----- stdout -----\n", 1)[1]
    js = body.split("\nTOTAL:", 1)[0]
    lines = body.splitlines()
    return json.loads(js), lines


def cache_line(lines, needle):
    for i, l in enumerate(lines):
        if needle in l:
            return i + 1
    return None


def cache_facts(C, lines):
    cases = C["cases"]
    return cases


# ------------------------------------------------------------------------------------------------ derivations
def derive_eq1():
    """The tridiagonal entries of Z^T R^-1 Z from Z|n> = 2[d_(n-1)|n-1> + d_n|n>] and the elimination constants, plus a numerical check of (1) against the explicit full matrix (S = 20)."""
    n, dm1, d0, R1, R0 = sp.symbols("n dm1 d0 R1 R0")
    Z = sp.Matrix([[2 * sp.Symbol(f"a{i}") if j == i else 0 for j in range(2)] for i in range(2)])       # placeholder for shape
    z = sp.Matrix(3, 2, lambda i, j: 0)
    dd = sp.symbols("d_a d_b")                     # window: m in {a, b}, n in {a, b, c}: Z[m=a, n=a] = 2 d_a, Z[a, a+1] = 2 d_a, Z[b, a+1] = 2 d_b, Z[b, a+2] = 2 d_b
    d_a, d_b, R_a, R_b = sp.symbols("d_a d_b R_a R_b", positive=True)
    Zm = sp.Matrix([[2 * d_a, 2 * d_a, 0], [0, 2 * d_b, 2 * d_b]])
    G = Zm.T * sp.diag(1 / R_a, 1 / R_b) * Zm
    ok = (sp.simplify(G[1, 1] - 4 * (d_a ** 2 / R_a + d_b ** 2 / R_b)) == 0 and sp.simplify(G[0, 1] - 4 * d_a ** 2 / R_a) == 0 and sp.simplify(G[1, 2] - 4 * d_b ** 2 / R_b) == 0)
    # constants of R and the scalar: at lam = 0 R = 2 - 4x d (the 1 - lam, 2 - lam factors) and the metric 1 + 4x - lam
    x, lam, d = sp.symbols("x lam d")
    ok &= sp.expand((1 - lam) * (2 - lam) - 4 * x * d - (2 - 3 * lam + lam ** 2 - 4 * x * d)) == 0
    # numerical: roots of the reduced equation against the explicit full matrix (S = 20, K = delta = 1), first three levels
    import numpy as np
    from scipy.linalg import eigh, eigvalsh_tridiagonal
    import itertools
    S, K, delta = 20, 1.0, 1.0
    C = S * (S + 1); xv = delta / (K * C)
    states = []
    for q in itertools.product((0, 1), repeat=4):
        if sum(q) != 2:
            continue
        for nn in range(-S, S + 1):
            E = (nn, q[0] - 1 - nn, -q[1] - nn, q[2] - 1 + q[1] + nn)
            if all(-S <= e <= S for e in E):
                states.append((q, E))
    idx = {s_: i for i, s_ in enumerate(states)}
    H = np.zeros((len(states), len(states)))
    edges = [(0, 1), (0, 3), (2, 1), (2, 3)]
    for i, (q, E) in enumerate(states):
        W = sum(1 - q[a] for a in (0, 2))
        H[i, i] += delta / xv ** 2 * W + (delta / xv ** 2 * xv * 4 if W == 0 else 0)
        for k, (a, b) in enumerate(edges):
            if q[a] == 1 and q[b] == 0:
                a2 = 1 - E[k] * (E[k] - 1) / C
                if a2 > 1e-14:
                    q2 = list(q); q2[a] = 0; q2[b] = 1; E2 = list(E); E2[k] -= 1
                    j = idx[(tuple(q2), tuple(E2))]
                    t = -delta / xv ** 1.5 * np.sqrt(a2)
                    H[i, j] += t; H[j, i] += t
    ev = eigh(H, eigvals_only=True, subset_by_index=(0, 2))

    def count(Ev):
        lamv = xv * xv * Ev / delta
        m = np.arange(-S, S); dm = 1 - m * (m + 1) / C
        Rv = (1 - lamv) * (2 - lamv) - 4 * xv * dm
        dg = 4 * K * np.arange(-S, S + 1).astype(float) ** 2 - Ev * (1 + 4 * xv - lamv)
        q_ = 4 * delta * dm ** 2 / Rv
        dg[m + S] -= q_; dg[m + S + 1] -= q_
        return int((eigvalsh_tridiagonal(dg, -q_) < 0).sum())
    ok &= all(count(e - 1e-7) == j and count(e + 1e-7) == j + 1 for j, e in enumerate(ev))
    return ok, ("Z^T R^-1 Z has entries 4[d_(n-1)^2/R_(n-1) + d_n^2/R_n] and 4 d_n^2/R_n (sympy on a window), (1 - lam)(2 - lam) - 4x d expands as written, and the inertia count of F at E_j -+ 1e-7 "
                "is j, j + 1 for the lowest three levels of the explicit full S = 20 matrix built from the parent's definitions")


def derive_eq2():
    n, x, K, dl, E = sp.symbols("n x K delta E")
    C = dl / (K * x)
    d = lambda m: 1 - m * (m + 1) / C
    lam = x ** 2 * E / dl
    R = lambda m: (1 - lam) * (2 - lam) - 4 * x * d(m)
    diag = 4 * (d(n - 1) ** 2 / R(n - 1) + d(n) ** 2 / R(n)); adj = 4 * d(n) ** 2 / R(n)
    sc = 1 + 4 * x - lam
    Hd = sp.series((4 * K * n ** 2 - dl * diag) / sc, x, 0, 2).removeO()
    Ha = sp.series((-dl * adj) / sc, x, 0, 2).removeO()
    ok = sp.simplify(Hd - ((4 * K * n ** 2 - 4 * dl) + x * (8 * dl - 8 * K * n ** 2))) == 0 and sp.simplify(Ha - (-2 * dl + x * (4 * dl + 4 * K * n * (n + 1)))) == 0
    return ok, "series of (1) to first order in x at fixed n gives H0(n,n) = 4Kn^2 - 4 delta, H0(n+1,n) = -2 delta, H1(n,n) = 8 delta - 8 K n^2, H1(n+1,n) = 4 delta + 4 K n(n + 1) (sympy)"


# ------------------------------------------------------------------------------------------------ items
def main():
    note = show(NOTE)
    runner = show(RUNNER)
    C, clines = load_cache()
    cases = C["cases"]
    pieces = statement_pieces(note)
    covered = {name: set() for name, _ in pieces}
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(clines)} stdout lines, {len(cases)} cases; statement pieces: {', '.join(n for n, _ in pieces)}")
    out = {"CACHE": 0, "RUNNER": 0, "DERIVED": 0, "DEFINITION": 0, "HIT": 0}
    hits = []

    def cover(pat):
        n_ = 0
        for name, text in pieces:
            for m in re.finditer(pat, text, flags=re.I):
                covered[name].update(range(m.start(), m.end())); n_ += 1
        return n_

    def item(iid, pat, kind, ok, source):
        n_ = cover(pat)
        if n_ == 0:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            return
        if ok:
            out[kind] += 1
            print(f"[{kind}] {iid} | {source}")
        else:
            out["HIT"] += 1
            hits.append(f"HIT: {iid} | {source}")

    Ks = {c["K"] for c in cases}; Ds = [c["delta"] for c in cases]; Ss = [c["S"] for c in cases]
    item("K", r"K=1", "RUNNER", "K=F(1)" in runner.replace(" ", "") and Ks == {"1"}, f"runner K=F(1); cache lines {cache_line(clines, chr(34) + 'K' + chr(34) + ': ' + chr(34) + '1' + chr(34))}: K = 1 in all {len(cases)} cases")
    d2 = Fr("31.607246")
    item("delta values", r"delta=1 or 15803623/500000|\b31\.607246\b|\bdelta=1\b|\b15803623/500000", "CACHE",
         set(Ds) == {"1", str(d2)} and d2 == Fr(15803623, 500000) and "F('31.607246')" in runner.replace('"', "'"),
         f"runner F(1), F('31.607246'); cache delta strings {sorted(set(Ds))}; 31.607246 = 15803623/500000 exactly (Fractions)")
    item("S values", r"S=20,50,120", "CACHE", sorted(set(Ss)) == [20, 50, 120] and "(20,50,120)" in runner.replace(" ", ""),
         f"runner 'for S in (20,50,120)'; cache S = {sorted(set(Ss))} for each delta")
    xs = [Fr(c["x"]) for c in cases]
    item("x below 1/4", r"Every required x is below 1/4|below 1/4|1/4", "CACHE", all(v < Fr(1, 4) for v in xs) and all(Fr(c["x"]) == Fr(c["delta"]) / (Fr(c["K"]) * c["S"] * (c["S"] + 1)) for c in cases),
         f"cache x = delta/(K S(S+1)) for all cases, largest {float(max(xs)):.4f} < 1/4 (Fractions)")
    ne = {len(c["microscopic"]["energy_intervals"]) for c in cases} | {len(c["approximate"]["energy_intervals"]) for c in cases} | {len(c["rotor"]["energy_intervals"]) for c in cases}
    ng = {len(c["microscopic"]["gap_intervals"]) for c in cases}
    item("seven energies", r"\bfirst seven\b|\bseven\b", "CACHE", ne == {7}, f"cache energy_intervals has 7 entries in microscopic, rotor and approximate blocks of every case ({sorted(ne)})")
    item("six gaps / six cases / six bounds", r"\bsix\b|\bfirst six\b", "CACHE", ng == {6} and len(cases) == 6 and all("maximum_absolute_gap_error_upper_bound" in c for c in cases),
         f"cache gap_intervals has {sorted(ng)} entries; {len(cases)} cases each with maximum_absolute_gap_error_upper_bound")
    wE = {Fr(c["microscopic"]["maximum_energy_width"]) for c in cases} | {Fr(c["rotor"].get("maximum_energy_width", "1/500000000")) for c in cases}
    ewidth = {max(Fr(b) - Fr(a) for a, b in c["microscopic"]["energy_intervals"]) for c in cases} | {max(Fr(b) - Fr(a) for a, b in c["approximate"]["energy_intervals"]) for c in cases}
    gwidth = {max(Fr(b) - Fr(a) for a, b in c["microscopic"]["gap_intervals"]) for c in cases} | {max(Fr(b) - Fr(a) for a, b in c["microscopic_minus_approximate_gap_intervals"]) - 0 for c in cases if False}
    item("width 2e-9 (energies)", r"2e-9", "CACHE", max(ewidth) == Fr(2, 10 ** 9), f"cache energy intervals: widest {float(max(ewidth)):.3g} (Fractions), microscopic maximum_energy_width {sorted(map(str, wE))}")
    item("width 4e-9 (gaps)", r"4e-9", "CACHE", max(gwidth) == Fr(4, 10 ** 9), f"cache gap intervals: widest {float(max(gwidth)):.3g} (Fractions)")
    Ls = {c["rotor"]["L"] for c in cases}, {c["approximate"]["L"] for c in cases}
    item("L20", r"\bL20\b|L 20|L20 ", "CACHE", Ls[0] == {20} and "L=20 if x is None else 30" in runner.replace(" ", "").replace("L=20ifxisNoneelse30", "L=20 if x is None else 30") or "L=20 if x is None else 30" in runner, f"runner 'L=20 if x is None else 30'; cache rotor L = {sorted(Ls[0])}")
    item("L30", r"\bL30\b", "CACHE", Ls[1] == {30}, f"cache approximate L = {sorted(Ls[1])}")
    # the table
    tab = re.findall(r"\|\s*([0-9./]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.]+)\s*\|", norm(note))
    rows = {}
    for r in tab:
        rows[r[0]] = r[1:]
    ok_tab = True; info = []
    for c in cases:
        b = Fr(c["maximum_absolute_gap_error_upper_bound"])
        key = "1" if c["delta"] == "1" else "15803623/500000"
        col = {20: 0, 50: 1, 120: 2}[c["S"]]
        note_val = rows[key][col]
        up = Fr(math.ceil(b * 10 ** 12), 10 ** 12)
        same = Fr(note_val) == up
        ok_tab &= same
        info.append(f"delta {key} S{c['S']}: cache bound {float(b):.15f} -> rounded up at 12 decimals {float(up):.12f} vs note {note_val}: {'equal' if same else 'DIFFERENT'} (cache line {cache_line(clines, chr(34) + 'maximum_absolute_gap_error_upper_bound' + chr(34))})")
    item("table values", r"\b0\.\d{9,12}\b|\b\d\.\d{9,12}\b", "CACHE", ok_tab and len(tab) >= 2, "; ".join(info))
    item("table row labels", r"\| 1 \||\| 15803623/500000 \|", "CACHE", set(rows) == {"1", "15803623/500000"}, "row labels are the cache's delta strings")
    item("rounded upward", r"rounded upward", "CACHE", ok_tab, "every table value equals the cache's exact rational bound rounded up at 12 decimals (see the table item)")
    ok1, s1 = derive_eq1()
    item("equation (1) constants", r"E\(1\+4x-lambda\) psi = \[4Kn\^2-delta Z\*R\(E\)\^\(-1\)Z\]psi, R_m\(E\)=\(1-lambda\)\(2-lambda\)-4x d_m\. \(1\)", "DERIVED", ok1, s1)
    ok2, s2 = derive_eq2()
    item("equation (2) constants", r"H0\(n,n\)=4Kn\^2-4delta, H0\(n\+1,n\)=-2delta, H1\(n,n\)=8delta-8Kn\^2, H1\(n\+1,n\)=4delta\+4K n\(n\+1\)\. \(2\)", "DERIVED", ok2, s2)
    item("first order", r"first joint-scaling|first-order", "DERIVED", ok2, "the coefficient of x^1 in the expansion of (1) (equation (2)); 'first' names the order in x")
    unc = []
    ntok = 0
    for name, text in pieces:
        for a, b, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a, b)):
                unc.append((name, v, text[max(0, a - 40):b + 30]))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    for h in hits:
        print(h)
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    print(f"SUMMARY: {sum(out.values()) - out['HIT']} items over claim_scope + target + certificates + equations (1), (2) ({ntok} numeric tokens, {len(unc)} uncovered): cache-sourced {out['CACHE']}, runner-constant {out['RUNNER']}, "
          f"derived here from the note's formulas {out['DERIVED']}, definitions {out['DEFINITION']}; unsourced {out['HIT']}")
    if unc or hits:
        print("HIT: " + "; ".join([h[5:] for h in hits] + [f"uncovered token {v} in {n}" for n, v, _ in unc]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
