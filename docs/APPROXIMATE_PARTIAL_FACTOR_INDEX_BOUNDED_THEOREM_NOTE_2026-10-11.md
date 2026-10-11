---
claim_id: approximate_partial_factor_index_bounded_theorem_note_2026-10-11
claim_type: bounded_theorem
claim_scope: "For spin-chain automorphisms satisfying explicit uniform tails and full-interior block-norm control, a quantified partial-factor index inequality yields a normalized O(log^2 L/L) tube bound. Microscopic finite-range Hamiltonian constants are matched; the full-algebra shift identity and physical representation premises remain supplied."
upstream_dependencies: []
runner: scripts/approximate_partial_factor_index_2026_10_11.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "The quantified partial-factor lemma below; N1's physical and representation premises remain supplied"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Approximate partial-factor index bound with explicit tube scaling

Source date: 2026-10-11. Status: conditional-support. The complete mathematical argument received a separate source review; no audit verdict or retained status is applied. This is a mathematical statement about automorphisms of a spin-chain algebra. It neither adopts Hamiltonian dynamics as a native physical law nor identifies an automorphism with permanent Record evolution.

## P1. Target, source and strongest statement

The target is N1 Section 2.2's previously unproved approximate partial-factor lemma: an automorphism nearly fixing the full interior block algebra of a thick tube should carry only a boundary-sized index, with quantified errors. N1 is frozen at candidate-law commit `b568c14df54a5e64f904f54f0251b2173f9302c3`, report SHA-256 `c284a41bfee8a1238643330ddd46f3a7c4f6f1a865509a9aaec5ab6f4238ad13`. Its exact source, B1/M1 premises and prior assessment are preserved in the [milestone packet](../.claude/science/physics-loops/toe-partial-factor-index-20261011/), with original identities in EVIDENCE_MAP.json. N1 is unchanged through candidate-law revision `407f99203a553b336f98e832213045ed49f7fc13`. New Y1/RZ material is outside this theorem.

