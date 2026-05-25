# H_unit Scalar-Singlet Matrix Element Core: y_t_bare = g_bare / sqrt(6)

**Date:** 2026-04-17 (audit-prep refresh: 2026-05-25)
**Status:** bounded support for the core unit-normalized `H_unit` matrix
element on the canonical bare-action surface. This note records the exact
`1/sqrt(6)` scalar-singlet matrix element on the Q_L block within
`A_min = {Cl(3), Z^3}`. It is **not** a derivation of the Standard Model top
Yukawa value, a Planck-surface ratio theorem, or a shared tadpole-transport
closure.
**Claim type:** bounded_theorem author hint; independent audit lane sets the
actual `claim_type`, `audit_status`, and pipeline-derived `effective_status`.
**Admitted context inputs (open-gate dependencies under
`MINIMAL_AXIOMS_2026-05-03.md`):**
- `staggered_dirac_realization_derivation_target` (parent: pending packaging,
  see `MINIMAL_AXIOMS_2026-05-03.md` §"recategorized from axiom to open gate")
- `g_bare_derivation_target` (parent: `G_BARE_DERIVATION_NOTE.md`)
The note conditions on closure of these two derivation targets; they are
explicitly listed as `admitted_context_inputs`, not derived here.
**Primary runner:** `scripts/frontier_yt_ward_identity_derivation.py`
(44 PASS / 0 FAIL on current source).
**Support (NOT part of the authority chain):**
`UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`
documents the perturbative 1-loop vertex correction, which is OPEN
for quantitative lane reuse (not part of this support-tier identification).

---

## Audit boundary

This note identifies only the unit-normalized `H_unit` matrix element on
the Q_L scalar-singlet channel within `A_min = {Cl(3), Z^3}`. The
auditable core is the `1/sqrt(6)` Clebsch-Gordan / normalization result.

**The identification map is not part of the audited core.** In this note
`y_t_bare` is local shorthand for the unit-normalized `H_unit`-to-top-basis
matrix element on the stated Q_L scalar-singlet channel. It is not asserted
here to be the Standard Model Yukawa coupling, and the note does not prove
that the defined matrix element is transported to `y_t(M_Pl)` with the same
tadpole factor as `g_s(M_Pl)`.

This note does **not** claim to derive the numerical Standard Model top
Yukawa value from first principles, to derive the existence of the SM
Yukawa construct independent of this identification, or to supply a
precision prediction after RG running and matching.

**Conditional on the named open gates (g_bare, staggered-Dirac), the
exact algebraic core claim `(T1)` below is runner-verified at machine
precision.** Any Planck-surface tadpole ratio is conditional context, not
the auditable claim of this note.

Prior audit history: the audit lane previously recorded
`audit_status=audited_renaming` for `yt_ward_identity_derivation_theorem`,
cross-confirmed as class E by `codex-fresh-context-20260430-01-yt-ward`
(2026-04-30) and `fresh-agent-popper-019ded72` (2026-05-03). The repeat
finding identifies the load-bearing step as the *definition* of `y_t_bare`
as the H_unit matrix element. This refresh:
1. Tightens scope language so the claim boundary is the core matrix-element
   identity, not the SM Yukawa map or Planck-surface tadpole transport;
2. Replaces the stale `MINIMAL_AXIOMS_2026-04-11.md` citation (now
   superseded) with `MINIMAL_AXIOMS_2026-05-03.md`;
3. Lists `g_bare = 1` and the staggered-Dirac realization as
   `admitted_context_inputs` (open gates) per the restored axiom set;
4. Narrows the claim_type author hint from `open_gate` to
   `bounded_theorem` to match the restored axiom set's per-lane bookkeeping
   rule for quantitative `y_t` results
   (`MINIMAL_AXIOMS_2026-05-03.md`:182-191).

---

## Structural identification (tree-level algebraic support)

On the Cl(3) × Z³ Wilson-staggered lattice with the canonical
bare-action normalization (C1 + C2, `g_bare = 1` at
`β = 2 N_c / g_bare² = 6`), the unit-norm (1,1) scalar composite
`H_unit` on the Q_L = (2,3) block satisfies the exact matrix-element
identity

