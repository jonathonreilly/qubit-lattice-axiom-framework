# LW1-5-X. The frame bound at exceptional angles

## 0. Status

**Pass 2; not refereed or frozen.** This item works the open LW1-5-X of frozen `LW1_5.md`. It does not amend that file. The laws and gauge actions are the conditional constructions in `LW1_5.md`, not a derivation of a physical gauge group.

**Proved here, conditional on those constructions.** For `L5-U[m]`, the compatible frames of one cube gate are exactly `U(5)` throughout the small-angle range in Theorem 5.1. For `m=1,9`, the even gate gives the bound at every point of the parameter window. For `2≤m≤8`, the result also holds when the relevant one-particle or one-hole gate determines its generator. The even gate has scalar site commutant throughout the window, for every `m`. For `L5-O[S_+]`, Theorem 6.1 gives a conditional site-commutant result.

**GAP.** The draft's assertion that the two-gate residual finite set also describes all exceptional *even-gate* parameter points is too broad: a fixed exceptional even angle leaves a continuum of parameter pairs. The finite-set statement needs compatibility with both gates. The draft's claim that an `SO(10)`-module decomposition alone gives finitely many candidate Lie algebras is not established; repeated irreducible summands permit continuously many invariant subspaces. The assertion that matter parity is the only matter-only conserved quantity is not proved. These gaps do not enter the U-law proofs.

**Open by name.** LW1-5-X remains open for the residual `L5-U` cases, reduced to the sufficient question LW1-5-X-B_m; and for `L5-O[S_+]`, as LW1-5-X-O. The amplitude hypothesis in Theorem 6.1 is unchecked at general window angles. No counterexample to LW1-5-X is established here. Other open items of `LW1_5.md` are unchanged.

**Provenance.** Pass 2 run (set by the lead from the run log): Codex `gpt-6.1-terra`, reasoning effort high, codex-cli 0.165.0, session `01a1aed1-ebe2-7382-8235-7e6a666a20f1`. Pass 1: Claude Opus 5.5, `LW1_5X_DRAFT.md`. Pass 2: Codex `gpt-6.1-terra`; reasoning effort not visible; session `01a1aed1-ebe2-7382-8235-7e6a666a20f1`; 2026-11-05. Draft SHA-256: `e6c4b1b880e9ab61b8263c09d4bb6d302fd7ebb3a603a4354c7359ac497ca720`. Frozen `LW1_5.md` SHA-256: `cbb2db58bfb6412e86cdd1f5aa87a2dfad9114ad7f156191171a320ac5c05413`. Working HEAD: `bf403a16a2bbb3bc0315a71f6cf1d791445cbb7f`. The draft describes an earlier source revision and a later date; the hashes here identify the files actually read. Its numerical scratch files are unavailable and were not rerun. Independent referee review remains due.

## 1. Definitions inferred by the distiller

1. A frame at `x` and compatibility with a gate have the meanings in `LW1_5.md` §1: the frame fixes all other sites and all links pointwise; a unitary on finitely many links can be composed with it to fix the gate. Compatibility with both gates permits separate register changes. This is a gate-wise question, not the full-tick question LW1-5-T.
2. A cube `C` has eight sites and twelve internal links. `H=H_C`, `W=e^{iaH}`, and `M=C\setminus{x}`. Each site has five CAR modes. Links are ordinary tensor factors commuting with matter. The U-law link register is `Λ^m C^10`, `1≤m≤9`, with five rishon modes at each end. The O-law register is `S_+`. The normalized cube generator and its signs are those in `LW1_5.md` §2.
3. For a U-law link with ends `u,v`, define
\[
T_{u\to v}=\sum_{j,k}c^\dagger_{v,j}r^{v}_j r^{u\dagger}_k c_{u,k},\quad h_\ell=T_{u\to v}+T_{v\to u}.
\]
A particle leaving `u` removes a rishon at `v` and creates one at `u`. For `m=1`, a link is *blocking at u* if its rishon is at `u`, and *open at u* if it is at the far end. `N_x` counts matter at `x`; `Π_k` projects onto `Λ^k C^5` there. `Γ(u)=⊕_k Λ^k u` fixes the vacuum.
4. `H_1` is the restriction of `H` to one cube matter particle, with all cube registers. An exceptional angle of a finite Hermitian `K` is an `a` for which `a(λ−λ')` is a nonzero multiple of `2π` for distinct eigenvalues. Thus `e^{iaK}` determines `K` by polynomial interpolation precisely outside that set. Extra link registers on which `H` acts trivially may be included in all commutant statements.
5. The window is `0≤μ<2ε<π`, `a_e=ε−μ/2`, `a_o=ε+μ/2`. The even gate has angle `−a_e`; `0<a_e≤ε<π/2`, and `0<a_o<π`.
6. “Scalar on the cube registers” allows an arbitrary operator on finitely many additional links. The phrase “holds at a parameter point” below means the frame bound for a frame compatible with the indicated gate or gates, not a claim about the full update.

