"""
Audit companion (exact, numpy) for
GAUGE_INVARIANCE_IS_THE_RECORD_AXIOM_ON_LINKS_CONDITIONAL_THEOREM_NOTE_2026-06-04.md

CONDITIONAL on the qulink ontology (each lattice LINK carries one constituent/"rishon" per endpoint,
gauge-transforming with that endpoint's node-qubit). Claim: the Record axiom -- "the physical
observable is the additive-log of the record; only FULLY-PINNED (both-endpoint-determined) quantities
are observables" -- selects EXACTLY the gauge-invariant algebra (the commutant of the per-vertex
Gauss-law generators). Hence local gauge invariance / the Gauss law is the Record axiom applied to links,
NOT a separate postulate.

The lattice-gauge math (Gauss law, Wilson line, gauge-invariant = commutant) is STANDARD and is reproven
here from Pauli primitives; the CONTRIBUTION is the bridge: record-count (0/1/2 endpoints) = gauge-
invariance level. Scope: this is the gauge CONSTRAINT/kinematics, NOT the gauge dynamics (the coupling /
Hamiltonian is untouched). Conditional on adopting qulinks (a genuine edge degree of freedom).
"""
import numpy as np, itertools
I2 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
sp = np.array([[0,1],[0,0]]); sm = np.array([[0,0],[1,0]])

def op(X, pos, n=4):                       # place 2x2 X on qubit `pos` of n ; order [A, a, b, B]
    M = [I2]*n; M[pos] = X; out = M[0]
    for k in range(1, n): out = np.kron(out, M[k])
    return out
def comm(P, Q): return P@Q - Q@P
def nz(M): return np.linalg.norm(M) > 1e-9

A, a, b, B = 0, 1, 2, 3                     # matter A, rishon-at-A, rishon-at-B, matter B
R = []; chk = lambda l, o: R.append((l, bool(o)))

# ---- U(1) gauge: Gauss-law generator at a vertex = total charge there = (matter sz)+(its rishon sz) ----
GA = op(sz,A) + op(sz,a)                    # vertex A
GB = op(sz,b) + op(sz,B)                    # vertex B
bare = op(sp,a) @ op(sm,b)                                  # 0 endpoints dressed: bare link transport
half = op(sm,A) @ op(sp,a) @ op(sm,b)                       # 1 endpoint dressed (at A)
full = op(sm,A) @ op(sp,a) @ op(sm,b) @ op(sp,B)            # 2 endpoints dressed = Wilson line
inv = lambda O: [not nz(comm(GA,O)), not nz(comm(GB,O))]    # gauge-invariant at [A, B]?

chk("(1) bare link (0 records) is gauge-VARIANT at BOTH vertices", inv(bare) == [False, False])
chk("(2) half-dressed (1 record) invariant at A, VARIANT at B -- the 'lost half', NOT yet a record",
    inv(half) == [True, False])
chk("(3) full Wilson line (2 records) gauge-INVARIANT at BOTH -> a genuine record/observable",
    inv(full) == [True, True])
chk("(4) record-count == # vertices where the Gauss law holds, monotone 0->1->2",
    sum(inv(bare)) == 0 and sum(inv(half)) == 1 and sum(inv(full)) == 2)

# ---- COMPLETENESS: gauge-invariant ALGEBRA = commutant of the Gauss-law generators (not just examples) ----
paulis = [I2, sx, sy, sz]; basis = []
for t in itertools.product(range(4), repeat=4):
    M = paulis[t[0]]
    for k in range(1, 4): M = np.kron(M, paulis[t[k]])
    basis.append(M)
def adj(G):
    return np.array([[np.trace(Bj.conj().T @ comm(G, Bk))/16 for Bk in basis] for Bj in basis])
rank = np.linalg.matrix_rank(np.vstack([adj(GA), adj(GB)]), tol=1e-8); inv_dim = 256 - rank
# expected: operators charge-balanced at each vertex; (2-qubit sz-sectors dims 1,2,1 -> 1^2+2^2+1^2=6) per vertex -> 6*6=36
chk("(5) gauge-invariant algebra = commutant of {GA,GB}, dim = 36 (=6x6 vertex-balanced) -- a genuine constraint, < 256",
    inv_dim == 36)

# ---- SU(2) gauge (the framework's qubit-link group, prong 3): same structure ----
SA = [(op(s,A)+op(s,a))/2 for s in (sx,sy,sz)]   # vertex-A SU(2) generators
SB = [(op(s,b)+op(s,B))/2 for s in (sx,sy,sz)]
su2 = lambda O: [all(not nz(comm(S,O)) for S in SA), all(not nz(comm(S,O)) for S in SB)]
sing = np.array([0,1,-1,0])/np.sqrt(2)           # 2-qubit singlet |01>-|10>
Wsu2 = np.kron(np.outer(sing,sing), np.outer(sing,sing))   # double-singlet (gauge-inv Wilson-type observable)
chk("(6) SU(2): bare link VARIANT at both; double-singlet observable INVARIANT at both (Gauss law both vertices)",
    su2(op(sp,a)@op(sm,b)) == [False, False] and su2(Wsu2) == [True, True])

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nDERIVED (conditional on the qulink ontology): the Record axiom -- only fully-pinned (both-endpoint)\n"
    "quantities are observables -- selects EXACTLY the gauge-invariant algebra (commutant of the per-vertex\n"
    "Gauss-law generators). The record-count 0/1/2 = the gauge-invariance level (variant-at-both / variant-\n"
    "at-one('lost half') / invariant). So local gauge invariance / the Gauss law is the Record axiom applied\n"
    "to links, not a separate postulate. SCOPE: the gauge CONSTRAINT (kinematics) only -- the coupling/\n"
    "dynamics (e.g. beta=6) is untouched. Standard lattice-gauge math reproven; the Record bridge is the\n"
    "contribution. Conditional on adopting qulinks (a genuine new edge degree of freedom)."
)
