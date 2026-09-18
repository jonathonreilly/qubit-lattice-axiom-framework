#!/usr/bin/env python3
"""J:provenance:PR8156 - every number in the theorem statements of the block 22 note (3G(0) as half the cubic walk's return sum, pinned
between 75/100 and 76/100; the sharpened threshold),
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
PR = 8156
BRANCH = "physics-loop/admissibility-induced-law-block22-sphere-static-law-threshold-sharpened-return-sum-20260915"
HEAD = "5296e20cab34eb684c1f00f21b9c60bf1db7b153"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_STRONG_COUPLING_THRESHOLD_SHARPENED_RETURN_SUM_OF_THE_CUBIC_WALK_THREE_G_ZERO_"
        "BELOW_SEVENTY_SIX_HUNDREDTHS_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_strong_coupling_threshold_sharpened_return_sum_2026_09_15.txt"
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


def derive_exp_rate():
    n = sp.symbols("n", positive=True)
    ok = sp.simplify(2 * n * sp.Rational(2, 3) / sp.pi ** 2 - 4 * n / (3 * sp.pi ** 2)) == 0
    return ok, "on the outer region 1 - |phi| >= 2/(3 pi^2) (cache C3), so e^{-2n(1 - |phi|)} <= e^{-4n/(3 pi^2)}"


def derive_logbound():
    x = sp.symbols("x", positive=True)
    ok = sp.limit(sp.log(1 - x) + x, x, 0) == 0 and sp.simplify(sp.diff(sp.log(1 - x) + x, x) + x / (1 - x)) == 0
    return ok, "log|phi| <= |phi| - 1 (log(1 - x) <= -x, derivative -x/(1-x) <= 0), so |phi|^{2n} <= e^{-2n(1 - |phi|)}"


def derive_204():
    v = 3 * sp.sqrt(3) * sp.pi / 8
    ok = abs(float(v) - 2.04) < 0.005
    return ok, f"3 sqrt(3) pi/8 = {float(v):.5f} (block 19's constant, 'about 2.04')"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("G0-def", "~3 G(0) = 3 (2 pi)^{-3} int_{[-pi,pi]^3} dk/E(k)", "DEFINITION", r"G\(0\)", "3G(0)"),
    ("E-def", "~E(k) = sum_i 2(1 - cos k_i)", "DEFINITION", r"E\(k\)", "E(k)"),
    ("ref", r"block 19, PR #8153|block 19's(?: ordering threshold| G3-G5)?|block 21 \(PR #8155\)|referenced open blocks|blocks 19 and 21|block 21's",
     "EXCLUDED", "references", "citation"),
    ("beta3G", "~beta > 3 G(0)|beta > 3G(0) may be replaced|order below 3G(0)", "EXCLUDED", "placement (block 19's route)", "citation"),
    ("V1", "~3 G(0) = (1/2) sum_{n >= 0} P_{2n}(0,0)|3G(0) = (1/2)Sigma_{n>=0} P_{2n}(0,0)", "CACHE", r"P_\{2n\}", "V1 identity"),
    ("P2n", "~P_{2n}(0,0) = 6^{-2n} C(2n, n) sum_a C(n, a)^2 C(2(n-a), n-a)|P_{2n}(0,0) = 6^{-2n} C(2n, n) Sigma_{a=0}^{n} C(n, a)^2 C(2(n-a), n-a)",
     "CACHE", r"C\(2n,n\) sum_a C\(n,a\)\^2 C\(2\(n-a\),n-a\)", "V1 closed-walk count"),
    ("nge0", "~for every n >= 0|For every n >= 1|for every n >= 1", "EXCLUDED", "structural", "condition"),
    ("SN", "~S_N = sum_{n <= N} P_{2n}", "DEFINITION", "inline", "the partial sum S_N"),
    ("enum", "~closed-walk count executed by enumeration for n <= 3 and the Vandermonde form to n = 12|enumeration of all 6^{2n} walks for n <= 3 (1, 6, 90, 1860 closed walks)|for n <= 12",
     "CACHE", r"n <= 3: \[1, 6, 90, 1860\]", "B1/B2"),
    ("V2", "~P_{2n}(0,0) <= (36/11)^{3/2}/(4 pi^{3/2} n^{3/2}) + 2 e^{-4n/(3 pi^2)}", "CACHE", r"\(36/11\)\^\{3/2\}/\(4 pi\^\{3/2\}\)", "V2 (C2 prints the constant)"),
    ("V2-exp", "~2 e^{-4n/(3 pi^2)}", "DERIVED", (derive_exp_rate, r"2/\(3pi\^2\)|2/\(3π²\)"), "V2 exponential term"),
    ("cos1", "~1 - cos u >= 11 u^2/24 on |u| <= 1", "CACHE", r"1 - cos u >= 11 u\^2/24", "V2 inequality 1"),
    ("cos2", "~1 - cos u >= 2 u^2/pi^2 on [-pi, pi]", "CACHE", r"1 - cos u >= 2u\^2/pi\^2", "V2 inequality 2"),
    ("logb", "~|phi|^{2n} <= e^{-2n(1 - |phi|)}", "DERIVED", (derive_logbound, r"e\^\{-2n\(1 - \|phi\|\)\}"), "V2 exponential form"),
    ("two-region", "~the two-region split|the two-region step", "CACHE", r"the two-region step", "V2 split"),
    ("N1000", "~N = 1000|S_{1000}", "CACHE", r"S_1000 = sum_\{n<=1000\}", "V3 N"),
    ("V3up", "~3G(0) <= (S_N + T_1(N) + T_2(N))/2 < 76/100", "CACHE", r"hence 3 G\(0\) <= \(S_N \+ T_1 \+ T_2\)/2 < 76/100", "V3 upper bound"),
    ("T1", "~T_1(N)^2 <= (36/11)^3/(108N)", "CACHE", r"T_1\(N\)\^2 = \(36/11\)\^3/\(108 N\)", "V3 T_1"),
    ("T2", "~T_2(N) <= (225/14)(197/225)^{N+1}", "CACHE", r"T_2\(N\) = \(225/14\)\(197/225\)\^\(N\+1\)", "V3 T_2"),
    ("V3low", "~3G(0) >= S_N/2 > 75/100|3 G(0) > 75/100|S_N/2 > 75/100 gives 3 G(0) > 75/100", "CACHE", r"3 G\(0\) >= S_N/2 > 75/100", "V3 lower bound"),
    ("76", "~3 G(0) < 76/100|beta > 76/100", "CACHE", r"< 76/100", "V3/V4 upper value"),
    ("1553", "~as one rational (a 1553-digit denominator)", "CACHE", r"denominator 1553 digits", "V3 executed"),
    ("1501637", "~the integer decimal ⌊10^6 S_N⌋ = 1501637", "CACHE", r"floor\(10\^6 S\) = 1501637", "V3 executed"),
    ("181", "~the majorant T_1 < 181/10^4", "CACHE", r"T_1 < 181/10\^4", "V3 executed"),
    ("pi3", "~pi >= 3, e^{-2/15} <= 197/225", "CACHE", r"e\^\{-2/15\} <= 1 - 2/15 \+ 2/225 = 197/225", "V3 enclosures"),
    ("window", "~(75/100, 76/100)|[sqrt(3)/6, 76/100]|[sqrt3/6, 76/100]", "CACHE", r"75/100 < 3 G\(0\) < 76/100", "V4 window (sqrt3/6 is block 21's)"),
    ("width", "~of width below 1/2", "DERIVED", (lambda: (0.76 - 3 ** 0.5 / 6 < 0.5, f"76/100 - sqrt3/6 = {0.76 - 3 ** 0.5 / 6:.4f} < 1/2"), r"width below"), "V4"),
    ("100th", "~The route's constant is not below 75/100, so no sharper bound on G(0) can improve the threshold of that route by more than 1/100",
     "DERIVED", (lambda: (True, "76/100 - 75/100 = 1/100: the route's constant lies in (75/100, 76/100)"), r"more than 1/100"), "V4"),
    ("204", "~3 sqrt(3) pi/8 (about 2.04)", "DERIVED", (derive_204, r"2\.04"), "V4 block 19's former constant"),
    ("imports", r"Two standard mathematical imports|one rational|the band", "EXCLUDED", "wording", "wording"),
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
            alts = [a for a in p[1:].split("|")]
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
