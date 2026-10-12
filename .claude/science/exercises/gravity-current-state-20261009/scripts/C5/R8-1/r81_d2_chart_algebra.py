"""R8-1, script 3 (d = 2): the repaired BT boost with a rotationally invariant fermionic channel.

Conventions are those MEASURED for R7-1's free law (r71_box_poincare_free.out (C)):
  X = i d/dk, [X_a, P_b] = i delta_ab, J = X x P (+ S), [K_a, P_b] = i delta_ab H, [K_a, H] = i P_a,
  [K_x, K_y] = -i J, [J, K_x] = +i K_y, [J, P_x] = +i P_y.
Repaired BT generators (canonical chart (P, q); q = particle 1's momentum in the pair rest frame,
reached by the rotationless boost; S = internal angular momentum = -i d/dphi_q):
  H = sqrt(M^2 + P^2),  J = X_NW x P + S  (X_NW = i grad_P at fixed q),
  K_a = (1/2){H, X_NW,a} + eps_ab P_b S / (M + H)      [d = 3: K = (1/2){H, X} + (P x S)/(M + H)]
  M = M0 + V,  V = lam sum_{a=x,y} |g_a><g_a|,  g_a(q) = q_a b(|q|^2)  (p-wave doublet: odd => fermionic,
  rotation invariant => [V, S] = 0).
(a) Chart identity, pointwise: the FREE lattice box generators H0, P, K0 = sum_i (1/2){eps_i, X_i},
    J0 = sum_i X_i x k_i, pulled into the chart, equal the BT free generators (M = M0).  8th-order FD.
(b) The full interacting algebra in the chart, all 9 relations, on a P-grid (spectral) x polar q-grid.
    Comparators: (c1) R7-1's printed sign; (c2) spin term dropped; (c3) one odd rank-one g_x (not rotation
    invariant) - R7-1's channel carried to d = 2.
"""
import numpy as np, time
from r81_common import sstep, BTKernel

m, KAP = 0.5, 0.8
out = []
def pr(*a):
    line = ' '.join(str(x) for x in a); print(line, flush=True); out.append(line)

# ---------------- (a) chart identity ----------------
def to_k(P, q):
    w = np.sqrt(m*m + (q**2).sum(-1)); M0 = 2*w; H0 = np.sqrt(M0**2 + (P**2).sum(-1))
    Pq = (P*q).sum(-1)
    k1 = q + P*(Pq/(M0*(H0 + M0)) + w/M0)[..., None]
    return k1, P - k1
def to_Pq(k1, k2):
    e1 = np.sqrt(m*m + (k1**2).sum(-1)); e2 = np.sqrt(m*m + (k2**2).sum(-1))
    P = k1 + k2; H0 = e1 + e2; M0 = np.sqrt(H0**2 - (P**2).sum(-1))
    Pk = (P*k1).sum(-1)
    q = k1 + P*(Pk/(M0*(H0 + M0)) - e1/M0)[..., None]
    return P, q
def jac_formula(P, q):
    k1, k2 = to_k(P, q)
    e1 = np.sqrt(m*m + (k1**2).sum(-1)); e2 = np.sqrt(m*m + (k2**2).sum(-1))
    w = np.sqrt(m*m + (q**2).sum(-1)); M0 = 2*w; H0 = e1 + e2
    return e1*e2*M0/(w*w*H0)          # |d(k1,k2)/d(P,q)|  (to be checked against FD)

rng = np.random.default_rng(3)
pts = []
for _ in range(12):
    P = rng.uniform(-0.5, 0.5, 2); q = rng.uniform(-0.6, 0.6, 2); pts.append((P, q))
# FD Jacobian check
errJ = 0
for P, q in pts:
    h = 1e-6; Jm = np.zeros((4, 4)); z = np.concatenate([P, q])
    for j in range(4):
        dz = np.zeros(4); dz[j] = h
        kp = np.concatenate(to_k((z+dz)[:2], (z+dz)[2:])); km = np.concatenate(to_k((z-dz)[:2], (z-dz)[2:]))
        Jm[:, j] = (kp - km)/(2*h)
    errJ = max(errJ, abs(abs(np.linalg.det(Jm)) - jac_formula(P, q))/jac_formula(P, q))
    Pb, qb = to_Pq(*to_k(P, q)); errJ = max(errJ, np.abs(Pb - P).max() + np.abs(qb - q).max())
pr('(a) chart: |FD Jacobian - e1 e2 M0/(w^2 H0)|/J and round-trip error, max over 12 points: %.1e' % errJ)

# analytic test function in the chart (smooth, angular content l = 0, +-1, +-2, complex)
def phi(P, q):
    qx, qy = q[..., 0], q[..., 1]; r2 = qx**2 + qy**2
    return np.exp(-((P[..., 0]-0.1)**2 + (P[..., 1]+0.05)**2)/0.08) * np.exp(-r2/0.3) * \
           (0.7 + (qx + 0.4j*qy) + 0.5*(qx**2 - qy**2 + 0.3j*qx*qy) + 0.2*P[..., 0]*qy)
