#!/usr/bin/env python3
"""Reviewer's exact / semi-analytic checks, by routes different from c8_exact.py.
S1  half-density identity in a different formalism: 2-component Weyl operator sigma^a e_a^i (p_i + spin conn.)
    with the Euclidean 3D spin connection Gamma_i = (1/8) omega_iab [sigma_a, sigma_b]; flat-measure form
    gamma^(1/4) H gamma^(-1/4) = (1/2){sigma^a e_a^i, p_i} + O(h^2) for arbitrary symmetric h_ij(x).
S2  EH normalisation for TT modes along (110) and (111) (author did q || z only):
    cell average of sqrt(gamma) R^(3) at O(h^2) = -(1/4) <(d h)^2>.
S3  Dirac a1 coefficient via an exactly solvable spectrum: on the unit S^2 the Dirac spectrum is +-(n+1),
    degeneracy 2(n+1); the heat trace 4 sum m e^{-s m^2} = 2/s - 1/3 + O(s) fixes tr a1 = 2(R/6 + E) with
    E = -R/4 (R = 2), i.e. a1 = -R/12 per spinor component -> tr a1 = -R/3 in d = 4.
S4  proper-time matching with the 1/2 of det D = (det D^2)^(1/2): 1/(16 pi G) = Lambda^2/(96 pi^2);
    without the 1/2 one gets Lambda^2/(48 pi^2) (the repo note's matching line).
S5  cubic averages <sum q^4> = 3/5, <qx^2 qy^2 qz^2> = 1/105 and the fit inversion used for c_G^iso.
S6  continuum sharp-cutoff bubble int dOmega F2 = -52 pi/105 by a numerical 4x4 band-sum route.
S7  Lemma L algebra on random curves in R^5 (N(m + t^2 z) = O(t^4)).
"""
import sys, os
import numpy as np
import sympy as sp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
PASS = FAIL = 0
def check(n, ok):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok); print(('PASS' if ok else 'FAIL'), n, flush=True)

X = sp.symbols('x y z', real=True)
d = sp.Symbol('d')
# ---------------- S1
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
hm = sp.Matrix(3, 3, lambda i, j: sp.Function(f'h{min(i,j)}{max(i,j)}')(*X))
g = sp.eye(3) + d*hm; ginv = sp.eye(3) - d*hm
E = sp.eye(3) - d*hm/2            # E[a,i] = e_a^i  (inverse triad, symmetric gauge)
Ec = sp.eye(3) + d*hm/2           # e^a_i
Chr = [[[sum(ginv[a, l]*(sp.diff(g[l, b], X[c]) + sp.diff(g[l, c], X[b]) - sp.diff(g[b, c], X[l])) for l in range(3))/2
         for c in range(3)] for b in range(3)] for a in range(3)]
# Riemannian spin connection omega_i^a_b = e^a_j (d_i e_b^j + Chr^j_{ik} e_b^k)
om = [[[sp.expand(sum(Ec[a, j]*(sp.diff(E[b, j], X[i]) + sum(Chr[j][i][kk]*E[b, kk] for kk in range(3))) for j in range(3)))
        for b in range(3)] for a in range(3)] for i in range(3)]
om = [[[sp.expand(sp.series(om[i][a][b], d, 0, 2).removeO()) for b in range(3)] for a in range(3)] for i in range(3)]
Gam = [sum((om[i][a][b]*(sig[a]*sig[b] - sig[b]*sig[a]) for a in range(3) for b in range(3)), sp.zeros(2))/8 for i in range(3)]
psi = sp.Matrix([sp.Function('u')(*X), sp.Function('v')(*X)])
tr = hm.trace()
chi = (1 - d*tr/4)*psi
Hc = sp.zeros(2, 1)
for a in range(3):
    for i in range(3):
        Hc += -sp.I*sig[a]*E[a, i]*(sp.diff(chi, X[i]) + Gam[i]*chi)
Hc = (1 + d*tr/4)*Hc
Hs = sp.zeros(2, 1)
for a in range(3):
    for i in range(3):
        Hs += (-sp.I/2)*(sig[a]*E[a, i]*sp.diff(psi, X[i]) + sp.diff(sig[a]*E[a, i]*psi, X[i]))
