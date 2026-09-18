#!/usr/bin/env python3
"""J:provenance:PR8027 - every number in the theorem statements of the static-source geodesic note (the SU(3) Wilson Hamiltonian's
static fundamental source sector: the free geodesic eigenspace, the exact first-order plaquette-flip operator, the planar flip spectrum),
located in the runner's cached stdout (its printed lines and DATA JSON), the independent cube helper's cached stdout, the runners' own
checks, or an exact derivation in the note.

The note has no Theorem headings: the statement text is the front-matter claim_scope plus every '## ' section of the body (with the proofs,
so numbers inside the arguments are sourced too).  The paragraphs before the first '## ' (the check counts, the prior-art citation, the
derivation time) are checked as an EVIDENCE group (a miss there prints INFO, not HIT: it is not a theorem statement).  The note glues some
numbers to the preceding word ('has34', 'energy4/a', 'trace1/3'); a de-glue list restores those spaces so the numbers are counted.  Kinds:
  CACHE       printed in the runner's cached stdout                                                    -> sourced
  CACHE-JSON  reproduced from the printed DATA of the runner or of the cube helper (their caches)      -> sourced
  RUNNER      asserted in a runner source (ck(...)), not printed                                       -> sourced (flagged)
  DERIVED     an exact derivation located in the note, re-executed here (sympy / exact enumeration)    -> sourced
  DEFINITION  a constant of an object defined inline;  EXCLUDED  labels, conditions, notation, number words, citations
  (else)      HIT.  Tokens covered by no item are printed as UNCOVERED; the run is logged only with zero UNCOVERED.
Self-contained; reads the PR head via git (fetches the branch if the commit is missing).
"""
import json
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PR = 8027
BRANCH = "codex/static-geodesic-block37-20260907"
HEAD = "ca0eebe4dffad7a53a201ad7773e804b8c89edef"
NOTE = "docs/GAUGE_WILSON_STATIC_SOURCE_GEODESIC_PERTURBATION_BOUNDED_THEOREM_NOTE_2026-09-07.md"
RUNNER = "scripts/gauge_wilson_static_source_geodesic_2026_09_07.py"
CACHE = "logs/runner-cache/gauge_wilson_static_source_geodesic_2026_09_07.txt"
HELPER = "scripts/gauge_wilson_static_source_geodesic_cube_check_2026_09_07.py"
HELPER_CACHE = "logs/runner-cache/gauge_wilson_static_source_geodesic_cube_check_2026_09_07.txt"
OTHER = []


# ------------------------------------------------------------------------------------------------------------------ text access
def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def show(path):
    if git("cat-file", "-e", HEAD).returncode != 0:
        git("fetch", "origin", BRANCH, "--quiet")
    r = git("show", f"{HEAD}:{path}")
    if r.returncode != 0:
        raise SystemExit(f"cannot read {path} at {HEAD}: {r.stderr.strip()}")
    return r.stdout


SUP = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺", "0123456789-+")
SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
REPL = (("θ̂", "theta^"), ("θ̄", "theta_bar"), ("ξ̂", "xi^"), ("m̂", "m^"), ("ŝ", "s^"), ("−", "-"), ("–", "-"), ("—", " - "), ("×", "x"),
        ("≤", "<="), ("≥", ">="), ("π", "pi"), ("β", "beta"), ("σ", "sigma"), ("φ", "phi"), ("θ", "theta"), ("`", ""), ("∗", "*"),
        ("Σ", "Sigma"), ("ᵀ", "^T"), ("≳", ">~"), ("√", "sqrt"), ("∂", "d"), ("≠", "!="), ("ξ", "xi"), ("γ", "gamma"), ("τ", "tau"),
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"), ("ε", "epsilon"), ("η", "eta"), ("δ", "delta"), ("→", "->"), ("α", "alpha"), ("γ", "gamma"),
        ("λ", "lambda"), ("↦", "->"), ("±", "+-"), ("D̄", "Dbar"), ("Ū", "Ubar"),
        ("F̄", "Fbar"), ("R̄", "Rbar"), ("μ", "mu"), ("⊥", " perp "), ("𝓔", "Ecal"), ("𝕋", "TT"), ("𝒯", "Tcal"), ("𝓒", "Ccal"), ("𝓕", "Fcal"))


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in REPL:
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


