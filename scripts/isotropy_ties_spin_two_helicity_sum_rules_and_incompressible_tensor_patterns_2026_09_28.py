#!/usr/bin/env python3
"""Incompressible tensor patterns exist, but isotropy ties a spin-2 field's helicity sum rules: 4 v1 = v2 + 3 v0.

Question (the owner, 2026-09-28): prove or refute the incompressible electric
pattern that the previous probe (one qubit per slot under the tensor momentum
rule) found necessary for a light-cone graviton.

Answer tested here:
  (refute) An incompressible momentum-rule tensor with a light-cone channel
  exists: E = curl_1(A~ - (1/2) I tr A~) built from three photon fields A~
  (a U(1) triplet), lattice-exact on the landed slot placement.
  (prove) A sharper obstacle replaces it. For any spin-j >= 2 multiplet of
  operators whose leading f-sum form is O(q^2) and isotropic, the helicity
  values are v_m = alpha + beta m^2 (invariant theory), so
  4 v_(+-1) = v_(+-2) + 3 v_0. In a ground state every v_m >= 0, so a
  first-order helicity-2 sum rule forces a helicity-1 one at least a quarter
  as large. Einstein's linearized form satisfies the identity only with a
  negative helicity-0 value (the conformal mode), which a positive model
  cannot have.

Landed context (not premises): the tensor stencil and linear comparator
(docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_..._2026-09-14.md,
docs/TENSOR_LINEAR_DISPERSION_NEEDS_OSCILLATOR_SLOTS_..._2026-09-24.md), the
spectral-moment chain (docs/RING_MODEL_ENERGY_ONLY_BOUNDS_..._2026-09-25.md),
probe 10 (docs/ONE_QUBIT_PER_SLOT_UNDER_THE_TENSOR_MOMENTUM_RULE_..._2026-09-28.md).
Reference only: Weinberg (1964-65) on massless helicity-h fields; Pretko
(arXiv:1604.05329) scalar-charge theory.

Not pre-registered: the identity was derived first and these checks frozen
before the note.

Checks:
  A  the identity by exact invariant projection: for spin 2 (one and two
     copies) and spin 3, the isotropic part of random Hermitian forms is
     helicity-diagonal with 4 v1 = v2 + 3 v0 about random directions;
     positive (group-averaged) families have every v_m >= 0 and v1 >= v2/4.
  B  worked forms (spin-2 part, unit Frobenius): Einstein-Hilbert
     (1/2, 0, -1/6) k^2 with v0 < 0; the landed lattice E-H symbol gives the
     same ratios; Pretko's scalar-charge theory and a photon triplet give
     (1, 1/2, 1/3) k^2; all satisfy the identity.
  C  the momentum rule removes helicity 1: ker G(k) (landed stencil) has no
     overlap with the spin-2 helicity-1 directions about the lattice momentum,
     so positivity plus the identity forces v2 = v0 = 0 at order q^2 (the
     previous probe's q^4 law, recovered from isotropy and positivity).
  D  the incompressible construction: E = curl_1(A~ - I tr A~/2) of a photon
     triplet obeys the landed momentum rule exactly and is symmetric, on the
     landed slot placement; in the Gaussian (Maxwell) triplet its channel has
     omega = sqrt(UK)|K| (light cone), chi_E ~ q^2, S_E ~ q^3, m1_E ~ q^4, and
     3 of the 6 photon modes are invisible to E (helicity 1 and 0 partners).
  E  isotropy is load-bearing: a cubic-invariant positive first-order form can
     have v1 = 0 and v2 > 0 along an axis, but then its helicity-2 stiffness is
     direction-dependent (no single light cone).
Prints one line per check, the N5 lines and TOTAL: PASS=N FAIL=M.
"""
import numpy as np
from scipy.linalg import expm, null_space

AUDIT_TIMEOUT_SEC = 900
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


EPS = np.zeros((3, 3, 3))
for a, b, c in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    EPS[a, b, c] = 1; EPS[b, a, c] = -1
JVEC = [-1j * EPS[c] for c in range(3)]            # vector rep, D = exp(-i theta J)


