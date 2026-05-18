# PL-Topology Infrastructure — Named Non-Derivation Imports

**Date:** 2026-05-17
**Claim type:** bounded_theorem
**Status:** bounded named-import wrapper bundling four textbook
PL-topology results consumed by the `S^3` cap-map uniqueness chain.
**Status authority:** independent audit lane only.

## Purpose

This wrapper note documents four standard accepted PL-topology /
geometric-topology results as named non-derivation imports so
downstream rows (notably
[S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md))
can register a one-hop dependency rather than carry the four textbook
results as unattributed accepted-mathematics infrastructure.

## Imports covered

### 1. PL Schoenflies / Alexander 1924

Statement: every PL `(n - 1)`-sphere PL-embedded in PL `S^n` separates
`S^n` into two components, each of whose closure is a PL `n`-ball. In
dimension `n = 3`, this is Alexander's PL-Schoenflies theorem.

Reference: J. W. Alexander, "On the subdivision of 3-space by a
polyhedron," *Proc. Nat. Acad. Sci.* **10**, 6-8 (1924).

Generalized form: M. Brown, "A proof of the generalized Schoenflies
theorem," *Bull. Amer. Math. Soc.* **66**, 74-76 (1960); B. Mazur, "On
embeddings of spheres," *Bull. Amer. Math. Soc.* **65**, 59-65 (1959).

Role in the `S^3` chain: provides the **global exhaustiveness** step.
Every PL 3-complex closure of the cubical ball `B` that yields a
closed simply-connected PL 3-manifold is, by Schoenflies, a PL 3-ball.

### 2. Alexander 1930 cone theorem

Statement: every PL `3`-ball is PL-homeomorphic to the cone on its
PL `S^2` boundary.

Reference: J. W. Alexander, "The combinatorial theory of complexes,"
*Annals of Math.* **31**, 292-320 (1930).

Role in the `S^3` chain: combined with PL Schoenflies, this completes
the global uniqueness: every PL 3-ball closure is PL-homeomorphic to
`cone(partial B)`.

### 3. Alexander trick (1923) + `MCG(S^2) = Z / 2` (Smillie 1977)

Statement: every self-homeomorphism of `S^n` extends to a
self-homeomorphism of `D^{n+1}` (the Alexander trick). Together with
the fact that the mapping class group of `S^2` is `Z / 2` (only
orientation-preserving vs. orientation-reversing isotopy classes),
this gives PL-rigidity of cone-cap gluing maps.

References: J. W. Alexander, "On the deformation of an `n`-cell,"
*Proc. Nat. Acad. Sci.* **9**, 406-407 (1923); J. Smillie, "Flat
manifolds with non-zero Euler characteristics," *Comment. Math. Helv.*
**52**, 453-456 (1977).

Role in the `S^3` chain: shows that any two cone caps are
PL-homeomorphic; the cone cap is unique up to PL homeomorphism.

### 4. Perelman 2003 + Moise 1952

Statement: every closed simply-connected 3-manifold is homeomorphic
to `S^3` (Perelman, completing the Poincaré conjecture); every
topological 3-manifold has a unique PL structure (Moise). Composed,
this gives: every closed simply-connected PL 3-manifold is
PL-homeomorphic to PL `S^3`.

References: G. Perelman, "The entropy formula for the Ricci flow and
its geometric applications," arXiv:math/0211159 (2002-2003);
E. E. Moise, "Affine structures in 3-manifolds, V: the triangulation
theorem and Hauptvermutung," *Annals of Math.* **56**, 96-114 (1952).

Role in the `S^3` chain: identifies the closed simply-connected PL
3-manifold `M = B ∪ cone(partial B)` with PL `S^3`.

### 5. Kawamoto-Smit 1981 staggered-fermion uniformity

Statement: the Kawamoto-Smit staggered fermion lattice action requires
uniform nearest-neighbor hopping at every lattice site. An open
cubical ball with cubically-boundary vertices is physically
inhomogeneous; closure of the cubical ball to a manifold without
boundary is required by the lattice action structure.

Reference: N. Kawamoto & J. Smit, "Effective Lagrangian and dynamical
symmetry breaking in strongly coupled lattice QCD," *Nucl. Phys. B*
**192**, 100-124 (1981).

Role in the `S^3` chain: provides the physical-closure premise — the
cubical ball must be closed to a manifold without boundary by the
lattice action's homogeneity requirement.

## What this note does NOT claim

- This is NOT a re-derivation of any of the cited theorems.
- This is NOT a framework-level derivation of the cubical ball closure
  from `Cl(3)` on `Z^3` alone — the Kawamoto-Smit homogeneity premise
  is a separate lattice-QFT input.
- The bounded scope is the named non-derivation import only.

## Standard textbook reference (PL topology)

- C. P. Rourke & B. J. Sanderson, *Introduction to Piecewise-Linear
  Topology*, Springer (1972). The PL Schoenflies theorem appears as
  Theorem 3.21; handle decomposition of PL manifolds with boundary as
  Theorem 6.13.

## Downstream usage

This wrapper is consumed by:

- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) — registers
  the four PL-topology imports plus the Kawamoto-Smit homogeneity
  premise as one-hop named non-derivation authorities for the cone-cap
  uniqueness chain.

## Boundary

This wrapper note is a named-import-only bounded theorem covering five
named PL-topology / lattice-QFT imports. It does not claim:

- a framework derivation of any of the imported textbook theorems;
- closure of any downstream `S^3` compactification or topology chain;
- a tighter audit-tier status for the consumers.

Its only function is to provide a citeable one-hop authority for the
five textbook imports so downstream notes register them cleanly
instead of carrying them as accepted-mathematics infrastructure
without an audit-lane handle.
