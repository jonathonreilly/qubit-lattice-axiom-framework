"""R7-3 script 4 (checked on one fibre): hard-core bosons (one qubit per site, Z^2, NN hopping) -- the
two-particle sector at one total quasi-momentum K.  Construction (report section 5):
  h      = free-boson pair energy diag(e(k)), e(k) = eps(k) + eps(K-k), eps = -2(cos kx + cos ky)
  V'     = sum_P lam_P |g_P><g_P|, g_P(k) = chi(k) chi(K-k) restricted to the class with real total
           momentum P = qhat(k) + qhat(K-k)  (box a = 0.7 pi > pi/2, s-wave, symmetric)
  lam_P  tuned so that every channel binds at the SAME energy e_* (below the continuum)
  b      = sum_P w_P b_P (degenerate bound states, w_P >= 0, sum w^2 = 1);  b(0) != 0
  Wc     = J (J^dag J)^(-1/2) on b-perp, J = P|_{b-perp}, P = 1 - |u><u| (u = delta at r = 0)
  H_B    = Wc (h + V' restricted to b-perp) Wc^dag   acts on the hard-core space Ran P.
Checks: (1) H_B is hard-core (H_B u = 0), Hermitian, spectrum = spec(h + V') minus one e_*;
(2) every free pair state phi_p outside the channel supports (all zone-edge pairs) gives an EXACT
    eigenvector Wc phi_p of H_B with eigenvalue e(p): those pairs do not scatter; Wc phi_p - P phi_p is a
    rank-one localized correction; (3) h + V' never mixes classes (in-class non-forward scattering only);
(4) locality: kernel of H_B - P h P in the relative coordinate r decays fast; (5) comparator: the bare
    hard-core problem P h P (no V') -- its eigenvectors mix classes."""
import numpy as np
L = 41
nK = (20, 3); K = 2*np.pi*np.array(nK)/L
def wrap(k): return -(((-k) + np.pi) % (2*np.pi) - np.pi)
def sstep(x):
    x = np.clip(x, 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)
A_BOX = 0.7*np.pi; W_EDGE = 0.25*np.pi
chi = lambda t: sstep((A_BOX - np.abs(wrap(t)))/W_EDGE)
eps = lambda kx, ky: -2*(np.cos(kx) + np.cos(ky))
idx = np.arange(L)
KX, KY = np.meshgrid(2*np.pi*idx/L, 2*np.pi*idx/L, indexing='ij'); kx = wrap(KX.ravel()); ky = wrap(KY.ravel())
k2x = wrap(K[0]-kx); k2y = wrap(K[1]-ky)
e = eps(kx, ky) + eps(k2x, k2y)
Kh = wrap(K)
cls = np.round((np.stack([kx+k2x, ky+k2y], 1) - Kh)/(2*np.pi)).astype(int)
cls_t = [tuple(c) for c in cls]
N = L*L
# symmetric basis: pairs {k, K-k}
partner = np.array([np.argmin((wrap(kx - k2x[i]))**2 + (wrap(ky - k2y[i]))**2) for i in range(N)])
basis = []; seen = set()
for i in range(N):
    if i in seen: continue
    j = partner[i]; v = np.zeros(N)
    if j == i: v[i] = 1.0
    else: v[i] = v[j] = 1/np.sqrt(2)
    seen.update([i, j]); basis.append(v)
B = np.array(basis).T          # N x Ns, columns orthonormal symmetric vectors
Ns = B.shape[1]
h = B.T @ np.diag(e) @ B
u = B.T @ (np.ones(N)/L)       # delta at r = 0 (in k-representation, normalized)
print("L=%d K=2pi*%s/L=(%.3f,%.3f): symmetric dim %d, |u|=%.6f, continuum [%.3f, %.3f]" % (L, nK, K[0], K[1], Ns, np.linalg.norm(u), e.min(), e.max()))
box = chi(kx)*chi(ky)*chi(k2x)*chi(k2y)
chans = {}
for c in set(cls_t):
    g = np.where([ct == c for ct in cls_t], box, 0.0)
    if np.linalg.norm(g) > 1e-8: chans[c] = B.T @ g
