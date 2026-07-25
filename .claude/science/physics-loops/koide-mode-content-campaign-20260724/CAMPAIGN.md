# CAMPAIGN: the count-once / count-twice binary (Koide r = 1/2)

Opened 2026-07-24. Owner directive: long campaign, do NOT accept
existing walls, run the wall exercise when stuck. This file is the
durable campaign state — it must be readable cold after any context
loss. Update the STATUS LOG at the bottom every wave.

## The target, stated exactly

Landed reduction (verified by frontier recon 2026-07-24): the
charged-lepton mass-ratio question reduces to ONE binary, stated four
equivalent ways, none of them selected:

> Does the physical charged-lepton matter action count the K/CPT
> orbit (equivalently: the holomorphic determinant grain det_C;
> equivalently: the 2-cell quotient menu; equivalently: 6 Grassmann
> generators per triple copy) ONCE, or count each sector/channel
> separately (|det_C|^2 realified grain; 3-cell carrier menu; 12
> generators)?
>
>   count-once  => w = 1/2 => r = 1/2 => Q = 2/3   (Koide)
>   count-twice => w = 1/3 => r = 1

The landed closure test is stronger than "pick a horn": a closing
theorem must DERIVE the count, not adopt it.

## Why this is not a wall re-walk

Foreclosed and NOT to be re-attempted (landed no-gos; re-walking
these is the failure mode):
- the multiplicative / AC_phi_lambda bridge — foreclosed
  STRUCTURALLY (C_3 regular rep + Schur), not by transcendence;
- the delta-pattern leg (3 vectors, blocked);
- "chiral => r = 1/2" (fluctuation modulus gives r = 1 robustly;
  chirality moves only the determinant PHASE).

The ONE door the landed no-go explicitly leaves open, in its own
words, is "a future physical CAR/action theorem that derives a
specific Gaussian measure". That is this campaign's target and the
only route it may take.

## The attack

**Central question (decidable by construction):** build the CAR
algebra of the charged-lepton corner carrier natively, and COUNT the
complex modes of its coherent-state Berezin representation. If the
carrier has n complex modes (n theta, n theta-bar), the K-conjugate
partner copy is NOT independently integrated, the measure grain is
det_C, and count-once is DERIVED => r = 1/2. If it has 2n, count-twice.

This is exactly the machinery this session built and hardened:
Grassmann rings with sign bookkeeping, CAR anticommutator gates,
coherent-state kernels and their induced exterior operators, Fock
assembly via the canonical intertwiner, and Berezin/Wick contraction.

**Why it might actually work now (and did not before):** the earlier
campaigns attacked the ratio ALGEBRAICALLY (Schur, moduli, phases)
and were foreclosed there. Nobody has built the carrier's CAR algebra
and counted its Berezin modes as an operator-theoretic fact. The
count is a property of the CARRIER, not of the ratio, so the
foreclosures do not obviously apply — but that must be TESTED, not
assumed (see Wave 1 kill-check).

## Hard rules for every wave

1. **Kill-check first.** Before any construction wave, an agent must
   try to show the route is ALREADY foreclosed by a landed no-go. If
   it is, the campaign stops and says so. Do not build on a corpse.
2. Never set or predict an audit verdict. Never add an axiom or new
   vocabulary. Rebuild cited algebra natively.
3. Every claimed constant must be gated by a CONSTRUCTION-mutation
   probe, not only an assertion probe (lesson 53).
4. Verification sections are written FROM the runner. Worker probes
   are never described as gates (lesson 55).
5. `axiom_first_rp_two_step_transfer_matrix_positivity_note_2026-05-28`
   is audited_failed on the coherent-kernel leg — do not depend on
   it (lesson 56).
6. When a wave dead-ends, run the repo's `/exercise` wall exercise
   before choosing the next wave. Record its output here.
7. A sharp NO-GO is a success. "count-twice is forced" closes the
   question against Koide and is publishable.

## STATUS LOG

- **Wave 0 (2026-07-24, opened).** Campaign defined. Kill-check +
  carrier-scout + mode-count derivation dispatched as one workflow.
  Supervisor prediction, recorded BEFORE any worker output: the
  carrier is a single Grassmann copy per generation with K acting as
  an ANTIUNITARY on it (not as a doubling), so the coherent-state
  representation should carry n complex modes and count-once should
  be derivable — BUT the honest risk is that the "corner carrier" is
  defined only up to the very polarization choice that fixes the
  count, in which case the binary is definitionally circular and the
  right output is a sharpened statement of that circularity. I hold
  this loosely and expect the kill-check to bite.
