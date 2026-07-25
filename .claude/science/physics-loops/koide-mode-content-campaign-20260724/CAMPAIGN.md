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

---

## WAVE 1 RESULT (2026-07-24): SHARP NEGATIVE, with a NEW structural no-go

**Supervisor prediction was WRONG.** I predicted K acts as an
antiunitary on a single copy making count-once derivable. It does
not follow, and the stated circularity worry was correct and is
sharper than I framed it.

**The computed fact.** Frobenius-Schur indicator on the landed
carrier: `FS(1, omega, omega-bar) = (+1, 0, 0)`. The charged-lepton
doublet is **complex type** — neither of the two options the wave
posed. The K/CPT structure is a REAL structure (`J^2 = +1`, rebuilt
natively), definitively NOT quaternionic, and that is landed as
`r`-silent.

**THE NEW RESULT (this is the campaign's deliverable so far).**
Not a case list — a structural no-go:

> The `C_3`-invariant symmetric-form cone is `diag(g_0, g_1, g_1)`
> with the singlet:doublet ratio FREE, and `r = g_0/g_1` on the
> equal-sector locus. The two horns are the HS point `diag(3,6,6)`
> and the flat point `diag(1,1,1)`. **FS is CONSTANT `(+1,0,0)`
> across the entire cone while `r` sweeps `(0, infinity)`.**
> Therefore NO reality-type invariant can ever select the count.

This kills an entire attack class in one statement, and it is
gated (95 exact sympy gates, all PASS, independently reproducing
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS`).

**Why FS could never have worked (the identity, not a risk).**
`FS = 0` is not a failure to decide the count — `FS = 0` IS the
count binary. The trichotomy is exactly `dim_R` vs `dim_C` of an
isotype (`+1 -> x1`, `0 -> x2`, `-1 -> x4`); only `FS = 0` produces
the factor 2 at issue, and it is precisely the value structurally
incapable of resolving it. Relatedly, the KCPT `FS: 0 -> +1` flip
occurs at DOUBLED complex dimension (`4->8`, `6->12`): adjoining the
conjugator IS the doubling, so `FS = +1` can never be evidence about
whether the doubling is physical.

**Route was already foreclosed and we reproduced the foreclosure.**
`KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:157`
carries `| Complex-type/orientation/Frobenius-Schur route | RULED
OUT BY PRIOR as selector |`, and `:47` records
`**Result inside the tested class: 0 of 8 survived.**` with
"CPT / antiunitary" among the eight lenses.

### THREE FLAGS THAT OUTLIVE THIS WAVE

1. **The landed four-way equivalence may be WRONG.** The
   "6 vs 12 Grassmann generators" horn is **`r`-NEUTRAL in its
   landed realization** (`KCPT_COUPLING_TRIPLE_BEREZIN...:177-180`,
   reproduced by gates K1-K5): it doubles singlet and doublet
   TOGETHER, so it is not interchangeable with `w = 1/2` vs
   `w = 1/3`. If the reduction's four-way equivalence is
   load-bearing anywhere, it needs re-derivation. **This is the
   highest-value loose thread in the campaign.**
2. **Stale status label on main.**
   `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`
   calls `koide_frobenius_isotype_split_uniqueness` `retained_no_go`;
   the live ledger says `unaudited`. (Worker did not rely on it.)
3. **The polarization is supplied at declaration time.** `R^3` is
   odd-dimensional and has no integral complex-mode count; the
   declared 6-generator surface has ALREADY complexified to `C^3`.
   So the Berezin machinery cannot be asked to derive the count it
   was handed. Also: on `omega + omega-bar` the equivariant
   antiunitaries include BOTH `J^2 = +1` and `J^2 = -1`
   representatives, and both commute with the whole K-real mass
   family (gates Q1-Q8) — so even the wave's own premise was not
   carrier-forced.

### WHERE THIS LEAVES THE BINARY

`r = g_0/g_1` is a FREE parameter of the `C_3`-invariant form cone.
No symmetry-type, reality-type, or orientation invariant can fix it
— that is now a theorem, not a survey. Therefore the count, if it is
fixable at all, must be fixed by something that distinguishes the
singlet from the doublet sector **dynamically**: the matter action's
own kinetic/measure normalization.

## WAVE 2 (next, not yet run)

**Target:** derive `g_0/g_1` from the landed corner action's own
kinetic normalization, rather than from any invariant. Concretely:
does the landed charged-lepton corner action assign the singlet and
doublet sectors a relative kinetic weight, and if so is it `3:6` (HS
point, `r = 1/2`) or `1:1` (flat point, `r = 1`) or neither?

**Kill-check for Wave 2 (run FIRST):** the landed no-go tested 8
selector lenses and 0 survived — establish whether "action kinetic
normalization" was one of the 8. If it was, this campaign is over
and the honest output is the structural no-go above, written up as
a narrow note.

**Deliverable regardless of Wave 2's outcome:** a narrow no-go note
carrying the FS-constant-across-the-cone theorem plus the
`r`-neutrality correction to the 6-vs-12 horn. That is real,
gated, and new.

**RUN THE `/exercise` WALL EXERCISE BEFORE WAVE 2** — campaign rule 6
is now triggered: a route dead-ended.
