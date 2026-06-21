# Plaquette beta=6 Perturbative-Derivation Admitted-Input Runner-Local Diagnostic

**Date:** 2026-05-27
**Date of scope repair:** 2026-05-30
**Date of source-boundary demotion:** 2026-06-12
**Date of Wilson-normalization edge repair:** 2026-06-17
**Date of source-boundary non-downstream-licensed scoping:** 2026-06-20
**Type:** no_go source-row label; non-downstream-licensed runner-local
diagnostic only with one source-wired Wilson coefficient edge (no downstream
row may cite this row as a retained or effective-bounded bridge/derivation)
**Claim type:** no_go
**Claim scope:** non-downstream-licensed admitted-input runner-local diagnostic
only (no downstream row may cite this as a retained/effective-bounded
bridge/derivation; the Wilson coefficient relation is dependency-wired, while
the NSPT packet, beta=6 action-surface/physical-selection and `g_bare = 1`
specialization, MC comparator, and F2 comparator required for any promotion
remain unsupplied/open). Given exactly the source-wired Wilson coefficient
relation, the runner-local diagnostic specialization, and the three
runner-local admitted inputs listed below, finite truncations `N <= 16`,
tadpole-improved fixed points `N <= 8`, Pade `[m/n]` resummations with
`m+n <= 12`, and tadpole-improved Pade fixed points with `m+n <= 8` land in
the `<P>_analytic ~ 0.91` band, about 53-55% above the admitted MC comparator.
This conditional arithmetic says nothing about the actual beta=6 plaquette
surface beyond that admitted-input diagnostic comparison. It does not derive
or validate the packet, action-surface selection, `g_bare = 1`, normalization,
or comparators, and it does not rule out strong-coupling, transfer-matrix,
exact Wigner-Racah, Monte Carlo, Borel-conformal, or other non-perturbative
analytic routes.
**Status authority:** independent audit lane only. This source note does not
set or predict downstream status.
**Runner:** [`scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py`](../scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py)
**Cached log:** [`logs/runner-cache/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.txt`](../logs/runner-cache/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.txt)

**Depends on:** [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)

## 2026-06-17 source-side edge repair: Wilson coefficient relation is wired

The Wilson coefficient-matching identity

```text
beta = 2 N_c / g_bare^2
```

