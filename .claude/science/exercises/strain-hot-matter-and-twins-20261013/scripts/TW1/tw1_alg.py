"""TW-1 (a), (b)-algebra, (c)-symmetries: the reduced (Majorana) staggered field in continuous time.

Setting (TESTS TW-1 shared setting): staggered law h = sum_j eta_j(x) S_j, S_j with symbol s = SymS(0.909103708) (root odd box
symbol, r = 0), continuous time, SF strain (per-axis 1D flow of E^2 = sum s^2), NF-1's reduced-zone gammas (nf1_gammas.npy).

Checks printed:
 1. Reduced-zone algebra: real commutant of (G1, G2, G3, Geps) (expect the quaternions H: 1, J1, J2, J3);
    J-space = span{Z_i Z_j} with Z_j the K = 0 matrices of the shift symmetries S_j (computed from position space, L = 8);
    Majorana-legal constant bilinears (hermitian AND antisymmetric: M = i A, A real antisymmetric; 28 of them);
    which are allowed by Theta_M ({M, Geps} = 0) and by P_stag ([M, Geps] = 0 at K = 0): intersection = {0};
    gap-opening ones (anticommute with G1, G2, G3) = span{i Geps J_a} (3), and Geps itself (the complex field's staggered
    mass) is symmetric, hence absent from a Majorana field.
 2. Fock-space identity on a small system (Jordan-Wigner, 6 modes): for h = i B with B real antisymmetric,
    sum chi^dag h chi = (i/2)(xi1 B xi1 + xi2 B xi2) + const (two decoupled Majorana copies); control: complex (charged) h
    leaves cross terms.
 3. Position space L = 8: the strained staggered law (t = 0, 0.3) is purely imaginary (h = i B, B real antisymmetric).
    SO(3) links (real rep, 3 colours, random): h[O] = i B[O], B real antisymmetric; Theta_M: eps B eps = -B;
    P_stag: P h[O] P^T = h[O^P] with O^P_j(x) = O_j(-x-e_j)^T.
    SU(2) links (pseudo-real): h[U] is not purely imaginary; the antiunitary (i sigma_2) K anticommutes with h[U] and squares
    to -1; the real commutant of the realified SU(2) action on R^4 is 4-dimensional with no nontrivial symmetric
    idempotent (no gauge-covariant halving); for SO(3) on R^6 = (C^3)_R the commutant is M_2(R) and contains rank-3
    projectors (Re/Im split).  U(1) charge 1 on R^2: commutant C, no projector.
 4. Locality of the J-type Majorana mass: R_12 = (S1 S2 - (S1 S2)^T)/2 has reduced-zone matrix f(K) Z1 Z2 (printed),
    so i eps R_12 is a local, hermitian, antisymmetric two-link operator; its parities under S_k, Theta_M.
 5. Cubic rotations: sign functions D_R making O_R = D_R P_R a symmetry of h (root symbol, L = 4 and 8);
    action on Geps and on the J-triplet at K = 0; is any i Geps J combination invariant?
argv: none.
"""
import numpy as np, sys, os, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', 'flat'))
from sublum import SymS

np.set_printoptions(linewidth=160, precision=4, suppress=True)
BF = 0.909103708
A = SymS(BF)
s, ds = A.s, A.ds
G4 = np.load(os.path.join(HERE, 'nf1_gammas.npy'))
Gam, Geps = G4[:3], G4[3]
print('0. gammas real: %s ; symmetric: max|G - G^T| = %.1e' % (np.isrealobj(G4) or np.abs(G4.imag).max() == 0,
      max(np.abs(g - g.T).max() for g in G4)))


def nullspace(M, tol=1e-10):
    u, sv, vh = np.linalg.svd(M)
    r = (sv > tol*max(1, sv.max() if len(sv) else 1)).sum()
    return vh[r:].conj().T


def commutant_real(mats, n):
    """real n x n X with [m, X] = 0 for all m (m real)."""
    rows = []
    E = np.eye(n*n).reshape(n*n, n, n)
    for m in mats:
        rows.append(np.array([(m @ e - e @ m).ravel() for e in E]).T)
    return nullspace(np.vstack(rows)).T.reshape(-1, n, n)


