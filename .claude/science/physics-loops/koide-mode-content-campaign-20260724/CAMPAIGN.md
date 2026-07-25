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

---

## WALL EXERCISE (2026-07-24, 6 sectors) — ranked portfolio

The exercise KILLED the planned Wave 2. My intended move — "derive
g_0/g_1 from the action's kinetic normalization" — was shown to be a
**convention-laundering false positive**: it would re-derive an
algebraic identity and read r = 1/2 off it only by silently adopting
a counting convention (s = 0). A mu-rescaling falsifier was supplied.
Running the exercise before Wave 2 was correct and I would have
shipped a false positive otherwise.

**Ranked attack vectors out of the exercise:**

1. **(Ex1) The associativity/Frobenius test the landed no-go never
   ran.** That no-go tested only positive-definiteness, Ad-invariance,
   and scalar/traceless orthogonality. It never imposed
   <uv, t> = <v, u^dag t>. Imposing it leaves the residual
   (2 g_0 - g_1)(...), so the unique associative ray is the HS/trace
   form and **g_0/g_1 = 1/2 is forced** — the cone collapses to a
   point. 26/26 gates, two implementations. If it holds, this is a
   NEW positive result and a correction to a landed no-go's framing.
2. **(Ex2) The factorization r = (g_0/g_1)(w_1/w_0), only the product
   physical.** Commutant theorem: Gamma = diag(lambda, mu, mu) sweeps
   r transitively over (0, infinity) while fixing the module, so NO
   invariant of any kind can select r — a selector must be a MEASURE
   WITH ATOMS. This generalizes the Wave 1 FS result to every finite
   group and every module invariant, in one line.
3. **(Ex3) Positivity forbids one side.** From the landed heat-trace
   identity, r(t) = (S + 2F)/(S - F) with F a strict sub-sum of S,
   so **r > 1 strictly** for all t > 0, N > 1. r = 1/2 is unreachable
   by any positive C_3-covariant spectral weight. Breach condition is
   a NUMBER: r = 1/2 iff F/S = -1/5, which requires a GRADED operator
   (negative contributions), turning the repo's open "a grading, not
   a complex structure" handle into a pass/fail target.
4. **(Ex2) Possible campaign-ender**: the registered
   realized_state_primitive's State-Contingency Register item 4 is
   reported to say dial settings (r = 0, 1/2, 1) are "sector data,
   never forced" — which would contradict the closure obligation
   itself. Must be adjudicated before any further construction.
5. **(Ex1/Ex2) Status hygiene**: the entire foreclosure scaffolding
   for this lane is `unaudited` on the live ledger while several
   notes call it "retained". Do not lean on any prose status.

Also flagged: the binary framing may be an **N = 3 artifact** — Z_2
has the freedom with no fork (the horns coincide) and Z_N>=4
dissolves it into >= 2 parameters, so only Z_3 makes it look like one
bit. Integrality is an undischarged hidden premise, and a third value
r = 2 is reachable.

## WAVE 2 (running) — supervisor prediction, recorded BEFORE results

Dispatched: steelman Ex1, steelman Ex2, adjudicate the primitive
register, verify the breach number.

**My prediction: the "tension" is not a contradiction — Ex1 and Ex2
will turn out COMPATIBLE, and both halves are right.** Ex1 gives
r = 2^s (g_0/g_1); with g_0/g_1 = 1/2 forced by associativity,
r = 2^(s-1), so s = 0 gives r = 1/2 and s = 1 gives r = 1. Ex2's
"free mode-count factor w_1/w_0" is, I predict, THE SAME OBJECT as
Ex1's 2^s. If so, the campaign's honest outcome is a **partial
closure**: the METRIC half of the counting bit is genuinely forced
(new result; corrects the landed no-go by supplying the test it never
ran), and the COUNTING half survives as the real residual —
form-equipartition vs state-equipartition, which is the original
count-once/count-twice bit relocated but NOT closed.

If that is what comes back, the deliverable is a narrow note carrying
(i) the associativity forcing of the metric ratio, (ii) the
commutant theorem that no invariant can ever select r, and (iii) the
positivity half-cone with the F/S = -1/5 breach target. All three are
gated results and (ii)+(iii) are sharp negatives.

**Risk I am holding:** Ex1's associativity requirement may be an
IMPORT rather than a framework consequence. If the Record readout
does not actually induce an associative form on that algebra, Ex1
demotes from theorem to conditional and the "forcing" evaporates.
The defend-ex1 agent is instructed to attack exactly that.

---

## WAVE 2 RESULT (2026-07-24)

**Prediction CONFIRMED on the central point.** Both defenders
independently concluded Ex1 and Ex2 never conflicted: EX1's `s` and
EX2's `nu` are the SAME residual (`nu = 2^s`), and
`r = 2^s (g_0/g_1)` IS `r = (g_0/g_1)(w_1/w_0)`. There was no
arithmetic contradiction.

