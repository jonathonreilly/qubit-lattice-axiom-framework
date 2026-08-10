---
claim_id: admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "For the retained flat four-coframe unit-hyperface action, the four orientation-resolved area Hessians are exact rank-nine Hermitian forms on the ten symmetric metric entries. Pulling them through the repository-local flat metric-to-edge map onto the six Block-23 physical modes gives four linearly independent full-rank seagull matrices. Strictly positive orientation weights realize all three target inertia classes 3-/3+, 4-/2+, and 2-/4+, and a source-linear action contributes at the required O(source) order. Nevertheless, at the supplied generic physical direction none of the three reconstructed sourced Regge mass coefficients lies in the entire real homogeneous four-orientation span: best unconstrained Frobenius residuals exceed 0.89 relative and operator residuals exceed 0.77. This is a bounded flat homogeneous carrier-span result, not a contact-term, coframe, source-law, Regge-gravity, continuous-zone, Lorentzian, nonlinear, axiom-necessity, or axiom-adoption no-go."
upstream_dependencies:
  - minimal_axioms
  - admissibility_sourced_regge_joint_ward_schur_completion_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_surface_coframe_stress_higher_form_ward_geometry_dynamics_boundary_bounded_theorem_note_2026-08-10
  - admissibility_cut_worldvolume_affine_bag_regge_monopole_boundary_bounded_theorem_note_2026-08-10
runner: scripts/admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py
---

# Four-Coframe Hyperface Seagull / Sourced-Regge Span Boundary

**Date:** 2026-08-10
**Type:** `bounded_theorem`
**Role:** execute Block 23's strongest direct-contact route on the retained
four-coframe carrier.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.

**Primary runner:**
[admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py](../scripts/admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py)

**Retained dependency surface:**
[minimal axioms](MINIMAL_AXIOMS_2026-06-29.md),
[Block 23 joint-Ward boundary](ADMISSIBILITY_SOURCED_REGGE_JOINT_WARD_SCHUR_COMPLETION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md),
[cut-coframe same-family response](ADMISSIBILITY_CUT_SURFACE_COFRAME_STRESS_HIGHER_FORM_WARD_GEOMETRY_DYNAMICS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md), and
[four-coframe worldvolume carrier](ADMISSIBILITY_CUT_WORLDVOLUME_AFFINE_BAG_REGGE_MONOPOLE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md).

## 1. Result Up Front

Block 23 proved that the unwanted six-mode sourced Regge coefficient is
algebraically repairable, but an ordinary decoupled Schur sector contributes
one coupling order too late. Its strongest live alternative was a direct
same-action Ward/contact term. The retained four-coframe worldvolume and
cut-coframe response supply a concrete carrier on which to test that route.

For a flat four-coframe `E=I` define the oriented unit-hyperface areas

```text
A_mu(E)=|cof(E)e_mu|,  mu=0,1,2,3.                         (1)
```

Use the symmetric coframe convention `delta E=h/2`, so the induced metric
variation is `delta g=h`. The four exact Hessians

```text
Q_mu = d^2 A_mu(I+s h/2)/ds^2 |_(s=0)                    (2)
```

are rank nine on the ten symmetric metric entries, each with inertia
`5-/4+/1-zero`.

Pull (2) through the exact flat Regge metric-to-edge map and restrict to the
same six physical modes used in Blocks 22--23. The four resulting Hermitian
forms `P_mu` are all full rank and linearly independent. They have three
important properties:

1. A source-linear hyperface action contributes `c sum q_mu P_mu` at the
   **correct O(c) order**. It does not require Block 23's auxiliary rank jump.
2. Strictly positive weights `q_mu` realize every target inertia class:
   `3-/3+`, `4-/2+`, and `2-/4+`. There is no signature-only obstruction.
3. None of the three required matrices `M_s` belongs to the complete real
   homogeneous **four-orientation span** of the `P_mu`, even when weights may
   have either sign. Best relative residuals are:

| source tangent | Frobenius residual | operator residual |
|---|---:|---:|
| two-stream | `0.964348...` | `1.047123...` |
| Bundle A | `0.895781...` | `0.793555...` |
| Bundle B | `0.912270...` | `0.772399...` |

Thus this carrier passes the coupling-order and inertia tests but fails the
actual tensor-matching test by large margins. The missing ingredient is not
merely “some seagull.” It must add tensor directions beyond the four
homogeneous unit-hyperface areas: connected covariance, site-dependent
coframes, a geometry-dependent additive zero, the full nonstationary Ward
connection, a different local carrier, or a combination of these.

No canonical axiom is edited. Fixed TOE percentages do not move. This is not
a contact-term no-go.

## 2. Exact Hyperarea Hessian

Delete column `mu` from `E` and call the resulting `4 x 3` matrix `V_mu`.
Then

```text
A_mu(E)=sqrt(det(V_mu^T V_mu)).                            (3)
```

