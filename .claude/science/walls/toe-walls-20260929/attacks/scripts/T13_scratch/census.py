"""Test 2: commutant census of local translation-invariant charges on an infinite qubit chain.

Operators: O = sum_s c_s sum_x T^x(s), s a canonical Pauli string (first and last
site non-identity), length <= r.  [H,O] is computed exactly in the Pauli algebra
(all output coefficients are imaginary, we store the real factor).  Nullity of
c -> [H,O] counts independent local conserved charges of range <= r (identity excluded).
"""
import itertools
import sys
import numpy as np
import scipy.sparse as sp

# single-site product: (a,b) -> (phase exponent k of i^k, result)
def sprod(a, b):
    if a == 0:
        return 0, b
    if b == 0:
        return 0, a
    if a == b:
        return 0, 0
    c = 6 - a - b
    if (a, b) in ((1, 2), (2, 3), (3, 1)):
        return 1, c
    return 3, c


def canon(chars, off):
    """trim identities; return (tuple, offset) or None for identity."""
    n = len(chars)
    lo = 0
    while lo < n and chars[lo] == 0:
        lo += 1
    if lo == n:
        return None
    hi = n - 1
    while chars[hi] == 0:
        hi -= 1
    return tuple(chars[lo:hi + 1]), off + lo


def commutator_terms(h, s, j):
    """[h placed at site j, s placed at site 0] -> (canonical string, real factor) or None.
    result = 2 * i^k * R with k odd; returns factor 2*(+1 if k==1 else -1) meaning coefficient = i * factor."""
    lo = min(j, 0)
    hi = max(j + len(h), len(s))
    n = hi - lo
    k = 0
    anti = 0
    res = [0] * n
    for idx in range(n):
        site = lo + idx
        a = h[site - j] if 0 <= site - j < len(h) else 0
        b = s[site] if 0 <= site < len(s) else 0
        ph, r = sprod(a, b)
        # anticommute at this site?
        if a != 0 and b != 0 and a != b:
            anti += 1
        k += ph
        res[idx] = r
    if anti % 2 == 0:
        return None
    k %= 4
    fac = 2 if k == 1 else -2
    cs = canon(res, lo)
    if cs is None:
        raise RuntimeError("commutator produced identity?")
    return cs[0], fac


def basis(r):
    B = []
    for n in range(1, r + 1):
        if n == 1:
            for a in (1, 2, 3):
                B.append((a,))
        else:
            for first in (1, 2, 3):
                for last in (1, 2, 3):
                    for mid in itertools.product(range(4), repeat=n - 2):
                        B.append((first,) + mid + (last,))
    return B


def build(Hterms, r):
    B = basis(r)
    col = {s: i for i, s in enumerate(B)}
    rows = {}
    data, ri, ci = [], [], []
    for s, ic in col.items():
        acc = {}
        for coef, h in Hterms:
            for j in range(-(len(h) - 1), len(s)):
                out = commutator_terms(h, s, j)
                if out is None:
                    continue
                t, fac = out
                acc[t] = acc.get(t, 0.0) + coef * fac
        for t, v in acc.items():
            if abs(v) < 1e-14:
                continue
            if t not in rows:
                rows[t] = len(rows)
            data.append(v); ri.append(rows[t]); ci.append(ic)
    M = sp.csr_matrix((data, (ri, ci)), shape=(len(rows), len(B)))
    return M, B


def nullity(M, tol=1e-9):
    G = (M.T @ M).toarray()
    ev = np.linalg.eigvalsh(G)
    scale = max(ev.max(), 1.0)
    return int((ev < tol * scale).sum()), ev


def vec_in_null(M, B, Hterms):
    v = np.zeros(len(B))
    idx = {s: i for i, s in enumerate(B)}
    for coef, h in Hterms:
        v[idx[h]] += coef
    return np.linalg.norm(M @ v)


models = {
    "tilted Ising (generic)": [(1.0, (3, 3)), (0.9045, (1,)), (0.8090, (3,))],
    "critical Ising (free fermion)": [(1.0, (3, 3)), (1.0, (1,))],
    "XX chain (free fermion, U(1))": [(1.0, (1, 1)), (1.0, (2, 2))],
    "XXZ chain (integrable, Delta=0.5)": [(1.0, (1, 1)), (1.0, (2, 2)), (0.5, (3, 3))],
    "XYZ chain (integrable, Baxter; J=1,0.7,0.3)": [(1.0, (1, 1)), (0.7, (2, 2)), (0.3, (3, 3))],
}

# ---- validation against dense matrices on a ring
def validate():
    L = 8
    I2 = np.eye(2); PX = np.array([[0, 1], [1, 0]], complex)
    PY = np.array([[0, -1j], [1j, 0]]); PZ = np.diag([1., -1.]).astype(complex)
    P = [I2, PX, PY, PZ]

    def string_op(s, x):
        mats = [I2] * L
        for i, c in enumerate(s):
            mats[(x + i) % L] = P[c]
        out = mats[0]
        for m in mats[1:]:
            out = np.kron(out, m)
        return out

    def ti(s):
        return sum(string_op(s, x) for x in range(L))

    Hterms = models["tilted Ising (generic)"]
    Hm = sum(c * ti(h) for c, h in Hterms)
    rng = np.random.default_rng(0)
    Bs = basis(3)
    cvec = {Bs[i]: rng.normal() for i in rng.choice(len(Bs), 6, replace=False)}
    Om = sum(c * ti(s) for s, c in cvec.items())
    dense = Hm @ Om - Om @ Hm
    # string-algebra version
    acc = {}
    for coef, h in Hterms:
        for s, c in cvec.items():
            for j in range(-(len(h) - 1), len(s)):
                out = commutator_terms(h, s, j)
                if out is None:
                    continue
                t, fac = out
                acc[t] = acc.get(t, 0.0) + coef * c * fac
    alg = sum(1j * v * ti(t) for t, v in acc.items())
    return np.linalg.norm(dense - alg) / max(np.linalg.norm(dense), 1e-12)


if __name__ == "__main__":
    print("validation (relative residual string algebra vs dense ring L=8):", validate())
    rmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    for name, Ht in models.items():
        row = []
        for r in range(2, rmax + 1):
            M, B = build(Ht, r)
            nl, ev = nullity(M)
            chk = vec_in_null(M, B, Ht)
            row.append((r, len(B), nl, chk))
        print(name)
        for r, nb, nl, chk in row:
            print(f"   r={r} basis={nb:5d} nullity={nl:3d}  |[H,H]|={chk:.1e}")
