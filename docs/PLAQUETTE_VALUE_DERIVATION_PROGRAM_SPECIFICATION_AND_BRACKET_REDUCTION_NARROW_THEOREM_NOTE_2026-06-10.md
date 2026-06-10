# Plaquette Value Derivation Program: Certified Bracket Interface and KP Certificate Boundary at beta = 6

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** Bounded import-retirement interface for the admitted
plaquette value: it specifies the exact thermodynamic-limit object behind
`<P> = 0.5934`, proves an unconditional `6 beta/L` finite-volume free-energy
rate, gives a certified three-point `ln Z_L` bracket route with an explicit
cost budget, and gives a scoped negative certificate for the standard
single-scale KP/sup-norm cluster-expansion certificate at `beta = 6`. It does
not derive or retire the admitted value.
**Status authority:** independent audit lane only. This source note writes no
audit verdict, retags no ledger row, and does not set or predict an audit
outcome.
**Primary runner:** [`scripts/plaquette_value_derivation_check_2026_06_10.py`](../scripts/plaquette_value_derivation_check_2026_06_10.py)
**Runner cache:** [`logs/runner-cache/plaquette_value_derivation_check_2026_06_10.txt`](../logs/runner-cache/plaquette_value_derivation_check_2026_06_10.txt) (PASS=32, FAIL=0)

## Headline (honest outcome)

This note does not derive `0.5934`. It turns the fuzzy admission "the
canonical plaquette value is an admitted number" into a precisely specified
import-retirement target, by proving three small statements around the exact
object the admission names:

- **Thermodynamic-limit rate.** The infinite-volume value that
  `<P> = 0.5934` stands for is a
  well-defined number, with a *quantitative* finite-volume error bound:
  `|f_L(beta) - f(beta)| <= 6*beta/L` for the per-plaquette free energy, all
  proven from the Haar/Wilson inputs licensed on this surface.
