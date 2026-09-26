#!/usr/bin/env python3
"""Readout remainder in a growing time window for the postmark electric Jacobi evolution
(J:derive:deferred-20260925-spectral-readout:a1).

Supplied model (landed notes on main): M_S = -H_{2,S} tridiagonal on I_S = [-5S, 5S-4], C = S(S+1),
    (M_S)_{n,n} = 2 - (y1+y2)/C,  (M_S)_{n,n+1} = sqrt((1-x1/C)(1-x2/C)),
G_S = M_S^2 - C M_S, prepared state |0>, readout O = 1[n = 0 mod 3] = (I + V + V*)/3.
Landed short-time theorem: at t = tau/C (tau fixed) the readout tends to 1/3 + (2/3) J0(2 sqrt3 tau).

Theorem proved here (ATTEMPT.md): with T = C t, for integer S >= 7 and 0 <= T <= S,
    |P_S(T/C) - 1/3 - (2/3) J0(2 sqrt3 T)| <= 2 eps(T,S),
    eps = (6/(25C)) (sqrt6 T^3/3 + (19/sqrt2) T^2 + 81 T) + 16 T/C + 6 T sqrt(32/15) (e/4)^(5S-6).
So P_S -> 1/3 along every window T_S -> oo with T_S^3/S^2 -> 0 (lab times 1/C << t << S^(-4/3)).

A  landed model loaded at a pinned main commit; exact residue polynomials; the all-n coefficient bound
   x_i, y_i <= (|n|+7)^2/25 proved per residue class by exact linear-function checks
B  Bessel facts: second and fourth moments of J_m(z)^2 (symbolic, from the Neumann generating function),
   |J_m(z)| <= (z/2)^m/m!, free readout J0(2 sqrt3 T)
C  the remainder constants
D  floating diagnostics: exact finite-S evolution respects the bound (not part of the proof)
"""
import hashlib, importlib.util, math, subprocess, sys, tempfile, time
from fractions import Fraction
import sympy as sp

T0 = time.time()
FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

MAIN = "78db61c32a39234bab16034c57361bf0c418c0b1"
CORE_SHA = "e282bbe1a92afdd8306892a95b537caa5222ea189a4f74a2ab8cac86f743b9c5"

print("== A  landed model")
src = subprocess.run(["git", "show", f"{MAIN}:scripts/core_derivation.py"], capture_output=True, check=True).stdout
check("A0 scripts/core_derivation.py at main 78db61c3 has the recorded sha256", hashlib.sha256(src).hexdigest() == CORE_SHA)
tmp = tempfile.NamedTemporaryFile("wb", suffix=".py", delete=False); tmp.write(src); tmp.close()
spec = importlib.util.spec_from_file_location("core", tmp.name); core = importlib.util.module_from_spec(spec); spec.loader.exec_module(core)
R = 1300
nodes = core.walk_nodes(R)
def x_pair(paths):
    assert len(paths) == 1, paths
    m1, a1, m2, a2 = paths[0][3]
    return (m1*(m1 + a1), m2*(m2 + a2))
def edge_x(n): return x_pair([p for p in core.two_hop_paths(nodes[n]) if p[0] == nodes[n + 1]])
def returns_x(n):
    paths = [p for p in core.two_hop_paths(nodes[n]) if p[0] == nodes[n]]
    assert len(paths) == 2
    out = []
    for p in paths:
        pr = x_pair([p]); assert pr[0] == pr[1]; out.append(pr[0])
    return tuple(out)
EX = {n: edge_x(n) for n in range(-R, R)}
RX = {n: returns_x(n) for n in range(-R, R)}
def fit(v0, v1, v2):
    A = Fraction(v2 - 2*v1 + v0, 2); B = Fraction(v1 - v0) - A
    return (A, B, Fraction(v0))
polys = {}
okA1 = True
for r in range(15):
    for name, tab in (("edge", EX), ("ret", RX)):
        for j in (0, 1):
            p = fit(*[tab[r + 15*k][j] for k in (0, 1, 2)])
            if p[0] != 9: okA1 = False
            for n in range(-R, R):
                if (n - r) % 15 == 0:
                    k = (n - r)//15
                    if p[0]*k*k + p[1]*k + p[2] != tab[n][j]: okA1 = False
            polys[(r, name, j)] = p
check("A1 every edge/return factor is 9k^2 + b k + c at fixed residue r (n = 15k + r), exact on |n| < 1300", okA1)
okA1b = all(v >= 0 for tab in (EX, RX) for pair in tab.values() for v in pair)
check("A1b all factors m(m+a) are >= 0", okA1b)
def bound_ok(p, r, c):
    """(|15k+r|+c)^2 - 25 p(k) >= 0 for every integer k: linear on each side of 15k+r = 0."""
    A, B, C0 = p
    # k >= 0: (15k + r + c)^2 - 25(9k^2 + Bk + C0) = (30(r+c) - 25B) k + (r+c)^2 - 25 C0
    s1, i1 = 30*(r + c) - 25*B, (r + c)**2 - 25*C0
    if not (s1 >= 0 and i1 >= 0): return False
    # k <= -1, write k = -j, j >= 1: (15j - r + c)^2 - 25(9j^2 - Bj + C0) = (30(c - r) + 25B) j + (c - r)^2 - 25 C0
    s2, i2 = 30*(c - r) + 25*B, (c - r)**2 - 25*C0
    return s2 >= 0 and s2 + i2 >= 0
