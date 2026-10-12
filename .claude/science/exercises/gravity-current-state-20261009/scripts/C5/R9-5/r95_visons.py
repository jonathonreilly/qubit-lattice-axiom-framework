"""R9-5 script 3: the complementary (vison) sectors of the actual spin law H_spin (not the bare Kitaev H_K).

In every flux sector H_spin is quadratic in the c-Majoranas: flipping the gauge field u on a set F of
z-bonds flips the sign of every AB string whose fixed path crosses an odd number of F bonds.
  (i)   vison-pair energies: fermion-vacuum shift E_vac(F) - E_vac(0) on an L x L dimer torus
        (hopping truncated at |r|_inf <= RMAX; the truncation is stated), for a local pair (one sigma^z)
        and for pairs separated by D plaquettes (single-vison energy = large-D limit / 2);
        plus 2 Delta_v per vison from the optional plaquette term -Delta_v sum_p W_p.
  (ii)  in-gap (bound) fermion states at the pair; parity of the sector vacuum (zero-crossing scan).
  (iii) the pi-flux-everywhere sector energy per plaquette (is flux-free the ground sector at Delta_v = 0?).
  (iv)  exact one-fermion on-shell T-matrix off the local vison pair, infinite volume (BZ quadrature
        Green function), for BOX momenta, non-forward.  Lemma S (R7-3, refereed) then excludes an
        additive momentum in that sector.
Visons are exactly static: every term of H_spin is a product of Kitaev bond operators, each of which
commutes with every W_p (proved; checked in r95_signed_ed)."""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()
Mfull, _ = hopping_M(512)
def Mof(r): return Mfull[r[0] % 512, r[1] % 512]

RMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 12
L = int(sys.argv[2]) if len(sys.argv) > 2 else 40
offs = [(a, b) for a in range(-RMAX, RMAX+1) for b in range(-RMAX, RMAX+1)]
Mv = np.array([Mof(r) for r in offs])
# z-bonds traversed by the AB path A_R -> B_{R+r}: dimer offsets relative to R
zoff = []
for r in offs:
    st, bd = path((0, 0, 'A'), 'B', r)
    zs = [(u[0], u[1]) for (u, v, t) in bd if t == 'z']
    zoff.append(zs)
# truncated dispersion and its deviation from eps on the box
k = 2*np.pi*np.arange(L)/L
K1, K2 = np.meshgrid(k, k, indexing='ij')
eps_tr = np.zeros_like(K1)
for r, m_ in zip(offs, Mv): eps_tr += m_*np.cos(K1*r[0] + K2*r[1])
pr('law truncated at |r|_inf <= %d on an L=%d dimer torus; max|eps_trunc - eps| on the k-grid = %.2e; min eps_trunc = %.4f'
   % (RMAX, L, np.max(np.abs(eps_tr - eps(K1, K2))), eps_tr.min()))
N = L*L
def dimer_index(n1, n2): return (n1 % L)*L + (n2 % L)
def build_A(F):
    """Majorana matrix A (2N x 2N): index 2*d = A-site, 2*d+1 = B-site of dimer d. F = set of flipped z dimers."""
    A = np.zeros((2*N, 2*N))
    Fset = set((a % L, b % L) for (a, b) in F)
    for n1 in range(L):
        for n2 in range(L):
            i = 2*dimer_index(n1, n2)
            for r, m_, zs in zip(offs, Mv, zoff):
                sgn = 1.0
                if Fset:
                    for (o1, o2) in zs:
                        if ((n1+o1) % L, (n2+o2) % L) in Fset: sgn = -sgn
                j = 2*dimer_index(n1+r[0], n2+r[1]) + 1
                A[i, j] += sgn*m_; A[j, i] -= sgn*m_
    return A
def spectrum(A):
    return np.linalg.eigvalsh(1j*A)          # +-eps_n
def Evac(ev): return -0.5*np.sum(ev[ev > 0])

