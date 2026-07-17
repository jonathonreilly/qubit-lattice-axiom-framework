# Free Staggered 3+1 Same-Action Scalar Spectral Transfer/Covariance Continuum Spine — Bounded Theorem

**Date:** 2026-07-12  
**Claim type:** bounded_theorem  
**Status authority:** independent audit lane only. This source note proposes a
bounded claim and neither sets nor predicts an audit verdict.  
**Primary runner:**
[`scripts/free_staggered_3plus1_same_action_transfer_gaussian_continuum_2026_07_12.py`](../scripts/free_staggered_3plus1_same_action_transfer_gaussian_continuum_2026_07_12.py)  
**Cached output:**
[`logs/runner-cache/free_staggered_3plus1_same_action_transfer_gaussian_continuum_2026_07_12.txt`](../logs/runner-cache/free_staggered_3plus1_same_action_transfer_gaussian_continuum_2026_07_12.txt)

## Purpose and exact scope

This note closes the scalar-spectral part of a specific mismatch in the
existing free-sector ladder. The
repo already contained a 3-spatial-dimensional action-derived two-step
dispersion, a four-dimensional Euclidean staggered covariance, a smeared
Gaussian limit, and a conditional free-field OS reconstruction. They were not
previously assembled through an exact identity showing that the transfer
eigenvalue and covariance pole location are two calculations on **one action
family `A_a`**. This note also constructs the finite-dimensional map from the
covariance-pole solution space to the stable transfer eigenspace. It does not
yet identify the pole residue/equal-time CAR inner product or prove that the
finite-`a` Gaussian correlators equal correlators of the second-quantized
stable contraction.

The result below supplies that identity and a single controlled scaling
parameter `a`. It is a free massive theorem conditional on the explicitly
displayed staggered action and, for Fock-space and Pfaffian statements,
conditional on the CAR/quasi-free branch. It does not identify that action as
the unique framework carrier, does not select one taste, and does not recover
the interacting Standard Model or GR.

## Reconciliation of the actual existing science

| Existing candidate surface | What it actually supplies | Mismatch before this note |
|---|---|---|
| [Free staggered two-step dispersion in `d` spatial dimensions](FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md) | Canonical phase algebra, action-derived `T_odd T_even`, `E_d=asinh sqrt(M²+sum sin²k)`, and quasilocal log-transfer for `d=3` | It did not identify its stable transfer channel with a pole of the four-dimensional covariance used by the Gaussian lane |
| [Free staggered-Dirac two-point SO(4) limit](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md) | Exact finite-`a` scalar spectrum and fourfold taste multiplicity; continuum Euclidean Dirac covariance | It explicitly did not establish a transfer/Hamiltonian or Wightman statement |
| [Free lattice-to-continuum Gaussian measure](FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md) | Smeared covariance convergence and fixed finite Pfaffian hierarchy in the supplied quasi-free branch | It deliberately did not use the transfer lane and therefore did not prove same-object unitarity |
| [Conditional free-field OS/Wightman reconstruction](FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md) | Continuum OS2 Gram positivity and the standard conditional Wightman reconstruction target | It names the lattice/continuum and `1+1 -> 4D` arena mismatch (its gap `G1`) |
| [Transfer-log quasilocality](TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md) | Analytic-strip exponential decay of the massive free log-transfer kernel | Its decay length was stated in lattice units, not as one member of the present physical scaling family |

All five rows in this table are `unaudited` in the live ledger at source time,
so they are candidate dependencies and cannot propagate retained grade. The
load-bearing new steps here are the pole--transfer identity and stable-solution
intertwiner. The surrounding continuum consequences are a conditional
one-family composition of those candidate rungs, not a new sector-specific
action and not a retained chain.

## The one-parameter family

For each `a>0`, take the isotropic Euclidean lattice `a Z^4`, fixed physical
mass `m>0`, dimensionless mass

```text
M(a) = a m,
```

and the free (`U=1`) staggered action

```text
A_a[bar chi,chi]
  = sum_n bar chi_n [ M(a) chi_n
      + (1/2) sum_{mu=0}^3 eta_mu(n)
          (chi_{n+e_mu} - chi_{n-e_mu}) ],

eta_0=1,
eta_mu(n)=(-1)^(n_0+...+n_{mu-1}).
```

