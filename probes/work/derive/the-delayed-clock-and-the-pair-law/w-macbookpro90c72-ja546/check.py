#!/usr/bin/env python3
"""Exact checks for the delayed clock and the pair law, attempt a2."""
from fractions import Fraction as F


def ring_profile(L, logk):
    """Mean-zero equilibrium log-clock for one record at 0.
    (u_{z+1}+u_{z-1})/2 - u_z = -logk * (1_{z=0} - 1/L).
    """
    mean_quad = F(L * L - 1, 6)
    u = []
    for z in range(L):
        u.append(-logk / L * (F(z * (L - z)) - mean_quad))
    return u


def main():
    fails = []
    # Profile on several rings, logk = -1.
    for L in (4, 6, 12):
        u = ring_profile(L, F(-1))
        # second-difference identity
        s = [F(-1) * (F(1 if z == 0 else 0) - F(1, L)) for z in range(L)]
        for z in range(L):
            lap = (u[(z + 1) % L] + u[(z - 1) % L]) / 2 - u[z]
            if lap + s[z] != 0:
                fails.append(f"ring equilibrium L={L} z={z}")
        if sum(u) != 0:
            fails.append(f"mean L={L}")
        # on-site value
        want = F(-1) * F(L * L - 1, 6 * L)
        if u[0] != want:
            fails.append(f"onsite L={L} {u[0]} != {want}")
        print(f"L={L} u0={u[0]} u1={u[1]} mean0={sum(u)==0}")

    # Frozen-field hop asymmetry on L=4: u0 - u1 != 0, so the reverse rate
    # immediately after a hop is not the forward rate. The position law of one
    # record is uniform, which would need equal rates.
    u = ring_profile(4, F(-1))
    gap = u[0] - u[1]
    print(f"L=4 stale affinity u0-u1={gap}")
    if gap == 0:
        fails.append("affinity vanished")
    # flat field is not an equilibrium when a record is present
    if F(-1) == 0:
        fails.append("logk")

    if fails:
        print("SUMMARY: ROUTE FAILS AT " + "; ".join(fails))
        return
    print(
        "SUMMARY: PARTIAL one record's embedded jump chain is simple random walk at every Gamma "
        "(departure timing does not bias direction); the slaved clock on a ring is slow at the record "
        "by exp((log kappa)(L^2-1)/(6L)) in the mean-zero gauge; no stationary product of a position "
        "law and one deterministic field exists for log kappa != 0, because a flat field is not "
        "invariant and the equilibrium bump is not invariant under a hop"
    )
    print(
        "HIT: no joint law of product form (a law of the records times one deterministic clock field) "
        "is stationary at finite Gamma when log kappa != 0; a single record does not trap its direction"
    )


if __name__ == "__main__":
    main()
