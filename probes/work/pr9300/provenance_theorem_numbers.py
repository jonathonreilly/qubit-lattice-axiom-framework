#!/usr/bin/env python3
"""J:provenance:PR9300 -- every number in the theorem statements of the flux-free-bands Chern-vector note, located in the runner's cached stdout, the runner source, the landed parent, or an
exact derivation re-executed here.

Statement text = the front-matter claim_scope + "Exact on the line f = (x, 1 - x, 0)" + "Finite diagnostics reproduced by the runner" (the note has no theorem headings).  Every numeric token
(integers, decimals, a/b, 3e-9 forms, number words) must fall inside one item:
  CACHE       printed by the PR's cached runner output (logs/runner-cache/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.txt at the PR head), re-parsed here -> sourced
  RUNNER      a constant of the runner source at the PR head                                                                                                                             -> sourced
  DERIVED     an exact derivation re-executed here (sympy / exact Fractions), or a value derived from printed numbers by the operation the note states (rounding, reduction modulo one)     -> sourced
  PARENT      a formula the note takes from the landed parent note; INFO when the parent's text prints it
  MISMATCH    a stated value that disagrees with the control output it is compared with
  (else)      HIT: no runner line, no cache line, no derivation.
Tokens covered by no item are printed as UNCOVERED and counted as HIT. Self-contained; reads the PR head and origin/main via git.
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
PR = 9300
BRANCH = "claude/composite-network-chern-vector-of-the-flux-free-bands-with-the-odd-term-20260926"
NOTE = ("docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_CARRY_A_CHERN_VECTOR_ODD_IN_THE_ODD_TERM_WITH_A_CLOSED_FORM_BELOW_THE_SPLIT_BOUNDED_THEOREM_NOTE_2026-09-26.md")
RUNNER = "scripts/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.py"
CACHE = "logs/runner-cache/composite_site_network_flux_free_bands_chern_vector_with_the_odd_term_2026_09_26.txt"
PARENT = ("docs/COMPOSITE_SITE_NETWORK_FLUX_FREE_BANDS_WITH_THE_ODD_TERM_TWO_CERTIFIED_TOUCHINGS_OF_OPPOSITE_CHARGE_BECOME_SIX_AT_KAPPA_ROOT_3_OVER_20_BOUNDED_THEOREM_NOTE_2026-09-26.md")
PARENT_CACHE = "logs/runner-cache/composite_site_network_flux_free_band_touchings_certified_with_the_odd_term_2026_09_26.txt"


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def head():
    git("fetch", "origin", BRANCH, "--quiet")
    r = git("rev-parse", f"origin/{BRANCH}")
    if r.returncode != 0:
        raise SystemExit("cannot resolve the PR branch: " + r.stderr.strip())
    return r.stdout.strip()


HEAD = head()


def show(path, ref=None):
    r = git("show", f"{ref or HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {ref or HEAD}: {r.stderr.strip()}")
    return r.stdout


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in (("−", "-"), ("×", "x"), ("κ", "kappa"), ("π", "pi"), ("√", "sqrt"), ("≥", ">="), ("≤", "<="), ("·", "*"), ("²", "^2"), ("∈", " in "), ("→", "->"), ("`", "")):
        t = t.replace(a, b)
    return t


def statement_pieces(note):
    fm = note.split("\n---\n", 1)[0]
    cs = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M).group(1)
    secs = {s.split("\n", 1)[0].strip(): s for s in re.split(r"^#+ ", note, flags=re.M)[1:]}
    ex = next(v for k, v in secs.items() if k.startswith("Exact on the line"))
    fd = next(v for k, v in secs.items() if k.startswith("Finite diagnostics"))
    out = [("claim_scope", cs), ("Exact on the line", ex.split("\n", 1)[1]), ("Finite diagnostics", fd.split("\n", 1)[1])]
    return [(n, re.sub(r"\s+", " ", norm(t))) for n, t in out]


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+e-\d+|\d+/\d+|[+-]?\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|first|second|single|pair)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


def main():
    note = show(NOTE); runner = show(RUNNER)
    raw = show(CACHE)
    lines = raw.split("----- stdout -----\n", 1)[1].splitlines()
    parent = show(PARENT, "origin/main"); pcache = show(PARENT_CACHE, "origin/main")
    pieces = statement_pieces(note)
    covered = {n: set() for n, _ in pieces}
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(lines)} stdout lines; statement pieces: {', '.join(n for n, _ in pieces)}")
    out = {"CACHE": 0, "RUNNER": 0, "DERIVED": 0, "PARENT": 0, "DEFINITION": 0, "HIT": 0, "MISMATCH": 0}
    hits = []

    def cover(pat, flags=re.I):
        c = 0
        for name, text in pieces:
            for m in re.finditer(pat, text, flags=flags):
                covered[name].update(range(m.start(), m.end())); c += 1
        return c

    def item(iid, pat, kind, ok, source, flags=re.I):
        if cover(pat, flags) == 0:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            return
        if ok:
            out[kind] += 1
            print(f"[{kind}] {iid} | {source}")
        else:
            out["HIT"] += 1
            hits.append(f"HIT: {iid} | {source}")

    def cline(needle):
        for i, l in enumerate(lines):
            if needle in l:
                return i + 1
        return None

    L = {k: next(l for l in lines if l.startswith(k)) for k in ("[PASS] exact", "[PASS] the numerical zero", "[PASS] kappa = 0.1 and 0.3", "[PASS] the slice-averaged", "[PASS] kappa = 0.6")}
    # ---- exact section: formulas
    J, c, k = sp.symbols("J c kappa")
    curve = 2 * (1 + c) * (1 + 2 * k ** 2 * (1 - c))
    bracket = J ** 2 + 4 * c ** 2 * k ** 2 - 2 * c - 4 * k ** 2 - 2
    ok_curve = sp.expand(bracket - (J ** 2 - curve)) == 0
    c_note = -(1 + 4 * k ** 2) / (1 + sp.sqrt(1 + 4 * k ** 2 + 16 * k ** 4)); c_run = (1 - sp.sqrt(1 + 4 * k ** 2 + 16 * k ** 4)) / (4 * k ** 2)
    ok_root = sp.simplify(c_note - c_run) == 0 and sp.simplify((bracket.subs(J, 1)).subs(c, c_note)) == 0 and sp.simplify(4 * k ** 2 * c ** 2 - 2 * c - (1 + 4 * k ** 2) - bracket.subs(J, 1)) == 0
    ok_zone = sp.simplify((J ** 2 - curve).subs({c: 1}) - (J ** 2 - 4)) == 0 and sp.expand(curve.subs(c, 1)) == 4 and sp.limit(c_note, k, 0) == sp.Rational(-1, 2)
    ok_c1 = "root True, J = 2 through c = 1 True, kappa -> 0 limit -1/2 True" in L["[PASS] exact"]
    parent_det = "D=16[J²+4c²kappa²-2c-4kappa²-2]²" in parent.replace(" ", "") or "16[J²+4c²kappa²-2c-4kappa²-2]²" in parent.replace(" ", "")
    parent_curve = "J²=2(1+c)[1+2kappa²(1-c)]" in parent.replace(" ", "")
    item("determinant on the line (from the landed parent)", r"from the landed determinant identity|det H = 16 \[J\^2 \+ 4c\^2kappa\^2 - 2c - 4kappa\^2 - 2\]\^2 on this line", "PARENT", parent_det,
         "the landed parent's text states D = 16[J^2 + 4c^2 kappa^2 - 2c - 4 kappa^2 - 2]^2 at w = 1 (INFO: printed in the parent note; the parent's cache prints " + ("no" if "16[" not in pcache.replace(' ', '') else "the") + " determinant line)")
    item("zero curve", r"J\^2 = 2 ?\(1 \+ c\)[\[( ]*1 \+ 2 ?kappa\^2 ?\(1 - c\)[\])]*|the curve|zero-determinant curve|for -1 < c < 1|the middle levels vanish|(?<=on the curve )", "DERIVED", ok_curve and parent_curve,
         "the bracket equals J^2 - 2(1 + c)[1 + 2 kappa^2 (1 - c)] identically (sympy); the parent note states the same curve (INFO)")
    item("root at J = 1", r"at `?J = 1`? (?:its root|this is)[^;.]*?(?:\(1 \+ 4 ?kappa\^2 \+ 16 ?kappa\^4\)\^\(1/2\)\)|sqrt\(1 \+ 4kappa\^2 \+ 16kappa\^4\)\))|4kappa\^2c\^2 - 2c - \(1 \+ 4kappa\^2\) = 0|root in \(-1, 1\) is c = -\(1 \+ 4 ?kappa\^2\) ?/ ?\(1 \+ (?:\(1 \+ 4 ?kappa\^2 \+ 16 ?kappa\^4\)\^\(1/2\)|sqrt\(1 \+ 4kappa\^2 \+ 16kappa\^4\))\)", "DERIVED",
         ok_root and ok_c1, "the note's form equals the runner's [1 - (1 + 4k^2 + 16k^4)^(1/2)]/(4k^2) (sympy); it solves 4k^2 c^2 - 2c - (1 + 4k^2) = 0 (sympy); the cache prints 'root True' (line " + str(cline("[PASS] exact")) + ")")
    item("J = 2 and the limit", r"passes through c = 1 at J = 2|at J = 2\.? The curve passes through c = 1, the zone centre|the curve reaches the zone centre at J = 2|c = 1|tending to -1/2 as kappa -> 0|J = 2|-1/2|kappa -> 0", "DERIVED", ok_zone and ok_c1,
         "at c = 1 the curve is J^2 = 4, i.e. J = 2 for every kappa (sympy), and the root tends to -1/2 (sympy limit); the cache prints 'J = 2 through c = 1 True, kappa -> 0 limit -1/2 True' (line " + str(cline("[PASS] exact")) + ")")
    item("definitions", r"J_x = J_y = 1|J_z = J|and odd term kappa|f = \(x, 1 - x, 0\)|c = cos 2 ?pi ?x|`?c = cos 2pix`?|u = \+1|\(-1, 1\)|-1 < c < 1|\bone copy\b|in one copy|\bJ = 1\b|\bJ = 1\.5\b", "DEFINITION", True,
         "the supplied setting (couplings, the line, c = cos 2 pi x, the u = +1 sector) and the interval (-1, 1) of the root")
    item("cleared zone (landed parent)", r"a cleared zone at J_z = 2\.5, kappa = 0\.3", "PARENT", "2.5" in parent and ("J_z=2.5" in parent.replace(" ", "") or "Jz=2.5" in parent.replace(" ", "") or "2.5" in pcache),
         "the landed parent's scan (INFO: the note attributes 'a cleared zone at J_z = 2.5, kappa = 0.3' to the landed note; " + ("found" if "2.5" in parent else "NOT found") + " in the parent's text)")
    # ---- numerical zero
    m = re.search(r"max difference ([0-9.e+-]+)", L["[PASS] the numerical zero"])
    md = float(m.group(1))
    pairs = re.findall(r"J ([0-9.]+), kappa ([0-9.]+): x ([0-9.]+) \(closed ([0-9.]+)\)", L["[PASS] the numerical zero"])
    stated = 3e-9
    item("3 x 10^-9 (matches to)", r"matches that root to 3e-9|within 3 x 10\^-9|3e-9|3 x 10\^-9", "MISMATCH" if md > stated else "CACHE", True,
         f"cache line {cline('[PASS] the numerical zero')} prints 'max difference {md:.1e}' over the seven (J, kappa) cases; the note states 3e-9 ({'the printed maximum EXCEEDS the stated value by ' + format((md - stated) / stated, '.1%') if md > stated else 'consistent'}); the runner asserts only dmax < 1e-6")
    if md > stated:
        out["MISMATCH"] += 0  # counted as a MISMATCH line, not an unsourced number
    cases = [(float(a), float(b)) for a, b, _, _ in pairs]
    item("the (J, kappa) cases of the numerical zero", r"at J = 1 \(kappa = 0\.05 to 0\.35\) and at J = 1\.5 \(kappa = 0\.3, 0\.5\)|kappa = 0\.05 to 0\.35|J = 1\.5|kappa = 0\.3, 0\.5|\b0\.05\b|\b0\.35\b|\b0\.5\b", "CACHE",
         sorted(cases) == sorted([(1.0, 0.05), (1.0, 0.1), (1.0, 0.2), (1.0, 0.3), (1.0, 0.35), (1.5, 0.3), (1.5, 0.5)]) and "(1.0, 0.05), (1.0, 0.1), (1.0, 0.2), (1.0, 0.3), (1.0, 0.35), (1.5, 0.3), (1.5, 0.5)" in runner,
         f"cache line {cline('[PASS] the numerical zero')} lists the cases {cases}; runner list in the source")
    # ---- slice fluxes
    ns = re.search(r"NS = 32 if DRY else 96", runner) is not None and re.search(r"slice_chern\(B, \(i \+ 0\.5\) / NS, m=48, axis=ax\)", runner) is not None
    item("96 slices, mesh 48", r"\b96\b|mesh 48|\b48\b", "RUNNER", ns and "on 96 slices per fractional axis" in L["[PASS] kappa = 0.1 and 0.3"], "runner: NS = 96 slices per axis (32 with --dry), slice_chern(..., m=48); the cache check line names '96 slices per fractional axis'")
    m1 = re.search(r"kappa 0\.1: \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\) against \(([+-][0-9.]+), ([+-][0-9.]+), 0\); kappa 0\.3: \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\) against \(([+-][0-9.]+), ([+-][0-9.]+), 0\)", L["[PASS] kappa = 0.1 and 0.3"])
    v1 = [float(x) for x in m1.groups()]
    r3 = lambda x: f"{abs(x):.3f}"
    ok_a = r3(v1[0]) == "0.667" and r3(v1[1]) == "0.667" and r3(v1[3]) == "0.672" and r3(v1[4]) == "0.672" and r3(v1[5]) == "0.708" and r3(v1[6]) == "0.708" and r3(v1[8]) == "0.710" and r3(v1[9]) == "0.710"
    item("averages at kappa = 0.1 and 0.3", r"\(arccos c / pi, -arccos c / pi, 0\)|\(0\.667, -0\.667, 0\)|\(0\.708, -0\.708, 0\)|\(0\.672, -0\.672, 0\)|\(0\.710, -0\.710, 0\)|at kappa = 0\.1|at kappa = 0\.3|kappa = 0\.1 and (?:0\.)?3|(?<=kappa = )0\.1|(?<=kappa = )0\.3", "CACHE", ok_a,
         f"cache line {cline('[PASS] kappa = 0.1 and 0.3')}: kappa 0.1 averages ({v1[0]:+.4f}, {v1[1]:+.4f}, {v1[2]:+.4f}) against ({v1[3]:+.4f}, {v1[4]:+.4f}, 0); kappa 0.3 ({v1[5]:+.4f}, {v1[6]:+.4f}, {v1[7]:+.4f}) against ({v1[8]:+.4f}, {v1[9]:+.4f}, 0), which round to the note's three-decimal values")
    tol = re.search(r"abs\(v\[0\] - pred\) <= 2\.0 / NS", runner) is not None
    item("within two slice spacings", r"two slice spacings|within two slice spacing", "RUNNER", tol, "runner: tolerance 2.0 / NS (two slice spacings) in the flux checks, for kappa = 0.1, 0.3 and 0.6")
    ints = "integers" in L["[PASS] kappa = 0.1 and 0.3"] and "allint" in runner
    item("integer-valued fluxes", r"all integer-valued|integer-valued|integers", "RUNNER", ints, "runner: allint &= abs(c - round(c)) < 1e-6 on every slice; the check line states 'are integers'")
    m2 = re.search(r"kappa 0\.3: \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\); kappa -0\.3: \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\)", L["[PASS] the slice-averaged"])
    v2 = [float(x) for x in m2.groups()]
    every = "every slice flux" in norm(note)
    item("reversal at kappa = -0.3", r"reverse at kappa = -0\.3|At kappa = -0\.3 every slice flux changes sign|kappa = -0\.3|-0\.3", "CACHE", all(abs(a + b) < 1e-4 for a, b in zip(v2[:3], v2[3:])),
         f"cache line {cline('[PASS] the slice-averaged')}: kappa 0.3 averages {v2[:3]}, kappa -0.3 averages {v2[3:]} (the runner compares the per-axis AVERAGES, np.allclose(v3, -v3m); it does not compare slice by slice)")
    if every:
        print("[INFO] the note's body says 'every slice flux changes sign' at kappa = -0.3; the runner asserts the sign change of the three per-axis averages and integrality on the kappa = -0.3 slices, not a slice-by-slice comparison")
    # ---- kappa = 0.6
    m3 = re.search(r"averages \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\); -sum q f = \(([+-][0-9.]+), ([+-][0-9.]+), ([+-][0-9.]+)\)", L["[PASS] kappa = 0.6"])
    v3 = [float(x) for x in m3.groups()]
    mod1 = [x % 1.0 for x in v3[3:]]
    mod1s = [(x % 1.0) for x in v3[3:]]
    cen = [x - round(x) for x in v3[3:]]
    ok_b = r3(v3[0]) == "0.104" and r3(v3[1]) == "0.104" and round(cen[0], 3) == 0.093 and round(cen[1], 3) == -0.093 and round(cen[2], 3) == 0.0
    item("kappa = 0.6 averages and -sum q f", r"\(0\.104, -0\.104, 0\)|\(0\.093, -0\.093, 0\)|kappa = 0\.6|\b0\.6\b", "DERIVED", ok_b,
         f"cache line {cline('[PASS] kappa = 0.6')}: averages ({v3[0]:+.4f}, {v3[1]:+.4f}, {v3[2]:+.4f}); -sum q f printed as ({v3[3]:+.4f}, {v3[4]:+.4f}, {v3[5]:+.4f}), i.e. ({cen[0]:.4f}, {cen[1]:.4f}, {cen[2]:.4f}) modulo one (centred residues), which rounds to the note's (0.093, -0.093, 0) "
         "(the mod-one reduction is the operation the note states; the cache prints the unreduced -0.9073, +0.9073)")
    ng = len(re.findall(r"\(([0-9.]+),([0-9.]+),([0-9.]+)\)([+-]1)", L["[PASS] kappa = 0.6"]))
    item("six numerical groups", r"\bsix\b|six numerical groups|six group", "CACHE", ng == 6 and "len(nodes6) == 6" in runner, f"cache line {cline('[PASS] kappa = 0.6')} lists {ng} group positions with charges; runner asserts len(nodes6) == 6")
    item("charges +1 / 0 profile", r"\+1|(?<=were )1|`?0`? inside|Chern numbers were \+1 outside|1 outside|and 0 inside|0 inside", "DEFINITION", True, "the conditional statement 'if the continuum slice Chern numbers were +1 outside ... and 0 inside' (a hypothetical profile; not a claim of the runner)")
    item("mirrored f_2 / labels", r"f_2|\bf_1\b", "DEFINITION", True, "axis labels")
    item("word counts", r"\bzero\b|\btwo\b|\bone\b|\bthree\b|\bsix\b|\bfirst\b|\bsecond\b|\bsingle\b", "DEFINITION", True, "wording (two lowest bands, two slice spacings, one momentum line, ...)")
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
    print(f"SUMMARY: {sum(v for kk, v in out.items() if kk not in ('HIT', 'MISMATCH'))} items over claim_scope + the exact and finite sections ({ntok} numeric tokens, {len(unc)} uncovered): cache {out['CACHE']}, runner {out['RUNNER']}, derived {out['DERIVED']}, "
          f"parent {out['PARENT']}, definitions {out['DEFINITION']}; unsourced {out['HIT']}; stated values disagreeing with the printed control: {'3e-9 vs ' + format(md, '.1e') if md > stated else 'none'}")
    if md > stated:
        print(f"HIT: 3e-9 | the note states that the numerical zero matches the closed-form root 'to 3e-9' (claim_scope) and 'within 3 x 10^-9' (Finite diagnostics); the cache prints max difference {md:.1e} > 3e-9 (cache line {cline('[PASS] the numerical zero')}); the runner asserts only < 1e-6")
    if hits:
        print("HIT: " + "; ".join(h[5:] for h in hits))
    if unc:
        print("HIT: uncovered tokens " + "; ".join(f"{v} in {n}" for n, v, _ in unc))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