For `E(s)=I+sX`, write `d(s)=det(V_mu(s)^T V_mu(s))`. Since
`d(0)=1`,

```text
A_mu''(0)=d''(0)/2-d'(0)^2/4.                             (4)
```

The runner evaluates (4) with exact rational symbolic arithmetic on all ten
symmetric metric basis entries and polarizes it to obtain every matrix entry
of `Q_mu`. Each exact matrix has rank nine and inertia `5-/4+/1-zero`.

The one null direction is not interpreted as physical gauge content. It is a
property of one hyperface area at one flat coframe.

## 3. Pullback To The Six Physical Regge Modes

Let `M_0` be the repository's exact flat line-averaged map from ten symmetric
metric entries to fifteen edge-length entries. Let `U_6` be Block 23's
orthonormal six-mode physical basis. The runner solves

```text
M_0 H_6 = U_6.                                             (5)
```

The residual is below `1e-12`, and `H_6` has rank six. Define

```text
P_mu = H_6^dagger Q_mu H_6.                               (6)
```

All four `P_mu` are full rank. Their real Hermitian vectorizations form a
rank-four design matrix with singular values

```text
2.102016..., 1.937259..., 1.438199..., 1.143544....       (7)
```

Equation (6) uses the same supplied generic direction
`(1,0.7,-0.4,0.2)` that defines the Block-22 infrared kinetic and source
coefficients. It is a single-direction flat test, not a continuous-zone
theorem.

## 4. Positive Signature Flexibility

The test enumerates a deterministic positive integer grid of orientation
weights. It finds strictly positive combinations with each source-matrix
inertia:

```text
inertia(sum_mu q_mu P_mu) in {3-/3+, 4-/2+, 2-/4+}.       (8)
```

This is the necessary counter-control. A comparison of inertia alone would
incorrectly declare the direct-contact route complete. The eigenvectors and
relative matrix entries matter.

The weights in (8) are mathematical controls. They are not selected cut
densities, source probabilities, or action coefficients.

## 5. Complete Homogeneous-Span Fit

Vectorize a complex Hermitian matrix by concatenating all real and imaginary
entries. For each source tangent solve the unconstrained real least-squares
problem

```text
min_(q in R^4) ||vec(M_s)-sum_mu q_mu vec(P_mu)||_2.       (9)
```

The design rank is four, while appending any `M_s` raises the rank to five.
Therefore no exact real weights exist. Because (9) already permits negative
weights, imposing physical positivity cannot repair the mismatch. Reversing
the overall contact sign also leaves membership and relative distance to the
span unchanged.

The smallest relative Frobenius residual is above `0.89`; the smallest
relative operator residual is above `0.77`. These order-one gaps make the
bounded numerical conclusion insensitive to floating-point tails. They are
not interval certificates, and no exact algebraic nonmembership claim is
made for the reconstructed double-precision `M_s`.

## 6. Coupling Order And Ward Meaning

For a source-linear action contribution

```text
S_face(c,E)=c sum_mu q_mu A_mu(E),                         (10)
```

the direct geometry contact is

```text
d_E^2 S_face(c,I)=c sum_mu q_mu Q_mu.                      (11)
```

This is a **direct source-linear contact** at `O(c)`. It avoids the regular
Schur order boundary because it changes the geometry block itself rather than
integrating out a decoupled auxiliary sector.

For the normalized cut family, the complete response is

```text
Psi''=Cov(S',S')-E[S''].                                  (12)
```

This block tests only the local hyperarea part of `E[S'']` under homogeneous
orientation totals. It does not test the connected covariance in (12),
source-dependent configuration weights, spatially varying coframes, or the
term `S_a partial_b R^a` in the differentiated joint Ward identity. Those
terms can add matrix directions absent from (6).

## 7. Exact Axiom/Convention Consequence

The current axioms do not select the four-coframe family, action unit,
geometry-dependent additive normalization, source coordinate, or joint
transformation law. The candidate interface sharpened by this result is:

> **Complete same-action contact candidate (unadopted).** A selected local
> geometry/history law supplies one geometry-dependent joint action, its
> action unit and geometry-dependent additive zero, and the transformations
> of every source and constraint variable. On a selected background, the
> complete differentiated Ward identity includes the connected, contact,
> mixed, source, multiplier, and generator-connection terms. Its physical
> quotient must match the full required `O(k^0)` tensor—not only its rank or
> inertia—before the derived massless `O(k^2)` pole. A massive or curved phase
> derives its scale, constraints, causal signature, and stability from the
> same law.

This wording is sufficient or target-equivalent, unadopted, and not proved
necessary or minimal. A downstream model law may supply it without editing a
canonical axiom.

## 8. TOE Consequence

