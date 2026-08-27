---
claim_id: admissibility_dirac_kahler_plaquette_holonomy_connection_curvature_bounded_theorem_note_2026-08-27
final_path: docs/ADMISSIBILITY_DIRAC_KAHLER_PLAQUETTE_HOLONOMY_CONNECTION_CURVATURE_BOUNDED_THEOREM_NOTE_2026-08-27.md
claim_type: bounded_theorem
claim_scope: "Exact closed-loop decomposition of the normalized natural exterior links from Block 216: endpoint coframes and volume densities telescope, leaving the exterior lift of the ordered orthogonal edge product; proof that the endpoint-only R=I section is flat on arbitrary positive cells; faithfulness of full exterior holonomy to tangent holonomy; a positive base-point-invariant D3 plaquette defect that vanishes exactly at identity holonomy; and exact coexistence of nontrivial holonomy with the Block 215 weighted-skew operator. The orthogonal edge factors are supplied. Their physical selection, a plaquette action, time interpretation, gravity dynamics, and continuum limit remain separate questions."
runner: scripts/admissibility_dirac_kahler_plaquette_holonomy_connection_curvature_2026_08_27.py
status: proposed_retained
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_metric_compatible_exterior_transport_bounded_theorem_note_2026-08-27
target_blocker_text: "plaquette holonomy/curvature decomposition"
source_of_blocker_text: proof_obligation_graph
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Derive or discriminate a framework-native local selection/dynamics law for the orthogonal edge factors, then test the resulting same-action operator at the OS/Lorentzian interface."
conditional_surface_status: "stacked on unmerged Blocks 214-216; proposed science remains review- and audit-required"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "the loop telescoping, exterior functoriality, faithfulness, gauge/base-point covariance, and positive defect identities are exact finite-dimensional theorems with rational witnesses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
parent_ref: origin/physics-loop/toe-metric-dynamics-bridge-block216-compatible-exterior-transport-20260827
parent_commit: 2e74d557fc16db52d57c598491735ca302d185de
current_main: 66e478505e055faf4a5b9e6f4883211e44304718
registered: 0
adopted: 0
axiom_movement: none
---

# Plaquette holonomy, connection curvature, and the remaining dynamics gate

**Date:** 2026-08-27

**Type:** `bounded_theorem`

**Status:** `proposed_retained` — a review proposal, not an audit verdict.

## Result in plain language

The [metric-compatible exterior-transport theorem](ADMISSIBILITY_DIRAC_KAHLER_METRIC_COMPATIBLE_EXTERIOR_TRANSPORT_BOUNDED_THEOREM_NOTE_2026-08-27.md)
factorized every compatible tangent edge map as

```text
A_sr = E_s^-1 R_sr E_r
```

and constructed its normalized natural exterior link. This note composes
those links around a closed plaquette. Every endpoint coframe cancels its
neighbor, and every volume-density factor cancels around the loop. At base
site zero, the exact tangent and exterior holonomies are

```text
H_A = E_0^-1 W_R E_0,
H_U = Lambda(H_A),
W_R = R_01 R_12 R_23 R_30.                         (1)
```

For the section `R_sr=I`, equation (1) evaluates to `H_A=I_3` and `H_U=I_8`
for arbitrary endpoint metrics. A nonidentity ordered product `W_R` gives a
nonidentity compatible exterior holonomy. The degree-one block of `H_U` is
`H_A`, so `H_U=I_8` implies `H_A=I_3`.

The result locates the discrete curvature carrier at the kinematic level. It
also supplies a positive, coframe-gauge and base-point-invariant plaquette
defect from the existing positive D3 carrier. That scalar is one possible
building block; physical action selection remains an open follow-on task.

## Orientation and hypotheses

Use a four-site loop with oriented edge representatives

```text
(0,1), (1,2), (2,3), (3,0).
```

The block `A_sr` maps one-form coefficients at `r` into the coordinates at
`s`. Therefore the displayed product in (1), read right to left, transports
from site zero through `3,2,1` and back to zero.

The hypotheses are:

1. four positive three-dimensional metrics on the Block 216 metric-volume
   locus, with chosen coframes `g_s^-1=E_s^T E_s`;
2. one supplied orthogonal edge factor `R_sr` per oriented edge;
3. the normalized natural exterior links
   `U_sr=sqrt(V_r/V_s)Lambda(A_sr)`;
4. closed-loop composition using all four links.

