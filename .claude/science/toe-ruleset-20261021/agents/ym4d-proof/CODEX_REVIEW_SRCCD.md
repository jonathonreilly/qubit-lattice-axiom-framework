# PRE-STATED

Independent hostile review of `SRCCD55.md` in the same directory. Written before reading its proofs or running its checks. Prior exposure: the user's claim list, the repository workflow, and a heading/claim/locator search of the target (including the existence of its appended errata). This is not a blinded review. No git operations; the sole writable artifact is this file. No scientific or audit status is granted by this review.

Acceptance criteria, fixed before testing:

1. Proposition B must follow from the actual normalized joint soft-chain law, including its reverse conditional law. Derive the conditional covariance identity independently and challenge it with an exact non-Markov example. Inspect and, if they do not write other files, execute `sc55_tel` and its controls.
2. Proposition A must state the conditional source representation it assumes, justify deleting any coarse remainder, and justify counterterm cancellation, differentiation, connected support, and uniform scale summation. A conditional identity is not a construction of the representation or its ultraviolet weights.
3. Lemma V must supply an unconditional finite-volume argument with correct conditioning, independent link selection, group/trace normalization, exact variance constants, and quantifiers on the coupling, torus, and test function. Inspect `sc55_vm` and independently check any numerical threshold with rational arithmetic. Infer an inconsistency of SRC-E only with the additional premises that actually imply it.
4. Audit every clause of SRC-kappa, SRC-M, SRC-I and Propositions C-E for missing norms, support restrictions, large-field quantifiers, factorial growth, powers of the cutoff, and volume dependence. Separate a formally sufficient hypothesis from a proved input. OS literature recalled without checking is labelled [m].
5. Check the Ward insertion contact term and the claimed repair without assuming the desired rotation-invariant continuum limit. Check the logarithmic and power-rate optimizations algebraically.

Verdicts are CONFIRMED, NOT-VERIFIED, or REFUTED, each with a file and locating string. CONFIRMED is confined to the stated domain and explicit premises; NOT-VERIFIED denotes an unclosed obligation; REFUTED requires an explicit contradiction, counterexample, or demonstrably invalid asserted inference. All computations use exact arithmetic. Literature recollections carry [m]. The final section will state exactly what may be banked.

## Scope and disposition

One independent review pass, including all of `SRCCD55.md` and errata E1–E14, the two scripts and their criteria/output, and the dependency ranges cited below. The local review-loop and no-go-discipline procedures were used for proof, runner, and negative-claim scrutiny. The user's no-git/single-output restriction controls: no source fixes, other output files, repository-status changes, or landing/audit operations were performed. This is a review of the local snapshot, not a verification of current-main status. Other lanes' theorem-status summaries are not independently certified here.

The core outcome is mixed. **Proposition B and the exact source recursion are CONFIRMED. Lemma V's lower bound is CONFIRMED, with E2 and the qualifications below.** The implication package A–E is not correct as a whole: B′ drops intermediate large fields; A uses an invalid spanning-tree inequality; C's corrected path argument still uses the wrong Euclidean distance conversion; D does not supply all the moments and matching bounds it uses; E omits conditional means and asserts uniform high moments not implied by SRC-I. These defects do not refute conditional decay, OS0, or constructive Yang–Mills. They refute particular inferences or leave the claimed Wilson conclusions NOT-VERIFIED.

Snapshot identities (SHA-256):

```text
SRCCD55.md       80a347f5d2bc801fc0395b6d61aa5c0661dd098ae4430bcf760b874729761d03
sc55_tel.py      6c40f57506ebcbea557db8a78f918497fd6e2e0fccadda87c829003770116389
sc55_vm.py       69d835a578797d9736609c989afed386293629420fa36433b702ae6845e95fc2
```

Paths below are relative to this directory unless stated otherwise. `EXISTENCE.md` means `../ym4d-existence/EXISTENCE.md`.

## 1. Proposition B and source recursion

**CONFIRMED.** Files/locators: `SRCCD55.md`, “Proposition B”, “(B1)”, “(B2)”, and “5.0 The exact source recursion”; `RLARGE.md`, “The exact chain”; `ROTDEF.md`, “5.1 The chain”.

The actual soft kernels are normalized in the outgoing variable. Their couplings are parameters of the joint law, not history-dependent random variables. Thus the normalized joint law is a level-index Markov chain. This is not a claim of spatial independence.

An independent derivation uses repeated conditional total covariance. Put

```text
μ_i = law of U_i,
Q_i(du | v) = μ_i(du) K_i(v,u) / μ_{i+1}(v),
G_i = E[G | U_i],  H_i = E[H | U_i],
C_i = Cov(G,H | U_i).
```

At positive marginal density, Bayes' formula gives `Q_i` exactly; null marginal sets are immaterial. Past and future are conditionally independent given `U_i`. Consequently

```text
C_{i+1} = E[C_i | U_{i+1}] + Cov(G_i,H_i | U_{i+1}).
```

Since `C_0=0`, iterating and using the same conditional independence gives (B1). Equivalently, the reverse-martingale differences in the target are orthogonal conditionally on `U_K`. The lack of nesting of `σ(U_i)` alone is harmless: the Markov property supplies the missing tower step. The target correctly uses the nested tail filtration for its proof.

The reverse law is the **normalized** RG-step integrand, including the full exact effective density `exp(-S_i)`. It is not merely the Wilson term, the classical minimizing background, or the Gaussian approximation to that step.

For a fixed source direction `A`, the exact recursion is

```text
Φ_{i+1}(t) = log E[exp Φ_i(t) | U_{i+1}],
Φ'_{i+1}(0) = E[Φ'_i(0) | U_{i+1}],
Φ''_{i+1}(0) = E[Φ''_i(0) | U_{i+1}]
                 + Var(Φ'_i(0) | U_{i+1}).
```

