# Area-Law Quarter Broader No-Go Note

**Date:** 2026-04-25
**Status:** unaudited no-go support theorem for Planck Target 2
**Runner:** `scripts/frontier_area_law_quarter_broader_no_go.py`

## Cited authorities (one-hop deps)

- [`BH_ENTROPY_DERIVED_NOTE.md`](BH_ENTROPY_DERIVED_NOTE.md) — `retained_bounded`.
  Records the bounded RT bond-dimension companion identification on the existing
  `Cl(3)/Z^3` free-fermion carrier; this no-go bounds the asymptotic Widom
  coefficient that companion approaches.
- [`BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md`](BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md)
  — `retained_bounded`. The single-carrier no-go that this note generalizes
  from one diamond / one cubic Fermi surface to the full simple-fiber Widom
  class.
- [`PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md`](PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md)
  — `audited_conditional`. Derives the action-side primitive coefficient
  `c_cell = Tr((I_16/16) P_A) = 1/4` on the primitive event cell. This is the
  Planck-side `1/4` that this no-go shows the simple-fiber Widom class cannot
  match by entanglement.
- [`PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md`](PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md)
  — `audited_conditional`. Records the additive finite-boundary extension of
  the action-side `c_cell = 1/4` carrier and the conditional carrier-share
  identity matching `S_BH = A/(4 G_Newton,lat)` at `G_Newton,lat = 1`.

These citations make the no-go's gap structure explicit: the Planck-side
`c_cell = 1/4` is now derived (conditional on the bridge premise) from the
cited primitive-coframe theorem, while this note shows the simple-fiber Widom
class cannot match it on the entanglement side.

## Admitted-context literature input

The Widom-Gioev-Klich leading-log coefficient formula

```text
c_Widom(Gamma, e_x) = I_x(Gamma) / (12 (2*pi)^(d-1)),
I_x(Gamma) = integral_{partial Gamma} |n_k . e_x| dS_k
```

is admitted as universal physics input from the rigorous Widom-Sobolev line
(Gioev-Klich 2006; Helling-Leschke-Spitzer 2011), as already used by the cited
single-carrier no-go. This note does not re-derive the Widom-Gioev-Klich
asymptotic theorem; it imports it and uses purely combinatorial coarea/fiber
counting on top of it.

## Purpose

This note sharpens the retained BH entropy Widom no-go from one carrier to a
class statement. It does not say that no entanglement carrier can ever produce
`1/4`. It says that the broad simple-fiber Widom class available to the current
free-fermion/Schur-block lane cannot do it.

## Safe statement

Let `Gamma` be a translation-invariant free-fermion Fermi sea in the Brillouin
torus `T^d = [-pi, pi)^d`, `d >= 2`, and let the real-space cut be a flat
primitive boundary face with normal `e_x`. Assume:

1. `partial Gamma` is piecewise smooth away from measure-zero singular sets;
2. for almost every transverse momentum `q in T^(d-1)`, the fiber
   `{k_x : (k_x, q) in Gamma}` is empty, full, or a single interval in the
   `k_x` circle;
3. the RT/bond-rank normalization counts the same primitive boundary rank for
   each independent Schur or species block, so direct sums are normalized by the
   sum of their boundary `log chi` weights.

Then the Widom-Gioev-Klich leading-log coefficient satisfies

```text
c_Widom <= 1/6.
```

In particular, no carrier in this class can produce

```text
c_inf = 1/4.
```

The existing 2D half-filled NN carrier saturates the bound with `c_Widom=1/6`.
The existing 3D half-filled cubic carrier lies below it, at `~0.105`.

## The theorem

For a flat cut with unit rescaled boundary area, the Widom coefficient is

```text
c_Widom(Gamma, e_x)
  = I_x(Gamma) / (12 (2*pi)^(d-1)),

I_x(Gamma)
  = integral_{partial Gamma} |n_k . e_x| dS_k.
```

For almost every transverse momentum `q`, let

```text
N_Gamma(q) = #(partial Gamma intersect (S^1_x x {q})).
```

The coarea formula gives the fiber-count identity

```text
I_x(Gamma) = integral_{T^(d-1)} N_Gamma(q) dq.
```

