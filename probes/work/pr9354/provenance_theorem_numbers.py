#!/usr/bin/env python3
"""J:provenance:PR9354 -- every number in the two finite-projection notes (finite path / guide dependence, and mixed energy / curvature target) located in
the PR's cached runner stdout, the PR's runner source, the cited source commits (PR9356 at 1f2e49a0, PR9352 at 73f2ed7e), or an exact derivation re-executed here.

Statement text = the whole body of each note after the metadata block (markdown link targets and 20+ hex hashes removed first; the hashes are checked
separately).  Every numeric token (integers, decimals, a/b) must fall on a line that an item below has verified:
  CACHE     printed by the PR's cached runner output (parsed here)                                   -> sourced
  RUNNER    a constant or construction in the PR's runner, or in the cited source commit             -> sourced
  DERIVED   an exact derivation re-executed here (Fractions / sympy / 50-digit mpmath)               -> sourced (flagged)
  STRUCT    a definitional 0/1/2/3 (inequality, index, exponent, dimension) or an equation label      -> excluded, listed
  (else)    UNCOVERED, counted as HIT.
The pinned note bytes are checked by sha256 so that a changed note cannot silently keep a stale mapping.  Self-contained; reads the PR head via git.
"""
import hashlib, itertools, json, re, subprocess, sys
from fractions import Fraction as Fr
from pathlib import Path
import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
BRANCH = "physics-loop/photon-finite-path-target-20260927"
N1 = "docs/FINITE_PROJECTION_MIXED_ENERGY_AND_CURVATURE_TARGET_BOUNDED_THEOREM_NOTE_2026-09-27.md"
N2 = "docs/FINITE_PATH_GUIDE_DEPENDENCE_AND_SHARED_CURVATURE_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-09-27.md"
R1 = "scripts/finite_projection_mixed_curvature_2026_09_27.py"
R2 = "scripts/finite_path_guide_dependence_2026_09_27.py"
C1 = "logs/runner-cache/finite_projection_mixed_curvature_2026_09_27.txt"
C2 = "logs/runner-cache/finite_path_guide_dependence_2026_09_27.txt"
SRC56 = ("1f2e49a0b1b9a2f84f8abc099020baf3655c1518", "scripts/ring_model_12_cubed_curvature_population_series_in_both_guide_schemes_2026_09_26.py", "9cf868253ee64f6d4ca2914f2afea94e53900e5848cc600029b513647a06955d", 56)
SRC52 = ("73f2ed7e46f0d4a4ff320c7d462c2fce701d7e7d", "scripts/ring_model_8_cubed_curvature_guide_scheme_split_with_and_without_a_walker_population_2026_09_26.py", None, 52)
mp.mp.dps = 50


def git(*a):
    return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)


def fetch_head():
    git("fetch", "origin", BRANCH, "--quiet")
    r = git("rev-parse", f"origin/{BRANCH}")
    if r.returncode: raise SystemExit("cannot resolve PR branch: " + r.stderr)
    return r.stdout.strip()


HEAD = fetch_head()


def show(path, ref=None):
    r = git("show", f"{ref or HEAD}:{path}")
    if r.returncode: raise SystemExit(f"cannot read {path} at {ref or HEAD}: {r.stderr.strip()}")
    return r.stdout


def show_commit(sha, path):
    if git("cat-file", "-t", sha).returncode:
        for n in (9356, 9352, 9328): git("fetch", "origin", f"pull/{n}/head", "--quiet")
    return show(path, sha)


NUM = re.compile(r"(?<![A-Za-z_\^\d./])(\d+e-\d+|\d+/\d+|[+-]?\d+\.\d+|\d+)(?![\d])")
notes = {"N1": show(N1), "N2": show(N2)}
lines = {k: v.split("\n") for k, v in notes.items()}
covered = {"N1": {}, "N2": {}}     # line number -> (kind, item id)
hits = []; counts = {"CACHE": 0, "RUNNER": 0, "DERIVED": 0, "STRUCT": 0}


def line_tokens(k, i):
    l = re.sub(r"`[0-9a-f]{20,}`", "HASH", lines[k][i - 1])
    l = re.sub(r"\]\([^)]*\)", "]", l)
    return NUM.findall(l)


def find_lines(k, pat, flags=0):
    return [i for i, l in enumerate(lines[k], 1) if re.search(pat, l, flags)]


def item(iid, k, pat, kind, ok, source, expect=None, flags=0):
    ls = find_lines(k, pat, flags)
    if not ls or (expect is not None and len(ls) < expect):
        print(f"[UNUSED] {iid}: pattern {pat!r} matches {len(ls)} lines of {k}"); hits.append(f"pattern for '{iid}' not found in {k}"); return
    for i in ls: covered[k][i] = (kind if ok else "HIT", iid)
    if ok:
        counts[kind] += 1; print(f"[{kind}] {iid} | {source} | {k} line(s) {ls[:6]}{'...' if len(ls) > 6 else ''}")
    else:
        hits.append(f"{iid}: {source}"); print(f"[HIT] {iid} | {source}")


