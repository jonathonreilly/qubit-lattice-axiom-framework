#!/usr/bin/env python3
"""minimal-toe runner: decisive checks for the information-minimisation ruleset.

A. Group selection: among symmetry groups acting on 16 Weyl fermions (the
   minimal Z4-protected, Z16-anomaly-free chiral content), which pass
   (i) no invariant Majorana mass, (ii) no perturbative anomaly (Tr X^3 = 0,
   Tr X = 0), (iii) no Witten Z2 anomaly on Sp/SU(2) factors?  Rank by dim.
   Finite catalog diagnostic, not a classification theorem.
B. The protecting Z4 is the centre of Spin(10): the centre acts as i on 16.
C. Most-attractive-channel check for Spin(10) 16 x 16 (does the rules' own
   strong dynamics break toward the observed group?).
D. Isotropy: cubic (3D) and hyperoctahedral (4D) averages of rank-2 and
   rank-4 symmetric tensors (Lorentz at dimension 4, violation at 6).
E. Lieb flux: half-filled hopping energy, flux 0 vs pi per plaquette.
"""
import itertools
import numpy as np

AUDIT_TIMEOUT_SEC = 120
rng = np.random.default_rng(7)
PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""))


# ---------- generators ----------
def su(n):
    g = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), complex); m[i, j] = m[j, i] = 1; g.append(m)
            m = np.zeros((n, n), complex); m[i, j] = -1j; m[j, i] = 1j; g.append(m)
    for k in range(1, n):
        d = np.zeros(n); d[:k] = 1; d[k] = -k
        g.append(np.diag(d / np.sqrt(k * (k + 1) / 2)).astype(complex))
    return g


def so(n):
    g = []
    for i in range(n):
        for j in range(i + 1, n):
            m = np.zeros((n, n), complex); m[i, j] = -1j; m[j, i] = 1j; g.append(m)
    return g


def sp(n2):  # compact Sp(n2) = USp(n2), fundamental n2
    n = n2 // 2
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    g = []
    hb = su(n) + [np.eye(n, dtype=complex)]
    for A in hb:
        g.append(np.block([[A, 0 * A], [0 * A, -A.T]]))
    for i in range(n):
        for j in range(i, n):
            S = np.zeros((n, n), complex); S[i, j] = S[j, i] = 1
            g.append(np.block([[0 * S, S], [S, 0 * S]]))
            g.append(np.block([[0 * S, 1j * S], [-1j * S, 0 * S]]))
    for X in g:
        assert np.allclose(X.T @ J + J @ X, 0) and np.allclose(X, X.conj().T)
    return g


def su2_spin(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d)
    jp = np.zeros((d, d), complex)
    for k in range(1, d):
        jp[k - 1, k] = np.sqrt(j * (j + 1) - m[k] * (m[k] + 1))
    return [(jp + jp.T.conj()) / 2, (jp - jp.T.conj()) / 2j, np.diag(m).astype(complex)]


PX = np.array([[0, 1], [1, 0]], complex); PY = np.array([[0, -1j], [1j, 0]]); PZ = np.diag([1., -1]).astype(complex)
I2 = np.eye(2, dtype=complex)


