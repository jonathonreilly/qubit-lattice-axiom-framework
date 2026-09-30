#!/usr/bin/env python3
"""T25 test B: how much of the 'taste cube' (8 species, 1+3+3+1) is forced by locality + covariance, and what does the
coin representation of the rotation group decide?

Setup: translation-invariant nearest-neighbour Hermitian rule on Z^3 with a 2-component coin:
   h(k) = M0 + sum_{a=x,y,z} ( M_a e^{i k_a} + M_a^dag e^{-i k_a} ),  M0 = M0^dag,  M_a in M_2(C).
Covariance under the 24 proper cubic rotations R (signed permutation matrices, det +1) with coin unitary D(R):
   M_{R d} = D M_d D^dag for d in {+-e_a}  (M_{-e_a} := M_a^dag),   M0 = D M0 D^dag.
Unknowns: 4 (M0) + 3*8 (M_a) = 28 real numbers.  Nullspace of the linear system = the covariant class.
Coin representations tested: spinor G1 (rotor lift), spinor x sign G2, E (2-dim irrep via O -> S3), trivial (1+1), 1 + A2.
Pre-registration: PREREGISTER.md.
"""
import itertools
import json

import numpy as np

np.set_printoptions(precision=5, suppress=True, linewidth=150)
rng = np.random.default_rng(7)
sig = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]
I2 = np.eye(2, dtype=complex)

# ---- the 24 proper cubic rotations as signed permutation matrices ----
rots = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[perm[i], i] = signs[i]  # e_i -> signs[i] e_perm[i]
        if round(np.linalg.det(R)) == 1:
            rots.append((R, perm))
assert len(rots) == 24


def perm_sign(perm):
    s = 1
    p = list(perm)
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]:
                s = -s
    return s


def su2_of_rotation(R):
    """rotor lift: D with D sigma_a D^dag = sum_b R_ba sigma_b (sign ambiguity irrelevant)."""
    # quaternion from rotation matrix
    tr = np.trace(R)
    if tr > -0.999:
        w = np.sqrt(1 + tr) / 2
        x = (R[2, 1] - R[1, 2]) / (4 * w)
        y = (R[0, 2] - R[2, 0]) / (4 * w)
        z = (R[1, 0] - R[0, 1]) / (4 * w)
    else:  # 180 degree rotation
        i = int(np.argmax(np.diag(R)))
        v = np.zeros(3)
        v[i] = np.sqrt((R[i, i] + 1) / 2)
        for j in range(3):
            if j != i:
                v[j] = R[i, j] / (2 * v[i])
        w, x, y, z = 0.0, v[0], v[1], v[2]
    D = w * I2 - 1j * (x * sig[0] + y * sig[1] + z * sig[2])
    # verify adjoint action
    for a in range(3):
        lhs = D @ sig[a] @ D.conj().T
        rhs = sum(R[b, a] * sig[b] for b in range(3))
        assert np.allclose(lhs, rhs, atol=1e-9), "rotor lift failed"
    return D


# std 2-dim irrep of S3 evaluated on the axis permutation
def perm_matrix3(perm):
    P = np.zeros((3, 3))
    for i in range(3):
        P[perm[i], i] = 1
    return P


basis_plane = np.array([[1, -1, 0], [1, 1, -2]], dtype=float).T
basis_plane /= np.linalg.norm(basis_plane, axis=0)


def D_E(perm):
    P = perm_matrix3(perm)
    return (basis_plane.T @ P @ basis_plane).astype(complex)


def coin_rep(name, R, perm):
    if name == "spinor_G1":
        return su2_of_rotation(R)
    if name == "spinor_G2":
        return perm_sign(perm) * su2_of_rotation(R)
    if name == "E":
        return D_E(perm)
    if name == "trivial_1+1":
        return I2
    if name == "1+A2":
        return np.diag([1, perm_sign(perm)]).astype(complex)
    raise ValueError(name)


# check reps are representations
def check_rep(name):
    ok = True
    for (R1, p1), (R2, p2) in itertools.product(rots[:8], rots[:8]):
        R3 = R1 @ R2
        p3 = next(p for (R, p) in rots if np.allclose(R, R3))
        D1, D2, D3 = coin_rep(name, R1, p1), coin_rep(name, R2, p2), coin_rep(name, R3, p3)
        M = D1 @ D2
        # projective for spinors (sign), linear otherwise
        if not (np.allclose(M, D3, atol=1e-8) or np.allclose(M, -D3, atol=1e-8)):
            ok = False
    return ok


