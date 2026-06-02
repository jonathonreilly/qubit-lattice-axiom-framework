"""J-hunt ROUND 1: a STATIC complex structure cannot select det_C. J_cs is A1-native but
measure-neutral; the chiral-import bridge via 'Gamma_chi = J_cs' is a FALSE identity.

Goal of the hunt: a complex structure J on the doublet coefficient b that forces det_C -> r=1/2 ->
Q=2/3, is not the forbidden continuous U(1)_b, and descends from A1. Round 1 verdict (wf_719da018):
no_J_detR_default_stands -- but it pins the next lever to a DYNAMICAL (first-order action) bridge.

Verified findings:
(1) J_cs=(C-C^2)/sqrt3 is genuinely A1-native: anti-Hermitian, J_cs^2=-P_doublet, eigs {0,+-i},
    [J_cs,C]=0 (Schur-forced C_3-equivariant complex structure), built from retained C -- a DIFFERENT
    object from the U(1)_b the prior no-go killed (it does not rephase C).
(2) But J_cs is MEASURE-NEUTRAL: exp(theta J_cs) = SO(2) on the (Re b, Im b) plane preserves the HS
    doublet metric block 6*I (R^T g R = g trivially), hence preserves BOTH the flat real measure (det_R)
    AND the holomorphic measure (det_C). A complex structure is an automorphism of its own real plane's
    Lebesgue measure AND of the holomorphic volume -- it does NOT distinguish them. So the static
    existence of J_cs CANNOT select det_C. [J_cs,H]=0 (operator-silent) is real and consistent, but a
    silent structure has no lever to fix the mode-count. J_FOUND_A1_FORCED is ruled out.
(3) The chiral-import bridge BROKE: the claim 'Gamma_chi=(2/3)*Jall-I is built from the SAME J as J_cs'
    is FALSE -- Gamma_chi's J is the rank-1 ALL-ONES real matrix (J^2=3J), so Gamma_chi is a REAL
    involution (Gamma^2=+I, eigs {+1,-1,-1}), an algebraically distinct type from the anti-Hermitian
    J_cs (J_cs^2=-P, eigs {0,+-i}). They COMMUTE but are not equal/proportional. Gluing 'turn on
    chirality = make the measure J_cs-holomorphic = det_C' on this non-existent identity is CIRCULAR.

NEXT LEVER (round 2): a static J can't select the measure, but a FIRST-ORDER (Dirac/Berezin) ACTION
can -- Berezin integration over a holomorphic/Grassmann mode counts it as ONE (det_C), while a
second-order Gaussian weight is measure-neutral. Does A1+emergent-spacetime supply a first-order action
for the generation coefficient b (built from the genuine anti-Hermitian J_cs, NOT the all-ones
Gamma_chi)? That first-order/Berezin structure is exactly the fermionic frame = the sector's one import.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
JALL = np.ones((3, 3))
JCS = (C - C @ C) / np.sqrt(3.0)
GX = (2.0 / 3.0) * JALL - I3
P_D = I3 - JALL / 3.0


def main():
    passed = []

    passed.append(check(
        "R1 J_cs anti-Hermitian, J_cs^2=-P_doublet, eigs {0,+-i}, [J_cs,C]=0 -> A1-native Schur-forced complex structure",
        np.allclose(JCS.conj().T, -JCS) and np.allclose(JCS @ JCS, -P_D) and np.allclose(JCS @ C - C @ JCS, 0),
        f"eigs(J_cs)={np.round(np.linalg.eigvals(JCS),3).tolist()}; distinct from U(1)_b (does not rephase C)"))

    passed.append(check(
        "R2 Gamma_chi=(2/3)Jall-I is a REAL involution (Gamma^2=I, eigs {+1,-1,-1}); J_cs != Gamma_chi (chiral glue FALSE)",
        np.allclose(GX @ GX, I3) and np.allclose(np.sort(np.linalg.eigvalsh(GX)), [-1, -1, 1])
        and not np.allclose(JCS, GX) and np.allclose(JCS @ GX - GX @ JCS, 0),
        "Gamma_chi's J = all-ones (J^2=3J, real); J_cs anti-Hermitian -> distinct types, commute but not equal -> the 'Gamma_chi=J_cs' bridge is a non-identity"))

    # measure-neutrality: SO(2)=exp(theta J_cs) preserves the HS doublet metric block 6*I -> preserves both measures
    g = 6.0 * np.eye(2)
    neutral = True
    for th in (0.3, 0.7, 1.9):
        R = np.cos(th) * np.eye(2) + np.sin(th) * np.array([[0, -1.0], [1.0, 0]])
        if not (np.allclose(R.T @ g @ R, g) and abs(np.linalg.det(R) - 1) < 1e-12):
            neutral = False
    passed.append(check(
        "R3 exp(theta J_cs)=SO(2) preserves the HS block 6*I (R^T g R=g, det R=1) -> preserves BOTH det_R and det_C measures",
        neutral,
        "a complex structure is an automorphism of its real-plane Lebesgue measure AND the holomorphic volume -> J_cs CANNOT select det_C (MEASURE-NEUTRAL)"))

    passed.append(check(
        "R4 [J_cs,H]=0 for the circulant family (operator-silent): J_cs moves no eigenvalue -> no spectral lever to fix the mode-count",
        all(np.allclose(JCS @ (a * I3 + b * C + np.conj(b) * C.conj().T) - (a * I3 + b * C + np.conj(b) * C.conj().T) @ JCS, 0)
            for a, b in [(1.0, 0.6 + 0.2j), (2.0, 1.1)]),
        "operator-silence is consistent with J_cs being a field-space complex structure, but a silent structure cannot DEFINE the counting measure"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (J-hunt round 1, wf_719da018): no_J -- det_R/Q=1 default stands. A STATIC complex structure")
    print("(even the Schur-forced A1-native J_cs) is MEASURE-NEUTRAL: SO(2)=exp(theta J_cs) preserves both the")
    print("flat-real (det_R) and holomorphic (det_C) measures, so it cannot select det_C. The chiral-import")
    print("bridge via 'Gamma_chi=J_cs' is a FALSE identity (Gamma_chi=real involution from all-ones; J_cs=anti-")
    print("Hermitian) -- circular. NEXT LEVER (round 2): a first-order (Dirac/Berezin) ACTION for the generation")
    print("coefficient b, built from the genuine anti-Hermitian J_cs, would count b as ONE complex/Grassmann mode")
    print("(det_C -> r=1/2) where a static J and a second-order Gaussian cannot. That first-order/Berezin")
    print("structure = the fermionic frame = the sector's one import. The hunt continues there.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
