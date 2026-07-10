# Adjacent Cell-Energy Obstruction For A Commuting-Auxiliary Constraint Ansatz

**Date:** 2026-07-08
**Type:** no_go
**Claim scope:** For one declared two-species cell Hamiltonian density, one
explicit coupling point, and auxiliary variables that commute both with one
another and with the matter algebra, the adjacent constraint pair
`G_n=eta_n-eta_{n-1}-h_n` is not abelian because its commutator equals the
computed nonzero operator `[h_n,h_{n+1}]`.

**Primary runner:**
[`scripts/energy_gauss_constraint_obstruction_2026_07_08.py`](../scripts/energy_gauss_constraint_obstruction_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/energy_gauss_constraint_obstruction_2026_07_08.txt`](../logs/runner-cache/energy_gauss_constraint_obstruction_2026_07_08.txt)

## Defined Surface

The local matter algebra and cell-density construction use the normal-ordered
operator machinery documented in the
[`FINITE-BASIS COMPUTATIONAL CONSERVED-DENSITY NOTE`](NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md).
The runner fixes

```text
(t_a,t_b,m_a,m_b,U,V_a,V_b,W_ab)
  = (0.8,1.1,0.4,0.6,0.9,0.5,1.2,0.7).
```

Introduce auxiliary operators `eta_n` with the explicit premises

```text
[eta_n,eta_m]=0,
[eta_n,h_m]=0,
G_n=eta_n-eta_{n-1}-h_n.
```

Then direct expansion gives

```text
[G_n,G_m]=[h_n,h_m].
```

## Computed Obstruction

At the displayed point, the paired runner finds `[h_0,h_1]` nonzero in the
normal-ordered coefficient representation and in an independent dense
eight-site representation. It also checks `[h_0,h_2]=0` for the displayed
cell apportioning and verifies the dense/symbolic adjacent commutator agreement
at the printed tolerance. Therefore this particular commuting-auxiliary
constraint pair is not abelian.

That is the entire negative claim. The calculation does not address a
different local-energy apportioning, noncommuting or matter-dependent
auxiliaries, additional constraints, a nonabelian closure, another coupling
point, a continuum limit, or a general energy-gauging construction.

## No-Go Discipline Gate

### N1 — Alternative route enumeration

| route | marker | attack | result at this scope |
|---|---|---|---|
| Cancel with commuting auxiliary terms | ATTEMPTED | Expand all `eta` contributions in `[G_0,G_1]`. | They vanish under the two displayed commutation premises, leaving the nonzero matter commutator checked by the [runner](../scripts/energy_gauss_constraint_obstruction_2026_07_08.py). |
| Add central constants to `G_n` | ATTEMPTED | Shift either constraint by a multiple of the identity. | Central terms commute and do not change the adjacent commutator. |
| Attribute the result to an adjacency-index artifact | ATTEMPTED | Compare the adjacent result with `[h_0,h_2]` using the same operator engine. | The separated commutator vanishes, isolating the tested residual to the adjacent pair. |
| Attribute the residual to the symbolic normal-ordering representation | ATTEMPTED | Reconstruct `h_0`, `h_1`, and their commutator as dense matrices on eight sites. | The dense matrix commutator agrees with the normal-ordered result to `6.7e-16`. |
| Attribute nonzero status to a small numerical coefficient | ATTEMPTED | Evaluate both the coefficient-space norm and the dense Hilbert--Schmidt norm. | The printed norms are `2.01528224` and `2.82696411e2`, respectively, both far above the declared `1e-12` threshold. |
| Attribute the result to a commutator-engine false positive | ATTEMPTED | Apply the same engine to all pairs of six displayed on-site charge operators. | The charge-control family is abelian, while the adjacent energy-density control is nonzero. |

The gate therefore supports only the stated conditional obstruction. Every
broader universal reading has been removed.

### N2 — Scope-condition independence

The ansatz `G_n=eta_n-eta_{n-1}-h_n` is the definition of the route tested
here, not an additional wall. Its four load-bearing scope conditions are:

- **W1:** the displayed cell-density definition and apportioning are fixed;
- **W2:** the displayed coupling point is fixed;
- **W3:** the auxiliary variables obey `[eta_n,eta_m]=0`;
- **W4:** the auxiliary variables obey `[eta_n,h_m]=0`.

The complete pairwise check is:

| pair | closing first closes second? | closing second closes first? | independent? | reason |
|---|---:|---:|---:|---|
| W1 / W2 | no | no | yes | A density apportioning can be held fixed while its coefficients vary, and a coupling point does not determine how the total Hamiltonian is apportioned into cells. |
| W1 / W3 | no | no | yes | The matter-density definition does not determine the auxiliary--auxiliary algebra, and an abelian auxiliary algebra does not select a matter-density split. |
| W1 / W4 | no | no | yes | Fixing `h_n` does not force every `eta_n` to commute with it, while imposing auxiliary--matter commutation does not select the displayed `h_n`. |
| W2 / W3 | no | no | yes | Numerical matter couplings do not determine auxiliary--auxiliary commutators, and W3 leaves the matter couplings free. |
| W2 / W4 | no | no | yes | The coupling point alone does not impose auxiliary--matter commutation, and W4 can hold at other coupling points. |
| W3 / W4 | no | no | yes | Mutual commutation of the `eta_n` does not imply commutation with the matter algebra, and commuting with all `h_m` does not require the `eta_n` to commute with one another. |

No condition follows from another, and none is hidden or counted as a
universal obstruction.

### N3 — Hidden-premise scan

The phrases targeted by the discipline check were scanned. The only
load-bearing premises are the displayed cell density, coupling point, and two
auxiliary commutators. No framework axiom, “standard” gauging rule,
background, canonical-gravity analogy, or unlinked registration claim is used.

### N4 — Residual matching

No prior no-go, campaign synthesis, or audit verdict is cited as evidence. The
residual is only the nonzero adjacent commutator of the displayed pair, so
there is no cross-note residual to mismatch.

### N5 — Rhetoric and resolution audit

The calculation checks a fixed adjacent cell pair and one separated-pair
control. It does not test all per-site apportionings, Fourier modes, blocks,
couplings, auxiliary algebras, or the lattice-wide constraint algebra. The
claim is phrased only at the tested adjacent-pair resolution.

### N6 — Partial-closure paths

The live escapes are physical/algebraic changes of ansatz: a different density
apportioning; noncommuting or matter-dependent auxiliaries; an enlarged or
nonabelian constraint algebra; or a different Hamiltonian coupling point.
These routes were not tested and remain open. No new axiom or missing
registered primitive is asserted, and no labeling convention is misclassified
as physics.

### N7 — Steelman

A hostile reviewer should allow the auxiliary sector to carry its own local
algebra and matter-dependent commutators. Those extra terms could cancel or
absorb `[h_0,h_1]`; alternatively, a different split of `H=sum_n h_n` could
alter the adjacent bracket. That steelman defeats the original universal
energy-Gauss language. It does not defeat the much narrower algebraic fact
proved here, because that fact explicitly fixes the density and requires the
auxiliaries to commute.

### N8 — Cross-cycle echo

A repository search for prior energy-constraint, commuting-auxiliary, and
adjacent energy-density claims found no independent live source note that
closes the open routes listed in N6. The negative is therefore restricted to
the exact operator and resolution actually tested. No previously successful
convention or primitive route was found and ignored.

**Gate result:** PASS for the displayed fixed-density, fixed-point,
commuting-auxiliary obstruction only. The gate does not pass any universal
energy-Gauss or interaction claim.

## Boundaries

- The normal-ordered coefficients are floating-point values at one declared
  parameter point; the dense representation is an independent numerical
  cross-check.
- The algebraic identity `[G_n,G_m]=[h_n,h_m]` is conditional on both auxiliary
  commutation premises.
- No gravitational dynamics, constraint algebra, or continuum theory is
  derived.
- Audit classification and verdict remain the responsibility of the
  independent audit lane.

## Dependencies

- [`NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md`](NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md)
  supplies the operator representation reused by the paired runner. Its
  broader finite-basis classification is not used as evidence for this
  obstruction.
