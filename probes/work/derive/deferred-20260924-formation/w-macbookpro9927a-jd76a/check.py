"""check.py -- deferred-20260924-formation, first pass (worker w-macbookpro9927a-jd76a).

Exact checks (Fractions / sympy) for every finite claim of ATTEMPT.md, plus a re-check of the
recorded seeded Monte Carlo evidence (mc_evidence.out, produced by mc_evidence.py) and a small
independent seeded Monte Carlo.  The Monte Carlo parts are numerical evidence, not exact facts.
Run from the repository root:  python3 <this dir>/check.py
"""
import hashlib, json, math, os, re, subprocess, sys
from fractions import Fraction as Fr
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, cwd=HERE).stdout.strip()
FAILS = []; NOK = 0

def ok(name, cond, detail=""):
    global NOK
    if cond:
        NOK += 1
    else:
        FAILS.append(name); print(f"FAIL {name} {detail}")

def gshow(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, cwd=ROOT)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "origin", rev.split(":")[0], "--quiet"], capture_output=True, cwd=ROOT)
        r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, cwd=ROOT)
    return r.stdout

# ---------------------------------------------------------------- Q: pinned sources
HEAD = "e6ffae5b460b9ec0fd0d99c99f9784232bd225bd"; LANDED = "5efa36e7c357ae2a62ee586a5407f90982f6ded9"
NOTE = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_"
        "BRACKETED_AND_THE_NONLINEAR_LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
DIR = ".claude/science/physics-loops/admissibility-induced-law-20260906/"
b5 = json.load(open(os.path.join(ROOT, "probes/work/deferred-science-20260924/batch-05.json")))
srcs = [s for s in b5["sources"] if s["pr"] == 8178]
nver = sum(1 for s in srcs if hashlib.sha256(gshow(s["head"], s["path"])).hexdigest() == s["sha256"])
ok("Q1 all PR8178 deferred sources verify", nver == len(srcs) == 18, f"{nver}/{len(srcs)}")
rev = json.load(open(os.path.join(ROOT, "probes/work/deferred-science-20260924/review-unit5-v1.json")))
fin = [e for e in rev["original_dispositions"]["8178"] if e["final_path"] == NOTE][0]["final_sha256"]
note = gshow(LANDED, NOTE)
ok("Q2 canonical note at landing commit", hashlib.sha256(note).hexdigest() == fin == "407e07d95da723167ea96d1d7a7d564c5e17b830d4e6f3dd3482a175bf41ee55")
main_same = hashlib.sha256(gshow("origin/main", NOTE)).hexdigest() == fin
nt = note.decode()
for q in ["Thus the chosen noise variance is the aligned conditional variance, but the exact Cartesian mean gain is A(3beta), not one. A direction-normalized or strong-coupling approximation needs an additional argument; none is supplied here.",
          "This recurrence is a supplied linear comparator, not the exact finite-beta Cartesian mean linearization of the nonlinear sphere kernel.",
          "The listed samples neither prove size independence nor a limiting coefficient, an exact phase or a universal memory law.",
          'next_trace_action: "Establish a controlled connection to the nonlinear kernel before importing linear conclusions"',
          "Define S_L=sum_(n!=0)1/|n|^2 over representatives n_i in (-L/2,L/2], V_L=(sigma^2/L^2)sum_(k!=0)1/(1-u_k), and tau_L=L^2/sigma^2."]:
    ok("Q3 note quote", q in nt, q[:60])
rows = re.findall(r"^\| (\d+) \| (\d+) \| `[^`]*` \| `(\d+)` \| `([\d.]+)` \| `([\d.]+), ([\d.]+), ([\d.]+)` \| `[^`]*` \| `([\d.]+)` \|$", nt, re.M)
ok("Q4 six historical rows parsed", len(rows) == 6)
res = gshow(HEAD, DIR + "RESULTS_block34.md").decode(); chk = gshow(HEAD, DIR + "CHECKER_block34_findings.md").decode()
msd = gshow(HEAD, DIR + "specs/supervisor_control_block34_torus_msd.py").decode()
ok("Q5 frozen quotes", "tracking `1/|m|²` of the stationary magnetization within `3–8 %`" in res
   and 'the first quantitative target for "spin-wave theory as a theorem"' in res
   and "the nonlinear excess is a property of the coupling, not of the size (`L = 16` and `32` agree within errors), and tracks `1/|m|²`" in chk
   and "D_1 = MSD/(2 l) per transverse component" in msd)
