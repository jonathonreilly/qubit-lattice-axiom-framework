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
