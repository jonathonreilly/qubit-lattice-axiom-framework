#!/usr/bin/env python3
"""J:provenance:PR8178 - every number in the theorem statements of the block 34 note (torus memory time of the sphere formation law),
located in the runner's cached stdout, in the runner's own checks, or in an exact derivation in the note.

Statement text = the front-matter claim_scope + each '## Theorem ...' section with its proof spans removed ('*Proof.* ... ∎').  Every
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
PR = 8178
BRANCH = "physics-loop/admissibility-induced-law-block34-sphere-formation-law-torus-memory-time-zero-mode-rate-and-stationary-modes-20260917"
HEAD = "e6ffae5b460b9ec0fd0d99c99f9784232bd225bd"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_BRACKETED_AND_THE_"
        "NONLINEAR_LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
RUNNER = "scripts/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_nonlinear_law_measured_2026_09_17.py"
CACHE = ("logs/runner-cache/admissibility_rule_unsoldered_formation_law_torus_memory_time_zero_mode_rate_exactly_stationary_modes_bracketed_"
         "nonlinear_law_measured_2026_09_17.txt")
SPECS = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/"
MSD, REF, SIM = (SPECS + "supervisor_control_block34_torus_msd.out.txt", SPECS + "supervisor_control_block34_refuter.out.txt",
                 SPECS + "supervisor_control_block34_torus_sim.out.txt")
OTHER = [MSD, REF, SIM]


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
        ("κ", "kappa"), ("∈", " in "), ("↑", " up "), ("·", "*"))


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
            out.append((title.split(" — ")[0], norm(body)))
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


# ------------------------------------------------------------------------------------------------------------------ exact re-derivations
def exp_lower(x, n=80):
    s, term = Fr(0), Fr(1)
    for k in range(n + 1):
        s += term
        term = term * x / (k + 1)
    return s


def tau_enclosure(beta, L):
    """tau = 3 beta L^2 / A(3 beta), A(kappa) = coth kappa - 1/kappa = 1 + 2/(e^{2 kappa} - 1) - 1/kappa: with E_lo <= e^{2 kappa},
    1 - 1/kappa < A < 1 - 1/kappa + 2/(E_lo - 1).  (A route different from the runner's two-sided series enclosure.)"""
    kappa = Fr(3 * beta)
    e_lo = exp_lower(2 * kappa)
    a_lo, a_hi = 1 - 1 / kappa, 1 - 1 / kappa + 2 / (e_lo - 1)
    return Fr(3 * beta * L * L) / a_hi, Fr(3 * beta * L * L) / a_lo


def derive_interval(beta, L, lo, hi):
    def f():
        t_lo, t_hi = tau_enclosure(beta, L)
        ok = lo <= t_lo and t_hi <= hi and t_hi - t_lo < Fr(1, 10)
        return ok, (f"tau_L = 3 beta L^2/A(3 beta) (the note's T3.1 formula) at (beta, L) = ({beta}, {L}): exact enclosure "
                    f"[{float(t_lo):.6f}, {float(t_hi):.6f}] (width {float(t_hi - t_lo):.1e}) inside the stated [{lo}, {hi}]")
    return f


def derive_reaches_one():
    s2, L, t = Fr(1, 7), 16, None                       # any sigma^2 > 0: Var theta_bar_t = sigma^2 t / L^2 = 1 at t = L^2/sigma^2
    tau = Fr(L * L) / s2
    ok = s2 * tau / (L * L) == 1
    return ok, "Var theta_bar_t = sigma^2 t/L^2 (cache B2) equals 1 exactly at t = tau_L = L^2/sigma^2; exp(-t/tau_L) = e^{-1} there"


def derive_lambda_max():
    # 1 - u <= Q(k) <= lambda_max |k|^2 with lambda_max(M) = 1/3: eigenvalues of (1/9)[[2,-1],[-1,2]] are the roots of x^2 - (4/9)x + 1/27
    tr, det = Fr(4, 9), Fr(3, 81)
    disc = tr * tr - 4 * det                           # = 4/81 -> sqrt = 2/9
    ok = disc == Fr(4, 81) and (tr + Fr(2, 9)) / 2 == Fr(1, 3) and (tr - Fr(2, 9)) / 2 == Fr(1, 9)
    return ok, "eigenvalues of M: (4/9 +- 2/9)/2 = 1/3, 1/9 exactly; so Q(k) <= |k|^2/3"


def derive_bracket_constants():
    # V_L = (sigma^2/L^2) sum 1/(1-u); 1/(1-u) >= 3/|k|^2 and <= (9 pi^2/4)/|k|^2; |k|^2 = (2 pi/L)^2 |n|^2
    import sympy as sp
    L, n2 = sp.symbols("L n2", positive=True)
    lo = sp.simplify((1 / L ** 2) * 3 / ((2 * sp.pi / L) ** 2 * n2) * n2)
    hi = sp.simplify((1 / L ** 2) * (9 * sp.pi ** 2 / 4) / ((2 * sp.pi / L) ** 2 * n2) * n2)
    ok = sp.simplify(lo - 3 / (4 * sp.pi ** 2)) == 0 and sp.simplify(hi - sp.Rational(9, 16)) == 0
    return ok, f"(1/L^2) * 3/((2 pi/L)^2 |n|^2) = {lo}/|n|^2 and (1/L^2) * (9 pi^2/4)/((2 pi/L)^2 |n|^2) = {hi}/|n|^2 (sympy)"


def derive_vt_split():
    import sympy as sp
    t, s2, L, W = sp.symbols("t sigma2 L W", positive=True)    # W = sum_{k != 0} (1 - u^t)/(1 - u)
    vt = s2 / L ** 2 * (t + W)
    ok = sp.simplify(sp.exp(-vt) - sp.exp(-(s2 / L ** 2) * W) * sp.exp(-t / (L ** 2 / s2))) == 0
    return ok, "e^{-v_t} = e^{-V_L(t)} e^{-t/tau_L} with V_L(t) = (sigma^2/L^2) sum_{k != 0}(1 - u^t)/(1 - u) (T1.3's v_t split; sympy)"


# ------------------------------------------------------------------------------------------------------------------ the items
# (id, statement regex, kind, source, role[, elsewhere])
ITEMS = [
    ("ref-b26", r"block 26(?: \(PR #8170\))?(?:, T5|'s| T5)?", "EXCLUDED", "reference (block 26 = PR #8170)", "citation"),
    ("gain-one", r"gain one", "DEFINITION", r"gain one", "the linearization's gain (block 26 T2)"),
    ("sigma2-def", r"sigma\^2 = A\(3 ?beta\)/\(3 ?beta\)", "DEFINITION", r"sigma\^2 = A\(3beta\)/\(3beta\)", "noise variance"),
    ("A-def", r"A\(kappa\) = coth kappa - 1/kappa", "DEFINITION", r"A\(kappa\) = coth kappa - 1/kappa", "A(kappa)"),
    ("recursion", r"theta_\{t\+1\} = P theta_t \+ xi_t", "DEFINITION", r"theta_\{t\+1\} = P theta_t \+ xi_t", "the linearized recursion"),
    ("phi-def", r"phi\(k\) = \(1 \+ e\^\{i ?k_1\} \+ e\^\{i ?k_2\}\)/3", "CACHE", r"phi = \(1 \+ e\^\{i k1\} \+ e\^\{i k2\}\)/3", "T1.1 multiplier"),
    ("T1-identity", r"1 - \|phi\(k\)\|\^2 = \(4/9\)\[sin\^2\(k_1/2\) \+ sin\^2\(k_2/2\) \+ sin\^2\(\(k_1 - k_2\)/2\)\]", "CACHE",
     r"1 - \|phi\(k\)\|\^2 = \(4/9\)\[sin\^2\(k1/2\) \+ sin\^2\(k2/2\) \+ sin\^2\(\(k1 - k2\)/2\)\]", "T1.2 multiplier identity"),
    ("T1-bounds", r"\|phi\| < 1 off the zero mode|0 <= u\(k\) <= 1 with u = 1 iff k in 2piZ\^2, i\.e\. only at the zero mode", "CACHE",
     r"0 <= \|phi\|\^2 <= 1 with equality only at the zero mode", "T1.2 |phi| < 1 off the zero mode"),
    ("T1-modvar", r"(?:multiplier modulus u\^\{1/2\} < 1 has variance sigma\^2 \(1 - u\^t\)/\(1 - u\))|(?:Var theta\^_k\(t\) = sigma\^2\(1 - u\^t\)/\(1 - u\) for u = u\(k\) < 1)",
     "CACHE", r"sigma\^2 \(1 - u\^t\)/\(1 - u\) after t levels", "T1.3 mode variance"),
    ("T1-modrec", r"theta\^_k\(t\+1\) = phi\(k\) theta\^_k\(t\) \+ xi\^_k\(t\) from theta\^_k\(0\) = 0", "CACHE",
     r"driven by white noise of variance sigma\^2", "T1.3 mode recursion from zero"),
    ("T1-sitevar", r"\(sigma\^2/L\^2\)\[t \+ (?:sum|Sigma)_\{k ?!= ?0\} ?\(1 - u_k\^t\)/\(1 - u_k\)\]", "CACHE",
     r"\(1/L\^2\)\[t \+ sum_\{k != 0\} \(1 - u_k\^t\)/\(1 - u_k\)\]", "T1.3 site variance"),
    ("T2-tori", r"tori L = 2, 3, 4", "CACHE", r"tori L = 2, 3, 4", "T2 torus sides"),
    ("T2-recursion", r"Sigma_\{t\+1\} = P ?Sigma_t ?P\^T \+ sigma\^2 ?I(?: from Sigma_0 = 0)?", "CACHE",
     r"Sigma_\{t\+1\} = P Sigma_t P\^T \+ I", "T2 covariance recursion"),
    ("T2-cosines", r"cos\(2pin/L\) are rational", "EXCLUDED", "structural: why L = 2, 3, 4 give rational cosines", "wording"),
    ("T2-size", r"rational L\^2 x L\^2 matrix", "EXCLUDED", "structural: matrix size", "wording"),
    ("T2-levels", r"t <= 12 \(L = 2, 3\) and t <= 8 \(L = 4\)", "CACHE", r"L=2: v_12 = .*L=3: v_12 = .*L=4: v_8 =", "T2 levels iterated"),
    ("T2-planeavg", r"1\^TSigma_t1/L\^4 equal to t/L\^2", "CACHE", r"t/L\^2 for the plane average", "T2 plane average"),
    ("T3-tau-def", r"tau_L :?= L\^2/sigma\^2 = 3 ?beta ?L\^2 ?/ ?A\(3 ?beta\)", "CACHE", r"tau_L = 3 beta L\^2 / A\(3 beta\)", "T3.1 memory time"),
    ("T3-reaches-one", r"reaches one|fallen by e\^\{-1\}", "DERIVED", (derive_reaches_one, r"reaches one"), "T3.1 the defining level"),
    ("T3-rate", r"(?:1/tau_L = )?A\(3 ?beta\)/\(3 ?beta ?L\^2\)", "CACHE", r"A\(3 beta\)/\(3 beta L\^2\)", "T3.1 rate"),
    ("T3-width", r"width below 1/10", "CACHE", r"width < 1/10", "T3.1 enclosure width"),
    ("T3-grid", r"beta = 6, 12, 24, 48 and L = 16, 32, 64", "CACHE", r"beta = 6, 12, 24, 48 and L = 16, 32, 64", "T3.1 grid"),
    ("T3-i616", r"\[4879, 4880\](?: at \(6, 16\))?", "CACHE", r"beta=6 L=16: tau in \[4879, 4880\]", "T3.1 interval (6,16)"),
    ("T3-i632", r"\[19516, 19517\](?: at \(6, 32\))?", "CACHE", r"beta=6 L=32: tau in \[19516, 19517\]", "T3.1 interval (6,32)"),
    ("T3-i664", r"\[78064, 78065\](?: at (?:\(6, 64\)|beta = 6))?", "CACHE", r"beta=6 L=64: tau in \[78064, 78065\]", "T3.1 interval (6,64)"),
    ("T3-i1216", r"\[9479, 9480\] at \(12, 16\)", "CACHE", r"beta=12 L=16: tau in \[9479, 9480\]", "T3.1 interval (12,16)"),
    ("T3-i2416", r"\[18691, 18692\] at \(24, 16\)", "DERIVED", (derive_interval(24, 16, 18691, 18692), r"\[18691, 18692\]"),
     "T3.1 interval (24,16): runner prints rows[:4] only and checks it within its (18680, 18700) window"),
    ("T3-i4816", r"\[37121, 37122\] at \(48, 16\)", "DERIVED", (derive_interval(48, 16, 37121, 37122), r"\[37121, 37122\]"),
     "T3.1 interval (48,16): runner prints rows[:4] only and checks it within its (37110, 37130) window"),
    ("T3-split", r"e\^\{-v_t\} = e\^\{-V_L\(t\)\} e\^\{-t/tau_L\}", "DERIVED", (derive_vt_split, r"e\^\{-v_t\} = e\^\{-V_L\(t\)\}"),
     "T3.1 proxy split"),
    ("T3-VL-def", r"V_L = \(sigma\^2/L\^2\) sum_\{k != 0\} 1/\(1 - u_k\)", "CACHE", r"V_L = \(1/L\^2\) sum_\{k != 0\} 1/\(1 - u_k\)", "T3.2 V_L"),
    ("T3-bracket", r"(?:lies in )?\[3/\(4 ?pi\^2\), 9/16\] sigma\^2 S_L|\(3/\(4pi\^2\)\) sigma\^2 S_L <= V_L <= \(9/16\) sigma\^2 S_L", "CACHE",
     r"V_L in \[3/\(4 pi\^2\), 9/16\] sigma\^2 S_L", "T3.2 bracket"),
    ("T3-bracket-const", r"with \|k\|\^2 = \(2pi/L\)\^2\|n\|\^2", "DERIVED", (derive_bracket_constants, r"\(2pi/L\)\^2\|n\|\^2"),
     "T3.2 bracket constants from the two sine bounds"),
    ("T3-SL-def", r"S_L = sum over nonzero n in the symmetric box of 1/\|n\|\^2", "CACHE", r"S_L", "T3.2 lattice sum"),
    ("T3-diffs", r"(?:consecutive differences lie within one of 2 ?pi log 2)|(?:S_16, S_32, S_64 increase and consecutive differences lie within one of 2pi log 2)",
     "CACHE", r"S_16, S_32, S_64 increase .* within 1 of 2 pi log 2", "T3.2 lattice-sum increments"),
    ("T3-growth", r"S_L = 2pi log L \+ O\(1\)", "CACHE", r"the growth 2 pi log L \+ O\(1\)", "T3.2 growth"),
    ("T3-eig", r"M has eigenvalues 1/9 and 1/3", "CACHE", r"M = \(1/9\)\[\[2,-1\],\[-1,2\]\] has eigenvalues 1/9 and 1/3", "T3.2 eigenvalues"),
    ("T3-sin1", r"sin\^2\(x/2\) <= x\^2/4 \(all x\)", "CACHE", r"sin\^2\(x/2\) <= x\^2/4", "T3.2 sine bound 1"),
    ("T3-Q", r"1 - u <= Q\(k\) <= \|k\|\^2/3", "DERIVED", (derive_lambda_max, r"1 - u <= Q\(k\) <= \|k\|\^2/3"), "T3.2 upper bound of 1 - u"),
    ("T3-sin2", r"sin\(x/2\) >= x/pi on \[0, pi\]", "CACHE", r"sin\(x/2\) >= x/pi on \[0, pi\]", "T3.2 sine bound 2"),
    ("T3-lowerQ", r"1 - u >= \(4/\(9pi\^2\)\)\|k\|\^2 for the representative with \|k_i\| <= pi", "CACHE",
     r"1/\(1 - u\(k\)\) <= \(9 pi\^2/4\)/\|k\|\^2 on the square", "T3.2 lower bound of 1 - u (printed as its reciprocal)"),
    ("T3-infplane", r"decays like t\^\{-gamma\}", "EXCLUDED", "reference: block 26 T5 (infinite plane)", "citation"),
    ("T3-Lsq", r"at level t = L\^2", "EXCLUDED", "structural: the level L^2 (exponent)", "wording"),
    ("T3-D1-encl", r"exact enclosure of A\(3beta\) \(D1\)", "CACHE", r"tau_L = 3 beta L\^2 / A\(3 beta\) enclosed exactly", "T3.1 route"),
    ("zero-mode", r"zero(?:-| )mode", "EXCLUDED", "structural: the name of the k = 0 mode", "wording"),
    ("pronoun-one", r"exponential one|one has", "EXCLUDED", "wording: 'one' used as a pronoun", "wording"),
    # executed and not claimed (control / refuter outputs)
    ("exec-VL", r"V_L(?:/sigma\^2)? = 2 ?(?:gamma|c_0) log L \+ 0\.353(?: ?sigma\^2)? \+ o\(1\)", "CACHE", r"0\.353",
     "executed-not-claimed: V_L asymptotic constant", r"V_L - 2 c0 log L = 0\.35"),
    ("exec-gamma", r"gamma = \(3 sqrt3/\(4 pi\)\) sigma\^2|c_0 = 3sqrt3/\(4pi\)", "DEFINITION", "inline",
     "gamma / c_0 = 3 sqrt3/(4 pi) (block 26's local-limit constant, restated inline)"),
    ("exec-VL-2g", r"V_L = 2gamma log L \+ 0\.353sigma\^2", "CACHE", r"0\.353", "executed-not-claimed: V_L asymptotic (restated)", r"V_L - 2 c0 log L"),
    ("exec-diffs", r"(?:the differences to 2c_0 log L being )?0\.3514, 0\.3525, 0\.3527, 0\.3528 at L = 16, 32, 64, 128", "CACHE", r"0\.3514", "executed-not-claimed: V_L - 2 c0 log L",
     r"V_L - 2 c0 log L = 0\.35"),
    ("exec-refspec", r"refuting spec, item 4", "EXCLUDED", "reference: the refuting spec's item 4", "citation"),
    ("exec-D1", r"times 1\.34, 1\.14, 1\.06, 1\.02 at beta = 6, 12, 24, 48 \(L = 16; 1\.42 and 1\.18 at L = 32 for beta = 6, 12\)", "CACHE",
     r"1\.34, 1\.14", "executed-not-claimed: D_1/(sigma^2/L^2)", r"lag    25: nonlinear"),
    ("exec-D1-sym", r"D_1 equal to sigma\^2/L\^2", "EXCLUDED", "structural: the name of the measured constant", "wording"),
    ("exec-m", r"tracking 1/\|m\|\^2 of the stationary magnetization within a few percent", "CACHE", r"1/\|m\|\^2",
     "executed-not-claimed: 1/|m|^2 tracking", r"mean \|m\| in the stationary regime"),
    ("exec-lin", r"linear model returning 0\.97-1\.01", "CACHE", r"0\.97-1\.01", "executed-not-claimed: linear-model calibration range",
     r"linear model MSD .* \(ratio"),
]


def control_checks():
    """compare the executed-not-claimed numbers of the claim_scope with the control outputs that print them."""
    msd = show(MSD)
    ref = show(REF)
    extra, notes = {}, []
    blocks = re.split(r"(?m)^beta=", msd)[1:]
    lin, lag25, mm = [], {}, {}
    for blk in blocks:
        head = blk.split("\n", 1)[0]
        beta, L = int(float(head.split()[0])), int(re.search(r"L=(\d+)", head).group(1))
        mm[(beta, L)] = float(re.search(r"mean \|m\| in the stationary regime ([0-9.]+)", head).group(1))
        for lag, nl, li in re.findall(r"lag +(\d+): nonlinear .*?ratio to sigma\^2/L\^2: ([0-9.]+) .*?\(ratio ([0-9.]+)", blk):
            lin.append((float(li), beta, L, int(lag)))
            if lag == "25":
                lag25[(beta, L)] = float(nl)
    stated = {(6, 16): 1.34, (12, 16): 1.14, (24, 16): 1.06, (48, 16): 1.02, (6, 32): 1.42, (12, 32): 1.18}
    parts = []
    for key, v in stated.items():
        c = lag25.get(key)
        parts.append(f"{key}: stated {v:.2f}, control lag-25 {c:.3f} ({'agrees' if abs(round(c, 2) - v) < 1e-9 else 'MISMATCH'})")
    extra["exec-D1"] = "; control: " + "; ".join(parts)
    lo = min(lin)
    hi = max(lin)
    lo_note_table = 0.96          # the note's own executed table lists 0.96 at (12, 32), lag 1000
    extra["exec-lin"] = (f"; control linear-model ratios over all lags/couplings {lo[0]:.3f} (beta={lo[1]}, L={lo[2]}, lag {lo[3]}) .. "
                         f"{hi[0]:.3f} (beta={hi[1]}, L={hi[2]}, lag {hi[3]}): stated 0.97-1.01 "
                         f"{'agrees' if round(lo[0], 2) >= 0.97 and round(hi[0], 2) <= 1.01 else 'MISMATCH'} (the note's own table shows {lo_note_table:.2f} at (12, 32), lag 1000)")
    gaps = []
    for key, c in lag25.items():
        inv = 1 / mm[key] ** 2
        gaps.append(f"{key}: {c:.3f} vs 1/|m|^2 {inv:.3f} ({100 * (inv - c) / inv:.1f}% below)")
    extra["exec-m"] = "; control: " + "; ".join(gaps)
    diffs = re.findall(r"L=(\d+): V_L/sigma\^2 = [0-9.]+; .*?V_L - 2 c0 log L = ([0-9.]+)", ref)
    extra["exec-diffs"] = "; refuter item 4 prints " + ", ".join(f"L={a}: {b}" for a, b in diffs)
    extra["exec-VL"] = extra["exec-diffs"]
    notes.append("control linear-model calibration: " + extra["exec-lin"][2:])
    notes.append("control D_1 ratios at lag 25 vs the claim_scope: " + extra["exec-D1"][11:])
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
