# Wilson Temporal-Kernel Casimir Generator and Beta/G-Bare Dial Transport

**Date:** 2026-07-01
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit verdict.
**Primary runner:**
[`scripts/wilson_temporal_kernel_casimir_generator_beta_gbare_transport_2026_07_01.py`](../scripts/wilson_temporal_kernel_casimir_generator_beta_gbare_transport_2026_07_01.py)

## Purpose

The finite-link/Wilson beta=6 bridge row
(`G_BARE_PARENT_FINITE_LINK_WILSON_BETA6_BRIDGE_NOTE_2026-06-18.md` — this
sentence names that row but is not a citation-graph dependency of this
note) records the same-scalar-slot identification `g_bare = s` for the
parent surface, which is exactly the choice of the normalization point
`beta = 2 N_c` on the supplied standard Wilson surface. The natural
question behind that identification is whether the operator/Hamiltonian
side of the same supplied surface supplies an independent reading of the
normalization. This note lands the first theorem package on that route.

What is proved here: the temporal-gauge one-step kernel of the supplied
Wilson action carries the **same single dial** as the plaquette (magnetic)
side, in Casimir form; the identity `beta * g^2 = 2 N_c` holds on the
kernel/generator side exactly as it does on the small-`a` matching side;
and `beta = 2 N_c` is precisely the point where the per-step generator is
the unit-coefficient canonical kinetic form. One dial, read on three
surfaces (coordinate slot, magnetic slot, kernel/generator slot), with all
three canonical normalizations coinciding at the single point
`beta = 2 N_c`.

What is **not** proved here: this note does not derive `beta = 2 N_c` and
does not remove or replace the surface definition recorded by the bridge
row. It transports the dial intact and sharpens what that declaration is
equivalent to on the operator side.

## Supplied surfaces (cited at audited scope)

1. [`G_BARE_RIGIDITY_THEOREM_NOTE.md`](G_BARE_RIGIDITY_THEOREM_NOTE.md) —
   the canonical generator basis with fixed half-trace form
   `Tr(T_a T_b) = delta_ab / 2` and no independent scalar-normalization
   freedom; the canonical quadratic Casimir at the fundamental,
   `sum_a T_a T_a = (4/3) I_3`, is carried on that chain as a decoration
   cite. This fixes the normalization in which the Casimir values below
   (`4/3`, `3`, `10/3`) are stated.
2. [`WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md`](WILSON_SMALL_A_MATCHING_BETA_GBARE_NARROW_THEOREM_NOTE_2026-06-07.md)
   — the magnetic-side coefficient identity `beta g_bare^2 = 2 N_c` inside
   the supplied standard Wilson plaquette action.
