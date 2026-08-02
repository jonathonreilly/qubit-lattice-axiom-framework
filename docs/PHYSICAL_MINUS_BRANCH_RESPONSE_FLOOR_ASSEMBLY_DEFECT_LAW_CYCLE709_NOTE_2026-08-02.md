# The minus-branch response floor is the solve image of the Hessian-assembly equivariance defect — Cycle 709

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

Supplied inputs: the landed Cycle-696 compiler and its landed constants, used
verbatim and never re-implemented. There is no measured, fitted, or literature
constant imported by this cycle.

## Result

Cycle 707 measured that the all-minus constant-sign transport defect of the
compiled source-response chain first resolves at the `b -> eps` solve, and named
the response-stage floor constant and the `L`-scaling of the branch floors as
next paths. This cycle locates the origin of that floor one stage earlier than
the solve and derives the solve's role exactly.

1. **The response-stage transport defect decomposes exactly into two floating
   terms**, `d_eps = term1 + term2`, with `term1 = eps_of(db)` (the solve image
   of the load-stage roundoff) and `term2 = eps_of(push(b0)) - push(eps0)` (the
   solve/permutation commutator). The decomposition identity holds at
   `<= 3.0e-15` in every branch-size cell, and on the all-minus branch `term1`
   contributes at most a `1.2e-04` fraction of the floor: the entire minus floor
   is the commutator term.

2. **The commutator is the first-order solve image of a Hessian-assembly
   equivariance defect.** Define `E := Pi^T Q Pi - Q`, the failure of the
   assembled static Hessian to commute exactly with the frame's dof relabeling.
   In exact arithmetic `E = 0`. In floating point the all-minus branch measures
   `dQ = |E|_max = 1.2e-10` — bit-identical at `L = 3` and `L = 7` — while the
   all-plus branch measures `7.1e-15`, a branch separation of `1.8e+04`. The
   zero-parameter first-order law

   `term2 ~= push(eps_of(E @ eps0))`

   reproduces the minus floor with relative residual `9.4e-04` (`L = 3`) and
   `8.7e-04` (`L = 7`) at cosine `1.0e+00`, and correctly fails on the plus
   branch, where `E` is sub-noise (residuals `1.1e+00` and `9.8e-01`).

3. **The defect is assembly roundoff, not truncation, and the floor's size
   growth is entirely response-side.** Under a step sweep the minus-branch
   defect decreases strictly monotonically as the finite-difference step grows
   (truncation would grow with the step), and between the two sizes the defect
   is bit-identical (ratio `1.0e+00`) while the softest regular eigenvalue
   softens by `4.3e+01` and the floor grows by `2.2e+01`: the growth is the
   response amplifying a size-independent local defect.

The floor cycle 707 measured is therefore no longer an unexplained constant of
the solve: it is the response image of a measured, localized, step-dependent
assembly roundoff object, reproduced by a law with no fitted parameter.

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
operator, `push(v)[m[i]] = v[i]`, and `u` denotes the float64 unit roundoff.

Witnesses: the constant-sign census of the 24 proper frames is `3` all-plus
(including the identity) and `3` all-minus, with `18` mixed. Following the
branch degeneracy measured by cycle 707, one witness per constant-sign branch is
probed: `g = 15` (all-plus 3-cycle) and `g = 1` (all-minus).

Defect diagnostics, per branch and size, all max-abs and componentwise under the
transport: `drho` (source stage), `db` (load stage, `db := b_h - push(b0)`),
`d_eps` (response stage, `d_eps := eps_of(b_h) - push(eps0)`); the assembly
equivariance defect `E := Pi^T Q Pi - Q`, entrywise
`E[i,j] = Q[m[i], m[j]] - Q[i,j]`, with `dQ := |E|_max`; and the decomposition
terms `term1 := eps_of(db)`, `term2 := eps_of(push(b0)) - push(eps0)`.

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
`3.6e-15` / `3.1e-15`, minus `2.1e-14` / `1.1e-14` (`L = 3` / `L = 7`). Neither
upstream stage carries a branch floor.

### Claim 3 — Exact two-term decomposition of the response defect

| branch, `L` | `d_eps`   | `term1`   | `term2`   | closure   |
|-------------|-----------|-----------|-----------|-----------|
| plus, 3     | `2.3e-14` | `1.0e-15` | `2.3e-14` | `6.0e-16` |
| minus, 3    | `6.9e-11` | `8.3e-15` | `6.9e-11` | `1.4e-15` |
| plus, 7     | `1.6e-12` | `2.7e-15` | `1.6e-12` | `3.0e-15` |
| minus, 7    | `1.5e-09` | `3.4e-14` | `1.5e-09` | `2.9e-15` |

The identity `d_eps = term1 + term2` is algebraic for a linear response map;
the closure gate certifies the solve's floating linearity at the working scales
(`<= 3.0e-15` in every cell), so the decomposition is a valid exact split of the
measured defect, not a physics claim by itself. On the minus branch the ratio
`term1 / term2` is `1.2e-04` (`L = 3`) and `2.2e-05` (`L = 7`): the load-stage
roundoff never drives the floor. The minus floor is the commutator term.

### Claim 4 — The assembly equivariance defect and its branch dichotomy

| branch | `dQ` at `L = 3` | `dQ` at `L = 7` | size ratio |
|--------|-----------------|-----------------|------------|
| plus   | `7.1e-15`       | `7.1e-15`       | —          |
| minus  | `1.2e-10`       | `1.2e-10`       | `1.0e+00`  |

The branch separation is `1.8e+04` at both sizes. The minus-branch defect is
bit-identical between `L = 3` and `L = 7`: `E` lives in the local
finite-difference stencils, not in the global operator.