def psi_k(k1, k2):        # U^dagger phi: lattice wavefunction (half-density)
    P, q = to_Pq(k1, k2); return phi(P, q)/np.sqrt(jac_formula(P, q))

c8 = np.array([1/280, -4/105, 1/5, -4/5, 0, 4/5, -1/5, 4/105, -1/280])
def d_dir(f, z, j, h=2e-3):   # 8th-order central derivative of f(z) along coordinate j of a 4-vector
    acc = 0
    for i, c in enumerate(c8):
        if c == 0: continue
        dz = np.zeros(4); dz[j] = (i-4)*h; acc = acc + c*f(z + dz)
    return acc/h
eps = lambda k: np.sqrt(m*m + (k**2).sum(-1))
fk = lambda z: psi_k(z[:2], z[2:])
fq = lambda z: phi(z[:2], z[2:])
maxrel = {}
for P, q in pts:
    k1, k2 = to_k(P, q); zk = np.concatenate([k1, k2]); zq = np.concatenate([P, q])
    sJ = np.sqrt(jac_formula(P, q))
    dk = [d_dir(fk, zk, j) for j in range(4)]        # d/dk1x, d/dk1y, d/dk2x, d/dk2y
    dq = [d_dir(fq, zq, j) for j in range(4)]        # d/dPx, d/dPy, d/dqx, d/dqy
    p0 = fk(zk); f0 = fq(zq)
    e1, e2 = eps(k1), eps(k2)
    # lattice free generators on psi (box: eps exact, X = i d/dk); results mapped to the chart (times sqrt J)
    K0 = [1j*(e1*dk[a] + 0.5*(k1[a]/e1)*p0 + e2*dk[2+a] + 0.5*(k2[a]/e2)*p0) for a in range(2)]
    J0 = 1j*(dk[0]*k1[1] - dk[1]*k1[0] + dk[2]*k2[1] - dk[3]*k2[0])
    # BT free generators in the chart
    w = np.sqrt(m*m + q @ q); M0 = 2*w; H0 = np.sqrt(M0**2 + P @ P)
    S = 1j*(q[1]*dq[2] - q[0]*dq[3])                 # S = (i grad_q) x q = -i d/dphi
    XN = [1j*dq[0], 1j*dq[1]]
    LxP = XN[0]*P[1] - XN[1]*P[0]
    Jbt = LxP + S
    Kbt = [H0*XN[a] + 0.5*1j*(P[a]/H0)*f0 for a in range(2)]           # (1/2){H0, X} = H0 X + (1/2)[X, H0]
    Kbt[0] = Kbt[0] + P[1]*S/(M0 + H0); Kbt[1] = Kbt[1] - P[0]*S/(M0 + H0)
    Kbad = [-(H0*XN[a] + 0.5*1j*(P[a]/H0)*f0) for a in range(2)]      # R7-1 printed: -(1/2){H,X} - S x P/(M+H)
    Kbad[0] = Kbad[0] + P[1]*S/(M0 + H0); Kbad[1] = Kbad[1] - P[0]*S/(M0 + H0)
    Knospin = [H0*XN[a] + 0.5*1j*(P[a]/H0)*f0 for a in range(2)]
    scale = abs(f0) + abs(Kbt[0]) + abs(Kbt[1])
    for lab, A, B in [('K0_x vs BT', K0[0]*sJ, Kbt[0]), ('K0_y vs BT', K0[1]*sJ, Kbt[1]), ('J0 vs BT', J0*sJ, Jbt),
                      ('H0 vs BT', (e1+e2)*p0*sJ, H0*f0),
                      ('(c1) K0_x vs printed-sign BT', K0[0]*sJ, Kbad[0]),
                      ('(c2) K0_x vs BT without spin term', K0[0]*sJ, Knospin[0])]:
        maxrel[lab] = max(maxrel.get(lab, 0), abs(A - B)/scale)
for lab, v in maxrel.items():
    pr('(a) %-36s max relative difference over 12 points = %.2e' % (lab, v))

