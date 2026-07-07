# Matter Realization: Qubit-Level Cross-Site Bilinear From K1 Structure

**Date:** 2026-07-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set,
predict, or apply an audit outcome.
**Primary runner:** `scripts/matter_realization_qubit_bilinear_from_k1_2026_07_06.py`
**Cache:**
`logs/runner-cache/matter_realization_qubit_bilinear_from_k1_2026_07_06.txt`
is supervisor-generated. This drafting worker does not write that cache.

## Summary
This draft derives the qubit-level cross-site coefficient bilinear carried by the
K1 representative on the licensed nearest-neighbor bilinear surface. It does not
derive color, a `C^3` carrier, or the color block-05 supplied matter bilinear.

Exact content: K1 on the licensed surface, conditional on the 2026-07-02 K1
selection cluster later auditing clean, gives rank-2 self-adjoint-unitary
nearest-neighbor coefficients on `C^2`. The relation to the color block-05
premise is STRUCTURAL ANALOGY ONLY (see T2): SUPPLIED-BILINEAR is a
state-level `C^3` object and is not decomposed, refined, or advanced here;
both the `C^2`-to-`C^3` carrier lift and a structure-to-state bridge are
named missing links.

## The texts in play
The current axiom memo gives the Admissibility sentence:

> For each site, the available possibilities are determined by, and vary with,
> the nearest-neighbor conditions.

The 2026-07-02 K1 selection note is UNAUDITED target/context. It names:

```text
K0: phi=+1, representative t == 1 (scalar tight-binding; extensive zero surface).
K1: phi=-1, representative eta0: eta0_1 = 1,
eta0_2 = (-1)^{x1}, eta0_3 = (-1)^{x1+x2}
(Kawamoto-Smit class; 8 isolated Dirac zeros; = absorbed naive Dirac).
```

It states the availability discriminator:

> K0 realizes only neighbor-constant maps, with dimensions `[1, 1, 1]`.

> K1 carries the direction-tagged varying family, with dimensions `[2, 2, 2]`.

And the selection statement:

> Hence the clarified Admissibility clause selects the flux(-1) class on the
> licensed surface.

Those sentences are recomputed here; they are not consumed as audited results.
The discriminator note, also UNAUDITED, defines the D1-D4 package as:

> four computable representative-level discriminators: D1, internal-factor load
> and grade-1 Clifford capacity; D2, first-order Dirac-square dispersion versus
> scalar perfect-square dispersion; D3, isolated zero points versus an extensive
> zero surface; and D4, nonvacuous per-direction qubit-factor admissibility
> algebras versus the scalar vacuous algebra.

The landed color block-05 premise text is:

```text
SUPPLIED-BILINEAR:
a full-rank cross-site bilinear map M(x,y): C_x^3 -> C_y^3 between the
supplied carriers is itself supplied data. No fermion fields, CAR algebra,
occupancy structure, local field operators, or physical matter ontology are
derived or imported; "matter bilinear" names the supplied map's intended
role, not a derivation.
```

## T1 - Exact K1 qubit-level coefficient bilinear
**T1 (exact K1-branch-conditional algebra; every sentence here is conditional on the UNAUDITED July-2 K1 selection cluster reaching audit grade -- if K0 survives audit instead, T1 collapses to branch-conditional bookkeeping with no selection context):** On the licensed nearest-neighbor bilinear
surface, take the K1 eta phases above, the absorbing-frame qubit module
`T(x) = sigma_1^x1 sigma_2^x2 sigma_3^x3`, and the oriented-edge coefficient
`C_mu(x) = eta_mu(x) T(x + e_mu) T(x)^dagger`.

In parity order `000,001,010,011,100,101,110,111`, the exact phases are:

```text
eta_1 = ++++++++
eta_2 = ++++----
eta_3 = ++----++
```

Substitution gives, at every parity site,

```text
C_1(x) = sigma_1
C_2(x) = sigma_2
C_3(x) = sigma_3
```

Thus every licensed K1 edge coefficient is self-adjoint, unitary, rank 2 on
`C^2`, direction-tagged, and pairwise anticommuting. The projectors
`P_mu^+ = (I + C_mu) / 2` and `P_mu^- = (I - C_mu) / 2` are rank-one and
orthogonal, so each direction generates `span_C{I, C_mu}`: `[2, 2, 2]`.

The K0 contrast is scalar. The `phi=+1`, `t == 1` representative has direction
coefficients proportional to `I`; each generated algebra is only `C * I`, with
dimensions `[1, 1, 1]`. Inflated to `C^2`, K0's scalar coefficient is also rank
2, so rank alone is not the discriminator. The discriminator is the non-scalar
direction-tagged qubit-factor algebra.

The runner also recomputes D1-D3 controls: K1 has scalar joint commutant and no
fourth anticommuting element on `C^2`; `K1(p)^2 = sum_mu sin^2(p_mu) I`; K0 has
a rational codimension-1 zero-family witness while K1 has 8 corner zeros.

## T2 -- Structural analogy to the color block-05 premise (NOT a decomposition)

