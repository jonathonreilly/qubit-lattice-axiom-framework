# Scalar-Generator Tensor-Action Localization No-Go

**Date:** 2026-07-12
**Type:** no_go
**Status:** exact negative boundary; independent audit is required before any
effective-status change
**Role:** direct universal-GR route / tensor-action localization obstruction
**Primary runner:**
[`scripts/frontier_universal_gr_tensor_action_blocker.py`](../scripts/frontier_universal_gr_tensor_action_blocker.py)
(`PASS=13 FAIL=0`)
**Paired output:**
[`outputs/frontier_universal_gr_tensor_action_blocker_2026-07-12.txt`](../outputs/frontier_universal_gr_tensor_action_blocker_2026-07-12.txt)

## Claim scope

This note replaces the former inventory-level blocker label with two
self-contained exact statements.

1. **Source-map underdetermination.** A scalar generator `W[J]` does not by
   itself define a metric Hessian. For a metric-to-source map `Phi`, the
   Hessian of `F = W o Phi` is

   ```text
   D^2 F_g(h,k)
     = D^2 W_{Phi(g)}(D Phi_g h, D Phi_g k)
       + D W_{Phi(g)}(D^2 Phi_g(h,k)).                 (1)
   ```

   Neither `D Phi` nor `D^2 Phi` is fixed by the scalar function `W`.
   Explicit same-`W` countermodels below give zero, trace, shear, and an
   arbitrary prescribed metric Hessian. Therefore the scalar generator alone
   does not entail a curvature-localization map.

2. **Real-pullback obstruction for the current direct-source prototype.** On
   `V = Sym^2(R^4)`, let `D = diag(a,b,b,b)` with `a,b > 0` and take the
   direct source identification `J = h`. The exact log-determinant Hessian is

   ```text
   B_D(h,k) = -Tr(D^-1 h D^-1 k).                     (2)
   ```

   In the Frobenius-orthonormal lapse/shift/spatial-trace/shear basis its Gram
   matrix is

   ```text
   diag(-a^-2, -(ab)^-1, -(ab)^-1, -(ab)^-1,
        -b^-2, -b^-2, -b^-2, -b^-2, -b^-2, -b^-2),   (3)
   ```

   so it is rank ten and negative definite. For every real linear
   localization `A(p)`, including a projector, a polarization section, or a
   connection-induced linear map acting through field pullback, the induced
   quadratic kernel `c A(p)^T B_D A(p)` is semidefinite for every real scalar
   normalization `c`.

   By contrast, at `p = (1,0,0,0)` the ungauge-fixed Euclidean linearized
   Einstein Hessian has four diffeomorphism-gauge zero modes and, on the
   six-dimensional quotient, mixed inertia. Its exact spectrum is

   ```text
   { +1/2 (multiplicity 5), -1 (multiplicity 1), 0 (multiplicity 4) }. (4)
   ```

   Hence no such real pullback can identify `(2)` with the full linearized
   Einstein metric operator. This remains true after quotienting the gauge
   kernel, because the quotient Einstein form still has both signs.

The no-go is deliberately narrow. It does not exclude a separately derived
metric-dependent operator, a non-pullback curvature kernel, a supplied Regge
action, a complex conformal contour, or a nonlocal/gauge-fixed construction.
Each escape adds structure not contained in the scalar generator or in the
direct-source Hessian.

## First-principles derivation

### 1. The scalar generator does not select a metric Hessian

Use the finite real block

```text
D_m = [[0,m],[-m,0]],       J(j) = j I,       m > 0.
```

Then

```text
W(j) = log(det(D_m + j I)/det D_m)
     = log(1 + j^2/m^2),
W'(0) = 0,                  W''(0) = 2/m^2.  (5)
```

Let `L_tr(h)` be a spatial-trace functional and `L_sh(h)` a shear
functional. The three linear source maps

```text
Phi_0(h)  = 0,
Phi_tr(h) = alpha L_tr(h),
Phi_sh(h) = alpha L_sh(h)
```