For two different source directions the last term is their covariance. Higher derivatives are triangular, with conditional cumulants of lower derivatives as inhomogeneities. Also `Φ_K = -(S_K(η)-S_K(0))` for the source-perturbed action defined with the same fixed kernels. All of this is exact near zero source, where the logarithm is defined. A uniform complex polydisc is a further analytic hypothesis, not a consequence of triangularity.

**CONFIRMED, finite checks only.** File/locators: `checks/sc55_tel.py`, `lhs`, `rhs`, `markov_property_holds`; criteria “T1”, “C1b”, “C2”. The script reproduced 50/50 Markov equalities and 50/50 non-Markov tail-filtration equalities; both controls fired. It tests the appropriate distinction. It does not test Wilson dynamics or decay.

Independent exact examples:

* Let `U_0` be a fair sign; let `U_1` agree with it with probability `3/4`, and `U_2` agree with `U_1` with probability `2/3`. For `G=H=U_0`, at either terminal sign, (B1) reads `35/36 = 3/4 + 2/9`.
* Let `U_0=U_2` be a fair bit and `U_1` an independent fair bit. Then the left side is zero, the incorrect Markov-form right side is `1/4`, and the tail-filtration right side is zero. Thus a tower-property argument without Markov would indeed be false.

**NOT-VERIFIED as a decay theorem; the omitted-large-field inference is REFUTED.** File/locator: `SRCCD55.md`, “Corollary B′”, specifically “every U_{i+1} in the level-(i+1) small-field set”.

B1 averages over **all** intermediate fields, even when the terminal field is small. B′ supplies its pointwise bound only on intermediate small fields. The bound on `E[c_i|U_K]` does not bound the covariance on the complementary event. The proof silently applies the small-field inequality there too.

A finite exact witness to this inference: take `K=2`, `U_2=0`, `P(U_1=0)=P(U_1=1)=1/2`. Given `U_1=0`, set `U_0=0`; given `U_1=1`, let `U_0` be a fair sign. Declare `U_1=0` small. For `G=H=U_0`, every stated small-field covariance is zero, and `G_1=H_1=0`, but `Var(G|U_2)=1/2`. These are normalized Markov kernels of the class in Proposition B. The example exposes the probabilistic omission; it is not a counterexample to Wilson CD. Strictly positive approximations keep an order-one terminal variance while making the small-field contribution arbitrarily small.

The repair is to bound the full one-step law, or to retain and estimate

```text
E[1_{U_{i+1} outside small fields}
  |Cov(G_i,H_i|U_{i+1})| | U_K]
```

at every step. Once this is done, the scale series displayed in B′ converges as claimed. No physical mass gap follows from B1 itself.

## 2. Proposition A: valid differentiation, overclaimed geometry and mechanism

**CONFIRMED, conditional cancellation and Cauchy estimate.** Files/locators: `SRCCD55.md`, “Proposition A”, proof steps (1)–(3); `EXISTENCE.md`, “Lemma X-SRC-CT” and “Lemma X-SRC-RED”.

For disjoint source supports, `η=Σz_i h_i` lies in the stipulated sup-norm polydisc. A local source counterterm of range less than half the support separation depends on at most one `z_i`; its mixed derivative vanishes. A polymer missing any source support also vanishes after mixed differentiation. Cauchy's estimate for the multi-index `(1,...,1)` has factor `r_0^{-n}` and **no extra `n!`**. The same argument works for a stipulated linear insertion. Rooting the polymer sum at a source support improves the extensive volume factor to the number of cubes meeting that support.

**REFUTED, the asserted geometric inequality. NOT-VERIFIED, the full stated multi-point bound at its advertised rate.** Files/locators: `SRCCD55.md`, Proposition A step (4), “d_r(X) ≥ τ_r − c”; §3.1, “minimal spanning-tree length”; `LINEAR_PACKAGE.md`, Theorem 5.1, “infimum of lengths of connected unions of segments”.

The polymer distance is a touching/Steiner-network length, whereas `tree(X_1,...,X_n)` was defined as a minimum spanning-tree length. These are different. In cube units take four small terminal supports at

```text
(t,0,0,0), (-t,0,0,0), (0,t,0,0), (0,-t,0,0).
```

The cross joining them has length `4t`. Let the polymer consist of the cubes touched by that cross. Its touching length is at most `4t` up to endpoint conventions. The terminal MST has length `3√2 t`. Since `18>16`, the difference grows linearly in `t` and cannot be absorbed in a fixed cube-diameter constant `c`, even with four insertions fixed. The step quoted above is false under the referenced definition of `d_r`.

A safe repair uses Steiner length consistently, or the bound `d_r ≥ MST/2 - C n`, with the corresponding rate and order-dependent prefactor. For **two separated sets**, the elementary bound `d_r ≥ dist/(Mℓ_r)-4` used in EXISTENCE is valid. A polymer meeting the distant insertion and the union of the two observable supports gives this same two-set estimate. Thus the basic conditional separated-support CD mechanism survives; the stated general MST formula does not.

**CONFIRMED, the scope reduction in E12; NOT-VERIFIED, “SRC-poly implies SRC-κ” without that reduction.** File/locators: `SRCCD55.md`, “SRC-poly (the mechanism; implies SRC-κ by Proposition A)” and erratum E12.

`sup_r A_r<∞` is needed for the asserted scale-uniform estimates. The fixed sup-norm source polydisc controls smeared observables, not the cutoff-independent pointwise weights in κ-1. Differentiating a source supported at a single fine site introduces `a^{-4}` per insertion. To replace these factors by separation-dependent weights requires the scale-adapted volume-fraction estimate named in E12. That estimate is an additional input. In particular, A does not prove the all-order OS0 input.

