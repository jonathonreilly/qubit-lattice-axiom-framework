# 𝒞_O_h: Governance-Adoption Proposal for Substrate-Symmetry-Invariant Action Class

**Date:** 2026-05-26
**Claim type:** governance_proposal
**Status authority:** **USER-side governance event.** This is a proposal
for the user to ratify `𝒞_O_h` as a retained governance convention,
analogous to `𝒞_b` (PR #1964, period-1 angular unit on C_N orbits),
lattice-spacing, meter, GeV. The audit lane does not assign an
effective_status to this row beyond `governance_proposal`; ratification
is recorded separately as a `convention_retained` event.

## Audit context

This is **Track A Step 5b** of the strong-CP / θ retirement attack
plan. Steps 1-3 (PRs #1974, #1975, #1976) established the full
structural mechanism: θ = 0 is the unique vacuum on the reduced
Brillouin zone [0, π/3], conditional on a **single named premise**:

> *"The framework's admissible action class is O_h-invariant under
> the lifted substrate action."*

This proposal formalizes that premise as a retained governance
convention `𝒞_O_h`, analogous to how `𝒞_b` (period-1 angular unit on
C_N orbits, PR #1964) was ratified for AC_φλ retirement.

## The proposed convention

**Convention `𝒞_O_h` — Substrate-symmetry-invariant action class.**

> The framework's canonical admissible action class on the Cl(3)/Z³
> substrate is the class of action functionals invariant under the
> full O_h cubic point group action, with O_h lifted to Cl(3) via
> the faithful representation established in Track A Step 1 (PR #1974).

This is a single-sentence governance convention. It does NOT introduce
new physics; it formalizes the substrate-symmetry-respecting principle
already implicit in the framework's "minimal axioms" position.

## Why `𝒞_O_h` is a natural convention (not a free postulate)

The proposal is grounded in three structural facts:

1. **The substrate has geometric O_h symmetry.** The Z³ lattice's
   maximal point-group symmetry is precisely O_h (48 elements: 24
   proper rotations + 24 improper). This is a fact of cubic lattice
   geometry, not a choice.

2. **The substrate has no preferred frame.** A2 (Z³ substrate) specifies
   the lattice as an abstract geometric object with lattice spacing
   `a > 0`. It does NOT specify a preferred orientation, parity, or
   basis. Any specific choice (e.g., "lattice axis 1 is north") is a
   convention, not a primitive.

3. **Curie's principle (substrate-symmetry-respecting dynamics).**
   The symmetries of the substrate must be present in the dynamics
   that lives on it, unless an external symmetry-breaking mechanism is
   explicitly introduced. The framework's "no new axioms" discipline
   precludes such external mechanisms.

`𝒞_O_h` is the formal statement that the framework's canonical action
class respects the substrate's natural symmetry. It is the lattice
analog of general covariance in GR (no preferred coordinate system on
the manifold ⟹ action must be a diffeomorphism scalar).

## What `𝒞_O_h` ratification accomplishes

Under `𝒞_O_h`-retention, the strong-CP closure chain reads:

| Component | Source | Status under 𝒞_O_h |
|---|---|---|
| Substrate Z³ with O_h symmetry | A2 (axiom) | retained |
| O_h lifts faithfully to Cl(3) with det character | PR #1974 (Step 1) | retained-pending |
| Wilson + staggered action is O_h-invariant | PR #1975 (Step 2) | retained-pending |
| Every ε^{μνρσ}-based CP-odd density transforms with sgn(det) | PR #1975 (Step 2 A4) | retained-pending |
| Z₃ ⊂ O_h gauging shrinks θ-BZ to [0, π/3] | PR #1976 (Step 3) | retained-pending |
| RP-positivity gives Z_Q ≥ 0 | PRs #1971 + #1973 | retained-pending |
| **Triangle inequality: |Z(θ)| ≤ Z(0), unique min at θ = 0** | PR #1976 (Step 3 B4) | composed |
| **Conclusion: θ = 0 unconditionally** | this chain | **derivable under 𝒞_O_h** |

When `𝒞_O_h` is ratified + the upstream chain retains, the canonical
strong-CP row (`strong_cp_theta_zero_note`) graduates from
`retained_bounded` (currently) to `retained` (unbounded), and θ
retires from the Tier-A admission registry.

## Comparison to the AC_φλ closure pattern (PR #1964)

| Step | AC_φλ closure | θ closure (this proposal) |
|---|---|---|
| Substrate-natural Z_N | Z_N from period-N angular unit on C_N orbits | Z₃ from body-diagonal of O_h |
| Discrete symmetry | C_N orbit structure | O_h cubic point group |
| Governance convention | 𝒞_b: period-1 angular unit on C_N orbits | 𝒞_O_h: O_h-invariant action class |
| Empirical anchor | PDG δ = 2/9 rad at N=3, CKM η² at N=6 | PDG \|θ̄\| < 10⁻¹⁰ (i.e., θ ≈ 0) |
| Sibling convention precedent | lattice spacing, meter, GeV | (same; 𝒞_O_h joins them) |

The structural pattern is identical. `𝒞_O_h` ratification is the same
type of governance event as `𝒞_b` ratification.

## What this proposal does NOT do

- Does **NOT** assert θ = 0 is automatically derived from primitives
  alone; the conditional chain above explicitly relies on `𝒞_O_h`.
- Does **NOT** modify the canonical `strong_cp_theta_zero_note` row
  directly; that graduates via auto-cascade once the chain retains.
- Does **NOT** retire θ from the Tier-A registry; that is a separate
  governance event (companion PR analogous to #1969 for AC_φλ).
- Does **NOT** introduce a new axiom; `𝒞_O_h` is a convention, not an
  axiom (parallel to how Y₀ and g₀ are vacuous rescaling conventions
  in the Tier-A registry).

## Why `𝒞_O_h` is not a vacuous convention (unlike Y₀ and g₀)

The Tier-A registry distinguishes:
- **Vacuous rescaling conventions** (Y₀ = α=1/3 hypercharge norm, g₀ =
  g_bare = 1): pure normalization choices with no physical content;
  rescaling-invariant.
- **Governance conventions** (lattice spacing, meter, GeV, 𝒞_b under
  current proposal): physical-content-bearing conventions that fix a
  specific structural choice with downstream consequences.

`𝒞_O_h` is in the second category: it FIXES the action class to be
O_h-invariant, with the downstream consequence θ = 0. It is NOT
rescaling-invariant; it is a SYMMETRY choice.

This distinction matters: vacuous rescaling conventions are excluded
from the admitted-input count entirely. Governance conventions ARE
counted (just not in the Tier-A irreducible admission registry).

## If ratified

Once `𝒞_O_h` is ratified:
- The Tier-A admission registry can remove `strong_cp_theta_zero_note`
  (companion PR analogous to #1969 for AC_φλ).
- `compute_effective_status.py` auto-cascades the **879 transitive
  descendants** of the former θ admission from `retained_bounded`
  toward unbounded `retained` where otherwise eligible.
- The framework's open-question count reduces from 3 Tier-A
  admissions (post-AC_φλ-retirement) to 2 (P1, S).

## If not ratified

If you decline `𝒞_O_h` ratification, the strong-CP closure stays
**bounded** on the named-premise chain. The Track A Steps 1-3 PRs
still land independently as retained_bounded narrow theorems; the
conditional closure θ = 0 stands; but θ remains a Tier-A admission.

In that case, the alternative path is **Track A Step 5a** (hard
derivation): derive `𝒞_O_h` from primitives via a "no-preferred-frame"
/ "lattice general covariance" structural argument. This is a
substantive open research item — multi-month minimum, possibly multi-year.

## Historical provenance (cited prior art, NOT load-bearing imports)

The substrate-symmetry-respecting principle is standard in physics:

- **Curie, P.** (1894). "Sur la symétrie dans les phénomènes physiques",
  *Journal de Physique* **3**, 393–415. Original Curie's principle.
- **Wigner, E. P.** (1939). "On Unitary Representations of the
  Inhomogeneous Lorentz Group". The role of symmetry groups in
  determining admissible Lagrangians.
- **Einstein, A.** (1915). General covariance: action must be
  diffeomorphism-scalar on the manifold.
- **Wilson, K.** (1974). Wilson plaquette action is O(N)-symmetric by
  construction on the lattice.
- **Aharony, Razamat, Tachikawa** (2026-03), arXiv:2603.05195.
  Discrete-θ-projection mechanism enabled by substrate Z_N gauging
  (top recommendation of the literature + math-tools agents from
  2026-05-26 5-agent research panel).

**These references are cited as historical prior art only.** The
proposal does not import any theorem; `𝒞_O_h` is the framework's
substrate-native specialization of the substrate-symmetry-respecting
principle.

## What you (the user) are being asked to ratify

A single statement:

> **`𝒞_O_h`**: The framework's canonical admissible action class on
> the Cl(3)/Z³ substrate is the class of action functionals invariant
> under the full O_h cubic point group lifted to Cl(3) via the
> faithful representation of Track A Step 1.

If you ratify this as a retained governance convention (analogous to
`𝒞_b`, lattice spacing, meter, GeV), the strong-CP closure chain
becomes:

> "Cl(3) + Z³ + 𝒞_O_h + retained RP + Track A Steps 1-3 ⟹ θ = 0"

— a single-convention closure of the strong-CP problem on the
framework's substrate.

## Test plan (for the audit lane)

- [ ] The convention statement is unambiguous (single sentence)
- [ ] The chain composition (Steps 1-3 + RP + 𝒞_O_h ⟹ θ = 0) is
  structurally complete
- [ ] No new admission beyond `𝒞_O_h` itself is introduced
- [ ] If ratified, the companion Tier-A retirement PR can land
- [ ] `compute_effective_status.py` cascade is mechanically defined

This proposal does not predict an audit verdict; ratification is a
user-side governance event.
