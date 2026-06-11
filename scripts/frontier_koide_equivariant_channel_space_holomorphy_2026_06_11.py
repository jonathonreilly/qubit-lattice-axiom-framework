#!/usr/bin/env python3
"""Koide equivariant channel space -- channel-independent holomorphy check.

Companion runner for
    docs/KOIDE_GENERATION_CHANNEL_SPACE_HOLOMORPHY_CHANNEL_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-06-11.md

Block01 (KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_..._2026-06-11)
showed, for ONE probe coupling (the C_3[111] rotation channel), that the
first-order staggered Berezin output is holomorphic in the channel
parameters and that count-twice |b|^2 dependence enters exactly through
the K-reality restriction c = conj(b).  The declared open residual was
channel generality.  This runner closes that residual at the bilinear
level by classifying the COMPLETE C_3-equivariant coupling space on the
corner sector and testing the localization on all of it:

  A. Surface: D, the exact corner basis, the rotation permutation P8.

  B. Channel-space classification: the commutant of the realized C_3
     action on the 8-dim corner space has complex dimension 24 (computed
     two ways: nullity of the commutator map, and the 24 integer
     orbit-sum basis elements); the isotype multiplicities are
     (triv, omega, omega-bar) = (4, 2, 2), so the channel space is
     M_4(C) + M_2(C) + M_2(C).

  C. Lattice realizability: the site-diagonal staggered phases
     eps(x) = (-1)^(x1+x2+x3) and eps_mu(x) = (-1)^(x_mu) restrict to
     the corner-label complement (hw_k <-> hw_(3-k), i.e. native
     hw=1 <-> hw=2 mixing channels EXIST) and the bit-mu toggles;
     together with translations they span ALL of M_8 on the corner
     sector, and their C_3 averages span the full 24-dim commutant --
     every equivariant channel is lattice-realizable.

  D. Block decomposition and factorization: in the exact isotype basis
     V, every channel is (A4, beta, gamma) with beta/gamma the 2x2
     doublet-isotype blocks; det(A|ker) = det(A4) det(beta) det(gamma)
     (verified at exact rational parameter points); the parameter map is
     C-linear with INTEGER coefficient matrices, so the corner factor is
     a POLYNOMIAL in the channel parameters for EVERY channel -- the
     measure never supplies a conjugate, channel-independently.

  E. Where count-twice enters, channel-independently: complex
     conjugation K maps the channel blocks (A4, beta, gamma) ->
     (conj A4, conj gamma, conj beta) (the omega/omega-bar K-orbit
     pairing); the K-real (real-parameter) section ties gamma =
     conj(beta), making the doublet factor det(beta) det(gamma) =
     |det beta|^2 -- the modulus; the Hermitian section ties each block
     to its own conjugate-transpose (in-block z zbar terms, Wirtinger
     -1).  Both tying classes are antiunitary parameter restrictions;
     the unrestricted output is holomorphic for every channel.  The
     block01 rotation channel and the 2026-06-08 Kahler-Dirac
     Hermitian-corner object are recovered as the circulant instance
     and the Hermitian point of the native eps-mixing channel family,
     respectively.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark load-bearing
premises at the point of use.  Final line: TOTAL: PASS=<n> FAIL=<m>
"""

import numpy as np
import sympy as sp

L = 4
N = L ** 3
TOL = 1e-9

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


def idx(x1, x2, x3):
    return (x1 % L) + L * ((x2 % L) + L * (x3 % L))


def sites():
    for x3 in range(L):
        for x2 in range(L):
            for x1 in range(L):
                yield (x1, x2, x3)


EMU = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(x, mu):
    if mu == 0:
        return 1
    if mu == 1:
        return (-1) ** (x[0] % 2)
    return (-1) ** ((x[0] + x[1]) % 2)


print("=" * 72)
print("Koide equivariant channel space -- channel-independent holomorphy")
print("box: Z^3 torus, L =", L, "(periodic sector; corner momenta exact)")
print("=" * 72)

# ===================== A. surface =====================================
print("\n--- A. surface reconstruction")

D = np.zeros((N, N))
for x in sites():
    for mu, e in enumerate(EMU):
        xp = tuple(x[k] + e[k] for k in range(3))
        xm = tuple(x[k] - e[k] for k in range(3))
        D[idx(*x), idx(*xp)] += 0.5 * eta_ks(x, mu)
        D[idx(*x), idx(*xm)] -= 0.5 * eta_ks(x, mu)

