"""R2-6 (b)(c)(d)(e): Snyder momentum composition on dS_4 = SO(4,1)/SO(3,1).

Momentum space: X in R^{1,4}, G = diag(-1,1,1,1,1), X.X = 1/a^2, origin O = e4/a.
Plane waves e^{i k.xhat} = exp(W(k)), W(k) = a (kappa e4^T G - e4 kappa^T G),
kappa = (k^0,k^1,k^2,k^3,0): these are the transvections (coset exponentials).
Composition (Weyl/exponential section, Girelli-Livine / Battisti-Meljanac form):
    g(k) g(q) = g(k (+) q) h,   h in SO(3,1)  (fixes O).
Momentum labels k are normal (geodesic) coordinates; any Lorentz-covariant
relabelling p = f(k^2) k (e.g. Snyder's projective chart) leaves every ratio
p_i/p_0 (velocity) and every invariant unchanged.

Checks:
 C1  g(k)O equals the closed-form geodesic point; h fixes O; Lorentz covariance
     L(k(+)q) = Lk (+) Lq.
 C2  non-commutativity and non-associativity at O(a^2 k^3); BCH prediction
     k(+)q = k + q - (1/6)[X,[X,Y]] - (1/3)[Y,[X,Y]] (projected), residual O(a^4).
 C3  collinear momenta add exactly (normal coordinates).
 C4  "body as one Snyder particle" (mapping A): response to a soft spatial kick
     q on a body at rest of mass M: left P(+)q gives v = a q / sinh(aM),
     right q(+)P gives v = a q coth(aM).
 C5  N-constituent body at rest with internal (Fermi) momenta: spurious total
     spatial momentum and ordering ambiguity vs N (sequential and tree bracketings).
 C6  Lemma W test: equal-mass 2->2 on the (+)-conservation surface; the linear
     law k1+k2 = k3+k4 fails at O(a^2 k^3); k1(+)k2 is not parallel to k1+k2.
 C7  free-particle worldline velocity in the Snyder realisation (sympy).
"""
import numpy as np
from scipy.linalg import expm
import sympy as sp

rng = np.random.default_rng(20261012)
G5 = np.diag([-1.0, 1, 1, 1, 1])
eta4 = np.diag([-1.0, 1, 1, 1])
e4 = np.array([0, 0, 0, 0, 1.0])


def dot4(u, v):
    return u @ eta4 @ v


def W(k, a):
    kap = np.concatenate([k, [0.0]])
    return a * (np.outer(kap, e4) @ G5 - np.outer(e4, kap) @ G5)


def g(k, a):
    return expm(W(k, a))


def point(k, a):
    """closed form geodesic point from O with normal coords k."""
    k2 = dot4(k, k)
    kap = np.concatenate([k, [0.0]])
    O = e4 / a
    if k2 < 0:
        mu = np.sqrt(-k2)
        return np.cosh(a * mu) * O + np.sinh(a * mu) / (a * mu) * kap
    elif k2 > 0:
        lam = np.sqrt(k2)
        return np.cos(a * lam) * O + np.sin(a * lam) / (a * lam) * kap
    return O + kap


def log_pt(X, a):
    """normal coordinates of a dS point X reachable from O."""
    v = X[:4]
    vv = dot4(v, v)
    if vv < 0:
        s = a * np.sqrt(-vv)
        if X[4] <= 0:
            raise ValueError("timelike point not reachable by a geodesic from O")
        return v * np.arcsinh(s) / s
    elif vv > 0:
        s = a * np.sqrt(vv)
        th = np.arctan2(s, a * X[4])
        return v * th / s
    return v.copy()


def oplus(k, q, a):
    return log_pt(g(k, a) @ g(q, a) @ (e4 / a), a)


def lorentz(rap, axis, rot):
    """a Lorentz transform in SO(3,1) embedded in 5D (fixes e4)."""
    M = np.zeros((5, 5))
    M[0, axis] = M[axis, 0] = 1.0
    B = expm(rap * M)
    R = np.eye(5)
    c, s = np.cos(rot), np.sin(rot)
    R[1:3, 1:3] = [[c, -s], [s, c]]
    return B @ R


def onshell(m, kv):
    return np.array([np.sqrt(m * m + kv @ kv), *kv])


out = []


def pr(*args):
    s = " ".join(str(x) for x in args)
    print(s)
    out.append(s)


