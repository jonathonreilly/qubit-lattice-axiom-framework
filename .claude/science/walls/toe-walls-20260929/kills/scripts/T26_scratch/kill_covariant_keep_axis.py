"""Kill check for T26, second construction: keep the graph-first weak axis (axis 1 fibre, weak su(2) = Pauli(axis 1)/2 on all of C^8)
but take the 3-block of the base (axes 2,3) to be a span of THREE of the four base translation characters instead of the tau-Sym block.
Test: is the resulting su(3)+su(2)+u(1) (dim 12, same abstract structure, commuting factors) closed under the lattice translations X_i
(and tau, and the axis-2/3 permutation)?  Attacker's graph-first g8 needs 18."""
import itertools, math, json
import numpy as np
exec(open('test_T26.py').read().split("# ------------- TEST A")[0])

def gm(n):
    ms = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), dtype=complex); m[i, j] = m[j, i] = 1; ms.append(m)
            m = np.zeros((n, n), dtype=complex); m[i, j] = -1j; m[j, i] = 1j; ms.append(m)
    for k in range(1, n):
        m = np.zeros((n, n), dtype=complex)
        for i in range(k): m[i, i] = 1
        m[k, k] = -k
        ms.append(m / math.sqrt(k * (k + 1) / 2))
    return ms
G3 = gm(3)
base_pos = list(itertools.product((0, 1), repeat=2))
def base_char(k):
    return np.array([(-1) ** (k[0] * b[0] + k[1] * b[1]) for b in base_pos], dtype=complex) / 2
out = {}
for label, chars in {"V3 = chars {00,01,10} (excl. 11)": [(0, 0), (0, 1), (1, 0)],
                     "V3 = chars {01,10,11} (excl. 00)": [(0, 1), (1, 0), (1, 1)],
                     "V3 = chars {00,01,11} (excl. 10, not tau-invariant)": [(0, 0), (0, 1), (1, 1)]}.items():
    Vb = np.column_stack([base_char(k) for k in chars])                     # 4 x 3
    Vfull = np.kron(np.eye(2), Vb)                                        # 6 -> (fibre (x) base), fibre first
    E = U @ Vfull                                                         # 8 x 6 (U maps (f,b1,b2) ordering to the cube corner index)
    su3 = [1j * (E @ np.kron(np.eye(2), l / 2) @ E.conj().T) for l in G3]
    weak_full = g_su2                                                      # repo's weak su(2): Pauli(axis 1)/2 on all of C^8 (from prefix)
    P6 = E @ E.conj().T
    Y = 1j * (P6 / 3 - (I8 - P6))
    g = su3 + weak_full + [Y]
    dim0 = close(g).dim
    # commuting factors?
    comm_ok = all(np.linalg.norm(comm(a, b)) < 1e-9 for a in su3 for b in weak_full + [Y]) and all(np.linalg.norm(comm(a, Y)) < 1e-9 for a in weak_full)
    cl_T = close(g, X).dim
    cl_Ttau = close(g, X + [tau]).dim
    cl_Tperm23 = close(g, X + [tau]).dim
    print(f"{label}: dim {dim0}; factors commute: {comm_ok}; closure under X_i: {cl_T}; under X_i + tau: {cl_Ttau};"
          f" tau normalises: {close(g, [tau]).dim}")
    out[label] = dict(dim=dim0, commute=bool(comm_ok), closure_X=cl_T, closure_X_tau=cl_Ttau)
json.dump(out, open('kill_covariant_keep_axis_results.json', 'w'), indent=1)
