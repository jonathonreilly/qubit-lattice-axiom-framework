# YM4 existence via the Balaban RG: lemma ledger (sessions 1-8, 2026-10-26/27)

**Session-8 header.** Session-8 additions are marked **[S8]** (all in L5). Targets were pre-stated in RTARGET.md §5-7
before any derivation. No review file was produced after session 7, so there are no review fixes in this session.
- **Lemma GT** (gauge-invariant Taylor lemma): for every gauge-, B_4- and ι-invariant C⁶ function of lattice data along
  a smooth radial-gauge background, order s² vanishes (semisimplicity), odd orders vanish (ι), and order s⁴ is
  c·Σ||F_μν(0)||² (Λ²R⁴ is absolutely irreducible under B_4; no ε·F·F term). PROVEN-HERE.
- **Proposition R4D-iso** (moved from OPEN): one isolated 4D SU(N) cube, frozen exterior, soft constraint, plaquette
  cut priced by inequality (B): ρ = ρ_0 + δβA_B + O(e^{-a/g²}s⁶), a < ε_1²/(4N), s_0 g-independent. PROVEN-HERE, met as
  pre-stated. For isolated cubes, LF-count's 4D divergence sits entirely in the field-independent ρ_0.
- **Check c19** (criteria first): 10/10 PASS (B_4 character norm 1; one invariant form; GT on three SU(2) function
  families, one exactly integrated; B_4-broken and ι-broken controls show the check has power).
- **W1 (2D, fluctuating sea): partial.** Lemmas W1-def (exact defect identity), W1-size (exact size reduction to a
  collar large deviation) and W1-sym (symmetry + locality ⇒ renormalised form) PROVEN-HERE. The exact remaining wall is
  the new OPEN item **W1-loc** = (W1-LD) collar large deviations + (W1-cl) exponential clustering of the block-pinned
  small-field sea. Both are small-field-sea statements (the 2D analogue of L4a-form / CMP 116), not large-field ones.
- W2 pre-stated only (RTARGET §7).


**Session-7 header.** REVIEW_S5_S6.md has been applied first; every fix is marked **[R56-fix]**. Session-7 additions
are marked **[S7]**.
- Fixes: A1 (supremum, not attained); A2 (E8** only, E8* corollary withdrawn); L4a-Π phase sign and the (1.21)
  citation; A1-NA(1) ((c) by concavity, principal branch, coarse side ≥ 3, c_N = c√N); A1-NA(k) and L1d [S6] restricted
  to S4' iterates (new OPEN L1e-(0.4)); the L4a-form torus side (4L^M vs 2L^m); LF-count in Balaban's normalisation
  (β'_B ≈ 4Nb_0, threshold a_B > 43/N², "ε_1 small enough", conditional on the one-loop rate); c18b declared outside
  the lemma's regime; new in-regime check c18c (pre-registered; 16/16).
- One-cube R-operation: the target was pre-stated in RTARGET.md before the derivation. The 2D wall was verified
  (every single-bond cut for 3 ≤ N ≤ 8; the O(3) instanton is exactly marginal). **Proposition R2D-iso** proves the
  target for an isolated cube. The full R-operation's remaining walls are named: W1 (localisation in a fluctuating
  sea), W2 (nested multi-scale large fields), W3 (hard constraints and branch sets). The 4D transfer is OPEN item
  R4D-iso.
- Literature: CMP 198 (1998) is the low-temperature d ≥ 3 N-vector series, not a 2D UV template.

**Session-6 header (CMP 109 reading session).** Session-6 additions are marked **[S6]**. No review file was produced
after session 5, so there are no [R5-fix] items. The owner supplied Balaban, CMP 109 (1987) 249-301. It was read in
full. Its notes, with page and equation numbers, are in `literature/NOTES.md` §9; the open-source search for the
large-field results is in §10.

