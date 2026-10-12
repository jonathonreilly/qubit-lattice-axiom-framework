"""C5 R12-3, script 1: the BF (cochain) Nicolai gauge multiplet on Z^3 and its Chern / helicity bookkeeping.

Fields per site: A in Omega^1 (links, gauge), B in Omega^2 (plaquettes, neutral), tau in Omega^3 (cubes, neutral).
Superpotential (real, quadratic, gauge invariant):  W = <B, dA> + <tau, dB>.
Hessian / photino one-particle operator  C(q) = [[0, d1^+, 0], [d1, 0, d2^+], [0, d2, 0]]  (7x7), with
  d0 = (D_1, D_2, D_3)^T,  (d1 A)_{jk} = D_j A_k - D_k A_j  [(23),(31),(12)],  d2 B = D_1 B_23 + D_2 B_31 + D_3 B_12,
  D_j(q) = e^{i q_j} - 1 (cochain, 'Wilson') or the R8-5 box symbol D_j = i d(q_j) e^{i q_j/2}, d = rho q + (1-rho) 2 sin(q/2).
Checks:
 (1) d1 d0 = 0, d2 d1 = 0 (complex), C (d0,0,0) = 0 (gauge invariance of W), C^2 = Delta * P_phys, Delta = sum |D_j|^2;
 (2) doubler scan: min over the N^3 grid (q != 0) of the smallest nonzero |eig C| -- equals min sqrt(Delta) > 0;
     box: sqrt(Delta) = |q| exactly in the box;
 (3) V = (1/2)|grad W|^2 = (1/2)|F|^2 + (1/2)<B, Delta B> + (1/2)<tau, Delta tau> (Maxwell emerges) -- symbol check;
 (4) Chern number of the positive-eigenvalue bundle on a small sphere around q = 0 (Fukui-Hatsugai, non-Abelian det):
     BF lattice / BF continuum / curl-only (class S, R10-5) / odd-signature (sigma, A) / full Kaehler-Dirac;
 (5) twisted helicity content (J_z on forms) of the positive band at q = q z-hat (continuum symbols);
 (6) linear-order A-field mixing allowed by proper cubic covariance + transversality, per irrep of O (A1,A2,E,T1,T2).
"""
import numpy as np, sys, itertools, time
sys.path.insert(0, '.')
from r85_box_qed_copy import plateau
t0 = time.time()
eps3 = np.zeros((3, 3, 3))
for (i, j, k), s in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    eps3[i, j, k] = s
PAIRS = [(1, 2), (2, 0), (0, 1)]  # Omega^2 basis (23),(31),(12)

def Dwil(q):
    return np.exp(1j * np.asarray(q)) - 1

def dbox(qj, c1=1.0, c2=2.0):
    rg = plateau(np.array([qj]), c1, c2)[0]
    return rg * qj + (1 - rg) * 2 * np.sin(qj / 2)

def Dbox(q, c1=1.0, c2=2.0):
    q = (np.asarray(q) + np.pi) % (2 * np.pi) - np.pi
    return np.array([1j * dbox(qj, c1, c2) * np.exp(1j * qj / 2) for qj in q])

def Dcont(q):
    return 1j * np.asarray(q, dtype=complex)

def ops(D):
    d0 = D.reshape(3, 1)
    d1 = np.zeros((3, 3), complex)
    for r, (j, k) in enumerate(PAIRS):
        d1[r, k] += D[j]; d1[r, j] -= D[k]
    d2 = np.array([[D[0], D[1], D[2]]], complex)
    return d0, d1, d2

def C_bf(D):
    d0, d1, d2 = ops(D)
    C = np.zeros((7, 7), complex)
    C[3:6, 0:3] = d1; C[0:3, 3:6] = d1.conj().T
    C[6:7, 3:6] = d2; C[3:6, 6:7] = d2.conj().T
    return C

def C_kd(D):
    """Full Kaehler-Dirac d + d^+ on Omega^0+1+2+3 (8x8): sigma, A, B, tau (gauge-FIXED: contains d0^+ A)."""
    d0, d1, d2 = ops(D)
    K = np.zeros((8, 8), complex)
    K[1:4, 0:1] = d0; K[0:1, 1:4] = d0.conj().T
    K[4:7, 1:4] = d1; K[1:4, 4:7] = d1.conj().T
    K[7:8, 4:7] = d2; K[4:7, 7:8] = d2.conj().T
    return K

def C_curl(q):  # class-S photino operator (R10-5): i eps . s(q), s = sin q
    s = np.sin(q)
    return 1j * np.einsum('ijk,j->ik', eps3, s)

def C_curl_cont(q):
    return 1j * np.einsum('ijk,j->ik', eps3, np.asarray(q, float))

def C_oddsig_cont(q):  # (sigma, A): [[0, q^T],[q, i eps.q]]  (Floer extended Hessian / twisted N=2 photino)
    L = np.zeros((4, 4), complex)
    L[0, 1:] = np.asarray(q); L[1:, 0] = np.asarray(q); L[1:, 1:] = C_curl_cont(q)
    return L

