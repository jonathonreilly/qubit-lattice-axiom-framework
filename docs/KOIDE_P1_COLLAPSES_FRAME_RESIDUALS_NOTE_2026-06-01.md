---
claim_id: koide_p1_collapses_frame_residuals_note_2026-06-01
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# P1 collapses the two carrier-frame residuals to one (faithfulness) — modulo auditing spin-statistics; and does not force faithfulness (the scalar is admitted)

**Date:** 2026-06-01
**Claim type:** bounded collapse-theorem + no-go-companion. Adds no axiom and no
import. `Q=2/3` never enters.
**Status authority:** independent audit lane only.
**Primary runner:**
`scripts/frontier_koide_p1_collapses_frame_residuals.py`
with cache
`logs/runner-cache/frontier_koide_p1_collapses_frame_residuals.txt`
(10/10 checks).

## The convergence

Two just-derived carrier-frame residuals point at one constraint:

- **G1 (boost lever, `KOIDE_ONSITE_WEYL_BOOST_FROM_BIVECTORS_NOTE_2026-06-01`):**
  faithfulness — matter in the boost-acting Weyl rep vs the trivial scalar
  `J=K=0`. The boosts are *derived* single-site (Grassmann-free); only the
  faithful-over-scalar *selection* is posited.
- **L1 (locus lever, `KOIDE_CARRIER_LOCUS_DECOMPOSITION_NOTE_2026-06-01`):**
  statistics — fermionic/CAR vs the hard-core boson (the cross-site hopping sign).

Both ask whether **P1** — microcausality / reflection-positivity / spin-statistics
on the matter operator M — closes them.

## Result: P1 collapses two posits to one, but tier-conditionally; and never to zero

**(A) The collapse is correct physics — `L1 ⟸ G1`.** Given the faithful spin-½
Weyl rep (G1), the Dirac spectrum is `±E` (doubly degenerate). Bose-quantizing the
negative-energy mode is **unbounded below** (`min H → −∞` with occupation cap),
while CAR is bounded (`H ≥ 0`) — so **CAR is the unique positive-energy
quantization** of the faithful spin-½ rep (runner §A). Statistics is the
*conclusion*, not an input (non-circular). So **L1 follows from G1** — the two
frame posits collapse to **one (faithfulness)**.

**(B) But the collapse is tier-conditional — on the retained surface P1 does not
exclude the hard-core boson.** The retained cardinality core
(`spin_statistics_cardinality_pauli_exclusion`) excludes only the **free/soft CCR**
boson (`[a,a†]=I` needs infinite dimension: `Tr[a,a†]=0 ≠ Tr(I)=D`). The
**hard-core** boson `b=σ_+` has `[b,b†]` traceless (≠ I), so it **evades** that
argument; and on a single site `b` is literally the *same* 2×2 matrix as the
fermion `c` (both `σ_+`, both `(·)²=0`) — the criterion is **blind** to it
(runner §B). The carrier-level forcing of CAR-over-hard-core-boson therefore rides
**unaudited** rows (`axiom_first_spin_statistics_theorem`,
`free_field_os_wightman_reconstruction`, `free_sector_spin_statistics_level1` —
all unaudited on the live ledger). So `L1 ⟸ G1` is *real-modulo-audit*, not
retained-load-bearing; on the retained-only tier the two posits stay independent.

**(C) P1 does not force G1 — the scalar is admitted, so it never reaches zero.**
The trivial scalar `J=K=0` is a healthy free field: **positive-energy**
(`ω_k>0`), **microcausal** (equal-time field bracket vanishes spacelike), and
**reflection-positive** (the OS-reflected Källén–Lehmann kernel is PSD, the
canonical Glimm–Jaffe RP theory; runner §C). RP is a property of a *given*
measure, and the free-scalar measure is reflection-positive — so RP cannot exclude
a rep whose 2-point function is itself RP. **P1 admits the scalar**, and
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

The carrier frame goes from **two posits to one (faithfulness)** — with `L1 ⟸ G1`
as correct physics — **modulo auditing the spin-statistics / OS-reconstruction
step** (currently unaudited). On the retained-only tier, two posits remain. P1
**never reaches zero**: the scalar is admitted, so faithfulness is the single
irreducible frame posit no microcausality / RP / positive-energy constraint on a
single matter field excludes.

Two concrete fronts: **(1)** **audit** the matter-2-point exchange-sign
forcing — ratify `axiom_first_spin_statistics_theorem` S2 and
`free_field_os_wightman_reconstruction` (closing its open lattice↔continuum and
`1+1d → 4D` gates) — which renders `L1 ⟸ G1` retained-clean; **(2)** the **single
auditable frontier** then becomes *faithful-Weyl-over-scalar* — **untouched by
P1** (which admits the scalar) — to be pursued through M's own spin content /
the `so(3,1)` carrier-assignment, not through microcausality.

## Non-circularity

No `Q=2/3`, no fermionic frame, no faithful rep is assumed: the Dirac forcing is
the c-number spectrum content of the spin-½ rep (statistics is derived, not
input); the scalar's RP/positive-energy/microcausality are computed directly
(runner).

## Anchors (live-ledger tiers, verified origin/main 2026-06-01)

retained / retained_bounded / retained_no_go:
`spin_statistics_cardinality_pauli_exclusion` (retained, the cardinality core,
shown blind to the hard-core boson), `reflection_positivity_gauge_half_cauchy_schwarz`
(retained), `free_dirac_poincare_representation` (retained_bounded),
`internal_external_su2_merger` (retained_bounded, the derived boost),
`cpt_exact_real_anti_hermitian_d` (retained_bounded),
`staggered_dirac_substep1_statistics_agnostic_no_forcing` (retained_no_go, L1).
**Not cited as retained (the collapse rides these):** `axiom_first_spin_statistics_theorem`,
`free_field_os_wightman_reconstruction`, `free_sector_spin_statistics_level1` — all
unaudited.
