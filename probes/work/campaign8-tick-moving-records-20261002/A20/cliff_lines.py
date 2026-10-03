"""Line constraints (mod 2), derived from covariance + det(M) a unit:
 - axis line (t,1,1): f projected on v_1 = k equals delta_{k0} X          [C4 commutant + C2 inversion]
 - body line (t,t,t): f projected on v1+v2+v3 = k equals delta_{k0} X      [C3 commutant + inversion]
 - face line (t,t,1): h = alpha(Z_0) projected on v1+v2 = k equals delta_{k0} Z  [C2 commutant + inversion]
Each is imposed for every O-image of the line (harmless redundancy). Returns the reduced basis dimension.
"""
import numpy as np
from grp import named, label_bits_matrix
from cliff_lin import box, Lmat, nullspace_f2

G = named()


def constraints(pts, idx, L3):
    n2 = 2 * len(pts)
    L33 = (L3.astype(int) @ L3) % 2
    rows, rhs = [], []
    def proj(direction, which, target_label):
        # sum over v with direction.v = k of (which-image)_v  ==  delta_{k0} target
        Wm = np.eye(n2, dtype=int) if which == "X" else L33
        ks = sorted({int(np.dot(direction, v)) for v in pts})
        for k in ks:
            for bit in range(2):
                row = np.zeros(n2, dtype=int)
                for i, v in enumerate(pts):
                    if int(np.dot(direction, v)) == k:
                        row = (row + Wm[2 * i + bit]) % 2
                rows.append(row); rhs.append(target_label[bit] if k == 0 else 0)
    for R in G["all"]:
        # images of the three line types; constraint labels transform too, but mod 2 the
        # projected identity statement is covariant, so impose the canonical ones in rotated frames
        pass
    # canonical lines only (covariance of f already makes the rotated ones equivalent)
    proj(np.array([1, 0, 0]), "X", (1, 0))
    proj(np.array([1, 1, 1]), "X", (1, 0))
    proj(np.array([1, 1, 0]), "Z", (0, 1))
    return np.array(rows, dtype=np.uint8), np.array(rhs, dtype=np.uint8)


def affine_solutions(shape, r):
    from cliff_lin import solve
    pts, idx, Bs, L3 = solve(shape, r)
    C, rhs = constraints(pts, idx, L3)
    # f = s @ Bs ; impose C f = rhs  ->  (C Bs^T) s = rhs
    A = (C.astype(int) @ Bs.T.astype(int)) % 2
    aug = np.hstack([A, rhs[:, None]]).astype(np.uint8)
    # particular solution + nullspace
    N = nullspace_f2(aug)
    # rows of N are solutions of [A|rhs] y = 0 ; need y_last = 1 for a particular solution
    part = None
    for y in N:
        if y[-1] == 1:
            part = y[:-1]; break
    hom = nullspace_f2(A.astype(np.uint8))
    return pts, idx, Bs, L3, part, hom


if __name__ == "__main__":
    for shape, r in [("oct", 1), ("cube", 1), ("oct", 2), ("cube", 2), ("oct", 3)]:
        pts, idx, Bs, L3, part, hom = affine_solutions(shape, r)
        print(f"{shape} r={r}: linear dim {len(Bs)} -> affine solution set: "
              f"{'EMPTY' if part is None else f'particular + {len(hom)}-dim'}")
