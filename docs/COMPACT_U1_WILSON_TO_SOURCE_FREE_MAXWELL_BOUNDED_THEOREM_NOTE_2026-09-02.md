# Compact U(1) Wilson-to-Source-Free-Maxwell Bounded Theorem

**Date:** 2026-09-02
**Claim type:** bounded_theorem
**Status authority:** independent audit only. This source note sets no audit
verdict and claims no effective obligation retirement.
**Runner:**
[`scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py`](../scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py)
**Cached receipt:**
[`logs/runner-cache/compact_u1_wilson_to_source_free_maxwell_2026_09_02.txt`](../logs/runner-cache/compact_u1_wilson_to_source_free_maxwell_2026_09_02.txt)

## Claim scope

On a finite periodic four-dimensional hypercubic carrier, supply compact
`U(1)` link variables and a positive Wilson plaquette action. Then:

1. link gauge transformations leave every plaquette holonomy and the action
   invariant;
2. the principal plaquette angles obey an exact oriented cube identity with
   integer monopole charge;
3. the exact Wilson field equation is the lattice codifferential of the sine
   of the plaquette angle;
4. on smooth principal-branch refinement families, the action and field
   equation converge with explicit bounds to the source-free Euclidean
   Maxwell action and equation, while the compact Bianchi identity converges
   to `dF=0` in the zero-monopole sector;
5. the flat-background anisotropic quadratic kernel has one gauge null and
   three positive Euclidean directions at nonzero four-momentum; after the
   temporal component is eliminated at nonzero spatial momentum, the local
   spatial sector has exactly two transverse modes; and
6. an explicitly assumed reflection-positive transfer interpretation has the
   exact `asinh` lattice dispersion and infrared speed fixed by the ratio of
   spatial to temporal gauge stiffness.

This is a theorem about a **supplied action surface**. It does not derive the
Wilson action, its stiffness, temporal/spatial equality, `beta=6`, the physical
identification with electromagnetism, a Record-readable field strength, a
charged source, the full compact quantum spectrum, or a continuum interacting
photon theory from the four axioms.

## 1. Compact connection and orientation convention

Let the lifted link phase be `ell_mu(x)` and set

```text
U_mu(x) = exp(i ell_mu(x)).
```

For the positively oriented path `+mu,+nu,-mu,-nu`, define

```text
tilde_theta_mu_nu(x)
  = Delta_mu^+ ell_nu(x) - Delta_nu^+ ell_mu(x)
  = bar_theta_mu_nu(x) + 2 pi n_mu_nu(x),
```

where `bar_theta_mu_nu` is the principal value in `(-pi,pi]` for
`mu<nu`, `n_mu_nu` is integer, and both are extended to the reversed
orientation by antisymmetry. This last convention matters at holonomy `-1`:
one must not apply `Arg(-1)=pi` independently to both orientations.

A link gauge transformation

```text
ell_mu(x) -> ell_mu(x) + alpha(x) - alpha(x+mu)
```

changes the lifted connection but not `exp(i tilde_theta)`. Hence it leaves
`bar_theta`, away from an immaterial endpoint convention, and every Wilson
plaquette term invariant.

## 2. Exact compact cube identity

For `mu<nu<rho`, the oriented six-face sum is

```text
(d bar_theta)_mu_nu_rho(x)
 = +bar_theta_nu_rho(x+mu) - bar_theta_nu_rho(x)
   -bar_theta_mu_rho(x+nu) + bar_theta_mu_rho(x)
   +bar_theta_mu_nu(x+rho) - bar_theta_mu_nu(x).
```

Since `d tilde_theta=d^2 ell=0`, it follows exactly that

```text
(d bar_theta)_mu_nu_rho = 2 pi m_mu_nu_rho,
m_mu_nu_rho = -(d n)_mu_nu_rho in Z.
```

Thus the product of the six oriented plaquette holonomies is one even when
their real principal-angle sum is nonzero. With the canonical half-open branch
and antisymmetric reverse orientation, an elementary-cube charge lies in
`{-2,-1,0,1,2}`. Reversing the cube orientation reverses the charge.

