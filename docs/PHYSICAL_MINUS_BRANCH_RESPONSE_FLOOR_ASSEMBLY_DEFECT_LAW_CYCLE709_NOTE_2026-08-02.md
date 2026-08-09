# The minus-branch response floor tracks the solve image of the measured Hessian-assembly equivariance defect, on two box sizes — Cycle 709

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

Supplied inputs: the landed Cycle-696 compiler and its landed constants, used
verbatim and never re-implemented. There is no measured, fitted, or literature
constant imported by this cycle.

**Primary runner:**
`scripts/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02.py`;
cached stdout
`logs/runner-cache/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02.txt`;
paired receipt
`outputs/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02_receipt_2026-08-02.json`.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "cycle 707 left the response-stage minus-branch floor constant and its L-scaling as named next paths; this note supplies measured structure for both at two box sizes, and does not retire either"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "the downstream consumer is the same lane's endpoint-floor work, which would carry this attribution through cycle 707's amplitude product identity; whether it does is not settled here. First obligations: a symbolic proof of exact-arithmetic assembly equivariance Pi^T Q Pi = Q, an a-priori remainder bound for the first-order expansion, and an entrywise account of E's magnitude"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "The two-term decomposition of the response-stage transport defect and the first-order law relating its commutator term to the assembly defect E are exact algebra for the stored linear response operator, and are measured on two constant-sign witness frames at L = 3 and L = 7 through the imported cycle-696 compiler. Everything causal is DIAGNOSIS, not proof: the exact-arithmetic equivariance premise Pi^T Q Pi = Q is argued structurally and not proved symbolically; the step sweep is a five-sample direction measurement over one decade, not an exclusion of other mechanisms; and the size attribution is bounded by what was measured, namely that the maximum local entry of E is size-independent while E's global measures and the response amplification both grow. No route-exhaustion, no mechanism exclusion, and no arbitrary-size claim is made."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the algebra is exact for the stored operator but every physical number is a finite measurement on two witness frames at two box sizes through an imported audit-excluded compiler, so the note is bounded support rather than a positive theorem"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Result

Cycle 707 measured that the all-minus constant-sign transport defect of the
compiled source-response chain first resolves at the `b -> eps` solve, and named
the response-stage floor constant and the `L`-scaling of the branch floors as
next paths. This cycle measures structure behind that floor one stage earlier
than the solve, and states the solve's role exactly for the stored operator.

1. **The response-stage transport defect splits into two floating terms**,
   `d_eps = term1 + term2`, with `term1 = eps_of(db)` (the solve image of the
   load-stage roundoff) and `term2 = eps_of(push(b0)) - push(eps0)` (the
   solve/permutation commutator). The split closes at `<= 3.0e-15` in every
   branch-size cell. On the all-minus branch `term1` contributes a `1.2e-04`
   (`L = 3`) and `2.2e-05` (`L = 7`) fraction of the floor, so the floor is the
   commutator term to within that measured fraction. The split is separately
   established as resolvable on the minus branch: deleting either term from the
   live comparison raises the residual by a gated factor (Claim 3). On the plus
   branch `term1` sits at the closure residual itself, so there the split is
   reported as unresolved rather than claimed.

2. **The commutator tracks the first-order solve image of a Hessian-assembly
   equivariance defect.** Define `E := Pi^T Q Pi - Q`, the failure of the
   assembled static Hessian to commute exactly with the frame's dof relabeling.
   In exact arithmetic `E = 0` under the structural argument of the derivation
   sketch, which is not proved symbolically here. In floating point the all-minus
   branch measures `dQ = |E|_max = 1.2e-10` — the same value at `L = 3` and
   `L = 7` — while the all-plus branch measures `7.1e-15`, a branch separation of
   `1.8e+04`. The zero-parameter first-order law

   `term2 ~= push(eps_of(E @ eps0))`

   reproduces the minus floor with relative residual `3.2e-04` (`L = 3`) and
   `5.5e-04` (`L = 7`) at cosine `1.0e+00`, and fails on the plus branch, where
   `E` is at summation noise (residuals `9.6e-01` and `9.8e-01`).