**CONFIRMED as an exact effective-action identity; NOT-VERIFIED as an implication from H-Bal-loc.** Files/locators: `SRCCD55.md`, “There is no unit-scale remainder: U_K is not integrated”, §5.0 “Both sides are the log of the same ratio”; `EXISTENCE.md`, “H-Bal-loc”, including `[RX12-fix 1]`.

Holding `U_K` fixed removes the **final integration over `U_K`**. It does not prove that the remaining source-dependent effective action has the proposed local polymer representation, that its logarithm is uniformly analytic, or that any existing remainder has disappeared. H-Bal-loc is an unconditional `log Z` hypothesis with a bounded remainder; conditional locality is a stronger, separately stated hypothesis. The target does explicitly propose SRC-poly as a new hypothesis, which is legitimate. It should not present the deletion of the remainder as a theorem extracted from the unconditional hypothesis.

For the logical distinction, independent fair signs `X,Y` have unconditional generating function `cosh η cosh ζ`. Observing a sign `V` through the positive normalized kernel `(1+vXY/2)/2` gives `Cov(X,Y|V=v)=v/2`. Unconditional factorization did not imply conditional factorization. This example is about conditioning, not a proposed Wilson counterexample.

There is a related unclosed estimate in **Proposition F**: SRC-poly permits dependence on `U_K` in a fixed halo of radius `Mℓ_ref` around a polymer. Changing a coarse field at distance `ρ` only forces the polymer to approach within `Mℓ_ref` of that field, not to reach distance `ρ` itself. The displayed fine-scale exponent must account for that halo. Moreover bounded `A_r` alone does not bound an unsuppressed sum of one-point contributions over `K` scales. Quasi-locality with a uniform amplitude needs a corrected halo estimate and control of the local one-point sum; it is NOT-VERIFIED from SRC-poly as written. Locator: `SRCCD55.md`, “Proposition F”, “Only polymers reaching the changed cubes change”.

## 3. Lemma V and the precise SRC-E incompatibility

**CONFIRMED.** Files/locators: `SRCCD55.md`, “Lemma V”, Steps 0–6 and E2; `ROTDEF.md`, “e_a(x)”; `checks/sc55_vm.py`, “V4”. This confirmation is for real `f∈C_c^∞`, fixed `N≥2`, the even hypercubic tori in the statement, `u_0≥u_*(N)`, and the corrected `O_f(a²)` remainder. No RG, flow, or large-field hypothesis is needed for the lower bound itself.

The normalization and conditioning checks are substantive:

1. The clover definition gives `O_a(f)=Σ_p h(p)s(U_p)` with `h(p)=(1/2)Σ_corners f`. For `f=1`, it is `2Σ_p s(U_p)`, not the sum with coefficient one.
2. The product Haar-ball lower bound has `4|Λ|` links and `6|Λ|` plaquettes. It gives `F(u)≤((N²-1)/3)log u+C_N`. Concavity and `F≥0` then give the stated volume-independent `E_u s→0`. Existence of `u_1(N)` follows; an explicit threshold is not claimed.
3. On an even torus, the selected direction-1 links based at `(2aZ)^4` never share a plaquette. Conditioning on all other links therefore makes them independent. This yields the lower bound by a **sum** of conditional link variances without assuming positive correlations of plaquettes.
4. Circle-coset disintegration is valid for the embedded `diag(e^{is},e^{-is},1,...)` subgroup of `SU(N)`. The von Mises parameter is `κ=u_0|z|/N`. The quantity `|z|` is coset-invariant, even though the good plaquette event used to lower-bound its probability is not. Thus using `P(|z|≥1)≥1/2` after disintegration is legitimate.
5. The six staples have operator norm at most six. Hence `|z|≥12-NΣ_{p∋b}s(U_p)`, and the deterministic source variation bound is `|z^h-h_bz|≤12ω_b`, `ω_b≤2a‖∇f‖∞`. The factors of `N` cancel in the final lower bound.
6. For `κ≥4`, the two event probabilities multiply to `c_v=8e^{-5}/π³`. The cosine gap is at least `1/κ`. For the sine part, `sin x≥x-x³/6` at `x=2/√κ≤1` gives `κ sin²(2/√κ)≥25/9>27/10`. The Gaussian normalizer bound and the two-event variance inequality have the stated directions.

Assembly gives, before replacing the lattice sum by integrals,

```text
Var(O_a(f)) ≥ (c_v/288) g_0^4
             Σ_{x∈(2aZ)^4} (2|f(x)|-24a‖∇f‖∞)_+².
```

Using `(x-y)_+²≥x²-2xy`, the cell volume `16a⁴`, a smooth Riemann sum for `f²`, and the Lipschitz Riemann sum for `|f|` gives exactly

```text
Var(O_a(f)) ≥ (c_v/1152) g_0^4 a^{-4}
 [‖f‖₂² - 24a‖∇f‖∞‖f‖₁ - O_f(a²)].
```

E2 is necessary: the nonsmooth `|f|` term does not justify the original arbitrary-order remainder.

An independent rational certificate, not using the script's Machin/bisection implementation, is

```text
e < Σ_{j=0}^6 1/j! + (1/7!)/(1-1/8)
  = 31967/11760 < 87/32,
π < 22/7,
c_v/1152 = 1/(144 e^5 π³)
  > (32/87)^5 (7/22)^3 / 144
  = 89915392/59705842090653
  > 3/2000000.
```

The last difference is exactly `713257728041/119411684181306000000`. The bound `π<22/7` follows, for example, by polynomial division and integration of the positive function `x⁴(1-x)⁴/(1+x²)` on `[0,1]`, whose integral is `22/7-π`. Thus the advertised rational coefficient is certified independently.

