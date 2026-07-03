# Koide MRU Unreduced Weight-Class Obstruction Boundary

**Date:** 2026-04-19 (source-boundary correction 2026-06-12; unreduced-scope correction 2026-06-15)
**Lane:** Charged-lepton Koide / MRU
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required.
**Status authority:** independent audit lane. This source note does not set,
predict, promote, or demote any audit outcome and does not edit audit-owned
registry, ledger, queue, or publication-status surfaces.
**Primary runner:** `scripts/frontier_koide_mru_weight_class_obstruction_theorem.py`
**Runner cache:** `logs/runner-cache/frontier_koide_mru_weight_class_obstruction_theorem.txt`

**Claim scope:** unreduced carrier obstruction only.

**Source boundary:** the exact unreduced `3 x 3` determinant carrier counts
weights `(1,2)` and therefore cannot force MRU by itself. This is the theorem
claimed by this source. The reduced two-slot calculation is kept only as
non-load-bearing future-route context: **if** an independent theorem supplies
the scalar-lane `SO(2)` quotient, then the reduced carrier has equal weights
and lands at `kappa = 2`. That context is not part of the theorem claim. This
note does not derive that physical quotient bridge.

**No-promotion statement:** the independent audit lane owns audit and
effective status. This source does not promote the row and does not assert
that the scalar charged-lepton lane physically lives on the `SO(2)` quotient.
It does **not** derive the physical quotient bridge.
The companion
`KOIDE_MRU_DEMOTION_NOTE_2026-04-20` already records that this MRU route is
supplementary / alternative-framing support for operator-side `kappa = 2`;
the operator-side gate is carried elsewhere without an `SO(2)` quotient
postulate.

---

## 0. Executive summary

On the `d = 3` cyclic carrier,

```text
E_+    = r_0^2 / 3   = 3 a^2,
E_perp = (r_1^2 + r_2^2) / 6 = 6 |b|^2.
```

For the weighted block-log-volume family

```text
S_{mu,nu} = mu log(E_+) + nu log(E_perp)
```

at fixed `E_tot = E_+ + E_perp`, every interior stationary leaf is

```text
kappa := a^2 / |b|^2 = 2 mu / nu.
```

So:

- MRU is the equal-weight leaf `(mu, nu) = (1,1)`;
- the unreduced determinant carrier

  ```text
  det(alpha P_+ + beta P_perp) = alpha beta^2
  ```

  carries weights `(1,2)` and lands at `kappa = 1`.

That obstruction remains exact. It is the whole bounded theorem asserted here:
on the unreduced `3 x 3` isotypic-scalar determinant carrier, the
log-volume/determinant law selects `kappa = 1`, not MRU.

The rest of this note records a non-load-bearing future route, not a theorem
claim. A later positive route would have to supply the carrier reduction the
old theorem said was missing:

```text
(r_0, r_1, r_2)  ->  (rho_+, rho_perp)
```

with

```text
rho_+^2    = E_+,
rho_perp^2 = E_perp,
```

if the scalar lane is independently shown to quotient the internal `SO(2)`
frame of the real doublet. On that supplied reduced carrier,

```text
det diag(rho_+, rho_perp) = rho_+ rho_perp,
```

so the same log-volume law is equal-weight automatically and lands at MRU.
That reduced-carrier paragraph is conditional context only; the unreduced
obstruction theorem does not consume it.
The missing science is the physical quotient theorem itself, equivalently the
decoupling of the `cos(3 arg b)` channel on the charged-lepton scalar lane.

---

## 1. Setup

On the upstream `hw=1` cyclic compression,

```text
H = a I + b C + b^bar C^2,
```

with canonical real cyclic basis

```text
B_0 = I,
B_1 = C + C^2,
B_2 = i (C - C^2).
```

Writing

```text
H = (r_0/3) B_0 + (r_1/6) B_1 + (r_2/6) B_2,
```

the real-trace norms give

