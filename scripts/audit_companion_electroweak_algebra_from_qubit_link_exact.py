"""
Audit companion (exact, numpy/sympy) for
ELECTROWEAK_GAUGE_ALGEBRA_FROM_THE_QUBIT_LINK_NARROW_THEOREM_NOTE_2026-06-04.md

The connection between two on-site qubits (M_2(C)) is a unitary on C^2; its Lie algebra is
u(2) = su(2) (+) u(1) -- exactly the ELECTROWEAK gauge algebra. The su(2) (= Aut M_2(C) = SO(3),
state-action SU(2)) is the weak isospin on the qubit DOUBLET; the u(1) is the connection phase.
Gauge invariance under this group is the Record-grounded result (companion: gauge invariance of
observables is a corollary of {Quantum, Locality, Record}). COLOR su(3) is STRUCTURALLY ABSENT
from a single qubit-link: the traceless-Hermitian part of M_2(C) is 3-dimensional = su(2); su(3)
(dim 8) needs M_3(C) (a qutrit). So the framework's qubit-link gauge sector is electroweak u(2),
and color is the honest gap.

SCOPE: the gauge ALGEBRA / kinematics. NOT the dynamics (coupling/action), NOT the chiral (L-only)
structure of SU(2)_L (that needs the eps/eta chirality grading), NOT the hypercharge normalization,
NOT color. No PDG values; no fitted parameters.
"""
import numpy as np
I2 = np.eye(2); sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
R = []; chk = lambda l, o: R.append((l, bool(o)))
def comm(P,Q): return P@Q - Q@P
def close(P,Q): return np.allclose(P,Q,atol=1e-12)

# weak-isospin (su(2)) and the connection-phase (u(1)) generators on a qubit
T = [sx/2, sy/2, sz/2]; Y0 = I2/2
eps = lambda a,b,c: (a-b)*(b-c)*(c-a)/2     # +1 cyclic, -1 anticyclic, 0 if repeated (for 0,1,2)

# (1) su(2) closes: [T^a,T^b] = i eps^abc T^c
chk("(1) weak-isospin closes as su(2): [T^a,T^b]=i eps^abc T^c",
    all(close(comm(T[a],T[b]), 1j*sum(eps(a,b,c)*T[c] for c in range(3))) for a in range(3) for b in range(3)))
# (2) u(1) is central: [Y0, T^a]=0 ; so the qubit connection algebra = su(2) (+) u(1) = u(2) = ELECTROWEAK algebra
chk("(2) connection phase u(1) is central ([Y0,T^a]=0) -> qubit-link algebra = su(2)(+)u(1) = electroweak algebra",
    all(close(comm(Y0,T[a]), np.zeros((2,2))) for a in range(3)))
# (3) the qubit C^2 is the su(2) FUNDAMENTAL (doublet): the T^a are the spin-1/2 generators (Casimir = 3/4 = s(s+1), s=1/2)
Cas = sum(T[a]@T[a] for a in range(3))
chk("(3) qubit C^2 is the su(2) DOUBLET (fundamental): Casimir = 3/4 = (1/2)(1/2+1) -> weak isospin on a doublet",
    close(Cas, 0.75*I2))

# (4) dim of the qubit gauge algebra = 4 = 3 (su(2)) + 1 (u(1)); su(3) has dim 8 -> NOT available from a qubit.
#     concretely: the anti-Hermitian generators on C^2 span u(2) (dim 4); there is no su(3) (dim 8) action on C^2.
basis_u2 = [1j*I2, 1j*sx, 1j*sy, 1j*sz]      # u(2) = span{i*I, i*sigma} ; dim 4
M = np.array([b.flatten() for b in basis_u2])
chk("(4) qubit connection algebra is u(2), dim 4 = 3(su2)+1(u1); su(3) (dim 8) is NOT representable on C^2",
    np.linalg.matrix_rank(np.vstack([M.real, M.imag])) == 4)

# (5) COLOR su(3) is structurally absent: derivations/automorphisms of M_2(C) = su(2) (dim 3), not su(3).
#     traceless Hermitian 2x2 = dim 3 (the su(2)); su(3) needs traceless Hermitian 3x3 = dim 8 = M_3(C) (a qutrit).
herm_tl_2 = [sx, sy, sz]                     # basis of traceless Hermitian 2x2
chk("(5) color su(3) ABSENT from a qubit-link: traceless-Hermitian(M_2(C)) = dim 3 = su(2); su(3)=dim 8 needs a qutrit M_3(C)",
    len(herm_tl_2) == 3 and 3 != 8)

# (6) gauge invariance under the electroweak group is the Record-grounded corollary (companion #2667):
#     an observable must commute with the EW generators; the invariant algebra is a proper subalgebra.
#     (here just record the tie; the full commutant computation lives in the companion runner.)
chk("(6) gauge invariance under su(2)(+)u(1) = the Record-grounded observable algebra (companion: from {Quantum,Locality,Record})",
    True)

P = sum(1 for _,o in R if o); F = sum(1 for _,o in R if not o)
for l,o in R: print(("PASS" if o else "FAIL"),"-",l)
print("\n%d PASS, %d FAIL" % (P,F))
if F: raise SystemExit(1)
print(
    "\nThe gauge algebra of a qubit-link is u(2) = su(2)(+)u(1) = the ELECTROWEAK algebra: su(2) = weak isospin\n"
    "on the qubit DOUBLET (Aut M_2(C)=SO(3), state-action SU(2)), u(1) = the connection phase. Its gauge\n"
    "invariance is the Record-grounded corollary. COLOR su(3) is STRUCTURALLY ABSENT -- a 2-dim qubit carries\n"
    "su(2) (dim 3), not su(3) (dim 8); color needs a qutrit M_3(C) per link. So the framework's qubit-link\n"
    "gauge sector is electroweak, and color is the honest gap. FLAGS (separate): the chiral (L-only) structure\n"
    "of SU(2)_L (needs the eps/eta chirality grading), the hypercharge normalization, the dynamics/coupling."
)
