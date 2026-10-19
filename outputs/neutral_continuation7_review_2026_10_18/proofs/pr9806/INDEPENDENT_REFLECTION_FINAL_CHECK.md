<!-- Original PR9806 source SHA256 acb2d5f610613318e9b0927568989ab1fc1d66b99095c3acda110fa3627d924e. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Final reflection-ground-sector check

Disposition: PASS for the exact finite-even-lattice existence theorem and its coupling to a previously established unique positive-sector low ground. No mathematical fix requested in REFLECTION_GROUND_SECTOR_PROOF.md. One stale cross-document statement is noted below.

## Matrix and character argument

The two polar factors have the same Hilbert-Schmidt norm as the original state. For real symmetric h the average of their internal energies equals the original internal energy. The crossing trace inequality follows from Hilbert-Schmidt arithmetic-geometric mean after the polar decomposition, including a unitary extension when the state matrix is singular. Negative crossing coefficients turn it into E(Psi)>=[E(P)+E(Q)]/2; since neither replacement can have energy below the ground energy, both replacements of a ground vector are ground vectors. This does not require an invertible coefficient matrix or a stoquastic basis.

For a real involution A spanning a cut, A Psi A=s Psi implies commutation of both reduced density matrices with A, so both positive square roots have spanning character +. For a plane in one half, its definite character restricts the support of the corresponding reduced density matrix. Its square root retains that support, and its Hermiticity gives the right-side constraint as well. Thus copying contained characters is valid simultaneously for the whole commuting plane family. It does not require selecting a special polar unitary.

I checked the primary reference, Lieb and Schupp, [Singlets and reflection symmetric spin systems](https://arxiv.org/html/math-ph/9910037v1), Eq. (4), which supplies the general trace inequality. The compass-specific character conclusion comes from the argument above and the following parity counts, not from the paper's singlet conclusion.

## Both periodic cuts

Reflection x->R-1-x pairs both periodic boundary bonds with their reflected sites. They are -Jlambda X tensor conjugate(X). Internal YY terms contain two imaginary factors and are real; reflected internal Hamiltonians agree. A spanning half-Y plane has 5R sites, even when R is even, so its transpose and conjugate signs are positive. Spanning Z is real directly. The first replacement sets all Y and Z characters positive and leaves a definite, reflected X pattern.

At the y cut, the right-half product of Z reverses every crossing YY bond on both boundaries. It leaves internal XX/YY bonds unchanged because both endpoints are twisted together, and leaves ZZ unchanged. The resulting crossing is +Jlambda Y tensor Y=-Jlambda Y tensor conjugate(Y), with identical real internal Hamiltonians.

This twist commutes with every full plane: its intersection with an X plane is 5R sites, with a contained Y plane 10R sites, and it commutes sitewise with Z. Therefore it preserves all inherited characters. At the second replacement, spanning X and Z become positive, while contained Y planes copy their already positive character. Undoing the twist preserves all positives and restores the original Hamiltonian.

All cross-family plane intersections have even length (R or 10), so the initial simultaneous-character ground vector exists. The all-positive character assignment is also compatible with global operator-product phases: 10R^2 is a multiple of four. The length-two periodic multibond convention merely repeats nonnegative crossing couplings and does not invalidate the argument.

## Consequence for the pole state

For every finite even R and positive J,lambda the positive plane sector contains a global ground vector. Thus its restricted minimum equals the unrestricted minimum exactly. If the inherited controlled low-energy construction proves the restricted ground is unique along the small-lambda grid family, that unique restricted state is necessarily one of the global ground states. No estimate of the splitting between plane characters is needed for this existence statement.

The original ZZ readout, including its Fourier-weighted form, commutes with all plane symmetries: every relevant X or Y plane either meets a vertical ZZ term in both sites or in none. Its spectral measure from this ground therefore stays in the same sector. Degenerate grounds in other characters cannot contaminate the source projector denominator. Within the chosen sector, the inherited ground and pole isolation bounds still supply the denominators; reflection positivity itself proves no excitation gap.

The proof correctly says 'there exists an actual global ground state' and does not assert that all ground states have the same response, that the full ground is unique, or that a physical preparation selects it. The isotropic pole and its source coefficient remain consequences of their separate low-energy theorem, not of the reflection inequality alone.

## Replayed controls and integration note

Ran native/neutral_reflection_ed.py without changing it. All six 2x2x2 / 2x2x4 cases completed. Maximum absolute unrestricted-minus-sector ground-energy difference: 9.24e-14. Maximum source-sector eigenvector residual: 3.36e-12. Maximum plane-expectation deviation from +1: 1.34e-15. Output: /tmp/neutral_reflection_review_replay.json. These test signs and finite projector implementation; they are not the large-size proof.

ISOTROPIC_BOUND_FEATURE_PROOF.md still describes uniform global-ground selection as open in its introductory/final wording. That should be narrowed or linked to this new result: existence of a positive-sector global ground is now proved, while uniqueness and quantitative character splitting remain open. This is a documentation integration issue, not a flaw in the new theorem.

## Source identities
- REFLECTION_GROUND_SECTOR_PROOF.md: 23b7f439e2ad66896a01700867927630a7098adbbb456a4ea26ea9ff8c540945
- INDEPENDENT_REFLECTION_GROUND_CHECK.md: 3ec959d096d8959a4b830efd6a86d28f2c84c56da9dc24089653ec6bd4fdb333
- neutral_reflection_ed.py: 1d468c2cdf6a53e051535ae03844ebb2386d8a4bffa17c8f4c6528af51c8116f

No shared files edited and no formal audit applied.
