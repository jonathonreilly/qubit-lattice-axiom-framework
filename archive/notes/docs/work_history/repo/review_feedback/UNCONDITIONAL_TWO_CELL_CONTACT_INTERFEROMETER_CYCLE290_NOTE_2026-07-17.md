# Unconditional two-cell contact interferometer — Cycle 290

**Date:** 2026-07-17

**Type:** constructive fixed-number contact-action comparator on the connected
physical-M2 code

**Status:** bounded two-cell fixture constructed and executable; coherent
branch routing and read remain supplied

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/unconditional_two_cell_contact_interferometer_cycle290_2026_07_17.py
```

This cycle creates only this note and runner. It changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, or audit-status surface.

## Result up front

Cycle 290 constructs a bounded **unconditional** contact interferometer. It
removes both weaknesses of the Cycle-285 calibration routes that matter for
this question:

1. the contact action is never controlled by an auxiliary flag; and
2. the coherent branches have the same exact total particle number.

Take two adjacent six-mode coarse cells `x,y`. The supplied coherent branch
pair is

```text
|r> = |N_x=3,N_y=3>,
|s> = |N_x=4,N_y=2>.
```

One occupied direction mode of `y` is moved to one empty direction mode of
`x`. This is a single bounded, number-preserving even bilinear redistribution.
Both branches have **fixed total N=6** and even total parity. Their contact
pair counts are

```text
P(r) = binom(3,2)+binom(3,2) = 6,
P(s) = binom(4,2)+binom(2,2) = 7.
```

Apply the ordinary local law at both cells,

```text
W_xy = W_g(x) W_g(y),
W_g(z) = exp(i g binom(N_z,2)),
g = 0.37.
```

The same `W_xy` acts in both branches. There is no controlled-`W_g` oracle.
The common phase `exp(i6g)` cancels and the surplus branch retains relative
phase `exp(ig)`. A supplied matched path recombiner therefore gives

```text
p_dark = sin^2(g/2) = 0.03383632719698277.
```

This is a coherent comparator close. It does not select a realized member or
make the close carrier permanent.

The decisive Q-only replacement is exact. For

```text
Q_z = 1_(N_z>=2),
W_Q,xy = exp(i g[Q_x+Q_y]),
```

both branches have `Q_x+Q_y=2`. The replacement is a common phase and the
comparator close is exactly zero. Deleting `W_g` or replacing it by any common
global phase also gives zero. Replacing `W_g` by `W_g^dagger` preserves the
unsigned close and reverses the supplied signed marker quadrature.

On the Cycle-278/269 connected physical-M2 code, each `W_g` is its exact
64-term Walsh polynomial in the six mapped local parity operators. The route
uses the actual mapped adjacent stream hopping generator `A_e`. The runner
tests both local action blocks and the connector at `L=3,4,5` and held-out
`L=6`, with zero local-check or Wilson leakage. It also carries the entire
two-cell motif through **648 frame-translation tests**: all 24 proper-cubic
frames and all 27 translations at `L=3`.

The result is a constructive removal of the controlled-action and
cross-number-reference imports. It is not a complete autonomous apparatus:
the branch state, one path-marker M2, coherent one-hop route, inverse route,
marker basis change, read basis, coupling, and action insertion are explicit
supplies. Scoped only to the Cycle-290 reviewed two-cell encoding, runner
controls, and cited same-code surfaces, there is no shared obstruction and no
axiom pressure. Unreviewed encodings, apparatus syntheses, preparations, and
autonomous completions remain unknown.

## 1. Exact branch fixture

For an executable representative, direction bits are ordered `0,...,5` and
the two branches use

```text
r_x = 001110,   r_y = 000111,       counts (3,3),
s_x = 001111,   s_y = 000101,       counts (4,2).
```

The change moves the occupied `y` direction-1 mode into the empty `x`
direction-0 mode. Those two vertices are the endpoints of the adjacent
`+x/-x` stream edge in the Cycle-235/269 graph. Its mapped `A_e` is a bounded
physical Pauli representative of the even hopping generator.

The choice of a representative direction is not an invariant-state claim.
Proper-cubic transformations carry it to the corresponding oriented adjacent
pair and transformed endpoint modes. The family, not one selected member, is
covariant.

The two branches are orthogonal, have the same total number, and remain inside
the declared total-even matter algebra. This is materially stronger than the
Cycle-285 direct `N=2/N=4` reference: no cross-number coherence is needed.

## 2. Explicit path marker, route, action, and recombiner

Let `p` be one supplied path-marker M2 and let the two-dimensional matter
subspace be spanned by `|r>,|s>`. Start from

```text
|0>_p |r>.
```

The exact circuit is

```text
H_p ; R_(p: r<->s) ; [W_g(x)W_g(y)] ; R^dagger ; H_p ; Z_p close.
```

Here `R` uses the single intercell redistribution only in the marker-one
branch. It is a supplied branch router. The action in square brackets is

```text
I_p tensor W_xy,
```

not

```text
|0><0|_p tensor I + |1><1|_p tensor W_xy.
```

The runner compares the two marker diagonal blocks and the off-diagonal
blocks of the action matrix. The marker blocks are identical and the
off-diagonal blocks vanish. Thus the action is ordinary and unconditional;
only the state-routing apparatus refers to the marker.

After the inverse route, matter returns to `|r>` and the marker is

```text
(|0> + exp(ig)|1>)/sqrt(2)
```

up to the common `exp(i6g)` scalar. The final `H_p` gives the displayed dark
close. Before that `H_p`, a supplied marker-`Y` quadrature has magnitude
`|sin(g)|`. The adjoint action reverses its sign.

## 3. Exact action and replacement controls

| fixture | relative branch phase | dark close |
|---|---:|---:|
| actual ordinary `W_g(x)W_g(y)` | `g` | `sin^2(g/2)=0.03383632719698277` |
| delete the contact action | `0` | `0` |
| Q-only replacement | `g(2-2)=0` | `0` |
| common global scalar | `0` | `0` |
| ordinary `W_g^dagger(x)W_g^dagger(y)` | `-g` | same positive close |

The unsigned close is sign blind. The signed marker quadrature is not: its two
expectations are equal and opposite for `W_g` and `W_g^dagger`.

These controls distinguish actual number-dependent pair counting from mere
contact activity. They do not infer which coupling or action law the framework
must select; `g=0.37` and insertion of `W_g` are still supplied physical-law
content.

## 4. Deletion and split controls

The runner evaluates the complete four-dimensional marker-times-branch
circuit rather than assigning expected labels by hand.

| deletion or replacement | exact dark close | interpretation |
|---|---:|---|
| delete `W_g` only | `0` | positive ideal close requires the ordinary action |
| delete incoming route only | `1/2` | unmatched inverse route leaves path information |
| delete outgoing inverse route only | `1/2` | un-erased matter branch destroys interference |
| delete both routes | `0` | matched bypass returns the marker close to zero |
| delete preparation `H_p` only | `1/2` | unmatched read basis is not a faithful action test |
| delete recombiner `H_p` only | `1/2` | direct path-basis read is balanced |
| delete both `H_p` factors | `0` | matched basis bypass closes |

The one-sided deletion values are intentionally not called action evidence.
They expose the route/recombiner boundary. Only the matched circuit with the
action replacement controls supports the contact-action conclusion.

## 5. Fixed-N=2 minimal steelman and why it is not decisive

A still smaller two-cell comparator uses two particles:

```text
|separated>  <->  |co-located>.
```

The ordinary onsite contact law is identity on the separated branch and gives
relative phase `g` on the co-located branch. It is an unconditional,
fixed-total-number constructive route, and the runner retains it as a strict
steelman.

However, on this subspace the threshold-only `W_Q` has exactly the same two
eigenvalues as actual `W_g`. Both predict `sin^2(g/2)`. The N=2 fixture cannot
satisfy the requested Q-only rejection control. This is why the primary
fixture uses `|3,3>` and `|4,2>`: it keeps the same bounded two-cell geometry
and fixed number while making Q-only a common phase.

The older fixed-N=4 five-cell fallback—four particles co-located versus four
single occupancies—also rejects Q-only at a cost of five cells. The primary
two-cell N=6 fixture supersedes it.

## 6. Same-code physical realization and support

For each cell, Cycle 285 represents the actual action as

```text
W_g(z) = sum_(m in {0,1}^6) w_m product_d B_(z,d)^(m_d).
```

All 64 Walsh coefficients are nonzero. Reconstruction of all 64 local
eigenvalues was already exact to numerical tolerance. Cycle 290 imports that
coefficient routine and places two copies at adjacent cells; it does not
replace `W_g` by `Q`.

The two-cell route connector is the actual `A_e` associated with the declared
stream edge. The support audit unions:

1. six mapped `B` operators at `x`;
2. six mapped `B` operators at `y`;
3. the mapped adjacent hopping connector `A_e`; and
4. one carried path-marker M2.

At every tested size the matter support is exactly `35 M2` and the complete
declared block is exactly `36 M2`, including the path marker. Every local
contact Pauli term has weight at most 12; the connector has weight five. These
are constant bounds independent of lattice size.

Every one of the `2*64` contact Pauli terms and the connector commutes with all
bounded local checks and all three Wilson-center operators. The aggregate
leakage count is zero at `L=3,4,5,6`.

This realizes the action and the even intercell connector on the same
connected physical code. It does not synthesize the complete controlled route,
Hadamard, or read from a single selected homogeneous microscopic gate law.

## 7. One-particle mass fixture

The contact action obeys

```text
W_g|_(N=0,1) = I.
```

Cycle 290 rechecks this on all local columns and imports the Cycle-219 rest
mass fixture through Cycle 278. The numerical analytic-to-operational mass
ratio remains one within `2e-12`.

The interferometer itself lives at total `N=6`; it does not derive an
interacting mass correction. The statement is compatibility: adding the
tested contact block leaves the existing one-particle mass fixture unchanged.

## 8. Proper-cubic covariance and held-size control

At `L=3`, for each of 24 proper-cubic frames and 27 translations, the runner:

1. composes the graph frame and translation maps;
2. computes the same local gauge repair used by Cycles 269 and 285;
3. transforms both six-`B` cell families;
4. transforms the actual adjacent `A_e` connector;
5. checks the transformed local-check family; and
6. compares every operator with the target transformed motif.

All **648 frame-translation tests** must pass. The oriented fixture is carried
as a covariant family. No preferred global ordering, nonlocal parity service,
or fixed direction is introduced.

Independent size tests run at `L=3,4,5` and held-out `L=6`. `L<3` is rejected
because the six-neighbor periodic geometry aliases there. The support bound
and zero leakage are required on the held size before this note is green.

## 9. Lawful domain

The exact tested domain is:

1. two adjacent Cycle-278/269 connected-code cells on a periodic cube `L>=3`;
2. the declared six-mode occupation representatives for `|3,3>` and `|4,2>`;
3. fixed total particle number six and even total parity;
4. one declared adjacent mapped stream connector;
5. actual `g=0.37` contact action at both cells;
6. one supplied path-marker M2;
7. supplied marker preparation, route, inverse route, recombiner, and read
   basis;
8. Walsh and code arithmetic at tolerance `3e-11`; and
9. `L=6` as held-out size.

The runner rejects `L<3`, a local cell dimension other than six occupation
modes, and a marker carrier other than M2.

## 10. Supplied structure inventory

| item | status | reason |
|---|---|---|
| `g=0.37` | supplied | empirical coupling fixture |
| actual functional form `binom(N,2)` | supplied | retained Cycle-230 candidate law |
| insertion of `W_g` at both cells | supplied | no unique law-selection result |
| adjacent cell pair and stream connector | supplied | bounded motif member selected |
| `|3,3>` representative | supplied | branch preparation not autonomous |
| path-marker M2 in `|0>` | supplied | fresh carrier and initialization |
| marker `H` | supplied | phase-reference preparation/read basis |
| controlled one-hop route and inverse | supplied | coherent branch apparatus |
| marker close effect and signed `Y` read | supplied | coherent read convention |
| relative phase `g` | derived | exact pair-count difference `7-6` |
| Q-only zero | derived | exact threshold-count difference `2-2` |
| dark close `sin^2(g/2)` | derived | exact four-dimensional circuit |
| bounded same-code support | derived | physical Pauli union audit |
| zero check/Wilson leakage | derived | exact Pauli commutators |
| all-frame covariance | derived | 648 operator-family comparisons |

The path marker is a coherent M2 carrier. Pointer copying is not invoked, and
no realized-history or permanence claim is made. Circuit order is only the
declared finite composition. The phase is dimensionless and receives no
source interpretation.

## 11. Dependency-ledger effect

| wall | Cycle-290 movement | residual |
|---|---|---|
| `C_ref` | fixed-number same-code path reference replaces the cross-number Cycle-285 reference | branch state, marker initialization, route, recombiner, and phase convention remain supplied |
| `C_num` | exact two-cell fixed-total-N=6 discriminator; no number-sector coherence | odd-state/full-Fock common embedding is not advanced |
| `C_wrap` | 648 motif-covariance tests and held `L=6`; connector remains bounded | whole-torus update/state preparation is not claimed |
| `C_int` | actual ordinary `W_g` is distinguished from deletion, Q-only, global phase, and adjoint without controlled `W_g` | coupling and action-law selection remain supplied |
| `C_local` | two action blocks and one even connector share a bounded zero-leakage physical neighborhood | complete route/H/read synthesis from one selected local law remains open |
| `C_source` | unchanged | no source or reciprocal geometry law is tested |

This is a real gain in the interaction and locality lanes. It removes an
auxiliary controlled-action oracle from the best action comparator. It does
not justify changing the five-lane maturity scores on its own: operational
quantum remains bounded-apparatus incomplete, matter retains a supplied
interaction law, and the causal-history, gravity/source, and Born-selection
lanes are unchanged.

## 12. No-go discipline N1–N8

The main result is constructive. The negative statements are narrow scope
boundaries: this two-cell circuit does not autonomously prepare its branch,
select its law, synthesize all apparatus from one microscopic rule, or select
a realized close. The no-go-discipline skill is applied so none of those
unfinished implementations is promoted into a substrate obstruction.

### N1 — alternative-route enumeration

The broad candidate negative would say that a bounded ordinary-contact
comparator cannot avoid a controlled-action oracle or cross-number coherence.
The following Cycle-290 runner routes attack that statement. Every honesty
marker is one of the two strings allowed by the current skill; Cycle 290 needs
only `ATTEMPTED` because every listed route is exercised here.

| route/control | honesty marker | exact Cycle-290 disposition |
|---|---|---|
| fixed-total `|3,3> <-> |4,2>` two-cell path | **ATTEMPTED** | succeeds; Q-only cancels exactly and ordinary `W_g` gives relative `g` |
| fixed-total N=2 separated/co-located two-cell path | **ATTEMPTED** | succeeds as an unconditional comparator; its Q-only discriminator is exactly degenerate |
| delete ordinary `W_g` while retaining matched apparatus | **ATTEMPTED** | close becomes zero |
| replace `W_g` by Q-only action | **ATTEMPTED** | common phase; close becomes zero |
| replace `W_g` by common global phase | **ATTEMPTED** | close becomes zero |
| replace `W_g` by its adjoint | **ATTEMPTED** | same unsigned close, opposite signed quadrature |
| delete either route half | **ATTEMPTED** | close becomes `1/2`; exposes unmatched path information |
| delete both route halves | **ATTEMPTED** | matched bypass gives zero |
| delete either marker `H` factor | **ATTEMPTED** | one-sided deletion gives `1/2` |
| delete both marker `H` factors | **ATTEMPTED** | matched basis bypass gives zero |

The earlier Cycle-285 controlled-process Ramsey and cross-number reference are
constructive context in N4/N8, not Cycle-290 honesty rows and not prior
exclusions. The current broad no-go therefore **FAILS** N1 and is demoted to
the constructive scoped result above. Live routes include a same-law
collision-and-recombination block, a finite mapped-hopping synthesis of `R`,
and homogeneous branch preparation. Their open status is evidence against any
impossibility wording.

### N2 — wall-independence audit

The raw named open conditions are:

- `K_branch`: prepare the fixed-number branch superposition and bounded route;
- `K_law`: select `g`, the pair-count action, and its insertion;
- `K_read`: supply the coherent marker basis and close test; and
- `K_auto`: autonomously place and run the complete motif from homogeneous
  admissible data.

“Close first” and “close second” below mean discharge that complete named
condition, not merely improve it.

| pair | close first => close second? | close second => close first? | independent? | witness / collapse action |
|---|---:|---:|---:|---|
| `K_branch`, `K_law` | no | no | yes | branch circuit runs with deletion/Q replacement; `W_g` exists without branch preparation |
| `K_branch`, `K_read` | no | no | yes | route can be prepared before read; one-sided read deletion leaves the branch route present |
| `K_branch`, `K_auto` | no | yes | no | running the complete motif autonomously includes autonomous branch preparation and routing; collapse `K_auto` as downstream composite |
| `K_law`, `K_read` | no | no | yes | physical `W_g` exists before marker read; a supplied read can be defined for deletion/Q controls |
| `K_law`, `K_auto` | no | yes | no | running the complete motif autonomously includes selecting/inserting its action; collapse `K_auto` as downstream composite |
| `K_read`, `K_auto` | no | yes | no | running the complete motif autonomously includes its read stage; collapse `K_auto` as downstream composite |

The collapsed independent set is exactly `{K_branch, K_law, K_read}`.
`K_auto` is a downstream integration objective, not a fourth independent wall.
The three surviving entries are supplied imports and live construction targets,
not impossibility results. The table provides no evidence that any target
resists constructive closure.

### N3 — hidden-wall scan

| phrase/concept | explicit content |
|---|---|
| branch preparation | fixed representative state and marker `H` are supplied |
| coherent control | route `R` and inverse are supplied; contact action is not controlled |
| reference frame | marker `H/Y/Z` phase convention is supplied |
| boundary/initialization | `L>=3`, two adjacent cells, and blank marker are declared |
| selected action | `g=0.37`, pair-count law, and insertion at both cells are supplied |
| read | coherent close effect is supplied; stronger semantics are excluded |
| geometry | proper-cubic transformed motif family is tested, not invariant preparation |

The load-bearing phrase scan found no uncatalogued use of “we assume,” “by
construction,” “as is standard,” “the framework provides,” “bridge context,”
“background,” “naturally,” “obviously,” “standard QFT,” “registered,” or
“canonical.” Every operative input is in the inventory above.

### N4 — residual matching

| cited witness | exact retained residual | Cycle-290 use | match? |
|---|---|---|---:|
| [Cycle 230:180–183](./SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md) | `W_g` phase is `g binom(N,2)` and identity at `N<=1` | pair counts and mass preservation | yes |
| [Cycle 230:160–170](./SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md) | stream has bounded two-layer fermionic swaps | one adjacent even redistribution route | yes, local connector only |
| [Cycle 278:34–49,104–124](./CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md) | six mapped `B` operators give bounded 64-term contact functions | physical `W_g` Walsh blocks | yes |
| [Cycle 278:64–89](./CONNECTED_EDGE_SAME_CODE_LOCAL_INSTRUMENT_CYCLE278_NOTE_2026-07-17.md) | same-code support is bounded and check/Wilson preserving | two-cell support and leakage audit | yes |
| [Cycle 285:129–169](./ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md) | actual `W_g` differs from threshold and has exact physical Walsh expansion | Q-only rejection and physical action | yes |
| [Cycle 285:298–343](./ACTUAL_CONTACT_ACTION_SYNDROME_TOURNAMENT_CYCLE285_NOTE_2026-07-17.md) | unconditional cross-number reference detects actual action | prior route improved to fixed-number two-cell path | yes |
| [Cycle 269:53–65](./WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md) | `A_e` is the connected-code hopping generator and Wilson center lies in matter algebra | adjacent route connector | yes |

No fixed-number after-the-fact density residual is used against process
interference. The path marker is present before the action and retains the
relative phase.

### N5 — resolution and rhetoric audit

This inventory covers every substantive negative or “not-a-fact” phrase in
the note. Repeated phrasings with the same tested residual are grouped under
one ID and quoted together. Administrative scope statements and rejected
candidate negatives are included so they cannot silently acquire physics
content. The runner's physics-bearing negative labels map to `R2` (ordinary
action rather than controlled action), `R10` (deletion faithfulness), and
`R11` (N=2/Q-only degeneracy). Its remaining `not`, `FAIL`, and `!=` tokens
are executable Boolean/test mechanics, not scientific rhetoric.

| ID | exact negative phrase(s) or close variants elsewhere in this note | narrow reading used here |
|---|---|---|
| `R1` | “changes no axiom...” | administrative two-file diff statement |
| `R2` | “never controlled by an auxiliary flag”; “no controlled-`W_g` oracle”; action “not” the controlled matrix; “contact action is not controlled”; “needs no controlled oracle” | marker blocks of the tested action are identical |
| `R3` | “does not select a realized member”; “pointer copying is not invoked”; “no realized-history or permanence claim”; “stronger semantics are excluded”; “do not infer stronger semantics” | those semantic questions are outside the tested observable algebra |
| `R4` | “not a complete autonomous apparatus”; “bounded-apparatus incomplete”; “not a complete physical apparatus or universal measurement mechanism” | the Cycle-290 runner imports the listed apparatus operations |
| `R5` | “no shared obstruction”; “no axiom pressure”; “none requires an axiom edit” | scoped Cycle-290 conclusion; unreviewed resolutions stay unknown |
| `R6` | “not an invariant-state claim”; family, “not one selected member”; invariant choice untested | covariance of a transformed family is tested; invariant selection is outside scope |
| `R7` | “no cross-number coherence is needed”; “no number-sector coherence” | both tested branches have total `N=6` |
| `R8` | signed quadrature “is not” sign blind | the tested `Y` expectations reverse sign |
| `R9` | controls “do not infer” a coupling/law; “no unique law-selection result”; law-selection remains supplied | Cycle 290 fixes `g` and the action instead of deriving them |
| `R10` | unmatched read “is not a faithful action test”; one-sided deletions “not called action evidence”; “no fixed-number after-the-fact density residual is used” | exact block deletion controls delimit the inference |
| `R11` | N=2 “cannot reject” Q-only and is “not decisive” | actual and Q-only N=2 closes are equal in the runner |
| `R12` | Walsh import “does not replace `W_g` by `Q`” | actual complex Walsh coefficients are used in both cells |
| `R13` | “does not synthesize” the route/H/read; branch preparation “not autonomous”; autonomous routing remains supplied | source inspection and supplied inventory for this runner |
| `R14` | “does not derive an interacting mass correction”; interacting spectrum untested | only one-particle identity and mass compatibility are tested |
| `R15` | “no preferred global ordering, nonlocal parity service, or fixed direction is introduced” | the tested mapped motif uses local Pauli words and a transformed frame family |
| `R16` | full-Fock embedding “is not advanced”; whole-torus update/preparation “is not claimed”; source law “is not tested”; phase receives “no source interpretation”; maturity scores do “not” change | dependency-ledger scope statements |
| `R17` | broad candidate says a comparator “cannot avoid” the imports; broad no-go **FAILS**; prior routes are “not prior exclusions” | rejected candidate negative, not a shipped conclusion |
| `R18` | open conditions are “not impossibility results”; table gives “no evidence” of resistance | classification of the collapsed N2 wall set |
| `R19` | phrase scan found “no uncatalogued use” of hidden-premise phrases | literal note-text scan plus supplied inventory |
| `R20` | current route synthesis is “unfinished implementation, not a demonstrated substrate obstruction” | narrow classification of the unimplemented Cycle-290 apparatus |
| `R21` | N8 responses proceed “without claiming the whole compiler is finished”; Q pointer is “not actual action” | cited prior residual boundaries |
| `R22` | “no route-independent failure survives”; scoped “no shared obstruction/no axiom pressure” | only the enumerated Cycle-290 routes and controls |

Every ID is now audited at the five resolutions required by the skill.
“Tested” names the actual witness. Every other physics resolution is written
as **unknown / not claimed**; no untested cell is allowed to inherit a negative
conclusion.

| ID | per-element | per-site | per-mode | per-block | lattice-wide |
|---|---|---|---|---|---|
| `R1` | N/A: administrative | N/A: administrative | N/A: administrative | tested: exact two-file status | N/A: administrative |
| `R2` | tested: equal marker blocks of `I_p tensor W` | tested: each inserted onsite action is marker independent | tested: all local diagonal action entries carry no marker selector | tested: exact 4D circuit | unknown / not claimed |
| `R3` | unknown / not claimed | unknown / not claimed | unknown / not claimed | unknown / not claimed | unknown / not claimed |
| `R4` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: runner source and inventory contain supplied apparatus | unknown / not claimed |
| `R5` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: enumerated Cycle-290 routes provide no shared failure | unknown / not claimed |
| `R6` | unknown / not claimed | tested: all translated motif sites remain in the family | tested: transformed endpoint modes remain in the family | tested: 648 family comparisons | unknown / not claimed |
| `R7` | tested: each branch vector has one number eigenvalue | unknown / not claimed | tested: occupation masks sum to six | tested: both arms have total `N=6` | unknown / not claimed |
| `R8` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: `Y=+/-sin(g)` | unknown / not claimed |
| `R9` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested only as an explicit supplied input, not as a negative derivation theorem | unknown / not claimed |
| `R10` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: all route/H/action split deletions | unknown / not claimed |
| `R11` | unknown / not claimed | unknown / not claimed | tested: N=2 pair-count and threshold eigenvalues coincide | tested: equal N=2 closes | unknown / not claimed |
| `R12` | tested: 64 actual eigenvalues reconstruct | tested: actual Walsh block at each cell | tested: six-mode Walsh characters | tested: two actual action blocks | unknown / not claimed |
| `R13` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: Cycle-290 runner supplies rather than synthesizes route/H/read | unknown / not claimed |
| `R14` | tested only for one-particle action identity | unknown / not claimed | tested only for local `N<=1` columns | tested only for retained one-particle mass ratio | unknown / not claimed |
| `R15` | tested: bounded Pauli representatives contain no ordering label | tested: two adjacent local cells | tested: direction family transformed by frames | tested: 35-M2 motif and 648 transforms | unknown / not claimed for a complete lattice compiler |
| `R16` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested only as dependency-ledger scope | unknown / not claimed |
| `R17` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested routes refute the broad candidate on this block | unknown / not claimed |
| `R18` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: literal pairwise dependency table | unknown / not claimed |
| `R19` | N/A: rhetoric scan | N/A: rhetoric scan | N/A: rhetoric scan | tested: exact note scan | N/A: rhetoric scan |
| `R20` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: missing apparatus synthesis is catalogued as an import | unknown / not claimed |
| `R21` | unknown / not claimed | tested only for cited local residuals | tested only for cited six-mode action residuals | tested only for cited same-code blocks | unknown / not claimed |
| `R22` | unknown / not claimed | unknown / not claimed | unknown / not claimed | tested: N1 controls and N2 collapsed conditions | unknown / not claimed |

This resolution table forces the narrow result wording: Cycle 290 establishes a
constructive two-cell comparator and finite motif covariance. Autonomous
apparatus, broader semantic interpretations, arbitrary encodings, and
lattice-wide compiler closure are unknown / not claimed. Therefore every live
route demotes a broad no-go rather than supporting one.

### N6 — partial-closure path scan

1. Keep the present physical `W_g` blocks and replace the abstract route with
   an explicit finite product of the mapped hopping generators.
2. Compile marker preparation/recombination into the same bounded physical
   neighborhood and rerun every split deletion.
3. Generate the branch by an ordinary local collision path so that both arms
   experience the same selected microscopic rule without a marker-controlled
   router.
4. Add a same-code coherent read carrier only after the collision block is
   executable; do not infer stronger semantics from the close probability.
5. Run the resulting autonomous motif under all proper-cubic frames and held
   sizes before considering any foundation-level wording.

Each path is constructive and live. Within the reviewed Cycle-290 evidence,
these paths create no axiom-edit requirement. Unreviewed completion routes are
unknown and receive no foreclosure claim.

### N7 — steelman

The strongest opponent says the current success may still be an apparatus
identity: a supplied controlled redistribution and its exact inverse create
and erase the which-path label, while the selected contact law is inserted at
the favorable point. A homogeneous local collision could, in principle,
generate the same two matter branches and recombine them without any external
marker-controlled route. If that succeeds, it directly closes `K_branch` and
advances the already-collapsed downstream integration objective `K_auto`.

Cycle 290 concedes this fully. Its advance is narrower and exact: once such a
fixed-number bounded branch exists, the ordinary onsite contact law itself
needs no controlled oracle and is distinguishable from Q-only action. The
remaining route synthesis is unfinished implementation, not a demonstrated
substrate obstruction.

The N=2 two-cell branch is also retained as a steelman because it best matches
the intuitive “co-located versus separated” contact path. Its exact failure to
reject Q-only explains, rather than hides, the extra occupancy used by the
primary fixture.

### N8 — cross-cycle echo

| earlier cycle | similar earlier boundary | retired here? | mechanism and whether it could apply further |
|---|---|---:|---|
| Cycle 230 | physical-site compiler remained open | partial only | retained connected physical-M2 mapping retires the two-cell contact/connector part; the same mapping could be extended to explicit route synthesis, while whole-compiler closure stays unknown |
| Cycle 269 | Wilson center blocks a global tensor-gauge reading | no, global boundary remains | Cycle 290 works on one bounded motif and checks Wilson commutators; locality avoids but does not retire the global residual, and larger-route tests could use the same bounded-cone tactic |
| Cycle 278 | Q-only pointer detects support rather than actual action | yes for this comparator | fixed-N pair-count surplus makes Q-only a common phase; analogous equal-Q/different-pair fixtures could apply elsewhere |
| Cycle 285 controlled route | controlled `W_g` was a supplied oracle | yes for this comparator | route matter branches first, then apply ordinary `I_p tensor W_xy`; the same mechanism could apply to other diagonal local actions |
| Cycle 285 direct reference | action calibration used cross-number coherence | yes for this comparator | fixed-total `N=6` branches with pair-count difference one; fixed-charge branch engineering could apply to other conserved sectors |
| Cycle 285 covariance | covariance covered one-cell action and separate reference family | yes for the declared motif | transform both cells plus `A_e` together; the mechanism can test a future compiled route but does not pre-certify it |

Within the enumerated Cycle-290 routes and controls, no route-independent
failure appears. Scoped to that reviewed evidence alone, there is no shared
obstruction and no axiom pressure. Unreviewed encodings, apparatus syntheses,
preparations, homogeneous completions, and lattice-wide compilers remain
unknown; the live routes above make any broader no-go **FAIL** and demote it to
an open constructive campaign.

## 13. Reproduction

```bash
python3 scripts/unconditional_two_cell_contact_interferometer_cycle290_2026_07_17.py
```

The runner exits nonzero on any failed action, replacement, route-deletion,
support, leakage, mass, covariance, lawful-domain, or note-contract check.
