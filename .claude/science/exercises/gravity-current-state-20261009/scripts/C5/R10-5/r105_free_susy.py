"""C5 R10-5, script 1: the free 'edge-SUSY' box multiplet as an exact lattice supercharge (SUSY-QM / Nicolai form).

Claim (Theorem Q): R10-1's Theorem-P content (8-component Clifford-flat fermion + 8 real = 4 complex scalars on the
same edge curve) is exactly the free multiplet of Q = sum_a psi_a^dag (p_a - i (M phi)_a), with M a REAL SYMMETRIC
quasi-local operator on 8 real components per site:
   M(k) = sum_j [ S(k_j) A_j + W(k_j) B_j ] + m B_0 ,
A_j (j=x,y,z) imaginary antisymmetric, B_j, B_0 real symmetric, 7 mutually anticommuting, squaring to 1
(a real 8-dim representation of Cl(4,3) = M_8(R) + M_8(R)).  Then Q^2 = 0 and {Q,Q^dag} = 2H with
   H = 1/2 [p^2 + phi M^2 phi] + psi^dag M psi - 1/2 tr M .
Checks here (numerical, all exact identities up to rounding):
  (1) the 7 generators exist (search over 3-qubit Pauli strings) and satisfy the reality/symmetry pattern;
  (2) M(k)^2 = E(k)^2 * 1 with E^2 = m^2 + sum_j v(k_j), v = S^2 + W^2 (R10-1 box curves and Wilson circle);
      real-space realness: M(-k) = conj(M(k));
  (3) vacuum energy per site: 8 real bosons (1/2)<E> - (1/2)<sum|eig M|> = 0; mass-split residual vs 2<1/E> dm^2;
  (4) uniform static TT strain through Q (M -> M + h Gamma, Gamma = (S_x A_y + S_y A_x)/2): pointwise-in-k cancellation
      of boson paramagnetic + seagull + fermion paramagnetic second-order energies;  t(k) = tr[P+ G P- G] formula;
  (5) the dynamic coefficient beta = d Pi / d omega^2 (q=0) for the through-Q coupling: -<(s_x+s_y)/(4E^3)> != 0.
"""
import numpy as np, itertools, sys, time
sys.path.insert(0, '.')
from r101_pairing import make_box_curve, wilson_curve

t0 = time.time()
I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)
P = {'I': I2, 'X': X, 'Y': Y, 'Z': Z}
strings = [''.join(s) for s in itertools.product('IXYZ', repeat=3) if ''.join(s) != 'III']
def mat(s):
    return np.kron(np.kron(P[s[0]], P[s[1]]), P[s[2]])
odd = [s for s in strings if s.count('Y') % 2 == 1]     # imaginary antisymmetric
even = [s for s in strings if s.count('Y') % 2 == 0]    # real symmetric
def anticomm(a, b):
    ma, mb = mat(a), mat(b)
    return np.allclose(ma @ mb + mb @ ma, 0)
found = None
for Aset in itertools.combinations(odd, 3):
    if not all(anticomm(a, b) for a, b in itertools.combinations(Aset, 2)):
        continue
    cand = [s for s in even if all(anticomm(s, a) for a in Aset)]
    for Bset in itertools.combinations(cand, 4):
        if all(anticomm(a, b) for a, b in itertools.combinations(Bset, 2)):
            found = (Aset, Bset); break
    if found: break
Aset, Bset = found
A = [mat(s) for s in Aset]; B = [mat(s) for s in Bset[:3]]; B0 = mat(Bset[3])
print('(1) Cl(4,3) real 8-dim generators: A_j =', Aset, ' B_j =', Bset[:3], ' B0 =', Bset[3])
gens = A + B + [B0]
err_ac = max(np.abs(g @ h + h @ g - (2 * np.eye(8) if i == j else 0)).max() for i, g in enumerate(gens) for j, h in enumerate(gens))
print('    max |{G_i,G_j} - 2 delta_ij| = %.1e ; A imaginary-antisym: %s ; B real-sym: %s' % (
    err_ac, all(np.allclose(a.real, 0) and np.allclose(a, -a.T) for a in A),
    all(np.allclose(b.imag, 0) and np.allclose(b, b.T) for b in B + [B0])))

def Mk(cur, k, m):
    kx, ky, kz = k
    out = m * B0.astype(complex)
    for j, kj in enumerate((kx, ky, kz)):
        out = out + cur['S'](np.array(kj)) * A[j] + cur['W'](np.array(kj)) * B[j]
    return out

curves = [('Wilson circle', wilson_curve()), ('box b1=0.5', make_box_curve(0.5, 1.2)), ('box b1=0.8', make_box_curve(0.8, 1.6))]
rng = np.random.default_rng(1)
print('(2) M^2 = E^2 and reality, 2000 random k per curve (m = 0.3):')
for lab, cur in curves:
    e1 = e2 = 0.0
    for _ in range(2000):
        k = rng.uniform(-np.pi, np.pi, 3)
        Mm = Mk(cur, k, 0.3)
        E2 = 0.09 + sum(cur['S'](np.array(x)) ** 2 + cur['W'](np.array(x)) ** 2 for x in k)
        e1 = max(e1, np.abs(Mm @ Mm - E2 * np.eye(8)).max())
        e2 = max(e2, np.abs(Mk(cur, -k, 0.3) - Mm.conj()).max())
    print('    %-14s max|M^2 - E^2| = %.1e   max|M(-k) - conj M(k)| = %.1e' % (lab, e1, e2))

