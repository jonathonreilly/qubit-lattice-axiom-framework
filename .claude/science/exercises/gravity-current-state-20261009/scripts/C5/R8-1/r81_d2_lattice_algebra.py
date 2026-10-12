"""R8-1, script 6 (d = 2, lattice-native end-to-end): all Poincare commutators of the interacting
two-body box law, with every generator built from LATTICE operators (no chart in the generators):
  representation psi(P, k1): relative momentum k1 on an L x L torus (= relative coordinate on an
  L x L ring of sites), total momentum P continuous (infinite lattice in the centre coordinate),
  sampled on a periodic window (spectral) on which the packet vanishes.
  X_1 = i(d_k1|P + d_P|k1), X_2 = i d_P|k1 (lattice site positions), eps = lattice box band, P_op = s(k1)+s(k2),
  H0 = eps1 + eps2, K0 = sum_i (1/2){eps_i, X_i}, J0 = sum_i (1/2)({X_i,x, j_i,y} - {X_i,y, j_i,x}), j = s s'.
  X_E = sum_i (1/2){eps_i/H0, X_i};  S = (H0/M0)(J0 - X_E x P_op) (masked off the interaction region),
  X_NW = X_E - eps_ab P_b S/(H0(M0+H0));  W = sampled smooth BT kernel (r81_common), F = (W1 - V)/P^2;
  H = H0 + c W;  K_a = K0_a + (1/2){c W, X_NW,a} + eps_ab P_b (1/2){S, c F};  J = J0.
Checks: the 12 relations on a packet (Gaussian in P, bound doublet + scattering with l = 0, +-1, +-2).
Comparator: the single odd rank-one g_x channel (R7-1's channel in d = 2), same construction.
"""
import numpy as np, sys, time
from r81_common import sstep, wrap, BoxLaw, BTKernel, lam_for_mass

L = int(sys.argv[1]) if len(sys.argv) > 1 else 64
NP = int(sys.argv[2]) if len(sys.argv) > 2 else 32
CHAN = sys.argv[3] if len(sys.argv) > 3 else 'doublet'
m, KAP, MU_B, PI1, PI2 = 0.5, 1.0, 0.85, 1.0, 1.4
WIN, SIGP, P0 = 1.0, 0.11, (0.1, -0.05)
LEG = 2.4
import os
FREE = os.environ.get('FREE') == '1'
lam = lam_for_mass(m, KAP, 2, MU_B)
Kk = BTKernel(m, KAP, lam, 2)
law = BoxLaw(m, B=2.6, B2=3.0)
cfun = lambda P: sstep((PI2 - np.abs(P))/(PI2 - PI1))
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)
t0 = time.time()
dP = 2*WIN/NP; Pg = -WIN + (np.arange(NP) + 0.5)*dP
kg = wrap(2*np.pi*np.arange(L)/L); dk = 2*np.pi/L
PX, PY, KX, KY = np.meshgrid(Pg, Pg, kg, kg, indexing='ij')
K2X, K2Y = wrap(PX - KX), wrap(PY - KY)
def ds(k):
    h = 1e-5; return (law.s(k + h) - law.s(k - h))/(2*h)
e1 = law.eps(KX, KY); e2 = law.eps(K2X, K2Y); H0 = e1 + e2
s1x, s1y, s2x, s2y = law.s(KX), law.s(KY), law.s(K2X), law.s(K2Y)
Pox, Poy = s1x + s2x, s1y + s2y
j1x, j1y, j2x, j2y = s1x*ds(KX), s1y*ds(KY), s2x*ds(K2X), s2y*ds(K2Y)
ok = (np.abs(KX) < LEG) & (np.abs(KY) < LEG) & (np.abs(K2X) < LEG) & (np.abs(K2Y) < LEG) \
     & (np.abs(KX + K2X - PX) < 1e-9) & (np.abs(KY + K2Y - PY) < 1e-9)
M0 = np.sqrt(np.maximum(H0**2 - Pox**2 - Poy**2, 1e-12))
Pk = PX*KX + PY*KY
qx = KX + PX*(Pk/(M0*(H0 + M0)) - e1/M0); qy = KY + PY*(Pk/(M0*(H0 + M0)) - e1/M0)
w_ = np.sqrt(m*m + qx**2 + qy**2)
Jq = (w_*w_*H0)/(e1*e2*2*w_)                     # |det dq/dk1| at fixed P (box)
q2 = qx**2 + qy**2
mask = np.where(ok, sstep((1.3**2 - q2)/(1.3**2 - 1.05**2)), 0.0)   # = 1 on |q| <= 1.05 > kappa
pr('grid: L = %d torus (relative), NP = %d window +-%.2f (centre), channel = %s; setup %.1fs' % (L, NP, WIN, CHAN, time.time() - t0))

