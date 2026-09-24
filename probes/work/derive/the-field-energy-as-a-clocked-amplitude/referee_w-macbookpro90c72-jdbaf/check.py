#!/usr/bin/env python3
"""Referee for the field energy as a clocked amplitude, a3.

Author w-jonathonsmac4f50-j52ec (claude-opus-5-5). Own mode count on the 4^3 torus.
The 6^3 floats were not rebuilt. Filled modes are held fixed, as the attempt states.
"""
import itertools
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def laplacian():
    L = 3
    sites = list(itertools.product(range(L), repeat=3))
    idx = {s: n for n, s in enumerate(sites)}
    n = len(sites)
    bonds = []
    for s in sites:
        for a in range(3):
            t = tuple((s[d] + (1 if d == a else 0)) % L for d in range(3))
            bonds.append((idx[s], idx[t]))
    phi = [Fr(i + 2, (i % 5) + 1) for i in range(n)]
    lam = [[Fr(0)] * n for _ in range(n)]
    for x, y in bonds:
        lam[x][x] += 1
        lam[y][y] += 1
        lam[x][y] -= 1
        lam[y][x] -= 1
    left = sum((phi[x] - phi[y]) ** 2 for x, y in bonds)
    right = sum(phi[x] * lam[x][y] * phi[y] for x in range(n) for y in range(n))
    killed = all(sum(lam[x][y] for y in range(n)) == 0 for x in range(n))
    report(
        "laplacian",
        left == right and killed and len(bonds) == 3 * n,
        "on the 3^3 torus, sum (phi_x-phi_y)^2 = phi Lambda phi, and Lambda kills the constant",
    )


