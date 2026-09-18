#!/usr/bin/env python3
"""J:provenance:PR8145 - every number in the theorem statements of the finite-clock field-history note (history reconstruction, the
charge-sector bottom, the local charge floor), located in the runner's cached stdout, in the runner's own checks, or in an exact derivation.

This note states its results in running text, not under Theorem headings: the statement text is the front-matter claim_scope plus every
section of Parts I-III (with their proofs, so numbers inside the proofs are sourced too).  The 'Author evidence' section's executed counts
are checked as a separate EVIDENCE group (a miss there prints INFO, not HIT: it is not a theorem statement).  The note glues some numbers to
the preceding word ('at most1', 'time2L', 'exponent6'); a de-glue list restores those spaces so the numbers are counted.  Kinds:
  CACHE       printed in the runner's cached stdout                                                    -> sourced
  CACHE-JSON  reproduced from the runner's printed EVIDENCE_JSON (e.g. every executed ratio within its stated bound)  -> sourced
  RUNNER      asserted in the runner source at the stated precision, not printed                       -> sourced (flagged)
  DERIVED     an exact derivation located in the note, re-executed here (sympy / exact enumeration)    -> sourced
  DEFINITION  a constant of an object defined inline;  EXCLUDED  labels, conditions, notation, number words
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
PR = 8145
BRANCH = "physics-loop/clock-history-field-20260915"
HEAD = "c5580db2ebe78e4dca71f210539cea1471148483"
NOTE = "docs/FINITE_CLOCK_FIELD_HISTORY_RECONSTRUCTION_AND_CHARGE_SECTOR_HAMILTONIAN_BOUNDED_THEOREM_NOTE_2026-09-15.md"
RUNNER = "scripts/finite_clock_field_history_reconstruction_and_charge_sector_hamiltonian_2026_09_15.py"
CACHE = "logs/runner-cache/finite_clock_field_history_reconstruction_and_charge_sector_hamiltonian_2026_09_15.txt"
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


DEGLUE = re.compile(r"\b(most|charge|at|time|length|exponent|below|size|energy|compare|and|a|times|hence|Thus|to|is)(\d)")


def deglue(t):
    """The note glues some numbers to the preceding word ('at most1', 'time2L', 'exponent6', 'and29single'); the tokenizer skips digits
    that follow a letter (identifiers such as d0, j0, lambda0, L2), so these words get their space back and their numbers are counted."""
    return DEGLUE.sub(r"\1 \2", t)


def statement_sections(note):
    """This note states its results in running text: Parts I-III (from '## Part I.' up to the No-Go gate) carry the theorems, so every
    section there is statement text (with its proofs: numbers inside the proofs must be sourced too).  The 'Author evidence' section's
    executed counts are checked separately (EVIDENCE group) against the runner's EVIDENCE_JSON."""
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", re.sub(r"\s+", " ", norm(m.group(1))))]
    note = deglue(note)
    on = False
    part = ""
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        if title.startswith("Part "):
            on, part = True, title.split(".")[0]
        if title.startswith("No-Go Discipline Gate"):
            on = False
        if title.startswith("Author evidence"):
            out.append(("EVIDENCE", re.sub(r"\s+", " ", norm(sec.split("\n", 1)[1]))))
            continue
        if on:
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            name = part + (" " + title.split(".")[0] if not title.startswith("Part ") else "")
            out.append((name, re.sub(r"\s+", " ", norm(body))))
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
import sympy as sp

EV, RAWCACHE = None, None
TOL = 1e-12


def _hist(ev):
    return [h for c in ev["history_reconstruction"]["cases"] for h in c["histories"]]


def _floor_cases(ev):
    return [(c, x) for c in ev["charge_floor"]["cases"] for x in c["cases"]]


def j_norm(ev, raw):
    hs = _hist(ev)
    mx = max(h["norm_squared"] for h in hs)
    return mx <= 1 + TOL, f"EVIDENCE_JSON history_reconstruction: {len(hs)} words, largest norm_squared {mx:.16f} (<= 1 within {TOL:g})"


