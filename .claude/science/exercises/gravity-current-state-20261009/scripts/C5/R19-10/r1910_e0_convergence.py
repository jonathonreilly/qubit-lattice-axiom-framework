"""R19-10 probe (a): e0(L) = E0/V for free lattice fields on growing tori, finite-size corrections, and the
L -> L+1 plane increment.  Lattice units a = c = hbar = 1.
Fields (free, Gaussian):
  S(m)  : real NN scalar, eps^2 = m^2 + sum_i 4 sin^2(k_i/2); E0 = (1/2) sum_k eps_k.
  D(m)  : 4-component Wilson-Dirac, r = 1, omega^2 = sum sin^2 k_i + (m + sum(1 - cos k_i))^2; filled sea
          E0 = -2 sum_k omega_k (each k: two negative levels -omega).  Periodic (P) and antiperiodic (AP) BCs.
  A     : noncompact lattice Maxwell, H = (1/2) sum E_l^2 + (1/2) sum_p B_p^2.  E0 = (1/2) sum over nonzero
          eigenvalues of the curl-curl operator; checked here by explicit construction at L = 3, 4 to equal
          2 x S(0) (two transverse polarisations, omega^2 = sum 4 sin^2(k_i/2)); k = 0 holonomies contribute 0.
Control: Dirichlet (open) box for S(m): shows a surface term ~1/L that a torus (or infinite lattice) does not have.
Increment test: dE(L) = E0(L+1, L, L) - E0(L, L, L) against e0 * L^2 (one inserted plane of L^2 sites).
"""
import numpy as np, time
T0 = time.time()

def kgrid(L, bc):
    n = np.arange(L)
    return 2*np.pi*(n + (0.5 if bc == 'AP' else 0.0))/L

def E0_box(field, m, Ls, bc='P'):
    kx, ky, kz = [kgrid(L, bc) for L in Ls]
    if field == 'S' or field == 'A':
        sx, sy, sz = [4*np.sin(k/2)**2 for k in (kx, ky, kz)]
        e2 = m*m + sx[:, None, None] + sy[None, :, None] + sz[None, None, :]
        e = np.sqrt(np.maximum(e2, 0.0))
        return (0.5 if field == 'S' else 1.0)*e.sum()
    if field == 'D':
        s2 = [np.sin(k)**2 for k in (kx, ky, kz)]
        c1 = [1 - np.cos(k) for k in (kx, ky, kz)]
        M = m + c1[0][:, None, None] + c1[1][None, :, None] + c1[2][None, None, :]
        w = np.sqrt(s2[0][:, None, None] + s2[1][None, :, None] + s2[2][None, None, :] + M*M)
        return -2.0*w.sum()

def E0_dirichlet(m, L):
    k = np.pi*np.arange(1, L+1)/(L+1)
    s = 4*np.sin(k/2)**2
    e = np.sqrt(m*m + s[:, None, None] + s[None, :, None] + s[None, None, :])
    return 0.5*e.sum()

out = []
def pr(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); out.append(s)

# ---- photon check: explicit curl-curl operator on L^3 torus -------------------------------------------
def maxwell_E0(L):
    N = L**3
    idx = lambda x, y, z: ((x % L)*L + (y % L))*L + (z % L)
    link = lambda s, mu: 3*s + mu          # link from site s in direction mu
    rows = []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                s = idx(x, y, z); r = [x, y, z]
                for mu in range(3):
                    for nu in range(mu+1, 3):
                        rmu = list(r); rmu[mu] += 1
                        rnu = list(r); rnu[nu] += 1
                        row = np.zeros(3*N)
                        row[link(s, mu)] += 1; row[link(idx(*rmu), nu)] += 1
                        row[link(idx(*rnu), mu)] -= 1; row[link(s, nu)] -= 1
                        rows.append(row)
    C = np.array(rows)                      # plaquette x link
    M = C.T @ C                             # curl-curl on links
    ev = np.linalg.eigvalsh(M)
    ev = ev[ev > 1e-9]
    return 0.5*np.sqrt(ev).sum(), len(ev)

pr('=== photon: explicit noncompact lattice Maxwell zero point vs 2 x massless NN scalar (torus) ===')
for L in (3, 4):
    eM, nnz = maxwell_E0(L)
    eS2 = E0_box('A', 0.0, (L, L, L))
    pr('  L=%d: Maxwell E0 = %.12f (nonzero modes %d = 2(L^3-1) = %d) ; 2 x S(0) = %.12f ; diff %.1e'
       % (L, eM, nnz, 2*(L**3-1), eS2, eM - eS2))

