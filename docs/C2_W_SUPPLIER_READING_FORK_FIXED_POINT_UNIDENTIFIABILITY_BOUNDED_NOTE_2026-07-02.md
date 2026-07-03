# C2 W-Supplier Reading Fork and Fixed-Point Unidentifiability

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope boundary:** Bounded reading-fork and fixed-point unidentifiability on the named two-cell rational-content class only; neither reading is adjudicated, no wall is closed, CTX-match remains open, no dictionary or value is selected, and no axiom, primitive, registry, audit, or publication surface is edited.
**Audit boundary:** independent audit lane only. This source note writes no audit verdict, sets no audit status, and forecasts no audit outcome.
**Primary runner:** [`scripts/frontier_c2_w_supplier_reading_fork_2026_07_02.py`](../scripts/frontier_c2_w_supplier_reading_fork_2026_07_02.py)
**Runner output:** [`outputs/frontier_c2_w_supplier_reading_fork_2026_07_02.txt`](../outputs/frontier_c2_w_supplier_reading_fork_2026_07_02.txt)

## FIREWALL

No wall closed. This note does not adjudicate either reading of the
no-privilege relabeling closure. The fork is recorded as an unmade
science-level decision under policy section 4. CTX-match remains open.
D-totality and R* are untouched. Nothing here edits axioms, primitives,
registries, or audit data. The block06, block11, block02, and block15 campaign
citations are review-pending context only, and the independent audit lane owns
all status.

## Purpose

This note packages one bounded result on the supplied two-cell rational-content class used by review-pending PR #4826 block11: current Record text discharges content-determination on that class; policy section 6 naturality turns the remaining one-parameter freedom into a reading fork; the agreement-conditioned fixed point makes the freedom unidentifiable on the equipartition diagonal; and the `kappa_EW` connection is only conditional on CTX-match.

## Supplied Surface

The current axiom and policy premises checked by the runner are:

> No possibility is privileged.

> Only records are readable. A readout value is determined by record content alone. For any finite collection of pairwise-disjoint records, scalar readout `I` is additive, with `I(empty)=0`.

> A state is a configuration of records.

> A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer.

Policy section 6 is used only as a reading note: privileging is judged extensionally by the selected set of states, with the naturality test that selected sets be closed under lattice motions and possibility relabelings. The same section records the standing promotion rule. It also states that the added sentences name no operator, basis, weighting, selector, kinetic class, or value, so nothing below says the axiom text names `w`; the conclusions are theorem content on the supplied class. [checks 1-2]

The three items still supplied in T1 are:

- the frame C1, here the two cells;
- the refinement-lattice combinatorics, namely reachability by disjoint union and k-fold equal splitting;
- the rational-content restriction.

## T1 - Class Discharge

On the supplied two-cell frame, review-pending PR #4826 block11 defines `C2_Q_content` by:

1. `I(empty)=0`;
2. finite additivity over disjoint union;
3. content determination by the rational pair `(x_A, x_B)`.

Those three conditions now read directly as current Record text on this class: empty value and finite additivity are the scalar readout sentence, while content determination is the 2026-07-02 Record sentence saying that a readout value is determined by record content alone.

For rational contents, k-fold equal refinement gives pieces `(1/k,0)` and `(0,1/k)`. Disjoint union builds the sampled rational pairs exactly. Additivity plus content determination forces each refined generator piece to carry the corresponding fractional readout, so every sampled record has

```text
I(x_A, x_B) = u x_A + v x_B,
u = I(1,0), v = I(0,1).
```

Thus the readout space on the supplied class is exactly the block11 normal form `{u x_A + v x_B}`. Block11's identity-dependent same-content counterexample family is now excluded by Record text rather than by class fiat.

Honesty boundary: this upgrades block11's conditionality only on the named class. It does not derive the frame C1, the refinement lattice, or the rational-content restriction. [checks 3-7]

## T2 - Reading Fork on `u = v`

There are two natural readings of the policy section 6 phrase "possibility relabelings" on this supplied two-cell surface.

**READING-X: exchange-closed.** Possibility relabelings include the set-level exchange

```text
sigma(x_A, x_B) = (x_B, x_A)
```

of the two cell generators. Then a readout with `u != v` privileges extensionally: the level set through `(1,0)` is not closed under `sigma`, because `I(1,0)=u` while `I(0,1)=v`. Under this reading, closure on the generators forces `u=v`, so modulo overall scale the surviving form is `x_A + x_B`; equivalently `w=1` on this class.

**READING-P: presentation-closed.** Possibility relabelings mean relabelings that respect the supplied algebraic presentation. On the canonical `C_3` context, the circulant span basis `{I, U, U^2}` has multiplication-table-preserving relabelings exactly identity and `U <-> U^2`; both fix the unit `I`, and none maps `I` to `U` or `U^2`.

The induced action on content pairs is trivial. In the canonical context, `(x_A, x_B)=(a^2, 2|b|^2)`, and `U <-> U^2` sends `b` to `conj(b)` while leaving `a^2` and `2|b|^2` unchanged. Hence every `(u,v)` readout is natural under READING-P. The `(u,v)=(2,1)` witness and the block02 `w=2` witness from review-pending PR #4817 block02 both survive these checks.

Fork statement: under READING-X, `w=1` is forced on this class; under READING-P, `w` is not forced. The readings' adjudication is an owner decision, not a new axiom and not a result of this note. Per policy section 6's standing promotion rule, an adjudicated reading may later be proposed for promotion into axiom text by owner approval. [checks 8-15]

