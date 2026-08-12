# The assembly equivariance defect obeys an exact cocycle law on the constant-sign sextet, with a finite mixed-frame comparator census — Cycle 710

Date: 2026-08-02

Claim type: bounded_theorem

Status: proposed_retained

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

Supplied inputs: the landed Cycle-696 compiler and its landed constants, used
verbatim and never re-implemented. There is no measured, fitted, or literature
constant imported by this cycle.

**Primary runner:**
`scripts/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.py`;
cached stdout
`logs/runner-cache/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.txt`;
paired receipt
`outputs/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02_receipt_2026-08-02.json`.

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "cycle 709 leaves symbolic exact-arithmetic assembly equivariance, an a-priori first-order remainder bound, and an entrywise derivation of the measured defect scale open; this note adds a finite sextet action/cocycle result and all-frame measurements without retiring those obligations"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "derive the assembly defect from the stencil summation, prove a remainder bound for the stored inverse, and test whether the finite sextet identities persist beyond L in {3, 7}"
```

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "The exact cocycle is algebraic once the finite constant-sign transport functoriality is established. Functoriality and every numeric level are checked only for the imported compiler at L in {3, 7}; the mixed-frame values are comparators between inequivalent label assemblies, not a theorem about physical covariance."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the action and cocycle have an exact finite core, but the compiler is imported, the scope is two finite boxes, the defect levels are measured floating-point values, and the symbolic assembly-equivariance and general-size obligations remain open"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Result

The Hessian-assembly equivariance defect `E_g := Pi_g^T Q Pi_g - Q` is measured
at every one of the 24 proper cubic frames, at both sizes `L = 3` and `L = 7`.
The landscape has four levels and one exact law:

- **Identity.** The identity frame has trivial transport and defect exactly
  `0.0e+00`.
- **All-plus branch.** At the two non-identity all-plus frames the defect
  ceiling is `|E|_max = 7.1e-15` — bit-identical across the two frames and
  across both sizes.
- **All-minus branch.** At the three all-minus frames the ceiling is
  `|E|_max = 1.2e-10` — again bit-identical across all three frames and across
  both sizes.
- **Mixed frames.** At every one of the 18 mixed-sign frames the transport is a
  well-defined bijective comparator (not the geometric edge map — see the
  boundary discussion), and the comparator value is `|E|_max = 4.0e+00`,
  bit-identical across all 18 frames at each size and within `1.3e-08` of the
  integer 4 at both sizes. The separation above the all-minus ceiling is
  `3.2e+10`.

The exact law: on the constant-sign sextet the dof transports compose as a
group action (`m_(a.b) = m_a[m_b]`, an integer identity verified on all 36
ordered pairs), and the defect satisfies the cocycle identity

`E_(a.b) = E_b + Pi_b^T E_a Pi_b`

with measured max-abs residual `0.0e+00` — bitwise zero — over all 20 ordered
non-identity pairs having non-identity product, at both sizes. Two discriminators show
the bracket is frame-specific: reversing the composition order changes 96
transport entries for the witness pair, and substituting the all-minus defect
into the all-plus slots of the bracket misses by `2.5e-10`.

Two corollaries of the cocycle law are measured independently and land bit for
bit. First, the coset-spread law: for `g` all-minus, `E_g - E_1` is a
permutation-conjugate of an all-plus defect, so the full-matrix coset spread
`max_g |E_g - E_1|_max` must equal the all-plus ceiling — measured equal bit
for bit (`7.1e-15`) at both sizes. Second, branch cancellation: the product of
two all-minus frames is all-plus, and the bracket says the two order-`1.2e-10`
all-minus defects combine to an all-plus defect at `7.1e-15` — four orders
below either input.

Finally, the Cycle-709 zero-parameter response law holds at every all-minus
frame at both sizes — six frame-size combinations, of which four
(`g = 4` and `g = 9` at each size) are new test points — with relative
residual at most `9.4e-04` and alignment cosine within `4.1e-07` of exact,
while both all-plus frames reject the law at residual `9.8e-01` or above. At
one mixed-frame witness (`g = 0`) the first-order law fails outright (residual
`3.8e+00` at `L = 3`, `2.0e+02` at `L = 7`). The minus-branch response floor
is uniform across the three all-minus frames to relative spread `4.0e-05`
(`L = 3`) and `5.6e-05` (`L = 7`).

## Setup

All measurements run the landed chain of the
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
used verbatim and never re-implemented, at `L = 3` and `L = 7` (open box,
`wrap = False`):

`build_domain -> rho_vector -> b = rho @ G -> sector_solve -> response -> eps`

with the centered single-edit source domain (label `5` on the central edge
`(A,A,A) -> (A+1,A,A)`, `A = (L-1)//2`). This cycle's chain stops at the
response `eps`; no amplitude, metric, or endpoint stage is exercised.