all use exactly the same `W`, but `(1)` and `(5)` give respectively

```text
H_0       = 0,
H_tr(h,k) = (2 alpha^2/m^2) L_tr(h)L_tr(k),
H_sh(h,k) = (2 alpha^2/m^2) L_sh(h)L_sh(k).  (6)
```

Thus the same scalar generator admits inequivalent zero, trace-rank-one, and
shear-rank-one metric Hessians.

The freedom is complete once nonlinear source maps are allowed. Choose any
`s != 0`, so `W'(s) != 0`, and any symmetric bilinear form `K` on metric
perturbations. Define near `h = 0`

```text
Phi_K(h) = s + K(h,h)/(2 W'(s)).                      (7)
```

At the origin, `D Phi_K = 0` and `D^2 Phi_K = K/W'(s)`. Equation `(1)` then
gives

```text
D^2(W o Phi_K)_0 = K.                                (8)
```

An Einstein kernel and a non-Einstein kernel are therefore equally
compatible extensions of the same `W`. Choosing `(7)` to reproduce Einstein
would encode the desired answer in `Phi_K`; it would not derive it from `W`.

### 2. Exact direct-source Hessian

For

```text
W_D[J] = log det(D+J) - log det D
```

on the positive neighborhood of `J=0`, Jacobi's formula gives

```text
d log det X = Tr(X^-1 dX),
d X^-1      = -X^-1(dX)X^-1.
```

For `X = D + s h + t k`, differentiating once in each parameter at zero
gives `(2)` exactly. Evaluating `(2)` in the canonical symmetric basis gives
`(3)`. In particular, this local fiber form has no gauge kernel, no momentum
dependence, and one sign.

This calculation analyzes the existing direct-source prototype on its own
terms. It does not infer that arbitrary symmetric `4 x 4` matrix sources are
derived from the framework's scalar-source surface; Section 1 proves that
such a metric-to-source identification is itself additional data.

The pure matrix theorem is self-contained. Its application to the repository's
current direct-source route is grounded by the retained exact formula in
[`UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md`](UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md),
which supplies the same positive-background Hessian `(2)` but does not supply
Einstein/Regge dynamics.

### 3. Exact Einstein comparator

Let `g_{mu nu} = delta_{mu nu} + h_{mu nu}`. To first order in `h`, direct
variation of the Levi-Civita connection gives

```text
delta Gamma^rho_{mu nu}
  = 1/2 (partial_mu h^rho_nu + partial_nu h^rho_mu
         - partial^rho h_{mu nu}).                    (9a)
```

Using `delta R_{mu nu} = partial_rho delta Gamma^rho_{mu nu}
- partial_nu delta Gamma^rho_{mu rho}` and tracing with `delta` gives

```text
delta R_{mu nu}
  = 1/2 (partial_rho partial_mu h^rho_nu
         + partial_rho partial_nu h^rho_mu
         - box h_{mu nu} - partial_mu partial_nu h),
delta R = partial_rho partial_sigma h^{rho sigma} - box h. (9b)
```

Therefore `delta G_{mu nu}=delta R_{mu nu}-1/2 delta_{mu nu} delta R`.
With the stated Fourier convention `partial_mu -> i p_mu`, its symbol is

```text
(E_p h)_{mu nu} = 1/2 [
    p^2 h_{mu nu}
  - p_mu p^rho h_{rho nu}
  - p_nu p^rho h_{rho mu}
  + p_mu p_nu h
  + delta_{mu nu}(p^rho p^sigma h_{rho sigma} - p^2 h)
].                                                       (9c)
```

This is not merely a named comparator. The runner separately constructs the
Fourier-space Fierz-Pauli quadratic density

```text
Q_FP(h;p) = 1/4 [
    p^2 h_{mu nu}h_{mu nu}
  - 2 (p_mu h_{mu nu})(p_rho h_{rho nu})
  + 2 h p_mu p_nu h_{mu nu}
  - p^2 h^2
]                                                        (9d)
```

