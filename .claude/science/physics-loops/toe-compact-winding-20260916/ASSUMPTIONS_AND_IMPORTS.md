# Premises and imports

The minimal framework axioms do not supply the Hamiltonian, its physical
coupling, a thermal state, a choice of source, or a continuum scaling law.
Every model here is explicitly supplied. The approved kinetic-isotropy
primitive is not used to assert a phase or a source identification.

| Unit | Load-bearing premises | Status |
|---|---|---|
| Sparse loops | Z4 oriented cubical complex; iid block activation and marks;24 independent sign sequences; randomized origin | Explicit construction, fully stated in this packet |
| Cover and source identities | Finite compact rotor graph; normalized Haar; standard real Brownian bridges; full thermal trace | Supplied model and standard probability/operator machinery |
| Exponential score bound | Positive cosine coefficients; positive diagonal kinetic heat operator in integer electric basis; bounded real time source | Explicit finite-volume proof; no earlier campaign theorem imported |
| Static shift limit | h=Cu, static; bounded l2 norm; vanishing l3 cube; deterministic L2 contact concentration | Conditional theorem with quantitative bound |
| Ergodic application | A supplied stationary spatially ergodic finite-beta Gibbs path state with the stated local loop specification | Explicit state premise; existence/uniqueness/selection not established here |

The contact average uses the mean ergodic theorem for amenable spatial
translations and bounded rectangular-step approximation. The Gaussian limit
uses a deterministic Taylor estimate, Cauchy-Schwarz, and MGF convergence.
The sparse-loop limit uses the elementary iid central limit theorem and a
uniform conditional characteristic-function expansion, not a general
mixing theorem for the correlated sign field.

Feynman-Kac, compact covering kernels, positive-character domination and
Ward/change-of-variable identities are known machinery. Their concrete
normalizations and hypotheses are derived here; no novelty of these tools
is claimed. There are no fitted empirical values or experimental claims.

Context only: PR8165 headc228dbcfc0a6b71639316915f460c32dbf479723 and PR8166
head02bfa4eb99fce8329619a476775299567f735d4b. Their whole-path rarity,
integer-filling and comparison-law estimates are not needed to prove this
packet's three units. The full compact-to-comparison bridge is still open.

The full finite-temperature trace has not been replaced by a physical
Gauss-projected trace. The state distinction is material. The ground-sector
identification from earlier work is not silently used at finite beta.