# ---------------- 1. reduced-zone algebra
C = commutant_real(list(G4), 8)
print('1. real commutant of (G1,G2,G3,Geps): dim %d' % len(C))
# antisymmetric (traceless) part -> J's
Asym = [c - c.T for c in C]
Js = np.array([a for a in Asym if np.linalg.norm(a) > 1e-8])
# orthonormalise the J-space
Q = nullspace(np.array([j.ravel() for j in Js]).T @ np.zeros((len(Js), 0))) if False else None
U_, S_, Vh_ = np.linalg.svd(np.array([j.ravel() for j in Js]).T, full_matrices=False)
Jb = [(U_[:, i]*np.sqrt(8)).reshape(8, 8) for i in range(int((S_ > 1e-8).sum()))]
print('   antisymmetric part of the commutant: dim %d; J^2 = -1: %s' % (len(Jb), [round(float(np.abs(J @ J + np.eye(8)).max()), 12) for J in Jb]))


# position-space helpers (L^3 torus), plain dense matrices
def lattice(L):
    V = L**3
    X = np.array(np.unravel_index(np.arange(V), (L, L, L))).T
    return V, X


def shift_op(L, j):
    """(S_j chi)(x) = zeta_j(x) chi(x + e_j), zeta_1 = (-1)^(x2+x3), zeta_2 = (-1)^x3, zeta_3 = 1 (NF-1 nf1_alg.py:3)."""
    V, X = lattice(L)
    Y = X.copy(); Y[:, j] = (Y[:, j] + 1) % L
    z = [(-1.0)**(X[:, 1] + X[:, 2]), (-1.0)**X[:, 2], np.ones(V)][j]
    S = np.zeros((V, V)); S[np.arange(V), np.ravel_multi_index(Y.T, (L, L, L))] = z
    return S


def rz_matrix(O, L, K):
    """reduced-zone 8x8 matrix <K + pi n| O |K + pi m>, plane waves |k> = V^-1/2 sum_x e^{i k x}|x>, n in {0,1}^3 (bit order x,y,z)."""
    V, X = lattice(L)
    bits = [((i >> 0) & 1, (i >> 1) & 1, (i >> 2) & 1) for i in range(8)]
    W = np.array([np.exp(1j*(X @ (np.array(K) + np.pi*np.array(b))))/np.sqrt(V) for b in bits]).T   # V x 8
    return W.conj().T @ O @ W


def ham(L, t, sym=None):
    """staggered h (U = 1) from per-axis symbols (strained by the separable SF flow, sgn = +1, -1, 0)."""
    import contextlib, io
    with contextlib.redirect_stdout(io.StringIO()):      # nf1_poslib prints its own module-level checks on import
        from nf1_poslib import pos_space
    H, X, sy, th = pos_space(L, t, None)
    return H, X


L = 8
Ssh = [shift_op(L, j) for j in range(3)]
H0, X8 = ham(L, 0.0)
print('   shifts commute with h (L = 8, t = 0): %s' % [float('%.1e' % np.abs(S @ H0 - H0 @ S).max()) for S in Ssh])
# convention check of the reduced-zone basis against nf1's gammas: h(K) at K = (2 pi/L) e_j
for j in range(3):
    K = np.zeros(3); K[j] = 2*np.pi/L
    hK = rz_matrix(H0, L, K)
    print('   convention: |h(K) + s(K_j) Gamma_j| at K = 2pi/L e_%d : %.1e  (s = %.6f; h|k> = -s(k)|k> in this plane-wave convention, an overall sign)' % (j + 1, np.abs(hK + s(K[j])*Gam[j]).max(), s(K[j])))
epsop = np.diag((-1.0)**X8.sum(1))
print('   eps at K = 0 equals Geps: %.1e' % np.abs(rz_matrix(epsop, L, np.zeros(3)) - Geps).max())
Z = [rz_matrix(S, L, np.zeros(3)) for S in Ssh]
print('   Z_j = S_j at K = 0: real %.1e ; [Z_j, G_i] max %.1e ; {Z_j, Geps} max %.1e ; Z_j^2 = 1: %.1e'
      % (max(np.abs(z.imag).max() for z in Z), max(np.abs(z @ g - g @ z).max() for z in Z for g in Gam),
         max(np.abs(z @ Geps + Geps @ z).max() for z in Z), max(np.abs(z @ z - np.eye(8)).max() for z in Z)))