and verifies on all 100 symmetric-basis pairs that its Hessian is exactly the
operator `(9c)`. Thus the geometry variation and action-Hessian routes agree
independently, including the overall normalization used below.

Direct substitution gives

```text
E_p(p tensor xi + xi tensor p) = 0                     (10)
```

for all four vectors `xi`. At `p=(1,0,0,0)`, the temporal lapse/shift slots
are precisely these four zero directions. On the six spatial symmetric
components, `(9c)` reduces to

```text
2 <s,E_p t> = Tr(s t) - Tr(s)Tr(t).                    (11)
```

The five traceless-shear directions have eigenvalue `+1/2`; the normalized
trace direction has eigenvalue `-1`. Equations `(10)` and `(11)` prove the
spectrum `(4)`. They also show `E_0=0` and
`E_{lambda p}=lambda^2 E_p`, so the target is a two-derivative operator with
a momentum-dependent gauge kernel.

### 4. Pullback no-go

Because `B_D` is negative definite,

```text
h^T A^T B_D A h = B_D(Ah,Ah) <= 0                    (12)
```

for every real `A`; multiplying by a real scalar changes at most the common
sign. The mixed-sign form `(4)` cannot equal `(12)`. If `A` is invertible,
rank and inertia also disagree by Sylvester's law. If `A` is rank-lowering,
it may create null directions but remains semidefinite. Allowing `A(p)` to
contain derivatives can supply momentum dependence, but not the missing
opposite-sign trace term while the action remains a pullback of `(2)`.

Therefore a polarization/projector bundle can organize channels, but it
cannot manufacture the Einstein quadratic form from the direct scalar
Hessian. A successful localization must add a genuinely new bilinear
dynamical operator (or leave the real-pullback class).

## Claim-state movement

The former note named `Pi_curv` as a missing object and inferred a blocker
from inventory. The result above replaces that inference with exact route
pruning for two precise classes:

- `W` alone does not determine any metric Hessian because the source map is
  underdetermined;
- the live direct-source Hessian cannot be the full linearized Einstein
  kernel under any real linear pullback;
- the old pointwise polarization-frame language is not load-bearing;
- the remaining positive route must derive a metric-to-source map and an
  independent spin-2, two-derivative, mixed-inertia operator with the
  diffeomorphism Ward kernel.

The direct scalar route therefore remains blocked at the tensor-valued
dynamics-identification level. The result does not close the full
`Pi_curv`/Regge residual: it proves that `W` alone supplies no metric Hessian
and that the current `J=h` real-pullback branch cannot equal the full
linearized Einstein operator.

This is an exact negative boundary for the direct scalar-generator route, not
a derivation or a no-go for general relativity.

## Assumptions and imports

The algebraic proof is self-contained finite-dimensional calculus and linear
algebra. Its theorem premises are the displayed positive diagonal `D`, the
displayed finite scalar generator, real linear pullback localization, and the
linearized Einstein target derived in `(9a)`–`(9d)`. The route-binding
corollary consumes the retained supermetric-normal-form note linked above.
No observed value, fitted selector, literature value, unit convention, or
framework primitive is load-bearing.

