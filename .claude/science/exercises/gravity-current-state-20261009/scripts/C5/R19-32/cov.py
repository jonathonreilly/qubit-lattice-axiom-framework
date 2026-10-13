"""R19-32 shared module: covariant 10-component lattice h_mn in Feynman-de Donder gauge (Krein / Gupta-Bleuler).
Conventions (pre-registered 07:21Z):
 eta = diag(-1,1,1,1). Components I = (m<=n), unit-normalised symmetric basis E_I (off-diagonal E/sqrt2), as R19-25 s5.
 DeWitt one-particle form G_IJ = E_I^{mn} E_J{mn} - 1/2 tr(eta E_I) tr(eta E_J); inertia (6,4).
 Eigenfields f_A = R^T h with G = R diag(eta_A) R^T, eta_A = +-1 (adapted basis: TT, vector, scalar sectors).
 Feynman gauge: every eigenfield is a free lattice scalar, H = sum_A eta_A/2 sum_x [pi_A^2 + f_A (-Lap) f_A],
 with [f_A, pi_A] = i eta_A (Krein), so positive frequency annihilators b_A(k) obey [b_A, b_B^K] = eta_A delta_AB.
 Lattice derivatives: staggered tensor placement (h_00,h_ii at sites, h_0i on i-links, h_ij on ij-plaquettes; C_n on n-links),
 so every difference maps offset to offset with symbol D_j(k) = 2i sin(k_j/2) (07:27Z correction: the plain forward symbol
 e^{ik}-1 carries a non-common phase e^{ik/2} that breaks mutual nullness of C_0 and C_3; s1 v1 output showed |N|/w^2 = 1).
 de Donder field C_n = eta^{mm} d_m hbar_{mn}; positive-frequency part C_n^+(k) = sum_A c_{nA}(k) b_A(k) with
 d_0 -> -i omega, d_j -> D_j(k), and the 1/sqrt(2 omega) normalisation dropped (overall factor per k).
"""
import numpy as np
eta4 = np.diag([-1., 1, 1, 1])
pairs = [(m, n) for m in range(4) for n in range(m, 4)]

def basis():
    B = []
    for (m, n) in pairs:
        E = np.zeros((4, 4)); E[m, n] = E[n, m] = 1.0
        if m != n: E /= np.sqrt(2)
        B.append(E)
    return B
B = basis()

def dewitt():
    G = np.zeros((10, 10))
    for i, Ei in enumerate(B):
        for j, Ej in enumerate(B):
            G[i, j] = np.sum((eta4@Ei@eta4)*Ej) - 0.5*np.trace(eta4@Ei)*np.trace(eta4@Ej)
    return G
G = dewitt()

def comp(E):
    return np.array([np.sum(E*b) for b in B])

def adapted_eigenfields():
    """Columns of R = component vectors of eigenfields; returns R, eta_A, names. G = R diag(eta) R^T, R orthogonal."""
    cols, etas, names = [], [], []
    def add(E, name):
        v = comp(E); v = v/np.linalg.norm(v); s = v@G@v
        assert abs(abs(s) - 1) < 1e-12, (name, s)
        cols.append(v); etas.append(np.sign(s)); names.append(name)
    def Eof(m, n):
        E = np.zeros((4, 4)); E[m, n] = E[n, m] = 1.; return E
    # TT (w.r.t. z): (h11-h22)/sqrt2, h12
    add((Eof(1, 1) - Eof(2, 2))/2, 'TT+'); add(Eof(1, 2), 'TTx')
    # vector sectors (w.r.t. z): (h01,h13), (h02,h23)
    add(Eof(0, 1), 'v0x'); add(Eof(1, 3), 'vzx'); add(Eof(0, 2), 'v0y'); add(Eof(2, 3), 'vzy')
    # scalar sector: diagonal block span{e00, (e11+e22)/2, e33} plus h03
    d00 = np.zeros((4, 4)); d00[0, 0] = 1
    dpp = np.zeros((4, 4)); dpp[1, 1] = dpp[2, 2] = 0.5
    d33 = np.zeros((4, 4)); d33[3, 3] = 1
    V3 = np.array([comp(d00), comp(dpp), comp(d33)]).T
    V3 = V3/np.linalg.norm(V3, axis=0)
    Gs = V3.T@G@V3; w, U = np.linalg.eigh(Gs)
    for j in np.argsort(w):
        add(sum(U[i, j]*[d00, dpp, d33][i]/np.linalg.norm(comp([d00, dpp, d33][i])) for i in range(3)), f'sc{j}')
    add(Eof(0, 3), 'v03')
    R = np.array(cols).T
    return R, np.array(etas), names

R, ETA, NAMES = adapted_eigenfields()
assert np.allclose(R.T@R, np.eye(10)) and np.allclose(R.T@G@R, np.diag(ETA))
OFFZ = np.array([0, 0, 0, .5, 0, .5, 0, 0, 0, .5])   # z-offset of each eigenfield on the 1x1xL slice (one z index -> 1/2)
SECTORS = {'TT': [0, 1], 'vecx': [2, 3], 'vecy': [4, 5], 'scal': [6, 7, 8, 9]}

def dD(k):
    return 2j*np.sin(np.asarray(k, float)/2)

def constraint_coeffs(k):
    """c[n, A] for C_n^+(k) = sum_A c[n,A] b_A(k)  (overall 1/sqrt(2w) dropped). k = 3-vector."""
    D = dD(k); w = np.linalg.norm(D)
    sym = np.array([-1j*w, *D])              # d_mu symbol on positive frequency e^{i(kx - wt)}
    c = np.zeros((4, 10), complex)
    for I, E in enumerate(B):
        trh = np.trace(eta4@E)
        Ebar = E - 0.5*eta4*trh              # hbar_mn component pattern of unit h_I
        for n in range(4):
            c[n, I] = sum(eta4[m, m]*sym[m]*Ebar[m, n] for m in range(4))
    return c@R, w                            # in eigenfield basis (h_I = sum_A R_IA f_A)