## T3 - Fixed-Point Unidentifiability

On the equipartition diagonal `x_A=x_B=x`,

```text
I(x,x) = (u+v) x.
```

Therefore any two pairs `(u,v)` and `(u',v')` with the same sum agree on every diagonal state, and they can still separate off the diagonal. More strongly, for any nonzero diagonal contents `x_1` and `x_2`,

```text
I(x_1,x_1) / I(x_2,x_2) = x_1 / x_2,
```

independent of `(u,v)`. All scale-invariant readouts are therefore `w`-independent at equipartition-selected states.

The agreement-conditioned double-registration flow from the occupancy note is recomputed inline in outcome-ratio coordinates:

```text
x' = x^2.
```

Its fixed set is `{0,1}`. Under `x=2r`, the coordinate map is `r -> 2r^2` with fixed set `{0,1/2}`; under `x=r`, it is `r -> r^2` with fixed set `{0,1}`. Both dictionaries select the same invariant outcome-space fixed point `x*=1`.

The hostile value cited from review-pending PR #4821 block06, `17/2 - 6 sqrt(2)`, lies in neither fixed set. The runner uses `(239/169)^2 < 2 < (17/12)^2`, so the value lies strictly between `0` and `5/338`, hence not in `{0,1/2,1}`.

Corollary: at flow-selected states the one-parameter `w` freedom degenerates to overall scale. Firewall: this does not fix `w`, does not select a dictionary, and does not re-derive any generation-sector value. [checks 16-20]

## T4 - `kappa_EW` Correspondence, Conditional on CTX-match

The parent `kappa_EW` wall states that the EW color readout uses

```text
Pi_phys = C + kappa_EW S,
```

and that the central-sector partition gives the cardinality count `8/9` without picking the inter-sector weight. That wall is not closed here.

If the EW color readout context is a two-cell instance of the same supplier
family, i.e. if CTX-match holds, then the class calculation says:

- under READING-X, `kappa_EW=1` on this class, and the equal per-component adjoint fraction is `8u/(8u+1u)=8/9`;
- under READING-P, `kappa_EW` remains one free parameter;
- at flow-selected equal-cell-content states, every readout sees `kappa_EW` only through the common scale `u + kappa_EW u`, so readout ratios are `kappa_EW`-independent there.

This generalizes the parent note's common-`K_EW` cancellation remark into a class-level diagonal statement, but only inside the CTX-match conditional. The parent wall is not closed. [checks 21-23]

## T5 - Ladder and Governance Map

Review-pending PR #4830 block15 records the carrier/kappa ladder as

```text
{R*, D-totality, w-supplier, CTX-match}.
```

On this block's class, the ladder updates to

```text
{R*, D-totality, READ(no-privilege relabeling closure), CTX-match}.
```

The `w`-supplier rung is retired as an independent missing number. What remains in that slot is a binary reading adjudication: READING-X fixes `w=1` on the class, while READING-P leaves `w` free on the class.

No new axiom and no new primitive is required to fix `w` under READING-X. The mechanism to move an adjudicated reading into axiom text already exists: policy section 6's standing promotion rule. This note only flags the governance shape and does not decide the reading.

Hand-off without claiming: R* is also flagged in review-pending context as a reading-level adjudication. Whether READ and R* are one adjudication surface is an owner/audit question, not a result here. [checks 24-25]

## Consequence

The enabling change is narrow: on the block11 class, the missing supplier is not an arbitrary number once a no-privilege relabeling closure is chosen. The owner-facing decision is binary:

- include cell-exchanging possibility relabelings, and the class has `w=1`;
- restrict to presentation-preserving relabelings, and the class leaves `w` free.

Flow-selected equipartition then explains why diagonal ratio readouts cannot identify the free parameter even when it remains open. This supports a cleaner handoff: separate the reading adjudication from CTX-match, D-totality, and R*.

## Does NOT

- Does not fix `w` unconditionally.
- Does not adjudicate READING-X versus READING-P.
- No wall closed: does not close the `kappa_EW` wall or any parent wall.
- Does not claim CTX-match.
- Does not select the component dictionary or the slot dictionary.
- Does not re-derive `Q` or any generation-sector value.
- Does not modify axiom text, primitives, registries, or audit data.
- Does not merge READ with R*.
- Does not treat review-pending sibling citations as landed authority.

## Dependencies And Context

Load-bearing dependency and governance surfaces:

- [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- [`docs/EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md`](EW_KAPPA_WEIGHTING_NOT_AXIOM_DERIVABLE_NO_GO_NOTE_2026-06-09.md)

Context surfaces only, not dependency links: `OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md` names the source of the flow motif, but the runner recomputes the fixed-set algebra inline; `C3_GENERATION_READOUT_CONTEXT_CANONICAL_DEFINITION_NOTE_2026-07-02.md` names the context label, but the runner recomputes the C3 table-preserving maps inline.

Review-pending campaign context cited without reading their branches:

- review-pending PR #4826 block11: C2 normal form and counterexample family;
- review-pending PR #4817 block02: supplied readout context and `w=2` witness;
- review-pending PR #4830 block15: carrier/kappa ladder and CTX-match handoff;
- review-pending PR #4821 block06: equal-channel-energy context and hostile
  fixed-set check.

## No-Promotion Statement

This note does not promote, demote, or set the audit status of any dependency.
The independent audit lane is the only status authority.