diff = [sp.expand(sp.series(sp.expand(e), d, 0, 2).removeO()) for e in (Hc - Hs)]
check('S1 Weyl/Euclidean route: flat-measure covariant operator = (1/2){sigma e, p} + O(h^2), arbitrary symmetric h(x)',
      all(sp.simplify(e) == 0 for e in diff))
# sanity: the identity is not vacuous -- with the spin connection dropped it fails
Hc0 = sp.zeros(2, 1)
for a in range(3):
    for i in range(3):
        Hc0 += -sp.I*sig[a]*E[a, i]*sp.diff(chi, X[i])
Hc0 = (1 + d*tr/4)*Hc0
diff0 = [sp.expand(sp.series(sp.expand(e), d, 0, 2).removeO()) for e in (Hc0 - Hs)]
check('S1 control: dropping the spin connection breaks the identity (non-vacuous test)', any(sp.simplify(e) != 0 for e in diff0))

# ---------------- S2
def ricci_scalar(gm):
    gi = gm.inv()
    G = [[[sum(gi[a, l]*(sp.diff(gm[l, b], X[c]) + sp.diff(gm[l, c], X[b]) - sp.diff(gm[b, c], X[l])) for l in range(3))/2
           for c in range(3)] for b in range(3)] for a in range(3)]
    Ric = sp.zeros(3)
    for b in range(3):
        for c in range(3):
            Ric[b, c] = sum(sp.diff(G[a][b][c], X[a]) - sp.diff(G[a][b][a], X[c]) for a in range(3)) + \
                sum(G[a][a][l]*G[l][b][c] - G[a][c][l]*G[l][b][a] for a in range(3) for l in range(3))
    return sum(gi[b, c]*Ric[b, c] for b in range(3) for c in range(3))
ep, Q = sp.symbols('epsilon Q', positive=True)
for nm, qv, u1, u2 in (('(110)', sp.Matrix([1, 1, 0])/sp.sqrt(2), sp.Matrix([1, -1, 0])/sp.sqrt(2), sp.Matrix([0, 0, 1])),
                       ('(111)', sp.Matrix([1, 1, 1])/sp.sqrt(3), sp.Matrix([1, -1, 0])/sp.sqrt(2), sp.Matrix([1, 1, -2])/sp.sqrt(6))):
    for pol in 'AB':
        e = (u1*u1.T - u2*u2.T)/sp.sqrt(2) if pol == 'A' else (u1*u2.T + u2*u1.T)/sp.sqrt(2)
        ph = Q*(qv.T*sp.Matrix(X))[0]
        h = e*ep*sp.cos(ph)
        gm = sp.eye(3) + h
        # expand to O(eps^2) before taking the inverse-heavy Ricci: use series of metric inverse via ricci on truncated
        R = ricci_scalar(gm)
        dens = sp.sqrt(gm.det())*R
        d2 = sp.diff(dens, ep, 2).subs(ep, 0)/2
        # cell average along the phase variable: substitute a point and average over phase w = ph
        w = sp.Symbol('w')
        d2w = sp.simplify(d2.subs({X[0]: w/(Q*qv[0]) if qv[0] != 0 else 0, X[1]: 0, X[2]: 0})) if False else None
        # average numerically-exactly: d2 depends on x only through cos/sin of ph; sample on a line
        lin = {X[0]: sp.Symbol('t')*qv[0], X[1]: sp.Symbol('t')*qv[1], X[2]: sp.Symbol('t')*qv[2]}
        tt = sp.Symbol('t')
        avg = sp.integrate(sp.expand(sp.simplify(d2.subs(lin))), (tt, 0, 2*sp.pi/Q))*Q/(2*sp.pi)
        dh2 = sum(sp.diff(h[i, j], X[kk])**2 for i in range(3) for j in range(3) for kk in range(3))
        tgt = -sp.Rational(1, 4)*sp.integrate(sp.expand((sp.diff(dh2, ep, 2).subs(ep, 0)/2).subs(lin)), (tt, 0, 2*sp.pi/Q))*Q/(2*sp.pi)
        check(f'S2 EH normalisation q || {nm} pol {pol}: <sqrt(g) R>_2 = {sp.simplify(avg)} = -(1/4)<(dh)^2>_2 = {sp.simplify(tgt)}',
              sp.simplify(avg - tgt) == 0 and sp.simplify(tgt + Q**2/8) == 0)