pr("== C1: geometry and Lorentz covariance ==")
a = 0.7
for _ in range(3):
    k = rng.normal(size=4)
    X1 = g(k, a) @ (e4 / a)
    X2 = point(k, a)
    pr(f"|g(k)O - closed form| = {np.linalg.norm(X1 - X2):.2e}, |X.X - 1/a^2| = {abs(X1 @ G5 @ X1 - 1 / a**2):.1e}")
k = onshell(1.0, np.array([0.3, -0.2, 0.5]))
q = onshell(1.0, np.array([-0.4, 0.1, 0.2]))
kq = oplus(k, q, a)
h = np.linalg.inv(g(kq, a)) @ g(k, a) @ g(q, a)
pr(f"h = g(k+q)^-1 g(k) g(q): |h O - O| = {np.linalg.norm(h @ e4 - e4):.2e}; h preserves G: {np.allclose(h.T @ G5 @ h, G5)}")
Lm = lorentz(0.9, 1, 0.6)
Lk, Lq = Lm[:4, :4] @ k, Lm[:4, :4] @ q
pr(f"Lorentz covariance |L(k(+)q) - (Lk)(+)(Lq)| = {np.linalg.norm(Lm[:4, :4] @ kq - oplus(Lk, Lq, a)):.2e}")
pr(f"mass of k(+)q = {np.sqrt(-dot4(kq, kq)):.12f}; mass of q(+)k = {np.sqrt(-dot4(oplus(q, k, a), oplus(q, k, a))):.12f} (equal: q(+)k = h^-1 (k(+)q))")

pr("")
pr("== C2: non-commutativity / non-associativity and the BCH form ==")


def bch_pred(k, q, a):
    X, Y = W(k, a), W(q, a)
    c = lambda A, B: A @ B - B @ A
    Z = X + Y - c(X, c(X, Y)) / 6 - c(Y, c(X, Y)) / 3
    return Z @ e4  # Z O / (1/a) * ... : W(k) e4 = a*kappa -> divide by a below


k0 = onshell(1.0, np.array([0.6, 0.0, 0.0]))
q0 = onshell(1.0, np.array([0.0, 0.5, 0.2]))
r0 = onshell(1.0, np.array([-0.3, 0.2, 0.4]))
pr(" a       |k+q - q+k|   ratio/a^2   |(k+q)+r - k+(q+r)|  ratio/a^2   |k+q - BCH3|  ratio/a^4")
for a in [0.2, 0.1, 0.05, 0.025, 0.0125]:
    kq, qk = oplus(k0, q0, a), oplus(q0, k0, a)
    nc = np.linalg.norm(kq - qk)
    na = np.linalg.norm(oplus(oplus(k0, q0, a), r0, a) - oplus(k0, oplus(q0, r0, a), a))
    pred = bch_pred(k0, q0, a)[:4] / a
    rb = np.linalg.norm(kq - pred)
    pr(f"{a:7.4f}  {nc:11.4e}  {nc / a**2:9.5f}   {na:11.4e}         {na / a**2:9.5f}   {rb:10.3e}  {rb / a**4:8.4f}")
# analytic leading commutator: k(+)q - q(+)k = -(1/2)[X+Y,[X,Y]] projected; compare closed form
a = 0.01
nc_vec = (oplus(k0, q0, a) - oplus(q0, k0, a)) / a**2
# closed form of [X,[X,Y]] O /a^3 : X=W(k): computed numerically -> express in momenta
kk, kq_, qq = dot4(k0, k0), dot4(k0, q0), dot4(q0, q0)
cand = (kk + kq_) * q0 - (kq_ + qq) * k0  # (k+q).k q - (k+q).q k
pr(f"(k(+)q - q(+)k)/a^2 at a=0.01: {np.round(nc_vec, 5)}")
pr(f"  compare c*[((k+q).k) q - ((k+q).q) k], c fitted: {np.round(np.linalg.lstsq(cand[:, None], nc_vec, rcond=None)[0], 5)}, "
   f"residual {np.linalg.norm(nc_vec - np.linalg.lstsq(cand[:, None], nc_vec, rcond=None)[0][0] * cand):.2e}")