**CONFIRMED, internal exact threshold checks; REFUTED, the printed enclosures.** Files/locators: `checks/sc55_vm.py`, `dec`, the five interval-print statements, and `VERDICT`; `checks/sc55_vm_out.txt`, “pi in” and “c_v/1152 in”.

The run reproduces V1–V5 PASS and the false-threshold control FIRED. Internally the Taylor, alternating-series, reciprocal, and square-root enclosures are rational and correctly directed. However `dec` floors **both** displayed endpoints. An interval such as `[3141592653,3141592653]/10^9` cannot contain π. The corrected outward-rounded coefficient display is

```text
c_v/1152 ∈ [1509091,1509092]/10^12.
```

This display defect does not invalidate the internal assertions or Lemma V. The script's 200-point test is a finite check, not a symbolic proof of the gap identity; direct common-denominator algebra proves that identity for every nonzero `κ`.

**CONFIRMED, a conditional incompatibility; NOT-VERIFIED, the unrestricted wording.** Files/locators: `SRCCD55.md`, “V-1”, “V-4”, §9 H1/H13, and “OS0 cannot be had from local moment bounds”; `ROTDEF.md`, “SRC-E (local moments)” and “Guard against a vacuous pass”.

For a real fine observable, exactly

```text
ν[(E_K G)²] + ν[Var(G|U_K)] = ω(G²).
```

For any fixed nonzero real `f`, SRC-E therefore forces `Z_e²≥c g_0⁴a^{-4}` for sufficiently small `a`. If a separated reflected pair has normalized covariance at least `c_0>0`, its **unnormalized** covariance must be at least `c_0 c g_0⁴a^{-4}`. Under `(F_R)`, this grows at least on the scale `a^{-4}/log²(1/a)` and contradicts any fixed-polylogarithmic upper bound for that same separated covariance. This is a valid incompatibility theorem.

It uses all of the following: the variance bound, non-vacuity for one separated pair, an unconditional separated upper bound, and a trajectory on which `g_0⁴a^{-4}` outgrows that upper bound. The small-field part of SRC-κ alone is not the unconditional upper bound; coarse images and large-field averaging must be controlled. Non-vacuity alone is insufficient.

The lower bound is unconditional, but **divergence is not uniform over arbitrary small-coupling trajectories**: for example `g_0=a²` makes its right side tend to zero. Nor does a one-sided lower bound establish an exact asymptotic equivalent. For the `u_0`-weighted action density in EXISTENCE's “X-SRC-GAP”, the lower bound instead contains `u_0²g_0⁴=1`, so its variance diverges at least as `a^{-4}` without this flow qualification.

The result rules out cutoff-uniform ordinary second/exponential moments for this clover-energy field with the specified non-vacuous normalization and separated upper bound. It is **not a theorem about every point-like dimension-4 composite**. Centering does not repair variance; positive-flow-time fields are different objects; subtracting local source counterterms changes Schwinger distributions and is not an ordinary positive-measure moment bound for the original random variable. These distinctions are the required scope of the correction to PANEL_P4.

## 4. SRC-κ, SRC-M, and SRC-I: counts versus sufficient hypotheses

**CONFIRMED, the formal component counts.** File/locators: `SRCCD55.md`, “3.2 The finite operator list” and “SRC-M (matching; the finitely many constants)”.

The listed entries number `1+4+16+10+16=47`. This is a component count, not a claim of 47 linearly independent operators. The real coefficients number `3+3+2=8`: three observable mixings, three insertion contacts, and two deviations `z_R` of current normalizations from one. It is the deviations `z_R`, not `Z_R=1+z_R`, that are proposed to be `O(g_bare²)`. Gauge invariance of the Ward variations follows from equivariance of the vector field. The stated symmetric local current is an additional existence/matching hypothesis, not furnished by the count.

**NOT-VERIFIED, a completely specified sufficient 47-operator package.** File/locators: `SRCCD55.md`, “(κ-2) One insertion”, “(N3) Output”, “(M-a)”, and Proposition D(iii).

There are concrete specification gaps:

* In κ-2, `n=0` invokes `δ_0=min_{j≠0}|x-x_j|`, with an empty index set. No one-point weight is defined. A convention of infinite distance would make `w_α` zero and demand vanishing **raw** conditional one-point functions. It should instead state a centered one-point clause, using κ-3, separately from separated cumulants.
* The dimension-four `τ_{μν}` weight must be distinguished from dimension-five `τ_ν`. “τ” alone does not specify which weight to use.
* D(iii) invokes bounds on `∇S^{(3)}` and `∇S^{(6′)}`, but the fixed clover tensors `S^{(3)},S^{(6′)}` are not in the 47-entry list. The statement does not explicitly identify their components with the controlled current components up to a bounded invertible matching and controlled remainders. An equation for `t_ν` with small coefficients does not separately bound these stress correlators. Add their source/coarse-image bounds, or give the missing matching. Smearing and summation by parts can move the derivative to the test function; they do not supply the missing bound on the tensor itself.
* E4 correctly makes `δ_c` a fixed **physical** distance and assigns the whole near region to M-b. The original multiple-of-`a` wording cannot be used. M-b must cover the full product observable, both contact neighborhoods, and the unconditional covariance after coarse averaging. A conditional contact formula alone would leave a coarse covariance.
* LF tree weights need a precise rule for shared cubes and branch multiplicities. A tree/path envelope at all orders is not automatically a uniform all-order integrability estimate; the explicit failure in §7 below applies.

The sizes of the eight coefficients, their cutoff/state/volume independence, and the remainder contraction remain NOT-VERIFIED hypotheses, as the target itself mostly acknowledges. Tree-level vanishing and engineering dimension do not prove the uniform nonperturbative `O(g_bare²)` estimate. Conditioning on `U_K` also supplies additional covariant data; finite-dimensional `H(4)` counting alone cannot exclude coarse-field-dependent contributions.

