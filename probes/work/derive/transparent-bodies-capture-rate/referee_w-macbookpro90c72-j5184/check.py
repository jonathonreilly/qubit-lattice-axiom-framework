#!/usr/bin/env python3
"""Referee for transparent-bodies capture rate, a1.

Author w-macbookpro90c72-j357b (claude-opus-5-5). Own enumeration and counts.
The porous collisionless quadratures are the attempt's notes, not re-run here.
The executed Q values are the task's, not a new simulator run.
"""
import itertools
import math
from fractions import Fraction as Fr

import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def capture(body, w):
    """Forward walk. Mass that steps onto the body is captured and removed."""
    body = set(body)
    reach = max(sum(p) for p in body)
    alive = {(0, 0, 0): Fr(1)}
    caught = Fr(0)
    for _ in range(reach):
        nxt = {}
        for pos, mass in alive.items():
            for axis, weight in enumerate(w):
                step = list(pos)
                step[axis] += 1
                step = tuple(step)
                moved = mass * weight
                if step in body:
                    caught += moved
                else:
                    nxt[step] = nxt.get(step, Fr(0)) + moved
        alive = nxt
    return caught


def capture_sequences(body, w):
    body = set(body)
    reach = max(sum(p) for p in body)
    caught = Fr(0)
    for length in range(1, reach + 1):
        for seq in itertools.product(range(3), repeat=length):
            pos = [0, 0, 0]
            prob = Fr(1)
            landed = False
            for axis in seq:
                pos[axis] += 1
                prob *= w[axis]
                if tuple(pos) in body:
                    landed = True
                    break
            if landed and sum(pos) == length:
                caught += prob
    return caught


def one_record():
    bodies = [
        {(1, 0, 0), (1, 1, 0), (2, 1, 1), (0, 2, 1)},
        {(1, 1, 0), (0, 1, 1), (1, 0, 1)},
        {(2, 0, 0), (1, 1, 1), (0, 0, 3), (2, 2, 0)},
    ]
    laws = [
        (Fr(1, 2), Fr(1, 3), Fr(1, 6)),
        (Fr(1, 3), Fr(1, 3), Fr(1, 3)),
        (Fr(3, 5), Fr(1, 5), Fr(1, 5)),
    ]
    ok = True
    first = None
    for body in bodies:
        for law in laws:
            left = capture(body, law)
            right = capture_sequences(body, law)
            ok &= left == right
            if first is None:
                first = left
    report(
        "one record",
        ok and first == Fr(7, 9),
        "enumeration matches the forward transport on 3 bodies x 3 step laws; the first is 7/9",
    )


def ball_sites(radius):
    return [
        (x, y, z)
        for x, y, z in itertools.product(range(-radius, radius + 1), repeat=3)
        if x * x + y * y + z * z <= radius * radius
    ]


def exposed_faces(sites):
    occupied = set(sites)
    axes = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
    return sum(
        (x + a, y + b, z + c) not in occupied
        for x, y, z in sites
        for a, b, c in axes
    )


def internal_bonds(sites):
    occupied = set(sites)
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    return sum(
        (x + a, y + b, z + c) in occupied
        for x, y, z in sites
        for a, b, c in axes
    )


def faces():
    rho, z = sp.symbols("rho z", real=True)
    face_anti = z ** 2 / 4
    l1_anti = 3 * z ** 2 / 4
    face = sp.simplify(face_anti.subs(z, 1) - face_anti.subs(z, 0))
    # <|z|> = 2 * int_0^1 z/2 dz = 1/2, so <|s|_1> = 3/2. Antiderivative on [0,1] doubled.
    mean_abs = sp.simplify(2 * (z ** 2 / 4).subs(z, 1))
    l1 = sp.simplify(3 * mean_abs)
    rate = sp.simplify(6 * rho / (4 * sp.sqrt(3)) - rho * sp.sqrt(3) / 2)
    counts = {r: (len(ball_sites(r)), exposed_faces(ball_sites(r))) for r in (2, 3, 4, 5)}
    ok = (
        sp.diff(face_anti, z) == z / 2
        and face == sp.Rational(1, 4)
        and mean_abs == sp.Rational(1, 2)
        and l1 == sp.Rational(3, 2)
        and rate == 0
        and [counts[r][0] for r in (2, 3, 4, 5)] == [33, 123, 257, 515]
        and [counts[r][1] for r in (2, 3, 4, 5)] == [78, 174, 294, 486]
    )
    # l1_anti is the one-sided piece used only to keep the 3/2 derivation next to the derivative.
    ok &= sp.diff(l1_anti, z) == sp.Rational(3, 2) * z
    report(
        "faces",
        ok,
        "face moment 1/4, <|s|_1>=3/2, q1=rho*sqrt(3)/2, balls 33/123/257/515 sites and 78/174/294/486 faces",
    )
    return counts