| lane | progress | remaining condition for movement |
|---|---|---|
| gravity / source / resources | executes the strongest Block-23 direct-contact route; proves correct order and signature flexibility; rejects the minimal homogeneous four-span by large matrix residuals | derive the complete same-action connected/contact/connection tensor on a selected nonuniform background |
| inertia / matter | shows matrix inertia is too coarse to identify the required source response | physical source degrees, constituent-causal matter, and stable dressed inertia |
| causal time | keeps causal interpretation separate from Euclidean seagull inertia | selected Lorentzian history/update and stability law |
| operational quantum / records | no direct closure | physical family/program registration and occurrence |
| Born / history | history carrier remains supplied | selected functional/program and realized history |

This is significant localization inside the gravity lane, not retirement of a
current-axiom physical obligation. Fixed percentages remain unchanged.

## 9. No-Go Discipline Gate

The only bounded negative eligible to ship is:

> At the supplied generic flat direction, under the symmetric-coframe
> convention and exact flat Regge metric carrier, none of the three named
> sourced six-mode mass matrices lies in the homogeneous real span of the four
> unit-hyperface area seagulls.

N1--N8 status: `PASS` only for that carrier-span statement.

### N1 — materially distinct routes

| route | executed outcome |
|---|---|
| homogeneous four-hyperface seagull | correct `O(c)` order and all target inertias; full tensor fit fails with large residuals |
| connected covariance | live; excluded from the four-span by construction |
| site-dependent coframe/contact | live; can add Fourier and orientation structure beyond four homogeneous totals |
| geometry-dependent additive zero | live; its Hessian changes the contact tensor and must be physically fixed |
| nonstationary generator connection | live; `S_a partial_b R^a` is not a hyperarea Hessian |
| mixed/singular source sector | Block 23 constructs the coefficient route; physical law remains open |
| alternate hypercells/coframes/carriers | live; no carrier exhaustion is claimed |
| selected massive/curved phase | live; need not cancel `M_s` |

### N2 — wall independence

`W_order` (first source order), `W_signature` (inertia), `W_tensor` (full
matrix), `W_local` (selected local law), and `W_causal` (Lorentzian nonlinear
stability) are independent. This block closes the first two for one carrier,
fails the third for its four-span, and does not close the last two.

### N3 — hidden-wall scan

The claim fixes: flat background, homogeneous orientation totals, four unit
hyperfaces, symmetric coframe `delta E=h/2`, inherited flat metric carrier,
one generic physical direction, and double-precision source matrices. It does
not assume configuration covariance is zero, local weights are homogeneous in
Nature, or the supplied carrier is selected.

### N4 — residual matching

Block 23 asked first for a direct Ward/seagull term. Equations (10)--(11)
execute that route at the correct order. Equation (9) compares it to the exact
six-mode target rather than to a proxy. The remaining terms in (12) match the
named residual and remain open.

### N5 — rhetoric and resolution

- “span” always means the four homogeneous orientation matrices at the named
  direction;
- “fails” means order-one numerical matrix residual, not universal
  nonexistence;
- “positive” means strictly positive test weights, not physical selection;
- “seagull” is the same-action second geometry insertion, not the whole Ward
  identity;
- no contact-term, coframe, gravity, or axiom no-go is claimed.

The runner emits five substantive `N5_CERTIFICATE` lines with the same scope.

### N6 — partial closure and premise scan

The four-coframe and same-family response are retained mathematical carriers;
the current axioms select neither. The result adds no primitive and consumes
no candidate axiom wording as a premise.

### N7 — actionable steelman

The strongest response is that a physical contact tensor is the complete
combination (12) plus the generator connection, not four homogeneous area
Hessians. That response is accepted. The next computation must put the cut
family and Regge geometry in one nonuniform action, derive configuration
covariance and `R_*(ell,J)`, and compare their sum to `-M_s`.

### N8 — cross-cycle echo

Block 23 showed algebraic completion exists but regular Schur mixing is too
high order. This block tests the distinct direct-order route. Its success on
order and inertia prevents an echo of the earlier “wrong signature” rhetoric;
the new residual is full tensor content.

### Gate result

`PASS` for the bounded homogeneous four-span mismatch and its positive
counter-controls. Any broader contact, coframe, source-law, gravity, or axiom
negative would fail this gate and is not shipped.

## 10. Exact Next Obligation

Construct the joint nonuniform action and compute

```text
D_complete = D_hyperface + D_connected + D_additive-zero
             + D_mixed/source + D_multiplier + D_connection. (13)
```

Then test `P_6^dagger D_complete P_6=-M_s` across source directions and
continuous momentum. If the massless cancellation closes, proceed to the
Lorentzian nonlinear stability law. If it does not, identify which local
tensor direction is absent before enlarging the action basis.

## 11. Reproduction

Run:

```bash
python3 scripts/admissibility_four_coframe_hyperface_seagull_sourced_regge_span_boundary_2026_08_10.py
```

The runner derives every hyperarea Hessian exactly, reconstructs the three
source matrices, performs the flat Regge pullback, enumerates positive
signature controls, solves the complete unconstrained real span fits, and
checks the physical and no-go boundaries. No external scientific input is
used.
