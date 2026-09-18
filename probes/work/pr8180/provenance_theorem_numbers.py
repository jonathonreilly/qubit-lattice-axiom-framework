#!/usr/bin/env python3
"""J:provenance:PR8180 - every number in the theorem statements of the block 35 note, located in the runner's cached stdout or in an
exact derivation in the note.

Statement text = the front-matter claim_scope + each '## Theorem ...' section up to its '**Proof' marker (the whole section when there
is none).  Every numeric token of that text (integers, decimals, fractions a/b, and number words) must fall inside one listed item:
  CACHE       a runner line in logs/runner-cache/<runner>.txt (PR head) prints the number / formula      -> sourced
  DERIVED     an exact derivation stated in the note, re-executed here (sympy / fractions)                -> sourced
  DEFINITION  a constant of a declared object (the note's 'Premises and declared objects')                 -> not a claim
  EXCLUDED    a reference (block / PR number) or a structural constant of a condition or domain            -> not a claim
  (else)      HIT: no runner line and no derivation in the note; other files of the PR that carry it are named.
Tokens covered by no item are printed as UNCOVERED (the item list is incomplete); the run is only logged with zero UNCOVERED.
For numbers found only in a control output, the stated values are also compared with that output (MISMATCH notes).
Self-contained; reads the PR head through git (fetches the branch if the commit is missing).
"""
import re
import subprocess
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
PR = 8180
BRANCH = "physics-loop/admissibility-induced-law-block35-gravity-kernel-under-the-formation-reading-heat-kernel-times-plane-green-function-20260918"
HEAD = "7c844adf7555a3558729be69179646f6a83a1539"
NOTE = ("docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_TIMES_A_PLANE_GREEN_FUNCTION_"
        "NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md")
RUNNER = "scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_function_2026_09_18.py"
CACHE = ("logs/runner-cache/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_green_"
         "function_2026_09_18.txt")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
OTHER = [SPECS + "supervisor_control_block35_kernel_sim.out.txt", SPECS + "supervisor_control_block35_refuter.out.txt"]


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
REPL = (("θ̂", "theta^"), ("θ̄", "theta_bar"), ("ŝ", "s^"), ("−", "-"), ("–", "-"), ("—", " - "), ("×", "x"), ("≤", "<="), ("≥", ">="), ("π", "pi"), ("β", "beta"), ("σ", "sigma"),
        ("φ", "phi"), ("θ", "theta"), ("`", ""), ("∗", "*"), ("Σ", "sum"), ("ᵀ", "^T"), ("≳", ">~"), ("√", "sqrt"), ("∂", "d"),
        ("≠", "!="), ("ξ", "xi"), ("γ", "gamma"))


def norm(t):
    t = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺]+)", lambda m: "^" + m.group(1).translate(SUP), t)
    t = re.sub(r"([₀₁₂₃₄₅₆₇₈₉]+)", lambda m: "_" + m.group(1).translate(SUB), t)
    for a, b in REPL:
        t = t.replace(a, b)
    return re.sub(r"[ \t]+", " ", t)


def statement_sections(note):
    fm = note.split("\n---\n", 1)[0]
    m = re.search(r'^claim_scope:\s*"(.*)"\s*$', fm, flags=re.M)
    out = [("claim_scope", norm(m.group(1)))]
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        title = sec.split("\n", 1)[0].strip()
        if title.lower().startswith("theorem"):
            body = sec.split("\n", 1)[1] if "\n" in sec else ""
            out.append((title.split(" — ")[0], norm(re.split(r"\*\*Proof", body)[0])))
    return out


def section(note, prefix):
    for sec in re.split(r"^## ", note, flags=re.M)[1:]:
        if sec.startswith(prefix):
            return norm(sec)
    return ""


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+/\d+|\d+\.\d+|\d+)(?![\d])")
WORDS = re.compile(r"\b(zero|one|two|three|four|five|six|seven|eight|nine|ten|twelve|sixteen|sixty-four|third|thirds|half|quarter|"
                   r"double|twice|single|pair)\b", re.I)


def tokens(text):
    return [(m.start(), m.end(), m.group(1)) for m in NUM.finditer(text)] + [(m.start(), m.end(), m.group(1)) for m in WORDS.finditer(text)]