### Declared inputs and read inventory

The runner declares `AUDIT_INPUT_PATHS` naming the Cycle-696 compiler and the
four `scripts/` modules it imports transitively, so the runner cache pins their
bytes and rejects drift. Those five files are the only ancestral scientific
inputs read; no sibling cycle's measured value is read or copied in. The only
package-local write is the paired receipt under `outputs/`, and the runner does
not perform a self-hash or receipt-verification read. Its declared timeout is
`AUDIT_TIMEOUT_SEC = 600`.

Backend sensitivity is disclosed: the solve residuals and bit-noise-scale
all-plus values depend on the BLAS/LAPACK backend. Consecutive runs on one host
are byte-identical; a different backend can move those cells within their gate
bands. Numbers quoted here are those of the committed cached run.

Frame action: for a proper cubic rotation `R` about the box center, the site
map is the compiler's `frame_site_map`, and the induced dof transport `m`
sends the undirected spatial edge `(class, base)` to its image edge
canonicalized to the low corner (direction `|R v|`, base `g(x) + min(R v, 0)`).
`Pi` denotes the corresponding permutation operator and
`push(v)[m[i]] = v[i]`. All 24 transports are verified bijective at both sizes
(`n_dof = 98` at `L = 3`, `1854` at `L = 7`), and `null_dim = 0` at both
sizes, so the computed response operator is the full inverse.

Frame census (all 24 proper frames, det `+1`): a frame is *constant-sign* when
every stencil direction maps to a stencil direction with entries of one sign —
3 all-plus frames (including the identity), 3 all-minus frames, 18 mixed. The
constant-sign sextet is `[1, 4, 9, 15, 18, 23]` in the compiler's frame
enumeration: `23` is the identity, `15` and `18` are the two 3-cycles about
the body diagonal (mutually inverse), and `1`, `4`, `9` are the three
all-minus involutions. Cycle 700 landed the identification of this sextet as
the body-diagonal stabilizer (dihedral of order 6); this note measures the
defect landscape over that identification and cross-checks the census against
it.

Objects, per frame `g` and size: the assembly equivariance defect
`E_g := Pi_g^T Q Pi_g - Q`, entrywise `E_g[i,j] = Q[m_g[i], m_g[j]] - Q[i,j]`,
with ceiling `dQ_g := |E_g|_max`; the response-stage frame defect
`term2_g := eps_of(push(b0)) - push(eps0)` (the solve/permutation commutator
of cycle 709, with `b0` the assembled load and `eps0` its response); and the
zero-parameter first-order prediction `push(eps_of(E_g @ eps0))`, whose sign
convention was fixed in cycle 709.

## Imported compiler contract

The compiler constants consumed by this cycle's chain segment, all landed and
none re-measured here: the landed local energy selection `F_17` with the
centered lift; the source scale `SRC_SCALE = 0.17` and the barycentric
source-row convention; the edit label `5`; the open box; the central
finite-difference assembly step `1.0e-4`; the null cut `1.0e-8`, under which
`null_dim = 0` at both sizes, so the regular sector is the full space and the
computed response operator is the full inverse; and the response solve itself.
The downstream metric and endpoint machinery of the compiler (principal square
root, positivity margin, amplitude dial) is not exercised. There is no
measured, fitted, or literature constant imported by this cycle.