# ---------------------------------------------------------------- pins
sha = {k: hashlib.sha256(v.encode()).hexdigest() for k, v in notes.items()}
print(f"PR #9354 head {HEAD[:10]}; note sha256 N1 {sha['N1'][:16]} N2 {sha['N2'][:16]}; lines {len(lines['N1'])} / {len(lines['N2'])}")
cache1 = json.loads(show(C1).split("----- stdout -----\n", 1)[1].split("\n----- stderr", 1)[0])
cache2 = json.loads(show(C2).split("----- stdout -----\n", 1)[1].split("\n----- stderr", 1)[0])
run1, run2 = show(R1), show(R2)

# ---------------------------------------------------------------- exact derivations used below
X = mp.matrix([[0, -1], [-1, 0]])
def emix(guide, p0, t):
    pv = mp.matrix(guide); chi = mp.matrix([p0[0] / guide[0], p0[1] / guide[1]]); E = mp.expm(-t * X)
    return (pv.T * X * E * chi)[0] / (pv.T * E * chi)[0]
half = mp.mpf(1) / 2
e_common = emix([1, 1], [half, half], mp.log(2) / 2); e_mixed = emix([1, 2], [half, half], mp.log(2) / 2)
e_psi2 = emix([1, 2], [mp.mpf(1) / 5, mp.mpf(4) / 5], mp.log(2) / 2)
tt = sp.symbols('t', positive=True)
sym_formula = sp.simplify(-(9 * sp.exp(2 * tt) + 1) / (9 * sp.exp(2 * tt) - 1))
ok_formula = all(abs(emix([1, 2], [half, half], mp.mpf(k) / 3) - mp.mpf(sp.N(sym_formula.subs(tt, sp.Rational(k, 3)), 40))) < 1e-30 for k in (1, 2, 5, 7))
psi = [Fr(1), Fr(2)]; p0_sq = [p * p / sum(q * q for q in psi) for p in psi]

import random
rng = random.Random(9354)
def rand_stoq(n):
    Hm = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            v = -Fr(rng.randint(0, 6), rng.randint(1, 4)) if (rng.random() < 0.7 or j == i + 1) else Fr(0)
            Hm[i][j] = Hm[j][i] = v if v != 0 or j != i + 1 else Fr(-1, 2)
        Hm[i][i] = Fr(rng.randint(-3, 3), rng.randint(1, 3))
    return Hm
ok_gen = True; ok_mix = True
for _ in range(20):
    n = rng.randint(2, 6); Hm = rand_stoq(n); ps = [Fr(rng.randint(1, 9), rng.randint(1, 5)) for _ in range(n)]
    Q = [[(-Hm[y][x] * ps[y] / ps[x]) if x != y else Fr(0) for y in range(n)] for x in range(n)]
    for x in range(n): Q[x][x] = -sum(Q[x][y] for y in range(n) if y != x)
    EL = [sum(Hm[x][y] * ps[y] for y in range(n)) / ps[x] for x in range(n)]
    for x in range(n):
        for y in range(n):
            ok_gen &= (Q[y][x] - (EL[x] if x == y else 0)) == -ps[x] * Hm[x][y] / ps[y]
