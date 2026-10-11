"""F1 (lane RF): which C3 sectors survive when GR's algebra is replaced by the
foliation-preserving one (spatial diffeos + time reparametrisation), free lattice scalar.

Uses C3's refereed symbol statements (RC_C3_report.md section 2; referee CONFIRMED WITH CORRECTIONS):
  * P_tot,c generates mode phase rotations with rate f_c = d_c u,  u = omega^2/2;
  * first-order part of {sum_x x_b T00, P_tot,c} = Hess u(q)_bc x (energy of mode q).
FDiff sectors:
  (R) rotation sector {L_ab, P_c} ~ P: lives in {H_i, H_j}, i.e. INSIDE the spatial-diffeo algebra.
      Needs Hess u = M + mu grad u grad u^T (C3 rotation theorem).
  (L) linear-lapse sector: in GR this is the boost relation {P_c, K_b} = delta_bc H. In a NON-projectable
      foliation theory N(x) is a field transported by H_i; preservation of H_i[const] under
      H = sum_x N(x) H_perp(x) with N linear needs  sum_x [ (D_c N) T00 + N D_c^{fw} T00 ] = 0  (a Leibniz
      first moment), i.e. the same bracket: weight matrix W(q) = Hess u(q) must equal Hess u(0) = I.
      Physical reading: in a uniform lapse gradient g, matter gains momentum at rate g_c sum_q W_cc(q) e_q
      instead of g_c sum_q e_q.
  (P) projectable (N = N(t)): (L) absent; (R) remains; the khronon is ghost/tachyon (RN L3).
This script evaluates W and the (R) residual for nearest-neighbour and improved stencils.
"""
import numpy as np

def stencil_u(k, rm=1, m2=0.25):
    """u = omega^2/2 with an improved range-rm second-difference Laplacian (exact in IR to O(k^{2rm+2}))."""
    # coefficients of the order-2rm central approximation of -d^2: sum_j c_j 2(1-cos(j k))
    # solve for c_j: sum_j c_j j^{2p} = delta_{p,1} (p=1..rm), Taylor of 2(1-cos jk) = sum_p 2(-1)^{p+1} (jk)^{2p}/(2p)!
    J = np.arange(1, rm + 1)
    A = np.array([[2 * (-1) ** (p + 1) * j ** (2 * p) / np.math.factorial(2 * p) for j in J] for p in range(1, rm + 1)])
    b = np.zeros(rm); b[0] = 1.0
    cj = np.linalg.solve(A, b)
    def u(kv):
        return 0.5 * (m2 + sum(sum(cj[i] * 2 * (1 - np.cos(J[i] * kc)) for i in range(rm)) for kc in kv))
    def hess(kv):
        return np.diag([0.5 * sum(cj[i] * 2 * J[i] ** 2 * np.cos(J[i] * kc) for i in range(rm)) for kc in kv])
    def grad(kv):
        return np.array([0.5 * sum(cj[i] * 2 * J[i] * np.sin(J[i] * kc) for i in range(rm)) for kc in kv])
    return u, grad, hess

import math
np.math = math

print("(L) linear-lapse / Leibniz sector: weight W_cc(q) = [Hess u(q)]_cc / [Hess u(0)]_cc (FDiff needs 1)")
for rm in [1, 2, 3]:
    u, grad, hess = stencil_u(None, rm)
    H0 = hess(np.zeros(3))[0, 0]
    rows = []
    for kk in [0.01, 0.1, 0.5, 1.5, np.pi]:
        W = hess(np.array([kk, 0, 0]))[0, 0] / H0
        rows.append(f"k={kk:.2f}: W-1={W-1:+.3e}")
    # zone average of W over the Brillouin zone
    ks = np.linspace(-np.pi, np.pi, 4001)[:-1]
    Wavg = np.mean([hess(np.array([x, 0, 0]))[0, 0] for x in ks]) / H0
    print(f"  range {rm}: " + "; ".join(rows) + f";  zone average of W = {Wavg:+.2e} (FDiff needs 1)")

print("\n  physical size of (L) for real matter, a = Planck length: (k a)^2/2 at p = 1 GeV ->",
      f"{0.5*(1.0/1.22e19)**2:.1e}; at lattice-scale (loop) modes O(1) (zone average of W-1 = -1)")

print("\n(R) rotation sector (inside spatial diffeos): min_mu |Hess u - M - mu grad grad^T| / |Hess u| at sample q")
rng = np.random.default_rng(0)
for rm in [1, 2, 3]:
    u, grad, hess = stencil_u(None, rm)
    M = hess(np.zeros(3))
    for kk in [np.array([0.1, 0.2, 0.05]), np.array([0.6, -0.4, 0.9]), np.array([1.7, 0.3, -2.2])]:
        Hq = hess(kk); gq = grad(kk)
        X = np.outer(gq, gq).ravel(); Y = (Hq - M).ravel()
        mu = (X @ Y) / (X @ X)
        res = np.linalg.norm(Y - mu * X) / np.linalg.norm(Hq)
        print(f"  range {rm}: q={kk}: residual = {res:.3e}")
print("  (any nonzero residual on an open set => no rotation-sector closure; C3 theorem: impossible for periodic u)")
