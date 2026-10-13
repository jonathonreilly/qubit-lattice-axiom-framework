"""R19-30 (e), robustness of the R19-5-literal face1 shift: Dirac face1 at m = 0.3, kbar grid N = 32.
delta Pi(s) = Pi_lit(0, s n) - Pi_rows(0, s n) for q = s (1,1,0)/sqrt2, with the literal phase e^{+i q.p} and its
conjugate e^{-i q.p}; delta Pi / s^2 must tend to the face1 shift (beta is identical at q = 0)."""
import numpy as np
import lib1930 as L
DI = L.Dirac(m=0.3); N = 32
kg = (np.arange(N) + 0.5)*2*np.pi/N - np.pi
KB = np.stack(np.meshgrid(kg, kg, kg, indexing='ij'), -1).reshape(-1, 3)
COMPS = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
UDc = {c: DI.UDcoef(KB, *c) for c in COMPS}
a = np.array([1, -1, 0])/np.sqrt(2); b = np.array([0, 0, 1.0]); e = 0.5*(np.outer(a, a) - np.outer(b, b))
n = np.array([1, 1, 0])/np.sqrt(2)
def Pi(q, sgn):
    acc = 0.0
    for (i, j) in COMPS:
        w = e[i, j] + (e[j, i] if i != j else 0.0)
        if w: acc = acc + w*UDc[(i, j)]*np.exp(sgn*0.5j*(q[i] + q[j]))
    G = np.einsum('na,aij->nij', acc, L.GAM); Gd = np.conj(np.swapaxes(G, -1, -2))
    k1, k2 = KB + q/2, KB - q/2
    Pp1, Pm1, Pp2, Pm2 = DI.proj(k1, 1), DI.proj(k1, -1), DI.proj(k2, 1), DI.proj(k2, -1)
    t = np.einsum('nij,njk,nkl,nli->n', Pp1, G, Pm2, Gd) + np.einsum('nij,njk,nkl,nli->n', Pm1, G, Pp2, Gd)
    return -np.mean(t.real/(DI.E(k1) + DI.E(k2)))
for s in (0.2, 0.1, 0.05, 0.025):
    q = s*n; p0 = Pi(q, 0.0)
    print('s = %.3f : [Pi_lit(+) - Pi_rows]/s^2 = %+.6e ; [Pi_lit(-) - Pi_rows]/s^2 = %+.6e' % (s, (Pi(q, 1.0) - p0)/s**2, (Pi(q, -1.0) - p0)/s**2), flush=True)