is now sourced from
[`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md),
which derives it inside the supplied standard Wilson plaquette action with
canonical `su(N_c)` trace normalization.

This closes only the coefficient-relation sub-edge. It does not derive Wilson
action-surface selection, physical selection of `beta = 6`, `g_bare = 1`, the
NSPT packet, the MC comparator, the F2 comparator, or a reusable
`alpha_bare` authority. The row remains a non-downstream-licensed
runner-local diagnostic.

## 2026-06-20 source-boundary repair: non-downstream-licensed scoping

Prior boundary review named the promotion boundary:

```text
missing_bridge_theorem: for promotion, add retained or effective-bounded
authority for the NSPT coefficient packet, beta=6 Wilson normalization, MC
comparator, and F2 comparator; otherwise keep this row as a
non-downstream-licensed runner-local diagnostic only.
```

This repair takes the second option: keep the row as a
non-downstream-licensed runner-local diagnostic. The later Wilson-edge repair
wires only the coefficient relation; no NSPT packet, beta=6
action-surface/physical-selection authority, `g_bare = 1` authority, MC
authority, or F2 authority is supplied. No downstream retained or
effective-bounded bridge is added; no new axiom, primitive, comparator
authority, or external citation is introduced.

The row is explicitly a **non-downstream-licensed runner-local diagnostic
only.** No downstream row may cite this row as a retained or effective-bounded
bridge or as a derivation of any quantity. The remaining authorities required
*for promotion* are explicitly **unsupplied / open** here:

- the **NSPT coefficient packet** `w_1..w_16` is admitted runner-local only;
  no retained/effective-bounded authority for it is supplied (open);
- the **Wilson coefficient relation** `beta = 2 N_c/g_bare^2` is now
  source-wired to the Wilson small-a theorem, but **Wilson action-surface
  selection**, physical `beta = 6`, `g_bare = 1`, and reusable `alpha_bare`
  authority are not supplied (open);
- the **MC comparator** `<P>_MC = 0.5934` is admitted runner-local only and is
  a fenced residual comparator, never a proof input; no
  retained/effective-bounded authority for it is supplied (open);
- the **F2 comparator** `F2_SCALE_PERCENT = 0.0833%` is admitted runner-local
  only; no retained/effective-bounded authority for it is supplied (open).

Because the remaining promotion authorities are open, this row is **not
promotable** and is **not licensed as a citeable bridge/derivation** for any
downstream row. The only load-bearing content remains the conditional
runner-local diagnostic: given the source-wired Wilson coefficient relation,
the diagnostic specialization, and the admitted local inputs, the tested
finite weak-coupling/tadpole/Pade envelope stays in the `~0.91` band and does
not reach the admitted MC comparator. This conditional arithmetic is not a
`beta = 6` derivation and says nothing about the actual `beta = 6` plaquette
surface or about any non-perturbative route.

The `0.5934` MC value stays fenced as a comparator only; it is never a proof
input, and no comparator number in this note is licensed for downstream reuse.

## 2026-06-15 source-boundary repair: second option elected

This row explicitly elects the second source-boundary option: keep the row as
an admitted-input runner-local diagnostic only. It is not a retained or
effective-bounded authority for the NSPT coefficient packet, beta=6
action-surface/physical-selection claim, `g_bare = 1`, MC comparator, F2
comparator, or the actual beta=6 plaquette surface. The Wilson coefficient
relation is sourced only within the Wilson small-a theorem's stated boundary.

The only load-bearing statement is the conditional runner-local diagnostic:
given the source-wired Wilson coefficient relation plus the local inputs in
`I_PT`, the tested finite weak-coupling/tadpole/Pade envelope stays in the
`0.91` band and does not hit the admitted MC comparator. That conditional
negative result prunes this finite perturbative route only. It does not rule
out strong-coupling,
transfer-matrix, Wigner-Racah, Borel-conformal, Monte Carlo, or any other
non-perturbative route, and it does not license the admitted numbers for
downstream use.

Downstream rows that need a beta=6 Wilson/Haar plaquette value, an NSPT packet,
or a Monte Carlo comparator must cite separate retained or effective-bounded
authority. They cannot cite this row for anything beyond the runner-local
diagnostic over the supplied packet.

No new axiom, primitive, comparator authority, imported value, or downstream
change is introduced.

## 2026-06-12 Source-Boundary Demotion

The source-boundary repair target was:

```text
missing_bridge_theorem: add retained or effective-bounded authority rows for
the NSPT coefficient packet, beta=6 Wilson normalization, MC comparator, and
F2 comparator, or keep this row as an admitted-input runner-local diagnostic
only.
```

The 2026-06-12 repair took the second option. The 2026-06-17 edge repair then
wired one named sub-edge, the Wilson coefficient relation, to a retained
bounded source theorem. No authority is claimed for the remaining NSPT, beta=6
surface-selection, `g_bare = 1`, MC, or F2 inputs; no new import, axiom,
comparator, or audit-status change is introduced. The row remains
source-demoted to the runner-local diagnostic license below.

## 2026-06-12 source firewall: no retained beta=6 surface claim

This packet remains an admitted-input runner-local diagnostic only. The
finite weak-coupling/tadpole/Pade checks are useful route pruning over the
listed supplied packet, but they do not derive the actual `beta = 6`
plaquette surface, do not derive `g_bare = 1`, do not validate the admitted
NSPT or comparator inputs, and do not license any downstream beta=6
Wilson/Haar surface claim.

The repair therefore stops at source-side dependency wiring plus demotion: no
retained/effective-bounded beta=6 surface bridge, new axiom, external
comparator authority, or downstream status is introduced here.

## Admitted Inputs (runner-local diagnostic license)

The runner-local packet is:

```text
I_PT = (source-wired beta*g_bare^2 = 2 N_c relation,
        diagnostic specialization N_c = 3 and beta = 6,
        admitted w_1..w_16, admitted <P>_MC = 0.5934,
        admitted F2_SCALE_PERCENT = 0.0833%).
```

- **NSPT coefficient packet:** the runner consumes
  `<P>(beta) = 1 - sum_{n>=1} w_n / beta^n` with
  `w_1..w_16 = (4/9, 0.20305, 0.16766, 0.18, 0.236, 0.336, 0.510,
  0.806, 1.30, 2.14, 3.59, 6.13, 10.65, 18.78, 33.51, 60.50)`.
  This packet is admitted for THIS diagnostic only, carries no derivation
  weight, and is not licensed for downstream reuse.
- **Wilson normalization edge and beta=6 diagnostic specialization:** the
  runner consumes the relation `beta = 2 N_C / g_bare^2` from
  [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md).
  With the diagnostic specialization `N_C = 3` and `BETA = 6.0`, the runner
  obtains `g_bare^2 = 2 N_C / BETA = 1.0` and, under the standard
  `alpha = g^2/(4 pi)` convention, `alpha_bare = 1/(4 pi)`. This does not
  derive Wilson action-surface selection, physical `beta = 6`, `g_bare = 1`,
  or a reusable `alpha_bare` authority.
- **MC comparator:** the runner consumes `MC_REFERENCE = 0.5934` as a
  residual comparator only. This comparator is admitted for THIS diagnostic
  only, carries no derivation weight, and is not licensed for downstream
  reuse.
- **F2 comparator:** the runner consumes `F2_SCALE_PERCENT = 0.0833%` as a
  scale comparator only. This comparator is admitted for THIS diagnostic
  only, carries no derivation weight, and is not licensed for downstream
  reuse.

Over exactly that repaired boundary, the runner checks that finite truncation,
tadpole fixed points, Pade resummation, and tadpole-Pade combinations stay in
the `<P>_analytic ~ 0.91` band and remain about 53-55% above the admitted MC
comparator. The diagnostic does not assert that the admitted packet or
comparators are repo-authorized values; it only records the arithmetic
consequence if the runner consumes them.

## Scope After Demotion

The obstruction finding is now conditional on the admitted-input packet:
within the tested finite weak-coupling/tadpole/Pade envelope, the best tested
values remain in the `~0.91` band and do not reach the admitted MC
comparator. Nothing in this note claims any fact about the actual beta=6
surface beyond that conditional runner-local comparison.

The residuals named here are open targets for other approaches. In
particular, strong-coupling, transfer-matrix, exact Wigner-Racah,
Borel-conformal, Monte Carlo, and other non-perturbative analytic routes are
not evaluated or excluded by this diagnostic.

## Statement (runner-local admitted-input diagnostic)

Let `BETA = 6` and `N_c = 3` be the diagnostic specialization. The relation
`g_bare^2 = 2 N_c / BETA = 1` is the algebraic specialization of the
source-wired Wilson coefficient matching theorem, while
`alpha_bare = g_bare^2 / (4 pi) = 1/(4 pi)` uses only the standard alpha
notation for the runner's scale diagnostic. This note does not derive the
physical selection of `BETA = 6`, `g_bare = 1`, or a reusable alpha authority.
Let `<P>_MC = 0.5934` be the admitted comparator for this diagnostic (used
only as a residual comparator, never as a derivation input or downstream
value). Let `{w_n}_{n=1..16}` be the admitted coefficient packet of
the Wilson-plaquette perturbative expansion
```text
<P>(beta) = 1 - sum_{n>=1} w_n / beta^n .                              (1)
```
The runner consumes `w_1 = 4/9` and the decimal values listed in the
admitted-input license above. This note does not derive those entries and
does not license them outside this diagnostic.

**Conclusion (T1; truncated series saturation).** The truncated series
in (1) at `beta = 6`, evaluated at every finite truncation order
`N in {1, 2, ..., 16}` using the admitted coefficients listed in the runner,
saturates at
```text
<P>_PT(N=16; beta=6)  =  0.919331 ,                                    (2)
```
with the differences `|<P>_PT(N) - <P>_PT(N=16)|` already below `1e-4`
for `N >= 6`. The truncated PT series is numerically Cauchy-convergent
to the value `~0.9193` at `beta = 6` over the truncation range in which
the admitted coefficients exist; this saturation value is distinct from the
admitted MC comparator by
```text
<P>_PT(N=16) - <P>_MC  =  0.919331 - 0.5934  =  +0.32593                (3)
```
i.e. a 54.9% relative residual.

**Conclusion (T2; tadpole-improvement saturation).** Adopting
Lepage-Mackenzie tadpole improvement, i.e. iterating the
self-consistent fixed point
```text
<P>_(k+1)  =  1 - sum_{n=1..N} w_n / (beta * <P>_k)^n                   (4)
```
to numerical convergence, every truncation `N in {1,...,8}` saturates at
```text
<P>_TI(N=8; beta=6)  =  0.910550 ,                                     (5)
```
with residual
```text
<P>_TI(N=8) - <P>_MC  =  0.910550 - 0.5934  =  +0.31715                 (6)
```
i.e. a 53.4% relative residual. Tadpole improvement reduces the
1-loop value from `0.925926` to `0.910550`, i.e. an absolute shift of
`0.01538` and a `1.66%` relative reduction against the 1-loop value at
`beta = 6`; it does not change the saturation regime.

**Conclusion (T3; Pade resummation saturation).** Pade `[m/n]`
approximants of the truncated series (1) at every `(m, n)` with
`m + n in {2, ..., 12}` evaluate at `beta = 6` to
```text
<P>_Pade[m/n](beta=6)  ~=  0.919331 ,                                  (7)
```
to better than `1e-5` for all `m + n >= 6` in the accepted runner
filter. Pade resummation does not extend the truncated-series
saturation regime inside this finite coefficient packet.

**Conclusion (T4; tadpole-improved Pade saturation).**
Self-consistent iteration of (4) using Pade `[m/n]` approximants in
place of the truncated polynomial in (4) gives accepted values from
`0.910668` down to the best value `0.910550` across the tested `(m, n)`
grid with `m + n in {3, ..., 8}`. From `m+n >= 5`, the accepted runner
values lie within about `2e-5` of `0.910550`; all accepted values remain
in the same `~0.9106` band. No combination of finite-order PT truncation,
tadpole improvement, and Pade resummation tested in the runner brings
`<P>_analytic` within `5%` of the admitted MC comparator.

**Conclusion (T5; finite-route residual and scale diagnostic).** The runner
also records the scale diagnostic
```text
n*  =  1 / (alpha_lat * b_0 / 4)  ~=  4.57                              (8)
```
with the runner's admitted `alpha_lat = 1/(4 pi)` and `b_0 = 11`.
Within the listed 16-term coefficient packet, the numerical minimum of
`|w_n / beta^n|` is much smaller than the residual `(3)`. The runner
therefore records a large finite-route residual and a scale comparison; it
does not prove that the residual is uniquely equal to any matrix element.
The residual exceeds the admitted F2 scale comparator `0.0833%` by roughly
three orders of magnitude.

**Final runner-local estimate.** The best value produced by
any of the combinations tested is
```text
<P>_analytic  =  0.910550        (tadpole-improved [3/2]-Pade, N=5)    (9)
```
with residual `+0.31715` (53.45%) versus the admitted MC comparator.

**Honest verdict.** Inside the supplied finite coefficient packet and tested
method grid, the supplied comparator `<P>_MC = 0.5934` is not reached by
finite-order lattice perturbation theory, tadpole improvement, or Pade
resummation. This diagnostic does not change any other note and does not
close the full non-perturbative derivation problem.

## What this claims

- `(T1)`: given the supplied coefficient packet, the truncated PT series in
  (1) at `beta = 6` saturates at
  `~0.9193`, with residual 54.9% to the admitted MC comparator.
- `(T2)`: given the same supplied packet, the tadpole-improved
  self-consistent fixed point saturates at `~0.9106`, with residual 53.4% to
  the admitted comparator.
- `(T3)`: Pade `[m/n]` resummations of the same series saturate at the
  same `~0.9193` value.
- `(T4)`: combined tadpole-improved Pade resummation saturates at the
  same `~0.9106` value.
- `(T5)`: the finite-route residual exceeds the admitted F2 comparator by
  ~640x, without proving a unique matrix element or importing the F2
  comparator as a reusable value.
- This note does NOT promote `<P>` to derived status and does NOT close any
  framework prediction-chain claim.

## What this does NOT claim

- Does **not** propose a new axiom or framework primitive. The
  perturbative coefficients `{w_n}_{n=1..16}` enter as an admitted
  runner-local packet for this diagnostic only, not as framework primitives
  or retained-grade authorities.
- Does **not** consume the admitted MC comparator `<P>_MC = 0.5934` as a
  derivation input. The admitted MC comparator enters only in the residual
  computation, never as authority on the analytic computation or as a
  downstream-licensed value.
- Does **not** provide retained/effective bounded authority for the NSPT
  coefficient packet, beta=6 action-surface/physical-selection claim,
  `g_bare = 1`, F2 scale comparator, or MC comparator. The Wilson
  coefficient relation is dependency-wired to the retained-bounded small-a
  theorem only inside its stated Wilson-action boundary.
- Does **not** claim a fresh derivation of `<P> = 0.5934`. The
  admitted comparator remains runner-local here.
- Does **not** claim that ALL non-perturbative methods fail. The
  obstruction is restricted to finite-order Wilson-action PT + tadpole
  improvement + Pade. Mean-field self-consistency (M4, framework's
  existing closed-form fan-out), strong-coupling expansion (M2), and
  other non-PT routes are not in scope; they are already covered in
  `SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md`.
- Does **not** introduce new repo vocabulary. Uses existing labels:
  `<P>`, `beta`, `g_bare`, `alpha_bare`, `u_0`, `w_n`, tadpole
  improvement, Pade resummation, and scale diagnostic.
- Does **not** import any external empirical target or fitted selector
  as authority on the analytic computation. The admitted MC comparator is
  only a comparator. The NSPT coefficients are admitted runner-local inputs
  for the finite-packet computation; no entry in the packet is licensed for
  downstream reuse by this note.
- Does **not** promote or demote any other note's status.

## Why this matters

This note records that one finite runner-local attack on `<P>(beta=6)` -
the admitted perturbative coefficient packet plus tadpole improvement plus
Pade resummation - does not reach the admitted comparator inside the tested
finite envelope. The named residual remains an open target for approaches
outside this diagnostic, including strong-coupling expansion, exact
Wigner-Racah transfer, Borel-conformal methods, or another
non-perturbative analytic method.

## Repo-local non-authority pointers

The following repo-local paths are context pointers only. They are not
authority imports for this diagnostic, and they do not license any comparator
number for downstream reuse.

- `PLAQUETTE_SELF_CONSISTENCY_NOTE.md` (finite MC diagnostic) -
  sibling finite-observable context.
- `SU3_WILSON_CLOSED_FORM_FANOUT_THEOREM_NOTE_2026-05-04.md` -
  sibling route-splitting context.
- `GAUGE_VACUUM_PLAQUETTE_BETA6_EVALUATION_SEAM_REDUCTION_SCIENCE_ONLY_NOTE_2026-04-17.md`
  - sibling beta=6 evaluation-context note.
- `ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`
  - sibling tadpole-identity context.

## No-Go Discipline Gate

**N1 alternative routes.** Five tested routes are explicitly in scope over
the admitted packet:
plain 1-loop weak-coupling PT (`0.925926`, 56.04% residual), listed
truncations `N = 1..16` (best `0.919331`, 54.93% residual),
Lepage-Mackenzie tadpole fixed points `N = 1..8` (best `0.910550`,
53.45% residual), Pade `[m/n]` with `m+n <= 12` (best `[3/2]`,
54.93% residual), and tadpole-improved Pade with `m+n <= 8` (best
`[3/2]`, 53.45% residual). Strong-coupling, transfer-matrix,
Wigner-Racah, exact finite-volume, and Monte Carlo routes are named as
out of scope rather than ruled out.

**N2 wall independence.** After the 2026-06-17 edge repair, W2 splits into a
source-wired Wilson coefficient relation and the still-open physical
specialization/surface-selection boundary. W1 the NSPT coefficient packet, W3
the MC comparator, and W4 the F2 comparator remain admitted for this diagnostic
only. The finite method grid is the runner operation over those inputs.
Closing any one admitted input would not close the others, and replacing W3 or
W4 would change only the reported comparison target, not the method values.

**N3 hidden-wall scan.** Phrases such as "standard", "canonical", and
"framework's existing" are treated as context unless they are the listed
coefficient packet, beta=6 specialization/surface-selection boundary, F2
scale, or MC comparator. The Wilson coefficient relation is the one wired
edge; the remaining inputs are explicitly admitted for this diagnostic only.
The MC and F2 values are comparator-only and not licensed for downstream reuse.

**N4 residual matching.** The residual attacked here is only the
`<P>(beta=6)` finite weak-coupling/tadpole/Pade residual to the MC
comparator. Existing plaquette fan-out rows are cited only as sibling
context unless they discuss the same weak-coupling route.

**N5 rhetoric audit.** The negative claim is at the method-grid level,
not at all analytic, all non-perturbative, all strong-coupling, or all
plaquette-derivation resolutions. The source wording is narrowed to the
tested finite envelope.

**N6 partial-closure path scan.** The strong-coupling Padé[3/3] packet,
the coefficient-derivation lane, exact transfer-matrix routes, and
future Wigner-Racah per-cube derivations remain partial-closure paths.
This note does not call them new axioms and does not foreclose them.

**N7 steelman.** A hostile reviewer can correctly argue that the
negative result is not a theorem about the plaquette itself: a
strong-coupling, Borel-conformal, exact character-transfer, or finite
volume Wigner-Racah computation could still derive the MC-compatible
value. That steelman is accepted by scoping this note only to the tested
finite weak-coupling/tadpole/Pade route.

**N8 cross-cycle echo.** Prior plaquette rows already split
weak-coupling, strong-coupling, mean-field, transfer, and MC routes.
This note reuses that split: it records that the tested finite envelope
misses the admitted comparator, not a repo-wide plaquette no-go.

## Verification

```bash
python3 scripts/frontier_plaquette_beta6_perturbative_derivation_2026_05_27.py
```

Expected output:

```text
TOTAL: PASS=39, FAIL=0
```

The runner exercises each conclusion (T1)-(T5) plus framework-side
algebraic constants, scope disclaimers, and the paired-note existence
check. No new axiom is introduced; no MC-value derivation or downstream
reuse license is claimed.
