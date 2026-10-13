"""R18-5 (a): Lemma-F forward test and C2 covariance for Dirac TT vertices on 4-comp Wilson-Dirac D1 edges.
h(k) = sum_j s(k_j) alpha_j + M(k) beta, M = m + sum W(k_j).  E = |c|, c = (s_x, s_y, s_z, M).
p_j = d_j(E^2/2) = s_j s_j' + M W_j'.  v_j = p_j / E.
Vertices (q -> 0 operator Gamma_ij(k), Hermitian 4x4):
  V0  (R16-13, stipulated):  Gamma_ij = (1/2)(s_j alpha_i + s_i alpha_j)            [vielbein family D0, a = s]
  UD  (strain-flow vertex):  Gamma_ij = (1/2)(p_j d_i h + p_i d_j h)               [family D, a = p]
  V0* (forward-repaired V0): Gamma_ij = V0_ij + h (p_i p_j - s_i s_j)/E^2           [same q=0 pair block as V0]
Lemma F (R17-12, imported W1-s + H-sym + H-E): forward block must be  P+ G P+ = E v_i v_j P+,  P- G P- = -E v_i v_j P-.
Covariance: S^dag Gamma_ij(k) S = R_ii' R_jj' Gamma_i'j'(R^-1 k) with S the spin-1/2 lift (checked for C2y, C2x, C4z).
"""
import numpy as np, sys
sys.path.insert(0, '.')
from content3 import D1q
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
Z2 = np.zeros((2, 2))
al = [np.block([[Z2, s], [s, Z2]]) for s in (sx, sy, sz)]
be = np.block([[s0, Z2], [Z2, -s0]]).astype(complex)
Sig = [np.block([[s, Z2], [Z2, s]]) for s in (sx, sy, sz)]
def rot(axis, ang):
    from scipy.linalg import expm
    return expm(-0.5j*ang*Sig[axis])
def tabs(law, k):
    S, Sp, Spp, W, Wp, Wpp = law.tables(np.atleast_1d(np.array(k, float)))
    return S, Sp, W, Wp
def band(law, m, k):
    S, Sp, W, Wp = tabs(law, k)
    M = m + W.sum()
    c = np.array([S[0], S[1], S[2], M]); E = np.linalg.norm(c)
    p = S*Sp + M*Wp
    h = sum(c[j]*al[j] for j in range(3)) + M*be
    dh = [Sp[j]*al[j] + Wp[j]*be for j in range(3)]
    return dict(S=S, Sp=Sp, W=W, Wp=Wp, M=M, c=c, E=E, p=p, h=h, dh=dh)
def vert(B, name, i, j):
    S, p, h, dh, E = B['S'], B['p'], B['h'], B['dh'], B['E']
    if name == 'V0':
        return 0.5*(S[j]*al[i] + S[i]*al[j])
    if name == 'UD':
        return 0.5*(p[j]*dh[i] + p[i]*dh[j])
    if name == 'V0*':
        return 0.5*(S[j]*al[i] + S[i]*al[j]) + h*(p[i]*p[j] - S[i]*S[j])/E**2
def comps(B, name, comp):
    if comp == 'T2g': return vert(B, name, 0, 1)
    if comp == 'Eg': return 0.5*(vert(B, name, 0, 0) - vert(B, name, 1, 1))
    if comp == 'xx': return vert(B, name, 0, 0)
def req(B, comp):
    p, E = B['p'], B['E']
    if comp == 'T2g': return p[0]*p[1]/E
    if comp == 'Eg': return 0.5*(p[0]**2 - p[1]**2)/E
    if comp == 'xx': return p[0]**2/E
def proj(B):
    hh = B['h']/B['E']; I = np.eye(4)
    return 0.5*(I + hh), 0.5*(I - hh)
def forward_defect(law, m, k, name, comp):
    B = band(law, m, k); Pp, Pm = proj(B); G = comps(B, name, comp); r = req(B, comp)
    dp = np.linalg.norm(Pp@G@Pp - r*Pp, 2); dm = np.linalg.norm(Pm@G@Pm + r*Pm, 2)
    return max(dp, dm), abs(r)
def pair_weight(law, m, k, name, comp):
    B = band(law, m, k); Pp, Pm = proj(B); G = comps(B, name, comp)
    A = Pp@G@Pm
    return float(np.real(np.trace(A@A.conj().T))), A, B
rng = np.random.default_rng(7)
laws = {'D1(1.4,0.3) [R16-13 sign law]': (D1q(1.4, 0.3), 0.01),
        'D1(1.313475,0.572783) [vR16-13 root]': (D1q(1.313474886012, 0.572783392213), 0.01),
        'D1(0.916719,0.559627) [R17-13 zero]': (D1q(0.916719, 0.559627), 0.01)}