```text
||B_0||^2 = 3,
||B_1||^2 = ||B_2||^2 = 6,
```

and therefore

```text
E_+    = r_0^2 / 3 = 3 a^2,
E_perp = (r_1^2 + r_2^2) / 6 = 6 |b|^2.
```

Hence

```text
E_+ = E_perp
<=> a^2 = 2 |b|^2
<=> kappa = 2.
```

---

## 2. Weighted block-log-volume classification

Define

```text
S_{mu,nu}(H) := mu log(E_+) + nu log(E_perp),
```

with `mu, nu > 0`, under fixed total block power

```text
E_+ + E_perp = E_tot.
```

The Lagrange equations give the unique interior stationary point

```text
E_+^*    = mu / (mu + nu) * E_tot,
E_perp^* = nu / (mu + nu) * E_tot.
```

So

```text
E_+^* / E_perp^* = mu / nu,
```

and therefore

```text
kappa = 2 mu / nu.
```

This theorem is exact and unchanged.

---

## 3. The unreduced determinant obstruction

Let `P_+` and `P_perp` be the `C_3` singlet and doublet projectors on the
unreduced `3 x 3` carrier, with ranks `1` and `2`.

Any positive operator that is scalar on these two isotypic blocks has the form

```text
D = alpha P_+ + beta P_perp.
```

Because the non-trivial block has multiplicity `2`,

```text
det(D) = alpha beta^2,
log|det D| = log alpha + 2 log beta.
```

So the unreduced determinant law carries weight pair `(1,2)` and therefore
selects

```text
kappa = 2 * 1 / 2 = 1.
```

That is the exact obstruction:

> no log-volume law applied on the unreduced `3 x 3` isotypic-scalar carrier
> can force MRU.

---

## 4. Non-load-bearing context: supplied SO(2) quotient route

The missing object identified above was:

```text
an independently audited 1:1 real-isotype measure, or an equivalent canonical reduction to a
two-slot (+, perp) carrier before applying the log-volume / extremal law.
```

This source does not derive that object. Sections 4 and 5 record only the
exact algebra that would become available after an independently audited
bridge supplies it. They are not part of the theorem claim and are not used
to prove the unreduced obstruction.

The non-trivial real doublet

```text
V_perp = span_R{B_1, B_2}
```

has an internal orthonormal frame freedom

```text
(B_1, B_2) -> (B_1', B_2') = (B_1, B_2) R(theta),
```

under which

```text
(r_1, r_2) -> R(theta) (r_1, r_2)
```

but

```text
r_1^2 + r_2^2
```

is invariant. So an `SO(2)`-quotient scalar lane would not retain the ordered
Cartesian pair inside the doublet plane. It would retain only the doublet
radius.

Therefore the conditional scalar reduction is

```text
(r_0, r_1, r_2)  ->  (rho_+, rho_perp),
```

with

```text
rho_+    = |r_0| / sqrt(3),
rho_perp = sqrt(r_1^2 + r_2^2) / sqrt(6).
```

Equivalently,

```text
rho_+^2    = E_+,
rho_perp^2 = E_perp.
```

This is the two-slot real-isotype carrier the earlier theorem said would be
sufficient. The carrier is not derived here as the physical charged-lepton
lane, and this branch does not ask audit to treat it as a load-bearing
premise of the bounded theorem.

---

## 5. Non-load-bearing context: reduced-carrier resolution

Apply the same log-volume / extremal law on the reduced carrier

```text
D_red = diag(rho_+, rho_perp).
```

Then

```text
det(D_red) = rho_+ rho_perp,
log|det D_red| = log rho_+ + log rho_perp.
```

At fixed reduced total power

```text
rho_+^2 + rho_perp^2 = E_tot,
```

the unique positive stationary point is

```text
rho_+^2 = rho_perp^2 = E_tot / 2.
```

So

```text
E_+ = E_perp
<=> a^2 = 2 |b|^2
<=> kappa = 2.
```

