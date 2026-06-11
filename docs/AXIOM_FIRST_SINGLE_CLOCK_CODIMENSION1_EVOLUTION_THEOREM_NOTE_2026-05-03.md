# Axiom-First Single-Clock Codimension-1 Unitary Evolution on Cl(3) ⊗ Z^3

**Date:** 2026-05-03 (hostile science-fix re-scope 2026-06-11; see §0)
**Type:** bounded_theorem
**Claim scope:** **Axis-conditional single-clock codimension-1 unitary
evolution.** Given the declared evolution-axis premise (B-AXIS) below
and the supplied transfer data of the retained_bounded
reflection-positivity and spectrum-condition rows — the positive
Hermitian two-step blocked transfer `T̂²` with blocked time-step
`2 a_τ` on the staggered fixed-background surface — the framework's
lattice dynamics is a single-clock codimension-1 unitary evolution:
(S1′) the generator `H := -(1/(2a_τ)) log(T̂²/M_T)` is the **unique**
self-adjoint generator (retained finite-dim Stone uniqueness,
transfer-relative and τ-relative) of the unique strongly continuous
one-parameter unitary group `U(t) = exp(-itH)` on the finite block
Hilbert space; (S2′) each lattice time slice `Σ_t = {t} × Z^3` is a
codimension-1 Cauchy surface: the equal-time local algebra is the
mutually commuting tensor product of per-site `M_2(C) ≅ Cl(3,0) ⊗ C`
factors, and slice data propagates with the finite Lieb-Robinson
velocity `v_LR = 2 e J_* D_int R_int` of the retained_bounded cluster
row (L1/L3); (S3′) **the axis is a premise, not a derivation**: the
staggered-Dirac hop operator is *exactly* invariant under the
time-space exchange unitary `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})`
(computed certificate, residual `0`), so RP-admissibility cannot
single out the temporal direction, and the prior revision's S3 claim
("the temporal direction is the unique RP-admissible reflection axis;
hence no second clock") is **withdrawn** as false-as-written. The
"exactly one clock" conclusion holds conditional on (B-AXIS) — one
declared axis/transfer construction (N4), one supplied `τ` (N2), and
no independent commuting clock factor (N5), per the retained
single-clock uniqueness scope boundary. The continuum-limit
identification with a Wightman one-parameter group remains bounded by
the emergent-Lorentz program's `retained_bounded` free-sector scope.
**Status authority:** independent audit lane only. This source note
does not set or predict an audit outcome; audit verdict and effective
status are set only by the independent audit lane.
**Loop:** `3plus1d-native-closure-2026-05-02` (original);
science-fix lane 2026-06-11 (re-scope)
**Runner:** [`scripts/axiom_first_single_clock_codimension1_evolution_check.py`](../scripts/axiom_first_single_clock_codimension1_evolution_check.py)
(`TOTAL: PASS=36 FAIL=0`, deterministic, runtime well under one minute)
**Authority role:** source-note proposal. If retained, this row
supplies the *axis-conditional* single-clock codimension-1 clauses
(S1′)+(S2′) cited by `ANOMALY_FORCES_TIME_THEOREM.md` (its SC premise
row), with the axis-selection content explicitly declared as (B-AXIS)
rather than derived.

## 0. Changelog

- **2026-05-03.** Original version: (S1) Stone evolution, (S2)
  codimension-1 Cauchy slices, (S3) "the temporal direction is the
  unique RP-admissible reflection axis, hence exactly one clock",
  proposed as positive_theorem on A_min (A1–A4 carrier).
- **2026-05-05 audit (archived).** `audited_conditional`,
  chain_closes=false: every one-hop input was unaudited or
  conditional; the A_min carrier's A3/A4 were recategorised as open
  gates. The S1/S2/S3 algebra was ratified as internally coherent
  *as a conditional step* only.
- **2026-05-09.** Upstream-status bookkeeping note added (now
  superseded by this changelog; the cited statuses have since moved).
- **2026-06-11 (hostile science-fix re-scope; the load-bearing
  change).** Three defects repaired:
  1. **S3 withdrawn (critical defect — false as written).** The old
     Step 4 tested only the *unconjugated* temporal RP template
     against spatial reflections: it fixed the time-first staggered
     phase convention `η_τ = 1, η_1 = (-1)^{x_τ}, …` and observed
     that the temporal-hop phase does not flip under `θ_1`. That
     argument quantified over one factorisation template, not over RP
     constructions. In fact the staggered hop operator is *exactly*
     invariant under the axis-exchange unitary
     `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})` (runner block [C-EX],
     residual `0` on a `4×4×2×2` even periodic block, temporal hop
     sector mapped exactly onto the spatial hop sector), so any RP /
     transfer construction about the `τ` axis conjugates by `W` into
     the identical construction about the `x_1` axis. The conclusion
     "no spatial reflection is RP, hence no second clock" therefore
     does not follow — and the broad no-second-clock inference is
     independently denied by the retained
     `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
     (retained_no_go: Stone uniqueness is transfer-relative and
     τ-relative; N2/N4/N5 are extra premises). The old runner's
     T8/T9 were tautologies over the convention labels (`-1 == -1`,
     `+1 != -1`) and its T10 tested a sign-flip criterion that is
     neither necessary nor sufficient for RP; all three are removed.
     S3 is replaced by (S3′): the computed exchange-symmetry
     certificate plus the declared axis premise (B-AXIS).
  2. **S1/S2 re-based on the current retained-grade suppliers.** The
     inline Stone re-proof is replaced by a citation to the retained
     `SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
     (N1–N4); the transfer supply is the retained_bounded RP row's
     two-step blocked `T̂²` (staggered-only, fixed background,
     factorized `A_+^(2)` observables) with the retained_bounded
     spectrum-condition normalization `H = -(1/(2a_τ)) log(T̂²/M_T)`;
     equal-time tensor locality is re-cited from the audited_conditional
     microcausality note to the retained_bounded
     `LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`;
     the finite-speed clause uses the retained_bounded cluster row's
     L1/L3 only, and the old S2(b) spatial-clustering clause is
     demoted to a conditional remark (the cluster row's L2 is
     conditional on a transfer-gap bridge and unconditional spatial
     clustering is explicitly excluded there).
  3. **Claim type bounded, premise declared.** positive_theorem was
     an over-claim: the transfer supply is retained_bounded (2-step,
     staggered-only, fixed background), the clustering clause is
     conditional, and the axis selection is a premise. The note is
     now bounded_theorem with (B-AXIS) declared. The runner is
     rebuilt to compute the load-bearing content with falsification
     legs: the exchange intertwiner (exact, with a no-sign-field
     falsifier), a two-clock tensor-factor comparator whose generator
     span is genuinely 2-dimensional (making the single-clock
     constraint non-vacuous), τ-rescaling (N2 is real), a
     non-Hermitian transfer falsifier, and computed Lieb-Robinson
     cone residuals against the cluster row's bound.

## Scope

`ANOMALY_FORCES_TIME_THEOREM.md` imports its upper bound `d_t ≤ 1`
from this note (its premise row SC). After this re-scope the supplied
content is: **conditional on (B-AXIS), exactly one generator and one
codimension-1 Cauchy slice structure** — i.e. `d_t ≤ 1` holds *given*
that the framework supplies one evolution axis with one transfer
construction and one time step, and admits no independent commuting
clock factor. The axis premise is anomaly-free (it references no
anomaly trace, no chirality content), so the consumer's
non-circularity argument survives in premise-supplied form; what no
longer exists is a derivation of the axis from reflection positivity
alone. The consumer's SC row wording ("the temporal direction is the
unique RP-admissible reflection axis") is stale against this revision
and needs a follow-up edit there.

## Framework objects in use

Current baseline carrier:
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
(Lattice supplies the `Z^3` carrier; Quantum supplies the one-qubit
local algebra per site; Record is not load-bearing here).

- **Per-site algebra.** Each site `x ∈ Z^3` carries the one-qubit
  algebra `M_2(C)`; the retained
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
  identifies `Cl(3,0) ⊗ C ≅ M_2(C) ⊕ M_2(C)` with the two factors
  exchanged by the central element, so the per-site operator content
  is the Pauli realization of the complexified Cl(3).
- **Spatial substrate.** `Z^3` with the cubic graph metric `d(x,y)`,
  used for slices `Σ_t` and for the Lieb-Robinson distance.
- **Euclidean block (supplied surface, not an axiom).** The staggered
  Dirac + Wilson surface `Λ = (Z/L_τ Z) × (Z/L_s Z)^3` enters only
  through the retained_bounded RP/SC supplier rows; its status as a
  gate (not an axiom) is inherited from those rows. No A3/A4 axiom
  status is asserted (the 2026-05-05 audit flagged that carrier as
  superseded; this revision complies).

No fitted parameters. No observed values used as proof inputs.

## Inputs (one hop, with exact licenses)

- **(R-STONE)** — retained positive_theorem
  [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md):
  given finite-dim positive Hermitian `T` with trivial kernel and a
  fixed `τ > 0`, `H_gen = -(1/τ) log(T)` is unique, `U(t) =
  exp(-itH_gen)` is the unique strongly continuous one-parameter
  unitary group with that generator, and `T^n = U(-inτ)` (N1–N4).
- **(R-RP2)** — retained_bounded
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md):
  bounded finite **2-step staggered-only** RP reduction for factorized
  `A_+^(2)` observables on the fixed-background surface; supplies the
  positive Hermitian blocked transfer `T̂²`.
