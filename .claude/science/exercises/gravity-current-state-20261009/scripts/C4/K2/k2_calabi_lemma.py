"""K2 lemma check (lattice Calabi / Killing-cokernel lemma).

Lemma: let y_mu = 1 - exp(-i q_mu) (lattice backward-difference symbols). A local vector R_nu(y)
(polynomial in y, coefficients in any ring) is a divergence  R_nu = sum_mu y_mu T_mu,nu  of a
SYMMETRIC local T  iff  R(0) = 0 and the antisymmetric part of dR/dy at 0 vanishes
(i.e. R is orthogonal to the 10 affine Killing fields).
Degree 1 is the symmetric-matrix statement; for degree d >= 2 the map
   div: Sym^2 (x) P_{d-1} -> V (x) P_d,   T -> (sum_mu y_mu T_mu,nu)
must be onto. Checked here by exact rank for d = 2..6 in 4 variables (and 3 variables).
Localisation from polynomials in y to Laurent polynomials in z = 1 - y keeps exactness.
"""
import itertools, sympy as sp

def monos(nvar, d):
    return [m for m in itertools.product(range(d + 1), repeat=nvar) if sum(m) == d]

for nvar in (3, 4):
    for d in range(1, 7):
        rows_m = monos(nvar, d); cols_m = monos(nvar, d - 1)
        rid = {(nu, m): i for i, (nu, m) in enumerate(itertools.product(range(nvar), rows_m))}
        sym = [(a, b) for a in range(nvar) for b in range(a, nvar)]
        cols = []
        for (a, b) in sym:
            for m in cols_m:
                col = {}
                # T_ab = T_ba = monomial m ; contributes to R_b via y_a and to R_a via y_b
                for (mu, nu) in ([(a, b), (b, a)] if a != b else [(a, a)]):
                    mm = list(m); mm[mu] += 1
                    key = rid[(nu, tuple(mm))]
                    col[key] = col.get(key, 0) + 1
                cols.append(col)
        M = sp.zeros(len(rid), len(cols))
        for j, col in enumerate(cols):
            for i, v in col.items():
                M[i, j] = v
        r = M.rank()
        target = len(rid) - (nvar * (nvar - 1) // 2 if d == 1 else 0)
        print(f"nvar={nvar} degree d={d}: dim V(x)P_d = {len(rid)}, rank(div) = {r}, expected = {target}",
              "OK" if r == target else "MISMATCH")
