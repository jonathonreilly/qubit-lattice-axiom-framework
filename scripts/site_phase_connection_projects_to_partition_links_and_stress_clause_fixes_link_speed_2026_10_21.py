#!/usr/bin/env python3
"""Photon placement: the site phase chi (what-is-a-link) versus partition-lattice E/B (light-cones). Supplied models,
finite checks, no physical identification.

 G  Geometry: each site is the midpoint of the bond joining its even and odd block centre (a nearest-neighbour bond of
    the body-centred block-centre lattice). The partition links of light-cones are its next-nearest bonds. Each mixed
    plaquette is one tetrahedron of the Delaunay complex. Its two remaining edges are one even link and one odd link.
 P  Exact relation: Pi(chi) = mean holonomy of the four two-site paths between neighbouring even centres is a
    gauge-covariant even-lattice connection. chi carries 6 gauge-invariant values per cell, Pi(chi) carries 2. At k = 0
    ker Pi is exactly the four gapped branches (8,8,8,24) of the mixed-plaquette law, and its massless pair is Pi-visible.
 N1 Gauge-invariant block-local operators on chi registers are functions of the electric fluxes only, so no Margolus
    update on the two partitions carries a magnetic term.
 N2 Any register hopped by the CL-2 coin carries the double-valued rotation class, so its quanta cannot be photons.
 S  CL-6's clause (one flat metric in which every source's stress is symmetric) gives alpha = v_g v_p. For fermions this
    is 1/3, so c_link = c_fermion at leading order for any placement. Beyond leading order Yee at C = 1/sqrt3 is
    identical at every K. The mixed-plaquette chi law as a leapfrog is never slower (photon-decay bound met); in continuous time it is.
 Z  Coarser rung: the CL-3 tick is a one-particle unitary. With mass, no proper site subset conserves its number, and
    pair (collective) modes form a continuum. A quantum-link carrier built from one-mode sites needs role-assigned sites
    and a number constraint, both of which change CL-3.
"""
from __future__ import annotations
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/SITE_PHASE_CONNECTION_PROJECTS_TO_PARTITION_LINKS_AND_STRESS_CLAUSE_FIXES_LINK_SPEED_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/CANDIDATE_LAWS.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
import os, sys, signal, itertools
os.environ['OPENBLAS_NUM_THREADS'] = '1'
sys.stdout.reconfigure(line_buffering=True)
signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('cap exceeded')))
signal.setitimer(signal.ITIMER_REAL, AUDIT_TIMEOUT_SEC - 2)
import numpy as np
from collections import deque
PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''))
rng = np.random.default_rng(20261021); r3 = np.sqrt(3.0)
R8 = np.array(list(itertools.product((0, 1), repeat=3))); RI = {tuple(r): i for i, r in enumerate(R8)}