- **(R-SC2)** — retained_bounded
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md):
  with `spec(T̂²) ⊂ (0, M_T]`, functional calculus gives
  `H := -(1/(2a_τ)) log(T̂²/M_T)` self-adjoint with `H ≥ 0`
  (SC1–SC2 after blocked-time normalization; SC3/SC4 conditional
  clauses not consumed here).
- **(R-ET)** — retained_bounded
  [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md):
  raw equal-time commutation and tensor factorization for
  finite-dim tensor factors at distinct sites (dynamics excluded
  there; supplied here by R-CD).
- **(R-CD)** — retained_bounded
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md):
  L1 Lieb-Robinson commutator bound and L3 lattice light cone for
  finite-range Hermitian finite-block Hamiltonians, with
  `v_LR = 2 e J_* D_int R_int`. **L2 spatial clustering is consumed
  nowhere in the theorem** (it is conditional on a transfer-gap
  bridge in that row).
- **(R-CL3)** — retained positive_theorem
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md):
  the per-site complexified Cl(3) algebra classification (2-dim
  irreducible Pauli factors).
- **(G-SCOPE)** — retained_no_go
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md):
  governing boundary. Stone uniqueness is transfer-relative and
  τ-relative; a no-second-clock claim must separately supply N2
  (the time step), N4 (axis/transfer-construction uniqueness), and
  N5 (exclusion of independent commuting transfer factors). This
  note **complies** by declaring those clauses as (B-AXIS) instead
  of deriving them.