`MINIMAL_AXIOMS_2026-06-29.md`,
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`,
and the later Regge/spin-2 notes are route context only. Their audit state is
not consumed by the theorem.

## No-Go Discipline Gate

### N1 — alternative routes

| Distinct challenge family | Test and result | Evidence | Honesty marker | Disposition relative to this no-go |
|---|---|---|---|---|
| Linear metric-source selection other than `J=h` | The same `W` produces inequivalent trace and shear rank-one kernels. | Equations `(5)`, `(6)`; runner symbolic trace/shear check | ATTEMPTED | Confirms source-map underdetermination. |
| Nonlinear metric-source selection | `Phi_K` realizes every symbolic symmetric `K`, including an Einstein-shaped kernel only by encoding it. | Equations `(7)`, `(8)`; runner symbolic arbitrary-`K` check | ATTEMPTED | Confirms that success requires extra source-map data. |
| Momentum-dependent York/TT gauge quotient | A TT projection may yield a semidefinite physical-mode kernel after supplying momentum, inverse operators, and boundary/zero-mode data, but it drops the full ungauge-fixed target tested here. | Full-space scope at `(4)`, `(10)`; N5 resolution audit | ATTEMPTED | Open partial escape outside the full-space claim; not a failed GR route. |
| Curvature of a distinguished connection | A curvature insertion need not be a pullback `A^T B_D A` and can carry derivatives and mixed inertia. | N7 steelman; equation `(12)` class boundary | ATTEMPTED | Open non-pullback escape; does not falsify the pullback theorem. |
| Supplied Regge action | A Regge Hessian can supply independent mixed-inertia dynamics without deriving it from scalar `W`. | N6 round-Regge inventory row | ATTEMPTED | Open supplied-action escape; not claimed to fail. |
| Complex conformal contour | Complex field maps can evade real semidefinite inertia. | Reality premise in N3 and equation `(12)` | ATTEMPTED | Open outside-real-class escape; not claimed to fail. |
| Nonlocal finite-momentum stress kernel | A metric-dependent nonlocal determinant can contain tensor vertices absent from the local `J=h` prototype. | Source-map boundary `(1)` and N6 scalar-TT inventory row | ATTEMPTED | Open different-operator escape; not claimed to fail. |
| Indefinite Lorentzian source background | Indefinite `D` removes the definite-form premise even though it does not itself derive the required Ward/operator structure. | Positive-`D` premise in `(2)`, N3 scope | ATTEMPTED | Open outside-positive-background class; not claimed to fail. |

Overall normalization, invertible frame congruence, rank-lowering projection,
and derivative-valued real `A(p)` are subcases of the single real-pullback
proof `(12)`. They are deliberately **not** counted as distinct N1 routes.

### N2 — collapsed wall set

The rank, inertia, derivative-order, and gauge-kernel discrepancies collapse
to one pullback obstruction. The two route walls used by this note have the
following pairwise audit:

| Pair | Does closing the first close the second? | Does closing the second close the first? | Independent? |
|---|---|---|---|
| source-map underdetermination / direct-source pullback mismatch | no — deriving some `Phi` need not repair the `J=h` branch | no — leaving the pullback class does not derive `Phi` | yes |

Source-map selection is logically prior to defining a metric Hessian, but the
two no-go statements concern distinct branches: arbitrary `Phi` selection and
the particular `J=h` prototype.

### N3 — hidden-wall scan

The phrases `background`, `by construction`, `canonical`, `current`, and
`direct-source` were scanned in the note, runner, and loop pack. The background
is explicitly `D=diag(a,b,b,b)` and Euclidean `delta`; the construction class
is explicitly real field pullback; and the basis is only
Frobenius-orthonormal bookkeeping. The `current direct-source` route binding is
the retained supermetric-normal-form dependency linked above. Positivity of
`D`, reality, flat linearization, and full ungauge-fixed metric space are
theorem premises, not claims about every gravity construction.

The separate per-mode scalar-dispersion source map analyzed in
`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md`
is a different, currently unaudited `Phi`; it is not silently identified with
`J=h` and is not consumed here.

### N4 — residual matching

The audited residual quoted in the task was the missing identification of the
scalar-generator Hessian with full Einstein/Regge metric dynamics. Section 1
prunes any claim that `W` alone selects that kernel; Sections 2–4 prune the
specific real-pullback `J=h` route to the full linearized Einstein operator.
They do **not** close a non-pullback `Pi_curv`, a supplied Regge action, or the
full Einstein/Regge residual. Older finite-frame-orbit and Casimir no-go notes
are not used as proof witnesses.

### N5 — rhetoric and resolution

The Einstein mismatch is proved per Fourier mode at one nonzero momentum;
one counterexample is sufficient to refute an identification asserted on the
full metric space for all momenta. The order check also includes `p=0`. No
claim is made for arbitrary curved triangulations, nonlinear completions,
finite-volume boundary prescriptions, or lattice-wide Regge spectra.

### N6 — partial-closure paths

The following pipeline states were inspected on 2026-07-12 as non-load-bearing
route inventory; they are not proof dependencies.

| Surface | Inspected status | What it closes / leaves open |
|---|---|---|
| `UNIVERSAL_GR_SUPERMETRIC_NORMAL_FORM_NOTE.md` | retained | Supplies the current `J=h` local Hessian `(2)`; leaves dynamics open. |
| `UNIVERSAL_GR_ROUND_PL_S3_REGGE_HESSIAN_CANONICAL_CHANNELS_NARROW_THEOREM_NOTE_2026-06-10.md` | retained_bounded | Supplies a mixed-inertia round spatial Regge Hessian; leaves action selection and full `3+1` open. |
| `UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING_BOUNDED_THEOREM_NOTE_2026-06-08.md` | unaudited | Tests a different per-mode scalar source map; does not derive a general metric source map. |
| `UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md` | audited_conditional | Narrows complement-channel structure; does not supply dynamics. |
| `UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO_NOTE_2026-06-18.md` | unaudited | Surveys current construction routes; is not used as an exact proof. |
| `UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED_FLAT_ATLAS_NARROW_THEOREM_NOTE_2026-06-10.md` | unaudited | Supplies a flat-atlas action route; does not derive the scalar route on `PL S^3 x R`. |

Partial and full escapes remain explicit: derive a metric-dependent Dirac or
source map; supply an independent curvature/Regge action; use a non-pullback
operator insertion; fix gauge and include the corresponding determinant; or
adopt a complex conformal contour. These are bridge/dynamics choices, not
labeling conventions and not automatically new axioms. The registered
kinetic-isotropy primitive supplies none of them.

### N7 — steelman

The strongest counterargument is that a distinguished connection may enter
the action through its curvature rather than merely transporting a
polarization frame. Then the resulting operator need not have the pullback
form `A^T B_D A`; it can have two derivatives, a Ward kernel, and mixed
inertia. That route can evade this theorem. It does not falsify the no-go as
stated, because the curvature operator is precisely independent dynamical
content absent from `W` and `(2)`.

### N8 — cross-cycle echo

| Prior wall | Current state | Retirement mechanism and applicability here |
|---|---|---|
| Pointwise complement-frame ambiguity (`UNIVERSAL_GR_COMPLEMENT_CANONICAL_NOTE.md`) | audited_conditional; later channel work is unaudited | Representation projectors can remove basis ambiguity. This applies here, so no frame-nonexistence claim remains. |
| Missing spin-2 generator on the scalar route (`UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL_SHARPENING...`) | unaudited | A supplied geometric action can bypass scalar `W`. This is preserved as an escape, not misread as scalar derivation. |
| Flat-atlas curvature supply (`UNIVERSAL_GR_SPIN2_TWO_DERIVATIVE_CURVATURE_GENERATOR_SUPPLIED...`) | unaudited | Supplied action/atlas data can retire the flat restricted wall, but not the source-map or `PL S^3 x R` derivation. |
| Current-stack `Pi_curv` route survey (`UNIVERSAL_GR_PICURV_ROUTE_EXHAUSTION_NO_GO...`) | unaudited | Route enumeration may sharpen scope, but its status cannot support this theorem; the present exact algebra stands independently. |

The surviving result is therefore route pruning at the source/dynamics
identification, with every known retirement mechanism kept open.

**No-Go Discipline disposition:** PASS. The claim is restricted to the exact
source-map and real-pullback classes tested here; all known escapes are stated.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_universal_gr_tensor_action_blocker.py
```

The runner independently checks the determinant/source-map countermodels,
the exact log-determinant Hessian, the Einstein gauge kernel and spectrum,
momentum scaling, gauge-kernel rotation, and the semidefinite-pullback
obstruction. It also checks that this note retains the N1–N8 scope firewalls.
