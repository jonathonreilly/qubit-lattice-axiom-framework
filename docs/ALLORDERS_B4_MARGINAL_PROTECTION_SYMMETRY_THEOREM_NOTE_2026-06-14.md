# All-Orders B4 Marginal-Velocity Protection: a Symmetry Theorem with First Two-Loop Confirmation

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-14
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome.

**Primary runner:**
[`scripts/frontier_allorders_b4_marginal_protection_twoloop_2026_06_14.py`](../scripts/frontier_allorders_b4_marginal_protection_twoloop_2026_06_14.py)
**Cached runner output:**
[`logs/runner-cache/frontier_allorders_b4_marginal_protection_twoloop_2026_06_14.txt`](../logs/runner-cache/frontier_allorders_b4_marginal_protection_twoloop_2026_06_14.txt)

## What is new here

The retained one-loop note
[`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
establishes the **one-loop** marginal-velocity protection (`Sigma_t = Sigma_s`
by an axis relabel of the one-loop measure). The free-`SO(4)` note
[`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
asserts the marginal protection is *"all-orders by the exact `B4` temporal-spatial
axis relabel"* — but supplies **no explicit all-orders argument** and **no
beyond-one-loop check**.

This note adds a bounded, perturbative support theorem inside a supplied
`B4`-symmetric Wilson/staggered regulated action:

1. **The explicit all-orders symmetry theorem inside that supplied regulator.**
   The protection is reorganized
   from an order-by-order relabeling fact into a single Ward-style symmetry
   statement: the *regulated action and integration measure are exactly
   `B4`-invariant*, therefore the perturbative effective action `Gamma` is
   `B4`-invariant order-by-order, therefore the `B4`-non-invariant marginal
   velocity operator has vanishing coefficient at **every** order. The zero is a
   symmetry, not an accident of any one diagram.
2. **The first two-loop confirmation.** A representative genuinely
   eight-dimensional two-loop self-energy channel is computed; its marginal
   velocity coefficients satisfy `Sigma_t = Sigma_s` on the OS0 surface to
   machine precision, and a deliberate `B4` break makes them differ. This is the
   first beyond-one-loop numerical evidence for the protection.

A scout of `origin/main` (and the current branch) found no note giving either
piece.

## The theorem

Work on the symmetric `Z^4` regulator block with the regulated action

```text
    S = S_gauge(Wilson plaquette) + S_fermion(staggered, eta_0 = 1)
```

and the hypercubic integration measure `prod_{x,mu} dU(x,mu) * prod_x d psi(x) d psibar(x)`.

**(A) The supplied regulated action and measure are exactly `B4`-invariant.**
`B4` is the signed-permutation group of the four Euclidean axes, `|B4| = 2^4 * 4! = 384`.

- The Wilson plaquette action density `sum_{mu<nu} (1 - (1/N) Re Tr U_{mu nu})`
  is invariant under all 384 elements (an axis relabel is a lattice automorphism
  that permutes the plaquette set; orientation reversal is absorbed by
  `Re Tr U_P = Re Tr U_P^dagger`).
- The staggered phase `eta_mu(x)` closes the Kogut-Susskind plaquette identity
  `eta_mu(x) eta_nu(x+mu) = - eta_nu(x) eta_mu(x+nu)` for every axis pair, and
  the free staggered fermion kinetic form
  `D_F(k) = sum_mu sin^2 k_mu + (M_0 + r sum_mu (1 - cos k_mu))^2` is invariant
  under all 384 elements because `sin^2` and `(1 - cos)` are even and `eta_0 = 1`
  treats the temporal axis on the same footing as the spatial axes.
- The integration measure is `B4`-invariant: the per-link Haar measure is
  left-invariant (`U -> V U` is an exact measure-preserving bijection for unitary
  `V`), and an axis relabel is a measure-preserving permutation of the product
  factors; the Grassmann measure reindexes by the same site bijection up to a
  fixed overall sign absorbed in normalization.

This is the **load-bearing supplied premise**. Runner Part A checks the finite
action/measure invariance claims used here, but the theorem does not derive the
choice of regulator action from the repo axioms.

**(B) `B4` leaves exactly one diagonal marginal kinetic coefficient.** The
diagonal quadratic form `c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2)` has a
one-dimensional `B4`-invariant subspace, so `c_t = c_s` is forced; the spatial
cubic group `O_h` plus a free temporal coefficient leaves two. (Reynolds-operator
rank; runner Part B.)

**(C, all-orders conclusion).** A symmetry of the regulated action **and** measure
is a symmetry of the generating functional `Z[J]`, hence of the perturbative
effective action `Gamma[phi]` order-by-order in the loop expansion. By (B) the
only `B4`-invariant diagonal marginal kinetic form has `c_t = c_s`; therefore the
coefficient of the `B4`-non-invariant marginal velocity operator
(`c_t p_t^2 + c_s p_s^2` with `c_t != c_s`) is identically zero in `Gamma` at
**all** perturbative orders for species/channels whose regulated kinetic and
interaction terms transform covariantly under this same supplied `B4` action.
The protection is one symmetry
constraint holding at every order — not an order-by-order cancellation.

**Why this is anomaly-free (the rigor closes here).** `B4` is a **finite** lattice
automorphism (`|B4| = 384`) acting by **permuting** sites and link variables; its
action on the path-integral measure is therefore a variable permutation whose
Jacobian is a constant `±1` (a permutation determinant), **not** a field-dependent
Jacobian. A Fujikawa anomaly requires a continuous rotation with a field-dependent
Jacobian and a regulator that cannot preserve the symmetry; here the lattice **is**
the manifestly `B4`-symmetric regulator (no separate UV step can secretly break
`B4`), and the Grassmann permutation sign is global and cancels in `Z^{-1}∫(...)`
for every connected correlator. So this is the standard statement "a manifest
symmetry of a regularized theory is a symmetry of all 1PI vertex functions,"
rigorous precisely because the lattice is the regulator.

## Confirmations

**One loop, two distinct channels (runner Part C).** The gauge-rainbow marginal
velocity self-energy gives `Sigma_t - Sigma_s = 0` on OS0 to machine precision
(`<= 9e-19` across resolutions), and a power-divergent channel gives
`Sigma_t - Sigma_s = 0` on the cut OS0 measure to machine precision
(`<= 2e-18`).

**Two loops — the new part (runner Parts D, D').** The representative channel is
the dressed-rainbow / sunset-family fermion self-energy: the fermion line carries
`k = p e_mu + q + r` with two independent loop momenta `q, r` (8D total), two
gluon lines `G(q), G(r)`, and a `B4`-invariant vertex
`V(q,r) = 1 + c sum_nu qhat^2_nu(q) qhat^2_nu(r)` coupling both loop momenta. The
marginal coefficient `Sigma_mu = (1/2) d^2 Sigma / d p_mu^2 |_{p=0}` is extracted
analytically inside the integrand, giving an `O(1)`-scale nonzero number, so the
`B4` test is an exact equality of two non-trivial numbers (not a finite-difference
of noise). On OS0:

```text
    Sigma_t = Sigma_s = -0.173713...,   |Sigma_t - Sigma_s| = 3.9e-16   (nk=6, 1.68e6 pts)
    Sigma_t = Sigma_s,                  |Sigma_t - Sigma_s| = 6.2e-17   (nk=8, 1.68e7 pts)
```

The zero is robust across the integrand: varying the vertex coupling
`c in {0, 0.7, 2.0}` (so `Sigma_mu` ranges over `-0.02 ... -0.46`) leaves the OS0
difference at machine precision (`<= 2e-15`) in every case. In particular `c = 0`
severs the vertex coupling, so the only `q`-`r` coupling left is the genuine 8D
fermion line `D_F(q+r)` — and the zero survives there, proving the protection is
the two-loop fermion-line `B4` covariance, not a vertex artifact.

What the two-loop result *adds* over one loop is not a new cancellation but a
confirmation that the **same** single symmetry constraint operates on a genuinely
**non-factorizable** 8D integrand (next section): if the all-orders protection
relied on order-by-order cancellation rather than the manifest `B4` symmetry, a
two-loop integral whose loop momenta enter a shared, non-factorizable denominator
would be exactly where that cancellation could first fail — and it does not.

**Genuine eight-dimensionality (runner Part D').** The two-loop channel is not a
relabeled one-loop sum:

- the fermion denominator `D_F(p + q + r)` does **not** factorize as `f(q) g(r)`
  (witnessed by `D(q1+r1) D(q2+r2) != D(q1+r2) D(q2+r1)`);
- the full 8D double sum differs from any factorized `4D x 4D` surrogate by an
  `O(1)` relative amount (`r` is a genuine second loop, not a spectator);
- the `B4` element `g = (axis 0 <-> axis 1)` acts on **both** `q` and `r`
  simultaneously, and that joint relabeling is a bijection of the 8D summation
  domain carrying the direction-0 integrand onto the direction-1 integrand.

So the two-loop zero comes from the genuine two-loop integrand being mapped onto
its axis-swapped image, exactly as the symmetry theorem predicts.

## Falsification (runner Part E)

A deliberate `B4`-breaking insertion — an anisotropic temporal gluon block
`xi != 1` applied in **both** internal gluon lines — makes `Sigma_t - Sigma_s`
nonzero at one loop (`1.8e-3` at `xi = 2`) **and** at two loops
(`7.1e-5` at `xi = 2`, versus the `3.9e-16` machine zero at `xi = 1`). The zero
therefore tracks the `B4` symmetry, not the numerical grid: it is genuine
`B4` covariance, not a quadrature artifact.

The first surviving (`B4`-invariant) lattice anisotropy is the dimension-6
hypercubic dispersion term (`k^4` coefficient `-a^2/3`), which is Planck-suppressed
under the approved scale-reference primitive `a^{-1} = M_Pl`.

## Honest scope

This is a bounded perturbative all-orders marginal-protection statement,
resting on the supplied **exact** `B4`-invariance of the regulated action and
measure (checked in Part A), confirmed numerically at one and two loops. It does
**not** address: non-perturbative effects; the `a -> 0` continuum limit; genuine
taste-**breaking** or per-single-taste effects;
or the continuous-time obstruction horn, where `B4` is **broken** (the temporal
integral is uncut while the spatial Brillouin zone is cut), and the protection
genuinely fails. It **consumes**, and does not derive, the
`kinetic_isotropy_primitive` (`c_t = c_s`, OS0).

## Dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — the approved primitive supplying the OS0 kinetic-form premise (`c_t = c_s`);
  chain-satisfies without bounding. Consumed, not derived.
- [EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  — the retained one-loop marginal protection this note generalizes.
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
  — the source of the bare "all-orders by exact axis relabel" assertion now made
  explicit.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md) — cited only for the
  axiom boundary; supplies no time dynamics.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md) — the
  units conversion `a^{-1} = M_Pl` used in the dimension-6 size estimate.

## Comparator literature (cross-check only, not derivation inputs)

- Reisz, *Communications in Mathematical Physics* **116** (1988) — lattice
  power-counting; comparator for the statement that the surviving lattice Lorentz
  violation begins at the dimension-6 (irrelevant) operator on the cut measure.
- The retained `B4` note above is the framework comparator for the one-loop
  boundary.

No fitted, PDG, lattice-Monte-Carlo, or `beta = 6` inputs are used; the runner
checks the supplied lattice-action symmetry and loop-integral consequences
without empirical inputs.