- **(B-AXIS)** — **declared premise of this bounded theorem** (not
  derived, not an axiom):
  - (B-AXIS.1) one supplied blocked time step `2a_τ` (= N2);
  - (B-AXIS.2) one declared evolution axis carrying one RP/transfer
    construction, namely the `(T̂², 2a_τ)` supply of (R-RP2)/(R-SC2)
    (= N4);
  - (B-AXIS.3) no independent commuting transfer factor is admitted
    as a second physical clock (= N5).

## Statement

Let `H_blk` be the finite block Hilbert space of the (R-RP2)
reconstruction and `T̂² : H_blk → H_blk` the supplied positive
Hermitian two-step transfer with `spec(T̂²) ⊂ (0, M_T]`. Fix the
blocked time step `2a_τ` (B-AXIS.1) and define
`H := -(1/(2a_τ)) log(T̂²/M_T)` per (R-SC2). Then, **conditional on
(B-AXIS)**:

**(S1′) Single-clock unitary evolution (transfer- and τ-relative).**
By (R-STONE) applied to `(T̂²/M_T, 2a_τ)`: `H` is the unique
self-adjoint generator determined by the supplied transfer data,
`U(t) := exp(-itH)` is the unique strongly continuous one-parameter
unitary group with generator `H`, and the discrete iteration is
consistent at imaginary argument, `(T̂²/M_T)^n = U(-i n · 2a_τ)`.
`H ≥ 0` by (R-SC2). Uniqueness is exactly the (R-STONE) N1/N3
uniqueness: **relative to the supplied `(T̂², 2a_τ)`**. The same
`T̂²` with a different declared `τ` gives a rescaled generator
(G-SCOPE); that is why (B-AXIS.1) is a premise.

