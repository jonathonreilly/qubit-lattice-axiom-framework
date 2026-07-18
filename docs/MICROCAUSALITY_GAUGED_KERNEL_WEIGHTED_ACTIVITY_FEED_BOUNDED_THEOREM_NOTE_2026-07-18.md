---
claim_id: microcausality_gauged_kernel_weighted_activity_feed_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional identification step at FIXED gauge background (axioms supply no dynamics; the one-particle kernel bound is SUPPLIED by the cited CT note on its own surface and is not re-proved here; the CAR algebra and second-quantization conventions are as in the siblings): (F1) the second-quantized bilinear family — pair terms h_{xy} = <x|h[U]|y> c_x^† c_y + h.c. and on-site terms <x|h[U]|x> c_x^† c_x — is even, Hermitian, set-indexed, with ||h_{xy}|| ≤ 2|<x|h[U]|y>| and ||c_x^† c_y|| = 1 (gated in the JW representation); (F2) feeding the supplied kernel bound ||<x|h[U]|y>|| ≤ K e^{−η||x−y||_∞} (K = Const(m,d), η = gamma_CT, BOTH independent of the background U and of the volume — the CT note's own words, needled) through the metric conversion ||z||_1 ≤ 3||z||_∞ and the exact l_∞ shell count 24r^2+2 gives, for every supplied mu < gamma_CT/3, the background-independent common ENVELOPE kappa_U ≤ kappa_bar = K + 8K·x(13+10x+x^2)/(1−x)^3 with x = e^{−(gamma_CT−3mu)} < 1 (numerator identity gated symbolically; the closed form DERIVED via finite-N telescoping identities plus a note-carried limit; the envelope value kappa_bar/K = 585 at x = 1/2 gated alongside the sharper exact-scalar value 293 — 585 is the envelope, not the true activity; scalar fiber declared, matrix fibers named open); (F3) hence the fixed-background BILINEAR dynamics lies in the block07 weighted quasilocal class unconditionally — with the per-background display and the genuinely uniform corollary ||[τ_t^U(A),B]|| ≤ ||[A,B]|| + 2||A||||B|||X|e^{−mu d}(e^{2 kappa_bar|t|}−1) — and the many-body TRANSFER operator itself is covered conditionally on an explicit supplied Gaussian factorization T_MB[U] = C(U)Γ(T_1[U]) (scalar C(U) > 0 is an identity shift dropping from commutators, gated; a review counterexample shows the one-particle kernel alone does not imply the factorization), together taking the fixed-background half of the CT note's open item (iii); (F4) a Z_2 toy-background uniformity exhibit gated by full enumeration (all 8 sign backgrounds of a 3-site chain give identical pair norms, hence identical kappa); (F5) the threshold mu < gamma_CT/3 is the d = 3 instance of the landed free-bilinear note's d·mu < eta pattern (needled). NOT claimed: the U-integrated / gauge-measure statement (open exactly as the CT note states); any re-proof of the Combes-Thomas kernel bound (supplied, with its own provenance and audit status); sharp constants; the spectral/transfer-operator side beyond the supplied kernel bound; the bilinear-equals-many-body-log-transfer identification outside the free/quadratic class (the quadratic identification is the free-sector notes' surface; for non-quadratic transfer operators the theorem is an LR bound for the bilinear dynamics itself, with no identification claimed); nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_weighted_quasilocal_class_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - microcausality_fermionic_even_car_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
  - free_bilinear_quasilocal_lr_bridge_theorem_note_2026-06-10
runner: scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py
---

# Microcausality: Gauged-Kernel Weighted-Activity Feed (Fixed Background)

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional identification step at fixed gauge
background; the one-particle kernel bound is supplied by the cited CT
note (not re-proved); the axioms supply no dynamics.
**Audit-status authority:** independent audit lane only. This note sets
no audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py`](../scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.txt`](../logs/runner-cache/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.txt)

## Purpose

