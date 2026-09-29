# Agent 4: is the gravity wall misframed?

**Read:** `MINIMAL_AXIOMS_2026-06-29.md` (full), `PRIMITIVE_REGISTRY_CHECK.md`, `axiom_premise_nodes.json` (skim), the brief, WALL.md, probes 11/13/14/18/20/21, the 09-24 comparator, the 05-02 CCR no-go, the 06-17 induced-G note, probe 6, the fourth panel. Checks: `agent4_checks.py` (same folder).

## Verdict

The wall's *verdict* stands: no gapless partner survives observation, and every harmonic escape closes. Misframed are: the observational content of "purity" (never priced); the option list, which leaves the axioms' own (composite) carrier without a bounded test; and the order of work, since three of the four classical tests are blind to the wall.

**Where misframing fails, honestly:**
- (a) *Weaker target.* For a conserved source `T^ij(q→0,ω) = −½ω²Q^ij`, so the ±1 tensors `√2·sym(q̂⊗e)` couple to a radiating quadrupole with direction-averaged weight **equal** to TT's (each helicity pair carries 2/5 of a spin-2 source; numerically 1.00). Partners with `c₁ ≥ c₂/2` (probe 18) radiate O(1) of the quadrupole power; the double pulsar allows 10⁻⁴. The exact-rule branch (ω ∝ q²) dies on GW170817. Purity is observational.
- (b) *RG flow.* Cannot gap the partners: gaplessness of all of `ker s(q̂)` is the exact scalar rule (zero zeroth moments), and lemma D (every ±1 tensor is a TT tensor of another direction) is algebra. Speeds flow; the count does not.
- (c) *Z⁴ covariance.* A reflection-positive Z⁴ action has a transfer matrix on the same slots; the counting returns. Only non-unitary actions escape.
- *Large S / "the CCR is a red herring".* The proofs never cite the CCR, but its content holds: E-H is exactly invariant (`X G^T = 0`) yet not a sum of squares of ker-G patterns (their TT first moments vanish), and DeWitt is only weakly invariant; a compact conjugate forces term-by-term invariant periodic functions. Probe 14: the large-S route fails at the algebra, not at O(1/S).

## Three routes

### Route 1 — Price the purity clause once
- **Family:** invariant: `P_extra/P_TT < 10⁻⁴`; obligation: a one-page lemma.
- **Premise changed:** S8 → "TT at c to 10⁻¹⁵; extra gapless radiators below 10⁻⁴; PPN to 10⁻⁵".
- **Believe:** universal coupling `h_ij T^ij`.
- **Artifact:** lemma (outlined above; check 1): static sources (`q_i T^ij = 0`) couple to ±1 tensors exactly zero; radiating quadrupoles with ratio 1. Corollary: any gapless partner with O(1) residue is excluded whatever its speed.
- **Cost:** half a day; done in outline.
- **Changes:** the panel dropped "partner–matter coupling" as moot; it is the observational form of the wall, and it frees the static sector (Route 3).

### Route 2 — The axioms' carrier is composite; its wall is probe 6, and that has a bounded test
- **Family:** mechanism: induced (Sakharov) graviton as a collective mode of the walker sea; invariant: the diffeomorphism Ward identity; obligation: the one-loop O(q²) helicity-±1 block.
- **Premise dropped:** S2/S11. One qubit per site cannot carry a slot tensor; any metric there is a many-site composite with effectively non-compact canonical pairs (CCR note N6). The 06-17 lane already has linear, partner-free spin-2, *given* a covariantly coupled metric.
- **Believe:** the lattice matter's Ward-identity breaking sits in finitely many cubic invariants. Probe 6 found the O(1) traceless block nonzero (two numbers, E_g and T_2g); by lemma D, tuning those two clears the O(1) block on TT and ±1 alike.
- **Artifact:** by probe 6's zone integral, the induced action's O(q²) block on `sym(q̂⊗e)` for the walker sea, natural coupling. PASS: zero (cost = 2 tunings + Λ). FAIL: a `|div h|²`-type term; with the loop's O(1) kinetic weight the ±1 partner is linear; count the extra tunings among the six cubic O(q²) invariants.
- **Cost:** 1–2 days. Pre-register FAIL at first order in interactions (probe 6 T10).
- **Changes:** option C gets a bounded test; the wall moves from "finite slots" (an axiom change) to "how many cutoff-scale tunings", the honest location of the composite route.

### Route 3 — Constraint sector first; it is blind to the wall
- **Family:** object: sourced Gauss laws plus the member's lapse (clause C1); invariant: PPN γ, β; obligation: the static second-order lapse response.
- **Premise changed:** the ordering under S10 (waves before statics). The wall lives only in the radiative sector.
- **Believe:** nothing new; by Route 1 static sources are blind to partners.
- **Artifact:** (i) lemma: in the broken branch the static minimiser under `s·h = ρ` is `h ∝ s^T`, i.e. `Φ(δ + x̂x̂)/r`; along a straight path only `q ⊥ n̂` contributes, so bending and Shapiro equal GR's (γ = 1). (ii) That profile is the gauge image of `2Φδ` under `ξ = (GM/2)x̂`, which shifts β by ½: perihelion equals GR **iff the lattice lapse's second-order static response gives β = ½ in the model's coordinates**. With β = 1 the advance is 0.834 × GR (check 2; PPN `(2+2γ−β_eff)/3`, β_eff = 1.5). A static second-order computation on clause C1, cheaper than A1's closure and prerequisite to it.
- **Cost:** 1 day.
- **Changes:** does not move the wave wall. If β fails, the member programme dies before any graviton question; if it passes, the only open gravity item is Route 2's block.

**Order:** Route 1 (done) → Route 2's ±1 block → Route 3's β. None needs an axiom change to run; only Route 2's outcome bears on option A versus C.