# ------------------------------------------------------------------------------------------------------------------ the items
# (id, statement regex, kind, source, role).  source: CACHE -> regex over cache stdout lines; DERIVED -> (callable, note regex locating
# the derivation); DEFINITION -> regex over the declared-objects section; EXCLUDED -> reason; HIT candidates are CACHE items not found.
def derive_stationary():
    t = sp.symbols("t", positive=True)
    uu = sp.Rational(1, 3)                       # any 0 < u < 1: the limit of (1 - u^t)/(1 - u) is 1/(1 - u); checked at u = 1/3 exactly
    ok = sp.limit((1 - uu ** t) / (1 - uu), t, sp.oo) == 1 / (1 - uu)
    return ok, "t -> oo of the cache's B1 formula sigma^2 phi^s (1 - u^t)/(1 - u) gives sigma^2 phi^s/(1 - u) (sympy limit at u = 1/3: " \
               f"{sp.limit((1 - uu ** t) / (1 - uu), t, sp.oo)} = 1/(1 - u))"


def derive_one_third():
    k1, k2, e = sp.symbols("k1 k2 e", real=True)
    ser = sp.series(((1 + sp.exp(sp.I * e * k1) + sp.exp(sp.I * e * k2)) / 3), e, 0, 2).removeO()
    ok = sp.simplify(ser - (1 + sp.I * e * (k1 + k2) / 3)) == 0
    return ok, "phi = 1 + i(k1 + k2)/3 + O(k^2) (cache D1) puts 1/3 of a step on each predecessor direction; sympy series re-derived"


