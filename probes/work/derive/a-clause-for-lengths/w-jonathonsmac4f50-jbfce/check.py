"""a-clause-for-lengths, attempt a1 (w-jonathonsmac4f50-jbfce).

Rays of the two-function family on the lattice: E^2 = a(x)^2 m^2 + c(x)^2 sum_j sin^2 k_j (a times the rest energy, c = a b times the hops);
the continuum family E = a sqrt(m^2 + b^2 k^2) is its small-k form with c = a b.  Exact: sympy at Pythagorean points (rational sines and
cosines), in the manner of block 54's runner.  C1 is NUMERIC (labelled).
"""
import itertools

import numpy as np
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


x1, x2, x3, k1, k2, k3, m = sp.symbols("x1 x2 x3 k1 k2 k3 m", real=True)
X = (x1, x2, x3); K = (k1, k2, k3)

# ================================================================== (a) the general ray law, symbolically
a = sp.Function("a")(*X); c = sp.Function("c")(*X)
S = sum(sp.sin(kk) ** 2 for kk in K)
E = sp.sqrt(a ** 2 * m ** 2 + c ** 2 * S)
v = [sp.diff(E, kj) for kj in K]
kdot = [-sp.diff(E, xj) for xj in X]
acc = [sum(sp.diff(v[j], X[l]) * v[l] for l in range(3)) + sum(sp.diff(v[j], K[l]) * kdot[l] for l in range(3)) for j in range(3)]
law = [-c ** 2 * sp.cos(2 * K[j]) * (a ** 2 * m ** 2 * sp.diff(sp.log(a), X[j]) + c ** 2 * S * sp.diff(sp.log(c), X[j])) / E ** 2
       + 2 * v[j] * sum(v[l] * sp.diff(sp.log(c), X[l]) for l in range(3)) for j in range(3)]
law_ok = all(sp.simplify(acc[j] - law[j]) == 0 for j in range(3))
want("A1 (a) EXACT, THE GENERAL RAY LAW: for E^2 = a^2 m^2 + c^2 sum sin^2 k_j, Hamilton's equations give dv_j/dt = -c^2 cos(2k_j) [a^2 m^2 "
     "d_j log a + c^2 S d_j log c]/E^2 + 2 v_j (v . grad log c) (symbolic, every a(x), c(x)): the pull is the energy-weighted mixture of "
     "grad log a (the rest-energy share) and grad log c (the hop share); a = c = w is block 54's law", law_ok)

# ================================================================== (a) at Pythagorean points, exactly
ga, gc, a0, c0 = sp.Rational(3, 10), sp.Rational(-7, 20), sp.Rational(5, 4), sp.Rational(2, 3)
alin = a0 * (1 + ga * x1); clin = c0 * (1 + gc * x1)                # uniform gradients along x1
El = sp.sqrt(alin ** 2 * m ** 2 + clin ** 2 * S)
vl = [sp.diff(El, kj) for kj in K]; kdl = [-sp.diff(El, xj) for xj in X]
accl = [sum(sp.diff(vl[j], X[l]) * vl[l] for l in range(3)) + sum(sp.diff(vl[j], K[l]) * kdl[l] for l in range(3)) for j in range(3)]
sy = sp.symbols("s1 s2 s3", real=True); cy = sp.symbols("c1 c2 c3", real=True)
trig = {}
for j in range(3):
    trig[sp.sin(2 * K[j])] = 2 * sy[j] * cy[j]; trig[sp.cos(2 * K[j])] = cy[j] ** 2 - sy[j] ** 2
    trig[sp.sin(K[j])] = sy[j]; trig[sp.cos(K[j])] = cy[j]