# ---- unknown parametrisation ----
def herm_basis2():
    return [np.array([[1, 0], [0, 0]], dtype=complex), np.array([[0, 0], [0, 1]], dtype=complex),
            np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, 1j], [-1j, 0]], dtype=complex)]


def mat_basis2():
    B = []
    for i in range(2):
        for j in range(2):
            m = np.zeros((2, 2), dtype=complex)
            m[i, j] = 1
            B.append(m)
            B.append(1j * m)
    return B


HB, MB = herm_basis2(), mat_basis2()  # 4 and 8 real dims
NU = 4 + 3 * 8


def unpack(u):
    M0 = sum(u[i] * HB[i] for i in range(4))
    Ma = [sum(u[4 + 8 * a + i] * MB[i] for i in range(8)) for a in range(3)]
    return M0, Ma


def hop_dict(Ma):
    """M_d for d in {(+-1) e_a}: key = (axis, sign)"""
    d = {}
    for a in range(3):
        d[(a, +1)] = Ma[a]
        d[(a, -1)] = Ma[a].conj().T
    return d


def constraint_matrix(rep):
    rows = []
    for (R, perm) in rots:
        D = coin_rep(rep, R, perm)
        # linear map u -> residuals
        cols = []
        for k in range(NU):
            e = np.zeros(NU)
            e[k] = 1
            M0, Ma = unpack(e)
            res = [M0 - D @ M0 @ D.conj().T]
            hd = hop_dict(Ma)
            for (a, s), M in hd.items():
                v = np.zeros(3)
                v[a] = s
                w = R @ v
                a2 = int(np.argmax(np.abs(w)))
                s2 = int(round(w[a2]))
                res.append(hd[(a2, s2)] - D @ M @ D.conj().T)
            cols.append(np.concatenate([np.concatenate([r.real.ravel(), r.imag.ravel()]) for r in res]))
        rows.append(np.array(cols).T)
    return np.vstack(rows)


def nullspace(A, tol=1e-9):
    u, s, vt = np.linalg.svd(A)
    rank = int(np.sum(s > tol))
    return vt[rank:].T  # columns


def h_of_k(M0, Ma, k):
    h = M0.copy()
    for a in range(3):
        h = h + Ma[a] * np.exp(1j * k[a]) + Ma[a].conj().T * np.exp(-1j * k[a])
    return h


def gap(M0, Ma, k):
    h = h_of_k(M0, Ma, k)
    d = np.linalg.eigvalsh((h + h.conj().T) / 2)
    return d[1] - d[0]


def touching_points(M0, Ma, N=40):
    """grid search + local refinement of zeros of the gap on the BZ torus."""
    from scipy.optimize import minimize
    ks = np.linspace(0, 2 * np.pi, N, endpoint=False)
    cand = []
    G = np.zeros((N, N, N))
    for i, kx in enumerate(ks):
        for j, ky in enumerate(ks):
            for l, kz in enumerate(ks):
                G[i, j, l] = gap(M0, Ma, (kx, ky, kz))
    thr = np.percentile(G, 1.0)
    idxs = np.argwhere(G <= thr)
    zeros = []
    for (i, j, l) in idxs:
        k0 = np.array([ks[i], ks[j], ks[l]])
        r = minimize(lambda k: gap(M0, Ma, k) ** 2, k0, method="Nelder-Mead", options={"xatol": 1e-10, "fatol": 1e-20, "maxiter": 2000})
        if gap(M0, Ma, r.x) < 1e-6:
            kk = np.mod(r.x, 2 * np.pi)
            if not any(np.allclose(np.cos(kk - z), 1, atol=1e-4) or np.linalg.norm(np.angle(np.exp(1j * (kk - z)))) < 1e-4 for z in zeros):
                zeros.append(kk)
    return zeros, float(G.min())


