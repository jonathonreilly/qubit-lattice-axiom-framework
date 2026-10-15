# Independent inertial-response derivation, frozen before root draft access

Date: 2026-10-15. Role: focused mathematical check, not a formal audit.
Only the already-published M4 note was read. No new root inertial derivation or
code was accessed before this precheck was written. No observation was read.

## Domain and conventions

Assume a real scalar satisfying the frozen free equation
`partial_s^2 h - Delta h + mu^2 h=0`, `mu>=0`, with the supplied laboratory
energy norm `||h||_H^2=2E=integral(p^2+|grad q|^2+mu^2 q^2) d^3x`.
The spatial transform is unitary. The time transform is
`Wtilde(nu)=integral W(s) exp(i nu s) ds`. Let `W,V` be real compactly
supported vector H1 windows. Prescribe `x(s)=x0+u s`, `beta=|u|<1`,
`ell=1-beta^2`, `gamma=ell^(-1/2)`. The linear conformal force is
`a=-ell[grad h+u partial_s h]`; its signed window is `L_W=integral W.a ds`.
This is evaluation on a reference trajectory, not a claim that a body in an
arbitrary nonzero force has exactly constant velocity.

The dual Gram is the inner product of the Riesz vectors for `L_W,L_V`.
Its diagonal is the squared norm in `|L_W|<=sqrt(2E)*sqrt(G(W,W))`.
The energy completion defines this averaged trace; pointwise classical
acceleration is not assumed for all rough finite-energy states.

## Real Fourier pairing

For positive frequency `Omega=sqrt(|k|^2+mu^2)`, define
`nu=Omega-k.u>0` and `b=k-Omega*u`. Direct cosine/sine evolution has two
signs. On summing the q and p energy-dual squares, the cross-sign terms
cancel. Each branch has one half the weight. The two integrated branches
are identical under `k -> -k` and complex conjugation because windows and
fields are real. Thus the exact real bilinear Gram is

```
G_mu,u(W,V) = ell^2/(2*pi)^3 * integral_R3
   Re[(b.Wtilde(nu))*conj(b.Vtilde(nu))]/Omega^2 d^3k.
```

The translation phase from x0 cancels. Dropping the factor one half before
summing branches would double the norm; keeping one half after using their
equality would halve it. Replacing `k-Omega*u` with k drops a physical term.

## Change of momentum variables while retaining lab energy

Choose the z axis along u when beta>0. Boost the on-shell momentum by

```
epsilon=gamma*(Omega-beta*k_z)=gamma*nu,
p_z=gamma*(k_z-beta*Omega), p_perp=k_perp,
Omega=gamma*(epsilon+beta*p_z),
d^3k/Omega=d^3p/epsilon.
```

Put `r=|p|`, `t=r/epsilon=sqrt(1-mu^2/(gamma^2*nu^2))`, and
`R=diag(1,1,1/gamma)`. Then b=r R n and the exact spectral tensor is

```
G_mu,u(W,V) = integral_(mu/gamma)^infinity nu^2 *
    Re[Wtilde(nu)^T S_mu,u(nu) conj(Vtilde(nu))] dnu,
S_mu,u(nu) = ell/(2*pi)^3 * t^3 * R A(beta*t) R,
A(a) = integral_S2 n n^T/(1+a*n_z) dOmega_n.
```

In particular `A_perp(a)=pi*integral_-1^1(1-z^2)/(1+a*z) dz` and
`A_parallel(a)=2*pi*integral_-1^1 z^2/(1+a*z) dz`.
For zero mass t=1. Threshold nu=mu/gamma is exact; its zero endpoint is
handled by a limit. The retained factor `1/(1+beta*t*z)` comes from the
laboratory norm. The coordinate change did NOT change the energy to a
comoving one. The field energies obey `E'=gamma*(E-u.P)` and cannot be
identified without controlling momentum. A lightlike path is excluded.

## Exact massless time-local anisotropy

For beta>0 write `P_parallel=u u^T/beta^2` and `P_perp=I-P_parallel`.
Let `D=log((1+beta)/(1-beta))`. Real Parseval gives

```
G_0,u(W,V) = integral W'(s)^T T_u V'(s) ds,
T_u = T_perp*P_perp + T_parallel*P_parallel,
T_parallel = ell^2*(D-2*beta)/(4*pi*beta^3),
T_perp = ell*(2*beta-ell*D)/(8*pi*beta^3).
```

Both coefficients tend to `1/(6*pi)` at beta=0, where the tensor is defined
by this isotropic limit. For a normalized triangle, `||w'||^2=2/T^3`, so
these coefficients reproduce M4's separately published scalar parallel and
perpendicular norms. As beta tends to one from below, the perpendicular
coefficient is asymptotic to `ell/(4*pi)` and the parallel coefficient to
`ell^2*(log(4/ell)-2)/(4*pi)`. Both go to zero for fixed LAB time window and
LAB energy norm. This limiting statement does not assert a null-path theorem
or uniform control of the boost at beta=1.

## All-mass and stationary Loewner enclosures

Pair angular points z and -z. Each diagonal component of t^3 A(beta*t)
is an integral with a nonnegative weight times

```
t^3/(1-beta^2*t^2*z^2), 0<=t<=1.
```

This quantity increases with t. Hence `S_mu,u(nu)<=S_0,u` in Loewner
order, and the positive-frequency omission below mu/gamma only decreases
the quadratic form. For any finite collection of the allowed windows,

```
G_mu,u <= G_0,u.
```

The massless tensor satisfies the stronger simple stationary enclosure

```
0<T_u<=I/(6*pi) for 0<=beta<1,
G_mu,u(W,W)<=G_0,u(W,W)<=integral |W'|^2 ds/(6*pi).
```

Indeed its perpendicular angular integrand relative to beta=0 is multiplied
by `ell/(1-beta^2*z^2)<=1`; its parallel integrand has `ell^2` instead and
is also at most one. The proof works for vector windows with arbitrary
time-dependent direction and signed components. It does not require an
isotropic initial state; angular integration concerns the energy dual norm.

The order extends to joint Grams by replacing W with every real linear
combination of the windows. Independent modes with a common lab energy
normalization and squared couplings summing to q give the corresponding
bound `sum alpha_j^2 G_mu_j,u <= q G_0,u <= q G_0,0`.

## Import boundary

The stable free operator, conformal matter-force law, prescribed inertial
path, energy normalization and physical readout map remain premises. No
mass, initial state, energy budget, coupling, clock conversion, acceleration
trajectory or retarded-radio measurement identification is derived here.
The result is a conditional mathematical refinement of the M4 envelope.
