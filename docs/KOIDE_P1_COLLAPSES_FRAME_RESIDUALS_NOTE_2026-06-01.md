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
(11/11 checks).

## 2026-06-13 current-grade source repair

The original note described the spin-statistics/OS leg as unaudited. On the
current audit ledger, the directly cited spin-statistics, reflection
positivity, free-Dirac, CPT, no-forcing, and `GL(F)` support rows are retained
or retained_bounded. The honest current reading is therefore:

- the finite positive-energy/CAR-over-Bose collapse is bounded support on the
  supplied faithful spin-1/2/free-field surface;
- the collapse does **not** force the faithful representation itself, because
  the scalar branch remains positive-energy, microcausal in its own frame, and
  reflection-positive;
- the result is not an unbounded interacting-field spin-statistics theorem and
  does not close the framework matter-operator identification by itself.

Thus the statistics residual can be treated as bounded-localized behind the
faithfulness posit on the cited retained/bounded support surface, while
faithful-Weyl-over-scalar remains the surviving frontier blocker.

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

**(B) What the retained/bounded support does and does not reach.** The retained cardinality core
(`spin_statistics_cardinality_pauli_exclusion`) excludes only the **free/soft CCR**
boson (`[a,a†]=I` needs infinite dimension: `Tr[a,a†]=0 ≠ Tr(I)=D`). The
**hard-core** boson `b=σ_+` has `[b,b†]` traceless (≠ I), so it **evades** that
argument; and on a single site `b` is literally the *same* 2×2 matrix as the
fermion `c` (both `σ_+`, both `(·)²=0`) — the criterion is **blind** to it
(runner §B). The current retained/bounded support rows now justify the
CAR-over-Bose collapse on the supplied faithful spin-1/2/free-field surface,
but not as a Record-native proof of the faithful representation or as a full
interacting-field OS/Wightman theorem. The finite collapse is therefore
bounded support behind the faithfulness posit, not zero residuals.

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

The carrier frame goes from **two posits to one (faithfulness)** on the
current retained/bounded support surface. The
microcausality/reflection-positivity constraint **never reaches zero**: the
scalar is admitted, so faithfulness is the single
irreducible frame posit no microcausality / RP / positive-energy constraint on a
single matter field excludes.

The concrete remaining front is now **faithful-Weyl-over-scalar**: the same
constraint that admits the scalar cannot decide it, so the next attack must
run through M's own spin content / the `so(3,1)` carrier-assignment, not
through microcausality or RP alone.

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
- [staggered_dirac_substep1_statistics_gl_f_conditional_discriminator_bounded_theorem_note_2026-06-10](STAGGERED_DIRAC_SUBSTEP1_STATISTICS_GL_F_CONDITIONAL_DISCRIMINATOR_BOUNDED_THEOREM_NOTE_2026-06-10.md)
