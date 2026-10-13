"""R19-10 probe (b): energy above the new ground state after inserting sites in a product state.
Lattice units (a = c = hbar = 1).  Exact Gaussian (quasi-free) bookkeeping.
Geometry:
  1D: ring of N sites -> N+1, the new site n placed between sites N-1 and 0 (bond (N-1,0) replaced by (N-1,n),(n,0)).
  3D: plane insertion on an Lx x Lp x Lp torus (antiperiodic in y,z so no zero mode), Lx -> Lx+1.  Transverse
      momentum k_perp is conserved, so the problem splits into Lp^2 one-dimensional ring insertions with
      M^2 = m^2 + 4 sin^2(ky/2) + 4 sin^2(kz/2) (scalar) or h0(k_perp) (Wilson-Dirac).  Per inserted site =
      average over sectors.
Rules for the new site (old sites stay in the old ground state):
  P-loc : the new site's local ground state = the BEST product state (proved below: for quadratic H, cross terms
          vanish on a product with zero means, so only the on-site block matters).  Scalar: omega_loc^2 = <K_nn>
          (= m^2 + 2 in 1D, m^2 + 6 in 3D).  Dirac: fill the negative eigenvectors of <h0> = beta (m + 3r).
  P-fix : a fixed product state independent of the law.  Scalar: Gaussian with omega_ref = 1.  Dirac: fill the
          negative eigenvectors of alpha_x (half filling, law-independent).
  P-plane (3D scalar only, less local): the new plane enters in its own 2D ground state (k_perp-dependent width).
dE = <H_new>_product - E0(H_new) >= 0 (variational).  Injected energy density per e-fold = 3 dE / a^4 (three new
sites per old site per e-fold, L-CR mean rate 3H); compared with rho_Lambda at a = l_P.
"""
import numpy as np, time
T0 = time.time()
out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

H0 = 67.4/3.0857e19*5.391e-44; rhoL = 0.685*3*H0**2/(8*np.pi)      # Planck units, RECALLED inputs

def ring_K(N, M2, insert=False):
    """K for a ring of N sites (insert=False) or N+1 sites with the new site last (index N) between N-1 and 0."""
    n = N + (1 if insert else 0)
    K = np.diag(np.full(n, M2 + 2.0))
    order = list(range(N)) + ([N] if insert else [])
    for a, b in zip(order, order[1:] + order[:1]):
        K[a, b] -= 1; K[b, a] -= 1
    return K

def msqrt(K):
    w, V = np.linalg.eigh(K)
    return (V*np.sqrt(w)) @ V.T, (V/np.sqrt(w)) @ V.T, w

def scalar_dE(N, M2, s_new):
    """Excess energy of (old GS) x (new site Gaussian with <phi^2> = s_new) under the new ring Hamiltonian."""
    Ko = ring_K(N, M2); sq, isq, _ = msqrt(Ko)
    Phi = np.zeros((N+1, N+1)); Pi = np.zeros((N+1, N+1))
    Phi[:N, :N] = 0.5*isq; Pi[:N, :N] = 0.5*sq
    Phi[N, N] = s_new; Pi[N, N] = 1/(4*s_new)
    Kn = ring_K(N, M2, insert=True)
    E = 0.5*np.trace(Pi) + 0.5*np.trace(Kn @ Phi)
    E0n = 0.5*np.sqrt(np.linalg.eigvalsh(Kn)).sum()
    E0o = 0.5*np.sqrt(np.linalg.eigvalsh(Ko)).sum()
    return E - E0n, E0n - E0o

# Dirac matrices (Dirac rep.)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.array([[1, 0], [0, -1]], complex)
Z2 = np.zeros((2, 2)); I2 = np.eye(2)
al = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
be = np.block([[I2, Z2], [Z2, -I2]]).astype(complex)

def dirac_ring(N, h0, T, insert=False):
    n = N + (1 if insert else 0)
    H = np.zeros((4*n, 4*n), complex)
    order = list(range(N)) + ([N] if insert else [])
    for a in order:
        H[4*a:4*a+4, 4*a:4*a+4] = h0
    for a, b in zip(order, order[1:] + order[:1]):
        H[4*a:4*a+4, 4*b:4*b+4] += T
        H[4*b:4*b+4, 4*a:4*a+4] += T.conj().T
    return H

def negproj(H):
    w, V = np.linalg.eigh(H)
    Vn = V[:, w < 0]
    return Vn @ Vn.conj().T, w[w < 0].sum()

def dirac_dE(N, h0, T, Psite):
    Ho = dirac_ring(N, h0, T); Go, E0o = negproj(Ho)
    Hn = dirac_ring(N, h0, T, insert=True)
    G = np.zeros_like(Hn); G[:4*N, :4*N] = Go; G[4*N:, 4*N:] = Psite
    E = np.real(np.trace(Hn @ G))
    E0n = np.linalg.eigvalsh(Hn); E0n = E0n[E0n < 0].sum()
    return E - E0n, E0n - E0o

