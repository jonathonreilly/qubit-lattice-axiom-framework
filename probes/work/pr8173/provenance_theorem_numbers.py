#!/usr/bin/env python3
"""J:provenance:PR8173 - every number in the theorem statements of the block 29 note (the transverse kernel's normalization in the ordered
sphere static law),
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
PR = 8173
BRANCH = "physics-loop/admissibility-induced-law-block29-transverse-kernel-normalization-measured-sum-rule-spin-wave-20260916"
HEAD = "e5b3aa31686d88d8a2fe0aad5e938acac0e39404"
NOTE = ("docs/ADMISSIBILITY_RULE_TRANSVERSE_KERNEL_NORMALIZATION_IN_THE_ORDERED_SPHERE_STATIC_LAW_MEASURED_BETWEEN_THE_BOUNDS_WITH_THE_"
        "TRANSVERSE_SUM_RULE_AND_THE_SPIN_WAVE_REFERENCE_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_transverse_kernel_normalization_ordered_sphere_static_law_measured_between_bounds_sum_rule_spin_wave_reference_2026_09_16.py"
CACHE = ("logs/runner-cache/admissibility_rule_transverse_kernel_normalization_ordered_sphere_static_law_measured_between_bounds_sum_rule_"
         "spin_wave_reference_2026_09_16.txt")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
KER, REF, EXA = (SPECS + "supervisor_control_block29_kernel.out.txt", SPECS + "supervisor_control_block29_refuter.out.txt",
                 SPECS + "supervisor_control_block29_exact.out.txt")
OTHER = [KER, REF, EXA]


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
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"))


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
            body = re.sub(r"\*{1,2}Proof\.?\*{1,2}.*?(?:∎|$)", " ", body, flags=re.S)
            body = re.split(r"\*Reading\.\*", body)[0]          # interpretation paragraphs are not statements
            out.append((title.split(" — ")[0], norm(body)))
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
def derive_real_space():
    """T1's <theta_0 . theta_r> = 2 G_L(r)/beta, exact on the 4^3 torus: the zero-sum Gaussian with precision beta*Lap has covariance
    (beta*Lap + J)^{-1} - J/beta... computed as the pseudo-inverse on the zero-sum subspace: C = ((Lap + J)^{-1} - J)/beta with J = 11^T/N,
    two components; G_L(r) = N^{-1} sum_{k != 0} cos(k.r)/E(k) with the rational cosines of L = 4."""
    import sympy as sp
    L, N = 4, 64
    idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
    Lap = sp.zeros(N, N)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = idx(x, y, z)
                for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
                    Lap[i, i] += 1
                    Lap[i, idx(x + d[0], y + d[1], z + d[2])] -= 1
    J = sp.ones(N, N) / N
    Cinv = (Lap + J).inv() - J                      # the Green operator on the zero-sum subspace (beta = 1, one component)
    cosL = {0: 1, 1: 0, 2: -1, 3: 0}
    ok = True
    vals = []
    for r in range(3):
        G = sp.Rational(0)
        for a in range(L):
            for b in range(L):
                for c in range(L):
                    if (a, b, c) == (0, 0, 0):
                        continue
                    E = 2 * (3 - cosL[a] - cosL[b] - cosL[c])
                    G += sp.Rational(cosL[(a * r) % L], E)
        G /= N
        two_comp = 2 * Cinv[idx(0, 0, 0), idx(r, 0, 0)]
        ok = ok and sp.simplify(two_comp - 2 * G) == 0
        vals.append(f"r={r}: 2G_L = {2 * G}")
    return ok, "exact on the 4^3 torus (beta = 1): <theta_0.theta_r> from the pseudo-inverse of the Laplacian equals 2 G_L(r) for r = 0, 1, 2 (" + "; ".join(vals) + ")"


def derive_response():
    import sympy as sp
    b, h, N, m1, m3 = sp.symbols("beta h N m1sq m3", positive=True)
    sol = sp.solve(sp.Eq(b * h * N * m1, m3), N * m1)
    ok = len(sol) == 1 and sp.simplify(sol[0] - m3 / (b * h)) == 0
    return ok, "N<(m^1)^2> = <m^3>/(beta h) by dividing the printed sum rule (cache C2) by beta h > 0 (sympy)"


def derive_local_moment():
    import sympy as sp
    s1, s2, s3 = sp.symbols("s1 s2 s3", real=True)
    # for a unit vector s and a unit vector u (take u = e3 without loss by rotation): |s_perp|^2 = |s|^2 - (s.u)^2 = 1 - (s.u)^2
    perp2 = s1 ** 2 + s2 ** 2
    ok = sp.simplify(perp2.subs(s3, sp.sqrt(1 - s1 ** 2 - s2 ** 2)) - (1 - (sp.sqrt(1 - s1 ** 2 - s2 ** 2)) ** 2)) == 0
    return ok, "|s^perp|^2 = 1 - (s.u)^2 for unit s, two transverse components -> the '/2' per component (sympy)"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("ref-b19", r"block 19's bounds", "EXCLUDED", "reference (block 19's bounds)", "citation"),
    ("T1-model", r"H = \(beta/2\) sum_bonds \|theta_x - theta_y\|\^2", "DEFINITION", r"e\^\{-\(beta/2\)Sigma_\{<xy>\}\|theta_x - theta_y\|\^2\}",
     "the quadratic transverse model"),
    ("T1-var", r"(?:k-mode variance exactly )?1/\(beta ?E\(k\)\)(?: per component)?(?: for k != 0)?", "CACHE", r"variance 1/\(beta E\(k\)\)",
     "T1 mode variance"),
    ("T1-E", r"E\(k\) = 2 sum_j \(1 - cos k_j\)", "CACHE", r"E\(k\) = 2 sum_j \(1 - cos k_j\)", "T1 plane-wave eigenvalue"),
    ("T1-norm", r"beta ?E\(k\) ?<\|theta_hat\(k\)\|\^2> = 1|betaE\(k\)<\|theta\^\(k\)\|\^2> = 1(?: for every k != 0)?", "CACHE",
     r"beta E\(k\) <\|theta_hat\(k\)\|\^2> = 1", "T1 spin-wave value"),
    ("T1-ring", r"the plane-wave eigenvalues and the ring modes symbolic", "CACHE", r"on the 4-ring the k-modes n = 1, 2", "T1 route"),
    ("T1-real", r"<theta_0\*theta_r> = 2G_L\(r\)/beta", "DERIVED", (derive_real_space, r"real-space correlation is the inverse transform"),
     "T1 real-space correlation"),
    ("T1-k0", r"k != 0", "EXCLUDED", "structural: the nonzero modes", "condition"),
    ("T2-field", r"field h > 0 along e_3", "EXCLUDED", "structural: the field's sign and axis", "condition"),
    ("T2-rule", r"beta ?h(?: \*)? N ?<\(m(?:_hat|\^)\^1\)\^2> = <m(?:_hat|\^)\^3>", "CACHE", r"beta h N <\(m\^1\)\^2> = <m\^3> on any torus",
     "T2 sum rule"),
    ("T2-onesite", r"the one-site instance", "CACHE", r"single site in a field: kappa E\[\(s\^1\)\^2\] = E\[s\^3\]", "T2 one-site instance"),
    ("T2-response", r"transverse response at k = 0(?:, N<\(m\^\^1\)\^2>,)? (?:is|equals) <m(?:_hat|\^)\^3>/\(beta ?h\)", "DERIVED",
     (derive_response, r"transverse response at k = 0"), "T2 k = 0 response"),
    ("T2-limit", r"as h ↓ 0 whenever <m\^\^3> stays bounded away from zero", "EXCLUDED", "structural: the h -> 0 limit statement", "wording"),
    ("T3-modesum", r"N\^\{-1\} ?(?:sum|Sigma)_k ?<\|s(?:_hat|\^)\^perp\(k\)\|\^2> = <\|s_x\^perp\|\^2>|N\^\{-1\}Sigma_k <\|s\^\^⊥\(k\)\|\^2> = <\|s_x\^⊥\|\^2>",
     "CACHE", r"N\^\{-1\} sum_k \|f_hat\(k\)\|\^2 = sum_x f_x\^2", "T3 mode sum (Parseval)"),
    ("T3-local", r"N\^\{-1\}Sigma_k S_⊥\(k\) = <1 - \(s_x\*û\)\^2>/2", "DERIVED", (derive_local_moment, r"1 - \(s_x\*û\)\^2"),
     "T3 local transverse moment"),
    # executed and not claimed
    ("exec-c-def", r"c\(beta, k\) = beta E\(k\) S_perp\(k\)", "DEFINITION", r"c\(beta, k\) = betaE\(k\) S_⊥\(k\)", "normalization (declared)"),
    ("exec-grid", r"16\^3, 24\^3, 32\^3 at beta = 0\.8, 1, 1\.5, 2, 3", "CACHE", r"16\^3, 24\^3, 32\^3 \(control\)",
     "executed: lattices (the runner prints a descriptive N5 line)", r"sphere static law, L="),
    ("exec-betas", r"at beta = 0\.8, 1, 1\.5, 2, 3", "CACHE", r"beta = 0\.8, 1, 1\.5, 2, 3 \(control and refuter outputs\)",
     "executed: couplings (the runner prints a descriptive N5 line)", r"beta=\d"),
    ("exec-range", r"lies at 0\.86-0\.98 for the modes n >= 2", "CACHE", r"0\.86", "executed-not-claimed: normalization range, n >= 2",
     r"beta E\(k\) S_perp\(k\)"),
    ("exec-n1", r"the longest mode n = 1 scattering more", "CACHE", r"longest mode", "executed-not-claimed: n = 1 scatter", r"beta E\(k\) S_perp\(k\)"),
    ("exec-spinwave", r"rising toward the spin-wave value 1 as beta grows", "CACHE", r"spin-wave value 1 as beta grows",
     "executed-not-claimed: trend in beta", r"beta E\(k\) S_perp\(k\)"),
    ("exec-lb", r"\(m\^2/3\)\^2 \(0\.008-0\.08\) and 1", "CACHE", r"0\.008", "executed-not-claimed: range of the lower bound (m^2/3)^2",
     r"\(m\^2/3\)\^2 = "),
    ("exec-tenth", r"the infrared bound is the kernel up to about a tenth", "CACHE", r"up to about a tenth", "executed-not-claimed: gap to 1",
     r"beta E\(k\) S_perp\(k\)"),
]


def control_checks():
    ker = show(KER)
    extra, notes = {}, []
    grid, c_n1, c_rest, lbs = [], [], [], []
    for blk in re.split(r"(?m)^===== kernel_L", ker)[1:]:
        L = int(blk.split(" ", 1)[0])
        for sub in re.split(r"(?m)^  beta=", blk)[1:]:
            beta = float(sub.split(":", 1)[0])
            lb = float(re.search(r"\(m\^2/3\)\^2 = ([0-9.]+)", sub).group(1))
            cs = [float(x) for x in re.search(r"S_perp\(k\): ([0-9. ]+)", sub).group(1).split()]
            grid.append((L, beta))
            c_n1.append(cs[0])
            c_rest.extend((v, L, beta, n + 2) for n, v in enumerate(cs[1:]))
            lbs.append(lb)
    lo, hi = min(c_rest), max(c_rest)
    agree = round(lo[0], 2) == 0.86 and round(hi[0], 2) <= 0.98
    extra["exec-range"] = (f"; control (n >= 2, {len(c_rest)} values over {len(grid)} (L, beta) runs): {lo[0]:.3f} (L={lo[1]}, beta={lo[2]}, n={lo[3]}) .. "
                           f"{hi[0]:.3f} (L={hi[1]}, beta={hi[2]}, n={hi[3]}): stated 0.86-0.98 {'agrees' if agree else 'MISMATCH'}; the note's own "
                           f"'What the runs say (i)' gives 0.86-1.01")
    extra["exec-n1"] = f"; control n = 1: {min(c_n1):.3f} .. {max(c_n1):.3f}"
    extra["exec-lb"] = f"; control (m^2/3)^2: {min(lbs):.4f} .. {max(lbs):.4f}"
    full = {(L, b) for L in (16, 24, 32) for b in (0.8, 1.0, 1.5, 2.0, 3.0)}
    missing = sorted(full - set(grid))
    extra["exec-grid"] = f"; control grid: {len(grid)} of the 15 (L, beta) pairs, missing {missing}"
    extra["exec-betas"] = extra["exec-grid"]
    notes.append("normalization range n >= 2: " + extra["exec-range"][2:])
    notes.append("grid actually run: " + extra["exec-grid"][2:])
    return extra, notes


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
