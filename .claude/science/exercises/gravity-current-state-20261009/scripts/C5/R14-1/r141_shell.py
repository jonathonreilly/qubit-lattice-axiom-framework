"""R11-4 (b): what the transition shell Pi1 < |P| < Pi2 does to a moving bound triplet (d = 3, R9-6 law), fibrewise.
Subtraction named before the run: every shell quantity is measured against the exact box (plateau, c = 1) value
at the same P, i.e. against the free spin-1 particle of mass M_b: E = sqrt(M_b^2 + P^2), J' = P, [H, J'] = 0.
Fibre at total momentum P (canonical chart; l = 1 radial channel; legs stay in the exact box for |P| <= 1.2):
  h(P) = H0 + c(|P|) W,  H0 = sqrt(M0^2 + P^2), W = sqrt(M^2 + P^2) - sqrt(M0^2 + P^2), M = M0 + lam |g><g|.
  Fibre part of the gravitating momentum, longitudinal: J'_par = (1/2){h, dh/d|P|} (the spin term i[h, (P x S) g]
  has zero expectation in an h eigenstate and is not included in the source norm below).
Outputs vs |P|: E_b - sqrt(M_b^2+P^2); <J'_par> - |P| (and the Hellmann-Feynman value E_b dE_b/d|P| - |P|);
||[h, J'_par] b|| / E_b (the shell-source norm on the bound state); E_b below the pair threshold sqrt(4m^2+P^2)?"""
import numpy as np
from numpy.polynomial.legendre import leggauss
def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
import sys
m, kap, PI1, PI2 = 0.5, 0.8, 0.6, float(sys.argv[1]) if len(sys.argv) > 1 else 1.2   # R14-1: 0.95 keeps legs < 1.4
cP = lambda p: sstep((PI2 - abs(p))/(PI2 - PI1))
def run(N):
    xr, wr = leggauss(N); r = 0.5*kap*(xr+1); w = 0.5*kap*wr
    M0 = 2*np.sqrt(m*m + r*r); bb = sstep(1 - r*r/kap**2)/kap
    G = np.sqrt(w)*r*np.sqrt(4*np.pi/3)*r*bb
    out = {}
    for Mb in (0.95, 0.85, 0.70):
        lam = 1.0/np.sum(G**2/(Mb - M0))
        Mmat = np.diag(M0) + lam*np.outer(G, G)
        mu, U = np.linalg.eigh(Mmat)
        def h(p):
            Hd = np.sqrt(M0**2 + p*p)
            Wm = (U*np.sqrt(mu**2 + p*p)) @ U.T - np.diag(Hd)
            return np.diag(Hd) + cP(p)*Wm
        rows = []
        for p in (0.0, 0.3, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2):
            hp = h(p); e, V = np.linalg.eigh(hp); Eb, b = e[0], V[:, 0]
            dp = 1e-4
            dh = (h(p+dp) - h(p-dp))/(2*dp)
            Jp = 0.5*(hp @ dh + dh @ hp)
            e1 = np.linalg.eigh(h(p+dp))[0][0]; e2 = np.linalg.eigh(h(p-dp))[0][0]
            HF = Eb*(e1 - e2)/(2*dp)
            src = np.linalg.norm(hp @ (Jp @ b) - Jp @ (hp @ b))/Eb
            rows.append((p, cP(p), Eb - np.sqrt(Mb**2 + p*p), b @ Jp @ b - p, HF - p, src, Eb < np.sqrt(4*m*m + p*p), mu[0]))
        out[Mb] = rows
    return out
o400 = run(400); o200 = run(200)
print('m = %.2f, kappa = %.2f, Pi1 = %.1f, Pi2 = %.1f; radial GL N = 400 (N = 200 in brackets for the source norm)' % (m, kap, PI1, PI2))
for Mb in (0.95, 0.85, 0.70):
    print('\nM_b = %.2f (f_B = %.2f); discrete lowest M eigenvalue %.12f' % (Mb, 1-Mb, o400[Mb][0][7]))
    print('  |P|    c     E_b - sqrt(Mb^2+P^2)   <J_par> - |P|    HF: E_b dE_b/dP - |P|   ||[h,J_par] b||/E_b        bound?')
    for (row, row2) in zip(o400[Mb], o200[Mb]):
        p, c, dE, dJ, dHF, src, bd, _ = row
        print('  %.2f  %.3f   %+.6e        %+.6e    %+.6e         %.3e (%.3e)   %s' % (p, c, dE, dJ, dHF, src, row2[5], bd))