f = {x["id"]: x for x in b5["findings"]}
ok("Q6 review findings", f["U5-R1"]["finding"] == "Gain-one recurrence is not the exact finite-beta Cartesian mean derivative."
   and f["U5-R3"]["class"] == "OVERCLAIM" and b5["prs"]["8178"]["claim_disposition"]["rejected_or_narrowed"] == ["U5-R1", "U5-R3", "U5-R8"])

# ---------------------------------------------------------------- V: von Mises-Fisher moments on the sphere
k, w, al, b, l = sp.symbols("kappa w alpha b ell", positive=True)
Z = sp.integrate(sp.exp(k * w), (w, -1, 1))
mom = [sp.simplify(sp.integrate(w**j * sp.exp(k * w), (w, -1, 1)) / Z) for j in range(4)]
Ak = sp.coth(k) - 1 / k
ok("V1 E w = A", sp.simplify((mom[1] - Ak).rewrite(sp.exp)) == 0)
ok("V2 E w^2 = 1 - 2A/k", sp.simplify((mom[2] - (1 - 2 * Ak / k)).rewrite(sp.exp)) == 0)
ok("V3 E w^3 = coth - 3/k + 6A/k^2", sp.simplify((mom[3] - (sp.coth(k) - 3 / k + 6 * Ak / k**2)).rewrite(sp.exp)) == 0)
T3 = mom[1] - mom[3] - Ak * (1 - mom[2])                         # E[(1-w^2)(w-A)]
ok("V4 third moment = 2/k - 6A/k^2 - 2A^2/k", sp.simplify((T3 - (2 / k - 6 * Ak / k**2 - 2 * Ak**2 / k)).rewrite(sp.exp)) == 0)
x = sp.symbols("x", positive=True)                                # x = 1/kappa, coth -> 1 (error e^{-2 kappa})
T3a = (2 * x - 6 * (1 - x) * x**2 - 2 * (1 - x)**2 * x)
ok("V5 third moment ~ -2/k^2 + 4/k^3", sp.expand(T3a) == -2 * x**2 + 4 * x**3)
qq, bet = sp.symbols("q beta", positive=True)                  # b(kappa) = A/kappa = (1-x)x up to e^{-2 kappa}
ratio = ((1 - x) * x).subs(x, 1 / (bet * (3 - qq / 2))) / ((1 - x) * x).subs(x, 1 / (3 * bet))
ok("V6 b(beta|S|)/sigma^2 -> 6/(6-q) = 1 + q/6 + O(q^2) at |S| = 3 - q/2", sp.simplify(sp.limit(ratio, bet, sp.oo) - 6 / (6 - qq)) == 0
   and sp.series(6 / (6 - qq), qq, 0, 2).removeO() == 1 + qq / 6)

# ---------------------------------------------------------------- P: projection of the vMF covariance off n
nv = sp.Matrix([0, 0, 1]); Sv = sp.Matrix([sp.sin(al), 0, sp.cos(al)]); I3 = sp.eye(3)
Cov = b * (I3 - Sv * Sv.T) + l * Sv * Sv.T
ok("P1 tr[(I-nn^T)Cov] = b(1+c^2) + l(1-c^2)", sp.simplify(((I3 - nv * nv.T) * Cov).trace() - (b * (1 + sp.cos(al)**2) + l * sp.sin(al)**2)) == 0)
ok("P2 (I-nn^T)Cov n = -(b-l) c S_perp", sp.simplify((I3 - nv * nv.T) * Cov * nv + (b - l) * sp.cos(al) * (I3 - nv * nv.T) * Sv) == sp.zeros(3, 1))

# ---------------------------------------------------------------- D: exact drift identities on rational configurations
def runit(p, q):
    d = p * p + q * q + 1
    return (Fr(2 * p, 1) / d, Fr(2 * q, 1) / d, Fr(p * p + q * q - 1, 1) / d)
