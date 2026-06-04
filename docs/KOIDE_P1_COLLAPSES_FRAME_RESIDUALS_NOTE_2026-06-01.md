# Microcausality/Reflection-Positivity Localizes Carrier-Frame Residuals Without Forcing Faithfulness

**Date:** 2026-06-01
**Claim type:** bounded_theorem
**Claim boundary:** bounded localization. If the faithful spin-1/2 matter
representation is supplied, positive-energy quantization selects CAR over Bose
occupation; microcausality/reflection positivity still admits the trivial
scalar. This note does not audit or promote the spin-statistics/OS
reconstruction rows, force faithfulness, or set an audit verdict.
**Primary runner:**
`scripts/frontier_koide_p1_collapses_frame_residuals.py`
with cache
`logs/runner-cache/frontier_koide_p1_collapses_frame_residuals.txt`
(10/10 checks).

## The convergence

Two carrier-frame residuals point at one constraint:

- **Faithful boost representation (local label: G1; see
  `KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01`):**
  faithfulness — matter in the boost-acting Weyl rep vs the trivial scalar
  `J=K=0`. The boosts are *derived* single-site (Grassmann-free); only the
  faithful-over-scalar *selection* is posited.
- **Fermionic statistics / cross-site hopping sign (local label: L1; see
  `KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01`):**
  statistics — fermionic/CAR vs the hard-core boson (the cross-site hopping sign).

Both ask whether microcausality / reflection-positivity / spin-statistics on the
matter operator `M` closes them.

## Result: one conditional collapse, but not zero residuals

**(A) The conditional collapse is correct physics.** Given the faithful spin-½
Weyl representation, the Dirac spectrum is `±E` (doubly degenerate). Bose-quantizing the
negative-energy mode is **unbounded below** (`min H → −∞` with occupation cap),
while CAR is bounded (`H ≥ 0`) — so **CAR is the unique positive-energy
quantization** of the faithful spin-½ rep (runner §A). Statistics is the
*conclusion*, not an input (non-circular). So the statistics posit follows from
the faithful-representation posit, conditionally collapsing those two frame
posits to **one (faithfulness)**.

**(B) But the collapse is tier-conditional — the current retained surface does not
exclude the hard-core boson.** The retained cardinality core
(`spin_statistics_cardinality_pauli_exclusion`) excludes only the **free/soft CCR**
boson (`[a,a†]=I` needs infinite dimension: `Tr[a,a†]=0 ≠ Tr(I)=D`). The
**hard-core** boson `b=σ_+` has `[b,b†]` traceless (≠ I), so it **evades** that
argument; and on a single site `b` is literally the *same* 2×2 matrix as the
fermion `c` (both `σ_+`, both `(·)²=0`) — the criterion is **blind** to it
(runner §B). The carrier-level forcing of CAR-over-hard-core-boson therefore rides
**unaudited** rows (`axiom_first_spin_statistics_theorem`,
`free_field_os_wightman_reconstruction`, `free_sector_spin_statistics_level1` —
all unaudited on the live ledger). So the collapse is real modulo independent
audit, but not retained-load-bearing; on the retained-only tier the two posits
stay independent.

**(C) Microcausality/reflection positivity does not force faithfulness — the scalar is admitted.**
The trivial scalar `J=K=0` is a healthy free field: **positive-energy**
(`ω_k>0`), **microcausal** (equal-time field bracket vanishes spacelike), and
**reflection-positive** (the OS-reflected Källén–Lehmann kernel is PSD, the
canonical Glimm–Jaffe RP theory; runner §C). RP is a property of a *given*
measure, and the free-scalar measure is reflection-positive — so RP cannot exclude
a rep whose 2-point function is itself RP. The constraint admits the scalar, and
faithfulness survives untouched as the **lone irreducible frame posit**.

## What is *not* claimed (honesty)

The bounded-local microcausality of gauge-invariant observables is **statistics-
blind only as a spectrum statement**: the nearest-neighbour bilinear has the
*same spectrum* in the fermion (JW-string) and hard-core-boson frames (they differ
by the JW-string unitary; runner §D), so bounded-local microcausality cannot reach
the field-bracket exchange sign. This note does **not** claim the
Lieb–Robinson commutators are byte-identical (they are not — the two Hamiltonians
generate different dynamics on the number operators); only the *spectrum* /
unitary-relabel statement is used.

## Net and the next path

The carrier frame goes from **two posits to one (faithfulness)** conditionally,
modulo auditing the spin-statistics / OS-reconstruction step (currently
unaudited). On the retained-only tier, two posits remain. The
microcausality/reflection-positivity constraint **never reaches zero**: the
scalar is admitted, so faithfulness is the single
irreducible frame posit no microcausality / RP / positive-energy constraint on a
single matter field excludes.

Two concrete fronts: **(1)** **audit** the matter-2-point exchange-sign
forcing — ratify `axiom_first_spin_statistics_theorem` S2 and
`free_field_os_wightman_reconstruction` (closing its open lattice↔continuum and
`1+1d → 4D` gates) — which would make the conditional collapse reusable after
independent audit; **(2)** the **single auditable frontier** then becomes
*faithful-Weyl-over-scalar*, untouched by the same constraint that admits the
scalar, to be pursued through M's own spin content / the `so(3,1)`
carrier-assignment, not through microcausality.

## Non-circularity

No `Q=2/3`, no fermionic frame, no faithful rep is assumed: the Dirac forcing is
the c-number spectrum content of the spin-½ rep (statistics is derived, not
input); the scalar's RP/positive-energy/microcausality are computed directly
(runner).

## Load-bearing authorities

[SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md](SPIN_STATISTICS_CARDINALITY_PAULI_EXCLUSION_NARROW_THEOREM_NOTE_2026-05-10.md),
[REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md),
[FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md),
[INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
and
[STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md).

Non-load-bearing audit targets named above remain plain text:
`axiom_first_spin_statistics_theorem`,
`free_field_os_wightman_reconstruction`, and
`free_sector_spin_statistics_level1`.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [axiom_first_spin_statistics_theorem_note_2026-04-29](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md)