def spin(j):
    ms = np.arange(j, -j - 1, -1); n = len(ms)
    Jz = np.diag(ms).astype(complex); Jp = np.zeros((n, n), complex)
    for a in range(1, n):
        Jp[a - 1, a] = np.sqrt(j * (j + 1) - ms[a] * (ms[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, Jz]


def invariant_basis(j, d):
    """Orthonormal basis of isotropic maps q -> sum_ab q_a q_b W_ab into End(spin j (x) C^d).
    Works on the full 3x3 index space, where the rotation action is unitary, so the orthogonal
    projection onto the invariants is the Haar average (it preserves positivity)."""
    Js = [np.kron(Jc, np.eye(d)) for Jc in spin(j)]; n = len(Js[0]); dim = 9 * n * n

    def unpack(v):
        return v.reshape(3, 3, n, n)
    Gs = []
    for c in range(3):
        G = np.zeros((dim, dim), complex)
        for i in range(dim):
            e = np.zeros(dim); e[i] = 1; W = unpack(e); out = np.zeros((3, 3, n, n), complex)
            for p in range(3):
                for q in range(3):
                    out[p, q] += -1j * (Js[c] @ W[p, q] - W[p, q] @ Js[c])
                    out[p, q] += sum(EPS[c, a, p] * W[a, q] for a in range(3)) + sum(EPS[c, b, q] * W[p, b] for b in range(3))
            G[:, i] = out.reshape(-1)
        Gs.append(G)
    Cas = sum(G.conj().T @ G for G in Gs)                      # Hermitian, positive; its kernel = the invariants
    w, U = np.linalg.eigh((Cas + Cas.conj().T) / 2)
    return U[:, w < 1e-9 * max(1.0, w.max())], unpack, Js


def helicity_blocks(W, j, d, qh):
    J1 = spin(j); w1, U1 = np.linalg.eigh(sum(qh[c] * J1[c] for c in range(3)))
    U = np.kron(U1, np.eye(d)); w = np.kron(w1, np.ones(d))
    V = U.conj().T @ np.einsum('a,b,abij->ij', qh, qh, W) @ U
    ms = np.round(w).astype(int); n = len(ms)
    off = max([abs(V[a, b]) for a in range(n) for b in range(n) if ms[a] != ms[b]] + [0])
    return {m: V[np.ix_(ms == m, ms == m)] for m in range(-j, j + 1)}, off


# ---------------------------------------------------------------- A: the identity
rng = np.random.default_rng(20260928)
rowsA = []; okA = True
for j, d in [(2, 1), (2, 2), (3, 1)]:
    Nb, unpack, Js = invariant_basis(j, d); n = (2 * j + 1) * d
    for trial in range(3):
        W0 = np.zeros((3, 3, n, n), complex)
        for a in range(3):
            for b in range(a, 3):
                r = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n)); W0[a, b] = W0[b, a] = r + r.conj().T
        W = unpack(Nb @ (Nb.conj().T @ W0.reshape(-1)))
        ax = rng.normal(size=3); ax /= np.linalg.norm(ax); th = rng.uniform(0.2, 2.5)
        D = expm(-1j * th * sum(ax[c] * Js[c] for c in range(3)))
        Rv = expm(-1j * th * sum(ax[c] * JVEC[c] for c in range(3))).real
        qh = rng.normal(size=3); qh /= np.linalg.norm(qh)
        inv = np.abs(np.einsum('a,b,abij->ij', Rv @ qh, Rv @ qh, W) - D @ np.einsum('a,b,abij->ij', qh, qh, W) @ D.conj().T).max()
        B, off = helicity_blocks(W, j, d, qh)
        iden = max(np.abs(4 * B[s] - B[2 * s] - 3 * B[0]).max() for s in (1, -1))
        okA &= inv < 1e-10 and off < 1e-10 and iden < 1e-10
    rowsA.append(f"spin {j} x {d} copies: {Nb.shape[1]} invariants, max |4v1 - v2 - 3v0| {iden:.1e}, helicity off-block {off:.1e}, invariance {inv:.1e}")
# positive families: group averages of PSD forms (orthogonal projection onto invariants = Haar average)
Nb, unpack, Js = invariant_basis(2, 1)
posok = True; worst = np.inf
for trial in range(20):
    M = rng.normal(size=(5, 3)) + 1j * rng.normal(size=(5, 3))       # a first-moment map q -> M q (5 = spin 2)
    Wr = np.zeros((3, 3, 5, 5), complex)
    for a in range(3):
        for b in range(3):
            Wr[a, b] = 0.5 * (np.outer(M[:, a], M[:, b].conj()) + np.outer(M[:, b], M[:, a].conj()))
    W = unpack(Nb @ (Nb.conj().T @ Wr.reshape(-1)))
    for qh in [np.array([0, 0, 1.]), rng.normal(size=3)]:
        qh = qh / np.linalg.norm(qh); B, _ = helicity_blocks(W, 2, 1, qh)
        vm = {m: B[m][0, 0].real for m in B}
        posok &= min(vm.values()) > -1e-12 and vm[1] >= vm[2] / 4 - 1e-12 and vm[-1] >= vm[-2] / 4 - 1e-12
        if vm[2] > 1e-9:
            worst = min(worst, vm[1] / vm[2])
