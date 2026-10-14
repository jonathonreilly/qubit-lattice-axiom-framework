"""NF-1 (a): structure checks for the Kogut-Susskind (staggered) fermion built from the root's odd box symbol s = SymS(b_f), r = 0.

Staggered single-particle law on Z^3 (continuous time, Hamiltonian form):  h = sum_j eta_j(x) S_j,  S_j = per-axis operator with symbol s(k_j)
(eta_1 = 1, eta_2 = (-1)^x1, eta_3 = (-1)^(x1+x2)).  SF strain (registered flow, applied to the staggered band E^2 = sum_j s(k_j)^2):
per-axis 1D flows phi_j of v = (t/2) sgn_j s s'  (sgn = +1, -1, 0 for x, y, z), strained symbols s_j,t = s o phi_j.
Reduced-zone (RZ) 8x8 form: h(k) = sum_j s(k_j) Gamma_j, Gamma_j[n, n^nu_j] = (-1)^{n_j}, nu_1 = 000, nu_2 = 100, nu_3 = 110;
epsilon = (-1)^(x1+x2+x3) -> Gamma_eps[n, n^111] = 1.
Checks (all printed):
 1. Clifford algebra of (Gamma_1, Gamma_2, Gamma_3, Gamma_eps).
 2. odd-harmonic property of s and of the SF-strained s_t: s_t(k + pi) = -s_t(k), phi(k + pi) = phi(k) + pi, phi odd.
 3. position space, periodic L^3: h_t built from per-axis symbols with eta phases; hermitian; spectrum = RZ symbol spectrum;
    even-range (same-sublattice) hop weight; {eps, h_t} = 0; with random U(1) links (straight axial Wilson lines) {eps, h_t[U]} = 0;
    shift symmetry S_1: chi(x) -> zeta_1(x) chi(x + e_1) commutes with h_t (any per-axis amplitudes).
 4. continuous U(1)_eps in Hamiltonian form: needs [eps, h] = 0 -> reports ||[eps, h]|| / ||h|| (= 2 when {eps, h} = 0).
 5. control dressing G1_stag = sum_j i eps eta_j sin(-i d_j) (RZ: sin k_j i Gamma_eps Gamma_j; KS image of F3's G1 with beta -> eps):
    h' = V h V^dag, V = exp(i a G1): weight of the eps-COMMUTING (same-sublattice, mass-type) part of h'.
 6. dictionary: an 8x8 unitary U with U Gamma_j U^dag = alpha_j x 1_2, U Gamma_eps U^dag = beta x 1_2 (F3's alpha, beta).
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from sublum import SymS
from f3_dirac import alpha, beta, I4

BF = 0.909103708
A = SymS(BF)
s, ds = A.s, A.ds

idx = lambda n: n[0] + 2*n[1] + 4*n[2]
bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
NU = [(0, 0, 0), (1, 0, 0), (1, 1, 0)]
def xor(a, b): return tuple((x + y) % 2 for x, y in zip(a, b))
Gam = []
for j in range(3):
    Gm = np.zeros((8, 8))
    for n in bits:
        Gm[idx(n), idx(xor(n, NU[j]))] = (-1)**n[j]
    Gam.append(Gm)
Geps = np.zeros((8, 8))
for n in bits:
    Geps[idx(n), idx(xor(n, (1, 1, 1)))] = 1.0
G4 = Gam + [Geps]
print('1. Clifford: max |{G_a, G_b} - 2 delta_ab| over a,b in (G1, G2, G3, Geps) = %.1e' %
      max(np.abs(G4[a] @ G4[b] + G4[b] @ G4[a] - 2*(a == b)*np.eye(8)).max() for a in range(4) for b in range(4)))


def rk4(f, y, n=8):
    h = 1.0/n
    for _ in range(n):
        k1 = f(y); k2 = f(y + 0.5*h*k1); k3 = f(y + 0.5*h*k2); k4 = f(y + h*k3)
        y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
    return y
def phi(k, t, sgn, n=8):
    """1D SF flow of the staggered band along one axis (separable: p_j = s s')."""
    if t == 0 or sgn == 0:
        return np.array(k, float)
    return rk4(lambda y: 0.5*sgn*t*s(y)*ds(y), np.array(k, float), n)

kk = np.linspace(-np.pi, np.pi, 20001)
print('2. odd-harmonic: max|s(k+pi) + s(k)| = %.1e' % np.abs(s(kk + np.pi) + s(kk)).max())
for t in (0.1, 0.3, -0.3):
    for sg in (+1, -1):
        p0, p1 = phi(kk, t, sg), phi(kk + np.pi, t, sg)
        print('   t=%+.1f sgn=%+d: max|phi(k+pi) - phi(k) - pi| = %.1e ; max|phi(-k) + phi(k)| = %.1e ; max|s_t(k+pi) + s_t(k)| = %.1e'
              % (t, sg, np.abs(p1 - p0 - np.pi).max(), np.abs(phi(-kk, t, sg) + p0).max(), np.abs(s(p1) + s(p0)).max()))


def pos_space(L, t, links=None, seed=0):
    """dense L^3 x L^3 staggered h_t; links: None or random U(1) angles on bonds (straight axial Wilson lines)."""
    k1 = 2*np.pi*np.arange(L)/L
    sym = [s(phi(k1, t, sg)) for sg in (+1, -1, 0)]
    # per-axis kernel K_j(r) = (1/L) sum_k s_j(k) e^{i k r}  (h acts as (S_j chi)(x) = sum_r K_j(r) chi(x + r e_j))
    ker = [np.fft.ifft(sy) for sy in sym]                 # ker[r] = (1/L) sum_k s(k) e^{+i k r}
    V = L**3
    X = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
    eta = [np.ones(V), (-1.0)**X[:, 0], (-1.0)**(X[:, 0] + X[:, 1])]
    rng = np.random.default_rng(seed)
    th = rng.uniform(-np.pi, np.pi, (3, L, L, L)) if links else np.zeros((3, L, L, L))
    H = np.zeros((V, V), complex)
    for j in range(3):
        for r in range(1, L):
            amp = ker[j][r]
            if abs(amp) < 1e-300:
                continue
            Y = X.copy(); Y[:, j] = (Y[:, j] + r) % L
            # straight Wilson line x -> x + r e_j : product of bond phases
            ph = np.zeros(V)
            Z = X.copy()
            if r < L - r:                                  # forward straight path, r bonds
                for st in range(r):
                    ph += th[j][Z[:, 0], Z[:, 1], Z[:, 2]]
                    Z[:, j] = (Z[:, j] + 1) % L
            else:                                          # backward straight path, L - r bonds (same path as the h.c. hop)
                for st in range(L - r):
                    Z[:, j] = (Z[:, j] - 1) % L
                    ph -= th[j][Z[:, 0], Z[:, 1], Z[:, 2]]
            iy = np.ravel_multi_index(Y.T, (L, L, L))
            H[np.arange(V), iy] += eta[j]*amp*np.exp(1j*ph)
    return H, X, sym

for L in (8,):
    for t, lk in ((0.0, False), (0.3, False), (0.3, True)):
        H, X, sym = pos_space(L, t, lk)
        eps = (-1.0)**X.sum(1)
        herm = np.abs(H - H.conj().T).max()
        anti = np.abs(eps[:, None]*H*eps[None, :] + H).max()
        same = np.abs(H[(eps[:, None]*eps[None, :]) > 0]).max()
        line = '3. L=%d t=%+.1f links=%s: herm %.1e ; |{eps,h}| %.1e ; max same-sublattice |h| %.1e' % (L, t, lk, herm, anti, same)
        if not lk:
            ev = np.sort(np.linalg.eigvalsh(H))
            kr = 2*np.pi*np.arange(-L//4, L//4)/L
            KX, KY, KZ = np.meshgrid(kr, kr, kr, indexing='ij')
            ix = lambda k: np.round(k/(2*np.pi/L)).astype(int) % L
            E = np.sqrt(sym[0][ix(KX)]**2 + sym[1][ix(KY)]**2 + sym[2][ix(KZ)]**2).ravel()
            evRZ = np.sort(np.concatenate([np.repeat(E, 4), -np.repeat(E, 4)]))
            line += ' ; max|spec - RZ spec| %.1e' % np.abs(ev - evRZ).max()
            # RZ symbol check at a random allowed k: eigenvalues of sum s Gamma_j are +-E (x4)
            # shift symmetry S_1: chi(x) -> zeta_1(x) chi(x + e_1), zeta_1 = (-1)^(x2 + x3)
            V_ = L**3
            Y = X.copy(); Y[:, 0] = (Y[:, 0] + 1) % L
            Sh = np.zeros((V_, V_)); Sh[np.arange(V_), np.ravel_multi_index(Y.T, (L, L, L))] = (-1.0)**(X[:, 1] + X[:, 2])
            line += ' ; |[S_1, h]| %.1e' % np.abs(Sh @ H - H @ Sh).max()
            Y = X.copy(); Y[:, 2] = (Y[:, 2] + 1) % L
            Sh3 = np.zeros((V_, V_)); Sh3[np.arange(V_), np.ravel_multi_index(Y.T, (L, L, L))] = 1.0
            line += ' ; |[S_3, h]| %.1e' % np.abs(Sh3 @ H - H @ Sh3).max()
            if t == 0.3:
                comm = np.linalg.norm(eps[:, None]*H - H*eps[None, :])/np.linalg.norm(H)
                print('4. continuous U(1)_eps (needs [eps, h] = 0): ||[eps, h]||/||h|| = %.6f  (2 exactly when {eps, h} = 0)' % comm)
                # 5. G1 dressing in position space: G = sum_j i eps eta_j Ssin_j
                k1 = 2*np.pi*np.arange(L)/L
                Gs = np.zeros_like(H)
                for j in range(3):
                    kerS = np.fft.ifft(np.sin(k1))
                    for r in range(1, L):
                        Yr = X.copy(); Yr[:, j] = (Yr[:, j] + r) % L
                        etaj = [np.ones(V_), (-1.0)**X[:, 0], (-1.0)**(X[:, 0] + X[:, 1])][j]
                        Gs[np.arange(V_), np.ravel_multi_index(Yr.T, (L, L, L))] += 1j*eps*etaj*kerS[r]
                print('5. G1_stag: hermitian %.1e ; {eps, G1} %.1e (G1 is an odd hop, so V = exp(i a G1) does NOT commute with eps)'
                      % (np.abs(Gs - Gs.conj().T).max(), np.abs(eps[:, None]*Gs*eps[None, :] + Gs).max()))
                w, U = np.linalg.eigh(Gs)
                for a in (0.01, 0.1):
                    Vd = (U*np.exp(1j*a*w)) @ U.conj().T
                    Hd = Vd @ H @ Vd.conj().T
                    even = 0.5*(Hd + eps[:, None]*Hd*eps[None, :])
                    print('   a=%.2f: ||eps-commuting part of V h V^dag|| / ||h|| = %.3e ; spectrum change %.1e'
                          % (a, np.linalg.norm(even)/np.linalg.norm(H), np.abs(np.linalg.eigvalsh(Hd) - ev).max()))
        print(line, flush=True)

# 6. dictionary: find U with U G_j U^dag = alpha_j x 1, U Geps U^dag = beta x 1
tgt = [np.kron(alpha[j], np.eye(2)) for j in range(3)] + [np.kron(beta, np.eye(2))]
# intertwiner: X = sum over the 16-element Clifford group basis of tgt-word x Gam-word^dag (Schur averaging)
words = []
for m in range(16):
    W8 = np.eye(8); Wt = np.eye(8, dtype=complex)
    for a in range(4):
        if (m >> a) & 1:
            W8 = W8 @ G4[a]; Wt = Wt @ tgt[a]
    words.append((W8, Wt))
rng = np.random.default_rng(5)
for trial in range(5):
    R = rng.normal(size=(8, 8)) + 1j*rng.normal(size=(8, 8))
    Xm = sum(Wt @ R @ W8.conj().T for W8, Wt in words)
    if np.linalg.matrix_rank(Xm) == 8:
        break
Uu, _, Vh = np.linalg.svd(Xm); Ud = Uu @ Vh                  # polar unitary part
print('6. dictionary U (8x8 unitary): max|U G_a U^dag - target_a| = %.1e  (targets alpha_j x 1_2, beta x 1_2)'
      % max(np.abs(Ud @ G4[a] @ Ud.conj().T - tgt[a]).max() for a in range(4)))
print('   => i G_eps G_j <-> i beta alpha_j x 1_2: %.1e' % max(np.abs(Ud @ (1j*Geps @ Gam[j]) @ Ud.conj().T - np.kron(1j*beta @ alpha[j], np.eye(2))).max() for j in range(3)))
np.save(os.path.join(HERE, 'nf1_dict.npy'), Ud)
np.save(os.path.join(HERE, 'nf1_gammas.npy'), np.array(G4))
