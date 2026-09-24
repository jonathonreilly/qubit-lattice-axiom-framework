#!/usr/bin/env python3
"""Records act as fields: under a nearest-neighbour two-qubit dynamics clause, a
site whose six neighbours carry records is a qubit in the field of their
contents, and a covariant law read from it has the form (1 + lam p.h)/2.

Supplied and not adopted: the dynamics clause (D-dyn) of the campaign's first
block, a Hermitian sum of covariant nearest-neighbour two-site terms
s_x^T M_f s_{x+f}. Record permanence is modelled as compression of the
generator onto the record subspace: a record locking the pure possibility with
Bloch vector q is the projector P_q = (1 + q.s)/2.

Checks:

A. Projection lemma: P_q s_a P_q = q_a P_q, exactly (symbolic) and numerically.
B. Compression on the seven-qubit star: with the six neighbours recorded,
   P H P = (h(N).s_0 + const) (x) P_N with h(N) = sum_f M_f q_f, for random
   Heisenberg and random fully soldered (J, K, D) couplings.
C. Isolation: with the six neighbours of x recorded, the compressed generator of
   x and a further unrecorded site y beyond one neighbour is a sum of an x term
   and a y term (no coupling survives).
D. Stationary states of the isolated site: [h.s, rho] = 0 exactly on the line
   rho = (1 + lam h^.s)/2; time averages of random states land on it.
E. Odds read from any stationary state: w(p|N) = (1 + lam p.h^)/2 on every
   antipodal menu {p, -p}; the Husimi density 1 + lam a.h^ on the sphere is
   normalised.
F. Heisenberg with one effective neighbour (the other five records sum to
   zero): the odds are f(t) = (1 + c t)/2 with c = -lam sgn J; ground-state
   relaxation gives c = +1 (J < 0, repeat certainty) and c = -1 (J > 0);
   thermal relaxation gives c = tanh(beta |J|) sgn(-J). The two landed
   non-affine witnesses are not affine in p and cannot be read from any
   stationary state.
G. Full soldering: h(N) = J sum q_f + K sum f (f.q_f) + D sum q_f x f; the
   Moriya part turns the conditional direction away from the resultant.
H. Scope: with one unrecorded neighbour y, two stationary states of the pair
   with the same records give different odds at x, and the ground-state odds
   at x change with records two steps away; the law is then not a function of
   the neighbour records alone.

The dynamics clause, the relaxation profile lam and the formation site and time
are not derived. Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22.md',
)

import numpy as np
import sympy as sp

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(924)
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
I2 = np.eye(2, dtype=complex)
DIRS = [np.array(v, dtype=float) for v in ([1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1])]


def sdot(v):
    return sum(v[k] * S[k] for k in range(3))


def proj(q):
    return 0.5 * (I2 + sdot(q))


def unit(v):
    return v / np.linalg.norm(v)


def rand_unit():
    return unit(rng.normal(size=3))


def cross_mat(f):
    """Matrix Df with s^T Df t = f.(s x t)."""
    return np.array([[0, f[2], -f[1]], [-f[2], 0, f[0]], [f[1], -f[0], 0]], dtype=float)


def coupling(J, K, D, f):
    return J * np.eye(3) + K * np.outer(f, f) + D * cross_mat(f)


def kron_list(ops):
    out = np.array([[1.0 + 0j]])
    for o in ops:
        out = np.kron(out, o)
    return out


def op(n, placed):
    return kron_list([placed.get(k, I2) for k in range(n)])


# ------------------------------------------------------------ A: projection
print("A. projection lemma")
qx, qy, qz = sp.symbols("qx qy qz", real=True)
Ps = sp.Rational(1, 2) * (sp.eye(2) + qx * sp.Matrix([[0, 1], [1, 0]]) + qy * sp.Matrix([[0, -sp.I], [sp.I, 0]])
                          + qz * sp.Matrix([[1, 0], [0, -1]]))
Ss = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
qs = [qx, qy, qz]
ok = True
for a in range(3):
    diff = (Ps * Ss[a] * Ps - qs[a] * Ps).applyfunc(sp.expand)
    diff = diff.subs(qz ** 2, 1 - qx ** 2 - qy ** 2).applyfunc(sp.expand)
    ok &= diff == sp.zeros(2, 2)
worst = max(np.abs(proj(q) @ S[a] @ proj(q) - q[a] * proj(q)).max() for q in [rand_unit() for _ in range(50)] for a in range(3))
check("P_q s_a P_q = q_a P_q for unit q", ok and worst < 1e-14, f"symbolic on the unit sphere; numeric max {worst:.1e}")


# ------------------------------------------------------------ B: compression
print("B. compression on the seven-qubit star")


def star_H(Ms):
    n = 7
    H = np.zeros((2 ** n, 2 ** n), dtype=complex)
    for fi, M in enumerate(Ms):
        for i in range(3):
            for j in range(3):
                if M[i, j] != 0:
                    H += M[i, j] * op(n, {0: S[i], 1 + fi: S[j]})
    return H


worst, cases = 0.0, 0
for family in ("heisenberg", "full"):
    for _ in range(6):
        if family == "heisenberg":
            J = rng.normal()
            Ms = [coupling(J, 0, 0, f) for f in DIRS]
        else:
            J, K, D = rng.normal(size=3)
            Ms = [coupling(J, K, D, f) for f in DIRS]
        qs_ = [rand_unit() for _ in range(6)]
        P = kron_list([I2] + [proj(q) for q in qs_])
        h = sum(M @ q for M, q in zip(Ms, qs_))
        lhs = P @ star_H(Ms) @ P
        rhs = np.kron(sdot(h), kron_list([proj(q) for q in qs_]))
        worst = max(worst, np.abs(lhs - rhs).max())
        cases += 1
check("P H P = (h(N).s_0) (x) P_N with h(N) = sum_f M_f q_f", worst < 1e-12,
      f"{cases} random cases (Heisenberg and J,K,D); max deviation {worst:.1e}")

# ------------------------------------------------------------ C: isolation
print("C. isolation of a site with six recorded neighbours")
# qubits: 0 = x, 1..6 = neighbours of x (direction DIRS[k-1]), 7 = y beyond neighbour +x
J, K, D = rng.normal(size=3)
n = 8
H = np.zeros((2 ** n, 2 ** n), dtype=complex)
bonds = [(0, 1 + k, DIRS[k]) for k in range(6)] + [(1, 7, DIRS[0])]
for (u, v, f) in bonds:
    M = coupling(J, K, D, f)
    for i in range(3):
        for j in range(3):
            H += M[i, j] * op(n, {u: S[i], v: S[j]})
qs_ = [rand_unit() for _ in range(6)]
P = op(n, {1 + k: proj(qs_[k]) for k in range(6)})
C = P @ H @ P
hx = sum(coupling(J, K, D, f) @ q for f, q in zip(DIRS, qs_))
hy = coupling(J, K, D, DIRS[0]).T @ qs_[0]      # y sees neighbour 1 across the bond (1, y)
expect = (op(n, {0: sdot(hx)}) + op(n, {7: sdot(hy)})) @ P
dev = np.abs(C - expect).max()
check("the compressed generator is h_x.s_x + h_y.s_y with no x-y coupling", dev < 1e-12, f"max deviation {dev:.1e}")

# ------------------------------------------------------------ D: stationarity
print("D. stationary states of the isolated site")
ok_line, worst_avg = True, 0.0
for _ in range(20):
    h = rng.normal(size=3)
    hh = unit(h)
    Hs = sdot(h)
    # commutant within Hermitian 2x2: solve [Hs, rho] = 0 on the basis {1, s_x, s_y, s_z}
    basis = [I2] + S
    cols = []
    for b in basis:
        c = Hs @ b - b @ Hs
        cols.append([np.real(np.trace(b2.conj().T @ c)) / 2 for b2 in basis] + [np.imag(np.trace(b2.conj().T @ c)) / 2 for b2 in basis])
    Mc = np.array(cols).T
    u, s, vt = np.linalg.svd(Mc)
    null = vt[np.sum(s > 1e-10):]
    span_ok = null.shape[0] == 2
    # the null space must be spanned by 1 and h^.s
    target = np.array([[1, 0, 0, 0], [0, *hh]])
    span_ok &= np.linalg.matrix_rank(np.vstack([null, target]), tol=1e-9) == 2
    ok_line &= span_ok
    # time average over one period of a random initial state
    r0 = unit(rng.normal(size=3)) * rng.uniform(0, 1)
    rho0 = 0.5 * (I2 + sdot(r0))
    w = 2 * np.linalg.norm(h)
    T = 2 * np.pi / w
    ts = np.linspace(0, T, 2001)[:-1]
    avg = np.zeros((2, 2), dtype=complex)
    for t in ts:
        U = np.cos(np.linalg.norm(h) * t) * I2 - 1j * np.sin(np.linalg.norm(h) * t) * sdot(hh)
        avg += U @ rho0 @ U.conj().T
    avg /= len(ts)
    want = 0.5 * (I2 + (r0 @ hh) * sdot(hh))
    worst_avg = max(worst_avg, np.abs(avg - want).max())
check("[h.s, rho] = 0 exactly on the line rho = (1 + lam h^.s)/2", ok_line, "20 random fields; commutant = span{1, h^.s}")
check("time averages of random states land on the line with lam = r0.h^", worst_avg < 1e-12, f"max deviation {worst_avg:.1e}")

# ------------------------------------------------------------ E: odds
print("E. odds read from a stationary state")
worst = 0.0
for _ in range(200):
    hh, p, lam = rand_unit(), rand_unit(), rng.uniform(-1, 1)
    rho = 0.5 * (I2 + lam * sdot(hh))
    w_p = np.real(np.trace(proj(p) @ rho))
    w_m = np.real(np.trace(proj(-p) @ rho))
    worst = max(worst, abs(w_p - (1 + lam * p @ hh) / 2), abs(w_p + w_m - 1))
# Husimi normalisation by Lebedev-free quadrature: Fibonacci sphere average of 1 + lam a.h is 1 exactly in the limit
N = 20000
k = np.arange(N) + 0.5
phi = np.arccos(1 - 2 * k / N)
theta = np.pi * (1 + 5 ** 0.5) * k
pts = np.stack([np.cos(theta) * np.sin(phi), np.sin(theta) * np.sin(phi), np.cos(phi)], axis=1)
hh, lam = rand_unit(), 0.7
dens = 1 + lam * pts @ hh
check("w(p|N) = (1 + lam p.h^)/2 on every antipodal menu; Husimi density normalised",
      worst < 1e-14 and abs(dens.mean() - 1) < 1e-4, f"200 random menus, max {worst:.1e}; sphere mean {dens.mean():.5f}")

# ------------------------------------------------------------ F: Heisenberg
print("F. Heisenberg with one effective neighbour")
pent = [np.array([np.cos(2 * np.pi * k / 5), np.sin(2 * np.pi * k / 5), 0.0]) for k in range(5)]
Rr = np.linalg.qr(rng.normal(size=(3, 3)))[0]
five = [Rr @ v for v in pent]
q1 = rand_unit()
recs = [q1] + five
Ssum = sum(recs)
res_ok = np.linalg.norm(Ssum - q1) < 1e-12
fvals = {}
for J in (-1.3, 0.8):
    h = J * Ssum
    Hs = sdot(h)
    evals, evecs = np.linalg.eigh(Hs)
    gs = np.outer(evecs[:, 0], evecs[:, 0].conj())
    ts = np.linspace(-1, 1, 9)
    fs = []
    for t in ts:
        # a menu {p, -p} with p.q1 = t
        perp = unit(np.cross(q1, rand_unit()))
        p = t * q1 + np.sqrt(max(0, 1 - t * t)) * perp
        fs.append(np.real(np.trace(proj(p) @ gs)))
    fvals[J] = (ts, np.array(fs))
fer = np.abs(fvals[-1.3][1] - (1 + fvals[-1.3][0]) / 2).max()
afm = np.abs(fvals[0.8][1] - (1 - fvals[0.8][0]) / 2).max()
check("ground state, J < 0: f(t) = (1 + t)/2 (repeat certainty f(1) = 1); J > 0: f(t) = (1 - t)/2",
      res_ok and fer < 1e-12 and afm < 1e-12, f"resultant = q1; deviations {fer:.1e}, {afm:.1e}")
worst = 0.0
for beta in (0.3, 1.0, 2.5):
    J = -0.9
    h = J * Ssum
    rho = np.array([[1, 0], [0, 1]], dtype=complex)
    ev, V = np.linalg.eigh(sdot(h))
    rho = V @ np.diag(np.exp(-beta * ev)) @ V.conj().T
    rho /= np.trace(rho)
    c = np.tanh(beta * abs(J))
    for t in np.linspace(-1, 1, 7):
        perp = unit(np.cross(q1, rand_unit()))
        p = t * q1 + np.sqrt(max(0, 1 - t * t)) * perp
        worst = max(worst, abs(np.real(np.trace(proj(p) @ rho)) - (1 + c * t) / 2))
check("thermal relaxation: f(t) = (1 + tanh(beta|J|) t)/2 for J < 0, affine at every beta", worst < 1e-12, f"max {worst:.1e}")
tt = sp.symbols("t")
witness = [(1 + tt ** 3) / 2, (1 + tt) / 2 + tt * (1 - tt ** 2) / 8]
nonaff = all(sp.degree(sp.expand(wf), tt) > 1 for wf in witness)
mid = [wf.subs(tt, sp.Rational(1, 2)) for wf in witness]
check("the landed non-affine witnesses have degree 3 in t; every stationary state gives degree <= 1",
      nonaff and mid == [sp.Rational(9, 16), sp.Rational(51, 64)], f"midpoint values {mid[0]}, {mid[1]} against 3/4")

# ------------------------------------------------------------ G: full soldering
print("G. full soldering: the field of six records")
worst, turn = 0.0, 0.0
for _ in range(20):
    J, K, D = rng.normal(size=3)
    qs_ = [rand_unit() for _ in range(6)]
    h1 = sum(coupling(J, K, D, f) @ q for f, q in zip(DIRS, qs_))
    h2 = J * sum(qs_) + K * sum(f * (f @ q) for f, q in zip(DIRS, qs_)) + D * sum(np.cross(q, f) for f, q in zip(DIRS, qs_))
    worst = max(worst, np.abs(h1 - h2).max())
qs_ = [rand_unit() for _ in range(6)]
hJ = sum(qs_)
hD = sum(coupling(1.0, 0, 0.8, f) @ q for f, q in zip(DIRS, qs_))
turn = np.degrees(np.arccos(np.clip(unit(hJ) @ unit(hD), -1, 1)))
check("h(N) = J sum q_f + K sum f (f.q_f) + D sum q_f x f; the Moriya part turns h away from the resultant",
      worst < 1e-12 and turn > 1.0, f"max deviation {worst:.1e}; turn at D/J = 0.8: {turn:.1f} degrees")

# ------------------------------------------------------------ H: scope
print("H. scope: a site with an unrecorded neighbour")
J = -1.0
qs_ = [rand_unit() for _ in range(5)]            # records on five neighbours of x (not direction +x)
qy = [rand_unit() for _ in range(5)]             # records on five neighbours of y
hx = J * sum(qs_)
hy = J * sum(qy)
Hpair = J * sum(np.kron(S[a], S[a]) for a in range(3)) + np.kron(sdot(hx), I2) + np.kron(I2, sdot(hy))
ev, V = np.linalg.eigh(Hpair)
odds = []
p = unit(hx)
for k in range(4):
    st = V[:, k]
    rho_x = np.einsum('ij,kj->ik', st.reshape(2, 2), st.reshape(2, 2).conj())
    odds.append(np.real(np.trace(proj(p) @ rho_x)))
spread = max(odds) - min(odds)
ent = []
for k in range(4):
    st = V[:, k].reshape(2, 2)
    sv = np.linalg.svd(st, compute_uv=False)
    ent.append(float(sv[-1]))
check("two stationary pair states with the same records give different odds at x",
      spread > 0.1 and max(ent) > 1e-3, f"odds of the four pair eigenstates on {{p,-p}}: {', '.join(f'{o:.3f}' for o in odds)}")


def ground_odds_x(hx, hy, p):
    Hp = J * sum(np.kron(S[a], S[a]) for a in range(3)) + np.kron(sdot(hx), I2) + np.kron(I2, sdot(hy))
    ev, V = np.linalg.eigh(Hp)
    st = V[:, 0].reshape(2, 2)
    return np.real(np.trace(proj(p) @ (st @ st.conj().T)))


hx0 = J * sum(five)                              # x's five records cancel (a pentagon)
pz = np.array([0.0, 0.0, 1.0])
vals = [ground_odds_x(hx0, J * sum(rand_unit() for _ in range(5)), pz) for _ in range(6)]
check("ground-state odds at x change with records two steps away (beyond x's neighbours)",
      max(vals) - min(vals) > 0.2, f"x's five records cancel; six draws of y's other records: odds {min(vals):.3f} to {max(vals):.3f}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