```
    y_t_bare = g_bare / sqrt(2 N_c) = g_bare / sqrt(6)                 (T1)
```

where `y_t_bare` denotes the `H_unit` matrix element defined in Eq. (3.7).
The equality to `g_bare/sqrt(6)` uses the canonical bare gauge unit
`g_bare = 1`; no physical Yukawa readout is asserted by this notation.

The older Planck-surface ratio statement
`y_t(M_Pl) / g_s(M_Pl) = 1/sqrt(6)` is not part of this note's auditable
core. It requires a separate retained tadpole-transport bridge and a
separate retained physical readout map.

**Scope of this support note:**
- It is the exact tree-level scalar-singlet matrix-element identity only.
- It makes NO quantitative precision claim (no `±%`, no NLO bound,
  no lane budget).
- Perturbative 1-loop corrections, higher-order topology corrections,
  physical Yukawa readout, shared tadpole transport, and any quantitative
  lane reuse are OUT OF SCOPE of this note and are discussed only as
  non-load-bearing context.
- Downstream quantitative reuse of this identity inherits whatever
  systematic the downstream package carries independently. This
  note does not narrow or claim such systematics.

---

## Inputs and dependency table

| # | Input | Status | Source |
|---|-------|--------|--------|
| **AX1** | **Cl(3) local algebra** | **AXIOM** | framework axiom |
| **AX2** | **Z³ spatial substrate** | **AXIOM** | framework axiom |
| D1 | Z³ bipartite → Z₂ parity ε = (-1)^{x+y+z} | DERIVED from AX2 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):14-18 |
| D2 | Staggered fermion η phases on Z³ | DERIVED from D1 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):14-18 |
| D3 | Taste doubling: 2³ = 8 internal species | DERIVED from D2 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):16 |
| D4 | η phases → Cl(3) action in taste space | DERIVED from D3 + AX1 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):17 |
| D5 | Cl(3) ⊃ su(2) → SU(2) weak gauge symmetry | DERIVED from D4 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):18 |
| D6 | Graph-first axis selector on taste cube {0,1}³ | DERIVED from D3 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):52-66 |
| D7 | Residual swap on complementary axes → `su(3)` closure | DERIVED from D6 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):69-75 |
| D8 | Selected nonabelian `(2,3)` block, dim `N_iso N_c = 6` | DERIVED from D5 + D7 | [`NATIVE_GAUGE_CLOSURE_NOTE.md`](NATIVE_GAUGE_CLOSURE_NOTE.md):93-95 |
| D9 | Local scalar-singlet bilinear operator on the Q_L block, `phi = Z^{-1} sum_{alpha,a} psi-bar_{alpha,a} psi_{alpha,a}` | DEFINED in this note from D8 + canonical state normalization | Eq. (1.1), runner Block 2 |
| D10 | Composite 2-point residue `<phi phi>_free = (N_c N_iso / Z²) G_0²` | DERIVED from D9 by explicit index contraction | Eq. (1.2), runner Block 2 |
| D11 | Unit-residue normalization `Z² = N_c N_iso = 6` | DERIVED from D10 | Eq. (1.3), runner Block 2 |
| D12 | Exact SU(N_c) Fierz identity on fundamental generators | STANDARD finite-dimensional Lie-algebra identity | Eq. (3.3), runner Block 4 |
| D13 | Wilson plaquette coupling `β = 2 N_c/g_bare²` at canonical surface | DERIVED from D5 + D7 + standard Wilson action | standard lattice QFT applied to D5, D7 |
| D14 | CMT change-of-variables tadpole identity | NON-LOAD-BEARING CONTEXT for the older Planck-ratio statement | not used in `(T1)` |
| D15 | `n_link` power counting for shared tadpole transport | NON-LOAD-BEARING CONTEXT for the older Planck-ratio statement | not used in `(T1)` |
| C1 | Canonical plaquette / `u_0 = ⟨P⟩^{1/4}` evaluation surface | ADMITTED context input (canonical-surface choice; closure target = staggered-Dirac realization derivation, see `MINIMAL_AXIOMS_2026-05-03.md`:56-93) | `MINIMAL_AXIOMS_2026-05-03.md`:182-191 |
| C2 | `g_bare = 1` on canonical surface | ADMITTED context input (open-gate derivation target; canonical parent: `G_BARE_DERIVATION_NOTE.md`) | `MINIMAL_AXIOMS_2026-05-03.md`:95-136 |
| S1 | SU(3) fundamental Casimir `C_F = (N_c²-1)/(2N_c) = 4/3` | STANDARD Lie-algebra fact | applied to D7 |
| S2 | Lorentz-group Fierz: `(γ^μ)(γ_μ) = c_S(1)(1) + c_P(iγ_5)(iγ_5) + c_V(γ^μ)(γ_μ) + c_A(γ^μγ_5)(γ_μγ_5) + 0·σσ`, with `|c_S| = 1` | STANDARD Clifford-algebra identity | Itzykson-Zuber §2-5; verified by Block 8 of runner |
| D16 | Tree-level Feynman-rule completeness of the bare action on the scalar-singlet channel: at O(α_LM), the bare Cl(3) × Z³ action (Wilson plaquette + staggered Dirac, C1-C2) yields exactly ONE tree diagram contributing to `Γ⁽⁴⁾(q²)` on the color-singlet × iso-singlet × Dirac-scalar channel — the single-gluon-exchange diagram, projected via D12 + S2 with coefficient (3.5) | DERIVED from tree-level Feynman rules of the cited action + the absence of any fundamental scalar field or bare contact 4-fermion vertex in the bare action | framework-native; follows from `MINIMAL_AXIOMS_2026-05-03.md`:32-43 + D9 |
| D17 | Scalar-singlet operator uniqueness on the Q_L block: the unique unit-normalized (Z² = 6) color-singlet × iso-singlet × Dirac-scalar operator on Q_L = (2,3) is `H_unit = (1/√(N_c · N_iso)) Σ ψ̄ψ`. Other (1,8), (3,1), (8,3) irreps give `Z² = 8, 9/2, 24` respectively (Block 5 verified) — each distinct from `Z² = 6`, hence none are the scalar singlet on this block | DERIVED and numerically verified (Block 5) | D9-D11 plus runner Block 5 |