sv = np.linalg.svd(D, compute_uv=False)
ker_dim = int(np.sum(sv < 1e-9))
corners = [(n1, n2, n3) for n1 in (0, 1) for n2 in (0, 1) for n3 in (0, 1)]
PHI = []
for (n1, n2, n3) in corners:
    phi = np.array([(-1.0) ** (n1 * x[0] + n2 * x[1] + n3 * x[2])
                    for x in sites()])
    PHI.append(phi / np.linalg.norm(phi))
PHI = np.column_stack(PHI)
hw = [sum(c) for c in corners]
ok = (np.allclose(D, -D.T) and ker_dim == 8
      and np.linalg.norm(D @ PHI) < TOL
      and np.allclose(PHI.T @ PHI, np.eye(8))
      and [hw.count(k) for k in range(4)] == [1, 3, 3, 1])
check(1, "staggered surface reconstructed: D real antisymmetric, "
         "dim ker D = 8, exact corner basis, Hamming grading 1+3+3+1",
      ok)

UR = np.zeros((N, N))
for x in sites():
    xr = (x[1], x[2], x[0])
    UR[idx(*x), idx(*xr)] = 1.0
P8 = np.rint(PHI.T @ UR @ PHI).astype(int)
ok = (np.allclose(PHI.T @ UR @ PHI, P8)
      and np.array_equal(P8 @ P8 @ P8, np.eye(8, dtype=int))
      and np.linalg.norm(D @ (UR @ PHI)) < TOL)
check(2, "the lattice C_3[111] rotation restricts to an exact integer "
         "permutation P8 on the corner basis, P8^3 = I", ok)

# ===================== B. channel-space classification =================
print("\n--- B. the complete C_3-equivariant channel space")

# isotype multiplicities from exact projector traces
w_exact = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2          # omega
P8s = sp.Matrix(P8.tolist())
mult = []
for j in range(3):
    Qj = (sp.eye(8) + w_exact ** (-j) * P8s
          + w_exact ** (-2 * j) * P8s ** 2) / 3
    mult.append(sp.simplify(sp.trace(Qj)))
ok = (mult == [4, 2, 2])
check(3, "isotype multiplicities of the realized C_3 on the corner "
         "space: (trivial, omega, omega-bar) = (4, 2, 2) (exact "
         "projector traces) -- channel space = M_4 + M_2 + M_2", ok,
      f"traces = {mult}")

# commutant dimension, route 1: nullity of the commutator map
comm_map = (np.kron(np.eye(8), P8) - np.kron(P8.T, np.eye(8)))
nullity = 64 - np.linalg.matrix_rank(comm_map)
ok = (nullity == 24)
check(4, "commutant dimension over C = 24 = 4^2 + 2^2 + 2^2 (nullity "
         "of the commutator map, computed)", ok,
      f"computed nullity = {nullity}")

# commutant dimension, route 2: integer orbit-sum basis
perm = [int(np.argmax(P8[:, j])) for j in range(8)]   # P8 e_j = e_perm[j]
seen = set()
BASIS = []
for i in range(8):
    for j in range(8):
        if (i, j) in seen:
            continue
        orbit = []
        a, b = i, j
        while (a, b) not in orbit:
            orbit.append((a, b))
            a, b = perm[a], perm[b]
        Bm = np.zeros((8, 8), dtype=int)
        for (a, b) in orbit:
            Bm[a, b] = 1
        BASIS.append(Bm)
        seen.update(orbit)
ok = (len(BASIS) == 24
      and all(np.array_equal(Bm @ P8, P8 @ Bm) for Bm in BASIS)
      and np.linalg.matrix_rank(
          np.array([Bm.flatten() for Bm in BASIS])) == 24)
check(5, "explicit INTEGER basis of the channel space: the 24 orbit-sum "
         "matrices commute with P8 and are linearly independent", ok)

# ===================== C. lattice realizability ========================
print("\n--- C. every equivariant channel is lattice-realizable")

# site-diagonal staggered phases restricted to the corner sector
def site_diag(f):
    return np.diag([float(f(x)) for x in sites()])


EPS = np.rint(PHI.T @ site_diag(lambda x: (-1) ** (sum(x) % 2)) @ PHI
              ).astype(int)
EPSMU = [np.rint(PHI.T @ site_diag(lambda x, m=mu: (-1) ** (x[m] % 2))
                 @ PHI).astype(int) for mu in range(3)]