# ---------------- G. geometry on an 8^3 torus
print('== G. sites, partition links and mixed plaquettes in one complex')
L = 8; S = np.array(list(itertools.product(range(L), repeat=3)))
ec = 2 * (S // 2) + 0.5; oc = 2 * ((S - 1) // 2) + 1.5; s = oc - ec
ok_mid = np.allclose((ec + oc) / 2, S) and set(map(tuple, s.astype(int))) == set(itertools.product((-1, 1), repeat=3))
bonds = {}
for i, x in enumerate(S): bonds.setdefault(tuple(ec[i] % L), set()).add(tuple(oc[i] % L))
check('G1 every site is the midpoint of the bond from its even to its odd block centre (offset in {+-1}^3); each even centre has 8 distinct odd neighbours',
      ok_mid and all(len(v) == 8 for v in bonds.values()))
idx = {tuple(x): i for i, x in enumerate(S)}; mixed = 0; good = 0
for x in S:
    for a, b in ((0, 1), (1, 2), (0, 2)):
        q = [x.copy() for _ in range(4)]; q[1][a] += 1; q[2][a] += 1; q[2][b] += 1; q[3][b] += 1
        ii = [idx[tuple(p % L)] for p in q]
        E = {tuple(ec[i] % L) for i in ii}; O = {tuple(oc[i] % L) for i in ii}
        if len(E) == 1 or len(O) == 1: continue
        mixed += 1; e1, e2 = [np.array(e) for e in E]; o1, o2 = [np.array(o) for o in O]
        de = (e2 - e1 + L / 2) % L - L / 2; do = (o2 - o1 + L / 2) % L - L / 2
        ax_e = np.nonzero(np.abs(de) > 1e-9)[0]; ax_o = np.nonzero(np.abs(do) > 1e-9)[0]
        good += (len(E) == 2 and len(O) == 2 and len(ax_e) == 1 and len(ax_o) == 1 and abs(abs(de).max() - 2) < 1e-9
                 and abs(abs(do).max() - 2) < 1e-9 and ax_e[0] != ax_o[0])
cells = (L // 2) ** 3
check('G2 each mixed plaquette spans 2 even + 2 odd blocks and is a tetrahedron whose free edges are one even link (axis a) and one odd link (axis b != a); 12 per cell',
      mixed == good == 12 * cells, f'{mixed // cells} per cell; per cell V,E,F,T = 2, 8+3+3, 24, 12 -> Euler 0')

# ---------------- Fourier model of chi: chi(n,r), site 2n+r, bond from even centre n with s = 2r-1
def gauge_vecs(K):
    ge = np.ones(8, complex); go = np.array([-np.exp(-1j * K @ (1 - r)) for r in R8]); return np.stack([ge, go], 1)
def Pi(K):
    P = np.zeros((3, 8), complex)
    for a in range(3):
        for r in R8:
            if r[a] != 1: continue
            P[a, RI[tuple(r)]] += 0.25; t = r.copy(); t[a] = 0; P[a, RI[tuple(t)]] -= 0.25 * np.exp(1j * K[a])
    return P
def Hol(K):                      # two-site-path holonomies h[(a, r)] as rows
    rows, lab = [], []
    for a in range(3):
        for r in R8:
            if r[a] != 1: continue
            v = np.zeros(8, complex); v[RI[tuple(r)]] = 1; t = r.copy(); t[a] = 0; v[RI[tuple(t)]] -= np.exp(1j * K[a]); rows.append(v); lab.append((a, tuple(r)))
    return np.array(rows), lab
def Mk(K):                       # mixed-plaquette (axial rhombus) magnetic form: sum |h_r - h_r'|^2, r,r' one transverse flip apart
    h, lab = Hol(K); rows = []
    for i, (a, r) in enumerate(lab):
        for j, (a2, r2) in enumerate(lab):
            if a2 == a and i < j and sum(u != v for u, v in zip(r, r2)) == 1: rows.append(h[i] - h[j])
    C = np.array(rows); return C.conj().T @ C, len(rows)
print('== P. exact relation chi -> partition-lattice connection')
K = rng.uniform(-np.pi, np.pi, 3); g = gauge_vecs(K); P = Pi(K)
de = 1 - np.exp(1j * K)
check('P1 Pi is gauge covariant: odd-block phases drop out, even-block phases enter as the even-lattice gradient',
      np.allclose(P @ g[:, 1], 0) and np.allclose(P @ g[:, 0], de))
M, nr = Mk(K); ev = np.linalg.eigvalsh(M); M0, _ = Mk(np.zeros(3)); e0, V0 = np.linalg.eigh(M0)
kerP = 8 - np.linalg.matrix_rank(P, 1e-9); rPg = np.linalg.matrix_rank(P @ g, 1e-9)
check('P2 per cell: chi has 8 - 2 = 6 gauge-invariant values; Pi has rank 3 and maps the gauge plane to one gradient, so Pi(chi) carries 2 '
      'and ker Pi carries 5 - 1 = 4; the 12-rhombus magnetic form reproduces what-is-a-link (2 gauge zeros; k=0: 0,0,0,0,8,8,8,24)',
      nr == 12 and int(np.sum(ev < 1e-9)) == 2 and np.allclose(e0, [0, 0, 0, 0, 8, 8, 8, 24], atol=1e-9) and kerP == 5 and rPg == 1,
      f'dim ker Pi = {kerP}, rank Pi(gauge) = {rPg}')
gap = V0[:, 4:]; zer = V0[:, :4]
check('P3 at k = 0 ker Pi = exactly the four gapped branches; the zero modes are uniform A (3) + gauge (1)',
      np.abs(Pi(np.zeros(3)) @ gap).max() < 1e-12 and np.linalg.matrix_rank(Pi(np.zeros(3)) @ zer, 1e-9) == 3)
vis = []
for n in (np.array([1., 0, 0]), np.ones(3) / r3, np.array([1., 2, 3]) / np.sqrt(14)):
    k = 0.03 * n; M, _ = Mk(k); w, V = np.linalg.eigh(M); Gk = gauge_vecs(k); Q, _ = np.linalg.qr(Gk)
    Vp = V - Q @ (Q.conj().T @ V); w2 = np.array([np.real(v.conj() @ M @ v) / np.real(v.conj() @ v) for v in Vp.T])
    sel = np.argsort(w2 + 1e9 * (np.linalg.norm(Vp, axis=0) < 1e-6))[:2]
    for j in sel:
        A = Pi(k) @ Vp[:, j]; vis.append((np.linalg.norm(A) / np.linalg.norm(Vp[:, j]), abs(n @ A) / np.linalg.norm(A), w2[j] / 0.03 ** 2))
vis = np.array(vis)
check('P4 the massless pair is Pi-visible (|Pi v|/|v| ~ 0.7) and transverse; omega^2/k^2 -> 1/2 (unit couplings)',
      vis[:, 0].min() > 0.5 and vis[:, 1].max() < 0.05 and np.abs(vis[:, 2] - 0.5).max() < 1e-3,
      f'|Pi v|/|v| in [{vis[:, 0].min():.3f},{vis[:, 0].max():.3f}], longitudinal <= {vis[:, 1].max():.1e}')

# ---------------- N1. block-local gauge-invariant chi operators
print('== N1/N2. what a Margolus link update can be')
N = 5; X = np.roll(np.eye(N), 1, 0); I = np.eye(N)
gens = [np.kron(X, I), np.kron(I, X)]
A = np.vstack([np.kron(Gm, np.eye(N * N)) - np.kron(np.eye(N * N), Gm.T) for Gm in gens])
null = N * N * N * N - np.linalg.matrix_rank(A, 1e-9)
check('N1 inside one block the 8 sites lie in 8 different opposite-partition blocks, so block phases shift each chi independently; '
      'the commutant of independent shifts (Z_5, 2 registers) is N^2 = 25-dim = functions of e only. Mixed plaquettes are never block-local (G2)',
      null == N * N)
# N2: projective class of the on-site rotation representation commuting with the CL-2 coin, 4^3 torus
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); xi = []
for i in range(8):
    n = (2 * R8[i] - 1.0) / r3; w_, v_ = np.linalg.eigh(sum(n[k] * J3[k] for k in range(3))); xi.append(v_[:, -1])
Gm = np.array([[xi[a].conj() @ xi[b] for b in range(8)] for a in range(8)])
W = np.array([[(-Gm[a, b] / abs(Gm[a, b]) / r3 if np.abs(R8[a] - R8[b]).sum() == 1 else 0) for b in range(8)] for a in range(8)])
L4 = 4; S4 = np.array(list(itertools.product(range(L4), repeat=3))); n4 = len(S4); i4 = {tuple(x): i for i, x in enumerate(S4)}
def lat(Wb):
    We = np.zeros((n4, n4), complex); Wo = np.zeros((n4, n4), complex)
    for o in itertools.product(range(0, L4, 2), repeat=3):
        o = np.array(o); se = [i4[tuple((o + c) % L4)] for c in R8]; so = [i4[tuple((o + 1 + c) % L4)] for c in R8]
        We[np.ix_(se, se)] += Wb; Wo[np.ix_(so, so)] += Wb
    return We, Wo
def rep(We, Wo, R):
    p = np.array([i4[tuple(np.round(R @ (x - .5) + .5).astype(int) % L4)] for x in S4]); inv = np.argsort(p); H = We + Wo
    th = np.full(n4, np.nan); th[0] = 0; dq = deque([0])
    while dq:
        y = dq.popleft(); x = inv[y]
        for x2 in np.nonzero(np.abs(H[:, x]) > 1e-12)[0]:
            if np.isnan(th[p[x2]]): th[p[x2]] = th[y] - np.angle(H[y, p[x2]] / H[x, x2]); dq.append(p[x2])
    Pm = np.zeros((n4, n4)); Pm[p, np.arange(n4)] = 1; Pr = np.diag(np.exp(1j * th)) @ Pm
    return Pr, max(np.abs(Pr @ We @ Pr.conj().T - We).max(), np.abs(Pr @ Wo @ Pr.conj().T - Wo).max())
ra = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); rb = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
def cls(Wb):
    We, Wo = lat(Wb); Pa, ea = rep(We, Wo, ra); Pb, eb = rep(We, Wo, rb)
    l = [np.linalg.matrix_power(M_, k)[0, 0] for M_, k in ((Pa, 4), (Pb, 3), (Pa @ Pb, 2))]
    return l[0] ** 3 * l[1] ** 4 / l[2] ** 6, max(ea, eb)
