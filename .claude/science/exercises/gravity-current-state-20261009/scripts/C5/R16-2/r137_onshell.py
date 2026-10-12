"""R13-7: ON-SHELL one-loop electron speed c_e(m) in R8-5's box QED (BQ), Feynman gauge, photon mass lam,
as a function of the electron mass m over a wide range (light -> heavy), plus the photon coefficient c_gamma(m)
from R10-1's refereed Theorem-D moment (one Dirac species = the electron itself, the only charged loop).

Self-energy: R8-5's refereed Euclidean form (r85_box_qed.py docstring; referee-confirmed),
  Sigma(p0,p) = -<sum_s s [sum_j delta_j P_s(k) delta_j / d_j^2 - P_s(k)] / (2W (W + E_k - i s p0))>_q + T(p),
  k = p - q, delta_j = h_j(p_j) - h_j(k_j) (Clifford vector: alpha_j comp S, beta comp W), P_s = (1 + s n_k.Gamma)/2,
  W = sqrt(sum_j d(q_j)^2 + lam^2),  T(p) = 1/2 sum_j < [h_j(p_j+q_j)+h_j(p_j-q_j)-2h_j(p_j)] / (d(q_j)^2 2W) >_q.
Convention fixed by R8-5: Sigma = (-i p0) A + B alpha.p + ...,  dc_e(off-shell, p0=0) = B - A.
On shell: G^{-1} ~ -i p0 + h + Sigma vanishes at p0 = -iE, so the denominator W + E_k - i s p0 -> W + E_k - s E_p,
and delta E(p) = (1/2) Tr[P_+(p) Sigma(-iE_p, p)] (first order; the two positive states are degenerate on the axis).
Clifford traces: with a = n_p, b = n_k,  <delta P_s delta> = [|d|^2 + s(2(d.b)(d.a) - |d|^2 a.b)]/2,  <P_s> = (1+s a.b)/2.
Speed: F(p) = 2 E_p delta E(p) (tree E_p^2 = m^2 + p^2 in the box), c_e^2 - 1 = dF/d(p^2) at p = 0 (Richardson).
VALIDATION: at small m the on-shell speed must approach R8-5's off-shell B - A (same law, same lam).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r85_box_qed_copy import Law, kgrid1, fermion, deriv
from r101_dirac_moment_copy import moment

U = 16 * np.pi ** 2

def dE_onshell(law, N, lam, ps, chunk=8):
    q1 = kgrid1(N)
    QY, QZ = np.meshgrid(q1, q1, indexing='ij')
    dy2, dz2 = law.d(QY) ** 2, law.d(QZ) ** 2
    out = {}
    for p in ps:
        # external p = (p,0,0): a = n_p
        Sp, Wp = law.S(np.array(p)), law.W(np.array(p))
        W0 = law.W(np.array(0.0))
        hp = np.array([Sp, 0.0, 0.0, law.m + Wp + 2 * W0])
        Ep = np.sqrt(hp @ hp); a = hp / Ep
        # y,z parts: k_j = -q_j, delta_j = h_j(0) - h_j(-q_j)
        Sy, Wy, Sz, Wz = law.S(-QY), law.W(-QY), law.S(-QZ), law.W(-QZ)
        dly = (0.0 - Sy, W0 - Wy); dlz = (0.0 - Sz, W0 - Wz)
        acc = 0.0; tad = 0.0
        for i0 in range(0, N, chunk):
            qx = q1[i0:i0 + chunk][:, None, None]
            dx2 = law.d(qx) ** 2
            Wq = np.sqrt(dx2 + dy2[None] + dz2[None] + lam ** 2)
            kx = p - qx
            hk = [law.S(kx) + 0 * Wq, Sy[None] + 0 * Wq, Sz[None] + 0 * Wq,
                  law.m + law.W(kx) + Wy[None] + Wz[None] + 0 * Wq]
            Ek = np.sqrt(hk[0] ** 2 + hk[1] ** 2 + hk[2] ** 2 + hk[3] ** 2)
            b = [c / Ek for c in hk]
            ab = a[0] * b[0] + a[3] * b[3]          # a has only x and beta comps
            # delta_x: (alpha_x comp, beta comp); delta_y: (alpha_y, beta); delta_z: (alpha_z, beta)
            dxa = Sp - law.S(kx); dxb = Wp - law.W(kx)
            terms_s = {}
            for s in (+1, -1):
                # x
                d2 = dxa ** 2 + dxb ** 2
                db = dxa * b[0] + dxb * b[3]; da = dxa * a[0] + dxb * a[3]
                X = (d2 + s * (2 * db * da - d2 * ab)) / (2 * dx2)
                # y
                d2y = (dly[0] ** 2 + dly[1] ** 2)[None]
                dby = dly[0][None] * b[1] + dly[1][None] * b[3]; day = dly[1][None] * a[3]
                X = X + (d2y + s * (2 * dby * day - d2y * ab)) / (2 * dy2[None])
                d2z = (dlz[0] ** 2 + dlz[1] ** 2)[None]
                dbz = dlz[0][None] * b[2] + dlz[1][None] * b[3]; daz = dlz[1][None] * a[3]
                X = X + (d2z + s * (2 * dbz * daz - d2z * ab)) / (2 * dz2[None])
                X = X - (1 + s * ab) / 2
                acc += np.sum(-s * X / (2 * Wq * (Wq + Ek - s * Ep)))
            # tadpole: a . (1/2) sum_j [h_j(p_j+q_j)+h_j(p_j-q_j)-2h_j(p_j)]/(d_j^2 2W)
            tx = a[0] * (law.S(p + qx) + law.S(p - qx) - 2 * Sp) + a[3] * (law.W(p + qx) + law.W(p - qx) - 2 * Wp)
            ty = a[3] * (law.W(QY) + law.W(-QY) - 2 * W0)[None]
            tz = a[3] * (law.W(QZ) + law.W(-QZ) - 2 * W0)[None]
            tad += np.sum(0.5 * (tx / dx2 + ty / dy2[None] + tz / dz2[None]) / (2 * Wq))
        V = N ** 3
        out[p] = dict(Ep=Ep, dE=(acc + tad) / V, sun=acc / V, tad=tad / V)
    return out

def ce2_minus_1(law, N, lam, h=0.02):
    r = dE_onshell(law, N, lam, [0.0, h, 2 * h])
    F = {p: 2 * r[p]['Ep'] * r[p]['dE'] for p in r}
    D1 = (F[h] - F[0.0]) / h ** 2; D2 = (F[2 * h] - F[0.0]) / (4 * h ** 2)
    Ft = {p: 2 * r[p]['Ep'] * r[p]['tad'] for p in r}
    T1 = (Ft[h] - Ft[0.0]) / h ** 2; T2 = (Ft[2 * h] - Ft[0.0]) / (4 * h ** 2)
    return (4 * D1 - D2) / 3, (4 * T1 - T2) / 3, r[0.0]['dE']

if __name__ == '__main__':
    t0 = time.time()
    mode = sys.argv[1] if len(sys.argv) > 1 else 'validate'
    if mode == 'validate':
        print('VALIDATION: on-shell dc_e = (c_e^2-1)/2 vs R8-5 off-shell B-A (lam = m), x16pi^2')
        for lab, b1, b2, r, c1, c2 in [('S1', 1.0, 2.0, 1.0, 1.0, 2.0), ('naive', None, None, 0.0, None, None)]:
            for m, N in [(0.2, 48), (0.1, 64), (0.05, 96)]:
                law = Law(b1, b2, r, c1, c2, m, naive_photon=(lab == 'naive'))
                ce, ct, dE0 = ce2_minus_1(law, N, lam=m)
                off = fermion(law, N, lam=m)
                print('%-6s m=%.3f N=%3d  onshell dc_e*U = %+9.4f   offshell(B-A)*U = %+9.4f   [tadpole part on-shell %+8.4f]'
                      % (lab, m, N, ce / 2 * U, off['dce'] * U, ct / 2 * U), flush=True)
        print('elapsed %.1fs' % (time.time() - t0))