## Claims

### Claim 1 — Scope and census

All 24 proper cubic frames have determinant `+1`; the constant-sign census is
3 all-plus (`[15, 18, 23]`, including the identity `23`), 3 all-minus
(`[1, 4, 9]`), 18 mixed. All 24 dof transports are bijective at both sizes.
The identity frame's transport is the trivial permutation and its defect is
exactly `0.0e+00`. `null_dim = 0` at both sizes. (Gates C0.)

### Claim 2 — The sextet transport is a group action

On the constant-sign sextet the integer functoriality identity
`m_(a.b) = m_a[m_b]` holds exactly on all 36 ordered pairs, at both sizes; the
sextet is closed under composition; and the branch label obeys the product
rule of a sign character (all-minus times all-minus is all-plus, all-minus
times all-plus is all-minus). Equivalently, `g -> Pi_g` restricted to the
sextet is a genuine group homomorphism. (Gates C1.)

### Claim 3 — Exact cocycle law

For every ordered pair `(a, b)` of non-identity sextet frames whose product is
also non-identity — 20 pairs at each size — the identity

`E_(a.b) = E_b + Pi_b^T E_a Pi_b`

holds with measured max-abs residual `0.0e+00`, bitwise zero, at both `L = 3`
and `L = 7`. Discriminators: (i) transport order matters — for the witness
pair, 96 transport entries differ between the two composition orders; (ii) the
bracket is frame-specific — substituting the all-minus defect `E_1` into both
slots of the bracket for the all-plus pair `(15, 15)` misses the true
`E_(15.15)` by `2.5e-10`, the all-minus scale, four orders above the all-plus
ceiling it should reproduce; (iii) the reversed-order bracket for the witness
pair lands at `7.1e-15` — exactly the coset-spread scale — which is itself the
branch-uniformity consistency prediction, not a rejector. (Gates C2.)

### Claim 4 — Branch bit-uniformity and the coset-spread law

The defect ceiling `dQ = |E|_max` is bit-identical (float hex equality) across
the frames of each branch and across both sizes: `1.2e-10` at all three
all-minus frames, `7.1e-15` at both non-identity all-plus frames, the same
bits at `L = 3` and `L = 7`. The full-matrix coset spread
`max_g |E_g - E_1|_max` over the all-minus coset equals the all-plus ceiling
bit for bit at both sizes — the corollary the cocycle law predicts, measured
independently. (Gates C3.)

### Claim 5 — The first-order law holds at every all-minus frame

The Cycle-709 zero-parameter law `term2 ~= push(eps_of(E @ eps0))` holds at
every all-minus frame at both sizes: relative residuals `9.4e-04`, `8.8e-04`,
`8.9e-04` (`L = 3`, frames `1, 4, 9`) and `8.7e-04`, `5.5e-04`, `4.9e-04`
(`L = 7`), with worst alignment-cosine gap `4.1e-07` (`L = 3`) and `3.7e-07`
(`L = 7`). The frame-size combinations `(4, L=3)`, `(9, L=3)`, `(4, L=7)`,
`(9, L=7)` are new test points beyond cycle 709's witnesses. Both all-plus
frames reject the law (residual at least `9.8e-01`, cosines far from 1). The
minus-branch response floor `|term2|` is uniform across the three all-minus
frames to relative spread `4.0e-05` (`L = 3`) and `5.6e-05` (`L = 7`); the
measured floors are `2.3e-10` (`L = 3`) and `1.5e-08` (`L = 7`), against
all-plus floors of `6.3e-14`/`4.7e-14` and `1.1e-11`/`1.0e-11`. (Gates C4.)

### Claim 6 — The mixed-frame comparator census is uniform and order one

