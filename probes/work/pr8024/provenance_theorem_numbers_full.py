#!/usr/bin/env python3
"""J:provenance:PR8024 - every number in the statements of
GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md (block 34),
located in the runner's cached stdout, in the runner's own checks, in an exact derivation in the note
(re-executed here), or in the cited block's own cache/runner/note.

The note has no '## Theorem' headers: its statements are the front-matter claim_scope, the result paragraph
and every section of the three parts (main theorem, the Peter-Weyl supplement, the penalty supplement).  So
the statement text is the whole body with the yaml status block, link targets and URLs removed.  The text
glues numbers to words ("at least2/a", "gap1", "checks35", "Theorems1-3"); those junctions are split, while
identifiers (c1, c2, e1..e3, Lambda0, SU3, L2, log2, block29/30/32, arXiv v1) are kept whole.  Tokens:
integers, decimals, fractions, denominators of symbolic fractions (u/4, a/4, W/3) and number words.

Categories:
  CACHE       printed by the runner (logs/runner-cache at the PR head)                          -> sourced
  RUNNER      checked by the runner source, not printed                                          -> sourced (flagged)
  DERIVED     an exact derivation in the note, re-executed here (Fractions / enumeration)        -> sourced
  OTHER       attributed to block29/30/32: that block's cache/runner/note checked; printed as INFO -> sourced
  IMPORT      a constant of the cited external stability theorem (Yarotsky, printed pp. 2-4)     -> sourced by citation (INFO)
  DEFINITION  a declared object, index range, supplied parameter                                 -> not a claim
  EXCLUDED    a reference label (theorem/section/page/equation numbers, arXiv id, group name)   -> not a claim
  (else)      HIT
Tokens covered by no item are printed as UNCOVERED (the run is only logged with zero UNCOVERED).
"""
import itertools
import math
import random
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "codex/volume-uniform-gap-block34-20260907"
HEAD = "1c814b95243c5f788f57bab57c67fdc542f1aab4"
NOTE = "docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md"
RUNNER = "scripts/gauge_wilson_electric_dominated_volume_uniform_gap_check_2026_09_07.py"
CACHE = "logs/runner-cache/gauge_wilson_electric_dominated_volume_uniform_gap_check_2026_09_07.txt"
B29 = ("docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md",
       "scripts/gauge_wilson_full_cube_compact_hamiltonian_limit_check_2026_09_07.py",
       "logs/runner-cache/gauge_wilson_full_cube_compact_hamiltonian_limit_check_2026_09_07.txt")
B30 = ("docs/GAUGE_WILSON_COMPACT_CUBE_LOW_ELECTRIC_SPECTRUM_RITZ_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md",
       "scripts/gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_2026_09_07.py",
       "logs/runner-cache/gauge_wilson_compact_cube_low_electric_spectrum_ritz_gap_2026_09_07.txt")
B32 = ("docs/GAUGE_WILSON_COMPACT_CUBE_FINITE_QUBIT_CUTOFF_BOUNDED_THEOREM_NOTE_2026-09-07.md",
       "scripts/gauge_wilson_compact_cube_finite_qubit_cutoff_2026_09_07.py",
       "logs/runner-cache/gauge_wilson_compact_cube_finite_qubit_cutoff_2026_09_07.txt")


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {HEAD}: {r.stderr.strip()}")
    return r.stdout


GLUE = (r"\b(and|are|attains|bound|by|checks|energy|equals|exactly|gap|is|least|most|or|pages|plus|retain|retains|"
        r"Section|tensor|Theorem|Theorems|therefore)(?=\d)")


def norm(s):
    s = re.sub(GLUE, r"\1 ", s)
    for a, b in (("–", "-"), ("—", " - "), ("²", "^2"), ("³", "^3"), ("≤", "<="), ("≥", ">="), ("’", "'")):
        s = s.replace(a, b)
    return s