Ic, ec_ = cls(W); Iu, eu = cls((np.abs(W) > 0).astype(complex))
check('N2 rotations about cube centres act on CL-2-hopped registers with class invariant l_a^3 l_b^4 / l_ab^6 = -1 '
      '(double-valued); control flux-0 hop gives +1. A W-hopped quantum has half-integer helicity: a fermion cannot emit one singly',
      abs(Ic + 1) < 1e-9 and abs(Iu - 1) < 1e-9 and ec_ < 1e-12 and eu < 1e-12, f'CL-2 {Ic.real:+.6f}, control {Iu.real:+.6f}')

# ---------------- S. speeds
print('== S. what fixes the link speed')
def wf(K):
    Wo = np.exp(-1j * R8 @ K)[:, None] * W * np.exp(1j * R8 @ K)[None, :]
    return np.sort(np.abs(np.angle(np.linalg.eigvals(Wo @ W))))[-1]
def coeff(wfun, n):
    ks = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.08]); w = np.array([wfun(k * n) for k in ks])
    c = np.linalg.lstsq(np.stack([np.ones_like(w), w ** 2, w ** 4], 1), w / ks, rcond=None)[0]
    return -c[1] / c[0], c[0]
k0 = 1e-3; alf = (wf(np.array([k0 + 1e-6, 0, 0])) - wf(np.array([k0 - 1e-6, 0, 0]))) / 2e-6 * wf(np.array([k0, 0, 0])) / k0
check('S1 symmetric stress in g = diag(-alpha,1,1,1) needs alpha = (energy flux)/(momentum) = v_g v_p; fermion alpha = 1/3, '
      'so a link source in the same flat metric needs c_link^2 = 1/3: g_E g_B tau^2 = 2/3 (chi law), C = 1/sqrt3 (Yee)', abs(alf - 1 / 3) < 1e-6, f'alpha_f = {alf:.8f}')
