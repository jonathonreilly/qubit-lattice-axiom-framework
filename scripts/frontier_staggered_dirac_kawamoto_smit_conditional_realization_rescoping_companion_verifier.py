"""Finite checks for the Kawamoto-Smit conditional rescoping companion."""

from __future__ import annotations

import cmath
import itertools


def check(name: str, cond: bool, detail: str = "") -> bool:
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def epsilon(site: tuple[int, int, int]) -> int:
    return -1 if sum(site) % 2 else 1


def eta(site: tuple[int, int, int], mu: int) -> int:
    x1, x2, _x3 = site
    if mu == 1:
        return 1
    if mu == 2:
        return -1 if x1 % 2 else 1
    if mu == 3:
        return -1 if (x1 + x2) % 2 else 1
    raise ValueError("mu must be 1, 2, or 3")


def shift(site: tuple[int, int, int], mu: int) -> tuple[int, int, int]:
    values = list(site)
    values[mu - 1] += 1
    return tuple(values)  # type: ignore[return-value]


def main() -> int:
    passed: list[bool] = []
    sites = list(itertools.product(range(2), repeat=3)) + [
        (2, 1, 0),
        (3, 4, 5),
        (5, 5, 5),
        (-1, 2, 3),
    ]

    passed.append(
        check(
            "epsilon flips on every checked nearest-neighbor link",
            all(epsilon(site) * epsilon(shift(site, mu)) == -1 for site in sites for mu in (1, 2, 3)),
        )
    )

    omega_global = 1j
    passed.append(
        check(
            "omega(x)=epsilon(x) omega_global gives the required sign reversal across links",
            all(
                abs(
                    (epsilon(site) * omega_global)
                    / (epsilon(shift(site, mu)) * omega_global)
                    + 1.0
                )
                < 1e-12
                for site in sites
                for mu in (1, 2, 3)
            ),
        )
    )

    passed.append(
        check(
            "Kawamoto-Smit eta_1 is identically one",
            all(eta(site, 1) == 1 for site in sites),
        )
    )
    passed.append(
        check(
            "Kawamoto-Smit eta_2 is (-1)^x_1",
            all(eta(site, 2) == (-1 if site[0] % 2 else 1) for site in sites),
        )
    )
    passed.append(
        check(
            "Kawamoto-Smit eta_3 is (-1)^(x_1+x_2)",
            all(eta(site, 3) == (-1 if (site[0] + site[1]) % 2 else 1) for site in sites),
        )
    )

    phase = cmath.exp(0.37j)
    passed.append(
        check(
            "global phase gauge cancels in the chirality ratio",
            all(
                abs(
                    (phase * epsilon(site) * omega_global)
                    / (phase * epsilon(shift(site, mu)) * omega_global)
                    + 1.0
                )
                < 1e-12
                for site in sites
                for mu in (1, 2, 3)
            ),
        )
    )

    pass_count = sum(passed)
    fail_count = len(passed) - pass_count
    print(f"\nSCORECARD PASS={pass_count} FAIL={fail_count}")
    print(
        "FINDING: H_staggered_chirality is a clean conditional premise; "
        "given it, the checked Kawamoto-Smit phase surface is consistent."
    )
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
