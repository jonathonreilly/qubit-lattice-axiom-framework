No files were written and nothing was run; this is hand derivation against origin/main `0485dc0738`. **EXACT** means a proof is given here or in a cited landed note. **ARGUED** means reasoning I have not verified.

## Verdicts
- **EXACT:** "set by the part within r steps" is equivalent to every Hamiltonian term having support diameter ≤ r. The clause2 claim checks.
- **EXACT:** in doubled coordinates the four links of U_p are pairwise at distance 2, so r = 2 is the smallest reach that admits it. They also sit inside one site's neighbourhood. A stricter wording, W★ ("each part of the change is confined to one site and its nearest neighbours"), admits U_p too and keeps the axiom's nearest-neighbour vocabulary.
- **EXACT:** no star-based wording and no diameter-2 wording admits SU(N) composite links, because such sets hold at most 7 sites. The landed composite-site bonds (diameter 5), odd paths (7) and BKSF hopping (4) are not admitted either. The diameter-2 escape rescues the ring, the Gauss hop, the soft Gauss energy and the star term, not the fermion or SU(N) items.
- **EXACT:** composition and Born are unaffected, because none of their proofs cites the generator.
- **EXACT:** Heisenberg uniqueness is lost. New covariant terms include next-neighbour exchange (two orbits), a handed, time-reversal-odd octant chirality, and four- to seven-site terms. U_p is not possibility-covariant at any r, so the ring also needs full soldering.

## 1. Which wordings admit U_p

**Notation.** d is the graph (L1) distance on Z³, or on tori with every side ≥ 5. B_r[x] = {y : d(x,y) ≤ r}, and N[x] = B_1[x] is a site plus its six neighbours. h_A is the Pauli-basis component of H supported exactly on A, and L_x(ρ) = Tr_{W∖x}(−i[H,ρ]).

**1.1 Generalised clique lemma (EXACT).** Take A-diff_r to mean "dρ_x/dτ depends on ρ through ρ_{B_r[x]}" for every x. Then A-diff_r holds if and only if every nonzero h_A has diam(A) ≤ r, measured in the ambient lattice (paths may leave A).
- **(⇐)** Terms not containing x vanish under the partial trace over A, by cyclicity. The remaining terms give L_x = Σ_{A∋x} Tr_{A∖x}[h_A, ρ_A], with every such A inside B_r[x].
- **(⇒)** The B4 construction transfers unchanged. Suppose x, z ∈ A with d(x,z) > r.
  - Pick a Pauli string S in h_A, and set M = Σ_a c(σ^a⊗S_rest) σ^a.
  - Set T = T_x⊗S_rest, with [M,T_x] ≠ 0.
  - T is nontrivial at z, so its B_r[x]-marginal vanishes, yet L_x(T) = 2^{|W|−1}[M,T_x] ≠ 0.
  - So (1±εT)/2^{|W|} share ρ_{B_r[x]} but differ in dρ_x/dτ.

At r = 1 this gives cliques, which have at most two sites on a triangle-free lattice.

**1.2 The ring in doubled coordinates (EXACT).** Roles follow the number of odd coordinates. Nearest neighbours differ by one role, so link sites are never adjacent.
- Take the plaquette site p = (1,1,0). Its four links are p±e_x and p±e_y: (1,0,0), (1,2,0), (0,1,0), (2,1,0).
- All six pairwise distances are 2:
  - adjacent sides connect through their shared vertex or through p;
  - opposite sides connect through p by the one geodesic.
- So the diameter is 2 and the smallest admitting reach is r = 2. The support is the in-plane part of the open star of p; p itself is not in it.

**1.3 Star wording W★ (EXACT).** Suppose the change is a sum Σ_y L_y, each L_y confined to N[y] and preserving total weight (Tr∘L_y = 0).
- Then L_x = Σ_{y∈N[x]} F_{x,y}(ρ_{N[y]}).
- That decomposition holds if and only if every h_A lies inside some N[y].
- For (⇒), use the same T. T is nontrivial on all of A, and A fits in no N[y], so every N[y]-marginal of T vanishes.

**Comparison of the wordings (EXACT, by a parity case analysis).** Z³ is bipartite, so two sites of opposite parity within distance 2 are adjacent.
- Every pair and every triple of diameter ≤ 2 lies in some N[y], so W★ and the diameter-2 wording agree on up to three sites.
- The diameter-2 sets that lie in no star are exactly two shapes:
  - unit squares {x, x+e_a, x+e_b, x+e_a+e_b};
  - alternate-corner tetrahedra {x, x+e_a+e_b, x+e_a+e_c, x+e_b+e_c}, with any signs.
