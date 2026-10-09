"""C4: 'see-or-stiff' on fixed graphs.  Uniform traceless strain h of a fixed periodic network whose
energy depends on the geometry only through local edge data.  Internal (sublattice) displacements u relax.
Quadratic energy, no prestress:  E2 = sum_b k (dl_b)^2 (+ optional bond-angle term), dl_b linear in (h,u).
Report: eigenvalues of the relaxed 5x5 traceless block (Schur complement over u), and the rank of the
map h -> edge data after relaxation ('visibility').  Prediction: modulus zero exactly on the invisible strains.
"""
import numpy as np
def traceless_basis():
    B = [np.diag([1., -1, 0])/np.sqrt(2), np.diag([1., 1, -2])/np.sqrt(6)]
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1/np.sqrt(2); B.append(M)
    return B
TB = traceless_basis()

def relaxed(bonds, n_inner, angle_pairs=(), kb=0.0):
    """bonds: list of (vector e, index of inner displacement or None); length change
    dl = (e.h.e/2 + e.u)/|e| for g = exp(h) (proper length sqrt(e^T g e))."""
    rows = []
    for e, ui in bonds:
        e = np.asarray(e, float); le = np.linalg.norm(e)
        row = [e @ Bh @ e/(2*le) for Bh in TB]
        uu = np.zeros(3*n_inner)
        if ui is not None: uu[3*ui:3*ui+3] = e/le
        rows.append(row + list(uu))
    # bond-angle term: change of e_a . e_b (proper) with both bonds sharing a site: d(e_a.g.e_b) = e_a.h.e_b + u-terms
    for (ea, ia), (eb, ib) in angle_pairs:
        ea = np.asarray(ea, float); eb = np.asarray(eb, float)
        row = [np.sqrt(kb)*(ea @ Bh @ eb) for Bh in TB]
        uu = np.zeros(3*n_inner)
        if ia is not None: uu[3*ia:3*ia+3] += np.sqrt(kb)*eb
        if ib is not None: uu[3*ib:3*ib+3] += np.sqrt(kb)*ea
        rows.append(row + list(uu))
    J = np.array(rows); K = J.T @ J
    Khh, Khu, Kuu = K[:5, :5], K[:5, 5:], K[5:, 5:]
    S = Khh - (Khu @ np.linalg.pinv(Kuu) @ Khu.T if Kuu.size else 0)
    ev = np.linalg.eigvalsh(S)
    # visibility after relaxation: rank of S equals rank of relaxed data map
    return np.round(ev, 12), int(np.sum(ev > 1e-10))

sc = [((1, 0, 0), None), ((0, 1, 0), None), ((0, 0, 1), None)]
fcc = [(v, None) for v in [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]]
tet = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
diamond = [(v, 0) for v in tet]          # A at 0, B displaced by u: bond vectors e_b + u
diamond_rigid = [(v, None) for v in tet]
angles = [((tet[a], 0), (tet[b], 0)) for a in range(4) for b in range(a+1, 4)]
print('simple cubic, NN central springs       :', relaxed(sc, 0))
print('FCC, NN central springs                :', relaxed(fcc, 0))
print('diamond, central, inner sublattice FIXED:', relaxed(diamond_rigid, 0))
print('diamond, central, inner sublattice relaxes (pentamode):', relaxed(diamond, 1))
print('diamond, + bond-angle term (kb=0.3)    :', relaxed(diamond, 1, angles, 0.3))