Physical time and space both use the same spacing `a`; the two-step transfer
advances physical time by `2a`. No independent Hamiltonian, continuum mass,
light speed, or temporal normalization is attached later. The covariance does
require the explicit normalization `D_phys=a^{-1}D_lat` and the field map
`chi_n=a^{3/2} psi(an)` (with the corresponding Fourier/block-cell
normalization); these are declared comparison conventions, not claimed to be
selected by the axioms.

## Theorem

### 1. Exact same-object action, transfer, and covariance identity

Fold the three spatial axes into the canonical `2^3` cell. The spatial hop is

```text
H_sp(k) = i sum_{j=1}^3 sin(k_j) Gamma_j,
H_sp(k)^2 = -lambda(k)^2 I,
lambda(k)^2 = sum_j sin^2(k_j).
```

The Clifford identity follows directly from the canonical staggered phases.
On an eigenline `H_sp=i lambda`, the action equation `D_lat chi=0` is exactly

```text
chi_{t+1} = chi_{t-1} - 2[M + (-1)^t i lambda] chi_t.
```

Hence its even/odd one-step matrices give

```text
T_2(lambda)=T_odd T_even,
spec T_2(lambda)={exp(-2E),exp(+2E)},
sinh^2 E=M^2+lambda^2.
```

Now block the **same action** in Euclidean time, writing `t=2r+s`, `s=0,1`,
and coarse momentum `Q=2q_0`. On the same spatial eigenline its exact
two-time-cell Dirac matrix is

```text
D_2(q_0,lambda)
 = [[M+i lambda,             (1-e^{-2iq_0})/2],
    [(e^{2iq_0}-1)/2,        M-i lambda        ]],

det D_2 = M^2+lambda^2+sin^2 q_0.
```

The forward covariance pole is `q_0=iE`, because
`sin^2(iE)=-sinh^2E`. Its coarse-time multiplier is therefore

```text
z_pole=e^{iQ}=e^{2iq_0}=e^{-2E},
```

which is exactly the stable eigenvalue of `T_2`. This is the pole--transfer
identity. It is an algebraic identity on one action family, not agreement of
two independently selected dispersions.

Moreover `T_odd=T_even^dag`, hence

```text
T_2=T_even^dag T_even>0.
```

For the full `8`-component spatial cell, let `z=e^{-2E}` and write a
time-cell covariance-pole vector as `u=(chi_even,chi_odd)`. The exact map

```text
J_z = diag(I_8,z^{-1}I_8)
```

converts the time-cell coordinates to the two-slice transfer-state
coordinates. Direct substitution gives

```text
D_2(z)u=0  iff  T_2 J_z u = z J_z u.
```

Both spaces have dimension `8`; thus `J_z` maps the full covariance-pole
solution space onto the stable transfer eigenspace, including the stable
multiplicity. This is a solution-space intertwiner. It does **not** fix the
normalization of the pole residue, the reflected/equal-time CAR inner product,
or the coherent-state functional-integral representation.

The growing reciprocal solution is the backward-time branch. Selecting the
forward stable subspace gives the positive one-particle contraction

```text
C_a(k)=e^{-2E_a(k)},
E_a(k)=asinh sqrt((am)^2+sum_j sin^2 k_j).
```

### 2. Positive Hamiltonian and exact real-time unitarity on the CAR branch

On the supplied CAR/quasi-free branch, finite second quantization gives

```text
T_hat,a^2 = Gamma(C_a) > 0,
H_hat,a = -(1/(2a)) log T_hat,a^2
        = dGamma(epsilon_a),
epsilon_a(p) = a^{-1} E_a(ap) >= 0.
```

Thus `H_hat,a` is self-adjoint and bounded below on each finite carrier, and

```text
U_a(t)=exp(-it H_hat,a)
```

is exactly unitary for every `a`; unitarity is not postponed to the continuum
limit. The statement is conditional on the CAR/quasi-free branch and on the
stable-transfer reading. This note does not derive CAR from the four minimal
axioms or from the two-point kernel, and it does not yet prove that correlators
of `Gamma(C_a)` equal the finite-`a` Gaussian covariance correlators.

### 3. Controlled physical continuum limit

For fixed physical momentum `p` in any compact band,

```text
epsilon_a(p)
 = a^{-1} asinh sqrt((am)^2+sum_j sin^2(ap_j))
 -> sqrt(m^2+|p|^2)
```

