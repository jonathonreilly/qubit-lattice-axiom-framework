# Lane RI, probe I1: exact closure and the folded-continuum tower

**Provenance.** Worker: Claude Opus 5.5 (same family as the supervisor). Ran 16:22Z to about 16:45Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/I1/`

| Script | Output | What it checks |
|---|---|---|
| `i1_multiband_boost.py` | `i1_multiband_boost.out` | Generalises C3's boost condition to many bands (random 3-band analytic model) |
| `i1_sumrule_partner.py` | `i1_sumrule_partner.out` | The band sum rule (d = 2, N = 1–8); the anomaly carried by the C1 face-touching partner; the anomaly of a truncated tower |

## Reading against the FIXED lines (I1's share of lane RI)

**PASS is not met inside the axioms.** An exact construction does exist (§3a), but only on a per-site space that is infinite-dimensional and carries unbounded energy. That is a Qubit price.

**I1 supports the first half of the lane FAIL clause, for free matter.**
- Exact closure (C1 together with C3) needs a one-particle fibre per cell that is infinite-dimensional, and the Hamiltonian must be unbounded on it.
- Every truncation to finitely many bands is inexact. This holds at any locality, including SLAC-type 1/r hopping (Theorems 2 and 3).
- For interacting matter built from finite-dimensional sites as composites, it is **not proved**. Only an index obstruction is given (§2c).
- The second half of the clause (does the coarse-cell anomaly fall with L?) belongs to I3.

**Equivalences claimed by the brief, as they actually stand:**
- (A) exact closure ⇔ (B) a union of complete folded towers ⇔ (C) an exact continuous translation group belonging to an exact Poincaré representation, with the lattice translations as its integer elements up to internal phases. **PROVED** under the stated hypotheses.
- (B) ⇒ (D): infinitely many degrees of freedom per cell, with unbounded H. **PROVED.**
- **(D) ⇒ (A) is FALSE.** Counterexample: infinitely many copies of one periodic band.
- **"Continuous translations alone ⇒ (D)" is FALSE.** Shannon/SLAC sampling gives exact continuous translations with one degree of freedom per cell, but no boost (§3c).

## 1. The theorem

### 1.0 Setting

- Free matter has one-particle space 𝓗 = L²(T^d) ⊗ 𝓚 with fibre h(k), where 𝓚 = C^N or a separable space with N = ∞.
- The lattice translation T_j acts on the fibre as e^{−ik·j}.
- **Position** in cell gauge: X = i∂_k + S, where S is the intra-cell position. For a decomposable operator A, i[X,A] = −DA with DA := ∂A − i[S,A].
- **Generators:**
  - boost K_b = ½{X_b, h} + a_b, the first moment of the energy density, with a_b a translation-invariant improvement;
  - P_b = i[h, K_b], the total energy current;
  - rotations L = first moment of the momentum density.
- **Closure (C1 + C3 global sector):**
  - [h,P] = 0 (C1: the shift source is the conserved energy current);
  - i[K_b,P_c] = −βδ_bc H (C3);
  - [K_b,K_c] ∝ L_bc, and the rotations close;
  - all as exact operator identities, with derivatives taken in the distributional sense.

### 1.1 Multi-band boost: computed

**Proposition 1 (PROVED; CHECKED in `i1_multiband_boost.out`).** Work in the moving band frame |α(k)⟩, at points where the spectrum is simple. Write 𝒜_αβ = ⟨α|(i∂_k + S)|β⟩.

1. **The naive boost K₀ = ½{X,h} mixes bands.** Its interband elements are ½(E_α+E_β)𝒜_αβ, and they make the total energy current non-conserved.
   - Random 3-band model: max|[h, P_naive]| = 4.4e2.
2. **Conservation [h,P] = 0 fixes the improvement uniquely off the diagonal:**
   - a_αβ = i(E_α+E_β)(Dh)_αβ / (2(E_α−E_β)), for E_α ≠ E_β.
   - This is exactly minus the naive interband part. It is hermitian to 1.6e-15, and then |[h,P]| ≤ 7e-13.
   - So **the closing boost is band-diagonal in the moving frame:** K_b = ½{i∂_b + 𝒜_b^diag, E_α}.
   - P is band-diagonal, with P_α = ∇u_α and u_α = E_α²/2.
3. **i[K,P] is then band-diagonal identically.**
   - Off-diagonal: 1.8e-7, the finite-difference floor.
   - The diagonal equals −E_α Hess u_α, to relative error 5e-7.
4. **C3's condition becomes band-resolved:** Hess u_α = βI on every band. With central deformations of the form δ_bc(βH + γ), d ≥ 2 forces γ = 0, because Hess u = λ(u)I forces λ to be constant. **PROVED.**

**What this means for "K must have interband elements".** A closing boost can move a state between bands in only two ways:
- (i) at exact degeneracies E_α = E_β, where a_αβ is not fixed;
- (ii) through the monodromy of the moving frame around the torus: a band followed across the zone face can arrive as a different band.

**Corollary (PROVED).**
- A band that is gapped from all others everywhere is a periodic function on T^d. The single-band C3 theorem then applies to it, and it fails.
- **So band touching at the zone face is necessary.** In the energy-sorted (cell) labelling, the boost's interband transfer is concentrated on the touching set.

### 1.2 Theorem 1: closure ⇔ complete towers

**Statement.** Exact closure holds if and only if the spectrum is a disjoint union of complete folded towers:

E_{j,n}(k)² = m_j² + β|k − θ_j + 2πn|², over all n ∈ Z^d,

with these properties:
- **β is common** to every band, whether it scatters or not;
- the set {θ_j} mod 2π is cubic-invariant (for example θ = 0, or (π,π,π), or the orbit of (π,0,0));
- each tower comes with a finite multiplicity.

**Proof of ⇒, route (i): representation theory (PROVED under H-int).**
- **H-int:** the closed Lie algebra integrates to a unitary representation U of the Poincaré group. This holds by Nelson's theorem given an analytic dense domain.
- First moments give T_j K T_j⁻¹ = K − j·H and T_j L T_j⁻¹ = L − j∧P. Exact closure gives the same action for U(j) = e^{−ij·P/β}.
- So V_j := U(j)⁻¹T_j commutes with H, P, K and L, and lies in the commutant. It acts only on multiplicity spaces; diagonalize it as V_j = e^{iθ·j}.
- Each nontrivial positive-energy irreducible component has momentum spectrum R^d (the mass shell, or the cone without its tip). Its lattice momentum is k ≡ p + θ (mod 2π).
- So the fibre over each k contains the whole tower {p = k − θ + 2πn : n ∈ Z^d}, on which E = √(m² + β|p|²) is unbounded. ∎
- No band labelling and no analyticity is used.

**Proof of ⇒, route (ii): bands (PROVED under H-band).**
- **H-band:** discrete fibre spectrum; bands smooth off a null crossing set; tr h² ∈ C² (or distributional).
- Proposition 1 gives Hess u_α = βI on each band, so locally u_α = β|k − c_α|²/2 + e_α.
- Periodicity of h makes the multiset of these quadratics invariant under k → k + 2πe. Distinct quadratics are separated by the identity theorem.
- So the set of centres {c_α} is invariant under 2πZ^d. **Every orbit is complete. A sub-tower that omits some n is impossible, and so is a finite tower.** ∎

**Proof of ⇐ (PROVED, by construction).**
- In periodic gauge, X = i∂_k exactly.
- The fibre is ℓ²(Z^d), with h = diag E(k + 2πn) and Π = k + 2πn.
- Set K = ½{X,H}, P = βΠ and L = X∧Π. This is the continuum one-particle representation rewritten, so every relation holds exactly.
- The required improvement is a = 0, since 𝒜 = 0 in the plane-wave frame.

**What the tower does at the face (READING of the construction).**
- In the energy-sorted labelling, the boost carries band n across k_c = π into band n + e_c, like a "Hilbert hotel".
- This replaces SLAC's face term. For a single SLAC band:
  - Hess u = βI − 2πβ Σ_c δ(k_c − π) e_c e_cᵀ (distributional);
  - so i[K,P] = −βH + (a face-supported term).
- **The tower is SLAC completed by exactly the bands the boost needs.** Its 1/r hopping becomes nearest-neighbour coupling between cells that each have infinite internal dimension (§3a).

### 1.3 Theorem 2: the finite-N sum rule

**Statement (PROVED; CHECKED in `i1_sumrule_partner.out` (a)).** Take any finite N and any periodic fibre h(k), with tr h² periodic in the distributional sense, at any locality. SLAC is included. Then:
- Σ_α ∫_T Hess u_α dk = ∫_T Hess(tr h²/2) dk = 0;
- equivalently, **the band- and zone-averaged C3 anomaly (Hess u − βI)/β is exactly −I for every N.**

Details:
- Bosons are covered, with u_α = ω_α²/2 and tr D/2 in place of tr h²/2.
- Check: ≤ 1.2e-12 for N = 1, 2, 4, 8 in d = 2, including crossings.
- This is C3's "zone average of A is −1", carried over to N bands. Adding bands **moves** the anomaly; it never **dilutes** it.

**Consequences (PROVED, CHECKED):**
- **(a) The C1 face-touching partner.** Suppose the lower band is exactly SLAC on the zone. Then the partner's analytic branch has ∫u_B″ = −2π exactly. That is a mean anomaly of −2β, independent of how its k ≈ 0 cap is shaped.
  - Cap widths 1, 0.3, 0.1, 0.03 give −2.0000 in every case.
  - The peak defect grows like −2π/w.
  - It sits at E ≈ √(m² + 4π²β): lattice scale, not removable.
- **(b) A truncated tower** (1D, N analytic branches glued into one 2πN-periodic branch). The total anomaly is −2πNβ, located at the top, at E ≈ πN√β.
  - Checked for N = 1, 3, 9, 27.
  - This is an input for I2: **low bands can be made exact, but the total defect grows like N and sits at the truncation edge.**
- **(c) Unfolding in 1D.** An N-band model whose monodromy is a single N-cycle is spectrally one band on a lattice of spacing a/N. So in 1D, N-band truncation is the same as denser sites, and C3's single-band obstruction reappears at the new face.

### 1.4 Theorem 3: winding (one-particle index)

**Statement (PROVED, assuming P(k) is continuous; this is the reason finiteness fails).** For finite N:
- the fibre of T_1 has det = e^{−iNk}, which winds N times;
- if P(k) is continuous (true for local P; this is an added hypothesis), Π(k) = P(k)/β is continuous and periodic, so det e^{−iΠ} = e^{−i tr Π} winds 0 times;
- V = U(1)⁻¹T commutes with h and with K, so in the moving frame its phases are constant along each band (−iE∂v = 0), and det V winds 0 times;
- this contradicts T = U(1)V.

**How the escapes fit:**
- For N = ∞ the winding is undefined. The tower absorbs it with the shift n → n+1, the Hilbert hotel.
- SLAC gets around the translation part, because Π = k is discontinuous and e^{−ik} winds once. It then fails the boost, through the face delta.

### 1.5 Partner bands

**Does Theorem A force every scattering partner to be SLAC with the same β?**
- **Stronger than that (PROVED).** C3's structure constant β is universal, so **every** band must have Hess u = βI with the common β, whether it scatters or not. T00 includes all matter.
- Theorem A, before its cubic step, allows shifted centres: E² = k·Bk + 2c·k + e.
- So the face partner must be the 2π-translate of the SLAC paraboloid. That partner then needs its own partner at k = 0, and so on. **The regress is the tower.**

**Can partners be made never to scatter?**
- **Not consistently (PROVED, given a Poincaré-invariant S-matrix).** The exact boost maps band-0 states across the face into band ±1, because mass-shell orbits cover all Π.
- S commutes with K, so scattering in band 0 fixes scattering in every tower member.
- A partner that scatters while band 0 does not, or the reverse, contradicts boost covariance. The same holds with the roles swapped.
- C1's two-band construction fails on its partner itself (Theorem 2a), before any scattering enters.

**Umklapp.**
- For tower matter, Theorem A's "no umklapp" becomes "Π is exactly conserved".
- Collisions that wrap k are ordinary band-changing processes and are allowed.
- **Umklapp-free interacting matter is the same thing as interactions invariant under continuous translations** (PROVED; immediate).

## 2. Axiom cost (one qubit per site on Z³, nearest-neighbour rule)

### (a) Infinite local dimension: Qubit price

- This is **necessary but not sufficient** (PROVED).
- Towers are unbounded. A quadratic network with any number of nodes per cell, including infinitely many, but with uniformly bounded couplings and bounded degree, has ‖h(k)‖ ≤ deg·J_max. It cannot hold a tower.
- **Price:** each site's algebra must be infinite-dimensional (for example CCR/CAR over L²(cube)) and must carry **unbounded** rule terms.
- One fixed rule built from M₂(C) terms is bounded, so the Qubit axiom as written is excluded.

### (b) Denser sites: Lattice price

- **Any finite refinement fails** (PROVED). It gives finite N, and Theorems 2 and 3 hold at every N. The anomaly total grows like N and moves to E ~ πN√β (1D: 1.3c).
- Only the continuum (refinement → ∞) works. So the Lattice price is "R³ for matter", not "denser Z³".

### (c) Collective modes of an unbounded network region

**What fails:**
1. **Free (quadratic) matter from the qubits.**
   - Jordan–Wigner or any fermionisation gives at most 2L³ Majorana bands per coarse cell of L³ sites.
   - That is finite, so Theorems 2 and 3 apply.
   - A bounded rule bounds the fibre, so §2a applies too. **PROVED.**
2. **Interacting composites.**
   - The n-th tower member has energy E_n ≈ 2π|n|√β.
   - With local terms of norm ≤ ε, a state that differs from the vacuum only in a region R has energy at most ~2ε|R ∪ ∂R|.
   - So member n must spread over at least ~π|n|√β/ε sites. **ARGUED** for exact eigenstates, which are not strictly localized.
   - Exact closure then needs an exact many-body Poincaré representation on the qubit lattice.
3. **Index obstruction.**
   - **Facts used (COMPARATOR, cited from memory, not re-fetched):**
     - The GNVW index (Gross–Nesme–Vogts–Werner 2012), extended to approximately locality-preserving unitaries by Ranard–Walter–Witteveen 2022, is 1 for any evolution e^{−iaP} under a local or fast-decaying generator P.
     - The lattice shift on a qubit chain, or on Z³ with a finite transverse torus of side L, has index 2, or 2^{L²}.
   - **Consequence (PROVED from those facts):** T_1 = U(1)V forces V to carry the whole index.
     - V must then be an exact symmetry that commutes with H, P, K and L and acts like a shift.
     - At one-particle level this is impossible (Theorem 3).
   - **Many-body case: SUGGESTED impossible, not proved.**
   - The remaining way out is a P whose tails fall outside the RWW decay class (SLAC-like 1/r). That route already fails C3.

**Minimal honest price.**
- Qubit becomes "the per-site algebra is the field algebra of a unit cube, with unbounded generators".
- Z³ adjacency and a nearest-neighbour rule can be kept (§3a).
- **READING:** this is a Lattice price in substance. Space becomes continuous at the matter level, and Z³ becomes a label or readout grid.
- **Strong-word check:** the internal basis can be countable (the cube's Fourier modes). Continuous node positions are not required, but the fibre is unitarily ℓ²(Z^d) ⊗ spin.

## 3. Constructive solutions (tried)

### (a) Continuum-cube cells: exact; outside the axioms

**Construction.**
- Site x carries the Dirac (or KG) field on the unit cube centred at x.
- The rule is the continuum Dirac operator inside each cube, plus boundary-flux matching with the 6 neighbouring cubes. That is nearest-neighbour and covariant under translations and proper cubic rotations about the site.
- In cell gauge, h_I(k) = W h_P W⁻¹, with W = e^{ik·s}, is a real-analytic periodic family of **unbounded** operators. B1 does not apply, because it needs bounded eigenvalues.

**What it gives (PROVED, being the continuum theory):**
- C1: the exact tower;
- no umklapp for any continuum-translation-invariant interaction;
- C3: exact Poincaré.

**Price and caveat.**
- Price: Qubit, as in §2a.
- **Caveat (READING):** the lattice no longer regulates anything. Interacting matter then needs its own continuum UV completion, so the original UV problem comes back.

### (b) The lattice as a readout (perfect action)

- φ_x is the cube average of a continuum field (Bietenholz–Wiese / Hasenfratz–Niedermayer blocking; COMPARATOR).
- The spatially blocked lattice propagator Σ_n |Π(k+2πn)|²/(ω² + m² + |k+2πn|²) has exactly the tower of poles.
- The site field has one degree of freedom, but its dynamics are non-Markovian. A Hamiltonian realization needs one oscillator per pole, i.e. infinitely many per site.
- **This is the same price as (a), in disguise** (PROVED: count the poles).

### (c) Shannon / band-limited fields

- These give exact continuous translations with one degree of freedom per site (the sinc kernel, which is SLAC).
- But i[X, Π] = 1 − 2πδ_face, so there is no boost. This is the C3 face delta.
- **It shows that exact translations are cheap; exact boosts are what force the tower.** CHECKED against C3; argument only.

### (d) Deformed (DSR-like) boosts on finite bands

Example: Bisio–D'Ariano–Perinotti quantum cellular automata (COMPARATOR).
- Keep K as the first moment and P as the energy current, and allow i[K,P] = −(G(H,P²)δ + F(H,P²)PP).
- Per band this gives Hess u = gI + f∇u∇uᵀ. Level sets are then umbilic, so in d = 3 they are spheres (Darboux).
- Cubic covariance makes them concentric, so u is radial, and a radial periodic analytic u is constant.
- **ARGUED:** within first-moment generators this does not rescue finite bands. It is only an altered-generator (non-GR) escape.

### (e) Coarse cells, L → ∞

- This is the ordinary continuum limit. It is exact only at L = ∞. Scaling is I3's job.
- Theorem 2 predicts the band- and zone-averaged anomaly stays exactly −β for every L. Only its location moves.

## Against the supervisor expectation (I1 line)

| Expectation | Outcome |
|---|---|
| Closure ⇔ empty-lattice tower | Confirmed, with common β, complete towers (no sub-towers), and cubic-invariant centres θ. |
| ⇔ continuous translations | Holds only for translations inside an exact Poincaré representation. Translations alone are cheap (Shannon/SLAC). |
| ⇔ infinite local dimension | Holds only as ⇒. The real price is stronger: **unbounded** local energy. Infinite dimension with bounded terms fails. |
| Not foreseen | The sum rule (anomaly average exactly −β for every N, so it is moved, never diluted); the winding / GNVW index as the reason; partner decoupling is ruled out by C3's universal β and by boost covariance. |

## Labels and strong words

**PROVED (same-family, unrefereed):**
- Proposition 1 and its corollary;
- Theorem 1 (⇒ under H-int, or under H-band; ⇐ by construction);
- Theorem 2 and consequences (a)–(c);
- Theorem 3 (assuming P(k) is continuous; Theorem 2 needs no such assumption);
- the partner and umklapp statements in §1.5;
- the bounded-fibre exclusion (§2a) and the finite-refinement exclusion (§2b);
- the free-qubit exclusion (§2c-1);
- the pole count in (b).

**CHECKED:**
- `i1_multiband_boost.out`: Proposition 1 numerically;
- `i1_sumrule_partner.out`: Theorem 2 and consequences (a) and (b).

**ARGUED:**
- the composite size bound;
- the DSR umbilic argument.

**SUGGESTED:**
- the many-body index-carrying V is impossible.

**READING:**
- the tower is "a hidden continuum";
- the UV-problem caveat;
- the "Hilbert hotel" picture.

**COMPARATOR (from memory, not re-fetched):**
- GNVW 2012 and RWW 2022;
- Wigner classification and Nelson's integrability theorem;
- Bietenholz–Wiese perfect actions;
- Bisio–D'Ariano–Perinotti;
- Darboux's umbilic theorem.

**Scope of strong words.**
- "Exact" refers to operator identities.
- "Impossible" applies only to free matter with finite or bounded fibres (any locality), and to finite refinements.
- Interacting composites on qubits are **not closed**.
- Hypotheses throughout: C1's H1–H5 where Theorem A is used; C3's A1–A5, plus taking the HDA global sector to be the full Poincaré algebra.
