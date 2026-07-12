# Green-Function Self-Consistency Does Not Force Massless Poisson from the Current Framework Premises

**Date:** 2026-04-14 (exact-boundary revision: 2026-07-12)
**Claim type:** no_go
**Status:** exact negative boundary; independent audit required.
**Primary runner:** [`scripts/frontier_gravity_full_self_consistency.py`](../scripts/frontier_gravity_full_self_consistency.py)
**Runner cache:** [`logs/runner-cache/frontier_gravity_full_self_consistency.txt`](../logs/runner-cache/frontier_gravity_full_self_consistency.txt)

## Claim

Fix the propagator operator and Green map used by the audited claim:

```text
X = ell^2(Z^3) tensor C^2,
A = (-Delta_lat) tensor I_2 in B(X),
R = Ran(A),
H = A,
G_0 = A^{-1} : R -> X.
```

On the current Lattice + Qubit + Admissibility + Record premise surface, the
field/propagator identity `L^{-1}=G_0` is not forced. Two exact conservative
extensions with the same framework model, the same fixed `H`, and the same
fixed `G_0` are:

```text
L_0 = A,
L_c = c A                 (c > 0, c != 1),
L_long = A(I+A).
```

As bounded endomorphisms `X->X`, all three field operators are self-adjoint
and have image `R`; when taking inverses, they are regarded as bijections
`X->R`. They also preserve translation symmetry, proper-cubic symmetry, and
the internal `Cl(3)` action, but

```text
L_0^{-1}    = G_0,
L_c^{-1}    = c^{-1} G_0 != G_0,
L_long^{-1} = (I+A)^{-1} G_0 != G_0.
```

The range-two `L_long` witness shows that the failure is not only an overall
normalization convention. Therefore the exact Green-map identification is an
additional field-selection statement, not a consequence of the current
framework premises.

A second, independent obstruction appears if one instead grants
`L^{-1}=G_0=H^{-1}` but tries to derive the propagator operator from the same
premises. Those inverse identities force only `L=H`; the proper-cubic family
`H_m=-Delta_lat+m^2I`, `m^2>0`, satisfies the identities but is not massless
Poisson. This second result strengthens the boundary but is not needed for the
direct fixed-`H` obstruction.

These are negative statements about derivability from the stated premise set.
They do not say that a later dynamics or field-selection theorem cannot select
the massless branch and the matching field Green map.

## Minimal premise set and forbidden imports

The minimal allowed surface is the current
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) premise node:

- Lattice: `Z^3`, nearest-neighbor adjacency, translations, and proper cubic
  rotations;
- Qubit: one-site algebra `M_2(C)`, equivalently `Cl(3,0)`;
- Admissibility: one fixed covariant nearest-neighbor availability rule;
- Record: fixed one-record-per-site readout with finite scalar additivity.

The premise source expressly says that Admissibility is not dynamics and
"does not choose a Hamiltonian or transfer operator." It also leaves
source/action and physical-observable identification outside the axioms.

The approved scale-reference, kinetic-isotropy, and realized-state primitives
do not select a spatial Hamiltonian, a massless branch, a field source, or a
field/propagator identification. No observed value, fitted selector,
literature theorem, unit convention, or proposed new primitive is used in the
proof.

Forbidden as hidden proof inputs are:

- assigning `H = -Delta_lat` and then describing the assignment as derived;
- defining the gravitational response to be `G_0 rho` and then using that
  definition to prove `L^{-1} = G_0`;
- selecting the static sector, a quadratic action, a source coupling, or a
  massless pole without a current-surface theorem that supplies it;
- using agreement with a `1/r` target to select the operator.

## Exact proof

### 1. Fixed-propagator non-forcing of the field Green map

Let `X=ell^2(Z^3) tensor C^2` and

```text
A = (-Delta_lat) tensor I_2.
```

The Fourier symbol of `A` is

```text
a(k) = 2 sum_i (1-cos k_i).
```

It vanishes only at the single measure-zero point `k=0`, so `A` has trivial
kernel on `X`. Write `R=Ran(A)`. The massless Green map is the complete
inverse graph

```text
G_0 = A^{-1} : R -> X.
```

For every `c>0`, `L_c=cA` is a bounded self-adjoint endomorphism of `X` with
image `R`. Regarded as a bijection `X->R`, it obeys

```text
L_c^{-1}=c^{-1}G_0.
```

Thus any `c!=1` is an exact fixed-`H`, fixed-`G_0` countermodel to the asserted
field/propagator identity. To remove the possibility that this is merely a
normalization issue, take

```text
L_long = A(I+A).
```

Because `I+A` is a bounded bijection of `X` commuting with `A`, `L_long` is a
bounded self-adjoint endomorphism of `X` with image `R`. Regarded as a
bijection `X->R`, it obeys

```text
L_long^{-1}=(I+A)^{-1}G_0 != G_0.
```

`L_long` is translation-invariant, proper-cubic invariant, self-adjoint,
positive, trivial on the internal `Cl(3)` factor, and has range-two stencil
`A+A^2`. Hence the current structural premises, even with the propagator
`H=A` and `G_0` held fixed, do not imply `L^{-1}=G_0`.

### 2. What equality of the complete inverse graphs implies

Let `H,L` be bounded injective endomorphisms of `X` with common image `R`, and
regard them as bijections `X->R`. If their complete inverse maps obey

```text
L^{-1} = G_0 = H^{-1}
```

as maps `R->X`, then inversion of the full operator graphs gives

```text
L = H.
```

