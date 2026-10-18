# COL-1 pre-registration: can colour be carried by combinations of sites?

Written 2026-10-14 ~21:35Z, before any script is run. Never edited afterwards; only dated follow-ups may be appended.
Agent: Claude Opus 5.5 (same family as the supervisor and panel; not independent). Memory cap 0.3 GB per run, one process at a time, OMP_NUM_THREADS=2.

Fixed readings (TESTS.md, branch `origin/claude/chirality-grid-exercise-20261014`, lines 78–95): COLOUR-SPREAD-OK / COLOUR-BLOCK-FORCED / COLOUR-EMERGENT-ONLY / OPEN. They are not changed here; this file only makes them operational.

## 0. Definitions

Lattice Λ = Z^d (d = 1 toy, d = 3 target), or a finite ring/torus. Two classes of site content:

- **Class Q (elementary modes).** One complex fermion mode c_s per site. Gauss generators are quadratic: G = c† t c (or the Majorana/BdG form (i/4) γ A γ). This is the class behind the qinfo panelist's "≥ 16 modes per site".
- **Class M (qubits, many-body).** One qubit per site (AX:47, M₂(C)). Gauss generators are arbitrary Hermitian operators of finite support.

A **local SU(3) gauge structure** is a family {G_α^a}, α in an index set I ("gauge points"), a = 1..8, with:
- (G1) for each α: [G_α^a, G_α^b] = i f^{abc} G_α^c, and SU(3)_α acts nontrivially (some state carries a 3 or 3̄ of SU(3)_α);
- (G2) [G_α^a, G_β^b] = 0 for α ≠ β, as operators on the **full** Hilbert space;
- (G3) twisted translation covariance: for each unit vector μ there is a unitary 𝒯_μ (the shift, optionally composed with a product of on-site unitaries) and a bijection τ_μ of I with 𝒯_μ G_α^a 𝒯_μ† = R_μ^{ab} G_{τ_μ(α)}^b, R_μ an automorphism of su(3) (identity allowed; a cyclic colour permutation is the TESTS example);
- (G4) finite range: every support S_α has diameter ≤ r.

A **Gauss law** additionally means: G_α = (matter colour charge at α) + (link-end terms), the physical space ∩_{α,a} ker G_α^a contains a state with colour-triplet matter at some point, and there is a local Hamiltonian term commuting with every G_α^a that acts nontrivially on the physical space.

"Colour components on different qubits" means: a triplet of SU(3)_α is spanned by three states that differ by which of three distinct qubits is excited.

## 1. Claims to establish (labels fixed in advance)

- **P-Q (proof, class Q).** Mode counting: commuting quadratic su(3) representations on a single-particle space of dimension N (complex) or 2N (real, Majorana form) number at most N/3. Translation covariance forces |I| ≥ N on a torus (τ acts freely because supports are finite). Hence class Q with one mode per site admits **no** structure (G1)–(G4), twisted or not. Also classify colour-component-to-site assignments s(α,i) compatible with a twisted shift: s(x,i) = x + c(σ^{−x} i), which puts three components on every site.
- **P-OWN (proof, both classes).** Ownership lemma (Bravyi–Vyalyi-type): if two finite-dimensional *-algebras commute and their supports overlap in region O, then H_O = ⊕_j L_j ⊗ R_j with each algebra acting only on its own factor. Corollary: a qubit touched by two commuting colour algebras is a read-only (classical) bit for both. So colour registers of different gauge points never share a qubit quantum-mechanically.
- **P-CAP (proof, class M).** If k gauge points with supports inside n qubits simultaneously carry nontrivial colour, then 3^k ≤ 2^n; so the density of simultaneously colour-charged points is ≤ 1/log₂3 ≈ 0.63 per site.
- **C-Z1 (construction, class M, Z¹).** A "floating token" construction: gauge points at every site; a gauge point is active only where a local marker pattern sits; colour registers are three single-excitation qubits. Two versions: (a) matter only, with gaps (cells float); (b) matter (quark/antiquark register) plus links (Kogut–Susskind-truncated 1 ⊕ (3̄,3) link with the x-end colour on 3 qubits owned by x and the y-end colour on 3 qubits owned by y) with a Gauss law and a gauge-invariant pair-creation/hopping term.
- **C-Z3 (construction, class M, Z³).** Version (b) extended with three link registers per token and row alignment, gauge points at every site, covariant under all three unit translations.

## 2. Checks (scripts in `scripts/`, outputs `.out`)

