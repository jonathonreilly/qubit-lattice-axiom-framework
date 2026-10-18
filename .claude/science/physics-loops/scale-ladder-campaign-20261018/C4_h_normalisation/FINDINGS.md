# C4 findings: does the repo's microscopic realisation fix the scale of h?

Provenance: a worker of the same model family. Checked by a fresh-context same-family agent (`../C4_check/REPORT.md`, PASS=12): the main answer holds, and its corrections are applied below. Saved by the supervisor from the hand-back. Runner: `c4_h_normalisation.py`, exact sympy, PASS=18 FAIL=0 (about 93 s). A 0/0 harness bug log is kept. The file `block120_runner_rerun_tail.log` is actually the 09-25 exact-lattice runner (11/11), not block 120's; the check re-ran block 120's runner at 13/13.

**Answer.** The repo fixes h's scale through the walker's hop, not through a bounded spectrum. That gives a_s = 1 in block-62 variables, but not r = 1.
- The walker fixes K1 (the u·R1 coefficient) relative to α.
- K2 (the TT coefficient) needs one more supplied clause: closure with the walker as matter, or block 64's background-free blind ansatz.

So r = 1, equivalently K1 = K2, is derived only conditionally.

## 1. Microscopic definitions in the repo

- **The axioms memo** supplies only the qubit algebra. Block 62 N7: a qubit algebra does not supply a dynamical frame.
- **Block 62:**
  - The frame E is a supplied real field. H = ½Σ{E^j·σ, S_j} and g^{ij} = ΣE_a^iE_a^j.
  - h = −(ε + εᵀ), and ∂⟨H⟩/∂h_ij = −½Θ_(ij). The member is written in this h.
  - E is an unbounded GL(3) c-number field. P has no microscopic assignment.
- **Block 64:** bond strains; to first order the frame strain is minus the walk's B.
- **Block 120** (lines 65–66, 116–117): "Each is normalised so that the walker sees the member's uniform field: sym P(0) = −½, ΛR(0) = 1", with B = −½φ_j h_ij. This holds only at q = 0.
- **The only bounded-spectrum tensor field** is the separate Z_N clock and slot model (`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`). It is not coupled to the walker: its source is supplied, and the matter map is listed as open. It has an R1-shaped constraint with no coefficient and no lapse. So it cannot fix r.

## 2. Computation

- **A1.** H(k)² = sᵀ(EᵀE)s·1 exactly.
- **A2.** Matching the walker against matter on δ + a h gives a = 1 uniquely (second order checked).
- **A3.** Block 62's source is the unit-strength metric stress.
- **A5.** Two-step coupling: H² = |s|² − a_R PᵀhP, so all eight species see δ + a_R h. Block 120's ΛR(0) = 1 is therefore a_s = 1.
- **A4 (caveat).** The placement matters:
  - site frame: ηhη, with 2 of 8 species seeing δ + h;
  - one-step bond: 1 of 8;
  - only the two-step coupling serves all eight.
- **B2.** At β = −α the lapse identity is ë_u = −(K1 a_s/(4α)) p·Θ·p, with no K2. So "α = K/4" in block 134 T4 and the 09-25 exact-lattice note T4 means K1 = 4α (with a_s = 1).
- **B4.** The TT cone is K2/(4α).
- **B5.** The invariants under Φ_ρ are K1a_s/α, K2/α and K1a_s/K2.
- **B6.** In a static pull, the space-to-time curvature ratio γ = a_s K1/K2 is invariant.
- **C.** R1 and R2 are the first- and second-order parts of √gR[δ+h] with unit coefficients (independent plane-wave route). B21's family is GR on δ + h/r, with a_s = 1/r.

## 3. Verdict

- **Fixed by definition:** a_s = 1 in block-62 variables. It comes from the identification clause g⁻¹ = EᵀE and block 120's stipulated ΛR(0) = 1, so it is not derived (check). It picks the Φ_ρ representative. The invariant statement is K1/K2 = γ_walker.
- **Not fixed:** K2. r = 1 follows from the frame clause plus one of:
  - **(II) Closure with the walker as matter** (continuum, degree ≤ 2, B19/B21 premises): this gives a_s = K2/K1. The walker's own {G, C} with frame coupling has not been computed.
  - **(I) Block 64's background-free ansatz,** which gives −√gR[eᵀe] with a single K. Blindness alone does not suffice: GR on δ + h/r is also blind. The ratio comes from the background-free form, which is supplied.

## Caveats

- The sentence "at α = K/4 the disturbances move at the walker's top speed" (block 62 T4, block 134 T4(a), the 09-25 exact-lattice note T4(b)) relies on those notes' declared single K. With K1 ≠ K2 the TT speed² after lapse matching is K2/(K1 a_s), so "top speed" is equivalent to γ = 1, i.e. r = 1.
- a_s = 1 holds for all species only with the two-step placement at q = 0.
- First order in the fields, plus a second-order check for uniform frames.