**CONFIRMED, the chessboard implication for matching block events. NOT-VERIFIED, the unqualified identification with every event/torus in §3.1.** Files/locators: `SRCCD55.md`, “SRC-I” and §6 “(M3)”; `EXISTENCE.md`, “Lemma CBE”, “Theorem CB”, “The disseminated hypothesis”; `RLARGE.md`, “Indicators” and “Thresholds”.

Given the reflection positivity and reflection-compatible even block partition in CBE, let `B_Q` be its reflected bad-block event. Set `f_Q=1_{B_Q}` for `Q∈A` and `f_Q=1` otherwise. CBE yields, without independence,

```text
P(∩_{Q∈A} B_Q)
 ≤ ∏_{Q∈A} P(∩_T B_T)^{1/N_blocks}
 ≤ ε^{|A|}
```

whenever the disseminated estimate is `P(∩_T B_T)≤ε^{N_blocks}`. This is the correct multi-block extension of Theorem CB's one-block application. No coarse correlation decay is being assumed.

The source events, however, use **interior plaquettes of the specified hierarchy blocks** and threshold `‖1-U_p‖op≥ε_1`. SRCCD55 uses level-K **M-cubes** containing a plaquette with `|log U_p|op>ε_0`. A rigorous application must match the partition, boundary plaquettes, threshold, and available reflection planes. For principal phases one has

```text
‖1-U‖op = 2 sin(|log U|op/2),
```

so a suitable threshold inequality is explicit, but must be imposed. Shifted partitions or a finite colouring can handle boundary events with adjusted constants/exponents; that construction is not written here. Similarly, `R/ℓ_ref` even does not ensure an even number of arbitrary M-blocks per direction. Restrict to compatible tori or supply the finite-block adaptation. CBE is an elementary conditional bridge; it does not prove `(RLF-3^dis)`, nor does this review independently reprove the entire soft-chain reflection-positivity theorem.

## 5. Proposition C and the averaged CD estimate

**CONFIRMED, the corrected set expansion in graph distance.** File/locators: `SRCCD55.md`, “Proposition C” and E3, with E14's smallness condition.

E3 must be used: paths are self-avoiding, and the coarse images have the stipulated pointwise local LF envelope. With

```text
b = exp(-m_c M),
Q = 80(exp(2C_LF) ε_LF + b) < 1,
```

the prefactor and path together give at most `exp(2C_LF)` at a bad cube in their overlap, `b` at a good path cube, and a factor bounded by `1+exp(C_LF)ε_LF` at each off-path prefactor cube after the Peierls expansion. Summing self-avoiding paths with `ℓ` visited cubes gives at most a fixed support factor times `Σ_{ℓ≥d_*} Q^ℓ`. Here `d_*` is the minimum number of visited cubes in the actual star-neighbor graph. This first-moment argument is valid and avoids the withdrawn double-path-square calculation.

The replacement of the original hypothesis by the pointwise image envelope is a real strengthening. E3 no longer proves the original statement assuming **only** SRC-E′(i)'s `L²` images. Its valid version assumes κ-3-LF as well.

**REFUTED, the stated distance conversion and consequent advertised rate.** File/locators: `SRCCD55.md`, Proposition C “The length is ≥ D_M”, E3 “m′ = −log(80q″)/M”; §3.1 “dist is the Euclidean distance”.

In four dimensions one star-neighbor step can move a cube center by `2Mℓ_ref`. Cubes with center displacement `(j,j,j,j)Mℓ_ref` are Euclidean distance `2jMℓ_ref` apart, but a diagonal path visits only `j+1` cubes. For `j>2` this is less than the claimed `D_M=2j-1`. The same problem was explicitly noticed for cube diameters in LINEAR_PACKAGE, but remains in C.

There is also an exact path-sum falsifier of the claimed exponent. Take no bad cubes, `M=ℓ_ref=1`, `b=1/12800`, `C_LF=0`, and choose the permissible Peierls parameter `ε_LF=1/1280000`. Then `Q=101/16000<1`, and the diagonal path contributes at least `b^{j+1}`. No constant independent of `j` bounds this by `Q^{2j-1}`, because

```text
b/Q² = 20000/10201 > 1.
```

This refutes the path-sum estimate used in the proof, not actual Wilson decay. In Euclidean distance the safe exponent from this counting is `-log Q/(2Mℓ_ref)`, up to endpoint constants. Alternatively state the result directly in graph distance.

**CONFIRMED, sufficient averaged form after these repairs; NOT-VERIFIED, the literal common-prefactor conclusion at the original rate.** File/locators: `SRCCD55.md`, “CD-avg”, Proposition C; `ROTDEF.md`, Theorem 7.1 step 5.

C's proof produces `Eν|Cov(F̃,T(x)|U_K)|≤C exp(-μ dist)`. That already suffices for ROTDEF's shell sum. The displayed CD-avg in §3.4 is stronger syntactically: a **single** random `C_G(U_K)` bounds all `x`, with bounded expectation. A separate argument can recover this at a smaller rate: define a supremum over target coarse cubes, majorize it by the sum, and use the polynomial growth in the number of coarse cubes at distance `r`. For any `0<μ'<μ` the resulting expectation is uniformly finite. This works because the pointwise CD-eff envelope depends on the target cube, not on the number of fine sites in it. The omitted supremum argument and this rate loss must not be silently identified with the displayed original rate.

## 6. Proposition D, SRC-E′, and the insertion contact

**CONFIRMED, the product-cumulant identity and the needed replacement of fine moments.** File/locators: `SRCCD55.md`, Proposition D(i), “SRC-E′”; `ROTDEF.md`, Theorem 7.1; `CODEX_REVIEW_ROTDEF.md`, Findings 3–5.

