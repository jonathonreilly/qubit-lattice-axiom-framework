AUDIT_INPUT_PATHS = ('docs/INDEPENDENT_REDERIVATION_OF_SIX_CANDIDATE_LAW_THEOREMS_WITH_CORRECTED_SCOPES_BOUNDED_THEOREM_NOTE_2026-10-21.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
"""theorem-review: independent hostile re-derivation of six load-bearing register theorems (own code, no probe imports).

T1 spin-3/2 forcing: covariant nearest-neighbour block unitaries for every corner character j = 0..6 and every
   phase assignment of the equal-modulus edge hop.
T2 universal step: exact rewrite; real-space bands under two readings of "the same unitary"; speed; Yee; decay.
T3 copy count: 2O content of the cube for every site character; Dirac-copy couplings; R point; 4^3 room.
T4 Born transport: supply-demand existence on many-body Margolus half-ticks; max-entropy uniqueness (KKT), label
   equivariance and independence of unentangled relays.
T5 cell factorisation: corner-set products, rotation commutant, Hilbert-space factorisations, spin content.
T6 cubic-frustum Lorentzian Regge FRW: explicit Minkowski dihedrals, Schlaefli, exact constraint vs (1 - rho/rho*).
Finite diagnostics of supplied models; no physical identification.
"""
import itertools, time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog, brentq
from scipy.sparse import coo_matrix, vstack as svstack
from scipy.integrate import quad

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0
def check(name, ok, detail=''):
    global NP, NF
    NP += bool(ok); NF += (not ok)
    print(('[PASS] ' if ok else '[FAIL] ') + name + ('  ' + detail if detail else ''))

rng = np.random.default_rng(20261021)
def null_space(A, rcond=1e-9):   # thin SVD (tall matrices only): avoids the full m x m U factor
    A = np.asarray(A); assert A.shape[0] >= A.shape[1]
    _, s_, vh = np.linalg.svd(A, full_matrices=False); rk = int((s_ > rcond * max(s_.max(), 1.0)).sum())
    return vh[rk:].conj().T
r3 = np.sqrt(3.0)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]

# ---------------- the double cube group 2O (48 SU(2) lifts of the 24 proper rotations) ----------------
def proper_rotations():
    out = []
    for p in itertools.permutations(range(3)):
        P = np.eye(3)[list(p)]
        for sg in itertools.product((1, -1), repeat=3):
            R = np.diag(sg) @ P
            if np.linalg.det(R) > 0: out.append((R, round(np.linalg.det(P))))   # det P = A2 character
    return out
def axis_angle(R):
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if th < 1e-9: return 0.0, np.array([0, 0, 1.0])
    if abs(th - np.pi) < 1e-9:
        M = (R + np.eye(3)) / 2; i = np.argmax(np.diag(M)); return np.pi, M[:, i] / np.sqrt(M[i, i])
    return th, np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(th))
def sv(v): return sum(v[k] * SIG[k] for k in range(3))
G = []
for R, sgn in proper_rotations():
    th, n = axis_angle(R)
    for t in (th, th + 2 * np.pi):
        G.append(dict(R=R, sgn=sgn, th=t, n=n, U2=expm(-1j * t * sv(n) / 2)))
lift_err = max(np.abs(g['U2'] @ sv(v) @ g['U2'].conj().T - sv(g['R'] @ v)).max() for g in G for v in np.eye(3))
U2s = np.array([g['U2'] for g in G])
def find(U):
    d = np.abs(U2s - U[None]).reshape(48, -1).max(1); k = int(np.argmin(d)); return k if d[k] < 1e-9 else -1
MUL = np.array([[find(G[i]['U2'] @ G[j]['U2']) for j in range(48)] for i in range(48)])
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
def Dj(g, J): return expm(-1j * g['th'] * sum(g['n'][k] * J[k] for k in range(3)))
def chi_j(j, th): return np.cos((j - np.arange(int(round(2 * j + 1)))) * th).sum()
IRR = ['A1', 'A2', 'E', 'T1', 'T2', 'E1/2', 'E5/2', 'G3/2']
def chi_irr(nm, g):
    tr, s, th = np.trace(g['R']), g['sgn'], g['th']
    return {'A1': 1.0, 'A2': s, 'E': chi_j(2, th) - tr * s, 'T1': tr, 'T2': tr * s,
            'E1/2': chi_j(.5, th), 'E5/2': chi_j(.5, th) * s, 'G3/2': chi_j(1.5, th)}[nm]
CT = np.array([[chi_irr(nm, g) for g in G] for nm in IRR])
def mult(chis): return np.rint((CT @ np.real(np.asarray(chis))) / 48).astype(int)
def label(m): return '+'.join((f'{k}' if k > 1 else '') + nm for nm, k in zip(IRR, m) if k) or '0'
check('2O built: lifts rotate sigma by R, closed under products, 8 orthonormal irreducible characters',
      lift_err < 1e-12 and (MUL >= 0).all() and np.abs(CT @ CT.T / 48 - np.eye(8)).max() < 1e-12)

# ---------------- cube corners, faces, coherent-state induced corner actions ----------------
C8 = np.array(list(itertools.product((0, 1), repeat=3))); NV = (2 * C8 - 1) / r3
def cidx(s): return int(4 * s[0] + 2 * s[1] + s[2])
PERM = [[cidx(np.rint(g['R'] @ (C8[i] - .5) + .5).astype(int)) for i in range(8)] for g in G]
EDGES = [(a, b) for a in range(8) for b in range(8) if np.abs(C8[a] - C8[b]).sum() == 1]
UND = [(a, b) for a, b in EDGES if a < b]
FACES = []
for a in range(3):
    b, c = [k for k in range(3) if k != a]
    for v in (0, 1):
        cyc = []
        for pb, pc in ((0, 0), (1, 0), (1, 1), (0, 1)):
            s = np.zeros(3, int); s[a], s[b], s[c] = v, pb, pc; cyc.append(cidx(s))
        FACES.append(cyc)
def fluxes(W):
    f = np.array([W[q[1], q[0]] * W[q[2], q[1]] * W[q[3], q[2]] * W[q[0], q[3]] for q in FACES]); return f / np.abs(f)