Under the single-interval hypothesis, `N_Gamma(q) <= 2` almost everywhere:
one interval has two endpoints on the `k_x` circle, while an empty or full
fiber has none. Therefore

```text
I_x(Gamma) <= 2 (2*pi)^(d-1),
```

and hence

```text
c_Widom <= 2 (2*pi)^(d-1) / (12 (2*pi)^(d-1)) = 1/6.
```

But `c_Widom = 1/4` would require

```text
I_x(Gamma) = 3 (2*pi)^(d-1),
```

which is impossible in the simple-fiber class.

## Consequences by dimension

### 2D

For `d=2`,

```text
c_Widom = I_x / (24*pi).
```

The half-filled NN square-lattice Fermi surface is the diamond
`|k_x| + |k_y| = pi`. Its fibers have two crossings for almost every `k_y`,
so

```text
I_x = 4*pi,
c_Widom = 4*pi / (24*pi) = 1/6.
```

Arbitrary one-band NN fillings have at most the same two crossings per
`k_y` fiber, so they cannot exceed `1/6`. Reaching `1/4` would require
`I_x = 6*pi`, equivalently average crossing number `3` across the Brillouin
zone. Since simple closed one-interval fibers have crossing number at most
`2`, this cannot occur without multi-pocket or multi-band structure.

### 3D

For `d=3`,

```text
c_Widom = I_x / (48*pi^2).
```

A simple-fiber cubic carrier obeys

```text
I_x <= 8*pi^2,
c_Widom <= 1/6.
```

The retained half-filled cubic NN carrier only has crossings on the subset
`|cos k_y + cos k_z| < 1`, so its projected crossing measure is smaller and
the coefficient is `~0.105`, in agreement with the retained runner. Reaching
`1/4` would require `I_x = 12*pi^2`, again beyond the one-interval maximum.

## Schur/direct-sum descendants

If a finite Schur block or species stack is a direct sum of independent
simple-fiber Slater determinants, the leading entropy and the maximal
boundary-rank normalization both add:

```text
S_total ~ sum_alpha w_alpha c_alpha |partial A| log L,
S_max   ~ sum_alpha w_alpha |partial A| log L,
```

with positive weights `w_alpha = log chi_alpha`. The normalized coefficient is
therefore the convex average

```text
c_total = (sum_alpha w_alpha c_alpha) / (sum_alpha w_alpha).
```

If every block has `c_alpha <= 1/6`, then `c_total <= 1/6`. Thus finite-density
Schur-block bookkeeping does not promote the simple-fiber class to `1/4`.

This matches the species-universality check in
[BH_ENTROPY_DERIVED_NOTE.md](./BH_ENTROPY_DERIVED_NOTE.md): duplicating
species does not change the RT ratio when the boundary rank is counted
consistently.

## What remains outside the no-go

The theorem deliberately does not rule out:

- multi-pocket or multi-band free fermions whose `k_x` fibers have more than
  one occupied interval on positive transverse measure;
- a physically selected NNN or longer-range dispersion whose projected crossing
  multiplicity is exactly `3` in the Widom integral;
- non-Fermi-liquid states for which the Widom-Gioev-Klich hypothesis is not the
  right asymptotic theorem;
- gapped horizon/edge carriers with a strict area law and a separately derived
  entropy-per-face coefficient;
- topological sectors whose universal content is subleading but whose leading
  edge Hilbert-space dimension is fixed by an additional microscopic axiom.

Those are residual positive targets. They require more structure than the
current simple-fiber free-fermion or Schur-block lanes provide.

## Relation to the Planck `c_cell = 1/4`

The Planck conditional packet proves

```text
c_cell = Tr((I_16/16) P_A) = 1/4
```

as a primitive gravitational boundary/action coefficient, and the finite-patch
extension theorem proves its additive extension once that carrier
identification is accepted. This note shows that the simple-fiber Widom
entanglement class cannot be identified with that coefficient. The two `1/4`
surfaces remain structurally different unless a new entropy carrier theorem
bridges them.

### Authority-chain provenance