Z = [z.real for z in Z]
print('   {Z_i, Z_j} (i != j) max %.1e' % max(np.abs(Z[a] @ Z[b] + Z[b] @ Z[a]).max() for a in range(3) for b in range(3) if a != b))
JZ = {(0, 1): Z[0] @ Z[1], (1, 2): Z[1] @ Z[2], (0, 2): Z[0] @ Z[2]}
for k, J in JZ.items():
    print('   J_%d%d = Z_%d Z_%d: J^2 + 1 %.1e ; antisym %.1e ; commutes with G1..3, Geps: %.1e ; in commutant span: resid %.1e'
          % (k[0] + 1, k[1] + 1, k[0] + 1, k[1] + 1, np.abs(J @ J + np.eye(8)).max(), np.abs(J + J.T).max(),
             max(np.abs(J @ g - g @ J).max() for g in G4),
             np.linalg.lstsq(np.array([c.ravel() for c in C]).T, J.ravel(), rcond=None)[1].sum() if True else 0))
J12, J23, J13 = JZ[(0, 1)], JZ[(1, 2)], JZ[(0, 2)]
print('   J12 J23 = %s J13 (sign) ; resid %.1e' % ('+' if np.abs(J12 @ J23 - J13).max() < 1e-12 else '-', min(np.abs(J12 @ J23 - J13).max(), np.abs(J12 @ J23 + J13).max())))

# Majorana-legal constant bilinears: M = i A, A real antisymmetric (28-dim)
basisA = []
for a in range(8):
    for b in range(a + 1, 8):
        E = np.zeros((8, 8)); E[a, b] = 1; E[b, a] = -1; basisA.append(E)
basisA = np.array(basisA)
def dim_solutions(cond):
    M = np.array([cond(Ab).ravel() for Ab in basisA]).T
    return len(nullspace(M).T)
dTh = dim_solutions(lambda Ab: Ab @ Geps + Geps @ Ab)              # Theta_M: anticommute with Geps
dPs = dim_solutions(lambda Ab: Ab @ Geps - Geps @ Ab)              # P_stag at K = 0: commute
dBoth = dim_solutions(lambda Ab: np.concatenate([(Ab @ Geps + Geps @ Ab).ravel(), (Ab @ Geps - Geps @ Ab).ravel()]))
dGap = dim_solutions(lambda Ab: np.concatenate([(Ab @ g + g @ Ab).ravel() for g in Gam]))
print('   Majorana-legal constant bilinears: 28; Theta_M-allowed %d ; P_stag-allowed (K=0) %d ; both %d' % (dTh, dPs, dBoth))
print('   gap-opening (anticommute with G1,G2,G3) Majorana-legal: dim %d ; (the i Geps J_a anticommute with G_j: resid %.1e; the other 3 are i G5 J_a, next line)'
      % (dGap, max(np.abs(Geps @ J @ g + g @ Geps @ J).max() for J in (J12, J23, J13) for g in Gam)))
G5 = Geps @ Gam[0] @ Gam[1] @ Gam[2]
print('   G5 := Geps G1 G2 G3: symmetric %.1e ; {G5, G_j} %.1e ; {G5, Geps} %.1e' % (np.abs(G5 - G5.T).max(), max(np.abs(G5 @ g + g @ G5).max() for g in Gam), np.abs(G5 @ Geps + Geps @ G5).max()))
gapB = [1j*Geps @ J for J in (J23, J13, J12)] + [1j*G5 @ J for J in (J23, J13, J12)]
Mg = np.array([g.ravel() for g in gapB]).T
print('   gap-opening Majorana masses = span{i Geps J_a} (+) span{i G5 J_a}: rank %d ; Majorana-legal (antisym) %.1e' % (np.linalg.matrix_rank(Mg), max(np.abs(g + g.T).max() for g in gapB)))
print('     i Geps J_a: [., Geps] = 0 -> excluded by Theta_M (allowed by P_stag) ; i G5 J_a: {., Geps} = 0 -> excluded by P_stag (allowed by Theta_M): %.1e %.1e'
      % (max(np.abs(g @ Geps - Geps @ g).max() for g in gapB[:3]), max(np.abs(g @ Geps + Geps @ g).max() for g in gapB[3:])))
print('   Geps symmetric (=> m eps xi xi = const for a Majorana field): |Geps - Geps^T| = %.1e ; [Geps J, Geps] = %.1e (so Theta_M forbids every Majorana mass)'
      % (np.abs(Geps - Geps.T).max(), max(np.abs(Geps @ J @ Geps - Geps @ Geps @ J).max() for J in (J12, J23, J13))))
