"""W2 parts 1 and 3: (A) sizes of the C3 anomaly density in the vacuum and in thermal states for the
RN-L1 free lattice scalar (Weyl-ordered Gaussian expectations, exact midpoint sums on an Nq^3 grid);
vacuum energy density rho, pressure p_c = <T_cc> (L1 stress), cos-weighted energy e_c = <E_c>/V,
anomaly a_c = e_c - rho.  Tests whether a single cosmological-constant counterterm can absorb the
vacuum c-numbers (needs w_vac = -1 and the Killing c-number to vanish).
(B) rank of the irreducible O(kappa) constraint-bracket matrix (ultralocal representative,
derivation in W2_report.md) on backgrounds: vacuum/homogeneous, density modulation, beam current.
"""
import numpy as np

def grid(Nq):
    q = 2 * np.pi * (np.arange(Nq) + 0.5) / Nq - np.pi   # midpoint grid, symmetric
    return np.meshgrid(q, q, q, indexing='ij')

def cnumbers(m, Nq=64, T=None, normal_ordered=False):
    qx, qy, qz = grid(Nq)
    Q = (qx, qy, qz)
    w2 = m**2 + sum(2 - 2 * np.cos(qi) for qi in Q)
    w = np.sqrt(w2)
    if T is None:
        occ = np.zeros_like(w)
    else:
        occ = 1.0 / np.expm1(w / T)
    nfac = occ if normal_ordered else occ + 0.5          # <a^dag a> (+1/2 zero point)
    Gphi = nfac / w           # <|phi_q|^2> per site normalisation: (n+1/2)/w  (both q and -q -> factor)
    Gpi = nfac * w
    # quadratic-form symbols (sum over sites) evaluated as zone averages
    avg = lambda f: float(np.mean(f))
    rho = avg(0.5 * Gpi + 0.5 * w2 * Gphi)
    c = 0
    sym_Tcc_phi = -0.5 * m**2 + np.cos(Q[c]) * (1 - np.cos(Q[c])) - sum((1 - np.cos(Q[i])) for i in range(3) if i != c)
    pc = avg(0.5 * Gpi + sym_Tcc_phi * Gphi)
    ec = avg(np.cos(Q[c]) * (0.5 * Gpi + 0.5 * w2 * Gphi))
    # IR moment for the anomaly per quantum: (cos q_c - 1) w ~ -q_c^2 w / 2
    return dict(rho=rho, p=pc, e=ec, a=ec - rho)

print("=== (A1) vacuum c-numbers per site (lattice units), Weyl ordered ===")
print(" m     rho        p_c       e_c        a_c=e_c-rho   w=p/rho   rho+p     e_c+p_c")
for m in (0.0, 0.5, 1.0, 2.0):
    r = cnumbers(m)
    print(f" {m:3.1f}  {r['rho']:.6f}  {r['p']:+.6f}  {r['e']:+.6f}  {r['a']:+.6f}    {r['p']/r['rho']:+.4f}  {r['rho']+r['p']:+.6f}  {r['e']+r['p']:+.6f}")
print(" grid check (Nq=96, m=0.5):", {k: round(v, 6) for k, v in cnumbers(0.5, Nq=96).items()})
print(" -> w_vac != -1 and a_c != 0: one CC counterterm cannot absorb the vacuum energy, the vacuum")
print("    pressure tadpole and the vacuum Killing c-number at once (3 conditions; see report).")

print("\n=== (A2) thermal (normal-ordered) anomaly density a_T vs energy density rho_T ===")
print(" m     T       rho_T         a_T          a_T/rho_T    -<q_c^2>/2-weighted IR estimate ratio")
for m in (0.0, 0.5):
    for T in (0.01, 0.03, 0.1, 0.3, 1.0):
        r = cnumbers(m, Nq=96, T=T, normal_ordered=True)
        # IR expectation: a_T/rho_T ~ -<q_c^2 w n>/(2<w n>) ~ -(c_T T)^2 ; massless: <q^2>_th = 12 zeta(5)/zeta(3)... use ratio/T^2
        print(f" {m:3.1f}  {T:5.2f}  {r['rho']:.4e}   {r['a']:+.4e}   {r['a']/r['rho']:+.4e}   ratio/T^2 = {r['a']/r['rho']/T**2:+.4f}")
print(" -> a_T < 0 always (cos q - 1 <= 0); a_T/rho_T ~ -(const) (T a)^2 in the IR, O(1) at the zone scale")

print("\n=== (A3) one-quantum anomaly symbol (cos q_c - 1): zone average ===")
qx, qy, qz = grid(64)
print(" <cos q_c - 1>_zone =", float(np.mean(np.cos(qx) - 1)), " (C3: -1 per mode)")

print("\n=== (B) rank of the irreducible O(kappa) bracket matrix on backgrounds (L^3 torus) ===")
L = 6
N = L**3
idx = lambda x, y, z: ((x % L) * L + (y % L)) * L + (z % L)
def cd(f, c):  # central difference on the torus
    return 0.5 * (np.roll(f, -1, axis=c) - np.roll(f, 1, axis=c))
