"""A23 tiny check: what cubic covariance + linearized gauge invariance force on a
symmetric-tensor (spin-2-like) lattice field.  Supplied toy algebra only.

C1  cubic-invariant kinetic forms on Sym^2(R^3)            (expect 3: A1, E, T2)
C2  cubic-invariant O(k^2) potentials; then spatial gauge invariance h->h+k xi+xi k
    (expect: many invariants, exactly 1 gauge-invariant = linearized EH potential)
C3  preservation of the linearized Hamiltonian constraint R(h)=k^2 tr h - k.h.k
    by the kinetic shear on transverse momenta -> conditions on (mA1, mE, mT2)
C4  reduced mode analysis (h mod gauge, pi transverse) for GR / anisotropic /
    lambda-shifted kinetic weights
C5  4D hypercubic B4 (Euclidean Z^3 x Z_tau regulator): invariant O(k^2) forms,
    4D gauge invariance -> unique?  and its k_tau^2 spatial block (kinetic metric)
C6  lattice leapfrog ("Yee for spin-2") symbol: s_j = 2 sin(k_j/2); constraint
    preservation per shear, CFL threshold, eigenphase formula, no pi phase
C7  static source in linearized ADM with the lapse multiplying the field's own
    potential: PPN gamma
C8  arithmetic: band tops below pi
"""
import itertools, sys, time
import numpy as np

t0 = time.time()
rng = np.random.default_rng(20261003)
np.set_printoptions(precision=6, suppress=True, linewidth=120)


def signed_perms(n, proper=False):
    out = []
    for p in itertools.permutations(range(n)):
        for sg in itertools.product((1.0, -1.0), repeat=n):
            M = np.zeros((n, n))
            for i in range(n):
                M[i, p[i]] = sg[i]
            if proper and np.linalg.det(M) < 0:
                continue
            out.append(M)
    return out


def sym_basis(n):
    B, pairs = [], []
    for i in range(n):
        for j in range(i, n):
            E = np.zeros((n, n))
            if i == j:
                E[i, i] = 1.0
            else:
                E[i, j] = E[j, i] = 1 / np.sqrt(2)
            B.append(E)
            pairs.append((i, j))
    return B, pairs


def coords(h, B):
    return np.array([np.sum(E * h) for E in B])


def rep(R, B):
    m = len(B)
    D = np.zeros((m, m))
    for J, EJ in enumerate(B):
        D[:, J] = coords(R @ EJ @ R.T, B)
    return D


def null_space(A, tol=1e-9):
    u, s, vt = np.linalg.svd(A)
    rank = int(np.sum(s > tol * max(1.0, s[0] if s.size else 1.0)))
    return vt[rank:].T, s


def invariant_quartic_space(n, group, B):
    """Orthonormal basis of C[I,J,a,b] (sym in IJ and ab) invariant under group."""
    m = len(B)
    dim = m * m * n * n
    P = np.zeros((dim, dim))
    for R in group:
        D = rep(R, B)
        P += np.kron(np.kron(D, D), np.kron(R, R))
    P /= len(group)
    # symmetrizer S = 1/4 (1 + swap_IJ + swap_ab + both), applied by index permutation
    idx = np.arange(dim).reshape(m, m, n, n)
    p1 = idx.transpose(1, 0, 2, 3).ravel()
    p2 = idx.transpose(0, 1, 3, 2).ravel()
    p12 = idx.transpose(1, 0, 3, 2).ravel()
    PS = 0.25 * (P + P[:, p1] + P[:, p2] + P[:, p12])      # P @ S
    SP = 0.25 * (P + P[p1, :] + P[p2, :] + P[p12, :])      # S @ P
    comm = np.abs(PS - SP).max()
    del SP
    PS = 0.5 * (PS + PS.T)
    w, v = np.linalg.eigh(PS)
    basis = v[:, w > 0.5]
    return basis, comm


