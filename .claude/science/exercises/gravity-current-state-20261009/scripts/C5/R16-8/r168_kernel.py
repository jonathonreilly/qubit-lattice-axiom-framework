"""C5 R16-8, script B: the W7 tail kernel in real space, and its gauge-invariant content (d = 3).

Minimal singular completion (R12-1 Corollary, JS slice p_xi = 0) for a unit isotropic defect point source
(Delta_cb = delta_cb, O_hat = delta at the origin):
    D_c(q) = i dh_c(q)                              (the defect's jet: local, a divergence)
    B_ij,c(q) = s_ij(q) D_c(q) / |s(q)|^2,   s_ij = dh_i dh_j - |dh|^2 delta_ij,  |s|^2 = (d-1)|dh|^4
dh = lattice gravity symbol e^{iq}-1 (forward difference = 2i sin(q/2) e^{iq/2}, the midpoint-phase form; a phase-free 2 sin(q/2) is not 2pi-periodic and gives spurious alternating 1/r tails). The tail is an IR statement.
Torus L^3, zero mode set to 0 (named subtraction: the q = 0 mode; D has no zero mode, so nothing physical is removed).
Gauge freedom of the completion: B -> B + Kill(zeta) + T with T transverse-traceless (s.T = 0, s.Kill = 0).
Gauge-invariant content (linear spatial diffeos): the linearized Ricci tensor
    R_ij[B] = 1/2 (dh_k dh_i B_kj + dh_k dh_j B_ki - |dh|^2 B_ij - dh_i dh_j B_kk),  tr R = s.B = D (local).
Checks:
 (1) r^2 B along axes vs the continuum  B_ij,c = 1/2 [d_c d_i d_j r/(8 pi) - delta_ij d_c (1/(4 pi r))]
     -> on the x-axis: B_xx,x = 1/(8 pi r^2), B_yy,x = 1/(16 pi r^2).   (1/r^{d-1}: the registered tail)
 (2) r^4 R_ij,c along axes vs continuum R_ij,c = -(1/(16 pi)) d_c d_i d_j (1/r)
     -> on the x-axis: R_xx,x = 6/(16 pi r^4), R_yy,x = -3/(16 pi r^4).   (1/r^{d+1})
 (3) TT projection of R[B](q): zero to roundoff, so no TT addition T can cancel the non-local part of R
     (R[T] = -|dh|^2 T/2 is TT; R[Kill] = 0).
 (4) The GR comparator: a point mass source of the Hamiltonian constraint, s.h = delta, minimal h = s delta/|s|^2:
     h ~ 1/r and R[h] ~ 1/r^3.  The W7 tail is the same constraint-solution map applied to the source D = div(defect).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np

L = 128
q1 = 2 * np.pi * np.fft.fftfreq(L)
QX, QY, QZ = np.meshgrid(q1, q1, q1, indexing="ij")
dh = [np.exp(1j * QX) - 1, np.exp(1j * QY) - 1, np.exp(1j * QZ) - 1]     # forward differences (midpoint phase)
dc = [np.conj(x) for x in dh]
d2 = (np.abs(dh[0]) ** 2 + np.abs(dh[1]) ** 2 + np.abs(dh[2]) ** 2).real
zero = d2 == 0
d2s = np.where(zero, 1.0, d2)

def sij(i, j):          # Hermitian gate: s_ij = dh_i conj(dh_j) - |dh|^2 delta_ij ; s.B := sum conj(s_ij) B_ij
    return dh[i] * dc[j] - (d2 if i == j else 0.0)

def B(i, j, c):
    v = sij(i, j) * (dh[c]) / (2.0 * d2s ** 2)
    v[zero] = 0.0
    return v

def Ric(i, j, c):
    Bc = {(a, b): B(a, b, c) for a in range(3) for b in range(3)}
    trB = Bc[(0, 0)] + Bc[(1, 1)] + Bc[(2, 2)]
    v = 0.5 * (sum(dc[k] * dh[i] * Bc[(k, j)] for k in range(3)) + sum(dc[k] * dh[j] * Bc[(k, i)] for k in range(3))
               - d2 * Bc[(i, j)] - dh[i] * dc[j] * trB)
    return v

def real(a):             # staggered (complex) placement: report the real-space values; magnitudes are what is compared
    return np.fft.ifftn(a)

out = []
def pr(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

pr(f"C5 R16-8 script B (r168_kernel.py): tail kernel on a {L}^3 torus, dh_c = exp(i q_c) - 1 (forward difference, midpoint phase); zero mode removed")
rs = [2, 4, 8, 12, 16, 24, 32]
pr("\n(1) r^2 B along the x-axis (raw, nothing else subtracted); continuum: B_xx,x r^2 = 1/(8pi) = %.5f, B_yy,x r^2 = 1/(16pi) = %.5f"
   % (1 / (8 * np.pi), 1 / (16 * np.pi)))
Bxxx = real(B(0, 0, 0)); Byyx = real(B(1, 1, 0)); Bxyy = real(B(0, 1, 1))
pr("   r      " + " ".join(f"{r:>9d}" for r in rs))
pr("   xx,x   " + " ".join(f"{abs(Bxxx[r,0,0])*r*r:9.5f}" for r in rs))
pr("   yy,x   " + " ".join(f"{abs(Byyx[r,0,0])*r*r:9.5f}" for r in rs))
pr("   xy,y   " + " ".join(f"{abs(Bxyy[r,0,0])*r*r:9.5f}" for r in rs) + "   (continuum: d_y d_x d_y r/(16 pi) = -1/(16 pi) = %.5f)" % (-1 / (16 * np.pi)))
# body diagonal
pr("   diag (r = |x|, x = (n,n,n)) r^2 |B_xx,x|: " + " ".join(f"{abs(Bxxx[n,n,n])*3*n*n:.5f}" for n in (2, 4, 8, 12, 16)))
pr("   finite-torus image corrections grow toward r = L/4 = %d" % (L // 4))

pr("\n(2) r^4 R along the x-axis (gauge-invariant content); continuum R_xx,x r^4 = 6/(16pi) = %.5f, R_yy,x r^4 = -3/(16pi) = %.5f"
   % (6 / (16 * np.pi), -3 / (16 * np.pi)))
Rxxx = real(Ric(0, 0, 0)); Ryyx = real(Ric(1, 1, 0)); Rzzx = real(Ric(2, 2, 0))
pr("   xx,x   " + " ".join(f"{abs(Rxxx[r,0,0])*r**4:9.5f}" for r in rs))
pr("   yy,x   " + " ".join(f"{abs(Ryyx[r,0,0])*r**4:9.5f}" for r in rs))
pr("   trace at r>=2 (must be 0: tr R = D is local): max |R_xx+R_yy+R_zz| over r = 2..32 on the axis = %.2e"
   % np.max(np.abs((Rxxx + Ryyx + Rzzx)[2:33, 0, 0])))
pr("   source check: tr R at the origin and its neighbours (should be the lattice divergence of a delta):",
   np.round([abs((Rxxx + Ryyx + Rzzx)[x, 0, 0]) for x in (0, 1, -1)], 6))

pr("\n(3) TT projection of R[B] (continuum symbols, 2000 random q, both B and B + T with random TT T):")
rng = np.random.default_rng(168)
mxTT = 0.0; mxR = 0.0; mxdiff = 0.0
for _ in range(2000):
    q = rng.normal(size=3); qq = q @ q; qh = q / np.sqrt(qq)
    s_ = np.outer(q, q) - qq * np.eye(3)
    for c in range(3):
        Bq = s_ * (1j * q[c]) / (2 * qq ** 2)
        def Rc(Bm):
            return 0.5 * (np.outer(q, q @ Bm) + np.outer(q, q @ Bm).T - qq * Bm - np.outer(q, q) * np.trace(Bm)) * (-1)
        P_ = np.eye(3) - np.outer(qh, qh)
        def TT(X):
            return P_ @ X @ P_ - 0.5 * P_ * np.trace(P_ @ X)
        R0 = Rc(Bq)
        T = TT(rng.normal(size=(3, 3)) + rng.normal(size=(3, 3)).T)
        R1 = Rc(Bq + T)
        mxTT = max(mxTT, np.max(np.abs(TT(R0)))); mxR = max(mxR, np.max(np.abs(R0)))
        # non-TT part of R[B+T] equals that of R[B]: T only moves the TT part
        mxdiff = max(mxdiff, np.max(np.abs((R1 - TT(R1)) - (R0 - TT(R0)))))
        # Bianchi-fixed non-TT part = (D/4)(qh qh + delta) up to the overall sign convention
        target = (1j * q[c] / 4) * (np.outer(qh, qh) + np.eye(3))
        mxdiff = max(mxdiff, min(np.max(np.abs(R0 - target)), np.max(np.abs(R0 + target))))
pr(f"   max |Lambda^TT R[B]| = {mxTT:.2e}  (vs max |R[B]| = {mxR:.2e});  max deviation of non-TT part of R[B+T] from (D/4)(qh qh + delta) = {mxdiff:.2e}")
pr("   => adding TT or Kill-exact pieces to B never changes the non-TT (Bianchi-fixed) curvature (D/4)(qh qh + delta):")
pr("      its traceless part is non-analytic for every nonzero defect; the gauge-invariant content of the tail is fixed.")

pr("\n(4) GR comparator: point mass, s.h = delta (Hamiltonian constraint), minimal h = s delta/|s|^2")
def hmin(i, j):
    v = sij(i, j) / (2.0 * d2s ** 2); v[zero] = 0.0; return v
def Ric_h(i, j):
    hc = {(a, b): hmin(a, b) for a in range(3) for b in range(3)}
    trh = hc[(0, 0)] + hc[(1, 1)] + hc[(2, 2)]
    return 0.5 * (sum(dc[k] * dh[i] * hc[(k, j)] for k in range(3)) + sum(dc[k] * dh[j] * hc[(k, i)] for k in range(3))
                  - d2 * hc[(i, j)] - dh[i] * dc[j] * trh)
hxx = real(hmin(0, 0)); hyy = real(hmin(1, 1))
Rhxx = real(Ric_h(0, 0)); Rhyy = real(Ric_h(1, 1))
pr("   r |h_yy| on the x-axis (1/r^{d-2}; image/zero-mode offsets on the torus): " + " ".join(f"{abs(hyy[r,0,0]-hyy[L//2,0,0])*r:.4f}" for r in rs[:5]))
pr("   r^3 R_xx (tidal, 1/r^{d}):  " + " ".join(f"{abs(Rhxx[r,0,0])*r**3:.5f}" for r in rs[:6]) + "   continuum |r^3 R_xx| = 1/(8 pi) = 0.03979")
pr("   => same constraint-solution map; W7's source D = div(defect) is one derivative higher, so every power is r^{-1} lower.")

with open(os.path.splitext(os.path.abspath(__file__))[0] + ".out", "w") as f:
    f.write("\n".join(out) + "\n")