uniformly with error `O(a^2)`. Taylor remainders of `sin x` and `asinh x` are
uniform on a compact band, so the statement is analytic rather than a fit.
For a compact band `K`, once `a` is small enough that `K` lies in the physical
Brillouin zone, choose a measurable orthonormal frame
`W_a(p):C^8 -> Ran P_stable,a(p)` and define the explicit comparison isometry
`J_a f(p)=W_a(p)f(p)`, extended by zero outside `K`. The stable eigenvalue is
scalar on this eight-dimensional fiber, so uniform multiplier convergence is
equivalently

```text
||J_a^* h_a J_a - multiplication_by_sqrt(m^2+|p|^2)|| -> 0
```

on `L^2(K;C^8)`. This comparison controls the transfer energy only; it is not
the missing covariance-residue/CAR-inner-product identification. On every
fixed-`n` sector,
`dGamma(epsilon_a)` converges with error at most `n` times the one-particle
multiplier error; the corresponding unitary groups converge uniformly for
time in compact intervals. This supplies a controlled finite-particle
quantum-mechanical limit.

The mass scaling is severely constrained inside the power-law class. If
`M(a)=m a^alpha`, then at rest

```text
a^{-1} asinh(M(a)) ->
  +infinity  for alpha<1,
  m          for alpha=1,
  0          for alpha>1.
```

Thus `M(a)=am` is the unique power law yielding a finite nonzero physical rest
mass with the fixed `2a` transfer-time normalization.

### 4. Same-family Euclidean covariance and free QFT limit

The four-dimensional phase matrices obey a `Cl_4` algebra, so the same action
has exact finite-`a` scalar spectrum

```text
D_lat(q)^dag D_lat(q)
  = [M^2+sum_{mu=0}^3 sin^2 q_mu] I_16.
```

With `D_phys=a^{-1}D_lat`, `chi_n=a^{3/2}psi(an)`, the corresponding
Fourier/block normalization, and `q=ap`, one irreducible continuum spin block
has covariance

```text
S_a(p)
 = [m-i sum_mu gamma_mu sin(ap_mu)/a]
   / [m^2+sum_mu sin^2(ap_mu)/a^2]
 -> (m-i gamma.p)/(m^2+p^2).
```

The convergence is pointwise and uniform on compact momentum sets at
`O(a^2)` for the displayed spin block/scalar-spectrum sector. The cited
Gaussian-measure rung upgrades this to Schwartz-smeared covariance convergence
and therefore, conditional on the free CAR/quasi-free branch, convergence of
every fixed finite Pfaffian Schwinger function. The limiting covariance is
SO(4)-bispinor covariant. The cited conditional OS rung then supplies the
standard free positive-spectrum Wightman reconstruction, with the abstract OS
reconstruction theorem still used as methodology for the full boost
representation.

The new content is that this covariance hierarchy and the positive transfer
generator are derived from the same `A_a`, `M(a)`, and `a`, and their pole
solution spaces are intertwined as above. The still-missing residue,
equal-time CAR metric, and coherent-state representation prevent promotion of
this scalar-spectral composition to a single finite-`a` QFT/Hilbert-object
identity.

### 5. Physical quasilocal scale

For `m>0`, the transfer-log symbol is analytic up to the nearest branch point
at lattice inverse length `asinh(M)`. Along an axis,

```text
xi_lattice(a)=1/asinh(am),
xi_physical(a)=a/asinh(am) -> 1/m,
r_physical(a)=asinh(am)/a -> m,
```

again with `O(a^2)` corrections. The generator is quasilocal, not strict
finite range. This statement controls its physical decay scale; it does not
claim that a fixed physical-distance tail vanishes as `a->0`.

## Taste, basis, and statistics firewalls

The exact finite-`a` statement is the scalar spectrum and its multiplicity.
The `16`-component hypercube representation decomposes into four identical
complex `Cl_4` spin blocks, giving four tastes. A momentum-dependent rephasing
can display `gamma_mu tensor I_taste`, but a local hypercube reconstruction has
finite-`a` spin--taste mixing. Nothing here roots a determinant, projects one
taste, or identifies a unique physical family. The continuum theorem therefore
recovers a free Dirac QFT with the staggered taste multiplicity, not the
one-generation fermion content of the Standard Model.