The only AXIOMS are AX1 (Cl(3)) and AX2 (Z³). The remaining inputs are
the framework chain (D1-D17), a CANONICAL NORM CHOICE (C1, C2), or a
STANDARD group-theoretic identity (S1, S2) that is independent of
framework content. S1 and S2 are properties any SU(N_c) gauge theory in
4D with Dirac fermions must respect — they are not framework axioms.
**There is no separate "matching axiom" in this note.** The bare-action
1PI Green's function `Γ⁽⁴⁾` on the scalar-singlet channel is computed two
algebraically equivalent ways within the same cited framework surface:
directly from Feynman rules (D16 → OGE only at O(α_LM)) and via
the composite operator `H_unit` (D17 → unique scalar singlet on
Q_L). The two evaluations of the same Green's function must agree;
that algebraic identity gives `y_t_bare² = g_bare²/(2 N_c)`.

---

## Structural identification fact: no physical Yukawa map is claimed

The core claim uses `y_t_bare` only as a local label for the matrix
element of the unit-normalized scalar-singlet operator `H_unit` on the
specified top-basis component of Q_L. It does not require, and does not
assert, an independent derivation of the Standard Model Yukawa readout.

The bare-action context still contains only the Wilson plaquette and
staggered Dirac operator. That observation is used here only to motivate
the same-1PI scalar-singlet consistency check in Step 3. The auditable
core remains the direct operator normalization and matrix element in
Steps 1-2 and Eq. (3.8).

---

## Structural calculation

### Step 1: Canonical kinetic normalization of phi on the Q_L block

Extend D9's color-only form to the full Q_L block (D8) by including the
isospin index α:

```
    phi(x) = (1/Z) * sum_{α,a} psi-bar_{α,a}(x) psi_{α,a}(x)           (1.1)
```

Compute `<phi(x) phi(y)>_{conn,free}` using D10's formula + the free
propagator δ_{αβ} δ_{ab} G_0(x,y):

```
    <phi(x) phi(y)>_{conn,free} = -(N_c · N_iso / Z²) · G_0(x,y)²      (1.2)
```

Canonical unit-residue (absorbing the fermion-loop sign):