def chords():
    ell, radius, mu, tau = sp.symbols("ell R mu tau", positive=True)
    dens_anti = ell ** 2 / (4 * radius ** 2)
    mean_anti = ell ** 3 / (6 * radius ** 2)
    norm = sp.simplify(dens_anti.subs(ell, 2 * radius) - dens_anti.subs(ell, 0))
    mean = sp.simplify(mean_anti.subs(ell, 2 * radius))
    nstar = sp.simplify(sp.Rational(4, 3) * sp.pi * radius ** 3 / (2 * radius))
    anti = -sp.exp(-mu * ell) * (ell / mu + 1 / mu ** 2)
    deriv = sp.simplify(sp.diff(anti, ell) - ell * sp.exp(-mu * ell))
    survival = sp.simplify((anti.subs(ell, 2 * radius) - anti.subs(ell, 0)) / (2 * radius ** 2))
    closed = (1 - (1 + 2 * mu * radius) * sp.exp(-2 * mu * radius)) / (2 * mu ** 2 * radius ** 2)
    mu_of = 3 * tau / (4 * radius)
    absorbed = sp.simplify(1 - survival.subs(mu, mu_of))
    ratio = sp.series(absorbed / tau, tau, 0, 2).removeO()
    at5 = sp.simplify(nstar.subs(radius, 5) - 50 * sp.pi / 3)
    report(
        "chords",
        deriv == 0
        and sp.simplify(survival - closed) == 0
        and norm == 1
        and mean == 4 * radius / 3
        and nstar == 2 * sp.pi * radius ** 2 / 3
        and at5 == 0
        and sp.simplify(ratio - (1 - sp.Rational(9, 16) * tau)) == 0,
        "chord density integrates to 1 with mean 4R/3; N*=(2*pi/3)R^2 = 50*pi/3 at R=5; Q/(N q1)=1-(9/16)tau+O(tau^2)",
    )


def numbers(counts):
    rho = 0.29
    faces_n = [counts[r][1] for r in (2, 3, 4, 5)]
    pred = [rho * f / (4 * math.sqrt(3)) for f in faces_n]
    shown = [round(p + 1e-12, 2) for p in pred]
    executed = [3.2, 7.8, 13.2, 21.8]
    rel = [abs(p - e) / e for p, e in zip(pred, executed)]
    ratios = [e / r ** 2 for e, r in zip(executed, (2, 3, 4, 5))]
    # One D fitted to the R=5 executed value makes Q proportional to R.
    predicted_r2 = Fr(218, 10) * Fr(2, 5)
    q1 = rho * math.sqrt(3) / 2
    bonds = internal_bonds(ball_sites(5))
    def local(n):
        exposed = 6 * n - 2 * bonds * n * (n - 1) / (515 * 514)
        return rho * exposed / (4 * math.sqrt(3))

    thin = [round(n * q1 + 1e-12, 2) for n in (51, 164)]
    short = 1 - 9.4 / (51 * q1)
    ok = (
        shown == [3.26, 7.28, 12.31, 20.34]
        and max(rel) < 0.07
        and pred[0] > executed[0]
        and all(p < e for p, e in zip(pred[1:], executed[1:]))
        and predicted_r2 == Fr(218, 25)
        and all(0.80 <= q <= 0.88 for q in ratios)
        and bonds == 1302
        and round(local(51) + 1e-12, 2) == 11.76
        and round(local(164) + 1e-12, 2) == 30.18
        and thin == [12.81, 41.19]
        and 0.26 < short < 0.28
        and abs(q1 - 0.2511) < 5e-5
    )
    report(
        "numbers",
        ok,
        "Q_loc rounds to 3.26, 7.28, 12.31, 20.34 (within 7% of the task values); "
        f"R-scaling from 21.8 gives {predicted_r2} at R=2; porous additive rates 12.81 and 41.19; "
        f"expected local rates 11.76 and 30.18 from {bonds} internal bonds",
    )


def main():
    one_record()
    counts = faces()
    chords()
    numbers(counts)
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - one streaming record is captured with the forward-walk probability "
        "(7/9 on the first body). A site's rate is rho*sqrt(3)/2, six faces times rho/(4*sqrt(3)). "
        "Lattice balls of radius 2..5 have 78, 174, 294, 486 exposed faces, so at rho=0.29 the local "
        "kinetic rates are 3.26, 7.28, 12.31, 20.34 against the task's 3.2, 7.8, 13.2, 21.8. "
        "A single diffusivity fitted at R=5 predicts 8.72 at R=2. The chord model has mean 4R/3, "
        "optical depth 2*R*phi, and N*=(2*pi/3)*R^2, with screening 1-(9/16)*tau."
    )
    print(
        "SUMMARY: confirmed the enumeration, the face identity, the ball counts, the chord expansion, "
        "and the failure of one R-scaling on the task's solid-ball numbers. "
        "The porous collisionless brackets were not re-integrated. The inflow correction was not derived."
    )


if __name__ == "__main__":
    main()
