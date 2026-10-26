"""Stationary points of supplied sector and per-DOF entropy functionals.
These checks do not select a physical lane or derive generations. At fixed r,
individual circulant masses also depend on arg(b). Fraction exchange on r>0
is r -> 1/(4r); the affine reflection r -> 1-r is a different map.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def main():
    passed = []

    def p_sector(r):
        return 3 / (3 + 6 * r), 6 * r / (3 + 6 * r)

    def S(r):
        ps, pd = p_sector(r)
        return -(ps * np.log(ps) + pd * np.log(pd))

    # (1) r=1/2 maximizes the sector-power entropy (peak), dS/dr=0, S=log2
    rs = np.linspace(0.01, 4, 2000)
    rmax = rs[int(np.argmax([S(r) for r in rs]))]
    h = 1e-6
    dS = (S(0.5 + h) - S(0.5 - h)) / (2 * h)
    passed.append(check(
        "1 sector-power entropy S(r) is MAXIMIZED at r=1/2 (peak); dS/dr=0 there; S(1/2)=log2",
        abs(rmax - 0.5) < 0.01 and abs(dS) < 1e-5 and abs(S(0.5) - np.log(2)) < 1e-12,
        f"argmax r={rmax:.3f}, dS/dr(1/2)={dS:.2e}, S(1/2)={S(0.5):.4f}=log2 -> a genuine STATIONARY point, not arbitrary"))

    # (1b) imbalance trough at r=1/2; (1c) swap fixed point
    passed.append(check(
        "1b singlet-doublet power imbalance |3-6r| is at a TROUGH (=0) exactly at r=1/2; r=1/2 = fixed point of sector exchange r->1/(4r)",
        abs(3 - 6 * 0.5) < 1e-12 and abs(1/(4*0.5) - 0.5) < 1e-12,
        "the balance point of the supplied sectors; r=1 is not an endpoint of r>=0"))

    # (2) the three lanes as distinguished points
    Q = lambda r: 1/3 + 2/3 * r
    passed.append(check(
        "2 three distinguished points: r=0->Q=1/3 (S_3 degenerate), r=1/2->Q=2/3 (balanced), r=1->Q=1 (signed-trace value)",
        abs(Q(0) - 1/3) < 1e-12 and abs(Q(0.5) - 2/3) < 1e-12 and abs(Q(1) - 1) < 1e-12,
        "three algebraic points; physical lane assignment is not tested"))

    # Per-DOF entropy uses three fractions (ps,pd/2,pd/2), maximized at equality.
    def S_dof(r):
        ps,pd=p_sector(r)
        return -ps*np.log(ps)-pd*np.log(pd/2)
    passed.append(check("per-DOF entropy is maximized at r=1 (three equal fractions)",
        abs(S_dof(1)-np.log(3))<1e-12 and S_dof(.5)<S_dof(1)
        and abs((S_dof(1+h)-S_dof(1-h))/(2*h))<1e-5))

    test_r = 2.0
    ps, pd = p_sector(test_r)
    swapped = p_sector(1/(4*test_r))
    passed.append(check("sector exchange swaps the two fractions for r=2",
                        np.allclose(swapped, (pd, ps))))
    a_phase, b_phase = 0.0, 0.2
    spectrum = lambda phase: np.sort((1+np.sqrt(2)*np.cos(phase+2*np.pi*np.arange(3)/3))**2)
    passed.append(check("r=1/2 does not fix mass ratios: phase changes normalized spectrum",
        not np.allclose(spectrum(a_phase)/spectrum(a_phase).sum(), spectrum(b_phase)/spectrum(b_phase).sum())))
    signed = 1 + np.sqrt(2)*np.cos(np.pi/3+2*np.pi*np.arange(3)/3)
    positive_q = np.sum(signed**2)/np.sum(np.abs(signed))**2
    passed.append(check("signed-trace Q need not equal positive-mass Q at fixed r=1/2",
        np.min(signed)<0 and abs(positive_q-2/3)>1e-3,
        f"phase pi/3, positive-mass Q={positive_q:.9f}"))
    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("Sector entropy has its maximum at r=1/2; physical selection and arg(b) remain unspecified.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
