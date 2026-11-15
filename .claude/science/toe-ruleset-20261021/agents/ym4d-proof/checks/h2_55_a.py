#!/usr/bin/env python3
# h2_55_a — comparator-side exact algebra. Criteria: h2_55_a_criteria.md (written before this script).
# Exact sympy / fractions only; no floats are computed.
import itertools, sys
import sympy as sp

results = []   # (name, ok)
controls = []  # (name, fired)
def gate(name, ok, detail=''):
    results.append((name, bool(ok)))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
def control(name, fired, detail=''):
    controls.append((name, bool(fired)))
    print(f"{'FIRES' if fired else 'DOES-NOT-FIRE'}  {name}  {detail}")

u, s, t, v, m, w, eps, M_ = sp.symbols('u s t v m w epsilon M', positive=True)
p0 = sp.symbols('p0', real=True)

def psd_exact(Mt):
    n = Mt.shape[0]
    for r in range(1, n+1):
        for idx in itertools.combinations(range(n), r):
            if sp.nsimplify(Mt.extract(list(idx), list(idx)).det()) < 0:
                return False
    return True

# ---------------- A1: Codex's N1 counterexample ----------------
s1 = 1/(u*(1+u)); s2 = 1/(1+u)
gate('A1.1 s1+s2 = 1/u', sp.simplify(s1 + s2 - 1/u) == 0)
ap = sp.apart(s1, u)
gate('A1.2a apart(s1) = 1/u - 1/(1+u)', sp.simplify(ap - (1/u - 1/(1+u))) == 0, f'apart={ap}')
rho0 = sp.diag(1, 0); rho1 = sp.diag(-1, 1)
gate('A1.2b colour-matrix weight at mass^2=1 is NOT PSD (law excluded from G^col)', (not psd_exact(rho1)) and psd_exact(rho0))
h_new = sp.simplify(u*(s1 + s2/4))
gate('A1.3a h_new = 1/4 + 3/(4(1+u))', sp.simplify(h_new - (sp.Rational(1,4) + sp.Rational(3,4)/(1+u))) == 0, f'h_new={h_new}')
dh = sp.simplify(sp.diff(h_new, u))
gate('A1.3b dh_new/du = -3/(4(1+u)^2) (negative)', sp.simplify(dh + sp.Rational(3,4)/(1+u)**2) == 0 and dh.is_negative is True, f'dh={dh}')
lim = sp.limit(h_new, u, sp.oo)
I1 = sp.integrate(v*sp.exp(-2*v), (v, 0, sp.oo))
coef = sp.Rational(3,32)*lim*I1
gate('A1.4 h_new(inf) = 1/4 and UV coefficient 3/512 (x 1/pi^2)', lim == sp.Rational(1,4) and coef == sp.Rational(3,512), f'lim={lim}, int v e^-2v={I1}, coef={coef}')
# control A1-F: colour-RP pair
s1c = 1/u; s2c = 1/(1+u)
rc0 = sp.diag(1, 0); rc1 = sp.diag(0, 1)
hc = sp.simplify(u*(s1c + s2c/4)); dhc = sp.simplify(sp.diff(hc, u))
fired = psd_exact(rc0) and psd_exact(rc1) and (dhc.is_negative is not True) and (dhc.is_nonnegative is True)
control('A1-F colour-RP pair: PSD at both masses, dh/du >= 0 (detector says not decreasing)', fired, f'dh={dhc}')

# ---------------- A2: closure of the matrix class ----------------
state = [12345]
def nxt():
    state[0] = (1103515245*state[0] + 12345) % (2**31)
    return state[0]
def rand_entry():
    a = (nxt() >> 8) % 7 - 3
    k = (nxt() >> 8) % 3 + 1
    return sp.Rational(a, k)
def rand_mat():
    return sp.Matrix(3, 3, lambda i, j: rand_entry())
viol = 0
for _ in range(60):
    B = rand_mat(); Lam = rand_mat(); C = rand_mat()
    rho = B*B.T; Mm = C*C.T
    LrL = Lam*rho*Lam.T
    if not psd_exact(LrL): viol += 1
    if (Mm*rho).trace() < 0: viol += 1
    if (Mm*LrL).trace() < 0: viol += 1
gate('A2 Lambda rho Lambda^T PSD, Tr(M rho) >= 0, Tr(M Lambda rho Lambda^T) >= 0 (60 triples)', viol == 0, f'violations={viol}')
rho_bad = sp.diag(1, -1, 2); e2 = sp.Matrix([0, 1, 0]); Mbad = e2*e2.T
control('A2-F non-PSD rho_bad with M = e2 e2^T gives Tr < 0', (Mbad*rho_bad).trace() < 0, f'Tr={(Mbad*rho_bad).trace()}')