gEB = 2 / 3
def chi_ct(K):
    M, _ = Mk(K); Q, _ = np.linalg.qr(gauge_vecs(K)); Pq = np.eye(8) - Q @ Q.conj().T
    lam = np.sort(np.linalg.eigvalsh(Pq @ M @ Pq)); lam = lam[lam > 1e-13]; return np.sqrt(gEB * lam[0])
def chi_lf(K):
    M, _ = Mk(K); Q, _ = np.linalg.qr(gauge_vecs(K)); Pq = np.eye(8) - Q @ Q.conj().T
    lam = np.sort(np.linalg.eigvalsh(Pq @ M @ Pq)); lam = lam[lam > 1e-13]; return 2 * np.arcsin(np.sqrt(gEB * lam[0] / 4))
def yee(K, C=1 / r3): return np.arccos(1 - 3 * C ** 2 + C ** 2 * np.cos(K).sum())
KR = rng.uniform(-np.pi, np.pi, (500, 3)); dy = max(abs(yee(k) - wf(k)) for k in KR)
check('S2 Yee at C = 1/sqrt3: cos w = 1 - 3C^2 + C^2 sum cos K equals the fermion band at every K (500 K)', dy < 1e-9, f'{dy:.1e}')
EP = 1.22089e28; Lb = 2 * np.sqrt(8 * np.pi); wE = lambda E: E / EP * Lb / r3
rows = []
for nm, n in (('axis', np.array([1., 0, 0])), ('face', np.array([1., 1, 0]) / np.sqrt(2)), ('body', np.ones(3) / r3)):
    bf, c = coeff(wf, n); bc, cc = coeff(chi_ct, n); bl, cl = coeff(chi_lf, n); rows.append((nm, bf, bc, bl, c, cc, cl))
    print(f'   {nm}: c = {c:.6f} {cc:.6f} {cl:.6f}; w/K = c(1 - b w^2): b_fermion {bf:+.5f}, b_chi(cont) {bc:+.5f}, b_chi(leapfrog) {bl:+.5f}')