Likewise, the covariance is statistics-blind until a Gaussian branch is
chosen. Transfer positivity plus finite second quantization proves the stated
CAR/Fock result **inside** the CAR branch; it does not force that branch from
the axioms.

## What is closed and what remains open

Established at bounded-theorem strength for the displayed free family:

- the `1+1 -> 3+1` transfer arena mismatch for the free action-derived
  dispersion;
- the exact identity between the 3+1 two-step stable transfer eigenvalue and
  the four-dimensional Euclidean covariance pole location, plus an exact map
  between their eight-dimensional solution/eigenspaces;
- one controlled `a->0` scaling with a positive generator, exact finite-`a`
  unitarity, uniform band-limited relativistic energy convergence, smeared
  Gaussian convergence, and a conditional chain to the free OS/Wightman
  limit, without claiming a finite-`a` transfer/Gaussian Hilbert identity;
- the physical massive quasilocal length scale.

Still open:

- derivation or unique selection of the free staggered action from the axiom
  set and record-forming dynamics;
- statistics selection, taste reduction/family structure, and the massless
  uniform limit;
- normalization of the covariance-pole residue, its equality with the
  reflected/equal-time CAR projector, and a coherent-state proof that
  `Gamma(C_a)` generates the same finite-`a` Schwinger functions;
- an interacting gauge-plus-fermion continuum construction with controlled
  renormalization, anomaly cancellation, chirality, and the full SM limit;
- a geometry/dynamical-metric extension on this same scaling family and its GR
  limit;
- one joint limit proving compatibility of the SM and GR sectors without
  importing separate laws.

No axiom-update stop condition is triggered. Every negative statement here is
only non-supply by the displayed `A_a` and cited candidate chain, not a
framework-wide impossibility. The remaining walls are unsolved bridges or
separately governed carrier/statistics/interaction choices; this packet proves
no contradiction showing that the present axioms make the next step
impossible.

## No-Go Discipline N1--N8

The positive theorem has scoped negative boundaries: the displayed `A_a` does
not itself supply the finite-`a` transfer/Gaussian Hilbert identification, a
physical carrier/statistics/taste selection, an interacting SM limit, or a
dynamical-geometry/GR joint limit. These are non-supply statements on the
displayed surface, not framework-wide impossibility claims.

### N1 — alternative-route enumeration

| attack route | marker | test and outcome | proof/authority surface |
|---|---|---|---|
| reuse the old `1+1` transfer result as if dimension did not matter | `ATTEMPTED` | fails as a proof route because the spatial phase algebra and multiplicity are absent | `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md:74-164`; arena repaired directly by current runner phase/spatial checks |
| derive the full `d=3` transfer from the canonical spatial phase algebra | `ATTEMPTED` | succeeds for `T_2`, positivity, energy, and stable multiplicity | current Sections 1--2; runner phase, spatial-square, `T_even^dag T_even`, and stable-space checks |
| use only the four-dimensional covariance/Gaussian continuum lane | `ATTEMPTED` | supplies no action-derived real-time transfer or finite-`a` Hilbert identification | `docs/FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md:121-146` |
| match only the transfer and covariance continuum dispersions | `ATTEMPTED` | rejected as insufficient; equality after the limit does not identify finite-`a` objects | current Section 1 derives both finite-`a` blocks before the limit |
| compare the blocked-time covariance pole with the stable transfer eigenvalue | `ATTEMPTED` | succeeds exactly, including the eight-dimensional solution-space map `J_z` | current Section 1; runner pole, factorization, and solution-space-intertwiner checks |
| promote the pole location/map to residue, equal-time CAR metric, and coherent-state equality | `ATTEMPTED` | not closed: the present `J_z` fixes the solution space but not residue normalization or reflected inner product | current Section 1 boundary; `docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md:14-72` is a finite-carrier candidate path, not a consumed dependency |
| use the cited Gaussian and OS rungs to claim one finite-`a` QFT object | `ATTEMPTED` | not closed: those rungs establish continuum Gaussian/conditional OS facts and explicitly leave the lattice representation bridge open | `docs/FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md:367-390` |

The route count is seven. No route is marked `RULED OUT BY PRIOR`: the exact
positive core is proved in this cycle, and the open residue/realization/SM/GR
boundaries are not no-go theorems.

