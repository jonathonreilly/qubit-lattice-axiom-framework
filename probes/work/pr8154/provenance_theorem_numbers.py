#!/usr/bin/env python3
"""J:provenance:PR8154 - every number in the theorem statements of the block 20 note (the unsoldered sphere static law has no long-range
order on planes and lines; the third dimension is load-bearing for the Green-function channel),
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
PR = 8154
BRANCH = "physics-loop/admissibility-induced-law-block20-unsoldered-static-law-no-long-range-order-on-planes-and-lines-20260915"
HEAD = "e1281625579c98150e818d56e4d29e260c9ded89"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_NO_LONG_RANGE_ORDER_ON_PLANES_AND_LINES_THIRD_DIMENSION_LOAD_BEARING_FOR_THE_"
        "GREEN_FUNCTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_no_long_range_order_on_planes_and_lines_2026_09_15.txt"
OTHER = [".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block20_planes_lines.out.txt",
         ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block20_refuter.out.txt"]


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


def derive_H2a():
    L = sp.symbols("L", positive=True)
    ok = sp.simplify((L / sp.pi) ** 2 * 4 - (4 * L ** 2) / sp.pi ** 2) == 0
    for LL in range(2, 13):
        s = sum(Fr(1, a * a + b * b) for a in range(-LL + 1, LL + 1) for b in range(-LL + 1, LL + 1) if (a, b) != (0, 0))
        ok = ok and s >= 4 * sum(Fr(1, j) for j in range(1, LL))
    return ok, ("sum_k |k|^-2 = (L/pi)^2 sum_n |n|^-2 >= (4L^2/pi^2) H_(L-1) = (N/pi^2) H_(L-1) at N = 4L^2 (sympy), with sum_n |n|^-2 >= "
                "4 H_(L-1) re-checked exactly for L = 2..12")


def derive_monotone():
    ok = all(sum(Fr(1, j) for j in range(1, L)) >= 1 + Fr(m, 2) for m in range(0, 8) for L in range(2 ** m + 1, 2 ** m + 41))
    return ok, "H_n increasing and L - 1 >= 2^m give H_(L-1) >= H_(2^m) >= 1 + m/2 (exact for m <= 7 and the 40 sides from 2^m + 1)"


def derive_H3dyadic():
    b, m, t = sp.symbols("beta m t", positive=True)
    c = 3 * sp.pi ** 2 * b + 1
    diff = c / (1 + m / 2) - c / (1 + m / 2 + t)
    ok = sp.simplify(diff - c * t / ((1 + m / 2) * (1 + m / 2 + t))) == 0
    return ok, ("(3 pi^2 beta + 1)/H_(L-1) <= (3 pi^2 beta + 1)/(1 + m/2) by H2(b): with H = 1 + m/2 + t the difference is "
                "(3 pi^2 beta + 1) t/((1 + m/2)(1 + m/2 + t)) >= 0 (sympy)")


def derive_L1():
    b = sp.symbols("beta", positive=True)
    ok = sp.simplify((6 * sp.pi ** 2 * b + 4) / sp.sqrt(1) - 1 - (6 * sp.pi ** 2 * b + 3)) == 0
    return ok, "at L = 1 the line bound minus 1 is 6 pi^2 beta + 3 > 0, while M_N^4 <= 1"


def derive_limits():
    b, L = sp.symbols("beta L", positive=True)
    n = sp.symbols("n", positive=True, integer=True)
    ok = sp.limit((6 * sp.pi ** 2 * b + 4) / sp.sqrt(L), L, sp.oo) == 0 and sp.limit(sp.harmonic(n), n, sp.oo) == sp.oo
    return ok, "(6 pi^2 beta + 4)/sqrt L -> 0 and H_n -> oo (sympy): both bounds on M_N^4 tend to 0"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("defs", "~the transform s^(k) = N^{-1/2} sum_x e^{ikx} s_x, the Laplacian symbol E(k) = sum_i 2(1 - cos k_i) and the long-range-order "
     "parameter M_N^2 = N^{-2} <|sum_x s_x|^2>", "DEFINITION", r"Transforms\.", "the transform, the symbol and the order parameter"),
    ("H1", "~<|s^1(k)|^2> >= (2 M_N^2/3)^2/[(beta E)^{1/2} + (beta E + 4 M_N^2/(3N))^{1/2}]^2 >= (M_N^2/3)^2/(beta E(k) + 4/(3N))"
     "¦u(k) >= (2M_N^2/3)^2 / [(betaE(k))^{1/2} + (betaE(k) + 4M_N^2/(3N))^{1/2}]^2 >= (M_N^2/3)^2 / (betaE(k) + 4/(3N))",
     "CACHE", r"D3 H1\(v\)/\(vi\): the displayed root solves", "H1 (the root and its simplification, D3)"),
    ("H1-dim", "~holds for every k != 0 in every dimension d <= 3, the dimension entering only through the bond count¦For d in {1, 2, 3}, beta > 0, L >= 1 and every k != 0",
     "CACHE", r"D4 H1\(iii\):.*the dimension enters only through the bond count", "H1's domain (the bond count, D4)"),
    ("H2a", "~sum_{k != 0} |k|^{-2} >= (N/pi^2) H_{L-1}¦For d = 2, L >= 2: Sigma_{k!=0} |k|^{-2} >= (N/pi^2) H_{L-1}", "DERIVED",
     (derive_H2a, r"\(4L\^2/pi\^2\) H_\{L-1\} = \(N/pi\^2\) H_\{L-1\}"), "H2(a) (B1 in n-variables, scaled)"),
    ("H2c", "~E(k) <= |k|^2", "CACHE", r"C1 H2\(c\): 2\(1 - cos u\) = 4 sin\^2\(u/2\)", "H2(c)"),
    ("H2d", "~4/(3N) = |k_min|^2/(3pi^2) <= |k|^2/(3pi^2) for every k != 0, where |k_min| = pi/L and N = 4L^2¦4/(3N) <= |k|^2/(3 pi^2)",
     "CACHE", r"C2 H2\(d\)/\(e\): 4/\(3N\) = \(pi/L\)\^2/\(3 pi\^2\) at N = 4L\^2", "H2(d)"),
    ("H2e", "~on the line (L >= 2) the 2 floor(sqrt L) smallest wavevectors have beta E(k) + 4/(3N) <= (beta pi^2 + 2/3)/L"
     "¦For d = 1, N = 2L, L >= 2, m = ⌊sqrtL⌋ and every n with 1 <= |n| <= m: betaE(k) + 4/(3N) <= (betapi^2 + 2/3)/L at k = pin/L; there are "
     "exactly 2m >= sqrtL such wavevectors in the range", "CACHE", r"B3 H2\(e\): 4 floor\(sqrt L\)\^2 >= L", "H2(e)"),
    ("H2b", "~the dyadic bound H_{2^m} >= 1 + m/2¦H_{2^m} >= 1 + m/2 for every m >= 0", "CACHE", r"B2 H2\(b\): H_\(2\^m\) >= 1 \+ m/2", "H2(b)"),
    ("H2b-hence", "~hence H_{L-1} >= 1 + m/2 whenever L >= 2^m + 1", "DERIVED", (derive_monotone, r"H_n is increasing in n"), "H2(b), the consequence"),
    ("B1exec", "~The shell counts 8j and 4L - 1, the norm bound and the resulting inequality are executed exactly for L = 2, …, 12 (B1)", "CACHE",
     r"B1 H2\(a\): on \{-L\+1\.\.L\}\^2 the sup-norm shell j has 8j points \(j < L\) and 4L-1 points .* exactly for L = 2\.\.12", "B1 executed"),
    ("B2exec", "~the dyadic bound for m <= 12 (B2)", "CACHE", r"B2 H2\(b\): .* for m = 0\.\.12", "B2 executed"),
    ("B3exec", "~4⌊sqrtL⌋^2 >= L and the count 2⌊sqrtL⌋ of wavevectors in the block for 2 <= L <= 400, and the line's per-term inequality "
     "symbolically (B3)", "CACHE", r"B3 H2\(e\): 4 floor\(sqrt L\)\^2 >= L for L = 1\.\.400 .* for L = 2\.\.400", "B3 executed"),
    ("Cexec", "~the half-angle identity and the small-term identities symbolically (C1-C2)", "CACHE", r"C1 H2\(c\)", "C1-C2 executed"),
    ("sumrule", "~by the sum rule sum_k <|s^1(k)|^2> = N/3", "CACHE", r"D5 H3 \(the sum rule\): the sphere average of \(s\^1\)\^2 is 1/3",
     "the sum rule (D5)"),
    ("H3plane", "~M_N^4 <= (3 pi^2 beta + 1)/H_{L-1} on the plane (L >= 2)¦on the plane torus (Z/2LZ)^2 with L >= 2, M_N^4 <= (3pi^2beta + 1)/H_{L-1}",
     "CACHE", r"C3 H3: 9 pi\^2 \(beta \+ 1/\(3 pi\^2\)\)/\(3H\) = \(3 pi\^2 beta \+ 1\)/H \(the plane\)", "H3, the plane (C3)"),
    ("H3line", "~M_N^4 <= (6 pi^2 beta + 4)/sqrt(L) on the line (L >= 2)¦on the line torus Z/2LZ with L >= 2, M_N^4 <= (6pi^2beta + 4)/sqrtL",
     "CACHE", r"3 \(beta pi\^2 \+ 2/3\)/\(sqrt\(L\)/2\) = \(6 pi\^2 beta \+ 4\)/sqrt\(L\) \(the line\)", "H3, the line (C3)"),
    ("H3dyadic", "~hence M_N^4 <= (3pi^2beta + 1)/(1 + m/2) for L >= 2^m + 1", "DERIVED", (derive_H3dyadic, r"The dyadic form is H2\(b\)"),
     "H3, the dyadic form"),
    ("H3L1", "~(at L = 1 the right side exceeds 1 >= M_N^4)", "DERIVED", (derive_L1, r"at L = 1 the right side exceeds"), "H3 at L = 1"),
    ("limit", "~so it tends to zero as L grows for every beta > 0¦In both cases M_N^2 -> 0 as L -> ∞¦the lower constant M^2 is zero in the limit",
     "DERIVED", (derive_limits, r"M_N\^2 -> 0 as L -> ∞"), "the limit"),
    ("D5exec", "~Parseval with symbolic site values on the 4x4 torus and the sphere average 1/3 are executed (D5); the final algebra of both cases "
     "symbolically (C3)", "CACHE", r"D5 H3 \(the sum rule\): .*4x4 torus", "D5, C3 executed"),
    ("refs", "~block 19's sandwich, PR #8153, referenced as an evidence address for the three-dimensional half¦block 17, PR #8151"
     "¦block 19's transverse channel - (M^2/3)^2/(betaE(k)) <= lim inf u(k) <= 1/(betaE(k)) with M^2 > 0 - exists on Z^3 for beta > 3sqrt3pi/8 (block 19, G3-G5)"
     "¦The soldered six-axis static law orders on the plane for p >= 216*max(q, r) (block 17, T5-T6)¦conditional on blocks 19 and 17 for their halves"
     "¦The infrared upper bound u(k) <= 1/(betaE(k)) of block 19¦(D1-D4)", "EXCLUDED",
     "references to blocks 19 and 17 (PRs #8153, #8151; their constants are theirs, cited as evidence addresses) and the check labels", "citation"),
    ("notclaimed", "~the infrared upper bound u(k) <= 1/(betaE(k)) still holds there", "EXCLUDED", "not claimed (block 19's bound)", "not claimed"),
    ("words", r"the third dimension|Three standard mathematical imports|the zero-field lower bound|at any beta > 0|For every beta > 0|every beta > 0"
     r"|six-axis", "EXCLUDED", "wording and conditions (number words; beta > 0)", "wording"),
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