# Wilson-type (same-sublattice, even, real symmetric) operators vanish as Majorana quadratic forms
Wil = sum(np.eye(L**3) - 0.5*(np.roll(np.eye(L**3).reshape(L, L, L, L**3), 1, axis=ax).reshape(L**3, L**3)
          + np.roll(np.eye(L**3).reshape(L, L, L, L**3), -1, axis=ax).reshape(L**3, L**3)) for ax in range(3))
print('   Wilson M_W = sum_mu [1 - (T_mu + T_mu^dag)/2]: real symmetric, |M_W - M_W^T| = %.1e -> its Majorana form (i/2) xi^T (i M_W) xi is a constant'
      % np.abs(Wil - Wil.T).max())

# ---------------- 2. Fock-space identity (Jordan-Wigner, 3 complex modes = 6 Majoranas)
def jw(n):
    sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex); I2 = np.eye(2)
    cs = []
    for k in range(n):
        ops = [sz]*k + [0.5*(sx + 1j*sy)] + [I2]*(n - k - 1)
        o = ops[0]
        for q in ops[1:]:
            o = np.kron(o, q)
        cs.append(o)
    return cs
cs = jw(3)
xi1 = [(c + c.conj().T)/np.sqrt(2) for c in cs]; xi2 = [(c - c.conj().T)/(1j*np.sqrt(2)) for c in cs]
rng = np.random.default_rng(11)
Bm = rng.normal(size=(3, 3)); Bm = Bm - Bm.T
hR = 1j*Bm                                                            # purely imaginary hermitian (real-rep / U = 1 case)
Hc = sum(cs[a].conj().T @ cs[b]*hR[a, b] for a in range(3) for b in range(3))
HM = sum(0.5j*Bm[a, b]*(xi1[a] @ xi1[b] + xi2[a] @ xi2[b]) for a in range(3) for b in range(3))
d = Hc - HM; d = d - np.trace(d)/d.shape[0]*np.eye(d.shape[0])
print('2. Fock identity, h = iB (B real antisym): |sum chi^dag h chi - (i/2)(xi1 B xi1 + xi2 B xi2)| (mod const) = %.1e' % np.abs(d).max())
cross = sum(xi1[a] @ xi2[b] for a in range(3) for b in range(3))
Q1 = sum(xi1[a] @ xi1[b]*0 for a in range(3) for b in range(3))
hC = hR + 0.3*(lambda M: M + M.T)(rng.normal(size=(3, 3)))          # complex hermitian (charged, e.g. U(1) links): real symmetric part
HcC = sum(cs[a].conj().T @ cs[b]*hC[a, b] for a in range(3) for b in range(3))
dC = HcC - sum(0.5j*Bm[a, b]*(xi1[a] @ xi1[b] + xi2[a] @ xi2[b]) for a in range(3) for b in range(3)); dC = dC - np.trace(dC)/dC.shape[0]*np.eye(dC.shape[0])
# copy-1 parity-like check: does H commute with the copy-1 algebra's "number" P1 = prod (i sqrt2 ... )? use [H, xi1-bilinear sum]
G1op = sum(1j*xi1[a] @ xi1[b]*Bm[a, b] for a in range(3) for b in range(3))
print('   control, complex h (real symmetric part 0.3): residual %.2e ; [H, copy-1 Hamiltonian] = %.2e (real case %.1e)'
      % (np.abs(dC).max(), np.abs(HcC @ G1op - G1op @ HcC).max(), np.abs(Hc @ G1op - G1op @ Hc).max()))


# ---------------- 3. position space with links
def phi_flow(k, t, sgn, n=8):
    if t == 0 or sgn == 0:
        return np.array(k, float)
    def rk4(f, y):
        h = 1.0/n
        for _ in range(n):
            k1 = f(y); k2 = f(y + 0.5*h*k1); k3 = f(y + 0.5*h*k2); k4 = f(y + h*k3)
            y = y + h/6*(k1 + 2*k2 + 2*k3 + k4)
        return y
    return rk4(lambda y: 0.5*sgn*t*s(y)*ds(y), np.array(k, float))


