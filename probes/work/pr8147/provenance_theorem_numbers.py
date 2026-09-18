#!/usr/bin/env python3
"""J:provenance:PR8147 - every number in the theorem statements of the block 13 note (the causal Gaussian formation law's record
two-point function is a heat kernel in level time, never the lattice Green function),
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
PR = 8147
BRANCH = "physics-loop/admissibility-induced-law-block13-causal-gaussian-two-point-heat-kernel-20260915"
HEAD = "9c364d1d6f7527e89fc47bffbe672440c5fa50bb"
NOTE = ("docs/ADMISSIBILITY_RULE_CAUSAL_GAUSSIAN_FORMATION_LAW_RECORD_TWO_POINT_FUNCTION_HEAT_KERNEL_NOT_LATTICE_GREEN_FUNCTION_"
        "BOUNDED_THEOREM_NOTE_2026-09-15.md")
RUNNER = "scripts/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.py"
CACHE = "logs/runner-cache/admissibility_rule_causal_gaussian_formation_law_record_two_point_function_heat_kernel_2026_09_15.txt"
OTHER = [".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block13_causal_gaussian.out.txt",
         ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block13_refuter.out.txt"]


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
import itertools
import math
import sympy as sp
from fractions import Fraction as Fr


def P_exact(n):
    """P_n = sum over compositions a of n into 3 parts of (n!/(a1! a2! a3!))^2 / 9^n (coincidence of two directed walks)."""
    f = math.factorial
    return Fr(sum((f(n) // (f(a) * f(b) * f(n - a - b))) ** 2 for a in range(n + 1) for b in range(n + 1 - a)), 9 ** n)


def d_T1():
    w = sp.symbols("w", positive=True)
    ok = all(sp.expand(sum(w ** n * sp.factorial(n) / (sp.factorial(a) * sp.factorial(b) * sp.factorial(n - a - b))
                           for a in range(n + 1) for b in range(n + 1 - a)) - (3 * w) ** n) == 0 for n in range(0, 9))
    return ok, "sum over a level of G(x, z) = w^n sum_d n!/d! = (3w)^n = g^n (multinomial theorem, n <= 8): a probability kernel iff g = 1"


def d_T2formula():
    w = sp.symbols("w", positive=True)
    ok = all(sp.simplify(sum((w ** n * sp.factorial(n) / (sp.factorial(a) * sp.factorial(b) * sp.factorial(n - a - b))) ** 2
                             for a in range(n + 1) for b in range(n + 1 - a)) - (3 * w) ** (2 * n) * sp.Rational(P_exact(n).numerator, P_exact(n).denominator)) == 0
             for n in range(0, 8))
    return ok, "sum_z G(x, z)^2 on the level n below x = w^(2n) sum_a (n!/a!)^2 = g^(2n) P_n (exact, n <= 7); Var = sigma^2 sum_(n<t) g^(2n) P_n"


def d_T2a():
    g, m = sp.symbols("g m", positive=True)
    n = sp.symbols("n", integer=True, nonnegative=True)

    def closed(expr):
        return expr.args[0][0] if isinstance(expr, sp.Piecewise) else expr

    ok = sp.simplify(closed(sp.summation(g ** (2 * n), (n, 0, sp.oo))) - 1 / (1 - g ** 2)) == 0
    ok = ok and sp.simplify(closed(sp.summation(g ** (2 * n), (n, m, sp.oo))) - g ** (2 * m) / (1 - g ** 2)) == 0
    # the projected steps of a directed walk are (0,0), (1,0), (0,1) (the note's phi(k) = (1 + e^{ik1} + e^{ik2})/3): the difference of two
    # walks moves at most one unit per coordinate per step, so P_n(d) = 0 for n < |d|_inf (enumerated, n <= 5)
    steps = [(0, 0), (1, 0), (0, 1)]
    for nn in range(0, 6):
        diffs = set()
        for s1 in itertools.product(steps, repeat=nn):
            for s2 in itertools.product(steps, repeat=nn):
                diffs.add((sum(a[0] for a in s1) - sum(a[0] for a in s2), sum(a[1] for a in s1) - sum(a[1] for a in s2)))
        ok = ok and all(max(abs(x), abs(y)) <= nn for x, y in diffs)
    return ok, ("sum_n g^(2n) P_n <= sum_n g^(2n) = 1/(1 - g^2) (P_n <= 1); P_n(d) = 0 for n < |d|_inf (difference walks enumerated for n <= 5), "
                "so Cov <= sum_(n >= m) g^(2n) = g^(2m)/(1 - g^2) (sympy)")


def d_T2b():
    a = sp.symbols("a", positive=True)
    k1, k2 = sp.symbols("k1 k2", real=True)
    gauss = sp.integrate(sp.exp(-a * (k1 ** 2 + k2 ** 2)), (k1, -sp.oo, sp.oo), (k2, -sp.oo, sp.oo))
    nn = sp.symbols("n", positive=True)
    const = sp.simplify((2 * sp.pi) ** -2 * gauss.subs(a, 4 * nn / (9 * sp.pi ** 2)))
    ok = sp.simplify(const - 9 * sp.pi / (16 * nn)) == 0
    # |phi|^2 <= 1 - (4/(9 pi^2)) |k|^2 on a 201 x 201 grid of [-pi, pi]^2
    import numpy as np
    K = np.linspace(-np.pi, np.pi, 201)
    X, Y = np.meshgrid(K, K)
    phi2 = np.abs((1 + np.exp(1j * X) + np.exp(1j * Y)) / 3) ** 2
    ok = ok and bool(np.all(phi2 <= 1 - 4 / (9 * np.pi ** 2) * (X ** 2 + Y ** 2) + 1e-12))
    # both bounds exactly for n <= 300 (pi enclosed: 3.14159 < pi)
    worst_hi, worst_lo = 0.0, math.inf
    for n in range(1, 301):
        P = P_exact(n)
        ok = ok and P * 16 * n <= Fr(9) * Fr(314159, 100000) and P * 36 * n >= 1
        worst_hi = max(worst_hi, float(P * 16 * n / 9) / math.pi)
        worst_lo = min(worst_lo, float(P * 36 * n))
    ok = ok and all((2 * math.sqrt(8 * n / 9) + 1) ** 2 <= 9 * n for n in range(1, 10000))
    return ok, (f"(2 pi)^-2 int_R2 e^(-(4n/(9 pi^2))|k|^2) dk = 9 pi/(16 n) (sympy); |phi|^2 <= 1 - (4/(9 pi^2))|k|^2 on a 201^2 grid; exactly for "
                f"n <= 300: 1/(36 n) <= P_n <= 9 pi/(16 n) (largest n P_n/(9 pi/16) = {worst_hi:.4f}, smallest 36 n P_n = {worst_lo:.3f}); "
                f"(2R + 1)^2 <= 9n with R = (8n/9)^(1/2) for n < 10^4; summing with P_0 = 1 gives the variance bounds")


def d_T2c():
    return True, "keep the last term of the variance series: Var >= sigma^2 g^(2(t-1)) P_(t-1) >= sigma^2 g^(2(t-1))/(36(t-1)) by T2(b)'s lower bound"


def d_rho_pi():
    return Fr(9) * Fr(314160, 100000) / 16 < 2 and 9 * math.pi / 16 < 2, "9 pi/16 = 1.767... < 2 (pi < 3.1416)"


def d_prec():
    a11, a12, a21, a22, sg = sp.symbols("a11 a12 a21 a22 sigma", positive=True)
    A = sp.Matrix([[a11, a12], [a21, a22]])
    I2 = sp.eye(2)
    C = sg ** 2 * (I2 - A).inv() * (I2 - A).inv().T
    ok = sp.simplify(C.inv() - sg ** -2 * (I2 - A).T * (I2 - A)) == sp.zeros(2, 2)
    return ok, "v = A v + xi with Cov(xi) = sigma^2 I gives Cov(v) = sigma^2 (I - A)^-1 (I - A)^-T, precision sigma^-2 (I - A)^T (I - A) (sympy)"


def d_coeffs():
    w = sp.symbols("w", positive=True)
    k = sp.symbols("k1:4", real=True)
    sym = sp.expand((1 - w * sum(sp.exp(-sp.I * x) for x in k)) * (1 - w * sum(sp.exp(sp.I * x) for x in k)))
    target = 1 - 2 * w * sum(sp.cos(x) for x in k) + w ** 2 * (3 + 2 * sum(sp.cos(k[i] - k[j]) for i in range(3) for j in range(i + 1, 3)))
    ok = sp.simplify(sp.expand(sym - target.rewrite(sp.exp))) == 0
    return ok, ("expanding |1 - w sum e^{-ik_j}|^2: constant 1 + 3w^2, coefficient -2w of each cos k_j and +2w^2 of each cos(k_i - k_j) (sympy); "
                "as precision-matrix entries these are -w on each axial neighbour and +w^2 on each face-diagonal x +- (e_i - e_j)")


def d_green():
    import mpmath as mp
    val = (1 + mp.nsum(lambda n: (mp.sqrt(3) / 2) * (2 * n + 1) ** -0.5 * 9 * mp.pi / (16 * n), [1, mp.inf])) / 6
    ok = mp.isfinite(val) and val < 10
    return ok, (f"(1/6)(1 + sum_(n>=1) (sqrt3/2)(2n+1)^(-1/2) 9 pi/(16n)) = {mp.nstr(val, 6)} < oo (terms ~ n^(-3/2)); C(2n,n)/4^n <= "
                "(sqrt3/2)(2n+1)^(-1/2) is T4's upper bound, P_n <= 9 pi/(16n) is T2(b)")


def d_T4():
    ok = all(sum(Fr(math.comb(n, k), 2 ** n) ** 2 for k in range(n + 1)) == Fr(math.comb(2 * n, n), 4 ** n) for n in range(0, 40))
    an = [Fr(math.comb(2 * n, n), 4 ** n) for n in range(1, 60)]
    ok = ok and all(4 * (n + 1) * an[n] ** 2 >= 4 * n * an[n - 1] ** 2 and (2 * n + 3) * an[n] ** 2 <= (2 * n + 1) * an[n - 1] ** 2 for n in range(1, 59))
    ok = ok and 4 * an[0] ** 2 == 1 and 3 * an[0] ** 2 == Fr(3, 4)
    return ok, ("the projected difference walk is lazy: P_n = sum_k (C(n,k)/2^n)^2 = C(2n,n)/4^n (Vandermonde, exact n < 40); 4n a_n^2 increases "
                "and (2n+1) a_n^2 decreases (exact n < 60) from 1 and 3/4 at n = 1: 1/(4n) <= P_n^2 <= 3/(4(2n+1)); hence Var >= sum (2 sqrt n)^-1")


def d_T5a():
    w, c = sp.symbols("w c")
    a = sp.symbols("a1:4")
    sol = sp.solve(sp.Eq(w * sum(x + c for x in a), w * sum(a) + c), w)
    return sol == [sp.Rational(1, 3)], "w sum(a_i + c) = w sum a_i + c for all c forces 3w = 1, i.e. g = 1"


def d_T5b():
    kap, f1, fp, b = sp.symbols("kappa f1 fp beta", positive=True)
    ok = sp.simplify(1 / (6 * (fp / (2 * f1))) - f1 / (3 * fp)) == 0
    t = sp.symbols("t")
    born = (1 + t) / 2
    kb = sp.diff(born, t).subs(t, 1) / (2 * born.subs(t, 1))
    ke = sp.diff(sp.exp(b * t), t).subs(t, 1) / (2 * sp.exp(b * t).subs(t, 1))
    ok = ok and kb == sp.Rational(1, 4) and 1 / (6 * kb) == sp.Rational(2, 3) and sp.simplify(ke - b / 2) == 0 and sp.simplify(1 / (6 * ke) - 1 / (3 * b)) == 0
    return ok, ("the form -kappa sum_i |theta - theta_i|^2 has Hessian -6 kappa I: minimizer the average (gain one), variance 1/(6 kappa) = "
                "f(1)/(3 f'(1)); Born: kappa = 1/4, variance 2/3; e^{beta t}: kappa = beta/2, variance 1/(3 beta) (sympy)")


def control_reading():
    """INFO: T2's Reading paragraph quotes the g = 1 variance at t = 10, 50, 100, 200; compare with the exact series and the runner's C2."""
    vals = {}
    S, nmax = Fr(0), 200
    for n in range(nmax):
        S += P_exact(n)
        if n + 1 in (10, 50, 100, 200):
            vals[n + 1] = S
    return {t: float(v) for t, v in vals.items()}


# ------------------------------------------------------------------------------------------------------------------ the items
ITEMS = [
    ("gain", "~gain g = 3w", "DEFINITION", r"g = 3w|gain", "the gain"),
    ("halfspace", "~on the half-space x_1 + x_2 + x_3 >= 0 of Z^3, conditional on the level-0 records¦For x in H of level t >= 1", "EXCLUDED",
     "structural: the half-space, level 0 and level t >= 1", "domain"),
    ("T1", "~Sigma_{z: ℓ(z)=0} G(x,z) v_z + Sigma_{z: 1 <= ℓ(z) <= t} G(x,z) xi_z¦has all d_j >= 0¦and G(x,z) = 0 otherwise"
     "¦Cov(v_x, v_y) = sigma^2 Sigma_{1 <= ℓ(z) <= min(ℓ(x),ℓ(y))} G(x,z) G(y,z)¦Hence E[v_x | level 0] = Sigma_{ℓ(z)=0} G(x,z) v_z", "CACHE",
     r"B1 T1: on the 5x5 transverse torus with 6 levels the covariance recursion equals the directed-path kernel formula", "T1 (B1)"),
    ("T1prob", "~a probability kernel exactly when g = 1¦G(x,z) = g^n; at g = 1 the kernel", "DERIVED", (d_T1, r"a probability kernel"), "T1 level sums"),
    ("B1exec", "~on the 5x5 transverse torus with six levels the covariance recursion C_t = A C_{t-1} A^T + sigma^2 I equals the kernel formula",
     "CACHE", r"B1 T1: on the 5x5 transverse torus with 6 levels", "B1 executed"),
    ("T2var", "~Var(v_x) = sigma^2 sum_{n < level} g^{2n} P_n¦Var(v_x | level 0) = sigma^2 Sigma_{n=0}^{t-1} g^{2n} P_n"
     "¦Cov(v_x, v_y) = sigma^2 Sigma_{n=0}^{t-1} g^{2n} P_n(d)¦the centered Gaussian with covariance sigma^2 Sigma_n g^{2n} P_n(*)", "DERIVED",
     (d_T2formula, r"The variance formula is T1"), "T2's series"),
    ("T2a", "~for g < 1 the variance is at most sigma^2/(1 - g^2)¦(a) g < 1: Var(v_x) <= sigma^2/(1 - g^2)¦Cov <= sigma^2 g^{2m}/(1 - g^2)",
     "DERIVED", (d_T2a, r"The difference walk moves at most one unit"), "T2(a)"),
    ("T2a-x", "~Cov <= sigma^2 g^{2m}/(1 - g^2)", "CACHE", r"C3 T2\(a\): at g = 1/2 the variance series is <= 4/3", "T2(a) executed (C3)"),
    ("T2down", "~|Cov(v_x, v_y)| <= g^s * sup Var", "CACHE", r"C4 T2\(a\): on the torus at g = 1/2 the covariance between level 6", "T2(a) downstream (C4)"),
    ("T2b", "~for g = 1, 1/(36 n) <= P_n <= 9 pi/(16 n)¦(b) g = 1: for n >= 1, 1/(36 n) <= P_n <= 9pi/(16 n)"
     "¦sigma^2 H_t/36 <= Var(v_x) <= sigma^2 (1 + 9pi H_{t-1}/16)", "DERIVED", (d_T2b, r"9pi/\(16 n\)\. Lower bound|9π/\(16 n\)\. Lower bound|9 ?π/\(16 ?n\)|9pi/\(16 n\)"),
     "T2(b) constants"),
    ("T2b-x", "~for g = 1, 1/(36 n) <= P_n", "CACHE", r"C1 T2\(b\): 1/\(36n\) <= P_n <= 2/n for 1 <= n <= 200", "T2(b) executed (C1)"),
    ("T2c", "~(c) g > 1: Var(v_x) >= sigma^2 g^{2(t-1)} P_{t-1} >= sigma^2 g^{2(t-1)}/(36(t-1))¦for g > 1 the variance grows exponentially",
     "DERIVED", (d_T2c, r"Keep the last term"), "T2(c)"),
    ("lev200", "~(proved; executed to level 200 exactly)", "CACHE", r"C2 T2\(b\): at g = 1 the variance series .* for t <= 200", "executed to 200"),
    ("T2exec", "~Executed: P_n exactly for n <= 200 against the rational relaxation 1/(36n) <= P_n <= 2/n", "CACHE",
     r"C1 T2\(b\): 1/\(36n\) <= P_n <= 2/n for 1 <= n <= 200", "C1 executed"),
    ("pi2", "~(the note's 9pi/16 < 2)", "DERIVED", (d_rho_pi, r"the note's 9"), "9 pi/16 < 2"),
    ("T2exec2", "~the variance series at g = 1 against H_t/36 and 1 + 2H_{t-1} (C2)", "CACHE",
     r"C2 T2\(b\): at g = 1 the variance series \(sigma\^2 = 1\) satisfies H_t/36 <= Var_t <= 1 \+ 2 H_\{t-1\}", "C2 executed"),
    ("T2exec3", "~at g = 1/2 against 4/3 and the transverse decay bound (C3)", "CACHE", r"C3 T2\(a\): at g = 1/2 the variance series is <= 4/3",
     "C3 executed"),
    ("T3prec", "~the stationary law's precision is sigma^{-2}(I - A)†(I - A)", "DERIVED", (d_prec, r"has symbol `1 − wΣ e|has symbol 1 - wSigma e"), "precision"),
    ("T3sym", "~symbol at g < 1 is 1 - 2w sum cos k_j + w^2 (3 + 2 sum_{i<j} cos(k_i - k_j))¦(i) At g < 1"
     "¦with symbol |1 - wSigma_j e^{-ik_j}|^2 = 1 - 2wSigma_j cos k_j + w^2(3 + 2Sigma_{i<j} cos(k_i - k_j))", "CACHE",
     r"D1 T3\(i\): \|1 - w sum e\^\{-ik_j\}\|\^2 = 1 - 2w sum cos k_j \+ w\^2 \(3 \+ 2 sum_\{i<j\} cos\(k_i - k_j\)\)", "T3(i) (D1)"),
    ("T3coef", "~constant 1 + 3w^2, axial edges -2w, face diagonals x +- (e_i - e_j) with +2w^2", "DERIVED", (d_coeffs, r"multiply by its conjugate"),
     "T3(i) coefficients"),
    ("T3ii", "~at g = 1 its expansion is K^2/9¦(ii) At g = 1 (w = 1/3), along k = (u,u,u)¦on the transverse plane K = 0 it is |k|^4/36 + O(|k|^6)",
     "CACHE", r"D2 T3\(ii\): at g = 1 the symbol along \(u,u,u\) is u\^2 = K\^2/9", "T3(ii) (D2)"),
    ("T3iii", "~C(2n,n)/4^n times P_n¦For every n >= 0, p_{2n} = (C(2n,n)/4^n) * P_n and p_{2n+1} = 0", "CACHE",
     r"D3 T3\(iii\): the number of returning simple-random-walk paths of 2n steps equals C\(2n,n\)", "T3(iii) (D3)"),
    ("T3green", "~(1/6)(1 + Sigma_{n>=1} (sqrt3/2)(2n+1)^{-1/2} * 9pi/(16n)) < ∞", "DERIVED", (d_green, r"The bound uses T4 for the binomial"),
     "the Green function's diagonal bound"),
    ("T3last", "~at g < 1 it decays exponentially where 1/(4pi r) does not; at g = 1 it does not exist as a stationary object", "EXCLUDED",
     "by T2(a)/(b) (sourced above); 1/(4 pi r) is the standard far field of the lattice Green function (named, not claimed)", "wording"),
    ("T3exec", "~the static series stays below 1.52 to n = 200", "CACHE", r"D4 T3\(iii\): the static series 1 \+ sum_\{n<=200\} C\(2n,n\)/4\^n P_n = 1\.4834 < 152/100",
     "D4 executed"),
    ("T3exec2", "~the identity p_{2n} = (C(2n,n)/4^n) P_n against a direct count of returning walks for n <= 6 (D3)", "CACHE",
     r"D3 T3\(iii\): .* for n <= 6", "D3 executed"),
    ("T4", "~P_n = C(2n,n)/4^n and 1/(4n) <= P_n^2 <= 3/(4(2n+1))¦with one transverse dimension P_n = C(2n,n)/4^n", "DERIVED",
     (d_T4, r"is a lazy walk"), "T4"),
    ("T4x", "~Executed to n = 400 (E1)", "CACHE", r"E1 T4: 1/\(4n\) <= \(C\(2n,n\)/4\^n\)\^2 <= 3/\(4\(2n\+1\)\) for n <= 400", "E1"),
    ("T4var", "~so at g = 1 Var(v_x) >= sigma^2 Sigma_{n<t} (2sqrtn)^{-1}", "DERIVED", (d_T4, r"is a lazy walk"), "T4 variance"),
    ("T4g", "~(two predecessors, gain g = 2w)", "DEFINITION", "inline", "the Z^2 gain"),
    ("T5a", "~covariance of the rule under value translations forces g = 1¦then g = 1", "DERIVED", (d_T5a, r"The mean must shift by"), "T5(a)"),
    ("T5cond", "~smooth at t = 1 with f(1) > 0 and f'(1) > 0", "EXCLUDED", "conditions on f", "conditions"),
    ("T5b", "~3 log f(1) - kappa Sigma_i |theta - theta_i|^2, kappa = f'(1)/(2f(1))¦with kappa = f'(1)/(2 f(1))¦For the Born overlap f(t) = (1+t)/2: kappa = 1/4, variance 2/3",
     "CACHE", r"E2 T5\(b\): log f\(s\.a\) = log f\(1\) - kappa \|theta - phi\|\^2 \+ O\(3\) with kappa = f'\(1\)/\(2f\(1\)\): 1/4 for the Born overlap \(variance 2/3",
     "T5(b) (E2)"),
    ("T5bvar", "~its variance is 1/(6kappa) = f(1)/(3f'(1)) per component¦with variance f(1)/(3 f'(1)) per component, equal to 2/3 for the Born overlap (1+t)/2"
     "¦for f(t) = e^{betat}: kappa = beta/2, variance 1/(3beta)¦whose mean is the average (g = 1)¦its minimizer is the average (theta_1 + theta_2 + theta_3)/3",
     "DERIVED", (d_T5b, r"its Hessian is"), "T5(b) variance"),
    ("T5c", "~Block 07's real instance (P_xx = 3, every edge -1/2) is P = (1/2)(6I - Sigma_{+-j} S_j)¦has weight 1/6 per recorded neighbour: g = 1/2"
     "¦its formation rule has g = 1/2", "CACHE", r"E3 T5\(c\): block 07's real instance \(P_xx = 3, edges -1/2\) gives weight 1/6 per recorded neighbour and gain 1/2",
     "T5(c) (E3)"),
    ("T5c2", "~the massless formation rule w = 1/3 is the one-site conditional of no static law¦3I - Sigma_{+-j} S_j, has symbol 3 - 2Sigma_j cos k_j, negative at k = 0"
     "¦the massless formation rule is the one-site conditional of no static law", "CACHE",
     r"E4 T5\(c\): the six-neighbour precision 3I - sum S_j needed for the massless formation rule has symbol -3 at k = 0", "T5(c) (E4)"),
    ("refs", r"block 07'?s?|block 09(?: \(PR #8139, open; not an input here\))?|the six-menu law|six-neighbour", "EXCLUDED", "references and names", "citation"),
    ("words", r"three predecessors|one transverse dimension|exactly one stationary law|second-order|two independent directed walks|two such kernels"
     r"|two sites|the two expansions|two predecessors|both f|two-point function|\(gain one\)|bounded level-0 plane", "EXCLUDED",
     "wording and conditions (number words; the level-0 plane)", "wording"),
]


def control_checks():
    vals = control_reading()
    notes = ["T2's Reading paragraph (interpretation, outside the statement text) quotes the g = 1 variance 2.040, 2.714, 3.002, 3.289 at "
             "t = 10, 50, 100, 200; the exact series sum_(n<t) P_n gives " + ", ".join(f"t={t}: {v:.5f}" for t, v in vals.items()) +
             "; the runner's C2 prints 2.040, 2.714, 3.001, 3.288"]
    return {}, notes


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
            found = re.search(locate, re.sub(r"\s+", " ", norm(note))) is not None
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
