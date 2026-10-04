"""Coordinator check of A49's basis counts and its compass-staggered eigenstate, from scratch (no a49lib).
(a) Covariant two-spin terms per bond class under the exact soldered turns: a term M_ab s^a_x s^b_{x+d} is kept by
    the bond's stabiliser (g d = d: M -> R M R^T; g d = -d: M -> R M^T R^T).  Count invariants (expect NN 3, face
    diagonal 4, axis-2 3, body diagonal 3) and check A49's named tensors lie in the invariant space.
(b) Dual-frame Neel state along (1,1,1)/sqrt3 is an exact zero-energy eigenstate of the dual image of the covariant
    NN rule J = K, i.e. sum over a-bonds of (3 s^a s^a - s.s), on 2x2x2 and 4x2x2 tori."""
import itertools
import numpy as np

O = [np.array(M) for M in {tuple(map(tuple, s[:, None] * np.eye(3, dtype=int)[list(p)]))
     for p in itertools.permutations(range(3)) for s in map(np.array, itertools.product((1, -1), repeat=3))}
     if round(np.linalg.det(np.array(M))) == 1]
eps = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    eps[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])
def invariant_space(d):
    d = np.array(d)
    P = np.zeros((9, 9)); n = 0
    for R in O:
        Rd = R @ d
        if np.array_equal(Rd, d) or np.array_equal(Rd, -d):
            T = np.zeros((9, 9))
            for k in range(9):
                M = np.zeros(9); M[k] = 1; M = M.reshape(3, 3)
                T[:, k] = (R @ (M if np.array_equal(Rd, d) else M.T) @ R.T).flatten()
            P += T; n += 1
    return P / n
dh = lambda v: np.array(v) / np.linalg.norm(v)
named = {"NN (0,0,1)": ((0, 0, 1), {"J": np.eye(3), "K": np.outer([0, 0, 1], [0, 0, 1]), "D": eps @ np.array([0, 0, 1.])}),
         "face diag (1,1,0)": ((1, 1, 0), {"J": np.eye(3), "Kn": np.outer([0, 0, 1], [0, 0, 1]),
                                           "Kd": np.outer(dh((1, 1, 0)), dh((1, 1, 0))), "D": eps @ dh((1, 1, 0))}),
         "axis-2 (0,0,2)": ((0, 0, 2), {"J": np.eye(3), "K": np.outer([0, 0, 1], [0, 0, 1]), "D": eps @ np.array([0, 0, 1.])}),
         "body diag (1,1,1)": ((1, 1, 1), {"J": np.eye(3), "Kd": np.outer(dh((1, 1, 1)), dh((1, 1, 1))), "D": eps @ dh((1, 1, 1))})}
expect = {"NN (0,0,1)": 3, "face diag (1,1,0)": 4, "axis-2 (0,0,2)": 3, "body diag (1,1,1)": 3}
ok = True
for name, (d, tensors) in named.items():
    P = invariant_space(d)
    rank = int(round(np.trace(P)))
    inside = all(np.allclose(P @ M.flatten(), M.flatten()) for M in tensors.values())
    span = np.linalg.matrix_rank(np.array([M.flatten() for M in tensors.values()]))
    good = rank == expect[name] and inside and span == rank
    ok &= good
    print(f"(a) {name}: invariants {rank} (A49 {expect[name]}), named {list(tensors)} inside {inside}, span {span} {'OK' if good else 'FAIL'}")

s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1]).astype(complex)]
def op(N, i, A, j, B):
    mats = [np.eye(2, dtype=complex)] * N
    mats[i] = A; mats[j] = B
    out = mats[0]
    for m in mats[1:]: out = np.kron(out, m)
    return out
n = np.ones(3) / np.sqrt(3)
w, v = np.linalg.eigh(sum(n[a] * s[a] for a in range(3)))
up, dn = v[:, 1], v[:, 0]                                  # spin along +n and -n
for dims in ((2, 2, 2), (4, 2, 2)):
    sites = list(itertools.product(*map(range, dims)))
    sid = {x: i for i, x in enumerate(sites)}
    N = len(sites)
    psi = np.array([1.0 + 0j])
    for x in sites:
        psi = np.kron(psi, up if sum(x) % 2 == 0 else dn)
    Hpsi = np.zeros_like(psi)
    for x in sites:
        for a in range(3):
            y = list(x); y[a] = (y[a] + 1) % dims[a]; y = sid[tuple(y)]
            i = sid[x]
            if i == y: continue
            # apply 3 s^a s^a - s.s to psi without building the full matrix for N = 16: use reshapes
            def apply(A, B, vec):
                t = vec.reshape([2] * N)
                t = np.tensordot(A, t, axes=([1], [i])); t = np.moveaxis(t, 0, i)
                t = np.tensordot(B, t, axes=([1], [y])); t = np.moveaxis(t, 0, y)
                return t.reshape(-1)
            Hpsi += 3 * apply(s[a], s[a], psi) - sum(apply(s[b], s[b], psi) for b in range(3))
    res = np.linalg.norm(Hpsi)
    good = res < 1e-10
    ok &= good
    print(f"(b) {dims} torus: |H psi| = {res:.1e} (exact zero-energy eigenstate) {'OK' if good else 'FAIL'}")
print("TOTAL:", "PASS" if ok else "FAIL")