The draft proposes no new reading or specification. The definitions above make its proof notation explicit; they do not adopt the proposed PS-3g or PS-3h5. Their four-test results remain those in `LW1_5.md` §2: tests 1, 2 and 4 pass, and test 3 is conditional. The owner keeps both laws live (`TOE_ASSEMBLY.md` §3.5).

## 2. Site commutant for one rishon

**Theorem 2.1 (draft Lemma 1.1).** If the site implementer `V` of a frame is even and `L` is a register unitary, their composition acts on the finite cube algebra as `Ad(V⊗L)` in a Jordan–Wigner ordering with `x` first.

*Proof.* Site elements transform by `Ad V`. An outside matter element of parity `q` has the form `P_x^q⊗b`. Since `V` commutes with `P_x`, conjugation by `V⊗L` fixes the matter part and applies `Ad L` to links, as required. □

**Theorem 2.2 (draft Lemma A).** For `L5-U[1]` and any real `a≠0`, an element `D` of the site algebra commuting with `W` is scalar.

*Proof.* The commutant `Dcal` is a unital *-algebra. The local Gauss charge commutes with `W`; its link part commutes with the site algebra. Fourier decomposition under `Ad e^{itN_x}` therefore puts every number-charge component `D_q` in `Dcal`.

Fix `k=1,…,5`, a neighbour `y` of `x`, and a state `A_ξ` with `ξ∈Λ^k C^5` at `x`, other cube matter empty, the link `xy` open at `x` with fixed far-end colour, and the other links incident on `x` or `y` blocking there. The cube has no triangles, so these choices are consistent. Put `B_ξ=T_{x→y}A_ξ` and `s=η_{xy}/√3`. The rishon colour left at `x` records which matter colour departed. The resulting register states are orthogonal. The only allowed moves give
\[
HA_ξ=sB_ξ,\quad HB_ξ=skA_ξ,\quad \|B_ξ\|^2=k\|ξ\|^2.
\]
The coefficient of `B_ξ` in `WA_ξ` is `is sin(a√(k/3))/√(k/3)`.

For a second block choose a path `x−y−z` in the cube. Open `xy` at `x` and `yz` at `y`; block every other link incident on `x,y,z` at its occupied endpoint. These seven links are distinct. With `C_ξ=T_{y→z}B_ξ` and `t=η_{yz}/√3`, the only moves give
\[
HA_ξ=sB_ξ,\quad HB_ξ=skA_ξ+tC_ξ,\quad HC_ξ=tB_ξ.
\]
Thus `H^3=(k+1)H/3` on this block, and the `B` coefficient in `WA_ξ` is `is sin(a√((k+1)/3))/√((k+1)/3)`. The two sines cannot both vanish: otherwise `(k+1)/k` is a rational square, whereas `k(k+1)` lies strictly between consecutive integer squares. Hence one block has a nonzero `B` coefficient for each `k`.

Let `D=D_0`. It is even and preserves each `Λ^k`. Compare the `B` parts of `DWA_ξ=WDA_ξ`; orthogonality of the register labels gives `Dc_{x,j}=c_{x,j}D` on `Λ^k` for all `k≥1`. Apply the same argument to `D*` and take adjoints. Since `D` is scalar on the vacuum line, it is scalar on the Fock basis generated from that line. For `q≠0`, `D_q*D_q` is charge zero and hence scalar, but `D_q` kills either `Λ^0` or `Λ^5`; it vanishes. □

**Corollary 2.3 (draft Corollary A.1).** A frame compatible with such a gate preserves `N_x` and has an even implementer preserving every `Λ^k`.