ITEMS = [
    # claim_scope
    ("ref-block26", r"block 26 \(PR #8170\)", "EXCLUDED", "reference (block 26 = PR #8170)", "citation"),
    ("ref-block19", r"block 19", "EXCLUDED", "reference (block 19)", "citation"),
    ("sigma2-def", r"sigma\^2 = A\(3 beta\)/\(3 beta\)", "DEFINITION", r"A\(3beta\)/\(3beta\)", "noise variance of the linearized law (block 26)"),
    ("T1-cov", r"Cov\(theta\^_k\(t\), theta\^_k\(t\+s\)\) = sigma\^2 phi\(k\)\^s \(1 - u\^t\)/\(1 - u\)", "CACHE",
     r"sigma\^2 phi\^s \(1 - u\^t\)/\(1 - u\)", "T1 mode covariance"),
    ("phi-def", r"phi\(k\) = \(1 \+ e\^\{i k_1\} \+ e\^\{i k_2\}\)/3", "DEFINITION", r"phi\(k\) = \(1 \+ e\^\{ik_1\} \+ e\^\{ik_2\}\)/3",
     "multiplier of a mode"),
    ("u-lt-1", r"u = \|phi\|\^2 < 1 off the zero mode", "EXCLUDED", "structural: the condition u < 1 off the zero mode", "condition"),
    ("T1-kernel-op", r"C_s = sigma\^2 ?\(I - P ?P\*\)\^\{-1\} P\*\^s", "CACHE", r"C_s = sigma\^2 \(I - P P\*\)\^\{-1\} P\*\^s",
     "T1 stationary kernel as an operator"),
    ("T1-tori", r"tori L = 3, 4", "CACHE", r"tori L = 3, 4", "T1 exact recursions: torus sides"),
    ("T2-form", r"1 - u\(k\) = k(?:\^T M k|\^TMk) \+ O\(\|?k\|?\^4\),? (?:with )?M = \(1/9\)\[\[2, ?-1\], ?\[-1, ?2\]\]", "CACHE",
     r"1 - u\(k\) = k\^T M k \+ O\(k\^4\) with M = \(1/9\)\[\[2,-1\],\[-1,2\]\]", "T2 small-k form and M"),
    ("T2-eig", r"eigenvalues 1/9 along \(1, ?1\) and 1/3 along \(1, ?-1\)", "CACHE",
     r"eigenvalues 1/9 \(along \(1,1\)\) and 1/3 \(along \(1,-1\)\)", "T2 eigenvalues and eigenvectors"),
    ("T2-order6", r"order six", "CACHE", r"group of order 6", "T2 symmetry group order"),
    ("T2-three-dirs", r"three predecessor directions", "CACHE", r"\(the three predecessor directions\)", "T2 the permuted set"),
    ("T2-E", r"E\(k\) = sum(?:_i)? 2\(1 - cos k_i\) = \|k\|\^2 \+ O\(\|?k\|?\^4\)", "CACHE",
     r"E\(k\) = sum 2\(1 - cos k_i\) = \|k\|\^2 \+ O\(k\^4\)", "T2 comparator's small-k form"),
    ("T2-48", r"48 signed permutations", "CACHE", r"48 signed permutations", "T2 comparator's symmetry group order"),
    ("T3-bound", r"exp\(-2\|k\|\^2 s/\(9 pi\^2\)\)|e\^\{-\(1 - u\)s/2\} <= e\^\{-2\|k\|\^2s/\(9pi\^2\)\}", "CACHE",
     r"exp\(-\(1 - u\) s/2\) <= exp\(-2\|k\|\^2 s/\(9 pi\^2\)\)", "T3 diffusive decay bound, rate 2/(9 pi^2)"),
    ("T3-phis", r"\|phi\(k\)\|\^s = u\^\{s/2\} <=", "CACHE", r"\|phi\(k\)\|\^s <= exp", "T3 |phi|^s = u^{s/2}"),
    ("T3-scale", r"\|k\|\^\{-1\} ~ s\^\{1/2\}|\|k\|\^\{-1\} >~ sqrts", "CACHE", r"\|k\|\^\{-1\} ~ s\^\{1/2\}", "T3 diffusive in-plane scale"),
    ("T3-drift", r"phi(?:\(k\))? = 1 \+ i\(k_1 \+ k_2\)/3 \+ O\(\|?k\|?\^2\)", "CACHE", r"phi\(k\) = 1 \+ i\(k1 \+ k2\)/3 \+ O\(k\^2\)",
     "T3 drift"),
    ("inv-E", r"1/E\(k\)", "EXCLUDED", "structural: the comparator's kernel 1/E(k) (block 19's object, declared)", "object"),
    ("exec-plane", r"256 x 256", "CACHE", r"256 x 256", "executed-not-claimed: plane size", r"L=256"),
    ("exec-betas", r"beta = 6, 12, 24", "CACHE", r"beta = 6, 12, 24", "executed-not-claimed: couplings", r"^beta=(?:6|12|24)\.0"),
    ("exec-lin", r"linearized kernel sigma\^2/\(1 - u\(k\)\)", "CACHE", r"sigma\^2/\(1 ?- ?u", "executed-not-claimed: the linear kernel",
     r"sigma\^2/\(1-u\(k\)\)"),
    ("exec-norm6", r"0\.83-0\.89", "CACHE", r"0\.83-0\.89", "executed-not-claimed: normalization range at beta = 6", ("6", r"mean ratio")),
    ("exec-norm12", r"0\.90-0\.94", "CACHE", r"0\.90-0\.94", "executed-not-claimed: normalization range at beta = 12", ("12", r"mean ratio")),
    ("exec-norm24", r"0\.94-0\.97", "CACHE", r"0\.94-0\.97", "executed-not-claimed: normalization range at beta = 24", ("24", r"mean ratio")),
    ("exec-s64", r"s = 64", "CACHE", r"s = 64", "executed-not-claimed: cross-level depth", r"s=64:"),
    ("exec-few", r"within a few percent", "CACHE", r"few percent", "executed-not-claimed: agreement of C_s/C_0 with phi^s", r"s=64:"),
    # Theorem T1 statement
    ("T1-cond", r"From theta_0 = 0, for every mode k and every t >= 1, s >= 0", "EXCLUDED", "structural: initial condition and index ranges",
     "condition"),
    ("T1-var", r"Var theta\^_k\(t\) = sigma\^2 ?\(1 - u\^t\)/\(1 - u\) for u = u\(k\) < 1", "CACHE", r"sigma\^2 phi\^s \(1 - u\^t\)/\(1 - u\)",
     "T1 variance (s = 0 of B1's formula)"),
    ("T1-stationary", r"C_s\(k\) = sigma\^2 phi\(k\)\^s/\(1 - \|phi\(k\)\|\^2\)", "DERIVED", (derive_stationary, r"sums geometrically"),
     "T1 stationary mode kernel"),
    # Theorem T2: covered by T2-* items above (the same statements in the section's words)
    # Theorem T3
    ("T3-square", r"\|k_i\| <= pi", "EXCLUDED", "structural: the domain of k", "domain"),
    ("T3-log", r"log\(1 - y\) <= -y", "CACHE", r"log\(1 - y\) <= -y", "T3 elementary inequality"),
    ("T3-import", r"block 34's 1 - u >= 4\|k\|\^2/\(9pi\^2\)", "CACHE", r"4\|k\|\^2/\(9 ?pi\^2\)", "T3 input: 1 - u >= 4|k|^2/(9 pi^2)"),
    ("T3-onethird", r"one third of a step", "DERIVED", (derive_one_third, r"drifts by one third of a step"), "T3 drift per level"),
    ("T3-mixed", r"d\^2log E/dk_1dk_3 != 0", "CACHE", r"non-vanishing mixed derivative in \(k1, k3\)", "T3/D2 non-product criterion"),
    ("dims", r"(?:two|three)-dimensional", "EXCLUDED", "structural: dimension of the named objects", "wording"),
    ("gain-one", r"gain one", "DEFINITION", r"P the average over the three predecessors",
     "gain one: P is an average (weights sum to one), block 26/34's linearization"),
    ("zero-mode", r"zero mode", "EXCLUDED", "structural: the name of the k = 0 mode", "wording"),
]