**(S2′) Codimension-1 Cauchy slice structure.** Each lattice slice
`Σ_t = {t} × Z^3` (finite block: `{t} × (Z/L_s Z)^3`) carries:

- (a) the mutually commuting equal-time local algebra
  `A(Σ_t) = ⊗_{x ∈ Σ_t} M_2(C)_x` — raw tensor-factor commutation
  and factorization by (R-ET), per-site factor content by (R-CL3)
  on the Quantum-axiom one-qubit carrier;
- (b) codimension 1: `dim(Σ_t) = 3 = dim(Λ) - 1`;
- (c) finite-speed propagation: for finite-range Hermitian `H` the
  Heisenberg evolution obeys the (R-CD) L1 bound
  `‖[α_t(O_x), O_y]‖ ≤ 2‖O_x‖‖O_y‖ exp(-d(x,y)/R_int) ·
  exp(2 J_* D_int e |t|)`, giving the L3 lattice light cone with
  `v_LR = 2 e J_* D_int R_int < ∞`; slice data on `Σ_t` determines
  slice data on `Σ_{t+1}` up to exponentially small tails outside
  the cone.

*Conditional remark (not part of the claim):* spatial factorization
of connected expectations on `Σ_t` (the old S2(b)) holds only
conditionally on the (R-CD) L2 transfer-gap bridge and is not
consumed by any clause above.

**(S3′) Axis selection is a premise; exchange-symmetry certificate.**
The staggered-Dirac hop operator on an even periodic block, in the
time-first Kogut-Susskind convention
`η_τ = 1, η_1 = (-1)^{x_τ}, η_2 = (-1)^{x_τ+x_1},
η_3 = (-1)^{x_τ+x_1+x_2}`, satisfies **exactly**

```text
    W M_KS W^T = M_KS ,   W := P_{τ↔1} ∘ diag( (-1)^{x_τ x_1} ) ,      (1)
```

with `W` orthogonal, where `P_{τ↔1}` relabels `(t, x_1, x_2, x_3) ↦
(x_1, t, x_2, x_3)`. Moreover `W` maps the temporal hop sector
exactly onto the `x_1` hop sector and vice versa,

```text
    W M_τ-hop W^T = M_1-hop ,   W M_1-hop W^T = M_τ-hop ,              (2)
```