At every one of the 18 mixed-sign frames the comparator value is
`|E|_max = 4.0e+00`, bit-identical across all 18 frames at each size, and
within `1.3e-08` of the integer 4 at both sizes. The separation above the
all-minus ceiling is `3.2e+10`. At the probed mixed frame `g = 0`, the
first-order law has residual `3.8e+00` at `L = 3` and `2.0e+02` at `L = 7`.
The sign-mixed image classes at every mixed frame include the
body-diagonal class, and a frame has zero sign-mixed classes exactly when it
lies in the constant-sign sextet — over all 24 frames. (Gates C5.)

### Claim 7 — Census cross-check against the landed identification

The constant-sign list `[1, 4, 9, 15, 18, 23]`, the sign-flip census
`[(0, 3), (1, 9), (2, 9), (3, 3)]` (number of flipped axes, count of frames),
and the sextet element orders `[(1, 2), (4, 2), (9, 2), (15, 3), (18, 3),
(23, 1)]` all match the identification landed in cycle 700. (Gates C6.)

## Exact target and proof obligations

**Exact target.** For the imported Cycle-696 finite compiler at
`L in {3, 7}`, the six constant-sign frame transports form an action, so their
stored Hessian-assembly defects satisfy the stated cocycle; the branch levels,
all-minus response-law residuals, and mixed-frame comparator values are finite
measurements on that same declared surface.

Obligation graph:

1. The constant-sign frames close and their dof maps compose: proved by exact
   integer enumeration of all 36 ordered pairs at both sizes.
2. Functoriality implies the cocycle: proved algebraically below, without a
   floating-point approximation.
3. The all-minus coset spread equals the non-identity all-plus ceiling: follows
   from the cocycle, the involution at frame `1`, and invariance of max norm
   under permutation conjugation; independently measured by the runner.
4. The stated defect levels and response residuals: measured by the paired
   runner only at `L = 3` and `L = 7`; no arbitrary-size extension is claimed.
5. A geometric transport for mixed-sign frames: not supplied. Their maps are
   explicitly label comparators between inequivalent assemblies, so no
   physical-covariance conclusion is drawn from their order-one values.

The strongest missing lemma is a symbolic, backend-independent account of the
stored assembly's exact-arithmetic equivariance and floating defect scale for
general boxes. Degenerate coverage: the identity is included in the 36 action
pairs and has zero defect; the 20 cocycle measurements do not repeat the five
pairs whose product is the identity because the corresponding identity is
already algebraically trivial.

## Derivation sketch

**Functoriality.** On a constant-sign frame the canonicalization is trivial in
the direction slot (`|R v|` is itself the image stencil direction, up to
overall sign absorbed into the base shift), and the base shift composes as the
site map does. The composite of two constant-sign canonicalizations is then
the canonicalization of the composite frame — an integer statement, verified
exactly on all 36 ordered pairs at both sizes (Claim 2). Off the sextet this
argument is unavailable, and no functoriality is claimed there.

**Cocycle.** Given functoriality, `Pi_(a.b) = Pi_a Pi_b`, so

`E_(a.b) = Pi_b^T (Pi_a^T Q Pi_a) Pi_b - Q = Pi_b^T (Q + E_a) Pi_b - Q
         = E_b + Pi_b^T E_a Pi_b.`

In exact arithmetic the identity is algebraically automatic. The measured
content is twofold: the residual is bitwise zero in floating point at both
sizes — entrywise the bracket telescopes through stored values of `Q`, and on
this data the telescoping incurs no rounding — and the discriminators show
the equality is about the specific frames entering the bracket, not a generic
property of small matrices (the cross-branch substitution misses by
`2.5e-10`). The runner gates the measured zero; no general floating-point
rounding theorem is claimed.

**Coset-spread law.** Frame `1` is an involution, so for `g` all-minus,
`k := g . 1` is all-plus and the cocycle bracket for the pair `(k, 1)` gives
`E_g = E_1 + Pi_1^T E_k Pi_1`, hence `E_g - E_1 = Pi_1^T E_k Pi_1`.
Permutation conjugation re-indexes entries without arithmetic, so
`|E_g - E_1|_max = |E_k|_max` — the coset spread must land on the all-plus
ceiling bit for bit. The runner measures the spread independently of the
cocycle gates and finds exactly that (Claim 4). The same bracket read in the
other direction is the branch-cancellation statement: two order-`1.2e-10`
all-minus defects combine, through one permutation conjugation and one
addition, to an all-plus defect four orders smaller.

