# P-FLUX Matter-Content Route Narrow No-Go

**Date:** 2026-06-10
**Type:** no_go
**Claim type:** no_go
**Claim scope note:** narrow finite-volume no-go for one route to the P-FLUX
selector. On the two nearest-neighbor flux branches tested here, the
matter-content generation-carrier battery is satisfied by both the flux
`-1` Kawamoto-Smit branch `K1` and an embedded zero-mode carrier inside the
flux `+1` scalar branch `K0`. Therefore that battery does not select
`phi = -1`.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/p_flux_selection_check_2026_06_10.py`](../scripts/p_flux_selection_check_2026_06_10.py)
(`TOTAL: PASS=36 FAIL=0`).
**Runner cache:**
[`logs/runner-cache/p_flux_selection_check_2026_06_10.txt`](../logs/runner-cache/p_flux_selection_check_2026_06_10.txt).

---

## Question

The kinetic-class surface has two branch representatives:

```text
K0: uniform plaquette flux +1, scalar nearest-neighbor hopping
K1: uniform plaquette flux -1, Kawamoto-Smit sign hopping
```

The question tested here is deliberately narrow: can the existing
matter-content/observable carrier package select `K1` over `K0`?

The tested package is encoded as a kernel-sector realization predicate `G`.
For a branch hopping operator `h`, `G(h)` means that the zero-mode sector of
`h`, with allowed site-local `U(1)` dressings of translations and `C3[111]`,
carries:

- the full Klein cube `{+-1}^3` with multiplicity one;
- Hamming grading `1+3+3+1`;
- `C3[111]` cycling of the carrier lines;
- the `hw=1` joint characters
  `(-1,+1,+1)/(+1,-1,+1)/(+1,+1,-1)`;
- a diagonal commutant of dimension 3 on the `hw=1` triplet;
- `M_3(C)` generation from projectors plus `C3`, with no proper quotient and
  observable-stable count `3`;
- a non-per-site chirality realizing the complementation involution;
- carrier canonicity: exactly one embedded pi-cube when the carrier exists.

`G` is a declared realization reading for this finite kinetic test. It is not
itself asserted as an axiom, primitive, or already-supplied physical
requirement.

## Result

The runner certifies:

1. `K1` satisfies `G` at `L = 4` and `L = 8`; its kernel is exactly the
   8-line carrier.
2. `K0` also satisfies `G` at `L = 4` and `L = 8`; its kernel strictly
   contains a unique embedded pi-cube carrier satisfying the same battery.
3. The tested branch-separating observables are not the generation-carrier
   package. They are kinetic-order data:
   - kernel growth: `K0` zeros grow `20 -> 68`, while `K1` stays `8 -> 8`;
   - carrier exactness: `ker(K1) = carrier`, while `ker(K0)` strictly
     contains the carrier plus extra zero modes.

Therefore the matter-content route does not select `phi = -1` on this
surface. Any future P-FLUX selection through this neighborhood must supply
some additional requirement that distinguishes the full kernel, such as a
point-like zero set, `ker = carrier`, no extra massless sectors, or a
branch-neutral transfer/positivity theorem. This note supplies none of those
requirements.

## Computed Witness

The important positive witness is on `K0`. At `4 | L` with periodic boundary
conditions, the `K0` zero-mode sector contains exactly one embedded pi-cube at
momenta `(+-pi/2, +-pi/2, +-pi/2)`. On that 8-line subspace, after the
global per-direction phase choice used by the runner, all carrier-battery
items match the `K1` carrier. The extra `K0` zero modes sit outside that
carrier; the battery tested here does not see them.

This is why the no-go is route-scoped rather than global. The computation
does not say `K1` is unselectable. It says that this matter-content battery is
not the selector.

## Boundaries

- Finite-volume scope: `L = 4, 8` for the positive certificates, plus `L = 6`
  as a shared wrap-sensitivity leg. Infinite-volume and boundary-condition
  classification are not claimed.
- `G` is a declared kernel-sector realization predicate. The note does not
  derive that this predicate is the physical bridge from abstract carrier rows
  to realized dynamics.
- The mass-pattern side of the matter sector is out of scope. The battery
  here tests the massless zero-mode carrier only.
- The note does not use species names as selectors. The embedded `K0` carrier
  is canonical by computed uniqueness.
- This note adds no framework premise, primitive, controlled-data action,
  accepted-premise change, empirical input, probability rule, weighting rule,
  or audit verdict.

## No-Go Discipline Gate

- **N1 alternative routes:** Matter-content carrier battery is tested and
  fails to select because both branches pass `G`. Symmetry, hermiticity, and
  fermion-parity grading are re-certified as tied. Single-clock/transfer,
  positivity, point-like zero set, and kernel-exactness are separate routes;
  they are not closed here and remain named escapes.
- **N2 wall independence:** The two separating observables are independent
  computed facts: zero-set growth and `ker = carrier`. Either could become a
  selector if separately supplied as a physical requirement; neither follows
  from the generation-carrier battery.
- **N3 hidden-wall scan:** The load-bearing hidden candidate is `G`; it is
  explicit and declared. The finite-volume/wrap convention, dressing class,
  and carrier canonicity assumptions are also explicit.
- **N4 residual matching:** The surviving residual is the kinetic-order
  selector: point-like zero set or no extra massless sectors. The matter
  content route is closed only because it does not distinguish those
  residuals.
- **N5 rhetoric audit:** "Does not select" means "does not select through the
  tested matter-content battery on the tested finite surfaces." It does not
  mean `K1` is wrong, unphysical, or underivable.
- **N6 partial-closure scan:** A later theorem could close the route by
  deriving point-like zero sets, deriving `ker = carrier`, forbidding extra
  massless sectors, or deriving a branch-neutral transfer/positivity
  principle. This note preserves those partial-closure paths.
- **N7 steelman:** The strongest counterargument is that the physically
  realized matter sector should be the whole kernel, not an embedded carrier,
  so the extra `K0` zero modes should disqualify `K0`. That would select
  `K1`, but it is precisely an additional `ker = carrier` or no-extra-sector
  requirement, not a consequence of the generation-carrier battery alone.
- **N8 cross-cycle echo:** The shape matches prior selector walls where a
  carrier theorem is true on an abstract or embedded surface but does not
  select the realizing dynamics without an additional bridge. This note keeps
  the bridge as an explicit residual rather than treating it as automatic.

## Runner Checks

The runner checks:

- exact branch construction, plaquette fluxes, cubic rotation group, and
  symmetry/parity ties;
- the full `G` battery on `K1` at `L = 4,8`;
- the same `G` battery on `K0` at `L = 4,8`;
- carrier canonicity for both branches;
- non-vacuity via an anisotropic comparator that fails the battery;
- frame robustness under a deterministic site-local `U(1)` gauge, where the
  bare battery fails and the dressed witness passes;
- shared wrap sensitivity at `L = 6`;
- the two separating observables: zero growth and `ker = carrier`.

## Falsifiers

- A failure of any `G` battery item on the embedded `K0` carrier at the
  certified volumes.
- More than one embedded pi-cube carrier in `K0` at the certified volumes.
- A matter-content requirement among the linked carrier rows that directly
  forbids the extra `K0` zero modes without adding a new kernel-exactness or
  point-zero-set premise.
- A branch-neutral theorem, already supplied by linked authorities, that
  requires `ker = carrier` or point-like zero sets.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) supplies the
  `Z^3` finite lattice and one-qubit local target.
- [U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md](U4_CLOSES_UNDER_QUBIT_REFRAME_NARROW_THEOREM_NOTE_2026-05-20.md)
  supplies the single-mode per-site surface used for the one-particle hopping
  blocks.
- [TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md](TENSOR_PRODUCT_TRANSLATION_FERMION_OPERATOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-25.md)
  supplies the finite periodic Fock/translation setting whose one-particle
  bilinear blocks are tested here.
- [STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
  supplies the named two-branch P-FLUX surface; this runner reconstructs the
  branch representatives directly.
- [STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP3_BZ_CORNER_HAMMING_ORBIT_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies the Klein-cube Hamming and `C3` carrier battery items.
- [STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md](STAGGERED_DIRAC_SUBSTEP4_AC_LAMBDA_SIMULTANEOUS_DIAGONALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md)
  supplies the commuting-translation triple and simultaneous-diagonalization
  battery items.
- [THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the `hw=1` distinct-character battery item.
- [THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
  [THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md),
  and
  [THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md](THREE_GENERATION_OBSERVABLE_COUNT_COROLLARY_NOTE_2026-05-03.md)
  supply the `M_3(C)`, no-proper-quotient, and count `3` battery items.
- [FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
  supplies the parity-grading tie check.
- [NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md)
  supplies the non-per-site chirality boundary respected by the battery.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