# ---- W, F blocks per P grid point
t0 = time.time()
blocks = []
for i in range(NP):
    for jj in range(NP):
        sel = ok[i, jj] & (q2[i, jj] < KAP**2)
        idx = np.where(sel.ravel())[0]
        if len(idx) == 0: blocks.append(None); continue
        Pv = np.array([Pg[i], Pg[jj]]); P2 = Pv @ Pv
        a, b = qx[i, jj].ravel()[idx], qy[i, jj].ravel()[idx]
        r = np.sqrt(a*a + b*b); bb = Kk.b(r**2)
        sj = np.sqrt(Jq[i, jj].ravel()[idx])*dk
        if CHAN == 'doublet':
            dot = np.outer(a, a) + np.outer(b, b)
            W1 = dot*np.outer(bb, bb)*Kk.Omega(P2, r, r)*np.outer(sj, sj)
            V = lam*dot*np.outer(bb, bb)*np.outer(sj, sj)
        else:   # single g_x channel: exact BT kernel for rank-one V = lam |g_x><g_x| via Nystrom on a fine polar grid
            V = lam*np.outer(a*bb*sj, a*bb*sj)
            # f(M) - f(M0) on the sampled points: use the lattice sample itself as the Nystrom grid (comparator only)
            Mm = np.diag(2*np.sqrt(m*m + r**2)) + V
            mu, U = np.linalg.eigh(Mm)
            W1 = (U*np.sqrt(mu**2 + P2)) @ U.T - np.diag(np.sqrt(4*(m*m + r**2) + P2))
        cc = cfun(np.sqrt(P2))
        if FREE: cc = 0.0
        if CHAN == 'doublet':
            Vf = (np.sqrt(abs(lam))*a*bb*sj, np.sqrt(abs(lam))*b*bb*sj)
        else:
            Vf = (np.sqrt(abs(lam))*a*bb*sj, 0*a)
        blocks.append((idx, (cc*W1).astype(np.float32), cc, P2, Vf))
pr('W/F blocks built in %.1fs' % (time.time() - t0))

def apply_block(v, which):
    o = np.zeros_like(v)
    for i in range(NP):
        for jj in range(NP):
            bl = blocks[i*NP + jj]
            if bl is None: continue
            idx, Wb, cc, P2, (ux, uy) = bl
            vv = v[i, jj].ravel()[idx]
            Wv = Wb.astype(np.float64) @ vv
            if which == 'W':
                res_ = Wv
            else:   # c F = (c W1 - c V)/P^2, V = lam (|ux><ux| + |uy><uy|), lam < 0
                res_ = (Wv + cc*(ux*(ux @ vv) + uy*(uy @ vv)))/P2
            ot = o[i, jj].ravel(); ot[idx] = res_
            o[i, jj] = ot.reshape(L, L)
    return o

fP = 2j*np.pi*np.fft.fftfreq(NP, d=dP); fk = 2j*np.pi*np.fft.fftfreq(L, d=dk)
def dPd(v, a):
    sh = [1, 1, 1, 1]; sh[a] = NP
    return np.fft.ifft(fP.reshape(sh)*np.fft.fft(v, axis=a), axis=a)
def dkd(v, a):
    sh = [1, 1, 1, 1]; sh[2 + a] = L
    return np.fft.ifft(fk.reshape(sh)*np.fft.fft(v, axis=2 + a), axis=2 + a)
X1 = lambda v, a: 1j*(dkd(v, a) + dPd(v, a))
X2 = lambda v, a: 1j*dPd(v, a)
anti = lambda f, Xop, v, a: 0.5*(f*Xop(v, a) + Xop(f*v, a))
def H0op(v): return H0*v
def Hop(v):  return H0*v + apply_block(v, 'W')
def Pop(v, a): return (Pox if a == 0 else Poy)*v
def J0op(v):
    return 0.5*(X1(j1y*v, 0) + j1y*X1(v, 0) - X1(j1x*v, 1) - j1x*X1(v, 1)
              + X2(j2y*v, 0) + j2y*X2(v, 0) - X2(j2x*v, 1) - j2x*X2(v, 1))