### Claim 5 — Zero-parameter first-order law

Prediction: `term2 ~= push(eps_of(E @ eps0))`, with `E` measured from the
assembled operator itself, `eps0` the base response, and `eps_of` the landed
solve — nothing fitted.

| branch, `L` | rel. residual | cosine     |
|-------------|---------------|------------|
| minus, 3    | `9.4e-04`     | `1.0e+00`  |
| minus, 7    | `8.7e-04`     | `1.0e+00`  |
| plus, 3     | `1.1e+00`     | `-3.6e-01` |
| plus, 7     | `9.8e-01`     | `8.1e-01`  |

The plus rows are a built-in wrong-regime rejector: there `E` sits at summation
noise, the first-order image is sub-noise, and the law is required to fail — and
does. On the minus branch the absolute residual (relative residual times floor)
lands at the plus-branch floor scale of the matching size — compare
`9.4e-04 x 6.9e-11` with `2.3e-14`, and `8.7e-04 x 1.5e-09` with `1.6e-12` — so
the law accounts for the minus floor down to the pipeline's own bit noise.

### Claim 6 — Roundoff character: step sweep and scale consistency

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
truncation error grows as the square of the step, so the direction of this sweep
discriminates: `E` is roundoff, not truncation. No power law is claimed — the
per-interval decrease is non-uniform (see Honest boundary). The plus-branch
defect is step-independent at summation noise and is bit-exactly zero at step
`5.0e-05`. Scale consistency: `dQ_minus * 2 * step / u = 1.1e+02`, in the same
decade as the spectral top `|w|_max = 6.3e+01` — the implied local gradient
scale is problem-sized. This is a decade-level consistency statement; the
constant is measured, not derived.

### Claim 7 — Size scaling is response-side; wrong-model rejector

Between `L = 3` and `L = 7`: `lam_min` softens by `4.3e+01`, the minus floor
grows by `2.2e+01`, and `dQ` is unchanged (`1.0e+00`). All floor growth is the
regular spectrum softening against a size-independent defect. The floor ratio
need not equal the `lam_min` ratio: the solve image weights `E`'s overlap across
the full regular spectrum, not the softest mode alone; the quantitative account
is Claim 5's law reproducing the floor at both sizes, while the dichotomy here
attributes the growth. Wrong-model rejector: the solve's intrinsic spectral
noise scale `u |Q| / lam_min` (`3.0e-14` at `L = 3`, `1.3e-12` at `L = 7`)
underpredicts the minus floor by `2.3e+03` and `1.2e+03` respectively — the
floor is not the solve's own roundoff; it is the solve's image of the assembly
defect.

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
summation-noise scale `u |Q|` — including one bit-exact zero in the sweep. An
all-minus image feeds sign-reversed displacement arguments into the central
differences; the two rounding paths differ addend by addend, leaving `E` at the
roundoff scale of an assembled gradient difference, `u * G / (2 * step)` with
`G` a local gradient scale — the measured `1.1e+02` decade of Claim 6.

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

- The defect magnitude `1.2e-10` is measured, not derived: no closed form for
  `E`'s entries is claimed. The scale row of Claim 6 places the implied local
  gradient scale in the `|w|_max` decade; that is a consistency check on the
  mechanism, not a derivation of the constant.
- The step sweep is a measured five-sample discriminator statement, not a
  scaling law: the strict monotone decrease fixes the roundoff direction, but
  the per-interval ratios are non-uniform and no exponent is claimed.
- Exact-arithmetic equivariance `Pi^T Q Pi = Q` is argued structurally and
  supported bit-level on the plus branch; it is not proven symbolically here.
- Scope stops at the response stage. No amplitude, metric, or endpoint stage is
  re-run; downstream rows remain those of cycle 707. Clipped downstream values
  are diagnostics, not theorem gates.
- The law is verified on the two constant-sign branches at two sizes, one
  witness per branch, justified by cycle 707's measured branch degeneracy; the
  18 mixed-sign frames are not probed here (named below as a next path).
- The first-order expansion's adequacy at the working scales is certified by the
  measured residuals, not by an a-priori error bound.

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
delivers both at the response stage: the floor constant is the solve image of
the measured assembly defect — derived given `E`, with `E` itself measured, not
derived — and the size growth is attributed entirely to the regular spectrum's
softening (`4.3e+01`) acting on a size-independent defect (`1.0e+00`).

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
runs 60 gates in seven sections: frame scope and witnesses; upstream transport;
assembly-defect dichotomy; exact decomposition; first-order law with the
plus-branch rejector; step sweep; size scaling with the wrong-model rejector.
It prints `TOTAL: PASS=60 FAIL=0` and writes the receipt
`outputs/physical_minus_branch_response_floor_assembly_defect_law_cycle709_2026_08_02_receipt_2026-08-02.json`
(floats stored as `{:.1e}`-formatted strings; no timestamps, hosts, or absolute
paths). Every gate band was fixed from probe measurements before the runner
ran; the runner re-measures everything from the landed chain. Three consecutive
runs produce byte-identical standard output and a byte-identical receipt. Every
floating-point number quoted in this note is the runner's own measurement in the
run that produced that TOTAL line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) — the axiom surface; nothing
  here touches it.
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
  — the operational source-response-readout chain whose compiled form this cycle
  measures.
- [Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
  — primary dependency: the constant-sign census, the branch degeneracy, the
  stage ladder this cycle explains, and the two next paths answered here.
- [joined-compiler tournament note](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)
  — provenance of the landed compiler.
- [Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
  — the landed chain, used verbatim and never re-implemented.
