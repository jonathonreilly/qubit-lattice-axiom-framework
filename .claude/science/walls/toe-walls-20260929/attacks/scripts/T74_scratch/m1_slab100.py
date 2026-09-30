"""M1: pi-flux cubic sea (+ staggered mass m), (100) cut, transverse-momentum chains.
Gauge: eta_x=1, eta_y=(-1)^x, eta_z=(-1)^(x+y); mass eps=(-1)^(x+y+z).
Cell: 2 in y, 2 in z -> 4 orbitals (sy,sz) per x slice. Periodic chain of Lx slices.
eta = mean_k S_k / (4 sites per transverse cell) / 2 cuts.
"""
import numpy as np, sys, time
def block(Lx, th_y, th_z, m):
    n = 4*Lx
    H = np.zeros((n,n), dtype=complex)
    idx = lambda x,sy,sz: 4*(x % Lx) + 2*sy + sz
    for x in range(Lx):
        sgn = (-1)**x
        for sy in range(2):
            for sz in range(2):
                i = idx(x,sy,sz)
                # x hop (eta_x = 1)
                j = idx(x+1,sy,sz)
                H[j,i] += 1.0; H[i,j] += 1.0
                # mass
                H[i,i] += m * (-1)**(x+sy+sz)
                # y hop: (sy=0)<->(sy=1) same cell weight 1 ; (sy=1)->(sy=0) next cell e^{i th_y}
                # site (sy=1, cell j) -> (sy=0, cell j+1)
                if sy == 0:
                    k = idx(x,1,sz)
                    w = sgn*(1.0 + np.exp(-1j*th_y))   # (0)<->(1): same cell and previous cell
                    H[i,k] += w; H[k,i] += np.conj(w)
                # z hop: eta_z = (-1)^(x+y) = (-1)^(x+sy)
                if sz == 0:
                    k = idx(x,sy,1)
                    w = (-1)**(x+sy)*(1.0 + np.exp(-1j*th_z))
                    H[i,k] += w; H[k,i] += np.conj(w)
    return H
def S_of_corr(C):
    nu = np.linalg.eigvalsh(C)
    nu = np.clip(nu, 1e-14, 1-1e-14)
    return float(-np.sum(nu*np.log(nu)+(1-nu)*np.log(1-nu)))
def eta100(Lx, ell, Nt, m, offset=0.5):
    ths = 2*np.pi*(np.arange(Nt)+offset)/Nt
    tot = 0.0; cnt = 0
    for a in ths:
        for b in ths:
            if b < a - 1e-12:  # symmetry (th_y,th_z)->(th_z,th_y)? not exact (gauge); do full grid
                pass
            H = block(Lx, a, b, m)
            E, V = np.linalg.eigh(H)
            occ = V[:, E < 0]
            P = occ @ occ.conj().T
            sel = np.arange(4*ell)
            tot += S_of_corr(P[np.ix_(sel,sel)]); cnt += 1
    Sk = tot/cnt
    return Sk/(4*2)   # per site of transverse cell, two cuts
if __name__ == "__main__":
    m = float(sys.argv[1]); Lx = int(sys.argv[2]); Nt = int(sys.argv[3])
    ell = Lx//2
    t=time.time()
    print(f"m={m} Lx={Lx} ell={ell} Nt={Nt} eta100={eta100(Lx,ell,Nt,m):.5f}  ({time.time()-t:.1f}s)")
