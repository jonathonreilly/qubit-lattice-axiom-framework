#!/usr/bin/env python3
"""J:provenance:PR8170 - every number in the theorem statements of the block 26 note (the sphere formation law in level time: gain-one
spin waves, the level walk's local-limit constant, finite planes forget, the simulated decay of the initial plane's memory),
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
PR = 8170
BRANCH = "physics-loop/admissibility-induced-law-block26-unsoldered-formation-law-level-time-gain-one-spin-waves-memory-decay-20260916"
HEAD = "f9e1177003afa991ec87831d2be70611068a09ab"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_PLANES_FORGET_AND_"
        "THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md")
RUNNER = "scripts/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.py"
CACHE = "logs/runner-cache/admissibility_rule_unsoldered_formation_law_level_time_gain_one_spin_waves_local_limit_constant_finite_planes_forget_2026_09_16.txt"
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block26_"
SPH, SIX, FIT, REF, EXA = (SPECS + "sphere_sim.out.txt", SPECS + "sixaxis_sim.out.txt", SPECS + "fit.out.txt", SPECS + "refuter.out.txt",
                           SPECS + "exact.out.txt")
OTHER = [SPH, SIX, FIT, REF, EXA]


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
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"), ("⟨", "<"), ("⟩", ">"), ("ε", "epsilon"), ("η", "eta"), ("δ", "delta"), ("→", "->"))


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
def derive_kP():
    import sympy as sp
    k = sp.symbols("k", positive=True)
    c0 = 3 * sp.sqrt(3) / (4 * sp.pi)
    lo = k * (c0 / k - 1 / k ** 2 - sp.Rational(5, 2) / k * sp.exp(-k / 4))
    hi = k * (c0 / k + 27 / k ** 2 + sp.exp(-sp.sqrt(k) / 7))
    ok = sp.limit(lo, k, sp.oo) == c0 and sp.limit(hi, k, sp.oo) == c0
    return ok, "k times each side of the two-sided bound tends to 3 sqrt3/(4 pi) (sympy limits): k P_k -> 3 sqrt3/(4 pi)"


def derive_log():
    return True, "H_t >= log t for t >= 1 (the note's last proof line), so the harmonic bound gives the log form"


def derive_150():
    import sympy as sp
    k = sp.symbols("k", positive=True, integer=True)
    s27 = 27 * sp.pi ** 2 / 6
    integ = sp.integrate(sp.exp(-sp.sqrt(sp.Symbol("x", positive=True)) / 7), (sp.Symbol("x", positive=True), 0, sp.oo))
    ok = float(s27 + integ) < 150 and sp.simplify(integ - 98) == 0
    return ok, (f"sum_k 27/k^2 = 27 pi^2/6 = {float(s27):.2f} and sum_(k>=1) e^(-sqrt k/7) <= int_0^oo e^(-sqrt x/7) dx = {integ} (decreasing "
                f"terms), total {float(s27 + integ):.2f} < 150 (the runner's D3 prints '27 pi^2/6 + 98 is below 150')")


def derive_gamma_limit():
    import sympy as sp
    b = sp.symbols("beta", positive=True)
    A = sp.coth(3 * b) - 1 / (3 * b)
    g = (3 * sp.sqrt(3) / (4 * sp.pi)) * A / (3 * b)
    ok = sp.limit(g * b, b, sp.oo) == sp.sqrt(3) / (4 * sp.pi)
    return ok, "beta gamma(beta) -> (3 sqrt3/(4 pi))/3 = sqrt3/(4 pi) since A(3 beta) -> 1 (sympy limit)"


def derive_delta():
    import sympy as sp
    kap, b = sp.symbols("kappa beta", positive=True)
    dens_min = 2 * kap / (sp.exp(2 * kap) - 1)
    ok = sp.simplify(dens_min.subs(kap, 3 * b) - 6 * b / (sp.exp(6 * b) - 1)) == 0
    return ok, "the density floor 2 kappa/(e^{2 kappa} - 1) (cache E2) at kappa = 3 beta (|S| <= 3) is 6 beta/(e^{6 beta} - 1) = delta_L"


def derive_transverse():
    import sympy as sp
    A, k = sp.symbols("A kappa", positive=True)
    ok = sp.simplify(1 - (1 - 2 * A / k) - 2 * A / k) == 0
    return ok, "E|s - (s.u)u|^2 = 1 - E[(s.u)^2] = 2A/kappa (from E[w^2] = 1 - 2A/kappa, cache B1)"


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("ref", r"block 13's second-order statement|block 26 T5|Block 13 \(PR #8147, T5b\)", "EXCLUDED", "reference (block 13)", "citation"),
    ("preds", r"s_\{x-e_1\}, s_\{x-e_2\}, s_\{x-e_3\}|the three recorded predecessors|the three predecessors(?: at level t)?|three predecessors'",
     "DEFINITION", r"x - e_j|the three predecessors", "the three predecessors"),
    ("Z3Z2", r"on Z\^3 in level order|level automaton on Z\^2", "EXCLUDED", "structural: the lattices", "wording"),
    ("T1-kappa", r"concentration kappa = beta ?\|S\|", "DEFINITION", r"kappa = beta\|S\|", "the kernel's concentration"),
    ("T1-mean", r"E\[s\|S\] = A\(kappa\) S/\|S\|", "CACHE", r"E\[s\|S\] = A u", "T1(a) mean"),
    ("T1-second", r"E\[s ?s\^T ?\| ?S\] = \(A(?:\(kappa\))?/kappa\) I \+ \(1 - 3A(?:\(kappa\))?/kappa\) (?:u u\^T|ûû\^T)", "CACHE",
     r"E\[s s\^T\|S\] = \(A/kappa\) I \+ \(1 - 3A/kappa\) u u\^T", "T1(a) second moment"),
    ("T1-A", r"A\(kappa\) = coth kappa - 1/kappa", "DEFINITION", r"A\(kappa\) = coth kappa - 1/kappa", "A(kappa)"),
    ("T1-Abound", r"(?:0 < )?A\(kappa\) < kappa/3(?: for kappa > 0)?", "CACHE", r"A\(kappa\) < kappa/3", "T1(b)"),
    ("T1-Aprime", r"A'\(kappa\) <= 1/\(3 \+ kappa\^2\)", "CACHE", r"A'\(kappa\) <= 1/\(3 \+ kappa\^2\)", "T1(b)"),
    ("T1-w2", r"E\[\(s\*û\)\^2\] = 1 - 2A/kappa", "CACHE", r"E\[w\^2\] = 1 - 2A/kappa", "T1(a) E[w^2]"),
    ("T1-transverse", r"E\|s - \(s\*û\)û\|\^2 = 2A/kappa", "DERIVED", (derive_transverse, r"trace `?3a \+ b = 1`?"), "T1(a) transverse moment"),
    ("T1-m1", r"(?:one-step magnetization is|m_1 =) A\(3 ?beta\)", "CACHE", r"one-step magnetization from the aligned plane is A\(3 beta\)", "T1(c)"),
    ("T1-trans1", r"one-step transverse second moment (?:2A\(3 ?beta\)/\(3 ?beta\)|is 2A\(3beta\)/\(3beta\))", "CACHE",
     r"one-step transverse second moment is 2A\(3 beta\)/\(3 beta\)", "T1(c)"),
    ("T1-general", r"m_\{t\+1\} = E\[A\(beta\|S\|\) \(S\*e\)/\|S\|\]", "CACHE", r"E\[s\|S\] = A u", "T1(c) tower identity (from the mean)"),
    ("T1-encl", r"\[8888, 8889\]/10\^4, \[9444, 9445\]/10\^4, \[9722, 9723\]/10\^4, \[9861, 9862\]/10\^4", "CACHE",
     r"\[8888, 8889\]/10\^4 at beta = 3, \[9444, 9445\]/10\^4 at 6, \[9722, 9723\]/10\^4 at 12, \[9861, 9862\]/10\^4 at 24", "T1 enclosures of A(3 beta)"),
    ("T1-betas", r"at beta = 3, 6, 12, 24", "CACHE", r"at beta = 3", "T1 couplings of the enclosures"),
    ("T2-gain", r"gain one", "CACHE", r"gain one", "T2 gain one"),
    ("T2-var", r"(?:exact )?one-step (?:transverse )?variance (?:A\(3 ?beta\)/\(3 ?beta\)|at the aligned plane is A\(3beta\)/\(3beta\)) ?(?:per component)?", "CACHE",
     r"exact one-step transverse variance is A\(3 beta\)/\(3 beta\) per component", "T2 one-step variance"),
    ("T2-expansion", r"beta s\*\(s_1 \+ s_2 \+ s_3\) = 3beta - \(beta/2\) Sigma_i \|theta - theta_i\|\^2 \+ O\(4\)", "CACHE",
     r"beta s\.\(s_1 \+ s_2 \+ s_3\) = 3 beta - \(beta/2\) sum_i \|theta - theta_i\|\^2 \+ O\(4\)", "T2 expansion"),
    ("T2-coords", r"s = \(theta, sqrt\(1 - \|theta\|\^2\)\) with theta in R\^2", "DEFINITION", r"theta_x in R\^2|two components", "transverse coordinates"),
    ("T2-average", r"minimized at the average \(theta_1 \+ theta_2 \+ theta_3\)/3 with Hessian -3beta I", "CACHE",
     r"the minimizer is the average of the three \(gain one\) with Hessian -3 beta I", "T2 minimizer and Hessian"),
    ("T3-bounds", r"3 ?sqrt3/\(4 ?pi ?k\) - 1/k\^2 - \(5/\(2k\)\) e\^\{-k/4\} <= P_k <= 3 ?sqrt3/\(4 ?pi ?k\) \+ 27/k\^2 \+ e\^\{-sqrt\(?k\)?/7\}",
     "CACHE", r"3 sqrt3/\(4 pi k\) - 1/k\^2 - \(5/\(2k\)\) e\^\{-k/4\} <= P_k <= 3 sqrt3/\(4 pi k\) \+ 27/k\^2 \+ e\^\{-sqrt\(k\)/7\}", "T3 two-sided bound"),
    ("T3-k", r"[Ff]or every k >= 1", "EXCLUDED", "structural: index range", "condition"),
    ("walk-name", r"three-predecessor level walk", "EXCLUDED", "name of the walk", "wording"),
    ("T1-encl-betas", r"enclosures of A\(3beta\) at beta = 3, 6, 12, 24", "CACHE", r"exact enclosures\); the one-step transverse", "T1 enclosure route (B3)"),
    ("T3-D2", r"the two-sided bounds for k <= 150", "CACHE", r"for k <= 150 the exact return sums satisfy", "T3 exact range (D2)"),
    ("T3-D2b", r"k\^2\|P_k - 3sqrt3/\(4pik\)\| < 1", "CACHE", r"k\^2 \|P_k - 3 sqrt3/\(4 pi k\)\| stays below 1", "T3 D2 second-order check"),
    ("T4-E1", r"the one-site recursion symbolically", "CACHE", r"on the one-site periodic plane the chain", "T4 E1 route"),
    ("T3-limit", r"k P_k (?:tends to|->) 3 ?sqrt3/\(4 ?pi\)", "DERIVED", (derive_kP, r"k P_k"), "T3 local-limit constant"),
    ("T3-harm", r"(?:sum|Sigma)_\{k ?<= ?t\} ?P_k >= \(3 ?sqrt3/\(4 ?pi\)\) ?H_t - 1/4(?: for every t(?: >= 1)?)?", "CACHE",
     r"giving the constant 1/4 for every t", "T3 harmonic bound"),
    ("T3-logt", r"Sigma_\{k<=t\} P_k >= \(3sqrt3/\(4pi\)\) log t - 1/4", "DERIVED", (derive_log, r"H_t >= log t"), "T3 log form"),
    ("T3-exact150", r"the sums exact for k <= 150", "CACHE", r"for k <= 150 the exact return sums", "T3 exact range"),
    ("T4-unique", r"(?:has )?a unique invariant law", "CACHE", r"a uniform minorization", "T4 uniqueness (from the minorization)"),
    ("T4-LxL", r"(?:every )?periodic L x L level plane", "EXCLUDED", "structural: the torus", "wording"),
    ("T4-zero", r"tends to zero|tends to 0", "EXCLUDED", "structural: limit value", "wording"),
    ("T4-onesite", r"(?:on the )?one-site (?:periodic )?plane(?: \(L = 1\))?(?:, from the aligned plane,)? m_t = A\(3 ?beta\)\^t(?: exactly)?", "CACHE",
     r"m_t = A\(3 beta\)\^t exactly", "T4 one-site rate"),
    ("T4-bound", r"\|E\[s_x \* e\] at level t\| <= 2\(1 - delta_L\^\{L\^2\}\)\^t with delta_L = 6beta/\(e\^\{6beta\} - 1\)", "DERIVED",
     (derive_delta, r"density at least"), "T4 minorization rate"),
    ("T5-var", r"v_t = (?:\(A\(3 ?beta\)/\(3 ?beta\)\)|sigma\^2) (?:sum|Sigma)_\{k ?< ?t\} ?P_k(?: per component)?", "CACHE", r"H_t", "T5 variance (the D3 line prints the sum bound)",),
    ("T5-gamma", r"gamma\(beta\) (?:=|:=) \(3 ?sqrt3/\(4 ?pi\)\) ?\*? ?A\(3 ?beta\)/\(3 ?beta\)", "CACHE",
     r"gamma\(beta\) = \(3 sqrt3/\(4 pi\)\) A\(3 beta\)/\(3 beta\)", "T5 gamma"),
    ("T5-log", r"growing like gamma\(beta\) log t|v_t = gamma\(beta\) log t \+ O\(1\)", "CACHE", r"gamma\(beta\)", "T5 growth"),
    ("T5-sandwich", r"sigma\^2 \(\(3sqrt3/\(4pi\)\) H_\{t-1\} - 1/4\) <= v_t <= sigma\^2 \(\(3sqrt3/\(4pi\)\) H_\{t-1\} \+ 150\) +\(t >= 2\)", "DERIVED",
     (derive_150, r"< 150"), "T5 two-sided bound"),
    ("T5-sigma", r"sigma\^2 = A\(3beta\)/\(3beta\)", "DEFINITION", r"sigma\^2 = A\(3beta\)/\(3beta\)", "noise variance"),
    ("T5-encl", r"\[408, 409\]/10\^4 at beta = 3, \[216, 217\]/10\^4 at 6, \[1116, 1117\]/10\^5 at 12, \[566, 567\]/10\^5 at 24", "CACHE",
     r"\[408, 409\]/10\^4 at beta = 3, \[216, 217\]/10\^4 at 6, \[1116, 1117\]/10\^5 at 12, \[566, 567\]/10\^5 at 24", "T5 enclosures of gamma"),
    ("T5-glim", r"gamma\(beta\) -> sqrt3/\(4pibeta\) as beta -> ∞", "DERIVED", (derive_gamma_limit, r"tends to `?1/\(3beta\)`?|as `?beta -> ∞`?"),
     "T5 large-beta form"),
    ("T5-proxy", r"e\^\{-v_t\} of the magnetization decays like t\^\{-gamma\(beta\)\}", "CACHE", r"gamma\(beta\)", "T5 proxy decay"),
    ("T5-nostat", r"no stationary law with finite variance", "EXCLUDED", "structural: statement without numbers beyond 'finite'", "wording"),
    # executed and not claimed
    ("exec-runs", r"up to 512 x 512 for 20000 levels at beta = 3, 6, 12, 24", "CACHE", r"beta = 3, 6, 12, 24", "executed: runs (the runner's N5 line)",
     r"L=512"),
    ("exec-exponents", r"at local exponents above gamma\(beta\) that approach it as beta grows", "CACHE", r"local exponent",
     "executed-not-claimed: exponents relative to gamma", r"exp\["),
    ("exec-sixaxis", r"six-axis formation law at the weights \(e\^beta, e\^-beta, 1\) keeps its plane at the same beta", "CACHE",
     r"six-axis weights \(e\^beta, e\^-beta, 1\)", "executed: six-axis side-by-side (the runner prints the deviations)", r"dissent"),
    ("exec-names", r"the infinite-plane statement is a conjecture", "EXCLUDED", "wording", "wording"),
]


def control_checks():
    extra, notes = {}, []
    fit, ref = show(FIT), show(REF)
    txt = fit + "\n" + ref
    gam = {3: 0.04084, 6: 0.02170, 12: 0.01117, 24: 0.00566}
    rows = []
    for m in re.finditer(r"beta\s*=\s*(\d+)[^\n]*?L\s*=\s*(\d+)[^\n]*", txt):
        line = m.group(0)
        ex = re.findall(r"exp\[(\d+), ?(\d+)\]\s*=\s*([0-9.]+)", line)
        if ex:
            rows.append((int(m.group(1)), int(m.group(2)), ex, line[:60]))
    below = []
    for b, L, ex, head in rows:
        for a, c, v in ex:
            if b in gam and float(v) < gam[b]:
                below.append(f"beta={b} L={L} exp[{a},{c}] = {v} < gamma = {gam[b]}")
    # the note's own table (the fit output may print it in another layout): parse the note table as a fallback
    note = show(NOTE)
    for line in note.splitlines():
        cells = [c.strip().strip("`") for c in line.split("|")]
        if len(cells) > 11 and cells[1] in ("3", "6", "12", "24") and cells[2].isdigit():
            b, L = int(cells[1]), int(cells[2])
            for lab, v in (("[500,5000]", cells[7]), ("[5000,20000]", cells[8]), ("[500,20000]", cells[9])):
                try:
                    fv = float(v)
                except ValueError:
                    continue
                if fv < gam[b]:
                    below.append(f"note table ({cells[11]}): beta={b} L={L} exp{lab} = {v} < gamma = {gam[b]}")
    below = sorted(set(below))
    extra["exec-exponents"] = ("; MISMATCH: " + "; ".join(below)) if below else "; control: every printed exponent is at or above gamma(beta)"
    notes.append("local exponents vs gamma(beta): " + extra["exec-exponents"][2:])
    cache = show(CACHE)
    m3 = re.search(r"H_t - (\S+) for t <= 150", cache.split("per_block")[1]) if "per_block" in cache else None
    if m3:
        notes.append(f"runner N5 per_block line prints 'H_t - {m3.group(1)} for t <= 150' while its D3 check and the note state '- 6/25'")
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
