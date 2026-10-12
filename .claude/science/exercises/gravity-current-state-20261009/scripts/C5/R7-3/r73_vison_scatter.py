"""R7-3 script 3 (checked): the static vison pair made by one single-site Pauli (s^z_j flips u on j's
z bond) is a static, translation-labelled scatterer for the Kitaev quasiparticle.  Exact single-particle
T-matrix (rank-2 perturbation on sites A0,B0), infinite-volume Green function by BZ quadrature.
Single-particle Bloch Hamiltonian h_k = [[0, i f],[-i f*, 0]], f = 2(Jz - Jx e^{ik1} - Jy e^{ik2}),
eps = |f| (gauge u_x = u_y = -1, momentum measured from the band minimum).  Flip u_z at cell 0:
delta h = [[0, -4 i Jz],[4 i Jz, 0]] on (A0,B0).  T(E) = dh (1 - G0(E) dh)^-1.
On-shell amplitude t(k',k) = psi_k'^dag T psi_k with psi_k = (i f/|f|, 1)/sqrt2.
Lemma S (report): a static scatterer with nonzero non-forward on-shell amplitude excludes any additive
measurable lift in that sector.  This script supplies the nonzero non-forward amplitude, including
for zone-edge in-momenta.  Comparator: a uniform (gauge) relabelling gives t = 0 (sanity)."""
import numpy as np
Jx, Jy, Jz = 0.25, 0.25, 1.0
def fk(k1, k2): return 2*(Jz - Jx*np.exp(1j*k1) - Jy*np.exp(1j*k2))
M = 1200
kk = 2*np.pi*(np.arange(M) + 0.5)/M - np.pi
K1, K2 = np.meshgrid(kk, kk, indexing='ij')
F = fk(K1, K2); E2 = np.abs(F)**2
def G0(E, eta):
    z = E + 1j*eta
    den = z**2 - E2
    gAA = np.mean(z/den); gAB = np.mean(1j*F/den); gBA = np.mean(-1j*np.conj(F)/den)
    return np.array([[gAA, gAB], [gBA, gAA]])
dh = np.array([[0, -4j*Jz], [4j*Jz, 0]])
def psi(k1, k2):
    f = fk(k1, k2); return np.array([1j*f/abs(f), 1.0])/np.sqrt(2)
def shell_points(E, n=720):
    # points on eps(k) = E by bisection along rays from the band minimum k = 0
    out = []
    for th in np.linspace(0, 2*np.pi, n, endpoint=False):
        d = np.array([np.cos(th), np.sin(th)])
        # march to first crossing, allowing wrap (k is taken mod 2pi)
        r_prev, e_prev = 0.0, abs(fk(0, 0)) - E
        for r in np.linspace(0.01, 2*np.pi*1.5, 600):
            e = abs(fk(*(r*d))) - E
            if e_prev < 0 <= e or e_prev > 0 >= e:
                lo, hi = r_prev, r
                for _ in range(60):
                    mid = 0.5*(lo+hi); em = abs(fk(*(mid*d))) - E
                    if (em - 0)*(e_prev) > 0: lo = mid
                    else: hi = mid
                k = 0.5*(lo+hi)*d; k = (k + np.pi) % (2*np.pi) - np.pi
                out.append(k); break
            r_prev, e_prev = r, e
    return np.array(out)
for E, eta in [(2.2, 2e-3), (2.6, 2e-3), (2.9, 2e-3)]:
    G = G0(E, eta)
    T = dh @ np.linalg.inv(np.eye(2) - G @ dh)
    pts = shell_points(E)
    edge = np.max(np.abs(pts), axis=1)
    i_edge = int(np.argmax(edge))  # in-momentum closest to the zone edge
    kin = pts[i_edge]
    amps = np.array([abs(np.conj(psi(*kp)) @ T @ psi(*kin)) for kp in pts])
    fwd = np.max(np.abs(((pts - kin + np.pi) % (2*np.pi)) - np.pi), axis=1) < 1e-6
    nf = amps[~fwd]
    print("E=%.2f: shell pts=%d, |k|_inf range on shell [%.3f, %.3f]; in-momentum k=(%.3f,%.3f) (|k|_inf=%.3f, zone edge=pi)"
          % (E, len(pts), edge.min(), edge.max(), kin[0], kin[1], edge[i_edge]))
    print("   |t(k',k)| over non-forward k' on the shell: min %.3e  median %.3e  max %.3e ; fraction > 1e-3: %.3f"
          % (nf.min(), np.median(nf), nf.max(), np.mean(nf > 1e-3)))
# eta / quadrature convergence for one amplitude
kin = np.array([np.pi*0.98, 0.3]); 
for MM in [600, 1200]:
    kq = 2*np.pi*(np.arange(MM) + 0.5)/MM - np.pi
    A1, A2 = np.meshgrid(kq, kq, indexing='ij'); FF = fk(A1, A2); EE = np.abs(FF)**2
    E = abs(fk(*kin)); z = E + 2e-3j; den = z**2 - EE
    G = np.array([[np.mean(z/den), np.mean(1j*FF/den)], [np.mean(-1j*np.conj(FF)/den), np.mean(z/den)]])
    T = dh @ np.linalg.inv(np.eye(2) - G @ dh)
    kout = np.array([kin[1], kin[0]])  # Jx = Jy: eps symmetric under k1 <-> k2, exactly on shell
    print("M=%d: E=eps(kin)=%.4f, eps(kout)=%.4f, |t(kout,kin)| = %.4e  (kin near zone edge k1=0.98pi; kout = swapped, non-forward)"
          % (MM, E, abs(fk(*kout)), abs(np.conj(psi(*kout)) @ T @ psi(*kin))))