- **Finite-volume bracket interface.** A finite-volume convexity bracket with
  a fully explicit, proven error budget gives the admission B1 of
  [`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md) a declared
  import-retirement route: a certified enclosure of `ln Z_L` at three couplings. The budget is
  then evaluated honestly: a rigorous `0.01`-wide bracket needs `L ~ 3.7e5`.
  This is a route with a price tag, **not a feasibility claim**.
- **KP certificate boundary.** The standard rigorous strong-coupling
  (polymer / Kotecky-Preiss)
  convergence certificate for the Wilson plaquette expansion certifies only
  `beta <= beta_KP ~= 3.08e-4` under the sup-norm activity bound; the
  certificate fails at `beta = 6` by a computed factor `~3.8e5` in activity
  (`~1.95e4` in coupling). So no off-the-shelf convergent-expansion-with-
  remainder route can certify the framework point; what *would* settle the
  value is enumerated precisely in Section 7.

Everything load-bearing is verified by the paired runner with
`[A]/[B]/[C]/[D]` tags (exact rational arithmetic and explicit lattice
enumerations for every counting lemma and constant).

## 1. Declared premises and consumed licenses (one hop)

- **P1 (evaluation surface; admitted).** Gauge group `SU(3)` per oriented
  link on the periodic hypercubic lattice, Wilson single-plaquette action
  `S_W[U; beta] = (beta/3) sum_p (3 - Re Tr U_p)`, compact Haar product
  measure, at the framework coupling `beta = 6`. One-hop authority for the
  finite-surface observable:
  [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  whose license this note uses exactly: the finite `<P>_L(beta)` is a unique bounded observable
  of `Z_L(beta)`, and the canonical value `0.5934` is an **admitted
  comparison/reuse number**, not a value derived there or here. The
  `beta = 6` convention traces to `g_bare = 1` via the Wilson matching
  `beta = 2 N_c / g_bare^2` (file-path pointer only, not a retained one-hop
  authority here:
  `docs/G_BARE_CONSTRAINT_VS_CONVENTION_THEOREM_NOTE_2026-05-03.md`,
  currently `audited_conditional`); this note treats `beta = 6` as a declared
  premise.
- **P2 (coefficient engine; reproven in-runner).** The single-link generating
  function `J(b) = int_{SU(3)} exp((b/3) Re Tr U) dU = sum_n a_n b^n` with
  the order-3 recurrence
  `6(N+1)(N+4)(N+5) a_{N+1} = N(N+1) a_N + 2(2N+3) a_{N-1} + a_{N-2}`,
  seeds `a_0 = 1, a_1 = 0, a_2 = 1/36`. Same engine as
  [`BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md`](BETA6_PLAQUETTE_CERTIFIED_CONVERGENT_BACKBONE_BOUNDED_NOTE_2026-06-04.md)
  (unaudited; cited as cross-check target only). The runner does not trust
  the recurrence: it re-derives `a_3 = 1/648` and `a_4 = 1/2592` from
  independent Haar trivial-rep multiplicities, verifies
  `0 <= a_n <= 1/n!` exactly for `n < 140`, and cross-checks `J(6)` against
  an independent Weyl-measure quadrature.
- **P3 (external mathematical infrastructure; method citation only).** The
  Kotecky-Preiss cluster-expansion convergence theorem (Kotecky-Preiss 1986;
  Friedli-Velenik, *Statistical Mechanics of Lattice Systems*, Ch. 5) and
  the standard connected-subgraph (lattice-animal) counting bound
  `#{connected sets of size n containing a fixed vertex} <= (e*Delta)^n` in
  a graph of maximum degree `Delta`. Both are standard textbook
  infrastructure, used the same way the backbone note uses Mezzarobba's
  certified-evaluation methodology. The KP certificate theorem below uses only the *weaker* animal
  bound `(e*Delta)^n` (the sharper `(e*Delta)^(n-1)` would only enlarge the
  certified domain).

No PDG value, no experimental import, no fitted selector enters anywhere.
The single literature numeral in Section 7 (singularity modulus `~5.7`) is a
`[D]`-tagged comparator recorded from
[`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md)
context, never an input.

## 2. Specification: the exact object the admission names

Fix `beta >= 0`. On the periodic torus `Lambda_L = (Z/L)^4` with `4L^4`
links and `N_P = 6L^4` plaquettes, define

```text
Z_L(beta)  = int prod_p exp(-(beta/3)(3 - Re Tr U_p)) prod_l dU_l ,
f_L(beta)  = (1/(6L^4)) ln Z_L(beta) ,
<P>_L(beta) = 1 + f_L'(beta)            (exact identity, d/dbeta under the
                                         compact integral)
```

The framework plaquette value consumed downstream as B1 is, by
specification,

```text
<P>* := 1 + f'(6),    f(beta) := lim_{L -> infinity} f_L(beta),
```

whenever `f` is differentiable at `6`; in general the well-defined object is
the bracket `[1 + f'(6-), 1 + f'(6+)]` of one-sided derivatives (the
thermodynamic-limit theorem guarantees both exist). The differentiability
caveat is exactly the
no-bulk-transition-at-`beta=6` premise already isolated by
[`SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md`](SU3_BETA6_GAP_BULK_CRITICALITY_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-09.md)
(unaudited; cited as context for the shared premise, not as authority).

This is the *entire* content of the number `0.5934`: nothing else about it
is framework-defined.

## 3. Thermodynamic-limit theorem with an explicit rate

**Thermodynamic-limit theorem.** For every `beta >= 0` the limit
`f(beta) = lim_{L->infinity} f_L(beta)` exists, is convex and nonincreasing
in `beta` with `f(0) = 0`, and for every `L >= 2`

```text
|f_L(beta) - f(beta)| <= 6*beta/L .
```

Consequently one-sided derivatives `f'(beta-) <= f'(beta+)` exist at every
`beta > 0`, they coincide off an at most countable set, and (Griffiths'
convexity lemma) at every differentiability point
`lim_L <P>_L(beta) = 1 + f'(beta)`.

**Proof.** Three elementary lemmas; every counting statement is enumerated
exactly by the runner.

*Lemma L1 (plaquette deletion).* On `SU(3)`, `Re Tr U in [-3/2, 3]`
(critical-point analysis of `cos t1 + cos t2 + cos(t1+t2)`; runner-verified),
so each plaquette Boltzmann factor lies in `[exp(-3*beta/2), 1]` pointwise.
Hence deleting any set `D` of plaquette factors from the integrand changes
`ln Z` by at most `(3*beta/2)|D|`.

*Lemma L2 (torus -> free box).* The torus plaquettes that use at least one
wrapping link number `6L^2(2L-1) <= 12L^3` (enumerated for `L = 2,3,4`).
Deleting them leaves an integrand supported on the embedded free `L`-box
link set; the wrapped links then integrate to `1` under normalized Haar, so
the deleted-torus partition function *equals* the free-box partition
function `Z_L^free`. By L1, `|ln Z_L - ln Z_L^free| <= (3*beta/2)*12L^3`,
i.e. per plaquette `|f_L - f_L^free| <= 3*beta/L`.

*Lemma L3 (block factorization).* Partition the free `(n*l)`-box sites into
`n^4` disjoint half-open `l`-blocks. Plaquettes interior to a block (all
four links intra-block) number exactly `n^4 * 6 l^2 (l-1)^2`; the rest
number `6 n^2 l^2 (n-1)(2nl - n - 1) <= 12 n^4 l^3` (both enumerated for
`(l,n) = (2,2), (3,2), (2,3)`). Deleting the non-interior plaquettes makes
the integrand factorize over the disjoint intra-block link sets — each
factor an independent copy of the free `l`-box — while seam links integrate
to `1`. By L1, with `phi_L := ln Z_L^free / (6L^4)`,

```text
|phi_{n*l} - phi_l| <= (3*beta/2) * 12 n^4 l^3 / (6 n^4 l^4) = 3*beta/l .
```

For any two sides `M, M'`, passing through the common multiple `M*M'` gives
`|phi_M - phi_{M'}| <= 3*beta*(1/M + 1/M')`: the sequence is Cauchy, the
limit `f` exists, and letting `M' -> infinity`, `|phi_M - f| <= 3*beta/M`.
Adding the L2 leg: `|f_L - f| <= 3*beta/L + 3*beta/L = 6*beta/L`. Convexity:
each `f_L` is convex (`f_L'' = Var((1/3) sum_p Re Tr U_p)/(6L^4) >= 0`) and
convexity survives pointwise limits; `f_L' = <P>_L - 1 in [-3/2, 0]` gives
monotonicity; `Z_L(0) = 1` gives `f(0) = 0`. The Griffiths step is the
standard two-line chord argument:
`f_L'(b) <= (f_L(b+t) - f_L(b))/t -> (f(b+t) - f(b))/t -> f'(b+)` as
`t -> 0+`, and symmetrically from below. **QED.**

The rate constant `6*beta/L` is assembled in exact rational arithmetic by
the runner from the two enumerated counting legs. At `beta = 6` it reads
`|f_L(6) - f(6)| <= 36/L`. This is a *surface* bound: it is what the
licensed Wilson/Haar surface proves unconditionally. (True finite-size effects are expected to
be far smaller; making that rigorous needs a proven mass gap with explicit
cluster constants — exactly the open premise of the bulk-criticality note.
A proven exponential bound would replace `6*beta/L` wholesale in the bracket
theorem below.)

## 4. Finite-volume bracket interface for admission B1

**Bracket theorem.** For every `L >= 2` and `0 < delta <= 6`,

```text
1 + [f_L(6) - f_L(6-delta)]/delta - (72 - 6*delta)/(L*delta)
    <= 1 + f'(6-) <= 1 + f'(6+) <=
1 + [f_L(6+delta) - f_L(6)]/delta + (72 + 6*delta)/(L*delta) .
```

If `f_L` at the three couplings is known only through certified enclosures
of half-width `eta`, the outer bounds widen by `2*eta/delta` each.

**Proof.** Convexity of `f` gives
`(f(6) - f(6-delta))/delta <= f'(6-) <= f'(6+) <= (f(6+delta) - f(6))/delta`.
Replace `f` by `f_L` at each of the three points using the
thermodynamic-limit theorem
(`|f_L(b) - f(b)| <= 6b/L` with `b in {6-delta, 6, 6+delta}`) and collect
the worst cases: `(36 + 6(6-delta))/(L*delta) = (72 - 6*delta)/(L*delta)`
on the left, `(36 + 6(6+delta))/(L*delta) = (72 + 6*delta)/(L*delta)` on
the right. **QED.**

**Interface (the point of this note).** Admission B1 of
[`ALPHA_S_DERIVED_NOTE.md`](ALPHA_S_DERIVED_NOTE.md) is thereby given
one declared import-retirement route with a proven error budget: produce certified
enclosures (half-width `eta`) of `ln Z_L` at the three couplings
`{6-delta, 6, 6+delta}` for one explicit `(L, delta)`, and the bracket
theorem returns a *rigorous* two-sided bracket for `<P>*`. No Monte-Carlo confidence
interval, no extrapolation ansatz, no fit enters the bracket.

**Honest budget (runner-verified arithmetic).** The bracket width is

```text
W(L, delta, eta) = [f_L(6+delta) - 2 f_L(6) + f_L(6-delta)]/delta
                   + 144/(L*delta) + 4*eta/delta
                 ~= delta*chi + 144/(L*delta) + 4*eta/delta ,
```

where `chi` is the per-plaquette curvature scale at `beta = 6`. Using the
exactly solvable single-plaquette curvature `chi = (ln J)''(6) = 0.06488`
as the declared proxy and optimizing `delta* = sqrt(144/(L*chi))`
(`eta = 0`), the minimal width is `24*sqrt(chi/L)`, so:

| target rigorous width | required L |
|---|---|
| `0.05` | `~1.5e4` |
| `0.01` | `~3.7e5` |
| `0.002` | `~9.3e6` |

and at the largest committed MC volume (`L = 8`,
[`PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md`](PLAQUETTE_4D_MC_FSS_NUMERICAL_THEOREM_NOTE_2026-05-05.md),
`retained_bounded`) the rigorous bracket is vacuous (width `~2.16` exceeds
the full observable range `3/2`). Since certified (non-MC) evaluation of
`ln Z_L` is already foreclosed at `L = 3` by the treewidth-29 wall
(`docs/SU3_WIGNER_L3_TREEWIDTH_INFEASIBLE_2026-05-04.md`, file-path
pointer), the bracket interface is a *specification with a price tag*, **not a feasibility
claim**. The named upgrade path is a proven lattice-units gap with explicit
constants, which would replace the `6*beta/L` surface rate by an
exponential rate and collapse the required `L` by orders of magnitude; that
is the same open premise carried by the bulk-criticality reduction note.

The runner validates the entire bracket machinery end-to-end on the exactly
solvable proxy surface (where `f` is known in closed form and
`<P>_proxy(6) = J'(6)/J(6) = 0.4225317396...`), including all `2^3` extreme
adversarial perturbations of `f_L` at the proven envelope `+/- 6*beta/L`
(containment must and does survive), a sign-flipped-budget falsification
(must and does break), and a non-convex-input falsification (must and does
be detected).

## 5. KP certificate boundary at beta = 6

**KP certificate theorem.** Write `c_0(beta) = e^{-beta} J(beta)` for the trivial
character coefficient of the plaquette weight and

```text
eps(beta) = sup_{U in SU(3)} | exp((beta/3) Re Tr U)/J(beta) - 1 | ,
```

the sup-norm polymer activity. Let `Delta = 20` be the plaquette
link-adjacency degree in `d = 4` (each of the 4 links is shared with 5
other plaquettes; enumerated exactly by the runner on the `L = 4` torus,
together with "each link lies in exactly 6 plaquettes"). If

```text
eps(beta) <= eps* := 1/(e^2 * Delta * (Delta + 2)) = 3.0758e-4 ,
```

then the polymer expansion of `ln[Z_L / c_0^{N_P}]` (polymers =
link-connected plaquette sets `gamma` with activity
`phi(gamma) = E[prod_{p in gamma} h_p]`, `h_p = w_p/c_0 - 1`, which
factorizes over link-disjoint components and obeys
`|phi(gamma)| <= eps^{|gamma|}` by Hoelder) converges absolutely, uniformly
in `L`, by the Kotecky-Preiss criterion with weight `a(gamma) = |gamma|`:
the one-anchor sum is dominated by
`sum_n (e*Delta)^n (eps*e)^n = q/(1-q)`, `q = e^2*Delta*eps`, and
`(Delta+1) * q/(1-q) <= 1` holds exactly when `eps <= eps*`. On that domain
`f(beta)` is given by a certified convergent expansion with explicit
geometric tail bounds.

**Computed verdict at the framework point (runner, rigorous rational
enclosures for `J`):**

```text
eps(6) = e^6/J(6) - 1 = 116.2267...        (J(6) = 3.4414403549877776)
eps(6)/eps*           = 3.779e5            -> certificate fails at `beta = 6`
certified domain      beta <= beta_KP = 3.0754e-4   (eps(beta_KP) = eps*)
coupling gap          6/beta_KP = 1.951e4
```

**Remark R1 (bounded; forecloses the obvious sharpening).** The crudest
part of the KP certificate theorem is the sup-norm activity. But even granting a hypothetical
sharpened scheme whose per-plaquette activity is as small as the normalized
fundamental character coefficient `u(6) = J'(6)/J(6) = 0.42253` — the
natural floor for plaquette-supported character expansions — the
neighborhood-counting condition gives `u(6) * e * (Delta + 1) = 24.1 > 1`:
any KP-type certificate whose activity is `>= u(6)` fails at `beta = 6` by
at least an order of magnitude. R1
forecloses single-scale cluster certificates only; it says nothing about
multi-scale / renormalization-group (Balaban-class) control, which remains
the named open alternative.

The KP certificate theorem sharpens the "undecided" convergence question recorded in
[`BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md`](BETA6_PLAQUETTE_CLOSURE_NOTE_2026-05-29.md):
the issue is not merely that the empirical ratio estimate (`R ~ 8` from
`d_5..d_11`) is unproven — it is that the entire standard certificate class
fails quantitatively at `beta = 6`, by five orders of magnitude in activity.

## 6. No-Go Discipline Gate for the KP certificate boundary

**Status: PASS for the scoped negative only.** The negative claim is not
"no expansion route can ever reach `beta = 6`." It is only: the standard
single-scale KP/sup-norm certificate, and the same neighborhood-counting
certificate class with activity bounded below by `u(6)`, cannot certify the
Wilson plaquette expansion at `beta = 6`.

- **N1 alternative routes.** Sup-norm KP polymer activity was attempted and
  fails by `eps(6)/eps* ~ 3.8e5`; single-scale neighborhood-counting with
  activity `>= u(6)` was attempted and fails by `u(6)e(Delta+1) ~ 24`;
  certified finite-volume `ln Z_L` bracketing remains open and is the
  positive route in Section 4; an exponential finite-size/gap theorem remains
  open; multiscale/Balaban-class control remains open. The last three are not
  claimed closed.
- **N2 wall independence.** The scoped negative has one wall family:
  single-scale activity-plus-neighborhood KP control. The finite-volume,
  gap/exponential, and multiscale routes are not counted as walls because
  this note explicitly leaves them open.
- **N3 hidden-wall scan.** "Standard," "canonical," and "framework coupling"
  are load-bearing only for the declared Wilson/Haar surface and `beta = 6`
  premise in Section 1; none is used to close the value. The differentiability
  caveat is explicit.
- **N4 residual matching.** The cited closure note residual is the same
  naive/convergent plaquette-expansion route at `beta = 6`; the
  bulk-criticality note is context for the separate finite-size upgrade, not
  evidence for the KP negative.
- **N5 rhetoric audit.** "Cannot reach" means "cannot certify by this
  single-scale KP/neighborhood-counting certificate." It does not mean the
  series diverges, nor that RG or multiscale expansions fail.
- **N6 partial-closure paths.** The legitimate partial-closure path is the
  import-retirement route in Section 4; no new axiom or primitive is requested.
  A proven gap/exponential finite-size theorem would also be a route, not a
  new foundational premise.
- **N7 steelman.** A hostile reviewer should say that the sup-norm activity
  is a crude certificate and that a multiscale expansion, a better character
  organization, or a rigorous finite-size/gap estimate could still reach
  `beta = 6`. This note accepts that steelman and scopes the negative away
  from those routes.
- **N8 cross-cycle echo.** Prior plaquette notes often turned "series route
  undecided" into an admitted-number wall. This note follows the import
  path instead: explicit import, bounded theorem interface, future audit can
  retire the import only after the certified computation or a stronger
  finite-size theorem exists.

## 7. How ALPHA_S_DERIVED_NOTE's B1 can cite this note

B1 remains exactly what it is: `<P> = 0.5934` consumed as an
**admitted comparison/reuse number** under the
[`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
license. This note changes the *shape* of that admission, not its status:

- The specification and thermodynamic-limit theorem give B1 a precise
  referent: a proven-to-exist number `1 + f'(6)`
  (modulo the stated differentiability caveat), rather than "the canonical
  lattice value".
- The bracket theorem gives the admission a declared retirement interface:
  one certified
  three-point `ln Z_L` computation with a proven error budget, with the
  budget honestly priced (`L ~ 3.7e5` for width `0.01` under the
  unconditional surface rate; exponentially less under a proven gap). The
  reduction is a specification, not a feasibility claim.
- The KP certificate theorem certifies that the rival retirement route
  (convergent strong-coupling
  expansion with rigorous remainder at `beta = 6`) is closed at the
  standard-certificate level, so future cycles do not respawn it.

## 8. What would settle the value (precise enumeration)

1. **Certified three-point `ln Z_L` enclosure** at `(L, delta)` per the
   bracket theorem's
   budget. Obstacles, quantified: exact contraction foreclosed at `L = 3`
   (treewidth 29); required `L ~ 1.5e4 .. 9.3e6` for widths `0.05 .. 0.002`
   under the unconditional `6*beta/L` rate.
2. **A proven exponential finite-size bound** (lattice-units gap `m` with
   explicit constants) to replace `6*beta/L` in the thermodynamic-limit and
   bracket theorems — the open premise
   shared with the bulk-criticality reduction note; would collapse item 1's
   `L` to `O((1/m) log(1/width))`.
3. **A radius theorem with effective tail bounds** for the connected
   `Delta(beta)` series past the KP certificate wall: the KP certificate
   theorem proves no single-scale cluster certificate can do this; multiscale
   (Balaban-class) control or a
   genuinely new analytic organization of the exact `d_5..d_11` data would
   be required. (Context comparator, `[D]`-tagged in the runner: the
   recorded literature complex-singularity modulus `~5.7` lies inside the
   `|beta| = 6` disc, so even a true radius statement for the naive
   `beta`-series about the origin would not reach the framework point.)
4. **The `rho_{p,q}(6)` environment vector** (the lane's named open
   object): unchanged by this note; the bracket route is the only route above that
   bypasses it entirely.

## 9. Boundaries and explicit non-claims

- This note **does not derive `0.5934`**, does not certify it, does not
  produce any bracket that contains it, and does not narrow the admitted
  status of B1.
- The thermodynamic-limit rate is a surface bound; no claim that it is sharp.
- The bracket budget's curvature term uses the single-plaquette `chi = 0.06488` as a
  declared proxy for budget arithmetic only; the bracket inequality itself
  never uses it.
- The KP certificate theorem is a *certificate* no-go for the standard
  sup-norm KP route (and, via
  R1, for any single-scale neighborhood-counting refinement with activity
  `>= u(6)`); it does **not** prove the expansion diverges at `beta = 6`,
  and does not foreclose RG-based certificates.
- The differentiability of `f` at `beta = 6` (equivalently, no first-order
  bulk point exactly at the framework coupling) is assumed only where
  `<P>*` is quoted as a single number rather than a one-sided bracket.
- No audit verdict, no status promotion, no edit to any upstream note.

## 10. Verification

Run:

```bash
python3 scripts/plaquette_value_derivation_check_2026_06_10.py
```

Expected result (deterministic, no RNG, runtime under one minute):

```text
Breakdown: A=22 B=3 C=6 D=1
TOTAL: PASS=32 FAIL=0
```

The runner verifies: the exact-rational `J` engine against two independent
Haar-moment values and a Weyl quadrature; the retained
`P_1plaq(6) = 0.422531739649983468...` reproduction; the `Re Tr` range; every
counting lemma of the thermodynamic-limit theorem by explicit lattice enumeration and the exact assembly
of the `6*beta/L` constant; the bracket theorem end-to-end on the exactly
solvable proxy including exhaustive adversarial envelope perturbations and
two falsification legs; the exact `Delta = 20` adjacency enumeration, the
rigorous `eps(6)` enclosure, `beta_KP`, and the KP certificate gap factors; the bracket cost
budget; and the cross-note residuals (`[B]`) plus the single `[D]`
comparator. The admitted `0.5934` appears only in `[B]/[D]` consistency
legs, never as a derivation input.

## 11. Changelog

- **2026-06-10.** Initial note. Specification of the exact object behind
  admission B1; thermodynamic-limit theorem (existence with explicit
  rate `6*beta/L`, convexity, Griffiths corollary); bracket theorem
  (finite-volume convexity bracket giving B1 a declared certified
  three-point `ln Z_L` retirement interface, with honest cost budget); KP
  certificate theorem plus
  remark R1 (rigorous KP-domain certificate `beta_KP ~= 3.08e-4` and
  quantified failure of all single-scale cluster certificates at
  `beta = 6`); paired runner with exact enumerations, rational enclosures,
  adversarial and falsification legs.