def statement_text(note):
    fm, body = note.split("\n---\n", 1)
    scope = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M).group(1)
    body = re.sub(r"```yaml.*?```", " ", body, flags=re.S)
    body = re.sub(r"\]\([^)]*\)", "]", body)
    body = re.sub(r"https?://\S+", " ", body)
    return norm("claim_scope: " + scope + "\n" + body)


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+/\d+|\d+\.\d+|\d+)(?![\d])")
DEN = re.compile(r"(?<=[A-Za-z)\]])/(\d+)")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|half|single)\b", re.I)


def tokens(t):
    out = [(m.start(1), m.end(1), m.group(1)) for m in NUM.finditer(t)]
    out += [(m.start(1), m.end(1), "/" + m.group(1)) for m in DEN.finditer(t)]
    out += [(m.start(1), m.end(1), m.group(1)) for m in WORDS.finditer(t)]
    return sorted(out)


# ------------------------------------------------------------------------------------------------ exact re-derivations
def d_smallness():
    rng = random.Random(8024)
    ok = Fr(4, 3) * Fr(1, 2) == Fr(2, 3)        # (4/3)(1/(2 c2)) = 2/(3 c2)
    for _ in range(4000):
        c1 = Fr(rng.randint(1, 400), rng.randint(1, 400))
        c2 = Fr(rng.randint(1, 400), rng.randint(1, 400))
        ustar = Fr(4, 3) * min(c1, 1 / (2 * c2))
        u = ustar * Fr(rng.randint(0, 999), 1000)
        eps = 3 * u / 4
        ok &= eps < c1 and c2 * eps < Fr(1, 2) and 1 - c2 * eps > Fr(1, 2)
        # at the threshold one of the two strict inequalities becomes equality
        e0 = 3 * ustar / 4
        ok &= (e0 == c1) or (c2 * e0 == Fr(1, 2))
    return ok, ("u < (4/3)min(c1, 1/(2c2)) <=> eps = 3u/4 < c1 and c2 eps < 1/2, so 1 - c2 eps > 1/2 (4000 exact random "
                "(c1, c2, u); equality at the threshold)")


def d_gap_scaling():
    a = Fr(7, 3)                                   # any a > 0
    ok = (4 / a) * Fr(1, 2) == 2 / a and (a / 4) * (4 / a) == 1 and (a / 4) * (Fr(3, 2) / a) == Fr(3, 8)
    return ok, "(4/a)(1/2) = 2/a; (a/4)(4/a) = 1; (a/4)(3/(2a)) = 3/8 (exact)"