print('(1) algebra checks')
rng = np.random.default_rng(1)
worst = dict(dd=0, gauge=0, sq=0, V=0)
for Dfun, lab in [(Dwil, 'cochain'), (Dbox, 'box (c1,c2)=(1,2)')]:
    for _ in range(400):
        q = rng.uniform(-np.pi, np.pi, 3)
        D = Dfun(q)
        d0, d1, d2 = ops(D)
        C = C_bf(D)
        worst['dd'] = max(worst['dd'], np.abs(d1 @ d0).max(), np.abs(d2 @ d1).max())
        g = np.concatenate([d0[:, 0], np.zeros(4)])
        worst['gauge'] = max(worst['gauge'], np.abs(C @ g).max())
        Delta = np.sum(np.abs(D) ** 2)
        Pphys = np.eye(7) - np.outer(g, g.conj()) / np.vdot(g, g).real
        worst['sq'] = max(worst['sq'], np.abs(C @ C - Delta * Pphys).max())
        # potential symbol: (1/2)|C x|^2 = (1/2) x^+ C^2 x ; A-block of C^2 = d1^+ d1 (Maxwell F^2), B-block Delta, tau-block Delta
        C2 = C @ C
        worst['V'] = max(worst['V'], np.abs(C2[0:3, 0:3] - d1.conj().T @ d1).max(),
                         np.abs(C2[3:6, 3:6] - Delta * np.eye(3)).max(), abs(C2[6, 6] - Delta))
    print('   %-20s max|d d|=%.1e  max|C g|=%.1e  max|C^2 - Delta P_phys|=%.1e  potential=Maxwell+Delta blocks: %.1e' % (
        lab, worst['dd'], worst['gauge'], worst['sq'], worst['V']))
    worst = dict(dd=0, gauge=0, sq=0, V=0)

print('(2) doubler scan: smallest nonzero |eig C_BF| over N^3 grid, q != 0 (photon/photino zeros only at q = 0?)')
for Dfun, lab in [(Dwil, 'cochain'), (Dbox, 'box (1,2)')]:
    for N in (16, 24):
        kk = 2 * np.pi * np.arange(N) / N - np.pi
        mn, arg, mnT = 9, None, 9
        for q in itertools.product(kk, kk, kk):
            q = np.array(q)
            if np.allclose(q, 0):
                continue
            w = np.linalg.eigvalsh(C_bf(Dfun(q)))
            w = np.sort(np.abs(w))[1:]  # drop the gauge zero
            if w[0] < mn:
                mn, arg = w[0], q.copy()
        print('   %-10s N=%2d  min|eig|=%.4f at q=%s ; sqrt(Delta) there = %.4f ; nearest-to-0 grid |q| = %.4f' % (
            lab, N, mn, np.round(arg, 3), np.sqrt(np.sum(np.abs(Dfun(arg)) ** 2)), 2 * np.pi / N))
    # class S curl control: zeros at the pi points
    if lab == 'cochain':
        z = [np.sort(np.abs(np.linalg.eigvalsh(C_curl(np.array(q)))))[1] for q in [(np.pi, 0, 0), (np.pi, np.pi, 0), (np.pi, np.pi, np.pi)]]
        print('   control class-S lattice curl i eps.sin q: transverse |eig| at (pi,0,0),(pi,pi,0),(pi,pi,pi) =', np.round(z, 12))
qs = [np.array([0.3, -0.5, 0.7]), np.array([0.9, 0.2, -0.95])]
for q in qs:
    w = np.sort(np.linalg.eigvalsh(C_bf(Dbox(q))))
    print('   box: q=%s (inside photon plateau) eigs=%s  |q|=%.12f' % (q, np.round(w, 12), np.linalg.norm(q)))

print('(4) Chern numbers of the positive-eigenvalue bundle on a sphere |q| = r around 0 (Fukui-Hatsugai)')

def chern_pos(Hfun, r=0.05, nt=60, nphi=60, drop_zero=True):
    th = np.linspace(1e-4, np.pi - 1e-4, nt)
    ph = np.linspace(0, 2 * np.pi, nphi, endpoint=False)
    frames = np.empty((nt, nphi), object)
    rank = None
    for a, t in enumerate(th):
        for b, p in enumerate(ph):
            q = r * np.array([np.sin(t) * np.cos(p), np.sin(t) * np.sin(p), np.cos(t)])
            w, V = np.linalg.eigh(Hfun(q))
            sel = w > 1e-9 * r
            frames[a, b] = V[:, sel]
            rank = sel.sum() if rank is None else rank
            assert sel.sum() == rank
    F = 0.0
    def U(X, Y):
        dt = np.linalg.det(X.conj().T @ Y)
        return dt / abs(dt)
    for a in range(nt - 1):
        for b in range(nphi):
            b2 = (b + 1) % nphi
            prod = U(frames[a, b], frames[a + 1, b]) * U(frames[a + 1, b], frames[a + 1, b2]) * \
                   U(frames[a + 1, b2], frames[a, b2]) * U(frames[a, b2], frames[a, b])
            F += np.angle(prod)
    # polar caps: north/south cap loops
    for a in (0, nt - 1):
        prod = 1.0
        for b in range(nphi):
            prod *= U(frames[a, b], frames[a, (b + 1) % nphi])
        F += (np.angle(prod) if a == 0 else -np.angle(prod))
    return F / (2 * np.pi), rank