Main findings:
- CMP 109 is **small-field only**.
- It **defers two things**: the localisation/cluster-expansion half of its own inductive theorem (to CMP 116, "II.
  Cluster expansions"), and the coupling-flow theorem (Theorem 2, (0.31)) to "a separate paper".
- It cites, without reproving, everything from CMP 98/99/102 that L1d, L2 and L3g need.
- Balaban's link average (0.4) equals our S4' up to the pairing of the coordinate orders at the two ends (c17(B)).
- Balaban's background small-field condition (1.2) is L1e's hypothesis, **[R56-fix]** for S4' iterates and up to the
  √N norm conversion; for Balaban's own (0.4) it needs L1e-(0.4) (OPEN).

Upgrades:
- None of L1d, L2, L3g, L4a is upgraded wholesale.
- **L4a-Π** (the definition of β_j from the polarisation tensor, CMP 109 §5) is re-derived: PROVEN-HERE.
- L1d is narrowed.
- The open item A1-NA is proven in its one-step form, A1-NA(1), together with a k-uniform corollary on the L1e domain
  (for S4' iterates [R56-fix]).
- **Proposition LF-count** names the exact 4D wall: the unrenormalised per-level large-field count diverges. This is
  why the R-operation (L5) is load-bearing, and no open source states it.

**Session-5 header (reading and re-verification session).** REVIEW_S4.md has been applied first; every fix is marked
**[R4-fix]**. Session-5 additions are marked **[S5]**. Dimock's open expositions of Balaban's method were read (source
notes with page and equation references: `literature/NOTES.md`). The mapping onto L1d, L2, L3g, L4a, L5 and L6, and the
E8** reassessment, are in the [S5] block of L6loc. No Balaban CMP body has been read; every Balaban statement is still
[unverified-exact-statement]. **Correction:** Dimock's "RG according to Balaban" I-III treats scalar φ⁴ in d = 3, not
scalar QED; QED in d = 3 is his separate series (arXiv:1512.04373, 1712.10029, 2009.01156, overview 2204.07201).

**Session-4 header.** REVIEW_S3.md has been applied first; every fix is marked **[R3-fix]**. Session-4 additions are
marked **[S4]**. From session 4 the single off-D extension defining V^(m) and O at every level is S4'' with the odd
branch rule (section S4); the session-3 "failed link := 1" extension is withdrawn.

**Session-3 header.** REVIEW_S2.md has been applied first; every fix is marked **[R2-fix]**. Session-3 additions are
marked **[S3]**.

**Session-2 header.** REVIEW_S1.md (independent hostile review of the session-1 snapshot) has been applied: every fix
is marked **[R1-fix]** in place. Session-2 additions are marked **[S2]**. Two general caveats from the review apply to
the whole file:
- **Checks test instances, not uniformity.** Each check in checks/ verifies a stated identity or inequality on finitely
  many configurations and sizes. Uniformity in n, k, K, M or the background rests on the written proofs alone.
- **The citation upgrades** marked [v-R1] were confirmed by the reviewer's web search, not by me.

**Goal (owner).** Derive, independently, the existence of 4D pure SU(N) Yang-Mills as a continuum limit of lattice gauge
theory satisfying the Osterwalder-Schrader (OS) axioms. No mass gap is claimed.

Probe document only. No PR, no CL edit, no axiom edit. The lemma DAG follows
`../openai-balaban-review/review.md` section 6 (L1-L10, F1-F4, C1-C4), refined below.

## Status legend
- **PROVEN-HERE**: the complete argument is written in this file.
- **IMPORTED-AND-REVERIFIED**: exact citation and statement; hypotheses checked on our setting; the load-bearing step
  re-derived here, or checked exactly or numerically (named check).
- **IMPORTED-NOT-YET-REVERIFIED**: a named obligation. It never supports a PROVEN claim.
- **OPEN**: the missing estimate is stated.

## Citation key
- **[v]**: title, journal, volume and pages confirmed by web search this session (bibliographic data only; the paper
  bodies are paywalled and were NOT read).
- **[v-abs]**: the abstract or introduction was read.
- **[m]**: from memory, not confirmed.
- **[unverified-citation]**: the attribution is plausible, but the exact reference was not confirmed.

- **[S6] [read]**: read in the primary text; **[read-abs]**: abstract only; **[v-crossref]**: bibliographic data from
  the Crossref API.

**[S6] Caveat update.** Statements attributed to CMP 109 and tagged [read] are transcribed from the paper (NOTES §9).
What CMP 109 says about CMP 98/99/102 is [read, second-hand]. Every other Balaban statement remains as below.

**Global caveat.** Every statement attributed to Balaban below paraphrases the *structure* of his programme. The exact
theorem statements (norms, constants, hypotheses) were not read. Each is therefore `[unverified-exact-statement]`, and
re-verifying it is part of the obligation.

---

## 0. Target, and how it decomposes

**T_fin (finite volume).** On the torus T^4_M (side L^M in resolution-0 units), the lattice measures along a tuned
sequence of bare couplings converge, as the lattice spacing L^-K → 0, to a limit state on a gauge-invariant observable
algebra. The limit is non-trivial and reflection positive, with the torus symmetries.

**T_OS (the owner's target).** There is a state on an E(4)-covariant algebra of gauge-invariant observables on R^4. It
arises as such a limit, satisfies OS0-OS3 (OS4 clustering is listed separately in L9d), and is not a free theory.

Structural findings of this session:
1. **Existence of limit points of block laws is cheap; existence of the theory is not.** At every fixed resolution the
   RG variables live in a compact space, so limit points of the *block laws* exist by compactness alone: L7a and L8a,
   proven here, at finite and at infinite volume, with no infrared control. [R1-fix] These limit points are not yet a
   theory: without E8 the per-resolution limits need not be consistent (A_* ν_{m+1} ≠ ν_m is possible), mass may sit on
   the arbitrary off-D extension, and non-triviality has the L7.0 gap. The content of the theorem lies elsewhere:
   - (a) the limit is non-trivial and consistent across resolutions (needs Balaban's local large-field suppression, L6loc;
     [S3] in the scale-local form E8*, since the "all steps succeed" form is false along AF sequences, E8.3);
   - (b) uniqueness, i.e. convergence of the whole sequence (estimate E7);
   - (c) Euclidean invariance and OS0 regularity on a *local* field algebra (L9b, L9c).
2. **The infrared strong coupling is not an obstruction to the existence of limit points of block laws** (section L8).
   [R1-fix: the session-1 wording "not an obstruction to existence" was overstated.] It obstructs uniqueness of the
   infinite-volume state, clustering and the mass gap. Through uniqueness it also obstructs route γ1 to OS1 on R^4, so
   it may well obstruct existence of the OS theory itself.
3. **Euclidean invariance is the hard core.** On T^4 it is false: the torus breaks O(4). On R^4 it cannot be obtained
   by averaging over rotations, because averaging destroys reflection positivity (remark R9.1). It needs either
   universality (orientation independence, which rests on E7-type estimates) or a second, rotation-covariant observable
   family identified with the block family.

---

## 1. Setting (fixed for the whole document)

- **S1 Lattice.** Fix an integer L ≥ 3, odd. Balaban takes L sufficiently large [m]. The resolution-j lattice is
  Λ_{j,M} = (L^-j Z / L^M Z)^4, in physical units with the resolution-0 spacing equal to 1. The UV cutoff is the
  resolution K, with spacing ε_K = L^-K.
- **S2 Group.** G = SU(N), N ≥ 2. The links are U_b ∈ G on oriented bonds, with U_{-b} = U_b^dag.
- **S3 Wilson action.** S_K(U) = β_K Σ_p (1 - N^-1 Re tr U_p), with β_K = 2N/g_K^2. The measure is
  dμ_K = Z_K^-1 e^{-S_K} Π_b dU_b, with Haar measure dU_b.
- **S4 Averaging (L1).** Fine blocks B(X) have side L in lattice units, and their roots are the block centres c_X (L is
  odd).
  - Paths: T_y = P(c_X → y) · [L straight steps from y in direction μ] · P(c_Y → y + L e_μ)^dag, where P is the
    complete-axial transporter (move in coordinate 1, then 2, 3, 4).
  - Coarse link: U'(X, X + e_μ) = T_{c_X} exp(L^-4 Σ_{y∈B(X)} log(T_{c_X}^-1 T_y)), with the principal logarithm.
  - The map is defined on the small-field domain D = {||T_{c_X}^-1 T_y - 1|| < 1 for all y}.
  - The iterate A^{K-m} gives the resolution-m field V^(m). [Balaban-type; whether it equals the CMP 98 definition is
    unverified.]
- **S4' [S3] Order-averaged averaging (adopted from session 3; S4 kept as the fixed-order special case).**
  - For each of the d! coordinate orders σ, let P^σ be the complete-axial transporter moving in the coordinates in
    the order σ, and T^σ_y = P^σ(c_X → y) · S_y · P^σ(c_Y → y + L e_μ)^dag, with S_y the straight leg of L steps.
  - The reference T^σ_{c_X} = S_{c_X} (the straight transporter c_X → c_Y) does not depend on σ.
  - U'(X, X + e_μ) = S_{c_X} exp( (1/d!) Σ_σ L^-d Σ_{y∈B(X)} log(S_{c_X}^-1 T^σ_y) ), on the domain
    D' = {||S_{c_X}^-1 T^σ_y - 1|| < 1 (D'_N: < 2 sin(π/N) for N ≥ 7) for all σ, y}.
  - **S4'' (everywhere-defined version).** Off D', replace the averaged log X̄ by its traceless part X̄ - (tr X̄/N)·1,
    with the principal log (arg ∈ (-π, π)). **[R3-fix] Odd branch rule (session 4):** if Z has an eigenvalue exactly -1,
    its log is set to 0. Then log(Z^-1) = -log Z and log(WZW^-1) = W log(Z) W^-1 hold for EVERY Z (Z^-1 and WZW^-1 have
    eigenvalue -1 iff Z does), so the L9a' reversal computation, gauge covariance and permutation covariance hold
    everywhere, with no null-set proviso. S4'' is SU(N)-valued and measurable everywhere, equals S4' on D'_N, and is
    discontinuous only on the branch set (some Z with eigenvalue -1). **S4'' with this rule is the single map that defines
    V^(m) and the observable algebra O at every level from session 4 on**; the session-3 extension "failed link := 1"
    of L8b/L8c is withdrawn (REVIEW_S3 fix 4). Used in S5' (L6loc).
  - **Re-checks of the dependent lemmas for S4' (done here).**
    - L0 (locality, iterated roots): every P^σ stays in its block. Unchanged.
    - L1a: each log(S_c^-1 T^σ_y) is conjugated by g(c_Y); so is the average. L1b: an average of traceless
      anti-Hermitian logs is traceless anti-Hermitian. L1c: linear in the path set, so it holds with the order average.
    - L1e: the proof used only (1) Z_y has ≤ (d+2)L links and (2) the ribbon decomposition, which holds for any order
      because axial paths of order σ are translation covariant and split into one segment per coordinate. Same
      constants.
    - L9a': a coordinate reflection preserves every order σ, maps the σ-path set onto itself, and maps the reference
      S_{c_X} to the reversed reference. The reversal computation is unchanged.
    - **New: axis permutations.** A permutation π of the axes maps order-σ paths to order-(π∘σ) paths and straight legs to
      straight legs; the order set is permutation invariant and the reference is order-free. Hence
      V^(m)[πU] = π V^(m)[U] (on D', and everywhere for S4''). This repairs L8b.
    - Check c8 (12/12, 2 s): gauge covariance, SU(N), pure gauge, axis-permutation covariance (error 1e-15; the
      fixed-order S4 control fails at 0.1), reflection covariance, for SU(2) and SU(3) on the even fine torus of side 6.
  - **Torus side [S3].** From session 3 the fine torus side is taken EVEN, 2L^{K+M} (coarse side 2L^M in resolution-0
    units). All blocks still tile. A block-boundary reflection plane then has a block-boundary antipode, so L8c needs
    only the pure link reflection of L9a (L9a-m remains valid for odd sides), and the chessboard estimate E8.1 applies.
  - **Torus side [S4].** From session 4 the fine side is 4L^{K+M}, so every level-m side 4L^{M+m} is divisible by 4;
    the coarse chessboard E8*-red needs an even number of 2-site cells per direction. Every S3 statement holds verbatim.
- **S5 Renormalisation condition (RC).** [R2-fix: aligned with L7.0.] RC is read with the continuous cut-off observable
  w̃ = ζ · (1 - N^-1 Re tr V^(0)_p) of L7.0. At each K, tune β_K so that E_{K,β_K}[w̃] = w*, which is possible for every
  w* ∈ (0, w̃_0(K)) (L7.0). A single w* for all K needs E7.0. [S3, R3-fix] Section L6loc shows that, for N = 2, 3, 4,
  E7.0 restricted to the AF window fails (sequences with β_K ≤ λ_c K), so this RC is replaced by S5' (L6loc); for
  N ≥ 5 it is undecided.
- **S6 Observables.** O_m(X) is the set of continuous, gauge-invariant f(V^(m)|_X) for X a finite union of
  resolution-m blocks, extended measurably off D. The algebra is O = ∪_m O_m.
- **S7 OS axioms (target).**
  - OS0: regularity / temperedness.
  - OS1: E(4) invariance.
  - OS2: reflection positivity.
  - OS3: permutation symmetry (automatic for these bosonic observables).
  - OS4: clustering.

---

## 2. Lemma ledger

### L0. Locality and consistency of the averaged fields: PROVEN-HERE
**Statement.**
- (i) V^(m)(X, X + e_μ) depends only on the fine links inside B^(m)(X) ∪ B^(m)(X + e_μ), the two resolution-m blocks.
- (ii) Under a fine gauge transformation g, V^(m)(X, Y) → g(c^(m)_X) V^(m)(X, Y) g(c^(m)_Y)^dag. Here c^(m) are the
  iterated roots: the centre of a block of side L^{K-m} is a fine site, because L is odd.
- (iii) A(V^(m+1)) = V^(m) holds identically on D (D_N for N ≥ 7, see L1b) (definition of the iterate).
- (iv) Every f ∈ O_m(X) is gauge invariant, bounded, and measurable with respect to the links in X.

**Proof.**
- (i) For one step: the axial paths P stay inside their own block. The straight leg runs from y ∈ B(X) to
  y + L e_μ ∈ B(X + e_μ), and its μ-coordinate stays in [X_μ L, X_μ L + 2L - 1], so it passes only through the two
  blocks. Induct on the number of steps; at each step the two coarse blocks contain the fine blocks used.
- (ii) Every T_y has the endpoints c_X and c_Y, so T_y → g(c_X) T_y g(c_Y)^dag. The rest is L1a, applied
  inductively, with the coarse gauge transformation g|_roots.
- (iii) By definition.
- (iv) f is a gauge-invariant function of the coarse field, which by (ii) transforms covariantly; locality is (i). ∎

### L1. Gauge-covariant averaging
- **L1a. Covariance: PROVEN-HERE.** U'[g·U] = g(c_X) U'[U] g(c_Y)^dag, and D is gauge invariant.
  - Proof: T_{c_X}^-1 T_y → g(c_Y) (T_{c_X}^-1 T_y) g(c_Y)^dag. The principal log commutes with unitary conjugation,
    the norm is conjugation-invariant (so D is invariant), and the exp of the averaged log is conjugated by g(c_Y).
    Multiply by T_{c_X} → g(c_X) T_{c_X} g(c_Y)^dag. ∎
  - Check c1(a): error 6e-16 for SU(2) and 6e-15 for SU(3), with random g on all fine sites.
- **L1b. SU(N)-valued; pure gauge goes to pure gauge: PROVEN-HERE.**
  - **Domain.** Take D_N = {||T_{c_X}^-1 T_y - 1|| < 2 sin(π/N) for all y}. For N ≤ 6 the bound 1 of S4 suffices
    (2 sin(π/6) = 1); for N ≥ 7 use D_N. [R1-fix: session 1 wrote "N ≤ 5" here and "fails for N ≥ 7" in LOG; the
    correct threshold is N ≤ 6.] D_N shrinks like 1/N, so any claim uniform in N must track it.
  - **Proof.** Each Z_y = T_{c_X}^-1 T_y ∈ SU(N) has eigenvalues e^{iθ_j}. The domain condition gives |θ_j| < 2π/N
    (for N ≤ 6, the bound 1 gives |θ_j| < π/3 ≤ 2π/N).
    - So the principal log is i·diag(θ_j) in the eigenbasis, anti-Hermitian, with trace iΣθ_j.
    - det Z_y = 1 gives Σθ_j ∈ 2πZ, and |Σθ_j| < 2π, so Σθ_j = 0.
    - The average of traceless anti-Hermitian matrices is traceless anti-Hermitian, its exponential lies in SU(N), and
      T_{c_X} ∈ SU(N).
  - Pure gauge: U_b = g_x g_y^-1 gives T_y = g(c_X) g(c_Y)^-1 for all y, all the logs vanish, and
    U' = g(c_X) g(c_Y)^-1. ∎
  - Check c1(b, c) for SU(2) and SU(3).
- **L1c. Linearisation: PROVEN-HERE.**
  - If U_b = exp(i t a_b) with ||a_b|| ≤ 1, then log U' = i t L^-4 Σ_y (Σ_{b∈Γ_y} a_b) + O(t^2), where Γ_y is the
    path of T_y. This is Balaban's abelian averaging Q applied to the line integrals.
  - Proof: BCH gives log T_y = i t Σ_{Γ_y} a_b + O(t^2) and log(T_{c_X}^-1 T_y) = log T_y - log T_{c_X} + O(t^2).
    Average, and add log T_{c_X} back at order t. ∎
  - [R1-fix] Check c1(d) compares log U' with avg_y log T_y, **not** with the averaged line integrals stated above. Those
    two differ at O(t^2) (the second-order BCH commutators cancel in the first, so log U' = avg log T_y + O(t^3)), which
    is why the halving ratio is about 4. The session-1 reading "second order, better than the claim" was a misreading of
    which identity was tested. The lemma itself stands on the BCH proof; the line-integral form is untested by c1(d).
  - The O(t^2) constant depends on L through the path lengths; no uniformity in L is claimed.
- **L1d. Regularity on Balaban's spaces of regular configurations: IMPORTED-NOT-YET-REVERIFIED.**
  - Content: analyticity of A on D; derivative bounds; the coarse small-field condition implied by the fine one with
    L-dependent constants; the composition of k steps controlled uniformly in k.
  - Sources: Balaban, "Averaging operations for lattice gauge theories", CMP 98 (1985) 17-51 [v]; "Spaces of regular
    gauge field configurations on a lattice and gauge fixing conditions", CMP 99 (1985) 75-102 [v-R1].
  - [R2-fix] The session-2 line "the k-uniform sup-curvature part of this obligation is now proven" is WITHDRAWN. L1e
    below is a theorem about *smooth* backgrounds (F small in physical units). Balaban's small-field conditions are
    dimensionless (||1 - U_p|| ≲ p(g_k) g_k at each scale, so F ~ ε^-2 there), and L1e says nothing about them. The
    fine-to-coarse small-field propagation of L1d is untouched by L1e.
  - Finite diagnostic c1(e): one coarse plaquette has F_coarse ≈ 0.14-0.2 F_fine,max for smooth SU(2) and SU(3) fields.
  - Obligation: a k-uniform version with explicit constants.
  - **[S5]** Abelian analogue [read]: Dimock arXiv:1712.10029 Theorem 1 (p.43, eq. 327), multiscale regularity with
    constant C_0 M p_j, described there as "abelian versions of non-abelian results" in CMP 99 (1985) 75-102 and CMP 102
    (1985) 277-309. What transfers: per-level dimensionless small-field conditions; gauge equivalence on enlarged cubes
    to a regular field. What is abelian-specific: linear averaging, gauge-potential RG variables. Status unchanged.
  - **[S6] CMP 109 [read] narrows L1d.** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
    - **Lemma B-avg [S6]: PROVEN-HERE (elementary).** Balaban's averaged link is CMP 109 (0.4) or (0.12). (0.4) is S4' with the two contour families
      averaged *independently*; S4' pairs them by order. With the same pairing the two are identical, by the conjugation
      identity exp(avg log(TS^{-1}))S = S exp(avg log(S^{-1}T)) (check c17(B): error ≤ 6e-16 in d = 3, 4). With
      independent pairing they agree at linear order and differ at second order (c17(B), ratio 3.96).
    - **Transfer of the CMP 98 results.** CMP 109 asserts that "all results of the paper [12] are valid" for (0.4) and
      (0.12) (p.254). It does not axiomatise link averages, so the transfer to S4' itself is NOT covered by any
      statement read. Either adopt (0.4) verbatim (L0, L1a-c, L8b and L9a' carry over by the same proofs, and A1 holds
      because the linearisations coincide), or keep S4' and prove the CMP 98 results for it.
    - **L1d(i), fine regular ⇒ coarse regular, k-uniformly.** This is now covered on Balaban's own domain. CMP 109
      (1.2) (p.260) defines the background small-field domain as |U(∂p) - 1| < ε_0η², η = L^{-k}, i.e. curvature
      F < ε_0 in units of the current coarse lattice. **That is L1e's hypothesis F ≤ F_0** [R56-fix: for S4' iterates and up to √N; see below]. L1e(b) then gives
      |V(∂p') - 1| ≤ (1 + 4C_δ)F, uniformly in k (d = 4, L ≥ 9 odd). Balaban states the same implication with the
      constant 2 ("By Proposition 2 [12]", p.260) and assumes L > 11. So the R2-fix sentence "L1e says nothing about
      Balaban's small-field conditions" is narrowed: it is true for the fluctuating RG variables (their threshold ε_1
      sits at the level's own scale, NOTES §9.5), and false for the background-field domain (1.2), which is precisely
      L1e's domain. Our constant 1 + 4C_δ (≈ 29 at L = 9) is worse than 2. Nothing downstream needs 2.
    - **[R56-fix] GAP in the narrowing above; scope restated.** L1e is proven for S4/S4' iterates only. Balaban's
      (0.4) averages the two contour families *independently* (Lemma B-avg), and L1e's ribbon step (the translate
      γ + s_je_μ of the SAME-order axial path) does not apply when the two ends use different orders σ ≠ σ': the loop
      is then the ribbon times a loop formed by two axial paths with the same endpoints. Also, Balaban's |·| uses the
      normalised trace (tr 1 = 1), so "|U(∂p) - 1| < ε_0η²" matches L1e's operator-norm F ≤ F_0 only up to the √N
      norm conversion. Corrected statement: **L1d(i) is covered on (1.2) for S4' iterates, up to the √N norm
      conversion; for Balaban's (0.4) it needs L1e for (0.4), the two-axial-path ribbon variant (new OPEN item
      "L1e-(0.4)", expected easy: C_A → ~2C_A, not written).** The bold sentence above is to be read with this
      restriction.
    - **What remains of L1d (still imported, from CMP 98 and 99:75-102):**
      - analyticity on the complexified spaces U^c_j(X, α_0, α_1) (NOTES §9.4, conditions (i)-(iv));
      - the second-order quantity J = D*_U η^{-2} π Im ∂U in (1.2), which L1e does not control;
      - the converse (V regular ⇒ U_k(V) ∈ U_k(ε_0)), which is L2;
      - Proposition 5 of CMP 89:411-445 (derivatives of averaging operations).

- **L1e. [S2] Iterated averaging stays uniformly close to straight fine transport, for smooth backgrounds:
  PROVEN-HERE.** [R2-fix: scope.] The hypothesis F ≤ F_0 ≈ 0.08 (d = 4, L = 9) is in *physical* units, i.e.
  ||1 - U_p|| ≤ 0.08 ε^2 at the fine scale. It describes classical smooth fields such as the backgrounds U(V) of L2. It
  does not describe typical Wilson configurations or Balaban's small-field regime (see L1d), exactly as L3s(d).
  - **Setting.** Fine spacing ε = L^-k in physical units, so unit blocks have side 1. Put V^(k) = U and
    V^(j) = A(V^(j+1)) (S4 applied on the resolution-(j+1) lattice), with s_j = L^-j.
    - For a resolution-j link b = (X, X + e_μ), let S_b be the fine straight transporter between the fine roots c^(j)_X
      and c^(j)_X + s_j e_μ. These roots are fine sites; the iterated root offset is (L^{k-j} - 1)/2.
    - F := max over fine plaquettes p in the region of ||1 - U_p|| / ε^2.
    - Define δ_j := max_b ||V^(j)_b - S_b|| / s_j^2, so that δ_k = 0.
    - Constants: c := 4 arcsin(1/4) = 1.0107, C_A := (d-1)/2, and ρ := (1 + c(d+2)) / L.
  - **Claim (recursion), for every odd L.** If every Z_y used at level j obeys ||Z_y - 1|| ≤ 1/2, then
    δ_j ≤ ρ δ_{j+1} + c C_A F.
  - **Corollary (uniform in k).** Let L > 1 + c(d+2) (= 7.07 in d = 4, so L ≥ 9), and put C_δ := c C_A / (1 - ρ). If
    F ≤ F_0 := 1 / (2(C_A + (d+2) C_δ / L)), then for all k and all j ≤ k:
    - (a) the domain hypothesis holds at every level, and δ_j ≤ C_δ F;
    - (b) coarse curvature: ||1 - V^(j)_p|| ≤ s_j^2 (1 + 4 C_δ) F, so F_j ≤ (1 + 4C_δ) F uniformly in k;
    - (c) every V^(j) lies in D (indeed ||Z_y - 1|| ≤ 1/2 < 1). For SU(N) membership via L1b we also need
      1/2 < 2 sin(π/N), i.e. N ≤ 12. For N ≥ 13, replace 1/2 by τ_N/2 throughout, which shrinks F_0 by a factor ~ 1/N.
    - The proof uses only unitarity and the spectral log, so it holds for every SU(N), with c computed at the threshold
      used.
  - **Proof of the recursion.**
    - Write V = V^(j)_b = T_c exp(X̄), where X̄ = avg_y log Z_y and Z_y = T_c^-1 T_y are products of resolution-(j+1)
      links. Let T^S and Z^S be the same products with every V^(j+1) link replaced by its S.
    - T_c is the straight product of L links, and T^S_c = S_b. For unitaries, ||Π A_i - Π B_i|| ≤ Σ ||A_i - B_i||.
      Hence ||T_c - S_b|| ≤ L δ_{j+1} s_{j+1}^2 = δ_{j+1} s_j^2 / L.
    - Z_y contains at most 2L + d(L-1) ≤ (d+2)L links: two axial legs of at most d(L-1)/2 links each, and two straight
      legs. Hence ||Z_y - Z^S_y|| ≤ (d+2) δ_{j+1} s_j^2 / L.
    - **Ribbon bound: ||Z^S_y - 1|| ≤ C_A s_j^2 F.**
      - Z^S_y is the fine holonomy of γ σ_y (γ + s_j e_μ)^-1 σ_c^-1. Here γ is the fine realisation of the
        resolution-(j+1) axial path c_X → y, σ is the straight μ-leg of length s_j, and γ + s_j e_μ is the axial path
        c_Y → y + s_j e_μ, because axial paths are translation covariant.
      - Insert σ_p σ_p^-1 at each corner p of γ. The loop becomes a product of conjugated rectangle loops, one per
        segment γ_ν.
      - For ν = μ the rectangle is degenerate and collinear, so its holonomy is exactly 1.
      - For ν ≠ μ it is a planar |γ_ν| × s_j grid. Its boundary holonomy is a product of conjugated plaquettes (row by
        row: each row is a ladder, as in L3s(i)), so its norm is ≤ |γ_ν| s_j F.
      - Finally |γ_ν| ≤ ((L-1)/2) s_j / L < s_j / 2. Summing over ν ≠ μ gives ≤ (d-1) s_j^2 F / 2.
    - **Log and exp bounds.**
      - If ||Z - 1|| ≤ 1/2, then ||log Z|| ≤ c ||Z - 1||. Z is normal, |e^{iθ} - 1| = 2 sin(|θ|/2), and
        2 arcsin(x/2)/x is increasing, with value c at x = 1/2.
      - For anti-Hermitian X, ||e^X - 1|| ≤ ||X||, and ||X̄|| ≤ max_y ||log Z_y||.
    - **Combine.** ||V - S_b|| ≤ ||T_c - S_b|| + ||e^{X̄} - 1||
      ≤ s_j^2 [δ_{j+1}/L + c(C_A F + (d+2) δ_{j+1}/L)]. Divide by s_j^2. ∎
  - **Proof of the corollary.** Induct downward from δ_k = 0.
    - If δ_{j+1} ≤ C_δ F, then ||Z_y - 1|| ≤ s_j^2 (C_A + (d+2) C_δ / L) F ≤ 1/2, using s_j ≤ 1 and F ≤ F_0. So the
      recursion applies, and δ_j ≤ ρ C_δ F + c C_A F = C_δ F.
    - (b): S_p is the fine holonomy of a planar s_j × s_j square, so ||1 - S_p|| ≤ s_j^2 F. Add the four link errors.
    - (c) is the domain bound. ∎
  - **Check c5** (SU(2); d = 2, 3, 4; L = 3, 5, 7, 9; k = 2-3). The recursion and the domain hold in every small-field
    case.
    - Measured δ_j/F lies in 0.01-0.08, far below the bound c C_A ≈ 1.5 (d = 4).
    - In the L = 3 cases (ρ > 1, not covered by the corollary) the measured δ_j grows roughly additively in the number of
      levels: 0.028, 0.057, 0.083 in d = 3 with k = 3. So uniformity in k at small L is genuinely not shown.
    - These are instances, not uniformity tests.
  - **What remains of L1d:** all of it for non-smooth fields (Balaban's small-field regime), plus analyticity in U,
    derivative and Hölder bounds, and the large-field side. c5 never instantiates d = 4 with L ≥ 9 (every d = 4 case has
    L = 3, ρ = 2.35), so the corollary rests on the proof alone (REVIEW_S2 re-derived it).

### L2. Background field (constrained minimiser): IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** For V in the coarse small-field domain, the Wilson action restricted to {U : A(U) = V}
  has a unique minimiser U(V) near the identity in a suitable axial/Landau gauge. U(V) is analytic in V and
  exponentially localised.
- **Source.** Balaban, "The variational problem and background fields in renormalization group method for lattice gauge
  theories", CMP 102 (1985) 277-309 [v-R1].
- **Obligation.** An SU(2) Newton/continuation check of uniqueness on an 8^4 torus, plus a written contraction argument.
- **[S5]** Abelian analogue [read]: the minimiser is a linear operator, A^min = H_k A_{k+1}, axial and Landau versions
  gauge equivalent (arXiv:2204.07201 p.6, eqs. 22-25); exponential decay of H_k is imported by Dimock from CMP 95, 96, 99
  (1512.04373 Lemma 9, "we sketch the proof"). The non-linear existence/uniqueness/analyticity problem has no abelian
  counterpart. Status unchanged.
- **[S6] The exact imported statement, as CMP 109 cites it [read, second-hand].** Status unchanged:
  IMPORTED-NOT-YET-REVERIFIED. Theorem 1 of CMP 102:277-309 is quoted by CMP 109 as follows. For V on T_1^{(k)} with
  |V(∂p') - 1| < ε_0', "there exists exactly one regular, critical orbit of the functional U → A(U),
  U : Ū^k = M^k(U) = V ... and it is a minimal orbit" (p.260; also p.256). The condition on V with B_3^{-1}ε_0 implies
  U_k(V) ∈ U_k(ε_0) (p.260). CMP 109 also uses, from the same paper: Sect. F (local coordinates U_k = exp iηH),
  Sect. G (multiscale minimisers U_n), and Proposition 9 / (190) (exponential decay of δH/δB, rate δ_0). None is
  reproved in CMP 109.
  - **New tree-level consequence (conditional on the regularity half of L2, and [R56-fix] on L1e-(0.4) plus the √N
    norm conversion, since V = M^k(U_k(V)) uses Balaban's (0.4)).** If U_k(V) lies in the L1e domain, which
    is what (1.2) + Theorem 1 [15] assert, then Corollary A1-NA(k) (L6loc [S6]) gives
    A_coarse(V) ≤ e^{C_7F} A(U_k(V)), uniformly in k. Equivalently, the background's fine Wilson action is at least
    e^{-C_7F} times the coarse Wilson action of V. This is the gauge analogue of Dimock III Lemma 20 (fine action ≥
    c_0 × coarse action), with c_0 → 1 in d = 4. It does not touch existence, uniqueness or analyticity, which remain
    the import.

### L3. Fluctuation propagators uniform in small-field backgrounds

#### L3s. Scalar multi-scale covariance in SU(N) backgrounds: PROVEN-HERE (a strictly weaker analogue of Balaban's bound)
[R1-fix] This is a scalar, weaker analogue of Balaban's propagator bounds. Its constants are uniform in n = 1/ε. Scope:
- (a) Session 1 proved it for the *direct* axial average only. [S2] Corollary L3s' below extends it to both forms of the
  iterated average, which closes R3.1.
- (b) It covers scalar 0-forms only: no gauge fixing, any unitary representation. The gauge-field (1-form) analogue is
  L3g, which is OPEN, and session 2 found an obstruction there (L3g-ob).
- (c) It gives only L^2 operator-norm bounds on block-localised pieces. The pointwise kernel bound that follows,
  |G(x,y)| ≤ (2/m) ε^-4 e^{-μρ}, is not uniform. No derivative or Hölder bounds are proved.
- (d) The hypothesis "F small" holds for smooth backgrounds such as the minimisers U(V) of L2, not for typical Wilson
  configurations, where F ~ g/ε^2. *Applying* L3s therefore needs L2 and L1d (imported).
- (e) It is quantitative: for a = 1 it needs F < 1/3.

**Setting.**
- d = 4 and n ≥ 1, with spacing ε = 1/n. The torus is Λ = (εZ/TZ)^4, partitioned into unit cubes B, each with n^d
  sites.
- φ ∈ ℓ^2(Λ, C^N), with ⟨φ, ψ⟩ = ε^4 Σ_x φ_x^dag ψ_x. The proof uses only unitarity, so any unitary representation
  works.
- Root: c_B has offsets r_0 = ⌊(n-1)/2⌋, and r = ⌈(n-1)/2⌉ ≤ n/2 is the largest coordinate distance from the root.
  P(c → y) is the complete-axial transporter inside B.
- ⟨φ, -Δ_A φ⟩ = ε^2 Σ_{bonds b=(x,y)} |φ_x - U_b φ_y|^2.
- (Q_A φ)(B) = ε^4 Σ_{y∈B} P(c_B → y) φ_y, with ||Qφ||^2 = Σ_B |(Qφ)(B)|^2.
- H_A = -Δ_A + a Q_A^dag Q_A, with a > 0.
- F := max over plaquettes p inside the blocks of ||1 - U_p|| / ε^2 (operator norm).
- A_max := max over intra-block bonds of ||1 - U_b^ax|| / ε, where U^ax is the field in the complete axial gauge of
  each block.

**Claims.** Every constant is independent of n, T, N and of the background.
- (i) A_max ≤ (d-1) r ε F ≤ (d-1) F / 2.
- (ii) H_A ≥ m := min(2, a) - d A_max^2 ≥ min(2, a) - d (d-1)^2 F^2 / 4, which is min(2, a) - 9 F^2 in d = 4.
- (iii) Suppose m > 0 and μ ∈ (0, 1/ε] satisfies (CT) (1 - η) m - 1.55 d μ^2 - a (η + η^2) ≥ m/2, with
  η = e^μ - 1. Then for all subsets Δ, Δ' ⊂ Λ,
  ||1_Δ H_A^-1 1_Δ'|| ≤ (2/m) exp(-μ ρ_∞(Δ, Δ')),
  where ρ_∞ is the ℓ^∞ torus distance in physical units.

**Proof of (i).**
- Gauge transform by g(x) = P(c_B → x) on each block. The blocks partition Λ, so this is one gauge transformation. It
  makes every tree link equal to 1 and sends the non-tree link b = (x, x + e_μ) to the holonomy of the loop
  P(c → x) b P(c → x + e_μ)^dag.
- The two axial paths agree in coordinates 1, ..., μ-1. They differ by one step in coordinate μ, then run in parallel
  through coordinates μ+1, ..., d.
- So the loop bounds a ladder of Σ_{ν>μ} |x_ν - c_ν| ≤ (d-1) r plaquettes, each entering as a lasso (a conjugated
  plaquette).
- For unitaries, ||Π V_i - 1|| ≤ Σ ||V_i - 1||, and conjugation preserves the norm. Hence
  ||U_b^ax - 1|| ≤ (d-1) r ε^2 F. Divide by ε and use r ε ≤ 1/2. Bonds in the last direction μ = d are tree bonds. ∎

**Proof of (ii).**
- In the gauge of (i), H_A is unitarily equivalent to the operator with U → U^ax. Because P^ax = 1, Q_A becomes the
  plain block average Q_0. Dropping the inter-block bonds (each term ≥ 0):
  ⟨φ, H φ⟩ ≥ Σ_B [ ||∂_A φ||_B^2 + a |Q_0 φ(B)|^2 ], with ||∂_A φ||_B^2 = ε^2 Σ_{b⊂B} |φ_x - U_b^ax φ_y|^2.
- **Step 1.** Split (φ_x - U φ_y)/ε = (φ_x - φ_y)/ε - (U - 1) φ_y / ε. The triangle inequality in ℓ^2(bonds) gives
  ||∂_A φ||_B ≥ ||∂φ||_B - A_max √d ||φ||_B, since each site is the forward end of at most d intra-block bonds.
  Then (x - y)^2 ≥ x^2/2 - y^2 (or the right side is negative) gives
  ||∂_A φ||_B^2 ≥ (1/2) ||∂φ||_B^2 - d A_max^2 ||φ||_B^2.
- **Step 2 (Poincaré, eq. P).** ||φ||_B^2 ≤ (1/4) ||∂φ||_B^2 + |Q_0 φ(B)|^2.
  - The Neumann grid Laplacian on {0, ..., n-1}^d with spacing ε has eigenvalues Σ_i (4/ε^2) sin^2(π k_i / (2n)),
    with cosine eigenvectors.
  - For k ≠ 0 the eigenvalue is at least (4/ε^2) sin^2(π/(2n)) ≥ (4/ε^2)(1/n)^2 = 4, using sin x ≥ 2x/π on [0, π/2].
  - Decompose φ = φ̄ + φ^⊥ with φ̄ the block mean, which equals Q_0 φ(B) because the block volume is 1. Then
    ||φ̄||_B^2 = |Q_0 φ|^2 and ||φ^⊥||^2 ≤ (1/4) ⟨φ^⊥, -Δ_N φ^⊥⟩ = (1/4) ||∂φ||_B^2. The cross terms vanish.
- **Step 3.** (1/2) x + a y ≥ min(2, a) (x/4 + y) ≥ min(2, a) ||φ||_B^2. Subtract d A_max^2 ||φ||_B^2 and sum over B. ∎

**Proof of (iii) (Combes-Thomas, in the form uniform in ε).**
- Let f(x) = ρ_∞(x, Δ'), which is 1-Lipschitz, and H_μ = e^{μf} H e^{-μf}.
- **Kinetic part.** For a bond, with z = φ_x^dag U φ_y and t = μ(f_x - f_y), |t| ≤ με ≤ 1, the off-diagonal terms give
  real part -2 cosh(t) Re z. Compared with t = 0, the change is ≥ -2 (cosh t - 1) |z| ≥ -(cosh t - 1)(|φ_x|^2 + |φ_y|^2).
  Summing over the 2d bonds at each site, the kinetic real part is
  ≥ ⟨φ, -Δ_A φ⟩ - 2d (cosh(με) - 1) ε^-2 ||φ||^2 ≥ ⟨φ, -Δ_A φ⟩ - d cosh(1) μ^2 ||φ||^2.
- **Block part.** In block B, write e^{±μ f(y)} = e^{±μ f(c_B)} (1 + s_±(y)), with |s_±| ≤ e^{μ/2} - 1 ≤ η. Let
  w = Q_A φ(B) and r_± = ε^4 Σ_y P s_± φ_y. Then |r_±| ≤ η ||φ||_B (Cauchy-Schwarz, block volume 1), and
  ⟨Q e^{μf} φ, Q e^{-μf} φ⟩_B = ⟨w + r_+, w + r_-⟩. Its real part is
  ≥ |w|^2 - 2η |w| ||φ||_B - η^2 ||φ||_B^2 ≥ (1 - η) |w|^2 - (η + η^2) ||φ||_B^2.
- **Combine.** Re ⟨φ, H_μ φ⟩ ≥ (1 - η) ⟨φ, H φ⟩ - [1.55 d μ^2 + a (η + η^2)] ||φ||^2 ≥ (m/2) ||φ||^2 under (CT).
  The numerical range then gives ||H_μ^-1|| ≤ 2/m.
- Finally 1_Δ H^-1 1_Δ' = (1_Δ e^{-μf}) H_μ^-1 (e^{μf} 1_Δ'), with ||1_Δ e^{-μf}|| ≤ e^{-μ ρ_∞(Δ, Δ')} and
  e^{μf} 1_Δ' = 1_Δ'. ∎

**Check c3.**
- n = 1, 2, 3, i.e. ε = 1, 1/2, 1/3, with smooth and rough SU(2) backgrounds at F = 0.1-0.3 and a large rough field.
  (i) and (ii) hold in every case.
- The free gap is exactly 1 = min(2, a) for a = 1: (P) is sharp on constants.
- The spectrum is gauge invariant.
- (iii) on n = 2, T = 4, F = 0.2: m_lb = 0.931, proven μ = 0.147. The block-block norms are ≤ 0.038 × the bound. The
  measured decay rate is 1.78 per unit length.

**Remark R3.1 (perturbed transports): PROVEN-HERE.** [R2-fix: this is the session-1 remark promoted to a counted item,
not new session-2 work.] Suppose Q' uses unitary transports V'_y with
||V'_y - P(c → y)|| ≤ θ for all y.
- Then |Q' φ| ≥ |Q_A φ| - θ ||φ||_B, by Cauchy-Schwarz with block volume 1. So a|Q'φ|^2 ≥ (a/2)|Q_A φ|^2 - a θ^2 ||φ||_B^2.
- Step 3 with a/2 gives H' ≥ m' := min(2, a/2) - d A_max^2 - a θ^2.
- (iii) holds verbatim with m' in place of m. The block part used only unitarity of the transports and Cauchy-Schwarz.

**Corollary L3s'. [S2] Iterated scalar averaging: PROVEN-HERE (closes the session-1 C_path obligation).**
The iterated scalar average is Q_k φ(B) = ε^d Σ_y W_y φ_y. Each y has a unique ancestor chain
c_B = c^(0) → c^(1)(y) → ... → c^(k)(y) = y, and W_y is the product of stage transports along it. Stage i is a
resolution-i axial path inside the level-(i-1) block. Two versions:
- **(I) Stage paths realised by fine links: θ_I ≤ C_path F, with C_path = d(d-1)/4 (= 3 in d = 4), for every L and k.**
  - Proof: in the unit-block axial gauge of L3s(i), ||W_y - P(c → y)|| = ||W^ax_y - 1||.
  - The composite path has physical length < d/2: per coordinate and per stage at most ((L-1)/2) L^-i, and summing over
    i gives < 1/2.
  - So it has < d/(2ε) fine bonds, each with ||U^ax_b - 1|| ≤ (d-1) ε F / 2 by L3s(i). Multiply. ∎
- **(II) Stage transports by the averaged fields V^(i) (Balaban's natural choice): θ_II ≤ [d(d-1)/4 + d C_δ/(2(L+1))] F.**
  - This holds under the hypotheses of L1e (L ≥ 9 in d = 4, F ≤ F_0).
  - Proof: compare with (I) link by link. Stage i has ≤ d(L-1)/2 links, each within C_δ s_i^2 F of its S, by L1e.
    Then Σ_{i≥1} d((L-1)/2) C_δ L^-2i = d C_δ / (2(L+1)). ∎
- **Consequence.** H' = -Δ_A + a Q_k^† Q_k ≥ min(2, a/2) - 9F^2 - a C_path'^2 F^2 in d = 4, and (iii) holds with this
  gap. Both are uniform in k.
- **Check c5(P).** Measured θ_I/F and θ_II/F are 0.01-0.08, against the bounds 0.5 (d = 2), 1.5 (d = 3) and 3 (d = 4).

**Scope.** L3s is scalar and has no gauge fixing. Balaban's operator acts on 1-forms. See L3g.

#### L3g. Gauge-field fluctuation operator: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** The covariance (Δ_k,A + a Q_k^dag Q_k)^-1 on Lie-algebra-valued 1-forms, in the
  background L2 with Balaban's gauge fixing, has uniform exponential decay and uniform Hölder/derivative bounds. It has
  a random-walk expansion analytic in the background.
- **Sources.** CMP 95 (1984) 17-40 [v]; CMP 96 (1984) 223-250 [v]; CMP 99 (1985) 389-434 [v].
- **Re-verification route (the L3s method).**
  - (a) A Hodge-Poincaré inequality on unit blocks:
    ||A||_B^2 ≤ C_H (||dA||_B^2 + ||d^* A||_B^2) + |Q_0 A|^2, uniform in ε. This is a discrete de Rham/Poincaré
    statement on a cube, a finite matrix problem for each n, and needs a uniform-in-n proof.
  - (b) The Weitzenböck curvature term ad F is bounded by F under the small-field condition, so it shifts the gap by
    O(F).
  - (c) Combes-Thomas exactly as in (iii).
  - (d) Derivative bounds, which do not follow from (iii) and need a separate local-regularity argument.
- (a) and (d) are the open sub-estimates.
- **[S5]** Abelian analogue [read-skim]: 1512.04373 Lemmas 6, 9, 11 (p.24, 29, 31): random-walk expansions on M-blocks
  for the Landau-gauge Green's function, the minimiser and C_k, C_k^{1/2}, with decay Ce^{-γd}; proofs sketched, citing
  CMP 95, 96, 99, 116. In QED the gauge covariance is background independent, so the background-dependence of L3g is
  not covered. Status unchanged.
- **[S6] What CMP 109 uses from L3g, and its gauge fixing [read].** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - Inputs it cites:
    - the operators H_{1,j} and Δ_1 ("defined in Sect. D [13]", CMP 99:389-434);
    - the fluctuation covariance C^{(k)} = (C*Δ^{(k)}C)^{-1} on {Q̃B = 0}, built from (3.156) [13] with the δ gauge
      fixing replaced by the exponential one (p.267-268);
    - Δ_j from (1.66) of CMP 95 (p.291);
    - the exponential decay of δH/δB, Proposition 9 (190) of CMP 102.
    None is reproved.
  - **Gauge fixing, relevant to L3g-ob.** The fluctuation integral carries the block constraint δ(Q̃B') (sharp, (0.17),
    (1.4)) together with a Euclidean-invariant **exponential block-axial gauge on the order-averaged contour variables**,
    exp(-(1/g_k²)Σ_{y,x≠y}[1 - Re tr U(y,x)]) ((0.14), (0.17); U(y,x) as in (0.11)). The estimates use the Landau
    gauge, reached by the transformation u_k of CMP 99:75-102 (p.265).
  - Linearised, the axial term penalises every averaged root-to-x path integral, which is a strictly stronger
    condition than our slice h(A) = 0 (L3g(a)-slice). This confirms L3g-ob's conclusion that a Q-adapted gauge fixing
    absorbs the root (point-source) part. Whether Balaban's combination has a uniform gap is the content of CMP 99:389,
    [not-read].

**L3g(a)-block. [S2] Block Hodge-Poincaré inequality, absolute boundary conditions: PROVEN-HERE.**
- **Statement.** On the bonds of a unit block {0, ..., n-1}^d with spacing ε = 1/n, let d_B be the block-restricted
  exterior derivative and d_B^* its adjoint (Neumann, i.e. absolute). For R- or Lie-algebra-valued 1-forms A:
  ||A||_B^2 ≤ (1/λ_n) (||d_B A||_B^2 + ||d_B^* A||_B^2), with λ_n = 4n^2 sin^2(π/(2n)) ∈ [4, π^2).
  No averaging term is needed.
- **Proof.**
  - The block's cubical cochain complex is the graded tensor product of d copies of the 1D path complex
    C^0 = R^n → C^1 = R^{n-1}, with the derivative scaled by 1/ε and uniform weights.
  - For graded tensor products, the mixed terms d_i d_j^* + d_j^* d_i (i ≠ j) vanish. So the Hodge Laplacian is
    Δ = Σ_i 1 ⊗ ... ⊗ Δ^(i) ⊗ ... ⊗ 1, each factor acting in its own degree.
  - A 1-form component in direction μ lies in C^1_μ ⊗ (⊗_{ν≠μ} C^0_ν). Its spectrum is λ^(1)_{k_μ} + Σ_{ν≠μ} λ^(0)_{k_ν}.
  - In 1D, the nonzero spectra of d d^* (on C^1) and d^* d (on C^0) coincide: (4/ε^2) sin^2(πk/(2n)), for k = 1, ..., n-1
    on C^1 and k = 0, ..., n-1 on C^0.
  - So the minimum is (4/ε^2) sin^2(π/(2n)) = λ_n ≥ 4, by sin x ≥ 2x/π. ∎
- **Check c6(A).** λ_min equals the formula to 1e-8 for d = 2, 3, 4 and n ≤ 8.
- **Why this does not close L3g.** Unlike ||dφ||^2, the global ||d^* A||^2 is a sum over *sites* of combinations that
  include inter-block bonds. It does not split as Σ_B ||d_B^* A_B||^2, so the L3s block-dropping step fails for the
  gauge-fixing term. The global gap must be obtained another way.

**L3g-ob. [S2] Obstruction for S4's complete-axial contours: OPEN (heuristic argument plus numerical confirmation; not
proven).**
- **Mechanism.** The linearised S4 average (L1c) is (QA)(X, μ) = n^-d Σ_y ∫_{Γ_y} A. All the axial legs out of the root
  c_X start along the coordinate-1 line through c_X. After averaging over y, Q contains a line functional
  ℓ_X(A_1) = ∫ w(x_1) A_1(x_1, c_2, ..., c_d) dx_1 with w = O(1). It enters as f(X) - f(X + e_μ), with f(X) = ℓ_X(A_1).
- **Size.** A line has zero H^1-capacity in d = 4 (codimension 3). So ||ℓ||^2_{H^-1} ~ n: a tube test function of
  radius ε has H^1 energy ~ 4πε and line integral O(1). In d = 3 it is ~ log n; in d = 2 it is bounded.
  - c6(B') measures ||Q_row||^2_{H^-1} = 0.196, 0.261, 0.334 at n = 3, 5, 7 (d = 4). The excess over the straight-leg
    part is 0.097, 0.167, 0.242, about 0.034 n, so linear.
  - The same quantity is 0.214 → 0.236 (d = 3, n = 3 to 15, log-like) and constant at 0.307 (d = 2). The straight-leg
    part alone is bounded in every d.
- **Heuristic consequence (not proven).** In Feynman gauge, M = d^*d + dd^* + aQ^†Q has no gap uniform in (n, T) in
  d = 4.
  - Trial A = dφ + σ, with φ of wave number k and σ = Σ_X φ(c_X) τ_X. Here τ_X are cheap tube profiles with
    ℓ_X(τ_X) = 1, which cancel the coarse gradient in QA.
  - The Rayleigh quotient is ≈ k^2 + C/(n k^2), so inf_T λ_min ≲ 2 (C/n)^{1/2}. This needs T ≳ n^{1/4}.
  - On the T = 2 torus of c6 the only low modes are the constants, which are exact eigenvectors with eigenvalue a
    (c6(B)). Their coarse "gradient" cannot be cancelled on a torus, so the effect is invisible at T = 2.
  - The cross-term estimates are not written out. Status: heuristic.
- **Gauge artifact, recorded so that it is not misread.** c6(C) restricts to the complete-axial gauge inside blocks
  without fixing the residual coarse gauge. Then λ_min ≈ 0.95 a/n even in d = 2. This comes from coarse pure-gauge modes
  on the inter-block faces (||A||^2 ~ n, |QA|^2 ~ 1, dA = 0), not from a coercivity failure.
- **What it means.** The scalar L3s is unaffected: its transports are unitary multipliers, not linearised line
  integrals. For the gauge field, a uniform L^2 gap needs one of:
  - contours spread so that each averaging functional is uniformly in H^-1 (the root funnel is the only problem, since
    the straight-leg part is fine);
  - a gauge fixing under which the funnel terms vanish *together with* a coarse gauge fixing;
  - Balaban's own construction, whose exact contour and gauge choices remain [unverified-exact-statement].
- **Caveat on spreading (heuristic).** Spreading cannot fully cure this. Any root-based covariant average has a
  linearised current J with div J = δ_{c_X} - δ_{c_Y}. Its gradient part has |Ĵ|^2/k^2 ~ k^-4 at large k, so
  ||J||^2_{H^-1} ≥ c log n in d = 4, whatever the contours. Equivalently, on pure gauge A = dφ, QA evaluates φ at points,
  and in d = 4 point evaluation is log-unbounded on H^2.
  - So a uniform Feynman-gauge L^2 gap needs a gauge fixing adapted to Q, one that absorbs the point-source part.
  - My unverified guess is that this is Balaban's choice [unverified-exact-statement]. The line part (~n) can be removed
    by spreading; the log part needs the gauge.
- **[S2] Literature cross-check: Dimock, "Covariant axial gauge", arXiv:1410.2798 [v-abs + body via a summarising fetch;
  data only].** This is an abelian treatment following Balaban.
  - [R2-fix] REVIEW_S2 read the abstract and HTML body (published: Lett. Math. Phys. 2015, DOI
    10.1007/s11005-015-0763-0). It is abelian, single-scale, mainly d = 3, so the weight is L^-d (not L^-4). Q sums A
    over paths parallel to the coarse bond, one per fine site, with no centre legs.
  - Covariance is Q ∂λ = ∂ Q λ with the *averaged* scalar gauge function, not a root value.
  - The centre (tree) paths appear only in the gauge-fixing operator τ, averaged over the d! coordinate orders. The gauge
    fixing is δ(τA); Q_k λ = 0 constrains the Faddeev-Popov parameter; Landau uses δ(R_k δ𝒜) and Feynman uses
    exp(-½ α^-1 ⟨δ𝒜, R_k δ𝒜⟩). Balaban is reported to have "averaged over various trees
    to regain the covariance" and to have used exponential gauge fixing in the YM papers.
  - Consistency with L3g-ob: the straight-leg, averaged-gauge form is precisely the part c6 found uniformly H^-1
    bounded, and the Q_k λ = 0 constraint is a Q-adapted gauge fixing of the kind L3g-ob says is needed.
  - [R2-fix] **What carries over to SU(N) and what does not.**
    - Does NOT carry over: the covariance Q∂λ = ∂Qλ with a block-*averaged* gauge function. A nonabelian covariant map
      whose coarse gauge group acts at points (here the roots c_X) necessarily linearises to root covariance,
      Q(dλ) = λ(c_Y) - λ(c_X). So the point-source (log) part of L3g-ob is unavoidable for any such map, by the caveat
      above. The session-2 phrase "revise S4 toward averaged gauge functions" is withdrawn for SU(N).
    - Carries over: straight legs (or spread funnels), which remove the ~n line part, and a Q-adapted gauge term R_k in
      place of the plain dd^*. [S3] L3g(a)-slice below makes this exact at the linearised level: Q_root = Q_str - d h.
    - Order averaging: in Dimock it acts on τ (the gauge fixing), not on Q. For L8b it is an analogy, not the repair.
      The S4' order-averaged map of [S3] has to re-prove L1e and L9a' itself (done in S4' below).
  - So the line part of the obstruction is specific to S4's complete-axial funnels; the point part is intrinsic to root
    covariance and is handled by the gauge slice, not by the averaging.
- **Revised L3g(a) target.** Prove the gap for M_Q = d^*d + (gauge term adapted to Q) + aQ^†Q, with spread contours,
  where the gauge term fixes the components of A that Q sees as point sources. The S4 contours plus the plain Feynman
  term are probably not the right object in d = 4.

**L3g(a)-glob. [S3] Global Hodge-Poincaré inequality for the straight-leg average (abelian, flat, linearised): PROVEN-HERE.**
- **Setting.** Fine torus Λ = (εZ / TZ)^d, ε = 1/n, T ≥ 2 an integer, unit blocks B(X), X ∈ (Z/TZ)^d. Real (or
  Lie-algebra-valued, componentwise) 1-forms A_μ(z) on the bonds (z, z + εe_μ); ⟨A, A'⟩ = ε^d Σ_{z,μ} A_μ(z)A'_μ(z).
  - Straight-leg average (Dimock-type): (Q_str A)(X, μ) = n^-d Σ_{x∈B(X)} ε Σ_{j=0}^{n-1} A_μ(x + jεe_μ), i.e. the block
    average of the unit-length straight line integrals from x to x + e_μ. ||Q_str A||^2 = Σ_{X,μ} |(Q_str A)(X, μ)|^2.
  - ⟨A, ΔA⟩ := ||dA||^2 + ||d^*A||^2.
- **Claim.** ||A||^2 ≤ 5 ⟨A, ΔA⟩ + 2 ||Q_str A||^2. Hence Δ + a Q_str^† Q_str ≥ min(1/5, a/2), uniformly in n, T and d.
- **Proof.**
  - (1) *Lattice Weitzenböck.* On the flat torus the forward and backward differences commute, so summation by parts gives
    ||dA||^2 + ||d^*A||^2 = Σ_{μ,ν} ||∂_ν A_μ||^2: the 1-form Laplacian is the scalar Laplacian on each component (check
    c9(A), exact). The problem splits into d scalar problems, one per component f = A_μ.
  - (2) *Density form.* (Q_str A)(X, μ) = ε^d Σ_z ω_X(z) f(z), with ω_X(z) = ε c(z_μ - X_μ n) on the slab
    S_X = B(X) ∪ B(X + e_μ) and 0 elsewhere, where c(t) = min(t + 1, 2n - 1 - t) for 0 ≤ t ≤ 2n - 2 (a tent along μ, a
    box across). Then ∫ω_X = ε^{d+1} n^{d-1} Σ_t c(t) = 1 and ω_X ≤ εn = 1. So ω_X is a probability density with
    ||ω_X||_∞ ≤ 1, and ||ω_X||_2^2 ≤ ||ω_X||_∞ ∫ω_X ≤ 1. (Check c9(B0).)
  - (3) *Slab Poincaré.* S_X is a Neumann grid of 2n × n^{d-1} sites, spacing ε, volume 2. Its first nonzero
    eigenvalue is min((4/ε^2) sin^2(π/(4n)), (4/ε^2) sin^2(π/(2n))) ≥ 4n^2 (1/(2n))^2 = 1 (sin x ≥ 2x/π). With f̄ the
    slab mean, ||f - f̄||^2_S ≤ ||∂f||^2_S (intra-slab bonds).
  - (4) *Averaging defect.* |ω(f) - f̄| = |∫ω (f - f̄)| ≤ ||ω||_2 ||f - f̄||_S ≤ ||f - f̄||_S. Then
    ||f||^2_S = 2|f̄|^2 + ||f - f̄||^2_S ≤ 4|ω(f)|^2 + 4|ω(f) - f̄|^2 + ||f - f̄||^2_S ≤ 4|ω(f)|^2 + 5||∂f||^2_S.
  - (5) *Covering.* For T ≥ 2 each fine point lies in exactly two slabs S_X (direction μ fixed), and each intra-slab bond in
    at most two. Summing (4) over X: 2||f||^2 ≤ 4 Σ_X |(Q_str A)(X, μ)|^2 + 10 ||∂f||^2. Sum over μ and use (1). ∎
- **Check c9(B)** (d = 2, 3, 4; n ≤ 16, 6, 5; T ≤ 8, 6, 4; a = 1, 0.2, 0.02): measured λ_min = a in every case (the
  constants are the minimisers at these sizes), above the bound min(1/5, a/2). These are instances, not uniformity.
- **Check c9(C).** ||ω||^2_{H^-1} = ω^T (Δ+1)^-1 ω in d = 4 is 0.110, 0.099, 0.096, 0.094, 0.093 at n = 2..6: bounded,
  where the root-based S4 linearisation grew like 0.034 n (c6(B')).
- **Scope.** Abelian, flat background, direct (one-level) average with n = L^k fine sites per block. The iterated
  composite of straight averages, and the nonabelian background-covariant version, are not covered (see L3g(a)-slice).

**L3g(a)-slice. [S3] The root-based average is the straight average up to a coarse exact 1-form dh(A) [R3-fix: not a
"coarse gauge transformation"; h depends on A, and the identity is linearised and abelian only: the nonabelian straight
average is not even covariant, so there is no nonlinear SU(N) analogue]; gap on a gauge slice (abelian, linearised):
the inequality on H_0 is PROVEN-HERE; its use as a fluctuation gap is CONDITIONAL on (FP), which is OPEN.**
- **Identity (exact).** For S4 or S4', with h(X) := avg_σ avg_{y∈B(X)} ∫_{P^σ(c_X → y)} A, the linearised average is
  Q_root A = Q_str A - d h, i.e. (Q_root A)(X, μ) = (Q_str A)(X, μ) - (h(X + e_μ) - h(X)).
  - Proof: ∫_{T^σ_y} A = ∫_{P^σ(c_X→y)} A + ∫_{S_y} A - ∫_{P^σ(c_Y→y+Le_μ)} A. Average over (σ, y). The last term averages
    to h(Y) because y ↦ y + Le_μ is a bijection B(X) → B(Y) and axial paths are translation covariant. ∎
  - Check c8(f): exact (error ≤ 2e-16) for U(1) small fields, where the S4/S4' map is exactly linear, for both S4' and S4.
- **What this explains.** The L3g-ob funnel terms are entirely in the coarse exact part d h (linearised, abelian). They never change the
  gauge-invariant content of Q (for instance its coarse curl dQ_root A = dQ_str A).
- **Slice.** H_0 := {A : h(A) = 0}. Every gauge orbit meets H_0: h(A + dλ) = h(A) + Q_0λ - λ(c), and the map
  λ ↦ Q_0λ - λ(c) is onto coarse scalars (take λ = s_X on B(X) minus its root, 0 at the root: the image is
  s_X(1 - n^-d)). On H_0, Q_root = Q_str, so by L3g(a)-glob
  ⟨A, (Δ + a Q_root^† Q_root) A⟩ ≥ min(1/5, a/2) ||A||^2 for all A ∈ H_0, uniformly in n, T.
- **Open (stated exactly).**
  - (FP) That the gauge-fixed fluctuation integral can be written with the δ(h) slice plus a Feynman term on the residual
    gauge group {λ : Q_0λ = λ(c)}, with a background-independent (abelian) or controlled (nonabelian) Faddeev-Popov
    factor. In the abelian case the factor is A-independent by linearity; this is plausible but not written out.
  - (NA) The nonabelian background version: covariant Weitzenböck with curvature terms of size O(F), a slab version of
    L3s(i) (axial gauge on 2-block slabs, A_max ≤ (d-1)F), and the R3.1 perturbation for transported densities. Each
    piece has an L3s analogue; the combination is not written.
  - (IT) Iterated straight averages: the composite density must stay a probability density with a uniform sup bound on
    an O(1) slab. Not checked.
- **Effect on L3g-ob.** L3g-ob stands as stated (plain Feynman gauge with the root-based Q has no uniform gap,
  heuristically), but it is now explained as a coarse exact-form artifact, and it is removed by the slice. [R3-fix] The
  revised L3g(a) target is met in the abelian linearised case CONDITIONAL on (FP): the slice gap uses Δ = d*d + dd* on
  top of δ(h), a double gauge fixing whose legitimacy is exactly (FP).

### L4. Small-field effective actions and the coupling flow
- **L4a. Structure: IMPORTED-NOT-YET-REVERIFIED.**
  - After k steps, on the small-field region the density is exp(-(1/g_k^2) S_W(V) - Σ_X E_k(X, V)), with polymer
    activities obeying |E_k(X)| ≤ C g_k^{?} e^{-κ d_X}. [The exponent and the norms are unverified.]
  - The coupling recursion, indexed by **resolution** j (finer = larger j), is 1/g_{j+1}^2 = 1/g_j^2 + β_j, with
    β_j → 2 b0 ln L. The coupling grows toward the IR, i.e. as j decreases. [R1-fix: session 1 indexed this by "steps" k,
    which gives the wrong sign if k counts coarse-graining steps.]
  - Sources: CMP 109 (1987) 249-301 [v]; CMP 116 (1988) 1-22 [v]; CMP 119 (1988) 243-285 [v].
  - **[S5]** d = 3 templates [read]: Dimock I Theorem 14 (p.23, eqs. 176-182) and QED Proposition 1 / Theorem 1
    (2009.01156 p.6-8, eqs. 29-30, 37-40). Same structure (density = exp(-action + polymer sum), normalised polymers,
    ||E_k(X)|| ≤ coupling^{1/4-} e^{-κ d_M(X)}), but super-renormalizable: no marginal coupling flow. The 4D content (the
    marginal coupling recursion, its β_j) is not covered. Status unchanged.
  - **[S6] CMP 109 read: L4a is split** (NOTES §9.4-9.8).
    - **L4a-form (IMPORTED-NOT-YET-REVERIFIED; exact statement now [read]).** Theorem 3 (p.264): there are constants
      κ_0, M(κ), γ, ε_0, ε_1, α_0, α_1 such that, if κ ≥ κ_0, M ≥ M(κ) and 0 < g_k ≤ γ for all k ≤ K, the small-field
      actions satisfy the inductive assumptions (1.1)-(1.22). These are:
      - the form (1.3);
      - E^{(j)} = Σ_{X∈D_j} E^{(j)}(X), analytic on U^c_j(X, α_0, α_1), with |E^{(j)}(X)| ≤ E_0 e^{-κd_j(X)} (1.18).
        There is NO positive power of g, so the session-1 placeholder "C g_k^{?}" was wrong in form;
      - gauge and Euclidean invariance.
      After the β-subtraction, the renormalised terms obey |V^{(j)}(X)| ≤ O(1)(L^jη)^{4+α} e^{-κd_j(X)} (0.29). This
      gives the k-uniform bulk bound (0.30).
      - **CMP 109 does not complete this proof.** The localisation and cluster expansion of (2.13) are deferred to
        "the next paper" (p.298), CMP 116 (1988) 1-22, "II. Cluster expansions" [v-crossref, not-read].
      - Its hypotheses, where they can be checked: G = SU(N) is compact, semisimple and in U(N); d = 4; L odd, but
        Balaban needs "L odd > 11", while our L1e needs L ≥ 9 and the checks use L = 3. **[R56-fix]** The torus side
        does NOT match: Balaban's torus has side 2L^m, ours (since session 4) has unit-lattice side 4L^M, and
        4L^M ≠ 2L^m for odd L. Whether his proofs are side-agnostic is [unverified].
      - The averaging hypothesis holds only up to the S4'/(0.4) pairing difference (L1d [S6]).
    - **L4a-flow (IMPORTED-NOT-YET-REVERIFIED; deferred by the source).** Theorem 2 (p.259) covers SU(2) only, "the
      restriction ... is superficial". For small γ and g there is a bare g_0(ε,g) with g_k ∈ ]0,γ], g_K = g, and
      1/g² + β(K - k) log L ≤ 1/g_k² ≤ 1/g² + β'(K - k) log L, with unspecified constants 0 < β ≤ β' (0.31). "A proof
      of this theorem ... will be given in a separate paper" [not-read].
      - **Correction:** PROOF.md's "β_j → 2b_0 ln L" is NOT stated in CMP 109. It is the perturbative expectation
        [inference]. CMP 109 gives only the two-sided logarithmic form.
      - The sign of (0.18) (1/g_0² = 1/g_1² + β_1, k counting coarse-graining steps) confirms the [R1-fix] convention
        of L4c, with j = K - k.
      - The E8.3/E7.0 corollaries need λ_K := 2N·β' log L below the λ_c of E8.3 (λ_c/λ_AF ≈ 6.1 for SU(2)). (0.31)
        alone does not give this, since β' is unspecified. They stay conditional on L4a-flow with β' < 6.1·2b_0.
    - **L4a-Π (the β-function as the coefficient of the transverse polarisation tensor): PROVEN-HERE [S6]**, below.
- **L4a-Π. [S6] Transverse structure of a gauge-invariant lattice polarisation tensor: PROVEN-HERE.** (A re-derivation
  of CMP 109 §5, (5.6)-(5.42), by a direct Taylor argument rather than Balaban's Laurent decomposition.)
  - **Setting.** Π_μν(z), z ∈ Z^d, d ≥ 2, real, with Σ_z e^{δ|z|}|Π_μν(z)| < ∞ for some δ > 0. It is the bond-bond
    kernel of a quadratic form, Π_μν(x - y) = Π(⟨x, x+e_μ⟩, ⟨y, y+e_ν⟩), extended to reversed bonds by oddness.
    Assume:
    - (S) symmetry, Π_μν(z) = Π_νμ(-z);
    - (H) hypercubic covariance, as induced by the action of the signed permutations on bonds, CMP 109 (5.4), (5.6),
      (5.7);
    - (G) transversality, Σ_μ Π_μν(x - y) evaluated against (dλ)_μ vanishes for all λ, CMP 109 (5.9).
    (G) holds when Π is the Hessian at 0 of a gauge-invariant functional. In CMP 109 it is derived from the Ward
    identity (4.15).
    **[R56-fix]** The scalar colour form (Π ∝ δ_ab, so that Π_μν is a single real kernel) is justified by CMP 109
    (1.21) [read, NOTES §9.4].
  - **Centred transform.** Π̃_μν(p) := Σ_z exp(-ip·(z + (e_μ - e_ν)/2)) Π_μν(z). This is the Fourier transform in the
    difference of bond midpoints. It is analytic in the strip |Im p| < δ.
  - **Claim.**
    Π̃_μν(p) = β (δ_μν Σ_κ s_κ² - s_μ s_ν) + R_μν(p), where s_κ = 2 sin(p_κ/2), R is analytic and R = O(|p|⁴), and
    β = Σ_z (z_1 + ½)(z_2 - ½) Π_12(z) = Σ_z z_1 z_2 Π_12(z) (CMP 109 (1.22)).
  - **Proof.**
    - (H) in midpoint coordinates. A coordinate reflection ε maps the midpoint of bond (x, μ) to the reflected
      midpoint, and multiplies the bond variable by ε_μ (orientation). Hence Π̃_μν(εp) = ε_μ ε_ν Π̃_μν(p).
      Permutations give Π̃_{πμ,πν}(πp) = Π̃_μν(p).
    - Reflecting all axes gives Π̃(-p) = Π̃(p). Reality gives Π̃(-p) = conj Π̃(p). So Π̃ is real and even, and its
      Taylor series at 0 has only even orders: Π̃ = A + Q(p) + O(p⁴), with A constant and Q quadratic.
    - **Order 0.** For μ ≠ ν, reflecting axis μ alone gives A_μν = -A_μν = 0. Permutations give A_μμ = a for all μ.
    - **Order 2.**
      - For μ ≠ ν, Q_μν is odd in p_μ, odd in p_ν and even in every other variable, so Q_μν = c p_μ p_ν, with c
        independent of (μ, ν) by permutations.
      - Q_μμ is even in each variable, so Q_μμ = b p_μ² + e Σ_{κ≠μ} p_κ².
    - **(G) in Fourier form.** (dλ)^_μ(p) = (e^{ip_μ} - 1)λ̂ = i s_μ e^{ip_μ/2}λ̂. Collecting the midpoint phases,
      (G) reads Σ_ν Π̃_μν(p) s_ν(p) = 0 for all p.
      - At order p: Σ_ν A_μν p_ν = a p_μ = 0, so a = 0.
      - At order p³ (using s_ν = p_ν + O(p³) and A = 0): c p_μ Σ_{ν≠μ} p_ν² + b p_μ³ + e p_μ Σ_{κ≠μ} p_κ² = 0 for all
        p. Hence b = 0 and c = -e.
    - So Q_μν(p) = e(δ_μν |p|² - p_μ p_ν). Set β := e = -c = -∂_1∂_2 Π̃_12(0) = Σ_z m_1 m_2 Π_12(z), with
      m = z + (e_1 - e_2)/2.
    - Replacing p by s(p) changes Q by O(p⁴). R := Π̃ - β(δ s² - s s^T) is analytic and O(p⁴).
    - Equality of the centred and uncentred second moments: (z_1 + ½)(z_2 - ½) = z_1 z_2 + ½(z_2 - z_1) - ¼. Here
      Σ_z Π_12 = Π̂_12(0) = 0. The first moments vanish because the uncentred Π̂_12 = e^{+i(p_1-p_2)/2}Π̃_12 [R56-fix: sign of the phase; harmless since Π̃_12 = O(p²)] =
      -βp_1p_2 + O(p³) has no linear term. ∎
  - **What it re-verifies, and what it does not.** It re-verifies the load-bearing algebra of CMP 109 §5: the marginal
    part of any symmetric, gauge-invariant quadratic local functional is a multiple β of the lattice Wilson quadratic
    form, and β is the mixed second moment (1.22). It does not compute β_j for the actual RG step, i.e. Π from the
    fluctuation integral (2.13), nor show that β_j → 2b_0 log L. That is L4a-flow, plus the one-loop identification of
    L4b.
  - **Check c17(A)** (8/8 with part B; 0.7 s, 39 MB; first run). Functionals: the plaquette action, plaquettes +
    1×2 rectangles, and three random closed lattice loops symmetrised over the 384-element hypercubic group (d = 4).
    - Π̃(0) = 0 and the transversality hold to ≤ 5e-14.
    - The centred, uncentred (1.22) and diagonal extractions of β agree to 1e-12. Plaquette c_0 = 1 gives β = 1; with
      rectangles c_1 = -1/12, β = c_0 + 8c_1 = 1/3 exactly.
    - |R(2t)|/|R(t)| = 16.00, i.e. R = O(p⁴); R ≡ 0 for the pure plaquette.
    - These are instances; the proof above is general.
- **L4b. One-loop coefficient b0 = 11N/(48π^2): IMPORTED-AND-REVERIFIED.**
  - **Hypotheses (imported).**
    - The Seeley-DeWitt coefficient a2 = tr[(1/12) Ω_{μν} Ω_{μν} + (1/2) E^2] for -(D^2 + E) in 4D (Vassilevich,
      Phys. Rept. 388 (2003) 279-360 [v]).
    - The background-field Feynman-gauge fluctuation operator -D^2 δ_{μν} + 2i ad F_{μν}, with adjoint ghosts -D^2
      [v-R1: Abbott, NPB 185 (1981) 189-203].
  - **Derivation (here).**
    - (1/2) a2_vec - a2_gh = [(1/2)(4·(1/12)·(-C_A) + (1/2)·4 C_A) + (1/12) C_A] F^a F^a = (11/12) C_A F^a F^a.
    - With UV proper-time cutoff Λ and IR scale μ: Γ ⊃ -(16π^2)^-1 ln(Λ^2/μ^2)(11/12) C_A ∫ F^a F^a.
    - Against S = (4g^2)^-1 ∫ F^a F^a this gives 1/g^2(μ) = 1/g_0^2 - (11/3) C_A (16π^2)^-1 ln(Λ^2/μ^2), so
      d(1/g^2)/d ln μ = 2 b0 with b0 = 11 C_A/(48π^2) and C_A = N.
    - The sign gives infrared growth (asymptotic freedom).
  - **Check c2(A).** Exact to 1e-12 for SU(2), SU(3) and SU(4).
  - **Lattice universality of the two log coefficients that enter (c2(B)):**
    - E^2: the slope of ∫_BZ (ω + m^2)^-2 against ln(1/m^2) is 1.0056 → 1.0017 times 1/(16π^2).
    - Ω^2: unit-charge lattice scalar in constant flux on a 64^2 torus; the slope is 0.94-1.10 times 1/(96π^2). This
      is a finite diagnostic, finite-size limited.
  - **Not covered.** That Balaban's lattice β_k → 2 b0 ln L is part of L4a, not reverified.
- **L4c. AF recursion arithmetic: PROVEN-HERE.**
  - Statement: let 1/g_{j+1}^2 = 1/g_j^2 + β_j, with |β_j - β| ≤ C g_j^2, β = 2 b0 ln L > 0, and C g_0^2 ≤ β/2. Then:
    - (a) 1/g_0^2 + jβ/2 ≤ 1/g_j^2 ≤ 1/g_0^2 + 3jβ/2;
    - (b) Σ_j g_j^{2+δ} < ∞ for every δ > 0;
    - (c) Σ_j g_j^2 = ∞.
  - Proof: by induction, g_j ≤ g_0, so β/2 ≤ β_j ≤ 3β/2; sum to get (a). (b) and (c) follow by comparison with
    Σ j^{-1-δ/2} and Σ j^-1. ∎
  - **Consequence used in L7b (heuristic, [R1-fix] softened):** per-scale error *bounds* of order g_j^2 are not
    summable. So a convergence proof by summing absolute per-scale bounds needs geometric decay L^{-κ(j-m)}, or
    O(g_j^{2+δ}). O(g^2) errors could still telescope or cancel; this is not excluded.

### L5. Large-field R-operation: IMPORTED-NOT-YET-REVERIFIED
- **Sources.** CMP 122 (1989) 175-202 [v-abs: "the basic step of the R operation"]; CMP 122 (1989) 355-392 [v].
- **Content (paraphrase).** Large-field regions are suppressed by exp(-c p(g_k)^2 / g_k^2) per unit block, with
  p(g) = (-log g)^p, and are localised and exponentiated.
- **[S5]** The R-operation is in NO open exposition: Dimock II p.31 Remark 3 [read] ("This difficult step is not
  necessary for this model"); none in QED either. What Dimock does have [read] is the per-level large-field factor
  without recycling: e^{-c_2 p_j^2} per M-cube in his normalisation (III Lemma 13, eq. 166) and e^{-p_j} per cube in QED
  (Lemma 23, eq. 471), with no 1/g^2. The "/ g_k^2" in the paraphrase above is therefore convention-dependent and
  unverified. Status unchanged; L5 can only be re-verified from CMP 122 (1989) 175-202 and 355-392.
- **[S6]** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - CMP 109 contains no large-field estimate ("the simplifying assumption that integrals are restricted to small
    fields", p.250).
  - Its small-field thresholds are:
    - fixed ε_0 on the background curvature (1.2);
    - fixed ε_1 on the dimensionless fluctuation B' ((2.9); alternatively g_kε_1/γ_k).
    So the excluded fluctuations cost ~ε_1²/g_k² in action. This is not the p(g)² form of the old paraphrase, whose
    "/g_k²" question is therefore moot for CMP 109's own cut.
  - CMP 122 abstracts [read-abs, OSTI; NOTES §10]: Part I "construct[s] the renormalization operation of the
    expressions connected with the large field regions"; Part II completes "the proof of the ultraviolet stability of
    four-dimensional pure gauge field theories".
  - **Why L5 is load-bearing in d = 4 and not in d = 3: Proposition LF-count (L6loc [S6], PROVEN-HERE).** The
    unrenormalised per-level large-field count of Dimock's template diverges along any flow of the form (0.31) whenever
    the excluded configurations cost a/g_k² with aβ' ≤ 4. **[R56-fix]** In Balaban's normalisation this covers every
    ε_1 below an explicit bound, ε_1 ≲ (8/(||Δ||β'_B))^{1/2} with β'_B ≈ 4Nb_0 [inference, conditional on the
    one-loop rate and on L4a-flow; not "every small-field threshold" unconditionally]. So L5 must
    deliver *renormalised* large-field contributions, with per-level weights summable against L^{4(K-k)}. No open
    source states such a bound (NOTES §10).
- **[S7] One-cube R-operation: target pre-stated in RTARGET.md (written before the derivation), attacked in d = 2.**
  Status of L5 unchanged: IMPORTED-NOT-YET-REVERIFIED. New: Proposition R2D-iso (PROVEN-HERE) and the OPEN item R4D-iso.
  - **d = 2 has the same wall (RTARGET §0).** LF-count's arithmetic with N_k ∝ L^{2(K-k)} gives divergence whenever
    aβ' ≤ 2. With the one-loop O(N) rate β' ≈ (N-2)/(2π) [m; inference for the lattice rate] and a single-bond cut
    (cost a = ε_1²/2 ≤ 2), every threshold is in the divergent window for 3 ≤ N ≤ 8. Sanity check: the O(3) instanton
    (a = 4π) gives aβ' = 2 = d exactly, i.e. the known log-divergent small-instanton gas of the lattice O(3) model [m].
  - **Literature correction.** Balaban CMP 198 (1998) 493-534 is the large-field operation of his LOW-TEMPERATURE
    N-vector series (d ≥ 3, an infrared problem) [read-abs, Rutgers record; search snippets for CMP 167/182/196], not a
    2D UV construction. The full-lattice UV analysis of the 2D O(N) model was open as of 1999, "so far only performed in
    the hierarchical case" (Kopper, CMP 202 (1999) 89-126, math-ph/9902020, introduction [read-skim]). So there is no
    open (or known closed) 2D template to compare with; d = 2 is a testbed, not a solved case.
  - **Proposition R2D-iso (one-cube, one-step renormalised large-field bound, isolated cube, d = 2): PROVEN-HERE [S7].**
    - *Setting* (RTARGET §1): 2D O(N), N ≥ 2; block □ of L×L sites, L odd, centred at 0; exterior neighbours Γ (4L
      sites) frozen at m_y; soft block-spin term (κ/2g²)|Φ - L^{-2}Σ_{x∈□}n_x|²; interior-bond cut
      χ = Π 1{|n_x - n_x'| < ε_1}; ρ := ∫(1-χ)e^{-S}dσ / ∫χe^{-S}dσ. Background family m_y(s) = n(sy),
      Φ(s) = L^{-2}Σ_{x∈□}n(sx), with n : R² → S^{N-1}, |∂^α n| ≤ 1 for 1 ≤ |α| ≤ 4. B := the nearest-neighbour bonds of
      □ ∪ Γ (D_4- and point-reflection symmetric, b bonds per direction), A_B(m) := Σ_B(1 - m_y·m_y').
    - *Claim* = (R2D) as pre-stated: for every a < ε_1²/4 there are C, s_0, g_0 depending on (L, N, κ, ε_1, a) only with
      ρ(s) = ρ_0(g) + δβ(g)A_B(m(s)) + R(s), 0 ≤ ρ_0 ≤ Ce^{-a/g²}, |δβ| ≤ Ce^{-a/g²} (both background-independent),
      |R(s)| ≤ Ce^{-a/g²}s⁴, for all g ≤ g_0, all n, all |s| ≤ s_0. The same holds for log(1 + ρ).
    - *Proof.*
      1. **Size.** Numerator: on {χ = 0} some interior bond has 1 - n_x·n_x' = ½|n_x - n_x'|² ≥ ε_1²/2, and every term of
         S is ≥ 0, so the numerator is ≤ e^{-ε_1²/(2g²)} (σ has mass 1). Denominator: restrict to the caps
         |n_x - n(0)| ≤ rg, r := ε_1/4, g ≤ 1; there χ = 1. Using |n(sy) - n(0)| ≤ s|y|_1 ≤ sL and
         |Φ(s) - n(0)| ≤ sL, and (u + v)² ≤ 2u² + 2v², S ≤ C_0 + Bs²/g² on the caps, with C_0 = C_0(L, κ, ε_1) and
         B := (4L + κ)L². Cap measures are ≥ c_N(rg)^{N-1}. Hence ρ(s) ≤ C_1 g^{-(N-1)L²} e^{-(ε_1²/2 - Bs²)/g²}, and
         for |s| ≤ s_0 := ε_1/(2√B): ρ(s) ≤ C_1 g^{-(N-1)L²} e^{-ε_1²/(4g²)}. (s_0 is g-independent: (F4) avoided.)
      2. **Derivatives.** χ does not depend on s; S does, polynomially through m(s) and Φ(s). Since
         ∂_s^j(n_x·m_y(s)) = n_x·(y·∇)^j n(sy), |∂_s^j S| ≤ Λ_j/g² with Λ_j ≤ (4L + 4κ)(2L)^j. By Faà di Bruno,
         |∂_s^q e^{-S}| ≤ B_q(Λ/g²)^q e^{-S} for g ≤ 1, with Λ := (4L + 4κ)2L. The integrands are ≥ 0 and the
         indicator is s-independent, so |Num^{(q)}| ≤ B_q(Λ/g²)^q Num, |Den^{(q)}| ≤ B_q(Λ/g²)^q Den, and by the
         quotient rule |ρ^{(q)}(s)| ≤ B'_q(Λ/g²)^q ρ(s). (No analyticity is needed: (F1) avoided, because the soft
         constraint is polynomial in Φ.)
      3. **Evenness.** The point reflection ι : x ↦ -x maps □, Γ, the interior bonds and B to themselves and preserves
         dσ, S's form and χ. Since m_{-y}(s) = m_y(-s) and Φ(-s) = Φ(s) (re-index x ↦ -x), ρ(-s) = ρ(s). (The family
         with s < 0 is the family of n∘(-1), which obeys the same bounds.) So ρ'(0) = ρ'''(0) = 0, and Taylor gives
         ρ(s) = ρ(0) + ½ρ''(0)s² + R_4(s), |R_4| ≤ (s⁴/24)sup_{|σ|≤s}|ρ^{(4)}(σ)|. ((F2) avoided.)
      4. **Vacuum part.** At s = 0 the background is constant, m_y = Φ = n(0). Rotating the integration variables
         (σ is O(N)-invariant), ρ(0) = ρ_0(g) does not depend on n(0).
      5. **Marginal part.** ρ is a smooth O(N)-invariant function of (m, Φ) ∈ (R^N)^Γ × R^N (S is polynomial in m, Φ).
         At the constant point e := n(0), the stabiliser O(N-1) forces the gradient components to be ∥ e (γ_y e, γ_Φ e)
         and the Hessian on e^⊥-components to be h_{yy'}·(u·v). Put u_μ := ∂_μn(0) ∈ e^⊥ and
         w_{μν} := ∂_μ∂_νn(0), with e·w_{μν} = -u_μ·u_ν (differentiate n·n = 1 twice). Then m'_y(0) = Σ_μ y_μu_μ,
         Φ'(0) = 0 (Σ_{x∈□}x = 0), m''_y(0) = Σ y_μy_νw_{μν}, and
         ρ''(0) = Σ_{μν}T_{μν} u_μ·u_ν, T_{μν} := Σ_{y,y'}h_{yy'}y_μy'_ν - Σ_yγ_y y_μy_ν - γ_Φ L^{-2}Σ_{x∈□}x_μx_ν.
         T depends on g and the fixed data only. The square's symmetry group D_4 maps the geometry to itself, so
         ρ''(0)[n∘R] = ρ''(0)[n], i.e. T = RTR^T for R ∈ D_4. D_4 acts irreducibly on R², so T = c(g)·1:
         ρ''(0) = c Σ_μ|∂_μn(0)|². ((F3) avoided: one marginal operator.)
      6. **Identification with A_B.** A_B(m(s)) = ½Σ_B|n(sy) - n(sy')|² is even in s (B is ι-symmetric), so
         A_B(m(s)) = (s²/2)·bΣ_μ|∂_μn(0)|² + R_B(s) with |R_B| ≤ C_B s⁴ (fourth derivatives ≤ 1). Put δβ := c/b and
         R := R_4 - δβR_B.
      7. **Bounds.** |c| ≤ |ρ''(0)| for a test background with |∂_1n(0)| = 1, ∂_2n(0) = 0, so |c| ≤ B'_2(Λ/g²)²sup ρ.
         With step 1, every term is ≤ C g^{-(N-1)L²-8}e^{-ε_1²/(4g²)}s^{0,0,4}, and g^{-p}e^{-ε_1²/(4g²)} ≤
         C_a e^{-a/g²} for a < ε_1²/4 and g ≤ g_0. For log(1 + ρ): it is even in s, smooth in ρ ≥ 0, and the same
         steps apply with c → c/(1 + ρ_0). ∎
    - *Consequence (the RTARGET §2 summation; arithmetic).* A level-j cube seen from level k has s = L^{-(k-j)}; there
      are L^{2(k-j)} of them per level-k cell, so the field-dependent remainders sum to ≤ C Σ_{j≤k}L^{-2(k-j)}w_j ≤
      C' sup w, uniformly in k, K. The δβ shifts sum to Σ_j|δβ(g_j)| ≤ Ce^{-a/g²}Σ_nL^{-aβn} < ∞ along the flow, and are
      ≪ g_j⁴. **So, for isolated cubes, LF-count's divergence sits entirely in the field-independent vacuum part ρ_0**,
      which is removed by the normalisation constants (as log Z^{(j)}(1), E^{(j)}(1) are in CMP 109 (1.3)). It
      cancels in normalised expectations and in Z_K/Z_K^ref with matching constants, which is why it is "uniform in K":
      it is cancelled, not bounded.
    - *What R2D-iso does NOT give (the exact walls of the full R-operation, now named):*
      - **W1 (localisation in a fluctuating sea).** The exterior is frozen. In the real integral the neighbours are
        small-field integration variables that respond to the large-field defect. A proof needs a polymer/cluster
        expansion with the large-field cube as a defect, giving ρ_full(□) = local terms with exponential tails and the
        same s-derivative bounds. This is Dimock's "difficult technical problem" of localising the characteristic
        functions (Rome p.57 [read]) and Balaban's CMP 122 II "Localization, exponentiation" [not-read].
      - **W2 (nested, multi-scale large fields).** Step 5 expands around a smooth background. Inside a region that is
        large-field at several consecutive scales the background is not smooth and the expansion has no small
        parameter. R2D-iso covers only cubes whose coarse neighbourhood is small-field.
      - **W3 (hard constraints).** With a normalised block spin, or Balaban's δ(M(U)V^{-1}) with log-based M, the
        V-dependence enters through the fibre of M. Large fluctuations reach M's branch set (an eigenvalue -1 of some
        Z_y: the off-D set of E8/S4''), where M is not smooth, so step 2 fails as written. The soft constraint avoids
        this; Balaban's δ-constraint would need a fibre-smoothness lemma on the large-field event, or a separate
        (E8*-type) probability bound for the branch set.
  - **4D SU(N): what changes (item R4D-iso, OPEN [S7]; [S8] now PROVEN-HERE, see Proposition R4D-iso below; the
    bracketed OPEN content is discharged by Lemma GT).** The isolated-cube statement transfers with these changes:
    - *Cut and positivity.* Use a gauge-invariant plaquette cut |1 - U_p| < ε_1. By inequality (B) its cost is
      s(U_p) ≥ ε_1²/(2N) (Balaban normalisation: a_B ≥ ε_1²/2 with tr 1 = 1). Wilson terms are ≥ 0, so step 1 holds with
      p = dim of the cube's link variables (no gauge fixing is needed for a compact group with frozen exterior). Balaban's
      own cut is on the gauge-fixed fluctuation B' and is not gauge invariant by itself, a difference to track.
    - *Constraint.* A soft gauge-covariant constraint, e.g. (κ/g²)Σ_cΣ_Γ[1 - N^{-1}Re tr(V(c)^{-1}U(Γ))] over the
      contours of (0.4), is polynomial in V and U, so step 2 holds verbatim. With Balaban's δ-constraint, W3 applies.
    - *Symmetry structure (the one new lemma).* Steps 3-4 transfer: point reflection gives evenness in s, and
      G-conjugation plus gauge invariance give a constant vacuum part. Step 5 must become a gauge-invariant Taylor lemma
      for background links U_b(s) = P exp(is∫_bA(s·)): order s² vanishes, since the only candidate is linear in F and
      tr F = 0 with no hypercubic-invariant linear form; order s⁴ is c·Σtr F_μνF_μν, because Λ²R⁴ is irreducible under
      the hyperoctahedral group B_4 and reflections exclude ε^{μνρσ}tr F_μνF_ρσ, while tr(DDF) = 0; odd orders vanish.
      The remainder is then O(s⁶) and sums against L^{4(k-j)} (α = 2). [The B_4 irreducibility and the order-s² and
      order-s⁴ classification are argued here, not yet written as a proof for general analytic gauge-invariant
      functions of links. This is the OPEN content of R4D-iso, together with s_0 for the 4D cube.]
    - W1 and W2 are unchanged in 4D. W3 is sharper, because Balaban's (0.4) uses log in the averaging itself.
- **[S8] Session 8: targets pre-stated in RTARGET.md §5-7 before the derivations. Status of L5 unchanged:
  IMPORTED-NOT-YET-REVERIFIED.** New PROVEN-HERE: Lemma GT, Proposition R4D-iso (moved from
  OPEN), Lemma W1-sym (with W1-def and W1-size). New OPEN: W1-loc. Check c19 (10/10).
  - **Lemma GT (gauge-invariant Taylor lemma): PROVEN-HERE [S8].**
    - *Setting* (RTARGET §6). Data D = a finite B_4- and ι-symmetric set of lattice links around the site 0 (and, for
      R4D-iso, the coarse links V(c), c = (0, ±Le_μ)), each carrying a G-valued variable, G = SU(N), N ≥ 2. Background:
      a smooth su(N)-connection A on R⁴ in radial gauge x^μA_μ(x) = 0, ||∂^αA_μ||_op ≤ 1 for 1 ≤ |α| ≤ 6; A^{(s)}(y)
      := sA(sy); D(s) := the parallel transporters of A^{(s)} along the straight segments of the data (convention
      U' = UA along the path; gauge action U_b → h(x)U_bh(y)^{-1}, A → hAh^{-1} - (dh)h^{-1}).
    - *Claim.* Let F be C⁶ near the trivial configuration 1 and along the family, and invariant under (i) all
      gauge transformations of the data, (ii) B_4 (signed permutations about 0, which contains ι = -1). Put
      f(s) := F(D(s)). Then f is even; f'(0) = f''(0) = f'''(0) = 0; f^{(4)}(0)/24 = c_F Σ_{μ<ν}||F_μν(0)||²_HS
      with c_F independent of A; and |f(s) - f(0) - c_F s⁴Σ||F_μν(0)||²| ≤ (s⁶/720)sup_{|σ|≤|s|}|f^{(6)}(σ)|.
    - *Proof.*
      1. **Radial gauge is no loss.** Every smooth A is gauge-equivalent to a radial-gauge one (Fock-Schwinger); the
         transporters of h·A are h(x)U_bh(y)^{-1}; (h·A)^{(s)} = h(s·)·A^{(s)}. So f is the same in every gauge, by (i).
      2. **Order of the data.** In radial gauge A(0) = 0 and ∂_μA_ν(0) + ∂_νA_μ(0) = 0 (differentiate x^νA_ν = 0
         twice), so ∂_νA_μ(0) = ½F_νμ(0). Hence A^{(s)}(y) = s²y^ν∂_νA(0) + O(s³), and for small s the data logs
         X_b(s) := log D_b(s) obey X_b(s) = s²X_b^{(2)} + O(s³), with (first Magnus term; path-ordering corrections are
         O(|A^{(s)}|²) = O(s⁴)) X_b^{(2)} = ∫_0^1(x + te_μ)^ν dt·½F_νμ(0) = ½x^νF_νμ(0) for b = (x, x + e_μ) (F_μμ = 0),
         and X^{(2)} = 0 for the coarse segments (0, ±Le_μ). So X^{(2)} = 𝓛(Φ) with Φ := F(0) ∈ su(N) ⊗ Λ²R⁴, 𝓛 linear.
      3. **Order s² vanishes (no relevant term).** F̃(X) := F(exp X) near 0. Constant gauge transformations fix 1 and
         act by Ad, so F̃∘Ad_h = F̃, hence DF̃(0)∘Ad_h = DF̃(0): each component of DF̃(0) is an Ad-invariant element of
         su(N)* ≅ su(N), i.e. central, i.e. 0 (G semisimple; cf. CMP 109 (4.14) [read, NOTES §9.6]). With X(0) = X'(0)
         = 0, Faà di Bruno gives f'(0) = 0, f''(0) = DF̃(0)X''(0) = 0, and f^{(4)}(0) = DF̃(0)X^{(4)}(0) +
         3D²F̃(0)(X''(0), X''(0)) = 12 D²F̃(0)(𝓛Φ, 𝓛Φ).
      4. **Evenness (odd orders vanish).** (ι^*A)_μ(x) := -A_μ(-x) is radial, its transporters are the ι-image of
         those of A (orientation reversed), and A^{(-s)} = ι^*(A^{(s)}). By (ii) for ι, f(-s) = f(s).
      5. **One invariant at order s⁴.** Q(Φ) := ½D²F̃(0)(𝓛Φ, 𝓛Φ) = f^{(4)}(0)/24. D²F̃(0) is Ad-invariant (step 3) and
         𝓛 is Ad-equivariant, so Q is Ad-invariant. For R ∈ B_4, R·A := (x ↦ RA(R^{-1}x)) is radial, its data are the
         R-permuted data, (R·A)^{(s)} = R·(A^{(s)}), and (R·A)'s curvature at 0 is Λ²(R)Φ; by (ii), Q∘Λ²(R) = Q. Now:
         - *Λ²R⁴ is absolutely irreducible under B_4.* The sign flips diag(ε) act on e_μ∧e_ν by ε_με_ν; the six lines
           have pairwise distinct characters of (Z_2)⁴ (the flip of coordinate k negates e_μ∧e_ν iff k ∈ {μ,ν}), so a
           (complex) endomorphism commuting with B_4 is diagonal in this basis; the permutations act transitively on the
           six pairs, so its diagonal is constant. (c19 P1: character norm 1; the rotation subgroup gives 2, i.e.
           self-dual ⊕ anti-self-dual, so the reflections are needed.)
         - su(N) is absolutely irreducible under Ad (its complexification sl(N,C) is irreducible).
         - Invariant endomorphisms of V ⊗ W under G_1 × G_2 are End_{G_1}(V) ⊗ End_{G_2}(W) = R. Hence every Ad × B_4
           invariant symmetric bilinear form on su(N) ⊗ Λ² is a multiple of Σ_{μ<ν}⟨Φ_μν, Φ'_μν⟩_HS (c19 P2: dimension 1
           for SU(2)). So Q(Φ) = c_F Σ_{μ<ν}||Φ_μν||²_HS. In particular ε^{μνρσ}tr Φ_μνΦ_ρσ (odd under reflections) is
           excluded: (R4-F2) avoided.
      6. Taylor with Lagrange remainder at order 6, odd terms and f''(0) zero. ∎
    - *What GT uses:* only gauge invariance, B_4 and ι invariance, and C⁶. It does not use positivity or the
      specific F; it applies to ρ, to log(1 + ρ) and to A_B alike.
  - **Proposition R4D-iso (one isolated 4D SU(N) cube, frozen exterior, one step): PROVEN-HERE [S8] (moved from OPEN).**
    - *Setting* = RTARGET §6: cube □ of L⁴ sites (L odd ≥ 3) centred at the site 0; integration over the interior links
      (Haar); frozen data = the other links of plaquettes meeting the interior, the contour links of the neighbouring
      blocks, and V(c); action S = (1/g²)[Σ_{p∩int≠∅}(1 - N^{-1}Re tr U_p) + κΣ_t(1 - N^{-1}Re tr W_t)], W_t the
      closed words U(Γ)U([x,x'])U(Γ')^{-1}V(c)^{-1} over Balaban's axial families (all orders, both ends; B_4-symmetric);
      cut χ = Π_{p⊂int}1{||1 - U_p||_op < ε_1}; ρ := ∫(1-χ)e^{-S}/∫χe^{-S}; f(s) := ρ(D(s)).
    - *Claim* = (R4D) as pre-stated: for every a < ε_1²/(4N) there are C, s_0, g_0 depending on (L, N, κ, ε_1, a) only
      with ρ(s) = ρ_0(g) + δβ(g)A_B(D(s)) + R(s), 0 ≤ ρ_0 ≤ Ce^{-a/g²}, |δβ| ≤ Ce^{-a/g²} (background-independent),
      |R(s)| ≤ Ce^{-a/g²}s⁶, for g ≤ g_0, all A as in GT, |s| ≤ s_0. The same for log(1 + ρ).
    - *Proof.*
      1. **Invariances.** Gauge: a gauge transformation of the data at sites outside the interior, together with the
         same transformation h_0 of the V(c) at 0 and the change of variables U_int → h·U_int (Haar invariance), leaves
         S, χ and dU_int invariant; so ρ(h·D) = ρ(D). B_4 and ι: the cube, the data, the word family and χ are
         B_4-symmetric about 0. Smoothness: S is a polynomial in the matrix entries, χ is data-independent, the
         denominator is > 0; so ρ is C^∞.
      2. **Size, priced by inequality (B).** On {χ = 0} some interior plaquette has ||1 - U_p||_op ≥ ε_1, and by (B)
         (1 - N^{-1}Re tr U_p) ≥ ||1 - U_p||²_op/(2N) ≥ ε_1²/(2N); all terms of S are ≥ 0 and Haar has mass 1, so the
         numerator is ≤ e^{-ε_1²/(2Ng²)}. Denominator: restrict to ||U_b - 1||_op ≤ rg (b interior), r := ε_1/8, g ≤ 1;
         there every interior plaquette has ||1 - U_p|| ≤ 4rg < ε_1, so χ = 1. By step 2 of GT and ||A^{(s)}(y)|| ≤
         s²|y|_1 on the data region, every data variable obeys ||D_b(s) - 1|| ≤ C_L s², C_L = O(L²). Each term of S has
         1 - N^{-1}Re tr W ≤ ½||1 - W||²_op ≤ ½(ℓ_W(rg + C_Ls²))² ≤ ℓ_W²(r²g² + C_L²s⁴), ℓ_W the word length. So
         S ≤ C_0 + Bs⁴/g² on the balls, C_0 = C_0(L, κ, ε_1), B = B(L, κ). Haar balls: μ{||U - 1|| ≤ δ} ≥ c_Nδ^{N²-1}
         (δ ≤ 1) [elementary]. With p := (N²-1)·#(interior links): ρ(s) ≤ C_1g^{-p}e^{-(ε_1²/(2N) - Bs⁴)/g²}, and for
         |s| ≤ s_0 := (ε_1²/(4NB))^{1/4} (g-independent; (R4-F4) avoided): ρ(s) ≤ C_1g^{-p}e^{-ε_1²/(4Ng²)}.
      3. **Derivatives.** The data are transporters of A^{(s)}, smooth in s with ||∂_s^jD_b(s)|| ≤ C_j(L) for |s| ≤ 1
         (smooth dependence of U' = Ua(t;s) on the parameter, a(t;s) = A^{(s)}(x + te_μ), with ||∂_s^ja|| ≤ C_j(L) from
         the bounds on A; unitarity) [elementary]. So |∂_s^jS| ≤ Λ_j/g², and exactly as in R2D-iso step 2 (positive
         integrands, s-independent indicator, quotient rule) |f^{(q)}(s)| ≤ B'_q(Λ/g²)^qρ(s), q ≤ 6.
      4. **Structure.** GT applies to f (step 1): f(s) = ρ(0) + c_ρs⁴Σ||F_μν(0)||² + R_f, |R_f| ≤ (s⁶/720)sup|f^{(6)}|.
         ρ_0 := ρ(0) is the trivial-data value, background-independent. A_B := Σ_{p∈B}(1 - N^{-1}Re tr U_p) over the
         plaquettes B of the data region (B_4- and ι-symmetric, n_B per plane) is itself gauge- and B_4-invariant, so by
         GT A_B(D(s)) = c_Bs⁴Σ||F_μν(0)||² + R_B with c_B = n_B/(2N) (1 - N^{-1}Re tr e^Y = ||Y||²_HS/(2N) + O(Y⁴);
         c19 P8: 9 = 36/4 for SU(2)) and |R_B| ≤ C'_Bs⁶. Put δβ := c_ρ/c_B, R := R_f - δβR_B.
      5. **Bounds.** Test connection A_ν(x) = ½x^μF⁰_μν with F⁰_12 = -F⁰_21 = T, ||T||_op = 1, ||T||²_HS = 2, other
         components 0 (radial, ||∂A|| ≤ ½, higher derivatives 0): |c_ρ| ≤ sup|f^{(4)}|/48. With steps 2-3 every term is
         ≤ Cg^{-p-12}e^{-ε_1²/(4Ng²)}·{1, 1, s⁶}, and g^{-q}e^{-ε_1²/(4Ng²)} ≤ C_ae^{-a/g²} for a < ε_1²/(4N), g ≤ g_0.
         log(1 + ρ) satisfies the hypotheses of GT directly, with the same bounds. ∎
    - *Consequence (arithmetic).* A level-j cube against a level-k background has s = L^{-(k-j)}; L^{4(k-j)} such cubes
      per level-k cell give Σ_{j≤k}L^{4(k-j)}L^{-6(k-j)}Cw_j ≤ C'sup w (α = 2), uniformly in k, K. The δβ shifts sum
      along the flow (Σ_n e^{-a/g²}L^{-aβn} < ∞) and are ≪ g_j⁴. So **in 4D, for isolated cubes, LF-count's divergence
      sits entirely in the field-independent ρ_0**, removed by normalisation, exactly as in d = 2. All four failure
      modes R4-F1..F4 are avoided as pre-stated.
    - *Scope.* Frozen exterior (W1), smooth background (W2), soft constraint (W3) and the gauge-invariant cut on
      interior plaquettes (Balaban's cut is on the gauge-fixed B'; difference still tracked) are as pre-stated "not
      success" items. c19 tests GT on explicit instances, including an exactly integrated single-link function; it does
      not evaluate the cube integral ρ itself.
  - **Check c19 (criteria checks/c19_criteria.md, written before checks/c19_gauge_taylor.py): 10/10 PASS** (first run,
    18 s, 64 MB, load 1.9, 36% free memory, nice 10, BLAS threads 1; output checks/c19_out.txt).
    - P1 Λ² character norm under B_4 = 1 (rotation subgroup: 2). P2 dim of Ad × B_4-invariant forms on su(2)⊗Λ² = 1.
    - Six radial-gauge SU(2) backgrounds (abelian, self-dual F(0), anti-self-dual F(0), three generic), box |x_μ| ≤ 1.
      F1 (Wilson sum), F2 (squares, 1×2 rectangles, adjacent-plaquette products), F3 (Σ over the 8 star links of the
      exact single-link Haar integral log[I_1(2β|K_b|)/(β|K_b|)]):
      evenness |f(0.2) - f(-0.2)| ≤ 4e-12 (P3 at s = 0.4, 0.2, 0.1); (f(s)-f(0))/s⁴ converges like s² (difference ratios 3.80-4.23); c_F universal to relative spread
      ≤ 5e-8 (c = 9.0000000, -77.999999, -2.1185381), self-dual and anti-self-dual agreeing; remainder ratios
      R(0.1)/R(0.05) = 63.4-64.6 (s⁶); gauge invariance under a non-radial gauge ≤ 3e-12.
    - Controls have power: plane-(1,2)-only sum (B_4 broken) gives c spread 0.80 across backgrounds; half-space sum
      (ι broken) has an odd part 1e-3..1e-2 at s = 0.2 scaling like s⁵ (ratios 27.8-36.5; criterion met on 4 of 6
      backgrounds, required on 1).
  - **W1 in d = 2 (RTARGET §5): partial. The exact wall is named (W1-loc). Three lemmas PROVEN-HERE [S8].**
    - **Lemma W1-def (exact defect identity).** In Setting W1, fix any states (cut/released) of the blocks ≠ □_0. Let
      Z^{cut}, Z^{rel} be the integrals with χ_0, resp. 1, for □_0, and ⟨·⟩_cut the probability measure of Z^{cut}.
      Then Z^{rel}/Z^{cut} = 1 + ⟨ρ_□(n_Γ, Φ_0)⟩_cut, with ρ_□ exactly R2D-iso's function of the exterior ring
      m = n_Γ and Φ_0. *Proof.* S = S_□(n_□; n_Γ, Φ_0) + S_rest, with S_rest independent of n_□ (crossing bonds only join
      □ to Γ); integrate n_□ first (Fubini): Z^{rel} = ∫(rest)(Den_□ + Num_□) = ∫(rest)Den_□(1 + ρ_□). ∎ So the
      fluctuating-exterior defect is R2D-iso's ρ averaged over the conditioned sea; F(Φ) := log(1 + ⟨ρ_□⟩_cut), and
      ∂_{Φ_c}⟨ρ_□⟩_cut = -(κ/g²)Cov_cut(ρ_□, Φ_c - L^{-2}Σ_{x∈c}n_x) for c ≠ □_0: derivatives are truncated
      correlations of ρ_□ with block averages.
    - **Lemma W1-size (exact size reduction).** Let δ_0 := ε_1/(2√(4L + κ)) and E := {n_Γ : no e ∈ S^{N-1} has
      |n_y - e| ≤ δ_0 for all y ∈ Γ and |Φ_0 - e| ≤ δ_0}. Then, with P_rel the measure of Z^{rel},
      ⟨ρ_□⟩_cut ≤ [C_1g^{-(N-1)L²}e^{-ε_1²/(4g²)} + P_rel(E)] / (1 - P_rel(E)).
      *Proof.* On E^c, R2D-iso step 1 with caps around e gives S ≤ C_0 + (4L + κ)δ_0²/g² (crossing bonds ½(rg + δ_0)²,
      constraint (κ/2)(δ_0 + rg)², (u+v)² ≤ 2u² + 2v²), hence ρ_□ ≤ C_1g^{-(N-1)L²}e^{-ε_1²/(4g²)}. On E:
      ⟨ρ_□1_E⟩_cut = Z^{rel}[□_0 large, E]/Z^{cut} ≤ Z^{rel}[E]/Z^{cut} = P_rel(E)(1 + ⟨ρ_□⟩_cut). Rearrange. ∎
      So the size half of W1 is exactly a collar large-deviation bound for the sea, not a property of the cube.
    - **Lemma W1-sym (symmetry + locality ⇒ renormalised form, for functions of the whole block-spin field).** Block torus
      Λ_T (T odd, representatives |c_μ| ≤ (T-1)/2, □_0 at 0). Let F be C⁴ on a neighbourhood of the family below,
      (i) O(N)-invariant, (ii) invariant under the stabiliser D_4 of 0 (which contains ι), and (iii) for 0 ≤ q ≤ 4
      |∂_{c_1,i_1}···∂_{c_q,i_q}F| ≤ C_qw e^{-κ_d max_j|c_j|_1} on the family (κ_d: decay rate; κ stays the constraint
      strength; RTARGET §5's decay "κ" is this κ_d). Family Φ_c(s) = n(sc), |∂^αn| ≤ 1
      (1 ≤ |α| ≤ 4), |s| ≤ s_0. Then F(Φ(s)) = f_0 + δβA_B(Φ(s)) + R(s), f_0 independent of n, |f_0|, |δβ| ≤ C'w,
      |R| ≤ C'ws⁴, C' depending on (C_q, κ_d, N, B) only, uniform in T.
      *Proof.* (1) |Φ_c^{(j)}(s)| = |(c·∇)^jn(sc)| ≤ |c|_1^j, so by Faà di Bruno |f^{(q)}| ≤ Σ C_kN^{k/2}w·S_k with
      S_k ≤ kΣ_R(2R+1)^{2k}R^qe^{-κ_dR} < ∞, T-independent. (2) Φ(-s) = Φ(s)∘ι, so f is even. (3) f(0) = F(e,…,e) is
      independent of e by (i). (4) At the constant point the O(N-1) stabiliser makes DF_c = γ_ce and the Hessian on
      e^⊥ equal to h_{cc'}(u·v); with u_μ := ∂_μn(0), e·∂_μ∂_νn(0) = -u_μ·u_ν, f''(0) = Σ_{μν}T_μνu_μ·u_ν,
      T_μν = Σ_{cc'}h_{cc'}c_μc'_ν - Σ_cγ_cc_μc_ν (absolutely convergent by (iii)). (5) Test backgrounds
      n(x) = cos(a·x)e + sin(a·x)v, |a_μ| ≤ 1, realise u_μ = a_μv; D_4 maps [-1,1]² to itself and (ii) gives
      T_sym = σT_symσ^T; D_4 is absolutely irreducible on R² (sign flips separate the axes, the swap equates them),
      so f''(0) = tΣ_μ|u_μ|². (6) A_B as in R2D-iso step 6 with b_B bonds per direction; δβ := t/b_B, R := R_4 - δβR_B. ∎
      R2D-iso steps 3-7 are the special case F = ρ with finitely many arguments.
    - **Corollary W1-red.** If W1-loc (below) holds, the weak (single-defect) form of (W1) holds with w = Ce^{-a/g²},
      uniformly in T: (i), (ii) hold for F = log(1 + ⟨ρ_□⟩_cut) (S, σ and the cuts are O(N)- and D_4-invariant), and
      W1-loc is (iii).
    - **W1-loc (OPEN, the exact W1 wall; a statement about the small-field sea only).** In Setting W1 with every block
      ≠ □_0 cut, there are C_q, κ_d, a, s_0, g_0 > 0 depending on (L, N, κ, ε_1) only such that for g ≤ g_0, all T and
      Φ = Φ(s), |s| ≤ s_0:
      - (W1-LD, size) P_rel(E) ≤ Ce^{-a/g²} (by W1-size this gives the q = 0 bound);
      - (W1-cl, decay) the joint truncated correlations of ρ_□ with q ≤ 4 block averages Φ_{c_j} - L^{-2}Σ_{x∈c_j}n_x
        are ≤ C_qe^{-a/g²}(g²/κ)^q e^{-κ_d max_j|c_j|_1} under ⟨·⟩_cut (this is (iii) for q ≥ 1).
      *Why it is not proven here.*
      - W1-LD needs the sea's stiffness at the δ_0 scale. The cheap route, local exponential moments ⟨e^{tS_c}⟩ via
        frozen-exterior bounds (Hölder: ∫χe^{-(1-t)S_c} ≤ Z_c^{1-t}, then R2D-iso's cap bound for Z_c), regenerates
        ⟨e^{t'S_{c'}}⟩ on the neighbouring blocks with t' = Mt, M ≈ 2(4L + κ)C_P·deg ≫ 1 (C_P the block Poincaré
        constant). The recursion does not close. [Route obstruction, not a no-go.]
      - W1-cl is exponential clustering of the block-pinned low-temperature O(N) sea, i.e. the small-field cluster
        expansion, the 2D analogue of L4a-form (Balaban defers it to CMP 116, NOTES §9.6) and of Dimock I Lemma 21.
      - (W1-F3, as pre-stated) Dimock I Thm 27 (NOTES §1) needs an ultralocal measure. The sea is ultralocal only after
        the Gaussian change of variables with the random-walk-expanded covariance (the L3 machinery). So the
        multi-defect strong form (W1-a/b) is not reached either.
      - Illustration [N = 2 only, outside the target's N ≥ 3; argument sketched, not counted]: if ε_1 < √2 and
        □'s cut also covers its crossing bonds, a winding-1
        exterior ring with all exterior bonds < ε_1 (L large) forces Den = 0, i.e. ρ = ∞, since bond angles < π/2 give zero
        vorticity on every plaquette of □, so □'s boundary loop, and with it the exterior ring, has winding 0. So no size bound uniform over the small-field exterior exists in general.
        The collar must enter jointly, as in W1-size.
    - **Outcome vs RTARGET §5.** Strong form (W1-a/b/c): not reached. Weak form: reduced exactly to W1-loc
      (W1-def + W1-size + W1-sym). Failure modes met: W1-F1 in the precise form W1-LD; W1-F2 = W1-cl; W1-F3 as stated.
      W1-F4 avoided (s_0 and a are g-independent in every reduction step).
    - **4D.** W1-def and W1-size transfer verbatim (Fubini; caps; inequality (B) for the numerator). W1-sym's 4D
      analogue is GT with the decay-summability step (1) [argued, not written; not counted]. W1-loc's 4D form is the
      clustering of the 4D small-field sea, i.e. L4a-form/L3g territory.
  - **W2** is pre-stated only (RTARGET §7); not attacked.

### L6. UV stability: IMPORTED-NOT-YET-REVERIFIED
- **Statement (paraphrase).** exp(-E_- |T|) ≤ Z_K / Z_K^ref ≤ exp(E_+ |T|), uniformly in K, with bulk dependence on
  the torus size.
- **Dimock's scalar analogue [v-abs, introduction read]:** torus (L^-N Z / L^M Z)^3, bounds "uniform in the ultraviolet
  cutoff N and with bulk dependence on the volume parameter M" (Dimock, arXiv:1212.5562; see also 1108.1335 and
  1304.0705; part III proves "convergence of the expansion" for the stability bound, not of correlations).
- **Correction to review.md §1.** "Small physical volume" is probably a misreading. The restriction is that the
  coupling be small at the stopping scale; the torus side in stopping-scale units is arbitrary (M is arbitrary). Status:
  pending the Balaban primary text.
- **[S5]** Upgraded to [read]: Dimock I Theorem 1 (p.2, eq. 7) and III Corollary 1 (p.33, eq. 225) give
  exp(∓λ^η Vol(T_M)) bounds for all M, N (φ⁴_3, arbitrary volume); QED Theorem 2 (2009.01156 p.8, eq. 42) gives
  1/2 ≤ Z/Z(0) ≤ 3/2 in unit volume, "works equally well for any finite volume" (2204.07201 p.2-3). For 4D SU(N): still
  IMPORTED-NOT-YET-REVERIFIED (CMP 109/116/119/122 bodies not read).
- **[S6]** Status unchanged: IMPORTED-NOT-YET-REVERIFIED.
  - CMP 109 [read] proves only the small-field half, and only modulo CMP 116 for the localisation. Its bulk bound
    (0.30), |E_k(U_k)| ≤ O(1)(1 - L^{-α})^{-1}M^{-4}|T_1^{(k)}|, is the small-field form of L6, conditional on
    L4a-form.
  - The torus in (0.1) has side 2L^m in unit-lattice units, with m arbitrary. So, as in Dimock's φ⁴_3, nothing in CMP
    109 restricts the physical volume to be small. This answers the review.md §1 question at the level of the
    small-field theorem; it does not settle it for the full L6.
  - Theorem 1 assumes only 0 < g_k ≤ γ, not asymptotic freedom (p.259).

### L6loc. Local, volume-uniform large-field suppression: E8 as stated is FALSE for SU(2), SU(3) with D (fixed bare g: unconditionally; tuned g: conditional on L4a) [S3, R3-fix]; the fine-scale local bound is PROVEN-HERE; the scale-local replacement E8* is OPEN (fixed-depth cases PROVEN-HERE [S4])
- **Estimate E8 (session-1 form).** There is δ(g) → 0 as g → 0 such that, for every K ≥ m, every M, and every
  resolution-m block B, μ_{K,M}(some averaging step K → m leaves D inside B) ≤ δ(g).
- **[S3] Verdict.** E8 in this form fails: Proposition E8.3 below proves that, along any sequence with β_K ≤ λK and λ
  below an explicit λ_c, the probability that some *first* step (K → K-1) leaves the domain inside B tends to 1. The AF
  rate of the tuned coupling (imported, L4a) lies below λ_c for SU(2) and SU(3) with the domain D. **[R3-fix]** The
  session-3 text also said "for every N with the τ_N/2 thresholds"; that concerns the stronger event "all steps within
  τ_N/2", which is not E8 and not what E7.0 needs. For SU(4) with D the crude bound is undecided; for N ≥ 6, t = 1 is
  inadmissible in the conditional lemma; D_N (N ≥ 7) is not covered. **[R3-fix] Reading of "g".** If g in E8 is a fixed
  bare coupling, E8 is false unconditionally (a fixed β is ≤ λK for all large K, so sup_K μ = 1). If g is the running
  coupling along the tuned sequence, the failure needs β_K ≤ λ_c K, i.e. the imported L4a rate: false conditional on L4a.
  Lattice-scale domain failures are dense in physical space in the continuum limit: their
  number per unit physical volume grows like L^{(4 - a)K} with a < 4. So "all steps succeed" is the wrong event, and the
  right object is a per-scale-block (Peierls-type) bound, E8* below.

**Setting for E8.1-E8.3.** Wilson SU(N) action S3 on a fine torus Λ = (Z/2mZ)^4 in lattice units (even side, as in the
[S3] torus convention; m ≥ 1), at any β ≥ 0. Cells C_t = t + [0,1]^4 (closed unit cubes), t ∈ Λ. For η > 0,
G_t := 1[max_{p ⊂ C_t} ||1 - U_p|| ≥ η] ("cell t is η-bad"). h_N(δ) := Haar{U : ||U - 1|| ≤ δ}.

**E8.1. Chessboard bound at the cutoff scale: PROVEN-HERE (given L9a, site reflection, on the even torus).** [R3-fix:
attribution] This is a special case of the Fröhlich-Israel-Lieb-Simon chessboard estimate (J. Fröhlich, R. Israel,
E. H. Lieb, B. Simon, "Phase transitions and reflection positivity. I", CMP 62 (1978) 1-34 [v-R4]); the special case is re-derived below, so nothing rests on the citation.
- **(i)** For every set R of cells, μ(all cells of R are η-bad) ≤ q̄(η)^{|R|}, with q̄(η) := μ(all cells η-bad)^{1/|Λ|}.
- **(ii)** For every δ ∈ (0, 1/2]: q̄(η) ≤ exp(-βη^2/(8N) + 48βδ^2) h_N(δ)^-4.
- **(iii)** h_N(δ) ≥ (κ_N δ)^{N^2-1} for δ ≤ 1/2, with κ_N > 0; for SU(2), h_2(δ) ≥ (8/(3π^3)) δ^3. With δ^2 = 1/(8β)
  (β ≥ 1/2), SU(2): q̄(η) ≤ e^6 (3π^3/8)^4 (8β)^6 e^{-βη^2/16}. In terms of g^2 = 2N/β the decay is e^{-η^2/(4g^2)}.
- **Proof of (i) (chessboard estimate, special case re-derived).**
  - Equivariance: a reflection θ through a site plane maps cell C_t onto a cell C_{t'} and its plaquette set onto that of
    C_{t'}, and ||1 - U_p|| is invariant under the orientation reversal U_p → U_p^dag-conjugates. So θ(G_t) = G_{t'}.
  - Regularise: G^ε_t := G_t + ε. For H ⊂ Λ put a(H) := E[Π_{t∈H} G^ε_t] and ρ(H) := a(H)/a(Λ)^{|H|/|Λ|} > 0.
  - Doubling inequality. Let θ be the site reflection through x_j = k (and its antipode x_j = k + m), with halves
    Λ_± of m cell-slabs each. Write Π_{t∈H} G^ε_t = A·θ(B), with A = Π_{H∩Λ_+} G^ε (measurable on the closed positive
    half, which includes the plane links) and B = θ(Π_{H∩Λ_-} G^ε). RP (L9a, site reflection) gives the Cauchy-Schwarz
    inequality E[Aθ(B)] ≤ E[Aθ(A)]^{1/2} E[Bθ(B)]^{1/2}. Here E[Aθ(A)] = a(H_+), with H_+ := (H∩Λ_+) ∪ θ(H∩Λ_+), and
    similarly a(H_-); |H_+| + |H_-| = 2|H|. Hence ρ(H) ≤ ρ(H_+)^{1/2} ρ(H_-)^{1/2}.
  - So if H maximises ρ over the finite set of subsets, then H_+ and H_- are maximisers too.
  - Reaching a constant pattern. In direction 1, let P_s be the transverse pattern of slab s; a reflection maps P_s to
    the mirrored slab unchanged. Take a maximal cyclic run of equal consecutive P_s, of length ℓ < 2m, and reflect
    through the plane at its end, keeping the half that contains the run. The new maximiser has a run of length
    ≥ 2 min(ℓ, m) > ℓ. Iterate until the pattern is constant in direction 1. Reflections in directions 2, 3, 4 preserve
    constancy in direction 1; repeat. The end is a maximiser that is ∅ or Λ, and ρ(∅) = ρ(Λ) = 1.
  - So ρ ≤ 1, i.e. a(H) ≤ a(Λ)^{|H|/|Λ|}. Let ε → 0 (dominated convergence). ∎
- **Proof of (ii).** If every cell is bad, there are at least |Λ|/4 distinct bad plaquettes, since a plaquette lies in
  at most 4 closed unit cubes (2 choices in each of the 2 transverse directions). With eigenvalues e^{iθ_j},
  1 - N^-1 Re tr U = N^-1 Σ(1 - cos θ_j) ≥ ||1 - U||^2/(2N). So on that event S ≥ β(|Λ|/4)η^2/(2N); Haar has mass 1.
  For the denominator, restrict to all links in the δ-ball: then ||1 - U_p|| ≤ 4δ and 1 - N^-1 Re tr U_p ≤ 8δ^2 for all
  6|Λ| plaquettes, so Z ≥ e^{-48βδ^2|Λ|} h_N(δ)^{4|Λ|}. Take the |Λ|-th root. ∎
- **Proof of (iii).** For X ∈ su(N), ||e^X - 1|| ≤ ||X||, so exp maps the operator-norm δ-ball of su(N) into the
  δ-ball of SU(N). exp is injective on ||X|| < π with a continuous positive Haar Jacobian on ||X|| ≤ 1/2, and the
  Lebesgue volume of the δ-ball is v_N δ^{N^2-1}. SU(2): class angle θ (eigenvalues e^{±iθ}) with density (2/π) sin^2 θ and ||U - 1|| = 2 sin(θ/2);
  h_2(δ) = (θ_δ - sin θ_δ cos θ_δ)/π with θ_δ = 2 arcsin(δ/2) ≥ δ, and sin θ ≥ 2θ/π gives ≥ (8/(3π^3))δ^3. ∎
- **Check c10(A)** (exact 2D U(1), tori 4×4 and 6×4, 90 cases): μ(R bad) ≤ q̄^{|R|} holds (max ratio 1.0000, attained at
  R = Λ). In 2D U(1) the plaquettes are exchangeable, so this tests the inequality, not the geometry. c10(B): the SU(2)
  ball bound holds with ratio ≈ 2.3-2.5.

**E8.2. One-step local ratio bound for S4': PROVEN-HERE (given E8.1).**
- Let b' = (X, X + e_μ) be a first-step coarse link (blocks of side L in lattice units) and F_{b'}(t) the event that some
  Z^σ_y = S_{c_X}^-1 T^σ_y (any order σ, any y ∈ B(X)) has ||Z^σ_y - 1|| ≥ t. Put A_L := (d-1)L(L-1)/2 (= 9 for L = 3,
  d = 4).
- **Claim.** μ(F_{b'}(t)) ≤ 2L^4 q̄(t/A_L). For first-step links b'_1, ..., b'_r whose two-block regions are pairwise
  site-disjoint, μ(all F_{b'_i}(t)) ≤ (2L^4 q̄(t/A_L))^r. Both are uniform in the volume and in K.
- **Proof.** The ribbon decomposition of L1e in lattice units: the loop of Z^σ_y is a product of conjugated plaquettes of
  the planar grids between γ (the order-σ axial path, inside B(X)) and γ + Le_μ, all inside the two-block region, and
  there are Σ_{ν≠μ} |γ_ν| L ≤ A_L of them. So ||Z^σ_y - 1|| ≤ A_L max_p ||1 - U_p||, and F_{b'}(t) forces some plaquette in
  the region with ||1 - U_p|| ≥ t/A_L; assign it to the cell whose lower corner is the plaquette's lower corner (≤ 2L^4
  cells). Union bound, then E8.1(i). For r links, sum over one cell per link; disjoint regions give distinct cells. ∎
- With β = 2N/g^2 this is the per-block e^{-c/g^2} bound: μ(F_{b'}(t)) ≤ C_N(L, β) exp(-t^2/(4A_L^2 g^2)), where C_N is
  polynomial in β. For L = 3, t = 1: c = 1/324. Explicit but small.
- **Check c10(E):** max over all 24 orders and 81 y of ||Z - 1|| = 0.673 ≤ 9 × 0.507 for one random SU(2) field.
- **Scope.** First step only. E8.1 uses RP of the *fine* Wilson measure under site reflections. For j < K-1 the law of
  V^(j+1) is RP only under block-boundary (link-plane) reflections (L8c); a site reflection through a block mid-plane
  cuts a block, so the coarse chessboard argument does not go through as it stands. OPEN.

**E8.3. Lower bound: lattice-scale failures are dense: PROVEN-HERE (the inequality); the AF reading is CONDITIONAL on the
imported AF rate (L4a).**
- **Lemma (second order at the maximum).** For W ∈ C^{N×N} with ||W|| ≤ w and f(U) = Re tr(UW), let U_* maximise f over
  SU(N). Then f(U_*) - f(U_* e^X) ≤ (N w/2) ||X||^2 for all X ∈ su(N).
  - Proof: the first variation Re tr(U_* X W) vanishes for all X ∈ su(N) (interior maximum). The remainder is
    -Re tr(U_*(e^X - 1 - X)W), with ||e^X - 1 - X|| ≤ ||X||^2/2 (X normal, |e^{iθ} - 1 - iθ| ≤ θ^2/2) and
    |tr(MW)| ≤ ||M|| ||W||_1 ≤ N ||M|| ||W||. ∎ For a Wilson staple sum, w = 2(d-1), giving N(d-1)||X||^2. Check c10(C):
    max ratio 0.74.
- **Lemma (conditional lower bound).** Let b be a fine link and condition on all other links. The conditional law of U_b
  is ∝ exp((β/N) Re tr(U_b W)) dHaar, with W the staple sum. For any R' ∈ SU(N), t > 0 and δ ∈ (0, 1/2] with t + 3δ ≤ 2 (SU(2)), resp. t + 3δ < 2 sin(π/N) (N ≥ 3, so that
  the principal logs below are traceless by L1b and the first lemma applies):
  P(||U_b - R'|| ≥ t | rest) ≥ q_-(β) := h_N(δ) exp(-β(d-1) x^2), x := 2 arcsin((t + 3δ)/2).
  - Proof: let U_* maximise f. If ||U_* - R'|| ≥ t + δ, take the set A' = U_* · Ball(1, δ). Otherwise U_* = R' e^Z with
    Z normal. In the eigenbasis of Z put Y = i a diag(1, -1, 0, ...), with |a| chosen and signed so that the top
    eigenphase ζ_1 of Z + Y has modulus w_0 = 2 arcsin((t + 2δ)/2) [R3-fix: ζ_1 is chosen as an eigenphase of Z of
    largest modulus, and sign(0) := +1]: a = sign(ζ_1)(w_0 - |ζ_1|), so |a| ≤ w_0 and the
    shifted second eigenphase also has modulus ≤ w_0. Y commutes with Z, so W_0 := U_* e^Y = R' e^{Z+Y}
    has ||W_0 - R'|| ≥ t + 2δ. Take A' = W_0 · Ball(1, δ) ⊂ {||U - R'|| ≥ t}.
  - In both cases each U ∈ A' is U_* e^{X'} with ||e^{X'} - 1|| ≤ t + 3δ, so ||X'|| ≤ x. Haar(A') = h_N(δ), and
    ∫ e^{(β/N) f} ≤ e^{(β/N) f(U_*)}, so P ≥ h_N(δ) e^{-(β/N) N(d-1) x^2} by the first lemma. ∎
  - Check c10(D) (SU(2), 18 random (W, R') cases, 4e5-sample MC): the bound holds in every case (max lb/p = 1.2e-4); it
    is very far from sharp.
- **Proposition E8.3.** Fix t ∈ (0, 2) and δ as above. Let B be a resolution-m block, with fine side L^{K-m}. Then
  μ_{K,β}(no first-step failure F_{b'}(t) inside B) ≤ exp(-q_-(β) L^{4(K-m-1)}/3) for K - m ≥ 2.
  - Proof: take the first-step links b' = (X, X + e_1) with X_1 even and X, X + e_1 inside B. Their two-block regions
    are disjoint, and there are ⌊s/2⌋ s^3 ≥ s^4/3 of them, s = L^{K-m-1} ≥ 3. In each, choose y_0 with a transverse coordinate
    different from c_X and y_{0,1} ≤ c_{X,1}, and let b be the last fine link of the straight leg S_{y_0}. Then b occurs
    exactly once in Z^{σ_0}_{y_0} (it is not on S_{c_X}, not in the axial path inside B(X), and not in the axial path in
    B(X + e_1), which reaches y_0 + Le_1 from above or not at all in coordinate 1), and in no other chosen Z. Writing
    Z = A U_b B, the event ||Z - 1|| ≥ t is ||U_b - A^-1 B^-1|| ≥ t. Condition successively on all links but b_r, then
    b_{r-1}, ...: the other events do not involve U_{b_r}, so each factor is ≤ 1 - q_-. Use 1 - q ≤ e^{-q}. ∎
- **Corollary (AF window).** If β_K ≤ λK with 3 λ x^2 < 4 ln L, then L^{4K} q_-(β_K) → ∞, so for each fixed m and B the
  probability that some first-step averaging inside B fails tends to 1 as K → ∞.
  - With the AF rate β_K ≈ 4N b0 K ln L (imported, L4a; b0 = 11N/(48π^2)), the condition reads 3 x^2 · 4N b0 < 4.
  - In the limit δ → 0 (c10(F)): with t = 1 (the S4 domain, N ≤ 6) the value is 1.22 (SU(2)) and 2.75 (SU(3)), so dense;
    SU(4) gives 4.89, undecided by this crude bound. [R3-fix] The relevant threshold for E7.0 is t = 3τ_N/4 (ζ = 0
    only when some ||Z - 1|| ≥ 3τ_N/4); recomputed (check c13(R)): 0.659 (N = 2), 1.482 (3), 2.635 (4), 4.117 (5),
    5.929 (6), 6.000 (7), 6.097 (10), → 6.19 (N → ∞). So dense for N = 2, 3, 4 only; N ≥ 5 undecided. (The session-3
    values at t = τ_N/2 bound the wrong event: {all < τ_N/2} ⊂ {all < 3τ_N/4}.)
- **Consequences.**
  - **E7.0 fails in the AF window for N = 2, 3, 4 [R3-fix].** E_K[w̃] ≤ E_K[ζ] ≤ μ(no failure at threshold **3τ_N/4**
    in the four resolution-0 blocks of p) → 0 along every sequence with β_K ≤ λK, 3λx^2 < 4 ln L, x = 2 arcsin(3τ_N/8).
    So the RC of S5 at fixed w* > 0 forces β_K > λK eventually: a bare coupling weaker than the AF rate (for SU(2),
    λ_c/λ_AF ≈ 6.1 at δ → 0; session 3 wrote 14, from the wrong threshold). For these N, S5 is not a viable
    renormalisation condition along AF-rate sequences. E7.0 as stated (sup over all β) is NOT falsified; only its
    AF-window restriction is (it is not excluded for β ≫ K, which is not the physical regime). For N ≥ 5: undecided.
  - **E8 as stated is FALSE** for SU(2) and SU(3) with D: unconditionally if g is a fixed bare coupling, and
    conditional on L4a's rate if g is the tuned running coupling (see the verdict above). SU(4) with D: undecided.
  - The session-3 off-D extension "failed link := 1" is then not harmless: it would be used on a dense set of fine
    links. [R3-fix] It is withdrawn; the single extension used from session 4 on is S4'' with the odd branch rule (S4).

**S5'. [S3] Repaired renormalisation condition: per-K tuning PROVEN-HERE; K-uniformity reduced to a β = 0 Haar
statement (E7.0', OPEN).**
- Use the everywhere-defined map S4'' and the plain observable w(V^(0)_p) = 1 - N^-1 Re tr V^(0)_p, with no cut-off.
  Tune E_{K,β_K}[w(V^(0)_p)] = w*.
- **Per K: PROVEN-HERE.** w ∘ V^(0) is bounded and measurable, so β ↦ E_{K,β}[w] is continuous (dominated convergence).
  As β → ∞ the measure concentrates on the flat set (Laplace), where every Z = 1; w ∘ V^(0) is continuous on a
  neighbourhood of the flat set (far from the branch set) and vanishes on it (zero-winding argument of L7.0), so
  E_{K,β}[w] → 0. At β = 0 the value w_0(K) := E_Haar[w(V^(0)_p)] is > 0. IVT: every w* ∈ (0, w_0(K)) is attained.
- **E7.0' (OPEN, now a pure Haar statement):** liminf_K w_0(K) > 0. It no longer involves large-field suppression:
  at β = 0 the fine links are i.i.d. Haar. [R3-fix] E7.0' is SUFFICIENT for a K-uniform w*, not equivalent to it
  (sup_β E_{K,β}[w] may exceed w_0(K)).
- **[R3-fix] Open, unflagged in session 3: AF compatibility of S5'.** Nothing shows that the S5'-tuned β_K follow the
  AF rate. By E8.3, first-step outputs are out of domain on a dense set at AF couplings, and S4'' then averages
  out-of-domain logs; S5' could force β_K ≫ AF by a mechanism like the one that defeats S5. "Repair" was premature:
  S5' is a candidate RC whose per-K tuning is proven and whose AF compatibility is OPEN (estimate E7.0'-AF).
  - Check c12 (finite diagnostic, SU(2), L = 3, MC): w_0 = 0.996 ± 0.017 (K = 1, S4''), 0.993 ± 0.008 (K = 1, fixed
    order), 0.980 ± 0.013 (K = 2, fixed order), 1.03 ± 0.02 (K = 2, S4'', 2 samples). About 77.5% of the first-step Z lie
    outside ||Z - 1|| < 1 at β = 0, so the extension S4'' is used almost everywhere there. Two values of K say nothing
    about the liminf. [R3-fix] The K = 2 S4'' value rests on 2 configurations; its error bar (from 96 correlated
    plaquettes) is not credible. The 77.5% matches exact Haar: Z is Haar unless y differs from c_X only in coordinate μ
    (Z ≡ 1, 3 of 81 sites), and P_Haar(||U - 1|| ≥ 1) = 0.8045, so 78/81 × 0.8045 = 0.775 (REVIEW_S3).
  - Heuristic (not a proof): at β = 0 the out-of-domain logs are spread over the ball of radius π, so the averaged log is
    small and V ≈ the reference, and the coarse plaquette is close to the holonomy of a large loop of nearly independent
    Haar links, whose trace has mean 0. That would give w_0 → 1. The dependence between overlapping paths is what a
    proof has to control.
- **[S4] Lemma H0 (crossing-link structure): PROVEN-HERE.** Let b = (X, X + e_μ) be a coarse link of one S4''-step. For
  each transverse line ℓ (the L^{d-1} lines in direction μ through B(X)), let u_ℓ be the unique link of the straight legs
  S_y, y ∈ ℓ, that crosses the face between B(X) and B(X + e_μ) (the same link for all y ∈ ℓ). Then:
  - (a) for y on the centre line ℓ_0, every Z^σ_y ≡ 1 identically (all axial paths from c_X to y are straight, and T^σ_y
    backtracks to S_{c_X});
  - (b) for ℓ ≠ ℓ_0 and y ∈ ℓ, Z^σ_y = S_{c_X}^-1 α_{yσ} u_ℓ β_{yσ}, with α, β products of in-block links (L0), and
    u_ℓ occurs in no other Z of b, in no Z or reference of any other coarse link, and not in S_{c_X};
  - (c) u_{ℓ_0} occurs only in S_{c_X} (and in the identically trivial Z of (a)).
  - Proof: straight legs cross exactly one block face, at the transverse position of their line; axial paths stay in
    their block (L0); distinct coarse links own distinct faces. ∎
- **[S4] Lemma H1 (one step from i.i.d. Haar): PROVEN-HERE.** If the input links are i.i.d. Haar on SU(N), the S4''
  output (odd branch rule) is V'_b = W_b e^{X̄_b} with W_b := S_{c_X}, and:
  - (i) the W_b are i.i.d. Haar (products of L i.i.d. Haar links over pairwise disjoint link sets);
  - (ii) E||X̄_b||_HS^2 ≤ m_N (L^{d-1} - 1) / L^{2(d-1)}, with m_N := E_Haar||Π_0 log U||_HS^2 (Π_0 the traceless
    projection; m_2 = 2π^2/3 - 1 = 5.58; m_N ≤ Nπ^2);
  - (iii) w_0(K = 1) ≥ 1 - 4 (m_N (L^{d-1} - 1))^{1/2} / L^{d-1}.
  - Proof. X̄ = avg_{(y,σ)} Π_0 log Z^σ_y in both branches of S4'' (on D' each log is already traceless, L1b). Let G be
    the σ-algebra of all links except {u_ℓ : ℓ ≠ ℓ_0}. Given G, the u_ℓ (ℓ ≠ ℓ_0) are i.i.d. Haar (product measure),
    so by H0(b) each Z^σ_y with y ∈ ℓ is conditionally Haar, and E[Π_0 log Z | G] = 0 (Haar is inversion invariant,
    and Π_0 log is odd for every Z by the odd branch rule). The line averages W_ℓ := (1/n) Σ_{y∈ℓ,σ} Π_0 log Z^σ_y
    (n = d! L^d) are conditionally independent and centred, and the centre line contributes 0 (H0(a)). By Jensen within
    a line, E[||W_ℓ||^2 | G] ≤ (L d!/n)^2 m_N = m_N L^{-2(d-1)}. Summing over the L^{d-1} - 1 lines gives (ii).
    For (iii): W_p := W_1 W_2 W_3^-1 W_4^-1 is Haar by (i), so E N^-1 Re tr W_p = 0, and
    |N^-1 Re tr V'_p - N^-1 Re tr W_p| ≤ ||V'_p - W_p|| ≤ Σ_i ||e^{X̄_i} - 1|| ≤ Σ_i ||X̄_i||_HS; Cauchy-Schwarz and (ii). ∎
  - The bound (iii) is useful only when 16 m_N (L^{d-1}-1) < L^{2(d-1)}. **[R4-fix]** The range L ≥ 5 below is for SU(2)
    only; m_N grows with N (m_N ≤ Nπ^2), so larger N needs larger L. For SU(2), d = 4, L ≥ 5 (w_0(1) ≥ 0.16 at L = 5,
    ≥ 0.49 at L = 7); it is vacuous at L = 3, where c12 measures 0.996.
  - Check c14 (H1a-c, 12/12): measured E||X̄||_HS^2 = 0.043 (bound 0.199; d = 4, L = 3), 0.186 (0.551; d = 3, L = 3),
    0.044 (0.214; d = 3, L = 5), 0.637 (1.240; d = 2, L = 3); the straight-transporter plaquette is Haar within 4 s.e.
- **[S4] Why H1 does not iterate, and the sufficient reduction (OPEN).** After one step the field is W e^{X̄}, not Haar,
  and H1's proof uses exactly that the crossing links are conditionally Haar. What survives at every level is H0's
  independence: conditional on all fine links except one designated fine crossing link per level-j crossing link, the
  level-j crossing links are conditionally independent (each is a function Φ_b(u*_b; G) of its own designated fine
  link, by H0(b)-(c) applied at each level). What is lost is centring: the conditional law λ_b = Φ_b#Haar need not be
  Haar (in the domain, Φ_b is nearly constant: the averaged log pulls V toward the mean of the T's).
  - **E7.0'-TV (sufficient condition, OPEN).** If, for every K, the conditional laws λ_b of the level-1 crossing links
    (the input of the last step 1 → 0) satisfy TV(λ_b, Haar) ≤ τ, then the H1 argument at the last step
    gives w_0(K) ≥ 1 - 4(√((m_N + 2τNπ^2)/L^{d-1}) + 2πτ√N) - 2τ (bias of each centred term ≤ 2τ||Π_0 log||_∞ ≤ 2τπ√N; the bias adds
    coherently over lines, the centred part as in H1). So E7.0' ⇐ E7.0'-TV with τ small and L large. Neither the TV
    closeness nor its K-uniformity is proven.
  - Diagnostic c14 (d = 2, L = 3, β = 0; no criterion): w_0(K) = 0.994 ± 0.014, 1.030 ± 0.027, 0.985 ± 0.030,
    0.998 ± 0.034, 0.905 ± 0.067 for K = 1..5 (400/100/60/40/12 samples; coarse torus side 2); first-run values with 4
    samples at K ≥ 3 kept in c14_out_firstrun.txt. Consistent with w_0 ≈ 1, nothing about the liminf, and d = 2 only.
- **Price.** S4'' is discontinuous on the branch set. Weak-limit arguments that pass A through the limit (consistency
  A_*ν_{m+1} = ν_m) need ν_{m+1}-small mass near the branch set *at level m+1*. That is exactly E8*.
- **Why not a physical-size Wilson loop as RC.** It is continuous and K-uniformly tunable (value 1 at β = 0), but its
  perimeter self-energy (∝ g^2 × length/ε in 4D) drives it to 0 along AF sequences, so it has the same defect as S5.
  This is a heuristic remark, not a proof.

**E8* (replacement for E8; OPEN).** For every K ≥ m + 1, every M and every resolution-m link b, with δ_0 > 0 fixed:
μ_{K,M}(the step m+1 → m at b is within δ_0 of failing, i.e. some ||Z^σ_y - 1|| ≥ τ - δ_0) ≤ ε(g_m), with ε(g) → 0 as
g → 0, plus the Peierls form μ(all of b_1, ..., b_r) ≤ ε(g_m)^r for links with disjoint regions. Here g_m is the running
coupling at resolution m. E8.2 is E8* at m = K - 1 with ε = 2L^4 q̄(t/A_L). The difficulty is the coarse levels, where
neither the Wilson form nor site-reflection RP is available for the law of V^(m+1).
- **What E8* buys.** Consistency A_*ν_{m+1} = ν_m of the limit points (S4'' is continuous off the branch set), and,
  with E7.0', a K-uniform RC.
- **Plausible route (not verified).** Ratios of constrained to unconstrained partition functions, as in Balaban's polymer
  representation, where they differ only by polymers touching b; the per-scale weight e^{-c p(g_m)^2}. The session-1
  sum Σ_j L^{4j} e^{-c p(g_j)^2} < ∞ is NOT the relevant condition (it would control "all steps succeed", which E8.3 shows
  is false); the relevant condition is per-scale smallness of ε(g_j) with polymer entropy, which holds for any p > 0.

**[S4] E8* at depth k ≥ 1: fixed-depth bounds PROVEN-HERE, the reduction of all depths to a homogeneous constrained-stability
statement PROVEN-HERE, general depth OPEN.** Notation: the step m → m-1 is the (k+1)-th averaging step, k = K - m (E8.2 is
k = 0). F_b(t) := {some Z^σ_y of the step m → m-1 at the level-(m-1) link b has ||Z - 1|| ≥ t}; Z is built from V^(m).
Constants: A_L = (d-1)L(L-1)/2, c = 4 arcsin(1/4) = 1.0107, C_1 := L^2 + 4cA_L (= 45.4 for d = 4, L = 3).
Torus convention [S4]: the fine side is 4L^{K+M}, so the level-m side 4L^{M+m} is divisible by 4 at every level (the S3
"even" convention is a special case of what E8.1 needs, and every S3 statement holds verbatim).

- **Lemma E8*-sup (one step, deterministic): PROVEN-HERE.** Let R be a union of level-j blocks and suppose every level-j
  plaquette with all links in the two-block regions of the level-(j-1) links inside R satisfies ||1 - V_p|| ≤ η, with
  A_L η ≤ τ_N/2 (τ_N = min(1, 2 sin(π/N)); **[R4-fix]** session 4 wrote 1/2, which is enough only for N ≤ 12: at N = 13
  the central element e^{2πi/13}·1 has ||Z - 1|| = 0.479 ≤ 1/2 but its principal log has trace 2πi, so S4'' ≠ S4'). Then every level-(j-1) plaquette whose four links have their two-block regions inside R satisfies
  ||1 - V'_p|| ≤ C_1 η.
  - Proof. Ribbon (L1e/E8.2; an identity valid for every lattice gauge field): ||Z^σ_y - 1|| ≤ A_L η ≤ τ_N/2 [R4-fix], so every
    step is in D'_N, S4'' = S4' (L1b), and ||log Z|| ≤ c ||Z - 1|| (θ/(2 sin(θ/2)) is increasing in θ and equals c where 2 sin(θ/2) = 1/2). Hence
    ||X̄|| ≤ cA_L η and ||U' - S_c|| = ||e^{X̄} - 1|| ≤ cA_L η for each coarse link. For a coarse plaquette, the straight
    transporters close to the holonomy S_p of an L×L square of level-j plaquettes, a product of L^2 conjugated
    plaquettes, so ||1 - S_p|| ≤ L^2 η (telescoping with unitaries). Telescoping again,
    ||V'_p - S_p|| ≤ Σ_{i=1}^4 ||U'_i - S_i|| ≤ 4cA_L η. ∎ (τ_N/2 ≤ 1/2, so c computed at 1/2 still bounds the log.)
  - **[R4-fix] Alternative.** Keep A_L η ≤ 1/2 for all N and use ||Π_0 X|| ≤ 2||X|| in S4''; then C_1 = L^2 + 8cA_L.
- **Proposition E8*-k (fixed depth): PROVEN-HERE (given E8.1).** For every k ≥ 0, every K ≥ k + 1, every M and every
  level-(m-1) link b (m = K - k), with t ≤ 1:
  μ_{K,M}(F_b(t)) ≤ 2L^{d(k+1)} q̄(t / (A_L C_1^k)),
  and for links b_1, ..., b_r with pairwise disjoint fine regions, μ(all F_{b_i}(t)) ≤ (2L^{d(k+1)} q̄(t/(A_L C_1^k)))^r.
  Uniform in K and M; q̄ is the fine chessboard constant of E8.1 at β_K.
  - Proof. If every fine plaquette in the fine region of b (two level-(m-1) blocks, 2L^{d(k+1)} fine sites) has
    ||1 - U_p|| < η_0 := t/(A_L C_1^k), then by k applications of E8*-sup (the domain hypothesis of the j-th application, j = 0..k-1,
    is A_L C_1^j η_0 = t C_1^{j-k} ≤ t/C_1 ≤ τ_N/2 [R4-fix: this needs t ≤ C_1 τ_N/2, automatic for t ≤ 1 unless
    sin(π/N) < 1/C_1, i.e. N ≳ 140 at L = 3, d = 4]; L0 keeps all
    regions nested inside the fine region of b), every level-m plaquette in the region of b is < t/A_L, so by the ribbon
    every Z of the step is < t: F_b(t) fails. Contrapositive, union over the ≤ 2L^{d(k+1)} fine cells whose lower corner
    lies in the region, then E8.1(i); disjoint regions give distinct cells. ∎
  - With E8.1(iii): μ(F_b(t)) ≤ 2L^{d(k+1)} poly(β) exp(-β t^2 / (8N A_L^2 C_1^{2k})). This is small iff
    β ≫ A_L^2 C_1^{2k} (k log L + log β), i.e. for the top k ≤ k_*(β) ≈ log β / (2 log C_1) levels only. Along an AF-rate
    sequence (β_K ~ K, imported L4a) that is ~ log K / (2 log C_1) levels out of K: a vanishing fraction.
- **Proposition E8*-ob (the deterministic induction is sharp): PROVEN-HERE.** For U(1) ⊂ SU(2) (or SU(N)) with constant
  flux η per (1,2)-plaquette (one flux quantum, η = 2π/S^2 on the fine torus of side S), the level-k coarse field has
  constant flux exactly L^{2k} η per coarse (1,2)-plaquette while L^{2k-2}A_L η < π/3, so
  ||1 - V^(m)_p|| / max ||1 - U_p|| = sin(L^{2k}η/2)/sin(η/2) ~ L^{2k}.
  - Proof. All transporters lie in one U(1), so they commute and log Z = i(enclosed signed flux)·σ_3 inside the principal
    branch. Loop fluxes are gauge invariant and, for constant field strength, depend only on the loop's shape, so the
    averaged log of link (X, X+e_μ) depends only on μ; in a coarse plaquette the four averaged logs cancel in pairs and
    the coarse flux is the straight square's flux L^2 η. The coarse field again has constant flux; induct. ∎
  - Check c13(B): flux L^2η and L^4η reproduced to 1e-9 (d = 3, L = 3, ratios 9.00, 80.48). Check c13(A): the sup lemma
    holds on random small fields (ratio 0.46 at one step, 0.19 at two, against C_1 = 33.3, C_1^2 = 1106); random
    roughness contracts under averaging, coherent flux grows by L^2 per step.
  - **Consequence.** Any argument that bounds a level-m failure through the fine-plaquette sup in a region needs a fine
    threshold ≲ t L^{-2k} and hence β ≳ L^{4k}. The deterministic route cannot give E8* at depths k ≳ log β.
  - **Energy-entropy reading (heuristic, not proven).** A coherent level-m flux φ costs Wilson action ~ β φ^2 (scale-free:
    Σ_p ||1 - U_p||^2 ≥ φ^2 in the abelian linearised case, by Cauchy-Schwarz over the L^{2k} parallel spanning surfaces),
    but the typical fluctuation energy in a level-m block is ~ L^{dk}/β. Energy bounds alone therefore also need
    β ≳ L^{4k}. Separating the coarse-mode cost from the fluctuation free energy is the multiscale effective action
    (L4-L6), not a shortcut around it.
  - **[R4-fix] Scope of E8*-ob.** It rules out only inductions through the fine-plaquette sup (sup-to-sup bounds have
    constant ≥ L^{2k}). Inductions on other quantities (L^2-type norms, polymer norms, level-wise probabilistic
    re-seeding) are NOT excluded.
- **Proposition E8*-red (coarse chessboard; reduction of every depth to a homogeneous bound): PROVEN-HERE (given L8c with
  S4'' and L9a).** Fix m. For s ∈ {0,1}^d let F_s be the family of level-m cells C_t = t + {0,1}^d, t ∈ s + 2Z^d (2^d
  level-m sites each; the cell event may use the level-m links with both ends in C_t). Let G_C(η) := 1[some level-m
  plaquette in C has ||1 - V_p|| ≥ η] and q̄_m(η) := ν_m(G_C(η) for every C ∈ F_0)^{1/n_c}, n_c = (2L^{M+m})^d, ν_m the law
  of V^(m) under μ_{K,M}. Then:
  - (i) ν_m(all C ∈ R bad) ≤ q̄_m(η)^{|R|} for every set R of cells of one family;
  - (ii) μ(F_b(t)) ≤ 2L^d q̄_m(t/A_L) for every level-(m-1) link b, and μ(all F_{b_i}(t)) ≤ (2L^d)^r q̄_m(t/A_L)^{r/2^d} for
    links with pairwise disjoint regions.
  - Proof of (i). The planes of F_s's cell boundaries are level-m link planes (resolution-m block boundaries = fine link
    planes, L odd). There are 2L^{M+m} cells per direction (even), and the antipode of a boundary plane (shift 2L^{M+m})
    is again a boundary plane, so each reflection splits the torus into two halves of L^{M+m} cell-slabs. ν_m is RP for
    these reflections for bounded measurable F (not only continuous f as in L8c): F∘V^(m) is a bounded measurable
    function of the positive-half fine links (L0), V^(m)[θU] = θV^(m)[U] everywhere (S4'' odd rule), and the fine
    link-plane RP of L9a holds for bounded measurable gauge-invariant F (its written proof uses only integrals of F
    against the gauge-fixed product measure; G_C is gauge invariant because ||1 - V_p|| is conjugation invariant) and θ(G_C) = G_{θC} (V[θU] = θV[U];
    ||1 - V_p|| is invariant under the orientation reversal). The E8.1(i) maximiser/run-doubling argument then applies
    verbatim with cells C ∈ F_s; translation invariance (L8b) gives the same q̄_m for every s. ∎
  - Proof of (ii). Ribbon at level m: F_b(t) ⊂ ∪_p {||1 - V_p|| ≥ t/A_L} over level-m plaquettes in the region of b; each
    such p lies in the cell with its lower corner, of one of the families; ≤ 2L^d lower corners; union bound and (i)
    with |R| = 1. For r links: union over one lower corner per link; for each choice, the largest single-family subset
    has ≥ r/2^d distinct cells. ∎
  - **What it buys.** E8* at every depth follows from the HOMOGENEOUS, translation-invariant bound
    **E8\*\* (constrained stability; OPEN):** q̄_m(η) ≤ ε(g_m) for fixed η > 0, uniformly in K ≥ m and M, with ε(g) → 0
    as g → 0. It is a ratio of partition functions, Z_K(every level-m cell of F_0 contains an η-large coarse plaquette)
    / Z_K ≤ ε^{n_c}: a statement of the same type as UV stability (L6), with the large-field constraint imposed in every
    cell. Whether Balaban's large-field estimates (L5) give it is [unverified-exact-statement]. E8*-k is the trivial
    bound q̄_m(η) ≤ (2L^k)^d q̄(η/C_1^k) (choose one fine cell per coarse cell; E8.1(i)), consistent with (ii).
- **Status of E8* after [S4].** PROVEN-HERE for each fixed depth k (constants uniform in K, M; useful for β ≫ C_1^{2k});
  for depths k ≳ log β it is reduced (sufficient condition) to E8**, OPEN. E8*-ob shows the induction through the
  fine-plaquette sup cannot close the general case [R4-fix]. Literature [S4]: Project Euclid (CMP back volumes) returned a bot-detection page
  (Incapsula); not bypassed. Dimock, "Ultraviolet stability for QED in d = 3", arXiv:2009.01156 [v-R4; body read-skim in S5, see L6loc [S5] and literature/NOTES.md]: abstract read
  ("an ultraviolet stability bound in a fixed finite volume", Balaban's formulation, weak coupling); body not read; no
  E8**-type statement in the abstract.

**[S5] Literature re-verification and E8** reassessment (session 5).** Source notes with page and equation references are
in `literature/NOTES.md`; tags there are [read] / [read-skim] / [not-read]. Every Dimock statement below was read in the
arXiv text. Every Balaban statement is still [not-read].

- **What E8** is, after reading. No source I read states E8** (a probability bound on a level-m constrained event) as a
  theorem. Dimock bounds densities and partition functions, never such a probability. The mechanism that would prove
  it is, however, stated explicitly in two places:
  - **Dimock III (arXiv:1304.0705), Lemma 13 (p.24, eq. 166).** In every cube where the level-j small-field condition on
    the level-j RG variables fails, the level-j effective action supplies e^{-c_2 p_j²}. The proof (p.25) goes through
    Lemma 20 (p.35, eq. 246): fine free action ≥ c_0 × the coarse gradient energy of the block variables. Theorem 2 and
    Corollary 1 (p.33) then sum the histories.
  - **Dimock QED (arXiv:2009.01156), Lemma 23 (p.64, eq. 471).** The gauge-field version. A large field at level k+1
    forces |dA_k| ≥ (CM)^{-1} p_{k+1} nearby, by ONE step of the regularity bound (478). The cost is charged to that
    level's own action ½||dA_k||², through ζ ≤ exp(-p + (CM)² p^{-1} ||dA_k||²) (479).
  - In both, **the sup bound crosses exactly one level and is never iterated**: each level re-seeds from its own action.
    That is the escape from E8*-ob, which rules out only iterated sup-to-sup inductions [R4-fix]. It is also why, in
    Balaban's set-up, the small-field conditions are dimensionless per level.
  - [Inference, not read] In d = 4 the dimensionless conditions allow fine field strengths up to ~L^{2(k-j)} at depth
    k - j; QED p.8, eq. 41 has L^{(3/2)(k-j')} in d = 3. That is exactly the L^{2k} growth of the E8*-ob constant-flux
    field, so that field is a *small-field* configuration at the coarse level. It is an obstruction to the sup
    induction, not to Balaban's.
- **Verdict on E8**.** E8** is NOT new content. It is the probability-level form of "large-field suppression per level
  (L5-type) + stability of the remaining integral (L6-type)", and it would follow from Lemma E8**-dens below once the
  level-m effective density obeys (D_m). It is NOT marked IMPORTED, because no source states it. Its status is
  **OPEN (import target: corollary of L5 + L6)**. The scalar template (Dimock III, Lemma 13 + Theorem 2) and the abelian
  template (QED, Lemma 23 + Theorem 2) are [read]. The 4D SU(N) source would be Balaban CMP 122 (1989) 175-202 and
  355-392, with CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285 [not-read].
  - **Caveat.** Balaban's RG variables are his own averaging (CMP 98 (1985) 17-51 [not-read]). Dimock's QED averages the
    gauge potential linearly, with block axial gauge fixing (2009.01156, p.2, eq. 4). Whether either equals S4' is
    unverified. A (D_m) for Balaban's variables transfers to S4' only through a comparison of the two maps.
- **Lemma E8**-dens (reduction of E8** to an effective-density bound): PROVEN-HERE.**
  - Setting.
    - Let ν_m, the law of V^(m), have density ρ_m with respect to product Haar on the n_ℓ = d·|Λ_m| level-m links.
    - **(D_m):** ρ_m(V) ≤ e^{C_+ n_ℓ} Π_{C∈F_0} w_C(V|_C), where 0 ≤ w_C ≤ 1, and w_C ≤ ω whenever C is η-bad.
  - Claim: q̄_m(η) ≤ e^{d 2^d C_+} ω.
  - Proof.
    - ν_m(every C ∈ F_0 bad) = ∫ Π_C 1[C bad] ρ_m dHaar ≤ e^{C_+ n_ℓ} ω^{n_c}. This uses Haar mass 1, and the fact that
      the cells of F_0 have disjoint link sets.
    - n_ℓ = d 2^d n_c. Take the n_c-th root. ∎
  - **Gibbs case.** Take w_C = exp(-a Σ_{P⊂C} (1 - N^{-1} Re tr V_P)). By (B) below, ω = e^{-aη²/(2N)}. So E8** holds
    with ε(g) = exp(d 2^d C_+ - aη²/(2N)), provided a(g_m)η²/(2N) - d 2^d C_+(g_m) → ∞. For example, a ~ c/g_m² and
    C_+ = O(1 + log(1/g_m)), where the log is the Gaussian normalisation.
  - **Balaban-type case.** Suppose the factor is per M-cube, ≤ e^{-c p(g_m)²} whenever the cube is large-field (Dimock
    III Lemma 13 form). A cube containing a bad 2-cell is large-field once η exceeds the level-m small-field threshold.
    Then q̄_m ≤ exp(d 2^d C_+ + (2/M)^d (C - c p(g_m)²)) → 0.
  - (B) **[S5] Inequality, PROVEN-HERE.** 1 - N^{-1} Re tr U = ||1 - U||_HS²/(2N) ≥ ||1 - U||_op²/(2N). Expand
    ||1 - U||_HS² = 2N - 2 Re tr U; then HS ≥ op. Check c16(B).
- **Lemma A1 (abelian averaging is action-contracting, sharp constant L^{4-d}): PROVEN-HERE.** For real link fields A on
  the fine torus, linearise S4' to A'(X, X+e_μ) := avg_{σ,y} A(T^σ_y). The same holds for compact U(1) whenever every
  loop flux involved lies in the principal branch, by the E8*-ob argument. Then:
  - (i) dA'(P) = avg_{y∈B(X)} Φ_A(sq_y), where sq_y is the straight L×L square with lower corner y in the plane of P.
  - (ii) Σ_P |dA'(P)|² ≤ L^{4-d} Σ_p |dA(p)|². **[R56-fix]** The constant L^{4-d} is the supremum over torus sizes,
    approached by long-wavelength modes; it is not attained for real A on a torus (a constant F is closed but not in
    Ran d, since its flux through a coordinate 2-torus is nonzero). Equality is attained for compact U(1) with a
    quantised constant flux inside the principal branch.
  - Proof of (i).
    - Pair the four links of P with the SAME σ and translated y: y, y + Le_μ, y + Le_ν, y.
    - The axial legs P^σ(c_{X+e_μ} → y + Le_μ) at the end of link 1 and at the start of link 2 coincide. In the abelian
      sum they cancel, and likewise at the other corners.
    - What remains is c_X → y, the square, and y → c_X. The flux of that loop is Φ(sq_y).
    - Averaging is linear, so the pairing is legitimate. ∎
  - Proof of (ii) (Schur test).
    - The weight of fine plaquette p in row P is w_P(p) = L^{-d} #{(y, a, b) : y ∈ B(X), y + a e_μ + b e_ν = p}.
    - It vanishes unless p_⊥ = y_⊥ (one value per transverse coordinate). In each in-plane coordinate it is a tent of
      height ≤ L.
    - Row sums: Σ_p w_P(p) = L^{-d} · L^d · L² = L².
    - Column sums: summing the tents over in-plane blocks gives L per coordinate, so Σ_P w_P(p) = L^{-d} · L · L = L^{2-d}.
    - Hence ||M||² ≤ L² · L^{2-d} = L^{4-d}. Constant row and column sums make the constant vector extremal for M on
      all plaquette fields; on Ran d it is approached, not attained [R56-fix]. ∎
  - Iterating, the level-m action is ≤ L^{(4-d)k} times the fine action. **In d = 4 the coarse action never exceeds the
    fine action, at any depth.** Contrast E8*-ob, where the sup grows like L^{2k}: the constant-flux field has equal
    action at every level. **[R56-fix]** "Equal action at every level" holds for the quadratic action only; for the
    cos action of compact U(1) the ratio of that mode is 0.81 at the c18b flux.
  - Cross-check with Dimock [read]: in d = 3 the per-step constant L is exactly the growth e_k² = L^k e_0² of the
    dimensionless QED coupling (2009.01156, p.2, eq. 7). For this linear map, "super-renormalizable" and "marginal" are
    the cases L^{4-d} > 1 and = 1.
  - This is the gauge analogue, in the dual direction, of Dimock III Lemma 20 (fine action ≥ c_0 × coarse gradient
    energy).
  - Check c16(A1): the identity holds to 1e-14 (d = 2, 3, 4; L = 3). ||M||² = 9, 3 and 1.000000 = L^{4-d} exactly. A
    two-step d = 2 run gives ratios ≤ L². The check is 11/11, 3 s, 69 MB.
- **Proposition A2 (E8** for the 4D Gaussian abelian model, all depths, uniform in K, M): PROVEN-HERE.**
  - Model. Noncompact abelian gauge field. The law of F = dA is N(0, β^{-1} Π_{Ran d}) on the fine plaquettes, i.e.
    e^{-(β/2)||dA||²} with any complete gauge fixing. Levels are built with the linearised S4'.
  - Claim. Let d = 4, and call a level-m cell bad if some plaquette in it has |F^(m)_P| ≥ η. Then for every set R of
    cells of one family:
    μ(every C ∈ R bad) ≤ (2^{n_pc/2} e^{-βη²/4})^{|R|}, where n_pc = C(d,2) 2^{d-2} = 24.
    So E8** holds with ε = 4096 e^{-βη²/4}, in the |F^(m)_P| ≥ η form, at every depth; the chessboard RP step is not
    even needed. **[R56-fix: scope]** The session-5 sentence "Through E8*-red(ii) this gives E8* at every depth" is
    WITHDRAWN: E8* and E8*-red(ii) concern the compact S4''/S4' steps and their domain events, and the noncompact
    Gaussian averaging is linear with no domain. An E8* statement for this model would need E8* defined through the
    compact embedding U = e^{iA}, plus a proof that the compact domain events are controlled by the linear F^(m) (they
    are while every flux stays in the principal branch, itself an E8*-type event). Not done. (The badness notions are
    compatible: ||1 - e^{iF}|| ≤ |F|.)
  - Proof.
    - By A1, F^(m) = M_m F with ||M_m|| ≤ 1.
    - Let Φ be the vector of the r = n_pc |R| level-m plaquettes of the cells in R. It is Gaussian with covariance
      C = β^{-1} M_R Π M_R^T, and ||C|| ≤ β^{-1}.
    - On the event, choose one bad plaquette per cell (the cells are disjoint). Then Q := |Φ|² ≥ |R| η².
    - For s = β/4: E e^{sQ} = det(1 - 2sC)^{-1/2} ≤ (1 - 2s/β)^{-r/2} = 2^{r/2}.
    - Markov: μ ≤ e^{-β|R|η²/4} 2^{r/2}. ∎
  - In d < 4 the same proof gives β_eff = β L^{(d-4)k}: the free coupling grows, as it should in a super-renormalizable
    model.
  - **What A2 shows, and what it does not.**
    - It shows that E8** is consistent and natural: it holds at every depth in the free 4D theory, where E8*-ob's
      sup-growth is present.
    - It also shows that the right quantity is the action (an L² object), not the sup. This is the "inductions on other
      quantities" escape that REVIEW_S4 flagged.
    - It is not SU(N). There the coupling runs, and the measure is non-Gaussian: the fluctuation integral replaces β_K by
      ~β_m. That replacement is L3g + L4a + L6, and (D_m) packages it.
- **A1-NA (OPEN, new).** For SU(N) with S4', on small-field configurations:
  Σ_P (1 - N^{-1} Re tr V'_P) ≤ (1 + o(1)) L^{4-d} Σ_p (1 - N^{-1} Re tr U_p).
  - The ribbon estimate of E8*-sup gives only C·L². The abelian cancellation of the axial legs is exact only at linear
    order; nonabelian legs conjugate.
  - This is the classical (tree-level) half of (D_m). Its likely Balaban counterpart is the variational analysis of CMP
    102 (1985) 277-309 [not-read].
  - **[S6] Status: proven in the one-step form A1-NA(1) below (OPEN → PROVEN-HERE), with a k-uniform corollary on the
    L1e domain.**

**[S6] Lemma A1-NA(1) (one-step non-abelian action bound, local form): PROVEN-HERE.**
- **Setting.**
  - Any d; one averaging step, S4' or Balaban's (0.4) (their linearisations coincide, L1d [S6]); G = SU(N).
  - For a fine plaquette p, let X_p = log U_p (principal), with |·| the Hilbert-Schmidt norm. **[R56-fix: branch]**
    "Principal" means every eigen-angle in (-π, π]; it is NOT the S4'' odd branch rule, under which a plaquette with
    an eigenvalue -1 would get X_p = 0, satisfy φ_R ≤ φ_0 and still have s(U_p) ≥ 2/N, breaking (b) and (c).
  - **[R56-fix]** Hypothesis: the coarse torus side is ≥ 3 coarse sites, so that W_P does not wrap (S4 [S4] gives side
    ≥ 4; c18's coarse side 2 violates it, which is harmless for a check).
  - For a coarse plaquette P, let W_P be the union of the 4 fine blocks at its corners. It contains every path used by
    P's four links (L0), and it is a box, so it is simply connected. Let W̃_P be its fine plaquettes.
  - For a set R of coarse plaquettes, put R̃ := ∪_{P∈R} W̃_P and φ_R := max_{p∈R̃} |X_p|.
- **Claim.** There are φ_0 = φ_0(L, d, N) > 0 and C_6 = C_6(L, d, N) < ∞ such that, if φ_R ≤ φ_0:
  - (a) Σ_{P∈R} |log V'_P|² ≤ (L^{4-d} + C_6φ_R) Σ_{p∈R̃} |X_p|²;
  - (b) the same with |X|² replaced by the Wilson density s(U) := 1 - N^{-1} Re tr U on both sides, with C_6 enlarged.
    In d = 4: Σ_{P∈R} s(V'_P) ≤ (1 + C_6φ_R) Σ_{p∈R̃} s(U_p).
  - (c) **One-step large-field transfer (dichotomy).** If Σ_{P∈R} s(V'_P) ≥ η, then either some p ∈ R̃ has
    |X_p| > φ_0, so that s(U_p) ≥ φ_0²(1 - φ_0²/12)/(2N), or Σ_{p∈R̃} s(U_p) ≥ η/(1 + C_6φ_0) (d = 4).
- **Proof.**
  1. **Elementary bounds.**
     - (BCH) If x_1, ..., x_n are anti-Hermitian with s := Σ|x_i| ≤ 1/4, then |log(e^{x_1}⋯e^{x_n}) - Σ x_i| ≤ 9s².
       Indeed, Y := Πe^{x_i} - 1 has |Y - Σx_i| ≤ e^s - 1 - s ≤ s² and |Y| ≤ e^s - 1 ≤ 2s ≤ ½. Then
       |log(1+Y) - Y| ≤ |Y|²/(1 - |Y|) ≤ 8s², using the power series of the principal log for |Y| < 1. The HS norm
       is submultiplicative.
     - If |Z - 1| ≤ ½, then |log Z| ≤ c|Z - 1| with c = 4 arcsin(1/4) (L1e).
     - |e^X - 1| ≤ |X|.
  2. **Local gauge.** Fix P and put the links of W_P in complete axial gauge from a corner of the box. As in L3s(i)
     (ladder of lassos), each a_b := log U^{ax}_b satisfies |a_b| ≤ c·(d-1)·2L·max_{p∈W̃_P}|X_p| =: C_1φ_P.
     Gauge transformations conjugate plaquette holonomies, so |X_p^{ax}| = |X_p|. They also conjugate V'_P (L1a, L0),
     so |log V'_P| is unchanged.
  3. **Linearisation of the coarse plaquette.**
     - Each Z_y used by P's links is a product of ≤ (d+2)L link exponentials e^{±a}. By (BCH),
       log Z_y = (signed sum of the a's on its path) + r_y, with |r_y| ≤ 9((d+2)LC_1φ_P)².
     - So X̄_b = ℓ_b(a) + r̄_b, with |r̄_b| bounded by the same constant.
     - V'_P is a product of 4L straight-link exponentials and four exponentials e^{±X̄_b}. By (BCH),
       log V'_P = Λ_P(a) + R_P, with |R_P| ≤ C_2φ_P² for φ_P ≤ φ_0.
     - Λ_P is the abelian linearised S4' plaquette of the field a, so by Lemma A1(i) Λ_P = avg_y Σ_{p∈sq_y}(da)_p.
     - φ_0 is chosen so that every (BCH) application has s ≤ 1/4 and every Z_y lies in D'_N (so S4'' = S4').
  4. **Fine plaquettes.** (da)_p is the sum of the four link logs, and log U^{ax}_p is the log of their product. By
     (BCH), |(da)_p| ≤ |X_p| + 9(4C_1φ_P)². Hence |Λ_P| ≤ Σ_p w_P(p)|X_p| + L²C_3φ_P², with the A1 weights
     w_P ≥ 0 and row sum L².
  5. **Collect.**
     - |log V'_P| ≤ Σ_p w_P(p)|X_p| + C_4φ_P².
     - φ_P² ≤ φ_R φ_P ≤ φ_R (Σ_{p∈W̃_P}|X_p|²)^{1/2}.
     - With (u + v)² ≤ (1 + φ)u² + (1 + 1/φ)v², φ := φ_R ≤ 1:
       - Σ_{P∈R}(Σ_p w_P|X_p|)² ≤ L² · L^{2-d} Σ_{p∈R̃}|X_p|² by the Schur test of A1(ii). The row sums are L² and the
         column sums, restricted to P ∈ R, are ≤ L^{2-d}.
       - Σ_{P∈R} C_4²φ² Σ_{p∈W̃_P}|X_p|² ≤ C_4² n_W φ² Σ_{p∈R̃}|X_p|², where n_W ≤ 4·d(d-1)/2 bounds how many W_P
         contain a given p.
     - This gives (a) with C_6 = L^{4-d} + 2C_4² n_W.
  6. **(b).** For U = e^X ∈ SU(N) with eigen-angles θ_j:
     - s(U) = N^{-1}Σ_j(1 - cos θ_j), and |X|² = Σθ_j²;
     - (θ²/2)(1 - θ²/12) ≤ 1 - cos θ ≤ θ²/2.
     - So |X|²(1 - φ²/12)/(2N) ≤ s(U) ≤ |X|²/(2N). Use the upper form on the coarse side and the lower form on the fine
       side. The factor (1 - φ_0²/12)^{-1} ≤ 1 + φ_0²/6 is absorbed into C_6.
  7. **(c) [R56-fix: proof replaced].** If φ_R ≤ φ_0, (b) gives η ≤ (1 + C_6φ_R)Σ_{p∈R̃}s(U_p) ≤ (1 + C_6φ_0)Σ s(U_p).
     Otherwise some p ∈ R̃ has |X_p|² = Σ_jθ_j² > φ_0², with θ_j ∈ (-π, π] (principal branch). Put t_j := θ_j² ∈ [0, π²]
     and f(t) := 1 - cos√t. f is increasing and concave on [0, π²] (f'(t) = sin√t/(2√t), and sin x/x decreases on
     (0, π]), with f(0) = 0, so f(t)/t is non-increasing. Take φ_0 ≤ π. If some t_j ≥ φ_0², then f(t_j) ≥ f(φ_0²).
     Otherwise every t_j < φ_0², so f(t_j) ≥ t_j f(φ_0²)/φ_0², and Σ_j f(t_j) ≥ (Σ_jt_j) f(φ_0²)/φ_0² > f(φ_0²). In
     both cases N s(U_p) = Σ_j f(t_j) ≥ 1 - cos φ_0 ≥ (φ_0²/2)(1 - φ_0²/12). The SU(N) constraint Σθ_j = 0 only
     shrinks the feasible set, so it does not affect the lower bound. (Session 6's "contrapositive of (b) plus step 6"
     was not a proof: step 6's lower bound needs every |θ_j| ≤ φ, which fails exactly in this branch.) ∎
  - **[R56-fix] Norm conversion used by A1-NA(k).** For ||1 - V||_op ≤ ½, |log V|_HS ≤ √N||log V||_op ≤
     c√N||1 - V||_op, so c_N = c√N with c = 4 arcsin(1/4).
- **Remarks.**
  - C_6 is finite and computable but grows with L. No attempt was made to optimise it.
  - (c) is the non-abelian, action-form analogue of the one-step mechanism of Dimock QED Lemma 23 (NOTES §4): a
    coarse large field forces either a fine large field or fine action, across ONE step.
  - The sharp leading constant L^{4-d} (= 1 in d = 4) is inherited from A1.
- **Check c18** (SU(2), d = 4, L = 3, fine 6⁴ → coarse 2⁴; 11 s, 422 MB; first run kept as c18_out_firstrun.txt).
  - 6 PASS / 2 FAIL. Criterion (i) R(t_min) ≤ 1 holds for all four fields: smooth abelian, two smooth non-abelian,
    rough.
  - The two FAILs are of the pre-registered criterion (ii), "log-log slope of |R(t) - R(t_min)| ≥ 0.9" (slopes 0.53 and
    0.71). The deviation is non-monotone in t (a linear and a quadratic part of opposite sign), so the slope test was
    ill-posed. The bounded quantity |R - R_0|/φ is ≤ 0.006.
  - Weakness: on a 2⁴ coarse torus these fields have ratios 0.001-0.04, far from the extremal value 1. So c18 does not
    probe the sharp constant.
- **Check c18b** (POST HOC, added after c18; 6 s, 404 MB).
  - Near-extremal background: one flux quantum of constant abelian field in a plane (the A1 extremal mode; ratio
    R(0) = 0.8126, below 1 because of compact-U(1) curvature at this flux), times a smooth non-abelian perturbation.
  - |R(t) - R(0)| ≤ 0.45t for t ≤ 0.04, and the deviation is quadratic (R decreases).
  - 1/1 PASS on its post-hoc criterion. It is an instance, not a test of C_6.
  - **[R56-fix]** c18b lies OUTSIDE A1-NA(1)'s small-φ regime: the coarse plaquette angle is π/2 (9 × 0.1745 per
    eigen-angle), far beyond the coarse-level BCH condition; R(0) = 0.81 is the cos nonlinearity at angle π/2, not a
    near-extremal ratio; and its criterion "C < 10" is effectively unfalsifiable. **It is not a test of the lemma.**
    The pre-registered in-regime test is c18c (below).
- **Check c18c [S7, R56-fix] (in-regime, pre-registered in checks/c18c_criteria.md before the script was written;
  first run; 16/16 PASS; 0.96 s, 66 MB).** SU(2), S4', L = 3; d = 2 with coarse side 5 and d = 3 with coarse side 3;
  principal-branch logs; HS norms; U = exp(tH), H = lowest Fourier modes (abelian τ_3 part plus a smooth τ_1/τ_2 part
  of relative size 0.3), t = 0.0025-0.02. R_ab is computed independently from the abelian linearised S4'.
  - Near-extremal: R_ab/L^{4-d} = 0.789 (d = 2) and 0.508 (d = 3), the largest available on these tori. R_ab is the
    same for both seeds because every component sits on a lowest axial mode, all of which share one eigenvalue of M.
  - In regime: fine φ ≤ 2.2e-2 and coarse |log V'_P| ≤ 0.13.
  - Key step confirmed on these instances: R_log(t) → R_ab, and D(t) = |R_log - R_ab|/φ decreases linearly in φ.
    So the non-abelian correction is O(φ²) here, below the lemma's O(φ), and it is negative (R_log < R_ab ≤ L^{4-d}).
    The reported C_rep = 0, i.e. R ≤ L^{4-d} at every t. |R_s - R_log| ≤ 1.6e-3.
  - Limitation: because L^{4-d} is a supremum that finite tori do not reach (A1 [R56-fix]), the gap L^{4-d} - R_ab
    (21%, 49%) exceeds the non-abelian deviation, so the inequality is not stressed at its exact edge. What is tested
    is that the leading constant is the abelian one, with a correction vanishing as φ → 0, inside the regime.

**[S6] Corollary A1-NA(k) (k-uniform classical action bound on the L1e domain, for S4' iterates): PROVEN-HERE.**
- **[R56-fix: scope]** Proven for **S4' iterates** V^{(j)} = A(V^{(j+1)}) only, because L1e is proven only for S4/S4'.
  The readings "= Balaban's background domain (1.2)" and the minimiser reading below apply it to V = M^k(U_k(V)) with
  Balaban's (0.4) (independent pairing), and need (i) the OPEN item L1e-(0.4) (two-axial-path ribbon variant, L1d
  [R56-fix]) and (ii) the √N conversion between Balaban's normalised-trace |·| and our operator norm. Until then they
  are conditional.
- **Setting.** d = 4 and the hypotheses of L1e: L ≥ 9 odd, F ≤ F_0; level-m torus side ≥ 3 coarse sites. Add F ≤ F_1 := φ_0/(c_N(1 + 4C_δ)), where c_N
  converts ||1 - V_p||_op into |log V_p|_HS (c_N = c√N).
- **Claim.** For all k and all j < k: A(V^{(j)}) ≤ exp(C_6 c_N (1 + 4C_δ) F/(L² - 1)) · A(V^{(k)}), where A is the
  Wilson action Σ s(·) on the respective lattice.
- **Proof.**
  - By L1e(b), the level-(j+1) plaquettes obey |log V^{(j+1)}_p| ≤ c_N(1 + 4C_δ)F L^{-2(j+1)} =: φ_{j+1} ≤ φ_0. By
    L1e(c), every step is in D'.
  - Apply A1-NA(1)(b) with R = all plaquettes at each step: A(V^{(j)}) ≤ (1 + C_6φ_{j+1}) A(V^{(j+1)}).
  - Multiply over the steps and use Σ_{i≥1}L^{-2i} = 1/(L² - 1). ∎
- **What it gives.**
  - On L1e's domain, for S4' iterates (on Balaban's (1.2) for (0.4) only conditionally on L1e-(0.4) and the √N
    conversion [R56-fix]), the classical Wilson action never grows
    under blocking by more than a factor 1 + O(F), uniformly in the number of steps. This is the k-step, non-abelian
    form of A1 in d = 4.
  - For the minimiser U_k(V) (L2 [S6]) it reads A_coarse(V) ≤ e^{C_7F} A(U_k(V)), with C_7 := C_6c_N(1 + 4C_δ)/(L² - 1).
    [R56-fix] This reading is conditional on L2, on L1e-(0.4) (V = M^k(U_k(V)) uses Balaban's M), and on the √N
    conversion.
- **Wall for fluctuating fields.** For general configurations the per-step factors 1 + C_6φ_j multiply. With
  Balaban-type per-level thresholds φ_j ~ g_j, Σ_j g_j = ∞ along (0.31) (compare L4c(c)), so no k-uniform iterated
  bound follows. This is consistent with Balaban/Dimock, who never iterate: they re-seed at each level from that level's
  own action (S5 finding 2). A1-NA(1)(c) is exactly the one-step input of that re-seeding.

**[S6] Proposition LF-count (the unrenormalised per-level large-field count diverges in d = 4): PROVEN-HERE (the
arithmetic); the interpretation is labelled.**
- **Template [read].** Dimock, Rome lectures p.39 (224)-(228) (NOTES §10). Each level-k M-cube in the large-field
  region carries a factor w_k ≤ 1. The sum over large-field regions is bounded by Π_□(1 + w_k) ≤ exp(Σ_k N_k w_k),
  where N_k = (L^kε)^{-4}M^{-4}|T| is the number of level-k M-cubes, and |T| the physical volume. A uniform-in-K bulk
  bound needs C_K := Σ_{k=0}^K L^{4(K-k)} w_k bounded uniformly in K.
- **Claim.**
  - Let g_k obey the upper half of (0.31), 1/g_k² ≤ 1/g² + β'(K - k) log L, and let w_k ≥ e^{-a/g_k²} for some
    a > 0. Then C_K ≥ e^{-a/g²} Σ_{n=0}^K L^{(4 - aβ')n}, which diverges as K → ∞ whenever aβ' ≤ 4.
  - Conversely, if w_k ≤ e^{-a/g_k²} and the lower half of (0.31) holds with aβ > 4, then C_K ≤ e^{-a/g²}/(1 - L^{4-aβ}).
  - In d = 3 (g_k² = g²L^kε, CMP 109 p.259), w_k = e^{-a/g_k²} gives a convergent C_K for every a > 0.
- **Proof.** Substitute: L^{4n}e^{-a(1/g² + β'n log L)} = e^{-a/g²}L^{(4-aβ')n}. The other cases are the same
  geometric or double-exponential sums. ∎
- **Interpretation (labelled).**
  - [inference] For a per-cube large-field factor to be a valid bound, w_k must be at least of the order of the
    Boltzmann weight of the cheapest configuration the small-field indicator excludes, e^{-a/g_k²}. For CMP 109's
    fluctuation cut |B'| < ε_1, that cost is a ≤ ½||Δ^{(k)}|| ε_1² = O(ε_1²).
  - **[R56-fix: one normalisation, Balaban's.]** CMP 109's action is (1/g_k²)Σ[1 - Re tr U] with tr 1 = 1 (NOTES
    §9.1), so 1/g_B² = 2N/g_std², and the perturbative rate in (0.31) is β'_B ≈ 2N·2b_0 = 4Nb_0 = 11N²/(12π²) ≈
    0.0929N² [inference; (0.31) leaves β' unspecified]. The cost a = ½||Δ^{(k)}||ε_1² is also in Balaban's
    normalisation ((2.10)). Divergence (aβ' ≤ 4) then holds when a_B ≤ 4/β'_B = 48π²/(11N²) ≈ 43.1/N² (10.8 for
    SU(2), 4.8 for SU(3)), i.e. for **ε_1 ≲ (8/(||Δ||β'_B))^{1/2}**; with ||Δ|| ≈ 16 this is ε_1 ≲ 1.16 (SU(2)), 0.77
    (SU(3)), falling like 1/N. So the statement holds **for ε_1 small enough** (which is what Balaban assumes),
    conditional on the one-loop rate [inference]; it is NOT shown for O(1) thresholds. The session-6 numbers "a > 86/N,
    a > 43 for SU(2)" mixed normalisations and were a factor 2N too strict; WITHDRAWN. At large N the per-bond
    cheapest-configuration estimate also ignores the N² fluctuation entropy.
  - The single instanton (a = 8π² in the normalisation of L4b) gives aβ' = 11N/3 > 4 for N ≥ 2 (the product aβ' is
    normalisation-independent). So genuinely non-perturbative excursions are summable. The divergence sits in the
    intermediate window O(ε_1²) ≲ a_B ≲ 4/β'_B.
  - [heuristic] Probabilistic counterpart: the level-k fluctuation has variance ∝ g_k², so the expected number of
    threshold-violating bonds per unit physical volume at level k is ~L^{4(K-k)}e^{-cε_1²/g_k²} → ∞. So fine-scale
    "large fields" are dense in d = 4, not rare. The PROVEN counterpart is E8.3: a first step leaves D in a fixed block
    with probability → 1, conditional on the AF rate.
- **Consequence: the exact wall of the reconstruction.**
  - In d = 4 the large-field regions cannot be bounded as rare excursions and then discarded, as in Dimock's d = 3
    template. Their contribution to log Z must itself be renormalised: the vacuum-energy and β_j·A counterterms must be
    applied in large-field regions too, so that the per-cube contribution at level k becomes summable against
    L^{4(K-k)}, as the small-field V^{(j)} are in (0.29)-(0.30).
  - Dimock's description of the R-operation ("converts some large field contributions back to small field
    contributions", II p.31 [read]) and the CMP 122 abstracts [read-abs] are consistent with this being its job. The
    exact statement is [not-read].
  - The same wall blocks E8**/(D_m): E8**-dens needs a K-uniform C_+. The classical part is now proven (A1-NA(1),
    A1-NA(k)). The fluctuation normalisation (L3g, L4a, L6) and the renormalised large-field bound (L5) are not.

**[S6] Large-field reconstruction: outcome.**
- **Route (a), open sources.** No open-access work states Balaban's 4D large-field bound or the R-operation (NOTES
  §10).
  - Found and read: Dimock's Rome lectures (d = 3 counting template, p.39); BFKT 1609.00968 p.4 (per-point extraction
    is "routine" for positive actions, which the Wilson action is); Jaffe-Witten (descriptive); the OSTI abstracts of
    CMP 122.
  - Project Euclid was bot-blocked and not bypassed.
- **Route (b), re-derivation.** Done: the per-level large-field extraction for the bare Wilson action (A1-NA(1)(c),
  plus inequality (B), plus E8**-dens).
  - **Wall (exact):** a renormalised large-field bound, i.e. per-level large-field contributions with the
    vacuum-energy and coupling counterterms applied inside large-field regions, summable against L^{4(K-k)}.
    Proposition LF-count proves that the unrenormalised version cannot be summed in d = 4 for every ε_1 below an
    explicit bound, conditional on the one-loop rate [R56-fix; inference]. The next attempt should construct this renormalisation for a single isolated large-field cube at level
    k in the 4D SU(N) model (a one-cube R-operation), not a further reduction.

**[S5] What the non-abelian 4D version needs beyond Dimock** (each item: what Dimock has [read], and the Balaban source
[not-read]).
1. **Non-abelian averaging and regular-configuration spaces (L1d).**
   - Dimock: only abelian regularity, 1712.10029 Thm 1 (p.43, eq. 327). Dimock calls it "abelian versions of non-abelian
     results" in CMP 99 (1985) 75-102 and CMP 102 (1985) 277-309.
   - Needed: CMP 98 (1985) 17-51 and CMP 99 (1985) 75-102.
2. **Non-linear constrained minimiser (L2).**
   - Dimock: in abelian theories it is a linear operator H_k (2204.07201, p.6, eqs. 22-25). So there is no abelian
     counterpart of the existence, uniqueness and analyticity problem.
   - Needed: CMP 102 (1985) 277-309.
3. **Background-dependent fluctuation propagators (L3g).**
   - Dimock: in QED the gauge propagator is background independent. Its bounds (1512.04373, Lemmas 6, 9, 11) are
     themselves "sketched" with citations to Balaban.
   - Needed: CMP 95 (1984) 17-40, CMP 96 (1984) 223-250 and CMP 99 (1985) 389-434.
4. **Marginal-coupling flow and the small-field effective action in 4D (L4a).**
   - Dimock: only super-renormalizable flows. φ⁴_3 has λ_k = L^k λ_0 (I, eq. 106; Theorem 14, eqs. 179-182). QED has
     e_k = L^{k/2} e_0, and "there are no marginal terms" (2204.07201, p.13).
   - Exponents in the d = 3 analogues: ||E_k(X)|| ≤ e_k^{1/4-7ε} e^{-κ d_M(X)} (QED Prop. 1, eq. 30), and
     β < 1/4 - 10ε (φ⁴, II eq. 212).
   - Needed: CMP 109 (1987) 249-301, CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285.
5. **R-operation (L5).**
   - Dimock: absent from every exposition. "This difficult step is not necessary for this model" (II, p.31, Remark 3);
     QED has none either.
   - Needed: CMP 122 (1989) 175-202 and CMP 122 (1989) 355-392.
6. **UV stability in 4D (L6).** This is the assembly of 1-5.
   - 3D templates: φ⁴_3 III Corollary 1 (p.33, eq. 225), with arbitrary M and bulk dependence; QED Theorem 2 (p.8,
     eq. 42), unit volume, "works equally well for any finite volume" (2204.07201, p.2-3). The 3D pure-gauge template is
     CMP 102 (1985) 255-275 [not-read].
   - The review.md §1 "small physical volume" question is settled for φ⁴_3 (M arbitrary, [read]) but still open for 4D YM.
7. **Scalar coercivity source:** CMP 89 (1983) 571-597 (Dimock III Lemma 20's citation).

- **[S2] Literature status of E8** (Dimock II, arXiv:1212.5562, full-text HTML read via a summarising fetch: data only,
  paraphrased; scalar φ^4 in 3D, not gauge).
  - Large-field regions are defined by characteristic functions χ, ζ with thresholds p_k = (-log λ_k)^p (§1, eq. 10).
  - Each large-field cube contributes e^{-O(1) p_0^2}, so a region Ω^c carries e^{-O(1) p_0^2 |Ω^c|_M}.
  - The result is a sum over decreasing regions Ω_1 ⊃ Ω_2 ⊃ ..., with exponentially decaying polymer activities.
  - **No local, volume-uniform probability bound of E8 type is stated** in the part read (the first 100k of 159k
    characters).
  - So E8 is NOT already in Dimock I-II as a stated result. The structure (a *local density-level* suppression, plus
    local polymers) is exactly what the E8 route needs: a ratio Z(B forced large)/Z ≤ e^{-c p^2} × (polymer
    correction). Whether Balaban's gauge papers state it is unknown [unverified-exact-statement]; their bodies were not
    read. **[S5]** Superseded by the direct reading of Dimock II-III and QED (NOTES.md): the absence of an E8-type
    probability statement is confirmed in the parts read; the density-level mechanism is Dimock III Lemma 13.

### L7. The continuum limit on T^4_M
- **L7.0. Tuning at each fixed K: PROVEN-HERE. Tuning to a K-independent w*: GAP (OPEN, estimate E7.0).**
  [R1-fix: session 1 claimed a fixed w* for all K; that does not follow.]
  - **Definitions.** RC is read with the continuous cut-off observable w̃ = ζ · (1 - N^-1 Re tr V^(0)_p). Here
    ζ ∈ [0, 1] is a continuous gauge-invariant function. It equals 1 when every averaging step inside the four
    resolution-0 blocks of p satisfies ||Z_y - 1|| ≤ τ_N/2, and 0 when some step has ||Z_y - 1|| ≥ 3τ_N/4.
    - τ_N := min(1, 2 sin(π/N)). [R1-fix] For N ≥ 13 the session-1 thresholds 1/2 and 3/4 did not imply D_N.
  - **Statement (per K).** For each K, β ↦ E_{K,β}[w̃] is continuous on [0, ∞) and tends to 0 as β → ∞. Its value
    w̃_0(K) at β = 0 is > 0. Hence every w* ∈ (0, w̃_0(K)) is attained at that K.
  - **The gap.** At β = 0 the links are i.i.d. Haar. ζ = 1 needs about L^{4K} of the Z_y, many with disjoint supports, to
    lie in a fixed ball. So w̃_0(K) → 0 super-exponentially in K, and even sup_β E_{K,β}[w̃] ≥ c > 0 uniformly in K is
    unproven.
  - **Estimate E7.0 (OPEN).** There are c > 0 and β-ranges such that sup_β E_{K,β}[w̃] ≥ c for all K. Its content is a
    large-field suppression statement, of L6/E8 type: with high probability all averaging steps stay in the domain.
    The RC, L7c and LOG decision 1 all need E7.0.
  - **[S3, R3-fix] E7.0 restricted to the AF window is FALSE for N = 2, 3, 4** (E8.3, consequences, threshold 3τ_N/4):
    sup_{β ≤ λK} E_{K,β}[w̃] → 0 for 3λx^2 < 4 ln L. E7.0 itself (sup over all β) is not falsified. The
    cut-off RC is replaced by S5' (L6loc), whose per-K tuning is PROVEN and whose K-uniformity is the Haar statement
    E7.0' (OPEN).
  - **Proof.**
    - Continuity: dominated convergence on the compact configuration space (the integrand is continuous and bounded,
      and the density is continuous in β).
    - w̃_0 > 0: w̃ is continuous, non-negative, and positive on a non-empty open set.
    - β → ∞: by Laplace's principle on the compact space, μ_β concentrates on the flat set {U_p = 1 for all p}.
      - On a flat configuration every Z_y is the holonomy of a null-homotopic loop (zero winding on the torus), so
        Z_y = 1, ζ = 1, and U' = T_{c_X}.
      - Every coarse plaquette is the holonomy of a null-homotopic loop, so it equals 1 and w̃ = 0. This includes flat
        configurations with non-trivial torus holonomy.
      - [R1-fix] Session 1 wrote "contractible union of blocks". That fails when the coarse torus has side ≤ 2; zero
        winding is the correct reason.
    - w̃ is continuous, so E_β[w̃] → 0. Conclude by the intermediate value theorem. ∎
  - That the tuned β_K lies in Balaban's regime for small w* is part of L4a and L6 (imported).
- **L7a. Subsequential limits at every resolution: PROVEN-HERE (content-free alone).**
  - Statement: for any sequence β_K, there is a subsequence along which, for every m, the law ν_{K,m} of V^(m) (a
    probability measure on the compact space C_m = G^{links of Λ_{m,M}}) converges weakly.
  - Proof: Prokhorov on a compact metric space, then a diagonal argument over m ∈ N. ∎
- **L7b. Convergence of the whole sequence: OPEN. The first open estimate of the DAG is E7.**
  - **E7 (trajectory Cauchy estimate).** Assume RC with w* ≤ w_*(N, L). There are κ > 0 and C < ∞ such that for all
    K ≥ m ≥ 0, M ≥ 0, every union X of resolution-m blocks, and every gauge-invariant f : C_m(X) → C with
    ||f||_∞ ≤ 1:
    |E_{K+1}[f(V^(m))] - E_K[f(V^(m))]| ≤ C |X|_m L^{-κ(K-m)},
    where |X|_m is the number of resolution-m blocks in X.
  - E7 is summable in K, so it gives convergence of all of O, with cutoff effects O(ε^κ). It is stated for the
    observable expectations so that it does not depend on Balaban's internal norms.
  - **Sub-estimates (all OPEN).**
    - **E7.1 (one-step comparison).** The (K+1)-theory after one step equals a Wilson action at the tuned coupling plus
      an irrelevant remainder R. R must be measured in Balaban's polymer norm, with size O(g^{2+δ}) or carrying
      L^{-κ}. L4c shows that O(g^2) is not enough.
    - **E7.2 (contraction).** The linearised RG map on Balaban's space of effective actions contracts the irrelevant
      directions by L^{-κ} per step, uniformly for g ≤ g_*, including across the large-field/small-field interface. The
      marginal direction is fixed by RC.
    - **E7.3 (tuning stability).** The tuned β_{K+1} and β_K differ by an amount the marginal flow absorbs, with error
      O(L^{-κK}).
    - **E7.4 (from norms to observables).** A polymer-norm difference of the effective densities on X gives an L^1
      difference of the X-marginals. This is a cluster-expansion ratio bound that uses L6loc.
  - **Note.** In the Dimock/Balaban scalar expositions only the stability bound is proved. No correlation-function
    convergence was found in the abstracts read.
  - **[S2] Toy test of E7 / E7.2: Migdal-Kadanoff SU(2), d = 4, b = 2 (check c7). FINITE DIAGNOSTIC, toy only.**
    - **Map.** Bond moving w → w^{b^2}, then decimation a_n → a_n^{b^2} on the character coefficients. This is an exact
      block map of a hierarchical model [m: A. A. Migdal, Sov. Phys. JETP 42 (1975) 413 and 743; L. P. Kadanoff,
      Ann. Phys. 100 (1976) 359; exactness for gauge models unverified], and an uncontrolled approximation of
      the real 4D RG.
    - **E7 analogue holds.** Tune a_1 = a* after K steps; the tuned resolution-0 weights converge geometrically in K.
      - The per-step ratio of D_K is 0.067 at a* = 0.6 and 0.0636 at a* = 0.9, tending to b^-4 = 1/16 at weak coupling.
      - Four bare families converge to the same limit with the same rate: Wilson, Wilson + adjoint, a large-field bump
        (factor 3 at θ > 2.2), and heat kernel.
      - The tuned β_K grows linearly in K (asymptotic-freedom-like). The implied MK coefficient 0.0457 is close to
        11·2/(48π^2) = 0.0464. This is not claimed as anything.
    - **Rate explained (derived here at leading order in small t; heuristic, since the re-expansion step is not controlled).**
      - Near a heat kernel K_t, a quartic-Casimir deviation u enters log w as (u/t^2) f(θ/√t).
      - Bond moving multiplies log w by p = b^{d-2} and maps t → t/p. Re-expanded on the new width, it gives
        u → u/p^3.
      - Decimation multiplies both t and u by b^2.
      - In d = 4 (p = b^2): t is marginal and u → u b^-4. The measured 1/16 matches.
      - In the real 4D RG the leading irrelevant (dimension-6) operators contract only like L^-2. So the MK rate is
        faster than the expected true κ = 2 (up to logs).
    - **Large fields in the toy.** The bump's effect falls from 7.6e-5 (K = 1) to 2.2e-9 (K = 3) at a* = 0.6. The power
      w^{b^2} suppresses large θ super-exponentially. [R2-fix] This sub-test is VACUOUS: the bump is a pointwise
      deformation that the power w^p kills trivially (at a* = 0.9 its effect is 1e-15). It tests nothing about large-field
      regions. The [S3] toy c11 has spatial large-field regions.
    - **Limits of the toy.** MK has no spatial large-field regions, no small-field/large-field interface, and no
      polymer tails. So it confirms only that the E7 *structure* (RC fixes the marginal direction; everything else
      contracts geometrically; the bare large-field shape is irrelevant) is consistent in an exact block map. It is NOT
      evidence for E7.2 in 4D Wilson theory, and in particular not across the interface.
  - **[S3] Toy test with spatial large-field regions: inhomogeneous MK tree (check c11). FINITE DIAGNOSTIC, toy only.**
    - **Model.** A hierarchical lattice: each node at depth k has 16 children (2^4 sub-blocks). Bond moving sums the
      children's log weights within each of the 4 decimation slots, and decimation multiplies the 4 slot coefficient
      vectors. With all leaves equal this is c7 exactly (T0: 7e-16). Leaves in a region R carry a strong-coupling bare
      weight (β_R = 0 Haar, or 0.5); the rest carry the tuned Wilson weight (homogeneous RC, a* = 0.6). Interface nodes
      have mixed leaves. Criteria were pre-registered in the script before the first run.
    - **T1 (PASS).** A fixed fine-size Haar defect (2^4 leaves straddling every dyadic boundary) affects the root by
      2.1e-3, 1.4e-4, ..., 2.7e-9 at K = 3..8, with per-step ratio 0.066: the volume factor b^-4 = 1/16 again.
    - **T2 (PASS).** A fixed *physical* strong-coupling region (box with 1/16-dyadic corners, β_R = 0.5): the tuned root
      converges in K. The Cauchy differences are 6.9e-4, 6.6e-6, 6.9e-8, 4.6e-9 (ratios 0.0095, 0.0105, 0.066), with
      limit a_1 = 0.590749 against 0.6 without the region. So the E7 structure survives a deterministic large-field
      region of fixed physical size in this toy.
    - **T3 (pre-registered FAIL; a finding).** The per-node sup-norm contraction Δ(parent)/max Δ(children) between runs
      K = 7 and 8 is 0.070 at exterior nodes but **0.667 at interface nodes** (86 node classes), above the
      pre-registered 0.5. The first-run output is kept as checks/c11_out_firstrun.txt; the criterion is NOT changed.
    - **T3b (diagnostic, hypothesis written before running, FALSIFIED).** I predicted the factor a_1(ext slot)^3 → 1 as
      a* → 1, from a lone small-field child that bond moving does not dilute. The measured worst interface ratio is
      0.667, 0.604, 0.617, 0.603 at a* = 0.6, 0.8, 0.9, 0.95, i.e. flat and well below the prediction (0.74 → 0.96). The
      mechanism is not identified.
    - **Reading for E7.2.** In this toy the contraction across the interface is uniform in the coupling but about 10×
      weaker per step than in the bulk (≈ 2/3 vs ≈ 1/16). The global Cauchy rate is still geometric (T2), because
      interface nodes are a vanishing fraction of each level. If the same holds in 4D, E7.2 needs a norm that tolerates
      a slower interface contraction, weighted by the interface's volume fraction, rather than a uniform per-block
      contraction constant. This is a heuristic reading of a toy.
    - **Limits.** Exactly local by construction (a tree): no polymers, no configurations, no random large-field regions.
      The regions here are deterministic bare inhomogeneities, not fluctuations. **[R3-fix]** The box corners are
      1/16-dyadic, so every node at depth ≥ 4 is pure and interface nodes exist only at depths ≤ 3: the toy never
      iterates an interface contraction and cannot say whether the slow factor compounds. "Vanishing fraction" above
      means "finitely many levels". The [S4] check c15 addresses both the mechanism and compounding.
  - **[S4] Mechanism of the slow interface contraction (check c15: 5 PASS / 3 FAIL, 5 s; first run kept as
    c15_out_firstrun.txt). FINITE DIAGNOSTIC, toy only.**
    - **Mechanism (identified).** At an interface node, a decimation slot holding j small-field children and 4 - j
      near-Haar (log w ≈ 0) children performs bond moving with power j instead of b^{d-2} = 4: locally the node is an MK
      step of effective dimension d_eff = 2 + log_2 j. The irrelevant deviation then contracts by ≈ b^2/j^3 at leading
      order (the c7 rate argument with p = j).
    - **Evidence.** A synthetic parent (4 slots of j copies of the c11 exterior node plus 4 - j exact Haar children)
      reproduces the c11 interface class with RRSS slots exactly (0.5266 vs 0.5266, j = 2). The exterior class (0.0704
      vs j = 4: 0.0691) misses the pre-registered 1e-3 tolerance, so H1 is recorded as FAIL. Synthetic ratios
      r(j = 1..4) = 1.12, 0.53, 0.21, 0.069 (a* = 0.6) and 1.20, 0.45, 0.19, 0.065 (a* = 0.9): ordered and coupling-flat
      within 14% (H2, H3 PASS), which explains the flatness that falsified the session-3 hypothesis. The worst c11 class
      (0.667) has interface children, so it is a mixture of j = 2 slots and interface sub-slots.
    - **Prediction confirmed (H4, H5).** A small-field box inside a strong sea has j = 1 slots at its corners. Predicted:
      no per-node contraction. Measured worst ratio 1.1201 (> 1) at a node with slots RRSR × 4, reproduced exactly by the
      synthetic j = 1 model. (Process: H5 first FAILED from a script bug, the synthetic reference being a strong-region
      node in the complement geometry, giving 0; fixed and rerun; the first output is kept.)
    - **Compounding (REVIEW_S3 point 6; H6 FAIL, H6' FAIL, H7 PASS).** Half-space strong region x_2 < 1/3 (non-dyadic,
      so interface nodes exist at every depth). The root response to an adjoint-character perturbation of the first
      small-field leaf layer, divided by the response to the same perturbation of a bulk layer at x_2 = 2/3, is
      0.91, 1.00, 0.92, 1.01, 0.94 for K = 6..10: flat, not increasing (H6 FAIL). Both decay by ≈ 1/2 per K, i.e. like the
      layer volume 2^-K: the root response is dominated by the marginal (coupling) component, which MK averages over
      children (REVIEW_S3's alternative). H7 PASS: the interface response decays (steps 0.47-0.56). H6' (added after the
      first run): removing the component along the tuned family's tangent gives residual ratios 25.4, 5.6, 3.3, 3.3, 2.9,
      decreasing, so FAIL, and the bulk residual itself is erratic (steps 2.47, 1.18, 0.55, 0.59). A single tangent does
      not isolate an irrelevant subspace for a position-dependent perturbation, so H6' is inconclusive by construction.
      INFO: a boundary normal to a decimation coordinate screens completely (the interface-layer response is 0 to double
      precision), because a strong slot makes the parent near-Haar.
    - **[R4-fix] Downgraded.** c15 is a FINITE DIAGNOSTIC, not a proof. The 0.5266 match is a bookkeeping identity (the
      synthetic parent recomputes the c11 slot arithmetic on the same children). The leading-order law b^2/j^3 fits
      poorly (j = 1: predicted 4, measured 1.12; j = 3: predicted 0.148, measured 0.21); only the ordering (H2) is
      supported. The claim "E7.2 needs a geometry-weighted norm" is WITHDRAWN: (1) rests on the j = 1 corners, which
      (3) calls an MK artefact, and the face/bulk rates L^-1, L^-2 are both < 1, so a uniform per-block contraction at
      the slower rate is not excluded; in 4D interfaces arise from random large-field regions handled by L5, whose polymer
      norms are already geometry-weighted. What remains is a toy-informed design note: "the contraction constant should
      be the face rate, or weighted by type". H6 (no compounding beyond the volume fraction) is the useful toy-only
      finding. The original text follows for the record.
    - **Design note for E7.2 (was "Decision", session 4).**
      - (1) A contraction constant that is uniform per block is FALSE in the toy (j = 1 corners: 1.12-1.20 > 1). So E7.2
        cannot be stated as "every block's irrelevant part contracts by L^-κ". It must be stated in a norm that weights
        deviations by their geometric type (bulk, face, corner), or summed over a region with volume weights.
      - (2) In this toy, the influence of an interface on the root does not compound beyond its volume fraction (H6, H7).
      - (3) Real 4D (heuristic, dimension counting only): gauge-invariant local operators have dimension ≥ 4, so a
        face-localised one scales like L^{3-4} = L^-1 per step and a corner-localised one like L^{2-4}. The MK j = 1
        non-contraction has no counterpart in this counting: it is an MK slot artefact (a lone child is an undiluted
        lower-dimensional system). The slower face rate (L^-1 against the bulk L^-2) is generic and must be built into
        E7.2's norm.
      - Not a threat to E7.2 as a statement about expectations; a constraint on its proof.
- **L7c. Non-triviality at resolution 0: CONDITIONAL on E7.0 (moved from PROVEN-HERE). [R1-fix]**
  - w̃ is a function of the fine field, not of V^(0). What holds is E_K[w(V^(0)_p)] ≥ E_K[w̃] = w*, since w ≥ w̃ ≥ 0
    on D. The session-1 "= w*" was wrong.
  - The inequality passes to the limit because w is continuous.
  - So, given a K-uniform w* (E7.0), the limit is not concentrated on pure gauge. [S3] E7.0 fails in the AF window;
    under S5' the same argument needs E7.0' and, to pass w ∘ V^(0) through the limit, E8* at level 1 (w ∘ S4'' is
    discontinuous on the branch set). This is weak; the meaningful version
    is L10.

### L8. Infinite volume
- **L8a. Subsequential limits as M → ∞: PROVEN-HERE.** The laws of V^(m) restricted to any fixed bounded region form a
  tight family on a compact space. By Tychonoff the product over all links of Λ_{m,∞} is compact, so a diagonal
  subsequence (M_i, K_i) converges for every m. ∎
- **L8b. Invariance: PROVEN-HERE in a narrowed form. [R1-fix: the session-1 statement was WRONG]**
  - The limits are invariant under resolution-m lattice translations (period L^-m), and under coordinate reflections
    through block-aligned hyperplanes (by L9a'), for every m along the subsequence.
  - Proof: weak limits of invariant measures are invariant. The torus measures are invariant, and the block map
    commutes with these operations: translations preserve every finer grid, and reflections are covered by L9a',
    which holds everywhere for S4'' with the odd branch rule [R3-fix; session 3 cited the withdrawn "failed link := 1"
    extension here], so V^(m)[θU] = θV^(m)[U] holds everywhere. ∎
  - **Axis permutations are NOT symmetries of the block laws under S4.** S4 fixes the path order 1, 2, 3, 4, so for a
    permutation R, V^(m)[RU] ≠ R V^(m)[U] in general.
  - **[S3] With S4' (order-averaged): the full hypercubic group.** V^(m)[πU] = πV^(m)[U] for axis permutations π
    (S4' re-checks; c8(d)), everywhere for S4'' [R3-fix]. The torus measures are invariant
    under π (the torus side is the same in every direction). So the limits are invariant under resolution-m translations,
    block-aligned reflections and axis permutations about a block centre: the hypercubic group at every resolution.
    PROVEN-HERE (same weak-limit argument). L3s' is unaffected (it uses its own scalar average).
- **L8c. RP is preserved: PROVEN-HERE, given L9a (incl. the mixed reflection L9a-m) and L9a'.**
  - For continuous f supported in a positive half-space union of blocks (for the mixed reflection: excluding the block
    cut by the fixed site plane Π_s, which is a block mid-plane [R2-fix]), ⟨θ(f)^* f⟩ ≥ 0 holds at every (K, M) and is a
    closed condition under weak limits. ∎
  - [R1-fix (a)] The fine torus side L^{K+M} is odd. A reflection through a block-boundary link plane therefore fixes the
    antipodal *site* plane: it is a mixed reflection, and L9a-m covers it.
  - [R1-fix (b), superseded by R3-fix] The measurable extension of the block map off D must be θ-covariant. Sessions 2-3
    set failed coarse links to 1. From session 4 the extension is S4'' with the odd branch rule (S4), which is
    θ-covariant everywhere by the L9a' computation (it uses only log(Z^-1) = -log Z and conjugation covariance, which
    the odd rule makes exact for all Z), and local (L0). So V^(m)[θU] = θ V^(m)[U] holds everywhere.
- **L8d. Uniformity: OPEN.** Non-triviality and consistency in infinite volume need E8 (L6loc) uniform in M.
- **The obstruction, stated exactly.**
  - The RG stops at resolution 0, where g is small. What remains is a lattice gauge theory with compact variables,
    strongly coupled at large distances.
  - Existence of limit points needs no infrared control: L8a is pure compactness.
  - The infrared coupling growth blocks:
    - (1) uniqueness of the infinite-volume state, i.e. independence of the subsequence and of the boundary conditions;
    - (2) clustering (OS4);
    - (3) the mass gap;
    - (4) through (1), the universality route to rotation invariance (L9b-β).
- **What the OpenAI claim must have done (inference, not fact).** Either:
  - (A) stay on T^4. Then OS1 fails, so "OS axioms" would have to be read as torus axioms. Or
  - (B) take infinite-volume limit points by compactness, as here, and solve L9b without uniqueness. Or
  - (C) prove uniqueness on R^4, which seems to require IR control comparable to a mass gap, which is not claimed.
  - (B) is the most consistent with "existence, no mass gap".

### L9. The OS axioms
- **L9a. RP of the Wilson action, link reflection and site reflection: IMPORTED-AND-REVERIFIED.**
  - **Source.** Osterwalder-Seiler, "Gauge field theories on a lattice", Ann. Phys. 110 (1978) 440 [v-R1, via a citing
    paper].
  - **[R4-fix] Scope.** RP holds for bounded measurable gauge-invariant F of the positive-half links, not only continuous
    ones: the written proof integrates F against the gauge-fixed product Haar measure and uses no continuity. E8*-red
    uses this extension.
  - **L9a-m. [S2, R1-fix] Mixed reflection on an odd torus: PROVEN-HERE (re-derived).**
    - Setting: θ fixes one link plane Π_l and, antipodally, one site plane Π_s. Assume side ≥ 3, so the two are distinct.
    - Gauge-fix the crossing links at Π_l to 1, by a gauge transformation on the positive-half sites adjacent to Π_l.
      It does not touch Π_s.
    - The links inside Π_s (call them W) are θ-fixed. Links from Π_s into either half belong to that half. Plaquettes
      inside Π_s are functions of W alone.
    - Then e^{-S} = h(W) e^{A_+(U_+, W)} θ(e^{A_+}) Π_{crossing p at Π_l} exp((β/N) Re tr(G_p θ(G_p)^†)), with A_+ real.
    - Expanding the crossing factors as in L9a and using Haar product structure, for every W:
      ∫ θ(F) F̄ e^{-S} dμ(·|W) = h(W) Σ_α c_α |∫ F Ḡ_α e^{A_+} dμ_+(·|W)|^2 ≥ 0, with c_α ≥ 0.
    - The equality uses that θ preserves the measure and fixes W, and that A_+ is real. Integrating over W ≥ 0 gives
      RP. ∎
    - Not separately checked numerically: c4 covers only pure link and pure site reflections.
  - **Proof re-derived (link reflection θ: t → 1 - t, on T^4 or Z^4).**
    - The links crossing the reflection plane(s) are pairwise disjoint edges and contain no loop. A gauge
      transformation supported on the positive half sets them to 1; it leaves gauge-invariant positive observables and
      the measure unchanged.
    - Then e^{-S} = e^{A_+} θ(e^{A_+}) Π_{crossing p} exp((β/N) Re tr(W_p θ(W_p)^dag)), where A_+ is positive-half
      measurable and W_p is a positive-half link.
    - Re tr(W θ(W)^dag) = Σ_{ab} Re(W_ab conj(θW_ab)) is a sum of terms G θ(Ḡ) + c.c.
    - Expanding the exponential gives a non-negative combination of products G_α θ(Ḡ_α). The Haar measure factorises
      as dμ_+ dμ_-, and θ is measure preserving.
    - So ⟨θ(F) F̄⟩ = Σ_α c_α |∫ F G_α e^{A_+} dμ_+|^2 ≥ 0, with c_α ≥ 0 when β ≥ 0. ∎
    - Site reflection is analogous. The plane variables are shared, and the plaquettes in the plane belong to both
      halves; split their weight symmetrically.
  - **Check c4.**
    - Exact enumeration for Z2 on 4×2: the RP matrix is PSD, minimum eigenvalue ≥ -2e-17, for both reflections. The
      non-RP control has minimum eigenvalue -1.5e-2 (link) and -1.7e-3 (site).
    - The SU(2) and SU(3) kernels exp(β Re tr W V^dag) are PSD for β ≥ 0 and not PSD for β = -1.
  - **Note.** β < 0 is *not* a usable negative control for Z2 (observed PSD; presumably a π-flux relabelling, not
    proven).
- **L9a'. Block observables are reflection covariant: PROVEN-HERE.**
  - Statement: for a reflection through a resolution-m block-boundary hyperplane, θ maps O_m(X) to O_m(θX), and
    V^(m)[θU] = θ(V^(m)[U]), with link orientation reversed in the reflected direction.
  - Proof: the complete-axial path between two sites is determined by its endpoints and the fixed order of directions.
    A coordinate reflection preserves that order and maps monotone segments to monotone segments, so it maps
    complete-axial paths to complete-axial paths.
  - For L odd the block centres map to block centres when the plane is a block boundary. Straight legs map to straight
    legs (reversed when the reflected coordinate is μ).
  - Directions other than the reflected one: the path set maps bijectively onto the path set of the reflected link,
    the reference maps to the reference, and the identity is exact.
  - **Reversal (reflected direction μ).** Let the reflected link run from X' to X' + e_μ.
    - Its paths are the images of the original reversed paths T̃_{y} = T_{y-Le_μ}^-1, for y ∈ B(X + e_μ).
    - Its reference is T̃_{c_Y} = T_{c_Y - Le_μ}^-1 = T_{c_X}^-1, because c_Y = c_X + L e_μ.
    - Write Z_y = T_{c_X}^-1 T_y. Then T_{c_X} T_y^-1 = T_{c_X} Z_y^-1 T_{c_X}^-1, and the reversed average is
      T_{c_X}^-1 exp(avg log(T_{c_X} Z_y^-1 T_{c_X}^-1)) = T_{c_X}^-1 T_{c_X} exp(-avg log Z_y) T_{c_X}^-1 = U'^-1.
    - This uses log(W Z W^-1) = W log(Z) W^-1 and log(Z^-1) = -log Z (principal branch on D; for every Z under the odd
      branch rule of S4'' [R3-fix], so the identity extends to S4'' everywhere). ∎
  - **Check c1(f).** Exact to 1e-15 for SU(2) and SU(3), for both the reflected and an unreflected direction.
  - A draft of this lemma wrongly flagged a reference asymmetry; the computation above removes it, see LOG.
- **L9b. Euclidean invariance (OS1): OPEN. This is the hard core.**
  - (α) On T^4 it is false by geometry.
  - (β) Continuum translations. Only translations by multiples of L^-K are exact symmetries. Translation by a general
    vector needs grids offset by fine-lattice vectors. **Estimate E9.1:** for f ∈ O_m(X) with Lipschitz constant 1,
    |E_K[f(V^(m)_{grid+a})] - E_K[f(V^(m)_{grid})]| ≤ C |X|_m (L^m |a|)^γ, uniformly in K, for some γ > 0. E9.1 plus
    L8b gives exact R^4 translation invariance of the limit.
  - (γ) Rotations. There is no lattice rotation beyond the hypercubic group.
    - **Remark R9.1:** averaging the limit over SO(4) gives invariance but destroys RP. A convex combination of
      measures that are RP with respect to different planes is not RP with respect to a fixed plane in general. This is
      not a proof of impossibility, only of the failure of the naive route.
    - **Route γ1 (universality).** The limit on a common continuum state space is independent of the lattice
      orientation. This needs E7 plus discretisation independence, and in infinite volume probably uniqueness (blocked,
      see L8).
    - **Route γ2 (two families).** A rotation-covariant family, e.g. gradient-flow observables at flow time t > 0
      [m: Lüscher, JHEP 08 (2010) 071; reviewer: consistent, not web-confirmed], provides OS1. The block family provides OS2. One must prove that both generate the same
      limit state, i.e. a 4D state space à la Cao-Chatterjee (3D: arXiv:2111.12813 [v]; CMP 405 (2024), no. 1, art. 3, DOI
      10.1007/s00220-023-04870-y [v-R2]). Flowed observables
      are not exactly local, so they cannot carry RP themselves.
- **L9c. OS0 regularity: OPEN.** The block observables are bounded, so their Schwinger "functions" are bounded, but
  they are not distributions in local fields. OS reconstruction needs a local field algebra with E(4) action. This is
  tied to γ2. E9.1 and E7 are the needed uniform estimates.
- **L9d. Clustering (OS4): OPEN.** Whether RP survives the ergodic decomposition of a translation-invariant RP state is
  [unverified]. Without a gap or uniqueness this is not available.

### L10. Non-triviality (not a free theory): OPEN
The target is a short-distance statement: for example, a connected 4-point function of resolution-m linearised fields,
or the β-function seen in O, differs from the free value at order g_m^4. It needs E7-level control.

### QCD and the GUT (carried from review.md; not attacked)
- **F1.** RP for Wilson fermions: IMPORTED-NOT-YET-REVERIFIED (Osterwalder-Seiler 1978 [unverified-citation]).
- **F2-F4:** OPEN.
- **C1-C4:** OPEN.

---

## 3. Tally (after session 8)
**[S8] Tally: 43 / 2 / 7 / 23.** + Lemma GT, + Proposition R4D-iso (OPEN → PROVEN-HERE), + Lemma W1-sym (with W1-def and
W1-size, which are short exact identities/inequalities and are counted with it); OPEN: - R4D-iso, + W1-loc.
- **PROVEN-HERE: 43** (40 + 3 [S8]). The [S8] items and R2D-iso [S7] are unreviewed.
- **IMPORTED-AND-REVERIFIED: 2**; **IMPORTED-NOT-YET-REVERIFIED: 7** (L5 unchanged: walls W1-loc, W2, W3).
- **OPEN: 23**: the session-7 list with R4D-iso removed and **W1-loc** added (W1-LD: P_rel(collar off a common direction
  by δ_0 = ε_1/(2√(4L+κ))) ≤ Ce^{-a/g²}; W1-cl: truncated correlations of ρ_□ with q ≤ 4 block averages
  ≤ C_qe^{-a/g²}(g²/κ)^qe^{-κ_d max|c_j|}; uniform in the torus).

**[S7] Tally (superseded by [S8] above).**
**[S7] Tally.** After the REVIEW_S5_S6 fixes (step 1): **39 / 2 / 7 / 22** (the added OPEN item is L1e-(0.4)). After
session 7's new work: **40 / 2 / 7 / 23**: + Proposition R2D-iso (PROVEN-HERE, isolated cube, d = 2; L5 [S7]); + R4D-iso
(OPEN, the 4D isolated-cube step, L5 [S7]). L5 itself stays IMPORTED-NOT-YET-REVERIFIED (walls W1-W3).
- **PROVEN-HERE: 40** (34 + 5 [S6] + 1 [S7]). REVIEW_S5_S6 confirmed all 39 earlier items (6 with fixes, applied as
  [R56-fix]); R2D-iso is new and unreviewed.
  - From sessions 1-3 (24, all confirmed by REVIEW_S3 as inequalities/identities): L0, L1a, L1b, L1c, L3s (weaker
    analogue), L4c, L7.0 (per K), L7a, L8a, L8b, L8c, L9a', L1e (smooth backgrounds only), R3.1 (promoted remark), L3s',
    L3g(a)-block (unused), L9a-m, S4' re-checks (now everywhere, with the odd branch rule [R3-fix]), L3g(a)-glob,
    L3g(a)-slice (the inequality on H_0; its use as a fluctuation gap is CONDITIONAL on (FP) [R3-fix]), E8.1, E8.2,
    E8.3 (inequality), S5' per-K tuning.
  - New in session 4 (6): Lemma E8*-sup; Proposition E8*-k (E8* at every fixed depth, uniform in K, M); Proposition
    E8*-ob (sharpness of the deterministic induction); Proposition E8*-red (coarse chessboard: every depth reduced to the
    homogeneous E8**); Lemma H0 (crossing-link structure); Lemma H1 (one step from Haar; w_0(1) bound for L ≥ 5, d = 4, SU(2) only [R4-fix]).
  - New in session 5 (4): Lemma E8**-dens (E8** ⇐ an effective-density bound (D_m)); inequality (B); Lemma A1 (abelian
    S4' averaging contracts the action, sharp constant L^{4-d}, = 1 in d = 4); Proposition A2 (E8** and E8* at every depth
    for the 4D Gaussian abelian model, ε = 4096 e^{-βη²/4}). (B) is elementary and is counted for bookkeeping only.
  - New in session 6 (5): L4a-Π (transverse structure of the polarisation tensor; β as the mixed second moment, a
    re-derivation of CMP 109 §5); Lemma B-avg (Balaban's (0.4) with diagonal order pairing = S4', conjugation identity,
    c17(B); elementary, counted for bookkeeping); Lemma A1-NA(1) (one-step non-abelian action bound with the sharp
    leading constant L^{4-d}, local form and large-field dichotomy; moved from OPEN); Corollary A1-NA(k) (k-uniform on
    the L1e domain, for S4' iterates [R56-fix]; on Balaban's (1.2) only conditionally on L1e-(0.4) and the √N
    conversion); Proposition LF-count (the unrenormalised large-field count diverges in d = 4 for every ε_1 below an
    explicit bound, ε_1 ≲ (8/(||Δ||β'_B))^{1/2} [R56-fix; inference, conditional on the one-loop rate]; the arithmetic
    only, its interpretation labelled).
  - New in session 7 (1): Proposition R2D-iso (2D O(N), one isolated cube, one step: the renormalised large-field
    weight is vacuum part + δβ·A_B + O(e^{-a/g²}s⁴); proven against the pre-stated RTARGET.md).
  - Soft or content-free alone: L7a, L8a-c, L7.0/S5' per-K.
- **IMPORTED-AND-REVERIFIED: 2.** L4b (b0) and L9a (Wilson RP, link and site reflections). The chessboard estimate is
  attributed to Fröhlich-Israel-Lieb-Simon, CMP 62 (1978) 1-34 [v-R4], but the special case used is re-derived, so it is not an import.
- **IMPORTED-NOT-YET-REVERIFIED: 7.** L1d, L2, L3g, L4a (its AF rate feeds the E8.3 corollary), L5, L6, F1. **[S5]** No
  status change: Dimock's abelian/scalar d = 3 analogues of L1d, L2, L3g, L4a, L6 were read and their transfer analysed
  (L6loc [S5] block); none of them re-verifies a 4D SU(N) statement, and the R-operation (L5) has no open exposition.
  Citation upgrades: L6's Dimock analogue [v-abs] → [read]. **[S6]** CMP 109 read in full (NOTES §9). Still no
  status change, for stated reasons: CMP 109 defers L4a-form's localisation to CMP 116 and L4a-flow (Theorem 2) to an
  unnamed later paper, and cites CMP 98/99/102 for L1d/L2/L3g without reproving them. Narrowings: L1d's
  background-regularity part is L1e on Balaban's domain (1.2); L4a's β-definition is split off as L4a-Π (PROVEN-HERE);
  L4a's "β_j → 2b_0 ln L" is corrected to CMP 109's two-sided (0.31) with unspecified β, β'.
- **OPEN: 23** (22 - A1-NA [S6] + L1e-(0.4) [R56-fix] + R4D-iso [S7]). **L1e-(0.4)**: L1e for Balaban's (0.4) with independent pairing (two-axial-path ribbon variant; needed by the A1-NA(k) (1.2)/minimiser readings and by decision 4). **R4D-iso**: the 4D SU(N) isolated-cube step (gauge-invariant Taylor lemma; soft constraint or fibre smoothness). **[S8] R4D-iso moved to PROVEN-HERE (soft constraint); fibre smoothness under Balaban's δ-constraint stays in W3.** Carried: E8* at depths k ≳ log β (fixed depths proven [S4]); E8** (constrained stability, sufficient for E8* at
  all depths; **[S5] reclassified: OPEN, import target = corollary of L5 + L6, not new content**; its sufficient form
  (D_m) is not counted separately); ~~A1-NA~~ (proven [S6] as A1-NA(1)); E7.0'; E7.0'-TV (new [S4], sufficient for E7.0'); E7.0'-AF (new [R3-fix]: AF compatibility of
  the S5'-tuned couplings); the L3g(a)-slice completion (FP, NA, IT); L7b (E7, E7.1-E7.4); L7c (conditional); L3g-ob
  (heuristic); L8d; L9b (E9.1, γ); L9c; L9d; L10; F2; F3; F4; C1; C2; C3; C4.
- **Retired as false [R3-fix: narrowed].** E8 with the domain D, for SU(2) and SU(3): unconditionally if g is a fixed
  bare coupling; conditional on L4a's AF rate if g is the tuned coupling. E7.0 restricted to the AF window, for
  SU(2), SU(3), SU(4) (threshold 3τ_N/4; SU(2) λ_c/λ_AF ≈ 6.1). N ≥ 5 (E7.0) and N ≥ 4 (E8 with D) are undecided. The
  session-3 "all N" statement concerned the stronger event "all steps within τ_N/2" and is withdrawn as a statement
  about E8.

**First open estimate: E8** (constrained stability) [S5: an import target, not a research target].** Z_K(every level-m 2-cell contains an η-large coarse plaquette) /
Z_K ≤ ε(g_m)^{n_c}, uniformly in K and M. By E8*-red it implies E8* at every depth. E8*-k proves E8* at depths
k ≲ log β / (2 log C_1), and E8*-ob shows that no induction through the fine-plaquette sup reaches deeper [R4-fix]. E8** is homogeneous and
translation invariant, of the same type as Balaban's UV stability bound. It is upstream of: the consistency of the limit
points; passing S5' through the limit; L7c; and E7.4. E7.0' is the second open estimate, independent of E8**: H1 does
the first step, and E7.0'-TV is a sufficient reduction.
**[S5]** E8** holds in the 4D Gaussian abelian model at every depth (A2), so the statement is natural and is NOT blocked
by the E8*-ob mechanism; for SU(N) it is the probability form of Balaban's per-level large-field bound plus stability
(the Dimock III Lemma 13 + Theorem 2 template), via E8**-dens. Further progress on it is reading Balaban CMP 122, not new
reductions.
**[S6]** CMP 109 is read, and confirms that E8** cannot come from it: it is small-field only. Proposition LF-count shows
that in d = 4 the per-level extraction (now proven at tree level, A1-NA(1)(c)) cannot be summed without renormalising
the large-field regions. So E8** waits on L5's renormalised large-field bound: CMP 122, or a reconstruction of a one-cube
R-operation.

## 4. Next session
**[S8] Order for session 9.**
1. **Review first.** A hostile review of sessions 7-8: R2D-iso; RTARGET §5-6 vs Lemma GT, R4D-iso and the W1 lemmas
   (were the targets met as pre-stated? the radial-gauge step 1, the B_4 irreducibility argument, the R4D-iso size step
   with the data-region constant C_L, W1-size's rearrangement); c19 criteria vs script vs output.
2. **W1-loc, size half first (W1-LD).** A local stability estimate for the pinned sea that does not go through
   frozen-exterior cap bounds (those amplify by M ≫ 1): e.g. a global Gaussian-domination / convexity bound in a chart
   around the background (the Hessian is ≥ c/g² by the block Poincaré inequality, L3 step 2, up to O(ε_1) corrections),
   with Brascamp-Lieb or Helffer-Sjöstrand for the deviation tails, then Helffer-Sjöstrand + Combes-Thomas for W1-cl.
   Imports allowed, re-verified on the pinned O(N) sea.
3. **W2**, against RTARGET §7 as pre-stated.
4. **L1e-(0.4)** (easy), and the R4D-iso cut: Balaban's gauge-fixed B' cut vs our gauge-invariant plaquette cut.
5. Owner request unchanged: CMP 122 I-II (decisive for L5), CMP 116.

**[S7] Order for session 8.**
1. **Review first.** A hostile review of session 7: the [R56-fix] applications; c18c (criteria file vs script vs
   output); RTARGET.md vs Proposition R2D-iso (was the target met as pre-stated? steps 2, 5, 7 in particular); the CMP
   198 reclassification; the 4D transfer claims in R4D-iso.
2. **R4D-iso.** Write the gauge-invariant Taylor lemma (order s² vanishes; order s⁴ = c·Σ tr F²; odd orders vanish)
   for smooth gauge-invariant functions of the links of a cube with frozen exterior, then the 4D isolated-cube bound
   with a soft constraint and a plaquette cut.
3. **W1 in d = 2 first.** Unfreeze the exterior: a one-step polymer expansion of the small-field sea with one
   large-field defect, giving ρ_full(□) as local terms with the R2D-iso s-derivative bounds. A failure with the exact
   step named is a valid outcome.
4. **L1e-(0.4)** (easy): the two-axial-path ribbon variant.
5. **Owner request, unchanged:** CMP 122:175-202 and 355-392 (L5: decisive, and it should show how Balaban handles
   W1-W3); CMP 116:1-22; the Theorem 2 paper; CMP 102/98/99. CMP 198 is NOT a 2D template (low-temperature d ≥ 3), so
   it is dropped from the request unless the owner wants the R-operation's structure in a simpler model anyway.
6. Decision 4 (adopt (0.4) vs keep S4') and the carried items E7.0'-TV, E7.0'-AF, (FP).

**[S6] Order for session 7** (done in session 7: review applied as [R56-fix]; one-cube target in RTARGET.md; R2D-iso).
1. **Review first.** No hostile review of session 5 or session 6 exists. A REVIEW_S6 should check L4a-Π, A1-NA(1) and
   A1-NA(k) (constants, the axial-gauge locality step, and the Schur restriction to R), LF-count's hypotheses, and the
   NOTES §9 transcriptions against the page images.
2. **One-cube R-operation (reconstruction target named by LF-count).** For a single level-k M-cube in which the
   fluctuation cut |B'| < ε_1 fails, inside a small-field sea, construct the renormalised contribution: subtract the
   vacuum-energy and β_k·A counterterms computed from the small-field flow, and bound the remainder by
   O((L^kε)^{4+α})·(weight), using A1-NA(1)(c) for the action and L4a-Π for the marginal part. A failure with the exact
   wall named is a valid outcome.
3. **Owner request, unchanged, narrowed by CMP 109's deferrals:** CMP 122:175-202 and 355-392 (L5, decisive);
   CMP 116:1-22 (L4a-form's localisation, "II. Cluster expansions"); the paper with Theorem 2's proof (CMP 119:243-285 is
   the likely candidate, [not-read]); then CMP 102:277-309, 98:17-51, 99:75-102 and 99:389-434.
4. **Decision for the owner, not taken here:** adopt Balaban's (0.4) verbatim in place of S4', so that CMP 109's "all
   results of [12] are valid" applies, or keep S4' and prove the CMP 98 results for it. The re-checks needed for (0.4)
   are listed in L1d [S6].
5. Carried: E7.0'-TV, E7.0'-AF, (FP).

**[S5] Binding order (REVIEW_S4 strategy): obtain and read before any new reduction.**
1. **Owner action: Balaban PDFs.** Ask the owner to place in `literature/` (open sources do not contain them):
   - CMP 122 (1989) 175-202 and 355-392: Large field renormalization I, II. This is L5, and it decides E8**.
   - CMP 109 (1987) 249-301, CMP 116 (1988) 1-22 and CMP 119 (1988) 243-285. These are L4a and L6.
   - CMP 102 (1985) 277-309 (L2, and A1-NA's likely counterpart) and CMP 98 (1985) 17-51 (whether his averaging equals
     S4').
   - Then CMP 95 (1984) 17-40, CMP 96 (1984) 223-250, CMP 99 (1985) 75-102 and 389-434 (L3g, L1d).
   - Optionally CMP 102 (1985) 255-275 (the 3D pure-gauge template) and Imbrie's Les Houches 1984 lectures.
2. **On receipt:** a line-level comparison of E8** / (D_m) against the CMP 122 large-field bound, in the
   NOTES.md format.
3. **Until then (low cost, no new reductions):**
   - A1-NA: a numerical diagnostic of the non-abelian action ratio on small-field SU(2) configurations.
   - The compact (Villain) U(1) version of A2.
4. E7.0'-TV, E7.0'-AF and (FP) are carried, with lower priority.

**Carried from session 4 (superseded order):**
1. ~~E8** abelian analogue~~ done as A2 [S5]. The SU(N) two-scale version waits for item 1 above.
2. **E7.0'-TV.** Bound the TV distance between Haar and the conditional crossing-link law Φ#Haar at β = 0, at level
   K - 1 first. This needs a Jacobian bound of S ↦ S e^{X̄(S)} away from the branch set.
3. **E7.0'-AF.** Test numerically whether S5'-tuned β_K grow at the AF rate (small K, d = 4, L = 3), as a diagnostic.
4. **(FP) and the SU(N) slice.** The abelian Faddeev-Popov identity for δ(h) plus the residual group; then decide whether
   the slice operator should be d*d + aQ^†Q rather than Δ.
5. ~~E7.2 norm~~ dropped [R4-fix] (REVIEW_S4 (2)).
