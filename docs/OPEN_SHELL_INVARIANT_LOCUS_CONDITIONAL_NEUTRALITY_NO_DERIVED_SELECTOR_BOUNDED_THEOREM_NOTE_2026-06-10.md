# The Open-Shell Selection Restructures: Conditional on the Invariant Locus, Neutrality Holds with Zero Further Admissions — and Nothing Derived Selects Either Way

**Date:** 2026-06-10
**Type:** bounded theorem (retire-mode; restructures admission (B)'s open-shell residual; panel-narrowed)
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.py`
**Cache:** `logs/runner-cache/frontier_open_shell_invariant_locus_no_derived_selector_2026_06_10.txt`
**Status:** source proposal; the audit lane grades. Runner `PASS=17 FAIL=0`, exact, no MC.
A mandatory 4-lens adversarial panel returned `land_with_edits`; **all five required edits
are applied** (the conditionalization, the continuity restatement, the all-site separator,
the instance-artifact labeling, and the exhibit-disclosure/novelty narrowing below).

## The residual under attack — and what is NOT resolved here

The admission-(B) program left the open-shell residual as *"which `ρ_color` spectrum on
the degenerate ground manifold"* (#3474-T3b; on `Z³`, half filling is generically
open-shell; the G3 guard re-opens there). This note **restructures** that residual.
**It does not resolve it**: which locus the realized state occupies remains the full
remaining residual, fully open. What changes is its *shape*: one locus is now proved
admission-free and dynamically stable, the departure from it is a registrable continuous
order parameter, and nothing derived selects in either direction.

## The theorems (exact — runner `PASS=17 FAIL=0`)

**(T1) Invariant-locus universality** *(the panel upgraded this from two exhibits to a
rigorous decomposition)*. The open-shell ground manifold is SU(3)-invariant as a subspace
and decomposes as **4·singlet ⊕ 2·octet** (Casimir eigenvalues `0×4` and `12×16` in the
un-halved-λ normalization; commutant dimension exactly `4²+2²=20`, computed). **Every**
SU(3)-invariant density supported on it — the full 20-dimensional commutant, exhausted by
basis and sampled by random invariant PSD states — is neutral at **every** site
(worst all-site deviation `3×10⁻¹⁵`). Mechanism: the block-08 Schur argument (#3445
lineage), here in many-body ground-manifold form — the genuinely new content relative to
the single-/two-carrier results already on main. **The #3474-T3b obstruction is a
property of non-invariant (color-polarized) pure selections, not of the manifold.** (No
thermodynamic limit and no SSB phenomenology are invoked anywhere — this is exact
finite-dimensional linear algebra on a degenerate manifold.)

**(T2) No derived selector.** The named color-diagonal hopping, the color-blind
instrument class, and the count/Casimir conservation laws all **commute exactly** with
the global SU(3) action. Hence: **(a)** the invariant locus is **dynamically stable** —
an invariant state stays invariant through interleaved (Hamiltonian + record) steps
(dev `10⁻¹⁷`), hence stays neutral by T1; **(b)** nothing derived selects *against* the
locus either — color-blind records preserve a non-invariant state's per-site `ρ_color`
**exactly**, and nothing derived lifts the degeneracy. *Preservation only*, consistent
with blocks 05–07 (derived structure cannot *create* depolarization). The novelty here is
the manifold-invariance and the interleaved propagation — the underlying equivariance
facts were landed in blocks 02/05–07.

**(T3) The registrable order parameter — continuous, all-site.** Define
`D = max_x [Tr(ρ_color(x)²) − 1/3]`: the **worst-site purity excess** — manifestly
SU(3)-invariant (verified `D(gρg†)=D(ρ)` exactly; a max-entry-norm draft form was *not*
unitarily invariant and was caught by the runner's own invariance check), two-copy
estimable (block-04's order parameter, in all-site form — the novelty claimed is only the
branch-detector use). **Invariance ⟹ D=0** (T1); `D>0` certifies departure. And `D` is
**continuous**: the convex family between a non-invariant ground state and an invariant
one sweeps `D` smoothly and monotonically to zero (verified) — so the restructured
residual is **"the invariant locus versus its complement, separated by a continuous
invariant order parameter" — not a binary**. **Panel faithfulness fix:** single-site
readings are *not* faithful — the runner constructs a manifold state whose site-0 purity
excess is an order of magnitude below its all-site `D` — so the separator must be
all-site, as defined.

**(T4) Honesty/teeth.** A non-invariant ground state sits at **exactly** the ground
energy (no derived lifting). Frame-naming instruments break the equivariance (the named
exception — their content is precisely the relative-orientation data of #3478). The
equipartition state `P_gs/20` — **the maximally-mixed invariant state, exactly the kind
of object the G3 guard polices** — appears as an *existence witness only*: no realization
is claimed, no weight is assigned, and it is **not** the Haar twirl of a non-invariant
manifold state in disguise (the broken exhibit's exact group average has a *non-flat*
manifold spectrum, computed — the demoted uniform-weight move is not being applied to
anything). All specific decimals in the checks are **instance/basis artifacts**, not
physical constants (the panel verified they sweep under degenerate-basis rotations).

## What this restructures, and what it does not

- **Restructured:** the open-shell residual was an apparently continuous weight-like
  spectrum selection. It is now: **conditional on the realized state lying in the
  invariant locus, all-site neutrality holds with zero further admissions and persists
  under all derived structure.** Off the locus, departure is registrable by the
  continuous invariant order parameter `D`, whose non-orientation content is exactly the
  orbit-invariant data #3474 priced (the orientation part being relative-only per #3478).
- **Not resolved (stated plainly):** *which* locus the realized state occupies — the full
  remaining residual. Nothing here selects it; no past-hypothesis-style selector is
  invoked (#3461 is respected — the note never claims symmetry of initial conditions pins
  anything); the G3 guard now sits exactly on that one question.
- **Global-side throughout** (admission (B)): the local `{P_r}` root and the
  relative-orientation data (#3478) are untouched, per the global-vs-local boundary. `r`
  is untouched. No new axiom, primitive, measure, or weight. Conditional on the supplied
  `C³` carrier, the named hopping, and the named instrument classes.

## Cross-references

- The residual restructured here: PR #3474 (T3b; **branch-only source proposal** — this
  note stands on the algebra verified in its own runner, not on that note's grade).
- The invariance⟹neutrality mechanism (single-/two-carrier form): campaign block 08
  (PR #3445, on main). The order parameter: block 04 (PR #3431, on main). The
  record-channel one-body rules: block 02 (PR #3425, on main).
- The relative-orientation structure of the non-invariant complement: PR #3478
  (**branch-only source proposal**); the state-orientation retirement on main:
  [`COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_ORIENTATION_OF_THE_STATE_IS_PREDICTIVELY_VACUOUS_NARROW_THEOREM_NOTE_2026-06-09.md).
- The past-hypothesis non-reduction this respects:
  [`COLOR_NEUTRALITY_ENTANGLEMENT_DEPOLARIZATION_IS_GLOBAL_INVARIANT_NOT_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_NEUTRALITY_ENTANGLEMENT_DEPOLARIZATION_IS_GLOBAL_INVARIANT_NOT_CONNECTION_NARROW_THEOREM_NOTE_2026-06-09.md)
  lineage and the block-17 purity result (PR #3461, on main).
- Standard math (method only): Schur's lemma; isotypic decomposition and commutants;
  equivariant channels; two-copy (SWAP-type) invariant estimators.