import random
rnd = random.Random(8178)
def dot(u, v): return sum(a * c for a, c in zip(u, v))
def add(*vs): return tuple(sum(c) for c in zip(*vs))
allD = True
for L in (2, 3, 4):
    for trial in range(3):
        s = {(i, j): runit(Fr(rnd.randint(-9, 9), rnd.randint(1, 9)), Fr(rnd.randint(-9, 9), rnd.randint(1, 9))) for i in range(L) for j in range(L)}
        S = {(i, j): add(s[(i, j)], s[((i - 1) % L, j)], s[(i, (j - 1) % L)]) for i in range(L) for j in range(L)}
        tot_S = add(*S.values()); tot_s = add(*s.values())
        allD &= all(tot_S[c] == 3 * tot_s[c] for c in range(3))                                   # D1
        for (i, j), Sx in S.items():
            pr = [s[(i, j)], s[((i - 1) % L, j)], s[(i, (j - 1) % L)]]
            D = sum(dot(add(pr[a], tuple(-c for c in pr[c2])), add(pr[a], tuple(-c for c in pr[c2]))) for a, c2 in ((0, 1), (0, 2), (1, 2)))
            allD &= dot(Sx, Sx) == 9 - D                                                            # D2
        M = tuple(c / (L * L) for c in tot_s); MM = dot(M, M)
        perp = lambda v: tuple(v[c] - dot(v, M) / MM * M[c] for c in range(3))
        hs = {key: Fr(rnd.randint(-20, 20), rnd.randint(1, 7)) for key in S}; hbar = Fr(rnd.randint(-5, 5), 3)
        lhs = add(*[tuple(hs[key] * c for c in perp(S[key])) for key in S])
        rhs = add(*[tuple((hs[key] - hbar) * c for c in perp(S[key])) for key in S])
        allD &= lhs == rhs and perp(tot_S) == (0, 0, 0)                                             # D3
ok("D1-D3 sum S_x = 3 sum s_x; |S|^2 = 9 - sum_{i<j}|s_i-s_j|^2; transverse drift uses only h_x - hbar", allD)

# ---------------------------------------------------------------- C: gain-one comparator moments (exact, zero mode removed)
def Sstar(L):
    t = 0
    for n1 in range(L):
        for n2 in range(L):
            if n1 or n2:
                k1, k2 = 2 * sp.pi * n1 / L, 2 * sp.pi * n2 / L
                t += 1 / (1 - (3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)) / 9)
    return sp.nsimplify(sp.simplify(t / L**2))
SST = {L: Sstar(L) for L in (2, 3, 4, 6)}
ok("C1 S*_2,3,4,6 = 27/32, 11/9, 189/128, 2627/1440", [SST[L] for L in (2, 3, 4, 6)] == [sp.Rational(27, 32), sp.Rational(11, 9), sp.Rational(189, 128), sp.Rational(2627, 1440)])
for L in (2, 3, 4):
    idx = [(i, j) for i in range(L) for j in range(L)]; pos = {d: n for n, d in enumerate(idx)}
    J = [(0, 0), (1, 0), (0, 1)]
    rowsM = []; rhs = []
    for d in idx:                                   # c(d) = (1/9) sum_{j,j'} c(d - j + j') + (delta_d0 - 1/L^2)
        r = [Fr(0)] * len(idx); r[pos[d]] += 1
        for a in J:
            for c in J:
                r[pos[((d[0] - a[0] + c[0]) % L, (d[1] - a[1] + c[1]) % L)]] -= Fr(1, 9)
        rowsM.append(r); rhs.append(Fr(int(d == (0, 0))) - Fr(1, L * L))
    rowsM.append([Fr(1)] * len(idx)); rhs.append(Fr(0))
    sol = sp.Matrix(rowsM).solve_least_squares(sp.Matrix(rhs)); c = {d: sp.nsimplify(sol[pos[d]]) for d in idx}
    resid = sp.Matrix(rowsM) * sol - sp.Matrix(rhs)
    VP = sum(c[((c2[0] - a[0]) % L, (c2[1] - a[1]) % L)] for a in J for c2 in J) / 9
    ok(f"C2 L={L}: stationary relative-field moments (per component, sigma^2=1)",
       all(sp.simplify(v) == 0 for v in resid) and c[(0, 0)] == SST[L] and sp.simplify(VP - (SST[L] - 1 + sp.Rational(1, L * L))) == 0
       and sp.simplify(3 * c[(0, 0)] - 3 * VP - 3 * (1 - sp.Rational(1, L * L))) == 0)

# ---------------------------------------------------------------- F: first-order assembly (formal; premises A1-A2 of ATTEMPT.md)
s2, Ss, iL = sp.symbols("s S iL", positive=True)       # sigma^2, S*_L, 1/L^2
Eb2 = 2 * s2 * iL * (1 - Ss * s2 + 2 * s2 * (1 - iL)); m = 1 - Ss * s2
Ea = -s2 * iL; Eb2a = -2 * s2**2 * iL**2; Eb4 = 2 * Eb2**2
x1 = Eb2 / (2 * m**2) - (Eb2 * Ea + Eb2a) / m**3 - sp.Rational(3, 8) * Eb4 / m**4
c1_one = sp.simplify(sp.series(x1 / (s2 * iL), s2, 0, 2).removeO().coeff(s2, 1))
c1_lam = sp.simplify(sp.series(-sp.log(1 - x1) / (s2 * iL), s2, 0, 2).removeO().coeff(s2, 1))
ok("F1 one-level coefficient S* + 2 - 1/L^2", sp.simplify(c1_one - (Ss + 2 - iL)) == 0, str(c1_one))
ok("F2 memory-rate coefficient S* + 2 - 1/(2L^2)", sp.simplify(c1_lam - (Ss + 2 - iL / 2)) == 0, str(c1_lam))
ok("F3 1/|M|^2 coefficient 2S*", sp.series(1 / m**2, s2, 0, 2).removeO().coeff(s2, 1) == 2 * Ss)
diff = {L: SST[L] + 2 - sp.Rational(1, 2 * L * L) - 2 * SST[L] for L in (2, 3, 4, 6)}
def Snum(L):
    return sum(1 / (1 - (3 + 2 * math.cos(2 * math.pi * a / L) + 2 * math.cos(2 * math.pi * c / L) + 2 * math.cos(2 * math.pi * (a - c) / L)) / 9)
               for a in range(L) for c in range(L) if a or c) / L**2
