# Finite-Lattice Center/Shell Endpoint Support-Response Coefficient

**Date:** 2026-04-14; self-contained finite-protocol revision 2026-07-12

**Scope:** the frozen microscopic cubic-scalar center/shell support sector
(irrep label `A1`) crossed with `{E_x,T1x}`, as defined below

**Status:** bounded support-response theorem; not an exact tensor observable;
independent audit required

**Claim type:** `bounded_theorem`
**Primary runner:**
[`scripts/frontier_s3_time_constructed_support_tensor_primitive.py`](../scripts/frontier_s3_time_constructed_support_tensor_primitive.py)
(`PASS=10 FAIL=0 TOTAL=10`)

## Scoped claim boundary

The claim is only this:

> On the declared finite lattice/ADM evaluation protocol, the two-channel
> endpoint response coefficient `Xi_R^(0)` is computed from four readout
> evaluations per bright channel. Both displayed components are nonzero at
> implementation precision with the stated sampled margins. The coefficient
> uniquely fixes the affine interpolant through the center and shell endpoint
> readouts, so that constructed interpolant is exactly compatible with those
> endpoint values. The same affine law approximates the declared canonical
> center/shell family at the recorded bounded tolerances.

The result combines one exact finite-lattice lemma, one bounded numerical
evaluation, and one exact affine-interpolation lemma. It does not identify the
readout with an exact tensor observable, take a continuum limit, derive an
Einstein/Regge action, or supply a physical support-to-time bridge. The runner
constructs every load-bearing finite-protocol operator and evaluates the mixed
response formula below without importing another frontier module or an
endpoint coefficient table.

## Frozen theorem domain

The theorem fixes the following finite evaluation surface:

| Item | Definition | Role |
|---|---|---|
| spatial lattice | `15^3` box, 13-site interior per axis, zero Dirichlet boundary | finite Green operator |
| support | center plus its six nearest-neighbor arms | seven-site source block |
| shell cut | radius `4` | reduced-shell normalization surface |
| probe radius | `4.25`, at the three displayed runner points | bounded readout surface |
| source response step | `epsilon = 0.005` | centered bright-source response |
| spacetime stencil step | `h = 0.04` | centered differential-geometric stencil |
| metric | `psi=1+phi`, `alpha=(1-phi)/(1+phi)`, `g=diag(-alpha^2,psi^4,psi^4,psi^4)` | declared conformastatic readout metric |
| probe points `(t,x,y,z)` | `(0,4.25,0,0)`, `(0.3,4.25/sqrt(2),4.25/sqrt(2),0)`, `(0.6,4.25/sqrt(3),4.25/sqrt(3),4.25/sqrt(3))` | finite maximum-readout set |
| field interpolation | cubic interpolation, `order=3`, `mode="nearest"` | off-grid probe convention |
| exterior cut | retain sites with `r > 4+1e-12` | strict shell-projection boundary condition |
| radial average | group nonzero entries (`abs(sigma)>1e-12`) by squared radius | finite shell convention |
| anisotropic anchor | `(3,3,0)` cubic orbit sum per shell charge | explicit normalization convention |

These numbers define the bounded theorem domain. They are not observational
targets or fitted source-family parameters. The runner also evaluates
`epsilon in {0.0025,0.005,0.01}` and `h in {0.03,0.04,0.05}` as controls; those
controls test robustness and do not turn the claim into a continuum theorem.

## Self-contained finite-protocol construction

Let `H` be the standard nearest-neighbor negative lattice Laplacian with zero
Dirichlet boundary, and let `G=H^{-1}`. On the seven support sites use the
orthonormal basis

```text
e0 = center source,
s  = (p_x+m_x+p_y+m_y+p_z+m_z)/sqrt(6),
e1 = (p_x+m_x-p_y-m_y)/2,
e2 = (p_x+m_x+p_y+m_y-2p_z-2m_z)/sqrt(12),
E_x = (sqrt(3)e1+e2)/2,
T1x = (p_x-m_x)/sqrt(2).
```

The unit-charge shell endpoint is `s/sqrt(6)`, which places charge `1/6` on
each arm. For a unit-charge support source `q`, set `phi_q=Gq` and

```text
delta_A1(q)
  = [phi_q(center) - mean(phi_q(arms))] / sum(q).
```

The reduced-shell normalization `A(q)` is not imported. The runner constructs
it by applying the finite lattice Laplacian to the radius-4 exterior projection
of `phi_q`, subtracting its radial average, and reading the `(3,3,0)` orbit sum
per total shell charge. On both unit-charge endpoints it obtains

```text
A(e0)          = 8.143540299590116e-02,
A(s/sqrt(6))   = 8.143540299590118e-02,
endpoint gap   = 2.776e-17.
```

For any unit-charge support source `q`, the runner builds the declared metric
from `phi_q`, computes its centered-stencil Einstein tensor at the three
declared probe points using the declared interpolation convention, and defines
`eta_h(q)` as the maximum absolute traceless-spatial component on those points.
This is an explicit finite-protocol condition, not a claim that `eta_h` is an
exact tensor observable or is physically selected by the framework axioms.

The two-channel endpoint readout is then computed as

```text
Theta_i(q)
  = [eta_h(q + epsilon b_i) - eta_h(q - epsilon b_i)]
    / [2 epsilon A(q)],

b_i in {E_x,T1x}.
```

Thus `Theta=(Theta_E,Theta_T)` is reconstructed inside this runner from the
finite operator definitions. The definition-only prototype note is not a
load-bearing premise of this computation.

## Exact support-gap lemma