def Ck(Cvec, k, m, n):
    C = Cvec.reshape(m, m, n, n)
    return np.einsum('IJab,a,b->IJ', C, k, k)


def gauge_vectors(k, B):
    n = len(k)
    return np.array([coords(np.outer(k, e) + np.outer(e, k), B) for e in np.eye(n)]).T  # m x n


def V_EH_matrix(k, B):
    """Hessian matrix Vm with V(h)=1/2 h^T Vm h, V = 1/4 k^2 h:h - 1/2|hk|^2 + 1/2 (khk) trh - 1/4 k^2 (trh)^2."""
    def V(h):
        return (0.25 * k @ k * np.sum(h * h) - 0.5 * np.sum((h @ k) ** 2)
                + 0.5 * (k @ h @ k) * np.trace(h) - 0.25 * (k @ k) * np.trace(h) ** 2)
    m = len(B)
    Vm = np.zeros((m, m))
    for I in range(m):
        Vm[I, I] = 2 * V(B[I])
        for J in range(I + 1, m):
            Vm[I, J] = Vm[J, I] = V(B[I] + B[J]) - V(B[I]) - V(B[J])
    return Vm


def irrep_projectors(B, n=3):
    m = len(B)
    a1 = coords(np.eye(n), B); a1 /= np.linalg.norm(a1)
    PA1 = np.outer(a1, a1)
    off = np.array([1.0 if not np.allclose(np.diag(np.diag(E)), E) else 0.0 for E in B])
    PT2 = np.diag(off)
    PE = np.eye(m) - PA1 - PT2
    return PA1, PE, PT2


def transverse_basis(k, B):
    L = np.array([E @ k for E in B]).T  # n x m : pi -> pi k
    T, _ = null_space(L)
    return T


def r_vec(k, B):
    return np.array([(k @ k) * np.trace(E) - k @ E @ k for E in B])


out = []
def say(*a):
    s = ' '.join(str(x) for x in a)
    print(s); out.append(s); sys.stdout.flush()

# ---------------------------------------------------------------- C1
B3, pairs3 = sym_basis(3)
Oh = signed_perms(3)
O = signed_perms(3, proper=True)
for name, G in (('O_h(48)', Oh), ('O(24)', O)):
    Pq = np.zeros((36, 36))
    for R in G:
        D = rep(R, B3)
        Pq += np.kron(D, D)
    Pq /= len(G)
    idx = np.arange(36).reshape(6, 6)
    Sw = np.zeros((36, 36)); Sw[np.arange(36), np.arange(36)] += .5; Sw[np.arange(36), idx.T.ravel()] += .5
    w = np.linalg.eigvalsh(0.5 * (Pq @ Sw + (Pq @ Sw).T))
    say(f'C1 {name}: invariant quadratic (kinetic) forms on Sym^2(R^3): {int(np.sum(w > 0.5))}')

# ---------------------------------------------------------------- C2
for name, G in (('O_h', Oh), ('O', O)):
    basis, comm = invariant_quartic_space(3, G, B3)
    d_inv = basis.shape[1]
    rows = []
    for _ in range(40):
        k = rng.normal(size=3); g = gauge_vectors(k, B3)
        for c in range(3):
            rows.append(np.array([Ck(basis[:, a], k, 6, 3) @ g[:, c] for a in range(d_inv)]).T)
    A = np.vstack(rows)
    N, s = null_space(A)
    say(f'C2 {name}: invariant O(k^2) quadratic forms = {d_inv}; gauge-invariant = {N.shape[1]}  (P,S commute: {comm:.1e})')
    if N.shape[1] == 1:
        Cvec = basis @ N[:, 0]
        errs = []
        for _ in range(20):
            k = rng.normal(size=3)
            C = Ck(Cvec, k, 6, 3); Vm = V_EH_matrix(k, B3)
            lam = np.sum(C * Vm) / np.sum(Vm * Vm)
            errs.append(np.linalg.norm(C - lam * Vm) / np.linalg.norm(Vm))
        say(f'   unique form vs linearized EH potential: max rel. deviation {max(errs):.2e}')