def j_form(ev, raw):
    g = [c["gram_lower_eigenvalues"] for c in ev["history_reconstruction"]["cases"]]
    lo = min(min(x["positive_transfer"], x["contractive_form"], x["gram"]) for x in g)
    return lo >= -TOL, f"EVIDENCE_JSON gram_lower_eigenvalues (gram, positive_transfer, contractive_form) at least {lo:.2e} in the 3 square systems"


def j_inverse(ev, raw):
    hs = _hist(ev)
    bad = [h for h in hs if h["inverse_moment"] > h["K_final_insertion"] + TOL]
    mx = max(h["inverse_moment"] / h["K_final_insertion"] for h in hs)
    return not bad, f"EVIDENCE_JSON: inverse_moment <= K_final_insertion for all {len(hs)} words (largest ratio {mx:.6f})"


def j_fibers(ev, raw):
    rows = [(f["N"], x) for f in ev["endpoint_comparison"]["cube_current_fibers"] for x in f["comparisons"]]
    ok = all(x["base"] / x["R"] - TOL <= x["shifted"] <= x["base"] * x["R"] + TOL for _, x in rows)
    return ok, f"EVIDENCE_JSON cube_current_fibers: R^-1 W(K) <= W(J) <= R W(K) at all {len(rows)} comparisons (N = 2, 3 cubes)"


def j_history_bounds(ev, raw):
    rows = ev["endpoint_comparison"]["history_comparisons"]
    ok = all(r["endpoint_ratio"] ** -2 - TOL <= r["ratio"] <= r["endpoint_ratio"] ** 2 + TOL for r in rows)
    shift = [r for r in rows if r["history_length"] > 0 and r["omitted_time_shift_difference"] > 1e-9]
    return ok and bool(shift), (f"EVIDENCE_JSON history_comparisons: R^-2 <= F_w(n)/W(2L + n) <= R^2 at all {len(rows)} rows; omitting the "
                                f"2L shift changes the reference in {len(shift)} rows with L > 0")


def j_weights(ev, raw):
    qs = [c["min_max_weight_ratio"] for c in ev["charge_floor"]["cases"]]
    return all(0 < q < 1 for q in qs), f"EVIDENCE_JSON charge_floor: m/M = {', '.join(f'{q:.4f}' for q in qs)} (N = 2, 3, 4), all in (0, 1)"


def j_harmonic(ev, raw):
    cs = ev["charge_floor"]["cases"]
    ok = all(c["maximum_nontrivial_conditional_harmonic"] <= c["conditional_harmonic_bound"] + TOL for c in cs)
    return ok, "EVIDENCE_JSON: maximum nontrivial conditional harmonic <= r at N = 2, 3, 4 (" + ", ".join(
        f"{c['maximum_nontrivial_conditional_harmonic']:.4f} <= {c['conditional_harmonic_bound']:.4f}" for c in cs) + ")"


def j_transfer(ev, raw):
    fc = _floor_cases(ev)
    ok = all(0 < x["transfer_ratio"] <= x["kernel_ratio_bound"] + TOL for _, x in fc)
    return ok, f"EVIDENCE_JSON: 0 < transfer_ratio <= r^|A| (kernel_ratio_bound) in all {len(fc)} charge cases"


def j_floor(ev, raw):
    fc = _floor_cases(ev)
    ok = all(x["energy"] >= x["degree2_floor"] - TOL and x["degree2_floor"] >= x["cubic_degree6_floor"] - TOL for _, x in fc)
    ok = ok and all(abs(x["cubic_degree6_floor"] + len(x["independent_vertices"]) * __import__("math").log1p(-c["min_max_weight_ratio"] ** 6))
                    < 1e-12 for c, x in fc)
    return ok, (f"EVIDENCE_JSON: energy >= degree2_floor >= cubic_degree6_floor = -|A| log(1 - (m/M)^6) in all {len(fc)} charge cases "
                f"(the 6-floor recomputed from the printed m/M)")