The action-side `c_cell = 1/4` is no longer asserted in this note: it is
imported from the cited
[`PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM`](PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md)
where it is derived (conditional on first-order coframe locality and unit
primitive response normalization, both also cited there) as the unique
source-free, additive, coframe-slot-symmetric, unit-normalized first-order
coframe boundary carrier coefficient. The cited
[`PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM`](PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md)
then extends this single-cell coefficient to finite boundary patches and
records the conditional carrier-share matching with `A/(4 G_Newton,lat)`.

What this no-go adds, on top of that derived action-side `1/4`, is purely the
entanglement-side bound: under the simple-fiber hypothesis,

```text
c_Widom <= 1/6 < 1/4.
```

The no-go therefore does not depend on whether the action-side `1/4` is
ultimately retained or not. It is a clean class statement about which
entanglement carriers can match any putative `1/4` action-side target, and is
agnostic to the bridge premise the cited Planck notes carry.

## What this PR is NOT

This rigorization does **not**:

- derive the Widom-Gioev-Klich coefficient formula from `A_min`. That formula
  remains an admitted universal physics input on the same footing as in the
  cited single-carrier no-go.
- close the upstream `BH_ENTROPY_DERIVED_NOTE` / `BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE`
  statuses. Those are `retained_bounded` and this note
  inherits their bounded surface.
- promote audit status. The audit ledger is not modified; status descriptor
  alignment to `unaudited` matches the live audit ledger entry.

## No-go discipline gate (N1–N8)

**Status:** PASS for the narrow simple-fiber-class bound only. The claim being
closed is `c_Widom <= 1/6 < 1/4` for the simple-fiber Widom class (every flat
free-fermion cut whose `k_x`-fiber is empty, full, or a single interval for
a.e. transverse momentum, plus its additive Schur/species descendants). It is
NOT a claim that no entanglement carrier on `Cl(3)/Z^3` can ever produce `1/4`,
and NOT a claim that the action-side `c_cell = 1/4` is wrong.

### N1 - Alternative route enumeration

| route | what it would attempt | why it fails for this scoped no-go | marker |
|---|---|---|---|
| Single-band NN filling sweep | Tune the half-filled NN diamond/cubic filling to push the average crossing number past 2 toward 3. | A one-band single-interval fiber crosses the `k_x` circle at most twice, so `I_x <= 2(2*pi)^{d-1}` and `c_Widom <= 1/6` for every filling; `1/4` needs crossing number 3. | ATTEMPTED |
| Schur / species stacking | Direct-sum many simple-fiber blocks and read off the combined boundary coefficient. | `c_total` is the `w_alpha = log chi_alpha`-weighted convex average of the per-block `c_alpha <= 1/6`, so it stays `<= 1/6` (matches the `BH_ENTROPY_DERIVED_NOTE` species-universality check). | ATTEMPTED |
| Per-direction / area re-normalization | Reweight the boundary area or pick a non-primitive cut to inflate `I_x` relative to the face count. | `c_Widom = I_x / (12(2*pi)^{d-1})` is taken at unit rescaled boundary area with the same face-counting convention; rescaling cancels in numerator and denominator and cannot lift the crossing-number ceiling. | ATTEMPTED |
| Multi-pocket / multi-interval Fermi geometry | Use a dispersion whose `k_x`-fiber has two or more occupied intervals on positive transverse measure (crossing number 3). | This LEAVES the simple-fiber hypothesis (2) and is explicitly outside the no-go's scope; it is left open as a positive target, not closed. | OUT OF SCOPE |
| Self-dual half-zone parity gate | Activate a second edge orbital on a `Z_2` low-Laplacian sheet of measure `1/2`, giving `<N_x> = 2 + 2*(1/2) = 3`. | Same exit: it leaves the single-interval class (the gated channel adds a second interval on half the transverse measure). Realized by `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`; this note does not foreclose it. | OUT OF SCOPE |
| Gapped horizon / topological edge carrier | Replace the gapless Widom asymptotics with a strict area law whose per-face coefficient is fixed by a separate microscopic input. | The Widom-Gioev-Klich theorem is not the asymptotic theorem for a gapped or topological-sector carrier; that carrier is governed by a different (separately derived) coefficient and is left as a residual positive target. | OUT OF SCOPE |

### N2 - Wall-independence audit