# EH gauge invariance and TT / conformal signs
k = np.array([0.3, -0.7, 0.5]); Vm = V_EH_matrix(k, B3)
say(f'   EH gauge check |V g| max: {np.abs(Vm @ gauge_vectors(k, B3)).max():.1e}')
kh = k / np.linalg.norm(k)
eT = coords(np.eye(3) - np.outer(kh, kh), B3); eT /= np.linalg.norm(eT)
# a TT element
u = np.cross(kh, [1, 0, 0]); u /= np.linalg.norm(u); w_ = np.cross(kh, u)
eTT = coords(np.outer(u, u) - np.outer(w_, w_), B3); eTT /= np.linalg.norm(eTT)
say(f'   potential on TT direction / k^2: {eTT @ Vm @ eTT / (k @ k):+.6f};  on transverse-trace direction / k^2: {eT @ Vm @ eT / (k @ k):+.6f}')

# ---------------------------------------------------------------- C3
PA1, PE, PT2 = irrep_projectors(B3)
rows = []
for _ in range(30):
    k = rng.normal(size=3)
    T = transverse_basis(k, B3); r = r_vec(k, B3)
    rows.append(np.array([r @ P @ T for P in (PA1, PE, PT2)]).T)  # 3 x 3
A = np.vstack(rows)
N, s = null_space(A)
say(f'C3 Hamiltonian-constraint preservation: solution space dim {N.shape[1]}; (mA1, mE, mT2) ∝ {N[:, 0] / N[1, 0] if N.shape[1] == 1 else N}')

# ---------------------------------------------------------------- C4
def reduced_modes(M, k, V=None):
    V = V_EH_matrix(k, B3) if V is None else V
    G = gauge_vectors(k, B3); Gq, _ = np.linalg.qr(G)
    Q = np.eye(6) - Gq @ Gq.T
    w, v = np.linalg.eigh(Q); Hb = v[:, w > 0.5]
    T = transverse_basis(k, B3)
    Ared = np.block([[np.zeros((3, 3)), Hb.T @ M @ T], [-T.T @ V @ Hb, np.zeros((3, 3))]])
    ev = np.linalg.eigvals(Ared)
    return ev

cases = {
    'GR  (mA1,mE,mT2)=(-1/2,1,1)': (-0.5, 1.0, 1.0),
    'aniso mT2=1.1              ': (-0.5, 1.0, 1.1),
    'lambda shift mA1=-0.40     ': (-0.40, 1.0, 1.0),
    'lambda shift mA1=-0.60     ': (-0.60, 1.0, 1.0),
}
dirs = {'axis': [0, 0, 1], 'face': [1, 1, 0], 'body': [1, 1, 1], 'rand': [0.37, -0.81, 0.22]}
for cname, (a1, e, t2) in cases.items():
    M = 2 * (a1 * PA1 + e * PE + t2 * PT2)   # factor 2: TT speed 1 for GR normalization
    line = []
    for dname, dv in dirs.items():
        k = 0.1 * np.array(dv, float) / np.linalg.norm(dv)
        ev = reduced_modes(M, k)
        lam2 = np.sort_complex(np.round(ev ** 2 / (k @ k), 6))
        line.append(f'{dname}: lambda^2/k^2 = {np.unique(lam2)}')
    say(f'C4 {cname} | ' + ' | '.join(line))
say('   (lambda^2 = -omega^2: negative -> oscillation at speed sqrt(-lambda^2); positive -> exponential growth)')

