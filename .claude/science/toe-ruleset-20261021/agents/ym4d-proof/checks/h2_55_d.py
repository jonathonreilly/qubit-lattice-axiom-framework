#!/usr/bin/env python3
# h2_55_d — inter-scale lemma arithmetic, continuous-time threshold, (B-BR) constants, k1 conversion.
# Criteria: h2_55_d_criteria.md (written before this script). Fractions/sympy exact only.
# Run 1 (03:23Z) was killed at ~03:33Z with no output (D2's linear threshold search did not terminate);
# run 2 replaces only that search by an exact monotone binary search. Gates, controls and data are unchanged.
from fractions import Fraction as Fr
import sympy as sp
results = []; controls = []
def gate(name, ok, detail=''):
    results.append(bool(ok)); print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
def control(name, fired, detail=''):
    controls.append(bool(fired)); print(f"{'FIRES' if fired else 'DOES-NOT-FIRE'}  {name}  {detail}")
st = [987654321]
def rnd(n):
    st[0] = (1103515245*st[0] + 12345) % (2**31); return (st[0] >> 8) % n
# ---------------- D1: Lemma INT arithmetic ----------------
def make_e():
    terms = []
    for _ in range(1 + rnd(4)):
        w = Fr(1 + rnd(9), 1 + rnd(5)); s_ = Fr(1 + rnd(40), 1 + rnd(40)); n_ = Fr(rnd(30), 1 + rnd(4))
        terms.append((w, s_, n_))
    return lambda t: sum((w*(1 if t <= s_ else 0)*(1 + 1/(1 + n_*t)) for (w, s_, n_) in terms), Fr(0))
viol = 0; checked = 0
efuncs = [make_e() for _ in range(40)]
for ct in (Fr(1), Fr(3, 2)):
    for L in (2, 3, 4):
        grid = [ct/Fr(L)**(2*m) for m in range(7)]
        for e in efuncs:
            for m in range(6):
                tm, tm1 = grid[m], grid[m+1]
                rhs = Fr(L)**4*tm1**2*e(tm1)
                for j in range(30):
                    t = tm1 + (tm - tm1)*Fr(j, 29)
                    checked += 1
                    if t*t*e(t) > rhs: viol += 1
gate('D1 t^2 e(t) <= L^4 t_{m+1}^2 e(t_{m+1}) on [t_{m+1}, t_m] for non-increasing e', viol == 0, f'checked={checked}, violations={viol}')
inc = lambda t: 1 + t
fired = False
for L in (2, 3, 4):
    grid = [Fr(1)/Fr(L)**(2*m) for m in range(7)]
    for m in range(6):
        tm, tm1 = grid[m], grid[m+1]
        if tm*tm*inc(tm) > Fr(L)**4*tm1**2*inc(tm1): fired = True
control('D1-F increasing e(t) = 1 + t violates the bound', fired)
# ---------------- D2: continuous-time threshold ----------------
def ge_pow(U, X, th):     # U^(1-th) >= X with th = p/q, U, X > 0, via integer powers
    if U <= 0: return False
    p, q = th.numerator, th.denominator
    return U**(q - p) >= X**q
