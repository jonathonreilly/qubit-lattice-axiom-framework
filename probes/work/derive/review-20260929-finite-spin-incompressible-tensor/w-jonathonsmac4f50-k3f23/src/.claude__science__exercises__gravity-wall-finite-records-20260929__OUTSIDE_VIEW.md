# Step 5 — outside view: literature, mathematical lenses, reframes

The literature returns of the four route agents are merged into the table
below. Each source is cited as the agent or supervisor found it. Nothing here
is imported as a repo result.

## Literature: known results first

Found by the route and kill agents. The citations were checked against
primary sources by the agents; they are reference only.

| Source | What it shows | Maps to the repo? | Import risk |
| --- | --- | --- | --- |
| Gu and Wen, arXiv:0907.1203 | Qubit-lattice gravitons: the reliable model disperses as k³; a linear "N-type" candidate is declared unreliable by its authors | the order-sum table: 6, 4, 2 | none: it is used as a map of the known |
| Xu, cond-mat/0602443; Xu and Hořava, arXiv:1003.0009 | Soft (k²) gravitons from rank-2 lattice gauge theory | the exact-rule branch (probes 10, 15) | low |
| Pretko, arXiv:1604.05329; Pretko, Zhai and Radzihovsky, PRB 100, 134113 | Linear rank-2 modes on finite slots come with five or three polarisations; two polarisations only at k² or k³ | agrees with probes 18 and 20 | low |
| Hermele, Fisher and Balents, PRB 69, 064404 | The linear emergent photon of quantum spin ice from spin-½ | a vector precedent; there is no spin-2 analogue | — |
| Watanabe and Murayama, PRL 108, 251602; Hidaka, PRL 110, 091601 | Linear modes on finite spins are Goldstones; a spin-2 order parameter polarises about its own axis | excludes a Goldstone graviton on Z³ | low |
| Weinberg and Witten, PLB 96, 59 (1980); Jenkins, IJMPD 18, 2249 (2009) | Silent on a lattice; an emergent graviton is non-relativistic or lacks a stress-energy operator | the one-light-cone obligation | — |
| Marolf, PRL 114, 031104 (2015) | Local kinematics (a tensor product of sites) gives no universally coupled gravity unless the bulk dynamics is constrained | agrees that the time rule cannot be softened (probe 18) | low |
| Hojman, Kuchař and Teitelboim, Ann. Phys. 96, 88 (1976) | Closure of the hypersurface algebra forces the λ = 1 DeWitt form | block 112's β = −α; continuum only | medium: needs the Leibniz and Jacobi properties that lattice brackets lack |
| Bahr and Dittrich, CQG 26, 225011 (2009); Bahr, Dittrich and He, NJP 13, 045009 (2011) | On a fixed lattice, curved solutions lose exact diffeomorphisms; perfect actions restore them non-locally | the expectation for test A1 (Regge analogy) | medium |
| Jacobson, PRL 116, 201101 (2016); Faulkner et al., JHEP 03 (2014) 051 | Einstein's equation as an entanglement equation of state | route F4; needs a metric, boosts and a universal η | high on Z³ (η is anisotropic) |
| Gibbons, Hawking and Perry, NPB 138, 141 (1978) | The conformal-factor sign problem | T1's knife edge is its lattice face | — |
| Moore and Nelson, JHEP 09 (2001) 023; Kramer et al., PRX 11, 041050 (2021) | Gravitational Cherenkov bounds; double-pulsar radiation within 1.3 × 10⁻⁴ of GR | route F6: partners slower than ≈12 c_TT are excluded | low |
| Kapustin and Fidkowski, arXiv:1810.07756; DeMarco and Wen, arXiv:2102.13057 | Finite commuting projectors have no Hall response; rotors evade this | the analogue of "compact finite slots versus non-compact" | — |
| Rovelli, PRL 97, 151301 (2006); Bianchi, Magliaro and Perini, NPB 822, 245 (2009) | Spin foams give a graviton only for large-spin coherent states | large spin is non-compact in effect (option A) | — |

## Mathematical lenses (chosen from the wall's structure)

