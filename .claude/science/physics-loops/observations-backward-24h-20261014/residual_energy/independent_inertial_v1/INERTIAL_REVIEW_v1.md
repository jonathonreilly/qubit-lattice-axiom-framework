# Focused independent check of the inertial scalar-force response

Date: 2026-10-15 02:39 UTC. Reviewer lane: `/root/inertial_response_check`.
This is a focused mathematical check, not a formal audit or retained-status
decision. Root remains the campaign's author. No observation was accessed.

## Conclusion and exact scope

The full conformal linear force evaluated on a prescribed constant subluminal
reference trajectory has the exact massless vector-window Gram stated in the
root's `INERTIAL_DERIVATION_v1.md`. All nonnegative-mass Grams are bounded above
by that massless inertial Gram, which in turn is bounded by the stationary
massless Gram. No discrepancy was found in the reviewed derivation. This
conclusion covers its explicit frozen free-field/reference-path model only.

The general vector H1-window tensor and all-mass inertial enclosure are the
newly checked scope. The triangular parallel/perpendicular constants were
already in the frozen M4 note; this check does not count those as new science.

## Independent derivation and chronology

1. Read only the frozen M4 note to establish Fourier, energy and force-law
   conventions.
2. Independently derived the real two-branch norm, transformed on-shell
   momentum while retaining laboratory energy, evaluated the tensor, and
   proved both Loewner enclosures.
3. Froze `PRECHECK_v1.md` before accessing any new root inertial draft or code.
4. Wrote and executed the independent `independent_check_v1.py`; all 66
   synthetic controls passed on the first recorded execution. There was no
   failed execution to discard or repair.
5. Only then read root's `INERTIAL_DERIVATION_v1.md` with SHA256
   `d3071b2ae96c3c5e87828d931dd7f41e7dd9a996baac66263b79bc82fd271856`.
   The derivations agree. No root inertial executable was read or imported;
   this report does not assert independent review coverage of that executable.

The complete independent proof is in `PRECHECK_v1.md`; its substantive equations
are recorded here for interpretation of the controls.

## Checked mathematics

Let `beta=|u|<1`, `ell=1-beta^2`, `gamma=ell^(-1/2)`, and use lab-frame
`||h||_H^2=2E`. With the supplied force
`a=-ell(grad h+u partial_s h)` on `x=x0+u s`, the real Gram is

```
G_mu,u(W,V)=ell^2/(2pi)^3 integral
 Re{[(k-Omega*u).Wtilde(Omega-k.u)]
      conjugate[(k-Omega*u).Vtilde(Omega-k.u)]}/Omega^2 d^3k.
```

Each signed branch initially carries one half. Reality makes the integrated
branches equal. Keeping the half after this equality or doubling the resulting
single integral would be a normalization error. The sign of the overall
acceleration does not affect the Gram; its relative spatial/time-derivative
sign does.

For `u` along z the massless local tensor has eigenvalues

```
T_parallel=ell^2 [log((1+beta)/(1-beta))-2beta]/(4pi beta^3),
T_perp=ell [2beta-ell log((1+beta)/(1-beta))]/(8pi beta^3).
```

Both continuous beta=0 limits are `1/(6pi)`. For arbitrary real compact vector
H1 windows, `G_0,u(W,V)=integral W'^T T_u V' ds`. No isotropic initial state
is selected; angular integration computes the energy-dual norm.

In primed momentum variables, put
`t=sqrt(1-mu^2/(gamma^2 nu^2))` above threshold `nu=mu/gamma` and
`R=diag(1,1,1/gamma)`. The exact spectral tensor divided by `nu^2` is

```
S_mu,u(nu)=ell/(2pi)^3 t^3 R A(beta*t) R,
A(a)=integral_S2 n n^T/(1+a*n_z) dOmega.
```

Pairing z and -z makes the positive integrands proportional to
`t^3/(1-beta^2*t^2*z^2)`, which increase with t. The matrix is diagonal in
the inertial parallel/transverse basis. Hence `G_mu,u<=G_0,u` for every finite
family of windows. The massless perpendicular integrand relative to beta=0
is multiplied by `ell/(1-beta^2*z^2)<=1`; its parallel counterpart has another
factor ell. This proves `T_u<=I/(6pi)` and the joint stationary enclosure.

