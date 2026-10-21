# Energy equality for supplied antiunitary-exchanged sectors

**Date:** 2026-05-02; source scope corrected 2026-10-21
**Type:** positive_theorem
**Claim scope:** a Hermitian Hamiltonian and a supplied commuting antiunitary map have equal energies on mapped eigenstates. If the map exchanges two invariant sectors, their spectra agree. Physical CPT, particle/antiparticle sector identification, momentum/spin action and rest-mass interpretation are separate supplied bridges.
**Status authority:** independent audit lane only; no retained status asserted.
**Runner:** [`cpt_particle_antiparticle_mass_equality_check.py`](../scripts/cpt_particle_antiparticle_mass_equality_check.py)

## Conditional statement and proof

Let H be Hermitian on a finite-dimensional complex Hilbert space and let Theta be antiunitary with `Theta H Theta^-1=H`. Let `H psi=E psi`. Hermiticity gives real E, so

```text
H(Theta psi) = Theta(H psi) = Theta(E psi)
            = conjugate(E) Theta psi = E Theta psi.
```

Antiunitarity preserves nonzero norm. Thus Theta psi is an eigenstate of the same energy. If invariant subspaces A and B obey `Theta(A)=B`, the bijection preserves multiplicities and their spectra agree. The same statement holds for a unitary symmetry. For unbounded operators, the corresponding domain-preservation hypothesis is additionally required; that extension is not the finite runner's subject.

This theorem is independent of numerical energy values. It does not require a particle interpretation or guarantee a distinct partner when Theta maps an eigenstate to itself. A pair of distinct physical species requires a separately established sector exchange.

## Relation to the repository's antiunitary example

The [exact free staggered source](CPT_EXACT_NOTE.md) distinguishes its real anti-Hermitian hopping D from the Hermitian lift `H=iD`. It defines `Theta_H=PK`, proves `Theta_H H Theta_H^-1=H` for even periodic lattice sizes, and explicitly does not identify that matrix symmetry as physical CPT. Its old `CPK` representative flips H rather than preserving it. The source is an example of the algebraic symmetry hypothesis, not authority for a physical particle interpretation.

Accordingly this note does not infer a momentum map `p -> -p`, a spin/helicity flip or species exchange from that source. If a sector/momentum label map tau is independently supplied, the theorem gives only `E_B(tau(label))=E_A(label)`. Translation invariance alone does not imply `E(p)=E(-p)`.

## Physical interpretation remains conditional

Calling A/B particle and antiparticle sectors requires a physical identification and the corresponding antiunitary action. Interpreting a p=0 eigenvalue as rest mass requires an appropriate physical Hamiltonian, vacuum-energy reference and mass/dispersion bridge; a random finite Hermitian block can have negative energies and carries no momentum labels. If those bridges and a map between the rest sectors are supplied, their rest energies, and hence the correspondingly defined masses, agree. The algebra does not supply the bridges.

A finite Hermitian spectrum contains neither resonance widths nor an inverse-lifetime operator. Lifetime equality requires a matched decay/scattering framework. Magnetic moments require a current/vertex and its symmetry action. Factoring an unspecified antiunitary into C, P and T does not determine a separately meaningful C or its square. No such corollaries or observational precision are asserted here.

## Runner scope and inputs

The runner constructs `H=diag(A,conjugate(A))` for Hermitian two-by-two A and uses block swap followed by conjugation. It tests Hermiticity, the antiunitary symmetry, equal block spectra and five further seeded examples. A deliberately unequal-block control breaks both this symmetry and spectrum equality; it is one counterexample to dropping the symmetry, not a proof that every symmetry violation splits spectra.

These are four-dimensional block matrices, not a four-mode fermionic Fock space. No statistics, physical momentum, species, rest masses or upstream staggered lattice is executed. NumPy and fixed seeds supply the numerical witnesses. The algebra above supplies the quantified finite-dimensional implication.

```bash
python3 scripts/cpt_particle_antiparticle_mass_equality_check.py
```

The previous physical-CPT wording and removed lifetime/magnetic/C-square claims are recoverable at commit `f24d17d97d372df977476e4a69674577f31af575`. The stable historical filename and primary runner identity are preserved for consumers. Review evidence grants no audit verdict.