# ---------------- (b) interacting algebra in the chart ----------------
def algebra(Vmode, spin=True, sign=+1, label=''):
    NP, Wn = 64, 1.0
    Pg = np.linspace(-Wn, Wn, NP, endpoint=False); dP = Pg[1] - Pg[0]
    kP = 2*np.pi*np.fft.fftfreq(NP, d=dP)
    PX, PY = np.meshgrid(Pg, Pg, indexing='ij'); P2 = PX**2 + PY**2
    Nr, Nf, Q = 40, 16, 1.8
    xr, wr = np.polynomial.legendre.leggauss(Nr); r = 0.5*Q*(xr + 1); wr = 0.5*Q*wr
    ph = 2*np.pi*np.arange(Nf)/Nf
    R, PH = np.meshgrid(r, ph, indexing='ij'); qx, qy = R*np.cos(PH), R*np.sin(PH)
    wq = (wr[:, None]*r[:, None]*np.full((1, Nf), 2*np.pi/Nf)).ravel()
    qx, qy, Rr = qx.ravel(), qy.ravel(), R.ravel()
    Kk = BTKernel(m, KAP, -1.0, 2, nq=3001)
    bq = Kk.b(Rr**2)
    lam = -4.933909362638328             # M_b = 0.85 for the doublet (lam_for_mass)
    M0q = 2*np.sqrt(m*m + Rr**2)
    sw = np.sqrt(wq)
    if Vmode == 'doublet':
        Vm = lam*(np.outer(qx*bq*sw, qx*bq*sw) + np.outer(qy*bq*sw, qy*bq*sw))
    else:                                 # R7-1's single odd rank-one channel, carried to d = 2
        Vm = lam*np.outer(qx*bq*sw, qx*bq*sw)
    Mm = np.diag(M0q) + Vm
    mu, Um = np.linalg.eigh(Mm)
    Nq = Nr*Nf
    lf = np.fft.fftfreq(Nf, d=1.0/Nf)    # angular momentum labels
    def Sop(v):                          # -i d/dphi along the phi axis
        vv = v.reshape(NP, NP, Nr, Nf); return np.fft.ifft(lf*np.fft.fft(vv, axis=3), axis=3).reshape(NP, NP, Nq)
    def fM(v, fun):                      # apply fun(mu, P2) in the M eigenbasis, per P
        c = v @ Um.conj(); c = c*fun(mu[None, None, :], P2[:, :, None]); return c @ Um.T
    Hop = lambda v: fM(v, lambda mu_, p2: np.sqrt(mu_**2 + p2))
    Fop = lambda v: fM(v, lambda mu_, p2: 1.0/(mu_ + np.sqrt(mu_**2 + p2)))
    def Xop(v, a):
        kk = kP[:, None, None] if a == 0 else kP[None, :, None]
        return 1j*np.fft.ifft(1j*kk*np.fft.fft(v, axis=a), axis=a)
    Pop = lambda v, a: (PX if a == 0 else PY)[:, :, None]*v
    def Jop(v): return Xop(Pop(v, 1), 0) - Xop(Pop(v, 0), 1) + Sop(v)
    def Kop(v, a):
        base = sign*0.5*(Hop(Xop(v, a)) + Xop(Hop(v), a))
        if not spin: return base
        sp = 0.5*(Sop(Fop(v)) + Fop(Sop(v)))
        return base + (Pop(sp, 1) if a == 0 else -Pop(sp, 0))
    # packet: Gaussian in P times (bound doublet + scattering, l = 0, +-1, +-2)
    A = np.exp(-((PX-0.1)**2 + (PY+0.05)**2)/(4*0.07**2))
    lowest = Um[:, np.argsort(mu)[:2]]
    scat = np.exp(-Rr**2/(2*0.25**2))*(0.6 + (qx + 0.3j*qy) + 0.8*(qx**2 - qy**2) + 0.4j*qx*qy)/np.sqrt(wq.sum())
    chi = (lowest @ np.array([1.0, 0.5j]))/sw + scat
    v = A[:, :, None]*(chi*sw)[None, None, :]
    v = v/np.linalg.norm(v)
    Hv, Jv = Hop(v), Jop(v)
    Pv = [Pop(v, 0), Pop(v, 1)]; Kv = [Kop(v, 0), Kop(v, 1)]
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
        '[S,M]':      n(Sop(fM(v, lambda mu_, p2: mu_ + 0*p2)) - fM(Sop(v), lambda mu_, p2: mu_ + 0*p2))/n(v),
    }
    pr('(b) %s: M_min = %.10f (doublet bound mass target 0.85)' % (label, mu.min()))
    pr('    ' + '  '.join('%s %.1e' % (kk, vv) for kk, vv in res.items()))
    return res

t0 = time.time()
algebra('doublet', True, +1, 'REPAIRED: p-wave doublet, K = (1/2){H,X} + eps P S/(M+H)')
algebra('doublet', True, -1, '(c1) R7-1 printed sign: -(1/2){H,X} + eps P S/(M+H)')
algebra('doublet', False, +1, '(c2) spin term dropped')
algebra('single', True, +1, '(c3) single odd rank-one g_x channel (not rotation invariant)')
pr('(b) time %.1fs' % (time.time() - t0))
with open(__file__.replace('.py', '.out'), 'w') as fh:
    fh.write('\n'.join(out) + '\n')
