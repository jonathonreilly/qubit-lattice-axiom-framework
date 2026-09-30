"""T22 test C: does the chiral (tails) tick pump quasi-energy in a magnetic field?
Winding of det V(k_z) over k_z in [0,2pi) for a 12x12 torus with flux 2pi/12 per plaquette (N_phi=12).
 - tails tick: polar factor of the |n_j|<=2 Fourier truncation of q_g = (c_x c_y c_z, g s)  (W3=4, probe 2 T4)
 - control 1: ordered strictly local tick S_x S_y S_z, each conditional shift dressed separately (exactly unitary)
 - control 2: the flowing (Hamiltonian) walker's own unitary exp(-i H), H = sum sin k_j sigma_j, via the polar factor
              of its range-1 truncation is not used; instead control 2 = straight-line-dressed expansion of the
              ordered tick polynomial, then polar factor.
"""
import numpy as np, sys
L = 12; Nphi = 12; B = 2*np.pi*Nphi/(L*L)   # flux per plaquette 2 pi/12
sig = [np.array([[0,1],[1,0]],complex), np.array([[0,-1j],[1j,0]]), np.array([[1,0],[0,-1]],complex)]
I2 = np.eye(2, dtype=complex)

def fourier_coeffs(N=48, R=2):
    k = 2*np.pi*np.arange(N)/N
    kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
    cx, cy, cz = np.cos(kx), np.cos(ky), np.cos(kz)
    sx, sy, sz = np.sin(kx), np.sin(ky), np.sin(kz)
    a = cx*cy*cz
    s2 = sx**2 + sy**2 + sz**2
    g = np.where(s2 > 1e-14, np.sqrt(np.clip((1 - a**2), 0, None)/np.where(s2 > 1e-14, s2, 1)), 1.0)
    comps = [a, g*sx, g*sy, g*sz]
    coef = {}
    for mu, f in enumerate(comps):
        F = np.fft.fftn(f)/N**3            # f(k) = sum_n F[n] e^{+ i k n}?  fftn uses e^{-i}, so f = sum F_n e^{+i k n}
        for nx in range(-R, R+1):
            for ny in range(-R, R+1):
                for nz in range(-R, R+1):
                    coef.setdefault((nx,ny,nz), np.zeros(4, complex))[mu] = F[nx % N, ny % N, nz % N]
    # sanity: truncated reconstruction on a coarse set, W-independent checks
    return coef

def hop_matrices(coef):
    """M_n = c0 - i sum_i c_i sigma_i ; Q(k) = sum_n M_n e^{i k n}."""
    return {n: c[0]*I2 - 1j*sum(c[i+1]*sig[i] for i in range(3)) for n, c in coef.items()}

def build_Q(M, kz):
    D = 2*L*L
    Q = np.zeros((D, D), complex)
    # collapse z
    Mxy = {}
    for (nx,ny,nz), m in M.items():
        Mxy.setdefault((nx,ny), np.zeros((2,2), complex))
        Mxy[(nx,ny)] += m*np.exp(1j*kz*nz)
    for x in range(L):
        for y in range(L):
            r = x*L + y
            for (nx,ny), m in Mxy.items():
                if np.abs(m).max() < 1e-13: continue
                xp, yp = (x+nx) % L, (y+ny) % L
                rp = xp*L + yp
                ph = np.exp(1j*B*ny*(x + nx/2))
                Q[2*r:2*r+2, 2*rp:2*rp+2] += m*ph
    return Q

def polar(Q):
    u, s, vh = np.linalg.svd(Q)
    return u @ vh, s

def winding(Vfun, nk=48):
    ks = 2*np.pi*np.arange(nk+1)/nk
    ang = []
    for kz in ks:
        V = Vfun(kz)
        sign, logdet = np.linalg.slogdet(V)
        ang.append(np.angle(sign))
    ang = np.unwrap(np.array(ang))
    return (ang[-1]-ang[0])/(2*np.pi)