check("A: isotropy ties the helicity sum rules: the isotropic part of any Hermitian form quadratic in q on a spin-j >= 2 multiplet is helicity-diagonal with v_m = alpha + beta m^2, so 4 v1 = v2 + 3 v0; positive families have v1 >= v2/4",
      okA and posok,
      "; ".join(rowsA) + f"; 20 positive (Haar-averaged) first-moment families: all v_m >= 0, smallest v1/v2 = {worst:.3f} (bound 0.25)")


# ---------------------------------------------------------------- spin-2 helicity tensors in Cartesian form
def spin2_helicity_tensors(qh):
    """Unit-Frobenius symmetric traceless 3x3 tensors with helicity m about qh (m = -2..2)."""
    J9 = sum(qh[c] * (np.kron(JVEC[c], np.eye(3)) - np.kron(np.eye(3), JVEC[c].T)) for c in range(3))
    basis = []
    for a in range(3):
        for b in range(a, 3):
            T = np.zeros((3, 3)); T[a, b] = T[b, a] = 1; basis.append(T.reshape(-1))
    B = np.array(basis).T
    tr = np.array([1, 0, 0, 0, 1, 0, 0, 0, 1.]); B = B - np.outer(tr, tr @ B) / 3
    Q = np.linalg.svd(B, full_matrices=False)[0][:, :5]          # orthonormal basis of the symmetric traceless tensors
    w, U = np.linalg.eigh(Q.conj().T @ J9 @ Q)
    out = {}
    for m in range(-2, 3):
        idx = np.argmin(abs(w - m)); T = (Q @ U[:, idx]).reshape(3, 3); out[m] = T / np.linalg.norm(T)
    return out


def v_of(form, k, qh):
    Ts = spin2_helicity_tensors(qh)
    return {m: form(Ts[m], k).real for m in Ts}


def eh(T, k):            # linearized Einstein-Hilbert spatial form on symmetric tensors
    kT = k @ T
    return 0.5 * (k @ k) * np.vdot(T, T) - np.vdot(kT, kT) + np.conj(k @ T @ k) * np.trace(T) - 0.5 * (k @ k) * abs(np.trace(T)) ** 2


def pretko(T, k):         # |curl A|^2 with curl on the first index
    C = np.einsum('iab,a,bj->ij', EPS, k, T); return np.vdot(C, C)


def triplet(T, k):        # three photons: rows of A as vector potentials, sum |k x a_m|^2
    C = np.einsum('iab,a,mb->mi', EPS, k, T); return np.vdot(C, C)


# ---------------------------------------------------------------- B: worked forms
rowsB = []; okB = True
dirs = [np.array([0, 0, 1.]), np.array([1, 2, 2.]) / 3, np.array([0.3, -0.5, 0.81]) / np.linalg.norm([0.3, -0.5, 0.81])]
for name, form, expect in [("Einstein-Hilbert", eh, (0.5, 0.0, -1 / 6)), ("Pretko scalar charge", pretko, (1.0, 0.5, 1 / 3)), ("photon triplet", triplet, (1.0, 0.5, 1 / 3))]:
    for qh in dirs:
        k = 0.1 * qh; vm = v_of(form, k, qh); kk = k @ k
        got = (vm[2] / kk, vm[1] / kk, vm[0] / kk)
        okB &= np.allclose(got, expect, atol=1e-12) and abs(vm[-2] - vm[2]) < 1e-14 and abs(vm[-1] - vm[1]) < 1e-14 and abs(4 * vm[1] - vm[2] - 3 * vm[0]) < 1e-14
    rowsB.append(f"{name} (v2, v1, v0)/k^2 = ({got[0]:.4f}, {got[1]:.4f}, {got[2]:.4f})")