The CT note
[`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
proves a one-particle kernel bound at fixed gauge background —
`|| <x| h[U] |y> || <= Const(m, d) e^{-gamma_CT ||x - y||_inf}` with
"both `gamma_CT` and `Const` independent of the background `U` and of
the volume" — and names its open item (iii): the full many-body
fermionic Lieb-Robinson lightcone needs a separate quasilocal-LR
composition step. The block07 sibling
[`MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md)
now supplies exactly the composition target: an all-time LR bound for
any even-CAR interaction family with finite weighted activity `κ`.
This note is the feed between the two: second-quantize the kernel,
bound the resulting family's `κ` by an exact shell sum, and conclude
that the fixed-background many-body bilinear log-transfer dynamics
satisfies the block07 bound uniformly in the background. That takes the
**fixed-background half** of the CT note's item (iii) **for the
bilinear dynamics unconditionally, and for the many-body transfer
operator itself conditionally on the explicit Gaussian-factorization
hypothesis stated below** — the `U`-integrated / gauge-measure side
remains open exactly as the CT note states it. The `U = 1` scalar
case recovers the same scalar-bilinear applicability pattern as the
landed free-bilinear note (its carrier conventions differ in detail;
no carrier match is claimed); this note's delta is the gauged,
background-uniform case, obtained purely by feeding the supplied
gauged kernel bound through the same shell arithmetic.

## Hypotheses (all supplied, none derived)