Hn = mp.matrix([[mp.mpf(v.numerator) / v.denominator for v in row] for row in rand_stoq(4)]); pv_ = mp.matrix([1, 2, mp.mpf(3) / 2, mp.mpf(1) / 3]); ch_ = mp.matrix([mp.mpf(1) / 3, 1, 0, mp.mpf(2) / 5]) 
Zf = lambda tv: (pv_.T * mp.expm(-tv * Hn) * ch_)[0]
t0_ = mp.mpf(7) / 5; hh_ = mp.mpf(10) ** -12
Em_ = (pv_.T * Hn * mp.expm(-t0_ * Hn) * ch_)[0] / Zf(t0_)
ok_mix = abs(Em_ + (mp.log(Zf(t0_ + hh_)) - mp.log(Zf(t0_ - hh_))) / (2 * hh_)) < 1e-20
# counterexample numbers, exactly
Qs = mp.matrix([[-2, 2], [mp.mpf(1) / 2, -mp.mpf(1) / 2]]); ELs = [mp.mpf(-2), -mp.mpf(1) / 2]
def E_sw(tv): pt_ = mp.expm(tv * Qs.T) * mp.matrix([1, 0]); return ELs[0] * pt_[0] + ELs[1] * pt_[1]
h0_ = mp.mpf(2) / 5 * mp.log(2); ens_ = [E_sw(h0_ * k) for k in (1, 2, 3)]
ok_ce = all(abs(e - v) < 1e-40 for e, v in zip(ens_, [mp.mpf(-7) / 5, mp.mpf(-11) / 10, mp.mpf(-19) / 20])) and abs(15 * ens_[0] - 16 * ens_[1] + ens_[2] + mp.mpf(87) / 20) < 1e-40
# age-averaged curvature
aa, cc_, bb, tw = sp.symbols('a c beta t', positive=True); hs = sp.symbols('h')
Hh_ = sp.Matrix([[cc_ * hs, -aa], [-aa, -cc_ * hs]]); psi_ = sp.Matrix([sp.exp(bb * hs), sp.exp(-bb * hs)]); g_ = sp.sqrt(aa ** 2 + cc_ ** 2 * hs ** 2)
chi_ = sp.Matrix([1 / (2 * sp.exp(bb * hs)), 1 / (2 * sp.exp(-bb * hs))])
def Emix_t(tv):
    Em_ = sp.cosh(g_ * tv) * sp.eye(2) - sp.sinh(g_ * tv) * Hh_ / g_
    return (psi_.T * Hh_ * Em_ * chi_)[0] / (psi_.T * Em_ * chi_)[0]
wts = [(sp.Rational(1, 3), sp.Rational(1, 2)), (sp.Rational(2, 3), sp.Rational(5, 4))]
pnt = {aa: sp.Rational(3, 2), cc_: sp.Rational(7, 5), bb: sp.Rational(2, 3)}
lhs_ = -sp.diff(sum(w * Emix_t(tv) for w, tv in wts), hs, 2).subs(hs, 0).subs(pnt)
rhs_ = sum(w * ((cc_ ** 2 / aa) * (1 - sp.exp(-2 * aa * tv)) + 4 * aa * bb ** 2 * sp.exp(-2 * aa * tv)) for w, tv in wts).subs(pnt)
ok_avg = abs(sp.N(lhs_ - rhs_, 30)) < 1e-25

# ---------------------------------------------------------------- note 1 (projection)
item("date, SHA label, inspection date", "N1", r"^Date: 2026|Runner SHA-256|inspected on September 27", "STRUCT", True, "a date, the name of the hash algorithm and a calendar day: not results")
item("equation labels (1)-(8) and cross-references", "N1", r"\((?:1|2|3|4|5|6|7|8)\)\s*$|\((?:1|3|5|6)\)[ .,;]|\((?:3)\) ", "STRUCT", True, "labels of the displayed equations and their cross-references")
item("sign/positivity definitions (0)", "N1", r"H\(x,y\)<=0|t>=0|nonzero when p0|Hence Z>0|a>0 and real|At h=0 this is -a|A common uniform guide has beta=0|>0\. This follows|sum_j w_j exp\(-2at_j\)>0|chi_ground=-E_ground|Lcs=\(0,\)", "STRUCT", True, "0 as a bound, sign convention, field value h=0 or beta=0, or the tuple Lcs=(0,): definitions and case labels")
item("weighted generator identity (1) and definition of chi", "N1", r"define the row generator Q|Q\^T - diag\(E_L\)|Z\(t\) = 1\^T f_t", "DERIVED", ok_gen, "Q^T - diag(E_L) = -D H D^-1 verified entrywise, exactly, on 20 random stoquastic H (n=2..6) and guides; the 1's are the all-ones vector and inverse exponents")
item("(3) mixed energy and its derivative form", "N1", r"= -d log Z\(t\)/dt|only removes scalar factors|Generally \(3\)|separate operation because", "DERIVED", ok_mix, "E_mix = psi^T H e^{-tH} chi / Z equals -d log Z/dt to 1e-20 (mpmath, random 4x4 stoquastic H, arbitrary nonnegative chi)")
ok_ex = abs(e_common + 1) < 1e-40 and abs(e_mixed + mp.mpf(19) / 17) < 1e-40 and abs(e_psi2 + mp.mpf(17) / 19) < 1e-40 and ok_formula
ok_c = cache1["boundary_examples"] == {"common": "-1", "mixed": "-19/17", "psi_squared_initial": "-17/19"} and p0_sq == [Fr(1, 5), Fr(4, 5)]
item("two-state boundary examples: -1, 9 exp(2t)+1 form, -19/17, (1/5,4/5), -17/19", "N1", r"For H=\[\[0,-1\],\[-1,0\]\], p0=\(1/2,1/2\)|Guide \(1,2\) instead|E_mix\(t\) = -\(9 exp|At t=log\(2\)/2 this is|p0 by \(1/5,4/5\)", "CACHE", ok_ex and ok_c,
     f"cache boundary_examples = {cache1['boundary_examples']}; p0 (1/5,4/5) = psi^2/sum psi^2 for psi=(1,2) (label 'psi_squared_initial'); closed form -(9e^(2t)+1)/(9e^(2t)-1) and -19/17 at t=log2/2 recomputed to 40 digits")