# scalar-sector energy sign for mA1=-0.6 (ghost test): kinetic weight on transverse-trace momentum
for a1 in (-0.4, -0.5, -0.6):
    M = 2 * (a1 * PA1 + PE + PT2)
    k = np.array([0.0, 0.0, 0.1]); kh = k / np.linalg.norm(k)
    eT = coords(np.eye(3) - np.outer(kh, kh), B3); eT /= np.linalg.norm(eT)
    G = gauge_vectors(k, B3); Gq, _ = np.linalg.qr(G); Q = np.eye(6) - Gq @ Gq.T
    say(f'   mA1={a1:+.2f}: physical kinetic weight on transverse-trace momentum e_T.Q M e_T = {eT @ Q @ M @ eT:+.4f}; potential weight e_T.V e_T/k^2 = {eT @ V_EH_matrix(k, B3) @ eT / (k @ k):+.4f}')

# ---------------------------------------------------------------- C5
t5 = time.time()
B4b, pairs4 = sym_basis(4)
W4 = signed_perms(4)
basis4, comm4 = invariant_quartic_space(4, W4, B4b)
d4 = basis4.shape[1]
rows = []
for _ in range(40):
    k = rng.normal(size=4); g = gauge_vectors(k, B4b)
    for c in range(4):
        rows.append(np.array([Ck(basis4[:, a], k, 10, 4) @ g[:, c] for a in range(d4)]).T)
A = np.vstack(rows)
N4, s4 = null_space(A)
say(f'C5 B4(384) hypercubic: invariant O(k^2) forms on Sym^2(R^4) = {d4}; 4D gauge-invariant = {N4.shape[1]}  ({time.time() - t5:.1f}s)')
if N4.shape[1] == 1:
    C4vec = basis4 @ N4[:, 0]
    # k_tau^2 block on spatial components (index 0 = tau)
    ktau = np.array([1.0, 0, 0, 0])
    Cfull = Ck(C4vec, ktau, 10, 4)
    sp = [I for I, (i, j) in enumerate(pairs4) if i > 0 and j > 0]
    Kblk = Cfull[np.ix_(sp, sp)]
    # express in the 3D orthonormal basis ordering (pairs (i,j) with i,j in 1..3)
    PA1s, PEs, PT2s = irrep_projectors(B3)
    cA1 = np.trace(PA1s @ Kblk) / 1; cE = np.trace(PEs @ Kblk) / 2; cT2 = np.trace(PT2s @ Kblk) / 3
    resid = np.linalg.norm(Kblk - (cA1 * PA1s + cE * PEs + cT2 * PT2s))
    say(f'   k_tau^2 block on spatial h: coefficients (A1, E, T2) = ({cA1:+.5f}, {cE:+.5f}, {cT2:+.5f}); ratios A1/E = {cA1 / cE:+.5f}, T2/E = {cT2 / cE:+.5f}; residual {resid:.1e}')
    say('   (GR Lagrangian kinetic metric h:h - (tr h)^2 has A1/E = -2, T2/E = 1; its inverse is the Hamiltonian weight (-1/2, 1, 1) of C3)')
    # spatial-momentum block vs 3D EH potential
    ksp = np.array([0, 0.3, -0.7, 0.5])
    Csp = Ck(C4vec, ksp, 10, 4)[np.ix_(sp, sp)]
    Vm3 = V_EH_matrix(ksp[1:], B3)
    lam = np.sum(Csp * Vm3) / np.sum(Vm3 * Vm3)
    say(f'   spatial-momentum block vs 3D EH potential: rel. deviation {np.linalg.norm(Csp - lam * Vm3) / np.linalg.norm(Vm3):.2e}; Euclidean ratio kin/pot sign: {np.sign(cE) * np.sign(lam):+.0f}')