def corner_action(j):
    J = Jm(j); xs = [np.linalg.eigh(sum(NV[i][k] * J[k] for k in range(3)))[1][:, -1] for i in range(8)]
    Us = []
    for g, pm in zip(G, PERM):
        D = Dj(g, J); U = np.zeros((8, 8), complex)
        for i in range(8): U[pm[i], i] = xs[pm[i]].conj() @ D @ xs[i]
        Us.append(U)
    return Us, xs
def covariant(Us, support):
    M = []
    for U in Us:
        cols = []
        for a, b in support:
            E = np.zeros((8, 8), complex); E[a, b] = 1; cols.append((U @ E @ U.conj().T - E).ravel())
        M.append(np.array(cols).T)
    return null_space(np.vstack(M), rcond=1e-9)
def to_mat(vec, support):
    X = np.zeros((8, 8), complex)
    for (a, b), z in zip(support, vec): X[a, b] = z
    return X

print('== T1 spin-3/2 forcing')
rows = []; hom_err = 0.0; ok_struct = True; HJ = {}; CORNER = {}
for j in np.arange(0, 6.01, 0.5):
    Us, xs = corner_action(j)
    hom_err = max(hom_err, max(np.abs(Us[a] @ Us[b] - Us[MUL[a, b]]).max() for a in range(0, 48, 5) for b in range(48)))
    ok_struct &= all(np.allclose(np.abs(U[np.abs(U) > 1e-9]), 1) and np.count_nonzero(np.abs(U) > 1e-9) == 8 for U in Us)
    Xn = covariant(Us, EDGES); Xd = covariant(Us, EDGES + [(a, a) for a in range(8)])
    X = to_mat(Xn[:, 0], EDGES); X /= np.abs(X[EDGES[0]]) * r3
    c = X.conj().T[EDGES[0]] / X[EDGES[0]]; H = np.sqrt(c) * X
    fl = fluxes(H); pred = np.exp(-2j * np.pi * j / 3)
    flux_ok = all(min(abs(f - pred), abs(f - np.conj(pred))) < 1e-9 for f in fl)
    eq_mod = np.allclose(np.abs(X[tuple(np.array(EDGES).T)]), 1 / r3)
    rows.append((j, Xn.shape[1], Xd.shape[1], np.abs(X.conj().T - c * X).max(), np.abs(H - H.conj().T).max(),
                 flux_ok and eq_mod, np.abs(H @ H - np.eye(8)).max() < 1e-9, np.angle(fl[0]) / np.pi))
    HJ[float(j)] = H; CORNER[float(j)] = (Us, xs)
check('every j = 0..6: coherent-state induction gives a monomial representation of 2O', ok_struct and hom_err < 1e-9, f'hom err {hom_err:.0e}')
check('every j: covariant edge-only hops span 1 dim, on-site+edge 2 dims (1, X); X^dag = cX, so X is a phase times Hermitian',
      all(r[1] == 1 and r[2] == 2 and r[3] < 1e-9 and r[4] < 1e-9 for r in rows))
check('every j: equal moduli and face phase exp(-+2 pi i j/3), computed gauge-invariantly from the covariant space',
      all(r[5] for r in rows))
uni = [r[0] for r in rows if r[6]]
check('a hopping covariant nn block unitary exists iff j = 3/2 mod 3 (1.5, 4.5 here); no genuine O action (integer j) admits one',
      uni == [1.5, 4.5], 'face/pi ' + ' '.join(f'{r[0]:g}:{r[7]:+.2f}' for r in rows[:7]))
Us32, xs32 = CORNER[1.5]
g3 = [k for k, g in enumerate(G) if abs(g['th'] - 2 * np.pi / 3) < 1e-9 and np.allclose(g['n'], np.ones(3) / r3)][0]
check('forced datum = one sign: the order-6 lift of C3 acts on its corner by -1, its square by +1, 2 pi by -1',
      abs(Us32[g3][7, 7] + 1) < 1e-9 and abs(Us32[g3 + 1][7, 7] - 1) < 1e-9)
def herm_hop(ph):
    W = np.zeros((8, 8), complex)
    for (a, b), p in zip(UND, ph): W[a, b] = np.exp(1j * p) / r3; W[b, a] = np.conj(W[a, b])
    return W
agree = n_sq = 0
for bits in itertools.product((0, 1), repeat=12):
    W = herm_hop(np.pi * np.array(bits)); sq = np.abs(W @ W - np.eye(8)).max() < 1e-12
    agree += (sq == (np.abs(fluxes(W) + 1).max() < 1e-12)); n_sq += sq
H32 = HJ[1.5]; agree_c = 0; NR = 3000
for t in range(NR):
    D = np.exp(1j * rng.uniform(0, 2 * np.pi, 8))
    if t % 3 == 0: W = herm_hop(rng.uniform(0, 2 * np.pi, 12))
    else:
        W = D[:, None] * H32 * D.conj()[None]
        if t % 3 == 2: a, b = UND[t % 12]; W[a, b] *= np.exp(1e-4j); W[b, a] = np.conj(W[a, b])
    agree_c += ((np.abs(W @ W - np.eye(8)).max() < 1e-10) == (np.abs(fluxes(W) + 1).max() < 1e-10))
check('every phase assignment: Hermitian equal-modulus W has W^2 = 1 iff all 6 faces are -1 (4096 sign, 3000 complex)',
      agree == 4096 and n_sq == 128 and agree_c == NR, f'{n_sq}/4096 sign patterns = one gauge class')
EV = [i for i in range(8) if C8[i].sum() % 2 == 0]; OD = [i for i in range(8) if C8[i].sum() % 2]
B = H32[np.ix_(EV, OD)]; Wn = np.zeros((8, 8), complex); Wn[np.ix_(EV, OD)] = B
Wn[np.ix_(OD, EV)] = np.diag(np.exp(1j * rng.uniform(0, 6, 4))) @ B.conj().T @ np.diag(np.exp(1j * rng.uniform(0, 6, 4)))
check('unitarity alone does not fix the face phase: non-Hermitian unitary edge hops with W^2 != 1, faces != -1 exist',
      np.abs(Wn.conj().T @ Wn - np.eye(8)).max() < 1e-12 and np.abs(Wn @ Wn - np.eye(8)).max() > 0.1 and np.abs(fluxes(Wn) + 1).max() > 0.1,
      '(none is covariant)')

