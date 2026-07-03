# `y_t` Vertex-Power Theorem: Why `alpha_s(v) = alpha_bare / u_0^2`

**Date:** 2026-04-15 (structural-derivation repair 2026-06-11)
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On the gauged staggered-Dirac kinetic surface — the
adjacency-licensed nearest-neighbor covariant hopping bilinear, with the
named link-exponential convention and the standard quadratic-response
(background-field) coupling normalization — the vertex power of the
mean-field link dressing is

```text
n_link  =  (external gauge legs of the quadratic response)
           x (gauge links per vertex insertion)
        =  2 x 1  =  2,
```

where the factor `1` (one gauge link per covariant hop, hence per vertex
insertion) is FORCED by site-local SU(3) gauge covariance plus the
edge-only adjacency license (Schur bi-equivariance, Lemma L1), and the
factor `2` (two vertex insertions in the coupling-defining channel) is
FORCED by the second-order structure of the fermion effective action
(Lemma L3). Specializing the exact coupling-map algebra at `n_link = 2`
gives `alpha_s(v) = alpha_bare / u_0^2`. The exponent is derived from
operator structure with NO consumption of any strong-coupling value,
Z-pole running, or external comparator (no-back-propagation certificate,
Section 6). Five named boundaries (B-GATE, B-ADJ, B-CONV, B-CHAN,
B-SPLIT) state exactly where the derivation stops.
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome; audit verdict and effective status
are set only by the independent audit lane.
**Primary runner:** [`scripts/frontier_vertex_power.py`](../scripts/frontier_vertex_power.py)
(`Breakdown: A=4 B=0 C=12 D=0`, `TOTAL: PASS=16 FAIL=0`)
**Authority role:** supplies the structural exponent `n_link = 2` that
the retained algebraic identity note
([`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](./ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md))
explicitly disclaims ("does **not** assert that the vertex-power
exponent `k = 2` is a prediction of the framework's axioms"). It is the
named discharge target of boundary input B3 of
`ALPHA_S_DERIVED_NOTE.md` — cited there and here strictly as
**motivation**, never as an authority for any step below.

## 0. Changelog

- **2026-04-15.** Original note: prose link-counting argument with the
  shared runner; coupling map asserted as the "LM link-counting rule".
- **2026-06-11.** Structural-derivation repair (this revision), written
  for the B3-discharge role of the alpha_s lane (motivation only; the
  alpha_s note is not an authority here). Defects fixed: (1) the prior
  registered runner hard-coded `condition=True` for every load-bearing
  link-count check; (2) the prior runner's Part 6 selected `n_link = 2`
  by closest match to the observed Z-pole strong coupling — class-(G)
  back-propagation now removed entirely and excluded by a computed
  certificate; (3) the prior runner made a class-(D) comparator
  load-bearing (2-loop running to the Z pole against the observed
  value) — removed, the runner now has zero class-(D) checks; (4) the
  note's only declared dependency was `ALPHA_S_DERIVED_NOTE.md`
  (circular, since that note's B3 names this lane as its supplier) —
  replaced by the genuine one-hop authorities of Section 4; (5) the
  vertex power was presented as a counting *prescription* — replaced by
  the Schur-forcing derivation (L1) plus the quadratic-response leg
  count (L3), each compute-checked, with the residual conventions named
  as boundaries instead of being silently absorbed. The companion
  coupling-map lane's citation of a "retained D14 CMT identity" in
  `YT_EW_COLOR_PROJECTION_THEOREM.md` was found stale (that note is now
  a kappa-family no-go containing no such identity), so this revision
  re-proves everything it needs self-contained and cites that lane only
  as a non-load-bearing pointer.

## 1. Question

The tadpole-improved physical gauge coupling on the lattice surface is
`alpha_eff = alpha_bare / u_0^{n_link}`. The hierarchy lane uses
`n_link = 1` (hopping). The alpha_s lane uses `n_link = 2` and has so
far carried that exponent as a declared structural input (its boundary
B3). Is `n_link = 2` *derivable* from the framework's structure — and
if not in full, what exactly is the irreducible residual?

## 2. Answer

`n_link = 2` is derived as a product of two forced counts, each
compute-certified by the registered runner:

1. **One gauge link per vertex insertion (forced; L1 + L2).** On the
   edge-only adjacency-licensed surface, a gauge-covariant hopping
   dressing `f` must satisfy `f(g U h^dag) = g f(U) h^dag` for all
   `g, h` in SU(3). Setting `U = I` and `h = g` shows `f(I)` commutes
   with all of SU(3), so `f(I) = c I` by Schur's lemma (fundamental
   irrep); then `f(V) = f(V I I^dag) = V f(I) = c V`. Hence the
   covariant hop is exactly LINEAR in the edge link — one link per
   hopping term, and therefore one link per background-field vertex
   insertion `D' = dD/d(eps)` under the link-exponential convention
   (`dU/d(eps)|_0 = i a U_0`, one explicit link factor).
2. **Two vertex insertions in the coupling-defining channel (forced;
   L3).** The coupling is read from the quadratic response of the
   fermion effective action `Gamma[A] = -Tr ln D[A]` (standard
   background-field normalization, declared as B-CHAN). Second-order
   expansion produces exactly two operator structures — the contact
   term `Tr[D^{-1} D'']` and the current-current term
   `Tr[D^{-1} D' D^{-1} D']` (runner: finite-difference log-determinant
   matches the operator formula to `~1e-6`). The coupling carrier, the
   channel with one independent single-link vertex per external gauge
   leg, contains exactly TWO insertions of `D'`: its computed
   link-degree is `2` to `1.3e-15`, while `n = 0, 1, 3, 4` are excluded
   by computed residuals `> 0.1` (falsification leg), and the leg count
   provably tracks the response order (quartic channel: computed degree
   4; cubic channel: vanishes by a Furry-type cancellation).

Combining with the exact coupling-map algebra at `n_link = 2` (retained
one hop away, Section 4 item 1):

```text
alpha_s(v) = alpha_bare / u_0^2,    alpha_LM^2 = alpha_bare * alpha_s(v).
```

What is NOT derived is stated as five named boundaries below. None of
them is a numeric knob: every one is a structural convention or gate,
and no choice among the surviving conventions can move the exponent off
`2` without leaving the licensed surface (the runner's falsification
legs exhibit exactly which license each alternative violates).

## 3. Boundaries (stated up front)

| ID | Boundary | Where it bites |
|---|---|---|
| B-GATE | The gauged staggered-Dirac kinetic surface is the realization gate. The kinetic-class forcing theorem (Section 4 item 2) collapses the licensed kinetic family to two flux classes, discharges the absorbing-frame premise on the flux-`(-1)` branch, and leaves exactly the one-bit flux selector open; the SU(3) color attachment by minimal coupling on edges is part of the gauge-sector realization | the whole note quantifies on this surface |
| B-ADJ | Edge-only support of the hopping dressing is the Lattice axiom's adjacency license, not derived; off-license, multi-link covariant dressings exist (runner leg D-ADJ exhibits a gauge-covariant 5-link dressing) and would change the count | L1 |
| B-CONV | The link-exponential convention `U(eps) = exp(i eps a) U_0`, hence `dU/d(eps)|_0 = i a U_0` (one link per vertex), is the named gauge-sector convention | L2 |
| B-CHAN | "The coupling is read from the quadratic (two-external-leg) gauge response of `Gamma[A]`" is the standard background-field normalization, declared not derived. Given it, the leg count `2` is forced; the single-link contact (tadpole) term is not the coupling carrier under this normalization | L3 |
| B-SPLIT | Converting the explicit-insertion operator dressing `u_0^{+2}` into the coupling dressing `u_0^{-2}` uses the tree-level split of the correlator into coupling x kinematic factor (Lepage-Mackenzie mean-field convention). The runner computes the consistency fact that the self-consistent response has link-degree `~0` (propagators absorb the vertex factors), which is exactly why the dressing must be assigned to the explicit insertions | L4 |

## 4. Cited authorities (one hop, with license statements)

Load-bearing (markdown links):

1. [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](./ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
   (retained, positive_theorem). License used: the exact algebraic
   identity surface over abstract positives — `alpha_s(v) u_0^2 =
   alpha_bare`, `alpha_LM^2 = alpha_bare alpha_s(v)`, constant-ratio
   chain. That note explicitly does NOT claim the exponent `k = 2` is
   derived; this note supplies exactly that exponent. Consumed at L4
   only.
2. [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](./STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
   (bounded_theorem). License used: the characterization of the
   licensed kinetic surface — the adjacency-licensed nearest-neighbor
   bilinear family collapses to two flux classes; the absorbing frame
   exists and is unique up to gauge x global frame on the flux-`(-1)`
   branch; the irreducible kinetic residual is the one-bit flux
   selector (its B-BIT). This is the supplier that narrows B-GATE from
   an infinite-dimensional kinetic declaration to one bit plus the
   gauge attachment. Consumed for the scope statement of B-GATE; the
   link-degree facts themselves are re-proved self-contained here.
3. [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
   (axiom premise node). License used: Lattice adjacency (the edge-only
   support reading behind B-ADJ). Nothing else is drawn from the
   axioms.

Plain-text pointers (NOT load-bearing):

- `ALPHA_S_DERIVED_NOTE.md` — **motivation only, never authority.** Its
  declared boundary input B3 ("the tadpole-improved physical coupling
  carries vertex power `n_link = 2` ... derivation ... is the open
  target of the coupling-map lane") names the gap this note closes on
  its stated surface. No value, step, or license is consumed from it;
  in particular this note does not read any downstream headline
  `alpha_s(v)` value, Z-pole readout, or plaquette reuse number.
- `ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md` —
  companion algebra of the rescaling map `(M)` given a correlator
  change-of-variables identity plus the tree-level split. NOT consumed:
  its cited "retained D14" authority (`YT_EW_COLOR_PROJECTION_THEOREM.md`
  §2.4) is stale — the current text of that note is a kappa-family
  no-go containing no CMT identity — so this revision re-proves what it
  needs self-contained and treats the operator-dressing-to-coupling
  conversion as the named boundary B-SPLIT instead.
- `YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md` —
  companion operator-counting lemma. Its S1–S3 are consistent with L2
  and L3 here, but it declares that it consumes the coupling-map
  identity "from the parent `YT_VERTEX_POWER_DERIVATION.md`", so citing
  it as an authority would be circular; this revision consumes nothing
  from it.
- `ALPHA_S_DERIVED_NARROW_THEOREM_NOTE_2026-05-10.md`,
  `PLAQUETTE_SELF_CONSISTENCY_NOTE.md` — adjacent lane context; no
  value or license consumed (in particular `<P> = 0.5934` is NOT read:
  this note's claim surface contains no plaquette number).

Forbidden imports: no PDG values, no observed strong coupling, no
Z-pole running, no fitted selectors, no new axioms. Enforced by the
runner's self-scan certificate (Section 6).

## 5. Derivation

### L1 (Schur forcing: one gauge link per covariant hop)

On the licensed surface (B-GATE, B-ADJ), the hopping term from `x` to
`x + mu` may depend on gauge data on that edge only, i.e. on
`U_mu(x) ∈ SU(3)`. Site-local gauge covariance of the bilinear
`psi^dag_{x+mu} f(U_mu(x)) psi_x` under
`U_mu(x) -> g(x+mu) U_mu(x) g(x)^dag` requires

```text
f(g U h^dag) = g f(U) h^dag        for all g, h ∈ SU(3).          (L1.1)
```

**Lemma.** The solutions of (L1.1) are exactly `f(U) = c U`, `c ∈ C`.

*Proof.* Set `U = I`, `h = g`: `f(I) = g f(I) g^dag` for all `g`, so
`f(I)` commutes with the full fundamental irrep; by Schur's lemma
`f(I) = c I`. Now set `U = I` with arbitrary `g` and `h = I`:
`f(g) = g f(I) = c g` for every `g ∈ SU(3)`. ∎

Hence the covariant hopping bilinear carries exactly ONE power of the
link per term: `n_link(hopping) = 1`, forced, not chosen. The runner
certifies the discriminating computation (only the linear dressings
pass a bi-equivariance scan; `U^2`, `U^dag`, `U tr(U)/3`, `(U+U^dag)/2`,
`I` are rejected with residuals `> 0.1`) and exhibits the off-license
escape (a gauge-covariant 5-link dressing `U_mu(x) W_P(x)`), showing
B-ADJ is genuinely load-bearing.

### L2 (the vertex insertion is single-link)

With the link-exponential convention (B-CONV), the background-field
vertex `D' = dD/d(eps)|_0` inherits exactly one link factor per
non-zero entry, since `dU/d(eps)|_0 = i a U_0`. Computed: (i) the
finite-difference derivative of actual matrix exponentials matches
`i a U_0` to `~4e-10`; (ii) `D(u I) = u D_hop` at `m = 0` to exactly
`0` (the hopping bilinear has link-degree 1 — the computed counterpart
of L1); (iii) `D'(u·base) = u D'(base)` exactly (the vertex has
link-degree 1); (iv) the built `D'`, `D''` match finite differences of
the full background-field Dirac operator (the derivative operators are
not hand-tuned).

### L3 (the quadratic response carries exactly two vertex insertions)

The coupling is defined through the quadratic response of
`Gamma[A] = -Tr ln D[A]` (B-CHAN). Expanding to second order in the
background amplitude produces exactly two operator structures,

```text
d^2/d(eps)^2 Tr ln D  =  Tr[D^{-1} D'']  -  Tr[D^{-1} D' D^{-1} D'],   (L3.1)
```

certified by the runner against a finite-difference log-determinant
(relative mismatch `~9e-7` at `L = 4`, `m_reg = 0.05`). The coupling
carrier is the current-current channel `Tr[D^{-1} D' D^{-1} D']`: one
single-link vertex per external gauge leg, two legs for a quadratic
response. Its link-degree — the n_link detector, computed by scaling
the base links `u` with V-scheme propagators held fixed — is

```text
n_link(VP) = 2.000000000000   (residual 1.3e-15),
```

with the falsification leg: `n ∈ {0, 1, 3, 4}` fail the computed
scaling law by margins `> 0.1`. The contact (tadpole) term has computed
link-degree exactly `1` — it is the single-insertion channel and is not
the coupling carrier under B-CHAN. That the leg count tracks the
response order (and is therefore not a dial) is certified by the
quartic channel (computed link-degree exactly `4`; the cubic channel
vanishes identically by a Furry-type cancellation, magnitude `~2e-16`).

### L4 (coupling map at the derived exponent)

Each explicit link in the coupling-defining operator carries one factor
of the mean-field dressing `u_0` under the vacuum-centered rescaling
`U = u_0 V`: the insertion-pair operator dresses as `u_0^{+2}` (exact,
computed), while the self-consistent response has link-degree `~0`
(propagators absorb the vertex factors) — which is exactly why the
dressing must be assigned to the explicit insertions (B-SPLIT). Under
the tree-level split, the physical coupling absorbs the inverse factor,
and the retained algebraic identity surface (Section 4 item 1) at
`n_link = 2` gives

```text
alpha_s(v) = alpha_bare / u_0^2,    alpha_LM^2 = alpha_bare * alpha_s(v),
```

verified by the runner in exact rational arithmetic (zero floating
error) over a grid of abstract positives — no numerical value of
`u_0`, `alpha_bare`, or `alpha_s` is consumed anywhere in L1–L4.

## 6. No-back-propagation certification

The hostile failure mode for a "vertex power derivation" is that
`n_link = 2` was reverse-engineered from the observed strong coupling.
This note and runner exclude that by construction and by certificate:

- the exponent is detected from operator structure (link-degree
  residuals at machine precision) with alternatives excluded by
  computed margins, on a chain that contains no strong-coupling number;
- the runner performs NO renormalization-group running, imports no
  Z-pole scale or observed coupling, and has ZERO class-(D) checks
  (`Breakdown: A=4 B=0 C=12 D=0`);
- a self-scan check (`no_back_propagation_from_alpha_s`) fails the
  runner if its source ever acquires the observed Z-pole coupling
  value, the downstream headline values, the experimental-data-group
  acronym, Z-pole masses/thresholds, or RG-integration machinery;
- the runner does not read downstream numeric helper modules or
  canonical-value surfaces; every computed check is internal to the
  operator-structural derivation.

## 7. What the runner computes

[`scripts/frontier_vertex_power.py`](../scripts/frontier_vertex_power.py)
— deterministic (fixed seed), numpy only, runtime well under one
minute. 16 checks tagged `[A]`/`[B]`/`[C]`/`[D]`, with
`RESIDUAL (declared-open): ...` lines printed where each boundary is
load-bearing:

- **L1 [C]:** Schur bi-equivariance scan over random SU(3) triples
  (only linear dressings survive); gauge-covariant 5-link dressing
  exhibited (B-ADJ falsification leg).
- **L2 [C]:** finite-difference link-exponential derivative; exact
  `D(uI) = u D_hop`; exact `D'(u·base) = u D'(base)`; built `D'`,`D''`
  vs finite differences of the background-field operator.
- **L3 [C]:** quadratic-response structure identity (L3.1) vs computed
  log-determinant; bubble link-degree `= 2` and tadpole `= 1` at
  machine precision; alternative powers `{0,1,3,4}` excluded
  (falsification leg); quartic-channel degree `4` with vanishing cubic
  channel; self-consistent response degree `~0` (B-SPLIT display).
- **L4 [A]:** integer exponent extraction; exact-rational coupling-map
  identities at `n = 2`.
- **Certificate [A]:** forbidden-token self-scan; zero class-(D)
  checks.

Expected output (deterministic):

```text
Breakdown: A=4 B=0 C=12 D=0
TOTAL: PASS=16 FAIL=0
```

Exit code 0 iff FAIL=0.

## 8. What this does NOT close

- **B-GATE.** The staggered-Dirac kinetic realization itself; reduced
  to the one-bit flux selector by the kinetic-class forcing theorem,
  plus the gauge-sector (SU(3) minimal-coupling) attachment. Not closed
  here.
- **B-CONV, B-CHAN, B-SPLIT.** The link-exponential convention, the
  quadratic-response coupling normalization, and the tree-level
  coupling/kinematic split are named conventions, not derivations from
  the axioms.
- Any numerical value of `u_0`, `alpha_bare`, `alpha_s(v)`, or the
  Z-pole coupling. This note's claim surface contains no number except
  the integer exponent.
- The alpha_s lane's other boundary inputs (its B1 plaquette reuse
  license, B2 normalization, B4 scheme/scale identification) and its
  running-bridge corollary. Discharging B3 does not promote that row;
  status flows only through the audit lane.
- The renormalized `y_t` lane, the `v`-endpoint selection, and the
  bridge-conditioned EFT transfer.

## 9. Honest status

```yaml
claim_type_author_hint: bounded_theorem
claim_scope: "On the adjacency-licensed covariant NN hopping surface with the named link-exponential convention and quadratic-response coupling normalization: gauge covariance forces exactly one link per vertex insertion (Schur), the coupling-defining channel carries exactly two insertions (computed link-degree 2, alternatives excluded), hence n_link = 2 and alpha_s(v) = alpha_bare/u_0^2 via the retained coupling-map algebra; boundaries B-GATE/B-ADJ/B-CONV/B-CHAN/B-SPLIT named; no strong-coupling value consumed (certified)."
upstream_dependencies:
  - alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10
  - staggered_dirac_kinetic_class_forcing_narrow_theorem_note_2026-06-10
  - minimal_axioms
admitted_context_inputs: []
source_sets_audit_outcome: false
```

## 10. Command

```bash
python3 scripts/frontier_vertex_power.py
```