# ---------------- A3: tensor structure ----------------
P = sp.symbols('p1:5', real=True)
d = lambda a, b: 1 if a == b else 0
R4 = range(4)
def TI(mu, nu, rh, si):
    return P[mu]*P[rh]*d(nu, si) - P[mu]*P[si]*d(nu, rh) - P[nu]*P[rh]*d(mu, si) + P[nu]*P[si]*d(mu, rh)
def II(mu, nu, rh, si):
    return d(mu, rh)*d(nu, si) - d(mu, si)*d(nu, rh)
def vv(lam, mu, nu):
    return P[mu]*d(nu, lam) - P[nu]*d(mu, lam)
ok = all(sp.expand(TI(a, b, c, e) - sum(vv(l, a, b)*vv(l, c, e) for l in R4)) == 0 for a in R4 for b in R4 for c in R4 for e in R4)
gate('A3.1 T^I = sum_l v^l v^l (Gram form, 256 components)', ok)
structs = {
 'dd(mn)(rs)': lambda a,b,c,e: d(a,b)*d(c,e),
 'dd(mr)(ns)': lambda a,b,c,e: d(a,c)*d(b,e),
 'dd(ms)(nr)': lambda a,b,c,e: d(a,e)*d(b,c),
 'd(mn)pp':    lambda a,b,c,e: d(a,b)*P[c]*P[e],
 'd(mr)pp':    lambda a,b,c,e: d(a,c)*P[b]*P[e],
 'd(ms)pp':    lambda a,b,c,e: d(a,e)*P[b]*P[c],
 'd(nr)pp':    lambda a,b,c,e: d(b,c)*P[a]*P[e],
 'd(ns)pp':    lambda a,b,c,e: d(b,e)*P[a]*P[c],
 'd(rs)pp':    lambda a,b,c,e: d(c,e)*P[a]*P[b],
 'pppp':       lambda a,b,c,e: P[a]*P[b]*P[c]*P[e],
}
def antisym(S):
    return lambda a,b,c,e: S(a,b,c,e) - S(b,a,c,e) - S(a,b,e,c) + S(b,a,e,c)
allok = True; anyA = False; anyB = False; coeffs = {}
for name, S in structs.items():
    AS = antisym(S)
    # solve from components (0,1,0,1): a + b(p1^2+p2^2); (0,1,0,2): b p2 p3
    b_ = sp.simplify(AS(0,1,0,2)/(P[1]*P[2]))
    a_ = sp.simplify(AS(0,1,0,1) - b_*(P[0]**2 + P[1]**2))
    const = (sp.diff(a_, P[0]) == 0 and all(sp.diff(a_, x) == 0 for x in P) and all(sp.diff(b_, x) == 0 for x in P))
    match = all(sp.expand(AS(i,j,k,l) - a_*II(i,j,k,l) - b_*TI(i,j,k,l)) == 0 for i in R4 for j in R4 for k in R4 for l in R4)
    coeffs[name] = (a_, b_)
    allok = allok and const and match
    anyA = anyA or a_ != 0; anyB = anyB or b_ != 0
gate('A3.2 every antisymmetrised O(4) structure = a I + b T^I (rational a,b); span {I, T^I}', allok and anyA and anyB, f'coeffs={coeffs}')
def Bi(S):
    return [[[sp.expand(sum(sp.LeviCivita(lam, mu, nu, ka)*P[mu]*S(nu, ka, rh, si) for mu in R4 for nu in R4 for ka in R4)) for si in R4] for rh in R4] for lam in R4]
BT = Bi(TI); BI = Bi(II)
zeroT = all(BT[a][b][c] == 0 for a in R4 for b in R4 for c in R4)
nonzeroI = any(BI[a][b][c] != 0 for a in R4 for b in R4 for c in R4)
gate('A3.3 Bianchi: Bi[T^I] = 0 identically; Bi[I] has a nonzero component', zeroT and nonzeroI)
def Tbad(mu, nu, rh, si):
    return P[mu]*P[rh]*d(nu, si) + P[mu]*P[si]*d(nu, rh) - P[nu]*P[rh]*d(mu, si) + P[nu]*P[si]*d(mu, rh)
