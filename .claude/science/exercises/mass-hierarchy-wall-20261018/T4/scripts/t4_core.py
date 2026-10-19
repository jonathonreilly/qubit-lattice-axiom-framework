"""T-F3 shared core: lattice image group B3 on the X-star generation triplet, residual elements from
geometry, irrep projectors on generation bilinears, F3 mass matrices, PMNS observables.
Conventions follow FP/scripts/s1_group.py (rep_rot, rep_tr) and s3/s4 (signed permutations)."""
import itertools, numpy as np

# ---------------- lattice -> image on the X triplet (copied logic of s1_group.py) ----------------
XS = [np.array(v) for v in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
def rot_group():
    G = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), int)
            for i in range(3): M[i, p[i]] = s[i]
            if round(np.linalg.det(M)) == 1: G.append(M)
    return G
O24 = rot_group()
def rep_rot(M):
    P = np.zeros((3, 3), int)
    for i in range(3):
        j = [jj for jj in range(3) if (((M @ XS[i]) % 2) == XS[jj]).all()][0]; P[j, i] = 1
    return P
def rep_tr(t): return np.diag([(-1) ** int(XS[i] @ np.array(t)) for i in range(3)])
def close(gens):
    grp = {tuple(np.eye(3, dtype=int).ravel())}; fr = list(grp)
    while fr:
        new = []
        for a in fr:
            A = np.array(a).reshape(3, 3)
            for g in gens:
                b = tuple((g @ A).ravel())
                if b not in grp: grp.add(b); new.append(b)
        fr = new
    return [np.array(g).reshape(3, 3) for g in sorted(grp)]
B3 = close([rep_rot(M) for M in O24] + [rep_tr(t) for t in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]])

# residual elements from geometry
C3_111 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]])          # e1->e2->e3, about (1,1,1) through the origin (a site)
R110 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, -1]])           # half-turn about [110]
G_L = rep_rot(C3_111)                                          # charged-lepton residual (site-centred C3)
G_NU = rep_tr((0, 0, 1)) @ rep_rot(R110)                       # x -> R x + e3 : axis [110] through (0,0,1/2)
G_NU_SITE = rep_rot(R110)                                      # same half-turn through a site (theta13 = 0 control)
assert np.allclose(R110 @ np.array([0, 0, .5]) + np.array([0, 0, 1]), [0, 0, .5])

# ---------------- bilinear irreps: M -> g M g^T ----------------
def act(g, M): return g @ M @ g.T
def pA1(M): return np.trace(M) / 3 * np.eye(3)
def pE(M): return np.diag(np.diag(M)) - pA1(M)
def pM(M): Q = M - np.diag(np.diag(M)); return (Q + Q.T) / 2
def pMp(M): return (M - M.T) / 2
PROJ = {'A1': pA1, 'E': pE, '3M': pM, "3M'": pMp}
MAJ_IRREPS = ['A1', 'E', '3M']                                 # symmetric part only

# ---------------- data (recalled; comparator) ----------------
ML = np.array([0.51099895e-3, 0.1056584, 1.77686])            # GeV
DM21, DM31 = 7.42e-5, 2.51e-3                                  # eV^2 (NO); IO uses |dm32| ~ 2.43e-3
S13_OBS = 0.0220
W3 = np.exp(2j * np.pi / 3)
FOUR = np.array([[W3 ** (a * b) for b in range(3)] for a in range(3)]) / np.sqrt(3)   # columns f_k, f_0 = (1,1,1)/sqrt3
V1 = np.array([1, 1, 0]) / np.sqrt(2); W1 = np.array([1, -1, 0]) / np.sqrt(2); W2 = np.array([0, 0, 1.])

def Ml0(phases, swap):
    lam = ML * np.exp(1j * np.asarray(phases))
    if swap: lam = lam[[0, 2, 1]]                               # tau on omega, mu on omega-bar
    return FOUR @ np.diag(lam) @ FOUR.conj().T

def nu_masses(m_light, order='NO'):
    if order == 'NO':
        m1 = m_light; return np.array([m1, np.sqrt(m1 ** 2 + DM21), np.sqrt(m1 ** 2 + DM31)])
    m3 = m_light; m2 = np.sqrt(m3 ** 2 + 2.43e-3 + DM21); m1 = np.sqrt(m2 ** 2 - DM21)
    return np.array([m1, m2, m3])

def Unu_tm1(theta, phi):
    c, s = np.cos(theta), np.sin(theta)
    u2 = c * W1 + np.exp(1j * phi) * s * W2
    u3 = -np.exp(-1j * phi) * s * W1 + c * W2
    return np.stack([V1.astype(complex), u2, u3], 1)

def Mnu0(theta, phi, masses, majph):
    U = Unu_tm1(theta, phi) @ np.diag(np.exp(1j * np.asarray(majph) / 2))
    return U.conj() @ np.diag(masses) @ U.conj().T

THETA0 = np.arccos(np.sqrt(3 * S13_OBS))                        # unperturbed |U_e3|^2 = cos^2(theta)/3

# ---------------- observables ----------------
def pmns(Ml, Mn):
    wl, Ul = np.linalg.eigh(Ml.conj().T @ Ml)                   # ascending: e, mu, tau
    wn, Un = np.linalg.eigh(Mn.conj().T @ Mn)                   # ascending: nu1, nu2, nu3 (NO)
    return Ul.conj().T @ Un, np.sqrt(np.abs(wl)), np.sqrt(np.abs(wn))
def obs(U, order='NO'):
    P = np.abs(U) ** 2
    if order == 'IO':                                           # eigh ascending gives (nu3, nu1, nu2)
        P = P[:, [1, 2, 0]]
    s13 = P[0, 2]; c13 = 1 - s13
    s12 = P[0, 1] / c13; s23 = P[1, 2] / c13
    D = abs(s12 - (1 - 2 / (3 * c13)))
    return dict(s13=s13, s12=s12, s23=s23, Delta=D, dmu1=P[1, 0] - 1 / 6, dtau1=P[2, 0] - 1 / 6, Ue1=P[0, 0])

# ---------------- state decomposition (real copies of irreducible components) ----------------
def components(M, irreps):
    """unit-normalised sector state -> list of (irrep, real 3x3 component matrix) (Re and Im copies)."""
    Z = M / np.linalg.norm(M)
    out = []
    for r in irreps:
        K = PROJ[r](Z)
        for part in (K.real, K.imag):
            if np.linalg.norm(part) > 1e-12: out.append((r, part))
    return out

def fixed_dim(g, irrep):
    """dimension of the g-fixed subspace of a real irrep of 3x3 matrices."""
    basis = []
    for i in range(3):
        for j in range(3):
            E = np.zeros((3, 3)); E[i, j] = 1; basis.append(PROJ[irrep](E).ravel())
    B = np.array(basis); r = np.linalg.matrix_rank(B, 1e-10)
    U, S, Vt = np.linalg.svd(B); Vb = Vt[:r]                    # orthonormal basis of the irrep subspace
    A = np.array([(act(g, v.reshape(3, 3))).ravel() for v in Vb]) @ Vb.T   # rep matrix
    return int(round(np.trace(sum(np.linalg.matrix_power(A, k) for k in range(order(g))) / order(g)))), r
def order(g):
    for k in range(1, 13):
        if np.allclose(np.linalg.matrix_power(g, k), np.eye(3)): return k
