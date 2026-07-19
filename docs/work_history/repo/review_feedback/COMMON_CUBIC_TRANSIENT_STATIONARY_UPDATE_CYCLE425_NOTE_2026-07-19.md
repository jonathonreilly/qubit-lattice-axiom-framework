# Common cubic transient/stationary physical update — Cycle 425

Date: 2026-07-19
Authority: none
Audit: unset

## Result and exact boundary

Cycle 425 constructs **one fixed response-controlled update** on a periodic cubic installation with **one reservoir M2 plus six directional field M2 per cell**. A frozen response M2 selects the free or source-defect branch of the same block-diagonal physical gate. The defect branch supports both:

1. **transient emission and transport** from the **Cycle-422 physical source seed**; and
2. a numerically selected **stationary dressed eigenstate** and shifted-Green profile of the **same update**.

The finite-volume comparison is frozen before output: periodic `L=3,...,9`, with **L=3,...,8 training** and **held L=9**. The eigenpair selection rule and the comparison with the older shifted-Green result and Cycle216 are inherited without refitting.

This is a positive common-update seam. **Eigenpair finding and preparation are host-supplied**. The eigenphase is not a rate; update count is not time; occupation is not energy or source; the profile is not gravity. No Born, occurrence, or Record claim is made.

## One physical update

Each periodic cell contains one reservoir bit and six hard-core directional field bits. Cycle 425 executes the conserved one-excitation sector, dimension `7 L^3`. The fixed branch update is

```text
U_r = S V_(r theta) C,  r=0,1,
```

where `C` is the onsite Cycle-214 field coin, `V` is the source-cell restriction of the Cycle-421 many-field vertex, and `S` is the ordinary directional field-bit stream. The response-controlled direct sum `|0><0| tensor U_0 + |1><1| tensor U_1` is one fixed unitary. Response, reservoir, and the scalar source convention are supplied physical labels.

The support is bounded by construction:

- field coin: six field M2 at one cell;
- response-controlled source vertex: response plus one reservoir and six field M2, support eight;
- each stream gate: one directional field-bit SWAP across an edge.

Every reservoir M2 streams trivially. Only the origin reservoir is response-coupled; the remaining reservoir modes are lawful stationary spectators in this Q1 construction. A translated defect is a covariant family member, not a translation-invariant single source.

## Physical source E/G

Cycle 422's nine-M2 `W` prepares, after clearing the old source/mediator pair,

```text
|source>   -> |R_origin>,
|mediator> -> -|s_F,origin>.
```

Cycle 425 embeds those exact target columns into the cubic Q1 code. Because the uniform field vector is fixed by the coin, for `r=0,1`

```text
U_r E_origin = (S E_origin) G_416(r).
```

The runner checks this forward and inverse relation on every frozen size. It also checks an exact intertwiner from the existing one-active-reservoir shifted-Green matrix into the full all-reservoir installation. Thus the transient and stationary calculations genuinely use one matrix word; no expectation readout selects a gate.

`W` remains a bounded preparation seam rather than part of each recurrent update. Blank-target preparation and primitive synthesis remain supplied.

## Dynamic face

Starting from `|R_origin>`, the response-one branch emits and streams a radius-one scalar field. On train `L=5` and held `L=9`, the first-step field weight equals `sin^2(theta)`, the second step remains normalized, and the adjoint exactly returns/reabsorbs the first-step state.

The **source-seam, vertex, stream, and coin deletions** are kept distinct:

- deleting the source seam gives no cubic input;
- deleting the vertex gives zero emitted field;
- deleting the stream leaves the emitted field at the origin while the nominal stream removes it to neighboring cells;
- deleting the coin is visible on the mediator/scalar input column.

This is transient unitary propagation, not a retarded continuum theorem.

## Stationary face and no-refit far shore

For every frozen size, the same response-one update has a selected dressed eigenpair with nonzero origin-reservoir and field weights. The selected eigenvector obeys

```text
U_1 Psi_L = lambda_L Psi_L,
```

so its basis-component squared norms are stationary. The shift-invert target `exp(+/- i theta/L^(3/2))`, three returned candidates, phase-sign filter, maximum-reservoir-weight choice, normalization, and real-positive reservoir phase convention are all supplied algorithmic structure. No physical preparation circuit or autonomous selection law is constructed.

Conditional on the selected eigenpair equations, the nonuniform scalar profile satisfies the existing exact relation

```text
phi_perp = q[-rho/2 + i sin(omega_L) 3(Laplacian-mu I)^-1 rho],
mu = 6(1-cos(omega_L)).
```

The normalized tail is compared without a fitted coefficient to the older shifted-Green profile and Cycle216's exact zero-mean `3 L^+ rho`. The shifted and zero-shift kernels are not forced equal. The source-specific ratio is required to decrease on the frozen sizes and remain below `7.1e-4` at held `L=9`, exactly as in the earlier comparison contract.

The full cubic installation includes decoupled reservoir spectator modes at eigenvalue one. The selected dressed state lies in the invariant subspace containing the active origin reservoir and all field modes; its embedding into the full update is checked directly.

## Exact controls

Cycle 425 checks:

- exact unitarity/inverse of both response branches;
- local block continuity at every `L=3` cell;
- all 24 proper-cubic frames of the source-centered update;
- physical source E/G and inverse on `r=0,1`;
- dynamic source/vertex/stream/coin deletion controls;
- positive and conjugate stationary branches on every train/held size;
- explicit uniform/zero-mode separation and the zero-shift Cycle216 equality;
- lawful-domain rejection; and
- one M64 matter/contact/mass spectator.

Each finite gate has an **exact inverse**, and the **conjugate branch** is checked independently. The normalized-tail comparison uses **no fitted coefficient**.

The M64 join is identity on matter. It tests compatibility with the existing contact and mass angle, not recoil, source work, or dressed inertia.

## Supplied, derived, and open

Supplied:

1. Cycle 422's physical `W` preparation, blank-target contract, and signed Cycle-418 seed;
2. one reservoir plus six field M2 per periodic cell and one frozen source response at the origin;
3. Cycle 214's field coin, the Cycle-421 Q1 vertex restriction, ordinary directional streams, and coin–vertex–stream order;
4. `L=3,...,8` training, held `L=9`, the source-centered defect, zero-mean convention, and Cycle216 `3L^+` comparator;
5. the host shift-invert target/candidate count/sign filter/reservoir-weight selection, normalization, and phase convention;
6. one M64 matter/contact spectator and diagnostic readout/tolerances.

Derived:

1. one fixed response-controlled cubic Q1 update with exact Cycle-422-source E/G and inverse;
2. unitarity, local continuity, proper-cubic covariance, transient transport, and deletion visibility;
3. stationary dressed eigenpairs of the same defect branch and the conditional no-refit shifted-Green identity;
4. zero-mode, conjugate-branch, held-size, domain, and matter/contact controls.

Open:

1. physical eigenpair selection and preparation—both remain host-supplied;
2. many-excitation cubic execution, carried matter/reservoir, recoil, contact work, and autonomous source recurrence;
3. equality to Cycle216 at finite nonzero shift or comparison under a different kernel/schedule;
4. physical energy/source interpretation, physical time/rate, Born law, actual Records, metric, and gravity.

No equality is forced between mismatched schedules or kernels. There is no no-go, minimum-content, shared-obstruction, or axiom-pressure claim.
