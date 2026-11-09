# Partial-terminal continuation: repo and literature record

2026-11-09. Source checkout 4a3f6be4cf4ea0321bb5042c2969fc035479e7c2;
current main bf92a1d763030836ed55631d5d7a7ef3b288f284. Read-only extraction
was performed by the explicitly requested gpt-6-luna worker at low effort,
in a fresh context. The supervisor checked the mathematical premises used
below and owns the subsequent proofs and scope judgments. This inventory
does not confer scientific or audit status.

## Existing repo work used

Luna read the complete two-region note
docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md
(SHA-256 94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c).
The decisive existing results are equations (2)-(10): actual Q_xi,
source-dependent posterior disintegration, covariance subtraction, total
covariance, source response of conditional means, and the exterior marginal
needed to reconstruct the unconditioned Wilson covariance. Equations
(22)-(24) already retain the conditional covariance in adjacent-plaquette
and boundary responses. Section 7 names the missing uniformity along the
weak-coupling trajectory and under actual subsequent blocking.

Luna also extracted the exact distinct-link score identity R3 and the Q
subtraction R24 in parts/full-connected-four-response.md, and the complete
source/orbit law from parts/compact-forest-exchange.md. Those arguments
specify a fixed-terminal numerator. They do not identify it with the law
obtained by integrating a subset of terminal outputs. Source hashes are
recorded in the two new proof parts and their check report.

The canonical older notation is Q_xi, not Q_B(V_Bc). The continuation
explicitly defines J as integrated terminal links and O as held terminal
links to prevent confusing an integrated variable with an exterior
parameter. If a derivative includes a variable in J, Q_J is independent
of it. If both varied links lie in O, its mixed coefficient remains.
This distinction was present in the existing normalization identities.

The new finite two-step specialization and all fifteen conditioning terms
are in [the exact normalization proof](../parts/partial-terminal-normalization.md).
The supervisor separately reconstructed the residual component-gauge action
using the compact forest and the Gaussian supplier's Haar convention; see
[the geometry proof](../parts/released-terminal-gauge-directions.md).
Neither argument assumes an intermediate Wilson density. The next proposed
coercivity supplier is identified in [the proof tree](../PROOF_TREE.md).

This was a targeted source check, not an exhaustive search of all branches.
Historical #10133 remains architectural provenance; its draft status does
not import a result into main. No absence or novelty claim is inferred.

## Primary literature checked

[David R. Brillinger, The Calculation of Cumulants via Conditioning (1969)](https://www.ism.ac.jp/editsec/aism/pdf/021_1_0215.pdf),
pp. 215-216, equation (4) and its proof, gives the general partition formula
for cumulants under conditioning. Its moment hypothesis holds here because
all four variables are bounded at fixed finite parameters. The formula is
an exact identity; it supplies no spatial decay or mass-gap estimate.

Luna identified this primary source. The proof worker opened it but received
no readable text. The supervisor subsequently downloaded the PDF, extracted
the embedded page images, and visually read the theorem and proof on both
pages. This resolves the extraction limitation without changing the frozen
worker proof, whose generating-function derivation is self-contained. The
fresh checker uses a separate moment-partition regrouping and a finite
counterexample to an incomplete conditioning formula. These are independent
derivations in separate contexts of the same provider, not a formal audit.

[Jaffe and Witten, Quantum Yang-Mills Theory](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf),
section 4, defines the target as a nontrivial theory on R^4 for a compact
simple group, with the required axiomatic properties and a positive physical
spectral gap. The mass is also required to be finite. The present SU(2)
finite-depth posterior estimate establishes none of those continuum steps.
Luna checked the official problem in the Clay volume; the supervisor checked
the individual official PDF's statement and spectral definition.

[Clay's current problem page](https://www.claymath.org/millennium/yang-mills-the-maths-gap/)
lists the problem as unsolved as checked on 2026-11-09. That status supplies
context, not evidence for or against this particular proposed route.

No external theorem was used as an automatic clustering result. No evidence
here justifies saying the mass gap is near, assigning a success probability,
or treating additional proof files as a measure of physical progress.
