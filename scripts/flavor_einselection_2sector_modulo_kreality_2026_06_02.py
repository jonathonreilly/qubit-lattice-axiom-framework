"""Einselection reduces the PARTITION half of the gate to K-reality (sound), but does NOT deliver the
VALUE r=1/2 -- and the genuine Born/thermalizing measure gives r=1, not r=1/2 (qualifying the prior
"thermalizing->r=1/2" claim). Residual = TWO physical inputs: (1) K-reality of the generation coupling,
(2) the equal-power-per-block (det_C) vs dimension (Born/det_R) measure.

Workflow wf_bfb916fc (5 routes + verify + synth). Verdict:
einselects_2sector_r_half_derived_modulo_k_reality.

SOUND (the PARTITION half, all routes agree, verified):
- A C_3-invariant + K-REAL (time-reversal-even) monitored Hermitian observable lies in span_R{I, C+C^2};
  eig(C+C^2)={2,-1,-1} -> singlet isolated, DOUBLET DEGENERATE. So it resolves only the 2 real-irreducible
  blocks (singlet P0 rank1, doublet P1 rank2). Resolving omega vs omega^2 (the 3-mode/spectral partition
  -> r=0) strictly requires the K-ODD observable i(C-C^2) (verified conj=-itself). So Zurek einselection by
  a K-real coupling KILLS the r=0 partition and einselects the 2-SECTOR partition -- NON-circular, modulo
  K-reality. This sharpens the gate's partition-half to ONE physical predicate (is the coupling T-real).

GAP A -- K-reality is POSITED, not derived: the emergent-time mechanism is conjugation-EVEN (retained_bounded
  koide_emergent_time_eta_conjugation_parity: b->conj(b) is a spectrum-preserving transpose similarity), so
  it is BLIND to arg(b) and cannot select the real axis (delta=0). K-reality is automatic on the WHOLE cone
  (holds at r=1 too) -> carries NO selective information. = the same delta=0 / det_C / Brannen pin relabeled.

GAP B -- the VALUE r=1/2 is NOT delivered (qualifies the prior thermalization claim), verified:
- H = aI+bC+conj(b)C^2 is ALREADY block-diagonal in {P0,P1} for EVERY r (||P0 H P1||~1e-16) -> the pointer
  map P0(.)P0+P1(.)P1 is a literal NO-OP -> einselection places ZERO constraint on the inter-block POWER ratio.
- The genuine Born/tracial max-entropy state rho=I/3 weights blocks by DIMENSION (Tr P0:Tr P1 = 1:2) -> r=1
  -> Q=1. r=1/2 requires equal-power-per-block (3a^2=6|b|^2, the HS/block-COUNTING measure), a SEPARATE input.
  So the prior "thermalizing flow -> r=1/2" used the 2-SECTOR (block-counting) entropy, NOT the Born entropy;
  the genuine second-law/Born equilibrium is r=1, and r=1/2 is the equal-power-per-block (det_C) equilibrium.

NET: the charged-lepton value r=1/2 reduces to TWO named physical inputs, both standing gates, both matching
Koide's free per-sector fit: (1) K-reality (T-reality of the generation coupling / delta=0 / transpose b=c) ->
the 2-block partition; (2) equal-power-per-block (det_C) vs dimension (Born/det_R) -> r=1/2 vs r=1 within the
2-block structure. Neither is currently derived from A1+A2+emergent-spacetime.
"""
import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)
J = np.ones((3, 3))
P0 = J / 3.0
P1 = I3 - P0