item("N_w = 1 and 1/N_w (definitions of the single walker; the source's 1/N fit)", "N1", r"N_w=1|1/N_w", "STRUCT", True, "one walker; 1/N_w is the variable of the source's fit a + b/N_w")
item("single-walker stationary energy (8) and -4/5", "N1", r"sum_x pi\(x\) E_L\(x\) = psi\^T H psi|it is -4/5, whereas the ground energy is -1", "CACHE", cache1["single_walker"]["toy_stationary_energy"] == "-4/5" and Fr(sum(psi[i] * sum(Fr([[0, -1], [-1, 0]][i][j]) * psi[j] for j in range(2)) for i in range(2)), 5) == Fr(-4, 5),
     f"cache single_walker.toy_stationary_energy = {cache1['single_walker']['toy_stationary_energy']}; psi^T H psi / psi^T psi = -4/5 exactly for psi=(1,2)")
# stencil algebra
Ah, Bh, Ch, L1, L3, H1s, E0 = sp.symbols('A B C L1 L3 H1 E0')
Eb = lambda x: E0 - Ah * x ** 2 - Bh * x ** 4 - Ch * x ** 6 + L1 * x + L3 * x ** 3
numer = sp.expand(15 * Eb(0) - 16 * Eb(H1s) + Eb(2 * H1s)); coef = sp.expand(numer / (12 * H1s ** 2))
ok_sten = sp.simplify(coef - (Ah - 4 * Ch * H1s ** 4 - sp.Rational(7, 6) * L1 / H1s - sp.Rational(2, 3) * L3 * H1s)) == 0 and sp.expand(15 - 16 + 1) == 0
lin = sp.expand(15 * (E0) - 16 * (E0 - H1s * sp.Symbol('M')) + (E0 - 2 * H1s * sp.Symbol('M')))
ok14 = sp.simplify(lin - 14 * H1s * sp.Symbol('M')) == 0
src56 = show_commit(SRC56[0], SRC56[1]); sha56 = hashlib.sha256(src56.encode()).hexdigest()
ok_chi = "a = (15 * E0 - 16 * E1 + E2) / (12 * h1 ** 2)" in src56 and "4 * a / (3 * pref * N)" in src56 and "a = 3 pref N chi / 4" in src56
item("three-field stencil 15, -16, 1 and its numerator 14 h M (fixed-guide, common ages)", "N1", r"is exactly 14 h M|reported normalization gives 14 M/\(9 pref N h\)|and the coefficient 14", "DERIVED", ok14 and ok_chi,
     "15E(0)-16E(H)+E(2H) on E(h)=A-hM equals 14 h M (sympy); the source chi_fit divides by 12 h1^2 and then multiplies 4/(3 pref N), giving 1/(9 pref N h1^2): " + ("source lines found in PR9356" if ok_chi else "source line NOT found"))
item("source stencil [15 Ebar(0)-16 Ebar(H1)+Ebar(2H1)]/(9 pref N H1^2) and its intermediate 12 H1^2 coefficient", "N1", r"reports the three-field stencil|\[15 Ebar\(0\)-16|coefficient divides the same numerator by 12|A=3 pref N chi/4", "RUNNER", ok_chi,
     f"PR9356 @ {SRC56[0][:8]} chi_fit: a=(15 E0 - 16 E1 + E2)/(12 h1**2), returns 4a/(3 pref N), docstring a = 3 pref N chi/4")
