"""C5 R10-5, script 2: graviton TT (T_2g = h_xy, q along z) one-loop speed coefficient Xi = (d_{q^2} + d_{omega^2}) Pi
for the paired edge-SUSY multiplet (8-comp Clifford-flat fermion + 8 real bosons on the same curve), two couplings:

 (Q)  'through Q' (SUSY-QM): fermions psi^dag dM psi with dM = h Gamma, Gamma = (S_x A_y + S_y A_x)/2 (Clifford-index vielbein);
      bosons 1/2 phi dM^2 phi with vertex  V(k+q,k) = 2 S_x S_y * 1  +  [M_z(k_z+q) - M_z(k_z)] Gamma   (spin term, O(q)).
      Static Pi(0,q) must be q-INDEPENDENT (exact SUSY: E_vac(h(z)) = 0 for every static h(z)).  Then Xi = beta.
 (M)  minimal: same fermion vertex, bosons only 2 S_x S_y (R9-9 class V, Theorem T: Xi_B = (1/32)<|V|^2 A_zz/eps^5> per real scalar).

Formulas (Pi = -chi + seagull; seagull is q- and omega-independent):
   chi_B(0,q) = 1/4 < tr[V V^dag] / (e e' (e + e')) >      (8 real bosons; tr over the 8 components)
   chi_F(0,q) = < 2 t(k,k') / (E + E') > ,  t = tr[P+(k') Gamma P-(k) Gamma]   (one 8-comp field)
   t = 1/2 (s_x+s_y) - 4 s_x s_y/(E E') + 1/2 (s_x+s_y)(E_perp^2 + S_z S_z' + W_z W_z')/(E E')
   tr[V V^dag] = 32 s_x s_y + 2 (s_x+s_y) |c_z(k_z+q) - c_z(k_z)|^2 ,  c = (S, W)
   d_{omega^2} chi at q=0: bosons <s_x s_y/E^5>, fermions <(s_x+s_y)/(4E^3) - s_x s_y/E^5>.
alpha = d_{q^2} Pi(0,q) from exact grid shifts q = 2 pi n/N, n = 1,2,4, Richardson.  Units: lattice, per multiplet.
c_T^2 - 1 = 2 kappa_lat Xi,  kappa_lat = 8 pi (l_P/a)^2  (R9-9 normalization; same vertex normalization |V|^2 = 4 u_x u_y).
"""
import numpy as np, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve
t0 = time.time()

def run(cur, m, N, check_t=True):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W = cur['S'](k), cur['W'](k)
    s = S * S; v = S * S + W * W
    IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
    sx, sy = s[IX], s[IY]
    Ep2 = m * m + v[IX] + v[IY]
    E = np.sqrt(Ep2 + v[IZ])
    def chis(n):
        Zs = (IZ + n) % N
        E2 = np.sqrt(Ep2 + v[Zs])
        dc2 = (S[Zs] - S[IZ]) ** 2 + (W[Zs] - W[IZ]) ** 2
        trVV_min = 32 * sx * sy
        trVV_Q = trVV_min + 2 * (sx + sy) * dc2
        chiB_min = 0.25 * np.mean(trVV_min / (E * E2 * (E + E2)))
        chiB_Q = 0.25 * np.mean(trVV_Q / (E * E2 * (E + E2)))
        t = 0.5 * (sx + sy) - 4 * sx * sy / (E * E2) + 0.5 * (sx + sy) * (Ep2 + S[IZ] * S[Zs] + W[IZ] * W[Zs]) / (E * E2)
        chiF = np.mean(2 * t / (E + E2))
        return chiB_min, chiB_Q, chiF
    c0 = chis(0)
    res = {}
    for lab, idx in [('B_min', 0), ('B_Q', 1), ('F', 2)]:
        d = []
        for n in (1, 2, 4):
            q = 2 * np.pi * n / N
            d.append(-(chis(n)[idx] - c0[idx]) / q ** 2)       # alpha = d_{q^2} Pi = -d_{q^2} chi
        r1 = (4 * d[0] - d[1]) / 3; r2 = (4 * d[1] - d[2]) / 3
        res['a_' + lab] = (16 * r1 - r2) / 15
        res['raw_' + lab] = d[0]
    res['b_B'] = -np.mean(sx * sy / E ** 5)
    res['b_F'] = -np.mean((sx + sy) / (4 * E ** 3) - sx * sy / E ** 5)
    # Theorem T moment for the bosons (minimal), A_zz = v''(k_z)/2 - 1
    h = 1e-4
    vpp = ((cur['S'](k + h) ** 2 + cur['W'](k + h) ** 2) - 2 * v + (cur['S'](k - h) ** 2 + cur['W'](k - h) ** 2)) / h ** 2
    Azz = (vpp / 2 - 1)[IZ]
    res['XiB_T'] = np.mean(sx * sy * Azz / E ** 5)            # 8 real scalars x (1/32)|V|^2, |V|^2 = 4 s_x s_y : 8*(1/32)*4 = 1
    # predicted total for minimal pairing: Xi_min = <g (|c'(k_z)|^2 - 1)/E^3>, g = Gamma^2 = (s_x+s_y)/4
    cp2 = (cur['Sp'](k) ** 2 + cur['Wp'](k) ** 2)[IZ]
    res['Xi_pred'] = np.mean(0.25 * (sx + sy) * (cp2 - 1) / E ** 3)
    res['XiF_box'] = None
    return res

curves = [('Wilson circle', wilson_curve()), ('box b1=0.5', make_box_curve(0.5, 1.2)), ('box b1=0.8', make_box_curve(0.8, 1.6)),
          ('CONTROL r=0.5 (not unit speed)', dict(S=np.sin, W=lambda k: 0.5 * (1 - np.cos(k)), Sp=np.cos, Wp=lambda k: 0.5 * np.sin(k)))]
print('per multiplet (8-comp fermion + 8 real bosons), lattice units; alpha by grid shifts + Richardson')
print('curve | m | N | alpha_Q(total) | Xi_Q = alpha_Q + beta | alpha_B,min | Xi_B,min (direct) | Xi_B Theorem T | alpha_F | Xi_F | Xi_min = Xi_B + Xi_F')
for lab, cur in curves:
    for m, N in [(0.3, 96), (0.3, 160), (0.1, 160)]:
        r = run(cur, m, N)
        aQ = r['a_B_Q'] + r['a_F']; bt = r['b_B'] + r['b_F']
        XiB = r['a_B_min'] + r['b_B']; XiF = r['a_F'] + r['b_F']
        print('%-13s | %.2f | %3d | %+.2e | %+.5f | %+.5f | %+.6f | %+.6f | %+.5f | %+.6f | %+.2e (pred %+.2e)' % (
            lab, m, N, aQ, aQ + bt, r['a_B_min'], XiB, r['XiB_T'], r['a_F'], XiF, XiB + XiF, r['Xi_pred']), flush=True)
print('elapsed %.1fs' % (time.time() - t0))