**T2 (bookkeeping at analogy strength only):** the landed color block-05
premise SUPPLIED-BILINEAR concerns a supplied, STATE-level, full-rank map
`M(x,y): C_x^3 -> C_y^3` between supplied color carriers. What T1 supplies
is a STRUCTURE-level, full-rank, direction-tagged cross-site coefficient
operator on the qubit modules, conditional on the K1 branch. These are
structurally analogous and NOT the same object, and this note does NOT
decompose, refine, or advance SUPPLIED-BILINEAR. Two independent missing
links, named exactly:

- the carrier lift `C^2 -> C^3` (this is SUPPLIED-C3's own open realization
  bridge, untouched here); and
- a structure-to-state bridge: no theorem here (or anywhere landed) connects
  full-rankness of the kinetic COEFFICIENT operator to full-rankness of the
  state-dependent matter bilinear `M(x,y)`; block-05's full-rank
  precondition is a statement about states/occupancy and remains exactly as
  open as block-05 left it.

If both links were ever supplied, the K1 coefficient structure would be a
natural candidate source for the transport's direction tagging -- recorded
as a program pointer, non-claim.

## T3 - Residual ledger (not a T-claim)
- R-k1-audit: all content here is conditional on the 2026-07-02 K1 selection
  cluster auditing clean. If K0 survives audit instead, T1's selection context
  collapses to a K1-branch-conditional statement only.
- R-carrier-lift: SUPPLIED-C3 is unchanged; this note supplies no
  `C^2`-to-`C^3` carrier bridge.
- R-licensed-surface: the parent kinetic-class surface's declared bounds remain
  in force.
- R-rank-vs-occupancy: full-rank kinetic coefficients do NOT imply full-rank
  state bilinears; the occupancy question survives.

## Honest boundary
This note does not audit K1, apply an audit verdict, edit `docs/audit/`, add an
axiom, add a primitive, add Tier-A content, decide a landing, derive a `C^3`
carrier, discharge SUPPLIED-C3, discharge SUPPLIED-BILINEAR, derive state-level
full rank, select occupancy, or assert gauge dynamics, action, probability,
path measure, rate, generator, or record-production rules.

## Citation contract
Citation is audit-gated. This draft has no premise weight until independent
audit ratification. Within that gate, downstream rows may cite T1's exact
algebra, conditional as stated:
`C_mu(x) = eta_mu(x) T(x + e_mu) T(x)^dagger = sigma_mu`, so `C_mu` is a
self-adjoint unitary of rank 2 on `C^2`. They may cite T2 only as the stated structural
analogy with its two named missing links (carrier lift; structure-to-state
bridge); never as a decomposition or refinement of SUPPLIED-BILINEAR, and
never as progress on block-05's state-level full-rank precondition.

They may NOT cite this note for: SUPPLIED-BILINEAR discharged; K1 as audited;
state-level full-rankness; color-level full-rankness; carrier lift supplied;
SUPPLIED-C3 discharged; occupancy selection; gauge dynamics; action;
probability; generator; rate; Tier-A content; a primitive; or audit upgrade.

## Dependencies
- docs/MINIMAL_AXIOMS_2026-06-29.md, current axiom memo: quoted Admissibility and premise-discipline
  sentences; no downstream physical structure imported.
- docs/REALIZED_KINETIC_BRANCH_SELECTED_BY_ADMISSIBILITY_VARIATION_NARROW_THEOREM_NOTE_2026-07-02.md, UNAUDITED K1 selection note: representative, discriminator, and
  selection quotes only; algebra recomputed here.
- docs/REALIZED_KINETIC_BRANCH_DISCRIMINATOR_DICHOTOMY_NARROW_THEOREM_NOTE_2026-07-02.md, UNAUDITED discriminator note: D1-D4 definitions quoted; consumed
  computations recomputed here.
- docs/COLOR_COMPOSITION_RULE_MATTER_BILINEAR_POLAR_TRANSPORT_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-07-06.md, landed block-05 note: exact SUPPLIED-BILINEAR premise quoted; no
  discharge imported.

## Runner verification map
The runner uses Python 3 and `fractions.Fraction` exact arithmetic only. It
recomputes eta phases for all directions/parities, K1 per-edge matrices,
self-adjointness, unitarity, rank, K0 contrast, `[1, 1, 1]` and `[2, 2, 2]`,
D1-D3 controls, quote audits from files 1-4, and an AST self-scan. It prints a
declaration line with verdicts and the not-consumed list, writes no cache, and
currently reports `TOTAL PASS=9 FAIL=0`.

## Source-note boundary
Hypothesis set: current framework axioms as context; the licensed surface; the
K1 representative if the UNAUDITED selection cluster later audits clean; the
one-site `C^2` qubit module; and exact finite-dimensional matrix algebra. No
audited K1 status, parent-row regrade, carrier bridge, state-level full-rank
theorem, occupancy theorem, dynamics, primitive, Tier-A admission, or audit
verdict is imported.

## Changelog
- **2026-07-06.** Initial draft note and exact Fraction runner. The runner
  reports `TOTAL PASS=9 FAIL=0`.