print("channels (class m = (P - Khat)/2pi) with nonzero box form factor:", {c: round(float(np.linalg.norm(v)), 4) for c, v in chans.items()})
estar = e.min() - 0.8
Vp = np.zeros((Ns, Ns)); bs = {}
hd = np.diag(h)
for c, g in chans.items():
    lam = 1.0/np.sum(g**2/(estar - hd))       # bound state of channel c exactly at estar
    Vp += lam*np.outer(g, g)
    b = g/(estar - hd); bs[c] = b/np.linalg.norm(b)
    print("  channel %s: lam=%.4f, overlap with other channels' supports = %.1e" % (c, lam, max([abs(np.dot(np.abs(g), np.abs(g2))) for c2, g2 in chans.items() if c2 != c] + [0])))
hW = h + Vp
w = {c: 1/np.sqrt(len(bs)) for c in bs}
b = sum(w[c]*bs[c] for c in bs); b /= np.linalg.norm(b)
print("removed vector b: residual |hW b - e* b| = %.2e ; b(r=0) = <u,b> = %.4f" % (np.linalg.norm(hW@b - estar*b), u@b))
Pi_b = np.eye(Ns) - np.outer(b, b)
Pm = np.eye(Ns) - np.outer(u, u)
wv = Pi_b @ u; nw2 = wv@wv
c = ((1 - nw2)**-0.5 - 1)/nw2
Wc = Pm @ (Pi_b + c*np.outer(wv, wv)) @ Pi_b           # maps b-perp -> Ran P
iso = Wc.T @ Wc - Pi_b
print("Wc: |Wc^T Wc - Pi_b| = %.2e (isometry on b-perp), |Wc Wc^T - P| = %.2e (onto Ran P)" % (np.abs(iso).max(), np.abs(Wc@Wc.T - Pm).max()))
HB = Wc @ hW @ Wc.T
print("(1) |H_B u| = %.2e, |H_B - H_B^T| = %.2e" % (np.linalg.norm(HB@u), np.abs(HB-HB.T).max()))
evB = np.sort(np.linalg.eigvalsh(HB + 1e3*np.outer(u, u)))[:-1]   # drop the u direction (pushed to 1e3)
evW = np.sort(np.linalg.eigvalsh(hW)); kill = np.argmin(np.abs(evW - estar)); evW2 = np.delete(evW, kill)
print("    spectrum(H_B on Ran P) vs spectrum(hW) minus one e*: max diff %.2e ; #eigs at e* in hW: %d, in H_B: %d"
      % (np.abs(evB - evW2).max(), np.sum(np.abs(evW-estar) < 1e-8), np.sum(np.abs(evB-estar) < 1e-8)))
# (2) free pairs outside channel supports
supp = np.zeros(Ns, bool)
for g in chans.values(): supp |= np.abs(g) > 0
free_cols = np.where(~supp)[0]
res = []; edge = []
for j in free_cols:
    phi = np.zeros(Ns); phi[j] = 1.0
    v = Wc @ phi; res.append(np.linalg.norm(HB@v - hd[j]*v)/np.linalg.norm(v))
    i = np.argmax(B[:, j]); edge.append(max(abs(kx[i]), abs(ky[i]), abs(k2x[i]), abs(k2y[i])))
res = np.array(res); edge = np.array(edge)
print("(2) %d free pair states outside channel supports (%d with a leg within 0.1 of the zone edge): max residual |H_B Wc phi - e Wc phi| = %.2e"
      % (len(free_cols), int(np.sum(edge > np.pi-0.1)), res.max()))