print('== T2 universal step')
W = H32; I8 = np.eye(8); Pinv = np.eye(8)[::-1]
def V(a): return np.cos(a) * W + 1j * np.sin(a) * I8
err = 0
for mu, b in ((0.0, 0.0), (0.07, 0.4), (0.3, 1.3), (0.2, -0.5)):
    e = np.pi / 2 - b
    err = max(err, np.abs(V(mu / 2 + b) - 1j * expm(-1j * (e - mu / 2) * W)).max(), np.abs(V(mu / 2 - b) + 1j * expm(1j * (e + mu / 2) * W)).max())
check('V(mu/2+b) = i exp(-i(eps-mu/2)W), V(mu/2-b) = -i exp(+i(eps+mu/2)W); phases i(-i) = 1 cancel per particle per full tick',
      err < 1e-13, f'{err:.0e}')
L = 6; NS = L ** 3; coords = np.array(list(itertools.product(range(L), repeat=3)))
IDX = {tuple(c): i for i, c in enumerate(coords)}
def layer(Vb, odd, conv):
    U = np.zeros((NS, NS), complex)
    for base in itertools.product(range(odd, L, 2), repeat=3):
        st = [IDX[tuple((np.array(base) + C8[k]) % L)] for k in range(8)]
        lab = [cidx(coords[x] % 2) for x in st] if conv == 'A' else list(range(8))
        U[np.ix_(st, st)] = Vb[np.ix_(lab, lab)]
    return U
def wform(K, mu, b):
    S = np.cos(np.atleast_2d(K)).mean(1); A = (np.cos(2 * b) + np.cos(mu)) / 2
    return np.arccos(np.clip(A * S - (np.cos(2 * b) - np.cos(mu)) / 2, -1, 1))
KG = 2 * np.pi * np.array(list(itertools.product(range(3), repeat=3))) / 3
mu0, b0 = 0.23, 0.41
pred = np.sort(np.concatenate([wform(KG, mu0, b0)] * 4 + [-wform(KG, mu0, b0)] * 4))
TK = {cv: layer(V(mu0 / 2 - b0), 1, cv) @ layer(V(mu0 / 2 + b0), 0, cv) for cv in 'AB'}
dev = {cv: np.abs(np.sort(-np.angle(np.linalg.eigvals(TK[cv]))) - pred).max() for cv in 'AB'}
def site_action(g, centre, xs, D):
    U = np.zeros((NS, NS), complex)
    for x in range(NS):
        Xp = np.rint(g['R'] @ (coords[x] - centre) + centre).astype(int) % L
        U[IDX[tuple(Xp)], x] = xs[cidx(Xp % 2)].conj() @ D @ xs[cidx(coords[x] % 2)]
    return U
J32 = Jm(1.5)
gens = [k for k, g in enumerate(G) if g['th'] < 2 * np.pi and ((abs(g['th'] - np.pi / 2) < 1e-9 and np.allclose(g['n'], [0, 0, 1]))
        or (abs(g['th'] - 2 * np.pi / 3) < 1e-9 and np.allclose(g['n'], np.ones(3) / r3)))]
SA = [site_action(G[k], cen, xs32, Dj(G[k], J32)) for k in gens for cen in (np.full(3, .5), np.full(3, 1.5))]
sa_unit = max(np.abs(U.conj().T @ U - np.eye(NS)).max() for U in SA)
cov = {cv: max(np.abs(U @ TK[cv] - TK[cv] @ U).max() for U in SA) for cv in 'AB'}
def bloch(K, Ve, Vo, conv='A'):
    D = np.exp(1j * C8 @ K); Vo = Vo if conv == 'A' else Pinv @ Vo @ Pinv; return (D[:, None] * Vo * D.conj()[None]) @ Ve
def qe(U): return np.sort(np.abs(np.angle(np.linalg.eigvals(U))))
Kt = np.array([0.3, 1.1, 2.0]); cubic = {cv: np.abs(qe(bloch(Kt, V(mu0 / 2 + b0), V(mu0 / 2 - b0), cv)) - qe(bloch(Kt[[1, 2, 0]], V(mu0 / 2 + b0), V(mu0 / 2 - b0), cv))).max() for cv in 'AB'}
check('6^3 torus, site-attached reading (a site keeps its overlap phases in both cubes): 216 quasi-energies obey cos w = A S - (cos2b - cos mu)/2; covariant about even and odd centres',
      dev['A'] < 1e-10 and cov['A'] < 1e-10 and sa_unit < 1e-12, f'band {dev["A"]:.0e}, cov {cov["A"]:.0e}')
PW = Pinv @ W @ Pinv; gq = np.zeros(8, complex); gq[0] = 1; seen = [0]
for b_ in seen:
    for a_ in range(8):
        if a_ not in seen and abs(W[a_, b_]) > 1e-9: gq[a_] = PW[a_, b_] * gq[b_] / W[a_, b_]; seen.append(a_)
lam = np.sqrt(gq[0] * gq[7]); kq = lam * gq.conj(); hq = np.ones(8, complex); hq[7 - np.arange(4)] = kq[:4]
W2 = hq[:, None] * W * hq.conj()[None]; V2 = lambda a: np.cos(a) * W2 + 1j * np.sin(a) * I8
devB2 = np.abs(np.sort(-np.angle(np.linalg.eigvals(layer(V2(mu0 / 2 - b0), 1, 'B') @ layer(V2(mu0 / 2 + b0), 0, 'B')))) - pred).max()
check('cube-frame reading (same 8x8 matrix in each cube\'s own corner labels) in the overlap gauge: bands off and not cubic, so covariant for no action; it is right only in an inversion-symmetric gauge (exists)',
      dev['B'] > 1e-2 and cubic['B'] > 1e-2 and cubic['A'] < 1e-12 and np.allclose(gq * gq[::-1], gq[0] * gq[7]) and np.abs(Pinv @ W2 @ Pinv - W2).max() < 1e-12 and devB2 < 1e-10,
      f'dev {dev["B"]:.2f}, asym {cubic["B"]:.2f}; PW\'P = W\': dev {devB2:.0e}')
