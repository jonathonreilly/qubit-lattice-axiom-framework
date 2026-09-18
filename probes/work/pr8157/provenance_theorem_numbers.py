#!/usr/bin/env python3
"""J:provenance:PR8157 - every number in the theorem statements of the block 23 note (plane correlations of the sphere static law decay
algebraically at every coupling; complex rotations; explicit exponent),
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
PR = 8157
BRANCH = "physics-loop/admissibility-induced-law-block23-sphere-static-law-plane-algebraic-decay-complex-rotations-20260915"
HEAD = "debbd76649e8a08469114e2dbfa52d1d1fd3e022"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_PLANE_CORRELATIONS_DECAY_ALGEBRAICALLY_AT_EVERY_COUPLING_COMPLEX_ROTATIONS_"
        "EXPLICIT_EXPONENT_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_plane_algebraic_decay_complex_rotations_2026_09_15.txt"
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
        if re.match(r"(theorem|corollary|lemma|proposition)\b", title.lower()):
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
import sympy as sp


def derive_three_halves():
    s0 = sp.symbols("a1:4", real=True)
    sx = sp.symbols("b1:4", real=True)
    pairs = (s0[0] * sx[0] + s0[1] * sx[1]) + (s0[1] * sx[1] + s0[2] * sx[2]) + (s0[0] * sx[0] + s0[2] * sx[2])
    ok = sp.expand(pairs - 2 * sum(a * b for a, b in zip(s0, sx))) == 0
    return ok, "the three pair sums add to 2 s_0.s_x, each bounded by the same exponential, so |<s_0.s_x>| <= (3/2) x bound (sympy)"


def derive_bondsum_constant():
    g = sp.symbols("gamma", positive=True)
    H = sp.symbols("H", positive=True)
    ok = sp.simplify((g ** 2 * sp.cosh(g) / 2) * 4 * (1 + 8 * H) - 2 * g ** 2 * sp.cosh(g) * (1 + 8 * H)) == 0
    return ok, "(gamma^2 cosh(gamma)/2) x 4 (four bonds per site) x (1 + 8 H_R) = 2 gamma^2 cosh(gamma) (1 + 8 H_R) (sympy)"


def derive_p3_exponents():
    b, g, c, lR = sp.symbols("beta gamma C logR", positive=True)   # C = cosh(gamma), logR = log(1 + R)
    expo = -g * lR + 2 * b * g ** 2 * c * (1 + 8 * (1 + lR))           # H_R <= 1 + log(1 + R)
    target = 18 * b * g ** 2 * c - (g - 16 * b * g ** 2 * c) * lR
    ok = sp.expand(expo - target) == 0
    return ok, "-gamma log(1+R) + 2 beta gamma^2 cosh(gamma)(1 + 8(1 + log(1+R))) = 18 beta gamma^2 cosh(gamma) - (gamma - 16 beta gamma^2 cosh(gamma)) log(1+R)"


def derive_p4_constants():
    ok = sp.nsimplify(4 * sp.Rational(3, 2)) == 6
    return ok, "4 C_1 = 4 (3/2) e^{9/16} = 6 e^{9/16} (the runner's D3 prints 4 C_1); the x = 0 term 1/N with N = 4L^2 gives 1/(4L^2)"


def derive_P2b():
    t = sp.symbols("t", nonnegative=True)
    ok = sp.diff(sp.log(1 + t), t) == 1 / (1 + t)
    return ok, "|log(1+p) - log(1+q)| <= |p - q|/(1 + min(p, q)) from (log(1+t))' = 1/(1+t) (cache C2 prints the derivative)"


def info_upper_bound():
    rows = []
    for beta in (1, 5):
        kappa = sp.Rational(5, 512) / beta
        c1 = sp.Rational(3, 2) * sp.exp(sp.Rational(9, 16))
        ok = all(float(1 / sp.Integer(1 + d)) <= float(c1 * sp.Integer(1 + d) ** (-kappa)) for d in (1, 10, 100, 10 ** 4, 10 ** 8))
        rows.append(f"beta={beta}: a decay (1+d)^-1 satisfies the bound (3/2)e^(9/16)(1+d)^-{float(kappa):.5f} at d = 1..10^8: {ok}")
    return "; ".join(rows)


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("torus", r"\(Z/2LZ\)\^2", "DEFINITION", r"\(Z/2LZ\)\^2", "the torus"),
    ("HR", r"H_R = sum_\{j<=R\} 1/j", "DEFINITION", r"H_R = Sigma_\{j=1\}\^R 1/j", "H_R"),
    ("kappa", r"kappa\(beta\) = 5/\(512 ?beta\) for beta >= 5/256(?:,| and) kappa\(beta\) = 1 - 128 ?beta/5(?: >= 1/2)? for beta <= 5/256", "CACHE",
     r"maximum 5/\(512 beta\)", "kappa(beta)"),
    ("components", r"s_0\^1 s_x\^1 \+ s_0\^2 s_x\^2|\(2, 3\) and \(1, 3\)|the other two component pairs", "EXCLUDED", "component labels", "notation"),
    ("three-halves", r"\(3/2\)(?: times the same| exp\(a_x - a_0 \+ beta Sigma_b \(cosh\(a_y - a_z\) - 1\)\))", "DERIVED", (derive_three_halves, r"sum of the three pair sums"), "P1 factor 3/2"),
    ("P1", r"\|<s_0\^1 s_x\^1 \+ s_0\^2 s_x\^2>\| <= exp\( ?a_x - a_0 \+ beta (?:sum|Sigma)_b \(cosh\(a_y - a_z\) - 1\) ?\)", "CACHE",
     r"\|e\^\{c cos\(phi \+ i a\)\}\| = e\^\{c cos phi cosh a\}", "P1 (B1 the modulus identity behind it)"),
    ("P2b", r"\|a_y - a_z\| <= gamma/\(1 \+ min\(d\(y\), d\(z\)\)\)(?: <= gamma)?", "DERIVED", (derive_P2b, r"the derivative of"), "P2(b)"),
    ("P2c", r"(?:sum|Sigma)_b \(cosh\(a_y - a_z\) - 1\) <= 2 ?gamma\^2 cosh ?\(?gamma\)? \(1 \+ 8 ?H_R\)", "DERIVED",
     (derive_bondsum_constant, r"Multiply"), "P2(c) constant"),
    ("shift", r"a_y = gamma max\(0, log\(\(1\+R\)/\(1\+d\(y\)\)\)\)", "DEFINITION", "inline", "the shift function (defined in P2's statement)"),
    ("P3gen", r"\(3/2\) (?:e\^\{18 beta gamma\^2 cosh gamma\}|exp\(18betagamma\^2 cosh gamma\)) \(1 \+ R\)\^\{-\(gamma - 16 ?beta ?gamma\^2 cosh gamma\)\}",
     "DERIVED", (derive_p3_exponents, r"the exponent is at most"), "P3 general gamma"),
    ("gamma-choice", r"gamma = min\(1, 5/\(256 ?beta\)\)", "CACHE", r"maximizer gamma\* = 5/\(256 beta\)", "P3 choice of gamma"),
    ("cosh1", r"cosh 1 <= 8/5", "CACHE", r"cosh 1 <= \(11/4 \+ 3/8\)/2 = 25/16 <= 8/5", "P3 constant"),
    ("P3final", r"\(3/2\) e\^\{9/16\} \(1 \+ (?:d\(x\)|\|x\|)\)\^\{-kappa\(beta\)\}", "CACHE", r"equals 9/16 at beta = 5/256", "P3 final bound (9/16)"),
    ("P4a", r"M_N\^2 <= 6 ?e\^\{9/16\} ?\(1 \+ L\)\^\{-(?:min\(kappa, 1\)|kappa')\} \+ 1/\(4 ?L\^2\)", "DERIVED", (derive_p4_constants, r"4C_1 = 6e\^\{9/16\}"),
     "P4(a) constants"),
    ("kprime", r"kappa' = min\(kappa\(beta\), 1\)", "DEFINITION", "inline", "kappa' (defined in P4's statement)"),
    ("P4-exec", r"shell sum inequality at kappa' = 1/2 and kappa' = 1 for L <= 40", "RUNNER", r"for L in range\(1, 41\)",
     "P4 executed range (the cache prints the two exponents, not L <= 40)"),
    ("P4-exp", r"at kappa' = 1/2 and kappa' = 1", "CACHE", r"at kappa' = 1 \(exact sums\) and kappa' = 1/2", "D3 exponents"),
    ("B4", r"\(Sigma_\{m<=4\}\(c cos phi\)\^m/m!\) e\^\{iphi\}, whose period integral pic\(c\^2 \+ 8\)/8 is nonzero", "CACHE",
     r"pi c \(c\^2 \+ 8\)/8", "P1 executed polynomial"),
    ("ineq", r"\(1 - cos theta\)\(cosh tau - 1\) >= 0", "CACHE", r"\(1 - cos phi\)\(cosh a - 1\) >= 0", "B2"),
    ("R60", r"Sigma_\{j<=R\} 8j/\(1\+j\)\^2 <= 8H_R for R <= 60", "CACHE", r"sum_\{j<=R\} 8j/\(1\+j\)\^2 <= 8 H_R exactly for R <= 60", "C1"),
    ("P2a", r"a_0 = gamma log\(1\+R\), a_x = 0, and a_z = 0 at every exterior site", "EXCLUDED", "structural: values of the defined shift", "definition"),
    ("P2-zero", r"a_y = a_z = 0 unless min\(d\(y\), d\(z\)\) < R", "EXCLUDED", "structural", "definition"),
    ("conds", r"R = d\(x\) >= 1|gamma > 0|every beta > 0|L >= 1|x != 0|zero at exterior sites|a_z = 0 at exterior sites|-> 0 as \|x\| -> ∞|d\(y\) < R",
     "EXCLUDED", "structural: conditions and limits", "condition"),
    ("dims", r"two dimensions|Z\^2|Z\^3|0, x in Λ", "EXCLUDED", "structural", "wording"),
    ("labels", r"B1-B2, B4|\(B3\)|\(C1\)|\(C2\)|\(D1\)|\(D2, D4\)|\(D3\)|\(E1\)|block 19's", "EXCLUDED", "labels and references", "labels"),
    ("imports", r"Two standard mathematical imports|should one exist|the two branches", "EXCLUDED", "wording", "wording"),
    ("two-site", r"the solvable two-site instance", "CACHE", r"the solvable two-site instance", "E1"),
    ("P4b", r"\|<s_0\*s_x>_ν\| <= \(3/2\)e\^\{9/16\}\(1 \+ \|x\|\)\^\{-kappa\(beta\)\}", "CACHE", r"infinite-volume laws on the plane", "P4(b)"),
]


def control_checks():
    return {}, ["INFO (numbers only): " + info_upper_bound() + " - the bound in P3/P4(b) is an upper bound whose exponent kappa(beta) -> 0 as beta grows"]


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