*Proof.* The gate conserves `N_x+N_M`. The combined frame and link change fixes `N_M`, so `φ(N_x)−N_x` commutes with the gate. Theorem 2.2 makes it scalar; its trace is zero. A site implementer commuting with `N_x` preserves each number sector and hence parity. □

## 3. One-particle register commutant and the `m=1` result

**Theorem 3.1 (draft Lemmas N and B).** For `m=1`, `||H_1||≤√3`. If `0<|a|<π/√3` and `1⊗L` commutes with `e^{iaH_1}`, then `L` is the identity on the twelve cube registers tensored with a unitary on any additional registers.

*Proof.* Split the links into the three directions. The four links in one direction are disjoint. On the one-particle sector a link hop exchanges the basis state with particle at one end and rishon at the other with the reversed state, up to sign; it kills the remaining states. Its norm is at most one. Thus the triangle inequality gives `||H_1||≤3/√3`.

The exponential is injective on the spectrum in the stated interval. A polynomial in `e^{iaH_1}` therefore equals `H_1`, so `L` commutes with `H_1`. Taking matter matrix elements on a link gives commutation with every `r^v_j r^{u†}_k` and its adjoint. On the one-rishon register these are the off-diagonal matrix units between the two five-dimensional ends; their products give the remaining matrix units. Their commutant is scalar on that link. Apply this to all twelve links. □

The pass-1 scratch report gives largest eigenvalue `1.3481` in a **one-colour** analogue of dimension `8·2^12`; it is not a five-colour check or a proof. Its reported `/tmp/toe-lw15x/check_n.py` and output were absent in this session.

**Theorem 3.2 (draft Theorem X).** For `L5-U[1]`, the frames compatible with a cube gate at `0<|a|<π/√3` are exactly `Ad Γ(u)`, `u∈U(5)`. In particular the even gate gives this result throughout the window.

*Proof.* The Gauss action supplies the compensating link unitary for every `Γ(u)`. Conversely, let a compatible frame have implementer `V`. Corollary 2.3 makes `V` even and number-preserving. Normalize its vacuum phase and set `u=V|_{Λ^1}`. Compose with the inverse exact `U(5)` gauge action. The new site implementer `V'` is the identity on `Λ^0⊕Λ^1`; its combined action still fixes the gate. By Theorem 2.1 it is `Ad(V'⊗L')`. On the one-particle sector `V'` is the identity. Theorem 3.1 removes `L'` from the cube registers. Thus `V'` commutes with the gate as a site operator, and Theorem 2.2 makes it scalar; the vacuum normalization makes it one. Finally `a_e<π/2<π/√3`. □

The odd gate separately has the same bound when `a_o<π/√3`. The smaller two-mode, two-rishon single-link example reported in the frozen source is at `π/√2` and does not contradict this cube result.

## 4. General rishon number

**Theorem 4.1 (draft Lemma D).** Particle–hole conjugation on every matter and rishon mode maps `L5-U[m]` to `L5-U[10−m]`, preserves each `H_C`, maps compatible frames to compatible frames, and maps `U(5)` to itself.

*Proof.* The map sends `c` and `r` to their adjoints. For `u≠v`, the matter swap and the rishon swap each contribute a minus sign, so it sends `T_{u→v}` to `T_{v→u}`. It sends rishon number `m` to `10−m` and `N_x` to `5−N_x`. It maps the site and outside algebras onto themselves and link unitaries to link unitaries. Conjugating a compatible combined action therefore preserves compatibility. On number-preserving frames it sends `Γ(u)` to `Γ(ū)` up to scalar. □

**Theorem 4.2 (draft Lemmas N_m and B_m).** Define
\[
\nu_m^2=\max_{\max(0,m-5)\le p\le\min(4,m-1)}(m-p)(p+1).
\]
For `m=1,…,9`, these squares are `1,2,4,6,9,12,16,20,25`. Then `||H_1||≤√3ν_m`. If the exponential is injective on `spec H_1`, in particular if `0<|a|<π/(√3ν_m)`, every register unitary commuting with `e^{iaH_1}` is scalar on the cube registers.

