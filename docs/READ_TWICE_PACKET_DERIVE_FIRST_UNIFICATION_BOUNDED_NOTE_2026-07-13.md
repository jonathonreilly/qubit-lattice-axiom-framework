# "Read Twice" And "Written Twice" Are One Packet Family: Derive-First Unpack Of R-READ, Its Reduction To R-FORM Plus FRAME-EXT, And The Two-Register Coincidence Form

**Date:** 2026-07-13
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note does not set,
predict, or apply an audit outcome, and no audit-lane pipeline was run for it.
**Primary runner:**
[`scripts/read_twice_packet_derive_first_unification_2026_07_13.py`](../scripts/read_twice_packet_derive_first_unification_2026_07_13.py)
**Cache:**
[`logs/runner-cache/read_twice_packet_derive_first_unification_2026_07_13.txt`](../logs/runner-cache/read_twice_packet_derive_first_unification_2026_07_13.txt)
**Commission:** executes the 2026-07-13 handoff "handle 'a record must be
read twice' as a derive-first registered packet (R-READ), NOT an axiom
edit," per its P0–P4 protocol, unified with the write-side packet the same
protocol demands for "a record must be written twice."

## P0 — the named targets (stated first, per the handoff)

- **Read-side target:** the modulus-squared readout weight — show that,
  conditional on named packet content, the statistical weight of a
  recorded outcome is the sesquilinear (conjugate-paired) form, with the
  discrete `r in {1, 1/2}` readout dichotomy as the falsifiable
  discriminator.
- **Write-side target:** the formation-interface objects that the read-side
  derivation consumes — a record's birth structure as two disjoint,
  independently outcome-tied registers — stated as a packet whose own
  targets (registration-criterion physics; the local formation-frequency
  variable) are named in P4.

Per the handoff's pivot rule, everything below is scoped to these targets.

## P1 — the packets, clause by clause

The slogan "a record must be read twice" quantifies over read events the
axioms do not contain, and the slogan "written twice" quantifies over write
events the axioms equally do not contain. Both unpack into four-clause
packets of the same shape. Neither packet is registered by this note.

```text
(R-FORM) Two-register formation packet (candidate; not registered).
(R-FORM-a) Ontology: write events exist, each associated with a
           (site, admissible possibility, fresh register) triple.
           [extension - underivable; see P2]
(R-FORM-b) Independence: a formation event comprises two write events on
           DISJOINT register regions, each register's conditional content
           tied to the site outcome and, given that outcome, to nothing
           else. The outcome decomposition is the site's admissible menu,
           supplied upstream by the Admissibility axiom - the packet
           chooses no basis. [physical clause, part 1]
(R-FORM-c) Counting: realized records count per admissible possibility,
           never per coordinate, dimension, or presentation.
           [physical clause, part 2 - where any weight content hides]
(R-FORM-d) Compatibility: one-record-per-site, permanence, readout from
           content alone, and finite additivity with I(empty)=0 hold at
           the two-register level. [proof obligations - discharged by the
           runner]

(R-READ) Read-event packet (candidate; not registered - and after P2,
         nothing of it remains to register).
(R-READ-a) Ontology: read events exist as (record, reading-context) pairs.
(R-READ-b) Independence: the two mandated reads are distinguished by ONE
           discriminator among: K-conjugate contexts | distinct sites |
           distinct ticks.
(R-READ-c) Pairing: the readout weight is the sesquilinear composition of
           the two read values.
(R-READ-d) Compatibility: both reads read the same record content;
           one-record-per-site, permanence, additivity, I(empty)=0
           untouched.
```

## P2 — derive-first audit, clause by clause

Attempted closure sources, per the handoff: the four axioms
([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)), the three
registered primitives (`scale_reference_primitive`,
`kinetic_isotropy_primitive`, `realized_state_primitive`), and retained
theorems — here principally the admissible one-step record-write
classification and the FRAME-EXT reduction. Verdicts:

