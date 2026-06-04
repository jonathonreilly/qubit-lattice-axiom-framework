# Matter-attachment locality does not force cross-site CAR: the staggered KS eta is Dirac-structure, the JW string is statistics, and they are orthogonal

**Date:** 2026-06-02
**Claim type:** no_go (clean)
**Angle:** non-geometric / algebraic forcing of the cross-site CAR sign from the
matter-attachment construction. Companion to the two geometric no-gos (framing
writhe non-fibered; graph-braid exchange class is the wrong Z2).
**Runner:** `/tmp/ks_eta_vs_jw_string_car_locality.py` (SCORECARD PASS=23 FAIL=0,
deterministic, venv `/private/tmp/cl3-review-venv/bin/python3`).
**Scope:** read-only investigation; deliverables to /tmp only; no repo edit, no
branch/commit. Status authority would be the independent audit lane if landed.

## Question

The carrier bit needs the cross-site CAR/fermionic anticommutation sign. Matter
attaches to Z^3 via a Kogut-Susskind (KS) / staggered-fermion realization. Two
recent results show the GEOMETRIC source of the cross-site sign is non-fibered
and is the wrong Z2. **This note attacks the non-geometric, algebraic horn:** does
LOCALITY of the matter operator on Z^3 + the staggered/KS structure +
single-valuedness FORCE Jordan-Wigner cross-site anticommutation `b_i b_j = - b_j b_i`,
even though no geometric class supplies it? Concretely: do the staggered phases
`eta_mu(x) = (-1)^{x_1 + ... + x_{mu-1}}`, combined with locality, FORCE CAR; or do
they give only the Dirac/taste (gamma) structure and leave boson-vs-fermion OPEN?

## Verdict: OPEN (clean no-go). Locality + KS does NOT force CAR.

**The KS staggered construction supplies the Dirac/taste structure and is
statistics-neutral. The cross-site CAR sign is carried by a separate object — the
Jordan-Wigner string — which (i) is algebraically orthogonal to the staggered
`eta`, (ii) requires an arbitrary total ORDER on Z^3, and (iii) is genuinely
non-local. A maximally-local, nilpotent, single-occupancy matter operator that is
NOT CAR (the hard-core boson) exists and carries every KS premise. So
locality + the staggered phases do not force fermionic statistics; the
statistics choice stays a separate admission, consistent with the retained
`statistics_agnostic` no-go.**

Confidence: **high.** The decisive facts are exact finite-linear-algebra
identities on a 2x2x2 Z^3 patch (PASS=23 FAIL=0), and the verdict coincides with
two independently-retained no-gos on the live ledger (below).

## The two objects must not be conflated (the crux)

The prompt's key tension — JW-string sign (statistics) vs staggered `eta` sign
(Dirac structure) — resolves because they are *different mathematical objects
living on different tensor factors*:

| | staggered `eta_mu(x)` | Jordan-Wigner string `S_x` |
|---|---|---|
| nature | **c-number** per LINK (`+1`/`-1`) | **operator** `prod_{y<x} sigma_3^(y)` |
| source | spin-diagonalization `T(x)=sigma_1^{x1}sigma_2^{x2}sigma_3^{x3}` that absorbs the Dirac gammas (Kawamoto-Smit, substep 2) | converts commuting tensor ladders into anticommuting ones |
| role | **Dirac / taste structure** coefficient of the hopping term | **statistics** (boson <-> fermion frame) |
| lives in | the kinetic-operator COEFFICIENT | the matter OPERATOR `c_x` |
| support | the two link endpoints | the intermediate sites `{y : pi(x_lo) < pi(y) < pi(x_hi)}` |
| needs an order? | no (lattice-translation-covariant pattern) | **yes** (a total order `pi` on Z^3) |

Runner evidence that they are orthogonal (C5, the decisive block):
- **drop the string, KEEP `eta`** -> cross-site CAR FAILS (the bare ladders carrying
  `eta` in the Hamiltonian still commute cross-site: hard-core boson).
- **drop `eta`, KEEP the string** -> cross-site CAR STILL HOLDS (`c_x` contains no
  `eta` at all; `eta` only ever appears as the kinetic-term coefficient).

So `eta` cannot supply CAR and is not needed for CAR. The CAR sign rides the
string. They are independent.