### N2 — open-condition independence

Collapse the surface to six top-level conditions:

- `C1`: the supplied massive isotropic free action/scaling and declared
  `D_phys`/field/Fourier normalization;
- `C2`: the exact scalar pole--transfer identity and stable solution-space map;
- `C3`: a finite-`a` residue/equal-time-inner-product/coherent-state
  transfer-to-Gaussian representation, plus the continuum comparison topology;
- `C4`: physical realization selection (carrier, statistics, and taste/family
  rule, audited internally below);
- `C5`: an interacting chiral gauge/SM continuum limit on a supplied
  representation;
- `C6`: a dynamical-geometry/GR limit on a supplied matter family.

| pair | first closes second? | second closes first? | independent? |
|---|---|---|---|
| `C1,C2` | no: a supplied action does not prove the pole identity | no: a spectral identity does not select the scaling/normalization | yes |
| `C1,C3` | no: the action alone does not identify residues/Hilbert metrics | no: a representation theorem need not select this action | yes |
| `C1,C4` | no: displaying `A_a` does not make it physical | no: a selector need not choose `A_a` | yes |
| `C1,C5` | no: free scaling gives no interacting existence bound | no: an interacting construction can use another regulator | yes |
| `C1,C6` | no: a flat lattice supplies no dynamical metric | no: a GR limit need not use this fermion action | yes |
| `C2,C3` | no: pole location/solution space does not fix residue or inner product | no: a representation equality need not imply this algebraic formula | yes |
| `C2,C4` | no: spectral matching does not select physical realization | no: selection does not prove pole matching | yes |
| `C2,C5` | no: a free pole identity supplies no renormalization control | no: an SM limit does not force this transfer block | yes |
| `C2,C6` | no: spectral matching supplies no geometry dynamics | no: a GR limit does not force this pole identity | yes |
| `C3,C4` | no: a supplied-branch representation does not select the branch | no: branch selection does not construct the representation | yes |
| `C3,C5` | no: a free representation theorem gives no interacting limit | no: an interacting limit need not prove finite-`a` free equality | yes |
| `C3,C6` | no: Hilbert reconstruction supplies no metric dynamics | no: GR reconstruction does not fix fermion residue normalization | yes |
| `C4,C5` | no: selecting carrier/statistics/taste gives no interacting bound | no: an interacting construction on a supplied representation does not derive the selector | yes |
| `C4,C6` | no: physical matter selection gives no GR limit | no: a GR limit does not select statistics/taste | yes |
| `C5,C6` | no: an SM continuum limit supplies no dynamical geometry | no: a GR limit supplies no chiral gauge/anomaly result | yes |

The joint SM--GR compatibility residual is not a seventh independent wall: it
is a dependent composite target that can be posed only after both `C5` and
`C6` exist. Neither component supplies the other, as the `C5,C6` row records.
The internal `C4` package also does not collapse: carrier selection does not
select CAR or one taste; statistics selection does not select the carrier or
taste; and a taste/family rule does not select the carrier or statistics. The
current theorem closes `C1+C2`, gives separately conditional scalar/energy and
Gaussian consequences, and leaves `C3--C6` independently open.

### N3 — hidden-condition phrase scan

| phrase hit | classification | disposition |
|---|---|---|
| `canonical` phase/cell language | explicit analyzed-action convention | formulas for `eta_mu`, `Gamma_mu`, and both blocks are displayed; no uniqueness inference |
| `standard` OS/Wightman methodology | external theorem condition | confined to the cited conditional OS rung; full boost reconstruction is not rederived |
| `conditional` / `supplied` | explicit branch condition | CAR/quasi-free, action, and dependency status remain named |
| `stable subspace` | nontrivial spectral choice | positive `T_2`, eight-dimensional eigenspace, and `J_z` are checked; physical selection is not inferred |
| `one irreducible continuum spin block` | comparison-basis choice | full finite-`a` scalar spectrum and commutant multiplicity are kept separate from the displayed block |
| `physical normalization` | load-bearing scaling convention | now displayed as `D_phys=a^{-1}D_lat`, `chi=a^{3/2}psi`, with Fourier/block normalization named |
| `unique power law` | restricted-class uniqueness | explicitly limited to `M=m a^alpha` and fixed `2a` time normalization |
| `same-action` | algebraic provenance only | means both blocks descend from `A_a`; it does not mean residue/Hilbert equality |