and fixes the transverse sectors. (Runner block [C-EX]: residuals are
exactly `0`; the plain permutation without the sign field fails by a
nonzero margin, so the identity is non-trivial.) Consequently the
staggered phase structure does **not** distinguish the temporal axis:
any reflection/transfer construction about the `τ` axis conjugates by
the unitary `W` into the identical construction about the `x_1` axis
(half-spaces, reflection planes, and hop sectors all map onto each
other under `W`). The framework direction is the same: the approved
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
premise sets `c_t = c_s`, which makes the surface *more*
exchange-symmetric, not less. Therefore the single-clock conclusion
cannot be derived from RP-admissibility of the action; it holds
conditional on (B-AXIS), exactly as the retained (G-SCOPE) boundary
requires. A two-clock comparator exists mathematically (two commuting
tensor-factor transfers with a 2-dimensional generator span; runner
block [C-2CLK]) and is excluded only by (B-AXIS.3) — the premise
excludes something realizable, so it is non-vacuous and load-bearing.

Statements (S1′)–(S3′), conditional on (B-AXIS), constitute the
framework's **axis-conditional single-clock codimension-1 unitary
evolution theorem**.

## Derivation

**Step 1 (S1′).** (R-RP2) supplies `T̂²` positive Hermitian on the
finite-dim `H_blk`; (R-SC2) supplies the normalization
`T := T̂²/M_T` with `spec(T) ⊂ (0, 1]` and trivial kernel. The
hypotheses of (R-STONE) — finite-dim, Hermitian, positive, trivial
kernel, `‖T‖_op ≤ 1`, fixed `τ = 2a_τ` — are met, so its N1–N4 apply
verbatim: unique `H`, unique group `U(t)`, consistency
`T^n = U(-inτ)`. `H ≥ 0` is (R-SC2) SC2. No content beyond the two
cited rows plus functional calculus is used. ∎

**Step 2 (S2′).** (a) is (R-ET)'s raw tensor-factor commutation and
factorization applied to the per-site factors, whose algebra content
is fixed by (R-CL3) on the one-qubit carrier. (b) is arithmetic.
(c) is (R-CD) L1/L3 applied to the finite-range Hermitian `H`: the
weighted-path Duhamel estimate gives the exponential cone bound with
`v_LR = 2 e J_* D_int R_int`. The runner computes the actual
commutator residuals on a finite-range block Hamiltonian and verifies
the L1 bound with explicit margins, plus genuine inside/outside-cone
contrast so the cone is not vacuous. ∎

**Step 3 (S3′).** Equation (1) is verified exactly: for the
transposition `τ↔1`, the sign field `ε(x) = (-1)^{x_τ x_1}`
intertwines the KS phases,

```text
    η_{Pν}(Px) · ε(x) · ε(x + ν̂)  =  η_ν(x)     for all sites x, ν,    (3)
```

(case check: `ν = τ`: `(-1)^{x_1} · (-1)^{x_1} = 1 = η_τ`;
`ν = 1`: `1 · (-1)^{x_τ} = η_1`; `ν = 2, 3`: `ε` cancels and the
relabelled phase reproduces `η_ν`), so the substitution
`χ_x → ε(x) χ_{Px}` maps the staggered action to itself; the mass
term is `ε²`-invariant and the Wilson plaquette is hypercubic
invariant. Hence any RP factorisation `⟨Θ_τ(F) F⟩ ≥ 0` over the
`τ ≥ 0` half-space algebra conjugates to
`⟨Θ_1(W F W^†) (W F W^†)⟩ ≥ 0` over the `x_1 ≥ 0` half-space algebra:
the `x_1` axis admits the identical construction. The old Step 4
tested only whether the *unconjugated* temporal template transfers
verbatim (it does not — `η_τ` does not flip under `θ_1` in the fixed
convention), which shows nothing about conjugated constructions; its
conclusion is withdrawn. What survives is: per declared axis and
supplied `(T̂², 2a_τ)`, the clock is unique (Step 1); selecting the
axis, the `τ`, and excluding commuting factor clocks is (B-AXIS). ∎

## Consistency with retained no-gos (declared, checked)