DEGLUE = re.compile(r"\b(has|after|energy|norm|least|is|most|modulo|factor|trace|to|at|rho|amplitude)(\d)")


def deglue(t):
    """The note glues some numbers to the preceding word ('at most1', 'time2L', 'exponent6', 'and29single'); the tokenizer skips digits
    that follow a letter (identifiers such as d0, j0, lambda0, L2), so these words get their space back and their numbers are counted."""
    return DEGLUE.sub(r"\1 \2", t)


def statement_sections(note):
    fm, body = note.split("\n---\n", 1)
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", re.sub(r"\s+", " ", norm(m.group(1))))]
    body = deglue(body)
    parts = re.split(r"^## ", body, flags=re.M)
    intro = re.sub(r"```yaml.*?```", " ", parts[0], flags=re.S)          # the status block carries no numbers of the claim
    out.append(("EVIDENCE", re.sub(r"\s+", " ", norm(intro))))
    for sec in parts[1:]:
        title = sec.split("\n", 1)[0].strip()
        text = sec.split("\n", 1)[1] if "\n" in sec else ""
        out.append((title, re.sub(r"\s+", " ", norm(text))))
    return out


def section(note, prefix):
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        if sec.startswith(prefix):
            return norm(sec)
    return ""


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+/\d+|\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|sixteen|sixty-four|third|thirds|half|quarter|"
                   r"tenth|tenths|hundred|hundredth|double|twice|single|pair)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


# ------------------------------------------------------------------------------------------------------------------ exact re-derivations
import itertools
import math
import sympy as sp

EV, RAWCACHE = None, None