# ---------------- S3
for s_ in (1e-2, 3e-3, 1e-3):
    m = np.arange(1, 200000)
    K = 4*np.sum(m*np.exp(-s_*m**2))
    print(f'   S^2 Dirac heat trace s={s_}: K - 2/s = {K - 2/s_:.8f}  (prediction -1/3 + O(s))')
check('S3 unit-S^2 Dirac heat trace: K(s) - 2/s -> -1/3, i.e. tr a1 = 2(R/6 - R/4) at R = 2 (E = -R/4 confirmed)',
      abs(4*np.sum(np.arange(1, 400000)*np.exp(-1e-4*np.arange(1, 400000)**2)) - 2/1e-4 + 1/3) < 1e-3)

# ---------------- S4
s, Lam, R = sp.symbols('s Lambda R', positive=True)
tra1 = 4*(R/6 - R/4)
Gam_half = sp.Rational(1, 2)*sp.integrate((4*sp.pi*s)**-2*s*tra1/s, (s, 1/Lam**2, sp.oo))   # Gamma_E = -1/2 log det D^2
Gam_full = sp.integrate((4*sp.pi*s)**-2*s*tra1/s, (s, 1/Lam**2, sp.oo))                   # -log det D^2 (no 1/2)
inv16piG_half = sp.simplify(-Gam_half/R); inv16piG_full = sp.simplify(-Gam_full/R)
print('   1/(16 pi G) with the 1/2:', inv16piG_half, '; without:', inv16piG_full)
check('S4 Dirac: 1/(16 pi G) = Lambda^2/(96 pi^2) (with det D = (det D^2)^(1/2)); the repo line (4pi)^-2 (1/3) Lambda^2 = Lambda^2/(48 pi^2) is the no-1/2 value',
      sp.simplify(inv16piG_half - Lam**2/(96*sp.pi**2)) == 0 and sp.simplify(inv16piG_full - (4*sp.pi)**-2*sp.Rational(1, 3)*Lam**2) == 0)
Gs = sp.symbols('G', positive=True)
sol_half = sp.solve(sp.Eq(1/(16*sp.pi*Gs), Lam**2/(96*sp.pi**2)), Gs)[0]
check(f'S4 consequence: G = {sp.simplify(sol_half*Lam**2)}/Lambda^2 per Dirac fermion (repo matching line gives 3 pi)', sp.simplify(sol_half*Lam**2 - 6*sp.pi) == 0)

# ---------------- S5
th, ph = sp.symbols('theta phi', real=True)
nx, ny, nz = sp.sin(th)*sp.cos(ph), sp.sin(th)*sp.sin(ph), sp.cos(th)
avg = lambda f: sp.integrate(sp.integrate(f*sp.sin(th), (ph, 0, 2*sp.pi)), (th, 0, sp.pi))/(4*sp.pi)
a4 = sp.simplify(avg(nx**4 + ny**4 + nz**4)); a6 = sp.simplify(avg(nx**2*ny**2*nz**2))
check(f'S5 <sum q^4> = {a4}, <qx^2qy^2qz^2> = {a6}', a4 == sp.Rational(3, 5) and a6 == sp.Rational(1, 105))
A_, B_, C_ = sp.symbols('A B C')
Kf = lambda q: A_ + B_*sum(qi**4 for qi in q) + C_*q[0]**2*q[1]**2*q[2]**2
Kz = Kf([0, 0, 1]); Kff = Kf([1/sp.sqrt(2), 1/sp.sqrt(2), 0]); Kd = Kf([1/sp.sqrt(3)]*3)
Bfit = 2*(Kz - Kff); Afit = Kz - Bfit; Cfit = 27*(Kd - Afit - Bfit/3)
check('S5 author fit inversion B = 2(Kz-Kf), A = Kz-B, C = 27(Kd-A-B/3) is exact', all(sp.simplify(x) == 0 for x in (Bfit - B_, Afit - A_, Cfit - C_)))