# ---------------------------------------------------------------- C6
def leapfrog(kvec, tau, M):
    s = 2 * np.sin(kvec / 2)
    V = V_EH_matrix(s, B3)
    I6, Z6 = np.eye(6), np.zeros((6, 6))
    K = lambda a: np.block([[I6, a * M], [Z6, I6]])
    P = lambda b: np.block([[I6, Z6], [-b * V, I6]])
    U = K(tau / 2) @ P(tau) @ K(tau / 2)
    L = np.array([E @ s for E in B3]).T              # momentum constraint pi -> pi s
    cm = np.hstack([np.zeros((3, 6)), L])
    cH = np.hstack([r_vec(s, B3), np.zeros(6)])[None, :]
    return U, cm, cH, s, (K(tau / 2), P(tau))

Mgr = 2 * (-0.5 * PA1 + PE + PT2)
worst_m = worst_H = 0.0
for _ in range(200):
    kv = rng.uniform(-np.pi, np.pi, 3)
    U, cm, cH, s, (Kh, Pf) = leapfrog(kv, 0.5, Mgr)
    for S_ in (Kh, Pf):
        worst_m = max(worst_m, np.abs(cm @ S_ - cm).max())
        Ncm, _ = null_space(cm)
        worst_H = max(worst_H, np.abs((cH @ S_ - cH) @ Ncm).max())
say(f'C6 per-shear constraint preservation over 200 random k: momentum rows max {worst_m:.1e}; Hamiltonian row on momentum-constraint surface max {worst_H:.1e}')
# anisotropic kinetic breaks Hamiltonian-row preservation
Man = 2 * (-0.5 * PA1 + PE + 1.1 * PT2)
wH = 0.0
for _ in range(50):
    kv = rng.uniform(-np.pi, np.pi, 3)
    U, cm, cH, s, (Kh, Pf) = leapfrog(kv, 0.5, Man)
    Ncm, _ = null_space(cm)
    wH = max(wH, np.abs((cH @ Kh - cH) @ Ncm).max())
say(f'   with mT2=1.1 the Hamiltonian row changes by up to {wH:.2e} per kinetic shear (not preserved)')

def tt_basis(s):
    """orthonormal basis (6x2) of symmetric traceless tensors transverse to s"""
    sh = s / np.linalg.norm(s)
    a = np.array([1.0, 0, 0]) if abs(sh[0]) < 0.9 else np.array([0, 1.0, 0])
    u = np.cross(sh, a); u /= np.linalg.norm(u); w = np.cross(sh, u)
    e1 = coords(np.outer(u, u) - np.outer(w, w), B3); e2 = coords(np.outer(u, w) + np.outer(w, u), B3)
    return np.array([e1 / np.linalg.norm(e1), e2 / np.linalg.norm(e2)]).T

def tt_block(kv, tau, M):
    U, cm, cH, s, _ = leapfrog(kv, tau, M)
    Tt = tt_basis(s)
    Pp = np.zeros((12, 4)); Pp[:6, :2] = Tt; Pp[6:, 2:] = Tt
    leak = np.linalg.norm(U @ Pp - Pp @ (Pp.T @ U @ Pp))
    ev = np.linalg.eigvals(Pp.T @ U @ Pp)
    # power traces: spectrum should be {1 x8} + TT eigenvalues
    Uj = np.eye(12); tr_err = 0.0
    for j in range(1, 13):
        Uj = Uj @ U
        tr_err = max(tr_err, abs(np.trace(Uj) - (8 + np.sum(ev ** j).real)) / max(1.0, np.abs(ev).max() ** j))
    return ev, s, leak, tr_err

