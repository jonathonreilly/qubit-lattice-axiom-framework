"""Test 2b (T70): induced action of a free scalar on Z^3 (Hamiltonian, continuous time) under a slowly
varying static metric.  Vacuum energy E0 = (1/2) sum omega, exact diagonalisation in supercells.

H = sum_s [ N/(2 sqrt g) pi^2 + (1/2) N sqrt g g^{ij} d_i phi d_j phi + (1/2) m^2 N sqrt g phi^2 ]
site-centred fields N(z), g_ii(z);  x,y stiffness at sites, z stiffness on bonds (midpoint evaluation).
Sectors: TT (g_xx=1+a c, g_yy=1-a c), CONF (g_ij = psi^4 delta, psi = 1+a c), LAPSE (N=1+a c),
and mixed (N=1+a c, psi=1+a c) via 'NP'.  c = cos(k z), k = 2 pi/p.

Per-site energy eps(a); response A(k) = [eps(a)+eps(-a)-2 eps(0)]/(2 a^2)  (coefficient of a^2, cos-modulated).
Continuum EH (verified in test2a): TT: A = k^2/(64 pi G);  CONF: A = -k^2/(4 pi G);  NP: A_nn+A_np+A_pp with
A_nn = 0, A_np = A_pp = -k^2/(4 pi G).   Uniform response A_uni(a-uniform) compared with the covariant value.
"""
import numpy as np, sys, math, time

def fields(sector, a, zc, k):
    c = np.cos(k*zc)
    one = np.ones_like(zc)
    if sector == 'TT':
        N, gx, gy, gz = one, 1+a*c, 1-a*c, one
    elif sector == 'CONF':
        psi4 = (1+a*c)**4; N, gx, gy, gz = one, psi4, psi4, psi4
    elif sector == 'LAPSE':
        N, gx, gy, gz = 1+a*c, one, one, one
    elif sector == 'NP':
        psi4 = (1+a*c)**4; N, gx, gy, gz = 1+a*c, psi4, psi4, psi4
    else:
        raise ValueError(sector)
    return N, gx, gy, gz

def energy_per_site(sector, a, p, m, Nt, Nqz, uniform=False):
    """vacuum energy per site.  uniform: constant amplitude a (k=0) with p=1 supercell."""
    k = 0.0 if uniform else 2*np.pi/p
    zs = np.arange(p, dtype=float)
    N, gx, gy, gz = fields(sector, a, zs, k)
    sg = np.sqrt(gx*gy*gz)
    Msite = sg/N
    wx = N*sg/gx; wy = N*sg/gy
    ms = m*m*N*sg
    # z-bonds at midpoints (evaluate fields at z+1/2)
    Nb, gxb, gyb, gzb = fields(sector, a, zs+0.5, k)
    wz = Nb*np.sqrt(gxb*gyb*gzb)/gzb                 # bond s -> s+1 (mod p)
    q = 2*np.pi*(np.arange(Nt)+0.5)/Nt
    ax = 2-2*np.cos(q)                               # (Nt,)
    th = 2*np.pi*(np.arange(Nqz)+0.5)/Nqz - np.pi    # Bloch phase across the supercell, in (-pi,pi)
    # base matrix (p x p) without transverse and without closing phase
    base = np.zeros((p, p), complex)
    for s in range(p):
        base[s, s] += ms[s] + wz[s] + wz[s-1]
    for s in range(p-1):
        base[s, s+1] -= wz[s]; base[s+1, s] -= wz[s]
    # transverse diag: wx*ax[i] + wy*ax[j]
    diag_t = wx[None, None, :]*ax[:, None, None] + wy[None, None, :]*ax[None, :, None]   # (Nt,Nt,p)
    total = 0.0
    Minv = 1/np.sqrt(Msite)
    for t in th:
        Dm = np.broadcast_to(base, (Nt, Nt, p, p)).copy()
        idx = np.arange(p)
        Dm[:, :, idx, idx] += diag_t
        if p == 1:
            Dm[:, :, 0, 0] += 2*wz[0]*0 + (-wz[0]*2*np.cos(t)) + 0   # bond to itself with phase: -w e^{it} - w e^{-it}
            # base already has +2 wz on diag (wz[s]+wz[s-1]); phase term adds -2 wz cos t
        else:
            Dm[:, :, p-1, 0] += -wz[p-1]*np.exp(1j*t)
            Dm[:, :, 0, p-1] += -wz[p-1]*np.exp(-1j*t)
        Km = Dm*Minv[None, None, :, None]*Minv[None, None, None, :]
        ev = np.linalg.eigvalsh(Km)
        total += 0.5*np.sqrt(np.clip(ev, 0, None)).sum()
    return total/(Nt*Nt*Nqz*p)

def response(sector, p, m, Nt, Nqz, a=0.02, uniform=False):
    e0 = energy_per_site(sector, 0.0, p, m, Nt, Nqz, uniform)
    ep = energy_per_site(sector, +a, p, m, Nt, Nqz, uniform)
    em = energy_per_site(sector, -a, p, m, Nt, Nqz, uniform)
    return e0, (ep+em-2*e0)/(2*a*a)

if __name__ == "__main__":
    m = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
    Nt = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    Nqz = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    ps = [int(x) for x in (sys.argv[4].split(',') if len(sys.argv) > 4 else "8,12,16".split(','))]
    sectors = sys.argv[5].split(',') if len(sys.argv) > 5 else ['TT', 'CONF', 'LAPSE']
    print(f"m={m}  Nt={Nt}  Nqz={Nqz}  p={ps}  sectors={sectors}")
    for sec in sectors:
        e0u, Au = response(sec, 1, m, Nt, Nqz*8, uniform=True)
        print(f"[{sec}] uniform: rho0(per site)={e0u:.6f}  A_uni={Au:.6f}   A_uni/rho0={Au/e0u:.4f}")
        for p in ps:
            t0 = time.time()
            e0, A = response(sec, p, m, Nt, Nqz)
            k = 2*np.pi/p
            print(f"[{sec}] p={p:3d} k={k:.4f}  A_cos(k)={A:.6f}   (A_cos - A_uni/2)/k^2 = {(A-Au/2)/k**2:.6f}   [{time.time()-t0:.1f}s]", flush=True)
