# C5 R7-3 report: exact additive momentum with scattering on ⊗M₂(C)

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 15:07Z to about 15:45Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R7-3/`. Scripts and outputs are in `S/scripts/`:
- `r73_kitaev_box_tmatrix.{py,out}`
- `r73_pauli_strings.{py,out}`
- `r73_vison_scatter.{py,out}`
- `r73_hardcore_fiber.{py,out}`

All runs take under 1 minute with OMP_NUM_THREADS=2.
**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (cited as AX); `TESTS.md` C5 method (2302–2319), Round 6 R6-1 (3031–3070), Round 7 and the Rounds 5–6 referee results (3240–3371); lane RG (1020–1092); `agents/C5_R6-1_report.md` in full; `agents/C5_R6-1_referee_verdict.md` in full (`agents/C5_R6-1_referee.md` does not exist in the packet; only the verdict file does); `agents/RG_G1G2_referee.md` items 1–7; lane RC C2 Kitaev lines (`TESTS:1196-1203`).
**Labels.** proved / checked (numerics here) / suggested / reading / comparator. "Web-verified" means the abstract was fetched and read this session. "Recalled" means from memory, not verified.

---

## 0. In plain words

- **Is there a qubit law with collisions where momentum adds up exactly?** I built one, but only for part of its states. It runs on one qubit per site, using Kitaev's honeycomb model drawn as a brick wall inside Z².
  - Its particles are emergent fermions that collide off each other, not just head-on.
  - They carry an exactly additive real momentum, using R6-1's trick (the collision rule switches off smoothly before the zone edge).
  - This holds in every state with no vortex. Those states include the ground state and every multi-particle collision state built from it.
- **The honest catch.** One spin flip creates a pair of vortices (a "vison" pair), which then never moves. A fermion passing a static vortex pair scatters off it. I prove that any static object which scatters a particle sideways makes an exactly additive momentum impossible. So in the vortex sectors the exact momentum is lost.
- **This catch is not specific to Kitaev.** Every local way of writing fermions with qubits in 2D (Chen–Xu, web-verified) carries partner excitations that the fermion sees as half a flux quantum. Fermion encodings are therefore sector-limited by construction.
- **Without fermions.** Plain hard-core bosons (one qubit per site, full Z² or Z³ symmetry) can be made to collide with exactly additive momentum in the two-particle sector.
  - The trick is to cancel the hard-core contact with a compensating interaction. A counting lemma shows this needs a bound pair in every total momentum, and a no-lift lemma shows the bound pair must be shared between momentum classes.
  - I prove the construction fibre by fibre and check it numerically on one fibre.
  - Three or more particles are not covered. I expect them to fail without extra many-body terms (argued, not shown).
- **Against the fixed readings.** Neither construction gives exact additive momentum on *all* states of ⊗M₂.
  - The Kitaev law gives it on a superselection sector.
  - The hard-core law gives it on the two-particle sector.
  - The no-go is proved only for the static-defect (flux-conserving) encodings.
  - **Worker reading: SUGGESTED, with derived parts.** If the referee accepts a superselection-sector statement, the Kitaev law meets REFUTED-class (positive) in that sector reading.

---

## 1. Hypotheses and classes (stated before titles)

- **Spin class 𝒮.** Quasi-local laws on ⊗_{Λ} M₂(C), with Λ = Z² or Z³ (or a periodic graph inside it with a finite unit cell). The Hamiltonian is a sum of interaction terms with norm Σ_{X∋0}‖Φ(X)‖F(diam X) < ∞ for a stated F.
- **Exact additive momentum (as at `TESTS:3058-3062`, RG class `RG_G1G2_referee.md` item 1).** A self-adjoint Q with e^{iQ_j} = T_j and [Q, H] = 0, acting on asymptotic states as Σ_i q_{s_i}(k_i), where each q_s is a bounded measurable lift of crystal momentum.
- **Sector qualifications.** These are named wherever they apply. "All states" means every state of ⊗M₂, including those obtained from the vacuum by any local operator.
- **Excluded and not addressed:**
  - boosts, Poincaré closure, the stress tensor and the Ward identity (R7-1 and R7-4);
  - finite temperature;
  - LRL;
  - integrable 1D chains. In d = 1, 2→2 collisions between equal-dispersion particles are kinematically forward (`R6-1_report:131-134`, counted once).

## 2. Prior art (each counted once)

- **R6-1 witness W** (CAR algebra) and its referee verdict.
  - W is sound in the graded category but outside ⊗M₂: "2D Jordan–Wigner gives long strings, and local bosonization needs gauge qubits and constraints" (`TESTS:3316-3330`; `C5_R6-1_referee_verdict.md:17,33`).
  - The worker's ⊗M₂ transfer was "suggested, flux-free sector only", and they wrote "hard-core-boson qubit versions fail" (`C5_R6-1_report.md:125-129`).
- **Prop. N.** In the rank-one separable class, the escape needs a non-quasi-analytic form factor, so tails are super-polynomial but non-exponential. Confirmed after narrowing (`C5_R6-1_referee_verdict.md:21`). It is reused here, not re-proved.
- **RG G1-B.** Nonzero rank-one contact scattering is excluded (`TESTS:1049`; `RG_G1G2_referee.md:67`). This is exactly the bare hard-core contact.
- **RG referee's loophole:** "exact leg projectors supported wholly inside a non-umklapp patch" (`RG_G1G2_referee.md` item 4, Pauli complementarity).
- **Lane RC C2.** The Kitaev honeycomb conserves its energy current only within flux sectors (`TESTS:1155,1198-1203`; `RC_C2_referee.md:9`). The sector structure used in §4 is the same phenomenon, and is counted once.
- **O3** recalls the Bravyi–Kitaev and CKR encodings and their extra qubits per site, and notes that Kitaev's honeycomb has a static flux sector (`C5_O3_report.md:115-122`).
- **Literature.**
  - Kitaev, cond-mat/0506438: spin-½ honeycomb solved by free fermions in a static Z₂ gauge field, with a gapped Abelian-anyon phase (web-verified, abstract).
  - Chen–Kapustin–Radičević, 1711.00515: exact 2D bosonization to a lattice gauge theory, an equivalence on simply connected space (web-verified, abstract).
  - Chen–Xu, 2201.05153: all locality-preserving fermion-to-Pauli maps in 2D derive from one exact bosonization whose gauge constraints "project onto the subspace of the toric code with emergent fermions" (web-verified, abstract).

---

## 3. Route A: the Kitaev-encoded witness W_K (one qubit per site)

**The law.**
- **Lattice.** The brick wall in Z²: every horizontal bond, plus vertical bonds (X,Y)–(X,Y+1) only where X+Y is even. Bond types: z = vertical; x = A(X,Y)–B(X+1,Y); y = A(X,Y)–B(X−1,Y), where A means X+Y even.
- **H = H_K + V_spin.**
  - H_K = −Σ_bonds J_α σ^α_iσ^α_j with J_x = J_y = 0.25 and J_z = 1. This is the gapped A_z phase.
  - V_spin = (λ/N) Σ_K Â_K†Â_K.
- **The pair operator.** A_K = ½ Σ_k g_K(k) a_{K−k} a_k, with R6-1's form factor g_K(k) = χ(k)χ(K−k)[f(k) − f(K−k)] (box a = 0.49π, f = sin k₁ + 0.3 sin k₂).
- **The modes.** a_k are Kitaev's Bogoliubov modes in the flux-free sector. The quasiparticle dispersion is ε(k) = 2|J_z − J_x e^{ik₁} − J_y e^{ik₂}|, with momentum measured from the band minimum (gauge u_x = u_y = −1). It is gapped: ε ∈ [1, 3] (checked).
- **Spin image.**
  - Â_K replaces every Majorana bilinear c_i c_j in A_K by the spin string along a fixed, translation-covariant path γ(i,j): S_γ(i,j) = ∏_{bonds∈γ} σ^α σ^α.
  - In the flux-free sector this string equals (phase) × i c_i u_γ c_j (Kitaev's representation, comparator).
  - Writing V_spin = Σ Â†Â keeps V_spin ≥ 0 in **every** flux sector.

**Exactness — proved (R6-1's two-line commutator, unchanged).**
- In the flux-free sector the a_k obey the CAR.
- Every nonzero summand of A_K has both legs in S = (−a,a)², so [Q, A_K] = −K̂ A_K with Q = Σ_k q̂(k) a_k†a_k.
- Hence [Q, H] = 0 on the whole flux-free sector, at every particle number and at operator level (see the R6-1 referee, item 1, `C5_R6-1_referee_verdict.md:5-9`).

**The spin realization — checked (exact GF(2) Pauli algebra on a 14×12 brick-wall patch; `r73_pauli_strings.out`).**
- (a) Two random paths with the same endpoints give strings that differ by a product of plaquette operators W_p: 200/200. So the strings are path-independent on W_p = +1.
- (b) String commutation follows the Majorana-bilinear rule ([c_ic_j, c_kc_l] = 0 iff |{i,j}∩{k,l}| is even): 3000/3000.
- (c) Every string commutes with every W_p: 300/300. So H preserves every flux sector.
- (d) A single σ^z_j flips exactly the two plaquettes that share j's z bond.
- Together with Kitaev's solution (comparator), this is the algebra isomorphism that the flux-free statement needs.

**Scattering — checked (`r73_kitaev_box_tmatrix.out`; on-shell T-matrix with L = 240, η = 0.05).**
- **Exact non-forward process at K = 0.** (π/4,0),(−π/4,0) → (0,π/4),(0,−π/4). E_in − E_out = 0 exactly, because J_x = J_y. g_in = √2, g_out = 0.3√2, and the Born product λg_out g_in = 1.80. The process is neither forward nor exchange, and Q_in = Q_out = 0.
- **Box shells.** Up to 37336 nonzero non-forward elements (K = (0.9, 0.4), E = 2.7), with umklapp count 0 and max|ΔQ| ≤ 8.9e-16.
- **Mixed shells:** 134 found at L = 120. Example: K = (−2.62, −1.57), E = 3.5, which holds box pairs plus another class. W_K has 24304 non-forward elements and 0 umklapp.
- **Analytic comparator (χ ≡ 1).** Umklapp |T|² fractions are 0.37–0.67 on the same shells, and 0.496 at K = (π, 0), E = 3. This reproduces G1 (counted once).

**Tails — checked in part, rest argued.**
- The Bogoliubov coefficients are analytic in k (gapped: f ≠ 0), so a_x is exponentially localized in the c's.
- The form factor g is C^∞ with compact support, so the kernel decays super-polynomially but not exponentially (Prop. N, counted once).
- A string's Pauli weight equals its path length: 3, 7 and 11 at displacements 2, 6 and 10 (checked).
- So the interaction norm is finite for any F that grows slower than the kernel decays. V_spin is super-polynomially quasi-local, not exponential (the tail statement is argued, as in R6-1).

**Ground state — proved, given Lieb's flux theorem (comparator, recalled; Kitaev uses it for the honeycomb).**
- V_spin ≥ 0 in every sector and V_spin|0⟩ = 0.
- So the flux-free quasiparticle vacuum stays the global ground state, and the vison sectors stay gapped.

**Prices (named, not adopted).**
- Bond-dependent couplings on a brick wall. Covariance survives only under the even-sublattice translations, with no cubic or square rotations. This conflicts with Lattice and Admissibility covariance (`AX:37-41,57-58`).
- **Comparator, not built:** the Γ-matrix square-lattice generalizations of Kitaev's model restore one-site translation covariance at 2 qubits per site. 3D Kitaev models (hyperhoneycomb) are the Z³-type analogue.
- Super-polynomial, non-exponential tails (Prop. N).
- The sector restriction of §4.

---

## 4. The honest sector count: why Route A is sector-limited

**Lemma S (static scatterers exclude additive momentum) — proved.**
- **Hypotheses.**
  - A translation-covariant sector contains a static defect D. Its position labels a flat band, and H acts on its momentum states D_p, p ∈ T^d, with p-independent dynamics.
  - D scatters a mobile particle with on-shell kernel S(k′,p′; k,p) = δ(k+p−k′−p′)[δ(k−k′) − 2πiδ(ε(k)−ε(k′)) t(k′,k)].
  - t ≠ 0 on a set M of non-forward pairs (k,k′) of positive shell×shell measure.
- **Claim.** No additive Q = q(k) + q_D(p) exists with bounded measurable lifts.
- **Proof.**
  - Conservation on the support forces q(k) + q_D(p) = q(k′) + q_D(p+Δ) for a.e. p, with Δ = k − k′. So q_D(p+Δ) − q_D(p) = c(k,k′) is independent of p.
  - Integrate over p ∈ T^d. Haar invariance and boundedness give c = 0.
  - But q_D(p+Δ) − q_D(p) ≡ Δ (mod 2π), since both terms are lifts. So Δ ≡ 0, the pair is forward, and this contradicts (k,k′) ∈ M. ∎
- **What it means.** No zone-edge structure is needed: a flat-band defect absorbs any momentum, so the lift's cut is always crossed.

**The vison pair is such a defect — checked (`r73_pauli_strings.out` (d); `r73_vison_scatter.out`).**
- One σ^z_j creates two visons on the plaquettes adjacent to j's z bond. They are static, because every term of H commutes with every W_p.
- **Single-quasiparticle T-matrix off this pair.** It is an exact rank-2 problem, with the Green function from 1200² BZ quadrature.
  - In-momentum at the zone edge (|k|_∞ = 3.135): |t(k′,k)| over every non-forward k′ on the shell is bounded below by 0.217 (E = 2.2), 0.484 (E = 2.6) and 0.358 (E = 2.9). All 100% of shell points are > 1e-3.
  - Convergence: |t| = 0.3530 at M = 600 and 0.3511 at M = 1200.
- With Lemma S, no additive Q exists in the vison-pair sector (proved plus checked). Single-site operators create these sectors from the vacuum. So Route A's exact Q holds on the vison-free superselection sector of H, not on all states of ⊗M₂.

**Every 2D fermion encoding has partner sectors — comparator plus suggested.**
- **Comparator.** Chen–Xu (web-verified) put every locality-preserving fermion-to-qubit map in 2D inside an exact bosonization with toric-code gauge constraints. The constraint-violating excitations (Z₂ charges and fluxes) have mutual statistics −1 with the encoded fermion. Remote detectability, i.e. modularity of bosonic topological order (recalled), says the same for any gapped bosonic system with an emergent fermion.
- **Flux-conserving case — proved by Lemma S, once a non-forward amplitude exists.** If H commutes with the constraints, as in exact encodings (CKR, Bravyi–Kitaev, Kitaev), the partners are static. The amplitude is checked here only for Kitaev; for CKR and Bravyi–Kitaev it is suggested.
- **Mobile-partner case — suggested only.** If the partners are made mobile, AB scattering between two mobile particles at all momenta should violate Q too. I did not show it on the lattice.
- **Reading.** Exact fermion encodings in ⊗M₂ give exact additive momentum at best on the partner-free superselection sector. Restricting the law to a sector privileges states, against "A law privileges no states" (`AX:94-95`). That is a price.

---

## 5. Route B: hard-core bosons (one qubit per site, full Z^d covariance)

**R6-1's "hard-core versions fail" (`C5_R6-1_report.md:129`) holds for the bare contact (RG G1-B, `TESTS:1049`), but not for compensated laws.**

**Lemma I (index; one-state deficit) — proved.**
- Fix the total quasi-momentum K. Let ℓ²_sym be the free-boson relative space and Ran P (P = 1 − |δ₀⟩⟨δ₀|) the hard-core space.
- J = P : ℓ²_sym → Ran P is Fredholm of index 1, with kernel span{δ₀} and onto.
- So no unitary U : ℓ²_sym → Ran P has U − J compact. A hard-core two-body law is never a compact (local) dressing of a free-boson law: one state per fibre must be removed.

**Construction H_B — proved per fibre; checked on one fibre (`r73_hardcore_fiber.out`).**
- **Channels.**
  - Use separable s-wave channels labelled by the real total momentum P, with g_P(k) = χ(k)χ(K−k) restricted to the class q̂(k) + q̂(K−k) = P. The box is a = 0.7π > π/2, so every fibre has channels.
  - Channels of one fibre have disjoint momentum supports, so they decouple exactly: the overlap is 0.0 (checked).
- **Coupling.** λ_P < 0 is tuned so that every channel binds at the same energy e_*(K) below the continuum, on a neighbourhood N of [−π,π]^d. Outside N it tapers smoothly to 0.
- **h_W.** h_W = h + Σ_P λ_P|g_P⟩⟨g_P| conserves Q exactly (it is class-diagonal). Its in-class scattering is non-forward.
- **The removed vector.**
  - Remove b_K = Σ_m w(K̂+2πm) b_{K,K̂+2πm}, where w ≥ 0 is smooth, supp w ⊂ N, and Σ_m w² = 1.
  - b_K is an exact eigenvector because the bound states are degenerate.
  - It is smooth in K and independent of the representative K̂.
  - b_K(0) < 0 strictly, because every bound state is (e_* − h)^{−1}g with g ≥ 0.
- **The hard-core law.** H_B = 𝒲 (h_W|_{b⊥}) 𝒲†, with 𝒲 = J(J†J)^{−1/2} = P(Π_{b⊥} + c ww†), w = Π_{b⊥}δ₀ and c = ((1−‖w‖²)^{−1/2} − 1)/‖w‖².
- **Scattering is unchanged.** 𝒲 − J is rank one with a localized vector, and free states decay locally. So Ω_±(H_B) = 𝒲Ω_±(h_W), and hence S(H_B) = S(h_W) (proved; the two-space wave-operator argument).
- **Locality.** H_B − PhP = P V′ P plus finite-rank-per-fibre terms built from b, w and h_W w. It is quasi-local in r, and (by smoothness in K) argued to be quasi-local in the centre of mass.
- **The single-fibre check** (L = 41, K = 2π(20,3)/41, two channels):
  - 𝒲 is an isometry onto Ran P to 7e-14;
  - |H_B δ₀| = 3e-14;
  - the spectrum equals spec(h_W) minus one e_* to 3e-13;
  - all 620 free pair states outside the channel supports (156 with a leg within 0.1 of the zone edge) give exact eigenvectors 𝒲φ_p of H_B, with residual 3e-13. So zone-edge pairs do not scatter;
  - class-mixing in the eigenspaces is 3e-14 for h_W, against **1.94** for the bare hard-core PhP (the comparator, i.e. umklapp);
  - in-class non-forward on-shell |T| is up to 66 (quadrature at M = 600);
  - the kernel of H_B − PhP falls from 0.80 to 6.9e-3 by |r|₁ ≈ 18. This is finite-size-limited and not an asymptotic rate.

**Lemma L (why the removed vector must mix classes) — proved.**
- Suppose a K-continuous family of nonzero removal vectors, each supported in one Q-class region. It cannot cross a cut, since touching both sides creates an inter-class rank-one coupling. So its class label P(K) would be a continuous lift T^d → ℝ^d of the identity, which is impossible.
- Hence the degenerate multi-channel device. The leftover bound states (one fewer than the number of binding channels per fibre) are a bound-pair species with a fibre-dependent count.

**Scope of Route B.**
- **Two-particle sector:** exact additive momentum and non-forward scattering, with full Z^d translation covariance. The construction is dimension-independent, and with cubic-symmetric χ, λ_P and w it is argued to be cubic-covariant on Z³.
- **Three or more particles: OPEN, suggested to fail without n-body counterterms.**
  - There is no operator-level Q. Hard-core Fock space has no momentum-mode factorization, which is the property that makes W exact in Fock space.
  - Zone-edge pairs are transparent on shell only. Their off-shell two-body T is nonzero (V₂ must cancel the contact) and enters three-body rescattering. This is argued, not computed.
  - The bound-pair species also needs its own lift.
- **The magnon route is this route.** The one-magnon sector over a ferromagnet is the hard-core boson space.
- **Comparator for distributing the deficit (recalled; 1D).** In 1D, hard-core bosons with S ≡ −1 carry the deficit as threshold half-shifts (½ per band edge), one in each class. In 2D the threshold terms differ, so I did not use a per-class counting argument.

---

## 6. Against the FIXED readings (`TESTS:3355-3358`)

- **REFUTED-class (positive): not met in the all-states reading.**
  - Route A (W_K) is an explicit ⊗M₂, one-qubit-per-site law with stated tails (super-polynomial, non-exponential). It has operator-exact additive momentum at every particle number and checked non-forward scattering, **on the vison-free superselection sector only**. Vison sectors are created by single-site operators, and Lemma S excludes Q there.
  - Route B gives the same on the **two-particle sector only**, with full Z^d covariance.
  - If the referee accepts a superselection-sector statement, Route A meets REFUTED-class in that sector reading.
- **DERIVED (no-go): met only for a subclass, and needs the referee.** For flux-conserving fermion encodings (static partner defects), exact additive momentum on all states is impossible. This follows from Lemma S (proved) plus a nonzero non-forward defect amplitude: checked for Kitaev, suggested for CKR and Bravyi–Kitaev. It is not a no-go for the full spin class 𝒮, because Route B's many-body question is open.
- **Worker reading: SUGGESTED, with derived parts (Lemmas S, I and L) and two sector-qualified constructions.**
- **Against the R6-1 worker's suggestion that hard-core versions fail:**
  - true for the bare contact (counted: RG G1-B);
  - false as a two-particle statement for compensated laws;
  - open beyond two particles.

**Prices, named and not adopted.**
- **Route A:** "exact momentum only in the partner-free (vison-free) superselection sector; bond-dependent brick-wall law, covariant only under a translation sublattice; super-polynomial, non-exponential tails".
- **Route B:** "exact momentum shown only for two particles; a tuned bound-pair band shared between momentum classes; many-body counterterms undetermined".

## 7. Strong-word check, and what is not established

- "Exact" means an exact operator identity (Route A, in-sector) or an exact per-fibre identity (Route B). The numerics check it to ≤ 1e-13; they do not prove it.
- "Every 2D fermion encoding" rests on Chen–Xu's classification (comparator). The mobile-partner case is suggested only.
- Not established:
  - an all-states ⊗M₂ witness;
  - three-or-more-body exactness for hard-core bosons;
  - the asymptotic decay rate of H_B's kernel. Smoothness in K is argued, and the kernel numbers are finite-size;
  - anything about boosts, SLAC energy currents, stress tensors, Ward identities, one-cone protection or a graviton (unchanged from R6-1, `C5_R6-1_report.md:185-191`).
- For the referee, check in order:
  1. Lemma S's averaging step;
  2. the two-space wave-operator step S(H_B) = S(h_W) under a rank-one localized dressing;
  3. Lemma L;
  4. that the string algebra (a)–(d) plus Kitaev's solution give the flux-free CAR representation.
