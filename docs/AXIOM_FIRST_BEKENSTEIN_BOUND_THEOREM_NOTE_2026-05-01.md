# Bekenstein-bound geometry and the missing entropy premise

**Date:** 2026-05-01; source correction 2026-10-21.
**Type:** bounded_theorem (only the stated conditional algebra; no physical entropy theorem)
**Source scope:** geometric identities and a counterexample to the former B2 inference.
**Status authority:** independent audit lane only; no audit verdict is set here.
**Runner:** `scripts/axiom_first_bekenstein_bound_check.py`

## Correction

The former B2 asserted that every sub-Schwarzschild system obeys
`S_matter(R,E)<=S_BH(M=E)=4 pi G E^2`. The cited inputs did not justify
compressing an arbitrary system into a black hole of the same energy while
ignoring work, radiation and exterior entropy. A generalized second law
cannot supply that unproved process. B3 consequently does not follow.
The old universal theorem and its claimed corollaries are withdrawn.
The GSL companion likewise does not establish this missing premise.

A finite countermodel to the stated assumptions is a maximally mixed qubit
with Hamiltonian `H=E I`, E=0.01, R=100 and G=1. It has nonnegative energy,
`2GE<R`, and entropy log(2), whereas `4 pi G E^2=0.0012566...`.
It even satisfies `log(2)<2 pi R E`, so it distinguishes the false stronger
B2 from the desired Bekenstein expression. This tests the sufficiency of
the listed algebraic/energy assumptions; it is not a construction of a
complete localized gravitational system.

## Exact geometric content

Supply Schwarzschild geometry and G>0 in units hbar=c=k_B=1. For
0<=2GE<=R,

```
A_BH(E)=16 pi G^2 E^2 <= 8 pi G R E,
S_BH(E)=4 pi G E^2 <= 2 pi R E.
```

Equality holds when R=2GE. These statements compare functions of R,E;
they impose no bound on an independent matter entropy. Even importing the
area bound `S<=A(R)/(4G)=pi R^2/G` would not repair B3: for 2GE<R this
area bound is *larger* than 2 pi R E, so it does not imply the desired
stronger inequality.

No uniqueness of an entropy maximizer, generic cosmological correction or
covariant entropy bound follows from these elementary identities.

## What an entropy-bound derivation would require

The choice of state, region, energy and entropy definitions matters. For
example, [Casini's relative-entropy formulation](https://arxiv.org/abs/0804.2182)
uses a region's vacuum reference state and relative entropy, rather than
asserting a bound on arbitrary un-subtracted matter entropy. An application
to this framework would have to define those objects and verify the relevant
hypotheses; this source does not do so. The familiar 2 pi R E expression
therefore remains a conditional external target here, not a result derived
from the supplied spectrum condition and area coefficient.

## Verification and provenance

The runner checks the geometric inequality and saturation, the qubit
countermodel to B2, and the ordering of the radius-area bound. It does not
select entropy values below a target and call the resulting sweep a proof.
The former argument is recoverable at commit
`f24d17d97d372df977476e4a69674577f31af575`; the filename is retained for
stable references. Historical citations below are provenance, not current
authority or a replacement proof.

## Citations

- A_min: [`MINIMAL_AXIOMS_2026-04-11.md`](MINIMAL_AXIOMS_2026-04-11.md)
- historical framework GR action: [`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md),
  [`UNIVERSAL_GR_LORENTZIAN_GLOBAL_ATLAS_CLOSURE_NOTE.md`](UNIVERSAL_GR_LORENTZIAN_GLOBAL_ATLAS_CLOSURE_NOTE.md),
  [`UNIVERSAL_QG_CANONICAL_TEXTBOOK_GEOMETRIC_ACTION_EQUIVALENCE_NOTE.md`](UNIVERSAL_QG_CANONICAL_TEXTBOOK_GEOMETRIC_ACTION_EQUIVALENCE_NOTE.md)
- historical BH 1/4 carrier composition:
  [`BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md`](BH_QUARTER_WALD_NOETHER_FRAMEWORK_CARRIER_THEOREM_NOTE_2026-04-29.md)
- historical primitive coframe carrier:
  [`PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md`](PLANCK_PRIMITIVE_COFRAME_BOUNDARY_CARRIER_THEOREM_NOTE_2026-04-25.md)
- spectrum condition:
  [`AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md)
- historical cluster decomposition (used implicitly):
  [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- historical external references:
  Bekenstein (1981) *Phys. Rev. D* 23, 287;
  Bousso (1999) *JHEP* 9907, 004;
  Bousso (2002) *Rev. Mod. Phys.* 74, 825;
  Casini (2008) *Class. Quantum Grav.* 25, 205021.
