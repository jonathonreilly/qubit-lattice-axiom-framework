#!/usr/bin/env python3
"""One dynamics clause: consolidated certificates and decision-point ledger.

A synthesis of the 2026-09-24 campaign (open PRs 9040, 9041, 9043, 9046,
9048, 9050, 9052, 9054, 9066, 9069, 9072). Each check re-derives, in a fast independent form,
the load-bearing identity of one block; the ledger records which supplied
decision points each block uses and checks the ledger is closed (every point
used is declared, every declared point is used). Nothing here adopts a
decision point or adds a premise.

Checks:

L. Ledger: the decision points used by the eleven blocks are exactly the
   declared ones.
1. (9040) Possibility covariance leaves the Heisenberg coupling alone; full
   soldering leaves three couplings.
2. (9041) Records act as fields (P_q s P_q = q P_q); a site with six recorded
   Heisenberg neighbours has stationary states along the resultant;
   ferromagnetic ground relaxation gives f(t) = (1 + t)/2.
3. (9043) Random records-only causal models stay at CHSH <= 2; the
   antiferromagnetic Heisenberg pair reaches 2 sqrt 2.
4. (9046) On the cube graph, isolated formation orders exist exactly for
   independent forming sets with initially recorded neighbourhoods.
5. (9048) The pi-flux staircase tube has eps(k)^2 = 12 + 8 cos k, gap 2|K|.
6. (9050) The Moriya-twisted pair has E(a,b) - E(b,a) = -2 sin(phi)(a x b).e.
7. (9052) Record frequencies: Var F = (1/4n^2) sum_ij C_ij for a random state.
8. (9054) The 20-site three-direction network has one local loop per cell;
   its local flux splits the sector energies and its dispersive Majorana
   bands are gapped above two flat zero-mode bands per cell.
9. (9066) Two-site terms on a vertex-link-vertex window that commute with
   both Gauss operators commute with the link field; among the four landed
   rotation actions an oriented link field is covariant for full soldering
   alone and a vertex charge needs an invariant axis; the soft-Gauss ring
   element is -5 h^4 / (32 U^3).
10. (9069) Under full soldering no role's stabilizer fixes a Bloch axis; with
   a soldered link, covariant vertex-link terms flip the link only for a
   fully soldered vertex (dimensions 0, 0, 0, 2); single-link flips commute
   (Levin-Wen exchange phase 1).
11. (9072) The covariant plaquette generators annihilating the symmetric
   flippable state and all other configurations are one ray, the
   Rokhsar-Kivelson projector 2g |-><-|.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    'docs/DYNAMICS_CLAUSE_CAMPAIGN_SYNTHESIS_WHAT_ONE_LOCAL_DYNAMICS_CLAUSE_BUYS_AND_WHAT_IT_LEAVES_OPEN_BOUNDED_THEOREM_NOTE_2026-09-24.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
)

import numpy as np

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
S = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]
I2 = np.eye(2, dtype=complex)


def sdot(v):
    return sum(v[k] * S[k] for k in range(3))


def proj(q):
    return 0.5 * (I2 + sdot(q))


def unit(v):
    return v / np.linalg.norm(v)


# ------------------------------------------------------------------ ledger
DECLARED = {
    "D-dyn": "covariant nearest-neighbour two-site Hermitian generator",
    "D-pc": "possibility covariance (versus a soldering)",
    "D-sold": "full soldering of the rotations to the Bloch vector",
    "D-perm": "record permanence as compression onto record projectors",
    "D-tr": "odds read from the site's state by the trace rule",
    "D-relax": "relaxation profile / which state records form from",
    "D-nn": "Admissibility conditions: records alone versus quantum states",
    "D-menu": "antipodal menus",
    "D-set": "independently formed setting records",
    "D-pattern": "record carving and contents",
    "D-sign": "sign of the Moriya coupling (handedness)",
    "D-roles": "doubled-coordinate roles (vertex, link, plaquette, cube sites)",
    "D-gauss": "a Gauss law on link sites, exact or as a soft vertex-star energy",
    "D-star": "a covariant generator on a plaquette site's four link neighbours",
}
USED = {
    9040: {"D-dyn", "D-pc", "D-sold"},
    9041: {"D-dyn", "D-perm", "D-tr", "D-relax", "D-menu"},
    9043: {"D-dyn", "D-perm", "D-tr", "D-menu", "D-set", "D-nn"},
    9046: {"D-dyn", "D-perm", "D-tr", "D-nn"},
    9048: {"D-dyn", "D-sold", "D-perm", "D-pattern"},
    9050: {"D-dyn", "D-sold", "D-tr", "D-menu", "D-sign"},
    9052: {"D-dyn", "D-tr", "D-menu", "D-relax"},
    9054: {"D-dyn", "D-sold", "D-perm", "D-pattern"},
    9066: {"D-dyn", "D-sold", "D-roles", "D-gauss", "D-pattern"},
    9069: {"D-dyn", "D-sold", "D-roles", "D-gauss", "D-pattern"},
    9072: {"D-dyn", "D-sold", "D-roles", "D-gauss", "D-star", "D-tr", "D-pattern"},
}
used_all = set().union(*USED.values())
check("ledger: the decision points used are exactly the declared ones",
      used_all == set(DECLARED), f"{len(DECLARED)} declared, {len(used_all)} used across {len(USED)} blocks")

# --------------------------------------------------------------- 1: couplings
print("1. the covariant nearest-neighbour couplings")
O = []
for p in itertools.permutations(range(3)):
    for s in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, p[i]] = s[i]
        if round(np.linalg.det(R)) == 1:
            O.append(R)
ez = np.array([0.0, 0.0, 1.0])
stab = [R for R in O if np.allclose(R @ ez, ez)]
flip = [R for R in O if np.allclose(R @ ez, -ez)][0]
T = np.zeros((9, 9))
for i in range(3):
    for j in range(3):
        T[3 * j + i, 3 * i + j] = 1


def coupling_dim(rho, internal):
    rows = [np.kron(rho(R), rho(R)) - np.eye(9) for R in stab]
    rows.append(np.kron(rho(flip), rho(flip)) - T)
    if internal:
        gens = [np.array([[0, 0, 0], [0, 0, -1], [0, 1, 0.0]]), np.array([[0, 0, 1], [0, 0, 0], [-1, 0, 0.0]]),
                np.array([[0, -1, 0], [1, 0, 0], [0, 0, 0.0]])]
        for L in gens:
            rows.append(np.kron(L, np.eye(3)) - np.kron(np.eye(3), L.T))
    A = np.vstack(rows)
    return 9 - np.linalg.matrix_rank(A, tol=1e-9)


full = lambda R: R
trivial = lambda R: np.eye(3)
check("possibility covariance leaves one coupling (Heisenberg); full soldering leaves three",
      coupling_dim(trivial, True) == 1 and coupling_dim(full, True) == 1 and coupling_dim(full, False) == 3,
      f"dims {coupling_dim(trivial, True)}, {coupling_dim(full, True)}, {coupling_dim(full, False)}")

# ------------------------------------------------------------ 2: fields, law
print("2. records act as fields")
lem = max(np.abs(proj(q) @ S[a] @ proj(q) - q[a] * proj(q)).max() for q in [unit(rng.normal(size=3)) for _ in range(20)]
          for a in range(3))
qs = [unit(rng.normal(size=3)) for _ in range(6)]
Sres = sum(qs)
Hs = -1.0 * sdot(Sres)                                 # J = -1, Heisenberg field J * resultant
ev, V = np.linalg.eigh(Hs)
gs = np.outer(V[:, 0], V[:, 0].conj())
bl = np.array([np.real(np.trace(gs @ S[a])) for a in range(3)])
aligned = np.allclose(bl, unit(Sres))
pent = [np.array([np.cos(2 * np.pi * k / 5), np.sin(2 * np.pi * k / 5), 0.0]) for k in range(5)]
q1 = unit(rng.normal(size=3))
Hp = -1.0 * sdot(q1 + sum(pent))
ev, V = np.linalg.eigh(Hp)
g1 = np.outer(V[:, 0], V[:, 0].conj())
fdev = 0.0
for t in np.linspace(-1, 1, 5):
    perp = unit(np.cross(q1, rng.normal(size=3)))
    p = t * q1 + np.sqrt(max(0.0, 1 - t * t)) * perp
    fdev = max(fdev, abs(np.real(np.trace(proj(p) @ g1)) - (1 + t) / 2))
check("P_q s P_q = q P_q; ground state points along the resultant; pentagon gives f(t) = (1 + t)/2",
      lem < 1e-14 and aligned and fdev < 1e-12, f"lemma {lem:.1e}; law deviation {fdev:.1e}")

# ----------------------------------------------------------------- 3: Bell
print("3. Bell values")


def chsh(E):
    return max(abs(E[0][0] + E[0][1] + E[1][0] - E[1][1]), abs(E[0][0] + E[0][1] - E[1][0] + E[1][1]),
               abs(E[0][0] - E[0][1] + E[1][0] + E[1][1]), abs(-E[0][0] + E[0][1] + E[1][0] + E[1][1]))


worst = 0.0
for _ in range(3000):
    k = 3
    p0 = rng.dirichlet(np.ones(k))
    Ka = rng.dirichlet(np.ones(2), size=2 * k)
    Kb = rng.dirichlet(np.ones(2), size=2 * k)
    E = [[sum(p0[w] * (Ka[sa * k + w][0] - Ka[sa * k + w][1]) * (Kb[sb * k + w][0] - Kb[sb * k + w][1])
              for w in range(k)) for sb in range(2)] for sa in range(2)]
    worst = max(worst, chsh(E))
singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
ang = [(0.0, np.pi / 2), (np.pi / 4, -np.pi / 4)]
Es = [[np.real(singlet @ np.kron(np.cos(a) * S[2] + np.sin(a) * S[0], np.cos(b) * S[2] + np.sin(b) * S[0]) @ singlet)
       for b in ang[1]] for a in ang[0]]
check("records-only shared-source models stay at <= 2; the singlet reaches 2 sqrt 2",
      worst <= 2 + 1e-12 and abs(chsh(Es) - 2 * np.sqrt(2)) < 1e-12, f"largest records-only {worst:.6f}; singlet {chsh(Es):.6f}")

# ------------------------------------------------------- 4: isolated orders
print("4. isolated formation orders on the cube graph")
Q3 = list(itertools.product((0, 1), repeat=3))
nbr = {v: [w for w in Q3 if sum(abs(a - b) for a, b in zip(v, w)) == 1] for v in Q3}
agree = 0
for labels in itertools.product("RFN", repeat=8):
    lab = dict(zip(Q3, labels))
    F = [v for v in Q3 if lab[v] == "F"]
    R0 = {v for v in Q3 if lab[v] == "R"}
    exists = False
    for order in itertools.permutations(F):
        rec, ok = set(R0), True
        for v in order:
            if not all(w in rec for w in nbr[v]):
                ok = False
                break
            rec.add(v)
        if ok:
            exists = True
            break
    agree += exists == (all(w not in F for v in F for w in nbr[v]) and all(w in R0 for v in F for w in nbr[v]))
check("an isolated order exists exactly for independent F with neighbourhood in R0", agree == 3 ** 8, f"{agree} of 6561")

# --------------------------------------------------------------- 5: the tube
print("5. the pi-flux staircase tube")
cellbonds = [(0, 1, 0), (2, 3, 0), (0, 2, 0), (1, 3, 0), (0, 2, 1), (1, 3, 1)]
u_pi = (1, 1, 1, -1, 1, -1)
dev = 0.0
for kk in np.linspace(-np.pi, np.pi, 41):
    A = np.zeros((4, 4), dtype=complex)
    for (j, k2, dz), ub in zip(cellbonds, u_pi):
        t = -2 * ub * np.exp(1j * kk * dz)
        A[j, k2] += t
        A[k2, j] -= np.conj(t)
    evs = np.sort(np.abs(np.linalg.eigvalsh(1j * A)))
    dev = max(dev, max(abs(x ** 2 - (12 + 8 * np.cos(kk))) for x in evs))
fxy = u_pi[0] * u_pi[3] * u_pi[1] * u_pi[2]
fxz = u_pi[4] * u_pi[1] * u_pi[5] * u_pi[0]
check("pi flux through both plaquettes: eps(k)^2 = 12 + 8 cos k, gap 2|K| at k = pi",
      fxy == -1 and fxz == -1 and dev < 1e-10, f"bond-product fluxes ({fxy}, {fxz}); max deviation {dev:.1e}")

# --------------------------------------------------------------- 6: Moriya
print("6. the handed record statistic")
Dv, Jv = 0.7, 1.0
H = Jv * sum(np.kron(S[a], S[a]) for a in range(3)) + Dv * (np.kron(S[0], S[1]) - np.kron(S[1], S[0]))
ev, V = np.linalg.eigh(H)
psi = V[:, 0]
cs = []
for _ in range(50):
    a, b = unit(rng.normal(size=3)), unit(rng.normal(size=3))
    Eab = np.real(psi.conj() @ np.kron(sdot(a), sdot(b)) @ psi)
    Eba = np.real(psi.conj() @ np.kron(sdot(b), sdot(a)) @ psi)
    tri = np.cross(a, b)[2]
    if abs(tri) > 0.2:
        cs.append((Eab - Eba) / tri)
check("E(a,b) - E(b,a) = -2 sin(phi) (a x b).z at D/J = 0.7", np.std(cs) < 1e-10 and abs(np.mean(cs) + 2 * np.sin(np.arctan2(Dv, Jv))) < 1e-10,
      f"c = {np.mean(cs):.10f}")

# ------------------------------------------------------------ 7: frequencies
print("7. record frequencies")
n = 5
psi = rng.normal(size=2 ** n) + 1j * rng.normal(size=2 ** n)
psi /= np.linalg.norm(psi)
menus = [unit(rng.normal(size=3)) for _ in range(n)]


def op(placed):
    return reduce(np.kron, [placed.get(k, I2) for k in range(n)])


X = [op({i: sdot(menus[i])}) for i in range(n)]
m = [np.real(psi.conj() @ X[i] @ psi) for i in range(n)]
C = sum(np.real(psi.conj() @ X[i] @ X[j] @ psi) - m[i] * m[j] for i in range(n) for j in range(n))
law = {}
for outs in itertools.product((1, -1), repeat=n):
    P = reduce(np.matmul, [op({i: proj(outs[i] * menus[i])}) for i in range(n)])
    law[outs] = np.real(psi.conj() @ P @ psi)
EF = sum(pr * sum(1 for o in outs if o == 1) / n for outs, pr in law.items())
VF = sum(pr * (sum(1 for o in outs if o == 1) / n) ** 2 for outs, pr in law.items()) - EF ** 2
check("Var F = (1/4n^2) sum_ij C_ij", abs(VF - C / (4 * n * n)) < 1e-12, f"{VF:.10f} vs {C / (4 * n * n):.10f}")

# ------------------------------------------------------- 8: the 3D network
print("8. the 20-site three-direction network")
N20 = [(0, 0, 0), (0, 0, 3), (0, 1, 0), (0, 2, 1), (0, 2, 2), (0, 3, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
       (1, 1, 1), (1, 2, 1), (2, 0, 1), (2, 0, 2), (2, 1, 1), (2, 1, 2), (3, 0, 0), (3, 1, 2), (3, 2, 2),
       (3, 3, 0), (3, 3, 1)]
cs_ = set(N20)
ix = {s: i for i, s in enumerate(N20)}


def nb(s, ax, d):
    t = list(s)
    t[ax] = (t[ax] + d) % 4
    return tuple(t)


bonds = []
for s in N20:
    for ax in range(3):
        t = list(s)
        t[ax] += 1
        off = [0, 0, 0]
        if t[ax] == 4:
            t[ax], off[ax] = 0, 1
        t = tuple(t)
        if t in cs_:
            bonds.append((ix[s], ix[t], ax, tuple(off)))
vg = np.array([1.0, np.sqrt(2.0), np.sqrt(3.0)]) / np.sqrt(6.0)
content = {}
for r in itertools.product(range(4), repeat=3):
    if r in cs_:
        continue
    cons = {ax for ax in range(3) for d in (1, -1) if nb(r, ax, d) in cs_ and nb(nb(r, ax, d), ax, d) in cs_}
    q = vg.copy()
    for a in cons:
        q[a] = 0.0
    content[r] = q / np.linalg.norm(q)
df = {}
for s in N20:
    for ax in range(3):
        if nb(s, ax, 1) not in cs_ and nb(s, ax, -1) not in cs_:
            df[(ix[s], ax)] = content[nb(s, ax, 1)][ax] + content[nb(s, ax, -1)][ax]
live = list(df)
uf = list(range(20))


def fnd(a):
    while uf[a] != a:
        uf[a] = uf[uf[a]]
        a = uf[a]
    return a


tree, non = [], []
for b in bonds:
    ra, rb = fnd(b[0]), fnd(b[1])
    if ra != rb:
        uf[ra] = rb
        tree.append(b)
    else:
        non.append(b)


def bloch(u_non, k):
    uu = {b: 1 for b in tree}
    uu.update({b: v for b, v in zip(non, u_non)})
    N = 20 + len(live)
    A = np.zeros((N, N), dtype=complex)
    for b in bonds:
        j, k2, ax, off = b
        t = -2 * uu[b] * np.exp(1j * np.dot(k, off))
        A[j, k2] += t
        A[k2, j] -= np.conj(t)
    for pos, (j, ax) in enumerate(live):
        A[20 + pos, j] += 2 * df[(j, ax)]
        A[j, 20 + pos] -= 2 * df[(j, ax)]
    return np.linalg.eigvalsh(1j * A)


ks = [np.array(k) * 2 * np.pi / 6 for k in itertools.product(range(6), repeat=3)]
secs = sorted((sum(-0.5 * e[e > 0].sum() for e in (bloch(u, k) for k in ks)) / len(ks), u)
              for u in itertools.product((1, -1), repeat=len(non)))
levels = sorted({round(e, 5) for e, u in secs})
z, g = 0, 9.0
for kk in itertools.product(range(8), repeat=3):
    e = np.sort(np.abs(bloch(secs[0][1], np.array(kk) * 2 * np.pi / 8)))
    zz = int(np.sum(e < 1e-9))
    z = max(z, zz)
    g = min(g, e[zz])
check("one local loop per cell; sectors split by the local flux; two flat zero modes per cell, gap above them",
      len(bonds) - 20 + 1 - 3 == 1 and len(levels) == 2 and z == 2 and g > 0.5,
      f"sector energies {levels[0]:.5f}, {levels[1]:.5f}; flat zero modes {z}; gap on 8^3 grid {g:.4f}")

# ------------------------------------------------------ 9: the Gauss freeze
print("9. an exact Gauss law and the two-site clause")
PA = [I2, S[0], S[1], S[2]]
# window v (vertex), l (link), w (vertex); dynamical charges s^z on v and w
Ew = np.kron(np.kron(I2, S[2] / 2), I2)
Qv_ = np.kron(np.kron(S[2] / 2, I2), I2)
Qw_ = np.kron(np.kron(I2, I2), S[2] / 2)
gauss = [Ew - Qv_, -Ew - Qw_]
basis = [np.kron(np.kron(A, B), I2) for A in PA for B in PA] + [np.kron(np.kron(I2, A), B) for A in PA for B in PA]
cols = [np.concatenate([(b @ g - g @ b).ravel() for g in gauss]) for b in basis]
from scipy.linalg import null_space as _ns
nsp = _ns(np.array(cols).T)
frozen = max(np.linalg.norm(Hc @ Ew - Ew @ Hc) for Hc in
             [sum(nsp[k, c] * basis[k] for k in range(len(basis))) for c in range(nsp.shape[1])])
psign = lambda R: round(np.linalg.det(np.abs(R)))
acts = [lambda R: np.eye(3), lambda R: np.diag([1.0, psign(R), psign(R)]), lambda R: psign(R) * np.abs(R), lambda R: R]
itw = [_ns(np.vstack([np.kron(a(R), np.eye(3)) - np.kron(np.eye(3), R.T) for R in O])).shape[1] for a in acts]
inv = [_ns(np.vstack([a(R) - np.eye(3) for R in O])).shape[1] for a in acts]
# ring element: flips of the four plaquette links in all 24 orders, charges at the corners
corner_of = [(0, 1), (1, 2), (2, 3), (3, 0)]   # link k joins corners corner_of[k]
amp = 0.0
for order in itertools.permutations(range(4)):
    den = 1.0
    ch = [0, 0, 0, 0]
    for m in range(3):
        a_, b_ = corner_of[order[m]]
        ch[a_] += 1
        ch[b_] -= 1
        den *= -sum(c * c for c in ch)
    amp += 1 / den
amp /= 16
check("two-site Gauss-invariant terms freeze E_l; oriented link field covariant for full soldering alone; ring element -5/32",
      frozen < 1e-10 and itw == [0, 0, 0, 1] and inv == [3, 1, 0, 0] and abs(amp + 5 / 32) < 1e-12,
      f"max |[H, E_l]| {frozen:.1e} over {nsp.shape[1]} invariant terms; intertwiners {itw}; invariant axes {inv}; ring element {amp:.6f} h^4/U^3")

# ------------------------------------------------------ 10: charges
print("10. where charge can live")
def _lift(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(ang, 0):
        return I2.copy()
    if np.isclose(ang, np.pi):
        w_, v_ = np.linalg.eig(R)
        nv = np.real(v_[:, np.argmin(abs(w_ - 1))])
    else:
        nv = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    nv = nv / np.linalg.norm(nv)
    from scipy.linalg import expm as _expm
    return _expm(-1j * ang * sum(nv[k] * S[k] for k in range(3)) / 2)


def _role(x):
    return sum(int(c) % 2 for c in x)


_win = [np.array(p_) for p_ in itertools.product(range(-2, 3), repeat=3)]
fixed_axes = []
for c_ in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]:
    c_ = np.array(c_)
    st_ = [R for R in O if all(_role(c_ + R @ (p_ - c_)) == _role(p_) for p_ in _win)]
    fixed_axes.append(_ns(np.vstack([R - np.eye(3) for R in st_])).shape[1])
bstab = [R for R in O if np.allclose(R @ np.array([1.0, 0, 0]), [1, 0, 0])]
El = np.kron(I2, S[0] / 2)
b2 = [np.kron(A, B) for A in PA for B in PA]
fd = []
for a_ in acts:
    rows_ = []
    for R in bstab:
        V_ = np.kron(_lift(a_(R)), _lift(R))
        rows_.append(np.array([(V_ @ B @ V_.conj().T).ravel() for B in b2]).T - np.array([B.ravel() for B in b2]).T)
    nsb = _ns(np.vstack(rows_))
    ops_ = [sum(nsb[k, c] * b2[k] for k in range(16)) for c in range(nsb.shape[1])]
    fd.append(int(np.linalg.matrix_rank(np.array([(o @ El - El @ o).ravel() for o in ops_]), tol=1e-9)))
t3 = [np.kron(np.kron(S[0], I2), I2), np.kron(np.kron(I2, S[1]), I2), np.kron(np.kron(I2, I2), S[2])]
lw = np.linalg.norm(t3[0] @ t3[1].conj().T @ t3[2] - t3[2] @ t3[1].conj().T @ t3[0])
check("no role fixes a Bloch axis; soldered links flip only against fully soldered vertices; defect hops commute",
      fixed_axes == [0, 0, 0, 0] and fd == [0, 0, 0, 2] and lw < 1e-12,
      f"fixed axes (vertex, link, plaquette, cube) {fixed_axes}; link-flip dims (trivial, sign twist, axis, full) {fd}; Levin-Wen {lw:.0e}")

# ------------------------------------------------ 11: the plaquette clause
print("11. the covariant plaquette clause")
confs4 = list(itertools.product([1, -1], repeat=4))
cr = np.array([[1, 0, 0, 1], [-1, 1, 0, 0], [0, -1, -1, 0], [0, 0, 1, -1]])
flp = [c for c in confs4 if not np.any(cr @ np.array(c))]
ix = {c: i for i, c in enumerate(confs4)}


def circ_kind(c):
    cc = (c[0], c[1], -c[2], -c[3])
    w_ = sum(1 for x in cc if x > 0)
    return "flip" if w_ in (0, 4) else ("odd" if w_ in (1, 3) else ("opp" if cc[0] == cc[2] else "adj"))


rg = np.zeros((16, 16))
rg[ix[flp[0]], ix[flp[1]]] = rg[ix[flp[1]], ix[flp[0]]] = 1.0
gens_ = [-rg] + [np.diag([1.0 if circ_kind(c) == k else 0.0 for c in confs4]) for k in ("flip", "opp", "adj", "odd")]
sv = np.zeros(16)
sv[ix[flp[0]]] = sv[ix[flp[1]]] = 1
tg = [sv] + [np.eye(16)[ix[c]] for c in confs4 if c not in flp]
nsr = _ns(np.array([np.concatenate([G_ @ t_ for t_ in tg]) for G_ in gens_]).T)
cf = nsr[:, 0] / nsr[0, 0]
check("the frustration-free covariant plaquette clause is the Rokhsar-Kivelson projector",
      nsr.shape[1] == 1 and np.allclose(cf, [1, 1, 0, 0, 0]),
      f"solution dimension {nsr.shape[1]}; coefficients (ring, flippable, opposite, adjacent, odd) {np.round(cf, 12).tolist()}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