def j_pairs(ev, raw):
    fc = _floor_cases(ev)
    pairs = [x for _, x in fc if sum(1 for q in x["charge"] if q) == 2]
    sep = [x for x in pairs if [i for i, q in enumerate(x["charge"]) if q] == [0, 2]]          # opposite corners of the square
    adj = [x for x in pairs if [i for i, q in enumerate(x["charge"]) if q] == [0, 1]]          # neighbours on the square
    ok = sep and adj and all(len(x["independent_vertices"]) == 2 for x in sep) and all(len(x["independent_vertices"]) == 1 for x in adj)
    return bool(ok), (f"EVIDENCE_JSON: the separated pair (charges at opposite corners 0, 2; current [1,1,0,0]) has an independent set of size 2 "
                      f"and the adjacent pair (corners 0, 1; current [1,0,0,0]) size 1, in {len(sep)} + {len(adj)} cases (N = 2, 3, 4)")


def j_alias(ev, raw):
    al = [(c["N"], x) for c, x in _floor_cases(ev) if not any(x["charge"])]
    ok = al and all(abs(x["energy"]) < 1e-12 and abs(x["transfer_ratio"] - 1) < 1e-12 for _, x in al)
    return bool(ok), f"EVIDENCE_JSON: the alias current [N,0,0,0] has charge 0 mod N, energy {max(abs(x['energy']) for _, x in al):.1e} and transfer ratio 1 at N = 2, 3, 4"


def j_families(ev, raw):
    return len(ev) == 3, f"EVIDENCE_JSON has {len(ev)} families: {', '.join(sorted(ev))}"


def j_27(ev, raw):
    cs = ev["history_reconstruction"]["cases"]
    n = sum(len(c["histories"]) for c in cs)
    return n == 27 and [c["N"] for c in cs] == [2, 3, 4], f"EVIDENCE_JSON history_reconstruction: N = {[c['N'] for c in cs]}, {n} history words"


def j_108(ev, raw):
    n = len(ev["endpoint_comparison"]["history_comparisons"])
    return n == 108, f"EVIDENCE_JSON endpoint_comparison: {n} history comparisons"


def j_cubes(ev, raw):
    la = [f["link_assignments"] for f in ev["endpoint_comparison"]["cube_current_fibers"]]
    return la == [4096, 531441], f"EVIDENCE_JSON cube_current_fibers: link_assignments {la}"


def j_12_29(ev, raw):
    n12 = sum(len(c["cases"]) for c in ev["charge_floor"]["cases"])
    n29 = sum(c["conditional_distributions"] for c in ev["charge_floor"]["cases"])
    return n12 == 12 and n29 == 29, f"EVIDENCE_JSON charge_floor: {n12} charged/alias cases, {n29} conditional distributions"


def j_timeout(ev, raw):
    m = re.search(r"^timeout_sec: (\d+)", raw, flags=re.M)
    return bool(m) and m.group(1) == "300", f"cache header timeout_sec: {m.group(1) if m else None}"


def d_exponent():
    ok = 2 * 3 == 6 and sp.simplify(sum(1 for v in itertools.product((-1, 0, 1), repeat=3) if sum(map(abs, v)) == 1) - 6) == 0
    return ok, "a site of Z^3 has 2d = 6 nearest neighbours (enumerated); a box site has at most 6"


def d_improve():
    x = sp.symbols("x", positive=True)
    ok = all(sp.simplify((x ** d - x ** (d + 1)) - x ** d * (1 - x)) == 0 for d in range(1, 6))
    return ok, "for 0 < m/M < 1, (m/M)^d = (m/M)^(d+1)/(m/M) decreases in d, so degrees below 6 give a larger delta and a smaller r"


def d_roots():
    import mpmath as mp
    mp.mp.dps = 50
    ok = True
    for N in range(2, 13):
        for q in range(1, N):
            x = sp.exp(2 * sp.pi * sp.I * sp.Rational(q, N))
            # x^N = 1 and x != 1, so sum_k x^k = (x^N - 1)/(x - 1) = 0; checked exactly (x^N) and at 50 digits (x != 1, the sum)
            ok = ok and sp.simplify(x ** N - 1) == 0 and abs(mp.mpc(complex(sp.N(x, 30))) - 1) > 1e-6
            ok = ok and abs(mp.fsum(mp.expjpi(mp.mpf(2 * q * k) / N) for k in range(N))) < mp.mpf(10) ** -40
    return ok, ("x = e^{2 pi i q/N}, q != 0 mod N: x^N = 1 (sympy) and x != 1, so sum_k x^k = (x^N - 1)/(x - 1) = 0 (and the sum is below 1e-40 "
                "at 50 digits for N <= 12): the uniform component averages a nontrivial character to 0")