For globally centered `X=Ō(f)`, `Y=Ō(g)` and arbitrary `Z`, conditionally on `U_K`,

```text
Cov(XY,Z|U_K)
 = κ_3(X,Y,Z|U_K)
   + E_K X κ_2(Y,Z|U_K) + E_K Y κ_2(X,Z|U_K).
```

No repeated-support variance occurs. Uniform separated insertion cumulants, with appropriately integrable LF envelopes, are the appropriate fine-scale input. Coarse `L²` bounds for `E_K X`, `E_K(XY)`, and the current, plus the separated conditional second cumulant, are sufficient for the specific uses listed as U4–U6. Lemma V does not obstruct these **coarse** moments.

**NOT-VERIFIED, the claimed derivation of all of SRC-E′ from the stated package.** File/locator: `SRCCD55.md`, Proposition D(ii), “SRC-E′(i) itself”.

The proof bounds `E_K X` but omits the product image. In fact

```text
E_K(XY) = κ_2(X,Y|U_K) + (E_K X)(E_K Y).
```

To put its centered version in `L²(ν)` one must control `κ_2(X,Y|U_K)` in `L²` and the product of the means in `L²`. The local κ-3-LF mean envelope is bounded on a fixed neighborhood, so it can supply all fixed moments of these means. But C/E3 proves a **first** path moment, not the required squared conditional-cumulant estimate. No correct second-moment estimate is supplied in D(ii). The original squared-path assertion in C was withdrawn. Jensen would instead introduce fine fourth moments with repeated supports, which are precisely not controlled by separated κ-1. State/prove the needed finite-order LF estimate or retain this part of SRC-E′ as an additional hypothesis.

Likewise D(i)'s LF three-point bound must actually reduce to an integrable path/tree envelope for the product observable; a product of path sums is not automatically a single path sum. The combinatorial LF rule and its required moment smallness must be checked at the orders used. This is separate from the valid small-field cumulant identity.

**CONFIRMED, an allowed insertion-side contact; NOT-VERIFIED, its coefficient or the original inequality's falsity.** File/locators: `SRCCD55.md`, §2.1 “F3”, “(M-b) Contact”, “SRC-W′”; `CODEX_REVIEW_ROTDEF.md`, “Finding 3”.

The possible contact is

```text
a² R_{7,ν}(x)e(y) ⊃ c δ⁽⁴⁾(x-y) ∂_μ X^{(4)}_{μν}(y).
```

Both sides have dimension nine and transform as a vector. With `v=Jy`, symmetry of `X` removes the contraction `J^ν_μ X_{μν}`, but integration by parts leaves

```text
-c ∫ (∂_μ f)(Jy)^ν X_{μν}.
```

For `X_{μν}=δ_{μν}e`, this is `c O(Jf)`, and it survives in the covariance with the other centered insertion. The two traceless H(4) sectors furnish the other candidate structures. Thus symmetry alone does not establish SRC-W's contact exclusion. A valid input must allow these terms or prove their cancellation. The `O(g_bare²)` size and possible nonzero value of their coefficients are not computed here. An allowed contact does **not** by itself refute the old SRC-W inequality; its status remains NOT-VERIFIED.

**CONFIRMED, the conditional bulk estimate and unchanged algebraic error budget once the missing hypotheses are supplied.** File/locators: `SRCCD55.md`, Proposition D(iv)–(v), “Bulk, coarse part”; `ROTDEF.md`, Theorem 7.1 step 4.

Assuming the `L²` product-image bound and M-c's actual per-cube bound,

```text
|Covν(E_K F̃, E_K B_bulk)|
 ≤ ‖E_K F̃-ω(F̃)‖₂ Σ_Q ‖E_K B_Q-ω(B_Q)‖₂
 ≤ C a² ℒ(a) r⁵.
```

There are `O(r⁴)` cubes and `|v|+|∂v|=O(r)` for `r≥1`. No decay of the coarse law is used. With the repaired conditional decay, the full near-contact estimate, the controlled stress representatives, and the matching remainder bounds, SRC-W′ and SRC-O give the same form of ultraviolet error as ROTDEF, with adjusted constants/decay rate. D as a whole is NOT-VERIFIED from its current literal hypotheses; the last algebraic implication is valid if those full bounds are assumed.

## 7. Proposition E: the asserted OS0 implication is not established

**NOT-VERIFIED.** File/locators: `SRCCD55.md`, “Proposition E”, its hypothesis sentence, proof (a), and §13 “OS0 needs only the e-part”. There are three distinct failures before the literature-matching question.

**First: missing one-point control.** E assumes κ-1, LF, and SRC-I, but uses “Each Φ_B ... obeys SRC-κ” also for singleton blocks. For a singleton,

```text
Φ_{ {i} } = E[e_a(x_i)|U_K] - ω(e_a(x_i)).
```

κ-1 only bounds orders at least two. It says nothing about this conditional mean. Already for `n=2`, total covariance contains the uncontrolled covariance of two means. κ-3 for `e`, or an appropriate substitute, is necessary.

The general probabilistic inference has an exact counterexample: make all fine fields deterministic given a fair coarse sign `Y`, with centered field `a^{-4}Y`. All conditional cumulants of order at least two are zero, so κ-1 holds with any of its bounds. Take the LF set empty, so SRC-I holds. The unconditional two-point function is `a^{-8}`. This is not asserted to be a Wilson configuration model; it proves that the conditioning argument quoted in E does not deduce its conclusion from the listed bounds.

**Second: SRC-I does not supply uniform all-order path moments. REFUTED.** File/locator: `SRCCD55.md`, Proposition E(a), “times an LF factor that is L^m(ν_K)-integrable by SRC-I”.