The massless tensor is positive for every beta<1. Both eigenvalues approach
zero as beta tends to one from below with lab energy and lab window fixed.
The boost becomes singular and beta=1 is outside the theorem. The isolated
zero spatial-frequency massless point is a measure-zero limiting mode, not
a positive-frequency exception requiring a new physical premise.

## Independent executable evidence

The 66 controls use independent angular quadrature, direct time-domain
cosine/sine evolution, paired signed Fourier coefficients, finite-difference
Lorentz Jacobians, nonconstant vector windows, and actual smooth real fields.
They are finite synthetic checks of the displayed proof, not proof by sampling.

- Closed tensor versus adaptive angular integration at seven speeds from
  zero to 0.999, plus positivity and stationary-enclosure controls.
- Three joint Grams of compact polynomial vector windows with changing
  component ratios, checking the matrix order against the stationary Gram.
- Twenty angular mass-shell monotonicity controls covering speeds from
  zero to 0.999 and five mass-shell ratios in each case. These sample the
  pointwise positive integrand used in the proof; they are not empirical
  mass limits.
- Direct cosine/sine q,p coefficients versus two signed branches, reality
  constraints, and the paired single-branch reduction at four speed/mass
  combinations. Maximum relative difference was `1.7482e-15`.
- Rotation covariance with nonconstant vector direction.
- Twelve momentum-shell/Jacobian controls. The maximum finite-difference
  invariant-measure relative discrepancy was `5.0765e-11`.
- A real Schwartz initial field, evaluated through separate time-domain
  force and Fourier-coefficient constructions. Four window responses were
  approximately `0.0356834, 0.117231, 0.0661818, 0.121811`; the two
  computations agreed to relative error `2.2787e-15`. The independently
  integrated mathematical energy was `6.79765821`, and the largest squared
  response divided by the stationary energy bound was `0.00874546`.
- Dropping the partial-time force term changed the same finite-field
  responses, with maximum absolute difference `0.15875627`. This confirms
  that the checked field does distinguish the physically incorrect omission.
- A positive-frequency packet had lab energy `27.48348513` and comoving
  energy `14.54406983`, with the latter matching `gamma(E-beta*P_z)`.
  The Lorentz change of variables therefore cannot justify identifying the
  two energy budgets.

The execution completed in approximately 0.4 seconds. `STDOUT_v1.txt` contains
the pass summary; `STDERR_v1.txt` is empty. No test input or tolerance was
changed after this run.

## Application boundary and remaining obligations

The stable frozen flat KG operator, supplied universal conformal matter
coupling, prescribed constant reference velocity, common laboratory time,
positive energy normalization and controlled linearization are assumptions.
No scalar state, mass, coupling or history profile is selected by this theorem.
No free-field energy budget, measurement-error budget, clock map, gravitational
normalization or actual radio observation operator is inferred.

The stationary matrix is a conservative upper enclosure on an inertial
response. It is generally not the exact moving Gram; an exact massless
minimum-energy inference must use the inertial anisotropic tensor. Count
windows may use that tensor only after establishing the supplied reduced
velocity readout and its nuisance-cancellation conditions. Arbitrary
accelerated trajectories and retarded endpoint mixtures remain outside this
focused result. No claim of a data exclusion, observed scalar signal, or a
fully derived action is made.

## Identities

| Artifact | SHA256 |
| --- | --- |
| Frozen M4 note | `059e1ff0ef5ab67e71763a55b022e130348b54e8477b478ecf5e0aaa25f0a74e` |
| Independent precheck | `aa3ff4ef0e3e5bbb350360adfc9dba274e5f55b5ec3a7764deaeeb2a94f1064c` |
| Independent source | `3d3cd9e3e2171d224ff50edb44b85300666ef7f1873a3a1319e940e674748ffd` |
| Independent results | `9744084fb3833668ac41ecf0d99697a11d6528313623802a3735afb710a4bf3e` |
| Root derivation read after independence freeze | `d3071b2ae96c3c5e87828d931dd7f41e7dd9a996baac66263b79bc82fd271856` |
