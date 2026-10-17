"""(3) every proper rotation with every admissible eps maps the signed group of
each uniform sector to itself (exact, including signs).  Extras:
  - non-uniform sectors are permuted (s_{ab} -> s_{R(ab)})
  - non-admissible eps send B_v -> -B_{Rv} (group not preserved)
  - improper elements (O_h) with det-condition eps
  - explicit on-site 8x8 unitary: Clifford, not a qubit permutation
"""
import sys, itertools, time
import numpy as np
from mpd_core import *

ok_all = True


def rep(name, ok):
    global ok_all
    ok_all &= ok
    print(("PASS " if ok else "FAIL ") + name, flush=True)


def orient_image(M, a, b):
    dp = dir_perm(M)
    ia, ib = dp[a] % 3, dp[b] % 3
    key = tuple(sorted((ia, ib)))
    for o in ORIENTS:
        if tuple(sorted(o)) == key:
            return o


def check(L, sectors, elems, eps_mode, full=True):
    lat = Lattice(L)
    tabs = {}
    gens = {}
    for sec in all_sectors():
        lab = tuple(sec[o] for o in ORIENTS)
        g = lat.generators(sec)
        T = Tableau(lat.n)
        for m in g:
            T.insert(lat.to_pauli(m))
        tabs[lab] = T
        gens[lab] = g
    results = {}
    for sec in sectors:
        lab = tuple(sec[o] for o in ORIENTS)
        g = gens[lab]
        if not full:  # by translation invariance: generators at one site suffice
            g = [m for m in g if m[1][0][0] == (0, 0, 0)]
        for M in elems:
            # target sector
            tgt = {orient_image(M, a, b): sec[(a, b)] for (a, b) in ORIENTS}
            tlab = tuple(tgt[o] for o in ORIENTS)
            dp = dir_perm(M)
            s = perm_sign(dp)
            if eps_mode == "admissible":
                epss = admissible_eps(M)
            else:
                epss = [e for e in itertools.product([1, -1], repeat=6) if np.prod(e) != s]
            for eps in epss:
                into_same = all(tabs[lab].sign_of(act_pauli_via_mono(lat, M, eps, m)) == 1 for m in g)
                into_tgt = all(tabs[tlab].sign_of(act_pauli_via_mono(lat, M, eps, m)) == 1 for m in g)
                results.setdefault((lab, tlab), []).append((into_same, into_tgt))
    return results


t0 = time.time()
R = rotations()
assert len(R) == 24
assert all(len(admissible_eps(M)) == 32 for M in R)
uni = [s for s in all_sectors() if len(set(s.values())) == 1]
non = [s for s in all_sectors() if len(set(s.values())) > 1]

res = check(4, uni, R, "admissible", full=True)
n = sum(len(v) for v in res.values())
rep("L=4: all 24 rotations x 32 admissible eps preserve signed groups of both uniform sectors (%d cases, all generators)" % n,
    n == 2 * 24 * 32 and all(a for v in res.values() for (a, b) in v))

res = check(6, uni, R, "admissible", full=True)
n = sum(len(v) for v in res.values())
rep("L=6: same (%d cases, all generators)" % n,
    n == 2 * 24 * 32 and all(a for v in res.values() for (a, b) in v))

res = check(4, non, R, "admissible", full=True)
ok = all(b for v in res.values() for (a, b) in v)
inv = sum(1 for v in res.values() for (a, b) in v if a)
rep("L=4: non-uniform sectors map to the orientation-permuted sector (always); cases left invariant: %d" % inv, ok)

res = check(4, uni, R, "bad", full=True)
rep("L=4: non-admissible eps (prod eps != sign) never preserve the group",
    not any(a for v in res.values() for (a, b) in v))

I = improper()
assert len(I) == 24
res = check(4, uni, I, "admissible", full=True)
cnt = sum(1 for v in res.values() for (a, b) in v if a)
print("INFO L=4 improper elements (O_h \\ O) with det-condition eps: %d of %d cases preserve the uniform signed groups"
      % (cnt, sum(len(v) for v in res.values())))

