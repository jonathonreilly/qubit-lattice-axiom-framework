# Doubling corollary check

Provenance: a fresh-context checker of the same model family. chk1, chk2 and chk4 use the independent rebuild `B7_check/chk_core.py`. chk3 uses `B18_check/chk_model.py`, which copies the runner's construction and so is not independent of the runner. Saved by the supervisor from the hand-back. All scripts PASS (chk1 9, chk2 8, chk3 3, chk4).

**Verdict:** the parity argument is correct. Six wording fixes are needed, none to the logic.

1. **Logic.**
   - Local constancy needs only continuity, so summable hopping suffices.
   - T³ minus finitely many points is connected, so n cannot jump by 2 at isolated points.
   - Evenness holds at the 8 points fixed by both C2s (checked exhaustively).
   - The count is odd next to k*, given: E of multiplicity exactly 2 at k*, zero tilt, and nonzero linear splitting.
   - −k* plays no role.
   - **Strengthening:** S_E must separate k* from every cube point not at E. So if S_E is finite, E is attained at all eight cube points. This is the step analogue of C20.
2. **Hypotheses.**
   - Some E′ is needed (a weaker non-separation condition suffices).
   - "Exactly 2-fold" means E has multiplicity 2 in spec W(k*); a 4-fold level at E can give an even count.
   - Under D2 alone, "an exactly 2-fold level" suffices.
3. **Tilt: correct.** The C2s act linearly on q by diag(±1), so t = 0 (≤ 2.4e−14 numerically). Wording: "one branch lies below E in every direction with nonzero linear splitting".
4. **Hamiltonian version: correct.** No E′ is needed. Pocket-free ⇒ μ at all eight points.
5. **Corrections.**
   - (1) "At odd filling all eight touch": at odd ν, bands ν and ν+1 touch at all eight points (B7 T2, pointwise). Only in a pocket-free state is the Fermi-level content of 1 + 3 form.
   - (2) "A touching at k* is isotropic" holds for 2-fold (E1/2 or E5/2) touchings only. 4-fold G3/2 touchings are generically anisotropic, with spread 0.026–0.26. The D4 axis assignment was confirmed independently.
   - (3) "Pocket-free" in the Hamiltonian line.
   - (4) The doubler-free contrapositive: the step has no quasi-energy gap (every quasi-energy is attained).
   - (5) Eight-node step: "hypothesis not established" → "hypothesis fails". chk3 certifies that every quasi-energy is attained (Bauer–Fike edge certificate at N = 24, 48, 64, with a negative control).
   - (6) Optional: relax finite range to continuity; add the S_E-finite strengthening.
6. **Numerics.**
   - Gapped examples with certified gaps:
     - A: O-symmetric, quasi-local, exp(−iτH);
     - B: D2-symmetric, range 2.
   - In both, all 8 doublets satisfy the counts and are attained elsewhere, on Fermi pockets around k*. The Hamiltonian version passes too.
   - A gapped, fully O-symmetric, finite-range example with a moving doublet was not built; it needs a k-dependent-spectrum factor such as S.
