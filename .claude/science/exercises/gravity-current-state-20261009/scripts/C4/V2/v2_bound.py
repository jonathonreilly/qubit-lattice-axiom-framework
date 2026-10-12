"""V2 (b2): universality of a two-particle bound state under the canonical (band-transported) strain coupling.

Two distinguishable lattice-KG particles on Z^3 (dispersion w(k) = sqrt(m^2 + sum 4 sin^2(k/2))) bound by a
potential V(r) of the relative coordinate r = x1 - x2 (two-particle sector; the vacuum cloud is inside W).
psi(x1,x2) = e^{iQ.x2} phi(r);  H_Q = w(k) + w(Q-k) + V(r),  k conjugate to r, kap = k - Q/2.
On an isolated band the canonical (Kato-transported) strain generator acts as its band symbol
   f_B(Q) = < sin k + sin(Q-k) > = 2 sin(Q/2) < cos kap >      (per axis, exact)
so a moving composite carries T_ij = f_B,i v_B,j (v_B = dE_B/dQ by Hellmann-Feynman = <grad w(Q-k)>).
An elementary lattice-KG particle has f = sin Q = w(Q) v(Q) EXACTLY (T^{0i} = T^{i0}, p = E v at every Q).
Universality parameters of the composite (Q -> 0 along x):
  eta_EP  = 1 - f_B/(E_B v_B)   (momentum density that gravitates vs energy current incl. binding; 0 for elementary)
  eta_mom = 1 - f_B/Q            (= 1 - <cos kap_x> at Q -> 0; gravitating momentum vs crystal momentum)
  eta_LI  = 1 - E_B(0) v_B/Q     (rest energy vs inertial mass from the dispersion: pure lattice Lorentz violation)
Exact relation: (1 - eta_EP) = (1 - eta_mom)/(1 - eta_LI).
"""
import numpy as np, sys, time
from scipy.sparse.linalg import LinearOperator, eigsh
L = int(sys.argv[1]) if len(sys.argv) > 1 else 40
k1 = 2*np.pi*np.fft.fftfreq(L)
KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing='ij')
r1 = np.fft.fftfreq(L)*L  # minimal-image coordinates
RX, RY, RZ = np.meshgrid(r1, r1, r1, indexing='ij'); R2 = RX**2 + RY**2 + RZ**2
def wd(kx, ky, kz, m): return np.sqrt(m**2 + 4*np.sin(kx/2)**2 + 4*np.sin(ky/2)**2 + 4*np.sin(kz/2)**2)
def solve(m, V, q):
    eps = wd(KX, KY, KZ, m) + wd(q - KX, -KY, -KZ, m)
    n = L**3
    def mv(x):
        p = x.reshape(L, L, L)
        return (np.fft.ifftn(eps*np.fft.fftn(p)) + V*p).ravel()
    A = LinearOperator((n, n), matvec=mv, dtype=complex)
    x0 = np.exp(-R2/8.0).astype(complex).ravel()
    E, X = eigsh(A, k=1, which='SA', v0=x0, tol=1e-11, maxiter=20000)
    phi = X[:, 0].reshape(L, L, L)
    pk = np.abs(np.fft.fftn(phi))**2; pk /= pk.sum()
    fB = np.sum(pk*(np.sin(KX) + np.sin(q - KX)))
    f2 = lambda k: (4/3)*np.sin(k) - (1/6)*np.sin(2*k)
    global fB2_last; fB2_last = np.sum(pk*(f2(KX) + f2(q - KX)))
    w2 = wd(q - KX, -KY, -KZ, m)
    vB = np.sum(pk*np.sin(q - KX)/w2)
    ckap = np.sum(pk*np.cos(KX - q/2))
    pr = np.abs(phi)**2; pr /= pr.sum()
    rrms = np.sqrt(np.sum(pr*R2))
    thr = eps.min()
    return E[0], fB, vB, ckap, rrms, thr
def run(label, m, V, q=0.04):
    t0 = time.time()
    E0, _, _, c0, rr, thr0 = solve(m, V, 0.0)
    Eq, fB, vB, cq, _, _ = solve(m, V, q)
    Ebind = thr0 - E0
    eta_mom = 1 - fB/q; eta_LI = 1 - E0*vB/q; eta_EP = 1 - fB/(Eq*vB)
    kx2 = 2*(1 - c0)   # lattice <kap_x^2>
    print(f'{label:28s} m={m:4.2f} L={L}: E_bind={Ebind:.4e} (bound: {Ebind>0}) r_rms={rr:6.3f} '
          f'<kap_x^2>_lat={kx2:.4e} | eta_mom={eta_mom:+.4e} (1-<cos kap_x>_0 = {1-c0:+.4e}) eta_LI={eta_LI:+.4e} '
          f'eta_EP={eta_EP:+.4e} | eta_mom*r_rms^2 = {eta_mom*rr**2:.4f} | improved f2: eta_mom={1-fB2_last/q:+.3e}, *r^4 = {(1-fB2_last/q)*rr**4:.3f} [{time.time()-t0:.1f}s]')
    sys.stdout.flush()
    return Ebind, rr, kx2, eta_EP
# elementary control: f = sin q, v = sin q / w(q): eta_EP = 1 - sin q/(w v) = 0 exactly
for m in [1.0, 0.3]:
    q = 0.04; wq = np.sqrt(m**2 + 4*np.sin(q/2)**2); v = np.sin(q)/wq
    print(f'elementary control m={m}: eta_EP = {1 - np.sin(q)/(wq*v):.1e} (exact 0), eta_mom = {1-np.sin(q)/q:.3e} (= q^2/6 -> 0)')
# contact interaction is separable: solved exactly in infinite volume by a fine k-grid (see v2_contact.py)
print('=== smooth Gaussian well V = -V0 exp(-r^2/(2 R^2)) (analytic tail); eta_EP, eta_LI include the static')
print('    potential\'s own (continuum) Lorentz violation ~ E_bind/2m; eta_mom is the pure lattice part (0 in continuum)')
res_g = []
for m in [1.0, 0.3]:
    for Rw, prod in [(1.5, 6.0), (2.0, 6.0), (3.0, 6.0), (4.0, 6.0), (2.0, 10.0), (3.0, 10.0)]:
        V0 = prod/(m*Rw**2)
        V = -V0*np.exp(-R2/(2*Rw**2))
        res_g.append(run(f'gauss R={Rw} V0={V0:.3f}', m, V))