Take independent bad-cube indicators with probability `ε=1/1024`, bad weight `e^{C_LF}=2`, and good weight `e^{-m_cM}=1/12800`. These satisfy exactly `P(A all bad)=ε^{|A|}` and the corrected condition

```text
80(e^{2C_LF}ε + e^{-m_cM}) = 51/160 < 1.
```

On arbitrarily large tori, choose a self-avoiding path between two fixed nearby endpoint cubes that makes an arbitrarily long excursion; let `ℓ` be its number of distinct cubes. On its all-bad event, the path sum is at least `2^ℓ`. Therefore

```text
E[ P(A,B)^{11} ] ≥ (1/1024)^ℓ (2^ℓ)^{11} = 2^ℓ.
```

Thus the hypotheses do not give a volume-uniform eleventh path moment, let alone all moments with the claimed factorial constants. Finite-volume integrability is not the required uniform integrability. Total cumulance uses products and higher moments of conditional cumulants; the displayed LF smallness condition only suited a particular low-order averaging argument. This counterexample is within the **stated Peierls/path-envelope assumptions**, independently of any conjecture about Wilson fields. It refutes the claimed probabilistic implication, not the existence of improved Wilson bounds.

**Third: E(a) implicitly asks for coarse decay despite saying none is needed.** File/locators: `SRCCD55.md`, “(N3) Output”, Proposition E(a), “Only boundedness of coarse cumulants is used, never their decay”.

As defined, `w_e(δ)=δ^{-4}𝔤_e(δ)` tends to zero at large separation, since the logarithmic envelope tends to a constant there. For `n=2`, E(a) therefore asserts an unconditional decay bound of order `δ^{-8}`. Boundedness of the coarse means/cumulants does not imply that.

Even after adding κ-3, an exact abstract test is a spatially constant fair sign field: conditional higher cumulants vanish, conditional images are bounded local functions of their own coarse spin, there are no LF cubes, yet the unconditional covariance of two centered fields is one at every distance. Locality of a function of the coarse field is compatible with perfect long-range dependence of the coarse law. This is also an illustration that **OS0 can hold without clustering**; it is the particular decaying bound E(a) that is too strong.

A repair should use a short-distance weight such as `w_e(min(δ,ℓ_ref))` in the unconditional estimate, add the e-part of κ-3, and supply genuine uniform estimates on products of conditional cumulants at every required order with quantified order growth. It need not assume coarse clustering. Those extra estimates are not proved in this packet.

**CONFIRMED, only as a downstream functional-analytic implication.** File/locators: `SRCCD55.md`, Proposition E(b)–(c), “F vanishes with all derivatives on the diagonals”. If suitable uniform all-order moment bounds with polynomial short-distance singularities and controlled order growth are actually supplied, flatness on the diagonals and Schwartz decay give distributional bounds; a countable dense family and a diagonal subsequence then give limits. The crude `‖e_a‖∞≤C a^{-4}` does control the contribution where some pair is closer than `4a` after sufficient flatness. This observation does not fix the failures in (a), and the specific exponent `(n!)^{p+2}` and seminorm in (b) have not been established from the stated hypotheses.

**NOT-VERIFIED [m], OS reconstruction matching.** File/locators: `SRCCD55.md`, §2.2 “What OS0 needs, precisely” and Proposition E “Status of the last step”. The recollection that the original OS regularity formulation uses test functions flat on coincident diagonals, and that OS II imposes an additional linear-growth condition, is explicitly [m] in the target and remains [m] for the exact theorem application here. I attempted the primary [OS I paper](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/Axioms-for-Euclidean-Greens-functions/cmp/1103858969.pdf) and [OS II paper](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf); access returned a security/service page, not readable theorem text. Search metadata is not a verification of the test-space definition or E0′. No reconstruction theorem or OS0 conclusion is banked on that recollection.

## 8. Logarithmic versus power rates

**CONFIRMED, the flow arithmetic and the rate of the supplied upper-bound budget.** Files/locators: `SRCCD55.md`, §7 “Consistent: CONFIRMED”; `RLARGE.md`, “Flow hypothesis (F_R)”.

With fixed `u_K`, `(F_R)` bounds `u_0` between two positive affine functions of `log(ℓ_ref/a)` for small enough `a`. Thus `g_bare²` is bounded above and below by constant multiples of `1/log(ℓ_ref/a)`. In the separate-bounds argument the positive error budget

```text
g_bare² + a²ℒ(a) r⁵ + r⁴ exp(-μr)
```

is dominated by its logarithmic term when `r=a^{-1/3}`. This is an upper-bound limitation, not a lower bound on the actual defect or a proof that the defect cannot converge faster.

**CONFIRMED, conditional power improvement from the stated joint input.** File/locator: `SRCCD55.md`, “Sharper input (OPEN): SRC-OW”. In the exact Ward identity the observable and insertion contributions enter with opposite signs. If the correctly normalized anisotropic coefficient differences and all residual terms really obey the stipulated `O(a²ℒ)` bound, and the scalar multiple of the derivative is absorbed using its nonzero near-one coefficient, the standalone `g_bare²` term can be removed. Then

```text
a² r⁵ = a^{1/3}  when r=a^{-1/3},
```

and the exponential term is smaller than this power for sufficiently small `a`. This concerns the **ultraviolet remainder**. The coarse torque still requires its own control, and the torus must be large enough that `r≤R/4`. SRC-OW alone is not an OS1 theorem or a rate for the full defect. The choice `a^{-1/3}` is sufficient, not optimal for this UV expression alone; logarithmically growing `r` can give an `a²` bound with additional logarithms when other constraints permit it.

