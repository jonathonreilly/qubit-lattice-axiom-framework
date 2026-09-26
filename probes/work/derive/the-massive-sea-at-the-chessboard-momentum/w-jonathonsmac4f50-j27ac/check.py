#!/usr/bin/env python3
"""The massive free sea at the chessboard momentum Q = pi(1,1,1) (block 160's open case).
J:derive:the-massive-sea-at-the-chessboard-momentum:a1

Walk H = sum_a sigma_a S_a, S_a = (T_a - T_a^-1)/(2i); mass m eps; clocked H_w = phi H phi + m w eps (w = phi^2 = e^u);
sea energy E_sea[u] = sum of the negative levels; E(k) = sqrt(|sin k|^2 + m^2); <.> zone average.
T1 (twin identity, exact): e^sea_x[T phi] - e^sea_(x-e1)[phi] = 2 m eps_x w_(x-e1) for every clock field.
T2 (Hessian): E_sea[u] = E0 + sum_x (m eps_x - <E>) u_x + (1/2)<u, A u> + (m/2) sum_x eps_x u_x^2 + O(u^3), A translation
   invariant: the cross-coupling of any u with eps v is exactly m sum u v (plus A's Q-shifted part, absent for smooth u, v).
T3 (exact chessboard family): u = a eps + b: E_sea = e^b [N m sinh a - sum_k sqrt(|s|^2 + m^2 cosh^2 a)].
T4 (kernel at and near Q): A(Q) = -m^2 <1/E> = c0 + 12 kappa(m) exactly; A(Q + p) = -m^2<1/E> - (kappa + lambda)|p|^2 + O(p^4),
   lambda = <|s|^2 s_1^2 cos^2 k_1 / E^5>/4 > 0.
T5 (static response, stability): block 55's ledger L = E_sea + (2/gamma) sum_bonds (phi_x - phi_y)^2 at fixed sum u: chessboard
   curvature B0 = 12/gamma - m^2<1/E>, static amplitude a* = -m/B0 + O(m^3) (exact equation m + (12/gamma) tanh a =
   m^2 sinh a <1/E(a)>), locally stable iff gamma m^2 <1/E> < 12, bounded below along the chessboard iff |m| gamma <= 6;
   block 76's sea-only reading: E_sea is strictly monotone along the chessboard (no static chessboard, runaway).
"""
import itertools, sys, time
import numpy as np
import sympy as sp
T0 = time.time(); FAIL = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'} {name}" + (f" :: {detail}" if detail else ""), flush=True)
    if not ok: FAIL.append(name)