viol2 = 0; viol2b = 0; ctrl2 = 0; nctrl = 0; sets = 0
for k in range(200):
    cm = Fr(1 + rnd(20), 1 + rnd(50)); Cp = cm*Fr(1 + rnd(200), 1 + rnd(3))
    bm = Fr(1 + rnd(30), 1 + rnd(10)); bp = bm + Fr(rnd(20), 1 + rnd(10)); R = Fr(rnd(15), 1 + rnd(4))
    u0 = Fr(1 + rnd(20), 1) + R; L = (2, 3, 4)[rnd(3)]; th = (Fr(0), Fr(1, 3), Fr(1, 2), Fr(2, 3))[rnd(4)]; m0 = rnd(3)
    Um = lambda m: u0 + bm*m - R
    Up = lambda m: u0 + bp*m + R
    X = 2*Fr(L)**4*Cp*Up(m0)/cm; Xp = 2*Cp*Up(m0)/cm
    # run-1 used a linear search that did not terminate in 10 min (thresholds ~1e15 steps); run 2: exact binary search
    def least(pred, lo):
        if pred(lo): return lo
        hi = lo + 1
        while not pred(hi): hi = 2*hi
        while hi - lo > 1:
            mid = (lo + hi)//2
            if pred(mid): hi = mid
            else: lo = mid
        return hi
    m1c = least(lambda m: ge_pow(Um(m + 1), X, th), m0)
    m1p = least(lambda m: ge_pow(Um(m), Xp, th), m0)
    sets += 1
    if not all(ge_pow(Um(m + 1), X, th) for m in range(m1c, m1c + 41)): viol2 += 1
    if not (m1c >= m1p - 1): viol2b += 1
    if m1c > m0:
        nctrl += 1
        if not ge_pow(Um(m1c), X, th): ctrl2 += 1
gate('D2 (i) threshold holds on [m1c, m1c+40]; (ii) m1c >= m1prime - 1', viol2 == 0 and viol2b == 0, f'sets={sets}, viol(i)={viol2}, viol(ii)={viol2b}')
control('D2-F at m1c - 1 the inequality fails (sharpness of the least index)', nctrl > 0 and ctrl2 == nctrl, f'{ctrl2}/{nctrl}')
# ---------------- D3: (B-BR) => F-flow constants ----------------
v3 = 0
for k in range(200):
    bp_ = Fr(1 + rnd(50), 1 + rnd(20)); bpp = bp_ + Fr(rnd(30), 1 + rnd(9)); ell = Fr(1 + rnd(40), 1 + rnd(30))
    Crg = bp_*ell/2*Fr(rnd(101), 100)
    bmin = bp_ - Crg/ell; bplus = bpp + Crg/ell
    if not (bmin >= bp_/2 and bmin > 0 and bplus <= bpp + bp_/2): v3 += 1
gate('D3 beta_- >= beta\'/2 > 0 and beta_+ <= beta\'\' + beta\'/2 when C_rho gamma^2 <= beta\' ell/2', v3 == 0, f'violations={v3}')
bp_ = Fr(3, 2); ell = Fr(7, 5); Crg = bp_*ell
control('D3-F C_rho gamma^2 = beta\' ell gives beta_- = 0', (bp_ - Crg/ell) == 0)
# ---------------- D4: k1 conversion ----------------
Asym, g2, al, kg, ka, gam, Lam, N = sp.symbols('A g2 alpha k_g k_alpha gamma Lambda N', positive=True)
expr = sp.expand(Asym*g2*(1 + kg*g2)).subs(g2, 4*sp.pi*al) - sp.expand(Asym*4*sp.pi*al*(1 + ka*al))
ok41 = sp.simplify(expr.subs(ka, 4*sp.pi*kg)) == 0
b0 = 11*N/(48*sp.pi**2)
kgv = N/(16*sp.pi**2)*(11*gam/3 + sp.Rational(52, 9) - 3*Lam)
val = sp.simplify(4*kgv/b0)
ok42 = sp.simplify(val - (4*gam + sp.Rational(208, 33) - sp.Rational(36, 11)*Lam)) == 0
gate('D4 k_alpha = 4 pi k_g; 4 k_g/b0 = 4 gamma + 208/33 - (36/11) log3', ok41 and ok42, f'{sp.expand(val)}')
kav = N/(4*sp.pi)*(11*gam/3 + sp.Rational(52, 9) - 3*Lam)
control('D4-F k_alpha in place of k_g changes the coefficient', sp.simplify(4*kav/b0 - val) != 0)
print(f"gates: {sum(results)}/{len(results)} pass; controls: {sum(controls)}/{len(controls)} fire")
print('VERDICT:', 'PASS' if all(results) and all(controls) else 'FAIL')
