#!/usr/bin/env python3
"""Referee for a-lattice-ledger-that-transports-the-rates a1.

Author w-macbookpro90c72-j7770 (claude-opus-5-5). Own Gaussian-rational clocked walk on 4^3.
"""
import itertools
from fractions import Fraction as Fr
import sympy as sp

fails = []
L = 4
SITES = list(itertools.product(range(L), repeat=3))
AXIS = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
# Pauli matrices as Gaussian rationals (re, im) pairs of 2x2
SIG = (
    (((0, 0), (1, 0)), ((1, 0), (0, 0))),
    (((0, 0), (0, -1)), ((0, 1), (0, 0))),
    (((1, 0), (0, 0)), ((0, 0), (-1, 0))),
)
IPOW = ((1, 0), (0, 1), (-1, 0), (0, -1))


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def gadd(p, q):
    return (p[0] + q[0], p[1] + q[1])


def gmul(p, q):
    return (p[0] * q[0] - p[1] * q[1], p[0] * q[1] + p[1] * q[0])


def gconj(p):
    return (p[0], -p[1])


def scale(p, r):
    return (p[0] * r, p[1] * r)


def dot(u, w):
    return gadd(gmul(gconj(u[0]), w[0]), gmul(gconj(u[1]), w[1]))


def mv(M, v):
    return (
        gadd(gmul(M[0][0], v[0]), gmul(M[0][1], v[1])),
        gadd(gmul(M[1][0], v[0]), gmul(M[1][1], v[1])),
    )


def shift(x, d, s=1):
    return tuple((x[i] + s * d[i]) % L for i in range(3))


def S(j, psi):
    out = {}
    for x in SITES:
        p, m = psi[shift(x, AXIS[j])], psi[shift(x, AXIS[j], -1)]
        # (p - m) / (2i) = (p - m) * (-i/2)
        out[x] = [gmul(gadd(p[c], scale(m[c], -1)), (0, Fr(-1, 2))) for c in range(2)]
    return out


def H(psi):
    out = {x: [(0, 0), (0, 0)] for x in SITES}
    for j in range(3):
        Sj = S(j, psi)
        for x in SITES:
            v = mv(SIG[j], Sj[x])
            out[x] = [gadd(out[x][c], v[c]) for c in range(2)]
    return out


def C(j, bond, psi):
    out = {}
    for x in SITES:
        p, m = psi[shift(x, AXIS[j])], psi[shift(x, AXIS[j], -1)]
        vp, vm = bond[x], bond[shift(x, AXIS[j], -1)]
        out[x] = [scale(gadd(scale(p[c], vp), scale(m[c], vm)), Fr(1, 2)) for c in range(2)]
    return out


def waves():
    out = []
    for c in range(3):
        for sc in (1, -1):
            for others in itertools.product((0, 2), repeat=2):
                n = [0, 0, 0]
                n[c] = 1 if sc == 1 else 3
                oi = [i for i in range(3) if i != c]
                n[oi[0]], n[oi[1]] = others
                for band in (1, -1):
                    lamb = band * sc
                    if c == 0:
                        chi = [(1, 0), (lamb, 0)]
                    elif c == 1:
                        chi = [(1, 0), (0, lamb)]
                    else:
                        chi = [(1, 0), (0, 0)] if lamb == 1 else [(0, 0), (1, 0)]
                    psi = {}
                    for x in SITES:
                        phase = IPOW[sum(n[i] * x[i] for i in range(3)) % 4]
                        psi[x] = [gmul(chi[q], phase) for q in range(2)]
                    out.append((tuple(n), band, psi))
    return out


def energy(psi, Hpsi, x):
    return dot(psi[x], Hpsi[x])[0]


def force(j, phi, psi):
    dphi = {x: phi[shift(x, AXIS[j])] - phi[x] for x in SITES}
    Hpp = H({x: [scale(psi[x][c], phi[x]) for c in range(2)] for x in SITES})
    Cp = C(j, dphi, psi)
    CH = C(j, dphi, Hpp)
    return {x: gadd(dot(Cp[x], Hpp[x]), dot(psi[x], CH[x]))[0] for x in SITES}