In other words:

> the obstruction remains exact on the unreduced carrier; it would no longer
> block the route after an independent bridge supplies the reduced carrier.

This is a future-route sanity check only. The theorem proposed by this source
is still the unreduced obstruction of Section 3.

---

## 6. Scientific consequence

The theorem should now be read as one closed negative layer plus one explicit
future-route context layer:

1. **negative layer:** unreduced determinant multiplicities alone do not force
   MRU. This is the theorem claim;
2. **context layer:** if the scalar charged-lepton lane is independently
   shown to live on the real-isotype quotient, then there are only two slots
   and the log-volume law is exactly the MRU leaf. This is not part of the
   theorem claim.

So the weight-class obstruction row should no longer be read as a conditional
positive MRU derivation. It is a bounded unreduced obstruction: derive the
quotient/`cos(3 arg b)` decoupling bridge in a separate upstream theorem, or
do not use this row as a positive MRU carrier.

---

## 7. Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_koide_mru_weight_class_obstruction_theorem.py
```

The runner now certifies:

1. the obstruction on the unreduced `3 x 3` carrier, which is the theorem
   claim, and
2. context-only checks of the real-isotype quotient algebra that would become
   relevant only after a separate physical quotient bridge is supplied.

## 8. Source-boundary perimeter

The internal algebra of this note (Sections 1–6) is intentionally separated
from the physical carrier-identification step:

| Internal algebra step | Source role |
|---|---|
| Real-trace pairing on the cyclic basis `(B_0, B_1, B_2)` (Section 1) | direct algebra |
| `E_+ = r_0^2/3 = 3 a^2`, `E_perp = (r_1^2 + r_2^2)/6 = 6 |b|^2` (Section 1) | direct algebra |
| Weighted family `S_{mu,nu} = mu log E_+ + nu log E_perp` has unique stationary leaf `kappa = 2 mu / nu` (Section 2) | direct algebra |
| `rank(P_+) = 1`, `rank(P_perp) = 2`, and `det(alpha P_+ + beta P_perp) = alpha beta^2` (Section 3) | unreduced obstruction |
| Unreduced weights `(1, 2)` land at `kappa = 1` (Section 3) | unreduced obstruction |
| `r_1^2 + r_2^2` is `SO(2)`-orbit invariant on `V_perp = span_R{B_1, B_2}` (Section 4) | non-load-bearing future-route context |
| Reduced determinant `det diag(rho_+, rho_perp) = rho_+ rho_perp` and equal-weight extremum at `rho_+^2 = rho_perp^2 = E_tot/2` (Section 5) | non-load-bearing future-route context |

What stays open is exactly the load-bearing carrier-identification step:

1. derive that the physical scalar charged-lepton lane must replace
   the ordered Cartesian pair `(r_1, r_2)` on the doublet plane by the
   single radius `rho_perp = sqrt(r_1^2 + r_2^2) / sqrt(6)` from a
   independently audited upstream theorem rather than introducing the quotient as
   the exact two-slot carrier;
2. equivalently, derive that the scalar charged-lepton observable
   principle on `Herm_circ(3)` factors through the `SO(2)`-orbit
   invariant `r_1^2 + r_2^2` rather than the ordered pair
   `(r_1, r_2)`, from an independently audited framework input.

Until (1)/(2) is supplied elsewhere, the load-bearing algebraic result of
this note is exactly the unreduced obstruction: the determinant weights are
`(1, 2)` and land at `kappa = 1`. The conditional reduced-carrier paragraph
is only a correct context calculation on a separately supplied future carrier; it is
not a theorem claimed here and not a first-principles closure of the
operator-side `kappa = 2` lane.
The companion `KOIDE_MRU_DEMOTION_NOTE_2026-04-20` documents
(Section 1.2) that spectrum-native scalar observables on
`Herm_circ(3)` are **not** `SO(2)`-invariant in general — `tr(H^3)`
and `det(H)` carry an explicit `cos(3 arg b)` channel — so the
`SO(2)` quotient is strictly stronger than "scalar observables are
spectrum-native" and is not a corollary of the audited observable
principle on this branch.

## 9. Path A future work

To promote a separate positive MRU quotient route, the missing work is:

1. an independently audited upstream theorem that derives the scalar-lane `SO(2)`
   quotient from the repository's axioms rather than defining it
   locally;
2. equivalently, an independently audited upstream theorem that decouples the
   `cos(3 arg b)` channel of `Herm_circ(3)` scalar observables on the
   physical charged-lepton lane.

Those tasks are not prerequisites for the bounded theorem claimed here,
because that theorem is the unreduced obstruction.

Per the demotion note already on main, the `kappa = 2` operator-side
gate does **not** depend on supplying (1)/(2): two independent
routes (`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19`
and `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19`)
already carry it without any `SO(2)`-quotient postulate. The Path A
work above is a path to promote **this** row, not a prerequisite for the
operator-side closure.

## 10. Boundaries

This note does **not**:

- modify the parent row's audit-ledger entry;
- derive the scalar-lane `SO(2)` quotient of the non-trivial real
  doublet from independently audited upstream inputs;
- use the conditional reduced-carrier calculation as a load-bearing premise;
- override the `KOIDE_MRU_DEMOTION_NOTE_2026-04-20` reclassification
  of this row's MRU route as supplementary / alternative-framing
  support;
- close the operator-side `kappa = 2` gate (already carried on main by
  the spectrum-operator bridge and block-total Frobenius routes
  without any `SO(2)`-quotient assumption);
- dispute the unreduced `(1, 2)` weight-class obstruction calculation
  itself, which the audit accepts as exact algebra on the unreduced
  `3 x 3` carrier.

The same audit-named missing bridge theorem also blocks the companion
row `koide_moment_ratio_uniformity_theorem_note_2026-04-19`
(for the same `SO(2)`-quotient carrier choice).

## 2026-05-22 source-graph hygiene: open-parent science backlog

The load-bearing carrier-identification step (mapping the 3x3 charged-lepton
block to the two-slot reduced carrier `(rho_+, rho_⊥)`) remains a definitional
reduction, not a derivation from independently audited source theorems. No
independently audited replacement theorem currently exists for that bridge.

Historical downstream rows in the BAE-probe family and the koide-A1-probe
family used this note as positive MRU carrier support. Under the present
unreduced-scope correction, those consumers must not treat this row as a
positive `kappa = 2` derivation. They either need a separate independently
audited carrier-identification theorem from the framework axioms, or they must
cite this row only for the unreduced determinant obstruction.

**Dispatch parent candidate:** If a future independent review evaluates
whether this row is a non-chain-closing alias/decorative handle, the nearest
independently audited sibling candidate is
[`KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md`](KOIDE_DWEH_CYCLIC_COMPRESSION_NOTE_2026-04-18.md)
for the cyclic-carrier setup only. Any future positive MRU quotient route is
a genuine science backlog item ("derive the carrier-identification bridge
that closes MRU") rather than a hygiene fix. This is source-side routing
context only; it does not assert an audit or effective-status outcome.

## 2026-06-15 audit-unlock residual certificate

This source-side update is a re-audit packet, not an audit verdict. The
unreduced `3 x 3` weight obstruction remains the current framework-native
closure: the determinant weights are `(1,2)` and therefore the unreduced
carrier lands at `kappa = 1`, not MRU. The reduced two-slot calculation is
kept only as a conditional consequence map.

The exact residual is unchanged and singular: a later theorem must derive
the scalar-lane `SO(2)` quotient, equivalently prove that the
`cos(3 arg b)` channel decouples on the physical charged-lepton scalar lane.
Until that theorem exists, this row should be re-audited only as an
unreduced obstruction plus conditional quotient algebra. No new axiom,
admission, observed value, or status promotion is introduced by this repair.