3. **Over the sampled step decade the defect moves in the roundoff direction,
   and the floor's size growth has two measured contributions.** Under a
   five-sample step sweep at `L = 3` the minus-branch defect decreases strictly
   monotonically as the finite-difference step grows, which is the direction a
   rounding term takes and the opposite of the direction the central-difference
   truncation term takes. That is a direction measurement on the sampled decade;
   it is diagnosis, and it excludes no other mechanism. Between the two sizes the
   MAXIMUM LOCAL ENTRY of `E` is unchanged (ratio `1.0e+00`), but `E`'s global
   measures are not: `|E|_F` grows by `4.6e+00`, its nonzero count by `2.1e+01`,
   and the load-specific forcing `|E eps0|_2` by `4.6e+00`. Meanwhile the softest
   regular eigenvalue softens by `4.3e+01` and the floor grows by `2.2e+01`. The
   response is therefore a substantial contributor to the growth, and the growth
   is NOT assigned to it alone.

The floor cycle 707 measured is therefore accompanied here by measured structure:
a localized, step-dependent assembly object whose solve image reproduces the
floor at both sizes with no fitted parameter. That is support for a mechanism,
not a closed derivation of the floor constant.

## Setup

All measurements run the landed chain of the
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
used verbatim and never re-implemented, at `L = 3` and `L = 7` (open box,
`wrap = False`):

`build_domain -> rho_vector -> b = rho @ G -> sector_solve -> response -> eps`

with the centered single-edit source domain (label `5` on the central edge
`(A,A,A) -> (A+1,A,A)`, `A = (L-1)//2`). This cycle's chain stops at the
response `eps`; no amplitude, metric, or endpoint stage is exercised.

Frame action: for a proper cubic rotation `h` about the box center, the site map
is the compiler's `frame_site_map`, and the induced dof transport `m` sends the
undirected spatial edge `(class, base)` to its image edge canonicalized to the
low corner (direction `|R v|`, base `g(x) + min(R v, 0)`). The transport is
verified bijective at both sizes. `Pi` denotes the corresponding permutation
operator, `push(v)[m[i]] = v[i]`, and `u` denotes the float64 unit roundoff for
round-to-nearest, `2^-53`. The runner computes it as `np.finfo(float).eps / 2`,
because `np.finfo(float).eps` is the spacing from 1 to the next representable
double, `2^-52` — twice the unit roundoff. Every `u`-scaled quantity below uses
`2^-53`. The decade-level statements that use `u` are insensitive to that factor
of two; the correction is a definition matter, not a change of conclusion.

Witnesses: the constant-sign census of the 24 proper frames is `3` all-plus
(including the identity) and `3` all-minus, with `18` mixed. Following the
branch degeneracy measured by cycle 707, one witness per constant-sign branch is
probed: `g = 15` (all-plus 3-cycle) and `g = 1` (all-minus).

Defect diagnostics, per branch and size, all max-abs and componentwise under the
transport: `drho` (source stage), `db` (load stage, `db := b_h - push(b0)`),
`d_eps` (response stage, `d_eps := eps_of(b_h) - push(eps0)`); the assembly
equivariance defect `E := Pi^T Q Pi - Q`, entrywise
`E[i,j] = Q[m[i], m[j]] - Q[i,j]`, with `dQ := |E|_max`; the global measures
`|E|_F`, the nonzero count of `E`, and the load-specific forcing `E eps0` in
2-norm and max-norm; and the decomposition terms `term1 := eps_of(db)`,
`term2 := eps_of(push(b0)) - push(eps0)`.

### Declared inputs and read inventory