```
    Z² = N_c · N_iso = 6  →  Z = sqrt(6)                              (1.3)
```

### Step 2: Clebsch-Gordan overlap of the unit-norm singlet

The (1,1) singlet state in the Q_L ⊗ Q_L* bilinear Hilbert space
(dim = 36), unit-normalized, is

```
    |S> = (1/sqrt(6)) * sum_{α,a} |α,a> ⊗ |α,a>*                      (2.1)
```

The top-channel basis bilinear `|top-pair> = |up, top-color> ⊗ |up, top-color>*`
has overlap

```
    <top-pair | S> = 1/sqrt(6)                                        (2.2)
```

(same for each of the 6 basis components, by singlet uniformity).

### Step 3: Same-1PI-function residue check (scalar-singlet channel)

This step records the load-bearing identity entirely within the
cited Cl(3) × Z³ framework surface, as a single 1PI Green's function
computed two ways. There is no UV-vs-EFT matching, no second
"effective theory" to be defined; only one theory, one Green's
function, two algebraically equivalent representations of it.

**Object of the check.** Define the amputated, 1PI, color-singlet
× iso-singlet × Dirac-scalar-scalar projection of the four-fermion
Green's function on the Q_L block:

```
    Γ⁽⁴⁾(q²) := P_{S,(1,1)} · ⟨ψ̄ψ(q) ψ̄ψ(-q)⟩_{1PI,amp}            (3.1)
```

where `P_{S,(1,1)}` projects onto the single channel
`O_S = (ψ̄ψ)_{(1,1)} (ψ̄ψ)_{(1,1)}` — color-singlet, iso-singlet,
Dirac-scalar on both bilinears. **Only this one channel is the
subject of the note; no other Dirac or representation channel is
claimed.**

**Representation A — direct OGE computation in the bare action.**

The cited bare action contains only the Wilson plaquette and the
staggered Dirac operator (D16, `MINIMAL_AXIOMS_2026-05-03.md`:32-43; conditional on staggered-Dirac realization gate, see :56-93) — no
fundamental scalar field, no contact 4-fermion operator. At tree
order in α_LM, the only Feynman diagram contributing to `Γ⁽⁴⁾(q²)` is
single-gluon exchange:

```
    Γ⁽⁴⁾(q²)|_OGE = -(g_bare² / q²) · Σ_a (T^a)_{ij}(T^a)_{kl}
                                    · (γ^μ)_{αβ}(γ_μ)_{γδ}        (3.2)
```

Project onto `O_S`: apply the exact SU(N_c) color-singlet Fierz
identity (D12, verified machine-precision by Block 4):

```
    Σ_a (T^a)_{ij}(T^a)_{kl}|_{δ_{ij}δ_{kl} channel} = -1/(2 N_c)  (3.3)
```

and the exact Lorentz-Clifford scalar projection (S2,
verified machine-precision by Block 8: `|c_S| = 1`):

```
    (γ^μ)_{αβ}(γ_μ)_{γδ}|_{(1)_{αβ}(1)_{γδ} channel} = c_S         (3.4)
```

Substituting (3.3) and (3.4) into (3.2):

```
    Γ⁽⁴⁾(q²)|_OGE = -c_S · g_bare² / (2 N_c · q²) · O_S            (3.5)
```

This is the COMPLETE tree-order value of `Γ⁽⁴⁾` from the bare
action: no other tree diagram contributes (D16 = Feynman-rule
completeness of the cited Wilson-staggered + plaquette action).

**Representation B — direct matrix-element computation of the local
`y_t_bare` shorthand from the H_unit operator content.**

The local scalar-singlet operator definition (D9) defines `H_unit`
on the Q_L block:

```
    H_unit(x) := (1/√(N_c · N_iso)) · Σ_{α,a} ψ̄_{α,a}(x) ψ_{α,a}(x)
              =  (1/√6) · (ψ̄ψ)_{(1,1)}(x)                          (3.6)
```

with the canonical normalization `Z = √6` derived in Step 1 and
shown UNIQUE in Step 2 / Block 5 (D17): `H_unit` is the only
unit-normalized scalar bilinear operator on the Q_L block with
`Z² = N_c · N_iso = 6`.