**Mixed-frame comparator mechanism.** For a mixed-sign frame some stencil direction maps to
an image with entries of both signs; the canonicalization `(|R v|,
g(x) + min(R v, 0))` then names a lattice edge that is not the rotated edge —
the transport is still a bijection of dof labels, but it compares the
assembled operator with a differently-assembled one rather than with its own
rotation image. `E` at a mixed frame is therefore a finite label comparator of
inequivalent assemblies, and its order-one value is a quantitative image of
the combinatorial obstruction cycle 700 landed: the body-diagonal class is
sign-mixed at every one of the 18 mixed frames, and zero mixed classes is
exactly sextet membership. The observed uniformity (one bit pattern across all
18 frames per size) and the proximity of the value to the integer 4 are
measurements; deriving the 4 from stencil combinatorics is a named next path.

**Law at all sextet frames.** Cycle 709 established the first-order mechanism
`Pi^T Q^-1 Pi = Q^-1 - Q^-1 E Q^-1 + O(E^2)` at one witness per branch. Here
the same zero-parameter prediction is evaluated at every non-identity sextet
frame: it holds on the entire all-minus coset (residuals at most `9.4e-04`,
cosines within `4.1e-07` of exact alignment) and is rejected on the all-plus
branch, where the defect is four orders smaller and the floor sits at the
all-plus scale. Branch uniformity of `E` (Claim 4) propagates to the response
floor: the three all-minus floors agree to `4.0e-05`/`5.6e-05` relative.

## Honest boundary

- The cocycle identity is gated as a measured bitwise-zero residual on this
  data at both sizes. The exact-arithmetic identity follows from
  functoriality; no theorem about floating-point rounding of general data is
  claimed.
- The branch ceilings `1.2e-10` and `7.1e-15` and the comparator value
  `4.0e+00` are measured, not derived. The bit-identity of the ceilings across
  frames and sizes is likewise a measurement. Cycle 709's step-sweep roundoff
  characterization is cited, not re-run here.
- Bit-identity claims are hex equality of the stated max-abs values (and, for
  the coset spread, of the full-matrix spread against the all-plus ceiling).
  Mixed-frame uniformity is per size; no cross-size bit claim is made for the
  comparator.
- The first-order law's measured success domain is the response stage on the
  all-minus coset. At the one probed mixed frame the comparator is order one,
  so no small-`E` expansion applies; that finite failure witness is not a
  theorem about every mixed-frame response.
- At mixed frames `E` is a comparator between inequivalent assemblies by
  construction; no covariance violation of the assembly is claimed there, and
  on the sextet the assembly is covariant only to the measured roundoff-scale
  ceilings, not exactly.
- The chain stops at the response `eps`; no amplitude, metric, endpoint, or
  `K`-stage quantity is measured. Nothing here touches an axiom, a primitive,
  or another supplied-premise surface.

## The next paths opened

- **Derive the integer 4.** The comparator sits within `1.3e-08` of 4 at both
  sizes with one bit pattern across all 18 mixed frames. A stencil-level count
  of the couplings displaced by a body-diagonal-mixing frame is a sharply
  posed combinatorial target for deriving the value.
- **Entrywise localization of the all-minus defect.** With all three all-minus
  defects now known to be bit-uniform, locating which couplings carry the
  `1.2e-10` entries (and deriving the gradient-scale constant of cycle 709's
  named path) has three times the data at no new cost.
- **Downstream propagation.** Push the cocycle law through the amplitude
  product identity of cycle 707 to the `K` stage: the bracket structure
  predicts how frame-composition acts on the downstream floors.
- **Path-symmetrized assembly.** Re-order the assembly summation and re-measure
  the branch ceilings; the coset-spread law now states exactly how the spread
  must respond if the all-minus ceiling moves.

