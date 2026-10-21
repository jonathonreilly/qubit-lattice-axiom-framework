#!/usr/bin/env python3
"""C8 exact (sympy) part. Every check is an exact symbolic identity; nothing is fitted.

E1. Einstein-Hilbert normalisation: for a static spatial metric gamma = 1 + h with h a
    single transverse-traceless (TT) Fourier mode, int sqrt(gamma) R^(3) = -(1/4) int (d h)^2
    + O(h^3) (cell average), for both TT polarisations with q along z.
E2. Continuum minimal coupling: for the symmetric triad e = 1 - h/2 + O(h^2) and arbitrary
    symmetric h_ij(x), the half-density (flat-measure) Dirac Hamiltonian
    gamma^(1/4) [-i alpha^a e_a^i (d_i + Gamma_i)] gamma^(-1/4) equals
    (1/2){alpha^a e_a^i, p_i} to first order in h, acting on an arbitrary spinor field.
E3. Heat-kernel reference: one Dirac fermion, proper-time cutoff s > 1/Lambda^2:
    Gamma_E = -1/2 log det D^2 contains -(Lambda^2/96 pi^2) int sqrt(g) R,
    so 1/(16 pi G) = Lambda^2/(96 pi^2).
E4. Clifford trace identity used by the lattice runner:
    Tr[P+(a) O P-(b) O] = o^2 (1 + a.b) - 2 (a.o)(b.o) for P+(a) = (1 - a.Gamma)/2,
    P-(b) = (1 + b.Gamma)/2, O = o.Gamma, with the 5 anticommuting Gammas of the walk.
E5. Series of rho(f) = arccos(f)/sqrt(1-f^2) and rho'(f) at f = 1 used for small u = 1-f.
"""
from __future__ import annotations

import sys

import sympy as sp

PASS = FAIL = 0


def check(name, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS [exact] {name}")
    else:
        FAIL += 1
        print(f"FAIL [exact] {name}")


x, y, z = X = sp.symbols('x y z', real=True)
q, eps, lam = sp.symbols('q epsilon lambda', positive=True)

# ------------------------------------------------------------------ E1  EH normalisation


def ricci_scalar(g, coords):
    n = len(coords)
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
                 for d in range(n))/2 for c in range(n)] for b in range(n)] for a in range(n)]
    R = 0
    for b in range(n):
        for c in range(n):
            Rbc = 0
            for a in range(n):
                Rbc += sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
                for d in range(n):
                    Rbc += Gam[a][a][d]*Gam[d][b][c] - Gam[a][c][d]*Gam[d][b][a]
            R += gi[b, c]*Rbc
    return R


for name, hmat in (('T2g (h_xy)', sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])),
                   ('Eg (h_xx = -h_yy)', sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))):
    h = hmat*eps*sp.cos(q*z)
    g = sp.eye(3) + h
    R = ricci_scalar(g, X)
    dens = sp.sqrt(g.det())*R
    d2 = sp.diff(dens, eps, 2).subs(eps, 0)/2          # O(eps^2) coefficient
    avg = sp.integrate(sp.simplify(d2), (z, 0, 2*sp.pi/q))*q/(2*sp.pi)
    dh2 = sum(sp.diff(h[i, j], X[k])**2 for i in range(3) for j in range(3) for k in range(3))
    target = -sp.Rational(1, 4)*sp.integrate(sp.diff(dh2, eps, 2).subs(eps, 0)/2, (z, 0, 2*sp.pi/q))*q/(2*sp.pi)
    print(f"  {name}: <sqrt(g) R>_2 = {sp.simplify(avg)},  -(1/4)<(dh)^2>_2 = {sp.simplify(target)}")
    check(f'E1 {name}: cell average of sqrt(gamma) R at O(h^2) = -(1/4) <(d h)^2>', sp.simplify(avg - target) == 0)
    lin = sp.integrate(sp.diff(dens, eps).subs(eps, 0), (z, 0, 2*sp.pi/q))
    check(f'E1 {name}: O(h) term integrates to zero', sp.simplify(lin) == 0)