dmx = 0; dirs = [np.array([1., 0, 0]), np.array([1., 1, 0]) / np.sqrt(2), np.ones(3) / r3]
for b in (0.0, 0.3, 1.1):
    for d in dirs:
        h = 2e-3; w1, w2 = [qe(bloch(k * d, V(b), V(-b)))[0] for k in (h, 2 * h)]
        dmx = max(dmx, abs((4 * w1 / h - w2 / (2 * h)) / 3 - np.sin(np.pi / 2 - b) / r3))
check('massless speed = sin(eps)/sqrt3 blocks per tick on axis, face and body directions', dmx < 1e-7, f'{dmx:.0e}')
rel = []
for mu, b in ((0.05, 0.3), (0.1, 0.0), (0.02, 1.0)):
    h = 2e-3; w1, w2 = [qe(bloch(k * dirs[0], V(mu / 2 + b), V(mu / 2 - b)))[0] for k in (h, 2 * h)]
    c2 = (4 * (w1 ** 2 - mu ** 2) - (w2 ** 2 - mu ** 2) / 4) / (3 * h ** 2); A = (np.cos(2 * b) + np.cos(mu)) / 2
    rel.append((c2 / (np.cos(b) ** 2 / 3) - 1, (A / 3) * (mu / np.sin(mu)) / (np.cos(b) ** 2 / 3) - 1, mu ** 2 * (1 / 6 - 1 / (4 * np.cos(b) ** 2))))
check('massive species: c^2 = (A/3)(mu/sin mu), below the massless value by ~mu^2(1/(4cos^2 b) - 1/6): one eps gives one speed only as mu -> 0',
      all(abs(x - y) < 1e-6 and x < 0 and abs(x - z) < 0.02 * abs(z) for x, y, z in rel), 'rel ' + ' '.join(f'{x:.2e}' for x, _, _ in rel))
def curl(d): return np.array([[0, -d[2], d[1]], [d[2], 0, -d[0]], [-d[1], d[0], 0]])
def yee(K, C):
    cf = curl(np.exp(1j * K) - 1); cb = curl(1 - np.exp(-1j * K)); I3 = np.eye(3)
    return np.block([[I3 - C ** 2 * cb @ cf, C * cb], [-C * cf, I3]])
KR = rng.uniform(-np.pi, np.pi, (300, 3)); m_ok = 0; m_off = 0
for b in (0.0, 0.5, 1.2):
    for K in KR:
        wf = wform(K, 0.0, b)[0]; ph = lambda C: np.sort(np.abs(np.angle(np.linalg.eigvals(yee(K, C)))))[-1]
        m_ok = max(m_ok, abs(ph(np.cos(b) / r3) - wf)); m_off = max(m_off, abs(ph(1.01 * np.cos(b) / r3) - wf))
check('own Yee leapfrog: transverse band = massless fermion band at every K iff C = cos(b)/sqrt3 = sin(eps)/sqrt3',
      m_ok < 1e-8 and m_off > 1e-3, f'match {m_ok:.0e}; C x1.01 off {m_off:.1e}')