check('S3 with the stress-fixed product the chi law has the fermion speed at leading order in every direction', all(abs(r[5] - 1 / r3) < 1e-7 and abs(r[6] - 1 / r3) < 1e-7 and abs(r[4] - 1 / r3) < 1e-7 for r in rows))
dirs = [r_ for r_ in (np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.ones(3) / r3)]
dirs += [v / np.linalg.norm(v) for v in rng.normal(size=(120, 3))]
dct = np.array([coeff(wf, n)[0] - coeff(chi_ct, n)[0] for n in dirs]); dlf = np.array([coeff(wf, n)[0] - coeff(chi_lf, n)[0] for n in dirs])
print(f'   (v_link - v_fermion)/c per w^2 over 123 directions: continuous-time chi [{dct.min():+.4f}, {dct.max():+.4f}], '
      f'leapfrog chi [{dlf.min():+.4f}, {dlf.max():+.4f}]')
pc = 0.938272e9 ** 2 / (2 * 1e20 ** 2); thr = 2 * 0.511e6 ** 2 / 1.4e15 ** 2
check(f'S4 continuous-time chi law: links slower than fermions in some directions by {-dct.min():.3f} w^2 = {-dct.min() * wE(1e20) ** 2:.1e} '
      f'at 1e20 eV > {pc:.1e}: proton vacuum Cherenkov excludes it if protons carry the fermion O(K^2)', -dct.min() * wE(1e20) ** 2 > pc)
check(f'S5 leapfrog chi law (electric and magnetic half-ticks): never slower (min {dlf.min():+.1e}, equal along face diagonals), faster by '
      f'<= {dlf.max():.3f} w^2 = {dlf.max() * wE(1.4e15) ** 2:.1e} at 1.4 PeV < photon-decay threshold {thr:.1e}: allowed; Yee at C = 1/sqrt3 has no offset',
      dlf.min() > -1e-6 and dlf.max() * wE(1.4e15) ** 2 < thr)

# ---------------- Z. coarser rung (owner's zoom question)
print('== Z. can coarse cells of one-mode sites carry the connection?')
def comps(U):
    adj = np.abs(U) + np.abs(U.T) > 1e-12; seen = -np.ones(len(U), int); c = 0
    for s0 in range(len(U)):
        if seen[s0] >= 0: continue
        dq = deque([s0]); seen[s0] = c
        while dq:
            x = dq.popleft()
            for y in np.nonzero(adj[x])[0]:
                if seen[y] < 0: seen[y] = c; dq.append(y)
        c += 1
    return c
We, Wo = lat(W); mu, bb = 0.3, 0.1
def coinm(Wx, a): return np.cos(a) * Wx + 1j * np.sin(a) * np.eye(n4)
Um = coinm(Wo, mu / 2 - bb) @ coinm(We, mu / 2 + bb); U0 = Wo @ We
check('Z1 site subsets with conserved number under the tick: massless 2 (the two sublattice sectors, swapped by 90-degree '
      'rotations); massive 1 (none proper). A carrier subset with its own number constraint is not supplied by CL-3', comps(U0) == 2 and comps(Um) == 1,
      f'massless {comps(U0)}, massive {comps(Um)}')
Kq = np.array([0.4, 0.1, 0.2]); qs = rng.uniform(-np.pi, np.pi, (4000, 3))
pair = np.array([wf(q) + wf(Kq - q) for q in qs]); thr = wf(Kq)
check('Z2 collective (pair) modes of the free tick at fixed total K form a continuum, not a two-helicity pole: lowest pair energy '
      '>= w(K) (edge reached as one partner -> 0), spread of order 1', pair.min() >= thr - 1e-12 and np.ptp(pair) > 1,
      f'w(K) = {thr:.4f}, pair energies in [{pair.min():.4f}, {pair.max():.4f}]')
budget = [(l, 8 * l ** 3, 8 * 2 * (5 - 1)) for l in (1, 2, 3)]
print('   quantum-link budget (N = 5 levels per link = 2 x 4 fermion rishon modes; 8 links per coarse cell):',
      ', '.join(f'rung {l}: {m} modes vs {need} for links' for l, m, need in budget))
check('Z3 counting alone allows one-mode carriers from rung 3 (216 modes vs 64 for N = 5 links + matter); rung 1 cannot (8 vs 64)',
      budget[0][1] < budget[0][2] and budget[2][1] > budget[2][2] + 8)
print('supplied: CL-2 coin; partitions; minimal coupling as site phases; quadratic chi/Yee laws; CL-6 stress clause; Planck block 2a. '
      'Literature, not rederived: Coulomb phase of Z_N (N >= 5) and U(1) lattice gauge theory.')
print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
