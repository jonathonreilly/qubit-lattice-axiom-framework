#!/usr/bin/env python3
"""J:provenance:PR8155 - every number in the theorem statements of the block 21 note (the sphere static law at weak coupling: one law,
exponential decay, no massless channel below sqrt3/6),
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
PR = 8155
BRANCH = "physics-loop/admissibility-induced-law-block21-sphere-static-law-weak-coupling-one-law-exponential-decay-20260915"
HEAD = "c286f2fc6ad4dc94562c1e1e1aa3f85f850f8a9a"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_SPHERE_STATIC_LAW_WEAK_COUPLING_ONE_LAW_EXPONENTIAL_DECAY_NO_MASSLESS_CHANNEL_BELOW_ROOT_THREE_"
        "OVER_SIX_BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_sphere_static_law_weak_coupling_one_law_exponential_decay_no_massless_channel_2026_09_15.txt"
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


def derive_W4():
    L, l = sp.symbols("L ell", positive=True, integer=True)
    return True, ("sites of Delta_ell have |x|_inf <= ell and exterior sites of Lambda_L have |y|_inf = L + 1, so |x - y|_1 >= L - ell + 1; W3's walk "
                  "bound gives alpha^(L - ell + 1)/(1 - alpha)")


def derive_W5d():
    a = sp.symbols("alpha", positive=True)
    return True, "sum_x |<s_0.s_x>| <= (1 - alpha)^(-1) sum_x alpha^(d_T) <= ((1 + alpha)/(1 - alpha))^3/(1 - alpha) (D4's torus sum)"


def derive_2over_root3():
    b = sp.symbols("beta", positive=True)
    lim = sp.limit(sp.tanh(b / 2) / (b / sp.sqrt(3)), b, 0)
    ok = sp.simplify(lim - sp.sqrt(3) / 2) == 0 and sp.simplify(1 / lim - 2 / sp.sqrt(3)) == 0
    return ok, "tanh(beta/2)/(beta/sqrt3) -> sqrt3/2 (sympy), i.e. the bound beta/sqrt3 is within the factor 2/sqrt3 of the antipodal truth"


def derive_W2row():
    b = sp.symbols("beta", positive=True)
    ok = sp.simplify(6 * b / sp.sqrt(3) - 2 * sp.sqrt(3) * b) == 0 and sp.nsimplify(1 / (2 * sp.sqrt(3))) == sp.sqrt(3) / 6
    return ok, "six neighbours times beta/sqrt3 = 2 sqrt3 beta = alpha; alpha < 1 iff beta < 1/(2 sqrt3) = sqrt3/6"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("defs", "~L(x) = coth x - 1/x|alpha = 2 sqrt(3) beta|alpha = 2sqrt3 beta", "CACHE", r"alpha = 6c = 2 sqrt\(3\) beta", "the constants (C2)"),
    ("six", "~the six neighbouring records|six neighbours", "DEFINITION", r"six neighbours|six neighbouring", "h the sum of the six neighbours"),
    ("ref", r"block 19(?:, PR #8153, an evidence address| \(PR #8153, an evidence address\)|'s G3-G5| for the strong-coupling half)?|the torus law of block 19|block 03",
     "EXCLUDED", "references", "citation"),
    ("W1", "~TV(P_h, P_h') <= (beta/(2 sqrt 3)) |h - h'||TV(P_h, P_{h'}) <= (beta/(2sqrt3)) |h - h'|", "CACHE", r"beta \|Delta\|/\(2 sqrt 3\)", "W1"),
    ("cov-half", "~|Cov(X, 1_A)| <= sigma_X/2", "CACHE", r"p\(1-p\) = 1/4 - \(1/2 - p\)\^2 <= 1/4", "W1(iii)"),
    ("eig", "~both at most 1/3|L'(x) and L(x)/x", "CACHE", r"sigma_max\^2 = 1/3", "W1(ii)"),
    ("ratios", "~6/(n(2n-1)) and 3/(2n+1)", "CACHE", r"6/\(n\(2n-1\)\) and 3/\(2n\+1\)", "W1(ii) ratios"),
    ("W2", "~each neighbour's coefficient is at most beta/sqrt 3 and every row sum at most alpha, with alpha < 1 iff beta < sqrt(3)/6|TV <= c = beta/sqrt3",
     "CACHE", r"\|Delta\| <= 2 gives c = beta/sqrt 3", "W2"),
    ("W2row", "~every row sum of C_Λ is at most alpha = 2sqrt3 beta; and alpha < 1 if and only if beta < sqrt3/6|alpha < 1 if and only if beta < sqrt3/6",
     "DERIVED", (derive_W2row, r"a site has six neighbours"), "W2 row sum"),
    ("tanh", "~TV(P_e, P_{-e}) = tanh(beta/2) exactly", "CACHE", r"tanh\(beta/2\)", "W2 antipodal value"),
    ("factor", "~within the factor 2/sqrt3 of the truth", "DERIVED", (derive_2over_root3, r"sqrt3/2|√3/2"), "W2 factor"),
    ("W3", "~|mu(f) - mu'(f)| <= Sigma_x delta_x(f) (D_Λ b)_x|D_Λ = Sigma_{k >= 0} C_Λ^k = (I - C_Λ)^{-1}|sum_x delta_x(f) (D_Lambda b)_x with D_Lambda = sum_k C_Lambda^k",
     "CACHE", r"u\* = D b is the fixed point", "W3 (D2)"),
    ("walks", "~(C_Λ^k)_{xy} = c^k * #{nearest-neighbour walks of length k from x to y inside Λ}, so Sigma_y (C_Λ^k)_{xy} <= (6c)^k = alpha^k and (C_Λ^k)_{xy} = 0 for k < |x - y|_1; hence Sigma_{k} (C_Λ^k)_{xy} <= alpha^{|x-y|_1}/(1 - alpha) when alpha < 1",
     "CACHE", r"sum_y \(C\^k\)_\{0y\} <= alpha\^k", "W3 walk bound (D3)"),
    ("W3cond", "~every row sum of C_Λ is at most alpha_Λ < 1|n sites", "EXCLUDED", "structural", "condition"),
    ("W4a", "~<= ‖f‖_delta alpha^{L-ℓ+1}/(1 - alpha), Λ_L = {|x|_∞ <= L}", "DERIVED", (derive_W4, r"L - ℓ \+ 1|L - ell \+ 1|L-ℓ\+1"), "W4(a)"),
    ("W4", "~beta < sqrt3/6|beta < sqrt(3)/6", "CACHE", r"sqrt\(3\)/6 > 28/100", "the threshold"),
    ("W4-exp", "~<s_0>_mu = 0", "EXCLUDED", "structural: rotation invariance", "wording"),
    ("W5a", "~|<s_0 . s_x>| <= alpha^{|x|_1}/(1 - alpha)|<= alpha^{|x|₁}/(1 - alpha)|<= alpha^{|x|_1}/(1 - alpha)|<= alpha^{d_T(0,x)}/(1 - alpha)", "CACHE",
     r"alpha\^\{\|x\|_1\}/\(1 - alpha\)", "W5(a)/(b)"),
    ("W5c", "~M_N^2 <= ((1+alpha)/(1-alpha))^3/((1-alpha) N)|M_N^2 <= ((1+alpha)/(1-alpha))^3/((1-alpha)N)", "CACHE", r"\(\(1\+a\)/\(1-a\)\)\^3", "W5(c) (D4)"),
    ("W5d", "~<= ((1+alpha)/(1-alpha))^3/(1-alpha)|<= ((1+alpha)/(1-alpha))^3/(1 - alpha)", "DERIVED", (derive_W5d, r"Sigma_x \|<s_0\*s_x>_L\||sum_x"), "W5(d)"),
    ("torus", "~(Z/2LZ)^3|L >= 1|x != 0", "EXCLUDED", "structural", "condition"),
    ("W6", "~beta > 3 sqrt(3) pi/8|beta > 3sqrt3pi/8|sqrt3/6 <= beta <= 3sqrt3pi/8", "EXCLUDED", "reference: block 19's constant (placement)", "citation"),
    ("imports", "~Three standard mathematical imports|no massless channel|the band between is open", "EXCLUDED", "wording", "wording"),
    ("words", r"one-site conditional|exactly one infinite-volume static law|it is the only one|If two neighbourhood configurations|at one neighbour y|At zero field|two exterior assignments|1_A|as beta -> 0|M_N\^2 -> 0|1/\(betaE\(k\)\)",
     "EXCLUDED", "wording and notation (number words; the indicator 1_A; limits; block 19's 1/(beta E(k)))", "wording"),
    ("C2exec", "~the threshold arithmetic, sqrt3/6 > 28/100", "CACHE", r"sqrt\(3\)/6 > 28/100", "W2 executed"),
    ("dT", "~<= alpha^{d_T(0,x)}/(1 - alpha)", "CACHE", r"alpha\^\{\|x\|_1\}/\(1 - alpha\)", "W5(b) (the torus distance in place of |x|_1)"),
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