def Xr(q):                 # landed lattice E-H symbol (2026-09-24 oscillator note), q-coordinates (h_xx,h_yy,h_zz,2h_xy,2h_yz,2h_xz)
    K = 2 * np.sin(q / 2); X = np.zeros((6, 6)); fc = {3: (0, 1), 4: (1, 2), 5: (0, 2)}
    for a in range(3):
        for b in range(3):
            if a != b:
                X[a, b] = -K[3 - a - b] ** 2
    for a in range(3):
        for f, (i, jj) in fc.items():
            if a not in (i, jj):
                X[a, f] = X[f, a] = K[i] * K[jj]
    for f, (i, jj) in fc.items():
        X[f, f] = K[3 - i - jj] ** 2 / 2
        for g, (kk, l) in fc.items():
            if g != f:
                sh = set((i, jj)) & set((kk, l)); X[f, g] = -K[(set((i, jj)) - sh).pop()] * K[(set((kk, l)) - sh).pop()] / 2
    return X


lat = []
for qh in dirs:
    q = 0.02 * qh; K = 2 * np.sin(q / 2); Kh = K / np.linalg.norm(K); Ts = spin2_helicity_tensors(Kh)
    vals = {}
    for m in (2, 1, 0):
        T = Ts[m]; w = np.array([T[0, 0], T[1, 1], T[2, 2], 2 * T[0, 1], 2 * T[1, 2], 2 * T[0, 2]])
        vals[m] = (w.conj() @ Xr(q) @ w).real / (K @ K)
    lat.append(vals)
ratio_ok = all(abs(v[1]) < 1e-12 and abs(v[0] / v[2] + 1 / 3) < 1e-9 for v in lat)
check("B: worked forms: Einstein-Hilbert (1/2, 0, -1/6) k^2 satisfies the identity only with v0 < 0; the landed lattice E-H symbol gives v1 = 0 and v0/v2 = -1/3; Pretko and the photon triplet give (1, 1/2, 1/3) k^2 with v1 >= v2/4",
      okB and ratio_ok,
      "; ".join(rowsB) + f"; landed lattice symbol at |q| = 0.02 (divided by t): v2 = {lat[0][2]:.4f}, v1 = {lat[0][1]:.1e}, v0/v2 = {lat[0][0] / lat[0][2]:.6f}")

# ---------------------------------------------------------------- C: the momentum rule removes helicity 1
def Gland(q):              # landed stencil symbol in the lattice-momentum convention: (G E)_j = sum_i i K_i E_ij (slot order xx,yy,zz,xy,yz,xz)
    K = 2 * np.sin(q / 2); G = np.zeros((3, 6), complex); comp = {(0, 0): 0, (1, 1): 1, (2, 2): 2, (0, 1): 3, (1, 0): 3, (1, 2): 4, (2, 1): 4, (0, 2): 5, (2, 0): 5}
    for j in range(3):
        for i in range(3):
            G[j, comp[(i, j)]] += 1j * K[i]
    return G


overl = 0.0
for qh in dirs + [rng.normal(size=3) for _ in range(20)]:
    qh = qh / np.linalg.norm(qh); q = 0.3 * qh; K = 2 * np.sin(q / 2); Ts = spin2_helicity_tensors(K / np.linalg.norm(K))
    Nk = null_space(Gland(q))
    for m in (1, -1):
        T = Ts[m]; e = np.array([T[0, 0], T[1, 1], T[2, 2], T[0, 1], T[1, 2], T[0, 2]])
        # E-slot vector of the tensor T (off-diagonal slot = the tensor component); overlap with ker G in the tensor metric
        Mt = np.diag([1, 1, 1, 2, 2, 2.])
        P = Nk @ np.linalg.inv(Nk.conj().T @ Mt @ Nk) @ Nk.conj().T @ Mt
        overl = max(overl, np.sqrt(abs((P @ e).conj() @ Mt @ (P @ e))))
check("C: the momentum rule removes helicity 1: ker G(k) of the landed stencil has zero overlap with the spin-2 helicity-1 tensors about the lattice momentum, so with the identity and positivity v2 = v0 = 0 at order q^2",
      overl < 1e-12,
      f"largest helicity-1 overlap with ker G over 23 directions at |q| = 0.3: {overl:.1e}; then 0 = 4 v1 = v2 + 3 v0 with v2, v0 >= 0 gives v2 = v0 = 0 (the previous probe's q^4 law, from isotropy and positivity alone)")

# ---------------------------------------------------------------- D: the incompressible construction, lattice-exact
# positions (coarse-cell units): photon l, component j at s - e_l/2 + e_j/2 (s = (1/2,1/2,1/2)); E_ii at vertices, E_ij at (e_i+e_j)/2
E3 = np.eye(3); s = np.full(3, 0.5)
pos_ok = True
for i in range(3):
    for jx in range(3):
        y = np.zeros(3) if i == jx else (E3[i] + E3[jx]) / 2
        for kx in range(3):
            for l in range(3):
                if EPS[i, kx, l] != 0:
                    p = s - E3[l] / 2 + E3[jx] / 2
                    fr = (y + E3[kx] / 2 - p) % 1.0
                    pos_ok &= bool(np.all(np.minimum(fr, 1 - fr) < 1e-9))


