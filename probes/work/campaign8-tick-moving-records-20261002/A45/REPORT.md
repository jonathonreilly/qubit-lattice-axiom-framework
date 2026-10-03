I'll return the full report here rather than writing `SP/c8/A45/REPORT.md`, because my harness forbids subagents from writing report files.

# A45 report: known ways to get light and electron-like matter from simple quantum units, mapped onto the grid

**Housekeeping**
- No git writes, no repo edits, no PRs. I read the repo only with `git show origin/main:` at `b6fda5ae1d` and did not fetch.
- I read three notes directly: the axiom memo, `U1_ROLE_…`, and `THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_…`. Two read-only reader agents digested the light lane and the fermion lane on main; claims taken from them carry their file paths. Every repo note cited is unaudited.
- Checks are in `SP/c8/A45/` and ran through `run.sh`: load gate below 6, free memory at least 25%, the shared `NUMLOCK`, `nice -n 10`, the four BLAS caps at 1, and a 55 s alarm.
  - I waited about 6 minutes for another lane's lock. It never went stale and was not removed.
  - `f1_statistics.py` first ran at 13.1 s and **234 MB, over the 200 MB cap**. The dense 10-qubit part caused it. That version is kept as `f1_statistics_v1_10qubit.py`. I reran at 9 qubits: 3.4 s, 81 MB, same conclusions, and parts 1–2 are identical.
  - `f2_parton_u1.py`: 8.6 s, 35 MB.
  - Final outputs are in `out_f1_final.txt` and `out_f2_final.txt`.

**Grades.** EXACT = proof or exact arithmetic. CHECKED = numerics with stated tolerance. ARGUED = reasoning without proof. COMPARATOR = literature recalled from memory, not verified, never adopted. Every rule here is a supplied toy, and nothing is adopted.

**Framework facts used (verbatim, `docs/MINIMAL_AXIOMS_2026-06-29.md`)**
- **Lattice:** "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site. No site is privileged."
- **Qubit:** "The full one-site possibility domain has algebraic presentation `M_2(C)`… No possibility is privileged."
- **Admissibility:** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations. For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
- **Record:** "Records form. When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent. Only records are readable."
- The owner's decided readings Q1, Q3, Q4 and Q7 are used as decided. The record-tick shape and the gate are unadopted options. More room per place stays parked as a named premise (standing default `M₂(C)`).

## 1. Question

Map the known constructions in which light, and electron-like matter, emerge from simple local quantum units onto the grid. For each:
- what does it cost in the framework's terms?
- which construction can give fermionic matter with one qubit per place?
- which route is most promising, and what single test would sharpen it?

## 2. Answer, graded

1. **Light fits the grid well (ARGUED overall; pieces graded where they appear).**
   - The quantum-ice / link route puts one qubit on each edge place of the 1-of-8 role pattern.
   - Its ring term is star-local and covariant under Q3 with one real coupling (repo).
   - Gauss's law can hold exactly.
   - With formation weights that respond only to charge, empty space is exactly quiet without the gate. A39's Theorem T then does not bind, because its visibility condition fails (EXACT).
   - The cubic-lattice photon itself is not established. The repo has energy-only upper bounds that are guide-dependent (unaudited).
2. **New, EXACT within a stated class, CHECKED.** Under Q3, the point charges of any such field are never fermions. This holds whenever their one-link hops are dressed by simple products of Pauli factors (any factors, provided the factor on the opposite link at the same corner is an electric-field factor). Call this lemma F.
   - A half-turn of the grid always makes the two opposite hops commute.
   - The repo's own statistics result covers bare flips in one channel and lists dressed hops as open. Lemma F closes that for this class.
