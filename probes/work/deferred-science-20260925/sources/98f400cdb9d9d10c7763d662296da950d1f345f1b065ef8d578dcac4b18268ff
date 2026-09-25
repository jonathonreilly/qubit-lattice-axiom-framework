#!/usr/bin/env python3
"""One dynamics clause: consolidated certificates and decision-point ledger.

A synthesis of the 2026-09-24 campaign (open PRs 9040, 9041, 9043, 9046,
9048, 9050, 9052, 9054, 9066, 9069, 9072, 9077, 9081, 9083, 9084, 9085, 9086, 9088,
9095, 9097, 9112). Each check re-derives, in a fast independent form,
the load-bearing identity of one block; the ledger records which supplied
decision points each block uses and checks the ledger is closed (every point
used is declared, every declared point is used). Nothing here adopts a
decision point or adds a premise.

Checks:

L. Ledger: the decision points used by the twenty-one blocks are exactly the
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
11. (9072) The covariant plaquette generators annihilating the equal-amplitude
   flippable state and all other configurations are the line of the
   Rokhsar-Kivelson projector 2g |-><-|.
12. (9077) Each row of the landed tensor vector constraint uses exactly its
   link site's six neighbours; every slot enters two or more rows; slot
   sites are never adjacent; no single neighbourhood supports a move.
13. (9081) The SU(2) action on one qubit has scalar commutant; the
   2N-dimensional link (N, 1) + (1, N) carries a covariant link operator.
14. (9083) Under the compression update a record on a purifying partner
   steers a qubit to either end of a chord with the chord weights; the
   trace rule matches the steered average and a cubic deformation does
   not; with a replacement update that keeps only the lock, an anti-Born
   law passes locality of marginals too.
15. (9084) A Weinberg-type precession lets a distant record shift a later
   marginal; channels do not; the transpose on half a singlet is negative.
16. (9085) Joint record effects with Born marginals are product projectors,
   so the distant update consistent with them is the Lueders conditional
   state.
17. (9086) Proportional Kraus operators give a unitary conjugation; random
   non-unitary channels mix some pure state.
18. (9088) Under possibility covariance time-reversal-odd star terms through
   the centre vanish, while the orientation-weighted octant chirality is
   invariant; the tripod is a product of three bond operators, so its
   Majorana degree is 4.
19. (9095) The path sum of a planar piece of the tensor constraint is
   111150053/31850496 over its 2304 monotone partial moves; the same sum for
   the U(1) plaquette ring is 5/2.
20. (9097) A chain of Kitaev sites with record fields on its dangling axes
   has a bipartite Majorana coupling graph (S H S = -H); a field along a
   leaf's kept axis matches the exact spin spectrum and breaks S.
21. (9112) Covariant odd star terms under full soldering, as signed rotation
   orbits, number 37 at weights 1 and 3; Kitaev's pattern on a three-site
   cluster maps to the same-class Majorana bilinear -i eps u u c c, checked
   against the exact spin spectrum.

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
    "D-dyn": "covariant nearest-neighbour two-site Hermitian generator, with the Hilbert-space kinematics it acts on",
    "D-pc": "possibility covariance (versus a soldering)",
    "D-sold": "full soldering of the rotations to the Bloch vector",
    "D-perm": "records update by compression: the lock, the support condition and the distant update",
    "D-tr": "odds are a function of the site's (conditional) state",
    "D-relax": "relaxation profile / which state records form from",
    "D-nn": "Admissibility conditions: records alone versus quantum states",
    "D-menu": "antipodal menus",
    "D-set": "independently formed setting records",
    "D-pattern": "record carving and contents",
    "D-sign": "sign of the Moriya coupling (handedness)",
    "D-roles": "doubled-coordinate roles (vertex, link, plaquette, cube sites)",
    "D-gauss": "a Gauss law on link sites, exact or as a soft vertex-star energy",
    "D-star": "a covariant generator on a plaquette site's four link neighbours",
    "D-loc": "at equal time, marginal record distributions do not depend on distant record formation",
    "D-rev": "reversible, continuous-time, time-homogeneous evolution with a nearest-neighbour generator",
    "D-chan": "the evolution of a finite region between records is a channel",
    "D-onlyrec": "records are the only irreversible events",
    "D-chir": "a time-reversal-odd star term (weight at most three, or up to seven in 9112)",
    "D-tsoft": "a soft vector-constraint energy on link sites with one-site slot fields",
    "D-slot": "the tensor slot type: rotor (unbounded) or qubit",
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
    9077: {"D-dyn", "D-roles", "D-gauss"},
    9081: {"D-roles", "D-gauss"},
    9083: {"D-dyn", "D-perm", "D-tr", "D-menu", "D-loc"},
    9084: {"D-dyn", "D-loc", "D-perm", "D-tr", "D-rev", "D-pc", "D-sold"},
    9085: {"D-dyn", "D-loc", "D-perm", "D-tr", "D-menu"},
    9086: {"D-chan", "D-onlyrec"},
    9088: {"D-pc", "D-sold", "D-chir", "D-pattern"},
    9095: {"D-roles", "D-tsoft", "D-slot"},
    9097: {"D-dyn", "D-sold", "D-perm", "D-pattern"},
    9112: {"D-dyn", "D-sold", "D-perm", "D-pattern", "D-chir"},
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
check("the covariant plaquette clause that annihilates uniform ice is the Rokhsar-Kivelson projector",
      nsr.shape[1] == 1 and np.allclose(cf, [1, 1, 0, 0, 0]),
      f"solution dimension {nsr.shape[1]}; coefficients (ring, flippable, opposite, adjacent, odd) {np.round(cf, 12).tolist()}")

# ------------------------------------------ 12: the tensor constraints
print("12. the landed tensor constraints")
E3i = np.eye(3, dtype=int)


def tkey(x, i, j):
    return (tuple(int(c) for c in x), (min(i, j), max(i, j)))


def trow(x, j):
    x = np.array(x)
    t_ = [(tkey(x + E3i[j], j, j), 1), (tkey(x, j, j), -1)]
    for i in range(3):
        if i != j:
            t_ += [(tkey(x, i, j), 1), (tkey(x - E3i[i], i, j), -1)]
    return t_


def tpos(k):
    x, (i, j) = k
    p_ = 2 * np.array(x)
    return p_ + (E3i[i] + E3i[j] if i != j else 0)


six_ok = all({tuple(tpos(k)) for k, _ in trow((0, 0, 0), j)} ==
             {tuple(E3i[j] + s_ * E3i[a]) for a in range(3) for s_ in (1, -1)} for j in range(3))


def star_nullity(center):
    center = np.array(center)
    near = {tuple(center)} | {tuple(center + s_ * E3i[a]) for a in range(3) for s_ in (1, -1)}
    sl = []
    for p_ in near:
        p_ = np.array(p_)
        odd = [a for a in range(3) if p_[a] % 2]
        if not odd:
            sl += [tkey(p_ // 2, j, j) for j in range(3)]
        elif len(odd) == 2:
            sl.append(tkey((p_ - E3i[odd[0]] - E3i[odd[1]]) // 2, odd[0], odd[1]))
    sid_ = {k: i for i, k in enumerate(sl)}
    rows_ = []
    for x in itertools.product(range(-3, 4), repeat=3):
        for j in range(3):
            v_ = np.zeros(len(sl))
            for k, c in trow(x, j):
                if k in sid_:
                    v_[sid_[k]] += c
            if v_.any():
                rows_.append(v_)
    A_ = np.array(rows_)
    return int(A_.shape[1] - np.linalg.matrix_rank(A_))


nul = [star_nullity(c_) for c_ in [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1)]]
check("tensor rows use exactly their link site's six neighbours; no single neighbourhood supports an integer move",
      six_ok and nul == [0, 0, 0, 0], f"six-neighbour placement {six_ok}; neighbourhood null dimensions (vertex, link, plaquette, cube) {nul}")

# ------------------------------------------------ 13: non-Abelian links
print("13. non-Abelian links")
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]])
Z2m = np.diag([1.0 + 0j, -1.0])
cm = _ns(np.vstack([np.kron(np.eye(2), g.T) - np.kron(g, np.eye(2)) for g in (X2, Y2, Z2m)])).shape[1]


def _su2():
    from scipy.linalg import expm as _e
    return _e(1j * sum(rng.normal() * g for g in (X2, Y2, Z2m)))


rows_ = []
for _ in range(3):
    OL_, OR_ = _su2(), _su2()
    V_ = np.block([[OL_, np.zeros((2, 2))], [np.zeros((2, 2)), OR_]])
    T1_ = np.einsum("ki,lj->ijkl", V_.conj(), V_)
    A_ = np.zeros((2, 2, 4, 4, 2, 2, 4, 4), dtype=complex)
    for a_ in range(2):
        for b_ in range(2):
            A_[a_, b_, :, :, a_, b_, :, :] += T1_
    A_ -= np.einsum("xz,yw,ik,jl->xyijzwkl", OL_, OR_.conj(), np.eye(4), np.eye(4))
    rows_.append(A_.reshape(64, 64))
G_ = np.vstack(rows_)
gw_ = np.linalg.eigvalsh(G_.conj().T @ G_)
nlink = int(np.sum(gw_ < 1e-9 * max(1.0, gw_.max())))
check("one qubit's SU(2) commutant is the scalars; the 4-dimensional SU(2) link carries a covariant link operator",
      cm == 1 and nlink >= 1, f"commutant dimension {cm}; covariant link operators on (2, 1) + (1, 2): {nlink}")

# ------------------------------------------ 14: the distant randomizer
print("14. a distant record is a recorded randomizer")
Pm = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]


def rho_r(r):
    return 0.5 * (np.eye(2) + sum(r[k] * Pm[k] for k in range(3)))


def bl(rho):
    return np.real(np.array([np.trace(rho @ P) for P in Pm]))


worst_steer, worst_tr, shift_cub = 0.0, 0.0, 0.0
for _ in range(100):
    r = rng.normal(size=3)
    r = r / np.linalg.norm(r) * rng.uniform(0.05, 0.95)
    d = rng.normal(size=3)
    d /= np.linalg.norm(d)
    bb = r @ d
    disc = np.sqrt(bb * bb - (r @ r - 1))
    t1, t2 = -bb + disc, -bb - disc
    n1, n2 = r + t1 * d, r + t2 * d
    pw = t2 / (t2 - t1)
    k1 = np.linalg.eigh(rho_r(n1))[1][:, 1]
    k2 = np.linalg.eigh(rho_r(n2))[1][:, 1]
    Psi = np.sqrt(pw) * np.kron(k1, [1, 0]) + np.sqrt(1 - pw) * np.kron(k2, [0, 1])
    v0 = Psi.reshape(2, 2)[:, 0]
    p0 = np.real(v0.conj() @ v0)
    worst_steer = max(worst_steer, abs(p0 - pw), np.linalg.norm(bl(np.outer(v0, v0.conj()) / p0) - n1))
    mm = rng.normal(size=3)
    mm /= np.linalg.norm(mm)
    tr = lambda x: 0.5 * (1 + x)
    cub = lambda x: 0.5 * (1 + x + 0.3 * (x ** 3 - x))
    worst_tr = max(worst_tr, abs(pw * tr(n1 @ mm) + (1 - pw) * tr(n2 @ mm) - tr(r @ mm)))
    shift_cub = max(shift_cub, abs(pw * cub(n1 @ mm) + (1 - pw) * cub(n2 @ mm) - cub(r @ mm)))
# replacement update (the lock alone): the site keeps its reduced state, so any normalized menu law passes D-loc
anti = lambda x: 0.5 * (1 - x)
rep_shift, rep_gap = 0.0, 0.0
for _ in range(100):
    v4 = rng.normal(size=4) + 1j * rng.normal(size=4)
    v4 /= np.linalg.norm(v4)
    M4 = v4.reshape(2, 2)
    rs_, rp_ = bl(M4 @ M4.conj().T), bl(M4.T @ M4.conj())
    nn_, mm = rng.normal(size=3), rng.normal(size=3)
    nn_, mm = nn_ / np.linalg.norm(nn_), mm / np.linalg.norm(mm)
    avg = sum(anti(sg * (rp_ @ nn_)) * anti(rs_ @ mm) for sg in (1, -1))
    rep_shift = max(rep_shift, abs(avg - anti(rs_ @ mm)))
    rep_gap = max(rep_gap, abs(anti(rs_ @ mm) - 0.5 * (1 + rs_ @ mm)))
check("a distant record steers every chord; the trace rule matches the steered average, a cubic deformation does not; the lock alone lets anti-Born pass",
      worst_steer < 1e-10 and worst_tr < 1e-12 and shift_cub > 1e-2 and rep_shift < 1e-12 and rep_gap > 0.3,
      f"steering deviation {worst_steer:.1e}; trace-rule discrepancy {worst_tr:.1e}; cubic shift {shift_cub:.3f}; "
      f"replacement update: anti-Born D-loc shift {rep_shift:.0e}, gap to the trace rule {rep_gap:.2f}")

# ------------------------------------------ 15: linear dynamics
print("15. locality of marginals forces linear dynamics")


def _rot(ax, ang):
    ax = ax / np.linalg.norm(ax)
    K_ = np.array([[0, -ax[2], ax[1]], [ax[2], 0, -ax[0]], [-ax[1], ax[0], 0]])
    return np.eye(3) + np.sin(ang) * K_ + (1 - np.cos(ang)) * K_ @ K_


nax = np.array([1.0, 2.0, 2.0]) / 3.0
prec = lambda r: _rot(nax, 1.5 * (r @ nax)) @ r
shift = 0.0
for _ in range(100):
    r = rng.normal(size=3)
    r = r / np.linalg.norm(r) * rng.uniform(0.1, 0.9)
    d = rng.normal(size=3)
    d /= np.linalg.norm(d)
    bb = r @ d
    disc = np.sqrt(bb * bb - (r @ r - 1))
    t1, t2 = -bb + disc, -bb - disc
    n1, n2 = r + t1 * d, r + t2 * d
    pw = t2 / (t2 - t1)
    mm = rng.normal(size=3)
    mm /= np.linalg.norm(mm)
    shift = max(shift, abs((pw * prec(n1) + (1 - pw) * prec(n2) - prec(r)) @ mm) / 2)
sing = np.array([0, 1, -1, 0], dtype=complex) / np.sqrt(2)
rs = np.outer(sing, sing.conj()).reshape(2, 2, 2, 2)
pt = np.zeros((4, 4), dtype=complex)
for i in range(2):
    for j in range(2):
        E_ = np.zeros((2, 2))
        E_[i, j] = 1
        pt += np.kron(E_.T, rs[i, :, j, :])
negev = np.linalg.eigvalsh(pt).min()
check("a Weinberg-type precession lets a distant record shift a later marginal; the transpose on half a singlet is negative",
      shift > 1e-2 and abs(negev + 0.5) < 1e-12, f"precession shift {shift:.3f}; transpose eigenvalue {negev:.3f}")

# ------------------------------------------ 16: the consistent distant update
print("16. compression is the distant update consistent with locality of marginals")
Pm_ = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]]), np.diag([1.0 + 0j, -1.0])]


def prj(n, sgn):
    return 0.5 * (np.eye(2) + sgn * sum(n[k] * Pm_[k] for k in range(3)))


a_ = np.array([0.3, -0.5, 0.8]); a_ /= np.linalg.norm(a_)
b_ = np.array([-0.6, 0.2, 0.7]); b_ /= np.linalg.norm(b_)
inter_ = int(np.sum(np.abs(np.linalg.eigvalsh(np.kron(prj(a_, 1), np.eye(2)) + np.kron(np.eye(2), prj(b_, 1))) - 2) < 1e-9))
dev_ = 0.0
for _ in range(50):
    G_ = rng.normal(size=(4, 3)) + 1j * rng.normal(size=(4, 3))
    rho_ = G_ @ G_.conj().T
    rho_ /= np.trace(rho_)
    P_ = prj(a_, 1)
    M_ = np.kron(P_, np.eye(2)) @ rho_ @ np.kron(P_, np.eye(2))
    lued = np.einsum("ijik->jk", M_.reshape(2, 2, 2, 2))
    lued /= np.trace(lued)
    pq_ = np.real(np.trace(np.kron(P_, np.eye(2)) @ rho_))
    tom = 0.5 * np.eye(2, dtype=complex)
    for k in range(3):
        pp = np.real(np.trace(np.kron(P_, prj(np.eye(3)[k], 1)) @ rho_)) / pq_
        tom = tom + 0.5 * (2 * pp - 1) * Pm_[k]
    dev_ = max(dev_, np.linalg.norm(tom - lued))
check("joint record effects with Born marginals are product projectors; the consistent partner state is the Lueders state",
      inter_ == 1 and dev_ < 1e-12, f"range intersection dimension {inter_}; tomography vs Lueders deviation {dev_:.1e}")

# ------------------------------------------ 17: records as the only irreversible events
print("17. records as the only irreversible events restate reversibility")
from scipy.linalg import expm as _expm2
H_ = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
U_ = _expm2(-1j * (H_ + H_.conj().T))
cc = rng.normal(size=3) + 1j * rng.normal(size=3)
cc /= np.linalg.norm(cc)
vv = rng.normal(size=3) + 1j * rng.normal(size=3)
vv /= np.linalg.norm(vv)
rr = np.outer(vv, vv.conj())
dev_u = np.linalg.norm(sum(abs(c_) ** 2 * U_ @ rr @ U_.conj().T for c_ in cc) - U_ @ rr @ U_.conj().T)
Gk = rng.normal(size=(6, 3)) + 1j * rng.normal(size=(6, 3))
Qk, _ = np.linalg.qr(Gk)
Ks = [Qk[:3, :], Qk[3:, :]]
low = min(np.real(np.trace(np.linalg.matrix_power(sum(K @ np.outer(w_, w_.conj()) @ K.conj().T for K in Ks), 2)))
          for w_ in [(lambda z: z / np.linalg.norm(z))(rng.normal(size=3) + 1j * rng.normal(size=3)) for _ in range(30)])
check("proportional Kraus operators give a unitary conjugation; a random non-unitary channel mixes some pure state",
      dev_u < 1e-12 and low < 0.99, f"proportional-Kraus deviation {dev_u:.1e}; lowest output purity {low:.3f}")

# ------------------------------------------ 18: time-reversal-odd star terms
print("18. time-reversal-odd star terms")
NBv = [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def _nid(v):
    return [k for k, u in enumerate(NBv) if np.array_equal(u, v)][0]


zero_all = True
for kind in ("perp", "collinear"):
    prs = [(i, k) for i in range(6) for k in range(6) if i != k and
           ((kind == "perp" and NBv[i] @ NBv[k] == 0) or (kind == "collinear" and NBv[i] @ NBv[k] == -1))]
    i0, k0 = prs[0]
    tot = {}
    for R in O:
        i2, k2 = _nid(R @ NBv[i0]), _nid(R @ NBv[k0])
        tot[(i2, k2)] = tot.get((i2, k2), 0) + 1
        tot[(k2, i2)] = tot.get((k2, i2), 0) - 1
    zero_all &= all(abs(v) < 1e-12 for v in tot.values())
# the orientation-weighted octant chirality: coefficient det[d1 d2 d3] on ordered octant triples
octs = [(d1, d2, d3) for d1 in NBv for d2 in NBv for d3 in NBv
        if abs(d1 @ d2) + abs(d2 @ d3) + abs(d1 @ d3) == 0]
oct_inv = all(abs(np.linalg.det(np.array([R @ d1, R @ d2, R @ d3])) - np.linalg.det(np.array([d1, d2, d3]))) < 1e-12
              for R in O for (d1, d2, d3) in octs)
# the tripod s^x_{m+x} s^y_{m+y} s^z_{m+z} = -i K_x K_y K_z on m and three neighbours; Majorana degree = odd-degree sites
_I = np.eye(2, dtype=complex)


def _op4(d):
    out = np.array([[1.0 + 0j]])
    for site in range(4):
        out = np.kron(out, d.get(site, _I))
    return out


trip = _op4({1: Pm[0], 2: Pm[1], 3: Pm[2]})
kkk = _op4({0: Pm[0], 1: Pm[0]}) @ _op4({0: Pm[1], 2: Pm[1]}) @ _op4({0: Pm[2], 3: Pm[2]})
_edges = [(0, 1), (0, 2), (0, 3)]                     # the three bonds of K_x K_y K_z
odd_sites = sum(sum(site in e for e in _edges) % 2 for site in range(4))
check("possibility covariance: star sums through the centre vanish, the octant chirality is invariant; the tripod is a quartic bond product",
      zero_all and oct_inv and len(octs) == 48 and np.linalg.norm(trip + 1j * kkk) < 1e-12 and odd_sites == 4,
      f"through-centre coefficients 0; det-weighted octant coefficients invariant on {len(octs)} ordered triples; "
      f"tripod = -i K_x K_y K_z residual {np.linalg.norm(trip + 1j * kkk):.0e}, odd-degree sites {odd_sites}")

# ------------------------------------------ 19: the tensor path sum
print("19. the tensor field's twelfth-order path sum")
from fractions import Fraction as _Fr
_E = np.eye(3, dtype=int)


def _row(x, j):
    x = np.array(x)
    t = [((tuple(x + _E[j]), (j, j)), 1), ((tuple(x), (j, j)), -1)]
    for i in range(3):
        if i != j:
            t += [((tuple(x), tuple(sorted((i, j)))), 1), ((tuple(x - _E[i]), tuple(sorted((i, j)))), -1)]
    return t


_piece = {((0, 1, 0), (0, 0)): 1, ((0, -1, 0), (0, 0)): 1, ((0, 0, 0), (0, 0)): -2,
          ((1, 0, 0), (1, 1)): 1, ((-1, 0, 0), (1, 1)): 1, ((0, 0, 0), (1, 1)): -2,
          ((0, 0, 0), (0, 1)): -1, ((-1, 0, 0), (0, 1)): 1, ((0, -1, 0), (0, 1)): 1, ((-1, -1, 0), (0, 1)): -1}
_sl = list(_piece)
_rows = []
for x in itertools.product(range(-2, 3), repeat=3):
    for j in range(3):
        r = [(_sl.index(k), c) for k, c in _row(x, j) if k in _piece]
        if r:
            _rows.append(r)
_Gt = np.zeros((len(_rows), len(_sl)), dtype=int)
for n_, r in enumerate(_rows):
    for a_, c_ in r:
        _Gt[n_, a_] += c_


def _psum(Gm, d):
    mags, sg = np.abs(d), np.sign(d)
    A_, zero_ = {}, 0
    for idx in sorted(itertools.product(*[range(m + 1) for m in mags]), key=sum):
        if not sum(idx):
            A_[idx] = _Fr(1)
            continue
        tot = sum((A_[tuple(v - (q == s_) for q, v in enumerate(idx))] for s_ in range(len(d)) if idx[s_]), _Fr(0))
        En = int(np.sum((Gm @ (sg * np.array(idx))) ** 2))
        if sum(idx) == mags.sum():
            A_[idx] = tot
        else:
            zero_ += En == 0
            A_[idx] = tot / En
    return A_[tuple(mags)], zero_


_d = np.array([_piece[k] for k in _sl])
A_t, z_t = _psum(_Gt, _d)
A_r, _ = _psum(np.array([[1, 0, 0, -1], [-1, 1, 0, 0], [0, -1, 1, 0], [0, 0, -1, 1]]), np.array([1, 1, 1, 1]))
check("the planar piece's twelfth-order path sum is 111150053/31850496; the U(1) ring's is 5/2",
      not np.any(_Gt @ _d) and z_t == 0 and A_t == _Fr(111150053, 31850496) and A_r == _Fr(5, 2),
      f"A = {A_t} (about {float(A_t):.4f}); ring {A_r}")

# ------------------------------------------ 20: sublattice symmetry of carved Majoranas
print("20. record fields keep the carved Majoranas sublattice-symmetric")
_n = 6                                   # a ring of sites along x; y and z axes dangling with record fields
_Am = np.zeros((3 * _n, 3 * _n))          # Majoranas: c_j (0..n-1), b^y_j (n..2n-1), b^z_j (2n..3n-1)
for j in range(_n):
    _Am[j, (j + 1) % _n] += -2.0 * rng.choice([1, -1])
    _Am[_n + j, j] += 2 * rng.normal()
    _Am[2 * _n + j, j] += 2 * rng.normal()
_Am = _Am - _Am.T
_S = np.diag([(-1) ** j for j in range(_n)] + [-(-1) ** j for j in range(_n)] * 2)
sub_viol = np.linalg.norm(_S @ (1j * _Am) @ _S + 1j * _Am)
_h = rng.normal(size=(2, 3))
_I = np.eye(2)
_Hs = np.kron(Pm[2], Pm[2]) + sum(_h[0][a] * np.kron(Pm[a], _I) + _h[1][a] * np.kron(_I, Pm[a]) for a in range(3))
_AL = np.zeros((6, 6))
_AL[0, 1] = -2.0
for j, (c_, bx, by) in enumerate(((0, 2, 3), (1, 4, 5))):
    _AL[bx, c_] += 2 * _h[j][0]
    _AL[by, c_] += 2 * _h[j][1]
    _AL[bx, by] += -2 * _h[j][2]
_AL = _AL - _AL.T
_eps = np.sort(np.linalg.eigvalsh(1j * _AL))[3:]
_lev = {0: [], 1: []}
for occ in itertools.product((0, 1), repeat=3):
    _lev[sum(occ) % 2].append(-0.5 * _eps.sum() + np.dot(occ, _eps))
_spin = np.sort(np.linalg.eigvalsh(_Hs))
leaf_dev = min(np.max(np.abs(np.sort(_lev[p_]) - _spin)) for p_ in (0, 1))
_SL = np.diag([1.0, -1.0, -1.0, -1.0, 1.0, 1.0])
leaf_break = np.linalg.norm(_SL @ (1j * _AL) @ _SL + 1j * _AL)
check("dangling-axis record fields keep S H S = -H; a leaf's kept-axis field is solvable and breaks it",
      sub_viol < 1e-12 and leaf_dev < 1e-12 and leaf_break > 1e-3,
      f"ring |S H S + H| {sub_viol:.0e}; leaf pair spectrum match {leaf_dev:.0e}, |S H S + H| {leaf_break:.2f}")

# ------------------------------------------ 21: covariant odd star terms and Kitaev's pattern
print("21. covariant odd star terms and the Majorana image of Kitaev's pattern")
_POS = [np.zeros(3, dtype=int)] + [np.array(v) for v in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]
_strs = [((0,), (a,)) for a in range(3)] + [(sup, labs) for sup in itertools.combinations(range(7), 3)
                                             for labs in itertools.product(range(3), repeat=3)]
_sid = {s_: i for i, s_ in enumerate(_strs)}
_pidx = {tuple(v): i for i, v in enumerate(_POS)}


def _image(R, s_):
    sup, labs = s_
    new = [_pidx[tuple(R @ _POS[x])] for x in sup]
    sign, lab2 = 1, []
    for a in labs:
        b = int(np.flatnonzero(R[:, a])[0])
        sign *= int(R[b, a])
        lab2.append(b)
    order = sorted(range(len(sup)), key=lambda t: new[t])
    return _sid[(tuple(new[t] for t in order), tuple(lab2[t] for t in order))], sign


_Rs = [np.round(R).astype(int) for R in O]
_seen, _count = set(), 0
for i0 in range(len(_strs)):
    if i0 in _seen:
        continue
    orb, front, ok = {i0: 1}, [i0], True
    while front:
        x = front.pop()
        for R in _Rs:
            y, sg = _image(R, _strs[x])
            if y in orb:
                ok &= orb[y] == orb[x] * sg
            else:
                orb[y] = orb[x] * sg
                front.append(y)
    _seen |= set(orb)
    _count += ok
# Kitaev's pattern s^x_i s^y_m s^z_k on i - m - k (bonds along x and z): its Majorana image is a c_i - c_k hopping.
# Spin model on three sites against free Majoranas c_i, c_m, c_k plus the five decoupled dangling b's.
_k = rng.normal()
_Hs = np.kron(np.kron(Pm[0], Pm[0]), np.eye(2)) + np.kron(np.eye(2), np.kron(Pm[2], Pm[2])) \
    + _k * np.kron(np.kron(Pm[0], Pm[1]), Pm[2])
_spin = np.sort(np.linalg.eigvalsh(_Hs))
_best = 9.0
for _sgn in (1, -1):
    _A = np.zeros((8, 8))                               # c_i, c_m, c_k, then five dangling b's (decoupled)
    _A[0, 1], _A[1, 2], _A[0, 2] = -2.0, -2.0, -2.0 * _sgn * _k
    _A = _A - _A.T
    _eps = np.sort(np.linalg.eigvalsh(1j * _A))[4:]
    _lev = {0: [], 1: []}
    for occ in itertools.product((0, 1), repeat=4):
        _lev[sum(occ) % 2].append(-0.5 * _eps.sum() + np.dot(occ, _eps))
    _best = min(_best, min(np.max(np.abs(np.sort(_lev[q_]) - _spin)) for q_ in (0, 1)))
check("covariant odd star terms number 37 at weights 1 and 3 under full soldering; Kitaev's pattern is a same-class c-c hopping",
      _count == 37 and _best < 1e-9,
      f"signed orbits {_count}; three-site spin levels reproduced by c_i - c_m - c_k hopping plus a c_i - c_k term to {_best:.0e}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
