"""R9-5 script 3b: convergence of the vison-sector energetics in the hopping truncation RMAX (vectorised;
bipartite: H = (i/2) sum M c_A c_B, so fermion levels = singular values of the N x N matrix Mab).
Prints: truncated-law gap, Delta E_vac for the local pair (D=1) and a far pair (D=12), the pi-flux
energy per plaquette, the lowest fermion level in each sector (bound states below the flux-free gap),
and the ground-state parity change (sign of det Mab(F)/det Mab(0): for a bipartite Majorana matrix,
Pf(A) = +-det(Mab), so the relative sign of det gives the relative vacuum parity)."""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r95_common import *
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()
Mfull, _ = hopping_M(512)
for (RMAX, L) in [(12, 40), (16, 48), (24, 64), (32, 80)]:
    offs = [(a, b) for a in range(-RMAX, RMAX+1) for b in range(-RMAX, RMAX+1)]
    zoff = [[(u[0], u[1]) for (u, v, t) in path((0, 0, 'A'), 'B', r)[1] if t == 'z'] for r in offs]
    N = L*L
    n1, n2 = np.meshgrid(np.arange(L), np.arange(L), indexing='ij'); n1 = n1.ravel(); n2 = n2.ravel()
    I = n1*L + n2
    def build(Fgrid):
        Mab = np.zeros((N, N))
        for r, zs in zip(offs, zoff):
            m_ = Mfull[r[0] % 512, r[1] % 512]
            sg = np.ones(N)
            for (o1, o2) in zs:
                sg *= 1 - 2*Fgrid[(n1+o1) % L, (n2+o2) % L]
            J = ((n1+r[0]) % L)*L + (n2+r[1]) % L
            Mab[I, J] += sg*m_
        return Mab
    def levels(Mab): return np.linalg.svd(Mab, compute_uv=False)
    F0 = np.zeros((L, L)); Mab0 = build(F0); sv0 = levels(Mab0); E0 = -0.5*sv0.sum(); gap0 = sv0.min()
    s0, ld0 = np.linalg.slogdet(Mab0)
    D0 = (L//2, L//2)
    line = 'RMAX=%2d L=%2d: flux-free gap %.5f (m = 0.3);' % (RMAX, L, gap0)
    for D in [1, 12]:
        F = np.zeros((L, L))
        for j in range(D): F[(D0[0]+j) % L, (D0[1]+j) % L] = 1
        Mab = build(F); sv = levels(Mab); s1, _ = np.linalg.slogdet(Mab)
        line += ' D=%d: dE_vac=%+.5f, lowest level %.5f, parity flip %s;' % (D, -0.5*sv.sum() - E0, sv.min(), 'yes' if s1*s0 < 0 else 'no')
    Fpi = np.zeros((L, L)); Fpi[0::2, :] = 1
    Mab = build(Fpi); sv = levels(Mab)
    line += ' pi-flux: dE/plaquette=%+.6f, gap %.4f' % ((-0.5*sv.sum() - E0)/N, sv.min())
    pr(line + '  [%.0f s]' % (time.time() - t0))
pr('runtime %.1f s' % (time.time() - t0))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