def h_links(L, t, Ol, n):
    """dense staggered h with n x n link matrices Ol[j][x] on bond x -> x + e_j (straight axial Wilson lines, as nf1_poslib)."""
    k1 = 2*np.pi*np.arange(L)/L
    ker = [np.fft.ifft(s(phi_flow(k1, t, sg))) for sg in (+1, -1, 0)]
    V, X = lattice(L)
    eta = [np.ones(V), (-1.0)**X[:, 0], (-1.0)**(X[:, 0] + X[:, 1])]
    idx = lambda Y: np.ravel_multi_index((Y % L).T, (L, L, L))
    H = np.zeros((V, n, V, n), complex)
    for j in range(3):
        for r in range(1, L):
            amp = ker[j][r]
            if abs(amp) < 1e-14:
                continue
            W = np.broadcast_to(np.eye(n), (V, n, n)).copy()
            Z_ = X.copy()
            if r < L - r:
                for st in range(r):
                    W = W @ Ol[j][idx(Z_)]
                    Z_[:, j] += 1
            else:
                for st in range(L - r):
                    Z_[:, j] -= 1
                    W = W @ Ol[j][idx(Z_)].conj().swapaxes(-1, -2)
            Y = X.copy(); Y[:, j] += r
            iy = idx(Y)
            H[np.arange(V), :, iy, :] += (eta[j]*amp)[:, None, None]*W
    return H.reshape(V*n, V*n), X


def rand_SO3(rng, m):
    Qs = []
    for _ in range(m):
        q, r = np.linalg.qr(rng.normal(size=(3, 3)))
        q = q @ np.diag(np.sign(np.diag(r)))
        if np.linalg.det(q) < 0:
            q[:, 0] *= -1
        Qs.append(q)
    return np.array(Qs)


def rand_SU2(rng, m):
    a = rng.normal(size=(m, 4)); a /= np.linalg.norm(a, axis=1)[:, None]
    return np.array([[[x[0] + 1j*x[3], x[2] + 1j*x[1]], [-x[2] + 1j*x[1], x[0] - 1j*x[3]]] for x in a])


L = 8; V, X = lattice(L)
for t in (0.0, 0.3):
    H, _ = ham(L, t)
    print('3. L=%d t=%.1f, U = 1: max|Re h| = %.1e ; B = -i h antisymmetric: %.1e' % (L, t, np.abs(H.real).max(), np.abs(H.imag + H.imag.T).max()))
rng = np.random.default_rng(3)
OlR = [rand_SO3(rng, V) for _ in range(3)]
eps = (-1.0)**X.sum(1)
for t in (0.0, 0.3):
    HO, _ = h_links(L, t, OlR, 3)
    B = HO.imag
    epsn = np.repeat(eps, 3)
    print('   SO(3) links, t=%.1f: herm %.1e ; max|Re h[O]| %.1e (h = iB, B real) ; B antisym %.1e ; Theta_M |eps B eps + B| %.1e'
          % (t, np.abs(HO - HO.conj().T).max(), np.abs(HO.real).max(), np.abs(B + B.T).max(), np.abs(epsn[:, None]*B*epsn[None, :] + B).max()))
    # P_stag with link lift O^P_j(x) = O_j(-x-e_j)^T
    idx = lambda Y: np.ravel_multi_index((Y % L).T, (L, L, L))
    OlP = []
    for j in range(3):
        Zm = -X.copy(); Zm[:, j] -= 1
        OlP.append(OlR[j][idx(Zm)].swapaxes(-1, -2))
    HP, _ = h_links(L, t, OlP, 3)
    Pm = np.zeros((V, V)); Pm[np.arange(V), idx(-X)] = eps
    Pn = np.kron(Pm, np.eye(3))
    print('                       P_stag |P h[O] P^T - h[O^P]| = %.1e' % np.abs(Pn @ HO @ Pn.T - HP).max())
    del HO, HP, B
OlS = [rand_SU2(rng, V) for _ in range(3)]
HU, _ = h_links(L, 0.3, OlS, 2)
s2 = np.array([[0, 1], [-1, 0]], complex)                              # i sigma_2
C2 = np.kron(np.eye(V), s2)
print('   SU(2) links, t=0.3: herm %.1e ; max|Re h[U]| %.2e (not purely imaginary) ; |(i s2) h* (i s2)^dag + h| = %.1e ; ((i s2)K)^2 = %+.0f'
      % (np.abs(HU - HU.conj().T).max(), np.abs(HU.real).max(), np.abs(C2 @ HU.conj() @ C2.conj().T + HU).max(), (s2 @ s2.conj())[0, 0].real))
del HU, C2


def realify(g):
    return np.block([[g.real, -g.imag], [g.imag, g.real]])