The scan also checked `we assume`, `by construction`, `as is standard`,
`framework provides`, `background`, `naturally`, and `obviously`; no unclassified
hit carries theorem weight.

### N4 — citation/residual matching

| witness | witness residual | residual claimed closed here | match? |
|---|---|---|---|
| `docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md:36-166` | `d=3` transfer spectrum and quasilocal symbol, no covariance-pole link | same `d=3` transfer input | yes for transfer only |
| `docs/LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md:424-471` | continuum covariance; no carrier, Wightman, or transfer identification | same covariance input and its explicit boundary | yes; not proof of `C3` |
| `docs/FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE_BOUNDED_NOTE_2026-05-30.md:121-146` | smeared free Gaussian hierarchy; no statistics selection or OS theorem | same conditional Gaussian consequence | yes; not transfer/Gaussian equality |
| `docs/FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md:367-390` | lattice/continuum representation and boost gaps remain | current conditional OS pointer | yes only as an open-boundary witness |
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md:139-205` | massive free lattice-unit decay bound | physical scaling of that same symbol | yes after `M=am`; no interacting locality claim |
| current Sections 1--3 plus paired runner | exact pole/eigenvalue, positive factorization, `J_z`, and compact-band energy comparison | scalar same-action spectral spine | yes; sole authority for the new claim |

Every nonmatching residue/Hilbert, selector, interacting-SM, and GR residual is
left open rather than silently inherited from a citation.

### N5 — rhetoric and resolution audit

| resolution | tested? | narrow result |
|---|---|---|
| one spatial-hop eigenmode | yes | exact `2 x 2` time-block determinant and transfer roots |
| full `2^3` spatial cell at fixed momentum | yes | positive `16 x 16` `T_2`, stable multiplicity eight, and `J_z` solution-space map |
| finite periodic free carrier / CAR branch | conditional | positive second quantization and exact unitary group; no statistics selection |
| compact physical momentum band | yes | explicit comparison isometry and uniform `O(a^2)` energy multiplier convergence |
| fixed finite particle number | yes | additive-energy and unitary convergence |
| smeared free Gaussian hierarchy | dependency-conditional | covariance/Pfaffian convergence only; no equality to `Gamma(C_a)` correlators |
| continuum OS/Wightman field | dependency/methodology-conditional | candidate free reconstruction; no rederived boost operators |
| interacting lattice-wide SM or dynamical geometry | no | open; no no-go or recovery claim |
| physical TOE carrier/law | no | open; no selection or occurrence claim |

Accordingly “same-action” always means common algebraic provenance and the
scalar spectral/solution-space identity, never a completed finite-`a` QFT
representation or a unique law.

### N6 — partial-closure, convention, reframe, and primitive scan

| candidate path | live status | what it can close |
|---|---|---|
| current pole/eigenvalue and `J_z` theorem | bounded candidate, audit pending | closes `C1+C2` only |
| `docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md` | `unaudited` | finite-carrier Berezin/operator Gram equality route toward `C3`; no continuum theorem |
| `docs/FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md` | `unaudited` | supplied continuum mass-shell comparison/strong continuity; no lattice residue map |
| explicit `D_phys`/field/Fourier normalization reframe | declared convention in this source | removes a hidden normalization but does not select it physically |
| gauge-link extension of the same `A_a` | live future route, not claimed | could attack `C5` if uniform renormalization/anomaly/taste bounds are proved |
| common-clock geometric extension | live future route, not claimed | could attack `C6`; joint compatibility is testable only after `C5` also exists |
| `scale_reference_primitive` | approved meta primitive, units only | no dynamics, representation, or continuum theorem |
| `kinetic_isotropy_primitive` | approved meta primitive, kinetic form only | no OS, carrier, statistics, interacting, or GR theorem |
| `realized_state_primitive` | approved meta primitive, point evaluation only | no physical carrier/statistics/taste selection |

The primitive registry and live ledger were checked. No proposed primitive,
new admission class, convention rename, or in-flight reframe is given premise
weight. Partial closure through a bounded supplied-carrier theorem followed by
an import-retirement audit remains available; no new axiom is inferred.

### N7 — hostile steelman

A hostile reviewer should say: matching a pole and mapping its nullspace still
does not construct a quantum field. The residue fixes normalization and
equal-time projectors; the reflected Berezin Gram fixes the physical inner
product; a coherent-state representation must show that `Gamma(C_a)` produces
the same finite-`a` Schwinger functions; and a continuum comparison must carry
those projectors, tastes, and particle/antiparticle sectors, not only the
scalar energy. The strongest concrete repo route is
`docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md:14-72`, which
computes finite-carrier Berezin/operator equality and therefore demonstrates
that the missing work is real and stronger than pole matching. Its own
`docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md:273-288`
boundary leaves continuum OS/Wightman open. This steelman defeats every claim
that a unified free QFT object is already proved, but it does not defeat the
current determinant, factorization, stable-space map, or compact-band scalar
limit. The theorem is narrowed accordingly.

### N8 — cross-cycle echo

| prior path | live status | later escape/change mechanism | implication here |
|---|---|---|---|
| `docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md` | `unaudited` historical anchor | later `d`-dimensional phase algebra removed the `1+1` arena restriction | do not cite `1+1` alone as `3+1` authority |
| `docs/FREE_STAGGERED_TWO_STEP_DISPERSION_D_DIMENSIONAL_NARROW_THEOREM_NOTE_2026-06-12.md` | `unaudited` | current blocked-time calculation adds the missing pole link | keep the new claim scalar-spectral |
| `docs/FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION_CONDITIONAL_THEOREM_NOTE_2026-05-30.md` | `unaudited` | its gap `G1` exposed the false lattice/continuum assembly | do not rename a conditional continuum theorem as finite-`a` equality |
| `docs/MIXED_OS_TRANSFER_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md` | `unaudited` | finite-carrier Berezin/operator computation supplies a stronger next route | attack residue/Gram equality next rather than infer it |
| `docs/TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md` | `unaudited` | strict locality was retired in favor of exponential quasilocality | retain physical decay scale, not strict support |
| Campaign 5 scalar/two-band QCA blocks | branch-local, audit pending | larger carriers and quasilocal generators escaped strict scalar classes | do not infer carrier uniqueness from this free family |

Each echo is retired by an explicit arena extension, stronger representation
calculation, or scope narrowing. None is used to infer an axiom-update need.

**No-Go Discipline verdict:** `PASS` for the displayed same-action scalar
spectral theorem and its explicitly conditional free consequences. It is
`FAIL` for a completed finite-`a` QFT/Hilbert identity, physical selector,
interacting SM, GR, joint TOE, or axiom-update conclusion; none is shipped.

## Runner coverage

The deterministic runner checks:

- exact 4D and 3D staggered Clifford phase algebras;
- the full action's scalar `D^dag D` spectrum;
- the `Cl_4` generated-algebra and commutant dimensions fixing four spin blocks;
- the spatial-hop square and action recurrence;
- the blocked-time determinant;
- `T_2=T_even^dag T_even`, the pole--transfer identity, the eight-dimensional
  stable solution-space map, and a one-step negative control;
- uniqueness of `M=am` in the power-law mass-scaling class;
- compact-band `O(a^2)` energy and covariance convergence;
- positive Fock contraction, explicit log/additive-energy equality,
  nonnegative `H_a`, and exact unitarity;
- an actual smeared `S_a` Nambu-doubled Pfaffian convergence check and
  continuum SO(4) covariance;
- taste multiplicity and the physical quasilocal scale;
- source guardrails and N1--N8 presence.

Reproduction:

```bash
python3 scripts/free_staggered_3plus1_same_action_transfer_gaussian_continuum_2026_07_12.py
```

Expected final line: `SCORECARD: PASS=23 FAIL=0`.

## Honest status

This is a bounded theorem for one explicitly specified massive free family. Its
new exact content is the same-action scalar pole--transfer identity, the stable
solution-space intertwiner, and the controlled physical energy/quasilocal
scaling. The cited free covariance, Gaussian, and conditional OS rungs give a
candidate conditional continuum chain, but all five dependencies are presently
`unaudited`. The missing residue/equal-time-CAR/coherent-state bridge prevents a
claim that one finite-`a` QFT/Hilbert object has been constructed. This is not
the full continuum campaign: that representation bridge, the interacting SM,
statistics/taste selection, and the dynamical-geometry/GR joint limit remain
open and are the next campaigns.
