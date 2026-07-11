# Record Permanence Forces Fresh-Site Double Registration, and Persistence Equals Agreement-Conditioned Survival (Bounded Theorem Note)

**Date:** 2026-07-11
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On admissible record histories under the four framework
axioms, the Record permanence and one-record-per-site sentences make repeated
registration of a lane quantity axiom-forced fresh-site double registration
with full retention of every prior record (T1); and, given the supplied
agreement-conditioned fresh-site kernel together with one NAMED new premise
(epoch-independent lane readout), lane-value persistence is equivalent to
agreement-conditioned survival of the registration history at a kernel fixed
point (T2), with permanence forcing exactness once persistence is observed
across the offset-escape window (T3). The note discharges the re-registration
GEOMETRY half of the proposed R-D bridge and reduces the physical
re-registration identification to one named premise plus two open atoms; it
does not adopt R-D, derive the flow map, fix `r`, or exclude the `psi(r) = r^2`
flow class.
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no registry row. It does not edit the durability
chain note or its runner.
**Primary runner:**
[`scripts/frontier_record_permanence_double_registration_2026_07_11.py`](../scripts/frontier_record_permanence_double_registration_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_record_permanence_double_registration_2026_07_11.txt`](../logs/runner-cache/frontier_record_permanence_double_registration_2026_07_11.txt)
(SCORECARD: PASS=24, FAIL=0)
**No-promotion statement:** this note promotes, demotes, retires, routes, or
adopts no premise. R-D remains proposed. The named epoch-independent-readout
premise is named, not adopted; the two remaining atoms are named, not
discharged.

## Boundary

This note proves T1, T2, and T3 below and names the remainder. It does not
adopt R-D, does not derive the flow map `r -> 2 r^2` or its multiplicity, does
not discharge the outcome-factorization (G3) atom, does not select a flow
class, and does not fix `r`. The value `r = 1/2` appears only as a fixed point
of the SUPPLIED kernel, never as a derived number.

The supplied kernel and its `(1,2)` bookkeeping are consumed exactly as the
anatomy note supplies them. The anatomy note
`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`
proves, at its claim scope, that agreement-conditioned independent composition
of the weight bookkeeping reduces to `r -> 2 r^2` (its G2) and names the
statistics atom (its G3). This note advances that decomposition: it shows the
G2 double-registration GEOMETRY is not a modeling choice but is forced by the
Record axiom, and it supplies the persistence/agreement equivalence and the
exactness statement, while leaving G3 and the multiplicity open.

## The two load-bearing axiom sentences (verbatim)

Quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), Record axiom,
and guarded at runtime by the runner (whitespace-normalized, so the quotes
survive the source line-wrap):

> Records form.

> When present, a record locks exactly one admissible local possibility.

> A site never carries more than one record; records are permanent.

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar readout
> `I` is additive, with `I(empty)=0`.

The two sentences that do the work in T1 are "A site never carries more than
one record" (one record per site) and "records are permanent" (no record is
ever removed or altered). The additivity sentence is load-bearing in T2's
honesty point: it covers an additive scalar readout `I`, and the lane
coordinate is not one.

## The supplied surface

The lane coordinate is `r = |b|^2 / a^2`, with the supplied singlet/doublet
bookkeeping `(p_s, p_d) = (a^2, 2|b|^2)` up to common normalization, so
`p_d / p_s = 2 r`. The supplied fresh-site registration kernel is the
anatomy note's agreement-conditioned composition

```text
p_i' = p_i^2 / (p_s^2 + p_d^2),   equivalently   f(r) = 2 r^2,
```

with finite fixed points `r in {0, 1/2}` and the projective endpoint
`r -> infinity` also fixed. The interior fixed point is `r* = 1/2`, at which
`f'(r*) = 4 r* = 2`. This note consumes the kernel as SUPPLIED; it does not
derive it and does not exclude the alternative flow class `psi(r) = r^2`.

## T1 (axiom-forced fresh-site double-registration geometry)

**Statement.** Let an admissible record history be a finite sequence of
registration events `e_1, ..., e_n`, each event locking one record at one site,
subject to the Record axiom: no record is ever removed or altered (permanence),
and no site ever carries two records (one record per site). Then in every
admissible history the target sites `s_1, ..., s_n` are pairwise distinct
(each repeated registration of a lane quantity occurs at a fresh site), and at
every epoch `k` all `k` prior records coexist unchanged (full retention: the
retained record set has exactly `k` members). Equivalently: a history is
admissible if and only if its site sequence is injective, and same-site
repetition is the only obstruction to admissibility.

**Proof.** Suppose event `e_k` targets a site `s_k` already carrying a record
placed by an earlier event `e_j`, `j < k`. Two readings exhaust the
possibilities. If the earlier record is first removed or overwritten so that
`s_k` can be relocked, permanence is violated ("records are permanent" forbids
removal or alteration). If the earlier record is retained and a second record
is added at `s_k`, then `s_k` carries two records, violating one record per
site ("A site never carries more than one record"). Both readings are
inadmissible, so `s_k` must be a fresh site, `s_k not in {s_1, ..., s_{k-1}}`;
the site sequence is injective. Permanence then gives `R_{k-1} subset R_k` (no
removals) and each event adds exactly one record at a fresh site, so
`|R_k| = k`; taking `k = n` gives full retention of all `n` records. The
converse is immediate: an injective site sequence never re-uses a site, so no
event ever confronts an occupied site, and the history is admissible.
∎

**What T1 converts.** The anatomy note's G2 reads a second registration as a
genuinely new registration event whose outcome is composed and
agreement-conditioned, rather than as a same-site re-pinch. Its G1 shows the
same-site reading is a weight no-op: the canonical pinch
`D(M) = P_s M P_s + P_d M P_d` is idempotent, `D(D(M)) = D(M)`, so re-pinching
the same site induces the identity on the bookkeeping (runner reproves this).
T1 shows the same-site reading is not merely uninformative but axiom-forbidden:
permanence and one-record-per-site remove it outright. The fresh-site
double-registration geometry that G2 assumed is therefore forced structure over
admissible histories, not a modeling choice.

**Runner.** Checks 1-5 guard the axiom sentences verbatim. Checks 6-9 enumerate
all candidate histories on a three-site set up to length three, verify
admissible `<=>` injective site sequence, verify full retention on every
admissible history, verify that the inadmissible histories are exactly those
with a same-site second event (forbidden under both the coexistence and the
overwrite readings), and reprove the `D(D(M)) = D(M)` idempotence tie to G1.

## T2 (persistence equals agreement-conditioned survival)

**Statement.** Assume (i) the supplied fresh-site registration kernel `f`
(agreement-conditioned independent composition of the weight bookkeeping, the
anatomy note's supplied premise) and (ii) the NAMED new premise

> **Epoch-independent lane readout.** The lane's registered value is one value
> across formation epochs: every epoch's record reads out the same `r`.

Then lane-value persistence is equivalent to agreement-conditioned survival of
the registration history at a kernel fixed point. Precisely, for a value `r`
carried by the history under premise (ii): the readout is constant across all
formation epochs (persistence) if and only if `r` is a fixed point of `f`
(`f(r) = r`), which is exactly the value the agreement-conditioned
re-registration reproduces and the value carried by the agreement-surviving
subpopulation.

**Proof.** Under the supplied kernel the readout at epoch `k+1` is `f(r_k)`.
By premise (ii) a single value `r` labels the lane across epochs, so
persistence means `r_{k+1} = r_k = r` for every `k`. Forward: persistence gives
`f(r) = r_{k+1} = r`, so `r in Fix(f)`; the history that reaches epoch `n`
through the agreement gate carrying the same `r` is the agreement-surviving
subpopulation. Backward: if `r in Fix(f)` then each re-registration reproduces
`r`, the agreement-conditioned retained history keeps value `r` at every epoch,
and the readout is constant, i.e. persistence. On the finite value grid the
biconditional `persists(r) <=> f(r) = r` holds, with the finite fixed set
exactly `{0, 1/2}`.
∎

**The honesty point (why premise (ii) is not derivable from additivity).** The
Record axiom's additivity sentence covers an additive scalar readout `I`:
`I(R_1 union R_2) = I(R_1) + I(R_2)` over disjoint records. The lane coordinate
`r = |b|^2 / a^2` is a ratio of two quadratic aggregates, not an additive
scalar. Even granting that the quadratic aggregates `A = sum a^2` and
`B = sum |b|^2` are each additive over disjoint records, the pooled ratio
`B / A` is a mediant-type combination of the per-epoch ratios and does not
equal them unless they already coincide. Additivity therefore does not force a
single lane value across epochs; epoch-independence is a genuine extra premise.

**The necessity exhibit (turning the premise's necessity into a theorem).**
Take two permanent records on distinct sites (fresh sites, by T1), fully
retained:

```text
epoch 1:  (a_1^2, |b_1|^2) = (2, 1)  ->  r_1 = 1/2
epoch 2:  (a_2^2, |b_2|^2) = (1, 1)  ->  r_2 = 1
```

Both are admissible, permanent, and coexisting. The per-epoch lane readout is
well-defined at each epoch, but the lane readout is genuinely multi-valued
across epochs: `r_1 = 1/2 != 1 = r_2`. Additivity of the aggregates yields a
single pooled `A = 3` and `B = 2`, hence a pooled ratio

```text
r_pool = (|b_1|^2 + |b_2|^2) / (a_1^2 + a_2^2) = 2/3,
```

a THIRD value, equal to neither epoch reading. So without premise (ii) the
predicate "the lane value persists" is not even single-valued: there is an
admissible, permanent, fully-retained history with three distinct legitimate
readings `{1/2, 1, 2/3}`. This configuration is exactly what makes premise (ii)
necessary; its existence is a theorem (runner check 14-15). A positive control
(check 16) shows that when the two epochs already agree, the mediant returns
the common value, so additivity is CONSISTENT with epoch-independence while not
entailing it.

**Runner.** Check 10 reproves the kernel reduction `p_i' = p_i^2/(p_s^2+p_d^2)`
to `r -> 2 r^2`. Checks 11-13 verify the finite biconditional both directions
and the fixed set. Checks 14-16 build the necessity exhibit, the
ratio-not-additive fact, and the positive control.

## T3 (exactness from permanence)

**Statement.** Permanence forbids re-preparation: once a disagreeing
(out-of-band) record exists it exists forever, so a drifted lane cannot be
erased and re-registered to appear persistent. Under the supplied flow family,
with local expansion factor `|f'(r*)| = 2` at the interior fixed point
`r* = 1/2`, an offset `eps` leaves any fixed agreement band of half-width
`band` in about `log2(band / eps)` steps. Hence a lane OBSERVED persistent at
precision `eps` across `n` re-registrations, with `n` at least the escape count
`log2(band / eps)`, sits exactly on a flow fixed point.

**Escape arithmetic (computed, not asserted).** Linearizing `f(r) = 2 r^2`
about `r* = 1/2` with `u = r - 1/2` gives `u_{k+1} = 2 u_k + 2 u_k^2`, whose
small-offset behaviour is `u_{k+1} approx 2 u_k`, so `|u_n| approx 2^n |u_0|`
and the offset leaves the band when `2^n eps >= band`, i.e. at
`n = ceil(log2(band / eps))`. For the observed Koide precision scale
`eps = 1e-5` and band `= 0.1`:

```text
n_linear = ceil(log2(0.1 / 1e-5)) = ceil(log2(1e4)) = ceil(13.2877...) = 14 steps.
```

The exact iterated map (starting at `1/2 + eps`, iterated until
`|r - 1/2| >= band`) leaves the band in `14` steps as well, matching the linear
estimate. The count is a formula, not a constant: a second pair
`eps = 1e-8`, band `= 0.2` gives `25` steps (linear and exact), verifying the
step count is computed from `(eps, band)` and is not hard-coded (runner checks
18-20). The exactness conclusion is then a biconditional over interior offsets:
observed persistence across the offset-dependent escape window holds if and
only if the offset is exactly zero; any nonzero offset produces, within its
escape window, a permanent out-of-band record that permanence forbids erasing
(check 21).

**Per-step agreement-survival probability, and survivorship not stasis.** At
the equipartition fixed point `r* = 1/2` the bookkeeping is
`p_s = p_d = 1/2`, so the normalizer and the per-step agreement-survival
probability coincide:

```text
p_s^2 + p_d^2 = 1/4 + 1/4 = 1/2.
```

Two independent registrations agree (both singlet or both doublet) with
probability `p_s^2 + p_d^2 = 1/2` at the fixed point; the agreeing subpopulation
carries `r*` forward, and after `n` steps its surviving fraction is `(1/2)^n`
(check 22-23). Fixed-point persistence is therefore survivorship of the
agreeing-history subpopulation, not stasis of every individual history: the
disagreeing histories do not vanish, they form permanent out-of-band records
(consistent with T1 and with the exactness statement), while the surviving
agreeing subpopulation reproduces the fixed-point value.

## Discharge ledger for the R-D bridge

R-D reads "durable registration is invariant under records-flow
self-composition" (a durably registered value is a fixed point of the flow).
This note decomposes the physical re-registration identification R-D packs and
reports each piece at its honest status:

- **Re-registration geometry (fresh-site double registration, full retention):
  DISCHARGED (axiom-forced), T1.** Repeated registration is a fresh-site event
  with all prior records retained; the same-site rewrite reading is
  axiom-forbidden. This is what G2 assumed and is now forced.
- **Durable = fixed point (persistence equals agreement-conditioned survival):
  DISCHARGED conditional on the supplied kernel and the named premise, T2;
  with exactness under the supplied flow class, T3.** Persistence is equivalent
  to survival at a kernel fixed point, and permanence sharpens observed
  persistence to exactness.
- **Epoch-independent lane readout: NAMED, necessity exhibited (not derived).**
  The ratio readout is not additive, so this cannot come from the additivity
  sentence; the exhibit shows a permanent disagreeing history whose readout is
  multi-valued across epochs, proving the premise does real work.
- **Outcome factorization (independent composition on the weight bookkeeping,
  the anatomy note's G3): OPEN.** Not discharged here; it remains a
  statistics-layer atom.
- **Bookkeeping multiplicity / flow class (the `(1,2)` component count that
  fixes `f(r) = 2 r^2` rather than `psi(r) = r^2`): OPEN, routed to the kappa
  lane.** This note fixes neither; the choice between the flow classes is the
  kappa question.

## Consumers

The durability chain note
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
consumes R-D as a named, unadopted bridge. That chain was written against the
2026-06-05 Record wording; the 2026-07-04 revision of
`MINIMAL_AXIOMS_2026-06-29.md` is what supplies the permanence and
one-record-per-site sentences T1 uses. This note discharges the geometry half
and the persistence/agreement half of the bridge and names the remainder; it
does NOT edit the chain note or its runner. The chain runner's check that pins
R-D as named-not-smuggled (its Record non-supply interface check) should be
retargeted to cite the discharged geometry and persistence pieces only when the
full R-D discharge lands — that retarget rides the eventual full discharge and
is not performed here.

The premise-relation note
`KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md`
exhibits, at its claim scope, the flow `psi(r) = r^2` as a law-level
counterexample under which the same side conditions select the sector cell
`r = 1`, showing OO and R-D are inequivalent as laws. This note is consistent
with that scope: T1-T3 are stated for the supplied kernel `f` and do not select
between `f` and `psi`. The runner confirms `psi` has interior fixed point
`r = 1` with the same multiplier `2`, distinct from `f`'s `r = 1/2`, so nothing
here excludes `psi` (check 24).

## What this note does NOT claim

- Does not derive the flow map `r -> 2 r^2`, its bookkeeping multiplicity, or
  the `(1,2)` component count; these are consumed as supplied.
- Does not discharge the outcome-factorization (G3) atom; it is named, open.
- Does not adopt R-D or the epoch-independent-readout premise; R-D stays
  proposed, the premise stays named.
- Does not exclude the `psi(r) = r^2` flow class; that is the kappa question, a
  separate block.
- Does not derive any value of `r`; `r = 1/2` appears only as a fixed point of
  the supplied kernel, never as a derived number.
- Does not edit the durability chain note, its runner, any registry, or any
  audit data file, and asserts no effective-status change.

## Residual atoms

- **Epoch-independent lane readout: NAMED.** Necessity exhibited (permanent
  disagreeing records, ratio readout multi-valued across epochs; additivity
  does not force it). Not derived, not adopted.
- **Outcome factorization: OPEN.** Independent composition of the two
  registration outcomes on the weight bookkeeping (the anatomy note's G3
  statistics atom). Not discharged here.
- **Bookkeeping multiplicity: OPEN, routed to the kappa lane.** The `(1,2)`
  component count / flow-class choice that fixes `f(r) = 2 r^2` rather than
  `psi(r) = r^2`. Not fixed here.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — the Record
  axiom sentences (permanence, one record per site, additive scalar readout),
  quoted verbatim and runtime-guarded.
- [`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md)
  — the supplied kernel, the G2 double-registration geometry T1 forces, the G1
  idempotence tie, and the G3 atom that remains open (cited at its claim scope).

Context (not load-bearing):

- `KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  — the consumer chain (not edited here).
- `KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md`
  — the `psi(r) = r^2` law-level counterexample this note does not exclude
  (cited at its claim scope).
- `KOIDE_OCCUPANCY_FROM_LOCKED_RECORD_OUTCOMES_BOUNDED_NOTE_2026-07-03.md`
  — house-style exemplar for the bounded note and runner.

## Verification

```bash
python3 scripts/frontier_record_permanence_double_registration_2026_07_11.py
```

Expected: 24 `CHECK NN: PASS` lines, four `SUMMARY` lines, then
`TOTAL: PASS=24 FAIL=0`. Exit code 0 iff `FAIL=0`.

**Independent audit required.** This note asserts no effective-status change.