Bb = Bi(Tbad)
control('A3-F sign-flipped T\' fails Bianchi', any(Bb[a][b][c] != 0 for a in R4 for b in R4 for c in R4))
tr4 = sp.expand(sum(TI(a, b, a, b) for a in R4 for b in R4))
sp3 = range(3)
tr3 = sp.expand(sum(TI(a, b, a, b) for a in sp3 for b in sp3))
indep = all(sp.diff(TI(a, b, c, e), P[3]) == 0 for a in sp3 for b in sp3 for c in sp3 for e in sp3)
gate('A3.4 traces: 6p^2 (4D); spatial 4|p_vec|^2; spatial components free of p4', sp.expand(tr4 - 6*sum(x**2 for x in P)) == 0 and sp.expand(tr3 - 4*(P[0]**2+P[1]**2+P[2]**2)) == 0 and indep, f'tr4={tr4}, tr3={tr3}')
gate('A3.5 T^I_{12,12} = p1^2+p2^2, T^I_{12,13} = p2 p3', sp.expand(TI(0,1,0,1) - P[0]**2 - P[1]**2) == 0 and sp.expand(TI(0,1,0,2) - P[1]*P[2]) == 0)

# ---------------- A4: K-subtracted remainder ----------------
okK = True; badK = True
for K in range(1, 7):
    lhs = 1/(u+s) - sum((1-u)**j/(1+s)**(j+1) for j in range(K))
    okK = okK and sp.simplify(sp.together(lhs - (1-u)**K/((u+s)*(1+s)**K))) == 0
    badK = badK and sp.simplify(sp.together(lhs - (1-u)**(K-1)/((u+s)*(1+s)**K))) != 0
gate('A4.1 remainder identity for K = 1..6', okK)
control('A4-F wrong exponent K-1 fails for every K', badK)
f2 = s*(u-1)**2/((u+s)*(1+s)**2)
pf = sp.apart(f2, s)
F = sp.integrate(pf, s)
F_inf = sp.limit(F, s, sp.oo)
S2 = sp.simplify(F_inf - F.subs(s, 1))
target = u*sp.log((u+1)/2) - (u-1)/2
diff_ = sp.simplify(sp.expand_log(S2 - target, force=True))
gate('A4.2 S2(u) = u log((u+1)/2) - (u-1)/2', diff_ == 0, f'partial fractions={pf}; S2={S2}')
l1 = sp.limit(target/u, u, sp.oo); l2 = sp.limit(target/u**2, u, sp.oo)
gate('A4.3 S2/u -> oo, S2/u^2 -> 0', l1 == sp.oo and l2 == 0, f'{l1}, {l2}')

# ---------------- A5: contact polynomials, Proposition CT ----------------
okk = True; badk = True
for k in range(0, 7):
    val = sp.integrate(u**(k+2)*sp.exp(-2*t*u), (u, 0, sp.oo))
    okk = okk and sp.simplify(val - sp.factorial(k+2)/(2*t)**(k+3)) == 0
    if k >= 1:
        badk = badk and sp.simplify(val - 1/(2*t)**(k+3)) != 0
gate('A5.1 int u^{k+2} e^{-2tu} = (k+2)!/(2t)^{k+3}, k=0..6', okk)
control('A5-F factorial dropped fails for every k >= 1', badk)
shat = 1/u - eps + eps**2*u
Fct = sp.simplify(t**2*sp.integrate(u**2*sp.exp(-2*t*u)*shat, (u, 0, sp.oo)))
target = sp.Rational(1,4) - eps/(4*t) + 3*eps**2/(8*t**2)
F1 = sp.Lambda(t, target.subs(eps, 1))
gate('A5.2 CT formula and the two signed differences', sp.simplify(Fct - target) == 0 and F1(8) - F1(4) == sp.Rational(7,512) and F1(1) - F1(sp.Rational(1,2)) == sp.Rational(-7,8), f'F(8)-F(4)={F1(8)-F1(4)}, F(1)-F(1/2)={F1(1)-F1(sp.Rational(1,2))}')
Pp = 1 + 2*u + 3*u**2
lhs = sp.simplify(t**2*sp.integrate(u**2*sp.exp(-2*t*u)*Pp, (u, 0, sp.oo)))
rhs = sum(c*sp.factorial(k+2)/(2**(k+3)*t**(k+1)) for k, c in enumerate([1, 2, 3]))
gate('A5.3 general contact formula on P = 1+2u+3u^2', sp.simplify(lhs - rhs) == 0, f'{lhs}')