## Relation to cycles 700, 707, 708, and 709

[Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
landed the identification of the constant-sign sextet with the body-diagonal
stabilizer and the all-24/sextet split of the prediction and coframe carriers.
This cycle measures the assembly-defect landscape over that identification and
cross-checks its census (Claim 7).
[Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
measured the branch degeneracy at one witness per branch and posed the
frame-structure questions this cycle answers at the Hessian level. The open-PR
note `PHYSICAL_SOURCE_EDIT_SET_SIGNED_STABILIZER_CLASSIFICATION_CYCLE708_NOTE_2026-08-02`
classifies source edits by signed stabilizer — complementary context only; no
claim or calculation here depends on it. The landed
[Cycle 709 response-floor note](PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02.md)
introduced `E`, the exact response-stage decomposition, and the zero-parameter
law at one witness per branch; this cycle extends that measurement from two
witnesses to all 24 frames, upgrades the per-frame statement to an exact
cocycle law with measured corollaries, and records the finite mixed-frame
comparator census.

## Runner

[physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.py](../scripts/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02.py)
runs 55 gates in seven sections: frame scope and census; sextet functoriality
and group structure; the exact cocycle law with its discriminators; branch
bit-uniformity and the coset-spread law; the first-order law at every all-minus
frame; the finite mixed-frame comparator census; and census cross-checks
against the landed Cycle-700 identification. The gates are finite-dimensional
computational identities and measured-band checks. It prints
`TOTAL: PASS=55 FAIL=0` and writes the receipt
`outputs/physical_assembly_defect_cocycle_and_mixed_frame_comparator_cycle710_2026_08_02_receipt_2026-08-02.json`
(floats stored as `{:.1e}`-formatted strings; no timestamps, hosts, or
absolute paths). Gate bands were fixed before the runner ran — from probe
measurements where probed, a priori where not (the `L = 7` mixed-frame rejector)
— and the runner re-measures everything from the landed chain. Three
consecutive runs on one host produce byte-identical standard output and a
byte-identical receipt. Every floating-point number quoted in this note is the runner's own
measurement in the run that produced that TOTAL line; none is copied from an
earlier probe.

The check families were mutation-tested during review. Reversing the cocycle
conjugation order fails `c2`; changing the expected constant-sign census fails
`c0`/`c6`; negating the response prediction fails `c4`; replacing a mixed-frame
defect by zero fails `c5`; and changing a declared compiler input makes the
runner cache stale through its input fingerprint.

## Citations

Load-bearing dependencies, linked:

- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
  — the landed sextet/stabilizer identification and carrier split this cycle
  measures over and cross-checks.
- [Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
  — the branch degeneracy and the stage ladder behind the response-stage
  objects measured here.
- [Cycle 709](PHYSICAL_MINUS_BRANCH_RESPONSE_FLOOR_ASSEMBLY_DEFECT_LAW_CYCLE709_NOTE_2026-08-02.md)
  — the bounded response-stage decomposition and first-order expression extended
  across the finite constant-sign census here.
- [Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py)
  — the landed chain, used verbatim and never re-implemented; it and its four
  transitive script imports are the declared `AUDIT_INPUT_PATHS`.

Provenance only, deliberately non-linking:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — the axiom surface; nothing here touches it.
- `docs/work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md`
  — provenance of the landed compiler.

## Review record

Review narrowed three surfaces without changing the finite computation:

- **Dropped:** the statement that the first-order law holds at every
  non-identity sextet frame. It holds on the three all-minus frames at each
  size; the two non-identity all-plus frames are explicit rejectors.
- **Dropped:** physical-covariance-boundary wording for the 18 mixed frames.
  Their transport is not the geometric edge map, so the durable result is only
  the finite label-comparator census plus one response-law failure witness.
- **Repaired:** Cycle 709 is now a landed, load-bearing markdown dependency;
  Cycle 708 remains non-linking context and creates no wait condition.

Independent audit remains required before any effective retained grade.
