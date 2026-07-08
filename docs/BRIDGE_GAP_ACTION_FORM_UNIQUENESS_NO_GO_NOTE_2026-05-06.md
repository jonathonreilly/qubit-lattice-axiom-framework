# Bridge Gap — Action-Form Uniqueness No-Go

**Date:** 2026-05-06
**Type:** named-obstruction no-go
**Claim type:** no_go
**Status:** no-go proposal: under the current accepted-premise and retained
support stack (Quantum / physical `Cl(3)` local algebra, Lattice / `Z^3`
substrate, canonical Tr-form, per-site dimension two, reflection positivity,
single-clock evolution, Lieb-Robinson support, and retained Casimir), the
action-form uniqueness question — does Cl(3)/Z³ select Wilson,
heat-kernel, Manton, or some other gauge action functional? — CANNOT
be resolved. The framework's derived action is action-form ambiguous;
distinct admissible actions remain compatible with the current support, and
Wilson versus heat-kernel already give distinct ⟨P⟩(6) values at finite β.
**Script:** `scripts/frontier_bridge_gap_action_form_uniqueness_no_go.py`
(source-side no-go verifier; PASS=14 FAIL=0 on current source)
**Authority role:** no-go source proposal. Audit verdict and downstream
status are set only by the independent audit lane.

## Question

