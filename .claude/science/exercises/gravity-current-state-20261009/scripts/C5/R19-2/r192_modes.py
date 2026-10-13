#!/usr/bin/env python3
"""R19-2 [A]: independent per-mode O(G noise^2) mean source of E1 + N_c in Poisson gauge, ALL six free channel
variables of R15-2 Lemma A (rho, T_perp, j_x, j_y, t_plus, t_cross), insertion family T^{ab} = (-g)^{a/4-1} J^{ab}.
Written from scratch (not a copy of r1811_modes.py). Exact second-order inverse metric:
   g^{-1} = eta - eps eta h eta + eps^2 eta h eta h eta.
G = c = 1, Einstein eq G_{mu nu} = 8 pi T_{mu nu}. One frame mode theta = k z - w t, all channels on cos(theta).
Mean source per mode: tau_{mu nu} = <T^(2)_{mu nu}> - <G^(2)_{mu nu}[h1,h1]>/(8 pi)   (theta average).
Subtraction: none.
Run: OMP_NUM_THREADS=2 python3 r192_modes.py
"""
import sympy as sp, time
t0 = time.time()
w, k = sp.symbols('omega k', positive=True)
a, eps = sp.symbols('a epsilon')
C, S = sp.symbols('C S')       # cos(theta), sin(theta)
X = w / k
eta = sp.diag(-1, 1, 1, 1)

def dth(f):
    f = sp.expand(f)
    return sp.diff(f, C) * (-S) + sp.diff(f, S) * C
def D(mu, f):
    if mu == 0: return -w * dth(f)
    if mu == 3: return k * dth(f)
    return sp.Integer(0)
MOM = {(0, 0): 1, (2, 0): sp.Rational(1, 2), (0, 2): sp.Rational(1, 2), (4, 0): sp.Rational(3, 8),
       (0, 4): sp.Rational(3, 8), (2, 2): sp.Rational(1, 8)}
def avg(e):
    p = sp.Poly(sp.expand(e), C, S); out = 0
    for (i, j), cf in p.terms():
        if i % 2 == 0 and j % 2 == 0: out += cf * MOM[(i, j)]
    return sp.simplify(out)
def trunc(e, top=2):
    e = sp.expand(e); return sum(e.coeff(eps, p) * eps**p for p in range(1, top + 1))

def einstein2(h):
    g = eta + eps * h
    ginv = eta - eps * eta * h * eta + eps**2 * eta * h * eta * h * eta
    chk = sp.simplify(sp.expand(g * ginv - sp.eye(4)))
    chk = chk.applyfunc(lambda e: sp.expand(e).coeff(eps, 1) + sp.expand(e).coeff(eps, 2))
    assert chk == sp.zeros(4, 4), "inverse not exact to O(eps^2)"
    n = 4
    dg = [[[D(l, g[m, q]) for l in range(n)] for q in range(n)] for m in range(n)]
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for al in range(n):
        for m in range(n):
            for q in range(m, n):
                v = sum(ginv[al, b] * (dg[b][m][q] + dg[b][q][m] - dg[m][q][b]) for b in range(n)) / 2
                v = trunc(v); Gam[al][m][q] = v; Gam[al][q][m] = v
    Ric = sp.zeros(n, n)
    for m in range(n):
        for q in range(m, n):
            v = 0
            for al in range(n):
                v += D(al, Gam[al][m][q]) - D(q, Gam[al][m][al])
                for b in range(n):
                    v += Gam[al][al][b] * Gam[b][m][q] - Gam[al][q][b] * Gam[b][m][al]
            v = trunc(v); Ric[m, q] = v; Ric[q, m] = v
    R = trunc(sum(ginv[m, q] * Ric[m, q] for m in range(n) for q in range(n)))
    Gt = sp.zeros(n, n)
    for m in range(n):
        for q in range(n):
            Gt[m, q] = trunc(Ric[m, q] - g[m, q] * R / 2)
    return Gt

rho, Tp, jx, jy, tp, tc = sp.symbols('rho T_perp j_x j_y t_p t_c', real=True)
J = sp.zeros(4, 4)
J[0, 0] = rho; J[0, 3] = J[3, 0] = X * rho; J[3, 3] = X**2 * rho
J[0, 1] = J[1, 0] = jx; J[1, 3] = J[3, 1] = X * jx
J[0, 2] = J[2, 0] = jy; J[2, 3] = J[3, 2] = X * jy
J[1, 1] = Tp / 2 + tp; J[2, 2] = Tp / 2 - tp; J[1, 2] = J[2, 1] = tc
J = J * C
# conservation check: i p_mu J^{mu nu} = 0 with p = (w, 0, 0, k) contravariant-time derivative: d_t J^{0nu} + d_z J^{z nu} = 0
cons = [sp.simplify(D(0, J[0, nu]) + D(3, J[3, nu])) for nu in range(4)]
print("[A0] flat conservation of the mode source J (all six channels):", cons)
Jl = eta * J * eta

