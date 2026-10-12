"""R13-1 checks: (1) soft selectron mass-split residual of DELTA; (2) product-rule defect and an on-shell 2->2 process with
Delta P != 0 (obstruction to a dressed conserved P at O(e^2)); (3) the free photino of the spinor class: Majorana-Wilson,
E_l(q) = omega(q) exactly, zero only at q = 0 (doubler question (d)); (4) the free spinor algebra per mode (Pauli algebra).
"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r85_box_qed_copy import Law, photon, fermion, plateau
from r131_photon_sqed import selectron
from r131_electron_sqed import dc_partner, he, alpha, beta, photino_funcs
from scipy.optimize import brentq
U = 16 * np.pi ** 2
t0 = time.time()

print('(1) soft selectron split: eps^2 = E_e^2 + dm2 (both loops).  DELTA x16pi^2 per e^2, m = 0.1, N = 96')
for lab, b1, b2 in [('S1', 1.0, 2.0), ('S3', 2.0, 3.0)]:
    for r in (0.0, 1.0):
        law = Law(b1, b2, r, b1, b2, 0.1)
        ph = photon(law, 96); fe = fermion(law, 96, 0.1)
        row = []
        for dm2 in (0.0, 0.005, 0.01):
            dS, _ = selectron(law, 96, dm2=dm2)
            pa = 2.0 * dc_partner(law, 96, dm2=dm2)
            row.append(U * (fe['dce'] + pa - ph['dcg'] - 2 * dS))
        slope = (row[2] - row[0]) / 0.01
        print('  %s r=%.0f: DELTA(dm2=0, .005, .01) = %+.4f %+.4f %+.4f ; dDELTA/d(dm2) ~ %+.2f (lattice units)' % (
            lab, r, row[0], row[1], row[2], slope), flush=True)

print('\n(2) product-rule defect D(k,q) = S(k+q) - S(k) - S(q), shape S1 (b1=1, b2=2):')
law = Law(1.0, 2.0, 1.0, 1.0, 2.0, 0.1)
for k, q in [(0.3, 0.4), (0.6, 0.39), (0.6, 0.5), (1.2, 0.3), (2.5, 0.2), (np.pi - 0.1, 0.2), (0.0, 1.5)]:
    print('  k=%.3f q=%.3f  k,q,k+q in box: %s   D = %+.3e' % (k, q, all(abs(x) <= 1.0 for x in (k, q, (k + q + np.pi) % (2 * np.pi) - np.pi)),
                                                             law.S(np.array(k + q)) - law.S(np.array(k)) - law.S(np.array(q))))
def Ee(k):
    return np.linalg.eigvalsh(he(law, k))[-1]
def pvec(k):
    return np.array([float(law.S(np.array(x))) for x in k])
k1 = np.array([0.95, 0.5, 0.0]); k2 = np.array([0.6, -0.5, 0.0]); K = k1 + k2; Ein = Ee(k1) + Ee(k2)
print('  2->2: k1=%s k2=%s (both in box), E_in=%.6f' % (k1, k2, Ein))
for s in (0.4, 0.5, 0.6):
    f = lambda y: Ee(K / 2 + np.array([s, y, 0])) + Ee(K / 2 - np.array([s, y, 0])) - Ein
    try:
        y = brentq(f, 0.0, 1.5)
    except ValueError:
        print('   s=%.2f no root' % s); continue
    k3 = K / 2 + np.array([s, y, 0]); k4 = K / 2 - np.array([s, y, 0])
    dP = pvec(k3) + pvec(k4) - pvec(k1) - pvec(k2)
    # Coulomb (A_0) vertex overlaps, positive-energy spinors (first state of each doublet)
    def u(k):
        w, V = np.linalg.eigh(he(law, k)); return V[:, 2:]
    ov31 = np.linalg.svd(u(k3).conj().T @ u(k1), compute_uv=False); ov42 = np.linalg.svd(u(k4).conj().T @ u(k2), compute_uv=False)
    print('   s=%.2f on shell at y=%.5f: k3=(%.3f,%.3f,0) [out of box: %s], k4=(%.3f,%.3f,0); |E_out-E_in|=%.1e; Delta P = (%+.4f, %+.4f, %+.4f);'
          ' charge-vertex singular values <u3|u1>: %s, <u4|u2>: %s' % (s, y, k3[0], k3[1], np.any(np.abs(k3) > 1.0), k4[0], k4[1],
          abs(f(y)), dP[0], dP[1], dP[2], np.round(ov31, 3), np.round(ov42, 3)))

print('\n(3) free photino of the spinor class (Majorana-Wilson, 4-comp form h_l = alpha.Sg + beta Wl), photon omega^2 = sum d(q_j)^2:')
for lab, b1, b2 in [('S1', 1.0, 2.0), ('S3', 2.0, 3.0), ('S5', 0.5, 1.5)]:
    law = Law(b1, b2, 1.0, b1, b2, 0.1)
    Sg = photino_funcs(law)
    N = 48; q = (np.arange(N)) * 2 * np.pi / N - np.pi
    QX, QY, QZ = np.meshgrid(q, q, q, indexing='ij')
    d2 = law.d(QX) ** 2 + law.d(QY) ** 2 + law.d(QZ) ** 2
    Wl2 = sum(np.maximum(law.d(Qc) ** 2 - Sg(Qc) ** 2, 0) for Qc in (QX, QY, QZ))
    El2 = Sg(QX) ** 2 + Sg(QY) ** 2 + Sg(QZ) ** 2 + Wl2
    off0 = (np.abs(QX) + np.abs(QY) + np.abs(QZ)) > 1e-12
    # direct eigenvalues of the 4x4 at random q
    rng = np.random.default_rng(1); err = 0.0
    for _ in range(200):
        qq = rng.uniform(-np.pi, np.pi, 3)
        wl = np.sqrt(sum(max(float(law.d(np.array(x))) ** 2 - float(Sg(np.array(x))) ** 2, 0) for x in qq))
        h = sum(float(Sg(np.array(qq[j]))) * alpha[j] for j in range(3)) + wl * beta
        ev = np.abs(np.linalg.eigvalsh(h))
        om = np.sqrt(sum(float(law.d(np.array(x))) ** 2 for x in qq))
        err = max(err, np.max(np.abs(ev - om)))
    print('  %s: max|E_l^2 - omega^2| on grid = %.1e ; min over q != 0 of omega on 48^3 grid = %.4f (grid spacing %.4f) ;'
          ' 4x4 eigenvalue check |E| = omega to %.1e ; Sg(pi) = %.1e, Wl at (pi,0,0) = %.4f' % (
          lab, np.max(np.abs(El2 - d2)), np.sqrt(np.min(d2[off0])), 2 * np.pi / N, err, float(Sg(np.array(np.pi))),
          np.sqrt(max(float(law.d(np.array(np.pi))) ** 2 - float(Sg(np.array(np.pi))) ** 2, 0))))

print('\n(4) free spinor algebra per mode: {Q_a, Qbar_b} = 2 (E 1 - sigma.p)_ab is realizable iff E >= |p|;'
      ' Clifford rank of 2(E - sigma.p): 2 if E>|p| (long, 2+2), 1 if E=|p| (short, 1+1).')
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
law = Law(1.0, 2.0, 1.0, 1.0, 2.0, 0.1)
for k in ([0.3, 0.2, 0.1], [2.5, 0.3, 0.0], [np.pi, 0, 0]):
    pk = pvec(np.array(k)); E = Ee(np.array(k))
    Mx = 2 * (E * np.eye(2) - sum(pk[j] * s[j] for j in range(3)))
    print('  electron k=%s: p=%s E=%.4f |p|=%.4f  eig 2(E - s.p) = %s' % (np.round(k, 3), np.round(pk, 4), E, np.linalg.norm(pk),
                                                                          np.round(np.linalg.eigvalsh(Mx), 4)))
print('elapsed %.1fs' % (time.time() - t0))