The runner declares `AUDIT_INPUT_PATHS` naming the cycle-696 compiler and the four
`scripts/` modules it imports transitively, so the runner cache pins their bytes
and rejects drift. Those five files are the only external or ancestral scientific
input read: every physical number below is computed through them, and no sibling
cycle's measured value is read or copied in. The runner's only package-local write
is its paired receipt under `outputs/`; it performs no self-hash or
receipt-verification integrity read. Its declared audit timeout is
`AUDIT_TIMEOUT_SEC = 600`, which is the number the cache header carries.

Backend sensitivity, disclosed: the plus-branch and solve-residual values at
bit-noise scale depend on the BLAS/LAPACK backend. Repeat runs on one host
reproduce byte-identically, but a different backend moves those cells within their
gate bands. The numbers quoted throughout are those of the cached run named above.

## Imported compiler contract

The compiler constants consumed by this cycle's chain segment, all landed and
none re-measured here: the landed local energy selection `F_17` with the
centered lift; the source scale `SRC_SCALE = 0.17` and the barycentric
source-row convention; the edit label `5`; the open box; the central
finite-difference assembly step `1.0e-4` (the step sweep re-assembles at the
stated multiples `0.25, 0.5, 1.0, 2.0, 4.0` of it); the null cut `1.0e-8`,
under which `null_dim = 0` at both sizes, so the regular sector is the full
space and the computed response operator is the full inverse; and the response
solve itself. The downstream metric and endpoint machinery of the compiler
(principal square root, positivity margin, amplitude dial) is not exercised.
There is no measured, fitted, or literature constant imported by this cycle.

## Claims

### Claim 1 — Scope, witnesses, and solver scope

All 24 frames have determinant `+1`; the constant-sign census is `3 + 3` of 24;
the dof transport is an explicit bijection at both sizes; `null_dim = 0` at both
sizes, so no null projection enters any measurement below.

| `L` | `n_dof` | `null_dim` | `lam_min` | `\|w\|_max` | `\|eps0\|_2` |
|-----|---------|------------|-----------|-------------|--------------|
| 3   | 98      | 0          | `4.7e-01` | `6.3e+01`   | `9.7e+00`    |
| 7   | 1854    | 0          | `1.1e-02` | `6.6e+01`   | `2.4e+01`    |

### Claim 2 — Upstream transport is exact at the source and summation-level at the load

`drho = 0.0e+00` in all four branch-size cells: the source stage is bit-exact
under transport, as it never touches the assembled Hessian. The load stage
carries only summation-level roundoff from the contraction with `G`: plus
`4.4e-15` / `3.1e-15`, minus `2.1e-14` / `1.1e-14` (`L = 3` / `L = 7`). Neither
upstream stage carries a branch floor at the measured scales.

### Claim 3 — Two-term decomposition of the response defect, with live rejectors

| branch, `L` | `d_eps`   | `term1`   | `term2`   | closure   | closure if `term1` deleted | closure if `term2` deleted |
|-------------|-----------|-----------|-----------|-----------|-----------------------------|-----------------------------|
| plus, 3     | `1.2e-14` | `1.3e-15` | `1.1e-14` | `7.8e-16` | `1.6e-15`                   | `1.1e-14`                   |
| minus, 3    | `6.9e-11` | `8.2e-15` | `6.9e-11` | `1.2e-15` | `8.4e-15`                   | `6.9e-11`                   |
| plus, 7     | `1.1e-12` | `2.7e-15` | `1.1e-12` | `1.1e-15` | `3.1e-15`                   | `1.1e-12`                   |
| minus, 7    | `1.5e-09` | `3.4e-14` | `1.5e-09` | `3.0e-15` | `3.4e-14`                   | `1.5e-09`                   |

The identity `d_eps = term1 + term2` is algebraic for a linear response map; the
closure gate certifies the solve's floating linearity at the working scales
(`<= 3.0e-15` in every cell), so the split is a valid decomposition of the
measured defect, not a physics claim by itself.