pr('=== 1D ring, point insertion, scalar (old ring N sites) ===')
for m in (0.05, 0.3, 1.0):
    for N in (64, 128, 256):
        wl = np.sqrt(m*m + 2)
        dl, inc = scalar_dE(N, m*m, 1/(2*wl))
        df, _ = scalar_dE(N, m*m, 1/(2*1.0))
        pr('  m=%.2f N=%d: dE(P-loc, omega_loc=%.4f) = %.6f ; dE(P-fix, omega_ref=1) = %.6f ; E0 increment = %.6f'
           % (m, N, wl, dl, df, inc))
pr('  check P-fix - P-loc = (omega_ref - omega_loc)^2/(4 omega_ref):', '%.6f' % ((1 - np.sqrt(0.05**2+2))**2/4))

pr('=== 3D plane insertion, scalar, per inserted site (Lx -> Lx+1, Lp x Lp antiperiodic transverse) ===')
Lx = 48
res3 = {}
for m in (0.0, 0.1, 1.0):
    for Lp in (8, 16):
        kp = 2*np.pi*(np.arange(Lp) + 0.5)/Lp
        wl = np.sqrt(m*m + 6)
        acc = dict(loc=0., fix=0., plane=0., inc=0.)
        cache = {}
        for ky in kp:
            for kz in kp:
                M2 = m*m + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2
                key = round(M2, 12)
                if key not in cache:
                    a, inc = scalar_dE(Lx, M2, 1/(2*wl))
                    b, _ = scalar_dE(Lx, M2, 0.5)
                    c, _ = scalar_dE(Lx, M2, 1/(2*np.sqrt(M2 + 2)))
                    cache[key] = (a, b, c, inc)
                a, b, c, inc = cache[key]
                acc['loc'] += a; acc['fix'] += b; acc['plane'] += c; acc['inc'] += inc
        for k in acc: acc[k] /= Lp*Lp
        res3[(m, Lp)] = acc
        pr('  m=%.1f Lp=%d: dE/site: P-loc (omega_loc=%.4f) = %.6f ; P-fix = %.6f ; P-plane (2D-GS plane) = %.6f ; E0 increment/site = %.6f'
           % (m, Lp, wl, acc['loc'], acc['fix'], acc['plane'], acc['inc']))

pr('=== 3D plane insertion, Wilson-Dirac (r = 1), per inserted site ===')
r = 1.0
Tx = al[0]/(2j) - 0.5*r*be
resD = {}
for m in (0.0, 0.1, 1.0):
    Lp = 8; Lxd = 32
    kp = 2*np.pi*(np.arange(Lp) + 0.5)/Lp
    hbar = be*(m + 3*r)
    w, V = np.linalg.eigh(hbar); Ploc = V[:, w < 0] @ V[:, w < 0].conj().T
    w2, V2 = np.linalg.eigh(al[0]); Pfix = V2[:, w2 < 0] @ V2[:, w2 < 0].conj().T
    acc = dict(loc=0., fix=0., inc=0.)
    for ky in kp:
        for kz in kp:
            h0 = be*(m + r*(2 - np.cos(ky) - np.cos(kz)) + r) + al[1]*np.sin(ky) + al[2]*np.sin(kz)
            a, inc = dirac_dE(Lxd, h0, Tx, Ploc)
            b, _ = dirac_dE(Lxd, h0, Tx, Pfix)
            acc['loc'] += a; acc['fix'] += b; acc['inc'] += inc
    for k in acc: acc[k] /= Lp*Lp
    resD[m] = acc
    pr('  m=%.1f Lp=%d Lx=%d: dE/site: P-loc = %.6f ; P-fix (alpha_x half filling) = %.6f ; E0 increment/site = %.6f'
       % (m, Lp, Lxd, acc['loc'], acc['fix'], acc['inc']))

pr('=== injected energy per e-fold (= per Hubble time at H = const), P-loc (best product), a = l_P ===')
pr('  rho_Lambda = %.4e (Planck units)' % rhoL)
for (m, Lp), acc in res3.items():
    if Lp == 16:
        pr('  scalar m=%.1f: 3 dE = %.4e -> %.2e rho_Lambda per Hubble time' % (m, 3*acc['loc'], 3*acc['loc']/rhoL))
for m, acc in resD.items():
    pr('  Wilson-Dirac m=%.1f: 3 dE = %.4e -> %.2e rho_Lambda per Hubble time' % (m, 3*acc['loc'], 3*acc['loc']/rhoL))
pr('  photon (transverse content = 2 massless scalars; Gauss-law bookkeeping NOT built): 3 dE ~ %.4e -> %.2e rho_Lambda'
   % (6*res3[(0.0, 16)]['loc'], 6*res3[(0.0, 16)]['loc']/rhoL))
pr('elapsed %.1f s' % (time.time() - T0))