1. `col1_quadratic.py` — class Q: commutator norms for the overlapping and twisted assignments on rings; the counting bound on small examples; the assignment classification for σ = cyclic.
2. `col1_ownership.py` — the minimal attempt (SU(3) on qubits (x,x+1) as 3⊕1, random basis): commutant of A_x inside operators on qubits (x+1,x+2); report its dimension and whether it contains any non-abelian su(3). Slice-algebra (ownership) decomposition for the token generators' overlaps.
3. `col1_tokens_z1_full.py` — version (a) on rings L = 14, 16, 18, 20, **full 2^L Hilbert space**, sparse: (G1) relations at every x; all [G_x^a, G_y^b] = 0; 𝒯 G_x 𝒯† = G_{x+1}; Casimir 4/3 on active states; maximal number of simultaneously active cells vs the P-CAP bound; active-cell sets that are not a single sublattice (floating).
4. `col1_tokens_z1_links.py` — version (b): (i) exhaustive parse lemma by constraint satisfaction over all relative offsets (P1: two token predicates are jointly satisfiable only for consecutive tokens; P2: every predicate is blind to colour moves inside the registers of another active token); (ii) on the constrained subspace of a ring with 2 tokens and all offsets: (G1), (G2), (G3) (𝒯 permutes offset sectors), [H, G] = 0; (iii) on one offset sector with 3 tokens: physical-space dimension, presence of quark–string–antiquark states, and H restricted to the physical space nonzero (its spectrum).
5. `col1_z3.py` — version (b) in Z³: 3D parse lemma (P1/P2) by the same constraint checker on 3D positions; register-level gauge invariance of x/y/z hopping terms and commutation of shared link registers.

Numerical tolerance: commutator and relation norms ≤ 1e-12 (entries are 0, ±1/2, ±1/(2√3), ±i/2).

## 3. Reading rule (decided now)

The TESTS setting allows "one complex fermion mode **or qubit** per site". The overall reading is therefore decided on class M; class Q is reported as a sub-reading.

- **COLOUR-SPREAD-OK** if C-Z1(b) passes every check in §2.3–2.4 (full-space G2 established through the checked parse lemma plus the proved register algebra, and directly on the full space for version (a)), **and** C-Z3 passes §2.5. Scope will be stated: kinematic gauge structure and Gauss law only.
- **COLOUR-BLOCK-FORCED** if the constructions fail and the obstruction is proved in class M. In class Q, P-Q gives the sub-reading COLOUR-BLOCK-FORCED with the named obstruction (mode counting), whatever happens in class M.
- **COLOUR-EMERGENT-ONLY** if exact local SU(3) with spread components is shown impossible in class M but an emergent route is not excluded.
- **OPEN** if C-Z1(b) passes but C-Z3 cannot be built or checked in budget (then: "SPREAD-OK in Z¹, OPEN in Z³"), or if neither a construction nor a proof is reached.

## 4. Not tested, stated in advance

- Dynamics: whether any gauge-invariant Hamiltonian on these structures has a continuum limit that is SU(3) Yang–Mills/QCD; confinement; fermionic statistics of tokens (registers are hard-core; Jordan–Wigner signs are irrelevant for the kinematic gauge checks).
- Whether a translation-invariant ground state exists (cells may crystallize: a spontaneous Z → ℓZ breaking).
- Cubic-rotation covariance (AX:37–38) of the Z³ construction (tokens along one axis are not rotation covariant).
- Chirality, SU(2)×U(1), the full SM content.
- Emergent (non-exact) SU(3) and Gauss-law-solved (string-net / local multiplet basis) formulations are reported as comparators only.

## 5. Prior art to cite (read before running)

Repo (origin/main): the landed SU(N) link state count (`docs/DYNAMICS_CLAUSE_NON_ABELIAN_GAUGE_LINKS_NEED_SEVERAL_QUBITS_..._2026-09-24.md`: ≥ 2N states, SU(3) needs 3 qubits per link), the non-abelian Gauss-law plaquette notes (09-03), the U(1)/Maxwell lane (`U1_MAXWELL_LIGHT_LANE_LANDING_CORE_META_NOTE_2026-09-05.md`, Gauss law as glued support 09-14, link-freezing 09-24, charges as Gauss defects 09-24), the taste-cube colour embedding (`CL3_COLOR_AUTOMORPHISM_THEOREM.md`, `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`: SU(3) on the 3-dim symmetric base of the 2³ taste cube, physical identification open), the two-site colour arena (`COLOR_ARENA_BONDED_PAIR_..._2026-07-06.md`; `EDGE_TWO_SITE_FRAMING_..._2026-06-08.md`), composite sites (09-24). Literature: Kawamoto–Smit; Golterman–Smit (shifts); Chandrasekharan–Wiese; Brower–Chandrasekharan–Wiese (rishons); Ciavarella–Klco–Savage; Seifnashri(–Shirley); Thorngren–Preskill–Fidkowski; Else–Nayak; Wen; Levin–Wen; Bravyi–Vyalyi; GNVW.