gnum = {L: 2 - 1 / (2 * L * L) - Snum(L) for L in (5, 7, 8, 9, 10, 16, 32, 64)}
ok("F4 c1 - 2S* > 0 at L = 2..7 (exact at 2,3,4,6) and < 0 at L = 8,9,10,16,32,64 (numerical)",
   all(v > 0 for v in diff.values()) and gnum[5] > 0 and gnum[7] > 0 and all(gnum[L] < 0 for L in (8, 9, 10, 16, 32, 64)))
print("F4 gap 2-1/(2L^2)-S*_L:", {L: round(float(v), 3) for L, v in diff.items()}, {L: round(v, 3) for L, v in gnum.items()})

# ---------------------------------------------------------------- E: the single-site control L = 1 (exact)
kk = sp.symbols("k", positive=True)
ident = sp.simplify(((sp.coth(kk) - 1 / kk - kk / (kk + 1)) - (2 * kk**2 + 2 * kk - (sp.exp(2 * kk) - 1)) / ((sp.exp(2 * kk) - 1) * (kk**2 + kk))).rewrite(sp.exp))
ok("E1 A - k/(k+1) = (2k^2+2k-(e^{2k}-1))/((e^{2k}-1)(k^2+k))", ident == 0)
ok("E2 e^{2k}-1-2k-2k^2 has only positive Taylor coefficients", all(c > 0 for c in sp.Poly(sp.series(sp.exp(2 * kk) - 1 - 2 * kk - 2 * kk**2, kk, 0, 12).removeO(), kk).all_coeffs()[:-3]))
lam1 = -sp.log(1 - x) / ((1 - x) * x)                  # lambda_1 tau_1 = -kappa log A / A with A = 1 - x (coth -> 1)
ser1 = sp.series(lam1, x, 0, 3).removeO(); sig = (1 - x) * x
ok("E3 lambda_1 tau_1 = 1 + (3/2) sigma^2 + O(sigma^4)", sp.simplify(sp.series(ser1 - (1 + sp.Rational(3, 2) * sig), x, 0, 2).removeO()) == 0
   and sp.simplify(c1_lam.subs({Ss: 0, iL: 1}) - sp.Rational(3, 2)) == 0)

# ---------------------------------------------------------------- H: historical rows (author-reported) against the first-order law
def Sf(L):
    return sum(1 / (1 - (3 + 2 * math.cos(2 * math.pi * a / L) + 2 * math.cos(2 * math.pi * c / L) + 2 * math.cos(2 * math.pi * (a - c) / L)) / 9)
               for a in range(L) for c in range(L) if a or c) / L**2
def Af(z): return 1 / math.tanh(z) - 1 / z
print("H historical rows: beta L | reported D1 ratio lag25 lag100 | 1/|m|^2 | first-order 1+s2(S*+2-1/2L^2) | 1+2S*s2")
hl = []
for bb, LL, tau, mm, d25, d100, d1000, im in rows:
    bb, LL = int(bb), int(LL); s2v = Af(3 * bb) / (3 * bb); Sv_ = Sf(LL)
    p1 = 1 + s2v * (Sv_ + 2 - 1 / (2 * LL * LL)); pm = 1 + 2 * Sv_ * s2v
    hl.append((float(d25) + float(d100)) / 2 < float(im))
    print(f"  {bb:3d} {LL:3d} | {d25} {d100} | {im} | {p1:.3f} | {pm:.3f}")
ok("H1 every historical short-lag D1 ratio lies below its reported 1/|m|^2", all(hl))