The last two columns are the runner's live wrong-value rejectors: what the same
comparison returns when either term is removed from the decomposition. Deleting
`term2` is rejected in every cell against a declared factor of `1.0e+01`, at
measured ratios `1.4e+01`, `5.8e+04`, `1.0e+03`, and `5.1e+05`. Deleting
`term1` is rejected on the minus branch by `7.1e+00` (`L = 3`) and `1.1e+01`
(`L = 7`), and the closure sits at `1.5e-01` and `8.8e-02` of `term1` there, so
`term1` is resolvable above the linearity residual. On the plus branch it is not:
deleting `term1` moves the residual by only `2.0e+00` and `2.7e+00`, i.e. `term1`
sits at the closure residual itself. The runner gates that honest converse rather
than claiming a resolution it does not have.

On the minus branch the ratio `term1 / term2` is `1.2e-04` (`L = 3`) and
`2.2e-05` (`L = 7`): the load-stage roundoff does not drive the floor in the
measured cells, and the floor is the commutator term to within that fraction.

### Claim 4 — The assembly equivariance defect: branch dichotomy and what is and is not size-independent

| branch | `dQ` at `L = 3` | `dQ` at `L = 7` | size ratio |
|--------|-----------------|-----------------|------------|
| plus   | `7.1e-15`       | `7.1e-15`       | —          |
| minus  | `1.2e-10`       | `1.2e-10`       | `1.0e+00`  |

The branch separation is `1.8e+04` at both sizes. The MAXIMUM ENTRY of the
minus-branch defect is the same at `L = 3` and `L = 7`, which says the largest
single stencil discrepancy does not grow with the box. It does not say the
assembled defect operator is size-independent, and the measured global quantities
say it is not:

| minus-branch measure of `E` | `L = 3`   | `L = 7`   | ratio     |
|-----------------------------|-----------|-----------|-----------|
| `\|E\|_max`                  | `1.2e-10` | `1.2e-10` | `1.0e+00` |
| `\|E\|_F`                    | `1.5e-09` | `7.0e-09` | `4.6e+00` |
| nonzero entries             | `740`     | `15660`   | `2.1e+01` |
| `\|E eps0\|_2`               | `1.2e-09` | `5.4e-09` | `4.6e+00` |
| `\|E eps0\|_max`             | `4.7e-10` | `6.3e-10` | `1.3e+00` |

So `E`'s entries are local — the largest one is box-independent — while its
support and its load-specific forcing both grow with the box. Claim 7 uses the
full table, not the max entry alone.

### Claim 5 — Zero-parameter first-order law

Prediction: `term2 ~= push(eps_of(E @ eps0))`, with `E` measured from the
assembled operator itself, `eps0` the base response, and `eps_of` the landed
solve — nothing fitted.

| branch, `L` | rel. residual | cosine     |
|-------------|---------------|------------|
| minus, 3    | `3.2e-04`     | `1.0e+00`  |
| minus, 7    | `5.5e-04`     | `1.0e+00`  |
| plus, 3     | `9.6e-01`     | `2.9e-01`  |
| plus, 7     | `9.8e-01`     | `4.8e-01`  |

The plus rows are a built-in wrong-regime rejector: there `E` sits at summation
noise, the first-order image is sub-noise, and the law is required to fail — and
does. On the minus branch the absolute residual (relative residual times floor)
lands at the plus-branch floor scale of the matching size — compare
`3.2e-04 x 6.9e-11 = 2.2e-14` with `1.2e-14`, and `5.5e-04 x 1.5e-09 = 8.3e-13`
with `1.1e-12` — so on these two cells the law accounts for the minus floor down
to the pipeline's own bit noise. Two branches at two sizes is the whole evidence
base for the law; nothing here says it holds for other frames or other sizes.

### Claim 6 — Measured step direction over the sampled decade, and scale consistency

Re-assembling at `L = 3` on the stated step multiples:

| step      | `\|E_minus\|_F` | `\|E_plus\|_F` |
|-----------|-----------------|----------------|
| `2.5e-05` | `9.8e-09`       | `5.0e-15`      |
| `5.0e-05` | `2.0e-09`       | `0.0e+00`      |
| `1.0e-04` | `1.5e-09`       | `2.0e-14`      |
| `2.0e-04` | `8.2e-10`       | `3.5e-14`      |
| `4.0e-04` | `3.9e-10`       | `3.4e-14`      |