# ---------------- S6 continuum sharp cutoff by band sums (own numerics)
import r8_walk as rw
al = [-m for m in rw.T3S]
def contF(k, t, qh, eps):
    def bands(kk):
        Hm = sum(kk[:, a, None, None]*al[a] for a in range(3))
        w, V = np.linalg.eigh(Hm); return w, V
    o = 0.5*np.einsum('ij,nj->ni', eps, k)
    Vm = -sum(o[:, a, None, None]*al[a] for a in range(3))      # -(1/2) eps_ij alpha_i k_j
    class Wd: pass
    return rw.bubble(None, Vm, None, None, bands(k + t*qh), bands(k - t*qh)) if False else _bub(Vm, bands(k + t*qh), bands(k - t*qh))
def _bub(Vm, ba, bb):
    oa, Va = ba; ob, Vb = bb
    Mx = np.einsum('nji,njk,nkl->nil', np.conj(Va), Vm, Vb); m2 = np.abs(Mx)**2
    occa, occb = oa < 0, ob < 0; gap = oa[:, :, None] - ob[:, None, :]
    w = np.where((~occa)[:, :, None] & occb[:, None, :], 1/gap, 0) + np.where(occa[:, :, None] & (~occb)[:, None, :], -1/gap, 0)
    return np.sum(m2*w, (1, 2))
xg, wg = np.polynomial.legendre.leggauss(40); nph = 80
phs = 2*np.pi*np.arange(nph)/nph
MU, PH = np.meshgrid(xg, phs, indexing='ij'); WT = (wg[:, None]*np.full(nph, 2*np.pi/nph)[None, :]).ravel()
st = np.sqrt(1 - MU**2)
nvec = np.stack([(st*np.cos(PH)).ravel(), (st*np.sin(PH)).ravel(), MU.ravel()], 1)
J5 = np.arange(5.0); ROW1 = np.linalg.inv(np.array([[j**(2*m) for m in range(5)] for j in J5]))[1]
for qn, qh, u1, u2 in (('z', np.array([0, 0, 1.0]), np.array([1.0, 0, 0]), np.array([0, 1.0, 0])),
                       ('d', np.ones(3)/np.sqrt(3), np.array([1.0, -1, 0])/np.sqrt(2), np.array([1.0, 1, -2])/np.sqrt(6))):
    for pol in 'AB':
        eps = (np.outer(u1, u1) - np.outer(u2, u2))/np.sqrt(2) if pol == 'A' else (np.outer(u1, u2) + np.outer(u2, u1))/np.sqrt(2)
        hst = 0.01
        Fv = np.array([contF(nvec, j*hst, qh, eps) for j in range(5)])
        F2 = ROW1 @ Fv/hst**2
        J = np.sum(WT*F2)
        print(f'   continuum q||{qn} pol {pol}: int dOmega F2 = {J:.12f}  vs -52 pi/105 = {-52*np.pi/105:.12f}')
        check(f'S6 continuum sharp-cutoff angular integral q||{qn}{pol} = -52 pi/105 (rel 1e-8) => c_G = 13 Lambda^2/(840 pi^2)',
              abs(J + 52*np.pi/105) < 1e-8*52*np.pi/105)

# ---------------- S7
rng = np.random.default_rng(3)
def unit_curve(t, c):
    v = c[0] + t*c[1] + t**2*c[2] + t**3*c[3]
    return v/np.linalg.norm(v)
ok = True
for trial in range(20):
    c = rng.normal(size=(4, 5)); z = rng.normal(size=5)
    vals = []
    for t in (1e-2, 5e-3):
        a = unit_curve(t, c); b = unit_curve(-t, c); m = unit_curve(0.0, c)
        o = m + t**2*z
        Mt = (1 + a @ b)*np.eye(5) - (np.outer(a, b) + np.outer(b, a))
        vals.append(o @ Mt @ o)
    ratio = vals[0]/vals[1]
    ok &= abs(ratio - 16) < 0.2
check('S7 Lemma L: N(m + t^2 z) scales as t^4 on 20 random curves (ratio for t-halving = 16)', ok)
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