**Local definition of y_t_bare via the H_unit-to-top-basis matrix element.**
On the canonical surface (`g_bare = 1`) this note uses `y_t_bare` as
local shorthand for the unit-norm-state matrix element of the H_unit
operator between the vacuum and a single top-pair basis state in the
(color = top-color, iso = up) component of the Q_L block:

```
    y_t_bare := ⟨0 | H_unit(0) | t̄_{top,up} t_{top,up}⟩            (3.7)
```

> **Identification-map boundary (audit-prep clarification, 2026-05-25).**
> Equation (3.7) is a local notation definition for this source note. The
> claim boundary is only that the defined matrix element satisfies `(T1)`.
> Whether this matrix element coincides with the Standard Model top-Yukawa
> observable, or transports to `M_Pl` with the same tadpole factor as the
> gauge vertex, is a separate downstream question. The prior
> `audited_renaming` verdicts correctly identified that the SM map was
> not derived; this refresh removes that map from the auditable core.

Computing this matrix element directly from (3.6):

```
    y_t_bare = (1/√(N_c · N_iso)) · ⟨0 | ψ̄_{top,up} ψ_{top,up}(0)
               | t̄_{top,up} t_{top,up} ⟩
            = (1/√6) · 1
            = 1 / √6                                                (3.8)
```

The first factor (1/√6) is the Clebsch-Gordan weight from (3.6).
The second factor (= 1) is the unit-amplitude Wick contraction of
the bilinear `ψ̄ψ` with the corresponding fermion-pair external
state in canonical fermion normalization — a kinematic identity,
not a dynamical input.

**This evaluation uses ONLY:**
- the explicit operator content of H_unit (3.6) — Clebsch-Gordan
  weight 1/√(N_c · N_iso), from D17 + Steps 1-2;
- canonical fermion-state normalization;
- canonical scalar-composite normalization (Step 1, Z = √6).

It uses **no** information about OGE, no gauge coupling, no
4-fermion coefficient, no matching rule. It is a direct evaluation
of a matrix element of a defined composite operator on a defined
external state.

**Compute Γ⁽⁴⁾(q²)|_H_unit-rep from (3.8) independently.** Tree-level
H_unit-mediated contribution to the same Green's function, with
H_unit Yukawa vertices given by (3.8) on each side:

```
    Γ⁽⁴⁾(q²)|_H_unit-rep = -y_t_bare² / q² · O_S
                         = -(1/√6)² / q² · O_S
                         = -1 / (6 · q²) · O_S                      (3.9)
```

in the tree-level scalar-singlet residue normalization used by this
source note.

**The same-1PI-function consistency identity.**

Representations (A) and (B) are now two INDEPENDENT computations
of the same Green's function `Γ⁽⁴⁾(q²)` in the same cited framework surface:
- (A) is computed from gauge-theory Feynman rules (OGE diagram
  + color/Dirac Fierz projection).
- (B) is computed from the H_unit operator's matrix element with
  the external top state (Clebsch-Gordan + canonical normalization).

Each is computed WITHOUT reference to the other. Comparing:

```
    Γ⁽⁴⁾_A = -c_S · g_bare² / (2 N_c · q²) · O_S
           = -1 · 1² / 6 / q² · O_S    (at canonical g_bare = 1, |c_S| = 1)
           = -1 / (6 q²) · O_S                                       (3.10)

    Γ⁽⁴⁾_B = -1 / (6 q²) · O_S      (3.9 above)                     (3.11)
```

The two values agree at the canonical surface (g_bare = 1). This
agreement is a non-trivial consistency check of the cited framework surface:
the bare action's gauge dynamics (Representation A) and the
operator content of `H_unit` (Representation B) give
the same Green's function on the load-bearing scalar-singlet
channel.

**The local matrix element y_t_bare = 1/√6 is therefore defined and
evaluated** from H_unit operator content (3.7-3.8). The
agreement (3.10 = 3.11) confirms internal consistency of the
framework but is not the source of the value.

**Inputs used (cited framework inputs plus exact group-theoretic identities):**

1. The bare Cl(3) × Z³ lattice action
   (`MINIMAL_AXIOMS_2026-05-03.md`:32-43; conditional on staggered-Dirac and `g_bare = 1` derivation gates) — contains exactly Wilson plaquette and
   staggered Dirac, no fundamental scalar, no contact 4-fermion.