The next coboundary vanishes: `dm=0`. In four Euclidean dimensions the dual
integer current is therefore closed. Periodicity also makes the total spatial
magnetic charge on each closed slice vanish, although local monopole and
antimonopole cubes can occur.

Local `m=0` is not global triviality. A four-torus retains four independent
flat-holonomy directions (`b_1=4`) and a rank-six global flux lattice
(`b_2=6`).

## 3. Exact Wilson equation and controlled quadratic limit

Allow separate positive temporal and spatial stiffnesses:

```text
S_W[ell]
 = sum_x [ beta_t sum_i (1-cos bar_theta_0i)
           + beta_s sum_i<j (1-cos bar_theta_ij) ].
```

For an isotropic coefficient write `beta_t=beta_s=beta`. Varying an interior
link on the periodic carrier gives

```text
d S_W / d ell_rho(y)
 = sum_nu!=rho beta_rho_nu
     [sin bar_theta_rho_nu(y)
      - sin bar_theta_rho_nu(y-nu)].
```

The exact sourceless lattice equation sets this expression to zero. An overall
minus sign results if the codifferential itself is defined with the opposite
sign; the stationary equation is identical. The branch discontinuity creates
no action or first-variation defect because sine and cosine are periodic.

For every real `t`,

```text
0 <= t^2/2 - (1-cos t) <= t^4/24,
|sin t-t| <= |t|^3/6.
```

Consequently, with

```text
Q = (beta/2) sum_p bar_theta_p^2,
epsilon = max_p |bar_theta_p|,
```

one has the global action bound

```text
0 <= Q-S_W <= (beta/24) sum_p |bar_theta_p|^4
            <= (epsilon^2/12) Q.
```

The pointwise nonlinear field-equation remainder in four dimensions obeys

```text
|grad S_W - beta d^dagger bar_theta| <= beta epsilon^3.
```

Positivity is essential for the stable quadratic interpretation. At
`beta=0` the action is flat; negative spatial stiffness produces negative
transverse directions. Adding a gauge-breaking mass lifts the gauge null.

## 4. Smooth zero-monopole continuum family

Let the physical four-volume be fixed while the spacing `a` tends to zero,
and define links by exact line integrals of a `C^4` one-form:

```text
ell_mu(x) = integral_[x,x+a mu] A.
```

On any refinement for which `a^2 ||F||_infinity < pi`, Stokes' theorem gives
without branch wrapping

```text
bar_theta_mu_nu = integral_plaquette F = a^2 F^a_mu_nu,
```

where `F^a` is the face average. Every elementary monopole charge then
vanishes. The exact compact cube equation is the discrete Bianchi identity,
and its smooth limit is `dF=0`.

In four dimensions the isotropic action has the limit

```text
S_W -> (beta/2) integral sum_mu<nu F_mu_nu^2 d^4x
     = (beta/4) integral F_mu_nu F_mu_nu d^4x.
```

The factor `1/4` uses the ordered Einstein sum, which counts each unordered
plaquette orientation twice. The convention here is `U=exp(i integral A)`.
Writing `U=exp(i g integral A_phys)` instead changes the displayed coefficient
to `beta g^2/4`; no value of `g` is selected by this theorem.

Let `G_rho` denote the exact isotropic lattice gradient above. At the midpoint
of the varied link, symmetric face and difference averaging give the explicit
bound

```text
|G_rho/(beta a^3) - sum_nu!=rho partial_nu F_rho_nu|
 <= (a^2/24) sum_nu!=rho
      (||partial_rho^2 partial_nu F_rho_nu||_infinity
       + 2 ||partial_nu^3 F_rho_nu||_infinity)
    + (a^3/3) sum_nu!=rho ||F_rho_nu||_infinity^3.
```

Therefore any smooth refinement family whose scaled exact Wilson gradient
vanishes in the limit obeys

```text
partial_nu F_rho_nu = 0,
```

equivalently `partial_nu F_nu_rho=0` by antisymmetry. Together with `dF=0`,
this is the source-free Euclidean Maxwell system on the stated smooth,
zero-monopole branch. Fixed nonzero monopole charge scales as a magnetic
current and cannot be silently included in this branch.

