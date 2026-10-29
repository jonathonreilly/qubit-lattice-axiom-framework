"""ns55_1 -- exact 1D interpolation arithmetic for the constant-data witness of NSL55 §1.

psi := (1 - I_j)(I_k[z_1]) on one level-k cell; quintic tents sigma_5(t) = 1 - p(t), p(t) = 10t^3 - 15t^4 + 6t^5.
Criteria: checks/ns55_1_criteria.md (written before this file). Exact Fractions only.
"""
from fractions import Fraction as Fr


def p_quintic(t):
    return 10 * t**3 - 15 * t**4 + 6 * t**5


def p_linear(t):
    return t


def psi_values(L, j, k, p):
    nk, nj = L**k, L**j
    g = [nk * p(Fr(m, nk)) for m in range(nk + 1)]          # I_k[z_1] - c_X on the level-k cell
    out = []
    for m in range(nk + 1):
        a = nj * (m // nj)
        if a == nk:                                         # m = n_k is itself a level-j root
            a = nk - nj
        s = m - a
        Ij = g[a] * (1 - p(Fr(s, nj))) + g[a + nj] * p(Fr(s, nj))
        out.append(g[m] - Ij)
    return out


CASES = [(3, 1, 2), (3, 1, 3), (3, 2, 3), (5, 1, 2), (7, 1, 2), (3, 1, 4)]
ok_all = True
for (L, j, k) in CASES:
    nk, nj = L**k, L**j
    psi = psi_values(L, j, k, p_quintic)
    # C1: zero at level-j roots
    c1 = all(psi[m] == 0 for m in range(0, nk + 1, nj))
    # C2: p(t) + p(1-t) = 1 at all sample points used
    samples = [Fr(s, nj) for s in range(nj + 1)] + [Fr(m, nk) for m in range(nk + 1)]
    c2 = all(p_quintic(t) + p_quintic(1 - t) == 1 for t in samples)
    # C3: closed form at m = 1, nonzero, negative
    closed = nk * (p_quintic(Fr(1, nk)) - p_quintic(Fr(nj, nk)) * p_quintic(Fr(1, nj)))
    c3 = (psi[1] != 0) and (psi[1] == closed) and (psi[1] < 0)
    # C4: count of nonzero values
    nnz = sum(1 for v in psi if v != 0)
    c4 = nnz >= 1
    # C5: designed-FAIL control with linear tents -> psi must vanish identically
    psi_lin = psi_values(L, j, k, p_linear)
    c5 = all(v == 0 for v in psi_lin)
    # C6: informational dimension count, T = 3
    T = 3
    N = lambda i: (T * L**(k - i))**4
    dims = (N(0) - N(j), N(0) - N(k))
    ok = c1 and c2 and c3 and c4 and c5
    ok_all = ok_all and ok
    print(f"(L,j,k)=({L},{j},{k}) n_k={nk} n_j={nj}: C1={c1} C2={c2} C3={c3} [psi(1)={psi[1]} = {float(psi[1]):.6e}] "
          f"C4: nonzero count={nnz}/{nk+1} C5(linear tents vanish)={c5}  "
          f"C6: N0-Nj={dims[0]} {'<' if dims[0] < dims[1] else '>='} N0-Nk={dims[1]}  -> {'PASS' if ok else 'FAIL'}")
print("OVERALL:", "PASS" if ok_all else "FAIL")