3. **Fermions from one qubit per place therefore need one of two things (ARGUED, consistent with A43's lemma S):**
   - a pattern held in the state that removes those half-turns. Examples: the repo's record-carved Kitaev networks, or its Bravyi–Kitaev ordering.
   - fractionalized spin-½ half-particles (partons). Their hops are not such products, and they carry the spinor class that lemma S requires.
4. **The parton route is the only one giving matter and light together (EXACT at mean field / CHECKED).** It uses one qubit per place, no role pattern and no painted signs.
   - A covariant hop between same-sublattice places (an even number of steps apart) reduces its mean-field gauge group from SU(2) to U(1), the light-capable kind. All eight Weyl crossings stay at zero energy.
   - The price: the crossings stop sharing one speed.
5. **Verdict (ARGUED).** The parton route is most promising for "matter and light from the axioms", because it is the only route not blocked by an exact obstruction under Q3. Its gap is energetic: no rule is known, here or in physics, that makes it the calmest state. The decisive next test is one variational energy contest (section 6).

## 3. The constructions and their fit

### 3.1 How links sit on the grid (repo, unaudited)

- **Role pattern.** A role label r ∈ Z₂³ sits in each site's possibility domain. The valid patterns are the 8 translates r_s(x) = x mod 2 ⊕ s, and the rule is covariant under all 24 proper turns (`U1_ROLE_ENCODED_DOUBLED_INCIDENCE_…_2026-09-03.md`). The label is injected as capacity only. A40 counts it as an 8-valued label at every place.
- **Places:** vertex places V (0 odd coordinates), edge places E (1), face places F (2), cube places C (3).
  - Gauss's law at V involves V's six neighbours, all of them E places. It is star-local.
  - A ring around a coarse square sits inside one face place's neighbourhood. It is star-local, not next-door.
- **Next-door rules cannot move light.** "Every generator that is a sum of nearest-neighbour two-site terms and commutes with every Gauss operator also commutes with every link field" (`DYNAMICS_CLAUSE_AN_EXACT_GAUSS_LAW_FREEZES_…_2026-09-24.md`). So light needs the record-tick shape's star-local allowance.
- **Covariance under full soldering.** "An oriented link field is covariant under full soldering alone… the covariant ring has one real coupling, and the Rokhsar–Kivelson potential is covariant too." But "a dynamical vertex charge is covariant under the trivial action and the sign twist alone. No single action has both" (`DYNAMICS_CLAUSE_THE_COVARIANT_PLAQUETTE_CLAUSE_…_2026-09-24.md`).
- **The model.** The ring model is H = V·D − g·A on cubic ice sectors, with the pure ring point at V = 0 and the RK point at V = g. Ice means 3 of 6 links occupied with a staggered sign convention.
- **Photon status.**
  - Not established: "No excitation dispersion… physical photon… is established" (`ROUND_FOUR_SYNTHESIS_…_2026-09-25.md`).
  - The curvature estimate is χ ≈ 1.113 ± 0.021 (16³) and 1.114 ± 0.010 (24³) in late windows, but convergence is not established (`RING_MODEL_ON_16_CUBED_…_1_11_…_2026-09-29.md`).
  - Guide dependence is about a quarter (`RING_MODEL_ENERGY_CURVATURE_ESTIMATES_DEPEND_ON_THE_GUIDE_SCHEME_…_2026-09-26.md`).
  - An earlier L = 12 reading of ω ≈ 0.78 k² is unverified historical arithmetic and remains unresolved against the flat χ (`THE_PURE_SPIN_HALF_LINK_MODEL_…_L_12_…_2026-09-04.md`).
  - In 2D the ring is gapped and confining (`THE_SPIN_HALF_LINK_RING_IS_GAPPED_…_2026-09-03.md`).

### 3.2 Facts that hold for every link-based route

- **Exact quietness without the gate (EXACT).** Suppose the change commutes with every Gauss operator. Then each charge sector is invariant. Any star-local weight F_v ≥ 0 supported on the charged configurations of v's star annihilates every state of the charge-free sector, at all times.
  - Visibility (A39's T3) fails: a ring or RK term that is nonzero on the charge-free sector cannot be bounded by weights that vanish there. So Theorem T does not bind. This is escape (e), "light in the kernel", arising naturally.
  - Cost: no term may create charge in charge-free space. A transverse single-link term does exactly that, for example the repo's −tΣσ_x in `RING_MODEL_WITH_SINGLE_LINK_CHARGE_HOPPING_…_2026-09-25.md`. It puts virtual pairs into the vacuum at order t²/M² (ARGUED, first order), and charge weights then fire.
- **What records can lock without breaking gauge invariance (EXACT).**
  - The two electric-field (E) eigenstates of a link place.
  - Charge-definite contents.
  - A transverse link content would change the charge at both of the link's ends.
  - So Q7 fits naturally: the Gauss condition sets each link's menu to its two E eigenstates.
  - The repo compresses rings through recorded links to zero (`RING_MODEL_TWO_REGULATORS_…_2026-09-25.md`, a supplied restriction).
  - Equal-odds formation of link records next door gives ice at a vertex with probability at most 5/16, and uniform ice only by conditioning (`ICE_SUPPORT_UNDER_NEAREST_NEIGHBOUR_FORMATION_…_2026-09-22.md`). So link records need charge-gating or conditioning.
- **Charges cannot be V's own record content under Q3.** One qubit at V carries no covariant charge operator (`DYNAMICS_CLAUSE_CHARGES_ARE_GAUSS_DEFECTS_…_2026-09-24.md`).
  - A coherent records story (ARGUED) is this: weights gated by charge lock E-basis contents on the links next to a charge. Light is then registered only where matter is, and Gauss's law becomes a support condition among records, as in the repo's reading.

### 3.3 Construction by construction

**(1) Levin–Wen string-net condensation (COMPARATOR).** Sources: Levin–Wen PRB 67, 245316 (2003); RMP 77, 871 (2005).
- **What it is.** Quantum rotors on the links of the cubic lattice, with a charging term U(div E)², an electric term and a ring term cos(curl θ). Photons are fluctuations of condensed closed strings. Electrons are ends of open strings whose string operators carry a framing that makes the ends fermions.
- **Key lesson (COMPARATOR):** in local bosonic models, emergent fermions are string ends and always come with an emergent gauge field.
- **Room.** Rotors are unbounded. Truncating to spin-½ links gives one qubit per edge place. Spin-1 or larger links need more room per place. The framing needs extra designed sites: the repo's version adds one link role per coarse edge on top of the encoded fermion, so 2 qubits per coarse edge.
- **Covariance.** The ring is covariant and star-local. The framing is the problem: by lemma F, no Pauli-type framing is covariant under Q3 (EXACT within class).
- **Gauss.** Energetic in Levin–Wen. Exact in the repo's coupled form: "Every `G_v` … is a pure `Z` operator", and it commutes with the law (`THE_FERMIONS_U1_COUPLED_TO_QUANTUM_LINKS_…_2026-09-03.md`).
  - Spin-½ links at 6-link corners force a staggered background charge. The repo declares this coordination-parity tension and does not resolve it.
  - The repo shows no gapless transverse mode.
- **Records.** As in 3.2.

**(2) Quantum spin ice (Hermele–Fisher–Balents PRB 69, 064404 (2004); COMPARATOR).**
- **What it is.** Spin-½ on pyrochlore sites, which are the links of the diamond lattice. A large Ising term enforces the ice rule energetically; transverse exchange generates ring terms at third order.
- **What emerges:** a linear photon, gapped bosonic spinons (electric charges) and gapped bosonic monopoles. QMC confirms the Coulomb phase (Banerjee et al. 2008; Shannon et al. 2012). The sign of the ring term picks a 0-flux or π-flux vacuum (Lee–Onoda–Balents 2012).
- **On Z³:** the cubic analogue is the repo's ring model, with one qubit per edge place, the role pattern, a star-local covariant ring, and E-basis link records.
- **Gauss.** Energetic Gauss means virtual spinons in the vacuum, so charge weights fire. That needs the gate, or A39's slow energy-selective formation (f). In the pure ring model Gauss is exact (3.2).
- **Matter:** bosons (repo bare-flip channel, plus lemma F).
- **Theorem T.** If formation tracks the ring energy, Lemma V forces a frustration-free vacuum, which is the RK point. There the photon is quadratic: COMPARATOR, and the repo's single-mode bound in `UNIFORM_ICE_RK_PHOTON_SINGLE_MODE_BOUND_IS_QUADRATIC_…_2026-09-23.md`. Formally the RK case lies outside T's twist hypothesis (A39), but the tension is the same.

**(3) Motrunich–Senthil 3D bosonic Coulomb phases (COMPARATOR).** Sources: PRL 89, 277004 (2002); PRB 71, 125102 (2005).
- **What it is.** Bosons or rotors with a large charging energy per cluster, so the cluster constraint acts as Gauss's law and frustration generates ring exchange. Monte Carlo in (3+1)D shows a Coulomb phase.
- **What emerges:** gapped charges that are bosons and may carry a fraction of the boson number.
- **Fit:** the same as (2): one qubit per edge place, energetic Gauss, no fermions.
- The 3D RVB / cubic quantum dimer models are siblings (Moessner–Sondhi 2003; Sikora et al. 2009: a Coulomb window below the RK point).

**(4) Wen's projective (parton) constructions (COMPARATOR).** Sources: PRB 65, 165113 (2002); PRL 88, 011602 (2002); PRD 68, 065003 (2003).
- **What it is.** Each spin-½ splits into fermions, S = f†σf/2, with n_f = 1. A mean-field choice plus its projective symmetry group fixes the emergent gauge group (SU(2), U(1) or Z₂). U(1) liquids have fermionic spinons and a photon. Massless Dirac spinons can be protected by "quantum order".
- **Fit: the best of all routes.**
  - Exactly one qubit per place, all places alike, no role pattern.
  - The soldered mean-field choice is covariant and translation-invariant (A43, A44).
  - Its Gauss constraint needs no imposition: the qubit space is the projected space.
  - Site records are physical spin states, so gauge-invariant automatically.
  - Gauge group: SU(2) at mean field (A44). New here (f2): a covariant hop between same-sublattice places reduces it to U(1) (section 4).
- **Costs.**
  - Next-door pair rules give ordered magnets (A44).
  - The vacuum is full rank on stars (ARGUED), so voids are quiet only with the gate, and the edges of recorded regions stay full rank.
  - Theorem T is open for this vacuum (A39 open edge 1).

**(5) 3D Z₂ gauge theories with fermionic charges (COMPARATOR).** Sources: Levin–Wen 2003; 3D Kitaev models (Mandal–Surendran 2009; Hermanns–O'Brien–Trebst 2015: Weyl spin liquids); Bravyi–Kitaev superfast encoding (2002); Chen–Kapustin 3D bosonization (2019).

*(5a) Records carve Kitaev networks (repo).*
- One qubit per site, the covariant compass coupling, and records removing bonds so that each unrecorded site keeps one unrecorded neighbour per axis. Then "the unrecorded generator is exactly Kitaev's model on the carved graph": Majoranas in a static Z₂ field (`DYNAMICS_CLAUSE_RECORDS_CARVE_KITAEV_MODELS_AT_THE_COMPASS_POINT_…_2026-09-24.md`).
  - Zero-field carvings are cubes or face-diagonal tubes. Winding in three directions needs records touching all three axes.
  - A covariant time-reversal-odd star term gives plane Chern sums (−1,0,0) on a supplied pattern, numerically (`DYNAMICS_CLAUSE_A_COVARIANT_TIME_REVERSAL_ODD_STAR_TERM_…_2026-09-24.md`).
  - An exact charge needs two qubits per site (`COMPOSITE_SITES_GIVE_THE_CARVED_MAJORANAS_AN_EXACT_CHARGE_…_2026-09-24.md`).
  - "Kitaev's pattern is never covariant" (`DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_…_2026-09-24.md`).
  - The Weyl-pair and dangling-field results are on branch commits only, not on main.
- **New (EXACT):** in an exact carving every network site has three recorded neighbours. So "records form only next to records" protects nothing: the whole network is edge. In a flux eigenstate ⟨σᵃ⟩ = 0 at every site, so single-site states are maximally mixed and any nonzero one-site weight fires (COMPARATOR-standard Kitaev fact). Quietness then needs blind or slow energy-selective weights.
- No light: the gauge field is static Z₂.

*(5b) Encodings (repo's encoded fermion).*
- Kawamoto–Smit (KS) staggered fermions on the coarse lattice, encoded by Bravyi–Kitaev superfast on coarse edges with the order "−x < −y < −z < +x < +y < +z", plus face stabilizers.
- Exact fermion algebra, but the order is a designed pattern. Lemma F shows no covariant replacement exists in its class.

**(6) Walker–Wang (COMPARATOR; Walker–Wang 2012).**
- Commuting-projector models on a trivalent resolution of the cubic lattice with a chosen planar projection. A modular input gives a confined bulk with surface topological order. The input {1, f} gives a Z₂ gauge theory with a fermionic charge.
- **Fit:** vertex splitting needs more places than Z³ sites, and the projection direction breaks the turns. Gapped, so no light. Relevant only as another fermionic Z₂ charge.

**Classification comparator (Wang–Senthil 2016; Kravec–McGreevy–Swingle 2015).** 3D U(1) spin liquids come as E_bM_b (spin ice), E_fM_b (partons, Levin–Wen) and others. "All-fermion electrodynamics" cannot occur in a strictly 3D bosonic system. The target here is E_fM_b.

## 4. The fermion question

**Lemma F (EXACT within class; CHECKED).**
- **Setting.**
  - Full soldering (Q3), any number of qubits per place.
  - A charge at vertex place v hops along δ ∈ {±eₐ} with t_δ = O_δ ⊗ D_δ:
    - O_δ acts on link ℓ_δ only and changes its flux by one unit;
    - D_δ is any Pauli monomial on all other qubits whose factor on the opposite link ℓ₋δ is 1 or σ^axis.
  - Let C be the half-turn about an axis ε ⊥ δ through v.
  - The hop set is covariant up to phases and Gauss-parity factors B_v: C(t_δ) ∝ t₋δ B_v^c and C(t_ε) ∝ t_ε B_v^{c′}.
- **Conclusion.** The Levin–Wen junction phase for the legs (δ, −δ, ε) is +1, so the charge is not a fermion.
- **Proof.**
  1. C conjugates every qubit by ±iσ^axis, which maps each Pauli to ± itself. Swapped pairs contribute anticommutations in pairs, and fixed qubits contribute none. So every Pauli monomial A commutes with C(A). The two hop links pair up the same way.
  2. Automorphisms preserve commutation signs, so s(t₋δ, t_ε) = s(t_δ, t_ε)·(−1)^{c+c′}.
  3. c′ = 0 is forced: C fixes ℓ₋ε and preserves t_ε's field-type factor there, while B_v would flip it.
  4. Hence θ = (−1)^c · s² · (−1)^{c+c′} = +1.
- **Checks (`out_f1_final.txt`).**
  - GF(2) census of electric-field decorations at a vertex:
    - fermionic: inconsistent under the 24 turns, with or without parity switching, and already under {1, C2z} alone;
    - bosonic: consistent;
    - C3-only, and no covariance: consistent;
    - the two covariant V-qubit factor patterns (none, and the compass pattern XXYYZZ): fermionic still inconsistent.
  - Random monomials on a 5³ window: 0/3000 anticommute with their soldered C2z image. Controls: a face-diagonal half-turn gives 1541/3000, and C2z with an extra quarter phase on fixed qubits gives 1483/3000.
  - Dense 9-qubit junction test: covariant dressings give phase +1 in all 60 trials. The Bravyi–Kitaev-ordered hops give −1 and are not C2z-covariant (residual 1.000).
- **Escapes (ARGUED).**
  - (a) A pattern held in the state that removes the half-turn: carving, designed orders.
  - (b) Hops that are not such monomials: projected exchange processes of fractionalized spin-½ partons.
  - (c) Charges carrying an internal frame (an O-multiplet), with frame-dependent dressing. This needs more room.
  - (d) A covariance reading weaker than Q3, with extra local relabelings on fixed places. Note: this repo reading was not found on main as a clause.

**Partons at mean field (f2, `out_f2_final.txt`).**
- On nearest-neighbour, face-diagonal, axis-2 and body-diagonal bonds, the soldered-covariant hop space is exactly span{t·1, iλσ·d̂}: dimension 2 for each (EXACT, null space).
- **Gauge group.** [η⁺, f†ₓMf_y + h.c.] = −f†ₓ(s_y Mε + sₓ εM*)f†_yᵀ, with εM* = Mε for this family. So a bond keeps η⁺ only if s_y = −sₓ (EXACT; CHECKED on a 2-site Fock space: 0 for opposite sublattices, 2.0 for same).
  - Any nonzero covariant same-sublattice hop leaves only U(1) as the continuous gauge group (EXACT).
  - Time reversal is kept; inversion is broken, and inversion is not among the axioms' symmetries.
- **Nodes.** The pure iλ′σ·d̂ face-diagonal hop vanishes at k ∈ {0,π}³. So all eight Weyl nodes stay at E = 0 (6e-16) with unchanged hands (4 of each), and covariance holds (2.3e-15).
  - Speeds split as |vₐₐ| = |2λ + 2√2·λ′·Σ_{b≠a}(−1)^{n_b}|.
  - At λ′ = 0.3λ: the k = 0 node (Γ) moves at 3.697 and the k = (π,π,π) node at 0.303, both round; the other six nodes are two-speed. The form is EXACT and the values CHECKED.
  - There are no other zeros on a 40³ grid (minimum |E| = 0.094 away from the nodes).
  - |λ′| must stay below λ/(2√2), where the speed at k = (π,π,π) vanishes.

**So (ARGUED).**
- With one qubit per place under Q3, electron-like fermions arise only from patterns that break the turns (carving: neutral Majoranas, static Z₂, no light) or as spinor partons. Partons have charge under an emergent gauge field that can be the light kind.
- The graded route stays parked. The repo's local-tomography note excludes one fermionic mode per site but "does not exclude every graded theory" (`RECORD_READOUT_LOCALITY_READ_AS_LOCAL_TOMOGRAPHY_…_2026-09-24.md`).
- Every route is doubled: net handedness zero (Nielsen–Ninomiya, COMPARATOR).
- In the U(1) parton phase, spinons are massless (they cannot be gapped within one-site cells). A mass needs a period-2 pattern or pairing, and pairing reduces U(1) to Z₂, which loses light (ARGUED).

## 5. Costs table

| Construction | Room per place | Pattern held in the state | Frustrating / ring terms | Gauge constraint | Fermions | Chirality | Records compatibility | Known parent rule (literature) |
|---|---|---|---|---|---|---|---|---|
| Levin–Wen photons + electrons | Spin-½ link: 1 qubit per edge place (rotors unbounded); framing adds designed sites (repo form: 2 qubits per coarse edge) | 1-of-8 roles + framing order (not covariant, lemma F) | 4-link ring, star-local about face places, one covariant coupling | Energetic (LW) or exact (repo); staggered background at 6-link corners | Yes (framed string ends) | KS-doubled | E-basis links, charge-definite corners; charge-gated weights exactly quiet without pair creation | The model is its own rule; Coulomb phase rests on 3D compact U(1) (COMPARATOR) |
| Quantum spin ice (cubic = repo ring model) | 1 qubit per edge place + role label | 1-of-8 roles | Ring: perturbative (QSI) or supplied (repo) | Energetic: vacuum pairs fire charge weights. Exact in pure ring model | No (bosons) | — | Records freeze rings; gate or slow selective formation if pairs exist | Pyrochlore: QMC Coulomb phase (COMPARATOR). Cubic: not established (repo upper bounds) |
| Motrunich–Senthil | 1 qubit per edge place (truncated) | Roles / cluster structure | Generated from frustration | Energetic (charging) | No | — | As spin ice | (3+1)D Monte Carlo evidence (COMPARATOR) |
| Wen partons (soldered π-flux) | Exactly 1 qubit, all places alike | None | Needed: next-door pairs give order (A44); J₂-type or multi-spin star terms untested beyond A44 | Emergent; none imposed. SU(2) → U(1) by covariant λ′ (f2) | Yes, spin-½ spinons | 8 Weyl, 4+4; λ′ splits speeds | Site records gauge-invariant; full-rank vacuum, so gate needed; edges full rank; T open | None known for 3D π-flux (COMPARATOR) |
| Z₂ + fermions: Kitaev carving (repo) | 1 qubit | The carving, held in records | None (compass K) | Static Z₂, exact | Yes, neutral Majorana (charge needs 2 qubits) | Chern/Weyl candidates (numerics; Weyl pair branch-only) | Records are the structure; gate protects nothing (all sites edge) | Exactly solvable on carved graphs |
| Z₂ + fermions: encodings (BK superfast / Chen–Kapustin; repo) | 1 qubit per coarse edge (or face) + designed roles | Roles + direction order (not covariant) | Face stabilizers | Z₂ flatness imposed | Yes, complex | KS-doubled | Gauss and parity record-diagonal | Exact encoding; light only if coupled to links |
| Walker–Wang | Edge qubits on a split lattice: more places | Projection + resolution (breaks turns) | Commuting decorated plaquettes | Exact | Yes for {1, f}; gapped | None | Stabilizer vacuum mixed on sites, so gate needed | Exactly solvable; no light |

## 6. Verdict and decisive next test

**Verdict (ARGUED).**
- **Light:** the link field is the best fit to the grid, with exact Gauss and charge-gated records, so Theorem T does not bind. It is not established on the cubic lattice.
- **Its charges:** bosons under Q3 for every Pauli-monomial dressing in lemma F's class.
- **The only route to electron-like matter and light from one mechanism** with one qubit per place, no pattern, and the spinor type lemmas S and F demand, is the parton route.
  - It survives every exact check here: covariance, a U(1) reduction, nodes kept.
  - It fails only on unknown energetics.
  - The fallback, if it fails: light from links, with fermions only through state-held patterns or more room.

**Decisive next test: one variational energy contest.** Use A44's variational Monte Carlo (pair-flip moves) and A43/A44's spin-wave library.
- **Trial state:** the projected U(1) parton state, with the soldered nearest-neighbour λ and the covariant face-diagonal λ′ optimised over λ′/λ ∈ [0, 0.3].
- **Competitors:** the λ′ = 0 (SU(2)) state, and spin-wave-corrected ordered states.
- **Rule:** the soldered-covariant star-local family J₁, K₁ plus j·Σ_fd(2σᶜσᶜ − σ·σ), the Klein dual of J₂. Scan j over 0.2–0.4 at 6³ and 8³.
- **Success:** at some point the optimum has λ′ ≠ 0 and beats every corrected ordered state by more than three combined error bars at both sizes, with the margin not shrinking from 6³ to 8³.
- **Failure:** ordered states win or tie everywhere, or the optimum sits at λ′ = 0. An SU(2) mean field in 3D is expected to confine into order (COMPARATOR). The parton route would then need multi-spin star terms or more room. Matter from one qubit per place under Q3 would then rest on patterns only.
- **Cost:** about 40 runs of 90 s each, one numeric worker at a time.

## 7. Open edges

1. Lemma F beyond its class:
   - charges with an internal frame;
   - non-monomial hops;
   - hops dressed by closed-loop flips through the opposite link.
2. Registering a charge at a one-qubit vertex under Q3 through which covariant menu the conditions supply (for example axis states versus diagonal states), using Q7. Untested (ARGUED).
3. A spinon mass needs a pattern or pairing, and pairing loses light. Is a "Higgs-like" state-held pattern acceptable? (COMPARATOR: the electron's mass comes from symmetry breaking.)
4. Whether gauge interactions restore one common speed after λ′ (COMPARATOR: Chadha–Nielsen).
5. A spectral rather than energy-only test of the cubic photon at the pure ring point. The quadratic reading against the flat χ is unresolved on main.
6. Quietness of Kitaev carvings, given the gate gives no protection.
7. A hybrid: light from links plus partons on V places. No construction exists.
8. Coordination parity of spin-½ links with fermionic matter. Larger links would need more room.

## 8. Plain-language summary for the owner

Physics knows a few recipes in which light and electron-like particles emerge from many simple quantum units. On our grid the recipe for light fits well. The light field sits on the in-between places of the 2×2×2 pattern and moves by turning around small squares, with charge kept track of exactly. Empty space then never triggers records unless charge is present, which is the escape the hard limit needed. But I showed that, with turns glued exactly, the charges this light carries always behave as bosons, never as electrons, for every simple way of dressing their hops. The only recipe that gives electron-like particles and light together from one qubit per place, with no pattern painted on, splits each place's qubit into spin-½ half-particles tied together by an emergent field. That field can be made the light kind without breaking any turn, at the cost of the eight crossings moving at different speeds. Nobody knows a rule, here or in physics, that makes this split state the calmest one, so the next step is a direct energy contest between it and ordered magnets.