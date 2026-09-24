#!/usr/bin/env python3
"""Referee for the-two-record-ledger-under-exclusion a2.

Author w-macbookpro90c72-j3fae (claude-opus-5-5). Own matrix arithmetic.
"""
from fractions import Fraction as Fr
fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def build_A(n, phi, periodic):
    """Real antisymmetric matrix of phi sigma_3 D phi. Index 2x+c."""
    d = 2 * n
    A = [[Fr(0) for _ in range(d)] for _ in range(d)]
    for x in range(n):
        for step, sgn_step in ((1, 1), (-1, -1)):
            y = x + step
            if periodic:
                y %= n
            elif not 0 <= y < n:
                continue
            bond = phi[x] * phi[y]
            for c, s in ((0, 1), (1, -1)):
                A[2 * x + c][2 * y + c] += Fr(s, 2) * bond * sgn_step
    return A


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def apply_A(A, vec):
    d = len(vec)
    return [sum(A[r][c] * vec[c] for c in range(d)) for r in range(d)]


def one_density(A, u, v):
    """Re psi† H psi with H = -i A: u·Av - v·Au, split by site."""
    Au, Av = apply_A(A, u), apply_A(A, v)
    n = len(u) // 2
    nrm = dot(u, u) + dot(v, v)
    out = []
    for x in range(n):
        s = Fr(0)
        for c in range(2):
            i = 2 * x + c
            s += u[i] * Av[i] - v[i] * Au[i]
        out.append(s / nrm)
    return out


def gram(u1, v1, u2, v2):
    nrm = dot(u1, u1) + dot(v1, v1)
    cr = (dot(u1, u2) + dot(v1, v2)) / nrm
    ci = (dot(u1, v2) - dot(v1, u2)) / nrm
    u = [a - (cr * p - ci * q) for a, p, q in zip(u2, u1, v1)]
    v = [b - (cr * q + ci * p) for b, p, q in zip(v2, u1, v1)]
    return u, v


def pair_energy(n, phi, u1, v1, u2, v2, sign):
    """Compressed pair energy and per-site density. sign = -1 antisymmetric, +1 symmetric."""
    A = build_A(n, phi, periodic=True)
    d = 2 * n
    # complex amplitudes as (re, im)
    p1 = list(zip(u1, v1))
    p2 = list(zip(u2, v2))
    # W[(i,j)] = p1_i p2_j + sign p2_i p1_j, different sites only
    W = {}
    for i in range(d):
        for j in range(d):
            if i // 2 == j // 2:
                continue
            # (a+ib)(c+id) = ac-bd + i(ad+bc)
            a, b = p1[i]
            c, e = p2[j]
            re = a * c - b * e
            im = a * e + b * c
            a2, b2 = p2[i]
            c2, e2 = p1[j]
            re += sign * (a2 * c2 - b2 * e2)
            im += sign * (a2 * e2 + b2 * c2)
            if re or im:
                W[(i, j)] = (re, im)
    nrm = sum(re * re + im * im for re, im in W.values())

    def hop(slot):
        """Apply H = -i A to one tensor factor. H(u+iv) = Av - i Au, so
        re' = Av component of the input, im' = -Au component."""
        out = {}
        for (i, j), (re, im) in W.items():
            src = i if slot == 0 else j
            for k in range(d):
                if A[k][src] == 0:
                    continue
                # input amplitude re+ i im at src, H gives (A im) + i (-A re) at k? 
                # H(re + i im) = A*(im) - i A*(re), coefficient of basis k is A[k][src] * im  in real
                # and -A[k][src] * re in imag.
                coef = A[k][src]
                hre = coef * im
                him = -coef * re
                key = (k, j) if slot == 0 else (i, k)
                pr, pi = out.get(key, (Fr(0), Fr(0)))
                out[key] = (pr + hre, pi + him)
        return out

    h0, h1 = hop(0), hop(1)
    dens = []
    for x in range(n):
        acc = Fr(0)
        for (i, j), (re, im) in W.items():
            if i // 2 == x and (i, j) in h0:
                hr, hi = h0[(i, j)]
                acc += re * hr + im * hi
            if j // 2 == x and (i, j) in h1:
                hr, hi = h1[(i, j)]
                acc += re * hr + im * hi
        dens.append(acc / nrm)
    return sum(dens), dens


