"""T-F4-3: folded (twisted I-bundle) Wilson slab: one Weyl, no mirror? Free fermions, numpy only."""
import numpy as np
s0 = np.eye(2, dtype=complex); sx = np.array([[0,1],[1,0]],complex); sy = np.array([[0,-1j],[1j,0]]); sz = np.diag([1.,-1.]).astype(complex)
G1, G2, G3, G4, G5 = np.kron(sx,sx), np.kron(sx,sy), np.kron(sx,sz), np.kron(sy,s0), np.kron(sz,s0)
MU = 3.0
Mt = (-1j*G4 - G5)/2   # c_t^dag Mt c_{t+1}
My = (-1j*G2 - G5)/2   # c_y^dag My c_{y+1}
S = G2 @ G4
assert np.allclose(S @ S, -np.eye(4))
for Gm, sgn in ((G1,1),(G2,-1),(G3,1),(G4,-1),(G5,1)):
    assert np.allclose(S @ Gm @ np.linalg.inv(S), sgn*Gm)
assert np.allclose(S @ Mt @ np.linalg.inv(S), Mt.conj().T)
lam = 1j

def H_quot(kx, kz, N, L, glued=True, gs=0.5):
    # gs=0.5 is the correct quotient bond (the loop below visits each {y,-y} pair twice); gs=1.0 was the 13:52Z run (doubled gluing bond)
    """Basis index: ((t-1)*N + y)*4 + a, t=1..L (t=L is the boundary face), y in Z_N.
    glued=True: quotient (midplane bond y <-> -y on layer 1). glued=False: layer 1 is a free face (ordinary slab of L layers)."""
    n = 4*N*L
    H = np.zeros((n, n), complex)
    on = G1*np.sin(kx) + G3*np.sin(kz) + G5*(MU - np.cos(kx) - np.cos(kz))
    idx = lambda t, y: ((t-1)*N + (y % N))*4
    for t in range(1, L+1):
        for y in range(N):
            i = idx(t, y); H[i:i+4, i:i+4] += on
            j = idx(t, y+1); H[i:i+4, j:j+4] += My; H[j:j+4, i:i+4] += My.conj().T
            if t < L:
                j = idx(t+1, y); H[i:i+4, j:j+4] += Mt; H[j:j+4, i:i+4] += Mt.conj().T
    if glued:
        A = gs*(lam*S).conj().T @ Mt * np.exp(1j*kx*N/2)
        for y in range(N):
            i = idx(1, -y); j = idx(1, y)
            H[i:i+4, j:j+4] += A; H[j:j+4, i:i+4] += A.conj().T
    assert np.allclose(H, H.conj().T)
    return H

def layer_centroid(v, N, L):
    w = np.abs(v.reshape(L, N, 4))**2
    wl = w.sum(axis=(1,2)); return (np.arange(1, L+1) @ wl)/wl.sum()

if __name__ == "__main__":
    for N, L in ((16, 4), (24, 6)):
        print(f"=== N={N}, L={L} ===")
        for glued in (False, True):
            w, v = np.linalg.eigh(H_quot(0.0, 0.0, N, L, glued))
            nz = np.sum(np.abs(w) < 1e-8)
            low = np.argsort(np.abs(w))[:6]
            print(f"  glued={glued}: zero modes at kx=kz=0: {nz}; lowest |E| (E, centroid):",
                  [(round(w[i],5), round(layer_centroid(v[:,i],N,L),2)) for i in low])
        # count |E|<delta over the full (kx,kz) grid
        delta = 2*np.pi/N*1.01*1.5
        ks = 2*np.pi*np.arange(N)/N
        for glued in (False, True):
            cnt = 0; cents = []
            for kx in ks:
                for kz in ks:
                    w, v = np.linalg.eigh(H_quot(kx, kz, N, L, glued))
                    sel = np.where(np.abs(w) < delta)[0]
                    cnt += len(sel); cents += [layer_centroid(v[:,i],N,L) for i in sel]
            cents = np.array(cents)
            print(f"  glued={glued}: states with |E|<{delta:.3f} over all kx,kz: {cnt}; centroid range "
                  f"[{cents.min():.2f}, {cents.max():.2f}]; on face t=L (centroid>L-1): {np.sum(cents>L-1)}; near t=1 (centroid<2): {np.sum(cents<2)}")
        # one free Weyl sigma.k on the same momentum grid
        ky = ks; cntW = 0
        for kx in ks:
            for kz in ks:
                for k2 in ky:
                    kk = np.array([kx,k2,kz]); kk = (kk+np.pi)%(2*np.pi)-np.pi
                    if np.all(np.abs(kk) < 1.0):
                        e = np.linalg.norm(np.sin(kk)); cntW += 2*(e < delta) if e < 1e-12 else int(e < delta)*2
        print(f"  reference: continuum-like single Weyl (2 bands, nodes only at k=0) count with |E|<delta: ~{cntW}")
    # nonlocal splitting vs L: in the quotient the y <-> -y bond couples k_y and -k_y on the face only through depth L
    print("=== nonlocal y<->-y splitting of the boundary branch vs L (N=16, kx=kz=0) ===")
    N = 16
    for L in (2, 3, 4, 6, 8):
        w, v = np.linalg.eigh(H_quot(0.0, 0.0, N, L, True))
        wu, vu = np.linalg.eigh(H_quot(0.0, 0.0, N, L, False))
        # compare the lowest positive face-localized levels (k_y = 2pi/N, 4pi/N, ...) glued vs unglued
        pos = np.sort(w[(w > 1e-9) & (w < 1.0)])[:6]; posu = np.sort(wu[(wu > 1e-9) & (wu < 1.0)])
        print(f"  L={L}: glued lowest positive {np.round(pos,6)}")