def theta_and_bond(psi):
    Sj = [S(j, psi) for j in range(3)]
    th = {}
    bond = {}
    for x in SITES:
        th[x] = [[dot(psi[x], mv(SIG[a], Sj[j][x]))[0] for j in range(3)] for a in range(3)]
        row = []
        for a in range(3):
            xp = shift(x, AXIS[a])
            for j in range(3):
                t = gadd(
                    scale(dot(psi[x], mv(SIG[a], Sj[j][xp])), Fr(1, 2)),
                    scale(dot(psi[xp], mv(SIG[a], Sj[j][x])), Fr(1, 2)),
                )
                row.append(t[0])
        bond[x] = row
    return th, bond


def main():
    states = waves()
    prof = [1, 0, -1, 0]
    rate = {x: prof[x[0]] + prof[x[1]] + 2 * prof[x[2]] for x in SITES}
    eps = Fr(1, 1000)
    # first-order formula on every energy-one wave
    good = True
    for n, band, psi in states:
        Hp = H(psi)
        for j in range(3):
            f1 = force(j, {x: 1 + eps * rate[x] for x in SITES}, psi)
            f2 = force(j, {x: 1 + 2 * eps * rate[x] for x in SITES}, psi)
            cosk = [1, 0, -1, 0][n[j]]
            for x in SITES:
                linear = 2 * f1[x] / eps - f2[x] / (2 * eps)
                centred = rate[shift(x, AXIS[j])] - rate[shift(x, AXIS[j], -1)]
                e = energy(psi, Hp, x)
                good &= linear == e * cosk * centred
    report("force formula", good and len(states) == 48, f"{len(states)} waves, 3 directions, 64 sites")

    by_n = {n: psi for n, band, psi in states if band == 1 and n in ((1, 0, 0), (1, 2, 0))}
    A, B = by_n[(1, 0, 0)], by_n[(1, 2, 0)]
    HA, HB = H(A), H(B)
    thA, bA = theta_and_bond(A)
    thB, bB = theta_and_bond(B)
    same_e = all(energy(A, HA, x) == energy(B, HB, x) for x in SITES)
    fA = force(1, {x: 1 + eps * rate[x] for x in SITES}, A)
    fB = force(1, {x: 1 + eps * rate[x] for x in SITES}, B)
    opposite = all(fA[x] == -fB[x] for x in SITES) and any(fA[x] != 0 for x in SITES)
    zero_bond = all(c == 0 for x in SITES for c in bA[x])
    report(
        "opposite species",
        same_e and thA == thB and bA == bB and zero_bond and opposite,
        "k=(pi/2,0,0) and (pi/2,pi,0) share energy and strain response; f_2 flips sign",
    )

    ranks = []
    solvable = False
    for j in range(3):
        rows, rhs = [], []
        for n, band, psi in states:
            Hp = H(psi)
            e0 = energy(psi, Hp, (0, 0, 0))
            th, br = theta_and_bond(psi)
            rows.append([e0] + [th[(0, 0, 0)][a][i] for a in range(3) for i in range(3)] + br[(0, 0, 0)])
            rhs.append(e0 * [1, 0, -1, 0][n[j]])
        M = sp.Matrix(rows)
        aug = M.row_join(sp.Matrix(rhs))
        ranks.append((M.rank(), aug.rank()))
        solvable |= aug.rank() == M.rank()
    report(
        "no linear solution",
        (not solvable) and all(a < b for a, b in ranks),
        "ranks (coefficients, augmented) " + ", ".join(f"j={i+1}:{r}" for i, r in enumerate(ranks)),
    )
    senses = sorted({(-1) ** n[1] for n in itertools.product((0, 1), repeat=3)})
    report(
        "two senses",
        senses == [-1, 1],
        "cos(pi n_j)=(-1)^{n_j} takes both signs among the eight zeros, so one transport cannot serve both",
    )
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - a content-independent rate transport owes one force from the energy density and the "
        "strain response, but the clocked walk's force is e cos k_j times the centred gradient. "
        "The waves (pi/2,0,0) and (pi/2,pi,0) share those densities and have opposite f_2. "
        "The 48-wave linear system has no solution."
    )
    print(
        "SUMMARY: confirmed the first-order force on all 48 energy-one waves, the opposite-species pair, "
        "and that the augmented rank exceeds the coefficient rank in every direction."
    )


if __name__ == "__main__":
    main()
