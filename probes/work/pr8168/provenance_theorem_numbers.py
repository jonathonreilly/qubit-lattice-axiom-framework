#!/usr/bin/env python3
"""J:provenance:PR8168 - every number in the theorem statements of the block 25 note (the three-dimensional formation law's ordered phase:
explanation trees, the tree count, the bound (391/100) epsilon, the thresholds, six invariant laws),
located in the runner's cached stdout, in the runner's own checks, or in an exact derivation in the note.

Statement text = the front-matter claim_scope + each '## Theorem ...' section with its proof spans ('*Proof.* ... ∎') and its '*Reading.*'
paragraphs removed.  Every
numeric token of that text (integers, decimals, fractions a/b, number words) must fall inside one listed item:
  CACHE       printed by the runner (logs/runner-cache/<runner>.txt at the PR head)                              -> sourced
  RUNNER      computed and checked by the runner source at the stated precision, not printed                     -> sourced (flagged)
  DERIVED     an exact derivation or formula stated in the note, re-executed here (fractions / sympy)             -> sourced
  DEFINITION  a constant of a declared object                                                                    -> not a claim
  EXCLUDED    a reference (block / PR number) or a structural constant of a condition, domain or notation        -> not a claim
  (else)      HIT: no runner line, no runner check, no derivation in the note; the PR files that carry it are named, and where a
              control output prints the quantity the stated value is compared with it (MISMATCH notes).
Tokens covered by no item are printed as UNCOVERED; the run is logged only with zero UNCOVERED.  Self-contained; reads the PR head via
git (fetches the branch if the commit is missing).
"""
import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PR = 8168
BRANCH = "physics-loop/admissibility-induced-law-block25-formation-law-ordered-phase-toom-stability-level-automaton-20260916"
HEAD = "c3bbf3758eb59b1d6c997389ae35738ce986dcbc"
NOTE = ("docs/ADMISSIBILITY_RULE_THREE_DIMENSIONAL_FORMATION_LAW_ORDERED_PHASE_STABILITY_OF_THE_NOISY_LEVEL_AUTOMATON_EXPLICIT_THRESHOLD_SIX_"
        "INVARIANT_LAWS_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.py"
CACHE = "logs/runner-cache/admissibility_rule_three_dimensional_formation_law_ordered_phase_stability_noisy_level_automaton_2026_09_16.txt"
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


def statement_sections(note):
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", re.sub(r"\s+", " ", norm(m.group(1))))]
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        if title.lower().startswith("theorem"):
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            body = re.sub(r"\*{1,2}Proof\.?\*{1,2}.*?(?:∎|$)", " ", body, flags=re.S)
            body = re.split(r"\*Reading\.\*", body)[0]          # interpretation paragraphs are not statements
            out.append((title.split(" — ")[0], re.sub(r"\s+", " ", norm(body))))
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
from fractions import Fraction as Fr

T_, S_ = Fr(91, 1000), Fr(1000, 107653)
DB, UB, FB = Fr(3290957526219, 10 ** 12), Fr(514547476033, 25 * 10 ** 10), Fr(943741493637, 25 * 10 ** 10)


def rbar():
    return (1 + T_ * UB) ** 3 * (1 + 3 * T_ * DB) * (1 + S_ * FB) ** 6


def derive_super():
    c1 = DB >= (1 + T_ * UB) ** 2 * (1 + 3 * T_ * DB) * (1 + S_ * FB) ** 6
    c2 = UB >= (1 + T_ * UB) ** 3 * (1 + S_ * FB) ** 6
    c3 = FB >= (1 + T_ * UB) ** 3 * (1 + 3 * T_ * DB) * (1 + S_ * FB) ** 5
    R = rbar()
    ok = c1 and c2 and c3 and R < Fr(391, 100) and min(DB, UB, FB) >= 1
    return ok, f"exact: the three super-solution inequalities {c1, c2, c3}; Rbar = {float(R):.9f} < 391/100: {R < Fr(391, 100)}"


def derive_eps0():
    ok = T_ ** 3 * S_ == Fr(7, 10 ** 6) and 753571 == 7 * 107653 and Fr(391, 100) * Fr(7, 10 ** 6) == Fr(2737, 10 ** 8) < Fr(3, 10 ** 5)
    ok = ok and Fr(7, 10 ** 6) * rbar() < Fr(391, 100) * Fr(7, 10 ** 6)
    return ok, "t^3 s = (753571/10^9)(1000/107653) = 7/10^6 (753571 = 7 x 107653); (391/100)(7/10^6) = 2737/10^8 < 3/10^5 (exact)"


def eps(p, q, r):
    p, q, r = Fr(p), Fr(q), Fr(r)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    d2 = 1 - p * p * q / (p * q * (p + q) + 4 * r ** 3)
    d3 = 1 - p * p * r / (r * (p * p + q * q) + r * r * (p + q) + 2 * r ** 3)
    return max(d1, d2, d3)


def derive_p0():
    e0 = Fr(7, 10 ** 6)
    rows = []
    ok = True
    for (q, r), p0 in (((1, 2), 285718), ((1, 1), 142861), ((2, 4), 571436), ((1, 3), 428576)):
        good = eps(p0, q, r) <= e0 < eps(p0 - 1, q, r)
        ok = ok and good
        rows.append(f"(p,{q},{r}): eps({p0}) <= eps_0 < eps({p0 - 1}): {good}")
    return ok, "closed forms of the note's T0 evaluated exactly: " + "; ".join(rows)


def derive_closed_forms():
    import sympy as sp
    p, q, r = sp.symbols("p q r", positive=True)
    # K(a | a,a,a): the six values: a gets p^3, -a gets q^3, four orthogonal values r^3 each
    k1 = p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    # K(a | a,a,b), b perp a: a: p^2 r; -a: q^2 r; b: r^2 p; -b: r^2 q; the two values perp to both: r^3 each
    k2 = p ** 2 * r / (p ** 2 * r + q ** 2 * r + r ** 2 * p + r ** 2 * q + 2 * r ** 3)
    # K(a | a,a,-a): a: p^2 q; -a: q^2 p; four orthogonal: r^3 each
    k3 = p ** 2 * q / (p ** 2 * q + q ** 2 * p + 4 * r ** 3)
    ok = (sp.simplify(k2 - p ** 2 * r / (r * (p ** 2 + q ** 2) + r ** 2 * (p + q) + 2 * r ** 3)) == 0
          and sp.simplify(k3 - p ** 2 * q / (p * q * (p + q) + 4 * r ** 3)) == 0)
    return ok, "the three normalizers summed over the six values (a, -a, and the four orthogonal) reproduce the stated closed forms (sympy)"


def derive_decreasing():
    import sympy as sp
    p, q, r = sp.symbols("p q r", positive=True)
    d1 = 1 - p ** 3 / (p ** 3 + q ** 3 + 4 * r ** 3)
    n1 = sp.factor(sp.numer(sp.together(sp.diff(d1, p))))
    ok = sp.simplify(n1 + 3 * p ** 2 * (q ** 3 + 4 * r ** 3)) == 0
    return ok, f"numerator of d_1'(p) = {n1} < 0 (the runner's B2 prints the other two)"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("ref", r"block-12 obligation S6|[Bb]lock 12's S0 \(PR #8146\)|block 08 \(PR #8138\)|Block 17 \(PR #8151\)|block 08's region", "EXCLUDED",
     "reference (blocks 08, 12, 17)", "citation"),
    ("Z3Z2", r"on Z\^(?:2|3)", "EXCLUDED", "structural: the lattices", "wording"),
    ("preds", r"x-e_1\}, eta_\{x-e_2\}, eta_\{x-e_3\}|three recorded predecessors", "DEFINITION", r"x - e_j|predecessors", "the three predecessors"),
    ("levels0", r"eta = 0 on levels <= 0", "DEFINITION", r"eta ≡ 0 on levels `?<= 0`?|eta ≡ 0", "initial condition"),
    ("arrows-forks", r"arrows \(x, x - e_i\) and forks \(x, x \+ e_i - e_j\)", "DEFINITION", r"forks", "the graph G"),
    ("edges4", r"(?:at most )?4\(n - 1\) edges|edges <= 4\(n - 1\)", "CACHE", r"edges <= 4\(n-1\)", "T4 edge bound"),
    ("forks-n1", r"(?:the forks number |exactly )?n - 1(?: forks)?", "CACHE", r"forks = n-1", "T4 fork count"),
    ("arrows3", r"(?:the arrows )?at most 3\(n - 1\)(?: arrows)?|arrows <= 3\(n - 1\)", "CACHE", r"arrows <= 3\(n-1\)", "T4 arrow bound"),
    ("Mk", r"M_k\(z\) = z_k - tau\(z\)/3", "DEFINITION", r"M_k\(z\) = z_k - tau\(z\)/3", "the functionals"),
    ("span-one", r"span rises by at least one per refinement", "CACHE", r"spanning identity", "T4 span increment"),
    ("one-arrow", r"at most one arrow to a predecessor|at most one arrow of T to a predecessor", "CACHE", r"at most one arrow to a predecessor", "T4 arrow condition"),
    ("n-ge-1", r"n >= 1 in number", "EXCLUDED", "structural", "condition"),
    ("cones", r"depth-2 backward cone(?: of x \(1024\))?|every depth-3 configuration with at most four noise sites|random (?:deeper )?cones(?: of depth 3-7)?",
     "CACHE", r"1024 noise configurations of the depth-2 backward cone|depth-3 configuration with at most four noise sites|random cones of depth 3-7",
     "T4 executed cones"),
    ("ratio3", r"the largest ratio observed is below 3", "CACHE", r"largest ratios 7/3, 11/4", "T4 executed ratio"),
    ("twelve", r"(?:the )?twelve edge types", "DEFINITION", r"twelve edge types", "the typed tree"),
    ("tsvals", r"\(?t, s\)? = \(91/1000, 1000/107653\)|t = 91/1000, s = 1000/107653", "CACHE", r"\(t, s\) = \(91/1000, 1000/107653\)", "T5 point"),
    ("sum391", r"(?:the sum is below |< )391/100|R ?bar := .*?< 391/100", "CACHE", r"< 391/100", "T5 bound"),
    ("trees66103", r"66103 trees with at most four edges|number 66103|with at most four edges", "CACHE", r"number 66103", "T5 executed count"),
    ("three-term", r"three-term recursion", "CACHE", r"recursion", "T5 recursion"),
    ("bars", r"Dbar = 3290957526219/10\^12, Ubar = 514547476033/\(25\*10\^10\), Fbar = 943741493637/\(25\*10\^10\)", "RUNNER",
     r"Fraction\(3290957526219, 10 \*\* 12\), Fraction\(514547476033, 25 \* 10 \*\* 10\), Fraction\(943741493637, 25 \* 10 \*\* 10\)",
     "T5 super-solution (hard-coded and checked in the runner's E1, not printed)"),
    ("super", r"Dbar >= \(1 \+ tUbar\)\^2\(1 \+ 3tDbar\)\(1 \+ sFbar\)\^6, Ubar >= \(1 \+ tUbar\)\^3\(1 \+ sFbar\)\^6, Fbar >= \(1 \+ tUbar\)\^3\(1 \+ 3tDbar\)\(1 \+ sFbar\)\^5",
     "DERIVED", (derive_super, r"super-solution"), "T5 the three inequalities"),
    ("Rbar", r"Rbar := \(1 \+ tUbar\)\^3\(1 \+ 3tDbar\)\(1 \+ sFbar\)\^6 < 391/100", "CACHE", r"R-bar = \(1 \+ t U-bar\)\^3 \(1 \+ 3 t D-bar\)\(1 \+ s F-bar\)\^6 < 391/100",
     "T5 Rbar"),
    ("T5-exec", r"counted by \(a, f\), each count is at most the coefficient of t\^a s\^f in the recursion's series, computed exactly - equal for at most two edges, below it for every pair with four edges - and the coefficients for at most three edges",
     "CACHE", r"equal for at most two edges, below it for every pair with four edges", "T5 executed comparison"),
    ("T6", r"(?:P\(eta_x = 1\) <= )?\(391/100\) ?\*? ?epsilon <= 3/10\^5|epsilon\*Rbar < \(391/100\)\*epsilon <= 2737/10\^8 < 3/10\^5", "CACHE",
     r"\(391/100\) epsilon_0 = 2737/10\^8", "T6 bound"),
    ("eps0", r"epsilon(?:_0)? (?:<= |:= |= )?(?:epsilon_0 := )?7/10\^6|epsilon_0 = 7/10\^6", "CACHE", r"epsilon_0 = 7/10\^6", "T6/T7 eps_0"),
    ("eps0-arith", r"<= 2737/10\^8", "DERIVED", (derive_eps0, r"753571 = 7\*107653|753571"), "T6 arithmetic"),
    ("T0-closed", r"K\(a \| a,a,a\) = p\^3/\(p\^3 \+ q\^3 \+ 4r\^3\), K\(a \| a,a,b\) = p\^2r/\(r\(p\^2 \+ q\^2\) \+ r\^2\(p \+ q\) \+ 2r\^3\), K\(a \| a,a,-a\) = p\^2q/\(pq\(p \+ q\) \+ 4r\^3\)",
     "DERIVED", (derive_closed_forms, r"the normalizer is"), "T0(a) closed forms"),
    ("T0-devs", r"d_1 = 1 - p\^3/\(p\^3\+q\^3\+4r\^3\), d_2 = 1 - p\^2q/\(pq\(p\+q\)\+4r\^3\), d_3 = 1 - p\^2r/\(r\(p\^2\+q\^2\) \+ r\^2\(p\+q\) \+ 2r\^3\)",
     "CACHE", r"closed forms", "T0(a) deviations"),
    ("eps-def", r"epsilon\(p, q, r\) = max\(1 - p\^3/\(p\^3 \+ q\^3 \+ 4 r\^3\), 1 - p\^2 q/\(p q \(p \+ q\) \+ 4 r\^3\), 1 - p\^2 r/\(r \(p\^2 \+ q\^2\) \+ r\^2 \(p \+ q\) \+ 2 r\^3\)\)",
     "CACHE", r"epsilon\(p, q, r\) as the exact maximum", "T7 eps closed form"),
    ("T0-decr", r"(?:strictly )?decreasing in p(?: > 0 for fixed q, r > 0)?", "DERIVED", (derive_decreasing, r"d_1' = "), "T0(b)"),
    ("T0-216", r"all 216 triples with at least two entries a", "CACHE", r"all 216 triples with two entries a", "T0 executed triples"),
    ("T0-couplings", r"at \(3, 1, 2\) and \(10, 1, 2\)", "CACHE", r"at \(3,1,2\), \(10,1,2\)", "T0 executed couplings"),
    ("p0-12", r"(?:[Aa]t \(p, 1, 2\) )?(?:this holds )?for every integer p >= 285718(?: and fails the condition epsilon <= epsilon_0 at p = 285717)?", "CACHE", r"285718 at \(1,2\)",
     "T7(b) threshold"),
    ("p0-others", r"at \(p, 1, 1\), \(p, 2, 4\), \(p, 1, 3\) the least such integers are 142861, 571436, 428576", "CACHE",
     r"142861 at \(1,1\), 571436 at \(2,4\), 428576 at \(1,3\)", "T7(b) other lines"),
    ("p0-exact", r"the least such integers", "DERIVED", (derive_p0, r"evaluates `?epsilon`? exactly"), "T7(b) recomputed"),
    ("six", r"(?:at least )?six (?:pairwise distinct )?(?:translation-invariant )?(?:invariant laws|extremal invariant laws|such laws)", "CACHE",
     r"the six invariant laws", "T7(c) six laws"),
    ("one-per-value", r"one per value", "CACHE", r"the six invariant laws", "T7(c)"),
    ("T7a", r"P\(v_x != a\) <= 3/10\^5", "CACHE", r"<= 3/10\^5", "T7(a)"),
    ("mu-bound", r"mu_a\(v_y != a\) <= 3/10\^5", "CACHE", r"<= 3/10\^5", "T7(c)"),
    ("thousand", r"a thousand times the first count's", "DERIVED", (lambda: (Fr(7, 10 ** 6) / (Fr(1, 2 * 96 ** 4)) > 1000,
     f"eps_0/(1/(2 * 96^4)) = {float(Fr(7, 10 ** 6) * 2 * 96 ** 4):.1f} > 1000 (the first count's threshold 1/(2*96^4), Prior art)"), r"1/\(2\*96\^4\)"),
     "T7 placement"),
    ("eta-values", r"every 1 at a site x|1\{v_x != a\}|P\(v_x != a\) <= P\(eta_x = 1\)|Let eta_x = 1|P\(eta_x = 1\)", "EXCLUDED",
     "structural: the value 1 of the 0/1 automaton", "notation"),
    ("names", r"three-dimensional|six-axis|the three deviations", "EXCLUDED", "names of the objects", "wording"),
    ("pronoun", r"a point of one to a point of the other|one of the C_k|the nodes without one|and this one|fork pair", "EXCLUDED", "wording", "wording"),
    ("b08-region", r"its region 3c < 1", "EXCLUDED", "reference: block 08's criterion", "citation"),
    ("zero-one", r"1-predecessor|1-site|non-noise|two distinct clusters|two-point subsets|one point each|every leaf|pairwise disjoint", "EXCLUDED",
     "structural: names of objects", "wording"),
    ("T2-third", r"M_k\(Excuse_k\(v\)\) = M_k\(v\) \+ 1/3", "CACHE", r"1/3 - delta_jk", "T2(a)"),
    ("T2-span1", r"Sigma_k M_k\(Excuse_k\(v_k\)\) = Span \+ 1", "CACHE", r"1/3 - delta_jk", "T2(a) sum"),
    ("T2-size1", r"has Size = 1, so any spanned set with base \{w, w'\} has Span <= 1", "CACHE", r"every fork pair has Size = 1", "T2(b)"),
    ("T1-levels", r"at level s >= 2|at level s - 1", "EXCLUDED", "structural: levels", "wording"),
    ("T3-poles", r"u_\{X,1\}, u_\{X,2\}, u_\{X,3\}|C_1, C_2, C_3|\(L, u_1, u_2, u_3\)|\(P, v_1, v_2, v_3\)", "EXCLUDED", "structural: pole labels", "wording"),
]