The minus-branch defect decreases strictly monotonically across a sixteenfold
step increase, end-to-end ratio `2.5e+01`. The central-difference assembly's
truncation error grows as the square of the step, so over this sampled decade the
defect moves in the direction a rounding term takes and opposite to the direction
the truncation term takes. That is what the five samples establish. It is a
diagnosis consistent with assembly rounding; it is not an exclusion of other
mechanisms, and no mechanism was ruled out by an exhaustive argument. No power law
is claimed — the per-interval decrease is non-uniform (see Honest boundary). The
plus-branch defect is step-independent at summation noise and is exactly zero in
stored bits at step `5.0e-05`. Scale consistency:
`dQ_minus * 2 * step / u = 2.2e+02`, in the same decade as the spectral top
`|w|_max = 6.3e+01` — the implied local gradient scale is problem-sized. This is a
decade-level consistency statement; the constant is measured, not derived.

### Claim 7 — What the size scaling shows, and a heuristic scale comparison

Between `L = 3` and `L = 7`: `lam_min` softens by `4.3e+01`, the minus floor grows
by `2.2e+01`, `|E|_max` is unchanged (`1.0e+00`), and — from Claim 4's table —
`|E|_F` grows by `4.6e+00`, `E`'s nonzero count by `2.1e+01`, and the forcing
`|E eps0|_2` by `4.6e+00`.

What that supports: the response softening is a substantial contributor to the
floor's growth, since the largest local entry of the defect does not grow at all
while the floor grows by a factor of `2.2e+01`. What it does not support: assigning
ALL of the growth to the response. The forcing the solve actually sees grows by
`4.6e+00` in 2-norm, because `E`'s support grows with the box even though its
largest entry does not. No decomposition separating the two contributions
quantitatively is offered here; that is named in the Honest boundary. The floor
ratio also need not equal the `lam_min` ratio: the solve image weights `E`'s
overlap across the full regular spectrum, not the softest mode alone, and the
quantitative account of the floor at each size is Claim 5's law.

Heuristic scale comparison, not a rejector: the solve's relative conditioning
indicator `u kappa_2(Q) = u |Q| / lam_min` is `1.5e-14` at `L = 3` and `6.6e-13`
at `L = 7`. Multiplying by the response magnitude `|eps0|_2` gives an absolute
scale `1.4e-13` and `1.6e-11`, which the minus floor exceeds by `4.8e+02` and
`9.7e+01`. This comparison omits the dimension- and algorithm-dependent stability
factor a valid forward-error bound requires, and that factor is not pinned here.
The comparison is therefore consistent with the floor being larger than the naive
solve-noise scale; it does not establish that the floor is not the solve's own
roundoff. Deriving and gating a valid forward-error bound is named as an open
obligation below.

## Derivation sketch

Write `m` for the dof transport of a witness `h` and `Pi` for its permutation
operator, so `(Pi^T Q Pi)[i,j] = Q[m[i], m[j]]` and `E = Pi^T Q Pi - Q`.

**Exact equivariance.** The compiler assembles `Q` by central finite differences
of a frame-covariant local energy evaluated on local edge configurations. Under
a proper cubic rotation the relabeled assembly evaluates the same local
quantities on the same geometric objects, so in exact arithmetic
`Pi^T Q Pi = Q`. This is argued structurally here and supported at bit level by
the plus branch and the sweep; it is not proven symbolically in this cycle (see
Honest boundary).

**Floating dichotomy.** An all-plus image traverses the same evaluation paths
with unchanged arguments (only coordinates permute), so `E_plus` sits at the
summation-noise scale `u |Q|` — including one exactly-zero sweep sample. An
all-minus image feeds sign-reversed displacement arguments into the central
differences; the two rounding paths differ addend by addend, leaving `E` at the
roundoff scale of an assembled gradient difference, `u * G / (2 * step)` with
`G` a local gradient scale — the measured `2.2e+02` decade of Claim 6. This
paragraph is a mechanism sketch consistent with the measurements, not a proof:
no addend-by-addend account of the magnitude is supplied.