| Lens | Object that changes | Invariant or theorem type | Minimal toy | What would falsify it | First artifact |
| --- | --- | --- | --- | --- | --- |
| Representation theory (SO(3) and cubic helicity) | the space of first moments of allowed moves (18 = two spin-1 parts + spin 2 + spin 3) | Schur averaging: ±1 weight ≥ ¼ of the TT weight | one wavevector's 6 × 6 symbol | a move family feeding TT with no ±1 weight | done: probe 20 B, F, H2 |
| Operator algebras (the trace obstruction; Lie-algebra contraction su(2) → Heisenberg as spin S → ∞) | the local algebra: M₂(C), spin-S, or collective spins of N qubits | no exact CCR in finite dimension; contraction errors of order 1/S | one spin-S slot and its Holstein–Primakoff expansion | a finite S with an exact canonical pair (impossible by trace) | the S-dependence of probe 10's constant C_H and of the crossover wavelength below which the q⁴ law takes over |
| Homological algebra (the elasticity complex, grad → sym-curl-curl → div-Div) | the stencils G and S as a lattice complex | exactness gives the moment lemmas (probe 20 A) | the 2³ box kernel | a non-exact lattice complex with the same continuum limit | done: probe 20 A |
| Commutative algebra (divisibility of polynomial identities) | the helicity content of kinetic ranges as polynomials in the direction | UFD divisibility; irreducible quadrics | two stiffness-kernel tensors t, k | a reducible quadric where k is nonsingular (impossible) | done: probe 20 H, H2 |
| Information theory and entanglement (first law of entanglement; area law) | whether the lattice's entanglement structure defines an effective geometry | δS = δ⟨K⟩ with a local modular Hamiltonian; the area-law coefficient | a free-fermion ball on Z³ | a nonlocal modular Hamiltonian at long distances, or a missing area law | see the route agents |
| Probability and large deviations (record statistics) | record counts as a thermodynamic variable | extensivity versus area scaling | probe 19's frozen boxes | — | done for flat counts (probe 19) |

Considered and found empty for this wall, one line each:
- category theory: no universal property is at stake;
- number theory: no arithmetic constant is involved;
- logic and independence: the wall is not an independence question;
- PDE and functional analysis: only as the continuum limit of the above;
- dynamical systems: the harmonic level is linear; beyond it, see the
  strongly correlated routes.

## Reframes

| Reframe | What moves | What becomes simpler | What becomes harder | New route | First test |
| --- | --- | --- | --- | --- | --- |
| Supplied model vs axiom content | The wall is placed on the supplied tensor reading, not on the axioms | The owner's decision is honest: it is about what we supplied | We have no gravity model built from the axioms themselves | build from records or admissibility odds | see route agents |
| Local wave pattern vs collective or global structure | Gravity as an equation of state of entanglement, or as a collective variable of many sites | No lattice graviton mode is needed | A metric must still emerge to define areas and horizons | entanglement route | the entanglement first law on the lattice |
| Dynamics vs kinematics | Newtonian gravity from Admissibility's odds (the source-link lane's slowed clocks) comes first; waves come later | The static pull is already partly derived (block 53: a drift toward slowed clocks) | The drift is not an acceleration, and light bending is half the observed value (block 59) | clock-odds gravity | known: blocks 53, 59, 60 |
| Finite carrier vs limiting family | Large spin S or collective variables approach canonical pairs | The comparator is the S → ∞ limit | The limit is not uniform: exact rules give q⁴ at every finite S | the crossover-scale route | the S-dependence of C_H |
| Exact theorem vs bounded theorem | The wall is harmonic, local and in a supplied model | — | — | strongly correlated routes | see route agents |
| Obstruction vs missing input | The wall is the absence of an exact canonical pair per slot | The price is sharp | Proving "only if" beyond harmonic order | the exact price | step 3 of `ASSUMPTIONS.md` |
| Central sector vs within-sector | not applicable here | — | — | — | — |
| Representation choice vs physical observable | Which variable is stored (metric or momentum) is a representation choice; both fail alike | Storage is not the issue (probe 17) | — | none | done |
