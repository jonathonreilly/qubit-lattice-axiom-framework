"""R19-31 probe (a): one-loop thermal self-energy of the lattice photon on Z^3 x R (continuous time), NN complex scalar
(charge e) and Wilson-Dirac fermion (r = 1) as matter. Lattice units a = 1; results quoted per e^2.
Strain: H-cov E_g, cell lengths l = (e^h, e^-h, 1); scalar hopping c_i = 1/l_i^2 (vol = 1); photon a_i = theta_i / l_i.
 (a1) static electric (Debye) mass  m_D^2 = Pi_00(0, k->0) = e^2 chi(T),  chi = d^2 P/d mu^2 (uniform static A_0 = chemical potential).
 (a2) static magnetic part Pi_ii(0, k->0) = e^2 [S_ii - L_ii(0)]_thermal: uniform static a_i shifts every lattice momentum, so the
      BZ sum is a-independent and the magnetic part vanishes identically (to all orders for U(1)); checked here at one loop.
 (a3) hard (lattice-scale) photons: on-shell thermal self-energy Pi_th^T(Omega_q, q) from thermal scalars (massive regulator m_s,
      so no Landau/threshold singularity at the sampled q) -- shows the UV modes' thermal shift is e^2 T^2 x f(q), q-dependent."""
import numpy as np, time
t0 = time.time()
def nB(e, T): return 1.0/np.expm1(e/T)
def nF(e, T): return 1.0/(np.exp(e/T) + 1.0)
# graded Gauss-Legendre grid on (-pi, pi), as r1921_nn_thermal.py Part 2
br = np.array([0, 0.0025, 0.005, 0.01, 0.02, 0.04, 0.08, 0.16, 0.32, 0.64, 1.28, 2.2, np.pi])
xg, wg = np.polynomial.legendre.leggauss(6)
nodes, wts = [], []
for a, b in zip(br[:-1], br[1:]):
    nodes += list(0.5*(b - a)*xg + 0.5*(b + a)); wts += list(0.5*(b - a)*wg)
nodes = np.array(nodes); wts = np.array(wts)
k1 = np.concatenate([-nodes[::-1], nodes]); w1 = np.concatenate([wts[::-1], wts])/(2*np.pi)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij', sparse=True)
W = w1[:, None, None]*w1[None, :, None]*w1[None, None, :]
def avg(x): return float((W*x).sum())
def Om2(h, kx=KX, ky=KY, kz=KZ):
    l = (np.exp(h), np.exp(-h), 1.0)
    return 4*np.sin(kx/2)**2/l[0]**2 + 4*np.sin(ky/2)**2/l[1]**2 + 4*np.sin(kz/2)**2/l[2]**2
print('(a1) Debye mass per e^2: complex NN scalar (mass m) chi = 2<beta n(1+n)>; Wilson-Dirac (r=1, m=0) chi = 4<beta nF(1-nF)>; continuum T^2/3 each')
Sw = np.sin(KX)**2 + np.sin(KY)**2 + np.sin(KZ)**2
Mw = (1 - np.cos(KX)) + (1 - np.cos(KY)) + (1 - np.cos(KZ))
Ew = np.sqrt(Sw + Mw**2)
for T in (0.4, 0.2, 0.1, 0.05, 0.025):
    out = []
    for m in (0.0, 0.1):
        e = np.sqrt(m*m + Om2(0.0)); n = nB(e, T)
        out.append(avg(2*n*(1 + n)/T)/(T*T/3))
    nf = nF(Ew, T); chif = avg(4*nf*(1 - nf)/T)
    print('  T=%.3f  scalar m=0: m_D^2/(e^2T^2/3) = %.5f   scalar m=0.1: %.5f   Wilson fermion: %.5f' % (T, out[0], out[1], chif/(T*T/3)), flush=True)
print('(a2) static magnetic part at k->0, thermal, per e^2: S_xx - L_xx(0) = <2 cos p_x n/eps> - <V_x^2 [n/(2 eps^3) - n\'/(2 eps^2)]>  (Ward: must vanish)')
for h in (0.0, 0.05):
    for (m, T) in ((0.0, 0.1), (0.1, 0.05), (0.5, 0.3)):
        l = (np.exp(h), np.exp(-h), 1.0)
        e = np.sqrt(m*m + Om2(h)); n = nB(e, T); npr = -n*(1 + n)/T
        S = avg(2*np.cos(KX)*n/e)                                 # thermal part of sum_P 2 cos p_x G(P)  [T sum_n G -> (1+2n)/(2 eps)]
        V2 = (2/l[0])**2*np.sin(KX)**2
        L = avg(V2*(n/(2*e**3) - npr/(2*e**2)))                   # thermal part of T sum_n G^2 = (1+2n)/(4eps^3) - n'/(2 eps^2)
        print('  h=%.2f m=%.2f T=%.2f: S_th = %+.6e   L_th(0) = %+.6e   S - L = %+.2e   (Debye-type scale chi/2 = %.3e)'
              % (h, m, T, S, L, S - L, avg(n*(1 + n)/T)), flush=True)
print('(a3) hard photon, on-shell thermal self-energy from thermal scalars of mass m_s (per e^2), transverse polarisation x, q along z:')
print('     Pi_th(w=Omega_q, q) = <2 cos p_x n/eps> - sum_p V_x^2/(4 eps1 eps2) [(n1+n2) A(w) + (n1-n2) B(w)],  A,B from the Matsubara sum')
def Pi_th_hard(qz, m, T):
    p_x, p_y, p_z = KX, KY, KZ
    e1 = np.sqrt(m*m + Om2(0.0)); n1 = nB(e1, T)
    e2 = np.sqrt(m*m + Om2(0.0, p_x, p_y, p_z + qz)); n2 = nB(e2, T)
    w = 2*np.sin(qz/2)                                            # photon on shell, k along z
    A = 1/(w + e1 + e2) - 1/(w - e1 - e2)
    B = 1/(w - e1 + e2) - 1/(w + e1 - e2)
    V2 = 4*np.sin(p_x)**2                                         # V_x(p, p+q) = 2 sin(p_x + q_x/2), q_x = 0
    S = avg(2*np.cos(p_x)*n1/e1)
    L = avg(V2/(4*e1*e2)*((n1 + n2)*A + (n1 - n2)*B))
    return S - L, S
for (m, T) in ((1.0, 0.25), (1.0, 0.125), (0.5, 0.1)):
    row = []
    for qz in (0.5, 1.0, 2.0, 3.0):
        P, S = Pi_th_hard(qz, m, T); row.append('q=%.1f: %+.4e (seagull %+.4e)' % (qz, P, S))
    e = np.sqrt(m*m + Om2(0.0)); n = nB(e, T); mD2 = avg(2*n*(1 + n)/T)
    print('  m_s=%.2f T=%.3f  Debye m_D^2 %.4e | ' % (m, T, mD2) + ' | '.join(row), flush=True)
print('time %.0f s' % (time.time() - t0))