cases = [('class S lattice curl i eps.sin q (R10-5 control)', lambda q: C_curl(q)),
         ('continuum curl i eps.q', lambda q: C_curl_cont(q)),
         ('continuum odd signature (sigma,A) [twisted N=2 photino]', lambda q: C_oddsig_cont(q)),
         ('BF continuum (A,B,tau)', lambda q: C_bf(Dcont(q))),
         ('BF cochain lattice (A,B,tau)', lambda q: C_bf(Dwil(q))),
         ('BF box lattice (A,B,tau)', lambda q: C_bf(Dbox(q))),
         ('Kaehler-Dirac Omega^0..3 cochain (8x8)', lambda q: C_kd(Dwil(q)))]
for lab, f in cases:
    c, rk = chern_pos(f)
    print('   %-58s rank(P+)=%d  c1 = %+.4f' % (lab, rk, c))

print('(5) twisted helicity content (J_z on forms) of the positive band, continuum symbols at q = (0,0,1)')
Lz1 = -1j * eps3[2]  # vector generator about z: (L_z)_{jk} = -i eps_{zjk}
def Jz_block(dims):
    blocks = []
    for d in dims:
        blocks.append(np.zeros((1, 1)) if d == 1 else Lz1)
    n = sum(b.shape[0] for b in blocks); J = np.zeros((n, n), complex); o = 0
    for b in blocks:
        J[o:o + b.shape[0], o:o + b.shape[0]] = b; o += b.shape[0]
    return J
for lab, Hq, dims in [('BF (A,B,tau)', C_bf(Dcont([0, 0, 1.0])), (3, 3, 1)),
                      ('odd signature (sigma,A)', C_oddsig_cont([0, 0, 1.0]), (1, 3)),
                      ('Kaehler-Dirac (sigma,A,B,tau)', C_kd(Dcont([0, 0, 1.0])), (1, 3, 3, 1)),
                      ('class S curl (A)', C_curl_cont([0, 0, 1.0]), (3,))]:
    w, V = np.linalg.eigh(Hq)
    Pp = V[:, w > 1e-9]
    Jz = Jz_block(dims)
    assert np.abs(Jz @ Hq - Hq @ Jz).max() < 1e-12
    h = np.linalg.eigvalsh(Pp.conj().T @ Jz @ Pp)
    print('   %-32s positive-band twisted helicities: %s  (count %d)' % (lab, np.round(h, 6), len(h)))

print('(6) linear A-field mixing c_{j alpha k} q_k allowed by proper-cubic covariance + transversality (q.c = 0)')
Rs = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[i, perm[i]] = sg[i]
        if np.isclose(np.linalg.det(R), 1):
            Rs.append(R)
assert len(Rs) == 24
def permsign(R):
    P = np.abs(R); p = [int(np.argmax(P[i])) for i in range(3)]
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s, p
# E rep: S3 permutation action on the 2-dim standard rep
e1 = np.array([1, -1, 0]) / np.sqrt(2); e2 = np.array([1, 1, -2]) / np.sqrt(6)
def Erep(R):
    s, p = permsign(R)
    P = np.zeros((3, 3))
    for i in range(3):
        P[i, p[i]] = 1
    B = np.vstack([e1, e2])
    return B @ P @ B.T
reps = {'A1': lambda R: np.eye(1), 'A2': lambda R: np.array([[permsign(R)[0]]], float), 'E': Erep,
        'T1': lambda R: R, 'T2': lambda R: permsign(R)[0] * R}
for name, rho in reps.items():
    da = rho(Rs[0]).shape[0]
    n = 3 * da * 3
    rows = []
    for R in Rs:
        M = np.kron(np.kron(R, rho(R)), R)
        rows.append(M - np.eye(n))
    # transversality: symmetric part in (j,k) vanishes for each alpha
    for al in range(da):
        for j in range(3):
            for k in range(j, 3):
                row = np.zeros(n)
                row[(j * da + al) * 3 + k] += 1; row[(k * da + al) * 3 + j] += 1
                rows.append(row[None, :])
    Mbig = np.vstack(rows)
    sv = np.linalg.svd(Mbig, compute_uv=False)
    null = int(np.sum(sv < 1e-9)) + max(0, n - len(sv))
    print('   field in irrep %-3s (dim %d): dimension of allowed linear transverse A-mixing = %d' % (name, da, null))
print('elapsed %.1fs' % (time.time() - t0))
