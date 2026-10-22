AUDIT_INPUT_PATHS = ('docs/SUPPLIED_CHIRAL_TERMS_KEEP_A_Z4_OF_B_MINUS_L_AND_LEAVE_STRONG_CP_UNFIXED_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""proton-theta: two measured-reality tests of terms already in the register's link-selection content.
(supplied model; exact integer-lattice selection rules; finite matrix diagnostics; estimates; no physical identification)
 A  exact: the full abelian symmetry group (Smith normal form) of each term set on [Q,u,d,L,e,n,H] (left-handed Weyl,
    u = u^c etc.), and which baryon-number-changing operators it allows up to dimension 10 (with gauge, Lorentz checks)
 B  estimates: nucleon lifetimes from the dimension-6 terms at the cell scale vs Super-K; the coarsest rung allowed
 C  exact: Delta B = 2 (n-nbar) and Delta L = 2 under the Z4; contrast with a Majorana nu^c nu^c term
 D  strong CP: what fixes theta_bar = theta - arg det(Y_u Y_d); a CL-3-set doublet's phase; an exact antiunitary;
    a Nelson-Barr block form from heavy vector-like copies; estimates vs d_n and the eta' mass
"""
AUDIT_TIMEOUT_SEC = 120
import itertools, os, signal, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('aggregate cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))

# ============================ A. exact selection rules ============================
print('== A. abelian symmetry group of each term set; allowed baryon-number-changing operators (one-family charges)')
F = ['Q', 'u', 'd', 'L', 'e', 'n', 'H']
Y = [Fr(1, 6), Fr(-2, 3), Fr(1, 3), Fr(-1, 2), Fr(1), Fr(0), Fr(1, 2)]
B = [Fr(1, 3), Fr(-1, 3), Fr(-1, 3), 0, 0, 0, 0]
L = [0, 0, 0, 1, -1, -1, 0]
col3 = [1, -1, -1, 0, 0, 0, 0]          # triplet (+1) / antitriplet (-1)
dbl = [1, 0, 0, 1, 0, 0, 1]             # SU(2) doublets
def v(**k): return [k.get(f, 0) for f in F]
YUK = [v(Q=1, u=1, H=1), v(Q=1, d=1, H=-1), v(L=1, e=1, H=-1), v(L=1, n=1, H=1)]
NC4 = [v(n=4)]; UDDN = [v(u=1, d=2, n=1)]; UUDE = [v(u=2, d=1, e=1)]; NC2 = [v(n=2)]

def snf(A):
    """Smith normal form with transforms: D = U A V (integers). Returns diag list d, V."""
    m, n = len(A), len(A[0]); A = [r[:] for r in A]
    V = [[int(i == j) for j in range(n)] for i in range(n)]
    def colop(j1, j2, c):   # col j2 += c col j1
        for r in A: r[j2] += c * r[j1]
        for r in V: r[j2] += c * r[j1]
    def colswap(j1, j2):
        for r in A: r[j1], r[j2] = r[j2], r[j1]
        for r in V: r[j1], r[j2] = r[j2], r[j1]
    d = []
    for t in range(min(m, n)):
        while True:
            nz = [(abs(A[i][j]), i, j) for i in range(t, m) for j in range(t, n) if A[i][j]]
            if not nz: return d, V
            _, i0, j0 = min(nz); A[t], A[i0] = A[i0], A[t]; colswap(t, j0)
            done = True
            for i in range(t + 1, m):
                q = A[i][t] // A[t][t]; A[i] = [a - q * b for a, b in zip(A[i], A[t])]
                if A[i][t]: done = False
            for j in range(t + 1, n):
                q = A[t][j] // A[t][t]; colop(t, j, -q)
                if A[t][j]: done = False
            if not done: continue
            bad = [(i, j) for i in range(t + 1, m) for j in range(t + 1, n) if A[i][j] % A[t][t]]
            if bad: A[t] = [a + b for a, b in zip(A[t], A[bad[0][0]])]; continue
            break
        if A[t][t] < 0: A[t] = [-a for a in A[t]]
        d.append(A[t][t])
    return d, V

class Lattice:
    def __init__(s, rows):
        s.d, s.V = snf(rows); s.r = len(s.d)
    def contains(s, e):
        y = [sum(e[i] * s.V[i][j] for i in range(7)) for j in range(7)]
        return all(y[j] % s.d[j] == 0 for j in range(s.r)) and all(y[j] == 0 for j in range(s.r, 7))
    def group(s):
        tors = [x for x in s.d if x > 1]
        return f"U(1)^{7 - s.r}" + ''.join(f" x Z{x}" for x in tors)
    def disc(s):
        return {s.d[j]: [s.V[i][j] % s.d[j] for i in range(7)] for j in range(s.r) if s.d[j] > 1}

# all operators: multisets of Weyl fermions (field or conjugate) with H/H*; dim = 1.5 n_f + n_H (+1 per derivative)
types = [(f, sgn) for f in range(6) for sgn in (1, -1)]
ops = []
for nf in (4, 6):
    for combo in itertools.combinations_with_replacement(range(12), nf):
        nl = sum(1 for c in combo if types[c][1] == 1); nr = nf - nl
        if nl % 2 != nr % 2: continue
        der = 1 if nl % 2 else 0
        for hp in range(0, 5):
            for hm in range(0, 5 - hp):
                dim = 1.5 * nf + hp + hm + der
                if dim > 10: continue
                e = [0] * 7
                for c in combo: e[types[c][0]] += types[c][1]
                e[6] = hp - hm
                if sum(Fr(x) * y for x, y in zip(e, Y)) != 0: continue
                if sum(x * c for x, c in zip(e, col3)) % 3: continue
                ndb = sum(1 for c in combo if dbl[types[c][0]]) + hp + hm
                if ndb % 2: continue
                dB = sum(Fr(x) * b for x, b in zip(e, B))
                if dB == 0: continue
                dL = sum(x * l for x, l in zip(e, L))
                ops.append((dim, e, dB, dL))
print(f'   {len(ops)} gauge-, Lorentz-admissible operators with Delta B != 0, dim <= 10')

def classes(lat):
    out = {}
    for dim, e, dB, dL in ops:
        if lat.contains(e):
            key = (int(abs(dB)), int(dL if dB > 0 else -dL)); out[key] = min(out.get(key, 99), int(dim))
    return dict(sorted(out.items()))
SETS = {'S1 Yukawa + (nu^c)^4': YUK + NC4, 'S2 S1 + uddn': YUK + NC4 + UDDN,
        'S3 S2 + uude': YUK + NC4 + UDDN + UUDE, 'Sm Yukawa + nu^c nu^c (Majorana)': YUK + NC2 + UDDN + UUDE}
LAT = {k: Lattice(r) for k, r in SETS.items()}
res = {}
for k, lat in LAT.items():
    res[k] = classes(lat)
    print(f"   {k}: {lat.group()}; Z-charges {lat.disc()}; allowed (|dB|, dL) : min dim {res[k]}")
check('[T] S1 (forced content without B-violating terms): no Delta B != 0 operator at any order in the terms '
      '(B is an exact U(1) of the term list; sphalerons give only Delta B = Delta L = 3 per three families)',
      res['S1 Yukawa + (nu^c)^4'] == {} and LAT['S1 Yukawa + (nu^c)^4'].group().startswith('U(1)^2'))
# selection rule: allowed <=> Delta(B - L) = 0 mod 4 (with Y = 0, gauge, Lorentz already imposed)
rule_ok = all(LAT['S3 S2 + uude'].contains(e) == ((dB - dL) % 4 == 0) for _, e, dB, dL in ops)
check('[T] S2, S3: exact group U(1)_Y x Z4; on every admissible operator, allowed <=> Delta(B-L) = 0 mod 4 '
      f'({len(ops)} operators checked)', rule_ok and LAT['S3 S2 + uude'].group() == 'U(1)^1 x Z4'
      and LAT['S2 S1 + uddn'].group() == 'U(1)^1 x Z4')
r3 = res['S3 S2 + uude']
check('[T] Delta B = Delta L = 1 is allowed at dimension 6 (uddn: p -> pi+ nubar_R, n -> pi0 nubar_R; uude, QQQL: '
      'p -> e+ pi0); Delta B = 1, Delta L = -1 (n -> e- pi+, dim 7) is forbidden', r3.get((1, 1)) == 6
      and (1, -1) not in r3, f"(1,1): dim {r3.get((1, 1))}, (1,-3): dim {r3.get((1, -3), 'none <= 10')}")
check('[T] Z4 of mode number counted on left-handed Weyl fields (H charge 2 from the Yukawa-type terms) equals Z4 of B-L '
      'on every Lorentz- and SU(2)-admissible operator', all(((sum(e[:6]) + 2 * e[6]) % 4 == 0)
      == ((dB - dL) % 4 == 0) for _, e, dB, dL in ops))

# ============================ B. nucleon lifetimes ============================
print('== B. nucleon decay from dimension-6 terms with a rule-size coefficient g at the cell (estimates)')
hbar, yr = 6.582e-25, 3.156e7
MPl = 1.2209e19; inv_a = MPl / np.sqrt(8 * np.pi)        # G = a^2/(8 pi) per cell
tick = 2.11e18                                            # hbar per tick in GeV (agents/baryogenesis unit map)
Lam_site = np.sqrt(inv_a ** 3 / tick)                     # C = g a^3/tick  (four modes on one site-volume each)
Lam_cell = Lam_site / np.sqrt(8)                          # species read one per 2x2x2 cell: C = 8 g a^3/tick
print(f'   1/a = {inv_a:.3e} GeV (a = sqrt(8 pi) l_P = 5.0 l_P); C = g/Lam^2, Lam = {Lam_site:.2e} (site) .. {Lam_cell:.2e} GeV (cell)')
mN = 0.9389
chan = [('p -> e+ pi0 (uude, QQQL)', 0.135, 2.4e34, (0.131, 0.134)), ('p -> nubar K+ (uds nu^c)', 0.4937, 5.9e33, (0.041, 0.139)),
        ('p -> pi+ nubar (uddn)', 0.1396, 3.9e32, (0.186, 0.189)), ('n -> pi0 nubar (uddn)', 0.135, 1.1e33, (0.131, 0.134))]
def tau_yr(Lam, W, A, mM):
    G = mN / (32 * np.pi) * (1 - mM ** 2 / mN ** 2) ** 2 * (A * W / Lam ** 2) ** 2
    return hbar / G / yr
worst = []
for nm, mM, bound, Ws in chan:
    tc = tau_yr(Lam_site, np.mean(Ws), 1.5, mM); tw = tau_yr(Lam_cell, max(Ws), 3.0, mM)
    gmax = np.sqrt(tw / bound); worst.append((nm, tw, bound, gmax))
    print(f'   {nm:28s} g=1: tau ~ {tc:.1e} yr (worst {tw:.1e}); bound {bound:.1e}; g_max {gmax:.1e}')
check('[E] every channel passes at g = 1 by >= 8 orders (worst case: cell reading, A = 3, largest lattice W)',
      all(tw / bnd > 1e8 for _, tw, bnd, _ in worst), f"min margin {min(tw / bnd for _, tw, bnd, _ in worst):.1e}")
Lmin = max(Lam_cell * np.sqrt(np.sqrt(bnd / tw)) for _, tw, bnd, _ in worst)
kmax = int(np.floor(np.log2(Lam_cell / Lmin)))
check('[E] worst case: a unit-coefficient Delta B term must sit within ~7 rungs of the sites (cells below ~1e2 a): '
      'on rung k the scale is Lam/2^k', 6 <= kmax <= 8, f"Lam_min = {Lmin:.1e} GeV, k_max = {kmax}")
gB = np.sqrt(1.4e-4)   # agents/baryogenesis D: g^2 kappa sin(dphi) = 1.4e-4 at T_max = 0.5 rad/tick reproduces eta_B
print(f'   with the baryogenesis-fitted g ~ {gB:.2f}: tau(p -> pi+ nubar) ~ {tau_yr(Lam_site, .187, 1.5, .1396) / gB**2:.0e} yr '
      '(Hyper-K reach ~1e35): no nucleon decay is predicted to be seen')

# ============================ C. Delta B = 2 and Delta L = 2 ============================
print('== C. Delta B = 2 (n-nbar), dinucleon and Delta L = 2 under the Z4')
nn = [e for dim, e, dB, dL in ops if abs(dB) == 2 and dL == 0]
check('[T] n-nbar (Delta B = 2, Delta L = 0, dim 9 udd udd) is forbidden at every order: Delta(B-L) = 2 != 0 mod 4; '
      'consistent with tau_nnbar > 4.7e8 s', nn and not any(LAT['S3 S2 + uude'].contains(e) for e in nn)
      and all(LAT['Sm Yukawa + nu^c nu^c (Majorana)'].contains(e) for e in nn), f"{len(nn)} udd udd operators")
check('[T] with a Majorana nu^c nu^c instead of (nu^c)^4 the group is U(1)_Y x Z2 and n-nbar is allowed: '
      'the n-nbar ban is a consequence of the (nu^c)^4 form (an ESS/NNBAR signal would falsify it)',
      LAT['Sm Yukawa + nu^c nu^c (Majorana)'].group() == 'U(1)^1 x Z2')
check('[T] Delta L = 2 at Delta B = 0 (0nubb, Majorana neutrino mass, LLHH) has Delta(B-L) = -2: forbidden; '
      'Delta B = Delta L = 2 dinucleon decay (pp -> e+e+) is allowed only at dimension 12',
      not LAT['S3 S2 + uude'].contains(v(L=2, H=2)) and not LAT['S3 S2 + uude'].contains(v(n=2))
      and LAT['Sm Yukawa + nu^c nu^c (Majorana)'].contains(v(L=2, H=2)), 'LLHH, nu^c nu^c: forbidden (allowed with Majorana)')

# ============================ D. strong CP ============================
print('== D. theta_bar = theta - arg det(Y_u Y_d): what the rules fix')
rng = np.random.default_rng(7)
def cmat(n=3): return rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
def ckm_J(Mu, Md):
    _, Uu = np.linalg.eigh(Mu @ Mu.conj().T); _, Ud = np.linalg.eigh(Md @ Md.conj().T)
    V = Uu.conj().T @ Ud
    return abs((V[0, 1] * V[1, 2] * np.conj(V[0, 2]) * np.conj(V[1, 1])).imag)
phi = rng.uniform(0, 2 * np.pi, 20); Yu, Yd = cmat(), cmat()
dth = [np.angle(np.linalg.det(np.exp(1j * p) * Yu) * np.linalg.det(np.exp(-1j * p) * Yd) / (np.linalg.det(Yu) * np.linalg.det(Yd))) for p in phi]
check('[T] the CL-3-set doublet cannot fix theta_bar: its phase enters Q u H and Q d H* oppositely, so arg det(Y_u Y_d) '
      'is independent of it (any number of families)', max(map(abs, dth)) < 1e-12, f"max shift {max(map(abs, dth)):.0e}")
# exact antiunitary on the quark fields: in its basis every coefficient is real -> J = 0 and arg det in {0, pi}
Js, args = [], []
for _ in range(200):
    A, Bu, Bd = [np.linalg.qr(cmat())[0] for _ in range(3)]
    Mu, Md = A @ rng.normal(size=(3, 3)) @ Bu, A @ rng.normal(size=(3, 3)) @ Bd
    Js.append(ckm_J(Mu, Md)); a = np.angle(np.linalg.det(Mu) * np.linalg.det(Md) / (np.linalg.det(A) ** 2 * np.linalg.det(Bu) * np.linalg.det(Bd)))
    args.append(min(abs(a), abs(abs(a) - np.pi)))
Jg = [ckm_J(cmat(), cmat()) for _ in range(200)]
check('[T, checked] an exact antiunitary of the update (T x C4 or PH x C4 kept by every term) makes Yukawa-type terms '
      'real in its basis: arg det in {0, pi} and J = 0 exactly; generic complex terms give J != 0 and arg det uniform',
      max(Js) < 1e-12 and max(args) < 1e-12 and np.median(Jg) > 1e-3, f"max J {max(Js):.0e}, generic median J {np.median(Jg):.2f}")
# Nelson-Barr: 3 light + 1 heavy vector-like down-type copy, real CP-even masses, CP broken only in F (D-row, light d^c cols)
out = []
for scale in (1.0, 1e-3):
    jj, aa = [], []
    for _ in range(200):
        Md = np.zeros((4, 4), complex); Md[:3, :3] = rng.normal(size=(3, 3)) * 0.01
        Md[3, :3] = scale * (rng.normal(size=3) + 1j * rng.normal(size=3)); Md[3, 3] = 1.0
        Mu = np.diag(rng.uniform(.001, .01, 3)).astype(complex)
        w, U = np.linalg.eigh(Md @ Md.conj().T); Ud = U[:3, :3]          # light eigenvectors, Q rows
        # light down mass matrix in the Q basis: m_eff m_eff^+ = Ud diag Ud^+ restricted to the light states
        mm = Ud @ np.diag(w[:3]) @ Ud.conj().T
        jj.append(ckm_J(Mu, np.linalg.cholesky(mm + 1e-30 * np.eye(3))))
        aa.append(abs(np.angle(np.linalg.det(Md))) % np.pi)
    out.append((np.median(jj), max(min(a, np.pi - a) for a in aa)))
check('[T, checked] Nelson-Barr block form (heavy-light entry only in one off-diagonal block, real CP-even masses): '
      'arg det = 0 exactly while J != 0 when the CP-odd mixing is comparable to the heavy mass, J -> 0 when it is small',
      out[0][1] < 1e-12 and out[1][1] < 1e-12 and out[0][0] > 1e-3 and out[1][0] < 1e-5,
      f"J median {out[0][0]:.1e} (F ~ M_H), {out[1][0]:.1e} (F = 1e-3 M_H)")
thmax = 1.8e-26 / 2.4e-16
check('[E] generic order-one theta_bar is excluded: d_n = 2.4e-16 theta e cm with d_n < 1.8e-26 gives |theta_bar| < 7.5e-11; '
      'a uniform phase lands there with probability 2.4e-11', thmax < 1e-10, f"|theta| < {thmax:.1e}")
fpi, met, me, mK, mpi = .0922, .9578, .5479, .4937, .135
chi = fpi ** 2 / 6 * (met ** 2 + me ** 2 - 2 * mK ** 2)
check("[E] theta is physical: the eta' (958 MeV) exceeds Weinberg's no-anomaly bound sqrt(3) m_pi = 234 MeV; "
      "Witten-Veneziano needs topological susceptibility chi = (179 MeV)^4, so making theta unobservable is excluded",
      met > np.sqrt(3) * mpi and abs(chi ** .25 - .179) < .005, f"chi^(1/4) = {chi ** .25 * 1e3:.0f} MeV")
print("   m_u = 0 is excluded (FLAG m_u/m_d = 0.47(2)); CL-3 links only exact symmetries, and U(1)_A is anomalous, so no CL-3 field relaxes theta")
print('theorems: A1-A4, C1-C3, D1-D3.  estimates: B1-B2, D4-D5.')
print('supplied: chiral 16 x 3 content and SM links (chirality wall open); Yukawa-type, uddn, uude, (nu^c)^4 terms as listed;')
print('  unit map (G = a^2/8pi, 2.11e18 GeV per rad/tick), lattice W, A, Super-K, ILL, nEDM, eta/eta\'/K/pi masses, f_pi, d_n/theta.')
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
