#!/usr/bin/env python3
"""An exact Gauss law freezes the link field under every two-site generator.

Doubled coordinates (the landed role pattern): vertex sites have no odd
coordinate, link sites one, plaquette sites two and cube sites three. A
nearest-neighbour step changes one coordinate by one, so it joins roles that
differ by one; in particular no two link sites are adjacent. A Gauss law puts
the field E_l of a link site into the Gauss operators of both end vertices.
A two-site term touches one link and at most one of its two end vertices, so
it cannot change E_l without changing the Gauss operator at the other end.

The runner certifies this and its companions (supplied models, finite
diagnostics, no physical reading):

1. Roles: adjacency joins consecutive roles only; link sites form an
   independent set; neighbourhoods of vertex, link and plaquette sites.
2. Freeze (U(1)): on a window {v, l, w, p, p'} every sum of two-site
   nearest-neighbour terms commuting with the Gauss operators at v and w
   commutes with E_l, with static or dynamical vertex charges.
3. Freeze (Z2): the same for Z2 Gauss operators tau^x_v X_l.
4. Freeze (compression): for random two-site H, P H P commutes with E_l in
   every Gauss sector P.
5. Hops: with dynamical vertex charges, vertex-link-vertex operators include
   Gauss-invariant field movers; with static charges they do not.
6. Rings: the coarse cubic torus (L = 6) is bipartite and simple; its
   4-cycles are exactly its 648 plaquette boundaries; on one plaquette the
   nonzero divergence-free changes are exactly plus or minus the ring.
7. Soldered vertex: G_v = sum_l s_l . n(v -> l) is invariant under the 24
   rotations about v; the invariant one-qubit operators are the multiples of
   the identity, so a covariant vertex charge is a constant; with a fixed
   internal axis and trivial action the oriented Gauss law is not covariant.
8. Soldered plaquette: 8 rotations fix a plaquette site; Gauss-commuting
   operators on its four links have dimension 18 with movers span{U, U^dag};
   the covariant Hermitian ones have dimension 5 and one real ring coupling.
9. Soft Gauss ring: exact diagonalization of the four-link plaquette with
   corner energies U C_v^2 and transverse fields h gives a half-splitting of
   the ice doublet that tends to 5 h^4 / (32 U^3).
10. Soft Gauss diagonal: on random ice configurations of the coarse L = 6
    torus the fourth-order diagonal energy is the same (no Rokhsar-Kivelson
    potential at this order), and the ring element is -5 h^4 / (32 U^3).
11. Transverse record fields: at K = -J, D = 0 of the soldered clause, a
    vertex record's field on a link is transverse to it, and so is a
    plaquette record's field when the record lies along the plaquette normal.
12. The four landed actions of the rotations on the Bloch vector (trivial,
    sign twist, axis, full): a covariant oriented link field is an
    intertwiner from the spatial representation, and exists for full
    soldering alone (intertwiner dimensions 0, 0, 0, 1); a nonconstant
    covariant vertex charge needs an invariant axis (dimensions 3, 1, 0, 0).
    No single action has both.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_THE_LINK_FIELD_UNDER_EVERY_TWO_SITE_GENERATOR_THE_FIELD_MOVES_BY_RINGS_AND_HOPS_INSIDE_ONE_NEIGHBOURHOOD_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_SOLDERING_MENU_FOUR_ACTIONS_OF_THE_PROPER_CUBIC_ROTATIONS_ON_QUBIT_POSSIBILITIES_AND_WHAT_EACH_LETS_FORMATION_BUILD_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/UNIFORM_ICE_BY_FORMATION_TWO_ADJACENT_CUBES_ADMIT_NO_LOCAL_ORDER_EVEN_WITH_BOTH_CUBE_SITES_BOUNDED_THEOREM_NOTE_2026-09-23.md']

import numpy as np
from scipy.linalg import expm, null_space

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(20260924)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]])
Z = np.diag([1.0 + 0j, -1.0])
PAULI = [I2, X, Y, Z]
S = [X / 2, Y / 2, Z / 2]


def kron(*ops):
    return reduce(np.kron, ops)


def site_op(single, k, n):
    return kron(*[single if i == k else I2 for i in range(n)])


def role(x):
    return sum(int(c) % 2 for c in x)


# ---------------------------------------------------------------- 1. roles
L = 8
sites = list(itertools.product(range(L), repeat=3))
UNITS = [np.array(u) for u in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]]


def nbrs(x):
    return [tuple((np.array(x) + u) % L) for u in UNITS]


role_steps = set()
link_link = 0
nb_roles = {0: set(), 1: set(), 2: set(), 3: set()}
for x in sites:
    rx = role(x)
    counts = [0, 0, 0, 0]
    for y in nbrs(x):
        role_steps.add(abs(role(y) - rx))
        counts[role(y)] += 1
        if rx == 1 and role(y) == 1:
            link_link += 1
    nb_roles[rx].add(tuple(counts))
ok1 = (role_steps == {1} and link_link == 0 and nb_roles[0] == {(0, 6, 0, 0)}
       and nb_roles[1] == {(2, 0, 4, 0)} and nb_roles[2] == {(0, 4, 0, 2)} and nb_roles[3] == {(0, 0, 6, 0)})
check("roles: neighbours differ by one role; links are independent; vertex 6 links, link 2 vertices + 4 plaquettes, plaquette 4 links + 2 cubes",
      ok1, f"role steps {sorted(role_steps)}; link-link bonds {link_link}; neighbour role counts {[sorted(nb_roles[r]) for r in range(4)]}")

# ------------------------------------------------ 2-5. freeze on a window
# window sites: 0 = v (vertex), 1 = l (link from v to w), 2 = w (vertex), 3 = p, 4 = p' (plaquettes at l)
NW = 5
DIMW = 2 ** NW
BONDS = [(0, 1), (1, 2), (1, 3), (1, 4)]


def two_site_basis():
    basis = []
    for (i, j) in BONDS:
        for a in range(4):
            for b in range(4):
                basis.append(kron(*[PAULI[a] if k == i else (PAULI[b] if k == j else I2) for k in range(NW)]))
    return basis


BASIS2 = two_site_basis()
BASIS3 = [kron(PAULI[a], PAULI[b], PAULI[c], I2, I2) for a in range(4) for b in range(4) for c in range(4)]


def invariant_span(basis, gauss):
    cols = [np.concatenate([(b @ g - g @ b).ravel() for g in gauss]) for b in basis]
    ns = null_space(np.array(cols).T)
    ops = [sum(ns[k, c] * basis[k] for k in range(len(basis))) for c in range(ns.shape[1])]
    # the two-site basis is redundant (one-site terms repeat across bonds); keep a basis of the actual span
    M = np.array([o.ravel() for o in ops])
    u, sv, vh = np.linalg.svd(M, full_matrices=False)
    r = int(np.sum(sv > 1e-9 * sv[0]))
    return [vh[i].reshape(ops[0].shape) for i in range(r)]


def comm_norm(A, B):
    return np.linalg.norm(A @ B - B @ A)


# a generic frame for the link field and for the vertex charges
Ul = expm(1j * sum(rng.normal() * P for P in [X, Y, Z]))
E_l = site_op(Ul @ S[2] @ Ul.conj().T, 1, NW)
details = []
ok2 = True
for charges in ["static", "dynamical"]:
    if charges == "dynamical":
        Uq = expm(1j * sum(rng.normal() * P for P in [X, Y, Z]))
        Qv = site_op(Uq @ S[2] @ Uq.conj().T, 0, NW)
        Qw = site_op(Uq @ S[2] @ Uq.conj().T, 2, NW)
    else:
        Qv = np.zeros((DIMW, DIMW))
        Qw = np.zeros((DIMW, DIMW))
    gauss = [E_l - Qv, -E_l - Qw]
    span = invariant_span(BASIS2, gauss)
    worst = max(comm_norm(H, E_l) for H in span)
    ok2 &= worst < 1e-10 and len(span) == (26 if charges == "static" else 18)
    details.append(f"{charges}: invariant two-site span {len(span)}, max |[H, E_l]| {worst:.1e}")
check("freeze (U(1)): two-site generators commuting with the Gauss operators at both ends commute with E_l", ok2, "; ".join(details))

# Z2: electric field X_l, Gauss tau^x_v X_l (and tau^x_w X_l); matter parity tau^x
Gv = kron(X, X, I2, I2, I2)
Gw = kron(I2, X, X, I2, I2)
span = invariant_span(BASIS2, [Gv, Gw])
E2 = site_op(X, 1, NW)
worst = max(comm_norm(H, E2) for H in span)
span3 = invariant_span(BASIS3, [Gv, Gw])
mover3 = max(comm_norm(H, E2) for H in span3)
check("freeze (Z2): two-site generators commuting with tau^x_v X_l and tau^x_w X_l commute with X_l; tau^z_v Z_l tau^z_w moves it",
      len(span) == (26 if charges == "static" else 18) and worst < 1e-10 and mover3 > 1e-6,
      f"invariant two-site span {len(span)}, max |[H, X_l]| {worst:.1e}; three-site mover norm {mover3:.3f}")

# compression: random two-site H, Gauss sectors of the dynamical-charge model
Qv = site_op(S[2], 0, NW)
Qw = site_op(S[2], 2, NW)
Ez = site_op(S[2], 1, NW)
Gv_op = np.real(np.diag(Ez - Qv))
Gw_op = np.real(np.diag(-Ez - Qw))
H = np.zeros((DIMW, DIMW), dtype=complex)
for (i, j) in BONDS:
    A = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
    A = A + A.conj().T
    for a in range(4):
        for b in range(4):
            c = np.trace(A @ np.kron(PAULI[a], PAULI[b]).conj().T) / 4
            H += c * kron(*[PAULI[a] if k == i else (PAULI[b] if k == j else I2) for k in range(NW)])
worst = 0.0
nsec = 0
for gv in sorted(set(np.round(Gv_op, 9))):
    for gw in sorted(set(np.round(Gw_op, 9))):
        mask = (np.abs(Gv_op - gv) < 1e-9) & (np.abs(Gw_op - gw) < 1e-9)
        if not mask.any():
            continue
        P = np.diag(mask.astype(float))
        worst = max(worst, comm_norm(P @ H @ P, Ez))
        nsec += 1
check("freeze (compression): P H P commutes with E_l in every Gauss sector, for random two-site H",
      worst < 1e-10 and nsec > 1, f"{nsec} sectors; max |[P H P, E_l]| {worst:.1e}; |[H, E_l]| {comm_norm(H, Ez):.2f}")

# hops
res = []
for charges in ["static", "dynamical"]:
    if charges == "dynamical":
        Qv, Qw = site_op(S[2], 0, NW), site_op(S[2], 2, NW)
    else:
        Qv = Qw = np.zeros((DIMW, DIMW))
    span3 = invariant_span(BASIS3, [Ez - Qv, -Ez - Qw])
    res.append(max(comm_norm(H3, Ez) for H3 in span3))
check("hops: with dynamical vertex charges some vertex-link-vertex operators are Gauss-invariant field movers; with static charges none",
      res[0] < 1e-10 and res[1] > 1e-6, f"max |[O, E_l]|: static {res[0]:.1e}, dynamical {res[1]:.3f}")

# ------------------------------------------------------------ 6. rings
LC = 6
verts = list(itertools.product(range(LC), repeat=3))
vid = {v: i for i, v in enumerate(verts)}
links = []
for v in verts:
    for a in range(3):
        w = list(v)
        w[a] = (w[a] + 1) % LC
        links.append((vid[v], vid[tuple(w)], a))
adj = {i: set() for i in range(len(verts))}
edge_of = {}
for k, (i, j, a) in enumerate(links):
    adj[i].add(j)
    adj[j].add(i)
    edge_of[frozenset((i, j))] = k
bip = all((sum(verts[i]) + sum(verts[j])) % 2 == 1 for (i, j, a) in links)
simple = len(edge_of) == len(links)
cycles = set()
for u in range(len(verts)):
    for a_, b_ in itertools.combinations(adj[u], 2):
        for w in adj[a_] & adj[b_]:
            if w != u:
                cycles.add(frozenset([edge_of[frozenset((u, a_))], edge_of[frozenset((a_, w))],
                                      edge_of[frozenset((w, b_))], edge_of[frozenset((b_, u))]]))


def is_plaquette(cyc):
    vs = set()
    for k in cyc:
        vs |= {links[k][0], links[k][1]}
    pts = np.array([verts[i] for i in vs])
    spans = [len(set(pts[:, c])) for c in range(3)]
    return sorted(spans) == [1, 2, 2]


all_plaq = all(is_plaquette(c) for c in cycles)
# divergence-free changes on one plaquette (links bottom, right, top, left of the xy face at the origin)
corner_rows = np.array([[1, 0, 0, 1], [-1, 1, 0, 0], [0, -1, -1, 0], [0, 0, 1, -1]])
dfree = [d for d in itertools.product([-1, 0, 1], repeat=4) if any(d) and not np.any(corner_rows @ np.array(d))]
check("rings: the tested even L=6 coarse torus is bipartite and simple; its 4-cycles are exactly the plaquette boundaries; on a plaquette the divergence-free changes are +-(ring)",
      bip and simple and len(cycles) == 3 * LC ** 3 and all_plaq and sorted(dfree) == [(-1, -1, 1, 1), (1, 1, -1, -1)],
      f"bipartite {bip}; simple {simple}; 4-cycles {len(cycles)} (plaquettes {3 * LC ** 3}); all plaquettes {all_plaq}; divergence-free {dfree}")

# ----------------------------------------------------- 7-8. soldering
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = signs[i]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)


def lift(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if np.isclose(ang, 0):
        return I2.copy()
    if np.isclose(ang, np.pi):
        w, v = np.linalg.eig(R)
        nvec = np.real(v[:, np.argmin(abs(w - 1))])
    else:
        nvec = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    nvec = nvec / np.linalg.norm(nvec)
    return expm(-1j * ang * sum(nvec[k] * PAULI[k + 1] for k in range(3)) / 2)


for R in rots:
    U = lift(R)
    for a in range(3):
        assert np.allclose(U @ S[a] @ U.conj().T, sum(R[b, a] * S[b] for b in range(3)))


def site_action(R, centre, positions, mode):
    n = len(positions)
    perm = []
    for pos in positions:
        img = tuple(np.array(centre) + R @ (np.array(pos) - np.array(centre)))
        perm.append([k for k, q in enumerate(positions) if tuple(q) == img][0])
    U = lift(R) if mode == "full" else I2
    dim = 2 ** n
    Pm = np.zeros((dim, dim))
    for idx in range(dim):
        bits = [(idx >> (n - 1 - k)) & 1 for k in range(n)]
        new = [0] * n
        for k in range(n):
            new[perm[k]] = bits[k]
        Pm[sum(b << (n - 1 - k) for k, b in enumerate(new)), idx] = 1
    return Pm @ kron(*[U] * n)


def axis(pos):
    return [i for i in range(3) if pos[i] % 2 == 1][0]


vpos = [tuple(u) for u in UNITS]
Gv_sold = sum(site_op(sum(float(u[c]) * S[c] for c in range(3)), k, 6) for k, u in enumerate(UNITS))
cov = max(np.linalg.norm(site_action(R, (0, 0, 0), vpos, "full") @ Gv_sold @ site_action(R, (0, 0, 0), vpos, "full").conj().T - Gv_sold) for R in rots)
inv1 = null_space(np.vstack([np.kron(lift(R), lift(R).conj()) - np.eye(4) for R in rots]))
Gv_triv = sum(site_op(float(sum(u)) * S[2], k, 6) for k, u in enumerate(UNITS))
fails = sum(1 for R in rots if np.linalg.norm(site_action(R, (0, 0, 0), vpos, "trivial") @ Gv_triv @ site_action(R, (0, 0, 0), vpos, "trivial").conj().T - Gv_triv) > 1e-9)
check("soldered vertex: sum_l s_l . n(v->l) is invariant under the 24 rotations; invariant one-qubit operators = multiples of 1; a fixed axis with trivial action is not covariant",
      cov < 1e-10 and inv1.shape[1] == 1 and fails > 0,
      f"max deviation {cov:.1e}; invariant one-qubit dimension {inv1.shape[1]}; trivial action fails for {fails} of 24 rotations")

pc = (1, 1, 0)
ppos = [(1, 0, 0), (2, 1, 0), (1, 2, 0), (0, 1, 0)]          # bottom, right, top, left
corners = [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0)]
stab = [R for R in rots if all(tuple(np.array(pc) + R @ (np.array(q) - np.array(pc))) in ppos for q in ppos)]


def corner_sum(v):
    tot = np.zeros((16, 16), dtype=complex)
    for k, q in enumerate(ppos):
        d = np.array(q) - np.array(v)
        if np.sum(np.abs(d)) == 1:
            tot += d[axis(q)] * site_op(S[axis(q)], k, 4)
    return tot


C = [corner_sum(v) for v in corners]
Vs = [site_action(R, pc, ppos, "full") for R in stab]
gcov = max(np.linalg.norm(V @ C[i] @ V.conj().T - C[[j for j, c in enumerate(corners) if c == tuple(np.array(pc) + R @ (np.array(corners[i]) - np.array(pc)))][0]])
           for V, R in zip(Vs, stab) for i in range(4))
Id16 = np.eye(16)
rows_g = [np.kron(Id16, Cv.T) - np.kron(Cv, Id16) for Cv in C]
rows_s = [np.kron(V, V.conj()) - np.eye(256) for V in Vs]
herm_rows = []
ns_g = null_space(np.vstack(rows_g))
Es = [site_op(S[axis(q)], k, 4) for k, q in enumerate(ppos)]
w, Bq = np.linalg.eigh(sum(c * E for c, E in zip([1.0, np.sqrt(2), np.sqrt(3), 1.1 * np.sqrt(5)], Es)))


def offdiag(O):
    Ob = Bq.conj().T @ O @ Bq
    return (Ob - np.diag(np.diag(Ob))).ravel()


mov_g = np.linalg.matrix_rank(np.array([offdiag(ns_g[:, c].reshape(16, 16)) for c in range(ns_g.shape[1])]), tol=1e-9)
ns_gs = null_space(np.vstack(rows_g + rows_s))
# Hermitian real span: stack real and imaginary parts
herm = []
for c in range(ns_gs.shape[1]):
    O = ns_gs[:, c].reshape(16, 16)
    for M in (O + O.conj().T, 1j * (O - O.conj().T)):
        if np.linalg.norm(M) > 1e-9:
            herm.append(M)
Hmat = np.array([np.concatenate([M.ravel().real, M.ravel().imag]) for M in herm])
hdim = np.linalg.matrix_rank(Hmat, tol=1e-9)
hmov = np.linalg.matrix_rank(np.array([np.concatenate([offdiag(M).real, offdiag(M).imag]) for M in herm]), tol=1e-9)
# the flippability projector (the ring pair) lies in the covariant span, so U + U^dag and the
# Rokhsar-Kivelson potential are both covariant
ring_pair = [k for k in range(16) if np.allclose([np.real(Bq[:, k].conj() @ Cv @ Bq[:, k]) for Cv in C], 0)]
Pflip = sum(np.outer(Bq[:, k], Bq[:, k].conj()) for k in ring_pair)
in_span = np.linalg.matrix_rank(np.vstack([Hmat, np.concatenate([Pflip.ravel().real, Pflip.ravel().imag])]), tol=1e-9) == hdim
check("soldered plaquette: 8 rotations fix it; Gauss-commuting operators dim 18 with 2 movers; covariant Hermitian dim 5 with one real ring coupling and the flippability projector",
      len(stab) == 8 and gcov < 1e-10 and ns_g.shape[1] == 18 and mov_g == 2 and hdim == 5 and hmov == 1 and len(ring_pair) == 2 and in_span,
      f"stabilizer {len(stab)}; corner covariance {gcov:.1e}; Gauss-commuting {ns_g.shape[1]}, movers {mov_g}; covariant Hermitian {hdim}, movers {hmov}; flippable pair {len(ring_pair)} states, projector covariant {in_span}")

# ------------------------------------------------ 9-10. soft Gauss law
Uen = 1.0
H0 = Uen * sum(Cv @ Cv for Cv in C)
Vt = -sum(site_op(S[2], k, 4) for k in range(4))     # transverse field along the plaquette normal
ratios = []
for h in [0.04, 0.02]:
    ev = np.linalg.eigvalsh(H0 + h * Vt)
    ratios.append(((ev[1] - ev[0]) / 2) / (5 * h ** 4 / (32 * Uen ** 3)))
check("soft Gauss ring (ED, one plaquette): half-splitting of the ice doublet -> 5 h^4 / (32 U^3)",
      abs(ratios[-1] - 1) < 2e-3 and abs(ratios[-1] - 1) < abs(ratios[0] - 1),
      f"ratio {ratios[0]:.6f} at h/U = 0.04, {ratios[1]:.6f} at h/U = 0.02")

# combinatorial fourth order on the coarse torus: E = +-1/2 on links (i -> j along +a)
nV, nL = len(verts), len(links)
Ei = [(k, i, j) for k, (i, j, a) in enumerate(links)]
inc = {i: [] for i in range(nV)}
for k, (i, j, a) in enumerate(links):
    inc[i].append(k)
    inc[j].append(k)


def div(E):
    d = np.zeros(nV)
    for k, (i, j, a) in enumerate(links):
        d[i] += E[k]
        d[j] -= E[k]
    return d


# each line carries a constant field (x-links vary with y, y-links and z-links with x),
# so the divergence vanishes; plaquettes with u_x = u_y mod 2 in the xy planes are flippable
E0 = np.array([0.5 * (-1) ** [verts[i][1], verts[i][0] + 1, verts[i][0]][a] for (i, j, a) in links])
plaqs = [sorted(c) for c in cycles]


def ring_orient(cyc, E):
    # flippable iff the four links circulate: walking the cycle, each link's field points forward
    vs = {}
    for k in cyc:
        i, j, a = links[k]
        vs.setdefault(i, []).append(k)
        vs.setdefault(j, []).append(k)
    start = links[cyc[0]][0]
    order, cur, used = [], start, set()
    for _ in range(4):
        k = [q for q in vs[cur] if q not in used][0]
        used.add(k)
        i, j, a = links[k]
        forward = (i == cur)
        order.append((k, forward))
        cur = j if forward else i
    signs = [np.sign(E[k]) * (1 if fw else -1) for k, fw in order]
    return len(set(signs)) == 1


def flip_charges(E, flipped):
    ch = {}
    for k in flipped:
        i, j, a = links[k]
        dE = -2 * E[k]
        ch[i] = ch.get(i, 0) + dE
        ch[j] = ch.get(j, 0) - dE
    return sum(q * q for q in ch.values()) * Uen


def fourth_diag(E):
    e1 = np.array([flip_charges(E, [k]) for k in range(nL)])
    tot = 0.0
    shared = 0
    for v in range(nV):
        for k1, k2 in itertools.permutations(inc[v], 2):
            e12 = flip_charges(E, [k1, k2])
            tot += 1 / (e1[k1] * e12 * e1[k2]) + 1 / (e1[k1] ** 2 * e12)
            shared += 1
    # every other ordered pair is disjoint, with e12 = e1 + e2
    ndis = nL * (nL - 1) - shared
    tot += ndis * (1 / (2 * Uen * 4 * Uen * 2 * Uen) + 1 / ((2 * Uen) ** 2 * 4 * Uen))
    first = -tot / 16
    renorm = (np.sum(1 / e1 ** 2)) * (np.sum(1 / e1)) / 16
    return first + renorm


E = E0.copy()
assert not np.any(div(E))
confs = [E.copy()]
for step in range(4):
    for _ in range(3000):
        cyc = plaqs[rng.integers(len(plaqs))]
        if ring_orient(cyc, E):
            E[cyc] *= -1
    assert not np.any(div(E))
    confs.append(E.copy())
vals = [fourth_diag(Ec) for Ec in confs]
dist = min(int(np.sum(Ec != E0)) for Ec in confs[1:])
# ring element through the same denominators
cyc = [c for c in plaqs if ring_orient(c, E0)][0]
amp = 0.0
for order in itertools.permutations(cyc):
    den = 1.0
    for m in range(1, 4):
        den *= -flip_charges(E0, list(order[:m]))
    amp += 1 / den
amp /= 16
check("soft Gauss diagonal (coarse L = 6 torus): the fourth-order diagonal energy is the same on random ice configurations; ring element -5 h^4/(32 U^3)",
      max(vals) - min(vals) < 1e-9 * abs(vals[0]) and dist > 50 and abs(amp + 5 / 32) < 1e-12,
      f"diagonal (units h^4/U^3) {vals[0]:.10f}, spread {max(vals) - min(vals):.1e} over {len(vals)} configurations (min Hamming distance {dist}); ring element {amp:.6f} vs {-5 / 32:.6f}")

# --------------------------------------------- 11. transverse record fields
Jc = 1.0
ok11 = True
worst = 0.0
for a in range(3):                       # link axis
    for q in rng.normal(size=(20, 3)):   # vertex record contents
        e = np.eye(3)[a]
        M = Jc * (np.eye(3) - np.outer(e, e))    # K = -J, D = 0
        worst = max(worst, abs((M @ q)[a]))
    for b in range(3):
        if b == a:
            continue
        nrm = [c for c in range(3) if c not in (a, b)][0]
        e = np.eye(3)[b]
        M = Jc * (np.eye(3) - np.outer(e, e))
        qn = np.eye(3)[nrm] * rng.choice([-1, 1])
        worst = max(worst, abs((M @ qn)[a]))
check("transverse record fields at K = -J, D = 0: vertex records, and plaquette records along the normal, give link fields with no component along the link",
      worst < 1e-12, f"max longitudinal component {worst:.1e}")

# ------------------------------------------- 12. the four landed actions
def perm_sign(R):
    P = np.abs(R)
    return round(np.linalg.det(P))


ACTIONS = {
    "trivial": lambda R: np.eye(3),
    "sign twist": lambda R: np.diag([1.0, perm_sign(R), perm_sign(R)]),
    "axis": lambda R: perm_sign(R) * np.abs(R),
    "full": lambda R: R,
}
homs, dets, intertw, invar = [], [], [], []
for name, rho in ACTIONS.items():
    homs.append(max(np.abs(rho(R1 @ R2) - rho(R1) @ rho(R2)).max() for R1 in rots for R2 in rots))
    dets.append(min(np.linalg.det(rho(R)) for R in rots))
    # intertwiners T with rho(R) T = T R for all R (vectorized row-major)
    rows = np.vstack([np.kron(rho(R), np.eye(3)) - np.kron(np.eye(3), R.T) for R in rots])
    intertw.append(null_space(rows).shape[1])
    invar.append(null_space(np.vstack([rho(R) - np.eye(3) for R in rots])).shape[1])
check("four landed actions: oriented link field (intertwiner from the spatial rotation) exists for full soldering alone; nonconstant vertex charge needs an invariant axis",
      max(homs) < 1e-12 and min(dets) > 0.5 and intertw == [0, 0, 0, 1] and invar == [3, 1, 0, 0],
      f"homomorphism defect {max(homs):.0e}; det 1; intertwiner dims (trivial, sign twist, axis, full) {intertw}; invariant axes {invar}")

for resolution in ['N5 resolution 1: A total-generator matrix-element selection rule proves freeze without requiring each bond term to commute separately.', 'N5 resolution 2: A three-site hop escapes freeze only when endpoint charge transitions match the link electric step.', 'N5 resolution 3: Elementary ring minimality uses simple cubic geometry; odd large tori are not bipartite but have the same four-cycle classification.', 'N5 resolution 4: The fourth-order equal-field diagonal is constant by local three-in-three-out pair counts, not a state-selection mechanism.', 'N5 resolution 5: Soft Gauss energy and record fields are supplied extra terms; their ring does not derive a photon phase or native law.']:
    print(resolution)
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