def grid(cur, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    S, W = cur['S'](k), cur['W'](k)
    return k, S, W

print('(3) vacuum energy per site (lattice units), separable sums on an N^3 grid:')
for lab, cur in curves:
    for N in (48, 96):
        k, S, W = grid(cur, N)
        v = S ** 2 + W ** 2
        IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
        vs = v[IX] + v[IY] + v[IZ]
        out = []
        for mf, ms in [(0.3, 0.3), (0.05, 0.05), (0.3, 0.3 + 1e-3)]:
            Ef, Es = np.sqrt(mf ** 2 + vs), np.sqrt(ms ** 2 + vs)
            Evac = 8 * 0.5 * Es.mean() - 0.5 * 8 * Ef.mean()      # 8 real bosons ; fermion: eig M = +-E, 4 each -> sum|eig| = 8E
            pred = 2 * np.mean(1 / Ef) * (ms ** 2 - mf ** 2)
            out.append('m_f=%.2f m_s=%.4f: E_vac=%+.3e (pred 2<1/E>dm^2 = %+.3e)' % (mf, ms, Evac, pred))
        print('    %-14s N=%3d | ' % (lab, N) + ' | '.join(out))
# direct eigenvalue check of the fermion sea at random k (not assuming the Clifford algebra)
cur = curves[2][1]
dev = 0.0
for _ in range(500):
    k = rng.uniform(-np.pi, np.pi, 3)
    lam = np.linalg.eigvalsh(Mk(cur, k, 0.3))
    E = np.sqrt(0.09 + sum(cur['S'](np.array(x)) ** 2 + cur['W'](np.array(x)) ** 2 for x in k))
    dev = max(dev, abs(0.5 * 8 * E - 0.5 * np.sum(np.abs(lam))), abs(np.sum(lam)))
print('    direct eig check (box b1=0.8): max |bosons - fermion sea| per k = %.1e (tr M = 0 included)' % dev)

print('(4) uniform static TT strain h_xy through Q: second-order energy per k, bosons vs fermions (random k, m=0.3):')
G = lambda k, cur: 0.5 * (cur['S'](np.array(k[0])) * A[1] + cur['S'](np.array(k[1])) * A[0])
worst = 0.0; worst_t = 0.0
for _ in range(500):
    k = rng.uniform(-np.pi, np.pi, 3)
    Mm = Mk(cur, k, 0.3); Gm = G(k, cur)
    E = np.sqrt(np.linalg.eigvalsh(Mm @ Mm).max())
    sx, sy = cur['S'](np.array(k[0])) ** 2, cur['S'](np.array(k[1])) ** 2
    Pp = 0.5 * (np.eye(8) + Mm / E); Pm = 0.5 * (np.eye(8) - Mm / E)
    t_num = np.trace(Pp @ Gm @ Pm @ Gm).real
    t_ana = (sx + sy) - 4 * sx * sy / E ** 2
    worst_t = max(worst_t, abs(t_num - t_ana))
    # exact: E_vac(h) = 1/2 sum|eig M(h)| (bosons) - 1/2 sum|eig M(h)| (fermions) = 0 identically; check 2nd-order pieces
    VB = 2 * cur['S'](np.array(k[0])) * cur['S'](np.array(k[1]))
    e_bos = 8 * (-VB ** 2 / (16 * E ** 3) + (sx + sy) / (16 * E))     # paramagnetic + seagull, 8 real scalars
    e_fer = -t_num / (2 * E)
    worst = max(worst, abs(e_bos + e_fer))
print('    max |t_numeric - [(s_x+s_y) - 4 s_x s_y/E^2]| = %.1e ;  max |E2_bos + E2_fer| per k = %.1e' % (worst_t, worst))

print('(5) beta = d Pi/d omega^2 at q=0 (TT T_2g, through-Q coupling) per multiplet, and its pieces; alpha_throughQ == 0 exactly:')
for lab, cur in curves:
    for m, N in [(0.3, 96), (0.05, 96), (0.05, 160)]:
        k, S, W = grid(cur, N)
        s = S ** 2; v = S ** 2 + W ** 2
        IX, IY, IZ = np.meshgrid(np.arange(N), np.arange(N), np.arange(N), indexing='ij')
        E = np.sqrt(m * m + v[IX] + v[IY] + v[IZ])
        sx, sy = s[IX], s[IY]
        bB = -np.mean(sx * sy / E ** 5)                       # 8 real bosons, standard vertex 2 S_x S_y
        bF = -np.mean((sx + sy) / (4 * E ** 3) - sx * sy / E ** 5)
        print('    %-14s m=%.2f N=%3d | beta_B=%+.5f beta_F=%+.5f beta_total=%+.5f (= -<(sx+sy)/4E^3>) | inner-cube part of beta_total (all |k_i|<0.5, inside every box): %+.5f' % (
            lab, m, N, bB, bF, bB + bF,
            -np.mean(np.where((np.abs(k[IX]) < 0.5) & (np.abs(k[IY]) < 0.5) & (np.abs(k[IZ]) < 0.5), (sx + sy) / (4 * E ** 3), 0.0))))
print('elapsed %.1fs' % (time.time() - t0))