# ------------------------------------------------------------------ E2  minimal coupling at O(h)
s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
Z2 = sp.zeros(2)
kr = sp.kronecker_product
alpha = [sp.Matrix(sp.BlockMatrix([[Z2, s], [s, Z2]])) for s in (s1, s2, s3)]
beta = sp.Matrix(sp.BlockMatrix([[sp.eye(2), Z2], [Z2, -sp.eye(2)]]))
gam = [beta*a for a in alpha]                       # spatial gamma^a = beta alpha^a
d = sp.Symbol('delta')                              # bookkeeping for O(h)
hf = [[sp.Function(f'h{min(i, j)}{max(i, j)}')(x, y, z) for j in range(3)] for i in range(3)]
hm = sp.Matrix(3, 3, lambda i, j: hf[i][j])
gmet = sp.eye(3) + d*hm                              # gamma_ij
einv = sp.eye(3) - d*hm/2                           # e_a^i (symmetric gauge), O(h)
ecov = sp.eye(3) + d*hm/2                           # e^a_i
gi = sp.eye(3) - d*hm
Chr = [[[sp.expand(sum(gi[a, l]*(sp.diff(gmet[l, b], X[c]) + sp.diff(gmet[l, c], X[b]) - sp.diff(gmet[b, c], X[l]))
                       for l in range(3))/2) for c in range(3)] for b in range(3)] for a in range(3)]
# omega_{i a b} = e_a^j (d_i e^b_j - Chr^k_{ij} e^b_k)   (frame indices lowered with delta)
omega = [[[sp.expand(sum(einv[a, j]*(sp.diff(ecov[b, j], X[i]) - sum(Chr[kk][i][j]*ecov[b, kk] for kk in range(3)))
                         for j in range(3))) for b in range(3)] for a in range(3)] for i in range(3)]
omega = [[[sp.series(omega[i][a][b], d, 0, 2).removeO() for b in range(3)] for a in range(3)] for i in range(3)]
# Signature (+,-,-,-): {gamma^a, gamma^b} = 2 eta^ab = -2 delta^ab for spatial a, b. Lowering the frame index
# of omega_i^a_b with eta_ab = -delta_ab gives Gamma_i = (1/8) omega_i{ab} [gamma^a, gamma^b] = -(1/8) omega_i^a_b [..].
Gamma_sp = [-sum((omega[i][a][bb]*(gam[a]*gam[bb] - gam[bb]*gam[a]) for a in range(3) for bb in range(3)), sp.zeros(4))/8
            for i in range(3)]
psi = sp.Matrix([sp.Function(f'psi{c}')(x, y, z) for c in range(4)])
detg = sp.series(gmet.det(), d, 0, 2).removeO()
w = 1 + d*(hm.trace())/4                            # gamma^(1/4) to O(h)
winv = 1 - d*(hm.trace())/4
chi = winv*psi                                      # gamma^(-1/4) psi
Hcov = sp.zeros(4, 1)
for a in range(3):
    for i in range(3):
        Hcov += -sp.I*alpha[a]*einv[a, i]*(sp.diff(chi, X[i]) + Gamma_sp[i]*chi)
Hcov = w*Hcov
Hsym = sp.zeros(4, 1)                               # (1/2){alpha^a e_a^i, p_i} psi, p = -i d
for a in range(3):
    for i in range(3):
        Hsym += (-sp.I/2)*(alpha[a]*einv[a, i]*sp.diff(psi, X[i]) + sp.diff(alpha[a]*einv[a, i]*psi, X[i]))
diff = (Hcov - Hsym).applyfunc(lambda e: sp.expand(sp.series(sp.expand(e), d, 0, 2).removeO()))
check('E2 half-density covariant Dirac operator = (1/2){alpha^a e_a^i, p_i} + O(h^2) for arbitrary symmetric h(x) '
      '(axial spin-connection term vanishes at O(h) in symmetric gauge)', all(sp.simplify(e) == 0 for e in diff))