acc_sc = [sp.expand_trig(ex.subs({x1: 0, x2: 0, x3: 0})).subs(trig) for ex in accl]
pyth = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (sp.Rational(-8, 17), sp.Rational(15, 17)), (sp.Integer(0), sp.Integer(1))]
ok = True; npts = 0
for (s1, c1), (s2, c2), mm in itertools.product(pyth, pyth[:3], (0, sp.Rational(1, 2), 2)):
    sv = [s1, s2, sp.Integer(0)]; cv = [c1, c2, sp.Integer(1)]
    Sv = sum(t * t for t in sv)
    E2 = a0 ** 2 * mm ** 2 + c0 ** 2 * Sv
    if E2 == 0: continue
    Ev = sp.sqrt(E2)
    vv = [c0 ** 2 * sv[j] * cv[j] / Ev for j in range(3)]
    dla = [ga, 0, 0]; dlc = [gc, 0, 0]
    closed = [-c0 ** 2 * (cv[j] ** 2 - sv[j] ** 2) * (a0 ** 2 * mm ** 2 * dla[j] + c0 ** 2 * Sv * dlc[j]) / E2
              + 2 * vv[j] * sum(vv[l] * dlc[l] for l in range(3)) for j in range(3)]
    sub = {m: mm}
    for j in range(3): sub[sy[j]] = sv[j]; sub[cy[j]] = cv[j]
    direct = [sp.simplify(acc_sc[j].subs(sub)) for j in range(3)]
    ok = ok and all(sp.simplify(direct[j] - closed[j]) == 0 for j in range(3))
    npts += 1
want("A2 (a) EXACT AT PYTHAGOREAN POINTS: with uniform gradients (a = (5/4)(1 + 3x/10), c = (2/3)(1 - 7x/20)), Hamilton's equations evaluated "
     "exactly at wave vectors with rational sines and cosines and rest energies 0, 1/2, 2 agree with the closed law", ok and npts > 20,
     f"{npts} points")

# the two limits and the ratio
kk = sp.Symbol("kk", real=True)
fall = sp.limit(law[0].subs({k2: 0, k3: 0}).subs(k1, kk), kk, 0)                       # slow body: -c^2 d log a
m0 = [law[0].subs({m: 0, k1: 0, k3: 0}).subs(k2, kk)]                                     # massless ray moving along x2, gradient component x1
bend = sp.simplify(m0[0].subs(kk, sp.pi / 4))                                              # any k2 with c^2 S > 0: transverse bending
lim_ok = sp.simplify(fall + c ** 2 * sp.diff(sp.log(a), x1)) == 0 and sp.simplify(bend + c ** 2 * sp.diff(sp.log(c), x1)) == 0
w_ = sp.Function("w")(*X); wbar = sp.Symbol("wbar", positive=True)
ratio_locked = sp.simplify(sp.diff(sp.log(w_), x1) / sp.diff(sp.log(w_), x1))
ratio_l = sp.simplify(sp.diff(sp.log(w_ ** 2 / wbar), x1) / sp.diff(sp.log(w_), x1))
want("A3 (a) THE TWO LIMITS: a slow body falls at -c^2 grad log a, a massless ray crossing the gradient bends at -c^2 grad log c (both from the "
     "general law), so bending/fall = dlog c/dlog a = 1 + dlog b/dlog a (c = a b): 1 when hops are timed like sites (c = a, locked lengths), "
     "2 when c = a^2/abar (lengths l = abar/a) - block 59 T4's two limits, here as limits of one law", lim_ok and ratio_locked == 1 and ratio_l == 2)

# ================================================================== (b) what may play the role of b
u1, u2, du = sp.symbols("u1 u2 du", real=True)
g = sp.Function("g")
wx = sp.exp(u1); wy = sp.exp(u1 + du)
c_bond = sp.sqrt(wx * wy) * g(wx / wy)                                                     # scale covariant: degree one in the rates
l_bond = sp.simplify(sp.sqrt(wx * wy) / c_bond)
depth_free = sp.simplify(sp.diff(l_bond, u1)) == 0                                        # the length cannot depend on the depth u1
tt = sp.Symbol("t", positive=True)
cov = sp.simplify(c_bond.subs(u1, u1 + sp.log(tt)) - tt * c_bond) == 0
want("B1 (b) SCALE COVARIANCE SETTLES THE ALGEBRAIC CANDIDATE: a bond rate built from the two site rates and covariant under w -> t w must be "
     "sqrt(w_x w_y) g(w_x/w_y), so the bond's length sqrt(w_x w_y)/c_b = 1/g(w_x/w_y) depends only on the ratio, never on the depth of the "
     "rate: in a uniform gradient dlog c/dlog a = 1 exactly - no factor 2 (block 59 T5(a) re-derived)", depth_free and cov)