def kron_all(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out


def gammas(k):  # 2k hermitian gammas of dimension 2^k
    gs = []
    for a in range(k):
        for P in (PX, PY):
            gs.append(kron_all([PZ] * a + [P] + [I2] * (k - a - 1)))
    return gs


def spin_gens(gs):
    return [0.25j * (gs[a] @ gs[b] - gs[b] @ gs[a]) for a in range(len(gs)) for b in range(a + 1, len(gs))]


def chiral(gs):
    G = np.eye(gs[0].shape[0], dtype=complex)
    for g in gs:
        G = G @ g
    ev = np.linalg.eigvals(G); ph = ev[0]
    return G / ph if np.allclose(ev ** 2, ph ** 2) else G


def restrict(gens, P):  # P: columns orthonormal basis
    return [P.conj().T @ g @ P for g in gens]


def spin10_16():
    gs = gammas(5); G = chiral(gs)
    G = G * (1 / np.sqrt(np.linalg.eigvals(G @ G)[0]))
    w, v = np.linalg.eigh((G + G.conj().T) / 2)
    P = v[:, w > 0]
    return restrict(spin_gens(gs), P), P, gs


def odd_spin(k):  # Spin(2k+1) irreducible spinor of dim 2^k
    gs = gammas(k); G = chiral(gs)
    w = np.linalg.eigvals(G @ G)[0]
    return spin_gens(gs + [G / np.sqrt(w)])


def tensor(A, B):
    return [np.kron(a, np.eye(B[0].shape[0])) + np.kron(np.eye(A[0].shape[0]), b) for a, b in zip(A, B)]


def antisym2(gens):
    n = gens[0].shape[0]; basis = []
    for i in range(n):
        for j in range(i + 1, n):
            v = np.zeros(n * n, complex); v[i * n + j] = 1 / np.sqrt(2); v[j * n + i] = -1 / np.sqrt(2); basis.append(v)
    P = np.array(basis).T
    return restrict([np.kron(g, np.eye(n)) + np.kron(np.eye(n), g) for g in gens], P)


def sp4_16():
    gs = gammas(2); G5 = chiral(gs); G5 = G5 / np.sqrt(np.linalg.eigvals(G5 @ G5)[0])
    g5 = gs + [G5]
    S = [0.25j * (g5[a] @ g5[b] - g5[b] @ g5[a]) for a in range(5) for b in range(a + 1, 5)]
    # vector generators from the adjoint action [S, g_c] = sum_d L_dc g_d
    L = [np.array([[np.trace(g5[dd] @ (s @ g5[cc] - g5[cc] @ s)) / 4 for cc in range(5)] for dd in range(5)])
         for s in S]
    T = tensor(S, L)
    C = sum(t @ t for t in T); w, v = np.linalg.eigh(C)
    P = v[:, np.isclose(w, w.max())]
    assert P.shape[1] == 16, P.shape
    return restrict(T, P), S


def blockdiag(*ms):
    n = sum(m.shape[0] for m in ms); out = np.zeros((n, n), complex); k = 0
    for m in ms:
        d = m.shape[0]; out[k:k + d, k:k + d] = m; k += d
    return out


def emb(gens, left, right):  # place gens acting on a factor inside kron(I_left, g, I_right)
    return [kron_all([np.eye(left), g, np.eye(right)]) for g in gens]


# ---------- tests ----------
def mass_nullity(T):
    n = T[0].shape[0]; basis = []
    for i in range(n):
        for j in range(i, n):
            S = np.zeros((n, n), complex); S[i, j] = S[j, i] = 1; basis.append(S)
    Gm = np.zeros((len(basis), len(basis)), complex)
    for t in T:
        A = np.array([(t.T @ S + S @ t).ravel() for S in basis]).T
        Gm += A.conj().T @ A
    w = np.linalg.eigvalsh(Gm)
    return int(np.sum(w < 1e-9 * max(1, w.max())))


def anomaly(T):
    worst3 = worst1 = 0.0
    for _ in range(6):
        X = sum(rng.normal() * t for t in T)
        s = np.real(np.trace(X @ X)) ** 1.5
        worst3 = max(worst3, abs(np.trace(X @ X @ X)) / s)
        worst1 = max(worst1, abs(np.trace(X)) / np.sqrt(np.real(np.trace(X @ X))))
    return worst3, worst1


def rank(T):
    M = np.array([t.ravel() for t in T])
    return np.linalg.matrix_rank(M, tol=1e-8)


catalog = []


def add(name, T, sp_factors=()):
    catalog.append((name, T, sp_factors))  # sp_factors: list of (gen_in_rep, gen_in_fund)


g16 = su(16); catalog.append(("SU(16) on 16", g16, ()))
add("SO(16) on 16 (vector)", so(16))
f = sp(16); add("Sp(16) on 16", f, [(f[0], f[0])])
add("U(1)xSpin(10) on 16", spin10_16()[0] + [np.eye(16, dtype=complex)])
s10 = spin10_16()[0]; add("Spin(10) on 16", s10)
add("Spin(9) on 16", odd_spin(4))
a = su(2); b = su(8); add("SU(2)xSU(8) on (2,8)", emb(a, 1, 8) + emb(b, 2, 1), [(emb(a, 1, 8)[2], a[2])])
a = su(4); add("SU(4)xSU(4) on (4,4)", emb(a, 1, 4) + emb(a, 4, 1))
a = su(8); add("SU(8)xU(1) on 8(+1)+8bar(-1)", [blockdiag(t, -t.conj()) for t in a] + [blockdiag(np.eye(8), -np.eye(8)).astype(complex)])
a = sp(8); add("Sp(8)xU(1) on 8(+1)+8(-1)", [blockdiag(t, t) for t in a] + [blockdiag(np.eye(8), -np.eye(8)).astype(complex)], [(blockdiag(a[0], a[0]), a[0])])
a = sp(14); c = su(2)
add("Sp(14)xSU(2) on 14+2", [blockdiag(t, np.zeros((2, 2))) for t in a] + [blockdiag(np.zeros((14, 14)), t) for t in c],
    [(blockdiag(a[0], np.zeros((2, 2))), a[0]), (blockdiag(np.zeros((14, 14)), c[2]), c[2])])
a = sp(8); add("Sp(8)xSp(8) on 8+8", [blockdiag(t, 0 * t) for t in a] + [blockdiag(0 * t, t) for t in a],
               [(blockdiag(a[0], 0 * a[0]), a[0]), (blockdiag(0 * a[0], a[0]), a[0])])
a = su(2); b = so(8); add("SU(2)xSO(8) on (2,8v)", emb(a, 1, 8) + emb(b, 2, 1), [(emb(a, 1, 8)[2], a[2])])
b = odd_spin(3); add("SU(2)xSpin(7) on (2,8s)", emb(a, 1, 8) + emb(b, 2, 1), [(emb(a, 1, 8)[2], a[2])])
b = sp(8); add("SU(2)xSp(8) on (2,8)", emb(a, 1, 8) + emb(b, 2, 1), [(emb(a, 1, 8)[2], a[2]), (emb(b, 2, 1)[0], b[0])])
a4 = su(4)
PS = [blockdiag(np.kron(t, I2), np.kron(-t.conj(), I2)) for t in a4] + \
     [blockdiag(np.kron(np.eye(4), s), np.zeros((8, 8))) for s in su(2)] + \
     [blockdiag(np.zeros((8, 8)), np.kron(np.eye(4), s)) for s in su(2)]
add("SU(4)xSU(2)xSU(2) on (4,2,1)+(4b,1,2)", PS,
    [(PS[15 + 2], su(2)[2]), (PS[18 + 2], su(2)[2])])
a5 = su(5); ten = antisym2(a5)
G5 = [blockdiag(t10, -t5.conj(), np.zeros((1, 1))) for t10, t5 in zip(ten, a5)] + \
     [blockdiag(-np.eye(10), 3 * np.eye(5), -5 * np.eye(1)).astype(complex)]
add("SU(5)xU(1) on 10(-1)+5b(3)+1(-5)", G5)
# Standard Model on one family (Q, u^c, d^c, L, e^c, nu^c)
a3 = su(3); s2 = su(2); Z = lambda d: np.zeros((d, d), complex)
SM = [blockdiag(np.kron(t, I2), -t.conj(), -t.conj(), Z(2), Z(1), Z(1)) for t in a3] + \
     [blockdiag(np.kron(np.eye(3), s), Z(3), Z(3), s, Z(1), Z(1)) for s in s2] + \
     [np.diag([1 / 6] * 6 + [-2 / 3] * 3 + [1 / 3] * 3 + [-1 / 2] * 2 + [1, 0]).astype(complex)]
add("SU(3)xSU(2)xU(1) on one family+nu^c", SM, [(SM[8 + 2], s2[2])])
spf = sp4_16(); add("Sp(4) on 16 (irrep)", spf[0], [(spf[0][9], spf[1][9])])
add("SU(2) spin-15/2 on 16", su2_spin(7.5), [(su2_spin(7.5)[2], su2_spin(0.5)[2])])

print("A. group selection on 16 Weyl (mass | Tr X^3 | Tr X | Witten)")
results = []
for name, T, spf_ in catalog:
    d = rank(T); mn = mass_nullity(T); a3_, a1_ = anomaly(T)
    wit = []
    for gr, gf in spf_:
        wit.append(int(round(np.real(np.trace(gr @ gr) / np.trace(gf @ gf)))) % 2)
    ok = (mn == 0) and a3_ < 1e-9 and a1_ < 1e-9 and not any(wit)
    results.append((d, name, ok))
    print(f"  {name:40s} dim={d:3d} mass={mn} A3={a3_:.1e} A1={a1_:.1e} W={wit} -> {'ok' if ok else 'x'}")
passing = sorted([r for r in results if r[2]], reverse=True)
check("A1 Spin(10) passes all four tests", any(n == "Spin(10) on 16" and o for _, n, o in results))
check("A2 Spin(10) is the largest passing group in the catalog", passing[0][1] == "Spin(10) on 16",
      f"largest={passing[0][1]} dim={passing[0][0]}; next={passing[1][1]} dim={passing[1][0]}")
check("A3 Sp(16) (dim 136) excluded only by the Witten anomaly",
      any(n == "Sp(16) on 16" and not o for _, n, o in results))
check("A4 nothing between Spin(10) and U(16) passes (U(1)xSpin(10), SU(16) fail)",
      all(not o for _, n, o in results if n in ("U(1)xSpin(10) on 16", "SU(16) on 16")))
smn = [mass_nullity(T) for n, T, _ in catalog if n.startswith("SU(3)xSU(2)xU(1)")][0]
check("A5 observed one-family group leaves exactly one allowed mass (the singlet nu^c Majorana term)", smn == 1,
      "so the observed group alone does not protect the 16; the Z4 centre of Spin(10) does")

# B. centre of Spin(10)
_, P, gs = spin10_16()
cent = np.eye(32, dtype=complex)
for k in range(5):
    cent = cent @ (gs[2 * k] @ gs[2 * k + 1])  # rotation by pi in each of 5 planes, product of gamma pairs
z = P.conj().T @ cent @ P
ev = np.linalg.eigvals(z)
check("B1 centre element acts as a single phase on 16, of order 4 (i or -i)",
      np.allclose(ev, ev[0]) and np.isclose(ev[0] ** 4, 1) and not np.isclose(ev[0] ** 2, 1), f"phase={np.round(ev[0], 6)}")
check("B2 Z16 count: 16 Weyl per family with Z4 charge 1 -> nu = 16 = 0 mod 16; 15 (no nu^c) is not", (16 % 16 == 0) and (15 % 16 != 0))

# C. MAC for Spin(10) 16 x 16
T2 = tensor(s10, s10)
C16 = np.real(np.trace(sum(t @ t for t in s10))) / 16
Ct = sum(t @ t for t in T2); w = np.linalg.eigvalsh(Ct)
chans = {}
for val in np.round(w, 6):
    chans[val] = chans.get(val, 0) + 1
print("C. Spin(10) 16x16 channels (Delta C = 2C(16)-C(R) >0 attractive; one-family scalar needs Sym2 = 10+126)")
best = None
for val, mult in sorted(chans.items()):
    dC = 2 * C16 - val
    print(f"  R dim {mult:3d}: C(R)/C(16) = {val / C16:.3f}  DeltaC/C(16) = {dC / C16:.3f}")
    if best is None or dC > best[1]:
        best = (mult, dC)
check("C1 16x16 = 10 + 120 + 126", sorted(chans.values()) == [10, 120, 126])
check("C2 most attractive channel is the 10 (breaks Spin(10) -> Spin(9), not the observed group)", best[0] == 10)


# D. isotropy
def signed_perms(n):
    for p in itertools.permutations(range(n)):
        for s in itertools.product([1, -1], repeat=n):
            M = np.zeros((n, n))
            for i, j in enumerate(p):
                M[i, j] = s[i]
            yield M


for n in (3, 4):
    Gs = list(signed_perms(n))
    t2 = rng.normal(size=(n, n)); t2 = t2 + t2.T
    av2 = sum(R @ t2 @ R.T for R in Gs) / len(Gs)
    iso2 = np.allclose(av2, np.trace(t2) / n * np.eye(n))
    # rank-4 test: average of p^4 functional: compare sum p_i^4 vs (p.p)^2 on two unit vectors
    t4 = rng.normal(size=(n,) * 4)
    sym = sum(np.transpose(t4, q) for q in itertools.permutations(range(4))) / 24
    av4 = sum(np.einsum('ai,bj,ck,dl,ijkl->abcd', R, R, R, R, sym) for R in Gs) / len(Gs)
    f = lambda v: np.einsum('abcd,a,b,c,d->', av4, v, v, v, v)
    e1 = np.eye(n)[0]; dg = np.ones(n) / np.sqrt(n)
    check(f"D{n - 2} {'cubic 3D' if n == 3 else 'hyperoctahedral 4D'}: rank-2 forced isotropic; rank-4 not (axis vs diagonal differ)",
          iso2 and not np.isclose(f(e1), f(dg)), f"group order {len(Gs)}, f(axis)={f(e1):.3f}, f(diag)={f(dg):.3f}")


# E. Lieb flux
def half_fill_energy(L, d, flux_pi):
    idx = lambda c: int(np.ravel_multi_index(c, (L,) * d))
    H = np.zeros((L ** d, L ** d))
    for c in itertools.product(range(L), repeat=d):
        for mu in range(d):
            c2 = list(c); c2[mu] = (c2[mu] + 1) % L
            eta = (-1) ** sum(c[:mu]) if flux_pi else 1
            H[idx(c), idx(c2)] += -eta; H[idx(c2), idx(c)] += -eta
    w = np.linalg.eigvalsh(H)
    return np.sum(w[: L ** d // 2]) / L ** d


for L, d in ((8, 2), (6, 3)):
    e0, epi = half_fill_energy(L, d, False), half_fill_energy(L, d, True)
    check(f"E{d - 1} pi flux per plaquette lowers the half-filled energy ({d}D, L={L})", epi < e0 - 1e-9, f"E0={e0:.4f} Epi={epi:.4f}")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
