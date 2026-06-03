"""Negative (route closure): the framework's physical record-forming dynamics SHARPENS, so r=1/2 is the
UNSTABLE separatrix -- the time-arrow 'stabilizer' that would make r=1/2 an attractor is realized by NO
framework CPTP map. Three independent strikes:
  (1) the record map is Lueders self-composition p -> p^2/Z, which on the 2-sector weight is r -> 2r^2,
      with r=1/2 an UNSTABLE fixed point (multiplier 2); the thermalizing g(r)=sqrt(r/2) (r=1/2 stable,
      multiplier 1/2) is merely its formal TIME-REVERSE (record erasure), not a physical channel;
  (2) NO-OP: H is C3-invariant hence already block-diagonal in the isotype projectors {P0,P1} for EVERY
      r (||P0 H P1||~0), so the physical einselection channel induces NO flow on r at all;
  (3) the genuine Born/2nd-law equilibrium is I/3 -> dimension weights (1/3,2/3) -> r=1; an honest
      depolarize-toward-I/3 drives r->0 (Q->1/3), never r=1/2.
So the dynamical/time-arrow route to FORCE r=1/2 is closed: the physical arrow sharpens (r=1/2 unstable),
and r=1/2 must be selected by a MEASURE choice, not by the record dynamics.

This note/runner sets no audit status (independent audit lane owns that).
"""
import numpy as np

C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # (1a) Sharpening flow r -> 2r^2: r=1/2 fixed, multiplier f'(1/2)=4*(1/2)=2 > 1 => UNSTABLE.
    f = lambda r: 2 * r ** 2
    fp = lambda r: 4 * r
    passed.append(check(
        "Lueders sharpening r->2r^2: r=1/2 is a fixed point, multiplier=2 => UNSTABLE separatrix",
        abs(f(0.5) - 0.5) < 1e-12 and fp(0.5) > 1,
        f"f(0.5)={f(0.5)}, f'(0.5)={fp(0.5)}"))
    # iterate from near 1/2 -> runs AWAY to 0 or 1
    lo = 0.49
    for _ in range(60):
        lo = f(lo)
    passed.append(check(
        "iterating the sharpening flow from r=0.49 runs AWAY from 1/2 (-> 0), confirming instability",
        lo < 1e-6, f"after 60 steps from 0.49: r={lo:.2e}"))

    # (1b) The thermalizing g(r)=sqrt(r/2): r=1/2 fixed, multiplier 1/2 stable -- but it is the formal
    # TIME-REVERSE of the sharpening map, not a physical channel.
    g = lambda r: np.sqrt(r / 2)
    gp = lambda r: 1.0 / (2 * np.sqrt(2 * r))
    hi = 0.05
    for _ in range(60):
        hi = g(hi)
    passed.append(check(
        "reverse g(r)=sqrt(r/2): r=1/2 stable (mult 1/2), all seeds -> 0.5 -- but it is record-ERASURE (time-reverse), not a CPTP record map",
        abs(g(0.5) - 0.5) < 1e-12 and gp(0.5) < 1 and abs(hi - 0.5) < 1e-6,
        f"g'(0.5)={gp(0.5)}, iterate from 0.05 -> {hi:.6f}"))

    # (2) NO-OP: H commutes with C => block-diagonal in isotype projectors {P0,P1} for every (a,b).
    # P0 = projector onto the trivial (symmetric) C-eigenspace; P1 = doublet projector.
    v0 = np.ones(3) / np.sqrt(3)
    P0 = np.outer(v0, v0.conj())
    P1 = I3 - P0
    max_offblock = 0.0
    for a, br, bi in [(1.0, 0.7, 0.0), (1.0, 0.3, 0.5), (2.0, 1.1, -0.4)]:
        b = br + 1j * bi
        H = a * I3 + b * C + np.conj(b) * C.conj().T
        max_offblock = max(max_offblock, np.linalg.norm(P0 @ H @ P1))
    passed.append(check(
        "H is already block-diagonal in {P0,P1} for every (a,b) => the einselection channel is a NO-OP on r",
        max_offblock < 1e-9, f"max ||P0 H P1|| = {max_offblock:.2e}"))

    # (3) Honest thermalization targets I/3 -> dimension sector weights (1/3,2/3) -> r=1, not r=1/2.
    # rho=I/3, sector Born weights = Tr(P_sector rho): trivial=1/3, doublet=2/3 -> r=(pd/pt)/2 = 1.
    pt, pd = np.real(np.trace(P0) / 3), np.real(np.trace(P1) / 3)
    r_eq = (pd / pt) / 2.0
    passed.append(check(
        "the genuine Born/2nd-law equilibrium I/3 gives sector weights (1/3,2/3) -> r=1 (Q=1), NOT r=1/2",
        abs(pt - 1/3) < 1e-12 and abs(pd - 2/3) < 1e-12 and abs(r_eq - 1.0) < 1e-12,
        f"(p_triv,p_doublet)=({pt:.3f},{pd:.3f}) -> r={r_eq}"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("FINDING: the framework's physical record dynamics SHARPENS (r->2r^2, r=1/2 unstable); the")
    print("einselection channel is a no-op on r (H already block-diagonal); honest thermalization targets")
    print("I/3 -> r=1. The time-arrow 'stabilizer' for r=1/2 is realized by no framework CPTP map -- r=1/2")
    print("must be a MEASURE choice, not a dynamical attractor. Sets no audit status.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