def E_num(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def d_casimir():
    ok = all(Fr(3, 2) * Fr(2, 3) * E_num(p, q) == E_num(p, q) for p in range(61) for q in range(61))
    nz = [(E_num(p, q), (p, q)) for p in range(61) for q in range(61) if (p, q) != (0, 0)]
    mn = min(v for v, _ in nz)
    arg = sorted(l for v, l in nz if v == mn)
    inc = all(E_num(p + 1, q) > E_num(p, q) and E_num(p, q + 1) > E_num(p, q) for p in range(60) for q in range(60))
    ok &= mn == 4 and arg == [(0, 1), (1, 0)] and inc and E_num(1, 0) == 4
    return ok, (f"E(p,q) = (3/(2a))(2/3)(p^2+pq+q^2+3p+3q) = [..]/a; over p,q <= 60 the nonzero minimum is {mn} exactly at "
                f"{arg}, strictly increasing under increments; E(1,0) = 4, first nonzero energy 4/a")


def d_counts():
    ok = True
    e = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    add = lambda x, y: tuple(a + b for a, b in zip(x, y))
    for L in range(1, 13):
        cells = set(itertools.product(range(L), repeat=3))
        groups = [x for x in cells if all(add(x, z) in cells for z in e)]
        indiv = [(x, i, j) for x in cells for i, j in itertools.combinations(range(3), 2)
                 if add(x, e[i]) in cells and add(x, e[j]) in cells]
        ok &= 3 * len(groups) == 3 * (L - 1) ** 3 and len(indiv) == 3 * L * (L - 1) ** 2 \
            and len(indiv) - 3 * len(groups) == 3 * (L - 1) ** 2
        if L == 2:
            ok &= (3 * len(groups), len(indiv)) == (3, 6)
    return ok, "whole-group 3(L-1)^3, individual 3L(L-1)^2, difference 3(L-1)^2 by enumeration for L = 1..12; L = 2: 3 and 6"


def d_anchors():
    x = (5, 5, 5)
    lam0 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    anchors = {tuple(a - b for a, b in zip(x, z)) for z in lam0}
    ok = len(anchors) == 4 and all(any(tuple(y + z for y, z in zip(yy, zz)) == x for zz in lam0) for yy in anchors)
    ok &= 4 + 4 == 8                                   # E <= E_rest + 4 eps and E >= E_rest + <h> - 4 eps
    return ok, "x lies in y + Lambda0 for exactly the 4 anchors y = x - {0,e1,e2,e3}; 4 eps + 4 eps = 8 eps"


def d_norms():
    rng = np.random.default_rng(8024)
    worst = 0.0
    for _ in range(2000):
        Z = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
        Q, R = np.linalg.qr(Z)
        Q = Q @ np.diag(np.diag(R) / np.abs(np.diag(R)))
        Q = Q / np.linalg.det(Q) ** (1 / 3)
        worst = max(worst, abs(np.trace(Q).real) / 3)
    ok = worst <= 1 + 1e-12 and 3 * Fr(1, 4) == Fr(3, 4)
    return ok, f"|ReTr W|/3 <= 1 (|Tr W| <= 3 for unitary W; max {worst:.6f} on 2000 Haar SU3); three terms of norm u/4 give 3u/4"


def pw_labels(R):
    return [(p, q) for p in range(R + 1) for q in range(R + 1 - p)]


def dim(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def d_pw():
    ok = True
    rows = []
    for R in range(0, 7):
        energies = []
        for p, q in pw_labels(R):
            energies += [Fr(E_num(p, q), 4)] * (dim(p, q) ** 2)
        D = len(energies)
        pos = [z for z in energies if z > 0]
        if R == 0:
            ok &= D == 1 and not pos
        else:
            ok &= energies.count(0) == 1 and min(pos) == 1
        qR = math.ceil(math.log2(D)) if D > 1 else 0
        ok &= qR == (D - 1).bit_length()
        rows.append((R, D, qR))
    return ok, ("scaled onsite spectrum on the p+q <= R carrier: unique 0 and smallest positive exactly 1 for R = 1..6; R = 0 "
                "is one-dimensional; D_R, q_R = ceil(log2 D_R): " + ", ".join(f"R={R}:{D}/{q}" for R, D, q in rows)), rows


def d_penalty():
    ok = True
    for R in (1, 2, 3):
        energies = []
        for p, q in pw_labels(R):
            energies += [Fr(E_num(p, q), 4)] * (dim(p, q) ** 2)
        D = len(energies)
        q = (D - 1).bit_length()
        a = Fr(5, 2)
        for Delta in (4 / a, 6 / a):
            pen = energies + [Delta * a / 4] * (2 ** q - D)
            ok &= pen.count(0) == 1 and min(z for z in pen if z > 0) == 1
    return ok, "with Delta >= 4/a the full 2^q_R register keeps a unique zero and smallest positive scaled energy 1 (R = 1, 2, 3)"


def d_projector():
    rng = np.random.default_rng(1)
    ok = True
    for _ in range(50):
        n1, n2 = 3, 4
        A = rng.standard_normal((n1, n1)); A = A + A.T
        Bm = rng.standard_normal((n2, n2)); Bm = Bm + Bm.T
        H = np.block([[A, np.zeros((n1, n2))], [np.zeros((n2, n1)), Bm]])
        P = np.diag([1.0] * n1 + [0.0] * n2)
        w, V = np.linalg.eigh(H)
        g = V[:, 0]
        val = g @ P @ g
        ok &= min(abs(val), abs(val - 1)) < 1e-12
    return ok, "a projector commuting with H has expectation exactly 0 or 1 in a rank-one ground (50 random block examples)"


# ------------------------------------------------------------------------------------------------ items
def items(runner, cache, b29, b30, b32):
    def has(txt, *needles):
        return all(n in txt for n in needles)
    r_counts = has(runner, "3*len(groups)==3*(L-1)**3", "len(indiv)==3*L*(L-1)**2", "len(indiv)-3*len(groups)==3*(L-1)**2",
                   "for L in [1,2,3]")
    r_open = has(runner, "for L in [1,2]:", "open_edges_", "padded_range_", "no_ghost_interaction_")
    r_scal = has(runner, "Fraction(1,4)*4==1", "3*Fraction(1,4)==Fraction(3,4)", "4*Fraction(1,2)==2")
    r_anch = has(runner, "len([(0,0,0)]+e)==4", "2*4==8")
    r_pw = has(runner, "PW_dimension_gap_", "min(z for z in energies if z)==1", "PW_R0_no_excitation", "penalty_full_register_")
    c_total = "TOTAL: PASS 35 unique named checks (28 original plus 7 prospective supplements)" in cache
    o29 = has(b29[2], "fundamental kinetic coefficient4/a") and has(b29[1], "s.Rational(3,2)*s.Rational(8,3)==4") \
        and has(b29[0], "H=-(3/(2a)) Delta+V")
    o30 = has(b30[1], "weight metric Casimir exact", "s.Rational(2,3)*(p*p+q*q+p*q+3*p+3*q)") \
        and has(b30[0], "(2/3)(p²+q²+pq+3p+3q)")
    o32 = has(b32[2], "Exact Peter-Weyl shell sum and dimension polynomial", '"R": 1, "dimension": 19', '"R": 2, "dimension": 155')
    return [
        # ---- references and names
        ("refs", r"Theorems? \d(?:-\d)?(?:'s)?|Sections? \d|printed pages \d+-\d+|pages \d-\d|reference\[\d+\]|equation\(\d\)|"
                 r"in\(\d\)|and\(\d\)|bound\(\d\)|^#+ \d\.|\(\d\)(?=\s*(?:\n|$| The| Then))|arXiv:math-ph/\d+v\d|SU\(3\)|"
                 r"interaction in\(1\)|onset in\(2\)|H\(1\)",
         "EXCLUDED", True, "theorem/section/page/equation labels, arXiv id, group name"),
        # ---- cache
        ("cache-total", r"checks 35 finite geometry/scalar cases \(28 original plus 7 prospective supplements\)", "CACHE", c_total,
         "cache: 'TOTAL: PASS 35 unique named checks (28 original plus 7 prospective supplements)'"),
        # ---- definitions
        ("defs-params", r"a>0|v>=0|p,q>=0|R>=1|0<=s<=1|at s=1|at s=0|Delta>=4/a|R=0|i=1,2,3|\^tensor 3|Lambda=\{0,\.\.\.,L-1\}\^3|"
                        r"Lambda0=\{0,e1,e2,e3\}|\^\(-1\)|W_\(x,ij\)/3|C\^\(2\^q_R\)|q_R=ceil\(log2 D_R\)",
         "DEFINITION", True, "declared parameters, index ranges, the cell tensor power, the normalised trace, the register"),
        ("defs-words", r"use all three outgoing links|The four link factors|complete three-link cells|set all other terms to zero|"
                       r"At one site x|one can additionally|unique zero vector|inert zero dynamics|extend it by zero|"
                       r"its four link registers|same four link registers|zero-off-code|four-register support|native two-qubit|"
                       r"ground energy is zero|A single link",
         "DEFINITION", True, "structural words of the declared objects (links per cell, plaquette links, registers)"),
        # ---- import
        ("import", r"gap at least 1, and bounded|gap at least 1-c2 epsilon", "IMPORT", True,
         "Yarotsky, arXiv:math-ph/0411042v1, Theorem 1 hypotheses/conclusion (printed pp. 2-4); not verifiable here"),
        # ---- other blocks
        ("block29", r"K_e=\(3/\(2a\)\)\(-Delta_e\)", "OTHER", o29,
         "block29: cache prints 'fundamental kinetic coefficient4/a'; runner checks 3/2 * 8/3 == 4; note H=-(3/(2a))Delta+V"),
        ("block30", r"C\(p,q\)=\(2/3\)\(p\^2\+pq\+q\^2\+3p\+3q\)", "OTHER", o30,
         "block30: runner check 'weight metric Casimir exact' (not printed); derived in block30 sec. 2 from the weight Gram matrix"),
        ("block32", r"D_R=sum d_\(p,q\)\^2", "OTHER", o32,
         "block32: cache prints the Peter-Weyl dimension polynomial rows (R=1: 19, R=2: 155)"),
        # ---- derived / runner
        ("smallness", r"av<\(4/3\)min\(c1,1/\(2c2\)\)|0<=u < u_\*=\(4/3\)min\(c1,1/\(2c2\)\)|epsilon< c1 and c2 epsilon<1/2|"
                      r"gap at least 1/2", "DERIVED", d_smallness, None),
        ("gap-2a", r"gap at least 2/a|gap\(H_Lambda\)>=2/a|at least 2/a|lower bound 2/a|generator by 4/a", "DERIVED+RUNNER",
         lambda: (d_gap_scaling()[0] and r_scal, d_gap_scaling()[1] + "; runner gap_rescaling 4*1/2 == 2"), None),
        ("casimir", r"E\(p,q\)=\[p\^2\+pq\+q\^2\+3p\+3q\]/a|at least 4, with equality only at \(1,0\) and \(0,1\)|"
                    r"the two minimal nonzero labels|first nonzero energy 4/a|At v=0 the full unperturbed link-space gap is 4/a",
         "DERIVED+RUNNER", lambda: (d_casimir()[0] and r_pw, d_casimir()[1] + "; runner PW_dimension_gap min scaled 1"), None),
        ("onsite", r"h_x=\(a/4\)sum_i K_\(x,i\)=\(3/8\)sum_i|has gap 1|onsite gap 1 after multiplication by a/4|"
                   r"formal scaled Hamiltonian \(a/4\)H|h_x=\(a/4\)sum_i K_\(x,i\)",
         "DERIVED+RUNNER", lambda: (d_gap_scaling()[0] and r_scal, d_gap_scaling()[1] + "; runner electric_gap_normalization"), None),
        ("norms", r"\|J\|<=1|phi_x=-\(u/4\)sum|\|\|phi_x\|\|<=3u/4|at most 3u/4|Adding \(3u/4\)|\|\|phi_\(x,R\)\|\|<=3av/4|"
                  r"norm bound 3av/4|norm at most 1|-\(av/4\)sum_\(three pairs\)|Group the three pairs|three-plaquette group",
         "DERIVED+RUNNER", lambda: (d_norms()[0] and r_scal, d_norms()[1] + "; runner perturbation_norm_coefficient"), None),
        ("counts", r"retains 3\(L-1\)\^3|retain 3L\(L-1\)\^2|difference is 3\(L-1\)\^2|at L=2 the counts are 3 and 6",
         "DERIVED+RUNNER", lambda: (d_counts()[0] and r_counts, d_counts()[1] + "; runner group/individual/omitted counts L=1,2,3"), None),
        ("runner-L", r"counts for L=1,2,3|open boxes L=1,2", "RUNNER", r_counts and r_open,
         "runner loops 'for L in [1,2,3]' (counts, loops, supports) and 'for L in [1,2]' (open boxes)"),
        ("anchors", r"at most 4 such anchors|E_rest\+4epsilon|E_rest\+<h_x>-4epsilon|<=8epsilon",
         "DERIVED+RUNNER", lambda: (d_anchors()[0] and r_anch, d_anchors()[1] + "; runner onsite_incidence_bound, local_energy_coefficient"), None),
        ("pad-gap", r"desired gap and 4/a|each with gap 4/a|operators with gap 4/a", "DERIVED",
         lambda: (d_casimir()[0] and d_pw()[0], "added links carry the electric gap E(1,0)/a = 4/a (R >= 1: fundamental retained)"), None),
        ("pw", r"exactly 0 and 1|three such links, dimension D_R\^3|three-cell actual support and four-cell padded|"
               r"carrier is one-dimensional|three q_R per cell",
         "DERIVED+RUNNER", lambda: (d_pw()[0] and r_pw, d_pw()[1]), None),
        ("penalty", r"at least 4/a; a fundamental code state attains 4/a|Regrouping three outgoing links",
         "DERIVED+RUNNER", lambda: (d_penalty()[0] and r_pw, d_penalty()[1] + "; runner penalty_full_register_1/2"), None),
        ("projector", r"rank one and separated|rank-one ground is exactly 0 or 1|equals 1 at s=0|therefore 1 for every s|"
                      r"omega\(P_e\)=1", "DERIVED", d_projector, None),
    ]


def main():
    note = show(NOTE)
    runner = show(RUNNER)
    cache = show(CACHE)
    b29 = [show(p) for p in B29]
    b30 = [show(p) for p in B30]
    b32 = [show(p) for p in B32]
    t = statement_text(note)
    toks = tokens(t)
    covered = [None] * len(toks)
    results = []
    hits = []
    for name, pat, cat, check, desc in items(runner, cache, b29, b30, b32):
        spans = [(m.start(), m.end()) for m in re.finditer(pat, t, flags=re.M)]
        if callable(check):
            out = check()
            ok, desc2 = out[0], out[1]
        else:
            ok, desc2 = bool(check), desc
        idx = [k for k, (s, e, _) in enumerate(toks) if any(a <= s and e <= b for a, b in spans)]
        for k in idx:
            if covered[k] is None:
                covered[k] = name
        results.append((name, cat, ok, len(spans), [toks[k][2] for k in idx], desc2))
        if not ok and cat not in ("EXCLUDED", "DEFINITION"):
            hits.append(f"{name}: {cat} source check failed ({desc2})")
        if not spans:
            print(f"UNMATCHED item pattern: {name}")
    for name, cat, ok, nsp, tk, desc in results:
        tag = "INFO" if cat in ("OTHER", "IMPORT") else cat
        print(f"[{tag}] {name}: {nsp} statement spans, tokens {tk}; source ok={ok}: {desc}")
    unc = [(toks[k], t[max(0, toks[k][0] - 40):toks[k][1] + 25].replace(chr(10), ' ')) for k in range(len(toks)) if covered[k] is None]
    for (s, e, v), ctx in unc:
        print(f"UNCOVERED {v!r}: ...{ctx}...")
    cats = {}
    for name, cat, ok, nsp, tk, desc in results:
        cats[cat] = cats.get(cat, 0) + len(tk)
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: PR8024 block34 note @ {HEAD[:10]}: {len(toks)} numeric tokens in the statement text, uncovered "
          f"{len(unc)}; by item category {dict(sorted(cats.items()))}; cache prints only the check totals (35 = 28 + 7), "
          f"every other statement number is re-derived exactly here (counts to L=12, Casimir minimum over p,q<=60, PW "
          f"spectra R<=6, penalty registers, smallness on 4000 exact triples) or checked by the runner; block29 "
          f"(3/(2a) via printed 4/a), block30 (Casimir, runner-checked not printed) and block32 (dimension rows) confirmed; "
          f"imported Yarotsky constants cited, not verified; unsourced numbers {len(hits)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