def L_symbol(q):           # E_ij = sum_kl eps_ikl i K_k A_lj,  A = A~ - I tr A~ / 2 ; maps 9 photon components (l,j) to 9 E_ij
    K = 2 * np.sin(q / 2); L = np.zeros((9, 9), complex)
    for i in range(3):
        for jx in range(3):
            for kx in range(3):
                for l in range(3):
                    if EPS[i, kx, l]:
                        c = EPS[i, kx, l] * 1j * K[kx]
                        L[3 * i + jx, 3 * l + jx] += c
                        if l == jx:
                            for m in range(3):
                                L[3 * i + jx, 3 * m + m] += -0.5 * c
    return L


def photon_gauss(q):       # photon l: sum_j i K_j A~_lj = 0
    K = 2 * np.sin(q / 2); P = np.zeros((3, 9), complex)
    for l in range(3):
        for jx in range(3):
            P[l, 3 * l + jx] = 1j * K[jx]
    return P


exact = 0.0
for _ in range(30):
    q = rng.uniform(-np.pi, np.pi, size=3); Np = null_space(photon_gauss(q)); Eq = L_symbol(q) @ Np
    sym = max(np.abs(Eq[3 * i + jx] - Eq[3 * jx + i]).max() for i in range(3) for jx in range(3))
    K = 2 * np.sin(q / 2)
    div = max(np.abs(sum(1j * K[i] * Eq[3 * i + jx] for i in range(3))).max() for jx in range(3))
    exact = max(exact, sym, div)
U_, Kc = 1.0, 1.0; qd = np.array([0.3, 0.5, 0.81]); qd /= np.linalg.norm(qd); ks = [0.2, 0.1, 0.05, 0.025]
Sx, Cx, M1x, speeds, invisible = [], [], [], [], []
for qq in ks:
    q = qq * qd; K = 2 * np.sin(q / 2); Np = null_space(photon_gauss(q))       # 6 transverse photon modes, all omega^2 = U K |K|^2
    om = np.sqrt(U_ * Kc * (K @ K)); speeds.append(om / np.linalg.norm(K))
    Lq = L_symbol(q) @ Np
    # E's TT channel: unit helicity-2 tensor about K
    Ts = spin2_helicity_tensors(K / np.linalg.norm(K)); T = Ts[2]
    ov = np.array([np.vdot(T.reshape(-1), Lq[:, nu]) for nu in range(Np.shape[1])])
    Sx.append(np.sum(abs(ov) ** 2) * om / (2 * U_)); Cx.append(np.sum(abs(ov) ** 2) / U_); M1x.append(np.sum(abs(ov) ** 2) * om ** 2 / (2 * U_))
    invisible.append(Np.shape[1] - np.linalg.matrix_rank(Lq, tol=1e-9 * np.linalg.norm(K)))
# the triplet's own spin-2 multiplet (symmetric traceless part of A~): helicity susceptibilities and f-sums
q = 0.02 * qd; K = 2 * np.sin(q / 2); Np = null_space(photon_gauss(q)); om = np.sqrt(U_ * Kc * (K @ K)); Tt = spin2_helicity_tensors(K / np.linalg.norm(K))
trip = {}
for m in (2, 1, 0):
    ovm = np.array([np.vdot(Tt[m].reshape(-1), Np[:, nu]) for nu in range(Np.shape[1])])
    trip[m] = (np.sum(abs(ovm) ** 2) / U_, np.sum(abs(ovm) ** 2) * om ** 2 / (2 * U_) / (K @ K))   # (chi, m1/|K|^2)