def control_checks():
    return {}, []


def main():
    note = show(NOTE)
    cache = show(CACHE).split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    cache_lines = cache.splitlines()
    runner_src = norm(show(RUNNER))
    declared = section(note, "Premises and declared objects")
    other = {p: show(p) for p in OTHER}
    secs = statement_sections(note)
    covered = {name: set() for name, _ in secs}
    counts = {k: 0 for k in ("CACHE", "RUNNER", "DERIVED", "DEFINITION", "EXCLUDED", "HIT")}
    hits = []
    print(f"PR #{PR} head {HEAD[:10]}; cache {len(cache_lines)} stdout lines; statement sections: {', '.join(n for n, _ in secs)}")
    for item in ITEMS:
        iid, pat, kind, src, role = item[:5]
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
            found = re.search(locate, norm(note)) is not None
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
    print(f"SUMMARY: {len(ITEMS)} items over claim_scope + {len(secs) - 1} theorem sections ({ntok} numeric tokens, {len(unc)} uncovered): "
          f"cache-sourced {counts['CACHE']}, runner-checked (not printed) {counts['RUNNER']}, derived here from the note's formulas {counts['DERIVED']}, definitions {counts['DEFINITION']}, "
          f"excluded {counts['EXCLUDED']}; unsourced {counts['HIT']} = {len(claimed)} in the proved statements ({', '.join(claimed) or 'none'}) + "
          f"{len(execd)} executed-not-claimed numbers printed only by controls; stated values disagreeing with the control output: "
          f"{', '.join(mism) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