comp_ok = all(
    EPS[i, j] == (1 if all(corners[i][k] != corners[j][k] for k in range(3))
                  else 0)
    for i in range(8) for j in range(8))
tog_ok = all(
    EPSMU[mu][i, j] == (1 if (corners[i][mu] != corners[j][mu]
                              and all(corners[i][k] == corners[j][k]
                                      for k in range(3) if k != mu))
                        else 0)
    for mu in range(3) for i in range(8) for j in range(8))
ok = comp_ok and tog_ok
check(6, "the staggered phase eps(x) restricts to the corner-label "
         "COMPLEMENT (hw_k <-> hw_(3-k): native hw=1 <-> hw=2 mixing "
         "channel), and eps_mu(x) to the bit-mu toggles (exact integer "
         "matrices)", ok)

# translations restrict to the diagonal corner characters
TC = []
for mu, e in enumerate(EMU):
    T = np.zeros((N, N))
    for x in sites():
        xp = tuple(x[k] + e[k] for k in range(3))
        T[idx(*x), idx(*xp)] = 1.0
    TC.append(np.rint(PHI.T @ T @ PHI).astype(int))
diag_ok = all(np.array_equal(TC[mu], np.diag(np.diag(TC[mu])))
              for mu in range(3))

# monomials in (T_mu, eps_mu) span all of M_8 on the corner sector;
# their C_3 averages span the full commutant
monos = []
for zm in range(8):
    Zm = np.eye(8, dtype=int)
    for mu in range(3):
        if (zm >> mu) & 1:
            Zm = Zm @ TC[mu]
    for xm in range(8):
        Xm = np.eye(8, dtype=int)
        for mu in range(3):
            if (xm >> mu) & 1:
                Xm = Xm @ EPSMU[mu]
        monos.append(Zm @ Xm)
rank_full = np.linalg.matrix_rank(np.array([m.flatten() for m in monos]))
P8inv = P8.T
avg = [sum(np.linalg.matrix_power(P8, k) @ m
           @ np.linalg.matrix_power(P8inv, k) for k in range(3))
       for m in monos]
avg += [a @ P8 for a in avg] + [a @ P8.T for a in avg]
rank_avg = np.linalg.matrix_rank(np.array([m.flatten() for m in avg]))
ok = (diag_ok and rank_full == 64 and rank_avg == 24)
check(7, "lattice realizability: translation/eps_mu monomials span ALL "
         "of M_8 on the corner sector (rank 64), and their C_3 averages "
         "(with U_R powers) span the FULL 24-dim channel space -- every "
         "equivariant channel is realizable by lattice-built operators",
      ok, f"rank(monomials) = {rank_full}, rank(averaged) = {rank_avg}")

# ===================== D. blocks, factorization, holomorphy ============
print("\n--- D. isotype blocks, exact factorization, holomorphy")