okA2 = all(bound_ok(p, r, 7) for (r, _, _), p in polys.items())
worst6 = [key for key, p in polys.items() if not bound_ok(p, key[0], 6)]
check("A2 for every integer n: x1,x2,y1,y2 <= (|n|+7)^2/25 (exact, all 15 residues, all k)", okA2, f"c=6 fails for {len(worst6)} polynomials")
okA2n = all(max(EX[n] + RX[n]) * 25 <= (abs(n) + 7)**2 for n in range(-R, R))
check("A2b direct confirmation on |n| < 1300", okA2n)
# the finite-spin entry form against the landed legal-hop finite-spin H2 (floating, one spin)
Sx = 20; Cx = Sx*(Sx + 1); okA3 = True
for n in range(-15, 16):
    h2 = core.finite_spin_h2(nodes[n], Sx)
    a = 2 - (RX[n][0] + RX[n][1])/Cx
    b = math.sqrt((1 - EX[n][0]/Cx)*(1 - EX[n][1]/Cx))
    if abs(-h2.get(nodes[n], 0.0) - a) > 1e-12 or abs(-h2.get(nodes[n + 1], 0.0) - b) > 1e-12: okA3 = False
check("A3 entry form a_n = 2-(y1+y2)/C, b_n = sqrt((1-x1/C)(1-x2/C)) matches the landed finite-spin H2 (S=20, |n|<=15)", okA3)
okA4 = True
for al in [Fraction(i, 17) for i in range(18)]:
    for be in [Fraction(j, 13) for j in range(14)]:
        prod = (1 - al)*(1 - be)
        if 1 - math.sqrt(prod) > float(al + be) + 1e-15: okA4 = False
check("A4 1 - sqrt((1-a)(1-b)) <= a + b on [0,1]^2 (proof in ATTEMPT; grid spot check)", okA4)

print("== B  Bessel facts")
z, th = sp.symbols("z theta", positive=True)
gen = sp.besselj(0, 2*z*sp.sin(th/2))
ser = sp.series(gen, th, 0, 6).removeO()
m2 = sp.simplify(-sp.diff(ser, th, 2).subs(th, 0))
m4 = sp.simplify(sp.diff(ser, th, 4).subs(th, 0))
check("B1 sum_m m^2 J_m(z)^2 = z^2/2 (from sum_m J_m(z)^2 e^{i m theta} = J0(2 z sin(theta/2)))", sp.simplify(m2 - z**2/2) == 0, str(m2))
check("B2 sum_m m^4 J_m(z)^2 = z^2/2 + 3 z^4/8", sp.simplify(m4 - (z**2/2 + 3*z**4/8)) == 0, str(sp.expand(m4)))
import mpmath as mp
mp.mp.dps = 40
okB3 = True
for zz in (mp.mpf("0.7"), mp.mpf("5.3"), mp.mpf("17")):
    s0 = sum(mp.besselj(k, zz)**2 for k in range(-120, 121))
    s2 = sum(k**2*mp.besselj(k, zz)**2 for k in range(-120, 121))
    s4 = sum(k**4*mp.besselj(k, zz)**2 for k in range(-120, 121))
    if abs(s0 - 1) > mp.mpf(10)**-30 or abs(s2 - zz**2/2) > mp.mpf(10)**-25 or abs(s4 - zz**2/2 - 3*zz**4/8) > mp.mpf(10)**-20: okB3 = False
check("B3 the three sums (normalization, m^2, m^4) numerically at z = 0.7, 5.3, 17 (40 digits)", okB3)
okB4 = all(abs(mp.besselj(k, zz)) <= (zz/2)**k/mp.factorial(k) for zz in (mp.mpf("0.5"), mp.mpf(3), mp.mpf(20)) for k in range(0, 60))
check("B4 |J_m(z)| <= (z/2)^m/m! (Poisson integral; spot check)", okB4)
okB5 = True
for T in (mp.mpf("0.3"), mp.mpf("2.1"), mp.mpf("7.5")):
    w = mp.exp(2j*mp.pi/3)
    val = sum(w**k*mp.besselj(k, 2*T)**2 for k in range(-150, 151))
    if abs(val - mp.besselj(0, 2*mp.sqrt(3)*T)) > mp.mpf(10)**-25: okB5 = False
check("B5 free readout: sum_m omega^m J_m(2T)^2 = J0(2 sqrt3 T)", okB5)