**CONFIRMED, the first Poisson reformulation; NOT-VERIFIED, the claimed inference to individual matching constants.** File/locators: `SRCCD55.md`, §7 “Exact reformulation” and “Hence ... anisotropic differences ... must cancel”. Translation invariance permits the exact lattice convolution before approximation. Poisson summation applies to the smooth test-function convolution, uniformly under the rotations. The elementary bound `|C_a(z)|≤C a^{-8}` allows the arbitrary-order test-function error to absorb the cutoff loss. Thus the defect probes the separated annulus as claimed. A smooth radial limiting kernel there, with a uniform `O(a²ℒ)` remainder and enough uniform derivatives for the second Poisson step, would imply the stated improved pair-defect bound.

However a small defect for one test pair does not identify each anisotropic matching coefficient. This requires enough independent tests and control of operator identities, current normalizations, and other remainders. Nor is smoothness of the radial kernel supplied merely by writing `C_∞(|z|)`. The target's Symanzik/Reisz claims remain **[m] and NOT-VERIFIED** here. Even agreement to every order of a formal coupling expansion does not prove a nonperturbative `O(a²)` bound: terms beyond all orders in `g_0` need a separate estimate along the chosen flow. SRC-OW is a useful explicit additional hypothesis, not a derived cancellation.

## 9. Check receipt and scope of negative findings

The two supplied scripts were inspected and executed with `python3 -B`, without redirecting output into other files. They reproduced their existing PASS text. In-memory mutations, with no edited scripts or additional artifacts, produced:

| Exact check/control | Observed result |
|---|---|
| Original `sc55_tel`: Markov identity | 50/50 equalities |
| Original `sc55_tel`: non-Markov tail form | 50/50 equalities |
| Original `sc55_tel`: non-Markov Markov-form control; omitted-step control | Both FIRED |
| Multiply every telescoping summand by two | `VERDICT: FAIL` |
| Original `sc55_vm`: V1–V5 and false lower-bound control | PASS; control FIRED |
| Change the lower `c_v` numerator from eight to seven | `VERDICT: FAIL` |
| Change the upper `c_v` numerator from eight to nine | `VERDICT: FAIL` |
| Independent rational coefficient comparison | Strictly greater than `3/2000000` |
| Outward interval audit | `[1509091,1509092]/10^12` |
| Independent two-step Markov chain | `35/36 = 3/4 + 2/9` at both endpoints |
| Independent path-moment counterexample | `Q=51/160<1`, but `E[P^11]≥2^ℓ` |

The supplied scripts report failures in text rather than returning a failing process status; their printed verdict was inspected. Random rational finite chains provide useful controls, not an exhaustive proof. The general identity and the variance mechanism were checked analytically above. No floating-point calculation was used for a verdict. No full repository pipeline, claim-status validator, or audit worker was run: this is a standalone mathematical review with no source changes.

Negative-claim discipline: the conclusions concern explicit inferences and the clover-energy normalization, not an impossibility theorem for Yang–Mills. Centering, rescaling, source contact subtraction, positive-time flow, and a faster-decaying bare coupling have different effects and were not conflated. The last two lie outside the divergence/non-vacuity argument being confirmed; counterterm-renormalized Schwinger distributions are a remaining route, not a prohibited one. The strongest repair of the source is concrete: add the missing full-law/LF product estimates and one-point bounds, correct graph/tree geometry, and keep non-vacuity separate. No independence count of open obligations, exhaustive five-route no-go certificate, new-axiom necessity, or retained-grade status is claimed. The inherited negative findings were checked against their actual residuals, including E11's withdrawal of the unsupported product-variance argument.

## Exactly what may be banked

1. **CONFIRMED:** the full normalized soft chain is Markov in the level index; B1, B2, the effective-action ratio, first-order linear source evolution, and triangular higher-order recursion are exact. The same statement does not prove any decay estimate.
2. **CONFIRMED:** separated-support local-counterterm cancellation and the mixed Cauchy estimate. Under the separately assumed conditional polymer representation, a corrected two-set geometry and scale bound give smeared conditional decay. Neither H-Bal-loc's unconditional statement nor the sup-norm polydisc supplies the full pointwise SRC-κ package.
3. **CONFIRMED:** Lemma V's volume-uniform lower bound for the real smeared clover energy, with E2 and coefficient at least `3/2000000`. The exact scoped incompatibility is SRC-E plus non-vacuity plus an unconditional separated upper bound along a sufficiently slowly vanishing coupling trajectory, in particular `(F_R)`. No exact variance asymptotic or blanket theorem for all dimension-four composites is established.
4. **CONFIRMED:** the component/parameter arithmetic `47` and `8`; the chessboard-to-Peierls implication for matching reflected block events; and the corrected self-avoiding-path first-moment argument in graph distance. The asserted precision of the whole SRC specification and the original Euclidean decay rate are not banked.
5. **CONFIRMED:** the product-cumulant identity, the relevance of coarse moments instead of divergent fine variances, the symmetry-allowed insertion contact, and the `a²ℒ r⁵` coarse bulk estimate under its explicit moment/matching hypotheses. **NOT-VERIFIED:** the complete derivation of SRC-E′, SRC-O, and SRC-W′ from the present literal package or any nonzero/contact-coefficient computation.
6. **CONFIRMED:** the separate error budget permits only a logarithmic bound under `(F_R)`, while an independently established joint SRC-OW bound permits a power bound for the UV remainder. **NOT-VERIFIED:** SRC-OW itself, the full OS1 defect rate, and the Symanzik/Reisz deductions [m].
7. **NOT-VERIFIED:** Proposition E and the claimed OS0 conclusion. Its singleton, all-order LF moment, and large-distance weight gaps are substantive; the exact OS reconstruction matching remains [m]. No conditional-decay theorem for Wilson YM, physical mass gap, nontrivial continuum field, or constructive 4D Yang–Mills completion is banked by this review.