names = ['V0', 'UD', 'V0*']
print('== Lemma F forward test: max_k ||P+ G P+ - E v_i v_j P+||, ||P- G P- + E v_i v_j P-|| (operator 2-norm) ==')
for lname, (law, m) in laws.items():
    b = law.b
    for region in ('box |k_j|<b', 'off box (|k_x|>b)'):
        ks = []
        while len(ks) < 300:
            k = rng.uniform(-np.pi, np.pi, 3)
            inbox = np.all(np.abs(k) < b - 1e-3)
            offx = abs(k[0]) > b + 1e-3
            if (region.startswith('box') and inbox) or (region.startswith('off') and offx): ks.append(k)
        row = []
        for nm in names:
            for comp in ('T2g', 'Eg', 'xx'):
                d = [forward_defect(law, m, k, nm, comp) for k in ks]
                mx = max(x[0] for x in d); sc = max(x[1] for x in d)
                row.append('%s %s %.2e (scale %.2e)' % (nm, comp, mx, sc))
        print('%s, %s, m=%g:' % (lname, region, m))
        for r_ in row: print('   ', r_)
# covariance: C2y: (kx,ky,kz)->(-kx,ky,-kz), tensor sign for xy and (xx-yy): T_xy -> -T_xy, Eg -> +Eg.
# C2x: (kx,ky,kz)->(kx,-ky,-kz): T_xy -> -T_xy, Eg -> +Eg.  C4z: (kx,ky)->(-ky,kx) [x->y, y->-x]: T_xy->-T_xy, Eg-> -Eg.
print('\n== Covariance: max ||S^dag G(k) S - sign * G(Rk)|| over 200 random k (proper rotations, spin-1/2 lift) ==')
ops = {'C2y': (rot(1, np.pi), lambda k: np.array([-k[0], k[1], -k[2]]), {'T2g': -1, 'Eg': +1}),
       'C2x': (rot(0, np.pi), lambda k: np.array([k[0], -k[1], -k[2]]), {'T2g': -1, 'Eg': +1}),
       'C4z': (rot(2, np.pi/2), lambda k: np.array([-k[1], k[0], k[2]]), {'T2g': -1, 'Eg': -1})}
law, m = laws['D1(0.916719,0.559627) [R17-13 zero]']
for nm in names:
    out = []
    for on, (Sm, Rk, sg) in ops.items():
        # check h covariance too
        for comp in ('T2g', 'Eg'):
            mx = 0.0
            for _ in range(200):
                k = rng.uniform(-np.pi, np.pi, 3)
                B1 = band(law, m, k); B2 = band(law, m, Rk(k))
                # S h(k) S^dag = h(Rk)
                G1 = comps(B1, nm, comp); G2 = comps(B2, nm, comp)
                mx = max(mx, np.linalg.norm(Sm@G1@Sm.conj().T - sg[comp]*G2, 2))
            out.append('%s/%s %.1e' % (on, comp, mx))
    print(' %-4s' % nm, '  '.join(out))
mxh = 0.0
for on, (Sm, Rk, sg) in ops.items():
    for _ in range(100):
        k = rng.uniform(-np.pi, np.pi, 3)
        mxh = max(mxh, np.linalg.norm(Sm@band(law, m, k)['h']@Sm.conj().T - band(law, m, Rk(k))['h'], 2))
print(' band covariance S h(k) S^dag = h(Rk): max %.1e' % mxh)
print('\n== Lemma-M face test (K_x = pi, K_z = 0): spin-summed q=0 pair weight tr[A A^dag], A = P+ G P- ==')
Sm = rot(1, np.pi)
for nm in names:
    for Ky in (0.3, 0.8, 1.5, 2.5):
        k = np.array([np.pi, Ky, 0.0])
        w, A, B = pair_weight(law, m, k, nm, 'T2g')
        oddA = np.linalg.norm(Sm.conj().T@A@Sm + A, 2)   # covariance at the fixed point requires S^dag A S = -A
        print(' %-4s T2g K=(pi,%.1f,0): tr AA^dag = %.4e   ||S^dag A S + A|| = %.1e' % (nm, Ky, w, oddA))
# scalar Lemma M contrast: S -> 1 forces A = -A = 0; spinor: S (x) S has a -1 eigenspace on pair labels
ev = np.linalg.eigvals(np.kron(Sm, Sm))
print(' eigenvalues of S(x)S on two-spinor labels (C2y):', np.round(np.sort_complex(ev), 6))