print("== C  remainder constants")
def eps(T, S):
    C = S*(S + 1)
    E1 = 6/(25*C)*(math.sqrt(6)*T**3/3 + 19/math.sqrt(2)*T**2 + 81*T)
    E2 = 16*T/C
    Et = 6*T*math.sqrt(32/15)*(math.e/4)**(5*S - 6)
    return E1 + E2 + Et
# integrand bound: ||(|m|+9)^2||_mu <= sqrt(z^2/2+3z^4/8) + 18 z/sqrt2 + 81 with z = 2s, and sqrt(2s^2+6s^4) <= sqrt6 s^2 + sqrt2 s
s_ = sp.symbols("s", positive=True)
integrand = sp.sqrt(6)*s_**2 + sp.sqrt(2)*s_ + 18*2*s_/sp.sqrt(2) + 81
integ = sp.integrate(integrand, (s_, 0, sp.Symbol("T", positive=True)))
Tsym = sp.Symbol("T", positive=True)
check("C1 integral of sqrt6 s^2 + 19 sqrt2 s + 81 over [0,T] = sqrt6 T^3/3 + (19/sqrt2) T^2 + 81 T",
      sp.simplify(integ - (sp.sqrt(6)*Tsym**3/3 + 19/sp.sqrt(2)*Tsym**2 + 81*Tsym)) == 0)
okC2 = all(math.sqrt(2*s*s + 6*s**4) <= math.sqrt(6)*s*s + math.sqrt(2)*s + 1e-12 for s in [i/7 for i in range(0, 400)])
check("C2 sqrt(2s^2 + 6s^4) <= sqrt6 s^2 + sqrt2 s (subadditivity of sqrt; grid)", okC2)
lead = 2*6/25*math.sqrt(6)/3
check("C3 leading readout constant 2*(6/25)*(sqrt6/3) = 0.3919...", abs(lead - 0.39191835884530846) < 1e-12, f"{lead:.6f}")
for S in (100, 1000, 10**4, 10**6):
    T = S**0.5
    print(f"   S={S}: T=S^(1/2)={T:.1f}: 2eps = {2*eps(T, S):.3e}; (2/3)|J0(2sqrt3 T)| <= {(2/3)*math.sqrt(2/(math.pi*2*math.sqrt(3)*T)):.3e}")
check("C4 along T_S = S^(1/2): 2 eps decreases (S = 10^2, 10^4, 10^6)", 2*eps(1000.0, 10**6) < 2*eps(100.0, 10**4) < 2*eps(10.0, 100))

print("== D  floating diagnostics (exact finite-S evolution vs the proved bound)")
import numpy as np
from scipy.linalg import eigh_tridiagonal
def pv(name, j, n):
    r = n % 15; k = (n - r)//15; A, B, C0 = polys[(r, name, j)]
    return A*k*k + B*k + C0
okD = True; rows = []
for S in (21, 42, 84, 168, 336):
    C = S*(S + 1)
    ns = list(range(-5*S, 5*S - 3))
    a = np.array([2 - float(pv("ret", 0, n) + pv("ret", 1, n))/C for n in ns])
    b = np.array([math.sqrt(max(0.0, (1 - float(pv("edge", 0, n))/C)*(1 - float(pv("edge", 1, n))/C))) for n in ns[:-1]])
    lam, vec = eigh_tridiagonal(a, b)
    i0 = ns.index(0)
    c0 = vec[i0, :]
    cls = np.array([n % 3 == 0 for n in ns])
    worst = 0.0
    for T in np.linspace(0.0, float(S), 61):
        t = T/C
        ph = np.exp(1j*(T*lam - t*lam**2))
        psi = vec @ (ph*c0)
        P = float(np.sum(np.abs(psi[cls])**2))
        Pinf = 1/3 + (2/3)*float(mp.besselj(0, 2*math.sqrt(3)*T))
        err = abs(P - Pinf); bnd = 2*eps(T, S)
        worst = max(worst, err/bnd if bnd > 0 else 0.0)
        if err > bnd + 1e-9: okD = False
    Tw = S**(2/3)
    rows.append((S, round(worst, 4)))
check("D1 exact finite-S readout stays within the proved remainder for 0 <= T <= S (S = 21..336)", okD, f"max err/bound per S: {rows}")
print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PARTIAL (new exact partial result): for integer S >= 7 and 0 <= T = Ct <= S, "
          "|P_S(T/C) - 1/3 - (2/3)J0(2sqrt3 T)| <= 2eps(T,S) = 0.392 T^3/C + O(T^2/C); the readout tends to 1/3 on every window "
          "T_S -> oo, T_S = o(S^(2/3)); first unresolved step: S^(2/3) <~ T <~ S^2 (fixed lab time is T ~ S^2)")
    print("HIT readout remainder: postmark vacancy readout -> 1/3 in the growing window 1 << T << S^(2/3) with explicit Duhamel bound")
