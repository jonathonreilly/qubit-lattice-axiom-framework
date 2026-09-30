"""Test B1: simplest bond energy of block 56 (phi harmonic: phi_x = mean of six neighbours),
box side L (sites 0..L-1, walls = outer shell held at phi=1), stopped ball (phi=0) of radius R.
Ledger = (12/gamma) Cap(B) with Cap(B)= sum_{x in B} q_x, psi = 1-phi.  Validation: R=6, L=41
must give 192.32 (block 56 note, historical table).  Then exterior profile along the axis."""
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl, json

def solve(L, R, centre=None):
    c = (L - 1) // 2 if centre is None else centre
    idx = np.arange(L)
    X, Y, Z = np.meshgrid(idx, idx, idx, indexing="ij")
    ball = ((X - c) ** 2 + (Y - c) ** 2 + (Z - c) ** 2) <= R * R
    wall = (X == 0) | (X == L - 1) | (Y == 0) | (Y == L - 1) | (Z == 0) | (Z == L - 1)
    free = ~wall & ~ball
    n = L ** 3
    flat = lambda a: a.reshape(-1)
    fid = -np.ones(n, dtype=int)
    ids = np.flatnonzero(flat(free)); fid[ids] = np.arange(len(ids))
    psi_fixed = np.zeros(n); psi_fixed[flat(ball)] = 1.0   # psi = 1 - phi
    rows, cols, vals = [], [], []
    rhs = np.zeros(len(ids))
    shifts = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    strides = np.array([L*L, L, 1])
    for s in shifts:
        nb = ids + s[0]*L*L + s[1]*L + s[2]
        isfree = fid[nb] >= 0
        rows += list(fid[ids][isfree]); cols += list(fid[nb][isfree]); vals += [-1/6] * int(isfree.sum())
        rhs[fid[ids][~isfree]] += psi_fixed[nb[~isfree]] / 6.0
    A = sp.csr_matrix((vals, (rows, cols)), shape=(len(ids), len(ids))) + sp.identity(len(ids))
    psi, info = spl.cg(A, rhs, rtol=1e-13, atol=0, maxiter=20000)
    assert info == 0, info
    P = psi_fixed.copy(); P[ids] = psi
    # ledger: Cap = sum over ball sites of ((1-A)psi)_x
    bids = np.flatnonzero(flat(ball))
    cap = float(np.sum(P[bids] - sum(P[bids + (s[0]*L*L + s[1]*L + s[2])] for s in shifts) / 6.0))
    return P.reshape(L, L, L), cap, c

if __name__ == "__main__":
    out = {}
    L = 41
    P, cap, c = solve(L, 6)
    print(f"validation: L=41 R=6  ledger = 12*Cap = {12*cap:.2f}   (note: 192.32)")
    out["validation_ledger_R6_L41"] = 12 * cap
    print("\nexterior profile along +x axis: phi_n = 1-psi, n = distance from first stopped-side site (n=0 is the last ball site)")
    print(" R   L  | phi_1..phi_5 ; local exponent p12 = 2 ln(phi_2/phi_1)/ln 2 ; p23 ; continuum shell (1-R/r) prediction p12")
    rows = []
    for (Lb, R) in [(41, 4), (41, 6), (41, 8), (41, 10), (61, 10), (61, 14), (81, 18)]:
        P, cap, c = solve(Lb, R)
        phi = 1 - P[c + R: c + R + 7, c, c]     # n=0 at x=c+R (last ball site, phi=0)
        p12 = 2 * np.log(phi[2] / phi[1]) / np.log(2)
        p23 = 2 * np.log(phi[3] / phi[2]) / np.log(1.5)
        cont = lambda n: (1 - R / (R + n))
        pc12 = 2 * np.log(cont(2) / cont(1)) / np.log(2)
        pc23 = 2 * np.log(cont(3) / cont(2)) / np.log(1.5)
        print(f"{R:3d} {Lb:3d} | " + " ".join(f"{v:.4f}" for v in phi[1:6]) + f" | p12={p12:.3f} p23={p23:.3f} | cont p12={pc12:.3f} p23={pc23:.3f} | ledger/(8 pi R)={12*cap/(8*np.pi*R):.3f}")
        rows.append(dict(R=R, L=Lb, phi=list(map(float, phi[:6])), p12=p12, p23=p23, cont_p12=pc12, cont_p23=pc23, ledger=12*cap))
    out["rows"] = rows
    # flat wall (half space of stopped sites) for the exact linear case
    L = 41; idx = np.arange(L)
    print("\n(the flat-face case is exactly phi_n = n phi_1 by 1D discrete harmonicity: p = 2 for all n)")
    json.dump(out, open("B1_results.json", "w"), indent=1)