def shift_op(axis, kz=None):
    """conditional shift S_j = (1-sigma_j)/2 T_j + (1+sigma_j)/2 T_j^dagger on the torus with Peierls in y (A_y = B x)."""
    D = 2*L*L
    S = np.zeros((D, D), complex)
    P = [(I2 - sig[axis])/2, (I2 + sig[axis])/2]
    for x in range(L):
        for y in range(L):
            r = x*L + y
            for sgn, Pm in zip((+1, -1), P):
                nx = sgn if axis == 0 else 0
                ny = sgn if axis == 1 else 0
                xp, yp = (x+nx) % L, (y+ny) % L
                rp = xp*L + yp
                ph = np.exp(1j*B*ny*(x + nx/2))
                S[2*r:2*r+2, 2*rp:2*rp+2] += Pm*ph
    return S

def Sz_kz(kz):
    Pm = [(I2 - sig[2])/2, (I2 + sig[2])/2]
    m = Pm[0]*np.exp(1j*kz) + Pm[1]*np.exp(-1j*kz)
    return np.kron(np.eye(L*L), m)

if __name__ == "__main__":
    coef = fourier_coeffs()
    M = hop_matrices(coef)
    print("Fourier coefficients: truncation box |n_j|<=2,", len(M), "hops; max |M_n| =", max(np.abs(m).max() for m in M.values()))
    # check smallness of imaginary parts (q real => c_{-n}=conj c_n)
    # norm check on a random k
    rng = np.random.default_rng(1)
    for _ in range(3):
        kk = rng.uniform(0, 2*np.pi, 3)
        Qk = sum(m*np.exp(1j*np.dot(n, kk)) for n, m in M.items())
        print("  |q_tr(k)| =", np.sqrt(abs(np.linalg.det(Qk))))
    # ---- tails tick
    def V_tails(kz):
        Q = build_Q(M, kz)
        V, s = polar(Q)
        return V
    # spectrum check at kz=0: unitarity residual and smallest singular value
    Q0 = build_Q(M, 0.0); V0, s0 = polar(Q0)
    print("tails tick: min/max singular value of dressed truncation at kz=0:", s0.min(), s0.max())
    w_tails = winding(V_tails, nk=48)
    print("winding of det V(kz), tails tick:", w_tails, " (per flux quantum:", w_tails/Nphi, ")")
    # ---- control 1: ordered tick
    Sx = shift_op(0); Sy = shift_op(1)
    def V_ord(kz):
        return Sx @ Sy @ Sz_kz(kz)
    Vo = V_ord(0.7)
    print("control 1 unitarity residual:", np.abs(Vo.conj().T @ Vo - np.eye(Vo.shape[0])).max())
    w_ord = winding(V_ord, nk=24)
    print("winding of det V(kz), ordered tick (exactly local):", w_ord)
    # ---- control 2: straight-line dressed expansion of ordered polynomial, then polar
    # ordered polynomial coefficients from the same FFT machinery
    N = 8; k = 2*np.pi*np.arange(N)/N
    kx, ky, kz_ = np.meshgrid(k, k, k, indexing='ij')
    def Sj(q, j): return np.cos(q)[..., None, None]*I2 - 1j*np.sin(q)[..., None, None]*sig[j]
    U = np.einsum('...ab,...bc,...cd->...ad', Sj(kx,0), Sj(ky,1), Sj(kz_,2))
    Mo = {}
    for nx in range(-1,2):
        for ny in range(-1,2):
            for nz in range(-1,2):
                ph = np.exp(-1j*(nx*kx + ny*ky + nz*kz_))
                Mo[(nx,ny,nz)] = np.einsum('xyz,xyzab->ab', ph, U)/N**3
    def V_ord2(kz):
        Q = build_Q(Mo, kz)
        return polar(Q)[0]
    w_ord2 = winding(V_ord2, nk=24)
    print("winding of det V(kz), ordered tick via straight-line dressing + polar:", w_ord2)