def main():
    passed = []

    # SOUND: K-real C_3-invariant -> 2 blocks; i(C-C^2) K-odd resolves omega vs omega^2
    CpC2 = C + C @ C
    passed.append(check(
        "S1 K-real C_3-invariant observable in span{I,C+C^2}: eig(C+C^2)={2,-1,-1} -> singlet isolated, DOUBLET DEGENERATE (2-block partition)",
        np.allclose(np.sort(np.linalg.eigvalsh(CpC2)), [-1, -1, 2]),
        "K-real monitoring resolves only the 2 real-irreducible blocks, not the 3 complex modes"))
    B2 = 1j * (C - C @ C)
    passed.append(check(
        "S2 resolving omega vs omega^2 (the r=0 3-mode partition) requires the K-ODD observable i(C-C^2) (conj=-itself)",
        np.allclose(B2.conj().T, B2) and np.allclose(B2.conj(), -B2),
        "-> a K-real (T-invariant) coupling CANNOT split the doublet -> einselection kills the r=0 partition (SOUND, modulo K-reality)"))

    # GAP B: H already block-diagonal -> pointer map is a no-op on the power ratio
    offblocks = []
    for r in [0.0, 0.09, 0.5, 1.0, 4.0]:
        b = np.sqrt(r)
        H = I3 + b * C + b * C.conj().T
        offblocks.append(np.linalg.norm(P0 @ H @ P1))
    passed.append(check(
        "B1 GAP B: H=aI+bC+conj(b)C^2 is ALREADY block-diagonal in {P0,P1} for EVERY r (||P0 H P1||~0) -> einselection pointer-map is a NO-OP on the power ratio",
        max(offblocks) < 1e-12,
        f"max ||P0 H P1|| over r in {{0,0.09,0.5,1,4}} = {max(offblocks):.1e} -> decoherence forbids nothing on the inter-block power ratio r"))

    # GAP B value: Born/dimension weighting -> r=1; equal-power-per-block -> r=1/2
    Q = lambda r: 1/3 + 2/3 * r
    born_block_weights = (np.trace(P0) / 3, np.trace(P1) / 3)   # rho=I/3 -> (1/3, 2/3) dimension weighting
    passed.append(check(
        "B2 GAP B value: Born/tracial max-entropy rho=I/3 weights blocks by DIMENSION (1/3,2/3) -> r=1 -> Q=1; equal-power-per-block -> r=1/2 -> Q=2/3 (separate input)",
        abs(born_block_weights[0] - 1/3) < 1e-12 and abs(born_block_weights[1] - 2/3) < 1e-12
        and abs(Q(1.0) - 1.0) < 1e-12 and abs(Q(0.5) - 2/3) < 1e-12,
        f"Born block weights={tuple(round(x,3) for x in born_block_weights)} -> r=1; the prior 'thermalizing->r=1/2' used the NON-Born 2-sector(block-counting) entropy"))

    # GAP A: emergent-time conjugation-even (b->conj(b) spectrum-preserving) -> blind to arg(b) -> can't derive K-reality
    a, b = 1.0, 0.6 + 0.4j
    H = a * I3 + b * C + np.conj(b) * C.conj().T
    Hc = a * I3 + np.conj(b) * C + b * C.conj().T   # b -> conj(b)
    passed.append(check(
        "A1 GAP A: b->conj(b) is SPECTRUM-PRESERVING (emergent-time is conjugation-EVEN) -> blind to arg(b) -> K-reality (delta=0) NOT derivable, it is POSITED",
        np.allclose(np.sort(np.linalg.eigvalsh(H)), np.sort(np.linalg.eigvalsh(Hc))),
        "K is automatic on the whole cone (holds at r=1 too) -> no selective info; = the delta=0/det_C pin relabeled"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT (einselection, wf_bfb916fc): einselects_2sector_r_half_derived_modulo_k_reality. The PARTITION")
    print("half is SOUND: K-real C_3-invariant einselection kills the r=0 three-mode partition and gives the 2")
    print("real-irreducible blocks -- reducing it to ONE physical predicate (is the coupling time-reversal-real).")
    print("BUT two gaps: (A) K-reality is POSITED (emergent-time is conjugation-EVEN, blind to arg(b)); (B) even")
    print("granting the 2 blocks, H is ALREADY block-diagonal -> einselection is a no-op on the power ratio, and the")
    print("genuine Born/second-law max-entropy weights by DIMENSION -> r=1, NOT r=1/2 (the prior 'thermalizing->r=1/2'")
    print("used the NON-Born block-counting entropy). NET: r=1/2 reduces to TWO physical inputs -- K-reality (-> 2-block")
    print("partition) + equal-power-per-block vs dimension (-> r=1/2 vs r=1) -- both standing gates, both = Koide's free fit.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
