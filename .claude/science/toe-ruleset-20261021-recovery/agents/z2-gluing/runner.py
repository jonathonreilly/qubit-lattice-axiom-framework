#!/usr/bin/env python3
"""z2-gluing: can the Z_2 gluing of charge parity to isospin parity be gauged in the disentangled (charge rotor x spin chain)
frame of su2-tpf, giving back the jointly chiral fermionic doublet content in 1+1D?
 A vertex lattices (exact rationals): the gluing eta = (-1)^{n_L + m_L} on the product lattice B; its charge half and spin half
   are each anomalous, the product is not; bosonic gauging (eta_j = +1) gives a cross-glued bosonic lattice with no h = 1/2
   doublets; fermionic gauging gives exactly the fermionic doublet lattice (content (3,1)); mixed structure with Q and SU(2)
 B the spin half on the spin-1/2 chain carrier: the on-site SU(2) centre is a c-number; the IR (-1)^{m_L} is lattice
   translation (exact diagonalisation, Sz = 0 sectors, L <= 10)
 C the charge half on the Villain rotor frame (exact rationals, su2-tpf conventions inlined): the half turn dresses cleanly under
   W and squares to the dressed constraint; the local winding parity does not preserve the Villain constraint
 D the glued lattice on these carriers: U = infinity doublet ring = spinless charges twisted by the spin-string translation
Labels: [T] theorem / exact computation. Supplied model, finite diagnostic; no physical identification.
Cited, not rederived: shift-orbifold / fermionisation rules for Narain lattices, Else-Nayak (anomalous symmetries are not on-site),
Lieb-Schultz-Mattis, Ogata-Shiba factorisation (checked exactly in D1), TPF arXiv:2601.04304 via the su2-tpf runner."""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120

import itertools, math, os, random, signal, sys, time
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 5)
from fractions import Fraction as Fr
import numpy as np

T0 = time.monotonic(); PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" | {detail}" if detail else ''))
H = Fr(1, 2); a_, b_ = 3, 1

# ===================================== A. vertex lattices =====================================
print('== A. doublet vertex lattices, v = (nL, mL, nR, mR): h = (nL^2+mL^2)/4, hbar = (nR^2+mR^2)/4, Q = a nL + b nR, (a,b) = (3,1)')
def ip(u, v): return Fr(u[0] * v[0] + u[1] * v[1] - u[2] * v[2] - u[3] * v[3], 2)
def spin(v): return ip(v, v) / 2
def hh(v): return Fr(v[0] ** 2 + v[1] ** 2, 4)
def hb(v): return Fr(v[2] ** 2 + v[3] ** 2, 4)
def add(u, v): return tuple(x + y for x, y in zip(u, v))
R4 = range(-5, 6)
B = [v for v in itertools.product(R4, repeat=4) if (v[0] - v[2]) % 2 == 0 and (v[1] - v[3]) % 2 == 0]
inbox = lambda v: all(abs(x) <= 3 for x in v)
dc, ds = (1, 0, 0, 0), (0, 1, 0, 0); dl = add(dc, ds)
eta = lambda v: (-1) ** ((v[0] + v[1]) % 2)
ok_eta = all(eta(v) == (1 if ip(dl, v).denominator == 1 else -1) for v in B)
tw = lambda d: {spin(add(v, d)) % H for v in B}
ok_an = tw(dc) == {Fr(1, 4)} and tw(ds) == {Fr(1, 4)} and tw(dl) == {0}
check('A1 [T] the gluing on the product lattice B = (charge rotor) x (SU(2)_1) is eta = (-1)^{nL+mL} = e^{2 pi i <delta,v>}, '
      'delta = (1,1,0,0): (-1)^{nL} = (-1)^{N+W} (half turn x winding parity) times (-1)^{mL} (centre of SU(2)_L); each half is an '
      'anomalous Z_2 (twisted spins in Z/2 + 1/4), the product is not (twisted spins in Z/2)',
      ok_eta and ok_an, f'twisted spins mod 1/2: charge {sorted(map(str, tw(dc)))}, spin {sorted(map(str, tw(ds)))}, product {sorted(map(str, tw(dl)))}')
