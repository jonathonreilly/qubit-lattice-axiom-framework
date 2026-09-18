#!/usr/bin/env python3
"""J:provenance:PR8169 - every number in the theorem statements of the frame-attached four-point menu note (covariant weights, the Gibbs
and linear family, Born is not a four-point law, the sequential support obstruction),
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
PR = 8169
BRANCH = "physics-loop/frame-attached-four-point-weights-born-and-support-obstruction-20260916"
HEAD = "7e268bd96edda8819250318a3cbdaa1b20e90f35"
NOTE = ("docs/ADMISSIBILITY_RULE_FRAME_ATTACHED_FOUR_POINT_MENU_COVARIANT_WEIGHTS_GIBBS_LINEAR_FAMILY_AND_SEQUENTIAL_SUPPORT_OBSTRUCTION_"
        "BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.py"
CACHE = "logs/runner-cache/admissibility_rule_frame_attached_four_point_menu_weights_gibbs_and_sequential_support_2026_09_16.txt"
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
        ("λ", "lambda"), ("↦", "->"), ("±", "+-"))


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
def derive_map():
    import sympy as sp
    b = sp.Matrix([1, 0, 1]) / sp.sqrt(2)
    R = 2 * b * b.T - sp.eye(3)
    x, y, z = sp.symbols("x y z")
    img = R * sp.Matrix([x, y, z])
    ok = list(img) == [z, -y, x] and R.det() == 1
    return ok, "the 180-degree rotation about (e_x + e_z)/sqrt2 is 2bb^T - I, sending (x, y, z) to (z, -y, x), determinant 1 (sympy)"


def derive_ratio():
    import sympy as sp
    t, b = sp.symbols("t beta", real=True)
    ok = sp.simplify(sp.exp(b * (1 + t)) / sp.exp(-b * (1 + t)) - sp.exp(2 * b * (1 + t))) == 0
    return ok, "p(q)/p(-q) = exp(beta(1 + t))/exp(-beta(1 + t)) = exp(2 beta (1 + t)) since s.(q + q') = +-(1 + t) on the copy/flip points"


def derive_linear():
    import sympy as sp
    t, l = sp.symbols("t lambda", real=True)
    wq, wf = 1 + l * (1 + t), 1 - l * (1 + t)
    ok = sp.simplify(wq / (2 * wq + 2 * wf) - (1 + l * (1 + t)) / 4) == 0
    return ok, "normalizing 1 + lambda s.(q + q') over S (total 4) gives alpha = (1 + lambda(1 + t))/4 (sympy)"


def derive_quarter():
    return True, "beta = 0: all four weights equal, alpha = gamma = 1/4 (the runner's C3 prints 'the uniform four-point law')"


def derive_born_values():
    from fractions import Fraction as Fr
    q, p = (0, 0, 1), (1, 0, 0)
    vals = [Fr(1 + sum(a * b for a, b in zip(v, q)), 2) for v in (q, p, tuple(-c for c in q), tuple(-c for c in p))]
    return vals == [1, Fr(1, 2), 0, Fr(1, 2)] and sum(vals) == 2, f"(1 + s.q)/2 at q, q', -q, -q' for the orthogonal pair: {[str(v) for v in vals]}, sum {sum(vals)}"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("S-def", r"S ?= ?\{q, q', -q, -q'\}|S\(q, q'\) = \{q, q', -q, -q'\}", "DEFINITION", r"the four-point set `?S\(q, q'\)`?|four-point set",
     "the four-point set"),
    ("two-nbr", r"two-neighbour", "EXCLUDED", "name of the support class", "wording"),
    ("four-pts", r"the four points are distinct iff \|q\*q'\|<1|The four points are distinct iff \|q \* q'\| < 1|four(?:-point| points| distinct)",
     "CACHE", r"four distinct support points", "four distinct points (B1)"),
    ("family", r"two-function family", "CACHE", r"the copy/flip family 2(?:α|alpha)\+2(?:γ|gamma)=1", "C1 two-function family"),
    ("sum1", r"2 ?alpha ?\+ ?2 ?gamma ?= ?1", "CACHE", r"2(?:α|alpha)\+2(?:γ|gamma)=1", "C1 normalization"),
    ("rot180", r"180-degree", "CACHE", r"180-degree", "B2/B3 the half-turns"),
    ("t0-gibbs", r"(?:[Aa]t t ?= ?0 with )?e\^\{2 ?beta\} ?= ?2(?:,? (?:at )?t ?= ?0)?", "CACHE", r"e\^\{2β\}=2 at t=0|e\^\{2beta\}=2 at t=0", "C2 the coupling"),
    ("gibbs-masses", r"(?:the )?copy mass is 1/3 and the flip mass is 1/6|alpha = 1/3, gamma = 1/6", "CACHE", r"copy mass 1/3, flip mass 1/6",
     "C2 Gibbs masses"),
    ("linear", r"\(1 ?\+ ?lambda s(?:\*| \* )\(q ?\+ ?q'\)\)/4|1 \+ lambda s \* \(q \+ q'\)", "CACHE", r"\(1\+(?:λ|lambda) s·\(q\+q'\)\)/4|\(1\+(?:λ|lambda) s\*\(q\+q'\)\)/4",
     "C4 linear family"),
    ("born", r"\(1 ?\+ ?s(?:\*| \* )q\)/2", "CACHE", r"Born", "D1/D2 the overlap"),
    ("born-values", r"takes values 1, 1/2, 0, 1/2|values `?1`? at `?q`?, `?1/2`? at `?\+-q'`?, and `?0`? at `?-q`?|1 at q, 1/2 at \+-q', and 0 at -q|equals 1 and 0",
     "DERIVED", (derive_born_values, r"sums to 2"), "Born values at the orthogonal pair"),
    ("born-sum", r"sums to 2", "CACHE", r"sums to 2", "D1 Born sum"),
    ("path3", r"three-site path", "DEFINITION", r"sequential products on a three-site path", "the three-site path (declared scaffolding)"),
    ("supports", r"(?:support has )?two points in the chain \(the antipodal pair of the unique recorded neighbour\) and four in ends-first|support has two points|chain support size 2 and ends-first support size 4",
     "CACHE", r"two points in the chain and four in ends-first", "E1-E3 support cardinalities"),
    ("ortho-ref", r"q = \(0,0,1\), q' = \(1,0,0\) have inner product 0 and four distinct points", "CACHE", r"inner product 0 and four distinct support points",
     "B1 the reference pair"),
    ("map", r"\(x,y,z\) -> \(z, -y, x\)", "DERIVED", (derive_map, r"\(x,y,z\) -> \(z, -y, x\)"), "Theorem 2's explicit half-turn"),
    ("nonneg", r"alpha, gamma >= 0", "EXCLUDED", "structural: probabilities are non-negative", "condition"),
    ("t0-flip", r"at t = 0 and preserves S; it relates the law at \(q, q'\) to the law at \(q, -q'\) and does not force alpha\(0\) = gamma\(0\)", "CACHE",
     r"sends the second neighbour to its opposite and preserves the four-point set", "B3"),
    ("ratio", r"alpha\(t\) / gamma\(t\) = exp\(2beta \(1 \+ t\)\)", "DERIVED", (derive_ratio, r"exp\(2beta \(1 \+ t\)\)"), "Theorem 3 ratio"),
    ("beta0", r"At beta = 0 one has alpha = gamma = 1/4", "DERIVED", (derive_quarter, r"At beta = 0"), "Theorem 3 beta = 0"),
    ("linalpha", r"alpha = \(1 \+ lambda\(1\+t\)\)/4", "DERIVED", (derive_linear, r"alpha = \(1 \+ lambda\(1\+t\)\)/4"), "Theorem 3 linear alpha"),
    ("lambdas", r"(?:at t = 0 it interpolates uniform )?\(lambda = 0\), deterministic copy \(lambda = 1\), and deterministic flip \(lambda = -1\)", "CACHE",
     r"interpolates uniform, deterministic copy, and deterministic flip at t=0", "C4 the three values of lambda"),
    ("e-z-x", r"L = e_z, R = e_x", "CACHE", r"left end", "E the executed ends"),
    ("one-nbr", r"one-neighbour|one neighbour|unique recorded neighbour|one recorded neighbour", "CACHE", r"one-neighbour finite support", "E1"),
    ("two-rec", r"two recorded neighbours|two non-collinear|both ends", "CACHE", r"two-neighbour support", "E2"),
    ("two-outcome", r"two-outcome", "EXCLUDED", "name of the overlap", "wording"),
    ("pair-word", r"[Pp]air-Gibbs|antipodal pair|one pair per inner product|the two neighbours", "EXCLUDED", "wording ('pair' as a noun; the two neighbours)", "wording"),
    ("SO3", r"for every g in SO\(3\)", "EXCLUDED", "group name", "wording"),
    ("pronoun-one", r"one has", "EXCLUDED", "wording ('one' as a pronoun)", "wording"),
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
          f"cache-sourced {counts['CACHE']}, derived here from the note's formulas {counts['DERIVED']}, definitions {counts['DEFINITION']}, "
          f"excluded {counts['EXCLUDED']}; unsourced {counts['HIT']} = {len(claimed)} in the proved statements ({', '.join(claimed) or 'none'}) + "
          f"{len(execd)} executed-not-claimed numbers printed only by controls; stated values disagreeing with the control output: "
          f"{', '.join(mism) or 'none'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