def wg(K, C): return 2 * np.arcsin(np.clip(C * np.sqrt((np.sin(np.atleast_2d(K) / 2) ** 2).sum(1)), 0, 1))
def margins(bf, bg, mu=0.01, n=20000):
    d = rng.normal(size=(n, 3)); d /= np.linalg.norm(d, axis=1)[:, None]; d[:n // 4] = np.ones(3) / r3
    K = d * rng.uniform(0.02, 1.0, n)[:, None]; x = rng.uniform(0.02, 0.98, n)[:, None]; K1 = x * K; Cg = np.cos(bg) / r3
    return (wform(K1, mu, bf) + wform(K - K1, mu, bf) - wg(K, Cg)).min(), (wform(K - K1, mu, bf) + wg(K1, Cg) - wform(K, mu, bf)).min()
mg = [margins(0.3, 0.3), margins(0.3, 0.2), margins(0.3, 0.4)]
check('kinematics mu = 0.01 (decay, Cherenkov margins): shared step closes both; faster photon opens only gamma -> f fbar, slower only f -> f gamma',
      min(mg[0]) > 0 and mg[1][0] < 0 < mg[1][1] and mg[2][1] < 0 < mg[2][0], ' '.join(f'({a:+.0e},{c:+.0e})' for a, c in mg))
print('   estimate: 1.4 PeV photons bound only a FASTER photon, dc/c < 2(m_e/E)^2 = %.1e; SN1987A |c_nu - c|/c < ~2e-9' % (2 * (0.511e6 / 1.4e15) ** 2))

print('== T3 copy count')
cont = {j: mult([np.trace(U) for U in CORNER[j][0]]) for j in (0.0, .5, 1.0, 1.5, 2.0, 2.5)}
print('   corner content: ' + '; '.join(f'j={j:g}: {label(m)}' for j, m in cont.items()))
check('only j = 3/2 gives 2G3/2; j = 1/2, 5/2 give E1/2+E5/2+G3/2; integer j contain no spinorial irrep',
      label(cont[1.5]) == '2G3/2' and label(cont[.5]) == label(cont[2.5]) == 'E1/2+E5/2+G3/2' and all(cont[j][5:].sum() == 0 for j in (0.0, 1.0, 2.0)))
def cint(*names): return int(np.rint(np.prod([[chi_irr(nm, g) for g in G] for nm in names], axis=0).sum() / 48))
check('massive Dirac copy needs a repeated 2-dim irrep: k-linear invariants E1/2-E1/2 = 1, E1/2-E5/2 = 0; masses 1 and 0; G3/2 = E1/2 x E',
      cint('E1/2', 'E1/2', 'T1') == 1 and cint('E5/2', 'E5/2', 'T1') == 1 and cint('E1/2', 'E5/2', 'T1') == 0 and cint('E1/2', 'E1/2') == 1 and cint('E1/2', 'E5/2') == 0
      and np.allclose(CT[7], CT[5] * CT[2]), 'no site action has room for ONE massive copy; E1/2+E5/2 = 2 Weyl cones, mass forbidden')
UR = bloch(np.full(3, np.pi), V(mu0 / 2 + b0), V(mu0 / 2 - b0)); U0 = bloch(np.zeros(3), V(mu0 / 2 + b0), V(mu0 / 2 - b0))
cr = max(np.abs(U @ X - X @ U).max() for U in Us32 for X in (UR, U0))
check('Gamma and R Bloch ticks commute with the corner action (content 2G3/2 at both); edge-hop tick puts all 8 Gamma states at +-mu',
      cr < 1e-12 and np.allclose(qe(U0), mu0), f'{cr:.0e}')
ALL64 = [(a, b) for a in range(8) for b in range(8)]; CB = covariant(Us32, ALL64)
def rand_cov():
    Hm = sum((rng.normal() + 1j * rng.normal()) * to_mat(CB[:, k], ALL64) for k in range(CB.shape[1])); Hm = Hm + Hm.conj().T
    return expm(0.7j * Hm / np.abs(Hm).max())
def ndist(U, tol=1e-7):
    ph = np.sort(np.angle(np.linalg.eigvals(U))); return 1 + int((np.diff(ph) > tol).sum())
Kg = np.array([0.3, 0.7, 1.9]); gen = [(ndist(bloch(np.zeros(3), Ve, Vo)), ndist(bloch(Kg, Ve, Vo))) for Ve, Vo in [(rand_cov(), rand_cov()) for _ in range(4)]]
nnf = [ndist(bloch(Kg, V(a1), V(a2))) for a1, a2 in rng.uniform(-3, 3, (4, 2))]
check('covariant commutant = U(2) x 1 (dim 4): generic covariant ticks are 4-fold at Gamma only, 8 levels at generic K; nn ticks V(a_e), V(a_o) stay 4-fold at all K',
      CB.shape[1] == 4 and all(g0 == 2 and gk == 8 for g0, gk in gen) and all(x == 2 for x in nnf), 'copies split off rest unless nn')
c64 = np.full(3, 1.5); S64 = np.array(list(itertools.product(range(4), repeat=3))); ch64 = []
for g in G:
    D = Dj(g, J32); tot = 0
    for x in S64:
        if (np.rint(g['R'] @ (x - c64) + c64).astype(int) == x).all(): tot += xs32[cidx(x % 2)].conj() @ D @ xs32[cidx(x % 2)]
    ch64.append(tot)
m64 = mult(ch64)
check('4^3 cell, same site states: 4E1/2+4E5/2+12G3/2 (room); a 2^3 tick has it too once its block unitaries may vary with period 4',
      label(m64) == '4E1/2+4E5/2+12G3/2', label(m64))

print('== T4 Born transport')
def mb(u, confs, tol=1e-11):
    ix = {c: i for i, c in enumerate(confs)}; r, c, v = [], [], []
    for jj, cf in enumerate(confs):
        cand = sorted(set(np.nonzero(np.abs(u[:, list(cf)]) > 1e-12)[0].tolist()))
        for cp in itertools.combinations(cand, len(cf)):
            val = np.linalg.det(u[np.ix_(cp, cf)])
            if abs(val) > tol: r.append(ix[cp]); c.append(jj); v.append(val)
    return np.array(r), np.array(c), np.array(v)
def ham(confs, r, c): return np.array([len(set(confs[a]) ^ set(confs[b])) for a, b in zip(r, c)], float)
def lp(p, q, r, c, cost, n):
    m = len(r); A = svstack([coo_matrix((np.ones(m), (c, np.arange(m))), (n, m)), coo_matrix((np.ones(m), (r, np.arange(m))), (n, m))]).tocsr()
    return linprog(cost, A_eq=A, b_eq=np.concatenate([p, q]), bounds=(0, None), method='highs',
                   options={'primal_feasibility_tolerance': 1e-10, 'dual_feasibility_tolerance': 1e-10})
def ipf(p, q, r, c, n, it=60000, J0=None):
    J = np.ones(len(r)) if J0 is None else np.maximum(J0, 0).copy()
    for k in range(it):
        s = np.bincount(c, J, n); J *= (p / np.where(s > 0, s, 1))[c]
        t = np.bincount(r, J, n); J *= (q / np.where(t > 0, t, 1))[r]
        if k % 100 == 0 and np.abs(np.bincount(c, J, n) - p).max() < 1e-15: break
    return J
def maxent(p, q, r, c, cost, n):
    res = lp(p, q, r, c, cost, n); al, be = res.eqlin.marginals[:n], res.eqlin.marginals[n:]
    Z = np.nonzero(cost - al[c] - be[r] < 1e-7)[0]; J = np.zeros(len(r)); J[Z] = ipf(p, q, r[Z], c[Z], n)
    return J, res
def kkt(J, r, c, n):   # max entropy on a face <=> log J additive in (source, target) on its support
    S = J > 1e-14; A = np.zeros((S.sum(), 2 * n)); A[np.arange(S.sum()), c[S]] = 1; A[np.arange(S.sum()), n + r[S]] = 1
    y = np.log(J[S]); return np.abs(A @ np.linalg.lstsq(A, y, rcond=None)[0] - y).max()
def rand_state(n):
    v = rng.normal(size=n) + 1j * rng.normal(size=n); return v / np.linalg.norm(v)
uq = lambda th: expm(-1j * th * W)
confs2 = list(itertools.combinations(range(8), 2)); r2, c2_, v2 = mb(uq(np.pi / 2 - 0.3 - 0.15), confs2)
Mmb = coo_matrix((v2, (r2, c2_)), (28, 28)).toarray(); psi = rand_state(28); p = np.abs(psi) ** 2; q = np.abs(Mmb @ psi) ** 2
hall = -1.0
for t in range(20000):
    S = rng.random(28) < rng.uniform(0.05, 0.95)
    if S.any(): pre = np.zeros(28, bool); pre[c2_[S[r2]]] = True; hall = max(hall, q[S].sum() - p[pre].sum())
check('supply-demand q(S) <= p(N^-1(S)) on every sampled target set (one block, N = 2, mu = b = 0.3; many-body block unitary)',
      hall < 1e-12 and np.abs(Mmb.conj().T @ Mmb - np.eye(28)).max() < 1e-12, f'max excess {hall:.0e}, 20000 sets')
L4 = 4; n4 = 64; co4 = np.array(list(itertools.product(range(L4), repeat=3))); ix4 = {tuple(c): i for i, c in enumerate(co4)}
def sp_layer(ublk, odd):
    u = np.zeros((n4, n4), complex)
    for base in itertools.product(range(odd, L4, 2), repeat=3):
        st = [ix4[tuple((np.array(base) + C8[k]) % L4)] for k in range(8)]; lab = [cidx(co4[x] % 2) for x in st]
        u[np.ix_(st, st)] = ublk[np.ix_(lab, lab)]
    return u
confs64 = list(itertools.combinations(range(n4), 2)); nC = len(confs64); psi = rand_state(nC); worst = 0; costs = []; nvar = []
for odd, ub in ((0, uq(np.pi / 2 - 0.3 - 0.1)), (1, uq(-(np.pi / 2 - 0.3 + 0.1)))):
    r, c, v = mb(sp_layer(ub, odd), confs64); M = coo_matrix((v, (r, c)), (nC, nC)).tocsr()
    p = np.abs(psi) ** 2; psi = M @ psi; q = np.abs(psi) ** 2; res = lp(p, q, r, c, ham(confs64, r, c), nC)
    keep = res.x > 1e-13; J = np.zeros(len(r)); J[keep] = ipf(p, q, r[keep], c[keep], nC, 2000, res.x[keep]); worst = max(worst, np.abs(np.bincount(c, J, nC) - p).max(), np.abs(np.bincount(r, J, nC) - q).max()); costs.append(res.fun); nvar.append(len(r))
check('many-body Margolus tick (4^3 torus, N = 2, entangled state, even then odd half-tick): a support-confined plan exists and carries |odds|^2',
      worst < 1e-9 and abs(np.linalg.norm(psi) - 1) < 1e-12, f'{nC} configs, err {worst:.0e}, min mean changes {costs[0]:.3f}, {costs[1]:.3f}')
r1, c1, v1 = mb(uq(np.pi / 2), [(k,) for k in range(8)]); psi1 = rand_state(8)
p1 = np.abs(psi1) ** 2; q1 = np.abs(coo_matrix((v1, (r1, c1)), (8, 8)).toarray() @ psi1) ** 2; cost1 = 2.0 * np.ones(len(r1))
Aeq = np.zeros((16, len(r1)))
for e in range(len(r1)): Aeq[c1[e], e] = 1; Aeq[8 + r1[e], e] = 1
fdim = len(r1) - np.linalg.matrix_rank(Aeq)
J1, _ = maxent(p1, q1, r1, c1, cost1, 8); pe = rng.permutation(8); inv = np.argsort(pe)
J1p, _ = maxent(p1[inv], q1[inv], pe[r1], pe[c1], cost1, 8)
def lexrank(cc, rr): o = np.lexsort((rr, cc)); rk = np.empty(len(o)); rk[o] = np.arange(len(o)); return rk
vx = lp(p1, q1, r1, c1, cost1 + 1e-3 * lexrank(c1, r1), 8).x; vxp = lp(p1[inv], q1[inv], pe[r1], pe[c1], cost1 + 1e-3 * lexrank(pe[c1], pe[r1]), 8).x
check('fewest changes alone: optimal face dim 10 at mu = 0, label-ordered vertex moves under relabelling; the max-entropy plan does not',
      fdim == 10 and np.abs(J1 - J1p).max() < 1e-10 and np.abs(vx - vxp).max() > 1e-3, f'relabel diff {np.abs(J1 - J1p).max():.0e} vs vertex {np.abs(vx - vxp).max():.2f}')
cost2 = ham(confs2, r2, c2_); psi2 = rand_state(28); p2 = np.abs(psi2) ** 2; q2 = np.abs(Mmb @ psi2) ** 2
J2, res2 = maxent(p2, q2, r2, c2_, cost2, 28); pe2 = rng.permutation(28); inv2 = np.argsort(pe2)
J2p, _ = maxent(p2[inv2], q2[inv2], pe2[r2], pe2[c2_], cost2, 28)
Hs = lambda J: -np.sum(J[J > 0] * np.log(J[J > 0]))
vtx = res2.x
check('N = 2, mu = 0.3: IPF point on the dual face is optimal, meets the max-entropy KKT form, is label-equivariant; strict concavity -> unique',
      abs(J2 @ cost2 - res2.fun) < 1e-10 and kkt(J2, r2, c2_, 28) < 1e-8 and np.abs(J2 - J2p).max() < 1e-10 and Hs(J2) > Hs(0.5 * (J2 + vtx)) > Hs(vtx),
      f'KKT {kkt(J2, r2, c2_, 28):.0e}; H {Hs(J2):.4f} > {Hs(vtx):.4f} (vertex)')
ua = uq(np.pi / 2 - 0.45); pa, pb = rand_state(8), rand_state(8)
def single(u, ps):
    r, c, v = mb(u, [(k,) for k in range(8)]); M = coo_matrix((v, (r, c)), (8, 8)).toarray(); return r, c, np.abs(ps) ** 2, np.abs(M @ ps) ** 2
ra, ca, Pa, Qa = single(ua, pa); rb, cb, Pb, Qb = single(ua, pb)
Ja, _ = maxent(Pa, Qa, ra, ca, 2.0 * (ra != ca), 8); Jb, _ = maxent(Pb, Qb, rb, cb, 2.0 * (rb != cb), 8)
RR = (ra[:, None] * 8 + rb[None]).ravel(); CC = (ca[:, None] * 8 + cb[None]).ravel()
hamAB = ((2.0 * (ra != ca))[:, None] + (2.0 * (rb != cb))[None]).ravel()
Jab, _ = maxent(np.outer(Pa, Pb).ravel(), np.outer(Qa, Qb).ravel(), RR, CC, hamAB, 64)
cfg = ((ra != ca)[:, None] | (rb != cb)[None]).astype(float).ravel()
Jcf, _ = maxent(np.outer(Pa, Pb).ravel(), np.outer(Qa, Qb).ravel(), RR, CC, cfg, 64)
Jcm = Jcf.reshape(len(ra), len(rb)); dprod = np.abs(Jab - np.outer(Ja, Jb).ravel()).max(); dcf = np.abs(Jcm - np.outer(Jcm.sum(1), Jcm.sum(0))).max()
check('two unentangled relays: occupation-change cost + max entropy = exact product plan; configuration-change cost couples them',
      dprod < 1e-10 and dcf > 1e-3, f'{dprod:.0e} vs {dcf:.1e}')

print('== T5 cell factorisation')
Pg = [np.eye(8)[:, pm] for pm in PERM]
m_plain = mult([np.trace(P) for P in Pg])
par = C8.sum(1) % 2; dia = np.array([min(i, 7 - i) for i in range(8)]); dmap = {d: k for k, d in enumerate(sorted(set(dia)))}
pb_ = np.zeros((8, 8))
for i in range(8): pb_[4 * par[i] + dmap[dia[i]], i] = 1
fac_ok = True
for k, g in enumerate(G):
    rho2 = np.eye(2) if g['sgn'] > 0 else SIG[0].real; rho4 = np.zeros((4, 4))
    for i in range(8): rho4[dmap[dia[PERM[k][i]]], dmap[dia[i]]] = 1
    fac_ok &= np.allclose(pb_ @ Pg[k] @ pb_.T, np.kron(rho2, rho4))
parts1 = [frozenset(s) for s in itertools.combinations(range(8), 4) if 0 in s]
def matchings(rest):
    if not rest: yield []; return
    a = rest[0]
    for b in rest[1:]:
        for m in matchings([x for x in rest if x not in (a, b)]): yield [frozenset((a, b))] + m
ALLM = list(matchings(list(range(8)))); prods = []
for P1 in parts1:
    for M2 in ALLM:
        if all(len(pr & P1) == 1 for pr in M2) and all(frozenset(pm[x] for x in P1) in (P1, frozenset(range(8)) - P1)
                                                     and {frozenset(pm[x] for x in pr) for pr in M2} == set(M2) for pm in PERM):
            prods.append((P1, M2))
check('plain corner permutation = A1+A2+T1+T2 (forced j = 3/2 action: 2G3/2); one rotation-invariant product of corner SETS: parity x diagonal',
      label(m_plain) == 'A1+A2+T1+T2' and len(prods) == 1 and fac_ok, f'{len(prods)} of {len(parts1)} x {len(ALLM)} candidates')
Pf = [pb_ @ P @ pb_.T for P in Pg]
cdim = null_space(np.vstack([np.kron(M, np.eye(8)) - np.kron(np.eye(8), M.T) for M in Pf])).shape[1]
X2 = np.kron(SIG[0].real, np.eye(4)); PA1 = np.kron(np.eye(2), np.full((4, 4), .25)); BL = (np.eye(8) - 4 * PA1) / 3; third = X2 @ BL
gens1 = []
for i, k in itertools.product(range(2), range(2)):
    e = np.zeros((2, 2)); e[i, k] = 1; gens1.append(np.kron(e, np.eye(4)))
for i, k in itertools.product(range(4), range(4)):
    e = np.zeros((4, 4)); e[i, k] = 1; gens1.append(np.kron(np.eye(2), e))
sol = null_space(np.array([np.concatenate([(Gm @ P - P @ Gm).ravel() for P in Pf]) for Gm in gens1]).T)
tl = np.array([(Op - np.trace(Op) / 8 * np.eye(8)).ravel() for Op in [sum(z * Gm for z, Gm in zip(col, gens1)) for col in sol.T]])
rk1 = np.linalg.matrix_rank(tl, tol=1e-9)
check('rotation commutant on C^8: 3 traceless generators (= 4 species numbers); one-factor ones only T3 = X/2, B-L = (1-4P_A1)/3; third T3(B-L)',
      cdim == 4 and rk1 == 2 and all(np.abs(third @ P - P @ third).max() < 1e-12 for P in Pf),
      'T3(B-L) eigs ' + ','.join(f'{x:g}' for x in sorted(set(np.round(np.linalg.eigvalsh(third), 6)))))
PT1 = sum(chi_irr('T1', g) * Pf[k] for k, g in enumerate(G)) * 3 / 48
Uphi = expm(1j * PT1); osr = np.sum(np.linalg.svd(Uphi.reshape(2, 4, 2, 4).transpose(0, 2, 1, 3).reshape(4, 16), compute_uv=False) > 1e-9)
check('the Hilbert-space factorisation is a U(1) family: exp(i phi P_T1) commutes with rotations, has operator Schmidt rank 2, fixes T3 and B-L',
      all(np.abs(Uphi @ P - P @ Uphi).max() < 1e-12 for P in Pf) and osr == 2 and np.abs(Uphi @ X2 - X2 @ Uphi).max() < 1e-12 and np.abs(Uphi @ BL - BL @ Uphi).max() < 1e-12)
cc = np.array([np.trace(U) for U in Us32]); cp_ = np.array([np.trace(P) for P in Pg])
m_geo = mult(cc * cp_); m_triv = mult(cc * 8)
check('rung-1 cell, coarse Gamma: geometric rotation (twist x site permutation) gives 4E1/2+4E5/2+12G3/2; 16G3/2 (all spin-1/2 x E) needs the cell index fixed',
      label(m_geo) == '4E1/2+4E5/2+12G3/2' and label(m_triv) == '16G3/2', 'W x 1_8 commutes with both')

print('== T6 cubic-frustum Regge FRW')
eta = np.diag([-1., 1, 1, 1])
def normal(pts, centre):
    V_ = np.array([q - pts[0] for q in pts[1:]]); n = null_space(V_ @ eta)[:, 0]
    if (np.mean(pts, 0) - centre) @ eta @ n < 0: n = -n
    return n / np.sqrt(n @ eta @ n)
def frustum(l, lp, T):
    pts = lambda sel: [np.array([0, *(np.array(s) * l / 2)]) for s in sel] + [np.array([T, *(np.array(s) * lp / 2)]) for s in sel]
    cen = np.array([T / 2, 0, 0, 0])
    nx = normal(pts([(1, a, b) for a in (-1, 1) for b in (-1, 1)]), cen); ny = normal(pts([(a, 1, b) for a in (-1, 1) for b in (-1, 1)]), cen)
    theta = np.pi - np.arccos(np.clip(nx @ eta @ ny, -1, 1)); m = np.array([T, (lp - l) / 2, (lp - l) / 2, 0])
    return 2 * np.pi - 4 * theta, (l + lp) / 2 * np.sqrt(-(m @ eta @ m)), np.arcsinh(abs(np.array([1., 0, 0, 0]) @ eta @ nx))
dmax = 0
for l, lp, T in ((1.0, 1.1, 0.3), (2.0, 2.5, 0.5), (1.0, 1.6, 0.45)):
    u = (lp - l) / (2 * T); e_, A_, z_ = frustum(l, lp, T)
    dmax = max(dmax, abs(e_ - 4 * np.arcsin(u * u / (1 - u * u))), abs(A_ - (l + lp) / 2 * T * np.sqrt(1 - 2 * u * u)), abs(z_ - np.arctanh(u)))
def SR(ls, Ts, sgn=1.0):
    us = [(ls[k + 1] - ls[k]) / (2 * Ts[k]) for k in range(len(Ts))]; S = 0
    for k in range(len(Ts)): e_, A_, _ = frustum(ls[k], ls[k + 1], Ts[k]); S += 3 * A_ * e_
    for k in range(1, len(ls) - 1): S += sgn * 3 * ls[k] ** 2 * 2 * (np.arctanh(us[k]) - np.arctanh(us[k - 1]))
    return S
ls = np.array([1.0, 1.07, 1.15, 1.22, 1.31]); Ts = np.array([0.21, 0.23, 0.2, 0.26]); h = 1e-6; e1 = np.eye(4)[1]; sch = {}
dA = 3 * (frustum(ls[1], ls[2], Ts[1] + h)[1] - frustum(ls[1], ls[2], Ts[1] - h)[1]) / (2 * h) * frustum(ls[1], ls[2], Ts[1])[0]
for sgn in (1.0, -1.0): sch[sgn] = abs((SR(ls, Ts + h * e1, sgn) - SR(ls, Ts - h * e1, sgn)) / (2 * h) - dA) / abs(dA)
def Af(u): return np.arcsin(u * u / (1 - u * u)) / np.sqrt(1 - 2 * u * u)
UMAX = (1 - 1e-15) / np.sqrt(2)
def u_of(y): return brentq(lambda u: Af(u) - y, 1e-300, UMAX, xtol=1e-300, rtol=1e-15) if y < Af(UMAX) else UMAX
uu = (ls[2] - ls[1]) / (2 * Ts[1])
check('explicit Minkowski frustum: trapezoid deficit 4asin(u^2/(1-u^2)), area (l+l\')T sqrt(1-2u^2)/2, square boosts atanh u; Schlaefli fixes the relative sign',
      dmax < 1e-12 and sch[1.0] < 1e-7 and sch[-1.0] > 1e-2, f'{dmax:.0e}; Schlaefli {sch[1.0]:.0e} (+) vs {sch[-1.0]:.1f} (-)')
check('lapse equation E = kappa dS/dT = 6 kappa (l+l\') A(u), A = asin(u^2/(1-u^2))/sqrt(1-2u^2); small u gives H^2 = (8 pi G/3) rho',
      abs(dA - 6 * (ls[1] + ls[2]) * Af(uu)) < 1e-6 * abs(dA))
ratios = {x: u_of(x / 2) ** 2 / (x / 2) for x in (0.01, 0.5, 1.0, 2.0)}
y = 1e-3; c2c = (u_of(y) ** 2 / y - 1 + 2 * y) / (4 * y * y); mono = np.all(np.diff([u_of(yy) for yy in np.logspace(-4, 4, 40)]) > 0)
check('exact law H^2 = (8 pi G/3) rho [1 - x + (13/12)x^2 ...], x = rho/rho*: monotone, Hl -> sqrt2, no zero at rho*; (1 - x) is first order only',
      abs(c2c - 13 / 12) < 1e-2 and abs(ratios[0.01] - (1 - .01 + 13 / 12e4)) < 1e-5 and ratios[1.0] > 0.45 and mono and abs(2 * u_of(5e3) - np.sqrt(2)) < 1e-2,
      f'x^2 coeff {c2c:.3f}; exact/(1-x): ' + ' '.join(f'{x:g}:{r:.3f}/{1 - x:.2f}' for x, r in ratios.items()))
def expo(kind, l):
    yv = (lambda s: 1 / (12 * np.exp(s))) if kind == 'dust' else (lambda s: 1 / (12 * np.exp(2 * s)))
    t = quad(lambda s: np.exp(s) / (2 * u_of(yv(s))), np.log(l) - 60, np.log(l), limit=400)[0] + l * np.exp(-60) / np.sqrt(2)
    return t * 2 * u_of(yv(np.log(l))) / l
ex = [expo('dust', 1e10), expo('rad', 1e10), expo('dust', 1e-8)]
check('dust l ~ t^(2/3), radiation l ~ t^(1/2) at late times (rho << rho*); early times coast, l ~ t, at the sqrt2 bound',
      abs(ex[0] - 2 / 3) < 1e-3 and abs(ex[1] - 0.5) < 1e-3 and abs(ex[2] - 1) < 1e-3, ' '.join(f'{e:.4f}' for e in ex))
print(f'elapsed_seconds {time.time() - T0:.1f}')
print(f'TOTAL: PASS={NP} FAIL={NF}')
