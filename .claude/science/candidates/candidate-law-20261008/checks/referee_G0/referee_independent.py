"""Independent small checks for G0; intentionally imports none of the worker code."""

import itertools
import numpy as np


DIRS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
I = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1, -1]).astype(complex)
SP = np.array([[0, 0], [1, 0]], dtype=complex)
SM = SP.T
S = np.diag([1, 1j]).astype(complex)
PAULI = {"I": I, "X": X, "Y": Y, "Z": Z}


def proportional(a, b, tol=1e-10):
    af = a.ravel()
    bf = b.ravel()
    if max(np.max(np.abs(af)), np.max(np.abs(bf))) < tol:
        return True
    j = int(np.argmax(np.abs(bf)))
    if abs(bf[j]) < tol:
        return False
    return np.max(np.abs(af - af[j] / bf[j] * bf)) < tol


def rotations():
    ans = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            r = np.zeros((3, 3), dtype=int)
            for row, (column, sign) in enumerate(zip(perm, signs)):
                r[row, column] = sign
            if round(np.linalg.det(r)) == 1:
                ans.append(r)
    return ans


ROTS = rotations()
DPERM = [[DIRS.index(tuple(r @ np.array(d))) for d in DIRS] for r in ROTS]
STAB_X = [g for g, p in enumerate(DPERM) if p[0] == 0]
REPS = [next(g for g, p in enumerate(DPERM) if p[0] == d) for d in range(6)]


def covariant_pattern(pattern, stabilizer):
    for g in stabilizer:
        if not any(
            all(
                proportional(
                    np.linalg.matrix_power(S, k)
                    @ pattern[d]
                    @ np.linalg.matrix_power(S.conj().T, k),
                    pattern[DPERM[g][d]],
                )
                for d in range(6)
            )
            for k in range(4)
        ):
            return False
    return True


def anticommutes(a, b):
    return np.allclose(a @ b, -(b @ a))


def transported_edge_factors(pattern):
    """Return factor[hop][edge-site] in the worker's orbit gauge."""
    factor = [[None] * 6 for _ in range(6)]
    for hop in range(6):
        for site in range(6):
            inv = ROTS[REPS[site]].T
            relative = DIRS.index(tuple(inv @ np.array(DIRS[hop])))
            factor[hop][site] = pattern[relative]
    return factor


def pair_signs(edge_factors):
    signs = np.zeros((6, 6), dtype=int)
    for a in range(6):
        for b in range(a + 1, 6):
            signs[a, b] = signs[b, a] = sum(
                anticommutes(edge_factors[a][q], edge_factors[b][q]) for q in range(6)
            ) % 2
    return signs


def triangle_sign(signs, triple):
    a, b, c = triple
    return (-1) ** ((signs[a, b] + signs[b, c] + signs[c, a]) % 2)


def class_a_check():
    accepted = []
    for own in ("X", "Y"):
        for rest in itertools.product("IXYZ", repeat=5):
            pattern = tuple(PAULI[x] for x in (own,) + rest)
            if covariant_pattern(pattern, STAB_X):
                accepted.append((own + "|" + "".join(rest), pattern))
    hist = {}
    for _, pattern in accepted:
        signs = pair_signs(transported_edge_factors(pattern))
        values = tuple(triangle_sign(signs, tr) for tr in itertools.combinations(range(6), 3))
        hist[values] = hist.get(values, 0) + 1
    print("independent Class A accepted:", len(accepted), "/ 2048")
    print("independent Class A outcome multiplicities:", [(set(k), v) for k, v in hist.items()])


def c_nonscalar_counterexample():
    # c4's printed example: own edge X, phase S on its four perpendicular hops;
    # all far-corner spectator factors are identity and endpoints are SP/SM.
    p_l = (X, I, S, S, S, S)
    edge = transported_edge_factors(p_l)
    factors = []
    for hop in range(6):
        row = [SM]
        row += [SP if site == hop else I for site in range(6)]
        row += edge[hop]
        factors.append(row)

    seen = {"T": set(), "corner": set()}
    for triple in itertools.combinations(range(6), 3):
        a, b, c = triple
        local = []
        for q in range(13):
            aa, bb, cc = factors[a][q], factors[b][q], factors[c][q]
            local.append(cc.conj().T @ aa @ bb.conj().T @ cc @ aa.conj().T @ bb)
        fixed = {0: 1, 1 + a: 1, 1 + b: 0, 1 + c: 0}
        free = [q for q in range(13) if q not in fixed]
        vals = set()
        for bits in itertools.product((0, 1), repeat=len(free)):
            state = dict(fixed)
            state.update(zip(free, bits))
            amp = 1 + 0j
            returns = True
            for q, hq in enumerate(local):
                bit = state[q]
                column = hq[:, bit]
                if abs(column[1 - bit]) > 1e-10 or abs(column[bit]) < 1e-10:
                    returns = False
                    break
                amp *= column[bit]
            if returns:
                vals.add(complex(np.round(amp, 9)))
        kind = "corner" if len({d // 2 for d in triple}) == 3 else "T"
        seen[kind].update(vals)
    print("independent c4 nonscalar support:", {k: sorted(v, key=str) for k, v in seen.items()})


if __name__ == "__main__":
    class_a_check()
    c_nonscalar_counterexample()
