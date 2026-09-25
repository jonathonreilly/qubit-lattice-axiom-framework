# At which order does the exchange sign first matter for three or more records?

Unit `J:derive:the-exchange-sign-with-three-or-more-records:a1`, worker `w-macbookpro9927a-j31aa` (Claude Opus 5.5), 2026-09-25.

**Related prior work by this worker (disclosed).**
- `the-exchange-sign-from-the-coin` a1 (#8642, refereed #9073, harvested as block 128) is the two-record result. This attempt builds on it.
- `the-exchange-sign-at-fourth-order-in-the-crowd` a1 (#9165) found the fourth-order sign part at fixed filling on Z³: −6ρ²(1−ρ)².
  - Step 3 below reproduces it as the density limit of an exact finite-V formula.
  - Everything else here is new: the general-N formula, the connected parts, the ring exchanges, the source statements and the torus ground energies.

## 1. Setting (definitions as landed on main)

- **The walk: block 54.** `docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_..._2026-09-21.md`.
  - (T_eψ)(x) = ψ(x−e), D_j = (i/2)(T_j − T_j†), and H = Σ_j σ_jD_j (β = 1, a = a₀ = 0).
  - Equivalently H = ½Σ_j u_j(T_j − T_j†) with u_j := iσ_j. A hop x → x + s e_j multiplies the coin by (s/2)u_j, so 2H has Gaussian-integer entries.
  - On Z² I use the two-axis form σ₁D₁ + σ₂D₂ of block 128 (PR #9185, open; not on main).
- **Records under exclusion: block 78's compression (main).**
  - HC_N = span{⊗_i e_{x_i,a_i} : the x_i pairwise distinct}, and H_N = Π(Σ_i h_i)Π.
  - P_π permutes records. K± are the totally symmetric and totally antisymmetric parts of HC_N; block 128 uses K± for N = 2.
- **The source: block 55 (main).** e_x = Re[χ_x†(H_wχ)_x], summed over internal components and walkers.
  - At uniform rate, for N records, e_x(Ψ) = Σ_i Re⟨Ψ|Q_x^{(i)}h_i|Ψ⟩ = ⟨Ψ|ê_x|Ψ⟩ with ê_x = Σ_i ½{Q_x^{(i)}, h_i}.
  - This is block 55's T1 derivative ∂⟨Ψ|H_{N,w}|Ψ⟩/∂u_x at u = 0, and Σ_x ê_x = H_N on HC_N. The evolution is block 55's iχ̇ = Hχ.
  - For N = 2 this is exactly the landed `..._MANY_RECORDS_UNDER_EXCLUSION_SOURCE_IS_THE_PROJECTED_DENSITY_..._2026-09-22` T1: e_x^(2) = Re⟨Ψ_P|(P_xH_w⊗I + I⊗P_xH_w)|Ψ_P⟩. The N-record form sums the same expression over walkers.
- **Units and conventions.**
  - Traces are summed over coins. "H units" means hop amplitude ½.
  - "Per site" means divided by V, which is the same as pinning record 1 at the origin.
  - n_p is the number of plaquettes per site: 1 on Z², 3 on Z³.

## 2. Statement attempted

**(a) Traces.** For every N ≥ 2 on Z² and Z³:

tr_{K+}H_N^k − tr_{K−}H_N^k = (2/N!) Σ_{π odd} tr(P_πH_N^k).

This difference vanishes for k ≤ 3 and first appears at k = 4. On tori of side ≥ 5:

Δ₄ = −8 n_p V · 2^{N−2} · C(V−4, N−2)

- **The process.** Two records exchange around a plaquette whose other two corners are empty, while every other record stays put.
- **Three records add no sign-carrying process.**
  - Their ring exchange is an even permutation. It has −3 per plaquette at order 4 and enters both sectors equally.
  - A third record changes the sign term only through exclusion. The connected three-record part is +64 (Z²) and +192 (Z³) per site at order 4, and +1764 and +8124 at order 6.
- **The first odd process beyond a pair** is the four-record ring exchange at order 6: +78 (Z²) and +546 (Z³) per site.

**(b) Source.**
- **Two or three records.** Take records starting on definite distinct sites with any coin state, product or entangled. Then block 55's source is the same in both sectors at every time.
  - For two records it vanishes identically.
  - For three it is carried by the even ring exchange alone.
- **Four records.** The sectors' sources first differ, at order t⁵, through the four-record ring exchange.

**(c) Ground energies.** On the 3×3 and 4×4 tori, both sectors, N = 2, 3 (and N = 4 on 3×3), exactly: minimal polynomials, certified windows and degeneracies (table in step 8).

## 3. Steps

**Step 1: the sector identity. PROVED; CHECKED A1.**
- The projector onto K± inside HC_N is (1/N!)Σ_π(±1)^{sgn π}P_π, so for X commuting with every P_π, tr_{K±}X = (1/N!)Σ_π(±1)^{sgn π} tr(P_πX).
- Conjugate permutations have equal traces.
- For N = 3 this gives:
  - tr_{K+}X − tr_{K−}X = tr(P₁₂X);
  - tr_{K+}X + tr_{K−}X = [tr X + 2 tr(P₁₂₃X)]/3.
- So the three-record ring exchange (a 3-cycle) enters only the sum. It separates K± from the mixed-symmetry part, never K+ from K−.
- A1 checks both formulas exactly on the non-bipartite 3×3 torus (odd windings present) for N = 3, k = 2, 3, 4.

**Step 2: no difference below order 4. PROVED.**
- A term of tr(P_πH^k) is a history of k hops that returns the set of occupied sites with the records permuted by π.
- An odd π has an even cycle of length m ≥ 2. If m ≥ 4, at least four records move, so k ≥ 4.
- **If m = 2 (records a, b swap):**
  - At distance ≥ 2, each record needs ≥ 2 hops.
  - If a and b are neighbours and use ≤ 3 hops, one of them, say a, hops once, directly onto x_b. That requires b to have left x_b first.
  - b must end on x_a, which a vacates only by that single hop, so b cannot reach x_a in one hop.
  - Two hops would need a common neighbour of x_a and x_b. There is none: Z^d has no triangles.
- So odd permutations need ≥ 4 hops.
- **Odd orders.** On bipartite lattices (Z^d, even tori) each record's hop count has the parity of its displacement. The displacements under a permutation sum to 0 mod 2, so tr(P_πH^k) = 0 for odd k and every π.
- A3 checks k = 2, 3 for N = 3 on the 5-tori.

**Step 3: order 4 for every N. PROVED; CHECKED A2, A3, A4.**
- At k = 4 an odd π is a transposition whose pair uses all four hops. Any other record that moved would need ≥ 2 hops to return.
- **A four-hop exchange uses exactly the four corners of one plaquette.**
  - *Neighbours.* The hop counts are 1 and 3. The three-hop walks between neighbours are:
    - the plaquette walks x_b → x_b+e → x_a+e → x_a;
    - walks through x_a first, which are blocked;
    - back-and-forth walks, which deadlock: either b's return to x_b or its final hop meets an occupied site.
  - *Face diagonal.* 2 + 2 hops through the two different middle corners; the same corner deadlocks.
  - *Distance 2 on a line.* Both records need the single middle site, so there is no exchange.
- So the other two corners must be empty. On tori of side ≥ 5 no history of ≤ 4 hops winds, so
  tr(P_{ab}H_N^4) = (−8 per plaquette) · n_pV · 2^{N−2}(V−4)!/(V−N−2)!.
- Summing over the C(N,2) transpositions with weight 2/N!:
  Δ₄ = tr_{K+}H_N^4 − tr_{K−}H_N^4 = −8 n_p V 2^{N−2} C(V−4, N−2).
- **Normalisation.** Per site and per state (dim K± = 2^N C(V,N)) this is −2n_p N(N−1)(V−N)(V−N−1)/[V(V−1)(V−2)(V−3)], which tends to −2n_pρ²(1−ρ)² at fixed ρ = N/V. On Z³ that is #9165's −6ρ²(1−ρ)².
- **Checks.**
  - A2 reproduces block 128's −8 per plaquette and its per-pair values −2, −1, 0.
  - A3 (N = 3 on 5² and 5³): tr P₁₂H⁴/V = −16n_p(V−4).
  - A4 (N = 4 on 5×5): tr P₁₂H⁴/V = −32(V−4)(V−5).

**Step 4: the three-record connected part. PROVED identity; CHECKED A3, A7.**
- **Reference.** Records 1 and 2 exclude each other, and record 3 is a free walker.
  - A history has the same amplitude in both. The admissible histories are the reference histories in which record 3 never shares a site with 1 or 2 (t = 0 included).
  - The reference trace factorises: tr_ref = Σ_j C(k,j) tr(PH₂^j) tr(h^{k−j}).
- **Definition.** c_k := [tr P₁₂H₃^k − tr_ref]/V = −(1/V) × (sum of the colliding reference histories). It is finite per site.
- **Order 4.** A plaquette exchange collides with a static third record on any of its 4 corners, with coin trace 2. So c₄ = −(−8n_p)·4·2 = +64n_p: +64 on Z² and +192 on Z³.
- **Order 6, per site, H units.**

| | c₆ | third record static | third record steps out and back |
|---|---|---|---|
| Z² | +1764 | 480 | 1284 |
| Z³ | +8124 | 1860 | 6264 |

- **Pair part at order 6.** −60 (Z²) and −252 (Z³).
- **Checks.**
  - A7: the path method is checked against brute force on the 7×7 torus. There, actual − reference = 1764, and the reference equals the factorised prediction V(15p₄t₂ + 2p₆).
  - Scratch only, not in check.py: brute force on 7³ gave 8124 (551 s).
- Both connected parts are positive: exclusion by a third record reduces the size of the (negative) pair sign term.

**Step 5: ring exchanges. PROVED orders; CHECKED A5, A8.**
- **Three records.**
  - The 3-cycle is even (step 1).
  - Its per-site traces are −3n_p at order 4 (a hole circulating a plaquette that holds three records) and 90 (Z²), 702 (Z³) at order 6.
- **Four records.**
  - The 4-cycle is odd. It needs ≥ 5 hops: with exactly 4, every record hops once onto the next record's site, and the first hop lands on an occupied site. So it needs ≥ 6 on bipartite lattices (A5: zero at order 4).
  - At order 6 its per-site trace is +78 (Z²) and +546 (Z³), confirmed on Z² by 7×7 brute force.
  - By step 1 it enters tr_{K+} − tr_{K−} for N = 4 with total weight 1/2. That is the first sign-carrying process with more than two records.

**Step 6: coin algebra. PROVED; CHECKED W1, W2.**
- The u_j = iσ_j satisfy u_j² = −1 and u₁u₂ = −u₃ (cyclically). They generate the quaternion group Q₈ = {±1, ±u_j}, and Q₈/{±1} ≅ Z₂² is abelian.
- So the coin factor of any walk (the time-ordered product of its hops' ±½u_j) equals ±2^{−n}q(p), where q(p) = u₁^{p₁}u₂^{p₂}u₃^{p₃}. The parities p_j of the per-axis hop counts equal the displacement parities.
  - Closed walks give ±1.
  - W1 checks all walks of ≤ 6 hops on Z³.
- **On Z² (W2).** σ₁ and σ₂ flip the σ₃ coin, so each record keeps g_i = (−1)^{a_i+x_{i,1}+x_{i,2}}. Records with different g never exchange.

**Step 7: the source. PROVED; CHECKED B1, B2, B3.**
- **Setup.** Let s_v be a coin state v ∈ (C²)^{⊗N} on labelled distinct sites X, and Ψ± ∝ Σ_π(±1)^{sgn π}P_πs_v.
- **Reduction to single blocks.** H and ê_x commute with every P_π, and the P_πs_v are orthogonal. Hence e_x^±(t)⟨s_v|s_v⟩ = Σ_σ(±1)^{sgn σ}⟨P_σs_v|A_x(t)|s_v⟩, with A_x(t) = e^{iHt}ê_xe^{−iHt}.
- **Taylor coefficients.** A_x^{(n)} = i^n Σ_j C(n,j)(−1)^{n−j}H^j ê_x H^{n−j}.
- **Each block is a real multiple of a fixed coin operator.**
  - Y_j^σ := ⟨P_σs_v|H^jê_xH^{n−j}|s_v⟩ is a sum over (n+1)-hop histories from X to σX.
  - Each history's weight is a real number: hop factors ±½, ê_x's ½(δ_{x,from} + δ_{x,to}), and real projections.
  - That real number multiplies the coin operator ⊗_i(±q(p_i)) (step 6), which is fixed by σ and X.
  - So Y_j^σ = r_j^σ c_σ(v), with r_j^σ real and c_σ(v) = ⟨v|Π_σ†⊗_iq(p_i)|v⟩ independent of j.
- **Transpositions σ = (ab).**
  - p_a = p_b, so the coin operator is SWAP_ab·(q⊗q)_ab. Here q⊗q ∈ {1, −σ_k⊗σ_k} is Hermitian and commutes with SWAP, so c_σ(v) is real.
  - Hermiticity and P_σ² = 1 give Y_{n−j}^σ = conj Y_j^σ, so r_{n−j} = r_j whenever c ≠ 0.
  - For odd n the weights C(n,j)(−1)^{n−j} and C(n,n−j)(−1)^j are opposite, so the sum vanishes. Even n has no histories (step 2).
  - A_x is entire in t (H is bounded), so the transposition part vanishes at all times.
- **Identity block.** The coin operator is 1, so the identity block vanishes the same way.
- **Consequences.**
  - For N = 2, e_x^± ≡ 0.
  - For N = 3 (odd permutations = transpositions), e_x^+(t) = e_x^−(t) for all x and t. The common value is the 3-cycle part, whose coin operator is not Hermitian; it is nonzero for suitable complex coins.
  - For N = 4 the odd 4-cycles have non-Hermitian coin operators, so a difference is possible.
- **Checks.**
  - B1: N = 2, three geometries, complex coins; all coefficients vanish up to t⁵.
  - B2: N = 3; the L and line clusters on Z² and the L cluster on Z³; e⁺ − e⁻ = 0 through t³. The L cluster with coins ((2, 1+i), (1, 2−i), (1, i)) has d³e/dt³ = ±1/144 on (1,0) and (0,1).
  - B3: N = 4 on a plaquette; d³(e⁺−e⁻)/dt³ = 0, and d⁵(e⁺−e⁻)/dt⁵ = ±1/224 on the far corners of the four neighbouring plaquettes, with zero sum.
  - Scratch only (float, not in check.py): sparse time evolution for N = 3 on the 4×4 torus gives max|e⁺−e⁻| < 10⁻¹⁷ at t = 0.3, 1 and 2.5, while max|e±| ≈ 5·10⁻⁴.

**Step 8: ground energies. CHECKED C, D.**
- **Method.**
  - Build the sector Hamiltonians and split them by total momentum. Use unnormalised orbit sums u_c = Σ_tφ_K(t)T_tc, with liveness tested exactly in Z[i] or Z[ω]. The matrix of 2H_N on span{u_c} has the characteristic polynomial of the restriction.
  - Obtain exact integer characteristic polynomials per momentum class (a Galois pair {K, −K} on 3×3) by reduction mod primes p ≡ 1 (mod 12) and CRT, beyond the bound max_k C(n,k)(4N)^k (|eig 2H_N| ≤ 2dN by row sums).
  - Certify with Descartes counts: no root below the window in any class, and m roots below its top.
  - Factor with sympy to get the irreducible polynomial and its multiplicity.

| torus, N | K+ (symmetric) | K− (antisymmetric) |
|---|---|---|
| 3×3, 2 | −2.3314730774: 2E₀ is a root of x⁸−40x⁶+493x⁴−2214x²+2736; 4-fold | −√6 = −2.4494897428; 1-fold |
| 3×3, 3 | −3.3485824207 (deg 16); 2-fold | −3.4071521701 (deg 72); 4-fold |
| 3×3, 4 | −3.7907221233 (deg 112); 4-fold | −4.0866558476 (deg 112, a different polynomial); 4-fold |
| 4×4, 2 | −2√2; 1-fold at K = (π,π) | −2√2; 3-fold at K = 0, (0,π), (π,0) |
| 4×4, 3 | −3.9991096304; 4-fold at K = (±π/2, ±π/2) | the same number: one root of the same irreducible degree-48 polynomial; 4-fold |

- On the non-bipartite 3×3 torus the antisymmetric sector is lower for N = 2, 3, 4.
- On the 4×4 torus the ground energies are equal for N = 2 and N = 3. Scratch only (float Lanczos): for N = 4 both are −5.17586201, while the excited levels differ.
- **The 4×4 ties and the g-content (step 6).**
  - The ground states lie in mixed g-content.
  - For N = 2 the content (1,1) has no exchange, so the sectors are unitarily equivalent there.
  - For N = 3 the content (2,1) holds one same-g pair that can exchange, yet the ground energies coincide exactly. The two K = (1,1) blocks share a degree-144 factor.
  - The mechanism behind the N = 3 tie is not identified here.

## 4. ASSUMED
- Descartes' rule of signs, and its exactness for real-rooted polynomials (sign variations = number of positive roots). This is classical. It is used only in step 8, on characteristic polynomials of Hermitian operators, which are real-rooted.
- Standard linear algebra: the characteristic polynomial of a restriction to an invariant subspace, the Gershgorin row-sum bound, and CRT.
- No physics theorem from outside the notes is used.

## 5. What would finish it / open
- The connected three-record series beyond order 6, and its resummation at fixed density; #9165 treated fourth order only.
- The mechanism of the 4×4 ground-energy ties at N = 3 (exact) and N = 4 (float), and their fate on larger even tori.
- Clusters that are not site-localised: packets whose supports overlap within a hop are not treated.
- The walk, the compression and the composition rule remain supplied, as in block 128. Nothing here selects a sector.

## 6. Reproduce
`python3 probes/work/derive/the-exchange-sign-with-three-or-more-records/w-macbookpro9927a-j31aa/check.py`

The script uses exact integer, Gaussian-integer, Fraction and polynomial arithmetic. Floats serve only to choose part C's rational windows, which are then certified exactly. It runs in about 6 minutes, single-threaded.
