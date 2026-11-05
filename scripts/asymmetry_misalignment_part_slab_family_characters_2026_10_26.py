#!/usr/bin/env python3
"""Test A (pre-registered in sol_criteria_pre_run.txt): on the adopted Wilson-type domain-wall slab
(4 components per Z^3 site, Shamir layer hop A_UP = (G5 + i G4)/2, as in the cube-three-families runner),
take the (2,4) window (m = 3), extract the three near-wall X-point Weyl families, bring every node to ONE
standard Weyl form (Lorentz-consistent frames), and compute the family action of rotations, translations
and the antiunitary T. Kill condition: no antiunitary, or all real family actions scalar, or non-real."""
import itertools, numpy as np
np.set_printoptions(precision=4, suppress=True)
s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
PAULI = [sx, sy, sz]
Gm = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]
G5, G4 = Gm[4], Gm[3]
A_UP = (G5 + 1j * G4) / 2
def bond(Ls):
    S = np.zeros((Ls, Ls)); S[np.arange(1, Ls), np.arange(Ls - 1)] = 1
    return np.kron(A_UP, S) + np.kron(A_UP.conj().T, S.T)
def h_on(k, m):
    return sum(np.sin(k[i]) * Gm[i] for i in range(3)) + (m - 1 - sum(1 - np.cos(k[i]) for i in range(3))) * G5
def H(k, m, Ls): return np.kron(h_on(k, m), np.eye(Ls)) + bond(Ls)
def dH(k, i, Ls): return np.kron(np.cos(k[i]) * Gm[i] - np.sin(k[i]) * G5, np.eye(Ls))
Ls, m = 8, 3.0
Xpos = np.kron(np.eye(4), np.diag(np.arange(Ls)))
corners = {''.join(map(str, c)): np.array(c, float) * np.pi for c in itertools.product((0, 1), repeat=3)}
def near_modes(k, m, tol=1e-8):
    e, v = np.linalg.eigh(H(k, m, Ls)); Z = v[:, np.abs(e) < tol]
    if Z.shape[1] == 0: return Z, Z
    xw, xv = np.linalg.eigh(Z.conj().T @ Xpos @ Z); B = Z @ xv
    return B[:, xw < Ls / 2], B[:, xw >= Ls / 2]
print("== A1 window content (near-wall zero modes per corner)")
for mm in (0.6, 3.0, 5.0):
    cnt = {c: near_modes(k, mm)[0].shape[1] for c, k in corners.items()}
    print(f"  m = {mm}: " + ", ".join(f"{c}:{n}" for c, n in cnt.items() if n))
A1 = all((near_modes(k, 3.0)[0].shape[1] == (2 if c.count('1') == 1 else 0)) for c, k in corners.items())
print("A1 PASS" if A1 else "A1 FAIL")
# ---- antiunitary T = C K with k -> -k: solve C h(k)^* = h(-k) C, C A^* = A C, C A^T = A^+ C
rng = np.random.default_rng(11)
def solve_intertwiner(pairs):
    # find C (4x4) with C Mi = Ni C for all (Mi, Ni)
    rows = []
    for Mi, Ni in pairs:
        rows.append(np.kron(np.eye(4), Mi.T) - np.kron(Ni, np.eye(4)))   # vec_row(C Mi - Ni C) = 0
    Aeq = np.vstack(rows); u, s, vh = np.linalg.svd(Aeq)
    nnull = int((np.abs(s) < 1e-9).sum())
    return [vh[i].conj().reshape(4, 4) for i in range(len(s) - nnull, len(s))], s.min()
ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(4)]
Cs, smin = solve_intertwiner([(h_on(k, m).conj(), h_on(-k, m)) for k in ks] + [(A_UP.conj(), A_UP), (A_UP.T, A_UP.conj().T)])
C = Cs[0]; C = C / np.sqrt(np.trace(C @ C.conj().T).real / 4)
resT = max(np.abs(np.kron(C, np.eye(Ls)) @ H(k, m, Ls).conj() @ np.kron(C, np.eye(Ls)).conj().T - H(-k, m, Ls)).max() for k in ks)
print(f"== A2 antiunitary T = C K: nullspace dim {len(Cs)}, unitary {np.allclose(C @ C.conj().T, np.eye(4))}, residual {resT:.1e}, T^2 = C C* = {np.round(np.trace(C @ C.conj())/4, 6)}")
A2 = resT < 1e-10
print("A2 PASS" if A2 else "A2 FAIL")
# ---- node frames: bring every X node to the standard Weyl form h = chi * v * p.sigma
def pauli_coeffs(V): return np.array([np.real(np.trace(V @ P)) / 2 for P in PAULI])
def adjoint(W): return np.array([[np.real(np.trace(PAULI[k] @ W.conj().T @ PAULI[j] @ W)) / 2 for k in range(3)] for j in range(3)])
def su2_from_rot(R):
    # W in SU(2) with W^+ sigma_j W = sum_k R_jk sigma_k  <=>  sigma_j W - W (sum_k R_jk sigma_k) = 0 (linear in W)
    rows = []
    for j in range(3):
        T = sum(R[j, k] * PAULI[k] for k in range(3))
        rows.append(np.kron(PAULI[j], np.eye(2)) - np.kron(np.eye(2), T.T))
    u, sv, vh = np.linalg.svd(np.vstack(rows))
    assert sv[-1] < 1e-8 and sv[-2] > 1e-6, f"no unique SU(2) lift (sing vals {sv[-2:]})"
    W = vh[-1].conj().reshape(2, 2)
    W = W / np.sqrt(np.linalg.det(W))
    assert np.allclose(adjoint(W), R, atol=1e-8)
    return W