# linear Poisson-gauge ansatz: h00 = -2 Phi, h0i = S_i (transverse), hij = -2 Psi delta + hTT
syms = sp.symbols('Phc Phs Psc Pss Sxc Sxs Syc Sys hpc hps hcc hcs', real=True)
Phi = syms[0] * C + syms[1] * S; Psi = syms[2] * C + syms[3] * S
Sx = syms[4] * C + syms[5] * S; Sy = syms[6] * C + syms[7] * S
hp = syms[8] * C + syms[9] * S; hc = syms[10] * C + syms[11] * S
h = sp.zeros(4, 4)
h[0, 0] = -2 * Phi
h[0, 1] = h[1, 0] = Sx; h[0, 2] = h[2, 0] = Sy
for i in (1, 2, 3): h[i, i] = -2 * Psi
h[1, 1] += hp; h[2, 2] += -hp; h[1, 2] = h[2, 1] = hc
G1 = einstein2(h)
eqs = []
for m in range(4):
    for q in range(m, 4):
        e = sp.expand(G1[m, q].coeff(eps, 1) - 8 * sp.pi * Jl[m, q])
        eqs += [e.coeff(C, 1).coeff(S, 0), e.coeff(S, 1).coeff(C, 0)]
eqs = [e for e in (sp.simplify(e) for e in eqs) if e != 0]
sol = sp.solve(eqs, syms, dict=True)
assert len(sol) == 1
sol = {kk: sp.factor(v) for kk, v in sol[0].items()}
print("[A1] Poisson-gauge linear solution (cos amplitudes):")
for kk in (syms[0], syms[2], syms[4], syms[6], syms[8], syms[10]):
    print("     %s = %s" % (kk, sol[kk]))
print("     sin amplitudes:", [sol[kk] for kk in syms[1::2]])
print("     linear equations satisfied:", sum(1 for e in eqs if sp.simplify(e.subs(sol)) == 0), "of", len(eqs))
hs = h.subs(sol)
G2 = einstein2(hs)
trh = sp.expand(sum(eta[i, i] * hs[i, i] for i in range(4)))     # (-g)^(1) = eta^{mu nu} h_{mu nu}
tau = sp.zeros(4, 4)
for m in range(4):
    for q in range(4):
        T2 = (a / 4 - 1) * trh * Jl[m, q]
        for al in range(4):
            for b in range(4):
                T2 += hs[m, al] * eta[q, b] * J[al, b] + eta[m, al] * hs[q, b] * J[al, b]
        tau[m, q] = sp.simplify(avg(T2) - avg(G2[m, q].coeff(eps, 2)) / (8 * sp.pi))
t00 = sp.expand(tau[0, 0]); tkk = sp.expand(tau[1, 1] + tau[2, 2] + tau[3, 3])
xs = sp.Symbol('x', positive=True)
mons = [rho**2, rho*Tp, Tp**2, jx**2, jy**2, tp**2, tc**2, rho*jx, rho*tp, jx*jy, tp*tc, Tp*tp, jx*tp, jy*tc]
print("\n[A2] per-mode coefficients (units pi/k^2), Poisson law, insertion weight a, x = w/k:")
coef = {}
for lab, ex in (("tau_00", t00), ("tau_kk", tkk)):
    P = sp.Poly(sp.expand(ex * k**2 / sp.pi), rho, Tp, jx, jy, tp, tc)
    for mon in mons:
        cf = sp.factor(sp.simplify(sp.sympify(P.coeff_monomial(mon)).subs(w, xs * k)))
        coef[(lab, mon)] = cf
        print("     %s [%s] = %s" % (lab, mon, cf))
print("     tau_0i:", [sp.simplify(tau[0, i]) for i in (1, 2, 3)])
# comparison with R18-11's table (rR18-11:166-171; r1811_modes.out:37-56)
r1811 = {("tau_00", rho**2): 2*a*xs**2 + 2*a - 3*xs**2 - 7, ("tau_00", rho*Tp): -a, ("tau_00", Tp**2): 0,
         ("tau_00", jx**2): 4, ("tau_00", tp**2): 4*(xs**2 + 1)/((xs - 1)**2*(xs + 1)**2),
         ("tau_kk", rho**2): (xs**2 + 1)*(2*a*xs**2 - 4*xs**2 - 1), ("tau_kk", rho*Tp): a*xs**2 + 2*a - 2*xs**2 - 2,
         ("tau_kk", Tp**2): -(a - 2), ("tau_kk", jx**2): -4, ("tau_kk", tp**2): -4*(xs**2 - 3)/((xs - 1)**2*(xs + 1)**2)}
ok = [sp.simplify(coef[kk] - v) == 0 for kk, v in r1811.items()]
print("\n[A3] agreement with R18-11's per-mode table: %d of %d entries" % (sum(ok), len(ok)))
print("     second V component and cross polarization equal the first: j_y^2 == j_x^2: %s ; t_c^2 == t_p^2: %s" % (
    all(sp.simplify(coef[(l, jy**2)] - coef[(l, jx**2)]) == 0 for l in ("tau_00", "tau_kk")),
    all(sp.simplify(coef[(l, tc**2)] - coef[(l, tp**2)]) == 0 for l in ("tau_00", "tau_kk"))))
print("     runtime %.1f s" % (time.time() - t0))
import pickle
pickle.dump({str(kk): str(v) for kk, v in coef.items()}, open('r192_coef.pkl', 'wb'))