This class-A algebra is exact. Agreement only on a common subdomain would not
be enough; the theorem requires equality of the complete inverse maps with
matching domain and codomain.

### 3. Independent propagator-selection obstruction

The framework premise source explicitly separates the named structural axioms
from dynamics: it does not choose a Hamiltonian or transfer operator. Thus
`H=-Delta_lat` is additional content, not a consequence already supplied by
the premise node.

For any real `m^2>0`, define

```text
H_m = (-Delta_lat + m^2 I) tensor I_2.
```

Its Fourier symbol is

```text
h_m(k) = 2 sum_i (1-cos k_i) + m^2 >= m^2 > 0.
```

Thus `H_m` is boundedly invertible, translation-invariant, proper-cubic
invariant, self-adjoint, nearest-neighbor plus onsite, and trivial on the
internal `Cl(3)` factor. Setting `G_m=H_m^{-1}` and `L_m=H_m` satisfies the
two inverse identities exactly, but `L_m!=-Delta_lat`.

This is a conservative expansion of any framework model: the current axioms
do not contain the auxiliary operator symbols `H`, `L`, or `G`, so adding the
displayed translation/cubic/Clifford-compatible operators does not change any
Lattice, Qubit, Admissibility, or Record fact. This second counterfamily is a
strengthening; the fixed-`H` result in section 1 already closes the quoted
field/propagator bridge negatively.

### 4. Additional unrestricted-range illustration

The proper-cubic, translation-invariant, self-adjoint stencil

```text
H_long = I - Delta_lat + (-Delta_lat)^2
```

has range two and strictly positive symbol `1+a(k)+a(k)^2`. With
`L=H_long` and `G_long=H_long^{-1}`, the inverse identities hold. This
non-load-bearing companion only illustrates the larger freedom available when
no operator range is supplied.

### 5. Exact surviving positive theorem

If separate premises or theorems supply equality of the complete inverse
graphs and `H=-Delta_lat` on the stated graph domain, then

```text
L = H = -Delta_lat
```

without restricting the candidate class for `L`. That conditional inversion
is exact. It is not a derivation of either supplied premise from the current
framework axioms.

## Why the main positive routes do not evade the countermodel

1. **Direct inversion.** It proves `L=H` only after equality of the complete
   inverse graphs has been supplied; it does not derive that equality.
2. **Weak-field linear response.** Once a field quadratic kernel `L` and a
   source coupling are supplied, first-order response is `L^{-1}`. Identifying
   this with the separate propagator `H^{-1}` is precisely the missing bridge.
3. **Variational/action route.** Varying a chosen quadratic action returns its
   chosen kernel. A massless action yields Poisson and a massive action yields
   screened Poisson. The selection is in the action premise.
4. **Translation/cubic/Clifford symmetry.** `H=A`, `L=cA`, and
   `L=A(I+A)` all have these symmetries while their inverse maps differ.
5. **Fixed-point/backreaction route.** Writing the update with `G_0` already
   supplies the response kernel. Fixed-point existence or numerical preference
   downstream of that choice does not derive the choice.
6. **Record/readout route.** The Record axiom supplies fixed scalar additivity,
   not source/action identification or a Hamiltonian selector.
7. **Static-sector route.** Restricting a supplied spacetime kernel to zero
   frequency does not identify an independently supplied field kernel with
   the propagator kernel.
8. **Convention/target route.** Choosing `c=1` by normalization can name an
   equality but does not exclude the non-rescaling `A(I+A)` field operator;
   using a `1/r` target to do so imports the desired output.

## Runner certificate

The primary runner is deterministic and checks:

- exact integer-stencil self-adjointness and proper-cubic invariance;
- exact distinction between the massless, massive, and range-two stencils;
- fixed-`H` character-space witnesses `G_0=1/4`, `(2H)^{-1}=1/8`,
  and `[H(I+H)]^{-1}=1/20` at `k=(pi,0,0)`;
- zero-momentum symbols `0`, `1`, and `2` for the tested family members;
- commutation of the internal identity with all `Cl(3)` Pauli generators;
- finite-torus inverse identities for two massive countermodels;
- a control in which substituting the massless field operator into the
  massive Green identity fails.

The finite inverse residuals are numerical companions. The decisive
countermodel and symmetry checks are exact stencil algebra.

Run:

```bash
python3 scripts/cached_runner_output.py \
  scripts/frontier_gravity_full_self_consistency.py --refresh
```

Expected terminal line:

```text
STATUS: EXACT_NEGATIVE_BOUNDARY
```

## Claim boundary

This note establishes only:

> With `H=-Delta_lat` and `G_0=H^{-1}` fixed on the explicit inverse graph,
> the current framework premises do not force the independent field operator
> to satisfy `L^{-1}=G_0`. If that identity is separately granted, it forces
> `L=H`; deriving `H=-Delta_lat` from the same premise surface is a second,
> independent selector problem.

It does not establish that Poisson is false, that no future theorem can select
the matching field operator, or that every gravity construction is blocked. A
positive closure of the audited bridge must supply a field/action/response
theorem that excludes `L=cH` and `L=H(I+H)` without defining the desired
identity into the response map.

## No-Go Discipline Gate

The physics-loop checklist records N1-N8 in full, including the
primitive-registry scan, prior-residual matching, the in-flight dynamics-PR
scan, and the strongest symmetry/naturalness steelman. The gate disposition is
`PASS` for the narrow logical non-forcing claim above; it is not a universal
no-go against later dynamics.
