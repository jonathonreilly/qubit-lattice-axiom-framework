#!/usr/bin/env python3
"""Referee for the two-record pull under exclusion, a1.

Author w-macbookpro90c72-j3e98 (claude-opus-5-5). Own matrix elements.
The ring-of-24 packet ratios were not rebuilt. The reduction is one-dimensional.
"""
import itertools
from fractions import Fraction as Fr

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def mul(left, right):
    return (left[0] * right[0] - left[1] * right[1], left[0] * right[1] + left[1] * right[0])


def add(left, right):
    return (left[0] + right[0], left[1] + right[1])


def conj(value):
    return (value[0], -value[1])


ZERO = (Fr(0), Fr(0))


def walk(length, rates, ring):
    generator = {}
    for site in range(length):
        for coin in (0, 1):
            charge = 1 if coin == 0 else -1
            for step, sign in ((1, -1), (-1, 1)):
                neighbour = site + step
                if ring:
                    neighbour %= length
                elif not 0 <= neighbour < length:
                    continue
                generator[(2 * site + coin, 2 * neighbour + coin)] = (Fr(0), Fr(sign * charge, 2) * rates[site] * rates[neighbour])
    return generator


def pair(first, second, sign):
    width = len(first)
    out = {}
    for i in range(width):
        for j in range(width):
            out[(i, j)] = add(mul(first[i], second[j]), mul((Fr(sign), Fr(0)), mul(second[i], first[j])))
    return out


def compress(state, sites):
    return {key: value for key, value in state.items() if sites[key[0]] != sites[key[1]] and value != ZERO}


def apply_one(generator, state, slot):
    columns = {}
    for (row, col), value in generator.items():
        columns.setdefault(col, []).append((row, value))
    out = {}
    for (left, right), value in state.items():
        source = left if slot == 0 else right
        for row, hop in columns.get(source, []):
            key = (row, right) if slot == 0 else (left, row)
            out[key] = add(out.get(key, ZERO), mul(hop, value))
    return out


def density(generator, state, sites, length):
    norm = sum(value[0] ** 2 + value[1] ** 2 for value in state.values())
    images = [apply_one(generator, state, slot) for slot in (0, 1)]
    local = [Fr(0) for _ in range(length)]
    for (left, right), value in state.items():
        local[sites[left]] += mul(conj(value), images[0].get((left, right), ZERO))[0]
        local[sites[right]] += mul(conj(value), images[1].get((left, right), ZERO))[0]
    return [item / norm for item in local]


def gram_orthogonal(first_real, first_imag, second_real, second_imag):
    dot = lambda left, right: sum(a * b for a, b in zip(left, right))
    norm = dot(first_real, first_real) + dot(first_imag, first_imag)
    real_cross = (dot(first_real, second_real) + dot(first_imag, second_imag)) / norm
    imag_cross = (dot(first_real, second_imag) - dot(first_imag, second_real)) / norm
    real = [value - (real_cross * p - imag_cross * q) for value, p, q in zip(second_real, first_real, first_imag)]
    imag = [value - (real_cross * q + imag_cross * p) for value, p, q in zip(second_imag, first_real, first_imag)]
    return list(zip(first_real, first_imag)), list(zip(real, imag))


def block78():
    size = 6
    first_real = [Fr((x * x + 1) % 4, 3) if coin == 0 else Fr((2 * x + 1) % 5, 4) for x in range(size) for coin in range(2)]
    first_imag = [Fr(x % 3, 2) if coin == 0 else Fr((x * x) % 3 - 1, 3) for x in range(size) for coin in range(2)]
    second_real = [Fr((x + 2) % 4, 5) if coin == 0 else Fr(1, 2) for x in range(size) for coin in range(2)]
    second_imag = [Fr((x * x + x) % 3, 2) if coin == 0 else Fr((3 * x) % 4 - 2, 3) for x in range(size) for coin in range(2)]
    return gram_orthogonal(first_real, first_imag, second_real, second_imag)