# ------------------------------------------------------------------ E3  heat-kernel normalisation
Rs, Lam, sv = sp.symbols('R Lambda s', positive=True)
tr_a1 = 4*(Rs/6 - Rs/4)                             # tr(R/6 + E), E = -R/4 (Lichnerowicz), 4 spinor components
check('E3 tr a1 = -R/3 for D^2 = -nabla^2 + R/4', sp.simplify(tr_a1 + Rs/3) == 0)
# Gamma_E = -log det D = -(1/2) log det D^2 = +(1/2) int_{1/Lam^2}^oo ds/s Tr exp(-s D^2)
GammaR = sp.Rational(1, 2)*sp.integrate(sv**-1*(4*sp.pi*sv)**-2*sv*tr_a1, (sv, 1/Lam**2, sp.oo))
coefEH = sp.simplify(-GammaR/Rs)                    # Euclidean S_EH = -(1/16 pi G) int sqrt(g) R
print(f"  induced 1/(16 pi G) per Dirac fermion (proper-time cutoff) = {coefEH}")
check('E3 1/(16 pi G) = +Lambda^2/(96 pi^2) per Dirac fermion (positive)', sp.simplify(coefEH - Lam**2/(96*sp.pi**2)) == 0)

# ------------------------------------------------------------------ E4  Clifford trace identity
t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]])
G5 = [kr(t1, sp.eye(2)), kr(t2, sp.eye(2)), kr(t3, s1), kr(t3, s2), kr(t3, s3)]
ok = all((G5[i]*G5[j] + G5[j]*G5[i] - 2*(1 if i == j else 0)*sp.eye(4)).is_zero_matrix for i in range(5) for j in range(5))
check('E4 walk Gammas (tau1, tau2, tau3 sigma_a) are 5 Hermitian anticommuting involutions', ok)
av = sp.symbols('a1:6', real=True); bv = sp.symbols('b1:6', real=True); ov = sp.symbols('o1:6', real=True)
dot = lambda u, v: sum(ui*vi for ui, vi in zip(u, v))
sl = lambda v: sum((vi*Gi for vi, Gi in zip(v, G5)), sp.zeros(4))
Pp = (sp.eye(4) - sl(av))/2; Pm = (sp.eye(4) + sl(bv))/2; O = sl(ov)
lhs = sp.expand((Pp*O*Pm*O).trace())
rhs = sp.expand(dot(ov, ov)*(1 + dot(av, bv)) - 2*dot(av, ov)*dot(bv, ov))
check('E4 Tr[P+(a) O P-(b) O] = o^2 (1 + a.b) - 2 (a.o)(b.o)', sp.simplify(lhs - rhs) == 0)
Pp2 = (sp.eye(4) + sl(av))/2; Pm2 = (sp.eye(4) - sl(bv))/2
check('E4 the partner term Tr[P-(a) O P+(b) O] is identical', sp.simplify(sp.expand((Pp2*O*Pm2*O).trace()) - rhs) == 0)

# ------------------------------------------------------------------ E5  rho series
u = sp.Symbol('u', positive=True)
fv = 1 - u
rho = sp.acos(fv)/sp.sqrt(1 - fv**2)
ser = sp.series(rho, u, 0, 5).removeO()
print(f"  rho(1-u) = {ser}")
want = 1 + u/3 + 2*u**2/15 + 2*u**3/35 + 8*u**4/315
check('E5 rho(1-u) = 1 + u/3 + 2u^2/15 + 2u^3/35 + 8u^4/315 + O(u^5)', sp.simplify(ser - want) == 0)
fs = sp.Symbol('f')
rhop = sp.diff(sp.acos(fs)/sp.sqrt(1 - fs**2), fs)
serp = sp.series(rhop.subs(fs, 1 - u), u, 0, 4).removeO()
print(f"  rho'(1-u) = {serp}")
wantp = -sp.Rational(1, 3) - sp.Rational(4, 15)*u - sp.Rational(6, 35)*u**2 - sp.Rational(32, 315)*u**3
check("E5 rho'(1-u) = -1/3 - 4u/15 - 6u^2/35 - 32u^3/315 + O(u^4)", sp.simplify(serp - wantp) == 0)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