# ---------------------------------------------------------------- N: recorded Monte Carlo evidence (numerical) + small re-run
mco = open(os.path.join(HERE, "mc_evidence.out")).read()
fits = re.findall(r"L=\s*(\d+) weighted linear fit in sigma\^2: intercept ([\d.]+)\+-([\d.]+) slope [-\d.]+ ; pred1 ([\d.]+) ; 2S\* ([\d.]+)", mco)
ok("N1 four fits recorded", len(fits) == 4)
nfit = all(abs(float(i) - float(p)) <= 2.5 * float(e) and (L_ == "16" or abs(float(i) - float(t)) >= 5 * float(e)) for L_, i, e, p, t in fits)
ok("N2 one-level intercepts: within 2.5 SE of S*+2-1/L^2 (L=2,3,4,16); at least 5 SE from 2S* (L=2,3,4)", nfit, str(fits))
lr = re.findall(r"L=(\d) lags \d+,\d+: lam1\*tau=([\d.]+)\+-([\d.]+) x1\*tau=[\d.]+ -log\(1-x1\)\*tau=([\d.]+) 1/E\|M\|\^2=([\d.]+) \(lam1\*tau-1/E\|M\|\^2\)/se=([-\d.]+)", mco)
ok("N3 memory rate at L=2,3,4: >= 5 SE above 1/E|M|^2 and within 3 SE of -log(1-x1)",
   len(lr) == 3 and all(float(z) >= 5 and abs(float(a) - float(c)) <= 3 * float(e) for _, a, e, c, _, z in lr), str(lr))
l16 = re.findall(r"L=16 beta=\s*(\d+) sigma2=([\d.]+) x1\*tau=([\d.]+) coef=[\d.]+\+-([\d.]+) 1/E\|M\|\^2=([\d.]+)", mco)
ok("N4 L=16: one-level rate >= 5 SE below 1/E|M|^2 at beta=48,96", len(l16) == 2 and all((float(im) - float(xt)) / (float(se) * float(sv)) >= 5 for _, sv, xt, se, im in l16), str(l16))
lag = re.findall(r"lag\s+64: -log C\(l\)/l \* tau = ([\d.]+)\+-([\d.]+)", mco); imc = re.findall(r"\(c\) L=16 beta=12: 1/E\|M\|\^2=([\d.]+)", mco)
ok("N5 L=16 beta=12: lag-64 memory rate >= 5 SE below 1/E|M|^2", len(lag) == 1 and (float(imc[0]) - float(lag[0][0])) / float(lag[0][1]) >= 5)
sys.path.insert(0, HERE)
import numpy as np
from mc_evidence import run, jack, A as Anp
xr, im2 = run(40, 2, 4000, 1500, 360, [1], 777)
s2v = Anp(120) / 120; cm, cse = jack(lambda i: (xr[0, i].mean() * 4 / s2v - 1) / s2v, 4000)
ok("N6 fresh seed, L=2 beta=40: one-level coefficient >= 10 SE above 2S* = 27/16", (cm - 27 / 16) / cse >= 10, f"{cm:.3f}+-{cse:.3f}")
print(f"N fresh L=2 beta=40 coef {cm:.3f}+-{cse:.3f} (first order 2.594, 2S* 1.6875); origin/main copy of note identical: {main_same}")

print(f"checks passed {NOK}, failed {len(FAILS)}")
if FAILS:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAILS)); sys.exit(1)
print("SUMMARY: PARTIAL PR8178's nonlinear torus memory separated from the gain-one proxy: exact drift/noise decomposition of the plane "
      "average (drift along local fields; direction drift only from |S_x| differences); single-site rate -3b log A(3b)/A(3b) > 1 = 1/|m|^2 "
      "for all b; under two stated small-noise premises (A1-A2, open) the first-order law lambda1 tau_L = 1 + s2(S*_L + 2 - 1/(2L^2)), "
      "S*_2,3,4 = 27/32, 11/9, 189/128, against 1 + 2 S*_L s2 for 1/|m|^2; seeded Monte Carlo agrees at L=2,3,4,16")
print("HIT: the historical 1/|m|^2 factor is not the strong-coupling law of the nonlinear sphere law's torus memory: at fixed L the first "
      "order is lambda1 tau_L = 1 + sigma^2 (S*_L + 2 - 1/(2L^2)), S*_L = L^-2 sum_{k!=0} 1/(1-u_k), versus 1/|m|^2 = 1 + 2 S*_L sigma^2 "
      "(log L coefficients differ by a factor 2; the gap changes sign between L=7 and L=8); seeded Monte Carlo puts the memory rate "
      ">= 5 SE above 1/|m|^2 at L=2,3,4 (beta=20) and >= 5 SE below it at L=16; exact at L=1: -3b log A(3b)/A(3b) > 1")