Xn = {'x': corners['100'], 'y': corners['010'], 'z': corners['001']}
frames = {}; Z = {}; chis = {}
for a, k in Xn.items():
    Zn, _ = near_modes(k, m); Z[a] = Zn
    Vs = [Zn.conj().T @ dH(k, i, Ls) @ Zn for i in range(3)]
    M = np.array([pauli_coeffs(V) for V in Vs]); tilt = max(abs(np.trace(V)) / 2 for V in Vs)
    chi = np.sign(np.linalg.det(M)); v = abs(np.linalg.det(M)) ** (1 / 3)
    R = np.linalg.inv(M) @ (chi * v * np.eye(3))
    assert np.allclose(R @ R.T, np.eye(3), atol=1e-8) and np.linalg.det(R) > 0
    W = su2_from_rot(R)
    chk = max(np.abs(W.conj().T @ Vs[i] @ W - chi * v * PAULI[i]).max() for i in range(3))
    frames[a] = W; chis[a] = chi
    print(f"  node X_{a}: velocity matrix diag {np.round(np.diag(M), 3)}, tilt {tilt:.0e}, chirality {int(chi)}, standard-form residual {chk:.0e}")
assert len(set(chis.values())) == 1
chi = list(chis.values())[0]
# fix each node's frame phase so that T acts as (i sigma_y) K (family part 1)
Cbig = np.kron(C, np.eye(Ls))
for a in Xn:
    Th = frames[a].conj().T @ (Z[a].conj().T @ Cbig @ Z[a].conj()) @ frames[a].conj()   # psi -> Th psi^*
    ph = np.trace(Th @ (1j * sy).conj().T) / 2
    assert np.allclose(Th, ph * 1j * sy, atol=1e-8), "T not of standard form on node"
    frames[a] = frames[a] * np.sqrt(ph)        # W -> W e^{i alpha} changes Th by e^{-2 i alpha}
    Th3 = frames[a].conj().T @ (Z[a].conj().T @ Cbig @ Z[a].conj()) @ frames[a].conj()
    assert np.allclose(Th3, 1j * sy, atol=1e-8), f"could not normalise T on node {a}"
print("  T acts on every X node as (i sigma_y) K after node rephasing: family part of T = 1 (A2 consistent)")
# ---- rotations: find spinor S with S G_i S^+ = sum_j R_ji G_j and [S, G4] = [S, G5] = 0
def spinor_rep(R):
    pairs = [(Gm[i], sum(R[j, i] * Gm[j] for j in range(3))) for i in range(3)] + [(G4, G4), (G5, G5)]
    Ss, _ = solve_intertwiner(pairs); S = Ss[0]; return S / np.sqrt(np.trace(S @ S.conj().T).real / 4)
rots = {'C2x': np.diag([1., -1, -1]), 'C2y': np.diag([-1., 1, -1]), 'C2z': np.diag([-1., -1, 1]),
        'C3(111)': np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.]])}      # k -> R k, (Rk) = (kz, kx, ky)
names = ['x', 'y', 'z']
def node_of(k):
    for a, kk in Xn.items():
        if np.allclose(np.mod(k - kk + np.pi, 2 * np.pi) - np.pi, 0, atol=1e-9): return a