Does the framework's current accepted-premise and retained support stack uniquely select
the gauge action functional `S(U)`? In particular, does it force
**heat-kernel** `S_HK = -log P_t(U)` (Block 01-02 candidate) over
**Wilson** `S_W = -β · Re Tr U / N_c` (currently imported per
[`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md))?

## Answer

**NO.** The framework's current accepted premises and retained support do not uniquely
select an action-form. At least three distinct gauge actions
(Wilson, heat-kernel, Manton) are jointly compatible with:

- Quantum / physical `Cl(3)` local algebra
- Lattice / `Z^3` substrate
- Canonical Tr-form `Tr(T_a T_b) = δ_{ab}/2`
- Per-site Hilbert dim 2 (Cl(3) Pauli)
- Reflection-positivity support
- Single-clock evolution + Lieb-Robinson
- Retained Casimir `C_2(1,0) = 4/3`
- Continuum-limit consistency at small `a`

Each has the same leading continuum limit `(1/2g²)∫Tr F² d⁴x` and the
same retained algebraic structure. Wilson and heat-kernel differ in
**finite-β behavior**, including ⟨P⟩(β=6) values; Manton is a third
leading-order-compatible action form but its finite-β value is not needed for
the non-uniqueness witness.

## Framework baseline for this no-go

Same as the predecessor heat-kernel bridge notes. No new axioms or primitives
are adopted here.

## Setup: candidate action functionals

Three concrete actions consistent with the framework's primitives:

### Candidate I: Wilson

```
S_W(U_p) = β · (1 - (1/N_c) Re Tr U_p), β = 2 N_c / g_bare² = 6.            (W)
```

Currently imported per `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18`
explicit "retained convention, not derived from Cl(3)."

### Candidate II: Heat-kernel

```
S_HK(U_p) = -log P_t(U_p), t = g_bare² = 1 (Block 01 derived).               (HK)
```

Casimir-diagonal: `P_t(U) = Σ_λ d_λ exp(-t·C_2/2) χ_λ(U)`. Uses
retained `C_2`. ⟨P⟩_HK,1plaq(6) = exp(-2/3) ≈ 0.5134 (Block 02).

### Candidate III: Manton

```
S_M(U_p) = β · d²(U_p, I), d(·,·) = bi-invariant geodesic distance.        (M)
```

Uses the canonical bi-invariant metric (Block 01 Step 1). For U near
identity: `d²(U, I) = |X|² + O(X⁴)` matching Wilson and HK at leading
order. Differs at higher orders.

## Step 1: All three pass continuum-limit matching

For `U = exp(iX)` with `X` small:

| Action | Small-X expansion | Continuum limit |
|---|---|---|
| Wilson | `(β/(4 N_c)) |X|² + O(X⁴)` (Block 01 eq. (8)) | `(1/2g²) Tr F² + O(a²)` |
| Heat-kernel | `|X|²/(2 t) + O(X⁴)` (Block 01 eq. (13)) | `(1/2g²) Tr F² + O(a²)` |
| Manton | `(β/2) |X|² + O(X⁴)` (Helgason-style geodesic expansion) | `(1/2g²) Tr F² + O(a²)` |

Setting `(β/(4 N_c)) = 1/(2t) = (β_M / 2)` matches all three at leading
order. At canonical `g_bare = 1, β = 6`:

```
β_W = 6, t_HK = 1, β_M = 1.                                                (Step 1.1)
```

All three actions are consistent with the Lattice + Quantum baseline,
canonical Tr-form, and continuum-limit matching at the framework's canonical
evaluation point. **No currently registered axiom, approved primitive, or
retained support theorem distinguishes them.**

## Step 2: Higher-order expansions differ

For `U = exp(iX)` with `X` not infinitesimal, the actions differ at
O(X⁴) and beyond. Standard SU(N) results (Drouffe-Zuber 1983,
Menotti-Onofri 1981):

| Action | O(X⁴) coefficient |
|---|---|
| Wilson | proportional to `Tr(X⁴)` and `(Tr X²)²` with specific Wilson coefficients |
| Heat-kernel | proportional to same monomials with different (Brownian-motion-derived) coefficients |
| Manton | proportional to same monomials with geodesic-curvature coefficients |

These differences already propagate to **distinct finite-β plaquette
expectations** for Wilson versus heat-kernel:

```
⟨P⟩_W(β=6) ≠ ⟨P⟩_HK(t=1) at finite β.                                      (Step 2.1)
```

In particular, single-plaquette evaluations:

| Action | ⟨P⟩_1plaq(canonical) | Source |
|---|---|---|
| Wilson | 0.4225317396 | V=1 PF ODE certified |
| **Heat-kernel** | **0.5134171190 = exp(-2/3)** | **Block 02** |
| Manton | not used for the numeric separation | compatible leading-order action form |

## Step 3: Naturality arguments — suggestive, not tight

Several arguments suggest HK is the most "Cl(3)-native" action, but
none rises to a uniqueness theorem without deriving or explicitly supplying an
action-selection criterion:

### Naturality argument (a): Casimir-diagonal under retained Tr-form

HK uses the Casimir `C_2(λ) = Σ_a (T_a)² eigenvalue on irrep λ` directly.
This Casimir IS retained (`SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02`)
and follows from the canonical Tr-form (`Tr(T_a T_b) = δ_{ab}/2`) as a
direct algebraic consequence. Wilson's Bessel-determinant character
coefficients `c_λ(β)` are NOT direct algebraic consequences of Tr-form
— they require defining `exp(β · Re Tr U / N_c)` and computing
characters, which is an external functional choice.

**But:** Wilson's coefficients can ALSO be expressed in terms of
Casimirs (via the integral representation of Bessel determinants). So
"Casimir-diagonal" is a cleaner formal property of HK, not a uniqueness
selector.

### Naturality argument (b): Brownian-motion uniqueness on Riemannian manifold

On a Riemannian manifold with metric `g`, the heat semigroup `exp(t·Δ_g)`
is **uniquely determined** by `g` (no convention freedom). Brownian motion
is the canonical diffusion generator. For the canonical Tr-form metric,
HK is the canonical heat semigroup.

**But:** "the canonical heat semigroup" doesn't translate directly to
"the canonical lattice gauge action." A lattice gauge action is a
functional `S: SU(N) → ℝ` of the link variables; Wilson, HK, and Manton
are all valid functionals. Their "canonicity" depends on what criterion
is being optimized.

### Naturality argument (c): Symanzik improvement

Standard Symanzik analysis: improved actions reduce O(a²) lattice
artifacts. HK has specific O(a²) coefficients; Wilson has different
ones; Manton has yet different ones. The framework's primitives don't
specify a Symanzik-improvement criterion that selects one over the
others.

## Step 4: Why this is a STRUCTURAL no-go, not a research-effort gap

The action-form ambiguity is structural because:

1. **All three actions use only the current support stack.** Wilson's
   functional `Re Tr U` is a Lie-algebra-level construction; HK uses
   retained Casimir; Manton uses canonical metric. None requires a
   new axiom or primitive.

2. **All three give the same continuum limit.** The `a → 0` matching
   at leading order is identical. There's no continuum-limit lever
   distinguishing them.

3. **The differences are at finite β** = lattice scale = the framework's
   evaluation point. Finite-β evaluation is exactly where the famous
   open lattice problem lives. There's no accepted premise or retained theorem that pins
   the finite-β coefficient structure tightly enough to force one
   action over others.

4. **No action-selection premise is currently supplied.** A future derivation,
   owner-approved admission, or convention could select an action, but that
   would be an explicit additional input rather than a consequence of the
   current stack.

## Theorem 4 (action-form uniqueness no-go)

**Theorem (T4, no-go).** Under the framework's current accepted-premise and
retained support stack (Lattice + Quantum baseline, canonical Tr-form,
per-site dimension two, reflection positivity, single-clock evolution,
Lieb-Robinson support, retained Casimir, and the `g_bare = 1` open gate), the
gauge action functional cannot be uniquely selected from the current candidates.
Wilson and heat-kernel are jointly compatible with the current support and
continuum-limit matching yet give distinct finite-β ⟨P⟩(6) values. Manton is
a third leading-order-compatible action form, but no Manton finite-β value is
needed for the non-uniqueness witness. The difference structure cannot be
resolved without deriving, explicitly admitting, or conventionally supplying an
action-selection criterion.

**Proof.** Steps 1-4. ∎

## No-Go Discipline Gate

This review uses the narrowed no-go above, not a permanent impossibility claim.

- N1 route enumeration: continuum-leading matching fails because Wilson and
  heat-kernel share the leading coefficient after parameter matching; Casimir /
  trace-form naturality fails as an action selector without an added criterion;
  diffusion-semigroup uniqueness selects HK only conditional on a supplied
  continuous Markov generator; a scheme convention can select an action only as
  an explicit admission or convention; a fixed-action nonperturbative solve
  computes a value after the action is chosen and does not choose the action.
- N2 wall independence: the collapsed wall is the missing action-selection
  criterion / realized dynamics / explicit convention. The Wilson-HK finite-β
  separation is the non-uniqueness witness, not a second wall.
- N3 hidden-wall scan: terms such as canonical, current support, and standard
  representation theory are non-load-bearing context unless linked above; the
  load-bearing wall remains explicit.
- N4 residual matching: the later HK diffusion theorem attacks exactly the
  diffusion-selection residual and leaves the generator/rate-law residual open;
  the record semigroup boundary names that same generator/rate-law residual.
- N5 rhetoric audit: the result is at the gauge-action-functional level for the
  named candidate surface. It is not a statement about every conceivable action
  or every possible future dynamics.
- N6 partial-closure scan: a future derivation of the gauge-link diffusion
  generator, or an owner-approved action convention/admission, can close the
  wall without changing the axioms. Approved primitives are not treated as
  bounded walls here.
- N7 steelman: the strongest counterargument is the HK diffusion theorem: among
  Wilson/HK/Manton, HK is the unique continuous-time diffusion kernel. The
  counterargument does not defeat this scoped no-go because the framework has
  not supplied the realized gauge-link diffusion generator.
- N8 cross-cycle echo: prior "new axiom" style walls have been narrowed by
  convention/admission or route-sharpening; this note is therefore phrased as a
  current-stack non-uniqueness boundary with explicit closure routes, not as a
  permanent no-route theorem.

## Consequence for the four cluster-obstruction lanes

The four cluster lanes (yt_ew M, gauge-scalar bridge, Higgs mass scalar
normalization, Koide-Brannen phase) per
[`LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md`](LATTICE_PHYSICAL_MATCHING_CLUSTER_OBSTRUCTION_NOTE_2026-05-02.md)
all anchor on the framework's gauge plaquette evaluation. Under T4's
no-go, the lanes' downstream quantitative claims are **range-bounded**
by the action-form ambiguity:

| Lane | Wilson value | HK value (Block 02 1-plaq, thermo open) | Range |
|---|---|---|---|
| `u_0 = ⟨P⟩^(1/4)` | 0.4225^(1/4) = 0.806 (1-plaq) | 0.5134^(1/4) = 0.847 (1-plaq) | ~5% range |
| `α_s(v) = α_bare/u_0²` | scaled by u_0² ~ 0.65 | scaled by u_0² ~ 0.72 | ~10% range |

The ~5-10% action-form range exceeds ε_witness ~ 3×10⁻⁴ by ~150-300×.
Until action-form uniqueness is closed, the four cluster lanes'
quantitative claims are **structurally ambiguous at the action-form
level**, not just at the famous-open-problem level.

## Scope and Non-Claims

This no-go is conditional on the current accepted-premise and retained support
stack enumerated in Step 4, and the representative action set
`{Wilson, heat-kernel, Manton}`. Other candidate actions may extend the
no-go but do not weaken it.

The note is reusable negative evidence. It does not add a new primitive
or select a preferred action form.

## What this closes

- The action-form uniqueness question is formally retired as a Resolution-A
  closure path under current accepted premises and retained support.
- The four cluster-obstruction lanes' downstream quantitative range-
  bounding is named explicitly: ~5-10% range across action choices,
  far exceeding ε_witness.
- Reusable negative evidence: future cycles can cite this no-go rather
  than re-deriving the action-form ambiguity from each candidate
  comparison.

## What this does NOT close

- The bridge gap itself. The action-form ambiguity adds a structural
  layer beyond the famous open lattice problem, but does not retire it.
- The thermodynamic ⟨P⟩_HK(6) under the heat-kernel candidate (Block 03
  named obstruction).
- Possible escape routes:
  - **Governance reclassification (Resolution B)**: admit a specific
    action (e.g., Wilson) as scheme convention with narrow non-derivation
    role. Per
    [`BRIDGE_GAP_INDUSTRIAL_SDP_BATTLE_PLAN_2026-05-06.md`](BRIDGE_GAP_INDUSTRIAL_SDP_BATTLE_PLAN_2026-05-06.md)
    + new-physics opening, Resolution B remains a defensive labeling
    option even though the user explicitly de-prioritized it.
  - **Cl(3) ⊗ Cl(3) → Spin(6) ≅ SU(4) embedding**: if the framework's
    actually-derived gauge group is SU(4) ⊃ SU(3) × U(1) (not pure
    SU(3)), the action analysis changes entirely. This is exploratory
    and not yet investigated. (Future block / future loop.)
  - **Externally-supplied non-perturbative input** (industrial SDP at
    L_max ≥ 22 with Mosek): closes the famous open problem at
    ε_witness for ONE specific action choice. Per
    [`BRIDGE_GAP_INDUSTRIAL_SDP_BATTLE_PLAN_2026-05-06.md`](BRIDGE_GAP_INDUSTRIAL_SDP_BATTLE_PLAN_2026-05-06.md)
    this is a $510k / 15mo engineering bet, demoted to fallback by
    the new-physics opening but viable.

## Cross-references

- Predecessor (this loop): [`BRIDGE_GAP_HK_THERMODYNAMIC_STRETCH_NOTE_2026-05-06.md`](BRIDGE_GAP_HK_THERMODYNAMIC_STRETCH_NOTE_2026-05-06.md) (Block 03 stretch + named obstruction)
- Block 02 deliverable: [`BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md`](BRIDGE_GAP_HK_PLAQUETTE_CLOSED_FORM_NOTE_2026-05-06.md) (HK 1-plaq closed form)
- Block 01 deliverable: [`BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06.md`](BRIDGE_GAP_HK_TIME_DERIVATION_NOTE_2026-05-06.md) (HK time)
- New-physics opening: [`BRIDGE_GAP_NEW_PHYSICS_OPENING_NOTE_2026-05-06.md`](BRIDGE_GAP_NEW_PHYSICS_OPENING_NOTE_2026-05-06.md)
- Wilson-as-import: [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
- Sister no-gos: [`BRIDGE_GAP_EXHAUSTED_ROUTES_CONSOLIDATION_NOTE_2026-05-06.md`](BRIDGE_GAP_EXHAUSTED_ROUTES_CONSOLIDATION_NOTE_2026-05-06.md)
- Standard methodology: Drouffe-Zuber 1983 Phys. Rep. 102 ("Strong coupling and mean field methods in lattice gauge theories"); Menotti-Onofri 1981 Nucl. Phys. B190; Helgason 1978 (bi-invariant metrics)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [plaquette_v1_picard_fuchs_ode_minimality_proof_note_2026-05-06](PLAQUETTE_V1_PICARD_FUCHS_ODE_MINIMALITY_PROOF_NOTE_2026-05-06.md)