The collapsed wall set for this no-go has ONE wall: the single-interval
crossing-number ceiling `N_Γ(q) <= 2` a.e. (hypothesis 2). Everything else is
arithmetic on top of it — the coarea identity converts `<= 2` into
`I_x <= 2(2*pi)^{d-1}`, and the division by `12(2*pi)^{d-1}` converts that into
`c_Widom <= 1/6`. The Schur/direct-sum descendant bound is not a second
independent wall; it is the convexity image of the same per-block ceiling.
What could change the verdict is exactly removal of that one wall (a fiber with
crossing number 3, i.e. a multi-interval or parity-gated occupied set), which
is precisely the open route N1 marks OUT OF SCOPE.

### N3 - Hidden-wall scan

The phrases "broader", "class statement", "simple-fiber", and "cannot match"
are not used as hidden retained inputs. The EXPLICIT load-bearing inputs are:
(i) the admitted Widom-Gioev-Klich coefficient formula
`c_Widom = I_x / (12(2*pi)^{d-1})` with `I_x = ∫_{∂Γ} |n_k · e_x| dS_k`
(imported physics, not re-derived here); (ii) the coarea fiber-count identity
`I_x = ∫_{T^{d-1}} N_Γ(q) dq`; (iii) the single-interval hypothesis (2)
yielding `N_Γ(q) <= 2` a.e.; (iv) additivity of leading entropy and of the
maximal boundary-rank normalization under direct sums, with positive weights
`w_alpha = log chi_alpha`, yielding the convex average. The action-side
`c_cell = 1/4` is imported context, NOT a premise of the entanglement-side
bound — the note states the bound is "agnostic to the bridge premise" and holds
whether or not the action-side `1/4` is retained.

### N4 - Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md` (`retained_bounded`) | The single-carrier `c_Widom < 1/4` gap for one diamond / one cubic Fermi surface. | The same gap, generalized to every simple-fiber carrier and its Schur descendants via the crossing-number ceiling. | yes |
| `BH_ENTROPY_DERIVED_NOTE.md` (`retained_bounded`) | The RT-ratio invariance under consistent boundary-rank counting (species universality). | The convex-average step uses exactly that invariance to bound Schur/direct-sum descendants by `1/6`. | yes |
| `PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md` (`audited_conditional`) | The derivation of the action-side target `c_cell = 1/4`. | Imported only to NAME the `1/4` target the class cannot reach; it is not a premise of the `<= 1/6` entanglement bound. | no |
| `PLANCK_BOUNDARY_DENSITY_EXTENSION_THEOREM_NOTE_2026-04-24.md` (`audited_conditional`) | The additive finite-patch extension and `A/(4 G)` carrier-share matching. | Context for the action-side surface only; supplies the face-counting convention, not the negative bound. | no |

Non-matching witnesses (the two Planck action-side notes) are not load-bearing
for this no-go; they fix the target value and the area convention but the
`c_Widom <= 1/6` inequality is proved without them.

### N5 - Rhetoric audit

The broad phrases — "broader no-go", "quarter", "cannot produce", "closed
negatively", "no carrier in this class" — are scoped strictly to the
simple-fiber Widom class defined by hypotheses (1)-(3): flat primitive cut,
single occupied `k_x`-interval per transverse fiber, additive Schur/species
normalization. "Quarter" refers only to the inability to reach the *value*
`1/4` within that class, not to any claim about the Planck `c_cell = 1/4`
itself. The over-broad reading "no entanglement carrier on `Cl(3)/Z^3` can ever
produce `1/4`" is explicitly disclaimed in the note's "Unsafe wording" block
and is NOT asserted here.

### N6 - Partial-closure path scan