def E_label(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def d_casimir():
    vals = {(p, q): E_label(p, q) for p in range(41) for q in range(41) if (p, q) != (0, 0)}
    ok = min(vals.values()) == 4 and sorted(k for k, v in vals.items() if v == 4) == [(0, 1), (1, 0)]
    ok = ok and all(isinstance(v, int) for v in vals.values())
    return ok, ("E(p, q) = p^2 + pq + q^2 + 3p + 3q over all labels p, q <= 40 other than (0, 0): minimum 4, attained exactly at (1, 0) and (0, 1); "
                "integer valued (the runner asserts E(1,0) = E(0,1) = 4 and the positive increments)")


def d_triality():
    ok = (1 - 0) % 3 == 1 and (0 - 1) % 3 == 2 and all((p - q) % 3 == 0 for p, q in [(0, 0), (1, 1), (3, 0), (0, 3)])
    return ok, "triality (p - q) mod 3 is +1 for the fundamental (1, 0) and -1 = 2 mod 3 for the antifundamental (0, 1)"


def d_path_energy():
    Lsym = sp.symbols("L", positive=True, integer=True)
    ok = all(sum(E_label(*lab) for lab in labs) >= 4 * n for n in range(1, 5) for labs in itertools.product([(1, 0), (0, 1), (1, 1), (2, 0)], repeat=n))
    return ok, "a component joining x and y has at least L occupied links, each with E >= 4: K >= 4L/a, equality iff exactly L links all at 4/a"


def d_norm1():
    U = sp.eye(3)
    return sp.trace(U.H * U) / 3 == 1, "Tr(U_P^dagger U_P)/3 = Tr(I_3)/3 = 1 for unitary U_P (the carrier's normalized inner product)"


def d_multinomial():
    ok = True
    for n in itertools.product(range(4), repeat=3):
        L = sum(n)
        words = set(itertools.permutations([0] * n[0] + [1] * n[1] + [2] * n[2]))
        ok = ok and len(words) == math.factorial(L) // (math.factorial(n[0]) * math.factorial(n[1]) * math.factorial(n[2]))
    return ok, "the shortest paths are the words with letter counts (n1, n2, n3): enumerated count = L!/(n1! n2! n3!) for all n_i <= 3"


def d_gap():
    ok = all(E_label(p, q) == int(E_label(p, q)) for p in range(10) for q in range(10))
    return ok, "all label energies are integers (in units 1/a), so the ground level 4L/a is separated from the next level by at least 1/a"


def weyl_su3(f, n=12):
    """Haar average over SU(3) of a class function f(e^{i a}, e^{i b}, e^{-i(a+b)}) by the Weyl integration formula on an n x n grid
    (exact for trigonometric polynomials of degree < n)."""
    import cmath
    tot = 0.0
    for i in range(n):
        for j in range(n):
            a, b = 2 * math.pi * i / n, 2 * math.pi * j / n
            z = [cmath.exp(1j * a), cmath.exp(1j * b), cmath.exp(-1j * (a + b))]
            vd = abs((z[0] - z[1]) * (z[0] - z[2]) * (z[1] - z[2])) ** 2
            tot += vd * f(z)
    return tot / (6 * n * n)


def d_characters():
    one = weyl_su3(lambda z: 1.0)
    m2 = weyl_su3(lambda z: abs(sum(z)) ** 2)
    sq = weyl_su3(lambda z: sum(z) ** 2)
    m1 = weyl_su3(lambda z: sum(z))
    ok = abs(one - 1) < 1e-12 and abs(m2 - 1) < 1e-12 and abs(sq) < 1e-12 and abs(m1) < 1e-12
    return ok, (f"Weyl integration over SU(3): int 1 = {one.real:.15f}, int |chi|^2 = {m2.real:.15f}, int chi^2 = {abs(sq):.1e}, int chi = {abs(m1):.1e} "
                "(so <P|J_f|P> = int Re chi/3 = 0 and the flip element keeps one conjugate term)")


def d_center():
    w = sp.exp(2 * sp.pi * sp.I / 3)
    ok = sp.simplify(w ** 3 - 1) == 0 and sp.simplify(sp.Abs(1 - w)) != 0 and sp.det(w * sp.eye(3)) == 1
    return ok, ("w = e^{2 pi i/3} I is central in SU(3) (det = w^3 = 1) and the Haar measure is invariant under U -> wU, so int U_ab = w int U_ab "
                "forces int U_ab = 0 (w != 1): a nontrivial fundamental matrix integrates to zero")


def d_flip_element():
    ok = sp.Rational(1, 3) * sp.Rational(1, 6) * (1 + 0) == sp.Rational(1, 18)
    return ok, "int [conj(chi)/3][chi + conj(chi)]/6 = (1/18)(int|chi|^2 + int conj(chi)^2) = (1/18)(1 + 0) = 1/18: one conjugate term, no factor 2"


def geodesics(n):
    out = []
    for w in set(itertools.permutations([0] * n[0] + [1] * n[1] + [2] * n[2])):
        x = [0, 0, 0]
        cur = {}
        for d in w:
            e = (tuple(x), d)
            cur[e] = cur.get(e, 0) + 1
            x[d] += 1
        out.append((w, cur))
    return out


def d_flips():
    ok, nflip = True, 0
    for n in [(1, 1, 0), (2, 1, 0), (2, 2, 0), (2, 1, 1), (2, 2, 1)]:
        G = geodesics(n)
        faces = []
        for x in itertools.product(*(range(k + 1) for k in n)):
            for d1, d2 in ((0, 1), (0, 2), (1, 2)):
                if x[d1] < n[d1] and x[d2] < n[d2]:
                    x1 = list(x); x1[d1] += 1
                    x2 = list(x); x2[d2] += 1
                    faces.append({(x, d1): 1, (tuple(x1), d2): 1, (tuple(x2), d1): -1, (x, d2): -1})
        for (w, P), (v, Q) in itertools.permutations(G, 2):
            diff = {e: P.get(e, 0) - Q.get(e, 0) for e in set(P) | set(Q)}
            ok = ok and all(c in (-1, 0, 1) for c in diff.values())
            surv = [(f, sg) for f in faces for sg in (1, -1)
                    if all((diff.get(e, 0) + sg * f.get(e, 0)) % 3 == 0 for e in set(diff) | set(f))]
            exact = [(f, sg) for f, sg in surv if all(diff.get(e, 0) + sg * f.get(e, 0) == 0 for e in set(diff) | set(f))]
            swap = any(w[k] != w[k + 1] and w[:k] + (w[k + 1], w[k]) + w[k + 2:] == v for k in range(len(w) - 1))
            ok = ok and surv == exact and (len(surv) == 1) == swap and len(surv) <= 1
            nflip += swap
    return ok, (f"all ordered geodesic pairs in the boxes (1,1,0), (2,1,0), (2,2,0), (2,1,1), (2,2,1) (enumerated here): coefficients of P - Q in "
                f"{{-1, 0, 1}}; a face survives mod 3 only when P - Q = -+ boundary f exactly, i.e. exactly for the {nflip} adjacent swaps of "
                f"unequal letters, one face each")


def d_mod3():
    return all((c % 3 == 0) == (c == 0) for c in range(-2, 3)), "|c| <= 2 and c = 0 mod 3 force c = 0"


def d_pt():
    u, v, a, F, rho, L = sp.symbols("u v a F rho L", positive=True)
    A = sp.Matrix([[0, 1, 0, 0, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0], [0, 1, 0, 0, 1, 0], [0, 0, 1, 1, 0, 1], [0, 0, 0, 0, 1, 0]])
    ev = (F * sp.eye(6) - A / 18).eigenvals()
    ok = sp.simplify(min(ev, key=lambda e: e.subs(F, 0)) - (F - sp.sqrt(5) / 18)) == 0
    ok = ok and sp.simplify(((4 * L + u * (F - rho / 18)) - u * F).subs(u, a * v) / a - (4 * L / a - v * rho / 18)) == 0
    return ok, ("degenerate first-order theory: the lowest eigenvalue of P_geo(F - S)P_geo = F - A/18 is F - rho/18 (checked on the (2,2) "
                "adjacency: F - sqrt5/18); subtracting the vacuum's uF and dividing by a with u = av gives 4L/a - v rho/18 (sympy)")


def d_rho0():
    return sp.zeros(1, 1).eigenvals() == {0: 1}, "a unique geodesic gives the 1 x 1 zero adjacency: rho = 0"


def flip_adjacency(r, s):
    words = [w for w in itertools.product((0, 1), repeat=r + s) if sum(w) == s]
    idx = {w: i for i, w in enumerate(words)}
    A = [[0] * len(words) for _ in words]
    for w in words:
        for k in range(r + s - 1):
            if w[k] != w[k + 1]:
                v = w[:k] + (w[k + 1], w[k]) + w[k + 2:]
                A[idx[w]][idx[v]] = 1
    return A


def rho_formula(r, s):
    L = r + s
    return 2 * sum(math.cos(math.pi * k / (L + 1)) for k in range(1, s + 1))


def d_spectrum():
    import numpy as np
    ok, n = True, 0
    for L in range(1, 9):
        # one-particle modes
        T = np.diag(np.ones(L - 1), 1) + np.diag(np.ones(L - 1), -1)
        for k in range(1, L + 1):
            phi = np.sqrt(2 / (L + 1)) * np.sin(np.pi * k * np.arange(1, L + 1) / (L + 1))
            ok = ok and abs(phi @ phi - 1) < 1e-12 and np.allclose(T @ phi, 2 * np.cos(np.pi * k / (L + 1)) * phi, atol=1e-12)
        for s in range(0, L + 1):
            r = L - s
            A = np.array(flip_adjacency(r, s), dtype=float)
            evs = np.sort(np.linalg.eigvalsh(A)) if len(A) else np.array([0.0])
            lam = [2 * math.cos(math.pi * k / (L + 1)) for k in range(1, L + 1)]
            sums = np.sort([sum(c) for c in itertools.combinations(lam, s)]) if s else np.array([0.0])
            ok = ok and np.allclose(evs, sums, atol=1e-10) and abs(evs[-1] - rho_formula(r, s)) < 1e-10
            ok = ok and abs(rho_formula(r, s) - rho_formula(s, r)) < 1e-12 and (s and r or abs(rho_formula(r, s)) < 1e-12)
            n += 1
    return ok, (f"for all planar (r, s) with L = r + s <= 8 ({n} cases, enumerated here): the sine modes are normalized eigenvectors with "
                f"2cos(pi k/(L+1)); the flip adjacency's whole spectrum is the sums of s distinct lambda_k; its top is 2 sum_(k<=s) "
                f"cos(pi k/(L+1)), symmetric in r <-> s and 0 when r = 0 or s = 0")


def d_examples():
    r11 = 2 * sp.cos(sp.pi / 3)
    r21 = 2 * sp.cos(sp.pi / 4)
    r22 = 2 * (sp.cos(sp.pi / 5) + sp.cos(2 * sp.pi / 5))
    ok = sp.simplify(r11 - 1) == 0 and sp.simplify(r21 - sp.sqrt(2)) == 0 and sp.simplify(sp.expand(sp.expand_trig(r22)) - sp.sqrt(5)) == 0
    ok = ok or (abs(float(r22) - math.sqrt(5)) < 1e-15 and sp.simplify(r11 - 1) == 0 and sp.simplify(r21 - sp.sqrt(2)) == 0)
    return ok, "rho_(1,1) = 2cos(pi/3) = 1, rho_(2,1) = 2cos(pi/4) = sqrt2, rho_(2,2) = 2(cos(pi/5) + cos(2pi/5)) = sqrt5; derivatives -rho/18"


def d_riemann():
    x, eta = sp.symbols("x eta", positive=True)
    ok = sp.simplify(2 * sp.integrate(sp.cos(sp.pi * x), (x, 0, eta)) - 2 * sp.sin(sp.pi * eta) / sp.pi) == 0
    L = 200000
    for e in (0.1, 0.3, 0.5, 0.9):
        ok = ok and abs(rho_formula(L - int(e * L), int(e * L)) / L - 2 * math.sin(math.pi * e) / math.pi) < 1e-4
    return ok, "rho/L = (2/L) sum_(k <= eta L) cos(pi k/(L+1)) -> 2 int_0^eta cos(pi x) dx = (2/pi) sin(pi eta) (sympy; L = 2e5 within 1e-4)"


def d_naive():
    ok = all(rho_formula(r, s) > 0 for r in range(1, 8) for s in range(1, 8))
    return ok, "for r, s > 0 the top rho_(r,s) > 0 (checked r, s < 8), so the first-order shift -v rho/18 is nonzero: 4L/a is not kept"


def j_counts(ev, raw):
    rows = ev["main"]["rows"]
    ok = all(len(r["paths"]) == math.comb(r["length"], r["R"]) for r in rows)
    ok = ok and all(h["geodesics"] == math.factorial(sum(h["dimensions"])) // math.prod(math.factorial(d) for d in h["dimensions"]) for h in ev["helper"])
    return ok, ("runner DATA: path counts C(L, R) for (R, S) = " + ", ".join(f"({r['R']},{r['S']}): {len(r['paths'])}" for r in rows) +
                "; helper DATA geodesics " + ", ".join(f"{h['dimensions']}: {h['geodesics']}" for h in ev["helper"]) + " = L!/(n1!n2!n3!)")


def j_coeff(ev, raw):
    return ev["main"]["plaquette_flip_coefficient"] == "1/18", f"runner DATA plaquette_flip_coefficient = {ev['main']['plaquette_flip_coefficient']}"


def j_amplitude(ev, raw):
    ok = all(x in (0, 1) for r in ev["main"]["rows"] for row in r["adjacency"] for x in row)
    return ok, "runner DATA: every adjacency entry is 0 or 1 (the flip moves a particle with amplitude 1)"


def j_rows(ev, raw):
    ok = True
    for r in ev["main"]["rows"]:
        top = max(float(sp.sympify(e)) for e in r["fermion_eigenvalues"])
        ok = ok and abs(top - rho_formula(r["S"], r["R"])) < 1e-12 and abs(top - rho_formula(r["R"], r["S"])) < 1e-12
    ex = {(r["R"], r["S"]): max(sp.sympify(e) for e in r["fermion_eigenvalues"]) for r in ev["main"]["rows"]}
    ok = ok and ex[(1, 1)] == 1 and sp.simplify(ex[(1, 2)] - sp.sqrt(2)) == 0 and sp.simplify(ex[(2, 2)] - sp.sqrt(5)) == 0
    return ok, ("runner DATA fermion eigenvalues: top = 2 sum_(k<=s) cos(pi k/(L+1)) in all 5 rows; rho_(1,1) = 1, rho_(1,2) = sqrt2 "
                "(= rho_(2,1)), rho_(2,2) = sqrt5 printed")


def j_34(ev, raw):
    return "PASS TOTAL=34 unique named checks" in ev["main_text"], "runner stdout: PASS TOTAL=34 unique named checks"


def j_37(ev, raw):
    return "PASS TOTAL=37 unique named checks" in ev["helper_text"], "cube helper stdout (its own cache): PASS TOTAL=37 unique named checks"


def j_resource(ev, raw):
    ok = "lattice_wide: PASS 1 resource guard" in ev["main_text"] and "lattice_wide: PASS 1 resource guard" in ev["helper_text"]
    return ok, "both caches print 'lattice_wide: PASS 1 resource guard'"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("links", r"\]\([^)]*\)", "EXCLUDED", "link targets (file names carrying dates)", "file names"),
    ("stamp", "~after 20:39UTC contract", "EXCLUDED", "a time stamp of the derivation record", "time stamp"),
    ("cite", r"Phys\.Rev\.D23,2945\(1981\)|https://journals\.aps\.org/\S+", "EXCLUDED", "prior-art citation", "citation"),
    ("ev34", "~has 34 named checks", "CACHEJSON", j_34, "evidence: 34 checks"),
    ("ev37", "~has 37", "CACHEJSON", j_37, "evidence: 37 checks (helper)"),
    ("evres", "~each includes one resource control", "CACHEJSON", j_resource, "evidence: one resource control each"),
    ("zero-rest", "~their zero rest/kinetic energy", "EXCLUDED", "declared probes (zero rest/kinetic energy is part of the supplied source model)", "definition"),
    ("casimir", "~[p^2+pq+q^2+3p+3q]/a>=4/a", "DERIVED", (d_casimir, r"equality exactly the fundamental and antifundamental"), "the link energy"),
    ("triality", "~has triality+1 or-1", "DERIVED", (d_triality, r"total endpoint triality in that component to vanish"), "triality"),
    ("K4L", "~Thus K>=4L/a¦all with energy 4/a", "DERIVED", (d_path_energy, r"contains an x-y path of at least L edges"), "K >= 4L/a"),
    ("words1", r"Degree-two invariant tensors|one tensor contraction per path|one for each oriented shortest path|present in only one path"
     r"|words in three directions|the two consecutive steps around one elementary square|a one-edge/three-edge replacement|exactly one such face flip"
     r"|the four-link plaquette|the two conjugate terms|one oriented face boundary|Adding one signed face coefficient|For more than one geodesic"
     r"|The two sources|the whole s-particle|The flip adjacency moves one particle|On one nontrivial Peter-Weyl link|For two distinct geodesics"
     r"|One-particle normalized",
     "EXCLUDED", "wording (number words; the proofs' counting is sourced by the enumeration items)", "wording"),
    ("norm1", "~Every path state has norm 1 since U_P is unitary¦the pointwise color-summed squared norm is 1", "DERIVED",
     (d_norm1, r"since U_P is unitary"), "norm 1"),
    ("multinomial", "~all ni>=0, the number of basis paths is L!/(n1!n2!n3!)", "DERIVED", (d_multinomial, r"fixed letter counts"), "path count"),
    ("multinomial-x", "~the number of basis paths is L!/(n1!n2!n3!)", "CACHEJSON", j_counts, "path counts (executed)"),
    ("gap", "~isolated by at least 1/a", "DERIVED", (d_gap, r"All-label energies are integers"), "the isolation gap"),
    ("center", "~its nontrivial fundamental matrix integrates to zero", "DERIVED", (d_center, r"Distinct paths are orthogonal"), "orthogonality"),
    ("haar0", "~<P|J_f|P>=integral J_f=0¦integral|chi_f|^2=1 and integral chi_f^2=0", "DERIVED", (d_characters, r"four-link plaquette product is Haar"),
     "Haar integrals (Weyl formula)"),
    ("haar-r", "~integral|chi_f|^2=1 and integral chi_f^2=0", "RUNNER", r"fundamental character Haar norm all diagonal pairs", "the runner's Haar checks"),
    ("coeff", "~[chi_f+bar chi_f]/6 =1/18", "CACHEJSON", j_coeff, "the flip element 1/18 (printed)"),
    ("coeff-d", "~there is no extra factor 2", "DERIVED", (d_flip_element, r"no extra factor"), "no factor 2"),
    ("trace13", "~The normalized source trace 1/3 is load bearing", "RUNNER", r"omitting external source normalization is adverse",
     "the source normalization (asserted: 1/6 != 1/18)"),
    ("coeffs", "~each difference coefficient is in{-1,0,1}", "DERIVED", (d_flips, r"monotone in the same directions"), "flip geometry (enumerated)"),
    ("mod3", "~has magnitude at most 2, so zero modulo 3 forces equality over the integers", "DERIVED", (d_mod3, r"zero modulo"), "mod 3"),
    ("u0", "~u down to 0¦The right-hand derivative at 0 is exact", "EXCLUDED", "condition: the expansion point u = v = 0", "condition"),
    ("PT", "~a E_xy(u)=4L+u(F-rho/18)+O_(box,x,y)(u^2)¦E_xy(v)-E_vac(v)=4L/a - v rho(A_geo)/18 + O_(box,x,y)(a v^2)", "DERIVED",
     (d_pt, r"Degenerate analytic perturbation theory"), "first order"),
    ("rho0", "~A unique geodesic has rho 0", "DERIVED", (d_rho0, r"A unique geodesic has"), "unique geodesic"),
    ("planar", "~Take n3=0, n1=r, n2=s, L=r+s, with r,s>=0 and L>=1¦Ordered positions 1<=j1<...<js<=L¦T_(j,j+1)=T_(j+1,j)=1", "DEFINITION", "inline",
     "the planar case and the hopping matrix"),
    ("dir2", "~Encode each direction-2 step", "EXCLUDED", "notation: the direction label 2", "notation"),
    ("amp1", "~with amplitude 1", "CACHEJSON", j_amplitude, "amplitude 1 (printed adjacencies)"),
    ("modes", "~sqrt(2/(L+1)) sin(pi k j/(L+1)) have eigenvalues lambda_k=2cos(pi k/(L+1)), k=1,...,L¦rho_(r,s)=2 sum_(k=1)^s cos(pi k/(L+1))"
     "¦vanishes if r=0 or s=0", "DERIVED", (d_spectrum, r"particle-hole symmetry"), "the planar spectrum (enumerated)"),
    ("examples", "~rho_(1,1)=1, rho_(2,1)=sqrt2, rho_(2,2)=sqrt5", "CACHEJSON", j_rows, "the examples (printed spectra)"),
    ("derivs", "~are -1/18, -sqrt2/18 and -sqrt5/18", "DERIVED", (d_examples, r"in units of v"), "the derivatives"),
    ("eta", "~If s/L tends to eta in[0,1]", "EXCLUDED", "condition: eta in [0, 1]", "condition"),
    ("riemann", "~rho/L -> (2/pi)sin(pi eta)", "DERIVED", (d_riemann, r"by a Riemann sum"), "the asymptotic"),
    ("naive", "~keeps energy 4L/a to first order is false whenever r,s>0", "DERIVED", (d_naive, r"The naive statement"), "the naive claim"),
]


def control_checks():
    return {}, []


def main():
    note = show(NOTE)
    cache = show(CACHE).split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    cache_lines = cache.splitlines()
    global EV, RAWCACHE
    RAWCACHE = show(CACHE)
    helper = show(HELPER_CACHE).split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    EV = {"main": json.loads(next(l for l in cache_lines if l.startswith("DATA: "))[len("DATA: "):]),
          "helper": json.loads(next(l for l in helper.splitlines() if l.startswith("DATA: "))[len("DATA: "):]),
          "main_text": cache, "helper_text": helper, "runner_src": show(RUNNER), "helper_src": show(HELPER)}
    runner_src = norm(show(RUNNER))
    declared = section(note, "Premises and declared objects")
    other = {p: show(p) for p in OTHER}
    secs = statement_sections(note)
    covered = {name: set() for name, _ in secs}
    counts = {k: 0 for k in ("CACHE", "RUNNER", "DERIVED", "DEFINITION", "EXCLUDED", "HIT")}
    hits = []
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(cache_lines)} stdout lines; statement sections: {', '.join(n for n, _ in secs)}")
    def loose(p):
        if isinstance(p, str) and p.startswith("~"):
            alts = [a for a in p[1:].split("¦")]          # "¦" separates alternatives ("|" is an absolute value)
            return "|".join(r"\s*".join(re.escape(c) for c in a.replace(" ", "")) for a in alts)
        return p
    for item in ITEMS:
        iid, pat, kind, src, role = item[:5]
        pat = loose(pat)
        other_pat = item[5] if len(item) > 5 else src
        where = []
        for name, text in secs:
            for m in re.finditer(pat, text):
                where.append(name)
                covered[name].update(range(m.start(), m.end()))
        if not where:
            print(f"[UNUSED] {iid}: pattern not found in the statement text")
            continue
        loc = ",".join(sorted(set(where), key=lambda s: (s != "claim_scope", s)))
        if kind == "EXCLUDED":
            counts["EXCLUDED"] += 1
            print(f"[EXCLUDED] {iid} | {loc} | {src}")
        elif kind == "DEFINITION":
            ok = src == "inline" or re.search(src, declared) is not None
            counts["DEFINITION" if ok else "HIT"] += 1
            if ok:
                print(f"[DEFINITION] {iid} | {loc} | {role} | {'inline in the statement' if src == 'inline' else 'declared under Premises and declared objects'}")
            else:
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | definition not found among the declared objects"))
        elif kind == "CACHEJSON":
            ok, txt = src(EV, RAWCACHE)
            if ok:
                counts["CACHE"] += 1
                print(f"[CACHE-JSON] {iid} | {loc} | {role} | {txt}")
            elif set(where) == {"EVIDENCE"}:
                print(f"[INFO] {iid} | {loc} | {role} | not reproduced from the runner's EVIDENCE_JSON: {txt} (evidence text, not a theorem statement)")
            else:
                counts["HIT"] += 1
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | the runner's EVIDENCE_JSON does not carry it: {txt}"))
        elif kind == "RUNNER":
            ok = re.search(src, show(RUNNER)) is not None
            counts["RUNNER"] += 1 if ok else 0
            counts["HIT"] += 0 if ok else 1
            if ok:
                print(f"[RUNNER] {iid} | {loc} | {role} | present and checked in the runner source (not printed)")
            else:
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | not in the runner source or its printed output"))
        elif kind == "DERIVED":
            fn, locate = src
            ok, txt = fn()
            found = re.search(locate, re.sub(r"\s+", " ", norm(note))) is not None
            if ok and found:
                counts["DERIVED"] += 1
                print(f"[DERIVED] {iid} | {loc} | {role} | {txt}")
            else:
                counts["HIT"] += 1
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | derivation {'FAILED: ' + txt if not ok else 'not located in the note'}"))
        else:
            lines = [(i + 1, l) for i, l in enumerate(cache_lines) if re.search(src, l)]
            if lines:
                counts["CACHE"] += 1
                i, l = lines[0]
                print(f"[CACHE] {iid} | {loc} | {role} | cache stdout line {i}: {l.strip()[:140]}")
            else:
                counts["HIT"] += 1
                elsewhere = []
                for p, txt in other.items():
                    js = [j + 1 for j, l in enumerate(txt.splitlines()) if re.search(other_pat, l)]
                    if js:
                        elsewhere.append(f"{p.split('/')[-1]} lines {','.join(map(str, js[:6]))}{'...' if len(js) > 6 else ''}")
                in_src = re.search(src, runner_src) is not None
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | not printed by the runner (cache), no derivation in this note"
                             + ("; present in the runner source only" if in_src else "")
                             + (f"; printed by {', '.join(elsewhere)}" if elsewhere else "; printed by no other file of the PR")))
    unc, ntok = [], 0
    for name, text in secs:
        for a, b, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a, b)):
                unc.append((name, v, text[max(0, a - 40):b + 30].replace("\n", " ")))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    extra, notes = control_checks()
    for n in notes:
        print(f"[CONTROL] {n}")
    for iid, h in hits:
        print(h + extra.get(iid, ""))
    claimed = [i for i, _ in hits if not i.startswith("exec-")]
    execd = [i for i, _ in hits if i.startswith("exec-")]
    mism = sorted({i for i, _ in hits if "MISMATCH" in extra.get(i, "")})
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    print(f"SUMMARY: {len(ITEMS)} items over claim_scope + {len(secs) - 2} body sections + the evidence paragraphs ({ntok} numeric tokens, "
          f"{len(unc)} uncovered): cache-sourced {counts['CACHE']} (printed lines and the printed DATA of the runner and the cube helper), "
          f"runner-asserted (not printed) {counts['RUNNER']}, derived here from the note's steps {counts['DERIVED']}, definitions {counts['DEFINITION']}, "
          f"excluded {counts['EXCLUDED']}; unsourced {counts['HIT']} ({', '.join(claimed) or 'none'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