The endpoint support gap does not require a numerical fit. On the interior
lattice let `d_center` be the Kronecker vector at the center. Locality of the
nearest-neighbor Laplacian gives the exact identity

```text
H[(1/6)d_center] = e0 - (1/6) sum(arms)
                 = e0 - s/sqrt(6).
```

Applying `G=H^{-1}` gives

```text
G[e0-s/sqrt(6)] = (1/6)d_center.
```

Consequently the two support potentials differ only at the center, and

```text
delta_A1(e0) - delta_A1(s/sqrt(6)) = 1/6.
```

The runner checks the sparse-vector identity with exactly zero floating-point
residual and independently obtains the endpoint gap as
`1.666666666666666e-01` from the solved Green columns.

## Computed mixed response

Because the denominator is exactly `1/6`, the response components have the
explicit four-evaluation form

```text
Xi_i
  = 1/(2 epsilon (1/6)) *
    { [eta_h(e0+epsilon b_i)-eta_h(e0-epsilon b_i)]/A(e0)
    - [eta_h(s/sqrt(6)+epsilon b_i)-eta_h(s/sqrt(6)-epsilon b_i)]
      /A(s/sqrt(6)) }.
```

This is the load-bearing bounded evaluation. It yields

```text
Theta(e0)          = (-3.772329167975e-04, +3.359952396063e-04),
Theta(s/sqrt(6))   = (-2.010572657265e-04, +4.031967723697e-04),

Xi_R^(0)           = (-1.057053906426e-03, -4.032091965809e-04),
||Xi_R^(0)||_2     =  1.131344605899e-03.
```

The quotient evaluation and the direct four-evaluation expression agree to
`3.795e-19` in the implementation. At displayed precision, each component is
separated from zero by more than `3e-4`, and the norm is larger than `1e-3` on
the declared protocol. These are bounded floating-point results, not an
interval-certified exact nonzero theorem.

## Affine compatibility theorem

Let

```text
Theta_shell = Theta(s/sqrt(6)),
F(delta)    = Theta_shell + Xi_R^(0) delta.
```

Because the shell endpoint has `delta_A1=0` and the center endpoint has
`delta_A1=1/6`, the two endpoint equations give

```text
F(0)   = Theta(s/sqrt(6)),
F(1/6) = Theta(e0).
```

Any affine map `a+v delta` satisfying these equations must have
`a=Theta_shell` and

```text
v = [Theta(e0)-Theta(s/sqrt(6))]/(1/6) = Xi_R^(0).
```

Therefore `F` is the unique affine endpoint interpolant and
`dF/d(delta)=Xi_R^(0)`. The derivative statement applies to this constructed
interpolant `F`; the note does not claim that the separately evaluated raw
family `Theta(q)` is exactly affine or differentiable as a function of
`delta_A1`. The runner's endpoint reconstruction residual is zero at displayed
precision.

In the registry's historical coordinate notation, this is the endpoint-fixed
affine bounded law on `A1 x {E_x, T1x}` with
`(gamma_E, gamma_T):=(Theta_E, Theta_T)`. The response has one cubic-scalar
support-coordinate input and two bright-channel outputs; it does not
reintroduce a mixed `A1`-bright support block. These aliases preserve
downstream registry compatibility and add no premise to the computation.

On the declared canonical unit-charge family

```text
q(r) = (e0+r s)/(1+sqrt(6)r),
r in {0.25,0.5,0.75,1,1.5,2},
```

the separately evaluated `Theta(q(r))` differs from
`F(delta_A1(q(r)))` by at most

```text
E_x channel: 4.838e-09,
T1x channel: 1.067e-08.
```

This last statement is bounded numerical compatibility, not exact affinity on
all sources.

## Nonzero-direction controls

Across the full `3 x 3` source-step/stencil-step control grid, both components
keep the same negative sign. The smallest absolute component values and norm
are

```text
min |Xi_E|       = 1.020038641650e-03,
min |Xi_T|       = 3.627695802105e-04,
min ||Xi||_2     = 1.082626712577e-03.
```

At fixed `h=0.04`, the source-step sweep changes `Xi_E` by less than
`8.3e-10` and `Xi_T` by less than `2.9e-10` (relative variation below
`8e-7`). The larger variation with `h` is retained as a bounded stencil
dependence. The controls establish a stable displayed nonzero direction on the
tested finite protocols, not a roundoff certificate or convergence as
`h -> 0`.

## Import and claim firewalls

The load-bearing runner imports only the Python standard library, NumPy, and
SciPy. It contains no fitted local-`O_h` or finite-rank source-family
parameters, no observed targets, no copied endpoint coefficients, and no
frontier helper imports. Its endpoint values are outputs of the displayed
operator chain.

The related `S3_TIME_TENSOR_PRIMITIVE_PROTOTYPE_NOTE.md` remains a
definition-only staging note. It supplies naming context but no premise used
here. Likewise, `TENSOR_SUPPORT_CENTER_EXCESS_LAW_NOTE.md` is a historical
cross-check; the exact `1/6` lemma is reproved here. They are intentionally
backticked rather than linked so neither context-only note becomes a claimed
dependency in the audit graph.

This note does not claim:

1. an exact endpoint coefficient theorem;
2. an exact tensor-valued support observable;
3. a continuum or stencil-convergence theorem for the ADM readout;
4. a physical theorem selecting this bounded readout and normalization;
5. an exact support-to-slice time-coupling law;
6. a full Einstein/Regge or nonlinear-GR closure theorem.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_constructed_support_tensor_primitive.py
```

Expected summary:

```text
PASS=10 FAIL=0 TOTAL=10
```