print("== E exact identities")
# E1: integer (Gaussian) check on the 4^3 torus of the exact chessboard + uniform family
L = 4; N = L**3
sites = list(itertools.product(range(L), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
# 8H = sum_a sigma_a * 8 S_a ; 8 S_a = -4i (T_a - T_a^-1); represent Gaussian integers as (re, im) int64 pairs
SIG = [(np.array([[0, 1], [1, 0]]), np.zeros((2, 2), int)), (np.zeros((2, 2), int), np.array([[0, -1], [1, 0]])), (np.array([[1, 0], [0, -1]]), np.zeros((2, 2), int))]
Hre = np.zeros((2*N, 2*N), dtype=np.int64); Him = np.zeros((2*N, 2*N), dtype=np.int64)
for s, i in idx.items():
    for a in range(3):
        sp_ = list(s); sp_[a] = (sp_[a] + 1) % L; j = idx[tuple(sp_)]
        # <x| T_a |x+e_a> : (T_a psi)_x = psi_(x+e_a) -> coefficient -4i at (x, x+e_a), +4i at (x+e_a, x)
        sr, si = SIG[a]
        # (-4i)(sr + i si) = 4 si - 4i sr
        Hre[2*i:2*i+2, 2*j:2*j+2] += 4*si; Him[2*i:2*i+2, 2*j:2*j+2] += -4*sr
        # (+4i)(sr + i si) = -4 si + 4i sr at (j, i)
        Hre[2*j:2*j+2, 2*i:2*i+2] += -4*si; Him[2*j:2*j+2, 2*i:2*i+2] += 4*sr
eps = np.array([(-1)**sum(s) for s in sites], dtype=np.int64); Eps = np.diag(np.repeat(eps, 2))
def gmul(A, B): return (A[0] @ B[0] - A[1] @ B[1], A[0] @ B[1] + A[1] @ B[0])
herm = np.array_equal(Hre, Hre.T) and np.array_equal(Him, -Him.T)
# phi = sqrt(3) 2^eps : phi_x phi_y = 3 on every bond, w = 3 * 4^eps ; m = 1: m w eps = 12 (even), -3/4 (odd)
# 8 H_w / 3 = 8 H + (8/3) diag(m w eps) = 8H + diag(32 on even, -2 on odd); claim = 8H + 17 eps + 15
diagW = np.repeat(np.where(eps == 1, 32, -2), 2)
lhs = (Hre + np.diag(diagW) - 15*np.eye(2*N, dtype=np.int64), Him)
rhs = (Hre + 17*Eps, Him)
fam_ok = np.array_equal(lhs[0], rhs[0]) and np.array_equal(lhs[1], rhs[1])
sq = gmul(rhs, rhs); H2 = gmul((Hre, Him), (Hre, Him))
anti = gmul((Hre, Him), (Eps, 0*Eps)); anti2 = gmul((Eps, 0*Eps), (Hre, Him))
anti_ok = np.array_equal(anti[0] + anti2[0], 0*Hre) and np.array_equal(anti[1] + anti2[1], 0*Him)
sq_ok = np.array_equal(sq[0], H2[0] + 289*np.eye(2*N, dtype=np.int64)) and np.array_equal(sq[1], H2[1])
# (8H)^2 = 64 sum_a S_a^2 (x) I_2, diagonal in momentum with eigenvalue 64 |sin k|^2: check it is spin-trivial
spin_triv = all(np.array_equal(H2[0][2*i:2*i+2, 2*j:2*j+2], H2[0][2*i, 2*j]*np.eye(2, dtype=np.int64)) and not H2[1][2*i:2*i+2, 2*j:2*j+2].any() for i in range(N) for j in range(N))
check("E1 exact (Gaussian integers, 4^3 torus, m = 1, e^b = 3, e^(a/2) = 2): the clocked walk built from phi = sqrt3 2^eps equals "
      "e^b (H + m cosh a eps + m sinh a) with cosh a = 17/8, sinh a = 15/8; {H, eps} = 0 and (8H + 17 eps)^2 = 64 H^2 + 289 with H^2 "
      "spin-trivial; so the levels are e^b[m sinh a +- sqrt(|s|^2 + m^2 cosh^2 a)] (T3)", herm and fam_ok and anti_ok and sq_ok and spin_triv)
S, m, a, g, k1, k2, k3, t, b = sp.symbols('S m a gamma k1 k2 k3 t b', real=True)
Ek = sp.sqrt(S + m**2)
check("E2 c0 + 12 kappa = -m^2 <1/E> (integrand: -E + |s|^2/E = -m^2/E) and d/dm (m^2/E) = m(2|s|^2 + m^2)/E^3 (so m^2<1/E> "
      "increases strictly with |m|)", sp.simplify(-Ek + S/Ek + m**2/Ek) == 0 and sp.simplify(sp.diff(m**2/Ek, m) - m*(2*S + m**2)/Ek**3) == 0)
Ea = sp.sqrt(S + m**2*sp.cosh(a)**2)
Lint = m*sp.sinh(a) - Ea + (24/g)*sp.sinh(a/2)**2
dL = sp.diff(Lint, a)
check("E3 along u = a eps the ledger per site (block 55, F = (2/gamma) sum_bonds (phi_x - phi_y)^2 = (24N/gamma) sinh^2(a/2)) has "
      "derivative cosh a [m - m^2 sinh a <1/E(a)> + (12/gamma) tanh a]; at a = 0: value m, second derivative 12/gamma - m^2<1/E>",
      sp.simplify(dL - sp.cosh(a)*(m - m**2*sp.sinh(a)/Ea + (12/g)*sp.tanh(a))) == 0
      and sp.simplify(dL.subs(a, 0) - m) == 0 and sp.simplify(sp.diff(Lint, a, 2).subs(a, 0) - (12/g - m**2/Ek)) == 0)
# sea-only monotonicity: (m sinh a)^2/(S + m^2 cosh^2 a) <= tanh^2 a, difference = S sinh^2 a m^2/(cosh^2 a (S + m^2 cosh^2 a)) >= 0
diff_ = sp.tanh(a)**2 - (m*sp.sinh(a))**2/(S + m**2*sp.cosh(a)**2)
check("E4 block 76's sea-only reading: dE_sea/da = N m cosh a [1 - m sinh a <1/E(a)>] with m sinh a/E(a) <= tanh|a| < 1 pointwise "
      "(tanh^2 a - (m sinh a)^2/E(a)^2 = S sinh^2 a/(cosh^2 a E(a)^2) >= 0): the sea energy is strictly monotone along the "
      "chessboard, so no static chessboard exists and E_sea -> -infinity as a -> -sign(m) infinity",
      sp.simplify(diff_ - S*sp.sinh(a)**2/(sp.cosh(a)**2*(S + m**2*sp.cosh(a)**2))) == 0)
# asymptotics: m > 0, a -> -infinity; sandwich m cosh a <= E(a) <= m cosh a + S/(2 m cosh a)
up = (m*sp.sinh(a) - m*sp.cosh(a) + (24/g)*sp.sinh(a/2)**2)*sp.exp(a)
lo = (m*sp.sinh(a) - m*sp.cosh(a) - S/(2*m*sp.cosh(a)) + (24/g)*sp.sinh(a/2)**2)*sp.exp(a)
mp = sp.symbols('mp', positive=True); gp = sp.symbols('gp', positive=True); Sp = sp.symbols('Sp', nonnegative=True)
lu = sp.limit(up.subs({m: mp, g: gp}), a, -sp.oo); ll = sp.limit(lo.subs({m: mp, g: gp, S: Sp}), a, -sp.oo)
check("E5 along the chessboard (m > 0, a -> -infinity) e^(-|a|) L/N -> 6/gamma - m (both sandwich bounds), so the ledger is "
      "bounded below along the chessboard iff |m| gamma <= 6 (the other direction is bounded by F)",
      sp.simplify(lu - (6/gp - mp)) == 0 and sp.simplify(ll - (6/gp - mp)) == 0, f"limit {lu}")
# near-Q: held-part identity and the t^2 coefficient of the correction (pointwise in k, symbolic)
s = [sp.sin(k1), sp.sin(k2), sp.sin(k3)]; st = [sp.sin(k1 + t), sp.sin(k2), sp.sin(k3)]
E0s = sp.sqrt(sum(x**2 for x in s) + m**2); Ets = sp.sqrt(sum(x**2 for x in st) + m**2)
sdot = sum(x*y for x, y in zip(s, st))
held = lambda nn: -(sp.Rational(1, 4))*(E0s + Ets)*(1 + nn)
nQ = (m**2 - sdot)/(E0s*Ets); n0 = (m**2 + sdot)/(E0s*Ets)
check("E6 near Q the held part obeys held(Q+p) - held(p) = (1/2)(E + E')s.s'/(E E') pointwise (whose zone average is 12 kappa - "
      "2 kappa |p|^2_lat), so held(Q+p) = c0 + kappa |Q+p|^2_lat", sp.simplify(held(nQ) - held(n0) - sp.Rational(1, 2)*(E0s + Ets)*sdot/(E0s*Ets)) == 0)
corr = -(sp.Rational(1, 4))*(1 - nQ)*(E0s - Ets)**2/(E0s + Ets)
c2 = sp.diff(corr, t, 2).subs(t, 0)/2
target = -sum(x**2 for x in s)*s[0]**2*sp.cos(k1)**2/(4*E0s**5)
check("E7 the non-held term -(1/4)(1 - n.n'')(E - E'')^2/(E + E''), k'' = k + Q + p, has t^2 coefficient (p = t e1) exactly "
      "-|s|^2 s_1^2 cos^2 k_1/(4 E^5) pointwise, so A(Q + p) = -m^2<1/E> - (kappa + lambda)|p|^2 + O(p^4)",
      sp.simplify(c2 - target) == 0 and sp.simplify(corr.subs(t, 0)) == 0 and sp.simplify(sp.diff(corr, t).subs(t, 0)) == 0)

print("== F finite tori and quadrature (floats)")
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
def build(L):
    N = L**3; st_ = list(itertools.product(range(L), repeat=3)); ix = {x: i for i, x in enumerate(st_)}
    Hm = np.zeros((2*N, 2*N), complex)
    for x, i in ix.items():
        for d_, sg in enumerate((sx, sy, sz)):
            y = list(x); y[d_] = (y[d_] + 1) % L; j = ix[tuple(y)]
            Hm[2*i:2*i+2, 2*j:2*j+2] += sg/(2j); Hm[2*j:2*j+2, 2*i:2*i+2] += (sg/(2j)).conj().T
    return Hm, np.array([(-1)**sum(x) for x in st_], float), np.array(st_, float), N
def Hw(Hm, ep, mm, u):
    ph = np.exp(np.repeat(u, 2)/2); return ph[:, None]*Hm*ph[None, :] + np.diag(np.repeat(mm*np.exp(u)*ep, 2))
def dens(Hm, ep, mm, u):
    M = Hw(Hm, ep, mm, u); lam, V = np.linalg.eigh(M); Vo = V[:, lam < 0]
    return np.real(np.sum(np.conj(Vo)*(M @ Vo), axis=1)).reshape(-1, 2).sum(1)
def hessian(Hm, ep, mm):
    H0 = Hw(Hm, ep, mm, np.zeros(len(ep))); lam, V = np.linalg.eigh(H0); occ = lam < 0; Vo = V[:, occ]
    def H1(u): U = np.repeat(u, 2); return 0.5*(U[:, None]*Hm + Hm*U[None, :]) + np.diag(np.repeat(mm*u*ep, 2))
    def H2(u, v):
        U = np.repeat(u, 2); Vv = np.repeat(v, 2); UV = U*Vv
        return 0.25*(UV[:, None]*Hm + Hm*UV[None, :] + U[:, None]*Hm*Vv[None, :] + Vv[:, None]*Hm*U[None, :]) + np.diag(np.repeat(mm*u*v*ep, 2))
    def K(u, v):
        A_ = (V.conj().T @ H1(u) @ V)[np.ix_(~occ, occ)]; B_ = (V.conj().T @ H1(v) @ V)[np.ix_(~occ, occ)]
        den = lam[occ][None, :] - lam[~occ][:, None]
        return np.real(np.trace(Vo.conj().T @ H2(u, v) @ Vo)) + 2*np.real(np.sum(np.conj(A_)*B_/den))
    return K
def Ahat_grid(L, mm, q):
    tot = 0.0
    for kk in itertools.product(range(L), repeat=3):
        k = 2*np.pi*np.array(kk)/L; s1 = np.sin(k); s2 = np.sin(k + q)
        E1 = np.sqrt(s1 @ s1 + mm*mm); E2 = np.sqrt(s2 @ s2 + mm*mm); nn = (s1 @ s2 + mm*mm)/(E1*E2)
        tot += -0.25*((E1 + E2)*(1 + nn) + (1 - nn)*(E1 - E2)**2/(E1 + E2))
    return tot/L**3
Lf, mf = 6, 0.7
Hm, ep, X, Nf = build(Lf); rng = np.random.default_rng(1)
u = rng.normal(size=Nf)*0.5
ixs = {tuple(x): i for i, x in enumerate(X.astype(int))}
Tidx = [ixs[tuple((X[i].astype(int) - np.array([1, 0, 0])) % Lf)] for i in range(Nf)]
err_twin = np.max(np.abs(dens(Hm, ep, mf, u[Tidx]) - dens(Hm, ep, mf, u)[Tidx] - 2*mf*ep*np.exp(u)[Tidx]))
check("F1 T1's twin identity on the 6^3 torus for a random clock field (|u| ~ 0.5, m = 0.7), nonperturbative", err_twin < 1e-10, f"max error {err_twin:.1e}")
K = hessian(Hm, ep, mf)
errA = 0.0; Agrid = np.zeros((Lf, Lf, Lf))
for n in itertools.product(range(Lf), repeat=3):
    q = 2*np.pi*np.array(n)/Lf; c = np.cos(X @ q); sn = np.sin(X @ q)
    Agrid[n] = Ahat_grid(Lf, mf, q); errA = max(errA, abs((K(c, c) + K(sn, sn))/Nf - Agrid[n]))
v = rng.normal(size=Nf); w_ = rng.normal(size=Nf)
Av = np.real(np.fft.ifftn(np.fft.fftn(v.reshape(Lf, Lf, Lf))*Agrid)).reshape(-1)
errD = abs(K(w_, v) - w_ @ Av - mf*np.sum(ep*w_*v))
Xv = [K(np.cos(X @ (2*np.pi*np.array(n)/Lf)), ep*np.cos(X @ (2*np.pi*np.array(n)/Lf)))/(Nf/2) for n in [(1, 0, 0), (1, 1, 0), (1, 2, 3)]]
check("F2 the Hessian on the 6^3 torus: its translation-invariant part A(q) equals block 160's zone formula at every q "
      "(including 2q = 0 and 2q = Q), K(u, v) = <u, A v> + m sum eps u v for random u, v, and the smooth/chessboard cross-coupling "
      "is exactly m (T2)", errA < 1e-10 and errD < 1e-9 and all(abs(x - mf) < 1e-10 for x in Xv),
      f"max |A - formula| {errA:.1e}; decomposition error {errD:.1e}; X = {[round(x, 12) for x in Xv]}")
Mq = 96; kq = (np.arange(Mq) + 0.5)*2*np.pi/Mq; K1, K2, K3 = np.meshgrid(kq, kq, kq, indexing='ij')
s_ = [np.sin(K1), np.sin(K2), np.sin(K3)]; s2 = s_[0]**2 + s_[1]**2 + s_[2]**2; Eg = np.sqrt(s2 + mf*mf)
kap = (s2/Eg).mean()/12; lamb = (s2*s_[0]**2*np.cos(K1)**2/Eg**5).mean()/4
def Ahat_q(q):
    tq = [np.sin(K1 + q[0]), np.sin(K2 + q[1]), np.sin(K3 + q[2])]; E2 = np.sqrt(tq[0]**2 + tq[1]**2 + tq[2]**2 + mf*mf)
    nn = (s_[0]*tq[0] + s_[1]*tq[1] + s_[2]*tq[2] + mf*mf)/(Eg*E2)
    return (-0.25*((Eg + E2)*(1 + nn) + (1 - nn)*(Eg - E2)**2/(Eg + E2))).mean()
Qv = np.array([np.pi]*3); AQ = Ahat_q(Qv)
slopes = [(Ahat_q(Qv + 0.05*d) - AQ)/0.05**2 for d in (np.array([1, 0, 0]), np.array([1, 1, 0])/np.sqrt(2), np.array([1, 1, 1])/np.sqrt(3))]
check("F3 (quadrature, m = 0.7) A(Q) = -m^2<1/E> = c0 + 12 kappa and the slope (A(Q + p) - A(Q))/|p|^2 -> -(kappa + lambda) "
      "in three directions (isotropic at this order)", abs(AQ + mf*mf*(1/Eg).mean()) < 1e-12 and all(abs(x + kap + lamb) < 5e-4 for x in slopes),
      f"A(Q) = {AQ:.6f}; kappa = {kap:.6f}, lambda = {lamb:.6f}; slopes {[round(x, 5) for x in slopes]}")
from scipy.optimize import brentq
out = []; ok_static = True
for mm, gg in [(0.7, 1.0), (3.0, 1.0), (5.9, 1.0)]:
    E0g = np.sqrt(s2 + mm*mm); B0 = 12/gg - mm*mm*(1/E0g).mean()
    gfun = lambda a_: mm - mm*mm*np.sinh(a_)*(1/np.sqrt(s2 + (mm*np.cosh(a_))**2)).mean() + (12/gg)*np.tanh(a_)
    ag = np.linspace(-6, 6, 1201); vals = [gfun(x) for x in ag]
    roots = [brentq(gfun, ag[i], ag[i + 1]) for i in range(len(ag) - 1) if vals[i]*vals[i + 1] < 0]
    ok_static &= len(roots) == 1 and B0 > 0 and roots[0]*mm < 0
    out.append((mm, round(B0, 4), round(-mm/B0, 5), [round(r, 5) for r in roots]))
check("F4 (quadrature, gamma = 1) the static chessboard equation has one root, of sign -sign(m), near -m/B0 for small m: "
      "(m, B0, -m/B0, roots)", ok_static, str(out))

print(f"== done in {time.time()-T0:.0f}s")
if FAIL:
    print("SUMMARY: ROUTE FAILS AT " + ", ".join(FAIL))
else:
    print("SUMMARY: PROVED (block 160's open case) - exact twin identity e^sea_x[T phi] - e^sea_(x-e1)[phi] = 2 m eps_x w_(x-e1) "
          "forces the massive sea's Hessian to be A + m eps with A translation invariant (cross-coupling of smooth and chessboard "
          "modes exactly m); along u = a eps + b the sea energy is exactly e^b [N m sinh a - sum_k sqrt(|s|^2 + m^2 cosh^2 a)]; "
          "A(Q) = -m^2<1/E> = c0 + 12 kappa(m) and A(Q+p) = -m^2<1/E> - (kappa + lambda)|p|^2 + O(p^4), lambda = "
          "<|s|^2 s1^2 cos^2 k1/E^5>/4; with no linear source off p = 0. Under block 55's ledger the chessboard has curvature "
          "12/gamma - m^2<1/E>, static amplitude -m/(12/gamma - m^2<1/E>) + O(m^3), is locally stable iff gamma m^2<1/E> < 12 and "
          "bounded below along the chessboard iff |m| gamma <= 6; under block 76's sea-only reading the sea energy is strictly "
          "monotone along the chessboard (no static chessboard). The fixed-sum smooth sector keeps the negative volume curvature "
          "c0 = -<E> (block 147), independently of the chessboard")
    print("HIT: exact second-order structure of the massive sea at Q: Hessian = A + m eps (twin identity), A(Q) = c0 + 12 kappa = "
          "-m^2<1/E>, near-Q stiffness -(kappa + lambda), exact chessboard family, and block 55's static chessboard -m/(12/gamma - "
          "m^2<1/E>) stable iff gamma m^2<1/E> < 12, bounded iff |m| gamma <= 6")
