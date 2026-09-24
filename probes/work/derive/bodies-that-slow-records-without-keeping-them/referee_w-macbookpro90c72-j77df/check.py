#!/usr/bin/env python3
"""Referee for bodies-that-slow-records-without-keeping-them a2.

Author w-jonathonsmac4f50-j40e2 (claude-opus-5). Own simplex integrals.
The angular factor, the cross-section, and the free-fall estimate are not re-derived.
"""
import sympy as sp

fails = []


def report(name, ok, detail):
    if not ok:
        fails.append(name)
    print(("PASS " if ok else "FAIL ") + name + ": " + detail)


def shell():
    f1, f2 = sp.symbols("f1 f2", positive=True)
    f3 = 1 - f1 - f2
    types = {
        2: [(2, 0, 0), (1, 1, 0)],
        3: [(3, 0, 0), (2, 1, 0), (1, 1, 1)],
        4: [(4, 0, 0), (3, 1, 0), (2, 2, 0), (2, 1, 1)],
    }
    ok = True
    for n, xs in types.items():
        for x in xs:
            hh = sp.factorial(n)
            for k in x:
                hh /= sp.factorial(k)
            hh *= f1 ** x[0] * f2 ** x[1] * f3 ** x[2]
            area = sp.simplify(sp.integrate(sp.integrate(hh, (f2, 0, 1 - f1)), (f1, 0, 1)))
            prob = sp.simplify(2 * area)
            ok &= area == sp.Rational(1, (n + 1) * (n + 2))
            ok &= prob == sp.Rational(2, (n + 1) * (n + 2))
    report(
        "shell constant",
        bool(ok),
        "every composition of n=2,3,4 integrates to 1/((n+1)(n+2)) in Lebesgue measure and twice that as a probability",
    )


def shadow():
    rho, h, kap, v = sp.symbols("rho h kappa v", positive=True)
    plain = rho * (1 - h)
    slowed = rho * h / kap
    density = sp.simplify(plain + slowed - rho * (1 + h * (1 / kap - 1)))
    number = sp.simplify(plain * v + slowed * (kap * v) - rho * v)
    current = sp.simplify(plain * v ** 2 + slowed * (kap * v) ** 2 - rho * v ** 2 * (1 - h * (1 - kap)))
    short = sp.simplify(rho * v ** 2 - (plain * v ** 2 + slowed * (kap * v) ** 2) - rho * v ** 2 * h * (1 - kap))
    report(
        "shadow",
        density == 0 and number == 0 and current == 0 and short == 0,
        "density is rho(1+h(1/kappa-1)); number current and momentum density stay rho v; momentum current is short by rho v^2 h(1-kappa)",
    )


def price():
    kap1, kap2, rho, m2, h = sp.symbols("kappa_1 kappa_2 rho m2 h", positive=True)
    force = (1 - kap1) * (1 - kap2) * rho * m2 * h
    swapped = force.subs({kap1: kap2, kap2: kap1}, simultaneous=True)
    u, nb, sig, m1, M, r = sp.symbols("u n_b sigma m1 M r", positive=True)
    tau = 1 / (nb * sig * m1 * u)
    pull = u ** 2 * rho * m2 / r ** 2
    approach = sp.simplify(sp.sqrt(r * M / pull))
    ratio = sp.simplify((approach / tau) ** 2)
    target = M * r ** 3 * nb ** 2 * sig ** 2 * m1 ** 2 / (rho * m2)
    report(
        "cancellation",
        sp.simplify(swapped - force) == 0
        and sp.simplify(approach - sp.sqrt(M * r ** 3 / (rho * m2)) / u) == 0
        and sp.simplify(ratio - target) == 0
        and sp.simplify(sp.diff(ratio, u)) == 0,
        "(t/tau)^2 = M r^3 n_b^2 sigma^2 <m>^2 / (rho <m^2>), independent of u=1-kappa; the pair prefactor swaps into itself",
    )


def main():
    shell()
    shadow()
    price()
    if fails:
        print("SUMMARY: fails at " + fails[0])
        return
    print(
        "HIT: confirmed - a slowing site denser by 1/kappa leaves the number current at rho v and shortens only the momentum current, by rho v^2 h(1-kappa). "
        "The free-fall time over the linear run-down cancels u=1-kappa, leaving M r^3 n_b^2 sigma^2 <m>^2 < rho <m^2>. "
        "Shell integrals of every composition at n=2,3,4 are 2/((n+1)(n+2)) in probability measure and half of that in Lebesgue measure."
    )
    print(
        "SUMMARY: confirmed the bookkeeping, the cancellation, and the shell constants including the n=4 endpoints (4,0,0) and (3,1,0). "
        "Block 48's angular factor, sigma, and the free-fall estimate were not re-derived."
    )


if __name__ == "__main__":
    main()