B0 = [v for v in B if eta(v) == 1]
orb = {v for v in B0 if inbox(v)} | {add(v, dl) for v in B if spin(add(v, dl)).denominator == 1 and inbox(add(v, dl))}
ferm = {v for v in B0 if inbox(v)} | {add(v, dl) for v in B if spin(add(v, dl)).denominator == 2 and inbox(add(v, dl))}
box3 = list(itertools.product(range(-3, 4), repeat=4))
cross = {v for v in box3 if (v[0] - v[3]) % 2 == 0 and (v[2] - v[1]) % 2 == 0}
Flat = {v for v in box3 if (v[0] - v[1]) % 2 == 0 and (v[2] - v[3]) % 2 == 0}
half = lambda S, L: sorted({(a_ * v[0] + b_ * v[2], Fr(v[1 if L else 3], 2)) for v in S if (hh(v), hb(v)) == ((H, 0) if L else (0, H))})
orb_h = half(orb, True) + half(orb, False)
low = sorted({(a_ * v[0] + b_ * v[2], Fr(v[1], 2), Fr(v[3], 2)) for v in orb if hh(v) + hb(v) == H and a_ * v[0] + b_ * v[2] != 0})
check('A2 [T] bosonic gauging (impose eta_j = +1, Z_2 links, ordinary Gauss law) = shift orbifold B_0 u (B_1 + delta) = '
      '{nL = mR, nR = mL mod 2}: even, no h = 1/2 or hbar = 1/2 operator; its lightest charged operators (h = hbar = 1/4) carry '
      'charge +-a with isospin on the RIGHT movers and charge +-b with isospin on the LEFT movers: cross-glued, not the doublet content',
      orb == cross and orb_h == [] and len(low) == 8 and all((abs(q) == a_ and jl == 0 and abs(jr) == H) or (abs(q) == b_ and abs(jl) == H and jr == 0) for q, jl, jr in low)
      and all(spin(v).denominator == 1 for v in orb), f'{len(orb)} vectors; lightest charged (Q, J3L, J3R) {[(q, str(x), str(y)) for q, x, y in low]}')
FL, FR = half(ferm, True), half(ferm, False)
check('A3 [T] fermionic gauging (eta coupled with the Arf/Kitaev term, on the lattice a Jordan-Wigner string of eta_j) = '
      'B_0 u (B_0 + delta) = {nL = mL, nR = mR mod 2}, the fermionic doublet lattice; h = 1/2 left movers are isospin doublets of '
      'charge +-a, right movers doublets of charge +-b: the swap content (3,1) is recovered',
      ferm == Flat and [q for q, j in FL] == [-3, -3, 3, 3] and all(abs(j) == H for q, j in FL + FR) and [q for q, j in FR] == [-1, -1, 1, 1],
      f'left {[(q, str(j)) for q, j in FL]}; right {[(q, str(j)) for q, j in FR]}')
TW = [add(v, dl) for v in B]
qB = {(a_ * v[0] + b_ * v[2]) % 2 for v in B}; qT = {(a_ * v[0] + b_ * v[2]) % 2 for v in TW}
jB = {(v[1] + v[3]) % 2 for v in B}; jT = {(v[1] + v[3]) % 2 for v in TW}
glueF = all((-1) ** ((a_ * v[0] + b_ * v[2]) % 2) * (-1) ** ((v[1] + v[3]) % 2) == 1 for v in Flat) and any((v[1] + v[3]) % 2 for v in Flat)
check('A4 [T] mixed structure of eta: Q is even on B and odd on the eta-twisted sector, so Q itself has no fractional charge '
      '(no Z_2 x U(1)_Q anomaly) but the faithful U(1)_{Q/2} of B has half charges there; the diagonal isospin is integral on B and '
      'half-integral on the twisted sector (eta x SO(3) mixed anomaly). In the glued theory e^{i pi Q} x (SU(2) centre) = 1 with '
      'the centre nontrivial: the gauge group is U(2) = (U(1) x SU(2))/Z_2, and the on-site centre of a carrier whose IR image is '
      'B is trivial on all of B',
      qB == {0} and qT == {1} and jB == {0} and jT == {1} and glueF, f'Q mod 2: B {qB}, twisted {qT}; 2j_V mod 2: B {jB}, twisted {jT}')