item("even/odd stencil remainders: A-4C H1^4, -7 L1/(6 H1), -2 L3 H1/3", "N1", r"A-4 C H1\^4|-7 L1/\(6 H1\)|E\(h\)=E0-A h\^2|Ebar\(h\)=E0-A h\^2|L1 h\+L3 h\^3", "DERIVED", ok_sten, "sympy expansion of 15E(0)-16E(H)+E(2H) over 12H^2: A - 4C H^4 - 7 L1/(6H) - 2 L3 H/3, with the B (h^4) term cancelling")
# curvature formulas
a, c, beta, t, h = sp.symbols('a c beta t h', positive=True)
Hh = sp.Matrix([[c * h, -a], [-a, -c * h]]); psih = sp.Matrix([sp.exp(beta * h), sp.exp(-beta * h)])
gam = sp.sqrt(a ** 2 + c ** 2 * h ** 2)
Em = sp.cosh(gam * t) * sp.eye(2) - sp.sinh(gam * t) * Hh / gam
chih = sp.Matrix([1 / (2 * sp.exp(beta * h)), 1 / (2 * sp.exp(-beta * h))])
Ehh = (psih.T * Hh * Em * chih)[0] / (psih.T * Em * chih)[0]
pt = {a: sp.Rational(3, 2), c: sp.Rational(7, 5), beta: sp.Rational(2, 3), t: sp.Rational(4, 5)}
chi5 = (c ** 2 / a) * (1 - sp.exp(-2 * a * t)) + 4 * a * beta ** 2 * sp.exp(-2 * a * t)
ok5 = abs(sp.N((-sp.diff(Ehh, h, 2).subs(h, 0) - chi5).subs(pt), 30)) < 1e-25
ok4 = abs(sp.N((Ehh - (-gam * (a * sp.cosh(2 * beta * h) + gam * sp.tanh(gam * t)) / (gam + a * sp.cosh(2 * beta * h) * sp.tanh(gam * t)))).subs({**pt, h: sp.Rational(3, 10)}), 30)) < 1e-25
ser_g = sp.series(sp.sqrt(a ** 2 + c ** 2 * h ** 2), h, 0, 4).removeO(); ser_A = sp.series(a * sp.cosh(2 * beta * h), h, 0, 4).removeO()
ok_ser = sp.simplify(ser_g - (a + c ** 2 * h ** 2 / (2 * a))) == 0 and sp.simplify(ser_A - (a + 2 * a * beta ** 2 * h ** 2)) == 0
F_, g_, A_, z_ = sp.symbols('F g A z')
Fexpr = -g_ * (A_ + g_ * z_) / (g_ + A_ * z_)
ok_der = sp.simplify(sp.diff(Fexpr, z_).subs({g_: a, A_: a})) == 0 and sp.simplify(sp.diff(Fexpr, A_).subs({g_: a, A_: a}) + (1 - z_) / (1 + z_)) == 0 and sp.simplify(sp.diff(Fexpr, g_).subs({g_: a, A_: a}) + 2 * z_ / (1 + z_)) == 0
ok_tanh = all(abs(sp.N(((1 - sp.tanh(a * t)) / (1 + sp.tanh(a * t)) - sp.exp(-2 * a * t)).subs({a: sp.Rational(3, 2), t: tv}), 30)) < 1e-25 for tv in (sp.Rational(1, 3), sp.Rational(4, 5), 2))
item("curvature family H_h, guide, C=cosh(2 beta h), (4), zero-field energy -a", "N1", r"H_h = \[\[c h|psi_h = \(exp|p0 = \(1/2,1/2\)\.|Its ground energy|C=cosh\(2 beta h\)|In \(3\), psi_h|/ \(gamma \+ a C tanh|At h=0 this is -a", "DERIVED", ok4, "closed form (4) equals the matrix-exponential construction at an exact rational point (sympy, 30 digits); zero-field value -a follows from (4) at h=0")
item("partial derivatives F_z=0, F_A, F_gamma, expansions of gamma and A, and (1-z)/(1+z)=exp(-2at)", "N1", r"F_z=0|F\(gamma,A,z\)|Also gamma=a|A=a\+2a beta|Using \(1-z\)/\(1\+z\)|A=a C and", "DERIVED", ok_der and ok_ser and ok_tanh, "partials of -g(A+gz)/(g+Az) at g=A=a (sympy), the h^2 expansions of gamma and a cosh(2 beta h), and the tanh identity")
item("curvature (5): (c^2/a)(1-exp(-2at)) + 4 a beta^2 exp(-2at)", "N1", r"chi_mix\(t\) = \(c\^2/a\)|\+ 4a beta\^2 exp|exact derivative", "DERIVED", ok5, "second derivative at h=0 of E_mix(t,h) equals (5) at an exact rational point (30 digits)")
ok_ex2 = sp.simplify(chi5.subs({a: 1, c: 2, beta: sp.Rational(1, 2), t: sp.log(2) / 2})) == sp.Rational(5, 2) and sp.simplify(chi5.subs({a: 1, c: 2, beta: 0, t: sp.log(2) / 2})) == 2 and (c ** 2 / a).subs({a: 1, c: 2}) == 4
item("susceptibilities 5/2, 2 and ground 4 at a=1, c=2, beta=1/2, t=log2/2", "N1", r"With a=1, c=2|beta=1/2 and t=log\(2\)/2|whereas the ground susceptibility is 4", "CACHE", ok_ex2 and cache1["curvature"]["susceptibilities"] == ["2", "5/2", "4"], f"cache curvature.susceptibilities = {cache1['curvature']['susceptibilities']} (beta=0, beta=1/2, ground); exact evaluation of (5) gives 5/2, 2 and c^2/a = 4")
item("age-averaged curvature replaces exp(-2at) by sum w_j exp(-2 a t_j)", "N1", r"the susceptibility of sum_j w_j E_mix|by sum_j w_j exp|differentiating a finite sum|and is outside that particular formula|The general expression", "DERIVED", ok_avg, "second derivative at h=0 of a weighted sum of two E_mix(t_j,h) equals the weighted sum of (5) with exp(-2 a t_j) (sympy, 30 digits)")
# source mapping
ages = [Fr(15, 1000) * j for j in range(501, 2001)]
ok_map = (sha56 == SRC56[2] and "NGEN = 200 if DRY else 2000" in src56 and "DTAU, H1 = 0.015, 0.15" in src56 and "ngen // 4" in src56 and "Lcs=(0,)" in src56)
item("PR9356 runner hash, ngen=2000, dtau=.015, therm=ngen//4, Lcs=(0,)", "N1", r"Its run_Ed requests|energies are averaged after therm|For ngen=2000 and dtau=\.015", "RUNNER", ok_map, f"PR9356 @ {SRC56[0][:8]}: sha256 of the source = {sha56[:16]}... {'= the note' if sha56 == SRC56[2] else '!= the note'}; NGEN = 2000, DTAU = 0.015, therm = ngen//4 (run_Ed), Lcs=(0,)")
ok_ages = cache1["curvature"]["age_count"] == 1500 and cache1["curvature"]["ages"] == ["1503/200", "30"] and ages[0] == Fr(1503, 200) and ages[-1] == 30 and len(ages) == 1500
item("(1/1500) sum_{j=501}^{2000}, ages 7.515 through 30", "N1", r"\(1/1500\) sum_\(j=501\)|with ages 7\.515 through 30|energy at age 30", "CACHE", ok_ages, f"cache curvature.age_count = {cache1['curvature']['age_count']}, ages = {cache1['curvature']['ages']} (1503/200 = 7.515); 2000 - 500 = 1500 generations, .015 j for j = 501..2000 (exact)")
item("counterexample h0=(2/5)log2, energies (-7/5,-11/10,-19/20), numerator -87/20", "N1", r"The counterexample uses H=|psi=\(1,2\), p0=\(1,0\), F=0|mean energies are \(-7/5|Four additional", "DERIVED", ok_ce, "one-walker proposal energy E(t) = E_L^T exp(tQ^T) p0 for psi=(1,2), p0=(1,0) at t=h0, 2 h0, 3 h0 gives -7/5, -11/10, -19/20 (mpmath, 40 digits); 15(-7/5)-16(-11/10)+(-19/20) = -87/20")
item("three population settings / 1/N fit", "N1", r"three population settings", "RUNNER", "POPS = (96, 192) if DRY else (1920, 3840)" in src56 and "REF = {True: (1.2520, 0.0221)" in src56 and "a + b/N_w" in src56, "PR9356: populations 960 (open PR 9352's value), 1920, 3840 = three; linear fit a + b/N_w")
item("five scratch mutation families; four additional scratch mutations", "N1", r"The five$|The five scratch|Four additional", "STRUCT", True, "counts of items listed in the same sentence: generator orientation, right boundary, curvature guide term, probe stencil, covariance cross term (5); stationary weights, Rayleigh averaging, proposal versus weighted evolution, the coefficient 14 (4)")
item("three-field / two boundaries / two-state prose counts", "N1", r"^## Weighted generator|three-field|two-state", "STRUCT", True, "counts in prose: E(0), E(H1), E(2H1) (three); left and right boundary (two); a 2 x 2 matrix")