def ledger():
    n = 6
    phi = [1 + Fr((3 * x * x + x) % 5, 7) for x in range(n)]
    u1 = [Fr((x * x + 1) % 4, 3) if c == 0 else Fr((2 * x + 1) % 5, 4) for x in range(n) for c in range(2)]
    v1 = [Fr(x % 3, 2) if c == 0 else Fr((x * x) % 3 - 1, 3) for x in range(n) for c in range(2)]
    u2r = [Fr((x + 2) % 4, 5) if c == 0 else Fr(1, 2) for x in range(n) for c in range(2)]
    v2r = [Fr((x * x + x) % 3, 2) if c == 0 else Fr((3 * x) % 4 - 2, 3) for x in range(n) for c in range(2)]
    u2, v2 = gram(u1, v1, u2r, v2r)
    # orthogonality
    orth = dot(u1, u2) + dot(v1, v2) == 0 and dot(u1, v2) - dot(v1, u2) == 0
    A = build_A(n, phi, True)
    e1 = one_density(A, u1, v1)
    e2 = one_density(A, u2, v2)
    E_free = sum(e1) + sum(e2)
    E_hc, dens = pair_energy(n, phi, u1, v1, u2, v2, -1)
    _, dens_s = pair_energy(n, phi, u1, v1, u2, v2, +1)
    ndiff = sum(1 for a, b, c in zip(dens, e1, e2) if a != b + c)
    ratio = E_free / E_hc
    claimed_free = Fr(16169964, 134909593)
    claimed_hc = Fr(12349656, 122046701)
    claimed_ratio = Fr(3356276805253, 2833481402466)
    # E is affine in each phi_x (each bond product contains phi_x once), so the derivative is an exact difference.
    deriv_ok = True
    for x in range(n):
        bumped = phi[:]
        bumped[x] = phi[x] + 1
        Eb = pair_energy(n, bumped, u1, v1, u2, v2, -1)[0]
        deriv = (phi[x] / 2) * (Eb - E_hc)
        deriv_ok &= deriv == dens[x]
    weight = sum(dens) == E_hc and sum(dens_s) == pair_energy(n, phi, u1, v1, u2, v2, +1)[0]
    report(
        "ledger",
        orth and weight and deriv_ok and E_free == claimed_free and E_hc == claimed_hc and ratio == claimed_ratio and ndiff == 6,
        f"E_hc={E_hc}, E_free={E_free}, ratio={ratio}, sites where density differs from e1+e2: {ndiff}",
    )


def translation():
    n = 6
    phi = [Fr(2) ** x for x in range(n)]
    A = build_A(n, phi, periodic=False)
    d = 2 * n

    def col(i, j):
        out = {}
        for k in range(d):
            if A[k][i] != 0 and k // 2 != j // 2:
                # H = -i A contributes the real matrix factor used consistently on both sides
                out[(k, j)] = out.get((k, j), Fr(0)) + A[k][i]
            if A[k][j] != 0 and k // 2 != i // 2:
                out[(i, k)] = out.get((i, k), Fr(0)) + A[k][j]
        return out

    checked = 0
    good = True
    for i in range(d):
        for j in range(d):
            if i // 2 == j // 2 or not (1 <= i // 2 <= n - 3 and 1 <= j // 2 <= n - 3):
                continue
            left = col(i + 2, j + 2)
            right = {(a + 2, b + 2): 4 * v for (a, b), v in col(i, j).items()}
            good &= set(left) == set(right) and all(left[k] == right[k] for k in left)
            checked += 1
    report(
        "translation",
        good and checked == 24,
        f"open chain w=4^x, P H P T = 4 T P H P on {checked} interior columns",
    )


def main():
    ledger()
    translation()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - under exclusion the pair's compressed energy is both its ledger source and "
        "what a uniform gradient pulls, so S/E = 1. On block 78's ring the additive source e1+e2 instead "
        "gives S/E = 3356276805253/2833481402466."
    )
    print(
        "SUMMARY: confirmed E_hc=12349656/122046701, E_free=16169964/134909593, the density differing from "
        "e1+e2 at all 6 sites, and the factor-4 translation identity on 24 columns. "
        "Block 54's step from that identity to the force was used as cited."
    )


if __name__ == "__main__":
    main()