def bracket_matrix(Acal, rho_cur):
    """Acal: (3,L,L,L) anomaly densities A_c(x); rho_cur: (3,3) antisymmetric rotation-anomaly density
    (homogeneous). Ordering of constraints: [C_s(x)] then [C_c(x)], c=0..2. Irreducible pieces:
      boost   : {C_c[xi], C_s[N]} = sum_x sum_c xi_c N d_c A_c      (ultralocal representative)
      rotation: {C_a[xi], C_b[eta]} = sum_x sum_{c,a} rho_ca (xi_c d_c eta_a - eta_c d_c xi_a)
    """
    M = np.zeros((4 * N, 4 * N))
    s = lambda x: x                    # C_s index block 0
    v = lambda c, x: (1 + c) * N + x   # C_c blocks
    for c in range(3):
        vc = cd(Acal[c], c).ravel()
        for x in range(N):
            M[v(c, x), s(x)] += vc[x]
            M[s(x), v(c, x)] -= vc[x]
    # rotation: Delta[xi,eta] = sum rho_ca xi_c(x) (D_c eta_a)(x) - (xi<->eta)
    D = [np.zeros((N, N)) for _ in range(3)]
    for x0 in range(L):
        for y0 in range(L):
            for z0 in range(L):
                i = idx(x0, y0, z0)
                for c, (dx, dy, dz) in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                    D[c][i, idx(x0 + dx, y0 + dy, z0 + dz)] += 0.5
                    D[c][i, idx(x0 - dx, y0 - dy, z0 - dz)] -= 0.5
    for c in range(3):
        for a_ in range(3):
            if rho_cur[c, a_] == 0:
                continue
            blk = rho_cur[c, a_] * D[c]            # xi_c (x) * (D_c eta_a)(x)
            M[(1 + c) * N:(2 + c) * N, (1 + a_) * N:(2 + a_) * N] += blk
            M[(1 + a_) * N:(2 + a_) * N, (1 + c) * N:(2 + c) * N] -= blk.T
    assert np.allclose(M, -M.T)
    return M

X = np.indices((L, L, L)).astype(float)
cases = {}
A0 = -0.4 * np.ones((3, L, L, L))
cases['vacuum / homogeneous isotropic (A_c const, no current)'] = (A0, np.zeros((3, 3)))
Amod = A0 + 0.1 * np.sin(2 * np.pi * X[0] / L)[None]
cases['density modulation along x (A_c(x) varies), no current'] = (Amod, np.zeros((3, 3)))
Arnd = A0 + 0.1 * np.random.default_rng(1).standard_normal((3, L, L, L))
cases['generic inhomogeneous A_c(x), no current'] = (Arnd, np.zeros((3, 3)))
rc = np.zeros((3, 3)); rc[1, 0] = 0.05; rc[0, 1] = -0.05; rc[2, 0] = 0.05; rc[0, 2] = -0.05
cases['homogeneous beam along x (rotation-anomaly current), A const'] = (A0, rc)
cases['beam + generic inhomogeneous A_c(x)'] = (Arnd, rc)
for name, (Acal, rcur) in cases.items():
    M = bracket_matrix(Acal, rcur)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1e-10 * max(sv.max(), 1e-300))) if sv.max() > 0 else 0
    extra = rank / (2 * N)
    print(f" {name:62s} rank {rank:5d} / {4*N}  -> second-class per site {rank/N:.3f}, dof per site = 2 + {extra:.3f}")
print(" (dof per site = (12 - 2*(#first class) - #second class)/2 = 2 + rank/(2N); no secondary constraints")
print("  arise where the pairing is invertible, the multipliers n(x) and v.N(x) are fixed instead)")

print("\n=== (B2) same backgrounds, C3's own (WZ-consistent) Killing representative for the boost block:")
print("    {C_c[xi], C_s[N]} = - sum_x sum_c xi_c(x) A_c(x) (D_c N)(x)   (rotation block unchanged)")
def bracket_matrix_rep1(Acal, rho_cur):
    M = bracket_matrix(np.zeros_like(Acal), rho_cur)      # rotation part only
    Dm = []
    for c in range(3):
        Dc = np.zeros((N, N))
        for x0 in range(L):
            for y0 in range(L):
                for z0 in range(L):
                    i = idx(x0, y0, z0); d = [(1, 0, 0), (0, 1, 0), (0, 0, 1)][c]
                    Dc[i, idx(x0 + d[0], y0 + d[1], z0 + d[2])] += 0.5
                    Dc[i, idx(x0 - d[0], y0 - d[1], z0 - d[2])] -= 0.5
        blk = -np.diag(Acal[c].ravel()) @ Dc          # rows: xi_c(x), cols: N(y)
        M[(1 + c) * N:(2 + c) * N, 0:N] += blk
        M[0:N, (1 + c) * N:(2 + c) * N] -= blk.T
    assert np.allclose(M, -M.T)
    return M
cases2 = dict(cases)
cases2['vacuum after the pressure counterterm (A_c = 0 homogeneous), no current'] = (np.zeros((3, L, L, L)), np.zeros((3, 3)))
for name, (Acal, rcur) in cases2.items():
    M = bracket_matrix_rep1(Acal, rcur)
    sv = np.linalg.svd(M, compute_uv=False)
    rank = int(np.sum(sv > 1e-10 * sv.max())) if sv.max() > 0 else 0
    print(f" {name:72s} rank {rank:5d} / {4*N}  -> dof per site = 2 + {rank/(2*N):.3f}")
print(" (homogeneous A_c != 0: rank deficit only at momenta with sin p_c = 0 for all c, i.e. p in {0,pi}^3)")
