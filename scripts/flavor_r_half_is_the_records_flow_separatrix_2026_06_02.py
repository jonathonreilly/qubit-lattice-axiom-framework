"""Bounded map theorem: r=1/2 (Q=2/3) is the UNSTABLE SEPARATRIX of the supplied
records/Lueders sharpening map r -> 2r^2. This runner does not derive that the map is
the physical charged-lepton records flow.

Workflow wf_f433eb9d (5 routes + verify + synth). Verdict: r_half_unstable_attractors_are_r1_r0.

Verified findings:
(1) LUEDERS / records sharpening (p->p^2/Z) on the 2-sector power distribution p_s=1/(1+2r),
    p_d=2r/(1+2r) reduces EXACTLY to the 1-D map r -> 2r^2. Fixed points r=0 and r=1/2;
    f'(r)=4r so f'(0)=0 (STABLE, singlet-collapse, Q=1/3) and f'(1/2)=2 (UNSTABLE separatrix, Q=2/3);
    r>1/2 runs away to the projective doublet-collapse end (r->infinity in this coordinate). Finite
    r=1 is not a fixed point of this map.
(2) Entropy functionals: the 2-SECTOR Shannon entropy S2(r) is MAXIMIZED at r=1/2 (a stable max,
    S2''<0); the 3-real-DOF entropy S3(r) is maximized at r=1. Only 2-sector thermalization -> r=1/2,
    and the 2-sector partition IS the unforced det_C/(1,1) block-count (the C^3=I-forbidden U(1)_b/SO(2)
    doublet quotient would be needed to justify it as emergent).
(3) Contextual route notes such as NJL -> r=4 or Coleman-Weinberg over 3 eigenvalue DOF -> dimension
    (1,2) do not supply a verified attraction to r=1/2 in this packet.
(4) LEDGER CORRECTION: the only measures landing on r=1/2 (bae_max_entropy, bae_f1_f3,
    koide_real_rep_block_count) are UNAUDITED on origin/main; the retained pieces (Lueders rule
    retained_bounded, Frobenius isotype split retained_no_go declining to rank (1,1)/(1,2),
    primitive trace-degeneracy retained_no_go) all point to r=0 / r=1.

CONDITIONAL PHYSICAL REFRAME: if the charged-lepton sector is governed by this records map, Koide
precision (Q=2/3 to ~1e-5) places it on the map separatrix -- a knife-edge that demands a STABILIZER
(or is a tuned/transient initial condition). The next lead remains open: does einselection (a pointer
basis from the C_3-invariant interaction Hamiltonian) stabilize the 2-isotype-sector partition
non-circularly?
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    # (1) Lueders sharpening on the 2-sector distribution == r -> 2r^2
    def luders(r):
        ps, pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r)
        Z = ps ** 2 + pd ** 2
        psn, pdn = ps ** 2 / Z, pd ** 2 / Z
        return (pdn / psn) / 2
    ok = all(abs(luders(r) - 2 * r ** 2) < 1e-12 for r in [0.1, 0.3, 0.49, 0.5, 0.7, 1.0])
    passed.append(check(
        "1 Lueders/records sharpening (p->p^2/Z) on the 2-sector power distribution = the map r -> 2r^2 EXACTLY",
        ok, "grounded in the cited Lueders composition-consistency source"))

    # (2) fixed points & stability: r=0 stable, r=1/2 UNSTABLE separatrix;
    # finite r=1 is not fixed by this map.
    fprime = lambda r: 4 * r
    passed.append(check(
        "2 fixed points r=0 (f'=0 STABLE) and r=1/2 (f'=2 UNSTABLE separatrix); finite r=1 is not fixed, and r>1/2 runs to projective doublet-collapse",
        abs(2 * 0 ** 2 - 0) < 1e-12
        and abs(2 * 0.5 ** 2 - 0.5) < 1e-12
        and abs(2 * 1 ** 2 - 1) > 1e-12
        and fprime(0) < 1
        and fprime(0.5) > 1,
        "r=1/2 is the REPELLING WATERSHED; the upper basin is r->infinity in this coordinate"))

    # (3) entropy functionals: S2 (2-sector) peaks at r=1/2; S3 (3-DOF) peaks at r=1
    def S2(r):
        ps, pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r)
        return -(ps * np.log(ps) + pd * np.log(pd))
    def S3(r):
        w = np.array([3.0, 3 * r, 3 * r]); p = w / w.sum()
        return -(p * np.log(p)).sum()
    rs = np.linspace(0.02, 4, 4000)
    r2 = rs[int(np.argmax([S2(r) for r in rs]))]
    r3 = rs[int(np.argmax([S3(r) for r in rs]))]
    passed.append(check(
        "3 2-SECTOR entropy S2 peaks at r=1/2 (the unforced det_C partition); 3-real-DOF entropy S3 peaks at finite r=1 as a separate comparator",
        abs(r2 - 0.5) < 0.02 and abs(r3 - 1.0) < 0.02,
        f"argmax S2={r2:.3f} (1/2), argmax S3={r3:.3f} (1) -> S3's r=1 is not a fixed point of r->2r^2"))

    # (4) the balanced lane is a saddle for the supplied map: stable for the sector
    # functional, unstable under r -> 2r^2.
    passed.append(check(
        "4 r=1/2 is a STABLE max of the (unforced) 2-sector entropy but an UNSTABLE separatrix of the supplied records map -> not an attractor for that map",
        S2(0.5) > S2(0.4) and S2(0.5) > S2(0.6) and (2 * 0.6 ** 2 > 0.6) and (2 * 0.4 ** 2 < 0.4),
        "a physical charged-lepton use would need a stabilizer/bridge that pins the 2-sector record basis"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (bounded records-map theorem): the supplied Lueders sharpening map is r -> 2r^2;")
    print("r=1/2 (Q=2/3) is its UNSTABLE SEPARATRIX. The finite fixed points are r=0 and r=1/2;")
    print("finite r=1 is not fixed by this map, while r>1/2 runs to the projective doublet-collapse")
    print("end (r->infinity in this coordinate). r=1/2 is a STABLE max only of the unforced 2-sector")
    print("(det_C) entropy. A physical charged-lepton use would need an additional bridge/stabilizer")
    print("selecting the 2-sector record basis; this runner does not derive the physical records flow.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