- A diameter-2 set has at most 7 sites, and a full closed star reaches 7.
- Hence: clause wording (r = 1) ⊊ W★ ⊊ diameter-2 wording.

**1.4 Plaquette-based neighbourhoods.** "The neighbourhood of a plaquette" is N[p] for a plaquette-role site.
- Roles are not invariant under unit translations: e_x maps a vertex to a link. A role-dependent wording therefore breaks the translation covariance that the Lattice axiom and sentence 2 require (EXACT).
- Made uniform over all sites, it becomes W★.
- A covariant H then carries the four-neighbour term at every site. Gauss compression keeps the ones around plaquette-role sites, with roles supplied by the Gauss-law choice and record patterns as in the landed photon notes (ARGUED).

**1.5 Smallest admitting reach for each cost item (EXACT from the landed coordinates)**

| Term | Diameter | In one star? | Smallest admitting wording |
|---|---|---|---|
| Nearest-neighbour bond | 1 | yes | r = 1 |
| U_p (four links of p) | 2 | yes, open star of p | W★ |
| Vertex–link–vertex hop | 2 | yes, N[l] | W★ |
| Soft Gauss energy U(div E_v)² (six links of v) | 2 | yes, open star of v | W★ |
| Weight-5/7 star term (#9112) | 2 | yes, N[y] | W★ |
| BKSF hop, landed encoding: A_ijB_j contains links i−e_x and i+3e_x | 4 | no | r ≥ 4, for every edge ordering, since the last edge's string is nonempty |
| Composite-site bond Jτ^λτ^λ(σ·σ), σ at 2p, τ at 2p+(1,1,1): sites (0,0,0) to (3,1,1) | 5 | no | r ≥ 5 |
| Odd path κ through 0 with ends at 2p±2e_x | 7 | no | r ≥ 7 |
| SU(N) plaquette, k ≥ 2 qubits per link (≥ 8 sites) | ≥ 3 under any placement | no | r ≥ 3; r = 2k for the along-axis placement on a spacing-(k+1) lattice (SU(2): 4, SU(3): 6) |

Notes on the SU(N) row:
- For the SU(2) encoding as a flag qubit times a colour qubit, every Pauli string of the plaquette operator is nontrivial on all 8 qubits, because the flag factors are σ^± (EXACT).
- A rotation-covariant link encoding must use sites fixed by the link's 90° stabiliser, which lie on its own axis. That forces the along-axis placement (ARGUED: assumes each link owns its sites exclusively).

**Correction to DECISION_POINT §4.** Its "hops" are Gauss hops, not BKSF. The fermion lane and SU(N) links stay effective-only under either the diameter-2 wording or W★.

## 2. What the wider wording changes

**Composition: unaffected (EXACT).** Steps A1–A6 use:
- complex-linear embeddings;
- the lock reading;
- local formation (Kraus operators in A_y);
- a faithful prior, Reach, spanning, and generation.

None cites H. Compression also stays within the wording: P_R h_A P_R acts on A∖R, so its diameter does not grow.

**Born: the proof chain is unaffected (EXACT); one input is ARGUED.**
- Lemma U1 and Theorems 1 and 1′ cite no generator. Their adjacency conditions refer to the formation neighbourhood, which the generator wording does not change.
- Equal-time C4 holds at every r. A non-selective cut at z leaves ρ_{W∖z} unchanged, by cyclicity.
- Under a range-r generator, ad_H^n(O_x) is supported in B_{nr}[x]. A cut at distance d therefore reaches x's odds first at order τ^⌈d/r⌉. Sentence 4's "except through the change between records" covers this at every r.
- The r-sensitive input is preparability of every ψ_r (D4) when preparation runs through H. Isolating a pair then needs records on B_2 rather than N (ARGUED to survive).

**e^{−iHτ}: unaffected (EXACT).** B1–B3 use no supports. The CP note on main says "unitarity alone gives neither a fixed Hamiltonian nor its spatial support".

**The generator class:**
- **Possibility covariance (EXACT, Schur–Weyl).**
  - Each h_A lies in the span of site permutations of A, so one-site fields vanish at every r.
  - On four qubits the invariant space has dimension 14 = 1 + 6 (σ_a·σ_b) + 4 chiralities (σ_a·(σ_b×σ_c)) + 3 pairing products ((σ_a·σ_b)(σ_c·σ_d)).
- **New covariant couplings under W★ (EXACT):**
  - next-neighbour exchange on two separate orbits: straight (x, x+2e_a) and diagonal (x, x+e_a+e_b);
  - the octant chirality K_χ Σ_y Σ_s s₁s₂s₃ σ_{y+s₁e₁}·(σ_{y+s₂e₂}×σ_{y+s₃e₃}):
    - it is covariant under translations and proper rotations, since det is preserved;
    - each triple has a single common neighbour, so no terms cancel;
    - every other diameter-2 triple shape has a proper rotation that swaps two of its sites, which kills the chirality there;
  - at least one fully symmetric four-site coupling per star-contained orbit, and further terms up to seven sites.
- **Heisenberg uniqueness is lost.** There are at least four real couplings plus the multi-site ones; their ratios to |J1| must be supplied.
- **Sign conventions under Θ (EXACT).** The Θ relabelling H ↦ −ΘHΘ⁻¹ flips even-weight couplings and keeps odd-weight ones.
  - sign J1 stays a convention;
  - sign K_χ becomes a readable handedness bit, tied to the lattice's proper rotations;
  - this term's relevance to the chirality lane is ARGUED.
- **U_p is excluded by possibility covariance at any r (EXACT).** An invariant operator acts as one scalar on the multiplicity-one S=2 block. U_p+U_p† annihilates |2,2⟩ but sends |2,0⟩ to (|↑↓↑↓⟩+|↓↑↓↑⟩)/√6 ≠ 0. The photon ring therefore needs W★ together with full soldering (D5).
  - Under full soldering the plaquette's four links carry one real ring coupling (landed).
  - The landed star-term note counts 325 odd-weight orbit sums on one star, so that class is far larger.
- **The landed two-site freeze theorem no longer applies.** Both the direct ring and the soft-Gauss route (g = 5h⁴/(32U³)) become admissible as microscopic terms.

## 3. Axiom versus clause

The axiom on main says: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." It continues: "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."

Reading note 2 says the distribution concerns "which possibility a forming record locks, conditional on formation at that site". The memo also says "Admissibility is not a dynamics axiom", and that it "does not choose a Hamiltonian or transfer operator".

- **No conflict with the text (EXACT).** The axiom constrains the formation distribution. The A-diff sentence constrains the generator, and the axiom says it does not choose one. A-diff_1 was already a supplied premise borrowing the nearest-neighbour vocabulary.
- **Under the reading R_pm** (the law reads the neighbourhood's joint possibility), F(ρ_x) is a function of ρ_{N[x]} for any H. So "determined by" and "one fixed" hold at every r (EXACT).
- **Where r does bite (EXACT):**
  - the static reading R_st: at r ≥ 2 a site with six recorded neighbours still couples to unrecorded sites at distance 2. R_st already fails at r = 1, so this changes nothing about its retirement.
  - the 9041 vector-sum fingerprint widens: records in B_2[x] act as fields, and two recorded octant partners give σ_x·(q_b×q_c).

## 4. Recommendation

**For the photon ring, Gauss hops, the soft Gauss energy and the star terms, use W★:**

> "…and at each moment the change is a sum of changes, each confined to one site and its nearest neighbours and set by the part held there."

**For composite gauge links as well, use a finite reach.** By the 7-site cap, no star or diameter-2 wording can admit them.

> "…and at each moment the change in a site's part is set by the part held by the sites within a fixed number of steps of it."

The reach needed is ≥ 4 for along-axis SU(2), ≥ 6 for SU(3), and 7 to cover the landed composite-site network together with BKSF.

**Kept under either wording (EXACT):**
- tensor composition;
- Lemma U1 and Theorems 1 and 1′ (preparability ARGUED);
- e^{−iHτ};
- no one-site field under possibility covariance;
- closure under compression;
- equal-time C4.

**Lost:**
- the two-site form and Heisenberg uniqueness: the new couplings become supplied, and their number grows with r;
- the J ↔ −J convention now covers even-weight couplings alone;
- under finite reach, the reach r is a new supplied integer.

U_p still needs full soldering, the Gauss law and the role pattern, all supplied.

**Cheapest follow-up (spec, not run):**
- enumerate all subsets of B_2[0] (25 sites) to confirm the 7-site cap and the square/tetrahedron list;
- check, with 16-dimensional exact algebra, the 14-dimensional invariant space and U_p's non-invariance;
- compute the Pauli-support diameters of the BKSF hop and the composite bond.