# exact isotype basis V: trivial (hw0, hw1-triv, hw2-triv, hw3),
# omega (hw1, hw2), omega-bar = conjugates of the omega columns
hw1_idx = [corners.index(c) for c in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
hw2_idx = [corners.index(c) for c in [(0, 1, 1), (1, 0, 1), (1, 1, 0)]]
s3 = sp.sqrt(3)


def iso_vec(idxs, weights):
    v = sp.zeros(8, 1)
    for i, c in zip(idxs, weights):
        v[i] = c
    return v


cols = [iso_vec([corners.index((0, 0, 0))], [sp.Integer(1)]),
        iso_vec(hw1_idx, [1 / s3] * 3),
        iso_vec(hw2_idx, [1 / s3] * 3),
        iso_vec([corners.index((1, 1, 1))], [sp.Integer(1)]),
        iso_vec(hw1_idx, [1 / s3, w_exact / s3, w_exact ** 2 / s3]),
        iso_vec(hw2_idx, [1 / s3, w_exact / s3, w_exact ** 2 / s3])]
cols += [c.conjugate() for c in cols[4:6]]              # omega-bar slots
V = sp.Matrix.hstack(*cols)
Vh = V.conjugate().T
G = sp.simplify(Vh * V)
P8blk = sp.simplify(Vh * P8s * V)
lam_om = P8blk[4, 4]
ok = (G == sp.eye(8)
      and P8blk == sp.diag(1, 1, 1, 1, lam_om, lam_om,
                           sp.conjugate(lam_om), sp.conjugate(lam_om))
      and sp.simplify(lam_om ** 3 - 1) == 0
      and sp.simplify(lam_om - 1) != 0)
check(8, "exact isotype basis V: unitary, block-diagonalizes P8 to "
         "diag(1,1,1,1, w,w, wbar,wbar) with w a primitive cube root "
         "(omega-bar columns DEFINED as conjugates of omega columns)",
      ok)

# block structure of every channel basis element
MBLK = [sp.expand(Vh * sp.Matrix(Bm.tolist()) * V) for Bm in BASIS]


def offblock_zero(M):
    zones = [(range(0, 4), range(4, 8)), (range(4, 8), range(0, 4)),
             (range(4, 6), range(6, 8)), (range(6, 8), range(4, 6))]
    for rows, colz in zones:
        for r in rows:
            for c in colz:
                if sp.simplify(M[r, c]) != 0:
                    return False
    return True


ok = all(offblock_zero(M) for M in MBLK)
check(9, "EVERY channel basis element is block-diagonal (A4, beta, "
         "gamma) in the isotype basis: all off-isotype entries are "
         "exactly zero (24 x 48 symbolic entries)", ok)

# K-orbit pairing: conjugation swaps the beta and gamma blocks
SWAP = sp.diag(sp.eye(4), sp.zeros(2), sp.zeros(2))
SWAP[4:6, 6:8] = sp.eye(2)
SWAP[6:8, 4:6] = sp.eye(2)
ok = all(sp.expand(M.conjugate() - SWAP * M * SWAP) == sp.zeros(8)
         for M in MBLK)
check(10, "K-orbit pairing, channel-independent: complex conjugation "
          "maps every channel's blocks (A4, beta, gamma) -> (conj A4, "
          "conj gamma, conj beta) -- the omega/omega-bar doublet blocks "
          "are one K-orbit for EVERY channel", ok)

# exact factorization at rational parameter points
theta_pts = [
    [sp.Rational(k * k + 3, 7 + (k % 5)) for k in range(24)],
    [sp.Rational(2 * k + 1, 9 + (k % 4)) + sp.I * sp.Rational(k, 5 + (k % 3))
     for k in range(24)],
    [sp.Rational(5 - k, 11 + (k % 6)) - sp.I * sp.Rational(k * k, 13)
     for k in range(24)],
]
fact_ok = True
for th in theta_pts:
    A8 = sp.zeros(8)
    for ci, Bm in zip(th, BASIS):
        A8 += ci * sp.Matrix(Bm.tolist())
    Ablk = sp.expand(Vh * A8 * V)
    lhs = A8.det()
    rhs = (Ablk[0:4, 0:4].det() * Ablk[4:6, 4:6].det()
           * Ablk[6:8, 6:8].det())
    if sp.simplify(lhs - rhs) != 0:
        fact_ok = False
check(11, "exact factorization det(A|ker) = det(A4) det(beta) "
          "det(gamma) at 3 exact rational/complex parameter points "
          "(full 8x8 determinant vs block product)", ok and fact_ok)

# holomorphy: the parameter map is C-linear with integer coefficients
theta = list(sp.symbols("th0:24"))
Asym = sp.zeros(8)
for ci, Bm in zip(theta, BASIS):
    Asym += ci * sp.Matrix(Bm.tolist())
Ablk_sym = sp.expand(Vh * Asym * V)
det_beta = sp.expand(Ablk_sym[4:6, 4:6].det())
det_gamma = sp.expand(Ablk_sym[6:8, 6:8].det())
ok = (all(Bm.dtype.kind == "i" for Bm in BASIS)
      and det_beta.free_symbols <= set(theta)
      and det_gamma.free_symbols <= set(theta)
      and sp.Poly(det_beta, *theta).total_degree() == 2)
check(12, "channel-independent holomorphy: the channel space is the "
          "C-span of INTEGER matrices, so for EVERY channel the corner "
          "factor is a POLYNOMIAL in the channel parameters (det beta, "
          "det gamma computed symbolically over all 24 parameters: no "
          "conjugate appears) -- the first-order measure never supplies "
          "count-twice", ok)
residual("bilinear (free/quadratic) matter actions only: interacting or "
         "beyond-bilinear couplings are outside this classification.")
residual("the C_3 carrier premise scopes the channel space: couplings "
         "not commuting with the realized C_3 break the generation "
         "carrier and are excluded by the gate-note species surface, "
         "not by this runner.")

# ===================== E. where count-twice enters =====================
print("\n--- E. antiunitary tying classes: K-real and Hermitian sections")

# K-real (real-parameter) section: gamma = conj(beta), doublet factor
# = |det beta|^2
theta_re = list(sp.symbols("s0:24", real=True))
Are = sp.zeros(8)
for ci, Bm in zip(theta_re, BASIS):
    Are += ci * sp.Matrix(Bm.tolist())
Ablk_re = sp.expand(Vh * Are * V)
beta_re = Ablk_re[4:6, 4:6]
gamma_re = Ablk_re[6:8, 6:8]
ok = (sp.expand(gamma_re - beta_re.conjugate()) == sp.zeros(2)
      and sp.simplify(sp.expand(beta_re.det() * gamma_re.det())
                      - sp.expand(beta_re.det()
                                  * sp.conjugate(beta_re.det()))) == 0)
check(13, "K-real section (real channel parameters): gamma = "
          "conj(beta) EXACTLY for every channel, and the doublet factor "
          "becomes det(beta) conj(det beta) = |det beta|^2 -- the "
          "modulus appears on the K-real section, channel-independently",
      ok)

# Hermitian section: blocks individually Hermitian; in-block z zbar
ttau_ok = True
tr_map = []
for i, Bm in enumerate(BASIS):
    found = None
    for j, Bn in enumerate(BASIS):
        if np.array_equal(Bm.T, Bn):
            found = j
            break
    if found is None:
        ttau_ok = False
    tr_map.append(found)
p_s, q_s = sp.symbols("p q", real=True)
z_s, u_s = sp.symbols("z u")
zbar_s = sp.Symbol("zbar")
det_free = sp.det(sp.Matrix([[p_s, z_s], [u_s, q_s]]))
det_herm = sp.det(sp.Matrix([[p_s, z_s], [zbar_s, q_s]]))
ok = (ttau_ok
      and det_free.free_symbols == {p_s, q_s, z_s, u_s}
      and sp.diff(det_herm, z_s, zbar_s) == -1)
check(14, "Hermitian section: transpose permutes the integer channel "
          "basis (A+ = A ties theta_i = conj theta_tau(i), blockwise "
          "Hermitian); a Hermitian-restricted doublet block [[p,z],"
          "[zbar,q]] carries the in-block count-twice term (Wirtinger "
          "d^2 det/dz dzbar = -1), while the unrestricted block det is "
          "conjugate-free", ok)

# rotation channel of block01 recovered as the circulant instance
a_s, b_s, c_s = sp.symbols("a b c")
lam_w = a_s + b_s * lam_om + c_s * sp.conjugate(lam_om)
lam_wb = a_s + b_s * sp.conjugate(lam_om) + c_s * lam_om
det3 = a_s ** 3 + b_s ** 3 + c_s ** 3 - 3 * a_s * b_s * c_s
Arot = a_s * sp.eye(8) + b_s * P8s + c_s * P8s.T
Ablk_rot = sp.expand(Vh * Arot * V)
ok = (sp.simplify(Ablk_rot[4:6, 4:6] - lam_w * sp.eye(2)) == sp.zeros(2)
      and sp.simplify(Ablk_rot[6:8, 6:8] - lam_wb * sp.eye(2))
      == sp.zeros(2)
      and sp.simplify(sp.expand((a_s + b_s + c_s) ** 4
                                * (lam_w * lam_wb) ** 2
                                - (a_s + b_s + c_s) ** 2 * det3 ** 2))
      == 0)
check(15, "block01's rotation channel is the scalar (circulant) "
          "instance: beta = lam_omega * I, gamma = lam_omegabar * I, "
          "and the block factorization reproduces the landed "
          "(a+b+c)^2 det3^2 identity exactly; its K-real line c = "
          "conj(b), a real is the channel-space K-real section", ok)

# the 2026-06-08 Kahler-Dirac Hermitian corner object: the Hermitian
# point of the native eps-mixing channel family
m0, m1, m2, n0, n1, n2 = sp.symbols("m0 m1 m2 n0 n1 n2")
EPSs = sp.Matrix(EPS.tolist())
circ_m = m0 * sp.eye(8) + m1 * P8s + m2 * P8s ** 2
circ_n = n0 * sp.eye(8) + n1 * P8s + n2 * P8s ** 2
# split by Hamming parity (hw odd = the two triplet-bearing sectors)
PARITY = sp.diag(*[(-1) ** hw[i] for i in range(8)])
Podd = (sp.eye(8) - PARITY) / 2               # hw odd (1 and 3)
Peven = (sp.eye(8) + PARITY) / 2              # hw even (0 and 2)
Amix = sp.expand(Peven * EPSs * circ_m * Podd
                 + Podd * EPSs * circ_n * Peven)
Ablk_mix = sp.expand(Vh * Amix * V)
beta_mix = Ablk_mix[4:6, 4:6]
gamma_mix = Ablk_mix[6:8, 6:8]
det_beta_mix = sp.expand(beta_mix.det())
herm_sub = {n0: sp.conjugate(m0), n1: sp.conjugate(m2),
            n2: sp.conjugate(m1)}
Amix_h = sp.expand(Amix.subs(herm_sub))
det_beta_h = sp.simplify(det_beta_mix.subs(herm_sub))
mu_w = beta_mix[0, 1]
ok = (offblock_zero(Ablk_mix)
      and beta_mix[0, 0] == 0 and beta_mix[1, 1] == 0
      and det_beta_mix.free_symbols <= {m0, m1, m2, n0, n1, n2}
      and sp.simplify(Amix_h - Amix_h.conjugate().T) == sp.zeros(8)
      and sp.simplify(det_beta_h
                      + mu_w.subs(herm_sub)
                      * sp.conjugate(mu_w.subs(herm_sub))) == 0)
check(16, "the native eps-mixing (hw=1 <-> hw=2) channel family is "
          "equivariant with off-diagonal doublet blocks; UNRESTRICTED "
          "it is holomorphic (det beta = -mu mu', conjugate-free); its "
          "HERMITIAN point ties mu' = conj(mu) and det beta = -|mu|^2 "
          "-- the 2026-06-08 Hermitian-corner |det M|^2 structure is "
          "the K-tied point of a holomorphic channel family, not a "
          "measure output", ok)

# full-surface confirmation with an hw-mixing coupling included
EPSfull = site_diag(lambda x: (-1) ** (sum(x) % 2))
t = 1e-3
pts = [(0.7, 0.31 + 0.22j, 0.31 - 0.22j, 0.15 + 0.07j),
       (0.9, 0.11 + 0.47j, 0.05 - 0.13j, -0.21 + 0.09j)]
dets = []
cdets = []
for (av, bv, cv, hv) in pts:
    Afull = av * np.eye(N) + bv * UR + cv * UR.T + hv * EPSfull
    with np.errstate(all="ignore"):
        dets.append(np.linalg.det(D.astype(complex) + t * Afull))
    A8n = av * np.eye(8) + bv * P8 + cv * P8.T + hv * EPS
    cdets.append(np.linalg.det(A8n))
ratio_full = dets[0] / dets[1]
ratio_corner = cdets[0] / cdets[1]
ok = abs(ratio_full - ratio_corner) / abs(ratio_corner) < 1e-2
check(17, "full-surface confirmation: det(D + tA) leading behaviour "
          "matches the corner determinant for a coupling INCLUDING the "
          "native eps hw-mixing channel (ratio of two parameter "
          "points)", ok,
      f"|ratio mismatch| = "
      f"{abs(ratio_full - ratio_corner) / abs(ratio_corner):.2e}")
residual("which reading section is physical (unrestricted holomorphic "
         "with K-orbit outcomes vs an antiunitary-tied section) is NOT "
         "decided here: it is the standing occupancy/K-reality "
         "selection -- the named owner-decision premise surface of the "
         "2026-06-09 occupancy note and the 2026-06-02 custody note. "
         "Nothing is adopted by this runner.")
residual("inherited gate-note residuals remain at their declared "
         "grades (kinetic-class premise, spin-statistics support tier, "
         "boundary-holonomy convention, AC_phi_lambda labeling "
         "convention).")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: the COMPLETE C_3-equivariant bilinear channel space on "
      "the corner sector is M_4 + M_2 + M_2 (24-dim, fully lattice-"
      "realizable, including native hw=1<->hw=2 eps-mixing channels); "
      "for EVERY channel the first-order corner output is a polynomial "
      "in the channel parameters (holomorphy is channel-independent); "
      "count-twice/modulus structure arises exactly on antiunitary-"
      "tied parameter sections (K-real: gamma = conj beta -> "
      "|det beta|^2; Hermitian: in-block z zbar), recovering block01's "
      "c = conj(b) line and the 2026-06-08 |det M|^2 object as "
      "instances. No premise adopted; no audit status set.")
raise SystemExit(0 if _fail == 0 else 1)