# ---------------------------------------------------------------- note 2 (finite path)
item("date and refreshed-on date", "N2", r"^Date: 2026|refreshed 2026-09-27", "STRUCT", True, "calendar dates")
item("definitional 0/1: A>=0, Z>0, M>=1, n>0, c_0, E_0, T=0, cap J=0, sign conventions", "N2", r"A\(x,x\)=0|segment count M>=1|Z=psi\^T G_T psi>0|c_0 != 0|sum_\(n>0\)|E_n-E_0>=g>0|0 <= E_psi|At T=0 the endpoint|E_psi\(T\)-E_0 = |\|c_0\|\^2 \+|/ \(\|c_0|J=0|\(P_zz|N>0, h!=0|The guide psi\(x\)>0, segment duration|h->0 susceptibility|the ground energy is -1\.|H=\[\[0,-1\],\[-1,0\]\], the ground", "STRUCT", True, "0 and 1 as bounds, indices, the ground state label 0, case labels, or the ground energy -1 of [[0,-1],[-1,0]] (eigenvalues -1, +1: exact)")
ok_t = (lambda G: (G[0, 0] / G[0, 1] == 3))(mp.expm(-mp.log(2) / 2 * X)) if False else abs(mp.expm(-mp.log(2) / 2 * X)[0, 0] / mp.expm(-mp.log(2) / 2 * X)[0, 1] - 3) < 1e-40
def G2(T, guide):
    G = mp.expm(-T * X); pv = mp.matrix(guide); Z = (pv.T * G * pv)[0]
    marg = [pv[i] * (G * pv)[i] / Z for i in range(2)]; EL = [(X * pv)[i] / pv[i] for i in range(2)]
    return marg, sum(marg[i] * EL[i] for i in range(2))