- **`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
  (retained_no_go).** This revision asserts nothing that row denies:
  uniqueness is stated transfer-relative and τ-relative; N2/N4/N5
  appear verbatim as (B-AXIS.1–3) declared premises. The prior
  revision's S3 violated its N4/N5 discipline and is withdrawn.
- **`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`
  (retained_no_go).** No SO(4)/continuum-isotropy wording is claimed
  from spatial cubic checks; the continuum corollary stays bounded by
  the emergent-Lorentz row. Where that row notes `c_t = c_s` is an
  extra premise now supplied by the kinetic-isotropy primitive, this
  note only *uses* the direction of that premise (exchange symmetry),
  never its converse.
- **`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`
  (retained_no_go).** Nothing here derives a physical boost action
  from the local algebra: (S1′) concerns the single time-translation
  group only; boosts/Lorentz enter only through the bounded continuum
  corollary, which carries that program's own bounded status.

## Continuum-limit corollary (bounded, unchanged in kind)

The identification of `U(t)` with the Wightman one-parameter group of
a relativistic continuum QFT is **not** part of (S1′)–(S3′); it is
bounded by the emergent-Lorentz program
([`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
retained_bounded free-sector structural dispersion scope only). The
ultrahyperbolic well-posedness obstruction for `d_t > 1`
(Craig-Weinstein 2009; Tegmark 1997) remains an external
classical-PDE result consumed, if at all, by the downstream consumer,
not here.

## Downstream contract (what may be cited)

For `ANOMALY_FORCES_TIME_THEOREM.md` (premise row SC):

- citeable now: **conditional on (B-AXIS), exactly one generator `H`
  of one strongly continuous unitary group, and codimension-1 Cauchy
  slice structure with finite `v_LR`** — i.e. the `d_t ≤ 1` cap in
  axis-conditional form. (B-AXIS) references no anomaly content, so
  the consumer's non-circularity separation (time defined upstream of
  the anomaly argument) is preserved in premise-supplied form.
- no longer citeable: "the temporal direction is the unique
  RP-admissible reflection axis of the staggered-Dirac action" and
  any unconditional "no second clock" wording. The consumer's SC row
  text predates this re-scope and needs a follow-up edit.

## Relation to the retained Stone narrow row

`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`
is consumed, not duplicated: the old inline Steps 1–2 re-proved its
N1–N4 content and are deleted in favor of the citation. This note
adds, beyond that row: the identification of its abstract `T` with
the (R-RP2)/(R-SC2) supplied `T̂²/M_T` (Step 1), the (S2′) Cauchy
slice structure (Step 2), and the (S3′) exchange-symmetry boundary
with the declared (B-AXIS) premise (Step 3). It contradicts nothing
in that row.

## Honest status

**Bounded theorem.** (S1′) closes from retained/retained_bounded
one-hop inputs given the declared premise; (S2′) closes at the
retained_bounded level of its suppliers; (S3′) is a computed exact
certificate plus a declared premise. Not positive_theorem: the
transfer supply is bounded (2-step, staggered-only, fixed
background), the clustering clause is conditional and excluded from
the claim, and the axis selection is a premise by the retained
(G-SCOPE) no-go.

The runner computes the load-bearing content: supply-hypothesis
residuals for (R-STONE) on a concrete finite-range block transfer;
Stone reconstruction and group-law residuals; τ-rescaling (N2
load-bearing); a non-Hermitian-transfer falsifier; equal-time tensor
locality and codimension arithmetic; Lieb-Robinson cone residuals
against the (R-CD) L1 bound with inside/outside contrast; the exact
exchange intertwiner (1)–(2) with a no-sign-field falsifier; and the
two-clock tensor-factor comparator (2-dimensional generator span,
excluded only by B-AXIS.3).

**Honest claim-status fields (audit-lane handoff):**

