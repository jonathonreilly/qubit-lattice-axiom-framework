# Lane RG, probe G1: theorem and loopholes (Claude Opus 5.5 xhigh; same family as supervisor; not refereed)

**Reading this probe supports: FAIL (bounded), with one named open sub-route.**

- Proved, for analytic or meromorphic on-shell amplitudes: an amplitude that vanishes on the umklapp set vanishes everywhere. This covers tree-level exchange through any network with finitely many fields per site, of any finite depth, gapped or gapless.
- Proved: the same holds exactly in U for contact two-body scattering, and for any family of laws analytic in its coupling down to zero coupling.
- Proved for one class of Fermi-surface and critical mediators: exchange with positive spectral weight and analytic vertices.
- Argued: Pauli-blocking filters, broken phases, topological order, and infinite depth.
- **One supervisor premise is false as stated.** Non-analyticity on a measure-zero set *can* create an open zero set when that set has codimension 1. Thresholds, van Hove walls and Kohn surfaces are of this kind (Im χ is the standard example). The FAIL holds for those sources for other reasons (spectral positivity, particle–hole complementarity), not because the set has measure zero.
- **Open:** at a fixed, strong coupling, amplitudes with dressed (non-analytic) vertices whose codimension-1 walls lie inside the on-shell fibres, beyond the two-body-potential sector. Finite-range (non-contact) two-body potentials, nonperturbatively, are reduced but not closed.

Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRG/G1/`
- `g1_levelsets.py` / `.out`, `g1_levelsets_swap.py` / `.out`: counts of level-set components (connectivity).
- `g1_umklapp_lifts.py` / `.out`: the umklapp set on M for four lifts, d = 2, 3, TB and KG; near-forward umklapp.

## 0. Setting

Matter band ε on T^d, d = 2, 3:
- nearest-neighbour tight binding (TB), ε = −Σ cos k_i;
- or lattice KG, ω = (m² + 2Σ(1 − cos k_i))^{1/2};
- staggered = KG at (2k, 2m) on the reduced torus (RS S1).

The 2↔2 on-shell manifold is

M = {(k1,k2,k3) ∈ T^{3d} : F := ε1 + ε2 − ε3 − ε4 = 0}, with k4 = k1 + k2 − k3 and dim M = 3d − 1.

- ∇F = (v1 − v4, v2 − v4, v4 − v3). So M is singular only where v1 = v2 = v3 = v4.
- M_reg denotes the regular part.
- A **lift** is a measurable s: T^d → R^d with s(k) ≡ k mod 2π (mod π for the staggered reduced zone).
- D_s := s(k1) + s(k2) − s(k3) − s(k4) ∈ 2πZ^d on M.
- The **umklapp set** is U_s = {D_s ≠ 0}.
- Fibres: for fixed incoming (k1,k2), the outgoing set is the level set L_{K,E} = {q : Ω_K(q) = E}, where Ω_K(q) = ε(q) + ε(K − q).

## 1. The theorem

### 1(iii). The exact collision-invariant condition (proved, standard)

Let P be conserved, acting on asymptotic one-particle states by the symbol s, with a dressing that clusters (the RN L2 Møller reduction; necessary, not sufficient, per the RN L2 referee). P is then diagonal in the momentum basis, so [S, P] = 0 holds elementwise:

T(k1,k2→k3,k4) · D_s(k1,k2,k3,k4) = 0 for each component of D_s, at every on-shell configuration (a.e. as a kernel on M).

- D_s ∈ 2πZ^d. So this is exactly: **T = 0 a.e. on U_s.** No amplitude-weighted average enters.
- An umklapp with D = +2π cancelling one with D = −2π is not allowed:
  - exact conservation must hold for every initial state, including single momentum wave packets;
  - the growth of the variance of P is Σ|T|²|D|², which is zero only if T = 0 on U.
- **Kinetic level.** The linearized Boltzmann null-space condition is the same: ∫ W |D|² n1 n2 (1 ± n3)(1 ± n4) δδ = 0, with W = |T|². At T > 0 the occupation factors are positive, so W = 0 a.e. on U.
  - At T = 0, Pauli factors can vanish. That is the "filter" route, treated in §2.
- **Fixed-state averages are weaker and are not conservation.** An example is Σ_f |T_fi|² D_fi = 0 for one initial state. In equilibrium it holds by symmetry even with umklapp present.
- T here is the *total* amplitude: all diagrams, plus the direct and exchange terms. Cancellations between diagrams at the same configuration are allowed and are included.

### 1(ii). Every lift has an open umklapp set (proved; plus a comparator for general lifts)

**(a) No continuous lift exists.** A continuous s would lift id: T^d → T^d through R^d → T^d, which would force π_1(T^d) = Z^d to factor through π_1(R^d) = 0. So every lift jumps.

**(b) Lemma G1-L1 (proved).** Take any lift with a C¹ jump point σ, where s jumps by 2πm, m ≠ 0. Then U_s contains an open subset of M_reg, adjacent to near-forward scattering.

*Proof.*
1. Off Σ̃ = {some k_j ∈ closure of the jump set}, D_s is locally constant on M. So U_s ∖ Σ̃ is open, and it is enough to find one umklapp point off Σ̃.
2. Take k1 = σ, with k2, k3, k4 ∉ Σ, k3 near k1, and v3 ≠ v4. These are generic, near-forward points.
3. ∂F/∂k3 ≠ 0, so k1 can be moved across Σ transversally, with k2 fixed and k3, k4 adjusting slightly (implicit function theorem). They stay off Σ because Σ is closed.
4. D jumps by 2πm, so one side has D ≠ 0. ∎

This covers every fundamental-domain choice with a piecewise-C¹ boundary: shifted cubes, Wigner–Seitz cells, curved domains, and the period-π reduced zone.

**(c) Comparator for arbitrary integrable lifts** (Spohn, math-ph/0605069, as read by the RN L2 referee: a periodic integrable pair-collision invariant is aω + c; recalled, not re-read).
- If U_s were null, each s_j would equal a ω + c a.e. It would then be continuous with s_j − k_j ∈ 2πZ, hence k_j − aω = const on R^d.
- That is impossible, because ω is bounded. So U_s has positive measure for every integrable lift, and positive measure is all the identity theorem needs.

**(d) Checked** (`g1_umklapp_lifts.out`). On-shell samples, energy residual ≤ 1.2e-14:

| Lift | d = 2 (TB, KG m = 1, KG m = 0) | d = 3 (TB, KG m = 0.5) |
|---|---|---|
| standard cube | 0.40–0.42 | 0.60–0.63 |
| shifted cube | 0.40–0.42 | 0.60–0.63 |
| wiggly sinusoidal domain | 0.40–0.42 | 0.60–0.63 |
| reduced zone (period π) | 0.43–0.46 | 0.64–0.68 |

- Entries are umklapp fractions.
- In every case about 1000 of the umklapp samples have every leg more than 0.03 from the jump set. So the umklapp set has an interior.
- **Near-forward umklapp at the edge** (TB, d = 2): |k3 − k1| = 0.20, 0.05 and 0.01 each give D/2π = (1, 0) exactly on shell.
- So umklapp is not only a large-transfer phenomenon. Arbitrarily small transfers across the zone edge are umklapp.

**Lift independence.** T is physical and does not depend on the lift. If T vanished on U_s for even one lift, §1(i) below would make T ≡ 0. So no choice of fundamental domain rescues an analytic T. The umklapp label moves with the lift, but its discontinuity surface is always somewhere on M with an open umklapp side.

### 1(i). Connectivity: umklapp and normal regions lie in one component (proved for TB; checked for KG)

**Lemma G1-L2 (proved, any d).** For TB, every level set of Ω_K has at most 2 connected components. When there are 2, q ↦ K − q swaps them.

*Proof.*
1. Ω_K(q) = −Σ t_i cos p_i, with t_i = 2cos(K_i/2) and p = q − K/2. Shift p_i by π where t_i < 0; t_i = 0 is a flat circle.
2. Set u_i = t_i cos p_i. This is a homeomorphism from the cube [0,π]^d onto the box Π[−t_i, t_i].
3. L ∩ cube = {Σu_i = −E} ∩ box, which is convex and hence connected.
4. L is the union of g(L ∩ cube) over g in G = Z_2^d, the group of reflections p_i ↦ −p_i.
5. The pieces for g and g·r_i share points whenever L ∩ cube meets the wall p_i ∈ {0, π}. With T_i := Σ_{j≠i} t_j, coordinate i fails to meet its wall only if T_i − t_i < −E < t_i − T_i, which needs t_i > T_i.
6. At most one coordinate can satisfy t_i > T_i. So the touching reflections generate a subgroup H of index ≤ 2.
7. Hence there are ≤ 2 components. When there are 2, they are swapped by r_i ≡ the full inversion mod H, and the full inversion is q ↦ K − q. ∎

**Corollary (proved, TB, d ≥ 2): M_reg is connected.** Proof steps:
1. **Bad points are nowhere dense.** These are points with v3 = v4 (dimension ≤ 2d), or lying over critical values of Ω_K (finitely many per K for analytic Ω_K; dimension ≤ 3d − 2). So every point of M_reg is joined within M_reg to a point over a regular (K,E).
2. **Regular fibres lie in M_reg.** Over a regular (K,E) the whole fibre has v3 ≠ v4. By G1-L2, k3's fibre component contains k1 (the forward point) or k2 (the exchange point).
3. **The forward and exchange sets are connected.** Φ_reg = {k3 = k1, v1 ≠ v2} and X_reg are complements of codimension-d sets in T^{2d}, so they are connected for d ≥ 2.
4. **Φ and X are joined.** A one-component regular fibre (K = 0, E near the band bottom) contains both k1 and k2.

The local structure at Φ ∩ X is also good. There F ≈ −(k3 − k1)ᵀ H (k3 − k2), a bilinear form of signature (d,d). Its cone minus the vertex is connected for d ≥ 2.

**KG (checked, not proved)** (`g1_levelsets*.out`):

| Case | Fibres with 1 component | Fibres with 2 components |
|---|---|---|
| d = 2, 480 random (K,E) per mass | 261–312 | 168–219 |
| d = 3, 60 random (K,E) per mass | 47–55 | 5–13 |

- No fibre had more than 2 components.
- **In d = 2, at m = 0.2 and m = 0, 5 cases have 2 components that are each invariant under q ↦ K − q.** All have K_i ≈ ±π and E near the top.
- In those fibres the second component contains neither k1 nor k2, so the fibre path above fails there.
- Those pieces join the main component when E is lowered and the components merge. That merger passes through regular points of M, because v1 ≠ v4 there.
- So KG connectivity is **argued plus checked**, not proved.
- Unequal species (A ≠ B) have no swap symmetry. Their connectivity is argued by merging, not proved.

### Theorem G1-A (proved, same-family, unrefereed)

**Hypotheses:**
- d ∈ {2, 3}, and ε is TB (any d ≥ 2). For lattice KG or staggered, add the connectivity of M_reg (checked, §1(i)).
- On M_reg, T = A/B a.e., with A and B real-analytic and B ≢ 0. Call this class 𝒜, "meromorphic on M".
- s is a lift as in 1(ii).

**Claim.** If T = 0 a.e. on U_s, then T = 0 a.e. on M: there is no 2↔2 scattering.

**Proof.** A vanishes on U_s ∖ {B = 0}, which has positive measure. A real-analytic function on a connected analytic manifold that vanishes on a set of positive measure vanishes identically. ∎

**What lies in 𝒜 (proved):** tree-level exchange through any network with finitely many fields per site and a finite-range, translation-covariant rule, of any finite depth, gapped or gapless.
- Vertices are trigonometric polynomials, hence entire.
- Mediator propagators are entries of (ω − h(q))^{-1} = adj/det, rational in e^{iq} and in ω = ε1 − ε3. ω is analytic on M except at the massless KG cone k = 0, which has codimension d ≥ 2 in M and does not separate it.
- The cone of a gapless mediator enters only through ω_γ², which is analytic, or through polarization sums sin q_i sin q_j / Σ sin², which are ratios. Both are in 𝒜.
- A pole set B = 0 of codimension 1, where a mediator goes on shell, is harmless. The argument runs on the numerator, and A·δ(B) also vanishes.
- **Infinite depth for a quadratic network:** summing all hops is the resolvent, which stays in 𝒜.

**Matter–mediator amplitudes** (Compton, emission) are in 𝒜 at tree level on their own on-shell manifolds. The same argument applies there, but connectivity of those manifolds is argued, not proved.

### Theorem G1-B (proved): contact two-body scattering, exact in U

Number-conserving contact interaction, any species. Then T = U/(1 − U G_K(E + i0)) depends only on (K,E). It is nonzero wherever G is finite, so it is nonzero a.e.

By §1(ii), the fibres at an open set of (K,E) contain umklapp pairs. So no nonzero U is umklapp-free.

This holds at van Hove walls too, because the walls enter only through (K,E) and T has no zeros there.

### Reduction G1-B′ (finite-range V; proved reduction, not closed)

For a rank-n separable V the on-shell amplitude is T = φ(k)†τ(K,E)φ(k′), with φ trigonometric polynomials.

1. φ is analytic along a fibre component. The two TB components are swapped by q ↦ K − q.
2. So vanishing on the umklapp pairs of a fibre forces T ≡ 0 on that whole fibre.
3. That is equivalent to P_R 𝒦(K,E) P_R = 0, with:
   - 𝒦 the real K-matrix;
   - R = span of φ on the shell.
4. R is *not* all of C^n. For nearest-neighbour V, Ω_K − E is itself a relation among the monomials.
5. The condition must hold on an open set of (K,E). It is overdetermined, but **not proved impossible.**

### Corollary G1-C (proved): families analytic in the coupling

Take H(g) analytic in g down to g = 0, conserving the sawtooth for all g in an interval.
1. Then the Born (tree) term must vanish on U. By Theorem G1-A it vanishes on M.
2. Exchange through a mediator with nonzero spectral weight, for distinguishable legs, then forces g_A(k1,k3) g_B(k2,k4) ≡ 0 on open sets. So one vertex polynomial is ≡ 0.
3. Matter therefore decouples from that mediator at every order.

**Not covered:** a single fine-tuned coupling where cancellations between orders occur.

## 2. Sources of non-analyticity in the thermodynamic limit

**Key distinction.**
- **Exponentially decaying kernels** are analytic in a strip (Paley–Wiener), so they never vanish on open sets.
- **Power-law kernels** can have open zero sets. The free Fermi-sea projector θ(μ − ε(k)) has compact momentum support and |x|^{−(d+1)/2} tails, and a nearest-neighbour network generates it as a ground-state correlation.
- **So "compact momentum support needs genuinely non-local kernels" is false for emergent objects.** The real question is whether such objects can filter *every* channel. Answer below: they cannot.

| Source | Codimension in M | Can it give "zero on U, nonzero elsewhere"? | Status |
|---|---|---|---|
| Gapless mediator cone points; on-shell mediator poles | ≥ 2 (cone); poles of codim 1 sit in a denominator | **No.** Class 𝒜, numerator argument | proved (G1-A) |
| Thresholds, van Hove walls (loops; also Born iterates) | **1, can separate M** | **Not excluded by real analyticity.** Im parts vanish identically on open sets below thresholds. Closed for the contact two-body sector (G1-B), for families analytic in g (G1-C), and for spectral-positive exchange (next row) | partly proved; **open** at fixed strong coupling with dressed vertices |
| Fermi surfaces: Kohn surfaces of χ(q,ω) (Lindhard) | 1 | **No, for exchange with analytic vertices.** With spectral weight ρ(q,ω) ≥ 0 and ρ(q,·) ≢ 0 (true for every q ≠ 0 at partial filling): Im χ ≠ 0 on supp ρ; Re χ < 0 below it, > 0 above it, and strictly monotone in ω² inside gaps. So χ ≠ 0 a.e., and T = A(k)·χ(q,ω) forces A = 0 on U, so A ≡ 0 | proved (lemma G1-L3) |
| Fermi seas as Pauli filters (sharp n(p)) | 1 | **No, for exact conservation**, by particle–hole complementarity: (1) particle momenta (∉ S) and hole momenta (∈ S) cover T^d; (2) one vertex polynomial governs both by crossing; (3) the matter's own umklapp at the edge (k → k − q while creating a pair (p, p+q), with the Pauli factor independent of k) forces Γ(q) = 0 on open q-sets; (4) filtering the matter's own momenta needs a matter sea, which moves umklapp into the matter-hole channel; (5) interacting seas have n(k) ∉ {0, 1}, so the filter is inexact. **What survives:** a *kinematic* umklapp gap. Two-body umklapp is absent below the energy of the lightest edge-momentum excitation, and n-body umklapp needs n ≳ π/κ. Approximate only | argued (tree level); comparator for (5): Fermi-liquid n(k) |
| Critical points / RG fixed points (anomalous power laws) | 1 (cone and threshold branch sets) | Exchange part: no (spectral positivity, as in the Lindhard row). Dressed 4-point vertices at a fixed critical coupling: **open**. Criticality is also codimension ≥ 1 in coupling space (fine-tuned) | partly proved; open |
| Infinite depth / range → ∞ | — | Any fixed finite range gives analytic amplitudes (G1-A). Compact support appears only in the limit (Weierstrass, Fejér). For a range-n trigonometric polynomial amplitude, Turán–Nazarov / Remez-type inequalities suggest sup_U \|T\| ≥ e^{−Cn} sup_M \|T\|: at best exponential suppression, never exact | proved (finite n); bound suggested (comparator; not proved on curved M) |
| Spontaneously broken phases | — | Translation breaking adds Bragg umklapp (strictly worse). Internal-symmetry breaking gives Goldstone mediators, which fall under G1-A. Bogoliubov dispersions are analytic away from nodes | argued |
| Topological order / anyons | — | Gapped, so exponentially local and analytic. Anyon (Aharonov–Bohm-type) forward singularities are meromorphic in angle, so in 𝒜. Symmetry fractionalization changes the zone period (like staggered π), not the existence of an edge, and G1-L1 applies with that period | argued |
| IR in d = 3 with a gapless gauge mediator | — | Exclusive 2→2 amplitudes vanish (soft quanta). The condition moves to inclusive channels 2 → 2 + nγ, each in 𝒜 at tree level. Soft quanta do not remove the matter's edge umklapp | argued |

**Lemma G1-L3 (proved).** Let χ(q,ω) = ∫ρ(q,ω′)[1/(ω − ω′ + i0) − 1/(ω + ω′ + i0)]dω′, with ρ ≥ 0 and ρ(q,·) ≢ 0. Then the zero set of χ(q,·) is null, provided ρ's zero set inside its support is null. That proviso holds for piecewise-analytic weights such as the lattice Lindhard function. A fat-Cantor ρ is not covered.

**The open route, stated plainly.**
- At one fixed coupling, an amplitude with non-analytic (dressed) vertices can be a different analytic function on each side of a codimension-1 wall inside a fibre.
- Real analyticity alone cannot rule out its zero region coinciding with U_s.
- Ruling it out needs one of:
  - physical-sheet analyticity, meaning on-shell T is the boundary value of one holomorphic function on a connected wedge over M, so that zeros cross the walls by edge-of-the-wedge;
  - a fibrewise structure as in G1-B.
- **Why the wedge is not established.** On M, Im E is tied to Im k through the group velocities, and |Im E| ≤ v_max|Im k|. That conflicts with the domain that iε gives, Im E > C|Im k|.
- **Suggested:** the walls are set by bands, Fermi surfaces and thresholds, while U_s is set by an arbitrary lift whose jump surface can be moved. Requiring every wall to track the edge for some lift is a strong coincidence, but it is not proved impossible.

## 3. Strongest correct statement, and the FIXED readings

**Statement.** Take matter with nearest-neighbour TB dispersion on Z^d, d = 2, 3. For lattice KG and staggered matter, add connectivity, which is checked but not proved. The rule is finite-range and translation-covariant, with finitely many fields per site.

1. The sawtooth momentum, for any lift (any fundamental domain, any period-π reduced zone), is an exact collision invariant only if the total on-shell 2↔2 amplitude vanishes a.e. on an umklapp set. That set has nonempty interior, including near-forward edge crossings.
2. Any on-shell amplitude meromorphic on M (class 𝒜) that does so vanishes identically. Class 𝒜 includes every tree-level exchange through any network of any finite depth, gapped or gapless, with cone points and on-shell mediator poles.
3. The same no-go holds:
   - exactly in U for contact scattering;
   - for every family analytic in its coupling down to zero (the coupling must vanish);
   - for exchange through any mediator with positive spectral weight and analytic vertices, Fermi-sea (Lindhard) and critical continua included.
4. A free Fermi sea, a local source of compact momentum support, cannot filter all channels, because of particle–hole complementarity. It gives only a kinematic umklapp gap.
5. Not excluded:
   - a single strongly coupled law whose dressed on-shell vertices carry codimension-1 walls inside the fibres, beyond the two-body-potential sector;
   - nonperturbative non-contact finite-range two-body potentials (reduced to P_R𝒦P_R = 0 on an open (K,E) set).

**Map to the FIXED readings.**
- **PASS: not met.** No construction was found, and every examined source fails.
- **FAIL (bounded): supported for this probe's part.** In order of strength:
  - the analytic class: proved;
  - meromorphic and gapless tree level, any depth: proved;
  - each non-analytic source examined:
    - cone: proved;
    - Fermi-surface exchange: proved;
    - Fermi-sea filter: argued;
    - critical exchange: proved; critical dressed vertices: open;
    - infinite depth: proved (finite n);
    - broken phases and topological order: argued.
  - The open sub-route above should be stated in the bound.
- **INCONCLUSIVE** would apply only if the referee requires the fixed-coupling dressed-vertex route closed, since the FAIL text asks for each non-analytic source *examined* to be decided.

**Against the supervisor expectation.**
- "The identity theorem excludes every analytic class": **confirmed.** It now comes with connectivity (TB, proved) and lift independence (proved).
- "Fermi-surface and cone non-analyticities live on measure-zero sets and cannot create an open zero set": **correct for cones (codimension ≥ 2), false as a principle for codimension-1 sets.** Im χ and below-threshold loop parts vanish on open sets. The Fermi-surface FAIL holds by spectral positivity and complementarity instead.
- **For G2 / readout Q (suggested).** At finite range n, Turán–Remez-type bounds imply ε_U(n) ≥ e^{−Cn}. Exponential decay is the best possible, matching the expectation for G2.

## Labels and strong words

**Proved (same-family, unrefereed):**
- the exact condition T = 0 a.e. on U (1(iii));
- G1-L1, every lift has an open umklapp set;
- G1-L2 and the connectivity of M_reg for TB;
- Theorem G1-A and what lies in 𝒜;
- G1-B, contact, exact in U;
- the reduction G1-B′;
- G1-C, analytic families;
- G1-L3, spectral positivity.

**Checked:** umklapp fractions and interiors for four lifts, d = 2, 3, TB and KG; near-forward umklapp; KG level-set component counts. That count includes 5 self-symmetric two-component fibres in d = 2 at small m.

**Argued:** KG and unequal-species connectivity; the Pauli complementarity filter; broken phases; topological order; the d = 3 IR inclusive channels.

**Suggested:** Turán–Nazarov ε_U ≥ e^{−Cn} on M; walls coinciding with the edge as a non-generic coincidence; a physical-sheet (edge-of-the-wedge) closure of the open route.

**Comparator:** Spohn (via the RN L2 referee); Paley–Wiener; Fermi-liquid n(k); Turán–Nazarov.

**Strong words checked:**
- "exact" is used only for the operator/S-matrix condition and for G1-B.
- "every lift" means every integrable lift. The open-interior claim holds for C¹-jump lifts, and positive measure (via Spohn) for the rest.
- "connected" is proved for TB only.