3. [`AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
   — the temporal-gauge reduction of the supplied Wilson action, in which
   the straddling temporal plaquette on a link reduces to the per-link
   class-function plane kernel; that row also carries the positive-kernel
   (nonnegative character coefficient) structure this note reuses. The
   `SU(3)` coefficient positivity used below is re-verified numerically
   inside this packet rather than leaned on beyond that row's audited
   scope.

No other physical input is used. The objects defined below
(`w_R`, `eps_R`, `g_E^2`) are definitions internal to this packet, made on
the supplied surfaces; no new axiom, import, or comparator is introduced.

## Definitions

In temporal gauge the temporal plaquettes of the supplied Wilson action
attach, to each spatial link crossing a time step, the per-link kernel

```text
W_beta(M) = exp((beta / N_c) Re Tr M),      M = U(t+1) U(t)^dagger,
```

a class function of `M`. Its Haar character coefficients and normalized
isotypic eigenvalues are

```text
c_R(beta) = int W_beta(U) chi_R(U)* dU,      w_R(beta) = c_R(beta) / d_R,
```

and the **per-step kernel generator** is defined as

```text
eps_R(beta) := -log( w_R(beta) / w_0(beta) ),
```

with `w_0` the trivial-representation eigenvalue. (In standard
lattice-gauge-theory language, the small-spacing limit of this object is
the electric/kinetic term of the transfer generator; that name is a gloss,
not an authority used by any step below.)

## Claim

**Theorem K1 (isotypic diagonalization; exact).** `W_beta` is a class
function, so its convolution operator on functions of the link acts on
each `R`-isotypic block as the scalar `w_R(beta)`. The per-step generator
is therefore a function of the representation label alone.

**Theorem K2 (Casimir asymptotics).** For `SU(N_c)` with the canonical
half-trace generator normalization,

```text
lim_{beta -> infinity}  beta * eps_R(beta) / N_c  =  C_2(R),
```

the quadratic Casimir in that same normalization (fundamental `4/3`,
adjoint `3`, symmetric-sextet `10/3` for `SU(3)`). Equivalently, the
large-`beta` per-step generator is `(N_c / beta) * Delta`, where `Delta`
is the canonical Laplacian acting as `C_2(R)` on the `R`-block — the
operator whose normalization is fixed by the same half-trace form that
fixes the canonical coordinates. Mechanism companions with their exact
constants: `U(1)` with kernel `e^{beta cos theta}` has
`2 beta eps_n -> n^2`; `SU(2)` has `beta eps_j / 2 -> j(j+1)`.

**Theorem K3 (dial transport).** Define the kernel-side coupling `g_E^2`
by the unit-mass-normalized reading
`eps_R = (g_E^2 / 2) C_2(R) (1 + O(1/beta))`. Then

```text
beta * g_E^2  ->  2 N_c,
```

the same identity the magnetic-side small-`a` matching carries. The
supplied surface has **one dial**: it appears as `beta` on the action,
as `g_bare^2 = 2 N_c / beta` in the magnetic matching, and as
`g_E^2 = 2 N_c / beta` in the kernel generator; the temporal-gauge
construction transports it intact. No new dial appears; none is removed.
At leading order the extracted dial is `R`-independent (the generator is a
multiple of the canonical Laplacian, not of a representation-dependent
deformation).

**Corollary K4 (normalization-point coincidence).** The leading dial map
`g_lead^2(beta) = 2 N_c / beta` takes the value `1` exactly at
`beta = 2 N_c` (`= 6` at `N_c = 3`), where the leading per-step generator
is the unit-coefficient canonical kinetic form `(1/2) Delta`. At that
point — and only there — the three canonical normalizations coincide:

```text
coordinate slot   s^2         = 1     (canonical finite-link coordinates),
magnetic slot     g_bare^2    = 1     (small-a matching at beta = 2 N_c),
kernel slot       g_E,lead^2  = 1     (per-step generator = Delta / 2).
```

Mismatched reading, exhibited on the same construction: at `beta = 24` the
leading generator is `(1/8) Delta` (coefficient `1/4 != 1`); the
coincidence fails off the point.

This packet does not derive `beta = 2 N_c`. What it proves is the
coincidence structure: the same-scalar-slot identification recorded by the
beta=6 bridge row is equivalent, on the operator side of the same supplied
surface, to the statement that the per-step kernel generator carries the
unit-coefficient canonical normalization `(1/2) Delta`.

## Proof

**K1.** `Re Tr(V M V^dagger) = Re Tr M` gives class invariance;
Peter-Weyl orthogonality gives, for any class function
`W = sum_R c_R chi_R` and any matrix element `D^R_{ij}`,
`int W(U V^dagger) D^R_{ij}(V) dV = (c_R / d_R) D^R_{ij}(U)`. Hence the
convolution operator is the scalar `w_R = c_R / d_R` on the `R`-block.

**K2.** Near the identity, write `M = exp(i X)` with `X = X^a T_a`. The
kernel exponent expands as

```text
(beta/N_c) Re Tr exp(iX) = beta - (beta / (4 N_c)) sum_a (X^a)^2 + O(X^4),
```

using `Tr(T_a T_b) = delta_ab / 2`. The heat kernel of the canonical
Laplacian `Delta` (the Laplacian of the bi-invariant metric in which the
`{T_a}` frame is orthonormal) at diffusion time `tau` has the same
Gaussian profile `exp(-sum_a (X^a)^2 / (4 tau))` and character
coefficients `w_R = exp(-tau C_2(R))`. Matching the Gaussian widths gives
`tau_eff = N_c / beta`, hence
`eps_R = tau_eff C_2(R) (1 + O(1/beta)) = (N_c / beta) C_2(R) (1 + O(1/beta))`.
The runner verifies this constructively — numeric Haar character
integrals, no asymptotic formula assumed — with Richardson extrapolation
in `1/beta` and strict error-decrease checks, for three `SU(3)`
representations and the `U(1)`/`SU(2)` companions with their exact
constants (`tau_eff = 1/(2 beta)` for the `U(1)` kernel `e^{beta cos}`,
`tau_eff = 2/beta` for `SU(2)`, `tau_eff = 3/beta` for `SU(3)`).

**K3.** Substituting K2 into the definition of `g_E^2` gives
`g_E^2 = 2 eps_R / C_2(R) -> 2 N_c / beta`, i.e. `beta g_E^2 -> 2 N_c`,
identical in content to the magnetic-side identity
`beta g_bare^2 = 2 N_c` of the cited small-`a` matching theorem.
`R`-independence at leading order is K2's statement that `eps_R` is
proportional to `C_2(R)` with an `R`-independent coefficient.

**K4.** Exact rational arithmetic on the leading map
`g_lead^2(beta) = 2 N_c / beta`: value `1` iff `beta = 2 N_c`; at
`N_c = 3` this is `beta = 6`, where the generator's leading form is
`(1/2) Delta`; at `beta = 24` it is `(1/8) Delta`. The coordinate-slot
value `s = 1` is the canonical-coordinate statement of the rigidity chain;
the magnetic-slot value at `beta = 2 N_c` is the cited matching identity.

## Boundary

This note does not claim:

- a derivation of `beta = 2 N_c`, of `g_bare = 1`, or of the
  same-scalar-slot identification — the bridge row's declared surface
  definition is characterized, not derived or replaced;
- Wilson plaquette action-surface selection from framework axioms;
- exclusion of improved or non-Wilson gauge actions;
- construction of a continuum Hamiltonian, a transfer-matrix spectral gap,
  or a continuum-limit existence statement;
- reflection positivity or kernel positivity beyond the cited row's
  audited scope (the `SU(3)` coefficient positivity used here is
  re-verified numerically inside this packet);
- finite-`beta` equalities for the asymptotic statements — K2 and K3 are
  `beta -> infinity` leading-coefficient theorems, verified by
  Richardson-extrapolated numeric character integrals at finite `beta`;
- a continuum running-coupling value or a phenomenological coupling;
- an audit verdict or any effective-status promotion.

The forward surface this opens: the declared normalization bit now has the
operator-side form "the per-step kernel generator is the unit-coefficient
canonical kinetic form `(1/2) Delta`". A framework-native derivation of
that per-step generator normalization — for instance from the
record-formation/per-step dynamics direction — would convert the declared
point into a derived one; that derivation surface is outside this row and
is the next path this packet opens.

## Falsifiers

The packet would fail if any of the following were true:

- the kernel's convolution operator failed to act as a scalar on some
  isotypic block (K1), or a computed character coefficient were negative
  on the tested range (kernel-positivity echo);
- `beta * eps_R / N_c` failed to converge to the half-trace Casimir
  `C_2(R)` for any tested representation, or the `U(1)`/`SU(2)`
  companions missed their exact constants (K2);
- `beta * g_E^2` failed to converge to `2 N_c`, or the extracted dial were
  representation-dependent at leading order (K3);
- the leading dial map failed `g_lead^2(2 N_c) = 1`, or the mismatched
  reading at `beta = 24` failed to give coefficient `1/4` on the same
  construction (K4);
- the three-normalization coincidence at `beta = 2 N_c` failed in exact
  arithmetic.

The runner checks these as source-boundary and construction checks rather
than audit verdicts.

## Verification

Run:

```text
python3 scripts/wilson_temporal_kernel_casimir_generator_beta_gbare_transport_2026_07_01.py
```

Expected:

```text
TOTAL: PASS=73 FAIL=0
```