**The risk I flagged BIT, exactly as flagged.** Ex1's algebra is
correct (72/72 gates, and strengthenable: Frobenius + scalar/traceless
orthogonality gives HS with NO group at all) — but the ASSOCIATIVITY
CONDITION IS AN IMPORT, not a framework consequence. The corpus has
already adjudicated this laundering: `MINIMAL_AXIOMS_2026-06-29.md:170`
puts source/action and physical-observable identification OUTSIDE
axiom content; `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md:45-57,63-69`
carries the readout identification as a declared Boundary with a
landed independence no-go, and classifies Record additivity as
`W = sum_i phi(x_i)` with `phi` FREE (log, not linear, in its
best-supported case). **Ex1 demotes from theorem to conditional.**

**Worse for the campaign's hoped direction: granting the bridge in
full does not give `r = 1/2` — it argues for `r = 1`.** The Frobenius
family on `Herm_circ(3)` is exactly `{Tr(rho X^dag Y)}`, which after
K-reality is verbatim the landed free dial; closure comes only from
isotype orthogonality, and on that dial orthogonality holds exactly at
`r = 1`. Independently, the second defender: the object associativity
pins is the TRACE, whose own block weights are
`Tr P_0 : Tr P_1 = 1 : 2`, giving `r = 1`; and the `(1,1)` weighting
is the value of NO linear functional on the algebra.

### THE TWO NEW RESULTS WORTH THE WAVE

1. **Positivity of the SPECTRUM bounds the PRODUCT (not a factor):**
   `e_2 = 3(a^2 - |b|^2) > 0` implies **`r < 1` STRICTLY**, with
   `r = 1` forcing the degenerate spectrum `(3a, 0, 0)` (exact
   witness `(1, 1/2) -> (1, 3/2)`: spectrum `(2, 1/2, 1/2)` ->
   `(4, -1/2, -1/2)`). **The horns are ASYMMETRIC: `r = 1/2` is
   INTERIOR, `r = 1` is on the BOUNDARY.** This also refutes EX2's
   clause that the Gamma-breaking list fixes "only the metric
   factor" — the positive cone is algebra content and it constrains
   the product. 83/0 gates, 12 mutation probes.
2. **Record additivity does NOT fix `w_1/w_0`, and this is now
   COMPUTED rather than asserted:** the space of finitely additive
   readouts on the 2-letter record alphabet is exactly
   2-dimensional (one free ratio after scale), and no symmetry can
   equate two inequivalent letters. `axiom_premise_nodes.json:25`
   and `MINIMAL_AXIOMS_2026-06-29.md:152-155` explicitly exclude
   weighting, normalization, K/CPT structure and central-sector
   decomposition from Record. EX2's own escape hatch ("exhibit the
   set") is circular: both `(1,2)` and `(1,1)` are cardinalities of
   landed framework-supplied sets — the fibre counts on the two
   sides of one K/CPT quotient.

Also: EX2's "only the product is physical" redundancy is FICTITIOUS
as a symmetry (the algebra is `R x R x R`, automorphism group the
finite `S_3`, which fixes `g_0/g_1` exactly). Honest statement:
"one factor is still unsourced", not "only the product is physical".

### PRIMITIVE ADJUDICATION: campaign is NOT closed by foundation

The quote is verbatim-accurate (`REALIZED_STATE_PRIMITIVE_NOTE:93`)
but the paraphrase dropped its governing scope: it sits in the
**Informative** State-Contingency Register (`:71`), whose own text
says it "records current examples" and "is documentation, not an
additional gate" (`:73-74`). It records non-supply BY THE PRIMITIVE,
not underivability in principle. Affirmatively contradicted:
`derivation_obligations.json` registers
`ac_orbit_occupancy_statistical_grain_derivation_obligation` —
target VERBATIM this campaign's question — as a LIVE `open_gate`,
sourced to a note dated one month AFTER the primitive, and
governance records the count-once horn as DEMOTED from owner-adopted
premise to open derivation obligation
(`TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:9-18,37-42`).

### REPO-HYGIENE FINDING (report to owner)

**33 of 37 counting-bit scaffolding rows have no retained-grade
standing live (89%); corpus-wide 75 rows / 279 lines in this lane
carry prose status labels that contradict the live ledger.** Do not
lean on any prose status in this lane.

## WAVE 3 (dispatched) — the positivity contradiction

Two gated results now point OPPOSITE ways and cannot both be about
the same object:
- Exercise sector 3: positive `C_3`-covariant SPECTRAL WEIGHTS force
  `r(t) = (S+2F)/(S-F) > 1` strictly, so `r = 1/2` is unreachable.
- Wave 2 defender: positivity of the SPECTRUM of the Hermitian
  element forces `r < 1` strictly, so `r = 1` is unreachable except
  at a degenerate rank-1 spectrum.

**Supervisor prediction, recorded before Wave 3 results:** these are
positivity conditions on DIFFERENT objects (a weight/measure versus
an element's spectrum), so both can hold — and if they do, they
squeeze from opposite sides and the physically admissible window is
narrow. The valuable outcome is not "one is wrong" but a precise
statement of which object each constrains, and whether the
intersection is empty (a no-go against BOTH horns, which would be a
major and publishable negative) or contains `r = 1/2` alone (which
would be the breakthrough). I expect non-empty and NOT uniquely
`1/2`, but the degenerate-spectrum exclusion of `r = 1` is the most
promising positive lead the campaign has produced.