**First-order law.** With `null_dim = 0` the computed response operator is
`M = Q^-1` and the solve is `eps_of(x) = sigma * M @ x` with `sigma = +1` or
`-1` the compiler's response sign convention. Inverting the conjugation
identity `Pi^T Q Pi = Q + E` gives

`Pi^T M Pi = (Q + E)^-1 = M - M E M + O(E^2)`.

Hence, using `M b0 = sigma * eps0` and `M (E @ eps0) = sigma * eps_of(E @ eps0)`
(one `sigma^2` factor cancels),

`term2 = eps_of(Pi b0) - Pi eps_of(b0) = sigma (M Pi - Pi M) b0
       = -sigma * Pi M E M b0 + O(E^2)
       = -sigma * push(eps_of(E @ eps0)) + O(E^2)`.

The magnitude of the law is convention-independent; its overall sign pins the
convention. The measured cosine `1.0e+00` at both sizes fixes `sigma = -1` (the
solve returns the response of `Q eps + b = 0`); the opposite convention would
reverse the predicted sign, and the measured cosine excludes it. The
second-order remainder is far below the working scales; the law's adequacy is
certified by the measured residuals of Claim 5, not by an operator-norm bound.

## Honest boundary

**Target claim, stated once.** For the stored assembled operator `Q` at a given
box size and a given dof-transport permutation `Pi`, the response-stage transport
defect satisfies `d_eps = term1 + term2` and `term2 = -sigma * push(eps_of(E @
eps0)) + O(E^2)` with `E = Pi^T Q Pi - Q`. That is the whole derived statement.
Every causal reading of it — that `E` is assembly rounding, that the floor's
growth is response-side, that the floor is not the solve's own roundoff — is
DIAGNOSIS supported by the measurements below, not a proved consequence.

**Obligation graph.**

1. `d_eps = term1 + term2` for a linear response map: **proved** (linearity),
   and measured to close at `<= 3.0e-15` with live deletion rejectors (Claim 3).
2. `Pi^T M Pi = M - M E M + O(E^2)` with `M = Q^-1` and `null_dim = 0`:
   **proved** algebraically for the stored operator (derivation sketch).
3. Exact-arithmetic equivariance `Pi^T Q Pi = Q`: **open**. Argued structurally,
   supported at bit level by the plus branch, not proved symbolically. Without
   it, `E` is only "the measured non-commutation of the stored operator", and
   the word "defect" is descriptive.
4. An a-priori bound on the `O(E^2)` remainder: **open**. Adequacy is certified
   only by the measured residuals of Claim 5 at two sizes.
5. `E` is assembly rounding rather than any other mechanism: **open, and not
   claimed**. The five-sample sweep measures a direction over one decade.
6. Attribution of the floor's size growth between response softening and the
   growth of `E`'s support: **open, and not claimed**. Both are measured to grow
   (Claim 4 table); no separation of their contributions is derived.
7. A dimensionally and algorithmically valid forward-error bound for the solve:
   **open**. Claim 7's comparison is heuristic and omits the stability factor.

**Strongest missing lemma.** A symbolic proof of exact-arithmetic assembly
equivariance `Pi^T Q Pi = Q` for the compiler's local-energy central-difference
assembly under proper cubic rotations, together with an a-priori bound on the
first-order remainder. With both, items 1-4 close and the note becomes a theorem
about the stored operator plus a measured magnitude. Items 5-7 would still be
open: no result here excludes an exact-arithmetic assembly or discretization
defect, and none is asserted to.

- The defect magnitude `1.2e-10` is measured, not derived: no closed form for
  `E`'s entries is claimed. The scale row of Claim 6 places the implied local
  gradient scale in the `|w|_max` decade; that is a consistency check on the
  mechanism, not a derivation of the constant.
