#!/usr/bin/env python3
"""Finite certificates for the companion supplied D3Q27 linear theorem.

Standard library only. No network, empirical data, off-repository files or
mutable cache. Exact rational checks certify the collision and corrector
identities. Floating-point matrix exponentials are a supplementary finite-mode
check; they do not prove the analytic PDE estimate or a nonlinear limit.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, permutations, product
from math import ceil, log2, sqrt
import sys

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md",
    "docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md",
)
PASS = 0
FAIL = 0


def check(label, condition, detail):
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}: {detail}", flush=True)
    else:
        FAIL += 1
        print(f"FAIL {label}: {detail}", flush=True)


def zero(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def scale(a, factor):
    return [[factor * x for x in row] for row in a]


def add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    cols = transpose(b)
    return [[sum(x * y for x, y in zip(row, col) if x and y)
             for col in cols] for row in a]


def rowscale(a, factors):
    return [[factor * x for x in row] for factor, row in zip(factors, a)]


def columns(*cols):
    return transpose(cols)


def inverse(a):
    n = len(a)
    work = [list(row) + erow for row, erow in zip(a, eye(n))]
    for k in range(n):
        pivot = next(i for i in range(k, n) if work[i][k])
        work[k], work[pivot] = work[pivot], work[k]
        factor = work[k][k]
        work[k] = [x / factor for x in work[k]]
        for i in range(n):
            if i != k and work[i][k]:
                factor = work[i][k]
                work[i] = [x - factor * y for x, y in zip(work[i], work[k])]
    return [row[n:] for row in work]


def iszero(a):
    return all(x == 0 for row in a for x in row)


def polyadd(a, b):
    out = [F(0)] * max(len(a), len(b))
    for src in (a, b):
        for i, x in enumerate(src):
            out[i] += x
    return out


def polymul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def mpolyadd(a, b):
    n, m = len(a[0]), len(a[0][0])
    out = [zero(n, m) for _ in range(max(len(a), len(b)))]
    for src in (a, b):
        for i, x in enumerate(src):
            out[i] = add(out[i], x)
    return out


def mpolymul(a, b):
    out = [zero(len(a[0]), len(b[0][0])) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] = add(out[i + j], mul(x, y))
    return out


def pair_key(velocities, pair):
    i, j = pair
    return tuple(velocities[i][a] + velocities[j][a] for a in range(3)) + (
        sum(x * x for x in velocities[i] + velocities[j]),
    )


def axial(velocities, pair1, pair2):
    def desc(pair):
        i, j = pair
        delta = [velocities[i][a] - velocities[j][a] for a in range(3)]
        axes = [a for a in range(3) if abs(delta[a]) == 2]
        if len(axes) != 1 or sum(x * x for x in delta) != 4:
            return None
        return tuple(F(velocities[i][a] + velocities[j][a], 2) for a in range(3)), axes[0]
    a, b = desc(pair1), desc(pair2)
    return bool(a and b and a[0] == b[0] and a[1] != b[1]
                and a[0][a[1]] == a[0][b[1]] == 0)


def main():
    print("Supplied D3Q27 dissipative approximation: exact rational certificates", flush=True)
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}", flush=True)
    velocities = list(product((-1, 0, 1), repeat=3))
    n = len(velocities)
    energy = [sum(x * x for x in v) for v in velocities]
    weights = [F(2, 3) ** (3 - e) * F(1, 6) ** e for e in energy]
    groups = defaultdict(list)
    for pair in combinations_with_replacement(range(n), 2):
        groups[pair_key(velocities, pair)].append(pair)
    reactions = [(p, q) for key in sorted(groups) for p, q in combinations(groups[key], 2)]
    special = [axial(velocities, p, q) for p, q in reactions]
    independent = set()
    for i, j, k, l in combinations(range(n), 4):
        for p, q in (((i, j), (k, l)), ((i, k), (j, l)), ((i, l), (j, k))):
            if pair_key(velocities, p) == pair_key(velocities, q):
                independent.add(tuple(sorted((p, q))))
    check("complete-network", len(reactions) == 288 and sum(special) == 9
          and set(reactions) == independent and sum(weights) == 1,
          "27 velocities; two exhaustive enumerations agree on 288 reversible reactions; nine axial exchanges")
    z = [[F(1), *map(F, v), F(e)] for v, e in zip(velocities, energy)]
    check("conservation-and-balance", all(
        len(set(p + q)) == 4
        and all(z[p[0]][a] + z[p[1]][a] == z[q[0]][a] + z[q[1]][a] for a in range(5))
        and weights[p[0]] * weights[p[1]] == weights[q[0]] * weights[q[1]]
        for p, q in reactions), "all five conserved moments and 288 detailed-balance monomials checked exactly")

    def bmatrix(alpha, omit=None):
        c = zero(n, n)
        for rid, (((i, j), (k, l)), is_axial) in enumerate(zip(reactions, special)):
            if rid == omit:
                continue
            factor = (alpha if is_axial else 1) * weights[i] * weights[j]
            support = ((i, -1), (j, -1), (k, 1), (l, 1))
            for a, sa in support:
                for b, sb in support:
                    c[a][b] += factor * sa * sb
        return rowscale(c, [1 / w for w in weights])

    def bapply(phi, alpha):
        # Separate direct derivative of the quadratic forward/reverse flux.
        out = [F(0) for _ in velocities]
        for ((i, j), (k, l)), is_axial in zip(reactions, special):
            flux = (alpha if is_axial else 1) * weights[i] * weights[j] * (phi[i] + phi[j] - phi[k] - phi[l])
            out[i] += flux / weights[i]
            out[j] += flux / weights[j]
            out[k] -= flux / weights[k]
            out[l] -= flux / weights[l]
        return out

    def inner(a, b):
        return sum(w * x * y for w, x, y in zip(weights, a, b))

    b0, b = bmatrix(F(0)), bmatrix(F(1))
    weighted_zt = transpose(rowscale(z, weights))
    gram = mul(weighted_zt, z)
    coord = mul(inverse(gram), weighted_zt)
    p = mul(z, coord)
    q = sub(eye(n), p)
    r = sub(inverse(add(b, p)), p)
    trace_r = sum(r[i][i] for i in range(n))
    check("exact-kernel-and-inverse", mul(p, p) == p and iszero(mul(b, p))
          and mul(b, r) == q and mul(r, b) == q and iszero(mul(p, r))
          and rowscale(r, weights) == transpose(rowscale(r, weights)),
          "rank 22 certified by BR=RB=I−P and rank(P)=5; R weighted self-adjoint")
    check("explicit-gap-bound", trace_r == F(6224911145567, 509693499350),
          f"tr R_1={trace_r}; ||R_kappa|| <= tr R_1 / min(kappa) at theta=1/3")

    index = {v: i for i, v in enumerate(velocities)}
    marked = {reaction: flag for reaction, flag in zip(reactions, special)}
    covariance = True
    for perm, signs in product(permutations(range(3)), product((-1, 1), repeat=3)):
        mapping = [index[tuple(signs[a] * v[perm[a]] for a in range(3))] for v in velocities]
        covariance &= all(weights[i] == weights[mapping[i]] for i in range(n))
        for reaction, flag in marked.items():
            target = tuple(sorted(tuple(sorted(mapping[i] for i in pair)) for pair in reaction))
            covariance &= marked.get(target) == flag
    check("complete-cubic-covariance", covariance,
          "all 48 signed coordinate permutations preserve M, every collision and the two rate classes")

    ss = [[F(1, 9), F(1, 27)], [F(1, 27), F(1, 27)]]
    sh = [[F(4, 27), F(4, 81)], [F(4, 81), F(8, 243)]]
    block_ok, entries = True, 0
    for alpha in (F(0), F(1)):
        for a, bb in combinations(range(3), 2):
            c = next(i for i in range(3) if i not in (a, bb))
            for kind in ("diag", "off"):
                first = [F(v[a] ** 2 - v[bb] ** 2, 2) if kind == "diag" else F(v[a] * v[bb]) for v in velocities]
                phi = columns(first, [x * v[c] ** 2 for x, v in zip(first, velocities)])
                d = ([[F(4, 9) * (alpha + 1), F(-5, 18)], [F(2, 3) - alpha / 3, alpha / 9 + F(35, 18)]]
                     if kind == "diag" else [[F(16, 9), F(-2, 9)], [F(1, 18), F(5, 2)]])
                block_ok &= mul(transpose(phi), rowscale(phi, weights)) == ss
                block_ok &= columns(*(bapply(col, alpha) for col in transpose(phi))) == mul(phi, d)
                block_ok &= mul(b0 if alpha == 0 else b, phi) == mul(phi, d)
                entries += 54
        for a in range(3):
            bb, c = [i for i in range(3) if i != a]
            phi = columns([F(v[a]) * (e - F(5, 3)) for v, e in zip(velocities, energy)],
                          [F(v[a]) * (v[bb] ** 2 * v[c] ** 2 - F(1, 9)) for v in velocities])
            d = [[F(79, 54), F(-2, 9)], [F(5, 9), F(5, 2)]]
            block_ok &= mul(transpose(phi), rowscale(phi, weights)) == sh
            block_ok &= columns(*(bapply(col, alpha) for col in transpose(phi))) == mul(phi, d)
            block_ok &= mul(b0 if alpha == 0 else b, phi) == mul(phi, d)
            entries += 54
    check("all-alpha-stress-and-heat-blocks", block_ok,
          f"{entries} exact entries at both affine coefficients, all axes; independent flux and matrix implementations")
    hd00, hd01, hd11 = [F(2, 27), F(1, 27)], [F(10, 243), F(1, 243)], [F(15, 243), F(1, 243)]
    determinant = polyadd(polymul(hd00, hd11), [-x for x in polymul(hd01, hd01)])
    numerator = polyadd(polyadd([F(1, 81) * x for x in hd11], [-F(2, 243) * x for x in hd01]),
                        [F(1, 729) * x for x in hd00])
    ho = [[F(97, 486), F(11, 162)], [F(11, 162), F(41, 486)]]
    hh = [[F(178, 729), F(22, 243)], [F(22, 243), F(52, 729)]]
    bs, bh = [[F(1, 9)], [F(1, 27)]], [[F(4, 27)], [F(4, 81)]]
    check("symbolic-response-certificate", determinant == [F(170, 59049), F(133, 59049), F(8, 59049)]
          and numerator == [F(31, 59049), F(4, 59049)]
          and mul(mul(transpose(bs), inverse(ho)), bs)[0][0] == F(67, 1083)
          and mul(mul(transpose(bh), inverse(hh)), bh)[0][0] == F(40, 441),
          "mu_D=(4a+31)/(8a²+133a+170); mu_O=67/1083; chi=40/441 for every a>0")
    difference_numerator = polyadd([F(1083 * 31), F(1083 * 4)],
                                   [-F(67 * x) for x in (170, 133, 8)])
    root = (-4579 + 3 * sqrt(7614177)) / 1072
    check("isotropic-rate-identity", difference_numerator == [F(22183), F(-4579), F(-536)]
          and 536 + 4579 - 22183 < 0 < 536 * 16 + 4579 * 4 - 22183,
          f"unique positive zero of 536a²+4579a−22183; a*={root:.15g} lies in (1,4); supplied rate, no empirical selection")

    stress = [[F(v[0] ** 2 - v[1] ** 2, 2) for v in velocities],
              [F(v[0] ** 2 + v[1] ** 2 - 2 * v[2] ** 2, 2) for v in velocities]]
    stress += [[F(v[a] * v[bb]) for v in velocities] for a, bb in combinations(range(3), 2)]
    heat = [[F(v[a]) * (e - F(5, 3)) for v, e in zip(velocities, energy)] for a in range(3)]
    sources = columns(*(stress + heat))
    response = mul(transpose(sources), rowscale(mul(r, sources), weights))
    expected = zero(8, 8)
    diagonal = [F(35, 311), F(105, 311)] + [F(67, 1083)] * 3 + [F(40, 441)] * 3
    for i, value in enumerate(diagonal):
        expected[i][i] = value
    check("full-eight-source-poisson-response", response == expected and iszero(mul(p, sources)),
          "full 27-dimensional inverse checks all five stresses, three heat modes and all cross responses at a=1")

    field_basis = columns([F(5 - 3 * e, 2) for e in energy],
                          *[[F(3 * v[a]) for v in velocities] for a in range(3)],
                          [F(3, 2) * (e - 1) for e in energy])
    fields_ok = mul(weighted_zt, field_basis) == eye(5)
    for direction in range(3):
        corrector = scale(mul(r, rowscale(field_basis, [v[direction] for v in velocities])), -1)
        for field, column in enumerate(transpose(corrector)):
            fields_ok &= all(inner([F(v[a]) for v in velocities], column) == 0 for a in range(3))
            strain = zero(3, 3)
            if field in (1, 2, 3):
                j = field - 1
                strain[direction][j] += F(1, 2)
                strain[j][direction] += F(1, 2)
                for a in range(3):
                    strain[a][a] -= F(direction == j, 3)
            for a, bb in product(range(3), repeat=2):
                actual = inner([F(v[a] * v[bb]) for v in velocities], column)
                want = -6 * (F(35, 311) if a == bb else F(67, 1083)) * strain[a][bb]
                fields_ok &= actual == want
            for a in range(3):
                want = F(20, 147) * (int(field == 0) - int(field == 4)) * int(a == direction)
                fields_ok &= inner([F(e * v[a]) for v, e in zip(velocities, energy)], column) == want
    check("complete-constitutive-flux", fields_ok,
          "every density/momentum/energy gradient: zero mass correction, trace-free cubic stress, q=−(20/147) grad(E−rho)")

    def residual_certificate(wave, wrong_sign=False):
        stream = [sum(v[a] * wave[a] for a in range(3)) for v in velocities]
        dz = rowscale(z, stream)
        rd_z = mul(r, dz)
        a0 = scale(mul(coord, dz), -1)
        a1 = mul(coord, rowscale(rd_z, stream))
        if wrong_sign:
            a1 = scale(a1, -1)
        agen = [a0, a1]
        vop = scale(rd_z, -1)
        rrd_z = mul(r, rd_z)
        z0 = add(mul(rrd_z, a0), mul(r, mul(q, rowscale(rd_z, stream))))
        z1 = mul(rrd_z, a1)
        zop = [z0, z1]
        app = [z, vop, z0, z1]
        bx = [mul(b, a) for a in app]
        assert iszero(bx[0])
        residual = mpolyadd(mpolyadd(mpolymul(app, agen), [rowscale(a, stream) for a in app]), bx[1:])
        target = [zero(n, 5), zero(n, 5)] + mpolyadd(mpolymul(zop, agen), [rowscale(a, stream) for a in zop])
        return all(iszero(sub(x, y)) for x, y in zip(residual, target))

    check("exact-corrector-residual", all(residual_certificate(k) for k in ((1, 0, 0), (1, 2, -1))),
          "all epsilon-polynomial coefficients in L_epsilon(U+epsilon v+epsilon² z)=epsilon²(z_t+Tz), on all five fields")
    dropped = next(i for i, flag in enumerate(special) if flag)
    changed = bmatrix(F(1), omit=dropped)
    check("scientific-discriminators", not residual_certificate((1, 2, -1), wrong_sign=True)
          and mul(changed, columns(stress[0])) != mul(b, columns(stress[0])),
          "opposite macro dissipation sign and a removed axial collision each fail their scientific identity")

    nu, diffusion, heat_energy = F(67, 361), F(4, 49), F(20, 147)

    def slow_solvability(wave, rho_diffusion):
        # Use real derivative symbols; restoring i in every first derivative
        # gives the Fourier identities with the same polynomial coefficients.
        wave2 = sum(x * x for x in wave)
        transverse = [[wave[1], -wave[0], 0], [wave[2], 0, -wave[0]], [0, wave[2], -wave[1]]]
        for rho, momentum in [(F(1), [F(0)] * 3)] + [(F(0), list(map(F, j))) for j in transverse]:
            divergence = sum(k * j for k, j in zip(wave, momentum))
            if divergence:
                return False
            u_tau = [rho_diffusion * wave2 * rho, *[nu * wave2 * j for j in momentum], F(0)]
            s_u = [F(0), *[nu * (wave2 * j + F(1, 3) * k * divergence) for k, j in zip(wave, momentum)],
                   -heat_energy * wave2 * rho]
            p_t_m = [-rho_diffusion * wave2 * rho, F(0), F(0), F(0),
                     -F(5, 3) * rho_diffusion * wave2 * rho]
            if any(a - b + c for a, b, c in zip(u_tau, s_u, p_t_m)):
                return False
        return True

    check("diffusive-slow-field-solvability", all(slow_solvability(k, diffusion) for k in ((1, 0, 0), (1, 2, -1), (0, 0, 0)))
          and F(5, 3) * diffusion == heat_energy,
          "tuned full tensor: rho_tau=(4/49)Delta rho; j_tau=(67/361)Delta j; m=−3(4/49)v·grad rho cancels the macro residual")
    # A direct full-operator check on an axial wave. Its two transverse stresses
    # have response mu_O independent of alpha, so alpha=1 is sufficient here.
    slow_z = columns([F(5 - 3 * e, 2) for e in energy],
                     [F(3 * v[1]) for v in velocities], [F(3 * v[2]) for v in velocities])
    dx = [v[0] for v in velocities]
    mop = columns([-3 * diffusion * v[0] for v in velocities], [F(0)] * n, [F(0)] * n)
    vdiff = add(scale(mul(r, rowscale(slow_z, dx)), -1), mop)
    zdiff = scale(mul(r, rowscale(vdiff, dx)), -1)
    slow_time = [[diffusion, F(0), F(0)], [F(0), nu, F(0)], [F(0), F(0), nu]]
    check("diffusive-full-operator-cancellations", iszero(add(rowscale(slow_z, dx), mul(b, vdiff)))
          and iszero(add(add(mul(slow_z, slow_time), rowscale(vdiff, dx)), mul(b, zdiff)))
          and not slow_solvability((1, 2, -1), heat_energy),
          "exact delta^−1 and delta^0 cancellations on density/two shear modes; confusing energy and density diffusivities fails")

    # Exact polynomial coefficients, not evaluation at selected rho/j values.
    slow = [[F(5 - 3 * e, 2) for e in energy]] + [[F(3 * v[a]) for v in velocities] for a in range(3)]
    witness = True
    for a in range(3):
        witness &= inner([F(e * v[a] ** 2) for v, e in zip(velocities, energy)], [F(1)] * n) == F(5, 9)
        witness &= inner([F(e ** 2 * v[a] ** 2) for v, e in zip(velocities, energy)], [F(1)] * n) == F(29, 27)
        for left in range(4):
            for right in range(left, 4):
                factor = F(1, 2) if left == right else F(1)
                monomial = [factor * x * y for x, y in zip(slow[left], slow[right])]
                want = F(-2, 3) if left == 0 and right == a + 1 else F(0)
                witness &= inner(heat[a], monomial) == want
                for bb in range(3):
                    stress_source = [F(v[a] * v[bb]) - (F(e, 3) if a == bb else 0)
                                     for v, e in zip(velocities, energy)]
                    want_stress = F(0)
                    if left and right:
                        if left == right:
                            want_stress = F(int(a == bb == left - 1)) - F(int(a == bb), 3)
                        else:
                            want_stress = F({a, bb} == {left - 1, right - 1} and a != bb)
                    witness &= inner(stress_source, monomial) == want_stress
    check("quadratic-slow-mode-moment-witness", witness,
          "all polynomial coefficients: Q-stress=j tensor j−|j|²I/3; H-flux=−2 rho j/3=(2/5) eta j with eta=−5 rho/3; no nonlinear-limit claim")

    # A supplementary stable scaling-and-squaring exponential in ordinary complex
    # arithmetic; exact checks above do not depend on this numerical evidence.
    def cmul(a, bb):
        bt = transpose(bb)
        return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]

    def expm(a):
        size = len(a)
        norm = max(sum(abs(x) for x in row) for row in a)
        squarings = max(0, ceil(log2(norm / 0.5))) if norm else 0
        small = [[x / (2 ** squarings) for x in row] for row in a]
        out = [[complex(i == j) for j in range(size)] for i in range(size)]
        term = [list(row) for row in out]
        for k in range(1, 25):
            term = [[x / k for x in row] for row in cmul(term, small)]
            out = [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(out, term)]
        for _ in range(squarings):
            out = cmul(out, out)
        return out

    def normvec(x):
        return sqrt(sum(float(w) * abs(a[0]) ** 2 for w, a in zip(weights, x)))

    wave = (1, 2, -1)
    stream = [sum(v[a] * wave[a] for a in range(3)) for v in velocities]
    tmat = [[1j * stream[i] if i == j else 0j for j in range(n)] for i in range(n)]
    bz = [[complex(float(x)) for x in row] for row in b]
    rz = [[complex(float(x)) for x in row] for row in r]
    pz = [[complex(float(x)) for x in row] for row in p]
    zz = [[complex(float(x)) for x in row] for row in z]
    cz = [[complex(float(x)) for x in row] for row in coord]
    tz = cmul(tmat, zz)
    vop = [[-x for x in row] for row in cmul(rz, tz)]
    a0 = [[-x for x in row] for row in cmul(cz, tz)]
    a1 = cmul(cz, cmul(tmat, cmul(rz, tz)))
    initial_coordinates = [[1.0], [0.2], [-0.1], [0.3], [0.15]]
    initial_u = cmul(zz, initial_coordinates)
    initial_v = cmul(vop, initial_coordinates)
    observed = []
    initial_corrected_errors = []
    for denominator in (16, 32, 64, 128):
        epsilon = 1.0 / denominator
        initial_h = [[u[0] + epsilon * v[0]] for u, v in zip(initial_u, initial_v)]
        initial_corrected_errors.append(normvec(
            [[h[0]-u[0]-epsilon*v[0]] for h,u,v in zip(initial_h, initial_u, initial_v)]))
        kg = [[-tmat[i][j] - bz[i][j] / epsilon for j in range(n)] for i in range(n)]
        ag = [[a0[i][j] + epsilon * a1[i][j] for j in range(5)] for i in range(5)]
        time = 0.7
        actual = cmul(expm([[time * x for x in row] for row in kg]), initial_h)
        coords = cmul(expm([[time * x for x in row] for row in ag]), initial_coordinates)
        macro = cmul(zz, coords)
        correction = cmul(vop, coords)
        projected = cmul(pz, actual)
        macro_error = normvec([[a[0] - u[0]] for a, u in zip(projected, macro)])
        corrected_error = normvec([[a[0] - u[0] - epsilon * v[0]] for a, u, v in zip(actual, macro, correction)])
        uncorrected_error = normvec([[a[0] - u[0]] for a, u in zip(actual, macro)])
        observed.append((denominator, macro_error, corrected_error, uncorrected_error))
        print(f"FOURIER epsilon=1/{denominator} t={time} macro_error={macro_error:.10g} corrected_error={corrected_error:.10g} full_uncorrected_error={uncorrected_error:.10g}", flush=True)
    check("actual-initial-preparation", all(e < 1e-14 for e in initial_corrected_errors),
          f"actual prepared h(0) has corrected distances {initial_corrected_errors}; the uniform-time comparison includes t=0")
    # This is only a finite-mode guard, not an inference of an all-data theorem.
    macro_ratios = [observed[i][1] / observed[i + 1][1] for i in range(3)]
    corrected_ratios = [observed[i][2] / observed[i + 1][2] for i in range(3)]
    uncorrected_ratios = [observed[i][3] / observed[i + 1][3] for i in range(3)]
    check("finite-mode-order-discriminator", all(3.0 < x < 5.0 for x in macro_ratios + corrected_ratios)
          and all(1.6 < x < 2.4 for x in uncorrected_ratios),
          f"halving-epsilon ratios: macro={macro_ratios}; first-corrected={corrected_ratios}; uncorrected={uncorrected_ratios}; floating-point supplement only")
    check("prepared-data-initial-distance", normvec(initial_v) > 0,
          f"first-prepared datum has ||h(0)−U(0)||=epsilon*{normvec(initial_v):.10g}; the theorem compares projected fields or the corrected distribution")
    print("per_element: all 288 reversible collisions, five invariant contractions and 972 affine block entries checked exactly")
    print("per_site: the supplied 27-velocity local collision space is complete; no native lattice site or record observable identified")
    print("per_mode: exact corrector polynomials on two Fourier directions; finite-mode exponential supplement; all-mode Sobolev estimates are proved in the note")
    print("per_block: all five stress and three heat sources, all cubic symmetry operations and diffusive slow-field solvability checked; nonlinear flux witness is finite algebra only")
    print("lattice_wide: supplied periodic continuum streaming is a theorem premise; no discrete spatial refinement, native dynamics or nonlinear fluid limit executed")
    print(f"TOTAL: {PASS} PASS, {FAIL} FAIL; exact finite identities and supplementary Fourier check; analytic proof in companion note", flush=True)
    return int(FAIL != 0)


if __name__ == "__main__":
    sys.exit(main())