pr("")
pr("== C3: collinear momenta add exactly in normal coordinates ==")
a = 1.3
u = onshell(1.0, np.array([0.4, -0.3, 0.2]))
for (m1, m2) in [(0.2, 0.5), (1.0, 3.0), (2.0, 7.5)]:
    s = oplus(m1 * u, m2 * u, a)
    pr(f"m1={m1}, m2={m2}, a(m1+m2)={a * (m1 + m2):.2f}: |k1(+)k2 - (k1+k2)| = {np.linalg.norm(s - (m1 + m2) * u):.2e}")

pr("")
pr("== C4: mapping A, body at rest (mass M) as one Snyder particle, soft spatial kick q ==")
pr(" aM      v_left*M/q   aM/sinh(aM)    v_right*M/q   aM*coth(aM)")
qk = 1e-7
for aM in [0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
    a = 1.0
    P = np.array([aM / a, 0, 0, 0])
    qv = np.array([0, qk, 0, 0])
    L = oplus(P, qv, a)
    R = oplus(qv, P, a)
    vL, vR = L[1] / L[0], R[1] / R[0]
    pr(f"{aM:6.2f}  {vL * P[0] / qk:12.8f}  {aM / np.sinh(aM):12.8f}   {vR * P[0] / qk:12.6f}  {aM / np.tanh(aM):12.6f}")

pr("")
pr("== C5: N constituents at rest with Fermi motion (units a=1; m, kF scaled) ==")
m, kF = 1e-3, 2.66e-4  # ratio kF/m = 0.25/0.94 as for nucleons


def fermi_sample(N):
    v = rng.normal(size=(N, 3))
    v /= np.linalg.norm(v, axis=1)[:, None]
    r = kF * rng.random(N) ** (1 / 3)
    kv = v * r[:, None]
    kv -= kv.mean(axis=0)  # linear total spatial momentum exactly zero
    return np.array([onshell(m, x) for x in kv])


def compose_seq(ks, a):
    Mtot = np.eye(5)
    for k in ks:
        Mtot = Mtot @ g(k, a)
    return log_pt(Mtot @ (e4 / a), a)


def compose_tree(ks, a):
    mats = [g(k, a) for k in ks]
    while len(mats) > 1:
        nxt = []
        for i in range(0, len(mats) - 1, 2):
            # combine pairs: g(p1)g(p2) = g(p1(+)p2) h ; keep only the transvection part
            Pm = mats[i] @ mats[i + 1]
            p = log_pt(Pm @ (e4 / a), a)
            nxt.append(g(p, a))
        if len(mats) % 2:
            nxt.append(mats[-1])
        mats = nxt
    return log_pt(mats[0] @ (e4 / a), a)


pr(" N      aM       |P_spatial|/M (seq)   ordering ambiguity/M   |P_spatial|/M (tree)   a^2 m kF N^1.5")
a = 1.0
rows = []
for N in [16, 32, 64, 128, 256, 512, 1024, 2048]:
    vals_seq, vals_amb, vals_tree = [], [], []
    for rep in range(6):
        ks = fermi_sample(N)
        Pseq = compose_seq(ks, a)
        Pperm = compose_seq(ks[rng.permutation(N)], a)
        Ptree = compose_tree(ks, a)
        M = N * m
        vals_seq.append(np.linalg.norm(Pseq[1:]) / M)
        vals_amb.append(np.linalg.norm(Pseq - Pperm) / M)
        vals_tree.append(np.linalg.norm(Ptree[1:]) / M)
    rows.append((N, np.mean(vals_seq), np.mean(vals_amb), np.mean(vals_tree)))
    pr(f"{N:5d}  {a * N * m:7.4f}   {np.mean(vals_seq):12.4e}          {np.mean(vals_amb):12.4e}          {np.mean(vals_tree):12.4e}        {a**2 * m * kF * N**1.5:10.3e}")
Ns = np.array([r[0] for r in rows], float)
for j, name in [(1, "seq spatial"), (2, "ordering ambiguity"), (3, "tree spatial")]:
    y = np.array([r[j] for r in rows])
    sl, ic = np.polyfit(np.log(Ns), np.log(y), 1)
    C = np.exp(np.mean(np.log(y) - 1.5 * np.log(Ns))) / (a**2 * m * kF)
    pr(f"fit {name:20s}: exponent {sl:.3f};  coefficient C in C*a^2*m*kF*N^1.5 = {C:.3f}")

pr("")
pr("== C6: Lemma W on the (+)-conservation surface (equal mass m=1, 2->2) ==")


def solve_k4(k3, v, a):
    return log_pt(g(-k3, a) @ point(v, a), a)


def find_k3(v, a, nhat, m=1.0):
    # find |k3| along direction nhat with k4 on shell
    from scipy.optimize import brentq

    def f(s):
        k3 = onshell(m, s * nhat)
        k4 = solve_k4(k3, v, a)
        return dot4(k4, k4) + m * m

    ss = np.linspace(0.0, 3.0, 301)
    fs = [f(s) for s in ss]
    for i in range(len(ss) - 1):
        if np.sign(fs[i]) != np.sign(fs[i + 1]):
            s = brentq(f, ss[i], ss[i + 1], xtol=1e-15)
            k3 = onshell(m, s * nhat)
            return k3, solve_k4(k3, v, a)
    raise RuntimeError("no root")


k1 = onshell(1.0, np.array([0.5, 0.1, 0.0]))
k2 = onshell(1.0, np.array([-0.4, 0.3, 0.2]))
nhat = np.array([0.2, -0.7, 0.5])
nhat /= np.linalg.norm(nhat)
pr(" a        |k1+k2-k3-k4|   /a^2       perp(k1(+)k2 vs k1+k2)/a^2   |k4^2+m^2|")
for a in [0.2, 0.1, 0.05, 0.025]:
    v = oplus(k1, k2, a)
    k3, k4 = find_k3(v, a, nhat)
    mis = np.linalg.norm(k1 + k2 - k3 - k4)
    s = k1 + k2
    perp = v - (dot4(v, s) / dot4(s, s)) * s
    pr(f"{a:6.3f}   {mis:12.4e}  {mis / a**2:9.5f}     {np.linalg.norm(perp) / a**2:9.5f}               {abs(dot4(k4, k4) + 1):.1e}")

pr("")
pr("== C6b: general Lemma W criterion: on-shell k(+)q = A k + B q needs A/B independent of k.q ==")
pr("   (ordering law and its symmetrisation; unequal masses m_k = 1, m_q = 0.6; a = 0.05)")
a = 0.05


def AB(k, q, comp):
    v = comp(k, q)
    Mx = np.vstack([k, q]).T
    coef, res, *_ = np.linalg.lstsq(Mx, v, rcond=None)
    return coef, np.linalg.norm(v - Mx @ coef)


sym = lambda k, q: 0.5 * (oplus(k, q, a) + oplus(q, k, a))
ordl = lambda k, q: oplus(k, q, a)
pr(" k.q        A/B (ordering)   A/B (symmetrised)   A/B sym, equal masses   |out of span|")
for sp_ in [0.1, 0.5, 1.0, 1.5]:
    k = onshell(1.0, np.array([sp_, 0.0, 0.0]))
    q = onshell(0.6, np.array([-0.3, 0.4, 0.0]))
    qe = onshell(1.0, np.array([-0.3, 0.4, 0.0]))
    c1, r1 = AB(k, q, ordl)
    c2, r2 = AB(k, q, sym)
    c3, r3 = AB(k, qe, sym)
    pr(f"{dot4(k, q):8.4f}   {c1[0] / c1[1]:.10f}   {c2[0] / c2[1]:.10f}      {c3[0] / c3[1]:.10f}          {max(r1, r2, r3):.1e}")

pr("")
pr("== C7: Snyder realisation, free worldline velocity (sympy) ==")
a_s = sp.symbols('a', positive=True)
p = sp.symbols('p0:4', real=True)
eta_s = sp.diag(-1, 1, 1, 1)
p2 = sum(eta_s[i, i] * p[i]**2 for i in range(4))
m_s = sp.symbols('m', positive=True)
C = p2 + m_s**2
# {x^mu, p_nu} = delta^mu_nu + a^2 p^mu p_nu  (Snyder realisation, mostly plus)
pup = [eta_s[i, i] * p[i] for i in range(4)]
xdot = [sp.simplify(sum((sp.KroneckerDelta(mu, nu) + a_s**2 * pup[mu] * p[nu]) * sp.diff(C, p[nu]) for nu in range(4)))
        for mu in range(4)]
ratio = [sp.simplify(xdot[i] / xdot[0]) for i in range(1, 4)]
pr("dx^mu/dtau =", [sp.factor(x) for x in xdot])
pr("dx^i/dx^0 =", ratio, " (undeformed: p^i/p^0)")

with open("r26_composition.out.txt", "w") as fh:
    fh.write("\n".join(out) + "\n")