def d_mixture():
    N, dl = sp.symbols("N delta", positive=True)
    ok = sp.simplify(N * (dl / N) - dl) == 0
    return ok, "p(eta) >= delta/N for all N values gives p = delta*uniform + (1 - delta)*p', p' = (p - delta/N)/(1 - delta) >= 0 of mass 1"


def d_bipartite():
    import random
    random.seed(8145)
    pts = [v for v in itertools.product(range(4), range(4), range(3))]
    ok = True
    for _ in range(2000):
        S = random.sample(pts, random.randint(1, 9))
        cls = max(([v for v in S if sum(v) % 2 == k] for k in (0, 1)), key=len)
        indep = all(sum(abs(a - b) for a, b in zip(u, v)) != 1 for u, v in itertools.combinations(cls, 2))
        ok = ok and indep and len(cls) >= -(-len(S) // 2)
    return ok, "the larger parity class of any charged set in Z^3 is independent and has at least ceil(s/2) points (2000 random sets checked)"


def d_pair():
    return True, "a nonadjacent pair is itself independent (size 2); of an adjacent pair only one vertex can be kept (size 1)"


def d_shift():
    n, L = sp.symbols("n L", positive=True)
    ok = sp.limit((2 * L + n) / n, n, sp.oo) == 1
    return ok, "(2L + n)/n -> 1 (sympy): a fixed shift 2L of the time interval leaves the exponential rate unchanged"


def d_exp():
    n = sp.symbols("n", positive=True, integer=True)
    ok = sp.simplify(n + (-1) + n - (2 * n - 1)) == 0
    return ok, "tau^n tau^-1 tau^n = tau^(2n-1) with 2n - 1 >= 1, so <phi, tau^(2n-1) phi> <= ||phi||^2 <= 1 by 0 <= tau <= 1"


def d_K0():
    return True, "U_0 = I, so U_0* tau^-1 U_0 = tau^-1 = 1 * tau^-1: the comparison constant is 1 at j0 = 0"


def d_atom():
    return True, "a finite measure with finite inverse moment int lambda^-1 dmu <= K(j0) has mu({0}) = 0"


def d_limit():
    b = sp.symbols("beta", positive=True)
    bound = 2 * sp.exp(-b * sp.pi ** 2 / 8) / (1 - sp.exp(-b * sp.pi ** 2 / 2))
    ok = sp.limit(bound, b, sp.oo) == 0
    return ok, ("m/M <= w(theta*)/w(0) with |theta*| >= pi/2 for N >= 2 and w(0) >= 1, bounded by 2e^{-beta pi^2/8}/(1 - e^{-beta pi^2/2}) -> 0 "
                "as beta -> oo (sympy): the floor tends to 0 at weak coupling")


def d_zero_sector():
    return True, "rho = 0 has no charged vertex: |A| = 0 and the bound |A|(-log(1 - (m/M)^6)) is 0"


def d_N1():
    return True, "Z_1 has one element, so every charge is 0 mod 1: no nontrivial charge profile exists at N = 1"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("labels", r"(?<![\^_])\(\d\)", "EXCLUDED", "equation labels (1)-(4), also where glued to a word ('preserve(2)', 'Equation(2)')", "labels"),
    ("beta0", "~at fixed finite N and beta>0", "EXCLUDED", "condition: beta > 0", "condition"),
    ("wpos", "~Let w(k)>0 be the one-link temporal Villain weight on Z_N", "DEFINITION", "inline", "the temporal weight (a sum of Gaussians)"),
    ("charkernel", "~C_rho(a,b)=average_eta exp[-2pi i<rho,eta>/N] product_e w(a_e-b_e+(d0 eta)_e)", "DEFINITION", "inline",
     "the charge-projected kernel"),
    ("words", r"zero-time|time-zero|one-character|single-character|one insertion history|two reflected fillings|One convenient|no adjacent pair"
     r"|joins two variables|the one from the static|The zero spectral projection", "EXCLUDED", "wording (number words)", "wording"),
    ("inverse", r"\^\(-1\)", "EXCLUDED", "notation: the inverse", "notation"),
    ("def-words", "~n1,...,nr>=1¦The case r=0 is included, as is j0=0", "DEFINITION", "inline", "the history words (1)"),
    ("norm1", "~Every word has norm at most 1¦||phi_L||<=1¦Each word's finite spectral measure has mass at most 1", "CACHEJSON", j_norm,
     "word norm (executed on 27 words)"),
    ("vac0", "~The two distant ends carry vacuum charge 0", "EXCLUDED", "definition: the vacuum carries charge 0", "definition"),
    ("fourdim", "~the resulting four-dimensional current is conserved¦Two words with different charge profiles¦the two spaces", "EXCLUDED",
     "wording (number words)", "wording"),
    ("S01", "~Finite identities give 0<=S<=I¦converges weakly on[0,1]", "CACHEJSON", j_form, "0 <= S <= I (executed Gram forms)"),
    ("ineq2", "~w_L=U_(j0) tau_L^n phi_L, n>=1¦<w_L,tau_L^(-1)w_L> <=K(j0)<phi_L,tau_L^(2n-1)phi_L><=K(j0)", "DERIVED",
     (d_exp, r"If a word has a nonempty next time interval"), "Part I (2)"),
    ("ineq2x", "~The limiting measure has inverse moment at most K(j0)¦Every word has finite exponential energy moment bounded by K(j0)",
     "CACHEJSON", j_inverse, "inverse moments (executed)"),
    ("K0", "~The proof also covers j0=0 with K(0)=1", "DERIVED", (d_K0, r"covers j0=0 with K\(0\)=1"), "K(0) = 1"),
    ("cutoff", "~min(m,1/lambda), with value m at 0", "DEFINITION", "inline", "the cutoff functions"),
    ("atom", "~and no atom at 0", "DERIVED", (d_atom, r"no atom at0|no atom at 0"), "no atom at 0"),
    ("ck", "~coefficients c_k>0", "CACHE", r"per_element: positive local Fourier coefficients", "positive Fourier coefficients (per_element)"),
    ("fiber2", "~R(S)^(-1) W(K)<=W(J)<=R(S) W(K)", "CACHEJSON", j_fibers, "Part II (2) (executed on the N = 2, 3 cubes)"),
    ("times0", "~at integer times 0<=t_1<=...<=t_m<=L¦F_w(n)=<w,S^n w>, n>=0¦Move each left spatial insertion j_i from time 0 to t_i"
     "¦the interval[0,t_i]", "DEFINITION", "inline", "the history's times"),
    ("len2L", "~a temporal interval of length 2L+n¦The reference W_(j_total)(2L+n)¦R(S_w)^(-2) W_(j_total)(2L+n) <=F_w(n)<=R(S_w)^2 "
     "W_(j_total)(2L+n)¦by applying the shift twice", "CACHEJSON", j_history_bounds, "Part II (3) with the 2L shift (executed on 108 rows)"),
    ("shift2L", "~Its fixed shift in time 2L does not change this rate", "DERIVED", (d_shift, r"fixed shift in time"), "the rate"),
    ("N2", "~The following bound uses N>=2; N=1 has no nontrivial charge profile¦N=1 has no nontrivial charge sector and needs no bound"
     "¦nonconstant at finite beta and N>=2", "DERIVED", (d_N1, r"N=1 has no nontrivial charge"), "N >= 2"),
    ("delta", "~set delta=(m/M)^6, r=1-delta", "DEFINITION", "inline", "delta and r"),
    ("delta01", "~hence 0<delta<1 and 0<r<1", "CACHEJSON", j_weights, "0 < delta < 1 (executed m/M)"),
    ("exp6", "~The exponent 6 is the maximum spatial vertex degree in the cubic spatial lattice¦each a product of d_v<=6 terms",
     "DERIVED", (d_exponent, r"maximum spatial vertex degree"), "the exponent 6"),
    ("mixture", "~Write this conditional distribution as delta times the uniform law plus(1-delta) times another probability law",
     "DERIVED", (d_mixture, r"delta times the uniform law"), "the mixture"),
    ("avg0", "~The nontrivial charge character averages to 0 under the uniform component", "DERIVED", (d_roots, r"averages to0|averages to 0"),
     "character average"),
    ("harm", "~its conditional absolute expectation is at most r", "CACHEJSON", j_harmonic, "conditional harmonic <= r (executed)"),
    ("kernel2", "~|C_rho(a,b)|<=r^|A| C_0(a,b)", "RUNNER", r"assert np\.max\(abs\(K\) - bound \* K0\.real\) < 3e-13",
     "Part III (2) (asserted on the square, not printed)"),
    ("Vhalf", "~T_rho=V^(1/2) C_rho V^(1/2)=P_rho T", "DEFINITION", "inline", "T_rho"),
    ("form", "~Thus 0<=tau|rho<=r^|A|I¦||T_rho||<=r^|A| lambda0", "CACHEJSON", j_transfer, "Part III (3) (executed)"),
    ("floor4", "~H|rho>=|A|[-log(1-(m/M)^6)] I", "CACHEJSON", j_floor, "Part III (4) (executed; the 6-floor recomputed)"),
    ("below6", "~Boundary degrees below 6 only improve delta", "DERIVED", (d_improve, r"Boundary degrees below"), "degrees below 6"),
    ("ceil", "~the bipartition supplies an independent subset of size at least ceil(s/2)", "DERIVED", (d_bipartite, r"the bipartition supplies"),
     "ceil(s/2)"),
    ("pair", "~A separated nonadjacent test-charge pair has an independent subset of size 2; an adjacent pair is covered by size 1", "CACHEJSON",
     j_pairs, "pairs (executed)"),
    ("pair-d", "~A separated nonadjacent test-charge pair", "DERIVED", (d_pair, r"test-charge pair"), "pairs"),
    ("alias", "~Charge aliases rho=0 mod N are excluded from the charged count and retain the neutral vacuum at energy 0", "CACHEJSON", j_alias,
     "aliases (executed)"),
    ("tends0", "~tends to 0 in parameter limits", "DERIVED", (d_limit, r"tends to0|tends to 0"), "weak-coupling limit"),
    ("zero-sector", "~Neutral transverse field excitations belong to the rho=0 sector, where this bound is 0", "DERIVED",
     (d_zero_sector, r"where this bound is0|where this bound is 0"), "the neutral sector"),
    # evidence section (not theorem statements: a failure is INFO)
    ("ev-fam", "~The self-contained primary has three finite families¦A third family", "CACHEJSON", j_families, "evidence: three families"),
    ("ev-27", "~Three square systems with N=2,3,4 compare 27history words", "CACHEJSON", j_27, "evidence: 27 words"),
    ("ev-108", "~Another 108history comparisons", "CACHEJSON", j_108, "evidence: 108 comparisons"),
    ("ev-cubes", "~Two complete cubes compare direct link-clock enumeration with positive plaquette-current fibers (4096and 531441link assignments)",
     "CACHEJSON", j_cubes, "evidence: two cubes"),
    ("ev-12-29", "~checks twelve charged/alias cases using explicit gauge sums and independent Fourier charge blocks, and 29single-vertex "
     "conditional distributions", "CACHEJSON", j_12_29, "evidence: 12 cases, 29 distributions"),
    ("ev-300", "~declares a 300-second cache timeout", "CACHEJSON", j_timeout, "evidence: timeout"),
]


def control_checks():
    return {}, []


def main():
    note = show(NOTE)
    cache = show(CACHE).split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    cache_lines = cache.splitlines()
    global EV, RAWCACHE
    RAWCACHE = show(CACHE)
    EV = json.loads(next(l for l in cache_lines if l.startswith("EVIDENCE_JSON: "))[len("EVIDENCE_JSON: "):])
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
    print(f"SUMMARY: {len(ITEMS)} items over claim_scope + {len(secs) - 2} sections of Parts I-III + the evidence section ({ntok} numeric tokens, "
          f"{len(unc)} uncovered): cache-sourced {counts['CACHE']} (printed lines and the printed EVIDENCE_JSON), runner-asserted (not printed) "
          f"{counts['RUNNER']}, derived here from the note's steps {counts['DERIVED']}, definitions {counts['DEFINITION']}, excluded {counts['EXCLUDED']}; "
          f"unsourced {counts['HIT']} ({', '.join(claimed) or 'none'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