The following non-axiom partial-closure paths remain OPEN (the note's "What
remains outside the no-go" list), and none is a new axiom:

- a multi-pocket / multi-band free fermion whose `k_x`-fiber has more than one
  occupied interval on positive transverse measure (crossing number 3);
- a physically selected NNN or longer-range dispersion with projected crossing
  multiplicity exactly 3 in the Widom integral;
- a self-dual `Z_2` half-zone parity gate supplying the second occupied
  interval on measure `1/2` (already constructed in
  `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`, whose
  selector is a residual primitive involution, not a fitted parameter);
- a gapped horizon/edge carrier with a strict area law and a separately derived
  entropy-per-face coefficient;
- a topological sector whose leading edge Hilbert-space dimension is fixed by an
  additional microscopic input.

Each of these is a positive structural target requiring more structure than the
simple-fiber free-fermion / Schur-block lane; the no-go does not relabel any of
them as a forbidden axiom.

### N7 - Steelman

The strongest objection is that the `1/6` ceiling looks like an artifact of the
single-interval hypothesis (2): a generic translation-invariant Fermi sea need
not have single-interval fibers, so a physically natural dispersion could
already sit at crossing number 3 and reach `1/4` without any exotic input. This
objection is correct AS STATED — and it is exactly why the note scopes the
claim to the simple-fiber class rather than to all free fermions. It does not
break the scoped no-go: within hypothesis (2) the coarea bound `N_Γ(q) <= 2` is
exact, so `c_Widom <= 1/6` is unconditional there. The objection instead
identifies the door out (multi-interval geometry), which the note already lists
as the residual positive route and which the parity-gate carrier note walks
through.

### N8 - Cross-cycle echo

A recurrent repo overclaim failure mode is to test one representative carrier
(here, the half-filled NN diamond) and then declare the entire entanglement-to-
`1/4` program closed. This note avoids that echo in two ways: (a) it states
explicitly that it "does not say that no entanglement carrier can ever produce
`1/4`" and brands the universal reading "Unsafe wording"; and (b) it keeps the
claim boundary at the simple-fiber crossing-number ceiling, enumerating the
multi-pocket, parity-gate, gapped-horizon, and topological routes as still
open. The downstream `AREA_LAW_PRIMITIVE_PARITY_GATE_CARRIER_THEOREM_NOTE_2026-04-25.md`
in fact realizes one of those routes (crossing count 3 → `c_Widom = 1/4`),
which is consistent with — not a contradiction of — this scoped no-go.

## Literature anchor

The logic here uses the free-fermion Widom coefficient from Gioev-Klich and
the rigorous Widom/Sobolev line used in the retained no-go. It is positioned
against the older black-hole entanglement and holographic literature:

- Bombelli, Koul, Lee, and Sorkin, "Quantum source of entropy for black holes,"
  Phys. Rev. D 34, 373-383 (1986).
- Srednicki, "Entropy and area," Phys. Rev. Lett. 71, 666-669 (1993).
- Ryu and Takayanagi, "Holographic Derivation of Entanglement Entropy from the
  anti-de Sitter Space/Conformal Field Theory Correspondence," Phys. Rev. Lett.
  96, 181602 (2006).
- Gioev and Klich, "Entanglement Entropy of Fermions in Any Dimension and the
  Widom Conjecture," Phys. Rev. Lett. 96, 100503 (2006).
- Brandao and Horodecki, "An area law for entanglement from exponential decay
  of correlations," Nature Physics 9, 721-726 (2013).
- Swingle, "Entanglement renormalization and holography," Phys. Rev. D 86,
  065007 (2012), and Pastawski, Yoshida, Harlow, and Preskill, "Holographic
  quantum error-correcting codes: toy models for the bulk/boundary
  correspondence," JHEP 06, 149 (2015).

## Package wording

Safe wording:

> The simple-fiber Widom class is closed negatively for Planck Target 2:
> any straight-cut free-fermion carrier with at most one occupied
> `k_x`-interval per transverse momentum fiber has `c_Widom <= 1/6`, and
> Schur/direct-sum descendants remain bounded by the same convexity argument.
> An exact `1/4` entanglement carrier therefore requires either
> multi-pocket/multi-interval Fermi geometry selected by a physical law or a
> gapped horizon-sector area law with a new primitive-boundary identification.

Unsafe wording:

> No entanglement carrier on `Cl(3)/Z^3` can ever produce `1/4`.

## Verification

Run:

```bash
python3 scripts/frontier_area_law_quarter_broader_no_go.py
```

The runner checks the fiber-count identity, the `1/6` upper bound in `2D` and
`3D`, the exact half-filled diamond saturation, the sub-saturation of the
retained cubic carrier, the impossibility of `1/4` in the simple-fiber class,
and the convexity of Schur/direct-sum descendants.

Current output:

```text
SUMMARY: PASS=24  FAIL=0
c_3D(midpoint quadrature) = 0.105064
```