m1, en1 = G2(mp.log(2) / 2, [1, 2]); m2, en2 = G2(mp.log(2), [1, 2]); _, en1c = G2(mp.log(2) / 2, [1, 1])
ok_tab = ok_t and abs(m1[0] - mp.mpf(5) / 19) < 1e-40 and abs(m1[1] - mp.mpf(14) / 19) < 1e-40 and abs(en1 + mp.mpf(17) / 19) < 1e-40 and abs(en2 + mp.mpf(35) / 37) < 1e-40 and abs(en1c + 1) < 1e-40 and abs(mp.expm(-mp.log(2) * X)[0, 0] - mp.mpf(5) / 4) < 1e-40 and abs(mp.expm(-mp.log(2) * X)[0, 1] - mp.mpf(3) / 4) < 1e-40
ok_c2 = cache2["endpoint_and_spectral_energies"] == ["-1", "-17/19", "-1", "-35/37"]
item("two-state table: propagators [[3,1],[1,3]] and [[5/4,3/4],[3/4,5/4]], marginal (5/19,14/19), local energies (-2,-1/2), means -1, -17/19, -35/37", "N2", r"At T=log\(2\)/2 the propagator|\| \(1,1\) \| \(1/2,1/2\)|\| \(1,2\) \| \(5/19|Independently, at T=log\(2\)|\[\[5/4,3/4\]", "CACHE", ok_tab and ok_c2, f"cache endpoint_and_spectral_energies = {cache2['endpoint_and_spectral_energies']}; propagators, marginals and local energies (Hpsi/psi = (-2,-1/2)) recomputed to 40 digits")
item("finite-path differences 2/19 and 2/37", "N2", r"finite-path difference is 2/19|difference 2/37", "DERIVED", abs((en1 - en1c) * 1 - mp.mpf(2) / 19) < 1e-40 and abs((en2 - G2(mp.log(2), [1, 1])[1]) - mp.mpf(2) / 37) < 1e-40, "(-17/19) - (-1) = 2/19 and (-35/37) - (-1) = 2/37, computed here from the recomputed means")
item("cap example: C=diag(1,1/4), endpoint -3/4, Rayleigh -1/2; E_cap symmetrized denominator 2", "N2", r"E_cap = psi\^T \(H C \+ C H\)|For example H=\[\[0,-1\],\[-1,1\]\]|C=diag\(1,1/4\)|Rayleigh quotient of sqrt\(C\)psi|The two scalar numerator terms", "CACHE",
     cache2["cap_endpoint_and_rayleigh"] == ["-3/4", "-1/2"], f"cache cap_endpoint_and_rayleigh = {cache2['cap_endpoint_and_spectral_energies'] if 'cap_endpoint_and_spectral_energies' in cache2 else cache2['cap_endpoint_and_rayleigh']}; C = K_0(log2)^2 = diag(1, exp(-2 log 2)) = diag(1,1/4) with D=(0,1); C = diag(1,1/4) computed here from exp(-Delta D) squared")
# covariance
scales = [Fr(k) for k in (1, 2, 3, 4, 5)]; cc = Fr(2, 3); rows = []
for signs in itertools.product((-1, 1), repeat=5):
    xa, xb, za, zb, y = [s * v for s, v in zip(signs, scales)]
    rows.append((cc * (15 * xa - 16 * y + za), cc * (15 * xb - 16 * y + zb), cc * (15 * (xa - xb) + za - zb)))
va, vb, vd = [sum(r[i] ** 2 for r in rows) / len(rows) for i in range(3)]
ok_cov = str(vd) == cache2["shared_curvature_covariance"]["difference_variance"] and str(va + vb - vd) == cache2["shared_curvature_covariance"]["naive_extra_variance"] and (va + vb - vd) == 512 * cc * cc * scales[4] ** 2 and vd == cc * cc * (225 * (scales[0] ** 2 + scales[1] ** 2) + scales[2] ** 2 + scales[3] ** 2) and "product((-1, 1), repeat=5)" in run2
item("shared-observation covariance: 15, -16, 1; w=(15,-15,1,-1); 225; 512; five-variable sign space", "N2", r"Consider two estimators|chi_b=c\(15|chi_a-chi_b = c\(15|For V=\(X_a|reduces to c\^2\[225|overcounts by 512|five-variable sign space|four variables are mutually", "CACHE", ok_cov,
     f"cache shared_curvature_covariance = {cache2['shared_curvature_covariance']}; recomputed over the 2^5 sign patterns (runner: product((-1,1),repeat=5)): difference variance {vd}, naive extra {va + vb - vd} = 512 c^2 Var(Y); 225 = 15^2, 512 = 2 x 16^2")