def commutant_report(name, gens, n):
    Cc = commutant_real(gens, n)
    sym = [c + c.T for c in Cc]
    Ssp = np.array([x.ravel() for x in sym if np.linalg.norm(x) > 1e-9])
    rk = np.linalg.matrix_rank(Ssp, tol=1e-9) if len(Ssp) else 0
    # look for a nontrivial symmetric idempotent: diagonalise a random symmetric element of the commutant
    R = sum(rng.normal()*c for c in Cc); R = R + R.T
    ev = np.linalg.eigvalsh(R)
    nd = len(np.unique(np.round(ev, 8)))
    print('   %-34s real commutant dim %d ; symmetric part dim %d ; distinct eigenvalues of a random symmetric commutant element: %d %s'
          % (name, len(Cc), rk, nd, '(only multiples of 1: no gauge-covariant halving)' if nd == 1 else '(projector exists: halving)'))
gs = rand_SU2(rng, 4)
commutant_report('SU(2) doublet, realified R^4:', [realify(g) for g in gs], 4)
commutant_report('SO(3) triplet, realified R^6:', [realify(g.astype(complex)) for g in rand_SO3(rng, 4)], 6)
commutant_report('U(1) charge 1, realified R^2:', [realify(np.array([[np.exp(1j*a)]])) for a in rng.uniform(0, 6, 3)], 2)
commutant_report('SU(3) triplet, realified R^6:', [realify(np.linalg.qr(rng.normal(size=(3, 3)) + 1j*rng.normal(size=(3, 3)))[0]
                                                   / np.linalg.det(np.linalg.qr(rng.normal(size=(3, 3)))[0])**0) for _ in range(4)], 6)
commutant_report('SU(2) doublet x flavour 2, R^8:', [np.kron(realify(g), np.eye(2)) if False else realify(np.kron(g, np.eye(2))) for g in gs], 8)

# ---------------- 4. locality of the J-type mass
L = 8
S12 = Ssh[0] @ Ssh[1]
R12 = 0.5*(S12 - S12.T)
print('4. R_12 = (S1 S2 - (S1 S2)^T)/2: real antisym %.1e ; commutes with eps %.1e ; anticommutes with h? |{R12,h}| %.1e, |[R12,h]| %.1e'
      % (np.abs(R12 + R12.T).max(), np.abs(epsop @ R12 - R12 @ epsop).max(), np.abs(R12 @ H0 + H0 @ R12).max(), np.abs(R12 @ H0 - H0 @ R12).max()))
for K in ((0, 0, 0), (2*np.pi/8, 0, 0), (2*np.pi/8, 2*np.pi/8, 0), (2*np.pi/8, -2*np.pi/8, 2*np.pi/8), (4*np.pi/8, 2*np.pi/8, 0)):
    MK = rz_matrix(R12, L, np.array(K))
    best = None
    for nm, f in (('cos(K1+K2)', np.cos(K[0] + K[1])), ('-i sin(K1+K2)', -1j*np.sin(K[0] + K[1])), ('i sin(K1+K2)', 1j*np.sin(K[0] + K[1])),
                  ('cos K1 cos K2', np.cos(K[0])*np.cos(K[1]))):
        r_ = np.abs(MK - f*J12).max()
        if best is None or r_ < best[1]:
            best = (nm, r_)
    print('   K = %s : |R12(K) - f(K) J12| best f = %s, resid %.1e ; |R12(K)| %.3f' % (np.round(np.array(K)/np.pi, 3), best[0], best[1], np.abs(MK).max()))
Mop = 1j*epsop @ R12
print('   M = i eps R12: hermitian %.1e ; antisymmetric %.1e ; {M, h} = %.1e (gap-opening) ; M at K=0 vs i Geps J12: %.1e'
      % (np.abs(Mop - Mop.conj().T).max(), np.abs(Mop + Mop.T).max(), np.abs(Mop @ H0 + H0 @ Mop).max(),
         np.abs(rz_matrix(Mop, L, np.zeros(3)) - 1j*Geps @ J12).max()))
for k in range(3):
    Sk = Ssh[k]
    par = np.abs(Sk @ Mop @ Sk.T - Mop).max() < 1e-12
    par2 = np.abs(Sk @ Mop @ Sk.T + Mop).max() < 1e-12
    print('   S_%d M S_%d^T = %s M' % (k + 1, k + 1, '+' if par else ('-' if par2 else '?')))