- The step sweep is a measured five-sample direction statement over one decade,
  not a scaling law and not an exclusion: the strict monotone decrease is the
  direction a rounding term takes, but the per-interval ratios are non-uniform,
  no exponent is claimed, and no alternative mechanism was tested and rejected.
- Exact-arithmetic equivariance `Pi^T Q Pi = Q` is argued structurally and
  supported bit-level on the plus branch; it is not proven symbolically here.
- Scope stops at the response stage. No amplitude, metric, or endpoint stage is
  re-run; downstream rows remain those of cycle 707. Clipped downstream values
  are diagnostics, not theorem gates.
- The law is measured on the two constant-sign branches at two sizes, one
  witness per branch, justified by cycle 707's measured branch degeneracy; the
  18 mixed-sign frames are not probed here (named below as a next path). Two
  witnesses at two sizes is a finite sample, not a family result.
- The first-order expansion's adequacy at the working scales is certified by the
  measured residuals, not by an a-priori error bound.
- On the plus branch the two-term split is not resolvable: `term1` sits at the
  closure residual, and the runner records that rather than claiming the split.

## The next paths opened

- **Entrywise localization of `E`.** Identify which stencil families carry the
  `1.2e-10` and account for the magnitude addend by addend, turning the measured
  constant into a derived one and the Claim 6 decade into an equality.
- **Mixed-sign prediction.** Extend the law to the 18 mixed-sign frames: predict
  each frame's response defect from its own measured `E` before running the
  transport, upgrading the law from two branches to all 24.
- **Downstream propagation.** Push the law through cycle 707's amplitude product
  identity so the endpoint floors are predicted from `E` alone.
- **Path-symmetrized assembly experiment.** A deliberately path-symmetrized
  assembly variant, run beside (never replacing) the landed compiler, would
  predict the minus floor collapsing to the plus floor — a cheap discriminating
  experiment for the mechanism.

## Relation to cycles 707 and 708

Cycle 707 named as next paths "Derive the response-stage reflection floor
constant" and "Derive the `L`-scaling of the two branch floors". This cycle
supplies measured structure toward both at the response stage, and retires
neither: the floor is reproduced as the solve image of the measured assembly
defect — an expression given `E`, with `E` itself measured, not derived — and the
size growth is shown to have at least two measured contributors, the regular
spectrum's softening (`4.3e+01`) and the growth of the defect's own support and
forcing (`4.6e+00` in `|E eps0|_2`) against a box-independent largest entry
(`1.0e+00`). Separating those contributions quantitatively remains open.

The minus-branch response floors measured here, `6.9e-11` and `1.5e-09`, agree
at printed precision with the response-stage minus rows of the cycle-707 stage
ladder, and the `L = 3` load-stage minus value `2.1e-14` likewise matches its
ladder row — from independently written transport code (componentwise under the
explicit dof permutation here; sorted multisets there). At bit-noise scales the
two diagnostics differ, so the remaining cells are same-scale rather than
same-digit; componentwise defects are never smaller than sorted-multiset ones.
Cycle 707's product identity carries the response floor downstream through the
amplitude dial, so this attribution feeds the endpoint floor directly.

Cycle 708's in-flight classification of the source edit-set stabilizers
(`PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02`,
cited as context only, not a dependency) probes the same chain's edit-domain
symmetries; nothing in this cycle depends on it.

## Runner

[physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02.py](../scripts/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02.py)
runs 73 gates in seven sections: frame scope and witnesses; upstream transport;
assembly-defect dichotomy with the global-growth measures; two-term decomposition
with live deletion rejectors; first-order law with the plus-branch rejector; step
sweep; size scaling with the heuristic solve-scale comparison. It prints
`TOTAL: PASS=73 FAIL=0` and writes the receipt
`outputs/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02_receipt_2026-08-02.json`
(floats stored as `{:.1e}`-formatted strings; no timestamps, hosts, or absolute
paths). Every gate band was fixed before the runner ran; the runner re-measures
everything from the landed chain. Consecutive runs on one host produce
byte-identical standard output and receipt, with the backend caveat recorded above.
Every floating-point number quoted in this note is the runner's own measurement in
the cached run that produced that TOTAL line; none is copied from an earlier probe.

