# A native defect couples to the neutral background through its motion

Status: bounded-support. A prepared heavy spin defect in the existing
one-qubit Hamiltonian has a derived loop vertex into the same neutral
plaquette operator that appears in the collective slab model. No additional
interaction or assigned scalar coupling is needed for this connection.

The proof (`outputs/neutral_continuation6_review_2026_10_18/proofs/pr9791/NATIVE_PROBE_LOOP_PROOF.md`)
derives the N=2 hopping signs directly from physical XX and YY actions. Four
native hops around a square multiply to the existing plaquette operator.
The rooted fourth return moment is 28I+2 sum of incident plaquettes. On the
hopping time scale this gives a neutral transition amplitude tau^4/12 times
that sum, with controlled fixed-box errors. A selected individual loop has
positive neutral weight: its vacuum plaquette variance is at least 0.36.
Position selection remains an explicit protocol, not a derived detector.

The environment cannot simply be identified with the vacuum field. At fixed
box and weak coupling the relaxed heavy sector prefers flat plaquette flux
at order lambda; the vacuum background is selected at order lambda^4 and
has different correlations. This difference follows from the Hamiltonian.
A prepared-probe vertex is therefore distinguished from the unresolved
coupling of a fully dressed, spatially extended matter feature.

[Replay](../scripts/native_probe_loop_coupling.py) checks physical Pauli
matrix elements, exact closed-path words, finite prepared-return evolution,
and flat-environment selection. Numerical work is exposed development data,
not an empirical fit. The sixteen-spin/slab structure is not a derived
three-dimensional fermion or scalar, and the vertex is not a universal
coupling to mass or a cosmological identification.


## Source and execution boundary

Claim type: bounded_theorem.
Primary runner: `scripts/native_probe_loop_coupling.py`

The complete mathematical sources and owning-head helpers are portable literal inputs. The supplied Hamiltonian, geometry, state, observable and order of limits remain premises. The primary executes finite coefficient and algebra controls under one enforced aggregate cap, streams child diagnostics, and writes fresh isolated outputs. Analytic asymptotic and microscopic transfer results are supplied by the complete proofs, not numerically established by finite controls. Historical verdicts and saved numerical diagnostics confer no current authority.