| Clause | Verdict | Basis |
|---|---|---|
| R-FORM-a | **Underivable extension.** | The axioms contain no event objects; "Records form." supplies occurrence only, and the landed no-go boundary states the minimal axioms "do **not** force the formation rule/process/state/site/weight/rate." |
| R-FORM-b | **Underivable; motivated and constrained, not free.** | Not derivable from axiom text (the memo lists formation rules and local observability among its open gates). It is however the unique candidate compatible with the permanence adjective being physically enforceable: a single register's write is, by the classified write class below, an isometry — invertible by construction, hence revocable by the adjoint; two disjoint outcome-tied registers are the minimal configuration whose joint reversal is not a local operation on either. The runner exhibits both facts exactly. |
| R-FORM-c | **Underivable; load-bearing.** | The no-privilege sentences do not force weightings (established by the 2026-07-02 five-seat blind-panel adjudication of the Qubit clause, recorded in the walls-attack block16 arc); the per-possibility rule must be supplied. Its falsifiable content is the `w in {1/3, 1/2} <-> r in {1, 1/2}` arithmetic the runner checks. |
| R-FORM-d | **Provable obligations — discharged.** | Runner blocks B6–B8: at the two-register level, each register is a distinct site carrying at most one record; branchwise permanence holds in the sense of the write-class note's repeat-channel stability; readout is invariant under register-basis unitaries (content-determined); the two witness records are pairwise disjoint and their readouts add with `I(empty)=0`. |
| R-READ-a | **Reduces to R-FORM-a.** | Given R-FORM, the only read events the target needs are readouts of the two formation registers. No separate read-event ontology is required. |
| R-READ-b | **Forced, conditional on R-FORM: the discriminator is "distinct sites," and it is not chosen but inherited** — the two reads are reads of the two formation witnesses. | "Distinct ticks" is eliminated on the current surface: with permanence and content-determined readout, a second read at a later tick reads the same content by a two-line corollary and can add nothing. "K-conjugate contexts" is not selected as an input; the conjugate structure appears in the OUTPUT of R-READ-c's derivation (the sesquilinear form), which is where it belongs. |
| R-READ-c | **Not an independent assumption. It reduces, verbatim, to the already-named FRAME-EXT premise plus Gleason's theorem (a textbook import at composite dimension >= 3) — with R-FORM supplying, as physically realized structure, the composite domain that FRAME-EXT's clause (4) otherwise has to supply by hand.** | See the theorem below. The remaining open crux is exactly the already-named FINITE-ADDITIVITY-TO-FRAME gap, narrowed as stated there — no new gap and no new premise are introduced by "read twice." |
| R-READ-d | **Provable obligations — discharged** (same runner blocks as R-FORM-d; the paired readout consumes register content only). |

### The unification theorem (conditional, exact on the minimal representative)

Consumed classification (verbatim from
[`RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md`](RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md),
conditional on its declared readings C1–C4):

> "Thus every admissible blank-input one-step write under these declared
> readings is, up to a register basis unitary and register phase choice, in
> the controlled-copy isometry class."

Consumed premise shape (verbatim from
[`READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md`](READOUT_BRIDGE_FRAME_EXTENSION_UNIFIES_MARGINAL_READ_AND_REGISTERED_FACTOR_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md)):
the FRAME-EXT four-clause premise, its reduction chain
"FRAME-EXT AND Gleason's theorem ... => REP on nearest-neighbor
composites," and its named crux, the FINITE-ADDITIVITY-TO-FRAME gap.

**Theorem (two-register coincidence form).** On the minimal finite
representative — one system pair of pointer projectors `P_0, P_1` and two
fresh blank registers `R_1, R_2` on distinct sites — let a formation event
per R-FORM-b be two admissible one-step writes from the classified
controlled-copy class, applied to the two disjoint registers. Then, for any
input in the pointer span with coefficients `c_0, c_1`:

1. the post-formation state is the two-register fan-out
   `sum_i c_i |i> |r_i> |s_i>` with `<r_0|r_1> = <s_0|s_1> = 0` — the two
   registers discriminate the outcome exactly and are conditionally
   independent given it (R-FORM-b is realizable, and its content is exactly
   the classified write class applied twice);
2. the **coincidence functional** — the weight of joint agreement of the two
   registers on outcome `i` — equals `c_i^* c_i = |c_i|^2`, the diagonal of
   a sesquilinear form: the R-READ-c pairing appears as the agreement
   functional of the two formation witnesses, not as a postulate;
3. this functional is content-determined (invariant under register-basis
   unitaries), nonnegative, and normalized, and the composite carrier that
   FRAME-EXT's clause (4) must otherwise supply by hand —
   `M_2 tensor M_2 = M_4` with its projection lattice — is here realized
   physically by the formation event. Precisely: given FRAME-EXT's
   extension clauses on that realized carrier, Gleason's theorem
   (dimension 4 >= 3, textbook import) forces the density form, and the
   coincidence functional is exactly the density-form diagonal the
   extension must match on the realized menu. The realized menu alone does
   NOT supply Gleason's domain — the extension to all orthogonal
   decompositions remains FRAME-EXT content; that is the surviving gap;