def XE(v, a):
    return anti(e1/H0, X1, v, a) + anti(e2/H0, X2, v, a)
def Sop(v):
    t = J0op(v) - (XE(Pop(v, 1), 0) - XE(Pop(v, 0), 1))
    return mask*(H0/M0)*t
def XNW(v, a):
    sv = Sop(v); g_ = mask/(H0*(M0 + H0))
    return XE(v, a) - (g_*Pop(sv, 1) if a == 0 else -g_*Pop(sv, 0))
def K0op(v, a): return anti(e1, X1, v, a) + anti(e2, X2, v, a)
def Kop(v, a):
    Wv = apply_block(v, 'W')
    kw = 0.5*(apply_block(XNW(v, a), 'W') + XNW(Wv, a))
    sp = 0.5*(Sop(apply_block(v, 'F')) + apply_block(Sop(v), 'F'))
    return K0op(v, a) + kw + (Pop(sp, 1) if a == 0 else -Pop(sp, 0))
Jop = J0op

# ---- packet: A(P) chi(q) sqrt(Jq) on the chart region
A = np.exp(-((PX - P0[0])**2 + (PY - P0[1])**2)/(4*SIGP**2))
bq = Kk.b(q2)
GAUSS = os.environ.get('GAUSS') == '1'
chi = (0.0 if GAUSS else 1.0)*bq*(qx + 0.5j*qy)/(MU_B - 2*w_) + 0.4*np.exp(-q2/(2*0.25**2))*(0.6 + qx + 0.3j*qy + 0.8*(qx**2 - qy**2))
v = np.where(ok, A*chi*np.sqrt(Jq), 0.0)
v = v/np.linalg.norm(v)
asym = None
t0 = time.time()
Hv = Hop(v); Jv = Jop(v); Pv = [Pop(v, 0), Pop(v, 1)]; Kv = [Kop(v, 0), Kop(v, 1)]
n = np.linalg.norm
res = {
    '[Kx,Px]-iH': n(Kop(Pv[0], 0) - Pop(Kv[0], 0) - 1j*Hv)/n(Hv),
    '[Kx,Py]':    n(Kop(Pv[1], 0) - Pop(Kv[0], 1))/n(Hv),
    '[Ky,Py]-iH': n(Kop(Pv[1], 1) - Pop(Kv[1], 1) - 1j*Hv)/n(Hv),
    '[Kx,H]-iPx': n(Kop(Hv, 0) - Hop(Kv[0]) - 1j*Pv[0])/n(Pv[0]),
    '[Ky,H]-iPy': n(Kop(Hv, 1) - Hop(Kv[1]) - 1j*Pv[1])/n(Pv[1]),
    '[Kx,Ky]+iJ': n(Kop(Kv[1], 0) - Kop(Kv[0], 1) + 1j*Jv)/n(Jv),
    '[J,Kx]-iKy': n(Jop(Kv[0]) - Kop(Jv, 0) - 1j*Kv[1])/n(Kv[1]),
    '[J,Ky]+iKx': n(Jop(Kv[1]) - Kop(Jv, 1) + 1j*Kv[0])/n(Kv[0]),
    '[J,Px]-iPy': n(Jop(Pv[0]) - Pop(Jv, 0) - 1j*Pv[1])/n(Pv[1]),
    '[J,H]':      n(Jop(Hv) - Hop(Jv))/n(Hv),
    '[Px,H]':     n(Pop(Hv, 0) - Hop(Pv[0]))/n(Hv),
}
pr('|cW psi|/|H psi| = %.3f ; |spin term|/|K psi| = %.3f' % (n(apply_block(v, 'W'))/n(Hv),
   n(0.5*(Sop(apply_block(v, 'F')) + apply_block(Sop(v), 'F')))/n(Kv[0])))
pr('residuals: ' + '  '.join('%s %.1e' % (kk, vv) for kk, vv in res.items()))
pr('free-only comparator (K0 with interacting H): [K0x,H]-iPx = %.1e' % (n(K0op(Hv, 0) - Hop(K0op(v, 0)) - 1j*Pv[0])/n(Pv[0])))
pr('time %.1fs' % (time.time() - t0))
with open(__file__.replace('.py', '_L%d_NP%d_%s%s%s.out' % (L, NP, CHAN, '_FREE' if FREE else '', '_GAUSS' if GAUSS else '')), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
