#!/usr/bin/env python3
"""Conditional isolated formation: graph structure and factorized-preparation controls.

Supplied and not adopted: the covariant nearest-neighbour two-qubit dynamics
clause of the supplied companion construction, record permanence as compression onto record projectors
and odds read by the trace rule (the supplied companion construction). "Records-only admissibility"
means: the odds of every forming record are fixed by the records at its six
neighbours, whatever the state of the unrecorded sites.

Checks:

A. State-insensitive closure fails for suitable product preparations. With a nonzero coupling, a site forming while one
   neighbour is unrecorded has odds that depend on that neighbour's state:
   two product states of the neighbour, with every record the same, give
   different odds after a short evolution (Heisenberg and random J, K, D), and
   the exact first derivative of the site's Bloch vector contains the term
   M <s_y> x ... that carries the dependence.
B. The formation structure. On the cube graph Q3 (every assignment of its 8
   sites to initial records R0, forming sites F and never-recorded sites N,
   every order of F), an order in which every forming site is isolated when it
   forms exists exactly when F is independent and every neighbour of F lies in
   R0. On the 4x4x4 torus the largest such F has 32 sites (a sublattice, with
   R0 the other sublattice).
C. Decoupling. On a 2x2x3 window with the forming sites independent and every
   neighbour of them recorded, the record-projected generator is a sum of
   single-site fields on the forming sites plus terms on never-recorded sites:
   no forming site couples to any other unrecorded site.
D. For a supplied product stationary preparation, The joint odds of the forming
   records are the product of their isolated-site laws; they are the same for
   every formation order and for every state and evolution of the
   never-recorded sites within that product preparation.
E. The other branch. Two adjacent unrecorded sites under the antiferromagnetic
   Heisenberg coupling have the singlet as ground state; their odds are
   correlated (E = -a.b), in this supplied model.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import itertools
import sys
from functools import reduce

AUDIT_INPUT_PATHS = ('docs/DYNAMICS_CLAUSE_RECORDS_ONLY_ADMISSIBILITY_LEAVES_THE_DYNAMICS_UNREADABLE_FORMING_SITES_MUST_BE_ISOLATED_AND_NEVER_INTERACT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
AUDIT_TIMEOUT_SEC = 300

import numpy as np
import scipy.sparse as sps

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))


rng = np.random.default_rng(92404)
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
    return np.array([[0, f[2], -f[1]], [-f[2], 0, f[0]], [f[1], -f[0], 0]], dtype=float)


def coupling(J, K, D, f):
    return J * np.eye(3) + K * np.outer(f, f) + D * cross_mat(f)


def op(n, placed):
    return reduce(np.kron, [placed.get(k, I2) for k in range(n)])


def bloch(rho):
    return np.array([np.real(np.trace(rho @ S[a])) for a in range(3)])


# ------------------------------------------------------ A: isolation needed
print("A. a site forming beside an unrecorded neighbour")
worst_gap, deriv_ok, cases = 1.0, True, 0
for family in ("heisenberg", "full"):
    for _ in range(10):
        J, K, D = (rng.normal(), 0.0, 0.0) if family == "heisenberg" else tuple(rng.normal(size=3))
        f = DIRS[0]                                   # y = x + e_x
        M = coupling(J, K, D, f)
        hx = sum(coupling(J, K, D, g) @ rand_unit() for g in DIRS[1:])   # x's five recorded neighbours
        hy = sum(coupling(J, K, D, g) @ rand_unit() for g in DIRS if not np.allclose(g, -f))  # y's five
        H = sum(M[i, j] * np.kron(S[i], S[j]) for i in range(3) for j in range(3)) \
            + np.kron(sdot(hx), I2) + np.kron(I2, sdot(hy))
        rx = unit(rng.normal(size=3)) * 0.8
        ry1, ry2 = unit(rng.normal(size=3)), unit(rng.normal(size=3))
        rho1 = np.kron(0.5 * (I2 + sdot(rx)), 0.5 * (I2 + sdot(ry1)))
        rho2 = np.kron(0.5 * (I2 + sdot(rx)), 0.5 * (I2 + sdot(ry2)))
        ev, V = np.linalg.eigh(H)
        t = 0.3
        U = V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
        bx = []
        for rho in (rho1, rho2):
            r = U @ rho @ U.conj().T
            bx.append(bloch(r.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3)))
        gap = np.linalg.norm(bx[0] - bx[1])
        worst_gap = min(worst_gap, gap)
        # exact first derivative: d r_x/dt = 2 (h_x + M r_y) x r_x
        for ry in (ry1, ry2):
            rho = np.kron(0.5 * (I2 + sdot(rx)), 0.5 * (I2 + sdot(ry)))
            drho = -1j * (H @ rho - rho @ H)
            d_num = bloch(drho.reshape(2, 2, 2, 2).trace(axis1=1, axis2=3))
            d_exact = 2 * np.cross(hx + M @ ry, rx)
            deriv_ok &= np.abs(d_num - d_exact).max() < 1e-12
        cases += 1
check("two states of the unrecorded neighbour, same records, give different site states",
      worst_gap > 1e-3, f"{cases} random cases; smallest Bloch-vector gap at t = 0.3: {worst_gap:.3f}")
check("exact first derivative d r_x/dt = 2 (h_x + M r_y) x r_x carries the dependence on r_y", deriv_ok,
      "Heisenberg and random J, K, D")

# ------------------------------------------------ B: the formation structure
print("B. which forming sets admit an isolated order")
Q3 = list(itertools.product((0, 1), repeat=3))
nbr = {v: [w for w in Q3 if sum(abs(a - b) for a, b in zip(v, w)) == 1] for v in Q3}
agree, total = 0, 0
for labels in itertools.product("RFN", repeat=8):
    lab = dict(zip(Q3, labels))
    F = [v for v in Q3 if lab[v] == "F"]
    R0 = {v for v in Q3 if lab[v] == "R"}
    # exists an order: each forming site has every neighbour recorded (initial or earlier-formed)
    exists = False
    for order in itertools.permutations(F):
        rec = set(R0)
        ok = True
        for v in order:
            if not all(w in rec for w in nbr[v]):
                ok = False
                break
            rec.add(v)
        if ok:
            exists = True
            break
    indep = all(w not in F for v in F for w in nbr[v])
    covered = all(w in R0 for v in F for w in nbr[v])
    agree += exists == (indep and covered)
    total += 1
check("on Q3 an isolated order exists exactly when F is independent and N(F) is inside R0",
      agree == total, f"{total} assignments of 8 sites to R0/F/N, all orders of F")
# largest forming set on the 4x4x4 torus
L = 4
sites = list(itertools.product(range(L), repeat=3))
even = [s for s in sites if sum(s) % 2 == 0]
odd = [s for s in sites if sum(s) % 2 == 1]


def torus_nbrs(s):
    for ax in range(3):
        for d in (1, -1):
            t = list(s)
            t[ax] = (t[ax] + d) % L
            yield tuple(t)


odd_set = set(odd)
even_ok = all(all(w in odd_set for w in torus_nbrs(s)) for s in even)
# a perfect matching of the torus graph bounds any independent set by 32 (Konig)
matching = [(s, tuple([(s[0] + 1) % L, s[1], s[2]])) for s in sites if s[0] % 2 == 0]
match_ok = len(matching) == 32 and len({v for e in matching for v in e}) == 64
check("4x4x4 torus: a sublattice forms with the other as initial records; no forming set exceeds 32",
      even_ok and match_ok, "even sites have all neighbours odd; a perfect matching of 32 bonds bounds independence")

# ----------------------------------------------------------- C: decoupling
print("C. the record-projected generator on a 2x2x3 window")
W = list(itertools.product(range(2), range(2), range(3)))
widx = {s: i for i, s in enumerate(W)}
n = len(W)
J, K, D = rng.normal(size=3)
bonds = []
for s in W:
    for ax in range(3):
        t = list(s)
        t[ax] += 1
        t = tuple(t)
        if t in widx:
            f = np.zeros(3)
            f[ax] = 1
            bonds.append((s, t, f))
F = [(0, 0, 0), (1, 1, 0)]                  # forming sites: independent
Nset = [(0, 1, 2), (1, 1, 2)]               # never recorded: an adjacent pair, away from F
R0 = [s for s in W if s not in F and s not in Nset]
nbw = lambda s: [w for w in W if np.sum(np.abs(np.array(s) - np.array(w))) == 1]
struct_ok = all(w in R0 for x in F for w in nbw(x)) and not any(w in F for x in Nset for w in nbw(x))
SS = [sps.csr_matrix(m) for m in S]
I2s = sps.identity(2, dtype=complex, format="csr")


def sop(placed):
    out = sps.identity(1, dtype=complex, format="csr")
    for k in range(n):
        out = sps.kron(out, placed.get(k, I2s), format="csr")
    return out


H = sps.csr_matrix((2 ** n, 2 ** n), dtype=complex)
for (a, b, f) in bonds:
    M = coupling(J, K, D, f)
    for i in range(3):
        for j in range(3):
            H = H + M[i, j] * sop({widx[a]: SS[i], widx[b]: SS[j]})
contents = {s: rand_unit() for s in R0}
P = sop({widx[s]: sps.csr_matrix(proj(q)) for s, q in contents.items()})
C = P @ H @ P
expect = sps.csr_matrix((2 ** n, 2 ** n), dtype=complex)
const = 0.0
for (a, b, f) in bonds:
    M = coupling(J, K, D, f)
    if a in contents and b in contents:
        const += contents[a] @ M @ contents[b]
    elif a in contents:
        expect = expect + sop({widx[b]: sps.csr_matrix(sdot(M.T @ contents[a]))})
    elif b in contents:
        expect = expect + sop({widx[a]: sps.csr_matrix(sdot(M @ contents[b]))})
    else:
        for i in range(3):
            for j in range(3):
                expect = expect + M[i, j] * sop({widx[a]: SS[i], widx[b]: SS[j]})
expect = (expect + const * sps.identity(2 ** n, dtype=complex, format="csr")) @ P
diff = (C - expect).tocoo()
dev = float(np.abs(diff.data).max()) if diff.nnz else 0.0
two_site_on_F = any((a in F or b in F) and a not in contents and b not in contents for (a, b, f) in bonds)
check("P H P = fields on each forming site + terms on never-recorded sites; nothing couples F",
      struct_ok and dev < 1e-12 and not two_site_on_F, f"12 qubits (sparse); max deviation {dev:.1e}")

# ------------------------------------------- D: nothing readable depends on it
print("D. the forming records' joint odds")
# Build the unrecorded part: F sites evolve in their fields; N pair evolves with its own coupling.
hF = {}
for x in F:
    h = np.zeros(3)
    for (a, b, f) in bonds:
        M = coupling(J, K, D, f)
        if a == x and b in contents:
            h += M @ contents[b]
        if b == x and a in contents:
            h += M.T @ contents[a]
    hF[x] = h
lam = {x: rng.uniform(-1, 1) for x in F}
menus = {x: rand_unit() for x in F}
law = {x: (lambda s, x=x: 0.5 * (1 + s * lam[x] * menus[x] @ unit(hF[x]))) for x in F}
# full model: stationary F states (1 + lam h^.s)/2, arbitrary N state, joint evolution, then record F in either order
rhoF = [0.5 * (I2 + lam[x] * sdot(unit(hF[x]))) for x in F]
worst = 0.0
for trial in range(4):
    psiN = rng.normal(size=4) + 1j * rng.normal(size=4)
    psiN /= np.linalg.norm(psiN)
    rhoN = np.outer(psiN, psiN.conj())
    rho = np.kron(np.kron(rhoF[0], rhoF[1]), rhoN)
    # generator on (F0, F1, N0, N1): fields on F, coupling + fields on N
    Mn = coupling(J, K, D, np.array([1.0, 0, 0]))
    hN = [rng.normal(size=3), rng.normal(size=3)]
    Hu = op(4, {0: sdot(hF[F[0]])}) + op(4, {1: sdot(hF[F[1]])}) \
        + sum(Mn[i, j] * op(4, {2: S[i], 3: S[j]}) for i in range(3) for j in range(3)) \
        + op(4, {2: sdot(hN[0])}) + op(4, {3: sdot(hN[1])})
    ev, V = np.linalg.eigh(Hu)
    for t in (0.0, 0.7, 2.9):
        U = V @ np.diag(np.exp(-1j * ev * t)) @ V.conj().T
        rt = U @ rho @ U.conj().T
        for s0 in (1, -1):
            for s1 in (1, -1):
                Pj = op(4, {0: proj(s0 * menus[F[0]]), 1: proj(s1 * menus[F[1]])})
                joint = np.real(np.trace(Pj @ rt))
                worst = max(worst, abs(joint - law[F[0]](s0) * law[F[1]](s1)))
check("joint odds of the forming records = product of isolated-site laws, for every time and N state",
      worst < 1e-12, f"4 random N states x 3 times x 4 outcomes; max deviation {worst:.1e}")
# sequential readout in both orders, with collapse after the first record
worst_ord = 0.0
rho = np.kron(np.kron(rhoF[0], rhoF[1]), np.eye(4) / 4)
for s0 in (1, -1):
    for s1 in (1, -1):
        P0 = op(4, {0: proj(s0 * menus[F[0]])})
        P1 = op(4, {1: proj(s1 * menus[F[1]])})
        first0 = np.real(np.trace(P0 @ rho))
        post0 = P0 @ rho @ P0 / first0
        seq01 = first0 * np.real(np.trace(P1 @ post0))
        first1 = np.real(np.trace(P1 @ rho))
        post1 = P1 @ rho @ P1 / first1
        seq10 = first1 * np.real(np.trace(P0 @ post1))
        worst_ord = max(worst_ord, abs(seq01 - seq10), abs(seq01 - law[F[0]](s0) * law[F[1]](s1)))
check("sequential formation in either order gives the same product law", worst_ord < 1e-12,
      f"max deviation {worst_ord:.1e}")

# ------------------------------------------------------ E: the other branch
print("E. two adjacent unrecorded sites")
HH = sum(np.kron(S[a], S[a]) for a in range(3))
ev, V = np.linalg.eigh(HH)
gs = V[:, 0]
singlet = np.array([0, 1, -1, 0]) / np.sqrt(2)
fid = abs(np.vdot(singlet, gs)) ** 2
worst = 0.0
for _ in range(50):
    a, b = rand_unit(), rand_unit()
    E = np.real(gs.conj() @ np.kron(sdot(a), sdot(b)) @ gs)
    worst = max(worst, abs(E + a @ b))
check("an adjacent unrecorded pair (J > 0) has the singlet ground state and correlated odds E = -a.b",
      abs(fid - 1) < 1e-12 and worst < 1e-12, f"fidelity {fid:.12f}; max |E + a.b| {worst:.1e}")

# Missing-preparation counterexample: no coupling does not imply independent records.
bell = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
rbell = np.outer(bell, bell.conj())
pz = proj(np.array([0., 0., 1.]))
pa = np.trace(np.kron(pz, I2) @ rbell).real
pb = np.trace(np.kron(I2, pz) @ rbell).real
pab = np.trace(np.kron(pz, pz) @ rbell).real
check("isolated entangled preparation violates product odds", abs(pa-.5)<1e-12 and abs(pb-.5)<1e-12 and abs(pab-.5)<1e-12 and abs(pab-pa*pb-.25)<1e-12)

print('per_element: Pauli interaction terms and dependence on a neighbour state are tested.')
print('per_site: Isolated local fields are tested without a universal preparation selector.')
print('per_mode: checked and not executed — no momentum-mode or continuum no-go is claimed.')
print('per_block: Finite formation graphs and an initially entangled isolated pair are tested.')
print('lattice_wide: checked and not executed — no universal unreadability or product law is established.')

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
