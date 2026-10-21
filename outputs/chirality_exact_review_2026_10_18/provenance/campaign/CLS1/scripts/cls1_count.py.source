"""CLS-1 step 4: count the symmetry-allowed light-sector bilinears (3 hw1 corners x 2 spin) under the 24 proper rotations,
for exact unit translations (corner-diagonal only) vs BCC (corner off-diagonal allowed).
dim-3: constant Hermitian M0 with U M0 U^dag = M0  (Theta-odd: forbidden if Theta is imposed)
dim-4: H(q) = sum_b M_b q_b with U M_b U^dag = sum_b' R_b'b M_b'  (Theta-even)
Also: whether each invariant dim-4 structure splits the light speeds (flavour non-universal) or is Lorentz-like."""
import numpy as np, itertools, sys
sys.path.insert(0, '.')
from cls1_core import *
def P(*a): print(*a); sys.stdout.flush()
LC = [np.array([PI, 0, 0]), np.array([0, PI, 0]), np.array([0, 0, PI])]
def cidx(Q):
    for i, C in enumerate(LC):
        d = (Q - C) / (2 * PI)
        if np.allclose(d, np.round(d)): return i
    raise ValueError
ROT = rotations()
Us = []
for R in ROT:
    Pm = np.zeros((3, 3))
    for i, C in enumerate(LC):
        Pm[cidx(R @ C), i] = 1
    Us.append((R, np.kron(Pm, spin_lift(R))))
# Hermitian basis of 6x6
def herm_basis(n, mask=None):
    B = []
    for i in range(n):
        for j in range(i, n):
            if mask is not None and not mask[i, j]: continue
            E = np.zeros((n, n), complex); E[i, j] = 1; E[j, i] = 1; B.append(E)
            if i != j:
                E = np.zeros((n, n), complex); E[i, j] = -1j; E[j, i] = 1j; B.append(E)
    return B
diag_mask = np.kron(np.eye(3), np.ones((2, 2))).astype(bool)
def invariant_dim3(mask=None):
    B = herm_basis(6, mask); nb = len(B)
    rows = []
    for R, U in Us:
        A = np.array([(U @ E @ U.conj().T - E).ravel() for E in B]).T   # 36 x nb complex
        rows.append(np.vstack([A.real, A.imag]))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A, full_matrices=False)
    null = vh[np.sum(s > 1e-9):]
    return [sum(c * E for c, E in zip(v, B)) for v in null]
def invariant_dim4(mask=None):
    B = herm_basis(6, mask); nb = len(B)
    # unknowns: coefficients x[b, n] for M_b = sum_n x[b,n] B_n
    rows = []
    for R, U in Us:
        for b in range(3):
            # U M_b U^dag - sum_b' R[b',b] M_b' = 0
            blocks = []
            for bb in range(3):
                coef = (1.0 if bb == b else 0.0)
                cols = []
                for E in B:
                    term = coef * (U @ E @ U.conj().T) - R[bb, b] * E
                    cols.append(term.ravel())
                blocks.append(np.array(cols).T)
            A = np.hstack(blocks)
            rows.append(np.vstack([A.real, A.imag]))
    A = np.vstack(rows)
    _, s, vh = np.linalg.svd(A, full_matrices=False)
    null = vh[np.sum(s > 1e-9):]
    sols = []
    for v in null:
        Ms = [sum(v[b*nb + n] * B[n] for n in range(nb)) for b in range(3)]
        sols.append(Ms)
    return sols
d3_all = invariant_dim3(); d3_diag = invariant_dim3(diag_mask)
d4_all = invariant_dim4(); d4_diag = invariant_dim4(diag_mask)
P(f"dim-3 (constant) cubic-invariant structures: corner-diagonal (exact translations) {len(d3_diag)}, all (BCC) {len(d3_all)} "
  f"-> new under BCC: {len(d3_all) - len(d3_diag)}  [all Theta-odd]")
P(f"dim-4 (linear in q) cubic-invariant structures: corner-diagonal {len(d4_diag)}, all (BCC) {len(d4_all)} "
  f"-> new corner-off-diagonal under BCC: {len(d4_all) - len(d4_diag)}  [all Theta-even]")
# characterise: eigenvalues of the dim-3 structures; speed splitting of the dim-4 structures
H0 = lambda q: np.kron(np.eye(3), np.zeros((2, 2))) + sum(np.kron(np.diag([np.cos(C[b]) for C in LC]), SIG[b]) * q[b] for b in range(3))
for i, M in enumerate(d3_all):
    ev = np.round(np.linalg.eigvalsh(M / np.abs(M).max()), 4)
    offd = np.abs(M[~diag_mask]).max()
    P(f"  dim-3 structure {i}: eigenvalues {ev}, corner-off-diagonal norm {offd:.2f}")
rng = np.random.default_rng(3)
qs = [x / np.linalg.norm(x) for x in rng.normal(size=(40, 3))]
for i, Ms in enumerate(d4_all):
    nrm = max(np.abs(M).max() for M in Ms)
    Ms = [M / nrm for M in Ms]
    offd = max(np.abs(M[~diag_mask]).max() for M in Ms)
    spreads = []
    for q in qs:
        e = np.linalg.eigvalsh(H0(q) + 1e-3 * sum(Ms[b] * q[b] for b in range(3)))
        sp = np.sort(np.abs(e))
        spreads.append((sp.max() - sp.min()) / 1e-3)
    P(f"  dim-4 structure {i}: corner-off-diagonal norm {offd:.2f}; speed spread per unit coefficient (max over q) {max(spreads):.3f}, min over q {min(spreads):.3f}")
# where does P-c's light block sit: project the folded P-c term onto the light corners and decompose
Pk = np.array([PI, 0, 0]); order = [0, 3, 2]   # folded indices of hw1_x, hw1_y, hw1_z at P
def light_block(Hf):
    idx = sum([[2*i, 2*i+1] for i in order], [])
    return Hf[np.ix_(idx, idx)]
Mpc = [ (light_block(h_psi(Pk + 1e-6*np.eye(3)[b], eta=1.0)) - light_block(h_psi(Pk - 1e-6*np.eye(3)[b], eta=1.0))) / 2e-6
        - (light_block(h_psi(Pk + 1e-6*np.eye(3)[b])) - light_block(h_psi(Pk - 1e-6*np.eye(3)[b]))) / 2e-6 for b in range(3)]
basis = np.array([np.concatenate([M.ravel() for M in Ms]) for Ms in d4_all]).T
target = np.concatenate([M.ravel() for M in Mpc])
coef, res, *_ = np.linalg.lstsq(basis, target, rcond=None)
P(f"P-c light block lies in the invariant span: residual {np.linalg.norm(basis @ coef - target):.1e}; corner-off-diagonal norm {max(np.abs(M[~diag_mask]).max() for M in Mpc):.2f}")