fam = {}
for gname, R in rots.items():
    S = spinor_rep(R); Sbig = np.kron(S, np.eye(Ls))
    res = max(np.abs(Sbig @ H(k, m, Ls) @ Sbig.conj().T - H(R @ k, m, Ls)).max() for k in ks)
    Sstd = su2_from_rot(R.T)    # standard spin lift in the common frame: U sigma_i U^+ = sum_j R_ji sigma_j
    if not np.allclose(adjoint(Sstd.conj().T), R, atol=1e-8): Sstd = su2_from_rot(R)
    F = np.zeros((3, 3), complex); ok = True
    for ia, a in enumerate(names):
        b = node_of(R @ Xn[a]); ib = names.index(b)
        U = frames[b].conj().T @ (Z[b].conj().T @ Sbig @ Z[a]) @ frames[a]
        # U should be phi * Sstd' where Sstd' satisfies U sigma_i U^+ = sum_j R_ji sigma_j
        cand = [Sstd, Sstd.conj().T]
        best = None
        for Sc in cand:
            if all(np.allclose(Sc @ PAULI[i] @ Sc.conj().T, sum(R[j, i] * PAULI[j] for j in range(3)), atol=1e-8) for i in range(3)):
                best = Sc
        phi = np.trace(best.conj().T @ U) / 2
        ok &= np.allclose(U, phi * best, atol=1e-7)
        F[ib, ia] = phi
    fam[gname] = F
    print(f"  {gname}: symmetry residual {res:.0e}; family matrix (rows: image node x,y,z) factorised={ok}\n{np.round(F, 4)}; det {np.round(np.linalg.det(F), 4)}")
# translations: Bloch phase e^{-i X_a . e}
for e, nm in zip(np.eye(3), ('tau_x', 'tau_y', 'tau_z')):
    fam[nm] = np.diag([np.exp(-1j * Xn[a] @ e) for a in names])
    print(f"  {nm}: family action diag {np.round(np.diag(fam[nm]).real, 4)}")
real = {g: np.allclose(F.imag, 0, atol=1e-8) and np.allclose(np.abs(F[np.abs(F) > 1e-6]), 1, atol=1e-8) for g, F in fam.items()}
scalar = {g: np.allclose(F, F[0, 0] * np.eye(3), atol=1e-8) for g, F in fam.items()}
print("  real family actions:", {g: v for g, v in real.items()}, "\n  scalar:", scalar)
A3 = all(real[g] for g in ('C2x', 'C2y', 'C2z', 'tau_x', 'tau_y', 'tau_z')) and not all(scalar[g] for g in ('C2x', 'C2y', 'C2z', 'tau_x', 'tau_y', 'tau_z'))
print("A3 PASS" if A3 else "A3 FAIL")
d3 = np.linalg.det(fam['C3(111)'])
print(f"A4 (report): C3(111) family action det = {np.round(d3, 4)}, det^2 = {np.round(d3**2, 4)}")
print(f"TEST A: {'PASS' if (A1 and A2 and A3) else 'FAIL'}  (A1 {A1}, A2 {A2}, A3 {A3})")
# ---------------- post-hoc (disclosed, NOT pre-registered): spin-statistics normalisation of the lattice operator
# A lattice rotation of order n acting on spin-1/2 fields satisfies g^n = (-1)^F. The solver fixed S_g only up to a
# global phase, so fix it by (F (x) Sstd)^n = -1 with Sstd in SU(2), i.e. F^n = -1 / Sstd^n (scalar).
orders = {'C2x': 2, 'C2y': 2, 'C2z': 2, 'C3(111)': 3}
famN = dict(fam)
for gname, nord in orders.items():
    R = rots[gname]; Sstd = su2_from_rot(R.T)
    if not all(np.allclose(Sstd @ PAULI[i] @ Sstd.conj().T, sum(R[j, i] * PAULI[j] for j in range(3)), atol=1e-8) for i in range(3)):
        Sstd = Sstd.conj().T
    Sn = np.linalg.matrix_power(Sstd, nord); target = -1 / Sn[0, 0]          # Sstd^n = +-1 (scalar)
    Fn = np.linalg.matrix_power(fam[gname], nord); lam = Fn[0, 0]
    assert np.allclose(Fn, lam * np.eye(3), atol=1e-8)
    c = (target / lam) ** (1 / nord)                                          # one admissible global phase
    famN[gname] = c * fam[gname]
    print(f"  natural normalisation {gname}: family action\n{np.round(famN[gname], 4)}; det {np.round(np.linalg.det(famN[gname]), 4)}; real {np.allclose(famN[gname].imag, 0, atol=1e-8)}")