2. D9-D11: local scalar-singlet operator definition and unit-residue
   normalization on the Q_L block, derived in Steps 1-2 and runner
   Block 2.
3. D16: Feynman-rule completeness of the bare action — at O(α_LM)
   only the OGE diagram contributes to `Γ⁽⁴⁾`.
4. D17: scalar-uniqueness of `H_unit` on the Q_L block (Z² = 6 is
   unique among (1,1) Dirac-scalar composites; verified by Block 5
   numerically against the (1,8), (3,1), (8,3) alternatives).
5. SU(N_c) color-singlet Fierz coefficient `-1/(2 N_c)` (D12,
   exact SU(N_c) identity, Block 4 verified to machine precision).
6. Lorentz-Clifford scalar projection coefficient `|c_S| = 1`
   (S2, exact Clifford-algebra identity, Block 8 verified).
7. No physical IR scale separation or Standard Model matching statement
   is load-bearing for `(T1)`.

There is no second theory, no matching rule, no auxiliary mass
freedom, no spectral assumption. The note records only that one
1PI Green's function on the Q_L scalar-singlet channel equals
itself when computed two algebraically equivalent ways.

### Step 4: Non-load-bearing canonical-surface ratio context

This section records the historical tadpole-ratio context only. It is
not part of the auditable `(T1)` claim and does not import the older
tadpole-transport rows as one-hop dependencies for this core matrix-element
repair.

If a later retained tadpole-transport bridge supplies the shared
single-link dressing for both the scalar-singlet matrix element and the
gauge vertex, then the Wilson gauge coupling on the canonical surface
would be written:

```
    g_s(M_Pl) = sqrt(4 pi alpha_LM) = g_bare / sqrt(u_0)              (4.1)
```

with `alpha_LM = alpha_bare / u_0`.

Under that additional, non-load-bearing premise, the matrix element
(3.8) would inherit the same `1/sqrt(u_0)` factor:

```
    y_t(M_Pl) = y_t_bare / sqrt(u_0)
              = (g_bare / sqrt(6)) / sqrt(u_0)
              = g_s(M_Pl) / sqrt(6)                                   (4.2)
```

and the ratio would be:

```
    y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)                               (4.3)
```

Equation (4.3) is conditional context only in this revision. It is not
claimed as audited support by this note.

### Boundary of the identification

```
    y_t_bare = g_bare / sqrt(6)              (T1, exact matrix-element algebra)
```

This is the exact algebraic identity on the stated canonical bare-action
surface. `y_t_bare` here is the source-note shorthand for the matrix
element in Eq. (3.7), not the SM observable; see the identification-map
boundary clarification following Eq. (3.7).

No precision bound, no NLO claim, no systematic is attached to this
identification. Perturbative and higher-order corrections are out of scope
and are discussed in the support note
`UV_GAUGE_TO_YUKAWA_BRIDGE_SC_VS_PERT_NOTE.md`.
Downstream quantitative reuse carries whatever systematic the
downstream package carries independently; the note does not
narrow that.

This is a framework-native scalar-singlet matrix-element calculation within
`A_min = {Cl(3), Z^3}` plus the named open-gate `admitted_context_inputs`
(staggered-Dirac realization, `g_bare = 1`), using the chain D1-D13,
D16-D17, exact SU(N_c) / Clifford algebra, and canonical normalization
choices C1-C2. No new axioms. No framework conventions beyond canonical
normalization. No package-status-doc imports.

---

## Scale/scheme statement

What is identified where:

1. **On the canonical bare-action surface**: the source-note matrix
   element `y_t_bare := <0 | H_unit | t-bar t>` equals
   `g_bare/sqrt(6)` when `g_bare = 1` is used as the canonical bare gauge
   unit.

2. **At M_Pl or v**: no physical Yukawa value, RGE bridge, color-readout
   correction, or shared tadpole transport is claimed by this note. The
   retained no-go row for `yt_color_projection_correction_note` remains
   compatible with this boundary because no `sqrt(8/9)` Yukawa correction
   is imported here.

3. **No blanket equality** is claimed across bare, Planck, and matching
   schemes; only the bare scalar-singlet matrix element is identified.