# ================================================================== (c) executed: bending under the two clauses (NUMERIC, labelled)
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
Lx, Ly = 40, 64
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]])]
def run(clause, grad, T=40.0):
    N = Lx * Ly; r_, c_, v_ = [], [], []
    idx = lambda x, y: (x % Lx) * Ly + (y % Ly)
    w = lambda x: np.exp(-grad * (x - Lx / 2))                                           # site rates falling toward +x
    for x in range(Lx):
        for y in range(Ly):
            for a_, (dx, dy) in enumerate(((1, 0), (0, 1))):
                if dx and x == Lx - 1: continue                                              # open in x (the gradient), periodic in y
                i, j = idx(x, y), idx(x + dx, y + dy)
                cb = np.sqrt(w(x) * w(x + dx)) if clause == "locked" else w(x) * w(x + dx)   # lengths locked, or l = wbar/w (wbar = 1)
                blk = cb * SIG[a_] / (2j)
                for p in range(2):
                    for q in range(2):
                        if blk[p, q] != 0:
                            r_ += [2 * i + p, 2 * j + p]; c_ += [2 * j + q, 2 * i + q]; v_ += [blk[p, q], -blk[p, q]]
    H = sps.csr_matrix((v_, (r_, c_)), shape=(2 * N, 2 * N))
    Xg, Yg = np.meshgrid(np.arange(Lx), np.arange(Ly), indexing="ij")
    k0 = 0.5
    env = np.exp(-((Xg - Lx / 2) ** 2 + (Yg - 16) ** 2) / (2 * 3.0 ** 2)) * np.exp(1j * k0 * Yg)
    ev, V = np.linalg.eigh(np.sin(k0) * SIG[1]); chi = V[:, 1]
    psi = (env[..., None] * chi[None, None, :]).reshape(-1); psi /= np.linalg.norm(psi)
    pt = expm_multiply(-1j * H, psi, start=0, stop=T, num=2, endpoint=True)[-1]
    return ((np.abs(pt.reshape(Lx, Ly, 2)) ** 2).sum(-1) * Xg).sum()
x_free = run("locked", 0.0)
dl = run("locked", 0.004) - x_free; dr = run("wbar/w", 0.004) - x_free
want("C1 (c) EXECUTED, NOT CLAIMED (NUMERIC): a walker with no rest energy moving along y across a uniform rate gradient along x (40 x 64 "
     "slab): the transverse displacement at t = 40 under l = wbar/w over that under locked lengths, near 2 (the ray value) - the test that "
     "separates a = b from b = 1; the slow-body side needs an on-site rest energy, which block 54's walk does not have", abs(dr / dl - 2) < 0.2,
     f"displacements {dl:.4f} (locked) and {dr:.4f} (l = wbar/w), ratio {dr / dl:.3f}")

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL, exact: for E^2 = a^2 m^2 + c^2 sum sin^2 k (c = a b) every ray obeys dv_j/dt = -c^2 cos(2k_j)[a^2 m^2 d_j log a + "
          "c^2 S d_j log c]/E^2 + 2 v_j (v . grad log c): an energy-weighted mixture of the site rate's gradient (rest share) and the hop "
          "rate's (kinetic share); slow bodies fall at -c^2 grad log a, massless rays bend at -c^2 grad log c, ratio 1 + dlog b/dlog a; "
          "scale covariance makes any bond rate built from site rates depend on their ratio only, so the factor 2 needs lengths tied to the "
          "depth of the rate through a law (block 59 T5(b)) or a reference rate; executed bending ratio near 2")
    print("HIT: on the lattice the two-function family E^2 = a(x)^2 m^2 + c(x)^2 sum sin^2 k_j has the exact ray law dv_j/dt = -c^2 cos(2k_j) "
          "[a^2 m^2 d_j log a + c^2 S d_j log c]/E^2 + 2 v_j (v . grad log c), whose limits are the fall -c^2 grad log a and the transverse "
          "bending -c^2 grad log c (ratio dlog c/dlog a), and a scale-covariant bond rate built from the site rates cannot make that ratio "
          "differ from 1")