The runner independently evaluates the action and operator on the exact-edge
integral mode `A_1=epsilon cos(x_2)`. It observes second-order refinement and
checks the analytic mode bound

```text
error <= epsilon a^2/12 + epsilon^3 a^6/24.
```

## 5. Flat-background Fourier kernel

Use link-centered Fourier variables and the forward-coboundary symbol

```text
hat_k_mu = 2 sin(k_mu/2),
T = hat_k_0^2,
P = sum_i hat_k_i^2.
```

The anisotropic quadratic kernel is

```text
K_00 = beta_t P,
K_0i = K_i0 = -beta_t hat_k_0 hat_k_i,
K_ij = beta_t T delta_ij
       + beta_s(P delta_ij-hat_k_i hat_k_j).
```

For every nonzero four-momentum its spectrum is exactly

```text
0,
beta_t(T+P),
beta_t T + beta_s P,
beta_t T + beta_s P.
```

The null vector is `(hat_k_0,hat_k_1,hat_k_2,hat_k_3)`. Hence the Euclidean
gauge quotient has **three** positive directions, not two.

For `P>0`, eliminating `A_0` gives the Schur complement

```text
K_red = (beta_t T + beta_s P)
        [I_3-hat_k_spatial hat_k_spatial^T/P].
```

It has rank two. Equivalently, the spatial Hamiltonian phase space has
dimension `6-1_Gauss-1_gauge=4`: two canonical pairs. This local mode count
does not apply to the spatial zero sector. For `P=0,T>0` there are three
time-dependent spatial toron directions; at full zero momentum all four
flat-holonomy directions remain.

The forward symbol is load-bearing. Replacing it by a centered `sin(k)`
symbol creates false Nyquist zero modes.

## 6. Conditional dispersion and infrared cone

The reduced Euclidean denominator is

```text
D_E = beta_t hat_k_0^2 + beta_s P.
```

If a reflection-positive transfer reconstruction is supplied, analytic
continuation gives

```text
4 sinh^2(E/2) = (beta_s/beta_t) P,
E = 2 asinh[(1/2) sqrt(beta_s/beta_t) sqrt(P)].
```

A separately declared continuous-time Hamiltonian instead gives
`omega^2=(beta_s/beta_t)P`. These are not the same exact finite-lattice
dispersion. A naive fully discrete Lorentzian equation
`4 sin^2(omega/2)=(beta_s/beta_t)P` has no real high-momentum solution when
the right side exceeds four.

Restoring temporal and spatial spacings, the infrared speed is

```text
c_IR^2 = (beta_s/beta_t) (a_s^2/a_t^2).
```

Equal graining `a_t=a_s` does not force `beta_t=beta_s`. An isotropic unit
light cone therefore uses both a common spacing and an isotropic supplied
gauge action.

## 7. Executable evidence and classification

The recovered runner reports `TOTAL: PASS=30 FAIL=0`. Its checks include:

- compact gauge invariance, integer cube charge, `dm=0`, and local nonzero
  monopole witnesses with periodic zero total charge;
- an independent finite-difference variation of the Wilson action;
- global action and pointwise equation remainder bounds;
- fixed-volume action/operator refinement and zero-monopole control;
- exhaustive `L=3,4,5` anisotropic spectra and Schur complements;
- toron, holonomy, transfer-dispersion, anisotropy, Nyquist, mass,
  wrong-sign, and zero-stiffness controls.

The original source payload was removed after passing 30 checks because a
portfolio gate was mistakenly treated as a preservation veto. This source was
reconstructed from the preregistered target and two independent derivations,
including the correction from an erroneous two-dimensional Euclidean quotient
to the rank-three Euclidean quotient stated above. The reconstructed runner was
then executed afresh; no original PASS line is reused as evidence.

The result fills the mathematical Wilson-to-Maxwell step only conditionally.
The higher-value open work is still to derive or explicitly classify the
physical gauge action, stiffness, field identification, source, and Record
readout. Until that occurs and independent audit evaluates the chain, this
note moves no retained TOE score.