def main():
    note = show(NOTE)
    cache_raw = show(CACHE)
    cache = cache_raw.split("----- stdout -----\n", 1)[1].split("\n----- stderr -----", 1)[0]
    cache_lines = cache.splitlines()
    declared = section(note, "Premises and declared objects")
    other = {p: show(p) for p in OTHER}
    secs = statement_sections(note)
    covered = {name: set() for name, _ in secs}
    counts = {"CACHE": 0, "DERIVED": 0, "DEFINITION": 0, "EXCLUDED": 0, "HIT": 0}
    hits = []
    print(f"PR #{PR} head {HEAD[:10]}; note {NOTE[:60]}...; cache {len(cache_lines)} stdout lines")
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
            ok = re.search(src, re.sub(r" ", " ", declared)) is not None
            counts["DEFINITION" if ok else "HIT"] += 1
            if ok:
                print(f"[DEFINITION] {iid} | {loc} | {role} | declared under 'Premises and declared objects'")
            else:
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | definition not found in the declared objects"))
        elif kind == "DERIVED":
            fn, locate = src
            ok, txt = fn()
            found = re.search(locate, norm(note)) is not None
            if ok and found:
                counts["DERIVED"] += 1
                print(f"[DERIVED] {iid} | {loc} | {role} | note: '{locate}' | {txt}")
            else:
                counts["HIT"] += 1
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | derivation {'failed' if not ok else 'not located in the note'}"))
        else:
            lines = [(i + 1, l) for i, l in enumerate(cache_lines) if re.search(src, l)]
            if lines:
                counts["CACHE"] += 1
                i, l = lines[0]
                print(f"[CACHE] {iid} | {loc} | {role} | cache stdout line {i}: {l.strip()[:150]}")
            else:
                counts["HIT"] += 1
                elsewhere = []
                for p, txt in other.items():
                    lines_p = txt.splitlines()
                    if isinstance(other_pat, tuple):          # (beta, regex): search only inside that beta's block of the control output
                        b0 = [j for j, l in enumerate(lines_p) if l.startswith(f"beta={other_pat[0]}.0")]
                        if not b0:
                            continue
                        b1 = [j for j, l in enumerate(lines_p) if l.startswith("beta=") and j > b0[0]] + [len(lines_p)]
                        js = [j + 1 for j in range(b0[0], b1[0]) if re.search(other_pat[1], lines_p[j])]
                    else:
                        js = [j + 1 for j, l in enumerate(lines_p) if re.search(other_pat, norm(l))]
                    if js:
                        elsewhere.append(f"{p.split('/')[-1]} lines {','.join(map(str, js[:6]))}{'...' if len(js) > 6 else ''}")
                in_runner_src = re.search(src, norm(show(RUNNER))) is not None
                hits.append((iid, f"HIT: {iid} | {loc} | {role} | not printed by the runner (cache), no derivation in this note"
                            + (f"; present in the runner source only (not printed)" if in_runner_src else "")
                            + (f"; appears in {', '.join(elsewhere)}" if elsewhere else "; appears in no other file of the PR")))
    # coverage
    unc = []
    ntok = 0
    for name, text in secs:
        for a, b, v in tokens(text):
            ntok += 1
            if not any(p in covered[name] for p in range(a, b)):
                unc.append((name, v, text[max(0, a - 40):b + 30].replace("\n", " ")))
    for name, v, ctx in unc:
        print(f"[UNCOVERED] {name} | {v} | ...{ctx}...")
    # comparison of the executed ranges with the control output (the only file that prints them)
    sim = other[OTHER[0]]
    notes = []
    extra = {}
    blocks = re.split(r"(?m)^beta=", sim)[1:]
    stated = {"6": (0.83, 0.89), "12": (0.90, 0.94), "24": (0.94, 0.97)}
    for blk in blocks:
        beta = blk.split(".", 1)[0]
        vals = [float(x) for x in re.findall(r"mean ratio ([0-9.]+)", blk)]
        lo, hi = min(vals), max(vals)
        mono = all(vals[i] <= vals[i + 1] for i in range(len(vals) - 1))
        slo, shi = stated[beta]
        agree = round(lo, 2) == slo and round(hi, 2) == shi
        notes.append(f"beta={beta}: control shell ratios {lo:.4f}..{hi:.4f} over {len(vals)} shells (rounded {lo:.2f}-{hi:.2f}; "
                     f"stated {slo:.2f}-{shi:.2f}: {'agrees' if agree else 'MISMATCH'}); increasing in |k| across shells: {mono}")
        imax = vals.index(hi)
        shells = re.findall(r"\|k\| in (\[[0-9.]+,[0-9.]+\))", blk)
        extra[f"exec-norm{beta}"] = (f"; control: {lo:.4f}..{hi:.4f} (max in shell {shells[imax]}), stated {slo:.2f}-{shi:.2f} "
                                     f"{'agrees' if agree else 'MISMATCH'}; increasing in |k| (claim_scope 'rising with |k|'): {mono}")
        mods = re.findall(r"s=64: ([0-9.]+)/([0-9.]+)", blk)
        worst = max(abs(float(a) / float(b) - 1) for a, b in mods)
        notes.append(f"beta={beta}: s=64 modulus of C_s/C_0 vs |phi|^s at the printed modes: max relative difference {worst:.3f}")
        extra["exec-few"] = extra.get("exec-few", "; control s=64 modulus vs |phi|^s, max relative difference:") + f" {worst:.3f} (beta={beta})"
    for n in notes:
        print(f"[CONTROL] {n}")
    # INFO on the one unsourced input of the proved statements: the imported inequality itself (not a provenance source)
    import numpy as np
    g = np.linspace(-np.pi, np.pi, 2001)
    K1, K2 = np.meshgrid(g, g, indexing="ij")
    uu = (3 + 2 * np.cos(K1) + 2 * np.cos(K2) + 2 * np.cos(K1 - K2)) / 9
    kk = K1 ** 2 + K2 ** 2
    ratio = np.where(kk > 0, (1 - uu) / np.where(kk > 0, kk, 1), np.inf)
    i = np.unravel_index(np.argmin(ratio), ratio.shape)
    corner = sp.nsimplify((1 - sp.Rational(1, 9)) / (2 * sp.pi ** 2))
    print(f"[INFO] T3-import checked here (not a source): min over a 2001^2 grid of the square of (1 - u)/|k|^2 = {ratio[i]:.12f} at k = "
          f"({K1[i]:.4f}, {K2[i]:.4f}); 4/(9 pi^2) = {4 / (9 * np.pi ** 2):.12f}; exact value at k = (pi, pi): (1 - 1/9)/(2 pi^2) = {corner} "
          f"(equality: {sp.simplify(corner - sp.Rational(4, 9) / sp.pi ** 2) == 0})")
    for iid, h in hits:
        print(h + extra.get(iid, ""))
    print(f"[COVERAGE] {ntok} numeric tokens in the statement text; uncovered {len(unc)}")
    claimed = [i for i, _ in hits if not i.startswith("exec-")]
    execd = [i for i, _ in hits if i.startswith("exec-")]
    print(f"SUMMARY: {len(ITEMS)} items over claim_scope + {len(secs) - 1} theorem sections ({ntok} numeric tokens, {len(unc)} uncovered): "
          f"cache-sourced {counts['CACHE']}, derived in the note {counts['DERIVED']}, definitions {counts['DEFINITION']}, excluded {counts['EXCLUDED']}; "
          f"unsourced {counts['HIT']} = {len(claimed)} in the proved statements ({', '.join(claimed) or 'none'}) + {len(execd)} executed-not-claimed "
          f"numbers printed only by the control (beta=12 range {'MISMATCH' if 'MISMATCH' in extra.get('exec-norm12', '') else 'ok'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