print('   Theta_M (xi -> eps xi, K): M -> eps M* eps = %s M' % ('+' if np.abs(epsop @ Mop.conj() @ epsop - Mop).max() < 1e-12 else '-'))

# ---------------- 5. cubic rotations
def rotation_signs(L, H, R):
    """find D (+-1 per site) with D P_R H P_R^T D = H, (P_R chi)(x) = chi(R^-1 x); BFS on the hop graph."""
    V, X = lattice(L)
    Rinv = np.round(np.linalg.inv(R)).astype(int)
    src = np.ravel_multi_index(((X @ Rinv.T) % L).T, (L, L, L))
    P = np.zeros((V, V)); P[np.arange(V), src] = 1
    Hp = P @ H @ P.T
    D = np.zeros(V); D[0] = 1; queue = [0]
    nz = np.abs(H) > 1e-10
    while queue:
        x = queue.pop()
        for y in np.nonzero(nz[x])[0]:
            ratio = H[x, y]/Hp[x, y] if abs(Hp[x, y]) > 1e-12 else np.nan
            if not np.isfinite(ratio) or abs(abs(ratio) - 1) > 1e-9:
                return None, None
            val = np.real(ratio)/D[x]
            if D[y] == 0:
                D[y] = val; queue.append(y)
    O = np.diag(D) @ P
    return O, np.abs(O @ H @ O.T - H).max()

Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]]); Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]]); Ry = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
L = 8; H8, _ = ham(L, 0.0)
rhos = {}
for nm, R in (('Rz', Rz), ('Rx', Rx), ('Ry', Ry)):
    O, res = rotation_signs(L, H8.imag, R)
    if O is None:
        print('5. %s: no pure-sign rotation found' % nm); continue
    rho = rz_matrix(O, L, np.zeros(3)).real
    rhos[nm] = rho
    Jt = []
    for J in (J23, J13, J12):
        Jr = rho @ J @ rho.T
        Jt.append([np.sum(Jr*Jb_)/8 for Jb_ in (J23, J13, J12)])
    print('5. %s: |O h O^T - h| = %.1e (L = 8, root symbol) ; rho Geps rho^T = Geps: %.1e ; rho Gamma_j rho^T -> %s' %
          (nm, res, np.abs(rho @ Geps @ rho.T - Geps).max(),
           [[int(np.round(np.sum((rho @ Gam[a] @ rho.T)*Gam[b])/8)) for b in range(3)] for a in range(3)]))
    print('   action on (J23, J13, J12):\n%s' % np.round(np.array(Jt), 6))
if len(rhos) == 3:
    # invariant combos c . J under all three generators
    Ms = []
    for rho in rhos.values():
        T = np.array([[np.sum((rho @ J @ rho.T)*Jb_)/8 for J in (J23, J13, J12)] for Jb_ in (J23, J13, J12)])
        Ms.append(T - np.eye(3))
    ns = nullspace(np.vstack(Ms))
    print('   cubic-invariant combinations of the J-triplet (=> of the Majorana masses i Geps J and i G5 J): dim %d' % ns.shape[1])
    # full 28-dim Majorana-legal space at K = 0: cubic-invariant subspace and its classification
    rows = [np.array([(rho @ Ab @ rho.T - Ab).ravel() for Ab in basisA]).T for rho in rhos.values()]
    ns28 = nullspace(np.vstack(rows))
    print('   cubic-invariant Majorana-legal constant bilinears (of 28): dim %d' % ns28.shape[1])
    for c in ns28.T:
        Mi = 1j*np.einsum('a,aij->ij', c, basisA)
        gapo = max(np.abs(Mi @ g + g @ Mi).max() for g in Gam) < 1e-10
        comm = max(np.abs(Mi @ g - g @ Mi).max() for g in Gam) < 1e-10
        print('     invariant: anticommutes with all G_j (gap-opening) %s ; commutes with all G_j %s ; Theta_M-allowed %s ; P_stag-allowed %s ; = i G1G2G3 ? %.1e'
              % (gapo, comm, np.abs(Mi @ Geps + Geps @ Mi).max() < 1e-10, np.abs(Mi @ Geps - Geps @ Mi).max() < 1e-10,
                 min(np.abs(Mi/np.abs(Mi).max() - sgn*1j*Gam[0] @ Gam[1] @ Gam[2]).max() for sgn in (1, -1))))
print('done')