The decomposition gate family is mutation-checked. Deleting `term1` from the
closure computation, deleting `term2`, and scaling `term1` by two each drive the
runner to a nonzero exit with failing `c3` gates; pinning `|E|_F` to its `L = 3`
value fails `c2.global_fro`. The mutations are recorded in the PR body.

## Citations

Load-bearing dependencies, linked:

- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
  — the operational source-response-readout chain whose compiled form this cycle
  measures.
- [Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
  — primary dependency: the constant-sign census, the branch degeneracy that
  justifies one witness per branch, and the stage ladder this cycle measures
  against.
- [Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
  — the landed chain, used verbatim and never re-implemented. It and its four
  transitive script imports are the runner's declared `AUDIT_INPUT_PATHS`.

Provenance only, deliberately non-linking — no claim or gate above reads either:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — the axiom surface; nothing here touches
  it.
- `docs/work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md`
  — provenance of the landed compiler.

## Review record

This note's scope was narrowed during review. What was dropped, and where the
retained scope ends:

- **Dropped:** "the entire minus floor is the commutator term". Retained: the
  measured `term1 / term2` fractions `1.2e-04` and `2.2e-05`, and the statement
  that the floor is the commutator term to within that fraction on the two
  measured cells.
- **Dropped:** "the defect is assembly roundoff, not truncation". Retained: over
  the sampled step decade the defect moves in the direction a rounding term takes
  and opposite to the truncation term's direction. No mechanism is excluded, and
  no route enumeration is claimed.
- **Dropped:** "the floor's size growth is entirely response-side". The claim
  rested on one measure, `|E|_max`. The runner now also measures `|E|_F`, `E`'s
  nonzero count, and `|E eps0|_2`, and all three grow with the box, so the
  attribution is retained only as "the response is a substantial contributor".
- **Dropped:** "the floor is not the solve's own roundoff". The comparison used
  `u kappa_2(Q)`, a relative conditioning indicator, against an absolute defect,
  and omits the stability factor a valid forward-error bound needs. Retained as
  an explicitly heuristic scale comparison.
- **Corrected:** `u` is now the float64 unit roundoff `2^-53` in both prose and
  code; the runner previously used `np.finfo(float).eps = 2^-52`. Every
  `u`-scaled number is recomputed. The decade-level conclusions are unchanged.
- **Rebuilt:** the decomposition gate. It previously compared the closure to a
  fixed `1e-13` and stayed green with one term deleted. It now carries live
  wrong-value rejectors on the same comparison path, gated where the split is
  resolvable and recording the honest converse where it is not.
- **Retained scope ends** at: exact algebra for the stored operator, and finite
  measurement on two constant-sign witness frames at `L = 3` and `L = 7` through
  the imported cycle-696 compiler, whose bytes are pinned by the runner cache.

**Outstanding at landing, as hard landing conditions.**

1. `docs/audit/data/citation_graph_manifest.json` must be regenerated on the
   proposed landing tree and included in the landing set: this delta adds one
   `docs/**/*.md` node, so graph topology changes. It is deliberately not carried
   on this branch, because every PR in this batch would edit the same base blob
   and collide pairwise. Regenerate with `docs/audit/scripts/build_citation_graph.py`
   then `docs/audit/scripts/write_citation_graph_manifest.py` on the landed tree,
   and inspect the added node's edges against this note's link set before
   acknowledgment. After this review the intended out-edge set is exactly two
   document edges, Cycle 700 and Cycle 707, plus the cycle-696 compiler script.
2. No claim-scoped helper-runner registry entry is requested. The compiler chain
   reaches the restricted audit packet as a transitive import of the primary
   runner, so `docs/audit/scripts/build_citation_graph.py` is not edited by this
   branch and no dependency-policy epoch question arises.