Existing [Lattice adjacency](MINIMAL_AXIOMS_2026-06-29.md#lattice--physical-locality)
supplies the local loop domain. Edge-factor and plaquette-action selection are
open follow-on tasks. No new axiom or primitive is introduced.

## Exact telescoping theorem

Substitute the Block 216 factorization into the ordered tangent product:

```text
A_01 A_12 A_23 A_30
= E_0^-1 R_01 E_1 E_1^-1 R_12 E_2
  E_2^-1 R_23 E_3 E_3^-1 R_30 E_0
= E_0^-1 W_R E_0.                                  (2)
```

The scalar density around the same closed loop is

```text
sqrt(V_1/V_0) sqrt(V_2/V_1)
sqrt(V_3/V_2) sqrt(V_0/V_3) = 1.                   (3)
```

Because the exterior lift is functorial,

```text
U_01 U_12 U_23 U_30
= Lambda(A_01 A_12 A_23 A_30)
= Lambda(E_0^-1 W_R E_0).                          (4)
```

Each edge link is an isometry between its endpoint D3 carriers, hence the
closed product is a base-carrier isometry:

```text
H_U^T D_0 H_U = D_0.                                (5)
```

Equations (2)–(5) prove the loop theorem without a continuum approximation.

## Flat endpoint section and nontrivial connection section

If every `R_sr=I`, then `W_R=I`, so (2) and (4) give

```text
H_A=I_3,       H_U=I_8.                             (6)
```

This statement is deliberately narrow: the endpoint-factorized section is
flat. A future dynamical connection may relate curvature to changing metrics;
equation (6) classifies only the displayed section.

If `W_R` is nonidentity, then `H_A` is nonidentity by conjugacy. The degree-
one block of the natural exterior lift is exactly `H_A`; therefore

```text
H_U=I_8  if and only if  W_R=I_3.                   (7)
```

This faithfulness turns the orthogonal edge product into an exact discrete
curvature carrier for the normalized natural-link sector. Additional
module-commutant factors excluded from Block 216 could carry additional
holonomy and are outside (7).

## Positive D3 plaquette defect

For a base-site endomorphism `X`, use the D3 adjoint

```text
X^dagger_D0 = D_0^-1 X^T D_0.
```

Define the plaquette defect

```text
Q_p := Tr[(H_U-I)^dagger_D0 (H_U-I)].               (8)
```

Positivity of `D_0` gives

```text
Q_p >= 0,       Q_p=0 if and only if H_U=I.         (9)
```

Using the isometry (5), the same scalar is

```text
Q_p = 16 - Tr(H_U) - Tr(H_U^-1).                   (10)
```

It depends only on the holonomy conjugacy class. Moving the base point
cyclically conjugates `H_U` by the intervening compatible link, so `Q_p` is
base-point independent. Replacing coframes by `E_s -> Q_s E_s` and edge
factors by

```text
R_sr -> Q_s R_sr Q_r^T                              (11)
```

leaves every `A_sr` and `H_U` fixed while sending
`W_R -> Q_0 W_R Q_0^T`.

For the exact flat-carrier one-rotation control with one `3/5,4/5` plane
rotation,

```text
Tr Lambda(W_R) = 32/5,
Q_p = 16/5.                                         (12)
```

The zero endpoint-only control gives `Q_p=0` exactly. Equation (8) is one
derived diagnostic from the existing carrier. Physical action selection among
functions of the same conjugacy data remains a follow-on task.

## Orientation reversal and base point

Reversing the loop uses the inverse edge maps in reverse order, hence

```text
H_A(reverse) = H_A^-1,
H_U(reverse) = H_U^-1.                              (13)
```

Starting at site one instead gives

```text
H_A(1) = A_01^-1 H_A(0) A_01,
H_U(1) = U_01^-1 H_U(0) U_01.                       (14)
```

These are exact finite covariance statements, not continuum gauge-field
assumptions.

## Coexistence with the weighted-skew operator

For each plaquette edge, choose a direction `q` at the right endpoint. Block
216 gives the compatible cross-form

```text
C_sr(q) = D_s Gamma_s(A_sr q) U_sr/2
        = U_sr^-T D_r Gamma_r(q)/2.                 (15)
```

Using (15) for the forward block and the forced Block 215 transpose for the
reverse block produces a global four-site operator satisfying

```text
H K + K^T H = 0                                     (16)
```

even when `W_R` and `H_U` are nonidentity. Thus nontrivial compatible
holonomy coexists exactly with the weighted-skew bridge already proved.

## Exact witnesses and mutations

The runner uses four unequal rational coframes and three noncommuting rational
Pythagorean rotations. It checks:

- every edge tangent metric and exterior-carrier isometry;
- tangent, density, and exterior telescoping;
- endpoint-only identity holonomy and nontrivial connection holonomy;
- exterior faithfulness and the positive D3 defect;
- exact single-angle values in (12);
- coframe gauge covariance, cyclic base-point covariance, and reversal;
- compatibility of nontrivial holonomy with the global weighted-skew
  plaquette operator.

Three declared mutations isolate the load-bearing loop structure:

1. dropping the closing link destroys closed-loop telescoping;
2. reversing the noncommuting connection-product order destroys (2);
3. breaking one density factor destroys the density cocycle and carrier
   isometry.

## Proof-obligation graph

| Obligation | Disposition |
|---|---|
| compatible single-edge exterior link | supplied by Block 216 and rechecked on each witness edge |
| closed tangent/coframe telescoping | proved by equation (2) |
| density cancellation and exterior composition | proved by equations (3)–(4) |
| endpoint-only flat section | proved by equation (6) and exact unequal-cell control |
| faithfulness to orthogonal product | proved by the degree-one block, equation (7) |
| positive gauge/base-point-invariant defect | proved by equations (8)–(11) and exact controls |
| weighted-skew operator coexistence | proved by equations (15)–(16) and exact four-site assembly |
| selection/dynamics of `R_sr` | open; not imported or renamed |
| physical curvature action | open; `Q_p` supplies one exact diagnostic while action selection is deferred |
| OS/Lorentzian time and continuum gravity | downstream physical bridge |

The proof graph is acyclic. Loop holonomy is a genuinely new object relative
to the single-edge theorem. The next gate is a framework-native law that
selects or evolves the orthogonal edge factors and couples that law to the
same operator used for matter/time reconstruction.

## TOE bridge status after this block

The three-block campaign now supplies an exact finite kinematic chain:

```text
local positive metric/Clifford cell
  -> all variable-cell weighted-skew edge couplings
  -> metric/Clifford-compatible natural transport
  -> faithful plaquette holonomy and positive curvature diagnostic.
```

That is real kinematic bridge progress. A completed theory of everything
additionally requires a local framework-native selection/dynamics law for
`R_sr`. The next coupled obligation is to test that same-action system at the
OS/Lorentzian interface and establish its physical-time interpretation.
Existing Lattice adjacency remains the sole axiom-level input here; no new
axiom, primitive, empirical value, fitted parameter, or external field
equation is introduced.