*Proof.* For a single link, `T^2=0` and `T*T`, `TT*` act on orthogonal particle-location spaces. On a state with `p` rishons at the departure end, write `Z(e_k⊗ρ)=r^{u†}_kρ`. Then `T*T=p_v Z*Z`, and `ZZ*=p_u` on the space with `p+1` rishons at `u`. Hence `||T||²≤(m−p)(p+1)`. The permitted range of `p` is as displayed. Sum the three disjoint directional layers as in Theorem 3.1. The listed values follow by direct maximization.

Interpolation reduces the commutant to that of the link operators `r^v_jr^{u†}_k` and adjoints. Their products include `n^v_j(1−n^u_k)` and `n^u_k(1−n^v_j)`. These diagonal operators separate the `m`-subset occupation basis: for a mode present in one subset and absent in another, a missing opposite-end mode in the first subset or an occupied opposite-end mode in the second distinguishes them. If neither exists, the first subset has at least six modes and the second at most four, contrary to equal size. A commuting operator is therefore diagonal. Cross-end trades connect all `m`-subsets: use one intermediate mode at the opposite end to exchange two modes on the same end, then adjust end counts by cross-end trades. Commutation forces equal diagonal entries along each trade. Apply this on each link. □

**Theorem 4.3 (draft Lemma A_m).** For `L5-U[m]`, `1≤m≤9`, and `0<|a|<π√(3/5)`, the site commutant of `W` is scalar.

*Proof.* By Theorem 4.1 it suffices to take `m≤5`. Let `Dcal_0` be the charge-zero part of the site commutant. It is a finite-dimensional unital *-algebra, invariant under the connected local gauge group `U(5)`. Its minimal central projections are permuted continuously, hence fixed individually. The commutant of `Γ(U(5))` is the span of `Π_0,…,Π_5`: number rotations split the sectors, and the operators `c_i†c_j` connect all occupation basis vectors within each sector.

No nonconstant `f(N_x)` commutes with `W` in the stated range. To see this, fix `k=1,…,5`, a link `xy`, a `k`-element occupied set `F` at `x`, and no matter elsewhere. Put all `m` rishons on every other link at `x` or `y` at that endpoint. On `xy`, if `k≥m`, choose `m−1` rishon colours at `x` inside `F` and one at `y`; if `k≤m`, choose `F\setminus{k_0}` at `x` and `m−k+1` colours at `y`. A departure either uses the sole far-end rishon or fills the sole hole in the departure-end rishons. No second departure is possible. The departed particle can return only to its original matter colour, because the initial departure-end rishons lie inside `F`. Thus the starting state and its `n` one-departure states form a star block with `n=k−m+1` in the first case and `n=m−k+1` in the second. In either case `1≤n≤5`, `H²A=(n/3)A`, and the one-departure component of `WA` is nonzero because `0<|a|√(n/3)<π`. It follows that `Π_{k−1}WΠ_k≠0`, and hence `f(k−1)=f(k)` for all `k`.

Consequently the centre of `Dcal_0` consists of scalars. Restriction to the vacuum line is a unital *-homomorphism `Dcal_0→C`. Its kernel, if nonzero, has a nonzero central support projection in this finite-dimensional algebra; that projection vanishes on the vacuum and is neither zero nor one, a contradiction. The restriction is injective, so `Dcal_0=C1`. The nonzero charge parts vanish by the boundary-sector argument in Theorem 2.2. □

## 5. Frame bound and residual U-law question

**Theorem 5.1 (draft Theorem X_m).** Put `ν'_m=min(ν_m,ν_{10−m})`; its squares for `m=1,…,9` are `1,2,4,6,9,6,4,2,1`. For `0<|a|<π/(√3ν'_m)`, the compatible frames of a U-law cube gate are exactly `Ad Γ(u)`, `u∈U(5)`. For `m≤5` the same holds for `0<|a|<π√(3/5)` outside the exceptional set of `H_1`; for `m≥6` use the dual one-hole sector.

*Proof.* For `m≤5`, Theorem 4.3 gives the scalar site commutant. The argument of Corollary 2.3 preserves `N_x`. Repeat Theorem 3.2, using Theorem 4.2 to remove the register unitary. The small-angle bound lies inside the range of Theorem 4.3. For `m≥6`, apply Theorem 4.1 to `10−m`. The Gauss action gives the converse. □