# B_v -> B_{Rv} exactly
lat = Lattice(4)
ok = True
for M in R:
    for eps in admissible_eps(M):
        for v in [(0, 0, 0), (1, 2, 3)]:
            img = act_pauli_via_mono(lat, M, eps, lat.B_mono(v))
            ok &= img == lat.to_pauli(lat.B_mono(apply(M, v)))
rep("B_v -> +B_{Rv} exactly for all admissible eps", ok)

# ---- explicit on-site unitary ------------------------------------------------
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex); I2 = np.eye(2)
def k3(a, b, c):
    return np.kron(np.kron(a, b), c)
G = [k3(X, I2, I2), k3(Y, I2, I2), k3(Z, X, I2), k3(Z, Y, I2), k3(Z, Z, X), k3(Z, Z, Y)]
paulis1 = {"I": I2, "X": X, "Y": Y, "Z": Z}
P3 = [(a + b + c, k3(paulis1[a], paulis1[b], paulis1[c])) for a in "IXYZ" for b in "IXYZ" for c in "IXYZ"]


def mono_mat(S, which):
    out = np.eye(8, dtype=complex)
    for d in S:
        out = out @ which[d]
    return out


def onsite_unitary(M, eps):
    dp = dir_perm(M)
    img = [eps[d] * G[dp[d]] for d in range(6)]
    rng = np.random.default_rng(1)
    A = rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))
    acc = np.zeros((8, 8), complex)
    for r in range(7):
        for S in itertools.combinations(range(6), r):
            P = mono_mat(S, G); Q = mono_mat(S, img)
            acc += Q @ A @ P.conj().T
    U = acc / np.sqrt(np.trace(acc.conj().T @ acc).real / 8)
    return U


def is_clifford(U):
    for name, P in P3:
        if name == "III":
            continue
        Q = U @ P @ U.conj().T
        hit = False
        for _, P2 in P3:
            c = np.trace(P2.conj().T @ Q) / 8
            if abs(abs(c) - 1) < 1e-9:
                hit = True
        if not hit:
            return False
    return True


def entangling(U):
    # local (product of single-qubit) Clifford maps each weight-1 Pauli to weight-1
    for name, P in P3:
        if sum(ch != "I" for ch in name) != 1:
            continue
        Q = U @ P @ U.conj().T
        for n2, P2 in P3:
            if abs(abs(np.trace(P2.conj().T @ Q) / 8) - 1) < 1e-9:
                if sum(ch != "I" for ch in n2) != 1:
                    return True
    return False


ok = True
ent = 0
qperm_impl = 0
for M in R:
    for eps in admissible_eps(M):
        U = onsite_unitary(M, eps)
        dp = dir_perm(M)
        ok &= np.allclose(U @ U.conj().T, np.eye(8))
        ok &= all(np.allclose(U @ G[d] @ U.conj().T, eps[d] * G[dp[d]]) for d in range(6))
        ok &= is_clifford(U)
        ent += entangling(U)
    # does any bare permutation of the three site qubits (times any phase/sign
    # pattern) implement gamma_d -> +- gamma_{Rd}?
    for qp in itertools.permutations(range(3)):
        Pm = np.zeros((8, 8))
        for b in range(8):
            bits = [(b >> (2 - i)) & 1 for i in range(3)]
            nb = [0, 0, 0]
            for i in range(3):
                nb[qp[i]] = bits[i]
            Pm[nb[0] * 4 + nb[1] * 2 + nb[2], b] = 1
        if all(any(np.allclose(Pm @ G[d] @ Pm.T, s * G[dp[d]]) for s in (1, -1)) for d in range(6)):
            qperm_impl += 1
            print("   bare qubit permutation", qp, "implements rotation", M)
rep("on-site unitaries exist, are 3-qubit Cliffords implementing gamma_d -> eps gamma_Rd (24 x 32)", ok)
print("INFO entangling on-site Cliffords: %d of %d" % (ent, 24 * 32))
print("INFO rotations implementable by a bare permutation of the 3 site qubits: %d (identity only expected)" % qperm_impl)
print("time %.1fs" % (time.time() - t0))
print("OVERALL", "PASS" if ok_all else "FAIL")