sl = lambda y: np.polyfit(np.log(ks), np.log(y), 1)[0]
okD = abs(4 * trip[1][1] - trip[2][1] - 3 * trip[0][1]) < 1e-9 and trip[1][0] > 0 and pos_ok and exact < 1e-12 and np.ptp(speeds) < 1e-12 and abs(sl(Cx) - 2) < 0.01 and abs(sl(Sx) - 3) < 0.01 and abs(sl(M1x) - 4) < 0.01 and all(v == 3 for v in invisible)
check("D: an incompressible momentum-rule tensor with a light-cone channel exists: E = curl_1(A~ - I tr A~/2) of a photon triplet is symmetric and obeys the landed rule exactly on the landed slot placement; in the Maxwell triplet its helicity-2 channel is light-cone with chi ~ q^2, S ~ q^3, m1 ~ q^4, and 3 of the 6 photon modes (helicity 1 and 0) are invisible to E",
      okD,
      f"positions consistent: {pos_ok}; symmetry and divergence residuals over 30 random zone momenta {exact:.1e}; omega/|K| = {speeds[-1]:.6f} (sqrt(UK)); exponents chi {sl(Cx):.3f}, S {sl(Sx):.3f}, m1 {sl(M1x):.3f}; photon modes invisible to E: {[int(v) for v in invisible]}; "
      f"the triplet's own spin-2 multiplet (helicity 2, 1, 0): chi*U = {[round(float(trip[m][0] * U_), 4) for m in (2, 1, 0)]}, m1/|K|^2 = {[round(float(trip[m][1]), 4) for m in (2, 1, 0)]} "
      f"(helicity-1 sum rule half the helicity-2 one, satisfying the identity; its partner channel is compressible, so gapless)")

# ---------------------------------------------------------------- E: isotropy is load-bearing (cubic counter-form)
def cubic_form(T, k, c1=1.0, a=0.6):
    kh = k / np.linalg.norm(k); kk = k @ k
    e1 = (T[0, 0] - T[1, 1]) / np.sqrt(2); e2 = (2 * T[2, 2] - T[0, 0] - T[1, 1]) / np.sqrt(6)
    t = {2: np.sqrt(2) * T[0, 1], 0: np.sqrt(2) * T[1, 2], 1: np.sqrt(2) * T[0, 2]}      # T2 labelled by the missing axis
    return kk * (a * (abs(e1) ** 2 + abs(e2) ** 2) + c1 * sum(kh[ax] ** 2 * abs(t[ax]) ** 2 for ax in range(3)))


vz = v_of(cubic_form, 0.1 * np.array([0, 0, 1.]), np.array([0, 0, 1.]))
bd = np.ones(3) / np.sqrt(3); vb = v_of(cubic_form, 0.1 * bd, bd)
psd = all(min(v_of(cubic_form, 0.1 * u / np.linalg.norm(u), u / np.linalg.norm(u)).values()) > -1e-14 for u in rng.normal(size=(200, 3)))
aniso = vb[2] / vz[2]
check("E: isotropy is load-bearing: a cubic-invariant positive first-order form has v1 = 0 and v2 > 0 along an axis (violating 4 v1 = v2 + 3 v0), but its helicity-2 stiffness then depends on direction",
      abs(vz[1]) < 1e-14 and vz[2] > 0 and psd and abs(aniso - 1) > 0.05 and abs(4 * vz[1] - vz[2] - 3 * vz[0]) > 1e-4,
      f"along z: (v2, v1, v0)/k^2 = ({vz[2] / 0.01:.3f}, {vz[1] / 0.01:.1e}, {vz[0] / 0.01:.3f}); positive in 200 random directions: {psd}; helicity-2 stiffness body diagonal / axis = {aniso:.3f}")

print("N5 resolution 1: an incompressible momentum-rule tensor with a light-cone channel exists (photon-triplet curl), so incompressibility itself is not the obstacle.")
print("N5 resolution 2: isotropy forces v_m = alpha + beta m^2 at order q^2 for any spin j >= 2 multiplet; in a ground state v1 >= v2/4, so first-order helicity-2 dynamics carries helicity-1 sum-rule weight.")
print("N5 resolution 3: Einstein-Hilbert meets the identity with v0 = -v2/3 < 0, the conformal mode; a model with a ground state cannot, unless a constraint removes that sector.")
print("N5 resolution 4: a cubic-only form escapes the identity along axes but then has direction-dependent helicity-2 stiffness.")
print("per_element: every stencil term of the construction is checked for position consistency; every worked form is evaluated on explicit helicity tensors.")
print("per_site: the construction uses vertex and face slots for E, cube-centre and link slots for the photon triplet (all four site types of the doubled lattice).")
print("per_mode: helicity blocks at random directions; photon normal modes and their overlap with E's helicity-2 channel at each momentum.")
print("per_block: exact invariant subspaces for spin 2 (one and two copies) and spin 3; 30 random zone momenta for the lattice identities.")
print("lattice_wide: checked and not executed - no qubit ground state, no phase, no helicity-1 susceptibility of a native model; the photon triplet is Gaussian (harmonic regime).")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