The supplied objects: (i) the CT note's kernel bound at fixed
background — `||<x|h[U]|y>|| ≤ K e^{−η||x−y||_∞}` with `K =
Const(m,d)`, `η = gamma_CT`, both independent of `U` and of volume
(cited on that note's own surface, with its own provenance and audit
status; **not re-proved here** — the Combes-Thomas argument is that
note's content); (ii) the CAR algebra and second-quantization
conventions of the fermionic siblings (JW realization as the
computational device); (iii) a supplied `mu` with `0 < mu <
gamma_CT/3`; (iv) the block07 class definition and theorem, cited
where natively gated. The second-quantized family is: for unordered
pairs `{x, y}`, `x ≠ y`:

> `h_{xy} = <x|h[U]|y> c_x^† c_y + <y|h[U]|x> c_y^† c_x`

(Hermitian since the kernel matrix is), and on-site terms
`h_x = <x|h[U]|x> c_x^† c_x`. Every term is **even** (two generators),
so the block07 even-CAR form applies. **What the many-body object
is, precisely (review-sharpened):** the theorem below concerns the
second-quantized BILINEAR `H[U] = Σ_{x,y} <x|h[U]|y> c_x^† c_y` built
from the supplied kernel — unconditionally. The further identification
of this bilinear with the many-body log-transfer generator holds ONLY
under an explicit additional supplied hypothesis, stated as such: a
positive, number-conserving **Gaussian factorization**
`T_MB[U] = C(U)·Γ(T_1[U])` with scalar `C(U) > 0` (then
`−log T_MB = −log C(U)·1 + dΓ(−log T_1)`, and the scalar term is an
identity shift that drops from every commutator — gated). A
one-particle kernel alone does NOT imply the factorization (review
counterexample: `Γ(e^{−h})·e^{−g n_1 n_2}` has the same one-particle
restriction but a quartic log). Without the factorization hypothesis,
only the bilinear theorem is claimed. The kernel here is treated with
a **scalar fiber**; matrix-valued (internal-component) kernels need a
fiber-dimension envelope, named open. The axioms supply no dynamics (needled). Workhorse disclosure: one Opus 4.8 max-effort verification
worker (owner-directed substitution under the workhorse skill) checked
the assembly line-by-line against supervisor ground truth recorded
first in the loop pack; the runner gates everything natively.

## Results

**Term norms and parity (gated in the JW representation).**
`||c_x^† c_y|| = 1` for `x ≠ y` and `||c_x^† c_x|| = 1` (partial
isometries; exact operator norms gated), so by the triangle
inequality

> `||h_{xy}|| ≤ 2 |<x|h[U]|y>| ≤ 2K e^{−η||x−y||_∞}`,  `||h_x|| ≤ K`,

and every term is even and Hermitian (gated).

**Metric conversion and shell count (exact).** On `Z^3`:
`||z||_1 ≤ 3 ||z||_∞` (per-coordinate: each of the three coordinates
is at most the maximum; gated by enumeration with equality attained on
the diagonal), so `e^{mu||z||_1} ≤ e^{3mu||z||_∞}`; and the `l_∞`
sphere `{z : ||z||_∞ = r}` has exactly `(2r+1)^3 − (2r−1)^3 =
24r^2 + 2` points (gated by enumeration at `r = 1, 2, 3`: 26, 98,
218).

**Activity bound (the feed).** For the block07 activity with the `l_1`
ambient diameter, grouping the pair sum by `l_∞` shells and using the
conversion:

> `κ ≤ K + sup_x Σ_{y≠x} ||h_{xy}|| · 2 · e^{mu||x−y||_1}`
> `≤ K + 4K Σ_{r≥1} (24r^2 + 2) x^r`,  `x := e^{−(gamma_CT − 3mu)}`,

(the `4 = 2 × 2`: the Hermitian-pair norm bound times `|S| = 2`), and
with the exact numerator identity
`24x(1+x) + 2x(1−x)^2 = 26x + 20x^2 + 2x^3 = 2x(13 + 10x + x^2)`
(gated symbolically),

> `κ_U ≤ κ̄ := K + 8K · x(13 + 10x + x^2)/(1 − x)^3`,

finite for every `mu < gamma_CT/3` (`x < 1`), where `κ_U` is the true
activity of the background-`U` family and `κ̄` is the **common
envelope**. At `x = 1/2` the envelope evaluates to exactly
`κ̄/K = 585` (gated by a derived closed form plus a
partial-sum-and-tail bracket); the envelope carries deliberate slack —
for a scalar fiber the exact pair norm is `|k|`, not `2|k|`, so the
sharper scalar bound is `1 + 2·146 = 293` (also gated) — `585` is the
value of the stated envelope, not of `κ_U`. Because `κ̄` depends on
the background only through `K` and `gamma_CT` — which the CT note
supplies as `U`-independent — the envelope is
**background-independent**.

**Theorem (fixed-background many-body LR for the gauged bilinear
generator).** For every fixed background `U`, the second-quantized
family above lies in the block07 weighted quasilocal class with the
`κ` bound displayed, so the block07 theorem applies verbatim: for
disjoint `X`, `Y` and all `t`,

> `||[τ_t^{U}(A), B]|| ≤ ||[A, B]|| + 2||A|| ||B|| (n_X^w(U)/κ_U) ·
> e^{−mu d} · (e^{2κ_U|t|} − 1)`
> `≤ ||[A, B]|| + 2||A|| ||B|| |X| · e^{−mu d} · (e^{2κ̄|t|} − 1)`,

the first line with the background's own constants, the second — the
genuinely **uniform corollary** — with the single envelope `κ̄` and
the coarse prefactor `|X|` shared by every background (the zeroth term
vanishing when either observable is even, per the block04
convention). This takes the **fixed-background half** of the CT
note's open item (iii); the `mu < gamma_CT/3` threshold is the
`d = 3` instance of the landed free-bilinear pattern
`0 < d·mu < eta` (needled), and the `U = 1` scalar specialization recovers the same
scalar-bilinear applicability pattern as the landed free-bilinear
note (comparator; carrier conventions differ in detail and no
carrier match is claimed).

**Background-uniformity exhibit (exact, exhaustively enumerated).** On
a 3-site chain with the toy `Z_2`-background kernel
`h[s]_{xy} = s_{xy}·(1/2)^{|x−y|}` (`s_{xy} = s_{yx} ∈ {±1}`,
`s_{xx} = 1`): all `2^3 = 8` sign backgrounds give identical pair
norms `|h[s]_{xy}| = (1/2)^{|x−y|}`, hence identical activity — gated
by full enumeration over backgrounds, with the box activity computed
exactly at `e^{mu} = 9/8` under the note's envelope convention
`||h_{xy}|| ≤ 2|k|` (the exact single-pair norm is `|k|`; using the
envelope consistently makes the exhibit match the theorem's
bookkeeping) (in one dimension `l_1 = l_∞`, so the
exhibit incurs no conversion loss — stated, not hidden). The exhibit
shows concretely what the uniformity claim uses: only the
background-independent envelope of the kernel, never its signs.

## No-Go Discipline Gate

- **N1 route inventory — ATTEMPTED (attacks executed, then the
  residual boundary).** Attacks: (1) hidden Gaussianity — ATTEMPTED
  and CONCEDED into an explicit hypothesis: the review counterexample
  `Γ(e^{−h})e^{−g n_1 n_2}` shows the one-particle kernel does not
  imply the factorization; the factorization is now a named supplied
  hypothesis, with the scalar-`C(U)` commutator drop gated; (2)
  envelope-vs-exact conflation — ATTEMPTED and CORRECTED: `585` is
  the envelope value, the exact-scalar `293` is gated beside it, and
  the toy exhibit gates both conventions (`11/2` envelope, `13/4`
  exact); (3) fake uniformity — ATTEMPTED and CORRECTED: the uniform
  corollary now uses the single envelope `κ̄` with the coarse `|X|`
  prefactor; per-background constants stay per-background; (4) matrix
  fibers — ATTEMPTED and SCOPED OUT: scalar fiber declared, the
  fiber-dimension envelope named open; (5) `l_∞` end-to-end weights —
  ATTEMPTED as a design and REJECTED for family coherence (the
  conversion is a threshold constant, not a shape change). Not
  attempted, not smuggled: the `U`-integrated measure side (CT's own
  sentence needled), re-proving Combes-Thomas, sharp constants, the
  spectral surface beyond the kernel bound.
- **N2 hypothesis independence (pairwise) — ATTEMPTED.** The kernel
  bound (norms only), the Hermiticity of the kernel matrix (term
  Hermiticity only), `mu < gamma_CT/3` (convergence only), and the
  evenness of bilinears (block07's CAR form only) enter at disjoint
  steps; the loop-pack battery flips each runner gate separately.
- **N3 hidden-wall scan — ATTEMPTED.** Conditions surfaced in review
  and now explicit: the Gaussian-factorization hypothesis (for the
  transfer-operator reading), the scalar-fiber declaration (matrix
  kernels need a fiber-dimension envelope, named open), and the
  envelope-vs-true-activity distinction (`κ_U ≤ κ̄`). Also stated:
  the conversion direction with diagonal equality (gated); the
  on-site term carried explicitly; the toy exhibit's one-dimensional
  no-conversion-loss caveat and its envelope convention; the worker
  verification disclosed and graded against ground truth recorded
  first.
- **N4 dependency roles, per citation — ATTEMPTED.**
  - [`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md):
    supplies the kernel bound and its `U`/volume independence (its
    (7) display and independence sentence needled); residual made
    precise in review: its item (iii) concerns the MANY-BODY TRANSFER
    operator — taken here conditionally on the explicit Gaussian
    factorization; the constructed-bilinear half is unconditional;
    the measure side is not touched.
  - [`MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_WEIGHTED_QUASILOCAL_CLASS_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    supplies the class and the LR display this note feeds (its
    theorem heading needled; the display quoted verbatim).
  - [`MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_FERMIONIC_EVEN_CAR_WALK_EXPANSION_LIEB_ROBINSON_BOUNDED_THEOREM_NOTE_2026-07-18.md):
    CAR conventions and the zeroth-term rule (JW norms re-gated
    here).
  - [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md):
    the `U = 1` landed regime and the `d·mu < eta` threshold pattern
    (needled; comparator, not re-proved).
  - [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):
    no-dynamics boundary needle only.
  - Loop-pack worker analysis (`worker_b08_*`): disclosed
    scaffolding; not executed or cited by the runner.
- **N5 rhetoric audit — ATTEMPTED.** "Identification" is scoped to
  the fixed-background kernel-to-class feed; "uniformly in the
  background" means exactly that the bound depends on `U` only
  through the supplied `U`-independent constants; nothing is called
  sharp; the `U = 1` overlap is cited as landed.
- **N6 partial-closure scan — ATTEMPTED.** Closed here: the
  fixed-background half of the CT note's item (iii) (kernel → class
  → LR bound). Still open, named: the `U`-integrated measure side,
  sharp constants (shell counting, the conversion, the pair-bound
  factor), and the spectral/transfer-operator surface beyond the
  supplied kernel bound.
- **N7 steelman (strongest counterarguments, answered) — ATTEMPTED.**
  (a) "The one-particle kernel does not make the many-body transfer
  Gaussian" — CORRECT (review counterexample with a quartic log);
  answered by making the factorization an explicit supplied
  hypothesis and keeping the bilinear theorem unconditional. (b)
  "`585` is the envelope, not the activity" — CORRECT; answered by
  the `κ_U ≤ κ̄` split, the gated exact-scalar `293`, and the
  dual-convention exhibit. (c) "This is just plugging one landed
  note into another." Largely yes — deliberately: the value is that
  the plug is EXACT and background-uniform via `κ̄`, which neither
  landed note states; the CT note's item (iii) names precisely this
  composition as missing. (d) "The conversion factor 3 wastes
  decay." True and stated; sharp constants named open. (e) "The toy
  exhibit is too small to mean anything." It exhibits the LOGIC (the
  bound never reads the signs), not the general statement.
- **N8 prior-wall echo — ATTEMPTED.** The CT note's fixed-background
  scope wall is respected (nothing measure-side is touched); the
  free-bilinear note's `U = 1` scope is extended, not contradicted;
  block07's class hypotheses are satisfied, not modified; no landed
  no-go concerns kernel-to-activity feeds. The family's exhibit-pair
  discipline is repeated (exact instance `585K`; exhaustive
  background enumeration).

**Status: PASS** (all eight items answered; the note is deliberately
narrow — an exact, gated composition of two landed surfaces, claiming
nothing beyond the feed).

## Non-Claims

- Does **not** derive or re-prove the Combes-Thomas kernel bound
  (supplied; its provenance and audit status are the CT note's own).
- Does **not** touch the `U`-integrated / gauge-measure case (open
  exactly as the CT note states it).
- Does **not** claim sharp constants anywhere in the feed (pair
  factor, metric conversion, shell majorization are all envelopes).
- Does **not** address the spectral/transfer-operator surface beyond
  the supplied kernel bound, and does **not** identify the bilinear
  with the many-body log-transfer generator outside the
  free/quadratic class (the quadratic identification is the
  free-sector notes' surface; non-quadratic transfer operators get no
  identification claim here).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains
  required.

## Verification

Primary runner:
[`scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py`](../scripts/microcausality_gauged_kernel_weighted_activity_feed_2026_07_18.py)
— exact throughout. Gate kinds, honestly distinguished: **exact
representation gates** (JW operator norms `||c_x^† c_y|| = 1`;
evenness and Hermiticity of the bilinear terms), **exhaustive finite
gates** (the `l_∞` shell counts 26/98/218; the metric-conversion
enumeration with diagonal equality; the full 8-background `Z_2`
uniformity exhibit with its exact box activity), **symbolic identity
gates** (the numerator identity; the closed-form assembly), **bracket
gates** (the `κ/K = 585` instance at `x = 1/2` by exact partial sum
plus geometric tail), and **presence needles** (the CT note's (7)
display, independence sentence, and item (iii); the block07 class
and theorem heading; the free-bilinear threshold pattern; the axiom
memo — presence checks, not correctness oracles). The gate sequence
is enforced against an ordered label manifest. The runner prints one
`PASS`/`FAIL` line per gate and a final total; the cached transcript
is committed at the path in the header at landing time.