# ---------------- A6: time-zero magnetic variant ----------------
om = sp.symbols('omega', positive=True)
a61 = sp.integrate(1/(2*sp.pi*(p0**2 + om**2)), (p0, -sp.oo, sp.oo))
gate('A6.1 int dp0/(2 pi (p0^2+w^2)) = 1/(2w)', sp.simplify(a61 - 1/(2*om)) == 0, f'{a61}')
JB0 = sp.integrate(v**3*sp.exp(-2*v**2), (v, 0, sp.oo))
gate('A6.2 J_B(0) = 1/8', JB0 == sp.Rational(1,8), f'{JB0}')
expr_u = u**4*sp.exp(-2*t*u**2)/sp.sqrt(u**2 + m**2)
sub = expr_u.subs(u, v/sp.sqrt(t))/sp.sqrt(t)
tgt = t**-2*v**4*sp.exp(-2*v**2)/sp.sqrt(v**2 + t*m**2)
gate('A6.3 substitution u = v/sqrt(t)', sp.simplify(sub/tgt) == 1)
val64 = sp.simplify((t**2/4)*sp.integrate((u**2/(2*sp.pi**2))*sp.exp(-2*t*u**2)*4*u**2/(2*u), (u, 0, sp.oo)))
gate('A6.4 massless time-zero value = 1/(32 pi^2) = J_B(0)/(4 pi^2)', sp.simplify(val64 - 1/(32*sp.pi**2)) == 0 and sp.simplify(JB0/(4*sp.pi**2) - val64) == 0, f'{val64}')
bad64 = sp.simplify((t**2/4)*sp.integrate((u**2/(2*sp.pi**2))*sp.exp(-2*t*u**2)*6*u**2/(2*u), (u, 0, sp.oo)))
control('A6-F 4D trace 6u^2 gives 3/(64 pi^2) != 1/(32 pi^2)', sp.simplify(bad64 - 1/(32*sp.pi**2)) != 0, f'{bad64}')
c1 = sp.integrate(1, (p0, -sp.oo, sp.oo)); c2 = sp.integrate(p0**2 + w**2, (p0, -sp.oo, sp.oo))
gate('A6.5 contact terms: Euclidean sharp-time integrals diverge', c1 == sp.oo and c2 == sp.oo, f'{c1}, {c2}')
sig = sp.symbols('sigma', positive=True)
dJ = sp.diff(v**4*sp.exp(-2*v**2)*(v**2 + sig)**sp.Rational(-1,2), sig)
gate('A6.6 d/dsigma of the J_B integrand = -(1/2) v^4 e^{-2v^2} (v^2+sigma)^{-3/2}', sp.simplify(dJ + sp.Rational(1,2)*v**4*sp.exp(-2*v**2)*(v**2+sig)**sp.Rational(-3,2)) == 0)

# ---------------- A7: Codex's massive-scalar example ----------------
x = sp.symbols('x', real=True)
g1 = sp.integrate(sp.exp(-2*t*x**2), (x, -sp.oo, sp.oo))
lhs4 = g1**4/(2*sp.pi)**4
rad = sp.Rational(1,16)/sp.pi**2*sp.integrate(u*sp.exp(-2*t*u), (u, 0, sp.oo))
gate('A7.1a radial measure d^4p/(2pi)^4 = u du/(16 pi^2) on e^{-2tu}', sp.simplify(lhs4 - rad) == 0 and sp.simplify(rad - 1/(64*sp.pi**2*t**2)) == 0, f'{sp.simplify(lhs4)}')
radbad = sp.Rational(1,8)/sp.pi**2*sp.integrate(u*sp.exp(-2*t*u), (u, 0, sp.oo))
control('A7-F radial measure 1/(8 pi^2) fails', sp.simplify(lhs4 - radbad) != 0)
subs7 = (u*sp.exp(-2*t*u)/(u + M_**2)).subs(u, v/t)/t
tgt7 = (1/t)*v*sp.exp(-2*v)/(v + M_**2*t)
gate('A7.1b substitution u = v/t', sp.simplify(subs7 - tgt7) == 0)
gate('A7.2 int_0^oo e^{-2v} dv = 1/2', sp.integrate(sp.exp(-2*v), (v, 0, sp.oo)) == sp.Rational(1,2))

allg = all(ok for _, ok in results); allc = all(f for _, f in controls)
print(f"gates: {sum(ok for _,ok in results)}/{len(results)} pass; controls: {sum(f for _,f in controls)}/{len(controls)} fire")
print('VERDICT:', 'PASS' if (allg and allc) else 'FAIL')
