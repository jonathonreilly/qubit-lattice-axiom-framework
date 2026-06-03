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

## Command

```bash
/private/tmp/cl3-review-venv/bin/python3 /tmp/ks_eta_vs_jw_string_car_locality.py
# Expected: SCORECARD: PASS=23 FAIL=0
```
