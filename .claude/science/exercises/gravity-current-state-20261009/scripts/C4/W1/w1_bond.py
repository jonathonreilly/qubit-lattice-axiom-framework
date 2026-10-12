"""W1 (d): second interaction = NN (1/4) sum_{x,mu} phi_x^2 phi_{x+mu}^2 (vertex V' = 6 sum_mu b_{bond_mu}), same L2 design.
 (i) O(lam') term: <:V':_0>_eps = (lam'/4) sum_mu 2 (G_eps(e_mu)-G_0(e_mu))^2 -> mu1 = lam' sum_mu Gdot(e_mu)^2  (Gdot(0)=0).
 (ii) O(lam'^2) basketball with dressing c':  mu2' = -(1/24)[A' + 4 c'.L' + 2 c'^T Q c'] (same Q as onsite).
 (iii) does the onsite-cancelling dressing (same operators, same coefficients) cancel the bond mu2'?  Mixed theory too."""
import numpy as np, sys, time
from w1_core import *
m = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
L = int(sys.argv[2]) if len(sys.argv) > 2 else 16
r = int(sys.argv[3]) if len(sys.argv) > 3 else 2
tn, wn = tquad(24, 9.0); t0 = time.time()
E3 = np.eye(3, dtype=int)
BOND = [canon([(0,0,0),(0,0,0),tuple(E3[mu]),tuple(E3[mu])]) for mu in range(3)]
k1 = 2*np.pi*np.fft.fftfreq(L); KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij'); W = wdisp(KX, KY, KZ, m)
mon = enumerate_monomials(r); orbs = orbits(mon); midx = {mo: i for i, mo in enumerate(mon)}
J0, W0 = strained(L, m, 0, 'E'); fld = Field(gx_from_k(J0, W0, tn), wn); F = FourPoint(fld, use_sym=True)
M = len(mon); Qm = np.zeros((M, M))
for i in range(M):
    for j in range(i, M):
        Qm[i, j] = Qm[j, i] = inner_mono(F, mon[i], mon[j])
print(f'm={m} L={L} r={r}: monomial Gram done [{time.time()-t0:.0f}s]'); sys.stdout.flush()
for ch in ['E', 'T2']:
    # (i) O(lam') : equal-time G_eps(x) = int J/(2 Omega) e^{ikx}; Gdot(e_mu)
    if ch == 'E':
        Jd = np.cos(KX)-np.cos(KY); Wd = (np.sin(KX)**2-np.sin(KY)**2)/W
    else:
        Jd = 0*KX; Wd = 2*np.sin(KX)*np.sin(KY)/W
    Gdk = Jd/(2*W) - Wd/(2*W**2)
    Gd = np.fft.ifftn(Gdk).real
    Gdot = [Gd[1,0,0], Gd[0,1,0], Gd[0,0,1]]
    mu1 = sum(g**2 for g in Gdot)
    print(f'[{ch}] O(lam\') bond: Gdot(0)={Gd[0,0,0]:.2e}, Gdot(e_x,e_y,e_z)=({Gdot[0]:+.6e},{Gdot[1]:+.6e},{Gdot[2]:+.6e}) -> mu1\'/lam\' = {mu1:+.6e}')
    # (ii) A' by finite differences with strained g (no cubic canonicalisation)
    d = 0.04; vals = {}
    for e in [-d, -d/2, 0, d/2, d]:
        J, Wst = strained(L, m, e, ch); Fe = FourPoint(Field(gx_from_k(J, Wst, tn), wn), use_sym=False)
        vals[e] = 36*sum(inner_mono(Fe, BOND[a], BOND[b]) for a in range(3) for b in range(3))
    D = lambda e: (vals[e]+vals[-e]-2*vals[0])/e**2; Ap = (4*D(d/2)-D(d))/3
    fdot = Field(gdot_x(L, m, ch, tn), wn)
    # L'_m = d/deps int V' b_m^* w = 6 sum_mu (1/24) sum_sigma Lmono(r^mu - r^m_sigma)
    Lpm = np.array([6*sum(sum(L_mono(fld, fdot, [tuple(np.array(BOND[mu][i]) - np.array(mo[s[i]])) for i in range(4)]) for s in PERMS)/24.0
                          for mu in range(3)) for mo in mon])
    Lm = np.array([L_mono(fld, fdot, mo) for mo in mon])
    funcs = channel_functions(orbs, ch)
    if not funcs:
        print(f'[{ch}] no dressing functions at r={r}; A\'={Ap:.6e} mu2\'(undressed)={-Ap/24:+.5e}'); continue
    C = np.zeros((len(funcs), M))
    for a, fd in enumerate(funcs):
        for mo, c in fd.items(): C[a, midx[mo]] += c
    Qf = C @ Qm @ C.T; Lf = C @ Lm; Lpf = C @ Lpm
    ev, U = np.linalg.eigh(Qf); keep = ev > 1e-9*ev.max(); Ub = U[:, keep]/np.sqrt(ev[keep])
    lo = Ub.T @ Lf; lpo = Ub.T @ Lpf
    # onsite A
    I = {e: onsite_I(L, m, e, ch, tn, wn) for e in [-d, -d/2, 0, d/2, d]}
    Do = lambda e: (I[e]+I[-e]-2*I[0])/e**2; A = (4*Do(d/2)-Do(d))/3
    cos = float(lo @ lpo/np.linalg.norm(lo)/np.linalg.norm(lpo))
    # onsite min-norm solution y* (Q-orthonormal coords), then bond residual with the same operators/coefficients
    ell = float(lo @ lo); s = 1 - np.sqrt(1 - A/(2*ell)); ys = -s*lo
    f_bond = Ap + 4*float(ys @ lpo) + 2*float(ys @ ys)
    # mixed theory lam*H4 + lam'*H4' with dressing (lam c + lam' c'): E2 ~ |lam(1+eps d) + lam'(V'+eps d')|^2 ; cross term needs <1,V'> pieces:
    print(f'[{ch}] A(onsite)={A:.6e}  A\'(bond)={Ap:.6e} mu2\'(undressed)/lam\'^2={-Ap/24:+.5e} | cos angle(L_onsite, L_bond)={cos:+.5f} '
          f'| onsite min-norm dressing applied to bond: mu2\'={-f_bond/24:+.5e} (undressed {-Ap/24:+.5e}) [{time.time()-t0:.0f}s]')
    # dimension count of simultaneous solutions (two hyperplanes, near-linear): rank of [lo; lpo]
    print(f'[{ch}] N_eff={int(keep.sum())}; joint (onsite & bond) solution set dimension ~ N_eff - rank = {int(keep.sum()) - np.linalg.matrix_rank(np.vstack([lo, lpo]), tol=1e-12)}')
    sys.stdout.flush()
