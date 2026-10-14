# The wall: a chiral world on the grid

Exercise packet started 2026-10-14 at 13:10Z on Jon's request: "run the exercise on chirality and the grid … what new approaches or combined disparate approaches could crack this open?"

- **Supervisor:** Claude Opus 5.5.
- **Route agents:** Opus 5.5 at xhigh, the same family as the supervisor, so they are not independent.
- **Referee for test results:** codex gpt-5.6-sol at xhigh.

**Status:** revised after step 0 (`step0/PRIOR_ART.md`, 13:16Z). The blind check is pending.

## Step 1: plain version

> We want the grid to produce the matter particles we actually see. In nature those particles are *handed*: the weak force acts only on the "left-handed" versions of electrons and quarks, and left- and right-handed versions carry different charges. Every known way of putting such particles on a grid produces each handed particle together with an unwanted mirror partner of the opposite hand and the same charges. The grid naturally makes a mirror-symmetric world, and ours is not one. The usual fixes either make the mirrors heavy by breaking a protecting symmetry (that broken symmetry caused our recent strain problem), or work only for simpler forces than ours. Getting past the wall means a grid construction whose light particles are exactly the observed handed ones, with no light mirrors, and with the forces acting on them correctly. *Analogy: a mirror that always shows your reflection; we need the room without it.*

## Step 1: precise version (exact target contract)

| Field | Content |
|---|---|
| **Target statement** | A construction on the framework's Z³ qubit lattice whose light fermion content is the SM's chiral gauge representation, per generation: Q_L (3,2,1/6), u_R (3,1,2/3), d_R (3,1,−1/3), L (1,2,−1/2), e_R (1,1,−1), optional ν_R. SU(3)×SU(2)×U(1)_Y must act exactly, or emergently with violations below observational bounds. There must be no light mirror or doubler states. |
| **Quantifiers / domain** | All three generations and all three gauge factors. Non-perturbative: not only order by order. |
| **Allowed premises** | The four axioms (Lattice, Qubit, Admissibility, Record) and the approved primitives. Supplied downstream dynamics (Hamiltonian, transfer matrix, QCA/Floquet unitary, record-formation process) are allowed but must be named and counted as prices, as must any extra structure (extra dimension, layers, auxiliary fields). |
| **Forbidden weakenings** | A vector-like spectrum with light mirrors; "perturbative only" presented as closure; Euclidean-only without a reflection-positive real-time reconstruction; dropping hypercharge or weak chirality; continuum Weyl fields placed per site by fiat; non-unitary or non-normalizable probabilities on readouts. |
| **Required edge cases** | Anomaly structure: perturbative cancellation, Witten's SU(2) anomaly, and the mod-16 (Z₁₆) condition with and without ν_R. One qubit per site, or a stated coarse-graining. Compatibility with C5's strain results (masses strain-covariant or protected; F1/F5/F6/NF-1). Locality (quasi-local). |
| **Completion witness** | (i) An explicit lattice construction with its spectrum checked (no light mirrors), exact or bounded gauge invariance, and an observational-bounds check; or (ii) a proof that the wall is equivalent to a named premise (an exact price); or (iii) a checked misframing. |
| **Does not count as closure** | A 1+1D construction alone. An abelian/U(1)-only construction alone (Lüscher's exists). Numerical hints of symmetric gapping in a toy without SM content. Perturbative-order existence. Map-only output. |
| **What currently fails** | Take any free, translation-invariant, finite-range one-body carrier on M₂(C) sites, in continuous or ticking time, with no extra dimension. Its content is balanced: 4L+4R for the walker, 2L+2R per staggered field, 8+8 for the ordered tick. The tick result is LATTICE_HANDEDNESS T1/T2, on a branch: every finite-range tick has winding W3 = 0. Every escape tried so far failed in a recorded way: covariant gapping (blocks 77/82/119/139), 3D domain walls (vector-like), record-time walls (partner at the end), vortex strings (handedness local only), Spin(10) symmetric mass generation in the atomic limit (8 doublers, Golterman–Shamir), ultralocal Ginsparg–Wilson operators (excluded in hypercube range, R2-4), and record-side handedness (texture/direction only). The SM chain obtains chirality only from declared premises: P-COMP plus mirror exclusion, P-REC, P-HY, P-ABJ, B-AXIS (`ANOMALY_FORCES_TIME_THEOREM.md:105-116, :364-375`). |
| **Progress / closure / no-go** | **Progress:** any route outside the free finite-range one-body class, i.e. interactions, quasi-local or infinite-range dynamics, an extra coordinate, a site-algebra enlargement or more matter per site, with its first test run on this lattice and the price named. **Closure:** the completion witness above. **No-go:** a proof that the wall is equivalent to a named premise, extending LATTICE_HANDEDNESS beyond its class (e.g. to interacting or gauge-coupled carriers). |

## Three-column split

| What the axioms say | What we supplied | What was proved (on supplied objects) |
|---|---|---|
| Z³ sites, nearest-neighbour adjacency, translations, proper cubic rotations (AX:37-41). **Proper rotations only: parity is not a stated symmetry.** | Fermionic statistics (Grassmann/Jordan–Wigner); a time direction and its signature (continuous or ticks); a Hamiltonian/transfer/QCA (AX:114-123 says admissibility supplies none); the staggered ε, Kawamoto–Smit phases, the Wilson term; gauge fields (U(1)/SU(2)/SU(3) links); SM charges and their assignment; species count per site (16–64 modes); P-COMP, P-REC, P-HY, P-ABJ, B-AXIS | No γ5 inside one site's M₂(C) (`NO_PER_SITE_CHIRALITY…:55-65`). γ5 exists iff the total Clifford dimension is even (needs odd time count). Free finite-range carriers are balanced (doubling; LATTICE_HANDEDNESS T1/T2, branch). Only mε gaps covariantly, pairing opposite hands. Spin(10) atomic SMG restores 8 doublers. No ultralocal Ginsparg–Wilson operator in hypercube range. |
| One qubit's algebra M₂(C) per site (AX:47); Cl(3,0)-compatible | Coarse-graining a "site" into blocks of 16–90 modes; M₄(C) enlargement (parked, DEFERRED_DECISIONS #4) | The 3D continuous-time mirror selector T₁T₂T₃ = −X exists (K2a, HEAD branch). No selector exists in hypercubic Z⁴ time. |
| A fixed nearest-neighbour admissibility rule setting each site's probability distribution (AX:57-61) | That this rule implies a nearest-neighbour Hamiltonian (or bounded-range dynamics). Whether quasi-local or infinite-range dynamics is allowed is an **open owner question** | Range: hypercube-range Ginsparg–Wilson excluded. A one-handed tick needs exponential tails and has no Hamiltonian, no reflection positivity, a time doubler, and heats. |
| Records form; one per site; permanent; only records are read (AX:77-83) | The arrow, record-production dynamics, readout contexts (outside the axioms, AX:185-186) | Records consume chirality rather than source it; handed rules register only texture or direction. |

**Reading (step 1):** most of the wall sits in the middle column. "Free, finite-range, one-body, M₂(C)-per-site, Hamiltonian-or-tick" are supplied choices. What the axioms fix is Z³ with proper rotations, the one-site algebra, a nearest-neighbour rule for probabilities, and records. Chirality is absent from that list; so is a prohibition on it.