def four_cube():
    sin4 = [0, 1, 0, -1]
    total = sp.Integer(0)
    speed = sp.Integer(0)
    per = [sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    alive = 0
    for nk in itertools.product(range(4), repeat=3):
        s = [sin4[n] for n in nk]
        ss = sum(v * v for v in s)
        if ss == 0:
            continue
        alive += 1
        root = sp.sqrt(ss)
        speed += root
        for a in range(3):
            per[a] += sp.Integer(s[a] ** 2) / root
            total += sp.Integer(s[a] ** 2) / root
    beta = sp.simplify(-per[0] / 64)
    claimed = -(24 + 24 * sp.sqrt(2) + 8 * sp.sqrt(3)) / 192
    c = sp.simplify(-beta / 2)
    closed = (3 + 3 * sp.sqrt(2) + sp.sqrt(3)) / 48
    same = all(sp.simplify(per[a] - per[0]) == 0 for a in range(3))
    report(
        "4-cube coefficient",
        alive == 56 and same and sp.simplify(beta - claimed) == 0 and sp.simplify(c - closed) == 0
        and sp.simplify(3 * per[0] - speed) == 0,
        "56 nonzero modes, beta = -(24+24*sqrt(2)+8*sqrt(3))/192, c = (3+3*sqrt(2)+sqrt(3))/48",
    )
    return beta


def algebra(beta):
    p, q = sp.symbols("p q", positive=True)
    bond = sp.simplify(p * q - ((p ** 2 + q ** 2) / 2 - (p - q) ** 2 / 2))
    u, v = sp.symbols("u v", real=True)
    delta = sp.exp(u / 2) - sp.exp(v / 2)
    sinh = sp.exp((u + v) / 2) * 4 * sp.sinh((u - v) / 4) ** 2
    form = sp.simplify(sp.expand(delta ** 2 - sinh).rewrite(sp.exp))
    # each site meets one outgoing and one incoming bond per axis, so three axes give 3 sum w
    report(
        "bond algebra",
        bond == 0 and form == 0 and sp.simplify(-beta) > 0,
        "phi_x phi_y = (w_x+w_y)/2 - (phi_x-phi_y)^2/2, and the difference is sqrt(w_x w_y)*4*sinh^2(du/4); c=-beta/2>0",
    )


def sea(beta):
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    ix = {s: n for n, s in enumerate(sites)}
    n = len(sites)
    sig = [
        np.array([[0, 1], [1, 0]], complex),
        np.array([[0, -1j], [1j, 0]], complex),
        np.array([[1, 0], [0, -1]], complex),
    ]
    H = np.zeros((2 * n, 2 * n), complex)
    bonds = []
    for s in sites:
        for a in range(3):
            t = tuple((s[d] + (1 if d == a else 0)) % L for d in range(3))
            x, y = ix[s], ix[t]
            bonds.append((x, y))
            H[2 * x:2 * x + 2, 2 * y:2 * y + 2] += sig[a] / (2j)
            H[2 * y:2 * y + 2, 2 * x:2 * x + 2] += -sig[a] / (2j)
    ev, vec = np.linalg.eigh(H)
    neg = ev < -1e-8
    P = vec[:, neg] @ vec[:, neg].conj().T
    beta_f = complex(beta).real
    uniform = np.full(n, 1.7)
    varied = np.array([1.1 + 0.3 * ((i * 5) % 7) for i in range(n)])
    ok = int(neg.sum()) == 56
    for phi in (uniform, varied):
        D = np.kron(np.diag(phi), np.eye(2))
        Hw = D @ H @ D
        efix = float(np.real(np.trace(P @ Hw)))
        bonds_sum = sum(phi[x] * phi[y] for x, y in bonds)
        evw = np.linalg.eigvalsh(Hw)
        eopt = float(evw[evw < -1e-8].sum())
        ok &= abs(efix - beta_f * bonds_sum) < 1e-8
        ok &= eopt <= efix + 1e-8
    # uniform rates: the two energies agree
    D = np.kron(np.diag(uniform), np.eye(2))
    Hw = D @ H @ D
    efix = float(np.real(np.trace(P @ Hw)))
    eopt = float(np.linalg.eigvalsh(Hw)[np.linalg.eigvalsh(Hw) < -1e-8].sum())
    ok &= abs(efix - eopt) < 1e-7
    report(
        "variational sea",
        ok,
        "on 4^3, E_fix equals beta times the bond sum for a constant and a varying field, and the re-optimised sea lies at or below it",
    )


def line_and_cube():
    # int_0^{2pi} |sin k| dk = 4, so the mean is 2/pi
    k = sp.symbols("k", real=True)
    area = sp.integrate(sp.sin(k), (k, 0, sp.pi)) + sp.integrate(-sp.sin(k), (k, sp.pi, 2 * sp.pi))
    N = 32
    kk = 2 * np.pi * np.arange(N) / N
    beta = -np.abs(np.sin(kk)).mean()
    # one random positive field on the ring
    phi = 1 + 0.2 * np.cos(kk)
    S = np.zeros((N, N), complex)
    for x in range(N):
        S[x, (x + 1) % N] += 1 / (2j)
        S[(x + 1) % N, x] += -1 / (2j)
    H = np.kron(S, np.array([[0.0, 1.0], [1.0, 0.0]]))
    ev, vec = np.linalg.eigh(H)
    P = vec[:, ev < -1e-8] @ vec[:, ev < -1e-8].conj().T
    D = np.kron(np.diag(phi), np.eye(2))
    efix = float(np.real(np.trace(P @ (D @ H @ D))))
    target = beta * sum(phi[x] * phi[(x + 1) % N] for x in range(N))
    M = 48
    g = (np.arange(M) + 0.5) * 2 * np.pi / M
    s2 = np.sin(g)[:, None, None] ** 2 + np.sin(g)[None, :, None] ** 2 + np.sin(g)[None, None, :] ** 2
    integral = float(np.sqrt(s2).mean())
    report(
        "line and cube",
        area == 4 and abs(efix - target) < 1e-8 and abs(beta + 2 / np.pi) < 5e-3 and 1.19 < integral < 1.20,
        f"the ring mean tends to 2/pi and the clocked sum matches; midpoint I={integral:.5f}, c=I/6={integral/6:.5f}",
    )


def main():
    laplacian()
    beta = four_cube()
    algebra(beta)
    sea(beta)
    line_and_cube()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - the filled lower band of the rate-independent walk, held fixed and then clocked, "
        "has energy beta * sum_bonds phi_x phi_y for every rate field. "
        "On the 4^3 torus c=-beta/2=(3+3*sqrt(2)+sqrt(3))/48. "
        "The identity rewrites this as 3 beta sum w + c sum (phi_x-phi_y)^2. "
        "The sea that re-optimises lies at or below that energy."
    )
    print(
        "SUMMARY: confirmed the Laplacian identity, the 4^3 closed form, the sinh rewriting, the 4^3 variational comparison, "
        "and the ring limit 2/pi. The 6^3 sample and the quoted gamma were not rebuilt; "
        "a 48^3 midpoint gives I in (1.19, 1.20). Holding the modes and dropping the volume term are the attempt's supplied clauses."
    )


if __name__ == "__main__":
    main()
