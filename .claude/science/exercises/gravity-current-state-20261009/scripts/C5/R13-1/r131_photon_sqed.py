"""R13-1 (c), photon leg: one-loop photon speed coefficient dc_gamma in minimal N=1 box SQED on Z^3 x R.

Matter multiplet forced by an untwisted spinor supercharge with P = p(k) (free level, see report section 3.1):
  electron: 4-component Dirac h(k) = sum_j S(k_j) alpha_j + beta M(k),  M(k) = m + sum_j W(k_j)   (= R8-5's BQ law)
  selectrons: two complex scalars with eps(k)^2 = E(k)^2 = sum_j S(k_j)^2 + M(k)^2              (matched, 'SUSY')
  scalar gauging = the D1-supersymmetric (factorized) one:  K_A = sum_j S_j(A)^2 + M(A)^2 , S_j(A), W_j(A) Peierls.
     For A_y with q along x (q_y = 0) the vertex is  G(k+q,k) = 2 S(k_y) S'(k_y) + W'(k_y) [M(k) + M(k+q)]
     and the seagull is q-independent (so Ward-subtracted P_M = [chi(0) - chi(q)]/q^2 is exact, cf. R10-1).
  literal edge: r = 0 (W = 0; doublers at mass m);  gapped edge: r > 0 (R8-5 Wilson edge, shared beta).
Photon one-loop at this order: electron loop + 2 selectron loops (photino does not couple at one loop).
dc_gamma = (P_M - P_E)/2 per e^2, printed x16pi^2 (R8-5 units).
Checks: literal edge vs R10-1 moment formulas (Theorem D with c1 = c2 = 0, Theorem T').
"""
import numpy as np, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r85_box_qed_copy import Law, photon, deriv

U = 16 * np.pi ** 2

def selectron(law, N, ns=(1, 2, 4), dm2=0.0):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W = law.S(k), law.W(k)
    Sp, Wp = deriv(law.S, k), deriv(law.W, k)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    def M(sx):
        return law.m + W[(IX + sx) % N] + W[IY] + W[IZ]
    def eps(sx):
        return np.sqrt(S[(IX + sx) % N] ** 2 + S[IY] ** 2 + S[IZ] ** 2 + M(sx) ** 2 + dm2)
    e0, M0 = eps(0), M(0)
    G0 = 2 * S[IY] * Sp[IY] + Wp[IY] * 2 * M0
    PE = np.mean(G0 ** 2 / e0 ** 5) / 16
    chi0 = np.mean(G0 ** 2 / (4 * e0 ** 3))
    PMs = []
    for s in ns:
        tot = 0.0
        for sg in (+1, -1):
            e1 = eps(sg * s)
            G = 2 * S[IY] * Sp[IY] + Wp[IY] * (M0 + M(sg * s))
            tot += 0.5 * np.mean(G ** 2 / (2 * e0 * e1 * (e0 + e1)))
        PMs.append((chi0 - tot) / (2 * np.pi * s / N) ** 2)
    r1 = (4 * PMs[0] - PMs[1]) / 3; r2 = (4 * PMs[1] - PMs[2]) / 3
    PM = (16 * r1 - r2) / 15
    return (PM - PE) / 2, PE

def literal_moments(law, N):
    """R10-1 Theorem D (c1=c2=0 since W=0) and Theorem T' for u = S^2: per-4-comp Dirac and per complex scalar."""
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, Sp, Spp = law.S(k), deriv(law.S, k), deriv(law.S, k, 2)
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    E = np.sqrt(S[IX] ** 2 + S[IY] ** 2 + S[IZ] ** 2 + law.m ** 2)
    a = Sp[IX] ** 2 - 1
    A = a + S[IX] * Spp[IX]
    x2 = Sp[IY] ** 2
    X = Sp[IY] * S[IY]
    dirac = np.mean(a * x2 / (4 * E ** 3) - A * X ** 2 / (4 * E ** 5))
    scal = np.mean((2 * X) ** 2 * A / E ** 5) / 32
    amom = np.mean(a * x2 / (4 * E ** 3))
    return dirac, scal, amom

if __name__ == '__main__':
    t0 = time.time()
    shapes = [('S1', 1.0, 2.0), ('S3', 2.0, 3.0), ('S5', 0.5, 1.5), ('S7', 1.0, 3.0)]
    print('minimal N=1 box SQED, photon coefficient x16pi^2 (per e^2): Dirac(4) + 2 complex selectrons, matched E')
    print('shape | edge r | m | N | dc(Dirac) | dc(selectron, each) | TOTAL Dirac+2sel | [literal: moment Dirac, moment sel, a-moment]')
    for lab, b1, b2 in shapes:
        for r in (0.0, 1.0):
            for (m, N) in [(0.2, 64), (0.2, 96)]:
                law = Law(b1, b2, r, b1, b2, m)
                ph = photon(law, N)
                dS, pS = selectron(law, N)
                tot = ph['dcg'] + 2 * dS
                extra = ''
                if r == 0.0:
                    md, ms, am = literal_moments(law, N)
                    extra = ' | mom D %+.4f  mom sel %+.4f  a-mom %+.4f' % (U * md, U * ms, U * am)
                print('%s | %.1f | %.2f | %3d | %+9.4f | %+9.4f | %+9.4f%s' % (
                    lab, r, m, N, U * ph['dcg'], U * dS, U * tot, extra), flush=True)
    # Wilson control (no box) and Clifford-flat reminder
    for r in (1.0,):
        for (m, N) in [(0.2, 96)]:
            law = Law(None, None, r, None, None, m)
            ph = photon(law, N); dS, _ = selectron(law, N)
            print('Wilson no-box | %.1f | %.2f | %3d | %+9.4f | %+9.4f | %+9.4f' % (r, m, N, U * ph['dcg'], U * dS, U * (ph['dcg'] + 2 * dS)))
    print('elapsed %.1fs' % (time.time() - t0))