The mathematical input is Ranard–Walter–Witteveen (RWW), arXiv:2012.00741v2, PDF SHA-256 `03fc3e67ccd36c1f6ac7e5336bdf6977010cc12d615f90e095ded550268eda17`. The imported statements and their matched hypotheses are recorded in P3 and P14. The proof uses their finite QCA index formula and algebra-stability construction, rather than an unquantified infinite-window entropy limit. [Primary RWW source](https://arxiv.org/pdf/2012.00741v2).

The result proved below is

\[
 |\operatorname{ind}\gamma|
 \le 2j\log d_B+8j\delta\log(d_I d_B)+3g(\delta),
 \qquad
 \delta={\epsilon+4C_Q f(j)\over\sqrt2},                 \tag{P1}
\]

provided the explicitly stated tail threshold and full-interior block-norm condition hold. Here `j` is a longitudinal blocking length, `d_I,d_B` are the interior and boundary Hilbert-space dimensions of one supersite, and

\[
 g(x)=(1+x)\log(1+x)-x\log x,\qquad g(0)=0.            \tag{P2}
\]

All logarithms are natural. For a tube with `L^(d-1)` qubits per longitudinal slice and exponentially small locality errors, P10 gives `j,R=O(log L)` and a normalized bound of order `log² L/L`. P11 verifies the required polynomial prefactors for finite-range, uniformly bounded Hamiltonian interactions. N1's independent integrated-Poincare, gap, scattering completeness and rational-centre assumptions remain exactly separate.

## P2. Algebras and exact hypotheses

At each integer `x` let

\[
 \mathcal A_x=M_{d_I}(\mathbb C)\otimes M_{d_B}(\mathbb C),
 \qquad d_s=d_I d_B,
\]

where `d_I,d_B` are positive integers. Let `A` be the norm-completed local tensor-product algebra. For an interval `X`, `A_I(X)` denotes its entire interior tensor-factor algebra, with the identity on every boundary factor. Interior/boundary are transverse tensor labels; they do not mean the left/right longitudinal sides of a cut.

An automorphism `gamma` has tails `f` when `f(r)` is non-increasing, tends to zero, and for every finite or infinite interval `X`, every `a in A(X)` has an approximant `b in A(X^{+r})` with

\[
 \inf_b\|\gamma(a)-b\|\le f(r)\|a\|.                    \tag{P3}
\]

This is RWW Definition 3.5. The constants are uniform in interval position and length. No factor depending on `|X|` is permitted in (P3). A separate length factor is permitted in the interior identity estimate below.

Fix the cut `0|1`, an integer `j>=1`, and

\[
 L_j=[-2j+1,0],\quad R_j=[1,2j],\quad X_j=L_j\cup R_j.
\]

The identity hypothesis is the norm of a linear map on the full matrix algebra:

\[
 \sup_{a\in\mathcal A_I(X_j),\ \|a\|\le1}
             \|\gamma(a)-a\|\le\epsilon.                 \tag{P4}
\]

Checking a state, single-site expectations, commuting observables, or finitely many chosen test vectors is not (P4). The supremum includes entangled block operators. Only one cut/window is needed for the theorem, because the QCA index can be calculated at that cut. In the tube application a uniform estimate supplies it at every position.

## P3. Explicit dimension-independent QCA constants

Use the following deliberately loose integers and threshold:

\[
 A_0=25\,97^4\,385^3,\qquad C_Q=435A_0,
 \qquad e_Q={1\over2048A_0}.                             \tag{P5}
\]

The RWW construction implies the following version of Proposition 5.5: if an automorphism is `e`-nearest-neighbour, with `e<=e_Q`, there is a radius-two QCA on that chain whose restriction to the algebra of any `m` sites differs by at most `C_Q e m`. These constants do not depend on any local dimension. Here is the constant bookkeeping, so no uncontrolled tail-dependent `C_f` is substituted into a tube estimate.

1. RWW Theorem 2.6(i) corrects a near inclusion of hyperfinite von Neumann algebras with error `e<=1/64` by a unitary within `12e` of one. Conjugation changes the automorphism norm by at most `24e`; its nearest-neighbour error is consequently at most `25e`.
2. Lemma 5.1(i), including its displayed proof, uses the inverse's `4e` near inclusion. It permits `e<=1/256` and a unitary within `48e`; the new near-inclusion error is at most `97e`.
3. Lemma 5.3(i) uses the inverse once more. It permits `e<=1/1024`, with unitary distance at most `192e`; the new error is at most `385e`.
4. Proposition 5.4's eight corrections are the initial step, four applications of Lemma 5.1 and three of Lemma 5.3. Their cumulative nearest-neighbour error is at most `A_0 e`, and their total automorphism displacement is at most `(A_0-1)e`. If `e<=1/(1024 A_0)`, every intermediate smallness condition is met. Thus one can take `C_1=A_0` and `e_1=1/(1024A_0)` in that proposition.
5. In Proposition 5.5 two local corrected automorphisms differ by at most `2A_0 e`. Proposition 4.10/Remark 4.11 yields its aligning unitary within `36(2A_0 e)=72A_0 e`, since `2A_0 e<=1/192`. The resulting QCA differs on any single site by at most `145A_0 e`.
6. Lemma 2.7 bounds the norm on `m` commuting generating site algebras by at most `2 sqrt(2) m(145A_0 e)` when the sum is less than one. If the sum is at least one, the trivial automorphism-difference bound two is smaller than `3m(145A_0 e)`. Thus `C_Q=435A_0` works for every `m`. Finally `e_Q` is at most both `e_1/2` and `1/(384C_1)`, as required in Proposition 5.5.

The imported infinite-algebra step applies: the tracial GNS closures of the local tensor-product algebras are hyperfinite; automorphisms extend normally and preserve the trace (RWW Section 3.1 and Lemma 3.8). No finite-dimensional substitute for that theorem is silently used. Parts (ii) of the localization lemmas, concerning detailed tails of individual corrections, are not needed for this constant extraction.

## P4. Blocking, stabilization and index identification

Partition the original chain into the `j`-site cells `[kj+1,(k+1)j]`. Equation (P3) makes `gamma` an `f(j)`-nearest-neighbour automorphism on this blocked chain. If `f(j)<=e_Q`, P3 gives a QCA `beta_j`, radius two in blocked units, and

\[
 \| (\gamma-\beta_j)|_{\mathcal A(Y)}\|
       \le C_Q f(j)N_j(Y),                                \tag{P6}
\]

where `N_j(Y)` is the number of blocked cells covering `Y`. In particular `N_j(X_j)=4`. A safe radius in the original site metric is `3j`; this avoids treating coarse-cell radius as exactly the same metric quantity. The finite-window index formula below will be used directly in the blocked chain.

Assume

\[
                 C_Q f(j)\le1/3456.                      \tag{P7}
\]

This implies `f(j)<=e_Q`; monotonicity gives the same for every integer `k>=j`. For adjacent `k,k+1`, both QCAs have radius at most `3(k+1)` in original units. Block by that length. On the two neighbouring cells `Y=[1,6(k+1)]`, the numbers of cells in the constructions of `beta_k,beta_{k+1}` are at most twelve and six, respectively. Therefore

\[
 \| (\beta_k-\beta_{k+1})|_{\mathcal A(Y)}\|
      \le18 C_Q f(k)\le1/192.                            \tag{P8}
\]

RWW Proposition 4.10 then gives equality of their indices. Consequently all indices for `k>=j` agree.

This stabilized value is the RWW index of `gamma`. To check the identification rather than stipulate it, compare `beta_k` with any defining QCA sequence from RWW Theorem 5.6/Definition 5.7. On `Y=[1,6k]`, the difference tends to zero: (P6) contributes `6C_Q f(k)` and the defining sequence contributes `O(f(k))`. Both radii are at most `3k`. Proposition 4.10 eventually equates their indices. Its qualitative constant may depend on the fixed chain and its tails; it is used only to identify the common limiting integer/logarithmic index. The explicit finite stabilization threshold (P7) has no such dependence.

Thus (P7) proves

\[
                \operatorname{ind}\gamma
                   =\operatorname{ind}\beta_j.           \tag{P9}
\]

This proof uses no rounding in a possibly non-discrete multi-prime logarithmic subgroup and no interchange of `L->infinity` with an uncontrolled `j->infinity` limit.

## P5. Full-factor norm control gives a quadratic Bell-pair loss

Let `alpha` be any trace-preserving automorphism of the quasi-local algebra, and let `F=M_m` be a finite full matrix tensor factor. Suppose `||(alpha-id)|_F||<=eta`. On two copies of the algebra use the Choi state

\[
 \phi_\alpha(a\otimes b)=\tau(\alpha(a)b^T),             \tag{P10}
\]

where transposition is fixed in the tensor-product basis. Its local restrictions are ordinary finite density matrices. For an orthogonal unitary Weyl basis `{W_l}_{l=1}^{m^2}` of `M_m`, the Bell projector is

\[
 P_F=|\Omega_m\rangle\langle\Omega_m|
       ={1\over m^2}\sum_l W_l\otimes\overline {W_l}.
                                                               \tag{P11}
\]

The normalization follows either by Weyl averaging or by applying the sum to the matrix-unit basis; the resulting rank-one projector has trace one. Since `(overline W)^T=W^*`,

\[
 p:=\phi_\alpha(P_F)
    ={1\over m^2}\sum_l\tau(\alpha(W_l)W_l^*).
                                                               \tag{P12}
\]

For each `W_l`, automorphism and trace properties give

\[
 2-2\operatorname{Re}\tau(\alpha(W_l)W_l^*)
 =\tau((\alpha(W_l)-W_l)^*(\alpha(W_l)-W_l))
 \le\eta^2.
\]

The average in (P12) is real because it is a projector expectation. Hence

\[
                     p\ge1-\eta^2/2.                    \tag{P13}
\]

There is no factor `m` or `m²`: the Weyl sum is normalized, and the hypothesis controls every unitary in that sum. This does not assert that an arbitrary linear map's completely bounded norm equals its ordinary norm. No diamond-norm estimate is used.

For a density matrix `rho` on `FF'` and any remaining finite factors, if `p=Tr(P_F rho)>0`, define

\[
 \sigma={P_F\rho P_F\over p}
            =|\Omega_m\rangle\langle\Omega_m|\otimes\sigma_{\rm rest}.
\]

Purify `rho`, project that purification by `P_F`, and normalize. The two purifications have overlap `sqrt(p)`, so their trace distance is `sqrt(1-p)`. Contractivity under partial trace proves

\[
 {1\over2}\|\rho-\sigma\|_1\le\sqrt{1-p}
                       \le\eta/\sqrt2.                  \tag{P14}
\]

The trace-distance formula for pure states follows by diagonalizing their difference on their two-dimensional span. Thus (P14) needs no boundary-value or infinite-dimensional entropy limit.

## P6. Finite entropy continuity with explicit dimensions

For density matrices `rho,sigma` on dimension `D`, let `x=||rho-sigma||_1/2`. For `x>0`, write their Jordan difference as `rho-sigma=x(tau_+-tau_-)`, with `tau_±` density matrices. The common state

\[
 \omega={\rho+x\tau_-\over1+x}
        ={\sigma+x\tau_+\over1+x}
\]

and the lower/upper entropy-of-mixture bounds imply

\[
                 |S(\rho)-S(\sigma)|
                    \le x\log D+g(x).                   \tag{P15}
\]

Indeed, compare the concavity lower bound for the first mixture with the upper bound for the second, then reverse them. The difference of the two auxiliary entropies has magnitude at most `log D`; multiplying by `1+x` gives the mixing term `(1+x)h(x/(1+x))=g(x)`. The entropy-of-mixture bounds are the finite flag-state concavity bound and its upper bound obtained by retaining the binary flag. The case `x=0` follows directly. Both terms in the right side increase with `x`.

For a bipartite state with dimensions `D_A,D_B`, applying (P15) to its two marginals and joint density matrix, and using trace-norm contraction, gives

\[
 |I(A:B)_\rho-I(A:B)_\sigma|
   \le2x(\log D_A+\log D_B)+3g(x).                       \tag{P16}
\]

This is intentionally weaker than optimal continuity estimates. Its logarithmic dimension dependence is sufficient here.

## P7. Strict-QCA partial-factor bound

Suppose first that `alpha` is a QCA of radius `r>=1` on the chain with supersite dimension `d_s`. Set `L=[-r+1,0]`, `R=[1,r]`, `X=L union R`. If `||(alpha-id)|_{A_I(X)}||<=eta<=1`, put `delta=eta/sqrt2`.

Restrict its Choi state to `XX'` and apply P5 with the entire interior factor `F=A_I(X)`. The projected state factors into Bell pairs on `I_L I_L'` and `I_R I_R'`, tensored with a state on all boundary factors. Consequently

\[
 I(L':R)_\sigma=I(B_L':B_R)_{\sigma_B},\qquad
 I(L:R')_\sigma=I(B_L:B_R')_{\sigma_B}.                    \tag{P17}
\]

Each quantity on the right is between zero and `2r log d_B`. Hence half the absolute difference is at most `r log d_B`, not twice that amount. Each mutual information on the left differs from its value in the original Choi state by at most `4r delta log d_s+3g(delta)`, by (P16). RWW Proposition 4.7's finite-window formula therefore gives

\[
 |\operatorname{ind}\alpha|
       \le r\log d_B+4r\delta\log d_s+3g(\delta).
                                                               \tag{P18}
\]

This bound applies at a single cut and requires no global factorization or gluing of correcting unitaries.

When `eta=0`, it yields the sharp range bound `r log d_B`, attained by translating every boundary factor by `r` sites while fixing all interior factors. More generally, if an automorphism fixes the infinite interior algebra pointwise, it preserves its relative commutant, the full boundary algebra, in both directions. It consequently factors as `id_I tensor alpha_B`. Exact identity alone is not a range bound: the `r` in this strict-QCA statement cannot be assigned to an ALPU without a quantified effective window.

## P8. The approximate partial-factor theorem for ALPUs

**Theorem.** Assume (P3), (P4), (P5) and (P7). Define

\[
 \eta=\epsilon+4C_Q f(j),\qquad 0\le\eta\le1,
 \qquad\delta=\eta/\sqrt2.                               \tag{P19}
\]

Then (P1) holds.

**Proof.** The QCA `beta_j` from P4 has index equal to that of `gamma`, and (P6) on `X_j` gives

\[
 \| (\beta_j-\mathrm{id})|_{\mathcal A_I(X_j)}\|
          \le\epsilon+4C_Qf(j)=\eta.
\]

Apply P7 to `beta_j` on the `j`-blocked chain. Its radius is two, one blocked supersite has dimensions `d_I^j,d_B^j`, and its two half-windows are exactly `L_j,R_j`. Thus (P18) is (P1). Every density matrix used in this step is finite. The infinite-chain input is confined to the matched RWW approximation, index formula and stability theorems. QED.

## P9. A separate near-intertwiner check of amplification

For completeness, on one finite full matrix subalgebra `F`, assume `||(alpha-id)|_F||<=eta<1`. The norm-convergent Haar integral

\[
 T=\int_{U(F)}\alpha(u)u^*\,du
\]

satisfies `||T-1||<=eta` and `alpha(v)T=Tv` for every unitary `v in F`, by Haar invariance. Since `T` is invertible, its polar unitary `U=T(T^*T)^(-1/2)` also intertwines: `alpha(v)U=Uv`. The positive factor commutes with `F`. Its singular values lie in `[1-eta,1+eta]`, so `||U-T||<=eta` and `||U-1||<=2eta`. Thus on this factor `alpha=Ad U`, with completely bounded displacement at most `4eta`.

This provides a different algebraic check that nearby homomorphisms have no uncontrolled amplification cost in this setting. It neither asserts a global family of compatible correcting unitaries nor establishes their locality. The proof of P8 does not need such a family. For arbitrary linear maps this conclusion fails; the finite transpose control in P13 distinguishes that hypothesis.

## P10. Explicit tube dimensions and logarithmic windows

Let spatial dimension `d>=2` be fixed. For a tube `Z times {1,...,L}^{d-1}`, use the middle transverse cube `{R+1,...,L-R}^{d-1}`, where `1<=R<L/2`. Set

\[
 V=L^{d-1},\quad V_I=(L-2R)^{d-1},\quad B=V-V_I,
 \quad d_I=2^{V_I},\quad d_B=2^B.                       \tag{P20}
\]

Suppose a family `gamma_L` obeys, for constants `A,E>=1` and `mu,nu>0` independent of `L,R,n`,

\[
 f_L(r)\le A L^{d-1}e^{-\mu r},\qquad
 \| (\gamma_L-\mathrm{id})|_{\mathcal A_I(X)}\|
       \le E n L^{d-1}e^{-\nu R}                         \tag{P21}
\]

for every longitudinal `n`-site interval `X`. It suffices to impose the second bound on the final `4j`-site interval. Define, for integers `L>=2`,

\[
 j=\left\lceil\mu^{-1}\log(3456C_Q A L^{d+3})\right\rceil,
 \quad
 R=\left\lceil\nu^{-1}\log(8E j L^{d+3})\right\rceil.
                                                               \tag{P22}
\]

Use this formula only when `R<L/2`. It gives

\[
 C_Q f_L(j)\le {L^{-4}\over3456},\qquad
 \epsilon\le\tfrac12L^{-4},\qquad
 \eta\le(\tfrac12+\tfrac1{864})L^{-4}<L^{-4}.             \tag{P23}
\]

Since `B<=2(d-1)R L^{d-2}`, P8 yields the explicit estimate

\[
 { |\operatorname{ind}\gamma_L|\over V\log2}
 \le {4(d-1)jR\over L}+8jL^{-4}
                 +{3g(L^{-4})\over L^{d-1}\log2}.        \tag{P24}
\]

The first term is `O(log² L/L)`, the second `O(log L/L^4)`, and the last tends to zero. In particular the right side tends to zero with all listed constants fixed. This is a quantitative boundary-size estimate despite the exponentially large supersite dimension. For a proposed fixed integer shift index `q V log 2`, (P24) is a finite, falsifiable necessary inequality with `|q|` on the left.

## P11. Matching finite-range Hamiltonian tubes to (P21)

This section is conditional mathematical dynamics, not an axiom identification. Assume an interaction on `Z^d` with terms `h_Z`, range `ell_0` in the `ell^1` distance and

\[
           J=\sup_x\sum_{Z\ni x}\|h_Z\|<\infty.
\]

Fix a finite time `t` and integer shift `q`, with `tau_q(A_n)=A_{n-q}` in the RWW convention. Write `alpha_t` for the infinite-volume dynamics and `alpha_t^W` for the dynamics retaining only terms wholly contained in the tube `W`; extend the latter by the identity on its complement. Assume, for this application, the exact identity `alpha_t=tau_q` on the full quasi-local algebra. Define `gamma_L=(alpha_t^W)^(-1) tau_q` on the tube. Reversing the translation convention changes only the sign of the index.

For any fixed `a>0`, set `F(s)=e^{-as}/(1+s)^{d+1}`. Its interaction norm is at most `N_F=J e^{a ell_0}(1+ell_0)^{d+1}`: pairs farther apart than the range contribute zero, and all other pair sums are at most `J`. Removing terms cannot increase this norm. Write `C_F=sup_{x,y} sum_z F(|x-z|_1)F(|z-y|_1)/F(|x-y|_1)`. It is finite, and `C_F>=1` because `F(0)=1`. These are the hypotheses of RWW Theorem 3.2. More explicitly, Nachtergaele–Sims–Young (NSY) Theorem 3.1, equations (3.21)–(3.24), gives the coefficient `2(C_F)^{-1}(exp(2 C_F |t| N_F)-1)` for disjoint supports, uniformly in finite volume. Their Theorem 3.5 and Corollary 3.6 give the norm limit and the same bound in infinite volume. A safe choice is

\[
 C_t=2\exp(2C_F|t|N_F)\ge2.
\]

It depends only on `d,a,J,ell_0,|t|`, and also covers overlapping supports by the trivial commutator bound. Hence, independently of tube width, truncation volume and `|s|<=|t|`, one has

\[
 \|[\alpha_s^W(x),y]\|
 \le C_t\|x\|\|y\|\sum_{z\in\operatorname{supp}x}
                        \sum_{w\in\operatorname{supp}y}e^{-a|z-w|_1}.
                                                               \tag{P25}
\]

The same bound applies to the full dynamics. This is a matched literature import from [NSY, arXiv:1810.02428v2](https://arxiv.org/pdf/1810.02428v2), whose exact source and selected reading scope are recorded below; the estimates that turn it into (P21) are as follows. Let

\[
 S_k(b)=\sum_{z\in\mathbb Z^k}e^{-b|z|_1}
       =\left({1+e^{-b}\over1-e^{-b}}\right)^k.
\]

**Longitudinal tails.** Sum first over transverse sites in the second support. Their total for each first transverse site is at most `S_{d-1}(a)`, giving a factor `V S_{d-1}(a)`, rather than `V²`. Across the two longitudinal endpoints, the remaining sum is bounded by `4 e^{-ar}/(1-e^{-a})²`, independently of the interval length. Averaging over outside unitaries, equivalently the near-commutant conditional expectation in RWW Lemma 2.4, bounds the distance to the expanded interval algebra. The shift changes `r` by at most `|q|`. Consequently a valid constant is

\[
 \mu=a,\qquad
 A=\max\left\{1,{4 C_t S_{d-1}(a)e^{a|q|}\over(1-e^{-a})^2}\right\}.
                                                               \tag{P26}
\]

This controls every finite interval and then every infinite interval by norm approximation, as in RWW Lemma 3.10. For small `r<|q|`, the enlarged right side is at least one and the zero approximant suffices.

**Interior identity error.** For `x` supported on `n` interior slices,

\[
 \|\gamma_L(x)-x\|
       =\|\alpha_t(x)-\alpha_t^W(x)\|.
\]

In finite volume, Duhamel's formula bounds this by the time integral of commutators of `alpha_s^W(x)` with the omitted interaction terms. Terms wholly outside `W` commute with this operator; only terms crossing the tube boundary remain. Each site in such a term is within `ell_0` of the boundary, hence at distance at least `R-ell_0` from an interior support site. Using (P25), the bound `J`, and

\[
 \sum_{w\ {\rm near\ boundary}}e^{-a|z-w|_1}
 \le e^{-a(R-\ell_0)/2}S_d(a/2),
\]

gives

\[
 \|\gamma_L(x)-x\|
 \le |t|C_t J S_d(a/2)e^{a\ell_0/2}
             n V e^{-aR/2}\|x\|.                         \tag{P27}
\]

The estimate remains valid when `R<ell_0`, since its right side is only enlarged. The sum is absolutely convergent for each finite support, uniformly in the outer truncation volume, which justifies the thermodynamic limit of the finite-volume Duhamel estimate. Thus choose

\[
 \nu=a/2,\qquad
 E=\max\{1,|t|C_t J S_d(a/2)e^{a\ell_0/2}\}.             \tag{P28}
\]

This deliberately uses the full support volume `nV`; it needs no sharper boundary-area prefactor. The polynomial loss is absorbed by (P22).

For each fixed `L`, the path of tube dynamics is strongly continuous with one exponential tail bound for all times between zero and `t`, by the same estimates. RWW Theorem 5.15 therefore gives its index zero. The transverse supersite is finite, though its dimension grows with `L`. Additivity and the shift normalization then give

\[
           \operatorname{ind}\gamma_L=q V\log2.           \tag{P29}
\]

All hypotheses entering (P24) are now matched. Combining (P24) and (P29) produces a necessary inequality whose right side tends to zero for fixed `q,t,J,ell_0,d`. The finite inequalities are the proved application; no alternative non-Hamiltonian or non-automorphic dynamics is constrained by this calculation.

## P12. Relation to N1 and preserved limits

N1's reduction from exact integrated first-moment closure to `tau_q=Ad exp(-i q P_b/beta)` also assumes its gap/unique-vacuum setting, the specified exact continuous-momentum scattering completeness and common rational centres. Those assumptions are not proved here. Its local momentum generator has finite-range uniformly bounded interactions by its own H-loc premise, so P11 is the corresponding mathematical tube estimate once the global shift identity is supplied. The normalization must use generator `P_b` at time `q/beta`, or generator `P_b/beta` at time `q`; the source's line 178 divides by `beta` twice.

The smooth global-band obstruction is not used. Nothing here infers a full-torus regular band from a local Haag–Ruelle shell, proves a preferred microscopic Hamiltonian, or upgrades a candidate-law/referee label into retained status. Neither nonlinear momentum actions nor long-range interactions outside the stated decay class are ruled out. The inequality remains conditional on automorphisms and the full block norm, not merely local expectation agreement.

## P13. Checks, failures and alternative routes

The publication runner is [finite partial-factor controls](../scripts/approximate_partial_factor_index_2026_10_11.py). The milestone packet preserves the original author runner, full baseline and mutation records, the separate review, and publication execution identities. Exact matrix/count checks and floating density-matrix examples are separated. No finite ring is assigned an infinite-chain index: its central window is used only when the explicit QCA rule has the same local Choi restriction. In the four-site density-matrix example, the wrap edge connects the two unselected sites and is not used in transporting an operator on either selected site.

The controls cover normalized Weyl/Bell identities; the quadratic Bell-loss estimate using actual conjugation matrices; an exact one-block intertwiner/polar correction; product-phase accumulation as a full-block versus single-site norm discriminator; partial transpose as an amplification discriminator outside the homomorphism class; independent Bell-edge entropy counts for shifts of each tensor factor; a gate-perturbed boundary shift using an actual finite Choi density matrix and its normalized Bell projection; the RWW constant/covering counts; and the tube resource formula. Finite controls do not prove the hyperfinite algebra-stability theorem, thermodynamic limit, or infinite-chain classification imported from RWW.

The initial square-root-in-operator-error route was valid but weaker: bounding each overlap linearly gives trace error `sqrt(eta)`. Unitarity and the tracial two-norm sharpen this to `eta/sqrt2`. A direct application of the qualitative `C_f` in Theorem 5.6 would leave its dependence on the tube-width tail amplitude untracked; P3 avoids this by tracking Proposition 5.5 instead. A global gluing of one-block intertwining unitaries was not proved or needed. No claim that such gluing is impossible is made. A direct infinite-half-chain entropy proof was not pursued after the finite-QCA route closed the chosen estimate.

The safe fine-site radius `3j` is used only for comparing blocking scales; the entropy formula is evaluated in the original `j`-blocked chain, where the constructed QCA has radius two. This distinction avoids silently transferring an exact physical radius through a change of cell size. The temporary setup error used a not-yet-created external working directory; it ran no process and is preserved in `setup_failure.txt`. Any subsequent failed numerical or mutation execution is preserved rather than overwritten.

## P14. Source coverage, claim boundary and remaining obligations

The complete N1/B1/M1 report arguments and short referees were read at the exact unchanged identities during the frozen C4 assessment. N1's full referee was also read completely. Those readings are reused here; capture alone is not claimed as a new review. The exact copies used in this probe are rehashed in the receipt. The local pinned main searched for matching statements is `a13caa4885f547c8d206265b031ba7649e539fd9`; the refined statement searches have no matching hits, while the initial broad expression matched unrelated occurrences of “choice.” This is a scoped repository prior-art check, not a literature-wide priority claim.

RWW's PDF pages 11–49 and 51 were read in full for the statements/proofs named above; page 68 was read for the primary LR reference. In particular the load-bearing constant route reads Theorem 2.6(i), Lemma 2.7, the tracial extension/ALPU definitions, Proposition 4.7, Proposition 4.10/Remark 4.11, Lemmas 5.1(i), 5.3(i), Proposition 5.4(i), Proposition 5.5, and the index-stability/identification argument. Theorem 3.2 and Theorem 5.15 are imported with their stated hypotheses. The full proof of Christensen-type near-inclusion stability in Appendix B was not independently reconstructed. No universal index-rounding claim for a multi-prime logarithmic subgroup is used.

NSY arXiv:1810.02428v2 has PDF SHA-256 `42fc3029fa582f14a01f858463f481d5cacf21ed785791d32c72dd9df97f66cd`. Its PDF pages 17–21 and 25–28 were read completely: the interaction and F-norm definitions, the volume-uniform LR statement, Duhamel comparison, norm thermodynamic limit and infinite-volume corollary. The proof of its LR theorem on pages 22–24 was not independently reconstructed; the theorem is imported. No full reading of the 106-page paper is claimed. The finite-range norm check and microscopic sums in P11 are supplied here, including `C_t>=2` for overlapping supports and the small-radius zero-approximant case.

The new proof obligation discharged is the dimension-controlled approximate partial-factor bound and its logarithmic-window use, not the physical premises of N1. Independent review of the complete proof and extracted constants found no material correction at the stated mathematical scope. Its report SHA-256 is `9118707fdcc85cdfd0a1160598872fb8544a9de757b3a1efe8e93292719c533c`; the milestone packet records the full reconstruction, source coverage and independent geometric check. No Lean verification, audit outcome or source edit to PR9476 is claimed. Original receipts and finite controls remain supporting evidence at their exact identities; they do not replace the analytic proof or the independent audit path.

## P15. No-go discipline at the exact conditional scope

The primary result is the positive inequality (P1). Its negative implication is restricted to a family simultaneously satisfying (P21) with fixed constants and the extensive fixed-shift index (P29). This is not a claim that no native dynamics, momentum observable, emergent boost, or Record model exists.

**N1 — Alternative mechanisms tested against that implication.** Five distinguishable mechanisms were examined: (a) amplification on an interior/reference tensor product, addressed by the exact Weyl/Bell and near-intertwiner proofs and tested against the non-homomorphic transpose; (b) large entropy capacity despite small trace error, addressed by the explicit logarithmic dimension bound (P15)–(P16), with actual density-matrix checks; (c) concentrating arbitrarily large transport in a small boundary factor, tested by boundary shifts and allowed by (P18) when their range/window grows—this does not obey the fixed-constant logarithmic-window consequence if the index remains extensive; (d) hiding a different index outside the tested window, addressed by the finite-QCA formula and the matched RWW stability theorem, with the exact window and covering counts retained; (e) a transverse-volume growth of the effective propagation speed, addressed in P11 by summing the microscopic LR kernel before replacing a slice with a supersite. Items (a), (b), (c), and (e) were attempted in this probe; item (d) uses checked primary theorems and the new explicit stabilization bookkeeping. These are scoped mathematical attack checks, not five independently exhausted physical theories or a claim that RWW is repository-retained physics authority.

**N2 — Wall relations.** No count of independent physical walls is claimed. A valid microscopic finite-range Hamiltonian bound implies the locality estimates used in P21; they are therefore not counted as independent conditions. The block-norm premise is separately needed for the abstract lemma; P11 derives it when the exact global shift identity is supplied. Relationships among N1's representation, gap, completeness and rational-centre conditions are not reclassified here.

**N3 — Hidden-premise scan.** The assumptions are the automorphism/full-factor/tail conditions P2, the imported RWW theorems P3–P4, finite entropy identities P5–P6, and the separately stated Hamiltonian/shift hypotheses P11. “Canonical” physical identification, an implicit diamond estimate, a global regular band, uniformity of an untracked `C_f`, global gluing, and a supersite-independent Hamiltonian norm are not used. “By construction” refers only to the explicit block algebra or the cited RWW construction, with its hypotheses spelled out.

**N4 — Residual matching.** N1's approximate Lemma B is the matching target. The B1 bounded-sector boost argument and M1 global-band obstruction are context, not witnesses for the present inequality. RWW's one-dimensional index theorems are used only after the tube is a one-dimensional chain of finite supersites; they are not cited as an already-proved higher-dimensional tube result.

**N5 — Resolution.** The core norm is on a complete finite interior block algebra. Single-site or selected-state tests do not substitute for it. The tube conclusion concerns a family of full qubit tensor-product automorphisms with the stated uniform locality bounds, not arbitrary per-mode dynamics, a subsystem channel, or permanent Records. The finite controls distinguish those scopes and do not test a lattice-wide physical theory.

**N6 — Partial closure.** This proves the named approximate-index estimate under imports already identified by N1. It is not a request to adopt a new physical axiom. The primitive registry was inspected; no dimensionful reference, isotropy convention or realized-state primitive is needed for or mislabeled as a wall of this dimensionless algebra theorem.

**N7 — Steelman.** The strongest objection is that apparent smallness might be only pointwise, that the QCA approximation's constants might grow with the exponentially large slice dimension, or that microscopic LR estimates might degrade into a slice-size propagation speed. Any of those substitutions would invalidate the proposed tube inference. P2 insists on the full block norm, P3 extracts dimension-independent constants from the primary construction, and P11 retains the microscopic metric when summing tails. Those three steps were explicit targets of the independent source reconstruction. An alternative model outside the hypotheses is a scope change, not a contradiction of the inequality.

**N8 — Prior echo and status.** The exact source of the previous unresolved estimate is preserved. This proof takes the suggested entropy route but replaces its uncontrolled ALPU entropy limit with a finite-QCA approximation and quadratic Bell-loss estimate. Scoped main searches found no matching theorem, and no broad absence claim follows from those searches. This milestone does not request a formal no-go packet PASS, apply an audit verdict, or claim independent retained authority. The bounded theorem and its conditional consequence stand or fall on the displayed proof; procedural route counts and finite control outcomes are not proof.
