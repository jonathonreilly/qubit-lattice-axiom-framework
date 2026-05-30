#!/usr/bin/env python3
"""
Exactness press (workflow wf_53b417b9) closure of the charged-lepton Koide VALUE
question. 7 angles, 0 native exact-forcings survived. Verified here.

THE QUESTION: the observed operator sits at Q=2/3 to ~1e-5. What forces it EXACTLY?
THE ANSWER: no native mechanism forces exact 2/3. The native covariant measure
CENTERS on 2/3 (median / ratio-of-expectations) but does NOT concentrate; exact
2/3 is the chiral CONSTRAINT (the import); and the data does not even demand
exactness (0.91 sigma).

Three verified facts:

(1) The covariant matrix-field measure e^{-Tr(M^2)/2} (Tr(M^2)=lambda0^2+2 lambda1^2,
    correct doublet multiplicity) CENTERS on 2/3: median Q=0.667, equal expected
    block masses (<lambda0^2>=<2 lambda1^2>=1). BUT per-config Q is Cauchy-broad --
    only ~5% of configs land in [0.6,0.7], and P(|Q-2/3|<1e-2)~1%. So 2/3 is the
    MEDIAN/center, NOT a concentration: the measure does not force the observed
    1e-5 sharpness (it is measure-zero in the per-config distribution).

(2) EXACT 2/3 comes only from the per-operator chiral CONSTRAINT {M,Gamma_chi}=0
    (retained koide_anticommuting_operator_derivation_theorem) -> <v|Gamma_chi|v>=0
    -> Q=2/3 exactly, theta-independent. Gamma_chi=(2/3)J-I is the generation
    grading: NON-native (retained_bounded no-go koide_z3_equivariant_anticommuting_
    no_go), and the SAME import as the open generation-ID chirality gate.
    CORRECTION: the EIGENVECTOR balance <v|Gamma_chi|v>=0 (-> 2/3) is NOT the
    operator trace condition Tr(M*Gamma_chi)=0 (which gives -a+4b=0 -> b/a=1/4 ->
    Q=0.375). 2/3 needs the eigenvector cone condition, not the operator trace.

(3) Data does NOT require exactness: Q_obs=0.66666051, |Q-2/3|=6.16e-6=0.91 sigma
    (m_tau-limited). 'Q approx 2/3' (the measure median) fits within ~1 sigma.

VERDICT (whole value question): the native covariant measure RANKS/centers toward
2/3 (import-free, modulo the doublet-multiplicity-2 block-count weighting, which is
audit-open) -- and that 'approx 2/3' is all the data demands. EXACT 2/3 reduces
cleanly to the chiral import (= the generation-ID chirality gate). NEXT PATHS (not
closure): (a) derive the doublet-multiplicity-2 (block) weighting from the Cl(3)
qubit / OS measure -> would make the native 2/3-ranking forced, and exactness a
non-question; (b) a variational functional whose SADDLE (not expectation) sits at
b/a=1/sqrt2 (the only native saddle is currently b=0).
"""

import numpy as np


def sep(t):
    print("\n" + "=" * 72); print(t); print("=" * 72)


def main():
    rng = np.random.RandomState(3)
    N = 2_000_000
    a = rng.randn(N) / np.sqrt(3); b = rng.randn(N) / np.sqrt(6)
    ev0 = a + 2 * b; ev1 = a - b
    Q = (ev0 ** 2 + 2 * ev1 ** 2) / (ev0 + 2 * ev1) ** 2

    sep("(1) covariant measure CENTERS on 2/3 (median) but does NOT concentrate")
    print(f"   median Q = {np.median(Q):.4f}  (2/3 = {2/3:.4f})")
    print(f"   equal expected block mass: <ev0^2>={np.mean(ev0**2):.3f}, <2 ev1^2>={np.mean(2*ev1**2):.3f}")
    print(f"   fraction in [0.6,0.7] = {np.mean((Q>0.6)&(Q<0.7))*100:.1f}%  (Cauchy-broad, no concentration)")
    print(f"   P(|Q-2/3|<1e-2) = {np.mean(np.abs(Q-2/3)<1e-2)*100:.1f}%  -> 1e-5 sharpness is measure-zero")

    sep("(2) exact 2/3 = the chiral constraint; traceless correction")
    J = np.ones((3, 3)); I = np.eye(3); Gx = (2 / 3) * J - I
    print(f"   eigenvector balance <v|Gamma_chi|v>=0 -> Q=2/3 (retained anticommuting theorem).")
    print(f"   NOT the operator trace: Tr(I*Gx)={np.trace(I@Gx):.0f}, Tr((J-I)*Gx)={np.trace((J-I)@Gx):.0f}")
    print(f"   -> Tr(M*Gx)=-a+4b=0 -> b/a=1/4 -> Q={1/3+2/3*(1/16):.4f} (NOT 2/3). Trace cond != cone cond.")
    print(f"   Gamma_chi=(2/3)J-I is NON-native (retained_bounded no-go) = the generation-ID chiral import.")

    sep("(3) data does not demand exactness")
    me, mmu, mt, dmt = 0.51099895, 105.6583755, 1776.86, 0.12
    Qf = lambda m: np.array([me, mmu, m]).sum() / np.sqrt([me, mmu, m]).sum() ** 2
    print(f"   Q_obs={Qf(mt):.8f}, |Q-2/3|={abs(Qf(mt)-2/3):.2e}={abs(Qf(mt)-2/3)/abs((Qf(mt+dmt)-Qf(mt-dmt))/2):.2f} sigma")

    sep("VERDICT")
    print("  No native EXACT forcing. Native covariant measure CENTERS on 2/3 (median, import-free,")
    print("  modulo the audit-open block-count weighting) -- and 'approx 2/3' is all the data needs.")
    print("  EXACT 2/3 reduces to the chiral import (= generation-ID gate). NEXT: derive the block")
    print("  weighting from the Cl(3)/OS measure (-> native rank forced); or find a saddle at b/a=1/sqrt2.")


if __name__ == "__main__":
    main()