A0 = build_A([]); ev0 = spectrum(A0); E0 = Evac(ev0)
pr('flux-free: E_vac = %.6f (k-grid prediction -1/2 sum eps_trunc = %.6f); gap = %.4f' % (E0, -0.5*eps_tr.sum(), ev0[ev0 > 0].min()))
D0 = (L//2, L//2)
res = {}
for D in [1, 2, 3, 4, 6, 8, 10, 12]:
    F = [(D0[0]+j, D0[1]+j) for j in range(D)]
    ev = spectrum(build_A(F)); dE = Evac(ev) - E0
    pos = ev[ev > 0]
    res[D] = dE
    pr('vison pair separated by D=%2d plaquettes (flip z on %d dimers along e1+e2): Delta E_vac = %+.6f ; lowest fermion level %.5f (bulk gap %.4f); in-gap levels: %d'
       % (D, D, dE, pos.min(), MASS, int(np.sum(pos < MASS - 1e-6))))
pr('single-vison fermion energy e_v ~ Delta E_vac(D=12)/2 = %.5f ; local pair (one sigma^z) = %.5f' % (res[12]/2, res[1]))
# parity of the local-pair sector vacuum: scan A(t) = A0 + t (A_F - A0) for a zero crossing
AF = build_A([D0]); mins = []
for t in np.linspace(0, 1, 11):
    e = spectrum(A0 + t*(AF - A0)); mins.append(np.min(np.abs(e)))
pr('local pair: min_t |eps| along A0 -> A_F (11 points) = %.4f  (no zero crossing => sector vacuum has the flux-free vacuum parity)' % min(mins))
# pi flux in every plaquette: flip z on all dimers with n1 even
Fpi = [(a, b) for a in range(0, L, 2) for b in range(L)]
evpi = spectrum(build_A(Fpi))
pr('pi-flux sector (every plaquette flipped): (E_vac(pi) - E_vac(0)) per plaquette = %+.6f' % ((Evac(evpi) - E0)/N))

# ---------------- (iv) exact on-shell T-matrix off the local vison pair (infinite volume) ----------------
dA = AF - A0
# support of dA around D0, as dimer offsets
rows = np.where(np.abs(dA).sum(axis=1) > 0)[0]
pr('local pair: dA has %d nonzero rows (Majorana sites), max |dA| = %.3f, ||dA||_F = %.3f' % (len(rows), np.abs(dA).max(), np.linalg.norm(dA)))
def site_pos(i):
    d, sb = divmod(i, 2); n1, n2 = divmod(d, L)
    o1 = (n1 - D0[0] + L//2) % L - L//2; o2 = (n2 - D0[1] + L//2) % L - L//2
    return o1, o2, sb
pos = [site_pos(i) for i in rows]
dh = 1j*dA[np.ix_(rows, rows)]
def G0_region(z, Nk):
    kq = 2*np.pi*np.fft.fftfreq(Nk)
    Q1, Q2 = np.meshgrid(kq, kq, indexing='ij')
    e = eps(Q1, Q2)
    den = z*z - e*e
    gAA = np.fft.ifft2(z/den)          # (1/Nk^2) sum_k e^{+ik R} ...
    gAB = np.fft.ifft2(1j*e/den)
    gBA = np.fft.ifft2(-1j*e/den)
    n = len(pos); G = np.zeros((n, n), complex)
    P = np.array(pos)
    for a in range(n):
        d1 = (P[a, 0] - P[:, 0]) % Nk; d2 = (P[a, 1] - P[:, 1]) % Nk
        sa = P[a, 2]
        for sb_ in (0, 1):
            mask = P[:, 2] == sb_
            g = gAA if sa == sb_ else (gAB if sa == 0 else gBA)
            G[a, mask] = g[d1[mask], d2[mask]]
    return G
psi_plus = np.array([1.0, -1j])/np.sqrt(2)
def wave(kv):
    P = np.array(pos)
    return np.exp(1j*(P[:, 0]*kv[0] + P[:, 1]*kv[1]))*psi_plus[P[:, 2]]
kin = np.array([0.5, 0.2]); Ein = eps(*kin)
outs = {'rotated 90deg': np.array([-0.2, 0.5]), 'backward': -kin, 'mirror': np.array([0.2, 0.5]), 'rotated 45deg': np.array([np.cos(np.pi/4)*0.5 - np.sin(np.pi/4)*0.2, np.sin(np.pi/4)*0.5 + np.cos(np.pi/4)*0.2]), 'forward': kin}
pr('box in-momentum k = (%.2f, %.2f), E = %.5f (|k| = %.4f, deep in the box |k_i| < %.1f); all out-momenta on shell: %s'
   % (kin[0], kin[1], Ein, np.linalg.norm(kin), Bbox, ', '.join('%.1e' % abs(eps(*v) - Ein) for v in outs.values())))
for Nk, eta in [(512, 0.02), (1024, 0.01), (1024, 0.005)]:
    G = G0_region(Ein + 1j*eta, Nk)
    T = dh @ np.linalg.inv(np.eye(len(pos)) - G @ dh)
    vin = wave(kin)
    line = []
    for name, kv in outs.items():
        vout = wave(kv)
        line.append('%s |t|=%.4f (Born %.4f)' % (name, abs(vout.conj() @ T @ vin), abs(vout.conj() @ dh @ vin)))
    pr('  Nk=%d eta=%.3f: ' % (Nk, eta) + '; '.join(line))
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '_R%d_L%d.out' % (RMAX, L)), 'w').write('\n'.join(out) + '\n')