# ---- e0(L) on tori ---------------------------------------------------------------------------------------
cases = [('S', 0.0, 'P'), ('S', 0.1, 'P'), ('S', 1.0, 'P'), ('A', 0.0, 'P'),
         ('D', 0.0, 'P'), ('D', 0.0, 'AP'), ('D', 0.1, 'AP'), ('D', 1.0, 'AP')]
Llist = [4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128]
pr('=== e0(L) = E0/L^3 on L^3 tori; d(L) = e0(L) - e0(128); L^4 d(L) is constant for a Casimir ~L^-4 term ===')
ref = {}
for f, m, bc in cases:
    vals = {L: E0_box(f, m, (L, L, L), bc)/L**3 for L in Llist}
    ref[(f, m, bc)] = vals
    e_inf = vals[128]
    pr('%s m=%.1f %s: e0(128) = %.12f' % (f, m, bc, e_inf))
    line = []
    for L in Llist[:-1]:
        d = vals[L] - e_inf
        line.append('L=%d d=%.3e L^4d=%.4f' % (L, d, d*L**4))
    for i in range(0, len(line), 4):
        pr('    ' + ' | '.join(line[i:i+4]))

# ---- L -> L+1 plane increment ------------------------------------------------------------------------------
pr('=== plane insertion L -> L+1 on a torus: (dE - e0 L^2)/L^2 = per-inserted-site deviation from e0 ===')
for f, m, bc in cases:
    e_inf = ref[(f, m, bc)][128]
    line = []
    for L in [8, 16, 32, 64, 96]:
        dE = E0_box(f, m, (L+1, L, L), bc) - E0_box(f, m, (L, L, L), bc)
        dev = (dE - e_inf*L*L)/(L*L)
        line.append('L=%d dev=%.3e L^4dev=%.3f' % (L, dev, dev*L**4))
    pr('%s m=%.1f %s: ' % (f, m, bc) + ' | '.join(line))
pr('  (AP Dirac with odd L+1: antiperiodic momenta on an odd ring; the deviation is still ~L^-4.)')

# ---- open box control ---------------------------------------------------------------------------------------
pr('=== control: Dirichlet (open) box, S(m): surface term ~1/L (absent on a torus or infinite lattice) ===')
for m in (0.0, 1.0):
    e_inf = ref[('S', m, 'P')][128]
    line = []
    for L in [8, 16, 32, 64, 128]:
        d = E0_dirichlet(m, L)/L**3 - e_inf
        line.append('L=%d d=%.4e L*d=%.4f' % (L, d, d*L))
    pr('S m=%.1f Dirichlet: ' % m + ' | '.join(line))

# ---- physical size of the finite-size term at a = l_P ----------------------------------------------------------
H0 = 67.4/3.0857e19*5.391e-44          # H0 in Planck units (t_P = 5.391e-44 s), RECALLED inputs
rhoL = 0.685*3*H0**2/(8*np.pi)         # rho_Lambda in Planck units (G = 1, a = l_P)
pr('=== sizes at a = l_P (Planck units; H0 = 67.4 km/s/Mpc, Omega_L = 0.685, RECALLED) ===')
pr('  H0 = %.4e, rho_Lambda = %.4e' % (H0, rhoL))
Lh = 1/H0
for f, m, bc, c4 in [('S', 0.0, 'P', None), ('A', 0.0, 'P', None), ('D', 0.0, 'AP', None)]:
    v = ref[(f, m, bc)]; c4 = (v[64] - v[128])*64**4/(1 - (64/128)**4)
    pr('  %s m=%.1f %s: Casimir coefficient c4 ~ %.4f ; at L = 1/H0 = %.2e sites: c4/L^4 = %.1e = %.1e rho_Lambda'
       % (f, m, bc, c4, Lh, c4/Lh**4, c4/Lh**4/rhoL))
pr('  d/dt of that term: 4 H c4/L^4 per unit time -> drift per Hubble time ~ %.1e rho_Lambda' % (4*abs(c4)/Lh**4/rhoL))
pr('elapsed %.1f s' % (time.time() - T0))