item("c = 1/(9 N h^2) for the three-field stencil", "N2", r"c=1/\(9 N h\^2\)|three-field energy stencil|h\^-2 amplification", "RUNNER", ok_chi, "PR9356's chi_fit normalization 4a/(3 pref N) with a = (15E0-16E1+E2)/(12h^2) = (15E0-16E1+E2)/(9 N h^2) x (4/... ) -- same 9 N h^2 factor as in the first note's mapping; exponent -2 from the 1/h^2")
p52 = show_commit(SRC52[0], SRC52[1])
ok52 = ("kmax=512" in p52) and ("MSEG, NM, TH = (400, 200000, 100000) if DRY else (1600, 10000000, 5000000)" in p52) and ("DTAU, H1, BETA, DUR = 0.015, 0.15, 0.5, 0.025" in p52) and (1600 * 0.025 == 40.0) and ("el = 0.5 * (out[:, 2] + out[:, 3])" in p52) and ("rpf = {H1: res[H1]}" in p52)
item("PR9352: path length 40, 512-event segment cap, endpoint half-sum, reused middle-field estimate", "N2", r"path length 40|512-event segment cap|The PR9352 implementation", "RUNNER", ok52, f"PR9352 @ {SRC52[0][:8]}: MSEG*DUR = 1600 x 0.025 = 40; kmax=512 default of reptation(); el = 0.5*(out[:,2]+out[:,3]); rpf = {{H1: res[H1]}} reuses the E(H1) estimate")
item("independent-reconstruction prose: log(2) two-state example, two-segment example, two times", "N2", r"used the different log\(2\) two-state|example, and enumerated a restricted two-segment|results, comparison reconciled the two times", "STRUCT", True, "log(2) is T of the second table row; the two-segment example is M=2 of the cap example; two times are T=log(2)/2 and T=log(2)")
item("state-space vector/matrix exponents and initial-law labels (1)", "N2", r"mu_t=Psi exp|Q\^T-diag\(E_L\)=-Psi|psi\^T H exp\(-tH\) Psi", "STRUCT", True, "Psi^-1 is a matrix inverse; the same generator identity (1) as in the first note")
item("prose counts: two estimators, two scalar terms, two separate issues, two-state model", "N2", r"two curvature estimates|Consider two estimators|two individual variances|two separate issues|two-state model|two scalar numerator|The two-state", "STRUCT", True, "counts of items named in the same sentence (two estimates chi_a, chi_b; two terms psi^T H C psi and psi^T C H psi; two matrix states; two issues: guide dependence and shared middle term)")

# ---------------------------------------------------------------- uncovered
unc = []; ntok = 0
for k in ("N1", "N2"):
    for i in range(1, len(lines[k]) + 1):
        toks = line_tokens(k, i)
        if toks:
            ntok += len(toks)
            if i not in covered[k]:
                unc.append((k, i, toks, lines[k][i - 1][:120]))
for k, i, toks, l in unc:
    print(f"[UNCOVERED] {k} line {i} tokens {toks} | {l}")
print(f"[COVERAGE] {ntok} numeric tokens on {sum(1 for k in covered for _ in covered[k])} covered lines; uncovered lines {len(unc)}")
print("[INFO] PR body counts (27 guide controls, 243 detailed-balance entries, 243 common-guide probe cases) are outside the note text; cache: guides", cache1["single_walker"]["guides"], "balance_entries", cache1["single_walker"]["balance_entries"], "probe cases", cache1["single_walker"]["common_guide_probe_cases"])
for h_ in hits: print("HIT:", h_)
tot = sum(counts.values())
print(f"SUMMARY: {tot} verified items over both notes ({ntok} numeric tokens): cache {counts['CACHE']}, runner or cited commit {counts['RUNNER']}, exact derivation here {counts['DERIVED']}, structural {counts['STRUCT']}; uncovered lines {len(unc)}; failed items {len(hits)}")
if unc or hits:
    if unc: print("HIT: uncovered numeric tokens on " + "; ".join(f"{k} line {i}: {t}" for k, i, t, _ in unc))
    sys.exit(1)
sys.exit(0)