4. the single-register control fails: on one register alone (`M_2`), the
   known dimension-2 loophole frame function `f(P_n) = (1 + n_z^3)/2` is
   nonnegative, normalized, and additive on every orthogonal `M_2` pair yet
   is not of density form — so nothing forces the pairing at one witness,
   and the second disjoint register is load-bearing for the read-side
   derivation, exactly as the graded-constraint memo's dimension-2
   exception sentence anticipates ("neighbor composites are `M_4` and
   above, where the theorem holds").

All four parts are verified exactly (rational/Gaussian-rational arithmetic)
by the runner. Gleason's theorem itself is consumed as a textbook import at
declared scope (dimension >= 3), not re-proven.

**What this does and does not close.** Given R-FORM, the entire surviving
content of "a record must be read twice" is: *the readout weight is the
agreement functional of the two formation registers*, and that functional's
sesquilinear form follows on the realized composite domain from FRAME-EXT's
remaining clauses plus Gleason. The FINITE-ADDITIVITY-TO-FRAME gap is not
closed: Gleason's uniqueness needs frame additivity over all orthogonal
decompositions of the composite lattice, while realized formation events
supply additivity on realized menus. The gap is **narrowed** in one honest
respect: FRAME-EXT's clause (4) — ownership of the composite domain — no
longer needs to be supplied by hand, because the two-register formation
event realizes that domain physically. The non-contextuality core of the
gap (menus never realized) stands and remains the named crux.

## P3 — placement (prepared, not executed)

Per the handoff: registry, not axioms. Nothing here edits
`MINIMAL_AXIOMS_2026-06-29.md` or any registry, and no registration is
performed by this note.

- **R-FORM** is the only packet with registrable content: clauses (a)–(c),
  with (d) carried as proven obligations. Prepared registration text, for
  whenever the owner takes it up, is the packet block in P1 verbatim.
- **R-READ requires no registration.** After P2, its ontology reduces to
  R-FORM's, its discriminator is inherited, its pairing is conditional
  theorem content (FRAME-EXT + Gleason on the realized composite), and its
  compatibility clauses are proven. Registering "read twice" separately
  would mint a second name for existing content — the exact double-naming
  the FRAME-EXT reduction removed for the color premises.
- **Family resemblance, decided separately:** the pending per-plaquette
  P-LINK-AVAIL four-clause registration belongs to the same
  certification-by-redundancy genre. Per the handoff's do-not, no coupling:
  noted here, decided there.

## P4 — the target theorems, conditional wording throughout

- **Read-side (the P0 target):** conditional on the R-FORM packet, the
  FRAME-EXT premise (its remaining clauses), and the Gleason import, the
  readout weight of a recorded outcome is `|c_i|^2` — the two-register
  coincidence form. Falsifiable discriminator: combined with R-FORM-c's
  per-possibility counting, the readout dichotomy resolves to `r = 1/2`
  against the `r = 1` per-coordinate alternative — the framework's standing
  discrete fork (the runner checks the `w in {1/3, 1/2} <-> r in {1, 1/2}`
  arithmetic exactly; the empirical identification of that fork is
  contextual, carried by the open r-program stack, and is not consumed as
  authority here).
- **Write-side (named, not derived here):** conditional on R-FORM, the
  local formation frequency is a well-defined dynamical variable (the
  criterion either fires or does not, per site, under the realized
  dynamics), giving the time-rate object the halted mass-lane synthesis
  names as its single supplied step — with the already-measured comparator
  facts (registration onset threshold, noise boundary where register
  independence dies, dimensional impossibility below d = 3) as its
  empirical silhouette. Those measurements live in open PRs and are cited
  as context, not authority. Deriving the clock theorem is a successor
  block, not this note.

## Boundaries

- Conditional on the R-FORM packet (unregistered candidate), on the
  FRAME-EXT premise as already named, on Gleason's theorem as a declared
  textbook import (dimension >= 3), and on the write-class note's declared
  readings C1–C4. No probability language in this note is unconditional.
- The FINITE-ADDITIVITY-TO-FRAME gap remains open and named; this note
  narrows clause (4) only.
- No axiom edit, no registry edit, no Tier-A content, no audit-lane action,
  no formation rule adopted, no Born weight derived unconditionally.
- The minimal representative is `C^2` system, two `C^2` registers; nothing
  here asserts grain-wide universality beyond what the consumed write-class
  note itself claims.
- Sets no audit status.

## Panel

Framework-blind physicist panel (three lenses) run on the packet and
theorem before this PR; verdicts and repairs recorded in
`REVIEW_HISTORY.md` in the campaign pack.

## Runner verification map

| Block | Verifies | Expected |
|---|---|---|
| B1 | Verbatim quotes: four Record clauses; FRAME-EXT clauses + gap sentence; write-class classification sentence; formation no-go boundary sentence | all present |
| B2 | Two-register fan-out from two classified writes; exact discrimination; conditional independence given the outcome; disjointness | exact |
| B3 | Coincidence functional equals the sesquilinear diagonal `|c_i|^2`; normalization; register-basis invariance (content-determination) | exact |
| B4 | Single-register loophole: `f(P_n) = (1+n_z^3)/2` is additive/nonnegative/normalized on `M_2` yet not density-form (explicit non-linearity witness) | exact |
| B5 | Composite domain: the realized menu lives in `M_4` (dim 4 >= 3); the coincidence functional is density-form there by direct construction | exact |
| B6 | Counting arithmetic: `r = (1-w)/2w` maps `{1/3, 1/2}` to `{1, 1/2}` | exact |
| B7 | Negative controls: no-write (no discrimination); one-write-only (adjoint reversal succeeds — single register revocable); corrupted second witness (conditional dependence appears and the paired weight deviates) | exact |
| B8 | Compatibility obligations: disjoint records' readouts add, `I(empty) = 0`, one record per register site, branchwise repeat stability | exact |