# (3) class mixing of hW eigenvectors vs bare hard-core
def class_mix(Hm, keep=None):
    ev, V = np.linalg.eigh(Hm)
    # break exact degeneracies across classes by grouping: measure class content per eigenspace
    mix = 0.0; i = 0
    labels = [cls_t[np.argmax(B[:, j])] for j in range(Ns)]
    labs = sorted(set(labels)); M = np.array([[1.0 if labels[j] == l else 0.0 for j in range(Ns)] for l in labs])
    while i < len(ev):
        j = i
        while j+1 < len(ev) and abs(ev[j+1]-ev[i]) < 1e-9: j += 1
        Vs = V[:, i:j+1]
        if keep is None or keep(ev[i]):
            # projector onto eigenspace; its class-block off-diagonal norm
            Pr = Vs@Vs.T
            off = sum(np.linalg.norm(np.diag(M[a])@Pr@np.diag(M[bb])) for a in range(len(labs)) for bb in range(len(labs)) if a != bb)
            mix = max(mix, off)
        i = j+1
    return mix
print("(3) max class-mixing of eigenspaces: hW (excluding e*) = %.2e ; bare hard-core P h P on Ran P = %.2e"
      % (class_mix(hW, keep=lambda E: abs(E-estar) > 1e-8), class_mix(Pm@h@Pm + 1e3*np.outer(u, u), keep=lambda E: E < 500)))
# (4) locality of H_B - P h P in relative coordinate r (symmetric k-space -> r-space)
D = B @ (HB - Pm@h@Pm) @ B.T       # N x N in k1 basis
rx, ry = np.meshgrid(idx, idx, indexing='ij'); rxv = rx.ravel(); ryv = ry.ravel()
F = np.exp(-1j*(np.outer(kx, rxv) + np.outer(ky, ryv)))/L     # k -> r unitary (columns r)
Dr = F.conj().T @ D @ F
dist = np.minimum(rxv, L-rxv) + np.minimum(ryv, L-ryv)
dmax = np.maximum.outer(dist, dist)
for R in [0, 2, 4, 6, 8, 10, 14, 18]:
    sel = dmax >= R
    print("(4) max |(H_B - PhP)(r,r')| over max(|r|_1,|r'|_1) >= %2d : %.2e" % (R, np.abs(Dr[sel]).max()))
# (5) on-shell non-forward in-class T-matrix of the binding channels, infinite-volume quadrature at the same K
# (H_B has the same S-matrix as hW: proved in report section 5; here T of hW per channel, closed form)
M = 600
q = 2*np.pi*(np.arange(M)+0.5)/M - np.pi
QX, QY = np.meshgrid(q, q, indexing='ij'); qx = QX.ravel(); qy = QY.ravel()
q2x = wrap(K[0]-qx); q2y = wrap(K[1]-qy)
eq = eps(qx, qy) + eps(q2x, q2y)
clq = [tuple(cc) for cc in np.round((np.stack([qx+q2x, qy+q2y], 1) - Kh)/(2*np.pi)).astype(int)]
boxq = chi(qx)*chi(qy)*chi(q2x)*chi(q2y)
for cch in sorted(chans):
    gq = np.where([ct == cch for ct in clq], boxq, 0.0)
    lamq = 1.0/np.mean(gq**2/(estar - eq))          # same tuning rule (normalised quadrature)
    for E in [eq[gq > 0.5].min() + 0.3, eq[gq > 0.5].min() + 0.8]:
        Pi = np.mean(gq**2/(E + 2e-3j - eq))
        sh = np.where((np.abs(eq - E) < 4e-3) & (gq > 1e-6))[0]
        T = lamq*np.outer(gq[sh], gq[sh])/(1 - lamq*Pi)
        same = np.array([[ (abs(wrap(qx[i]-qx[j])) < 1e-9 and abs(wrap(qy[i]-qy[j])) < 1e-9) or
                           (abs(wrap(qx[i]-q2x[j])) < 1e-9 and abs(wrap(qy[i]-q2y[j])) < 1e-9) for j in sh] for i in sh])
        nf = np.abs(T)[~same]
        print("(5) channel %s E=%.3f: %d on-shell in-class pairs, non-forward |T| min %.3e max %.3e (lam=%.4f)"
              % (cch, E, len(sh), nf.min() if nf.size else 0, nf.max() if nf.size else 0, lamq))
