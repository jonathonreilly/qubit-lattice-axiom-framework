"""R19-5 part 2: checks of the exact Dirac completion (imports the construction from r195_dirac_exact.py).
(i) forward-value convergence O(q); (ii) pair block == UD exactly (right projectors);
(iii) far region with R9-9's full graviton symbol D(q) = d(q) e^{iq/2} (C1 = 1, C2 = 2.5);
(iv) partition-of-unity glue chi(q) M_near + (1 - chi) M_far, chi = plateau(|q|_inf; 0.5, 0.9)."""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'arch9'))
from r195_dirac_exact import Band, near, residual, herm, UD, Dnear, D1, I4
from r99_profiles import plateau, wrap
C1, C2 = 1.0, 2.5
def dsym(q):
    q = wrap(q); r = plateau(q, C1, C2); return r*q + (1-r)*2*np.sin(q/2)
def Dfull(q): q = wrap(np.asarray(q, float)); return dsym(q)*np.exp(0.5j*q)

def far(band, k2, q):
    k1 = k2 + q; D = Dfull(q); Dc = D.conj(); n2 = (np.abs(D)**2).sum()
    E1, E2 = band.E(k1), band.E(k2)
    Pp1, Pm1, Pp2, Pm2 = band.proj(k1, 1), band.proj(k1, -1), band.proj(k2, 1), band.proj(k2, -1)
    M = [[np.zeros((4, 4), complex) for _ in range(4)] for _ in range(4)]
    for sgn, Pa, Pb in ((1, Pp1, Pp2), (-1, Pm1, Pm2)):
        PP = Pa @ Pb; w = sgn*(E1 - E2)              # h1 X - X h2 = w X on this block
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
    G = [[UD(band, kb, i, j) for j in range(3)] for i in range(3)]
    for sgn, Pa, Pb in ((1, Pp1, Pm2), (-1, Pm1, Pp2)):
        Mij = [[Pa @ G[i][j] @ Pb for j in range(3)] for i in range(3)]
        M0i = [sgn*sum(D[j]*Mij[j][i] for j in range(3))/(E1 + E2) for i in range(3)]
        M[0][0] += sgn*sum(D[j]*M0i[j] for j in range(3))/(E1 + E2)
        for i in range(3):
            M[0][i+1] += M0i[i]
            for j in range(3): M[i+1][j+1] += Mij[i][j]
    for j in range(1, 4): M[j][0] = M[0][j]
    return M

def glued(band, k2, q):
    qi = np.abs(wrap(np.asarray(q, float))).max()
    chi = float(plateau(np.array([qi]), 0.5, 0.9)[0])
    if chi == 0.0: return far(band, k2, q)
    Mn = near(band, k2, wrap(np.asarray(q, float)))
    if chi == 1.0: return Mn
    Mf = far(band, k2, q)
    return [[chi*Mn[a][b] + (1-chi)*Mf[a][b] for b in range(4)] for a in range(4)]

rng = np.random.default_rng(1905)
law = D1(0.909103707957, 0.555604225797)
for m in (0.3, 0.01):
    band = Band(law, m)
    print(f'== D1 root edge, m = {m} ==')
    # (i) forward convergence
    for s in (1e-2, 1e-3, 1e-4):
        fm = 0.0
        for t in range(30):
            k = rng.uniform(-np.pi, np.pi, 3); n = rng.normal(size=3); n /= np.linalg.norm(n)
            M = herm(band, k, s*n, near); E = band.E(k); p = band.p(k)
            Pp, Pm = band.proj(k, 1), band.proj(k, -1)
            for i in range(3):
                fm = max(fm, np.abs(Pp@M[0][i+1]@Pp + Pm@M[0][i+1]@Pm - p[i]*I4).max())
                for j in range(3):
                    fm = max(fm, np.abs(Pp@M[i+1][j+1]@Pp + Pm@M[i+1][j+1]@Pm - p[i]*p[j]/E*(Pp - Pm)).max())
        print(f'  (i) forward values (Lemma F: p_i p_j/E on ++, -p_i p_j/E on --; p_j on M^0j) at |q| = {s:.0e}: max dev {fm:.2e}')
    # (ii) pair block exactly UD (after Hermitization), right projectors
    pm = 0.0
    for t in range(100):
        k2 = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-1, 1, 3)
        M = herm(band, k2, q, near); k1 = k2 + q; kb = k2 + q/2
        for i in range(3):
            for j in range(3):
                for Pa, Pb in ((band.proj(k1, 1), band.proj(k2, -1)), (band.proj(k1, -1), band.proj(k2, 1))):
                    pm = max(pm, np.abs(Pa@M[i+1][j+1]@Pb - Pa@UD(band, kb, i, j)@Pb).max())
    print(f'  (ii) interband (pair) blocks of M^ij minus UD(midpoint), 100 random (k,q), |q_j|<=1: {pm:.2e}')
    # (iii) far region, full symbol, whole torus
    rf = sf = 0.0
    for t in range(300):
        k2 = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-np.pi, np.pi, 3)
        if np.abs(q).max() < 0.5: continue
        M = far(band, k2, q); r, s_ = residual(band, M, k2, q, Dfull)
        MH = herm(band, k2, q, far); rH, sH = residual(band, MH, k2, q, Dfull)
        rf, sf = max(rf, r, rH), max(sf, s_, sH)
    print(f'  (iii) far region (|q|_inf >= 0.5, full D): W1 residual {rf:.2e}, symmetry {sf:.2e}')
    # (iv) glued, whole torus incl. the transition shell
    rg = 0.0; ng = 0
    for t in range(300):
        k2 = rng.uniform(-np.pi, np.pi, 3); q = rng.uniform(-1.0, 1.0, 3)*rng.choice([0.6, 1.0, 3.0])
        M = glued(band, k2, q); r, s_ = residual(band, M, k2, q, Dfull); rg = max(rg, r, s_); ng += 1
    print(f'  (iv) glued M = chi M_near + (1-chi) M_far, {ng} random (k,q): W1 residual + symmetry max {rg:.2e}')
