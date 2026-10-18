# Step 2: load-bearing assumptions, and step 3: the reduction

Sources: `step0/PRIOR_ART.md` and the notes it cites (path:line there).

| ID | Kind | Assumption (plain) | Where the wall uses it | What if wrong? | Already tested? | Cheapest test | Owner decision? |
|---|---|---|---|---|---|---|---|
| A1 | axiom | Sites are Z³ points with proper cubic rotations and translations | All doubling counts (corners {0,π}³) | Another lattice changes the node count but not the balance (BCC Weyl walk also balanced) | yes (BCC: balanced) | — | no |
| A2 | axiom + reading | One site = M₂(C); no larger per-site algebra | No-per-site-γ5; 8 = 2³ corners; matter-count prices | M₄(C) or blocks of qubits provide room for γ5 and the 16 per generation (parked #4) | partly (T2 tension: the Euclidean count) | Check whether a 3+1 continuous-time Hamiltonian on M₂(C) blocks has a γ5 that commutes with the velocities and anticommutes with the mass (K2a says yes) | **yes (#4)** |
| A3 | supplied | The dynamics is a Hermitian Hamiltonian, or a finite-range unitary tick | Nielsen–Ninomiya; LATTICE_HANDEDNESS T1/T2 | Non-Hermitian/record-driven, quasi-local or infinite-range dynamics escape the theorem's premises | partly (tails tick has pathologies) | Classify one-handed dynamics by which pathology each escape pays | yes (range question) |
| A4 | supplied | Locality: finite range | T1/T2; ultralocal Ginsparg–Wilson excluded | Exponentially local (overlap) evades; does it violate "nearest-neighbour admissibility"? | partly | Can an exponentially local operator arise as an effective law from nearest-neighbour admissibility plus a gap (e.g. integrating out a gapped bulk)? | yes (range) |
| A5 | supplied | Free (one-body) carrier | All doubling theorems | Interactions: SMG gaps mirrors without bilinears (the 16) | atomic limit only (fails: 8 doublers) | Finite-coupling SMG on the smallest Z³ cluster that carries a 16 | no |
| A6 | supplied | Translation invariance (no extra coordinate, no defects) | Domain walls vector-like; no fifth dimension | An extra coordinate (layers / record-time / internal) gives inflow; mirrors on the far wall | 3D walls and record-time tried (partner); 5D not | Layered qubit slab Z³ × {1..L} with a mass wall and far-wall SMG | yes (extra structure) |
| A7 | supplied | Fermion statistics via Jordan–Wigner/Grassmann on qubits | All fermion work | Emergent fermions bound to an emergent Z₂ gauge field (3D bosonization) change which symmetries are on-site | no | Check whether the 3D bosonization map turns the non-onsite chiral symmetry into an on-site one | no |
| A8 | supplied | Gauge fields are link variables acting on-site on matter | Chiral gauging needs a chiral projector | Non-onsite (Lüscher measure / GW) gauge actions; the gauge field emerges from qubit constraints (ice/ring lane) | Lüscher abelian (literature) | Lüscher's measure conditions on Z³ with continuous time | no |
| A9 | supplied | Continuous time vs hypercubic ticks | Selector exists only in continuous time; reflection positivity needs ticks (T5) | — | K2a / set B | — | yes (set B vs C) |
| A10 | reading | "Chirality" means net Weyl imbalance of light species carrying the SM gauge charges | The target | If observation only needs low-energy chiral couplings with heavy mirrors, the target is SMG-type gapping, not lattice chirality | — | F6 (misframing) | — |
| A11 | supplied | SM content: 16 Weyl per generation, 3 generations; hw=1 → generations | Count | The 16 and the Z₁₆ anomaly are what SMG needs; the hw=1 readings conflict (T4) | no | Count the anomaly on the hw=1 / hw=2 split | no |
| A12 | supplied (hidden) | The low-energy effective theory must be Lorentz invariant with one cone (C5) | Strain/Lorentz results | Chiral constructions that break the cone at grid scale feed back into C5's prices | no | Check every surviving route against F1/F6/NF-1 | — |

**Not load-bearing** (the wall survives without them): the specific cubic vs BCC geometry (A1); the K/CPT readout structure; the Koide/generation-sector meaning of "chirality" (Tension T1).

## Route clusters

| Route | Assumptions challenged | Why it might open the wall | Expected artifact | Risk | First test |
|---|---|---|---|---|---|
| SMG | A5, A10, A11 | Interactions can gap mirrors without bilinears for anomaly-free counts (16) | A finite-coupling phase with gapped mirrors and gapless 16 | Symmetric-phase doublers (Golterman–Shamir); fine-tuning | A small-cluster exact-diagonalization or tensor-network check of a gapped mirror with a gapless light 16 |
| Exact lattice chiral symmetry (GW / non-onsite) | A4, A8 | Modified or non-onsite symmetry evades Nielsen–Ninomiya's on-site premise | A gauge-invariant chiral projection | Non-abelian measure existence; range vs admissibility | Lüscher measure / non-onsite U(1) on Z³ in continuous time |
| QCA / tick with index | A3, A4 | Index theory classifies one-handed unitaries | A one-handed QCA without pathologies, or a theorem | T1/T2 already: finite range has zero winding | The interacting / gauge-coupled tick index |
| Extra coordinate / inflow | A6, A2 | Anomaly inflow localizes one hand per boundary | A slab with a chiral surface and a gapped far surface | Needs 5D bulk or layers; far-wall decoupling | A layered slab with SMG on the far wall |
| Records / non-Hermitian | A3, (Record) | Formation breaks T and hermiticity | A record process with a one-handed physical spectrum | Records register texture only; probabilities | Non-Hermitian single-Weyl band with record readout |
| Misframing | A10, A2, A9 | The target may be a low-energy chiral EFT or net imbalance, not lattice chirality | The cheaper question | — | — |

## Step 3: first-principles reduction

1. **Less wrong requirement.** Observation needs: light fermions with SM chiral couplings; no light mirrors (bounds: Z width, direct searches; mirror masses ≳ TeV); anomaly-free gauge dynamics. It does not need exact lattice chiral symmetry at the grid scale. The requirement is "a gapped mirror sector at ≥ TeV, with the light sector chiral".
2. **Delete.** The gravity/strain links (A12) and the Koide sense of chirality are not needed for the wall itself.
3. **Shrink.** The smallest object that still bites is one Weyl doublet with U(1) charge on Z³: the 3-4-5-0-type analogue in 3+1D needs the 16. The smallest test that bites is a free one-body Z³ carrier, which is balanced (proved). The smallest open question is: does an interacting Z³ cluster gap 16 mirrors while keeping 16 light ones?
4. **Split.** Two walls: (W-a) remove or gap the mirror species (a spectrum problem); (W-b) gauge the light chiral species exactly or with bounded violation (a gauge-invariance problem). SMG addresses W-a; Ginsparg–Wilson/Lüscher addresses W-b; inflow addresses both if the far wall is gapped.
5. **Price.** If neither can be derived, the exact missing input is: the dynamics' range (A3/A4), interactions (A5), extra structure (A6), or site-algebra size (A2). Each is an owner decision.
6. **Speed up the loop.** Small-cluster exact diagonalization and free-fermion slab spectra are cheap; reuse the C5 runners and K2a.