dN = (H, 0, -H, 0)
twN = {spin(add(v, dN)) % H for v in B}
fN = {add(v, dN) for v in B if ip(dN, v).denominator == 2} | {add(v, dN) for v in B if ip(dN, v).denominator == 1}
check('A5 [T] the local part alone (on-site half turn x on-site centre of a spin-1/2 chain, IR image (-1)^N) is non-anomalous '
      '(twisted spins in Z) but gauging it, bosonically or fermionically, never produces an h = 1/2 isospin doublet: it does not glue',
      twN == {0} and not any((hh(v), hb(v)) in ((H, 0), (0, H)) for v in fN),
      f'twisted spins mod 1/2 {sorted(map(str, twN))}; h = 1/2 states after fermionising (-1)^N: 0')

# ===================================== B. spin half on the spin-1/2 chain =====================================
print('== B. spin-1/2 Heisenberg ring, Sz = 0 sector (dense, dim <= 252)')
def heis(L):
    st = [s for s in range(1 << L) if bin(s).count('1') == L // 2]; ix = {s: i for i, s in enumerate(st)}; n = len(st)
    Hm = np.zeros((n, n)); Tm = np.zeros((n, n)); S2 = np.zeros((n, n))
    for i, s in enumerate(st):
        for j in range(L):
            k = (j + 1) % L; bj, bk = (s >> j) & 1, (s >> k) & 1
            Hm[i, i] += 0.25 if bj == bk else -0.25
            if bj != bk: Hm[ix[s ^ (1 << j) ^ (1 << k)], i] += 0.5
        t = ((s << 1) | (s >> (L - 1))) & ((1 << L) - 1); Tm[ix[t], i] = 1
        for j in range(L):
            for k in range(L):
                bj, bk = (s >> j) & 1, (s >> k) & 1
                if j == k: S2[i, i] += 0.75; continue
                S2[i, i] += 0.25 if bj == bk else -0.25
                if bj != bk: S2[ix[s ^ (1 << j) ^ (1 << k)], i] += 0.5
    E, V = np.linalg.eigh(Hm)
    Sv = [(-1 + math.sqrt(1 + 4 * float(V[:, i] @ S2 @ V[:, i]))) / 2 for i in range(n)]
    s2ev = np.linalg.eigvalsh(S2); intS = all(abs((-1 + math.sqrt(1 + 4 * max(e, 0))) / 2 - round((-1 + math.sqrt(1 + 4 * max(e, 0))) / 2)) < 1e-8 for e in s2ev)
    Tv = [float(V[:, i] @ Tm @ V[:, i]) for i in range(n)]
    return E, Sv, Tv, intS
resB = {}
for L in (6, 8, 10):
    E, Sv, Tv, intS = heis(L); t1 = next(i for i in range(1, len(E)) if abs(Sv[i] - 1) < 1e-6); s1 = next(i for i in range(1, len(E)) if abs(Sv[i]) < 1e-6)
    resB[L] = (round(Tv[t1] * Tv[0], 9), round(Tv[s1] * Tv[0], 9), intS, (E[t1] - E[0]) * L, (E[s1] - E[0]) * L)
check('B1 [T] on the spin-1/2 ring the on-site SU(2) centre prod_j (-1)^{2S_j} = (-1)^L is a c-number (every level has integer S), '
      'while the lowest triplet and singlet excitations (the h = hbar = 1/4 multiplet of SU(2)_1, (-1)^{mL} = -1) carry momentum pi '
      'relative to the ground state: on this carrier the spin half of eta is lattice translation (Lieb-Schultz-Mattis), not an '
      'internal symmetry, so eta_j = (half turn) x (winding parity) x (on-site centre) has IR image the charge half alone',
      all(r[0] == -1 and r[1] == -1 and r[2] for r in resB.values()),
      '; '.join(f'L={L}: T-ratio triplet {r[0]:+.0f} singlet {r[1]:+.0f}, L*gap {r[3]:.2f}/{r[4]:.2f}' for L, r in resB.items()))

# ===================================== C. charge half on the Villain rotor frame =====================================
print('== C. Villain rotor frame (su2-tpf conventions): x = (phi[flavour][site], n[flavour][link], theta[site], a[link])')
def rnd(x): return math.floor(x + H)
def f1(x): return x - math.floor(x)
def cp(x): return ([r[:] for r in x[0]], [r[:] for r in x[1]], x[2][:], x[3][:])
def ylink(ph, n, th, qs, k):
    N = len(th); return sum(qA * (rnd(ph[al][(k + 1) % N] - ph[al][k] + qV * (th[(k + 1) % N] - th[k])) + n[al][k]) for al, (qV, qA) in enumerate(qs))
def Xr(ph, qs, k): return rnd(sum(qA * ph[al][k % len(ph[al])] for al, (qV, qA) in enumerate(qs)))
def ytil(ph, n, th, qs, k): return ylink(ph, n, th, qs, k) - (Xr(ph, qs, k + 1) - Xr(ph, qs, k))
def Phi(ph, n, th, qs): return -sum(th[k] * ytil(ph, n, th, qs, k) for k in range(len(th)))
def W(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] + qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, Phi(x[0], x[1], x[2], qs)
def Wd(x, qs):
    y = cp(x); y[0][:] = [[f1(x[0][a][j] - qV * x[2][j]) for j in range(len(x[2]))] for a, (qV, qA) in enumerate(qs)]
    return y, -Phi(y[0], y[1], y[2], qs)
def comp(x, ops):
    ps = Fr(0)
    for op in ops: x, p = op(x); ps += p
    return x, ps
def same(u, v): return u[0] == v[0] and f1(u[1] - v[1]) == 0
def K(x, al, j, be):
    N = len(x[2]); y = cp(x); p = x[0][al]; d1 = p[j] - p[(j - 1) % N]; d2 = p[(j + 1) % N] - p[j]
    y[1][al][(j - 1) % N] += rnd(d1) - rnd(d1 + be); y[1][al][j] += rnd(d2) - rnd(d2 - be); y[0][al][j] = f1(p[j] + be); return y, Fr(0)
def Kg(x, al, j, be, qs):
    N = len(x[2]); qV, qA = qs[al]; y = cp(x); p = x[0][al]; g = lambda k: qV * (x[2][(k + 1) % N] - x[2][k] - x[3][k])
    d1 = p[j] - p[(j - 1) % N] + g((j - 1) % N); d2 = p[(j + 1) % N] - p[j] + g(j)
    y[1][al][(j - 1) % N] += rnd(d1) - rnd(d1 + be); y[1][al][j] += rnd(d2) - rnd(d2 - be); y[0][al][j] = f1(p[j] + be)
    X = sum(q[1] * x[0][b][j] for b, q in enumerate(qs)); dlt = rnd(X + qA * be) - rnd(X)
    return y, dlt * (x[2][j] - x[2][(j - 1) % N] - x[3][(j - 1) % N])
def m_link(x, k): N = len(x[2]); p = x[0][0]; return rnd(p[(k + 1) % N] - p[k]) + x[1][0][k]
def omega(x, k): return cp(x), H * m_link(x, k)
def ring(x): return cp(x), H * sum(m_link(x, k) for k in range(len(x[2])))
rng = random.Random(20261022); DEN = 48; NB = 5; NT = 150
CH = [(4, 2), (4, -1), (4, -1)]
def rx(N, F, links=False):
    r = lambda: Fr(rng.randrange(DEN), DEN)
    return ([[r() for _ in range(N)] for _ in range(F)], [[rng.randrange(-2, 3) for _ in range(N)] for _ in range(F)],
            [r() for _ in range(N)], [r() for _ in range(N)] if links else [Fr(0)] * N)
cnt = {'K1K': 0, 'sq': 0, 'dress1': 0, 'dress2': 0, 'comm': 0}
for t in range(NT):
    x = rx(NB, 3); j = rng.randrange(NB); i = rng.randrange(NB)
    Kh = lambda z: K(z, 0, j, H); K1 = lambda z: K(z, 0, i, 1)
    cnt['K1K'] += not same(comp(x, [Kh, K1]), comp(x, [K1, Kh]))
    cnt['sq'] += not same(comp(x, [Kh, Kh]), K(x, 0, j, 1))
    u = comp(x, [lambda z: W(z, CH), Kh, lambda z: Wd(z, CH)]); v = Kg(x, 0, j, H, CH)
    cnt['dress1'] += not (same(u, v) and f1(v[1] - (x[2][j] - x[2][(j - 1) % NB])) == 0)
    u = comp(x, [lambda z: W(z, CH), lambda z: K(z, 0, j, 1), lambda z: Wd(z, CH)]); v = Kg(x, 0, j, 1, CH)
    cnt['dress2'] += not (same(u, v) and f1(v[1] - 2 * (x[2][j] - x[2][(j - 1) % NB])) == 0)
    xl = rx(NB, 3, links=True); k2 = (j + rng.randrange(1, NB)) % NB
    cnt['comm'] += not same(comp(xl, [lambda z: Kg(z, 0, j, H, CH), lambda z: Kg(z, 0, k2, H, CH)]),
                            comp(xl, [lambda z: Kg(z, 0, k2, H, CH), lambda z: Kg(z, 0, j, H, CH)]))
check('C1 [T] the half-turn part is fine: K_j(1/2) commutes with every Villain constraint K_i(1) and squares to K_j(1); in the '
      'disentangled frame W^dag K_j(1/2) W = K^cov_j(1/2) e^{2 pi i (theta_j - theta_{j-1} - a)} and W^dag K_j(1) W = K^cov_j(1) '
      'e^{2 pi i qA (theta_j - theta_{j-1} - a)} (the dressed constraint, qA = 2); dressed half turns on different sites commute',
      all(v == 0 for v in cnt.values()), ', '.join(f'{k} {v}/{NT}' for k, v in cnt.items()))
fl = {'local': 0, 'ring': 0, 'eta_anti': 0, 'Kh_om': 0}
for t in range(NT):
    x = rx(NB, 3); k = rng.randrange(NB); i = rng.randrange(NB)
    K1 = lambda z: K(z, 0, i, 1); y = K1(x)[0]
    flips = (m_link(y, k) - m_link(x, k)) % 2; fl['local'] += flips != (i in (k, (k + 1) % NB))
    fl['ring'] += sum(m_link(y, q) - m_link(x, q) for q in range(NB)) != 0
    j = rng.randrange(NB); ej = lambda z: comp(z, [lambda s: K(s, 0, j, H), lambda s: omega(s, (j - 1) % NB)])
    Km = lambda z: K(z, 0, (j - 1) % NB, 1); u = comp(x, [ej, Km]); v = comp(x, [Km, ej])
    fl['eta_anti'] += not (u[0] == v[0] and f1(u[1] - v[1]) == H)
    fl['Kh_om'] += same(comp(x, [lambda s: K(s, 0, j, H), lambda s: omega(s, (j - 1) % NB)]), comp(x, [lambda s: omega(s, (j - 1) % NB), lambda s: K(s, 0, j, H)]))
check('C2 [T] the winding-parity part is not local: the link parity (-1)^{m_k}, m_k = round(D phi_k) + n_k, flips under exactly the '
      'two constraints K_k(1), K_{k+1}(1); only the ring product is constraint-invariant. So eta_j = K_j(1/2)(-1)^{m_{j-1}}(centre) '
      'anticommutes with K_{j-1}(1) and leaves the Villain-gauge-invariant space (the lattice face of the anomaly in A1); K_j(1/2) '
      'and the link parity fail to commute on configurations where phi_j wraps',
      fl['local'] == 0 and fl['ring'] == 0 and fl['eta_anti'] == 0 and 0 < fl['Kh_om'] < NT,
      f"local-flip mismatches {fl['local']}, ring changes {fl['ring']}, eta_j K_(j-1)(1) not anticommuting {fl['eta_anti']}; "
      f"K_j(1/2) commutes with (-1)^m_(j-1) on {fl['Kh_om']}/{NT}")

# ===================================== D. the glued lattice on these carriers =====================================
print('== D. U = infinity doublet ring (no double occupancy), L sites, N particles, t = 1, fermion signs')
def uinf(L, N):
    basis = [(ps, sp) for ps in itertools.combinations(range(L), N) for sp in itertools.product((0, 1), repeat=N)]
    ix = {b: i for i, b in enumerate(basis)}; Hm = np.zeros((len(basis), len(basis)))
    for (ps, sp), i in ix.items():
        occ = set(ps)
        for r, p in enumerate(ps):
            q = p + 1
            if q < L and q not in occ:
                nps = list(ps); nps[r] = q; Hm[ix[(tuple(nps), sp)], i] -= 1; Hm[i, ix[(tuple(nps), sp)]] -= 1
        if ps[-1] == L - 1 and 0 not in occ:
            nps = (0,) + ps[:-1]; nsp = (sp[-1],) + sp[:-1]; jdx = ix[(nps, nsp)]
            Hm[jdx, i] -= (-1) ** (N - 1); Hm[i, jdx] -= (-1) ** (N - 1)
    return np.sort(np.linalg.eigvalsh(Hm))
def predicted(L, N):
    out = []
    for m in range(N):
        strings = [sp for sp in itertools.product((0, 1), repeat=N)]
        rot = np.zeros((len(strings), len(strings))); sx = {s: i for i, s in enumerate(strings)}
        for s in strings: rot[sx[(s[-1],) + s[:-1]], sx[s]] = 1
        ev = np.linalg.eigvals(rot); mult = int(np.sum(np.abs(ev - np.exp(2j * np.pi * m / N)) < 1e-8))
        q = 2 * np.pi * m / N
        for I in itertools.combinations(range(L), N):
            out += [sum(-2 * math.cos((2 * math.pi * k + q) / L) for k in I)] * mult
    return np.sort(np.array(out))
resD = {(L, N): float(np.abs(uinf(L, N) - predicted(L, N)).max()) for L, N in ((5, 3), (6, 4), (7, 3))}
check('D1 [T] the glued lattice on these carriers is the Ogata-Shiba squeeze: the U = infinity doublet ring (where the gluing is '
      'local: charge parity = isospin parity on each site) has exactly the spectrum of spinless charges whose boundary twist is '
      'the spin string\'s translation eigenvalue e^{2 pi i m/N}. In the product frame the gluing is a translation of the squeezed '
      'spin chain at each charge hop, not an on-site Z_2',
      all(v < 1e-10 for v in resD.values()), ', '.join(f'L={L},N={N}: {v:.1e}' for (L, N), v in resD.items()))
print(f'elapsed_seconds {time.monotonic() - T0:.1f}')
print('all [T]. Supplied: rotor matter (Villain), the swap content (a, b) = (3, 1), ancillas, the spin-1/2 chain as SU(2) carrier. '
      'Cited: orbifold/fermionisation rules, Else-Nayak, LSM, TPF 2601.04304 via su2-tpf.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