**Corollary 5.2 (draft Corollary X_m.1).** The even gate gives LW1-5-X throughout the window for `m=1,9`. For `2≤m≤8`, it gives the bound for `a_e<π/(√3ν'_m)` and whenever the relevant one-particle or one-hole angle is nonexceptional. The small-angle thresholds are `π/√6`, `π/(2√3)`, `π/√18`, `π/(3√3)` for `m=2,3,4,5`, respectively, and the same in reverse for `m=8,7,6`. If a frame is compatible with **both** gates, any unresolved parameter pairs form a subset of the finite set where both full cube angles are exceptional.

*Proof.* Apply Theorem 5.1 at `a=−a_e`; use `a_e<π/2` for the window claims. For compatibility with both gates, `LW1_5.md` M.1 gives the bound whenever either full cube angle is nonexceptional. Each exceptional set meets its bounded angle interval in finitely many points, and `(a_e,a_o)` determines `(ε,μ)`. □

**GAP in the draft's finite-set wording.** Nonexceptionality of the even gate alone is a sufficient condition. Its exceptional angle can persist along a line in `(ε,μ)`; only the simultaneous full-gate exceptional condition bounds the two-gate residual to finitely many pairs.

**LW1-5-X-B_m (OPEN).** For `2≤m≤5`, at an exceptional one-particle angle `π/(√3ν_m)≤|a|<π/2`, does every register unitary commuting with `e^{iaH_1}` act as a scalar on cube registers? For `6≤m≤8`, use the dual one-hole sector. An affirmative answer is sufficient, not shown necessary, for the even-gate frame bound by Theorem 5.1's proof. A non-`U(5)` compatible frame would require a nonscalar such register commutant after normalization. No counterexample is found.

The draft's three searches do not close this question: interpolation fails at a spectral coincidence; the connected-gauge centre argument does not supply the invariant one-dimensional sector used in Theorem 4.3; and fixed register blocks do not control a unitary that may mix their basis states. These are limitations of the routes, not no-go results.

## 6. Majorana law

**Theorem 6.1 (draft Lemma A_O).** For an `L5-O[S_+]` cube gate, suppose the nonzero blocks `Π_{k'}WΠ_k` connect all vertices `0,…,5`, with an edge for each `k≠k'` whose block is nonzero. Then its site commutant is scalar.

*Proof.* The local `SO(10)` Gauss action contains `U(5)` and commutes with the gate. The charge decomposition and centre argument in Theorem 4.3 apply. If `f(N_x)` commutes with `W`, every nonzero block forces `f(k')=f(k)`. Connectivity makes `f` constant. The vacuum-line argument then makes the charge-zero commutant scalar, and the nonzero charge components vanish as before. □

The connectivity hypothesis holds for sufficiently small nonzero `|a|`: the faithful one-mode inflow in `LW1_5.md` M gives nonzero adjacent-number blocks of `H`; their analytic gate matrix elements have nonzero first derivative at zero. It is unchecked at general angles in the window.

**LW1-5-X-O (OPEN).** At the finitely many parameter pairs where both full cube angles are exceptional, does compatibility with both gates force a Bogoliubov frame? The U-law argument uses conserved total matter number and a one-particle sector; the Majorana hop has pairing terms, so those particular tools are unavailable. A proposed route is to find an invariant sector on which a normalized frame is trivial and the gate determines the generator, and then prove the required register commutant. Those properties are proof obligations, not a constructed sector. The draft reports no counterexample.

The draft's parity-slice search does not constrain the site action to degree one: higher odd degrees can occur at finite angle. Its Lie-algebra search also leaves spectral projections and disconnected components uncontrolled. **GAP:** the stated decomposition `45⊕45⊕210⊕210⊕1` does not by itself yield finitely many invariant subspaces, because equivalent copies can mix; no finite classification of candidate Lie algebras is proved. The assertion that parity is the *only* conserved matter-only quantity is also unproved and is not needed to show that matter number fails to be conserved.

## 7. Scope and dependencies

The proofs use the finite CAR and link algebra, the exact local gauge actions and faithful generator inflow in frozen `LW1_5.md`, and standard finite-dimensional spectral interpolation. The proofs re-establish the needed commutants and block calculations. They do not independently re-audit the frozen source. The pass-1 one-colour numerical report is unverified here. Neither this item nor the owner's choice of both live laws fixes `m`, selects a law, establishes a continuum theory, or grants retained status. The independent referee pass and any dated amendment remain future work.