grid = np.linspace(-np.pi, np.pi, 13)
for tau in (0.99 / np.sqrt(3), 1.01 / np.sqrt(3)):
    maxmod, maxph, formula_err, maxleak, maxtr = 0.0, 0.0, 0.0, 0.0, 0.0
    for kx in grid:
        for ky in grid:
            for kz in grid:
                kv = np.array([kx, ky, kz])
                if np.allclose(kv, 0):
                    continue
                ev, s, leak, trerr = tt_block(kv, tau, Mgr)
                maxleak = max(maxleak, leak); maxtr = max(maxtr, trerr)
                maxmod = max(maxmod, np.abs(ev).max())
                if np.all(np.abs(np.abs(ev) - 1) < 1e-9):
                    th = np.abs(np.angle(ev)).max(); maxph = max(maxph, th)
                    formula_err = max(formula_err, abs(np.cos(th) - (1 - tau ** 2 * (s @ s) / 2)))
    say(f'   tau={tau:.5f} (tau*sqrt3={tau * np.sqrt(3):.2f}): TT block invariance leak max {maxleak:.1e}; power-trace check (spectrum = 1 x8 + TT) max dev {maxtr:.1e}; max |eig| {maxmod:.6f}; max TT phase/pi {maxph / np.pi:.4f}; |cos(theta)-(1-tau^2 s^2/2)| max {formula_err:.1e}')
kv = np.array([0.02, 0.01, -0.015]); tau = 0.4
ev, s, leak, trerr = tt_block(kv, tau, Mgr)
say(f'   small k: theta/(tau|k|) = {np.abs(np.angle(ev)).max() / (tau * np.linalg.norm(kv)):.6f} (z=1, speed 1); TT eigenvalues {np.round(ev, 8)}')
corner = np.array([np.pi] * 3)
ev, s, leak, trerr = tt_block(corner, 0.99 / np.sqrt(3), Mgr)
say(f'   zone corner (pi,pi,pi), tau*sqrt3=0.99: TT phases/pi {np.round(np.abs(np.angle(ev)) / np.pi, 6)} (approach 1 only as tau -> 1/sqrt3)')

# ---------------------------------------------------------------- C7
for kv in (np.array([0, 0, 0.2]), np.array([0.13, -0.21, 0.07])):
    Vm = V_EH_matrix(kv, B3); r = r_vec(kv, B3); rho = 1.0
    # unknowns x = (h[6], n): Vm h - n r = 0 ; r.h = rho
    A = np.zeros((7, 7)); b = np.zeros(7)
    A[:6, :6] = Vm; A[:6, 6] = -r; A[6, :6] = r; b[6] = rho
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    h, n = x[:6], x[6]
    kh = kv / np.linalg.norm(kv)
    PT = np.eye(3) - np.outer(kh, kh)
    hm = sum(h[I] * B3[I] for I in range(6))
    psiT = np.sum(hm * PT) / np.sum(PT * PT)
    resid = np.linalg.norm(A @ x - b)
    say(f'C7 static source k={kv}: lapse n={n:+.5f}, U=-n={-n:+.5f} (k^2 U = {-n * (kv @ kv):.4f}), psi_T={psiT:+.5f}, PPN gamma = psi_T/(2U) = {psiT / (2 * -n):.6f}; residual {resid:.1e}')
say('   (without the lapse multiplying the field potential the static equations read Vm h = 0 and r.h = rho: inconsistent for rho != 0)')
Vm = V_EH_matrix(np.array([0, 0, 0.2]), B3); r = r_vec(np.array([0, 0, 0.2]), B3)
A = np.zeros((7, 6)); A[:6] = Vm; A[6] = r
b = np.zeros(7); b[6] = 1.0
x, *_ = np.linalg.lstsq(A, b, rcond=None)
say(f'   unpaced variant least-squares residual: {np.linalg.norm(A @ x - b):.4f} (nonzero = no static solution)')

# ---------------------------------------------------------------- C8
say(f'C8 proposed Regge dispersion 4sinh^2(w/2)=s^2 continued: band top 2*asinh(sqrt3) = {2 * np.arcsinh(np.sqrt(3)):.6f} < pi = {np.pi:.6f}')
for h_ in (0.3, 0.5, 1 / np.sqrt(3) - 1e-9):
    say(f'   Yee/leapfrog band top at step h={h_:.4f}: 2*asin(h*sqrt3) = {2 * np.arcsin(min(1, h_ * np.sqrt(3))):.6f}')
say(f'done in {time.time() - t0:.1f}s')