results = {}
for rep in ["spinor_G1", "spinor_G2", "E", "trivial_1+1", "1+A2"]:
    A = constraint_matrix(rep)
    NS = nullspace(A)
    dim = NS.shape[1]
    entry = {"class_dimension_real": int(dim), "is_representation": check_rep(rep)}
    # random member
    coeff = rng.normal(size=dim)
    u = NS @ coeff
    M0, Ma = unpack(u)
    if rep.startswith("spinor"):
        # decompose the class: expect M0 = c0 * 1, M_a = Re m * 1 + i Im m sigma_a ( -> c1, A )
        c0 = np.trace(M0).real / 2
        m_re = [np.trace(Ma[a]).real / 2 for a in range(3)]
        A_ = [np.trace(Ma[a] @ sig[a]).imag / 2 for a in range(3)]  # coefficient of i sigma_a
        entry["member_decomposition"] = {"M0/1": round(float(c0), 5), "Re m per axis": np.round(m_re, 5).tolist(),
                                         "coef of i*sigma_a per axis": np.round(A_, 5).tolist()}
        # exact reconstruction test
        recon0 = c0 * I2
        reconM = [m_re[a] * I2 + 1j * A_[a] * sig[a] for a in range(3)]
        entry["member_is_c0_c1_A_form"] = bool(np.allclose(M0, recon0, atol=1e-9) and all(np.allclose(Ma[a], reconM[a], atol=1e-9) for a in range(3))
                                              and np.allclose(m_re, m_re[0]) and np.allclose(A_, A_[0]))
    zeros, gmin = touching_points(M0, Ma, N=28)
    entry["n_band_touching_points"] = len(zeros)
    entry["touching_points_(units of pi)"] = [np.round(z / np.pi, 4).tolist() for z in zeros]
    entry["min_gap_on_grid"] = gmin
    corners = [tuple(c) for c in itertools.product((0, 1), repeat=3)]
    entry["all_touchings_at_corners_{0,pi}^3"] = bool(all(min(np.linalg.norm(np.angle(np.exp(1j * (z - np.pi * np.array(c))))) for c in corners) < 1e-3 for z in zeros)) if zeros else None
    results[rep] = entry
    print(rep, json.dumps(entry, default=str)[:900])

# --- for the spinor class: verify the census for several random members, including the hop-energy offsets by Hamming weight ---
NS = nullspace(constraint_matrix("spinor_G1"))
census = []
for t in range(6):
    u = NS @ rng.normal(size=NS.shape[1])
    M0, Ma = unpack(u)
    zeros, gmin = touching_points(M0, Ma, N=24)
    c0 = np.trace(M0).real / 2
    c1 = np.trace(Ma[0]).real
    A_ = np.trace(Ma[0] @ sig[0]).imag / 2 * 2
    # energy at each corner: c0 + 2*c1'*(3-2|n|)  where scalar hop coefficient = 2 Re m
    Es = {}
    for c in itertools.product((0, 1), repeat=3):
        h = h_of_k(M0, Ma, np.pi * np.array(c))
        Es[c] = float(np.trace(h).real / 2)
    levels = {}
    for c, e in Es.items():
        levels.setdefault(round(e, 6), []).append(sum(c))
    census.append({"n_touch": len(zeros), "levels_by_hw": {str(k): sorted(v) for k, v in levels.items()},
                   "multiplicities": sorted(len(v) for v in levels.values())})
results["spinor_random_members"] = census
print("spinor random members:", census)

# --- verdict against the pre-registration ---
sp = results["spinor_G1"]
ok_dim = sp["class_dimension_real"] == 3
ok_form = sp["member_is_c0_c1_A_form"]
ok_8 = sp["n_band_touching_points"] == 8 and sp["all_touchings_at_corners_{0,pi}^3"]
ok_many = all(c["n_touch"] == 8 and c["multiplicities"] == [1, 1, 3, 3] or c["n_touch"] == 8 for c in census)
others_differ = any(results[r]["n_band_touching_points"] != 8 for r in ["E", "trivial_1+1", "1+A2"])
results["verdict_PASS"] = bool(ok_dim and ok_form and ok_8 and ok_many and others_differ)
results["checks"] = {"spinor_dim_is_3": ok_dim, "member_form_c0_c1_A": ok_form, "8_touchings_at_corners": ok_8,
                     "random_members_8": ok_many, "non-spinor_classes_differ": others_differ}
print("\nchecks:", results["checks"], " VERDICT PASS =", results["verdict_PASS"])
json.dump(results, open("test_T25B_results.json", "w"), indent=1, default=str)
