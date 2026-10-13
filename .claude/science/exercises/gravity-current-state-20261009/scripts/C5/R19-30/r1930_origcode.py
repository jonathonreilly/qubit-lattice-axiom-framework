"""R19-30 probe (a)/(b) on the ORIGINAL code (unmodified copies), so the defect is not an artefact of my re-implementation.
 (i)  R13-5's r135_w1_pair.pair_kernel (the scalar U pair completion R19-5 cites), d = 3, profile G, m = 0.3:
      site-label kernel F^{mu nu}(k1, k2), k1 + k2 = q, compared at the two sides of the cut q_x = +-pi (same torus point).
 (ii) R19-5's Dirac construction (r195_dirac_exact.near + r195_dirac_exact2.far/glued, copied verbatim; archived
      tabulated D1 law): full kernel and scattering-only kernel (UD -> 0) across q_x = +-pi.
 (iii) R13-5's own locality test (6) is in d = 1, where no off-diagonal component exists (stated, shown by its code)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
# ---- (i) R13-5 ----
src = open(os.path.join(HERE, 'r135copy', 'r135_w1_pair.py')).read()
src = src.split("def w1_res")[0].replace("sys.path.insert(0, __file__.rsplit('/', 1)[0])", "sys.path.insert(0, %r)" % os.path.join(HERE, 'r135copy'))
ns = {}; exec(compile(src, 'r135_w1_pair_head', 'exec'), ns)
pair_kernel = ns['pair_kernel']
rng = np.random.default_rng(193007)
print('(i) R13-5 pair_kernel (unmodified), member U, profile G, m = 0.3, d = 3: jump across q_x = +-pi at fixed torus point')
for eps in (1e-6, 1e-8):
    k2 = rng.uniform(-np.pi, np.pi, (400, 3)); qo = rng.uniform(-np.pi, np.pi, (400, 3))
    qa, qb = qo.copy(), qo.copy(); qa[:, 0] = np.pi - eps; qb[:, 0] = np.pi + eps
    Fa, *_ = pair_kernel('U', 'G', 0.3, qa - k2, k2); Fb, *_ = pair_kernel('U', 'G', 0.3, qb - k2, k2)
    J = np.abs(Fa - Fb).max(0); S = np.abs(Fa).max(0)
    print('  eps=%.0e  max jump: F^xy %.2e  F^xz %.2e  F^yz %.2e  F^xx %.2e  F^yy %.2e  F^00 %.2e  F^0x %.2e  F^0y %.2e   (|F^xy| up to %.2f, |F^00| up to %.2f)'
          % (eps, J[1, 2], J[1, 3], J[2, 3], J[1, 1], J[2, 2], J[0, 0], J[0, 1], J[0, 2], S[1, 2], S[0, 0]))
# ---- (ii) R19-5 ----
sys.path.insert(0, os.path.join(HERE, 'r195copy'))
import r195_dirac_exact as R5
from r99_profiles import plateau, wrap
C1, C2 = 1.0, 2.5                               # verbatim from r195_dirac_exact2.py
def dsym(q):
    q = wrap(q); r = plateau(q, C1, C2); return r*q + (1-r)*2*np.sin(q/2)
def Dfull(q): q = wrap(np.asarray(q, float)); return dsym(q)*np.exp(0.5j*q)
def far(band, k2, q):
    k1 = k2 + q; D = Dfull(q); Dc = D.conj(); n2 = (np.abs(D)**2).sum()
    E1, E2 = band.E(k1), band.E(k2)
    Pp1, Pm1, Pp2, Pm2 = band.proj(k1, 1), band.proj(k1, -1), band.proj(k2, 1), band.proj(k2, -1)
    M = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sgn, Pa, Pb in ((1, Pp1, Pp2), (-1, Pm1, Pm2)):
        PP = Pa @ Pb; w = sgn*(E1 - E2)
        M00 = sgn*0.5*(E1 + E2)*PP
        M0 = [Dc[j]*w*M00/n2 for j in range(3)]
        V = [w*M0[i] for i in range(3)]
        DV = sum(D[l]*V[l] for l in range(3))
        M[0][0] += M00
        for i in range(3):
            M[0][i+1] += M0[i]
            for j in range(3):
                M[i+1][j+1] += (V[i]*Dc[j] + Dc[i]*V[j])/n2 - DV*Dc[i]*Dc[j]/n2**2
    kb = k2 + q/2
    G = [[R5.UD(band, kb, i, j) for j in range(3)] for i in range(3)]
    for sgn, Pa, Pb in ((1, Pp1, Pm2), (-1, Pm1, Pp2)):
        Mij = [[Pa @ G[i][j] @ Pb for j in range(3)] for i in range(3)]
        M0i = [sgn*sum(D[j]*Mij[j][i] for j in range(3))/(E1 + E2) for i in range(3)]
        M[0][0] += sgn*sum(D[j]*M0i[j] for j in range(3))/(E1 + E2)
        for i in range(3):
            M[0][i+1] += M0i[i]
            for j in range(3): M[i+1][j+1] += Mij[i][j]
    for j in range(1, 4): M[j][0] = M[0][j]
    return M
band = R5.Band(R5.D1(0.909103707957, 0.555604225797), 0.01)
UD0 = R5.UD
print('(ii) R19-5 Dirac construction (verbatim far(); q_x near +-pi is in the far region), archived D1 root law, m = 0.01')
for lab, patch in (('full kernel as built', UD0), ('scattering blocks only (UD -> 0)', lambda b, k, i, j: np.zeros((4, 4), complex))):
    R5.UD = patch
    for eps in (1e-6, 1e-8):
        J = np.zeros((4, 4)); Sz = np.zeros((4, 4))
        for t in range(60):
            k2 = rng.uniform(-np.pi, np.pi, 3); qo = rng.uniform(-np.pi, np.pi, 3)
            qa, qb = qo.copy(), qo.copy(); qa[0] = np.pi - eps; qb[0] = -np.pi + eps
            Ma, Mb = far(band, k2, qa), far(band, k2, qb)
            for a in range(4):
                for b in range(4):
                    J[a, b] = max(J[a, b], np.abs(Ma[a][b] - Mb[a][b]).max()); Sz[a, b] = max(Sz[a, b], np.abs(Ma[a][b]).max())
        print('  %-34s eps=%.0e  max jump M^xy %.2e M^xx %.2e M^yy %.2e M^zz %.2e M^yz %.2e M^00 %.2e M^0x %.2e  (|M^xy| up to %.2f)'
              % (lab, eps, J[1, 2], J[1, 1], J[2, 2], J[3, 3], J[2, 3], J[0, 0], J[0, 1], Sz[1, 2]))
R5.UD = UD0
print('(iii) R13-5 check (6) evaluates pair_kernel with k1, k2 of shape (..., 1): d = 1 has only F^{11} (p = e_1, an integer'
      ' placement), so the off-diagonal half-integer placement was never exercised by that test.')