## What the KS docs on main actually say (read, not assumed)

- **Substep 1 — Grassmann forcing** (`STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07`,
  live `unaudited`): sources the Grassmann property only via spin-statistics S2,
  and only proves *single-site* `chi_x^2=0` (per-site dim 2 vs infinite bosonic
  Fock). It does **not** establish cross-site `{chi_x, chi_y}=0`.
- **Substep 2 — Kawamoto-Smit forcing** (`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07`,
  live `unaudited`): derives the `eta_mu(x)` from the spin-rotation `T(x)` that
  diagonalizes the gamma structure, `T(x)^dag gamma_mu T(x+mu) = eta_mu(x) I`.
  These are explicitly the **Dirac-structure** signs (taste), NOT a JW string.
- **Substep 1 JW bridge** (`...jw_bridge_narrow_theorem_note_2026-05-17`, live
  `retained_pending_chain`, claim_type `decoration`): CONSTRUCTS cross-site CAR via
  the JW string but explicitly disclaims uniqueness ("Does **not** claim the JW
  representation is the unique cross-site CAR realization") and records (its §10)
  that the bare ladders COMMUTE on disjoint factors. Admits the total-order choice
  as an input.
- **statistics-agnostic no-go** (`...statistics_agnostic_no_forcing_note_2026-05-25`,
  live **`retained_no_go`**): the A1/A2 operator-algebra + dimension baseline does
  **not** select CAR over the hard-core boson; both are the same ungraded algebra
  `M_{2^N}(C)` in different frames; includes a "locality horn" (its (E)): the
  2x2x2 grid has bandwidth 4>1, so no order makes every neighbour adjacent.
- **FS rotation-exchange no-go** (`fs_rotation_exchange_discrete_insufficiency...2026-05-28`,
  live **`retained_no_go`**): the discriminator is the **cross-site graded-vs-ungraded**
  relation, not any on-site sign; retained locality (Lieb-Robinson tensor-locality)
  is **ungraded** (the bosonic signal); **graded** locality is not retained.
- **flavor carrier momentum-forced** (`flavor_carrier_from_axioms_momentum_forced_2026-05-31`,
  live `audited_conditional`): the staggered/KS first-order operator is needed for
  the *chiral* `{eps,D}=0` structure and the corner locus; its own discriminator
  calls the fermionization "compatibility, not forcing."

My finding is the precise *KS-internal sharpening* these imply but do not isolate
as one explicit test: the `eta` factors — the one KS-specific structure a
"locality forces CAR" argument would lean on — are demonstrably Dirac-structure
c-numbers, present identically in the boson and fermion Hamiltonians, and
orthogonal to the statistics-carrying string.

## What the runner establishes (PASS=23 FAIL=0)

On the 2x2x2 Z^3 patch (8 qubits, dim 256), lexicographic order, exact arithmetic:

- **C1** `eta_mu(x)` are the Kawamoto-Smit phases, reproduced from the
  spin-diagonalization `T(x)^dag gamma_mu T(x+mu)`; each is a pure `+-1` **c-number**
  carrying no operator/statistics content.
- **C2** The staggered KS hopping operator carries the *identical* `eta` sign on
  every link in BOTH realizations; every link term is nearest-neighbour LOCAL
  (supported on its two endpoints). `H_hcb != H_jw`, differing only by the string.
- **C3** The bare ladders `b_x = sigma_+^(x)` are maximally local (single-site),
  nilpotent (`b_x^2=0`, single occupancy), yet **commute** cross-site
  (`[b_x,b_y]=0`): a hard-core BOSON. So a local, nilpotent, single-occupancy
  matter operator exists that is **not** CAR.
- **C4** The JW-dressed `c_x = S_x sigma_+^(x)` satisfy full cross-site CAR
  (`{c_x,c_y}=0`, `{c_x,c_y^dag}=delta_{xy} I`, `c_x^2=0`).
- **C5** (decisive) CAR rides the **string**, not `eta` (both counterfactuals,
  above).
- **C6** HCB and JW generators span the **same** full `M_{2^N}(C)` (dim `4^N`);
  statistics is a frame choice on one ungraded algebra (reproduces the retained
  no-go on the patch).
- **C7** (locality horn) min grid-graph bandwidth over **all** orderings = 4 > 1;
  the lexicographic slow-axis link (0,0,0)-(1,0,0) spans 4 positions with a
  non-trivial string over the intermediate sites. A maximally-local matter
  operator carries NO string, so locality does not force the string / CAR.

## Why "locality + single-valuedness" does not rescue forcing

A "locality forces CAR" argument would need the matter operator's locality to
*entail* the string. It cannot, for three independent reasons the runner exhibits:
1. The **most** local matter operator (single-site `b_x`) has no string and is
   bosonic (C3). Locality, if anything, points away from the string.
2. The string is **non-local** by the bandwidth horn (C7): on Z^3 there is no
   total order making every nearest-neighbour link string-free, so the string is
   not a local object that locality could canonically generate.
3. The KS-specific structure (`eta`) is orthogonal to the string (C5) and lives in
   the kinetic coefficient, not the operator. "Single-valuedness of the field" is
   satisfied by the hard-core boson too; it does not select the graded frame.

The genuine selector, as the retained `fs_rotation_exchange` no-go states, is a
**graded-locality / fermion-parity-superselection** input (odd operators
anticommute at disjoint separation). That is not in A1+A2 and not supplied by the
KS construction; it is the missing ingredient.

## Missing ingredient (flagged)

The cross-site CAR sign requires ONE of (neither in A1+A2 / KS):
- a **graded-locality** axiom / fermion-parity superselection rule giving cross-site
  anticommutation directly (the `fs_rotation_exchange` §7 path 2), or
- a lattice-native **discrete-homotopy / graph-braid** Z2 coupled to an on-site
  spinor sign (the `fs_rotation_exchange` §7 path 1) — but the companion geometric
  results already show the available graph-braid / writhe class is the wrong Z2.

## Import flags

- **IMPORT FLAG: requires user approval — graded locality / fermion-parity
  superselection (`FS`) as an admitted input.** This is the statistics selector the
  KS construction does not supply. Per the live ledger it is an open admission
  candidate, not a derived theorem.
- No other imports used. Pure A1 (one qubit / Cl(3,0) spinor per site) + A2 (Z^3),
  the Kawamoto-Smit staggered phases (standard methodology, as in the on-main
  substep-2 note), and standard finite linear algebra. No PDG values, no fitted
  selectors, no new vocabulary.

## Ledger verification (live, `git show origin/main:docs/audit/data/audit_ledger.json`, 2026-06-02)

| row | effective_status |
|---|---|
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | **retained_no_go** |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | **retained_no_go** |
| `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` | retained_pending_chain (decoration) |
| `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` | retained_bounded |
| `axiom_first_spin_statistics_theorem_note_2026-04-29` | unaudited |
| `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` | unaudited |
| `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07` | unaudited |
| `fermion_parity_z2_grading_theorem_note_2026-05-02` | retained |

The verdict (locality+KS does not force CAR; statistics-neutral) is consistent
with the two retained no-gos and adds the explicit KS-`eta`-vs-JW-string
orthogonality test they did not isolate.

## What this does / does not claim

**Claims.** The staggered KS `eta` factors are statistics-neutral Dirac-structure
c-numbers; the cross-site CAR sign is the orthogonal JW-string object that needs an
order choice and is non-local; matter-attachment locality + KS therefore does
**not** force CAR. The boson-vs-fermion choice stays a separate admission.

**Does not claim.** Does NOT claim fermions are impossible on Z^3 (the JW frame
exists; CAR is *compatible*, not forced). Does NOT overturn any retained row. Does
NOT register the `FS` admission. Does NOT foreclose a future graded-locality or
lattice-native discrete-homotopy derivation of CAR — those remain open paths
("the next path this opens").

## No-go discipline gate (N1–N8)

**Status:** PASS for the narrow algebraic-horn no-go only. The claim being closed
is *not* "fermions cannot live on Z^3" and *not* "the JW representation is wrong".
It is the single statement that the staggered/KS construction (the `eta_mu(x)`
Kawamoto-Smit phases) + matter-attachment locality + single-valuedness do not, by
themselves, force the cross-site CAR sign `b_i b_j = - b_j b_i` over the hard-core
boson. The decisive object is the C5 counterfactual pair on the 2x2x2 Z^3 patch:
drop the string keep `eta` -> CAR fails; drop `eta` keep the string -> CAR holds.

### N1 - Alternative route enumeration

Each route below is a concrete way an opponent might try to force CAR *from the KS
construction itself* (i.e. without admitting graded locality / `FS`). Each is
exhibited and refuted on the 2x2x2 patch.

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| `eta`-as-statistics route | Read the staggered `eta_mu(x)` sign as the cross-site anticommutation sign, so locality-of-`eta` would deliver CAR. | C1/C2/C5: `eta` is a per-link `+-1` c-number in the kinetic COEFFICIENT, identical in `H_hcb` and `H_jw`; `c_x` contains no `eta`. Dropping `eta` keeps CAR; keeping `eta` without the string loses CAR. `eta` neither supplies nor is needed for CAR. | ATTEMPTED |
| Locality-generates-the-string route | Argue that requiring the matter operator to be local forces a Jordan-Wigner tail. | C3/C7: the MOST local matter operator (single-site `b_x = sigma_+^(x)`) carries NO string and is bosonic (`[b_x,b_y]=0`); the string is provably non-local (min grid-graph bandwidth over all orderings = 4 > 1). Locality points away from the string, not toward it. | ATTEMPTED |
| Single-valuedness route | Claim "the field must be single-valued" selects the graded (fermionic) frame. | The hard-core boson `b_x` is single-valued, nilpotent (`b_x^2=0`), and single-occupancy and satisfies every stated KS premise (C3). Single-valuedness is satisfied by both frames and does not discriminate. | ATTEMPTED |
| Per-site Grassmann-uplift route | Use substep-1 Grassmann forcing (`chi_x^2=0`) to upgrade per-site nilpotency into cross-site `{chi_x,chi_y}=0`. | The cited substep-1 note proves only single-site `chi_x^2=0` (dim-2 per site) and explicitly does not establish cross-site `{chi_x,chi_y}=0`; the hard-core boson already has `b_x^2=0` cross-site-commuting (C3). The uplift is exactly the gap, not a route across it. | ATTEMPTED |
| Algebra-spanning route | Argue HCB and JW generate the same operator algebra, so CAR is "already there". | C6: both span the same ungraded `M_{2^N}(C)` (dim `4^N`); sameness of the ungraded algebra is precisely why statistics is an unfixed frame choice (the retained `statistics_agnostic` result). Spanning the algebra does not select the graded relation. | ATTEMPTED |
| Choose-the-order route | Pick a total order `pi` on Z^3 that makes the JW string trivial (string-free) on every nearest-neighbour link, so the string "isn't really non-local". | C7: bandwidth horn — over ALL orderings the min grid-graph bandwidth is 4 > 1, so no order makes every NN link adjacent; some link always carries a non-trivial string. The order cannot be removed; it is an arbitrary admitted input. | ATTEMPTED |
| Graded-locality / `FS` route | Admit fermion-parity superselection (odd operators anticommute at disjoint separation) to deliver CAR directly. | This is the genuine selector — and it is exactly the flagged import requiring user approval (it is NOT in A1+A2 and NOT supplied by KS). Admitting it does not refute the no-go; it confirms the no-go's own statement that CAR needs an external input. | ATTEMPTED (out of scope — confirms, not breaks) |

### N2 - Wall-independence audit

The collapsed wall set for this no-go is a SINGLE wall: the statistics frame
(graded vs ungraded) is not fixed by any structure the KS construction provides;
it lives in the cross-site (anti)commutation relation of the matter operator, not
in the kinetic coefficient `eta` and not in per-site nilpotency. The three reasons
listed in "Why locality + single-valuedness does not rescue forcing" (most-local
operator is bosonic; string is non-local by the bandwidth horn; `eta` is orthogonal
to the string) are not three independent walls — they are three views of the one
wall (locality cannot reach the cross-site graded relation). The two retained
ledger no-gos are *concordant external witnesses* to this same wall, not extra
independent walls: `statistics_agnostic` states the algebra baseline does not
select CAR (same wall, algebra view); `fs_rotation_exchange` states the
discriminator is the cross-site graded-vs-ungraded relation and that retained
Lieb-Robinson locality is ungraded (same wall, locality view). **What future work
could change it:** a derivation of graded locality / `FS` from A1+A2, or a
lattice-native discrete-homotopy / graph-braid `Z2` coupled to an on-site spinor
sign, would move the wall — both are named as open in "Missing ingredient".

### N3 - Hidden-wall scan

The words "standard", "framework", "obviously", "must", and "canonical" are not
used as hidden retained inputs for the negative result. ("standard" appears only to
label the Kawamoto-Smit phases and finite linear algebra as ordinary methodology,
not as a load-bearing premise.) The EXPLICIT load-bearing inputs of the no-go are
exactly: (i) A1 = one qubit / Cl(3,0) spinor per site; (ii) A2 = the Z^3 lattice;
(iii) the Kawamoto-Smit staggered phase definition
`eta_mu(x) = (-1)^{x_1 + ... + x_{mu-1}}` and `T(x)^dag gamma_mu T(x+mu) = eta_mu(x) I`;
(iv) the hard-core-boson ladder `b_x = sigma_+^(x)` and the JW-dressed
`c_x = S_x sigma_+^(x)` with `S_x = prod_{y<x} sigma_3^(y)`; (v) exact finite linear
algebra on the 2x2x2 patch (dim 256). No appeal to "what fermions usually do",
"the standard lattice fermion", or any rhetorical authority carries weight; every
sign in C1-C7 is an exhibited matrix identity. The only non-derived ingredient is
the *absent* one (graded locality / `FS`), which is named as an import, not hidden.

### N4 - Residual matching

Each cited prior result is checked against the residual it actually attacks versus
the residual at issue here (does the KS construction force cross-site CAR?).

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `statistics_agnostic_no_forcing_note_2026-05-25` (retained_no_go) | A1/A2 operator-algebra + dimension baseline does not select CAR over hard-core boson (same ungraded `M_{2^N}(C)`); includes a locality horn. | KS-specific `eta`-vs-string sharpening of the same non-forcing of CAR. | yes |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` (retained_no_go) | The discriminator is the cross-site graded-vs-ungraded relation; retained Lieb-Robinson locality is ungraded. | Identifies the same graded relation as the missing selector the KS `eta` cannot supply. | yes |
| `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` (unaudited) | Derives `eta_mu(x)` as the Dirac/taste (gamma-diagonalization) structure. | Used only to fix WHAT `eta` is (Dirac-structure c-number), the object shown statistics-neutral. Not invoked as forcing CAR. | yes (as definition, not as forcing) |
| `staggered_dirac_substep1_jw_bridge_narrow_theorem_note_2026-05-17` (retained_pending_chain, decoration) | Constructs cross-site CAR via the JW string; disclaims uniqueness; records bare ladders commute on disjoint factors; admits total-order input. | Corroborates that CAR rides the string and needs an order; its own non-uniqueness disclaimer is what this no-go formalizes. | yes |
| `staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16` (retained_bounded) | Per-site Grassmann property `chi_x^2=0` via spin-statistics; single-site only. | Bounds the per-site horn; does NOT reach cross-site CAR — so it is not a witness that CAR is forced. | not load-bearing (per-site only; does not match the cross-site residual) |
| `flavor_carrier_from_axioms_momentum_forced_2026-05-31` (audited_conditional) | The staggered/KS first-order operator is needed for chiral `{eps,D}=0` + corner locus; calls fermionization "compatibility, not forcing." | Concordant on "compatibility, not forcing", but it is about chirality/corner-locus, not the CAR sign. | not load-bearing (different residual; cited only for the concordant "compatibility" verdict) |

Non-matching witnesses are explicitly marked "not load-bearing" and are not used as
proof of the no-go; the no-go rests on the two `retained_no_go` rows plus the
exhibited C1-C7 patch identities.

### N5 - Rhetoric audit

- **"orthogonal"** is scoped to: the staggered `eta` c-number (a kinetic-term
  coefficient on the link endpoints) carries no operator/statistics content, and the
  JW string operator (on the intermediate sites) carries no `eta`; the C5
  counterfactuals make this exact. It does NOT claim Dirac structure and statistics
  are orthogonal *in every formulation of lattice fermions* — only that in this KS
  realization the two specific objects live on different tensor factors and neither
  determines the other.
- **"statistics-neutral"** is scoped to the `eta` factors specifically: they are
  identical in `H_hcb` and `H_jw` (C2). It does NOT claim the whole KS construction
  is statistics-neutral in some global sense; the *choice* of dressing (string or
  none) is exactly what fixes statistics.
- **"does not force"** is scoped to: KS + locality + single-valuedness do not, by
  themselves, *entail* cross-site CAR. It does NOT claim CAR is unreachable, nor
  that no axiom set forces it; with the flagged `FS` import (or a future
  discrete-homotopy route) CAR is reachable.
- **"non-local" (of the string)** is scoped to: on Z^3 no total order makes every
  NN link string-free (bandwidth >= 4, C7). It does NOT claim the JW construction is
  ill-defined or that fermions are non-local as physics — only that the string is
  not an object locality can canonically generate.
- **"no-go" / "OPEN"** denotes that the forcing question is open (CAR not forced),
  i.e. a negative result on *forcing*, NOT a positive prohibition on CAR existing.
  The over-broad reading "CAR is forbidden / fermions are excluded on Z^3" is
  explicitly disclaimed.

### N6 - Partial-closure path scan

The following non-axiom partial-closure paths remain OPEN and none is called a new
axiom by this note:
- a derivation of **graded locality / fermion-parity superselection (`FS`)** from
  A1+A2 (would close the gap from inside the axioms; currently an admission
  candidate, NOT asserted as an axiom here);
- a **lattice-native discrete-homotopy / graph-braid `Z2`** coupled to an on-site
  spinor sign (the `fs_rotation_exchange` §7 path 1) — left open even though the two
  companion geometric no-gos show the *currently available* graph-braid/writhe class
  is the wrong `Z2`;
- a sharper **cross-site Grassmann uplift** that would carry single-site `chi_x^2=0`
  to `{chi_x,chi_y}=0` without an external statistics input (currently unestablished,
  per substep-1).
Each is described as a route to *future positive work*, not as a postulate; the note
registers none of them and adds no axiom.

### N7 - Steelman

The strongest objection: in a *physical* lattice gauge theory the staggered field is
declared Grassmann from the outset (spin-statistics is assumed at the path-integral
level), so "the KS construction" — taken to include that declaration — *does* come
with CAR, and treating `eta` and the string as separable is reading the construction
too narrowly. **Why it does not break the SCOPED claim:** the objection smuggles in
exactly the statistics declaration (Grassmann / fermion-parity) that this no-go
isolates as the missing ingredient. The substep-1 Grassmann note sources that
property only from spin-statistics S2 and proves only the per-site `chi_x^2=0`; it
does not derive cross-site `{chi_x,chi_y}=0` from A1+A2+KS. So the steelman concedes
the no-go's own claim (an external statistics input is required) rather than refuting
it. **What broader claim the steelman does block:** any reading of this note as
"staggered fermions are not really fermions" or "the standard KS fermionization is
defective" — that broader claim is false and is not made here; standard KS *with* the
assumed Grassmann/`FS` input is perfectly CAR, the note only denies that locality + the
`eta` phases *alone* supply that input.

### N8 - Cross-cycle echo

The repo's recurrent overclaim failure mode is: *test one representative
expression/operator, find it negative, then declare the whole lane closed*
(the "tested-one-witness, declared-the-lane-dead" echo). This note avoids that echo
in three concrete ways: (i) it tests BOTH directions of the decisive
counterfactual (drop-string-keep-`eta` AND drop-`eta`-keep-string, C5), not a single
operator; (ii) it fixes the claim boundary at *forcing from KS + locality* and
explicitly leaves CAR reachable via the flagged `FS` import and via future
discrete-homotopy / cross-site-Grassmann routes (N6), rather than declaring "no
fermions on Z^3"; (iii) it cross-checks its verdict against two independently
`retained_no_go` rows on the live ledger plus the non-uniqueness disclaimer of the
JW-bridge decoration, so the negative result is corroborated, not extrapolated from
the single 2x2x2 patch. The patch is finite (dim 256); the note treats the C1-C7
identities as an existence-of-a-counterexample (the hard-core boson exists and
carries every KS premise), which is logically sufficient for a *non-forcing* claim
and does not over-reach to a universal prohibition.

## Command

```bash
/private/tmp/cl3-review-venv/bin/python3 /tmp/ks_eta_vs_jw_string_car_locality.py
# Expected: SCORECARD: PASS=23 FAIL=0
```