```yaml
proposed_claim_type: bounded_theorem
proposed_claim_scope: |
  Axis-conditional single-clock codimension-1 unitary evolution.
  Conditional on the declared premise B-AXIS (one supplied blocked
  time step 2a_tau; one declared evolution axis carrying the
  retained_bounded RP/SC two-step transfer supply T_hat^2; no
  independent commuting transfer factor admitted as a second clock),
  the retained finite-dim Stone row gives the unique generator
  H = -(1/(2a_tau)) log(T_hat^2/M_T) >= 0 and the unique strongly
  continuous one-parameter unitary group U(t) = exp(-itH); each
  lattice slice Sigma_t is a codimension-1 Cauchy surface with
  mutually commuting per-site M_2(C) tensor-product equal-time
  algebra and finite Lieb-Robinson propagation (cluster row L1/L3).
  The prior S3 claim that the temporal direction is the unique
  RP-admissible reflection axis is withdrawn: the staggered hop
  operator is exactly invariant under the time-space exchange
  unitary W = P_{tau<->1} diag((-1)^{x_tau x_1}) (computed, residual
  0), so axis selection is a premise, consistent with the retained
  single-clock uniqueness scope boundary (N2/N4/N5). Continuum
  Wightman identification stays bounded by the emergent-Lorentz
  program.
proposed_load_bearing_step_class: A (algebraic closure of the
  retained Stone row over the retained_bounded transfer supply,
  conditional on the declared B-AXIS premise; the S3' exchange
  certificate is a class-C computed fact consumed as a boundary).
status_authority: independent audit lane only
actual_current_surface_status: support
conditional_surface_status: bounded theorem on retained +
  retained_bounded one-hop inputs + declared premise B-AXIS
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: true
proposal_allowed_reason: |
  Every load-bearing input is retained or retained_bounded on the
  current surface; the one previously-cited audited_conditional
  input (microcausality 2026-05-01) is no longer consumed. The
  single non-derived ingredient is the declared B-AXIS premise,
  required by the retained scope-boundary no-go. No new axiom, no
  fitted parameter, no observed value.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

**Not in scope.**

- Any unconditional no-second-clock / unique-RP-axis claim (withdrawn;
  see §0 and S3′).
- Spatial clustering on `Σ_t` (conditional L2 of the cluster row; not
  consumed).
- Continuum Osterwalder-Schrader / Wightman reconstruction (bounded
  by the emergent-Lorentz program).
- The ultrahyperbolic `d_t > 1` well-posedness obstruction (external,
  consumer-side).
- Deriving the (B-AXIS) premise itself. Candidate future suppliers:
  a Record-axiom registration-direction theorem, or a
  boundary-condition (antiperiodic temporal BC) selection row; either
  would be a separate note.

## Citations

- baseline carrier: [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Stone core (retained): [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md)
- transfer supply (retained_bounded):
  [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md),
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- equal-time tensor locality (retained_bounded):
  [`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md`](LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md)
- Lieb-Robinson cone (retained_bounded, L1/L3 only):
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- per-site Cl(3) algebra (retained):
  [`AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CL3_PER_SITE_UNIQUENESS_THEOREM_NOTE_2026-04-29.md)
- governing boundaries (retained_no_go):
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  [`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md),
  [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md)
- kinetic-form premise context (meta, approved premise):
  [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
- continuum bound (retained_bounded):
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- downstream consumer (cross-reference only, not a dep):
  `ANOMALY_FORCES_TIME_THEOREM.md` (premise row SC)
- standard external references (theorem-grade, no numerical input):
  Stone (1932) *Ann. Math.* 33, 643; Streater-Wightman (1964) ch. 3;
  Osterwalder-Schrader (1973) *Comm. Math. Phys.* 31, 83;
  Sharatchandra-Thun-Weisz (1981) *Nucl. Phys. B* 192, 205;
  Menotti-Pelissetto (1987) *Comm. Math. Phys.* 113, 369;
  Golterman-Smit (1984) staggered lattice rotation symmetry
  (context for the axis-exchange field redefinition);
  Craig-Weinstein (2009) *Proc. Roy. Soc. A* 465, 3023; Tegmark
  (1997) *Class. Quant. Grav.* 14, L69 (both consumer-side only).