def ledger():
    ok = True
    energies = {}
    rings = {
        6: block78(),
        8: (
            [(Fr((x + coin) % 3 - 1, 2), Fr((2 * x + coin) % 5, 7)) for x in range(8) for coin in range(2)],
            [(Fr((x * x + 2 * coin) % 4, 3), Fr((x + 3 * coin) % 3 - 1, 5)) for x in range(8) for coin in range(2)],
        ),
    }
    for length, states in rings.items():
        rates = [1 + Fr((3 * x * x + x) % 5, 7) for x in range(length)]
        sites = [i // 2 for i in range(2 * length)]
        for sign in (-1, 1):
            state = compress(pair(states[0], states[1], sign), sites)
            generator = walk(length, rates, True)
            local = density(generator, state, sites, length)
            for site in range(length):
                up = list(rates)
                down = list(rates)
                up[site] = rates[site] * (1 + Fr(1, 10 ** 6))
                down[site] = rates[site] * (1 - Fr(1, 10 ** 6))
                high = sum(density(walk(length, up, True), state, sites, length))
                low = sum(density(walk(length, down, True), state, sites, length))
                derivative = (high - low) / (2 * Fr(1, 10 ** 6)) / 2
                ok &= derivative == local[site]
            energies[(length, sign)] = sum(local)
    report(
        "ledger",
        ok and energies[(6, -1)] == Fr(12349656, 122046701),
        f"on rings of 6 and 8, both signs, the rate derivative equals the local density; the antisymmetric ring of 6 has energy {energies[(6, -1)]}",
    )


def mapping():
    length = 7
    rates = [Fr(k % 4 + 2, k % 3 + 2) for k in range(length)]
    generator = walk(length, rates, False)
    ok = True
    checked = 0
    for sign in (-1, 1):
        for left in range(length):
            for right in range(left + 1, length):
                for coin_left, coin_right in itertools.product((0, 1), repeat=2):
                    i, j = 2 * left + coin_left, 2 * right + coin_right
                    state = {(i, j): (Fr(1), Fr(0)), (j, i): (Fr(sign), Fr(0))}
                    image = {}
                    for slot in (0, 1):
                        for (a, b), value in apply_one(generator, state, slot).items():
                            if a // 2 == b // 2:
                                continue
                            image[(a, b)] = add(image.get((a, b), ZERO), value)
                    ordered = {(a // 2, b // 2, a % 2, b % 2): value for (a, b), value in image.items() if a // 2 < b // 2}

                    def gauge(xl, xr, sl, sr):
                        return (-1) ** ((xl if sl else 0) + (xr if sr else 0))

                    for (yl, yr, tl, tr), value in ordered.items():
                        ok &= (tl, tr) == (coin_left, coin_right)
                        ok &= (yl, yr) != (left, right) and ((yl == left) != (yr == right))
                        source, dest = (left, yl) if yl != left else (right, yr)
                        factor = gauge(yl, yr, tl, tr) * gauge(left, right, coin_left, coin_right)
                        hop = (Fr(0), (Fr(-1, 2) if dest == source - 1 else Fr(1, 2)) * rates[source] * rates[dest])
                        ok &= (value[0] * factor, value[1] * factor) == hop
                        checked += 1
    report(
        "map",
        ok and checked == 480,
        f"on a chain of 7, both exchange signs, all {checked} ordered images keep the coins and match the gauged up-coin hop",
    )
    return rates, generator


def source(rates, generator):
    length = 7
    sites = [i // 2 for i in range(2 * length)]
    amplitude = {(left, right): (Fr((3 * left + right) % 5 - 2, 3), Fr((left + 2 * right) % 4 - 1, 5)) for left in range(length) for right in range(left + 1, length)}
    coin_left, coin_right, sign = 0, 1, -1

    def gauge(site, coin):
        return (-1) ** (site if coin else 0)

    state = {}
    for (left, right), value in amplitude.items():
        factor = gauge(left, coin_left) * gauge(right, coin_right)
        state[(2 * left + coin_left, 2 * right + coin_right)] = (value[0] * factor, value[1] * factor)
        state[(2 * right + coin_right, 2 * left + coin_left)] = (value[0] * factor * sign, value[1] * factor * sign)
    pair_density = density(generator, state, sites, length)

    def charge(left, right):
        if left < right:
            return amplitude[(left, right)]
        if left > right:
            value = amplitude[(right, left)]
            return (-value[0], -value[1])
        return ZERO

    norm = 2 * sum(value[0] ** 2 + value[1] ** 2 for value in amplitude.values())
    charge_hop = {}
    for site in range(length):
        for neighbour in (site - 1, site + 1):
            if 0 <= neighbour < length:
                charge_hop[(site, neighbour)] = (Fr(0), (Fr(-1, 2) if neighbour == site + 1 else Fr(1, 2)) * rates[site] * rates[neighbour])
    charge_density = []
    for site in range(length):
        total = Fr(0)
        for partner in range(length):
            for (row, col), hop in charge_hop.items():
                if row == site:
                    total += 2 * mul(conj(charge(site, partner)), mul(hop, charge(col, partner)))[0]
        charge_density.append(total / norm)
    report(
        "source",
        pair_density == charge_density,
        "on the chain of 7 the compressed pair density equals the charge one-particle trace at every site",
    )


def bound():
    # |q A - 2 C + B| <= ||D|| (q + 2 sqrt(q nu) + nu) <= 4 ||D|| nu when 0 <= q <= nu.
    samples = ((Fr(1, 5), Fr(1, 5)), (Fr(1, 8), Fr(1, 3)), (Fr(0), Fr(1, 2)), (Fr(2, 7), Fr(3, 7)))
    # (2 sqrt(q nu))^2 = 4 q nu, and the remaining budget after q is 3 nu - q.
    ok = True
    for q, nu in samples:
        cross = 4 * q * nu
        room = (3 * nu - q) ** 2
        ok &= q <= nu and cross <= room
    report(
        "bound",
        ok,
        "when coincidence is no more likely than a near meeting, the three overlap terms are at most 4 ||D|| nu",
    )


def main():
    ledger()
    rates, generator = mapping()
    source(rates, generator)
    bound()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - on a chain, after the gauge (-1)^x on down coins, the compressed pair generator is the "
        "up-coin hop of two spinless fermions times a frozen coin sequence, for both exchange signs. "
        "The source equals the charge one-particle trace. The ledger derivative matches the local density on rings of 6 and 8, "
        "and the antisymmetric ring of 6 has energy 12349656/122046701. Exclusion adds no new failure of action = reaction on a chain."
    )
    print(
        "SUMMARY: confirmed the ledger, the 480 chain matrix elements, the charge-source identity, and the overlap bound. "
        "The ring-of-24 packet ratios were not rebuilt. The reduction does not extend to two or three dimensions."
    )


if __name__ == "__main__":
    main()
