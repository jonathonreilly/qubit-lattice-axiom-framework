---
title: Positive-time external compilation with fixed amplitude and slew caps
claim_id: bounded_slew_positive_time_compiler_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: fixed supplied finite plant and augmented polynomial certificate admit qualitative external compilation under positive amplitude and first-derivative caps
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: supplied computable plant, certificate, positive path, external waveform, timing and isolation; no polynomial resources or autonomous realization
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["accuracy_scaled_compiler_bounded_theorem_note_2026-10-15", "conditioned_positive_time_compiler_bounded_theorem_note_2026-10-15"]
runner: scripts/bounded_slew_positive_time_compiler_2026_10_15.py
next_trace_action: separately bind final canonical review, run source-integrity integration and regular publication, then independent retained audit
---

Claim type: bounded_theorem

For the supplied finite computable plant and augmented polynomial Lie certificate, any fixed positive amplitude and first-derivative caps permit a terminating qualitative positive-time external compiler. The emitted control is positive, uses one allowed Pauli ray at a time, and is C1 with zero value and derivative at every pulse boundary. Its actual duration is selected by the search. No polynomial bound on runtime, pulse count, search, precision or accumulated action is established.

The primary publication theorem is the protected weak-bump SU(d) proof with the parent's scalar ledger. The root full-U(d) ramp proof is a separate variant with a different coherent phase target. A positive minimum-runtime prefix is a later exposed corollary; it is not retroactively part of the original protected proof. The exact three bodies follow once each, without edits.

Qualified source acceptance is `270985de36fb34e6b4a91260d7a546eea7d2b859906f1464217b4e856bbb6868`, recorded at 23:58:00.924598 UTC on 2026-10-15. It accepts these conditional contracts, not this new wrapper, canonical integration, publication or retained status. Historical pending language remains in the bodies. The historical source-integrity proposal remains unexecuted. The canonical derivative requires captured frozen-draft and final-canonical review evidence before execution. It checks source bytes, recovery, receipt linkage and later real binding evidence; it cannot certify general reachability, theorem validity or physics.

## 1. Complete supplied interface

Fix d>=2 and the literal complete computable Hamiltonian H, including H0, apparatus, memories, clocks, dirty fillers and all other retained factors. Allow every joint plant input and arbitrary correlated passive reference. Supply the parent's positive ordinary-nearest-neighbor path J, accessible X/Y port, g>0, time unit t0>0, complete geometry and target data. No old factor moves, is initialized or discarded. Write H=h0 I+Hbar and J=j0 I+Jbar, and supply h>=||H||. The intended nominal generator is

```
H_ph(t)=H+R_s I+lambda J+C(t),   R_s>=h,
C(t)=a(t)(I+sigma P_p)>=0,
P_p in {X_p,Y_p}, sigma in {+1,-1}, 0<=a(t)<=g.
```

At most one ray is active. Supply fixed positive computable operator-norm caps C_max and S_max, so ||C(t)||<=C_max and ||dC(t)/dt||<=S_max. Scalar coefficient caps differ by a factor two. There is no minimum nonzero amplitude or pulse width, hard frequency cutoff or common higher-derivative bound in this premise. External waveform generation, timing, coefficient access and isolation are supplied. Design/search precedes the declared physical timeline; aging during design, if present, needs a separate chronological contract.

For the primary theorem supply computable W and a determinant lift theta, with Wtilde=exp(-i theta)W in SU(d). Supply the same d^2-1 binary bracket trees in

```
X_i(z)=diag(-i t0[Hbar+z Jbar+v_i], -i t0 Hbar),
v_i in {0,+gX_p,-gX_p,+gY_p,-gY_p}.
```

Each tree has at least two leaves, evaluates to diag(b_l(z),0), and uses consistent computable real coordinates. The determinant p(z) has degree at most D and a supplied coefficient witness |a_k0|>=a>0. H,J,g,t0,d, trees, coordinates, witness and finite output window w remain fixed as accuracy varies. The direct sum records actual aging mathematically; it is not another physical plant. Certificate discovery and arbitrary oracle complexity remain outside the result.

The exact direct parents are the [accuracy-scaled compiler](ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md), SHA256 `c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2`, and the [protected positive-time compiler](CONDITIONED_POSITIVE_TIME_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md), SHA256 `db922c9b3f67a603961f5a621a67eea7fa4894b793befbcdd3b7b034011e540a`. PARENT_BINDING gives their canonical bodies and exact intervals. Only their complete-plant interface, certificate and scalar/actual-time contracts are used here. Their polynomial recipes and any autonomous construction are not conclusions of this new schedule.

## 2. Protected weak-bump theorem

For rational 0<epsilon<=1, choose fixed rational bounds b_bar>=||Jbar||, w_bar>=w and L_win>=max(1,64 b_bar(1+w_bar)). Set Lambda=epsilon/L_win. On the D+1 rational nodes x_j=1/2+j/[2(D+1)], coefficient extraction by the rational Vandermonde inverse gives

```
max_j |p(Lambda x_j)| >= a Lambda^k0/A_V = b>0,
A_V=sum_j |(V^-1)_(k0,j)|.
```

Evaluate each node to certified absolute error b/8; accept the first satisfying |p_hat_j|-b/8>b/2. A witness has lower estimate at least 3b/4. The selected rational lambda lies in [Lambda/2,Lambda), has the required augmented span, and obeys lambda||Jbar||w<=epsilon/64. This does not assert that every small coupling works or that higher-degree coefficients can be omitted.

Choose fixed positive rationals kappa,delta_0 with 16kappa<=S_max, 2kappa delta_0<=C_max and kappa delta_0<=g. The physical library consists of positive rational waits and the four rays with pulses

```
psi(x)=16x^2(1-x)^2,
a_delta(t)=kappa delta psi(t/delta),   0<=t<=delta,
0<delta<=delta_0 rational.
```

These pulses and their first derivatives vanish at both ends. Their peak and derivative bounds are 2kappa delta_0 and 16kappa in operator norm; finite concatenations retain the same caps. Their scalar area is (8kappa/15)delta^2. Smaller pulses become both weaker and shorter; their second derivatives need not share a bound.

For the traceless augmented drift A=diag(-i[Hbar+lambda Jbar],-iHbar), let G be the closure of all finite nonempty library words. It is a compact semigroup, and the full augmented unitary recurrence makes it a group. Positive waits and inverses in the closure give exp(tA) for real t. These inverse endpoints are limiting positive-time words, not signed physical waits.

For B=diag(-iP_p,0), the interaction-picture endpoint E_delta=exp(-delta A)F_delta(delta) lies in G. With beta=8kappa/15, the complete proof gives

```
||E_delta-exp(beta delta^2 B)|| <= beta||A||delta^3,
||E_delta^floor(u/(beta delta^2))-exp(uB)||
    <= u||A||delta+beta delta^2 -> 0.
```

Thus both port one-parameter groups lie in G. Finite-dimensional Trotter and commutator limits, followed through the supplied trees, put diag(Wtilde,I) in G. The original proof supplies the full compact recurrence, local estimate and span argument; these are the load-bearing mathematical steps, not consequences of a metadata check.

Fairly enumerate every finite nonempty rational library word and certify its augmented endpoint. Smooth-pulse evaluation uses controlled piecewise-constant error and finite matrix-exponential approximations; interval products must include truncation and roundoff amplification even when approximants are not exactly unitary. With eta=epsilon/8, accept a certified Frobenius upper error below eta whose excess over the actual error is at most eta/4. Density supplies a word below eta/2, so a strict witness is eventually reached. Each preceding fixed-precision evaluation terminates. The returned duration T>0 is the exact sum of its rational segment lengths, including all waits.

Both augmented block errors are below eta. Hence the returned traceless plant endpoint differs from Wtilde exp(-iTHbar) by less than 2eta=epsilon/4. No assumption lambda T small, selected logarithm branch, exact-zero test or prescribed completion deadline is used.

## 3. Actual complete output, calibration and positivity

The port is zero throughout [T,T+w]. Retain the literal scalar area and comparison phase

```
A_s=(8kappa/15)sum_pulses delta_j^2,
chi(T+s)=(R_s+lambda j0)(T+s)+A_s+theta,
V_SU(s)=exp[-i chi(T+s)] exp(-isH) W exp(-iTH),  0<=s<=w.
```

The full nominal coherent error is at most epsilon/4+epsilon/64=17epsilon/64. H ages the complete input before W and acts afterward during the window in the displayed order. Every wait accrues its full reserve and path phase and action. The physical scalar rate is h0+R_s+lambda j0+a(t); theta is a comparison-phase lift, not applied energy.

For the actual full-space generator defect E(t), impose one shared allowance

```
E_int=integral_0^(T+w)||E(t)||dt <= epsilon/64.
```

For every plant/reference input, the complete unhalved trace error is then at most 2[epsilon/4+epsilon/64+epsilon/64]=9epsilon/16<=epsilon. Timing, coefficient, scalar, old-background and omitted-edge errors share this single allowance. Input error adds once and needs its own allocation; unused numerical margin does not supply an unmentioned physical interface. A sufficient constant defect-rate tolerance is epsilon/[64(T+w)]. Delivered waveform cap compliance is a separate condition, not implied by an integrated defect bound.

Whole nominal positivity follows from H+R_s I>=0 and J,C>=0. Robust actual positivity requires a supplied peak bound zeta_pk and R_s>=h+zeta_pk. Separate positivity of every old local summand is not obtained. Extra literal local reserves, when required, change phase and action. For fixed reserve the nominal full norm is bounded by h+R_s+||J||+C_max and its explicit time derivative by S_max. These common instantaneous bounds do not bound total T, accumulated action or an autonomous replacement's clock/mediator resources. Norm action is not identified with thermodynamic work or a physical energy observable.

## 4. Separate root full-U(d) ramp variant

The root variant uses the full pair A_full=(-i[H+R_sI+lambda J],-iH), B_r=(-i[I+sigma P_p],0), and cubic ramp/hold/down controls with delta=3a/(2S0). Its closure argument extracts B_r through (Ad_Da(A_full+aB_r)-A_full)/a -> B_r. The central sum B_(+X)+B_(-X)=(-2iI,0), together with the supplied commutator trees, gives the first full u(d) direction. It searches near (W,I) including the actual runtime scalar phases. Choosing a0<min(g,C_max/2) and S0<=S_max/2 meets the specified operator caps, as the exposed comparison explains.

Its coherent comparator is distinctly

```
V_full(s)=exp[-i(R_s+lambda j0)s] exp(-isH) W exp(-iTH).
```

It is not obtained by assigning the SU(d) word this formula. For formally equal T,A_s,W, the two comparators differ by exp[-i((R_s+lambda j0)T+A_s+theta)]. They define the same density-operator channel, but their coherent targets can differ substantially. The full-phase search pays for runtime scalar recurrence; it does not erase literal scalar Hamiltonians or their action. This variant needs no determinant-lift oracle for its own search.

The root body's displayed epsilon window estimate is nominal. Its exposed robustness qualification selects eta=epsilon/8, lambda||Jbar||w<=epsilon/64 and the shared E_int<=epsilon/64 to obtain the same conservative 9epsilon/16 trace bound. Peak positivity and delivered-cap compliance remain separate. Its added incident-strength estimate R_s+4+2g uses the supplied path and an onsite representation of the scalar reserve, and establishes no autonomous hardware bound.

## 5. Later exposed minimum-runtime corollary

For supplied computable finite T_min, or a supplied computable upper bound, choose a positive rational tau>=T_min. Prefix a zero-control wait of duration tau. For the protected traceless pair set Z=diag(Wtilde,I), F_pre=exp(tau A), and search a suffix near Z F_pre^-1; test the complete chronological product F_suffix F_pre against Z. The group property and computability give terminating strict search. The total T=tau+T_suffix satisfies the lower bound, and the original caps and endpoint conditions persist.

The prefix adds no port area but adds its full H, reserve and path aging/phase. The same chi formula uses the increased total T; calibration and action use T+w. The analogous full-pair residual target gives the root variant. This is a separately attributed source-exposed corollary, not the original protected result, an upper runtime estimate or an arbitrary exact completion-time theorem.

## 6. Evidence, exposure and publication boundary

The protected proof was frozen before its author read the new root argument. The later comparison was exposed to both, and explicitly supplies the SU(d) minimum-runtime corollary and root robustness qualification. The selected model, prior parent machinery and question framing are shared. This is separate-context checking, not independent model-family replication. Root's acceptance reports complete argument and check-source review. This packaging adds no protected derivation or scientific execution.

The historical symbolic program checks only pulse polynomial identities, the degree-two noncommuting jet, arithmetic budgets, source pins and labelled deliberate-defect detections. Both original and final actual receipts are preserved; the repeat records final prose clarifying numerical-enclosure error. The historical ramp program records 32 floating-point local-ramp cases on one fixed two-qubit example. It checks neither an augmented Lie certificate nor a full compiler. Their exact source captures, streams and receipt linkage remain recoverable; successful exits are not proofs of general reachability or physical implementation.

The theorem is positive conditional mathematics. It constructs no external actuator or autonomous controller, native preparation or purity supply, cooling or reusable memory, permanent stopping or physical energy identification. Fixed slew is not hard bandwidth. The absence of a polynomial upper recipe here is not an impossibility claim for other mechanisms. No ferromagnetic or energy candidate is a dependency or was inspected.

The frozen-draft review is captured separately from the required final canonical review and actual integration outcomes. Raw draft and canonical body offsets may differ; final canonical review must explicitly link the exact body identities and final intervals. No canonical review, primary/cache execution, Git base, publication or retained audit is fabricated in this source draft. Its historical PUBLICATION_STATE remains null. Exact source/AST checks establish only the stated provenance and assembly facts.


---

## Immutable source body: protected_weak_bump_body

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# Qualitative positive-time external compilation with fixed amplitude and slew caps

Status: independent conditional derivation, prepared without exposure to any new root or other worker derivation for this question. This is a proof proposal for the supervisor's scientific review, not a retained/audit verdict. The conclusion is affirmative under the exact supplied computable augmented polynomial certificate and external-control premises below. No polynomial bound on runtime, pulse count, search, precision or higher derivatives is claimed.

## 1. Exact scope and admitted inputs

Use the fixed complete finite plant of dimension d >= 2 from the two parent notes. H is its literal complete unchanged computable Hamiltonian, including H0, apparatus, memories, clock factors, dirty fillers and all other terms retained for this invocation. An arbitrary correlated passive reference is retained. Write H = h0 I + Hbar and J = j0 I + Jbar, where the supplied positive ordinary-nearest-neighbor path Hamiltonian is J. The same geometry, isolation, target-data, external waveform and calibration contracts remain supplied. No additional physical factor, initialized subsystem or actuator is constructed here.

Supply the parent's computable full target W and determinant lift theta with Wtilde = exp(-i theta) W in SU(d). Supply its fixed computable polynomial bracket certificate: the same d^2-1 binary bracket trees in

    X_i(z) = diag(-i t0 [Hbar + z Jbar + v_i], -i t0 Hbar),
    v_i in {0, +g X_p, -g X_p, +g Y_p, -g Y_p},

have values diag(b_l(z), 0). Their coordinate determinant p(z), in the parent's consistent computable real basis, has degree at most D and has a supplied coefficient witness |a_k0| >= a > 0. The supplied data H, J, g, t0 (with g,t0 > 0), the trees, coordinate data, coefficient witness, plant dimension and finite requested output window w remain fixed as accuracy varies. The accuracy-dependent selected lambda is allowed, as in the accuracy-scaled parent.

Prescribe any fixed positive port operator-norm cap C_max and fixed positive port operator-norm first-derivative cap S_max. Positive rational caps suffice. More generally computable positive caps allow effective selection of strictly positive rational lower margins. These caps are upper bounds, with no minimum pulse amplitude or width. The supplied ray strengths still obey 0 <= a(t) <= g. The construction below meets

    C(t) = a(t) (I + sigma P_p) >= 0,
    P_p in {X_p, Y_p}, sigma in {+1,-1},
    ||C(t)|| <= C_max,     ||dC(t)/dt|| <= S_max,

with at most one active ray and with C = dC/dt = 0 at every pulse boundary. If the requested caps instead refer to the scalar coefficient, divide the displayed operator-norm bounds by two. The nominal full Hamiltonian is

    H_ph(t) = H + R_s I + lambda J + C(t),   R_s >= h >= ||H||.

No part of H is slowed, deleted, reversed or scaled. R_s is retained. All times below are actual physical times expressed in fixed units; t0 remains the fixed normalization in the supplied certificate. Rational physical intervals are a subset of the parent's supplied computable timing contract.

## 2. Select a small valid coupling without a conditioning claim

For a rational 0 < epsilon <= 1, use the parent's fixed rational bounds b_bar >= ||Jbar|| and w_bar >= w, and choose once

    L_win >= max(1, 64 b_bar (1+w_bar)),   Lambda = epsilon/L_win.

Take exactly the D+1 rational nodes x_j = 1/2 + j/[2(D+1)]. Let V_jk = x_j^k and A_V = sum_j |(V^-1)_(k0,j)|. Rational Vandermonde inversion is effective and A_V > 0. Coefficient extraction for q(x) = p(Lambda x) gives

    a_k0 Lambda^k0 = sum_j (V^-1)_(k0,j) p(Lambda x_j),
    max_j |p(Lambda x_j)| >= a Lambda^k0/A_V =: b > 0.

Evaluate each p(Lambda x_j) with certified absolute error at most b/8 and accept the first node satisfying

    |p_hat_j| - b/8 > b/2.

A witness has the left side at least 3b/4, so the fixed finite strict test terminates. For the selected rational lambda = Lambda x_j,

    0 < Lambda/2 <= lambda < Lambda <= 1,
    det C(lambda) != 0,
    lambda ||Jbar|| w <= epsilon/64.

Thus the given trees at the actual lambda span (su(d),0). This proof needs only that span, not a uniform conditioning lower bound or any polynomial resource estimate. It does not assert controllability at every small coupling. Higher coefficients remain in the D+1-node interpolation, and k0 need not be the first nonzero coefficient.

## 3. A countable library of admissible smooth pulses

Choose fixed positive rationals kappa and delta_0, independent of epsilon, with

    16 kappa <= S_max,
    2 kappa delta_0 <= C_max,
    kappa delta_0 <= g.

Strict choices can be obtained effectively from the positive computable caps and g. Define

    psi(x) = 16 x^2 (1-x)^2,   0 <= x <= 1,
    c0 = integral_0^1 psi(x) dx = 8/15,
    c1 = integral_0^1 x psi(x) dx = 4/15.

For every positive rational delta <= delta_0 and each of the four supplied rays, include the pulse

    a_delta(t) = kappa delta psi(t/delta),    0 <= t <= delta,
    C_delta(t) = a_delta(t) (I + sigma P_p).

Also include every positive rational zero-control wait. These form a countable, effectively enumerable library. All coefficients of a_delta are rational in the fixed physical time coordinate.

Here 0 <= psi <= 1, psi(0)=psi(1)=psi'(0)=psi'(1)=0, and

    psi'(x) = 32 x(1-x)(1-2x),   |psi'(x)| <= 8.

Consequently ||C_delta|| <= 2 kappa delta_0 <= C_max and ||dot C_delta|| <= 16 kappa <= S_max. Every pulse is positive, and its value and first derivative join the zero-control state continuously at both ends. Any finite concatenation is C1 and obeys the same caps. Directly adjacent different rays cause no discontinuity because both are zero, with derivative zero, at the join.

These pulses become weaker as they become shorter. Their integrated scalar area is exactly kappa c0 delta^2. Their second derivative need not have a uniform bound as delta decreases. A fixed first-derivative cap is used here; no hard bandwidth, minimum width or minimum nonzero amplitude is assumed or established.

## 4. The augmented reachable closure is a group

For this selected lambda define the per-unit-physical-time skew matrices

    A = diag(-i[Hbar + lambda Jbar], -i Hbar),
    B_X = diag(-i X_p, 0),   B_Y = diag(-i Y_p, 0).

Their direct sum is mathematical bookkeeping. For any admissible physical schedule of duration T, its augmented traceless propagator is exactly

    F(T) = diag(U_tr(T), exp(-i T Hbar)).                 (1)

The scalar ledger is not inside this pair and will be restored in section 7. Let S be the set of these pairs for all finite **nonempty** words from the rational library, with their actual durations. Let G be its closure in the full 2d-dimensional unitary group. Ordinary multiplication is allowed: the product of two endpoints is realized by the corresponding reverse chronological concatenation. Therefore S is a semigroup. Its closure is a compact semigroup, and I belongs to it by arbitrarily short positive waits.

For completeness, G is a group. For any Q in G, diagonalize Q unitarily and consider its 2d eigenangles. For each positive integer N, place the N^(2d)+1 points of successive multiples of twice those angles, modulo 2pi, into N^(2d) boxes. A pair in one box supplies 1 <= n <= N^(2d) with ||Q^(2n)-I|| <= 2pi/N. Taking N to infinity gives Q^(2n) -> I. This finite-dimensional spectral recurrence includes **both** augmented blocks. Then Q^(2n-1) belongs to G and converges to Q^-1. Hence every Q in G has its inverse in G. This only puts inverse endpoints in the closure of positive-time schedules. It does not authorize a negative physical time or remove the elapsed time of a recurrence.

All exp(t A), for real t, belong to G: positive rational waits and continuity give t >= 0, and inversion gives t < 0. Full-group closure, not a first-block-only recurrence, is essential to the old-aging statement.

## 5. Fixed-slew pulses generate the port directions

Consider a positive X or Y pulse; write B for its B_X or B_Y, with ||B||=1. Let F_delta(t) solve

    dot F_delta(t) = [A + a_delta(t) B] F_delta(t),
    F_delta(0) = I,       0 <= t <= delta.

Its endpoint F_delta(delta) belongs to S. Form the **mathematical** interaction-picture endpoint

    E_delta = exp(-delta A) F_delta(delta) in G.

The inverse drift is in G by section 4; it is not being installed as a signed wait. The interaction-picture evolution has generator

    a_delta(t) exp(-t A) B exp(t A).

Because A and B are skew-Hermitian, unitary conjugation and integration give

    ||exp(-tA) B exp(tA) - B|| <= t ||[B,A]|| <= 2t ||A||.

Duhamel between this evolution and the one with generator a_delta(t) B yields the exact upper estimate

    ||E_delta - exp(beta delta^2 B)||
      <= 2 ||A|| integral_0^delta t a_delta(t) dt
      = beta ||A|| delta^3,           beta = 8 kappa/15 > 0.       (2)

No cancellation of the physical drift or smallness of lambda times total runtime has been assumed. Equation (2) is a local small-pulse estimate used only to prove the reachable closure.

Fix any u >= 0, take positive rational delta -> 0, and set m_delta = floor(u/(beta delta^2)). Unitary telescoping and (2) give

    ||E_delta^(m_delta) - exp(u B)||
      <= m_delta beta ||A|| delta^3 + beta delta^2
      <= u ||A|| delta + beta delta^2 -> 0.                     (3)

For u=0, the conclusion is I in G. For u>0, m_delta is positive eventually. Every left-hand approximant belongs to G, so exp(u B) belongs to G. Inverses give all real u. Both port directions B_X and B_Y are therefore available in the closure despite the fixed amplitude and slew caps. The supplied negative rays are also in the physical library; no additional ray has been introduced.

The finite-dimensional unitary Lie-Trotter formula now puts

    exp[t t0(A + sigma g B_P)] in G

for all real t and either axis/sign, and exp(t t0 A) is already in G. These are precisely the exponentials of the five supplied X_i(lambda). The physical pulse peak need never reach g. The value g in this line names a direction in the mathematical closure, obtained by repetition and limits, not a larger instantaneous applied coefficient.

One can avoid invoking a general Lie subgroup theorem. For finite skew matrices C,D whose full real one-parameter groups lie in G, multiplication of their Taylor expansions gives

    exp(v C) exp(v D) exp(-v C) exp(-v D)
        = I + v^2 [C,D] + O(v^3).

Repeating with v=sqrt(u/n) and letting n grow puts exp(u[C,D]) in G for u>=0; inverse endpoints give u<0. Induction down each finite supplied bracket tree therefore puts exp(t diag(b_l(lambda),0)) in G for every real t. Lie-Trotter then puts exp(diag(Z,0)) in G for every real linear combination Z of the basis b_l(lambda), hence every Z in su(d).

Every Wtilde in SU(d) has some traceless skew logarithm: diagonalize unitarily, choose real eigenangles, and change one angle by the integral multiple of 2pi needed to make their sum zero. This is an existence argument; no computable eigenangle branch is selected. It follows that

    diag(Wtilde, I) in G.                                    (4)

Equations (2)-(4), together with compact positive-time closure, are the load-bearing fixed-slew argument. They do not reuse the parent's accuracy-dependent sharp-ramp recipe.

## 6. A terminating compiler, rather than only dense existence

Enumerate all finite nonempty words in the rational library fairly. For example, at stage n enumerate all words of length at most n whose rational pulse durations, and rational wait durations, have positive numerators and denominators at most n, retaining the admissible delta <= delta_0 pulses. Duplicate words may be skipped or reevaluated. Every finite rational library word eventually occurs. Each word has finite positive actual duration T, computable exactly from its rational segment durations.

Every candidate augmented endpoint is computable with certified absolute matrix error. One explicit evaluation route is:

* On a pulse, replace its scalar polynomial amplitude by midpoint constants on m equal intervals. Its scalar Lipschitz constant is at most 8 kappa, so full augmented traceless Duhamel error is at most 2 kappa delta^2/m. This is an evaluation approximation, not a change to the physical pulse.
* Evaluate each constant skew-matrix exponential using the finite Taylor series and a certified norm-based tail bound; all matrix entries and required norm majorants are computable from the supplied data.
* Telescope the smooth-versus-piecewise-constant unitary errors. Enclose the finite products of numerical exponential approximants by interval matrix multiplication, including truncation and roundoff amplification; the approximants need not themselves be exactly unitary. Allocate enough precision to enclose the candidate matrix and its Frobenius distance from the computable target. For a long candidate this may require arbitrarily extensive finite computation.

Thus for any candidate one can compute an upper bound on its full augmented Frobenius error exceeding the true error by at most any specified positive rational. This uses no numerical exact-zero test, eigenvalue branch selection or undocumented spectral oracle.

Set eta = epsilon/8. Evaluate each candidate once to obtain an upper Frobenius error bound whose excess is at most eta/4, and accept if this bound is strictly below eta. Otherwise proceed to the next candidate. This test terminates: by (4), S has a candidate at Frobenius distance strictly below eta/2, and that candidate passes with margin. Every preceding fixed-precision computation terminates. The emitted finite schedule uses only the allowed rays and satisfies both caps identically.

For the returned word,

    ||diag(U_tr(T), exp(-i T Hbar)) - diag(Wtilde,I)||_op < eta.

Both block errors are below eta, whence

    ||U_tr(T) - Wtilde exp(-i T Hbar)|| < 2 eta = epsilon/4.     (5)

All recurrence waits implicitly selected by the successful word are part of this actual T. There is no prescribed completion deadline. The proof of termination supplies no useful upper bound on search, T, word length, precision or physical action. It does not transfer the parent's polynomial recipe to this different compiler.

## 7. Full scalar, output window and arbitrary retained input

The returned scalar port area is exactly

    A_s = integral_0^T a(t) dt = kappa c0 sum_pulses delta_j^2.

The actual nominal scalar rate is h0 + R_s + lambda j0 + a(t). Every wait accrues its full h0, reserve and path scalar phase. The control is zero throughout [T,T+w], with no additional settling interval. Define

    chi(T+s) = (R_s + lambda j0)(T+s) + A_s + theta,
    V_s = exp[-i chi(T+s)] exp(-isH) W exp(-iTH),  0<=s<=w.

Restoring the scalar from (5), then applying Duhamel only over the post-endpoint window, gives

    sup_(0<=s<=w) ||U_ph(T+s) - V_s||
      <= epsilon/4 + lambda ||Jbar|| w
      <= 17 epsilon/64.                                      (6)

The comparator uses the complete original H, in the displayed chronological order, at the actual returned T. In general exp(-isH) W is not W exp(-isH). The static path has acted for the entire compilation interval; no lambda T smallness assumption appears anywhere.

For the parent's full retained-space defect E(t) = H_actual(t)-H_ph(t), use one total integrated allowance

    E_int = integral_0^(T+w) ||E(t)|| dt <= epsilon/64.

Then the complete unhalved trace-distance error, for every joint plant/reference input rho, uniformly over the window, is at most

    2 [epsilon/4 + epsilon/64 + epsilon/64] = 9 epsilon/16 <= epsilon.    (7)

The reference does not alter the operator norm and the standard two-term expansion of U rho U* - V rho V* proves this bound without a dimension factor or any discarded output. Input-state error, if present, adds once and must be separately budgeted. All simultaneous timing, calibration, coefficient, scalar, old-background and omitted-edge errors share the one E_int budget; no source may independently spend it all.

Nominal whole-generator positivity follows from H+R_s I >= 0 and J,C >= 0. Robust actual positivity still needs a supplied peak-defect bound zeta_pk and R_s >= h+zeta_pk. This argument does not prove separate positivity of every old local term. Additional literal local reserves, if a consumer requires them, remain explicit and change phase and action.

The nominal full norm has the accuracy-independent bound

    ||H_ph(t)|| <= h + R_s + ||J|| + C_max,

while its explicit time derivative is bounded by S_max. These common instantaneous bounds do not bound accumulated action: it includes the complete actual T+w, all reserves and path action. A sufficient constant defect-rate allowance is epsilon/[64(T+w)], so no fixed positive error floor is silently tolerated when T grows. The theorem constructs neither the external waveform source nor a physical clock. It is not an autonomous bounded-strength construction or an assertion of bounded energy moments for a later autonomous substitute.

## 8. Checks, failure distinctions and remaining scope

The independent mechanism differs from shrinking the parent's ramp widths after a fixed bang-bang compilation. That latter smoothing estimate prices lost area per switch and does not itself meet a common slew cap as accuracy increases. Here admissible small-amplitude bumps define the reachable semigroup from the start; compact recurrence and a computable search select an actual finite schedule.

The following distinctions are essential to the positive theorem:

* The certificate concerns the complete augmented pair and a valid selected lambda; projected rank or arbitrary weak lambda is not substituted.
* Approximate inverse group elements are limits of positive-time schedules. The compiler emits a finite positive-time word and recomputes both augmented coordinates and T.
* The smooth pulses may have arbitrarily small amplitude and duration. A fixed slew cap supplies no hard frequency cutoff. No claim is made under extra minimum-amplitude, minimum-width or hard-bandwidth restrictions.
* A finite window uses an accuracy-dependent selected path coupling. A permanently idle interval of unbounded duration is not covered.
* The external design/search occurs before the declared physical timeline, as in the parents. Plant aging during design, if present, needs its own chronological contract.
* All old/filler/reference inputs are arbitrary. A reset or preparation consumer still needs its premise on the actually aged input; no purity, cooling, memory supply, reuse or native physical identification follows from this compiler.

The accompanying exact symbolic check covers the bump endpoint identities, its two integrals, the degree-two commutator sign, and the error-budget arithmetic. It is not a full compiler run, a numerical controllability example, a formal proof checker, or an audit. Source hashes and captures establish provenance only. The remaining review obligation is independent examination of this full argument, especially the compact semigroup closure, its port-direction extraction and its effective enumeration. The worker used the inherited selected model and reasoning effort in a separate context and did not inspect another current derivation. No external theorem lookup, model/effort change or child-agent spawn occurred. No Git/PR mutation, canonical-source edit, cache/graph/audit/axiom/prompt edit or other-chat communication was used.


---

## Immutable source body: root_full_unitary_variant

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# Fixed-slew positive controls: a conditional external compiler ingredient

Status at creation, 2026-10-15: root proposal, not independently checked, not
installed in the repository. This derivation was written before seeing either
new worker's scientific results. It does not construct an autonomous controller.

## 1. Exact inherited interface and proposed sharpening

Use the complete finite plant, literal supplied H (including H0), positive path
J, accessible X/Y port, and computable polynomial augmented bracket certificate
in the accuracy-scaled compiler note at correlation-worktree HEAD
9ca474a32b3a4799d2d14cfee7580d77750422b4. The parent note is
docs/ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md,
SHA256 c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2.
Its current wrapper sections 1--3 were read again for this argument. The
conditioned positive-time compiler note at the same revision, SHA256
db922c9b3f67a603961f5a621a67eea7fa4894b793befbcdd3b7b034011e540a,
already handles actual-duration aging by an augmented pair. That idea is reused,
not claimed as new. Existing complete parent reviews remain conditional on their
recorded identities; no historical numerical execution is claimed here.

Let d>=2. All matrices and target entries are computable. Supply h>=||H||,
Rs>=h, g>0, and a fixed positive scalar slew cap S>0, independent of requested
accuracy. Choose a rational 0<S0<=S and rational 0<a0<g by strict computable
search. Write J=j0 I+Jbar and supply b>=||Jbar||. All old factors, dirty fillers,
and arbitrary passive references remain in the complete output contract.

The proposed conclusion is qualitative: for every epsilon>0 and finite window
w>=0, a finite computable externally supplied C1 control of the form

  Hph(t)=H+Rs I+lambda J+u(t) Cr,
  Cr in {I+X_p,I-X_p,I+Y_p,I-Y_p},

can be found. At most one ray is active, 0<=u<=a0<g, |u'|<=S0<=S,
and both u and u' vanish at each pulse boundary. Its duration is the actual
returned T. No polynomial duration, pulse count, precision, or search bound is
asserted. The stronger uniform slew condition trades away the parent's explicit
polynomial resource bounds. A bound on the first derivative is not a hard
frequency-bandwidth bound or a bound on all higher derivatives.

The supplied certificate is essential. This statement does not establish native
control availability, a source law, programmable isolation, or any physical
axiom. It does not cover an arbitrary H lacking the parent's certificate.

## 2. Compact semigroup with physically rounded pulses

For a selected lambda>0 with nonzero certified bracket determinant, put
HP=H+Rs I+lambda J. In G=U(d) x U(d), define skew-Hermitian pairs

  A=(-i HP,-i H),       Br=(-i Cr,0).

The second component records the same elapsed physical time and is not another
physical plant. Let K be the closure of endpoint pairs reached by finite words
of free waits and the cubic ramp--hold--down C1 pulses defined below, with real
amplitudes in (0,a0] and nonnegative hold lengths. Include the empty word.
Concatenation preserves the endpoint conditions,
so K is a compact closed semigroup containing the identity.

Every compact closed subsemigroup of a unitary group containing the identity
is a group. For k in K, compact recurrence of the powers gives integers n_j>=2
with k^{n_j}->I (a finite-order element also has such a sequence). Thus
k^{n_j-1}->k^{-1}, so the inverse belongs to K. One elementary recurrence proof
places finitely many powers in arbitrarily small cells of the compact group,
takes two powers in one cell, and uses the unitary invariant norm; repeating
powers of a finite-order element handles bounded recurrence indices.

Define L={X skew-Hermitian pairs: exp(tX) in K for every real t}. Matrix Trotter
limits prove closure under addition; the standard four-exponential commutator
limit proves closure under brackets; rescaling and continuity prove real-linear
and norm closure. Consequently L is a closed real Lie algebra. Free positive
waits and the group property imply A in L.

For any rational 0<a<=a0 and any ray r, use q(x)=3x^2-2x^3 and

  delta(a)=3a/(2S0).

The up-ramp u(s)=a q(s/delta), 0<=s<=delta, has max|u'|=S0;
the down-ramp uses a[1-q(s/delta)]. Both endpoint derivatives vanish.
Let Ua and Da be their augmented propagators. A hold of length t>=0 gives

  Pa(t)=Da exp[t(A+a Br)] Ua.

Both Pa(t) and Pa(0) belong to K, and K is a group. Hence

  Pa(t) Pa(0)^{-1}=Da exp[t(A+a Br)] Da^{-1}

belongs to K, and X_a=Ad_Da(A+a Br) belongs to L. The inverse is used only
inside the closure proof; this is not a physical negative-time instruction.

Unitary Duhamel comparison gives

  ||Da-exp(delta A)|| <= ||Br|| integral_0^delta u(s) ds
                         = ||Br|| a delta/2 = O(a^2).

For a fixed lambda, A is fixed. Since Ad_exp(delta A) A=A,

  ||Ad_Da A-A|| <= 2||A|| ||Da-exp(delta A)|| = O(a^2).

Also Da->I, so Ad_Da Br->Br. Therefore

  (X_a-A)/a -> Br as rational a decreases to zero.

Each quotient belongs to L, and L is closed: every Br belongs to L. This is
the specific step avoiding ramps whose slew must diverge at higher accuracy.
It uses arbitrarily small positive amplitudes and durations, and may require
unbounded precision, numbers of pulses, and total runtime.

## 3. Use of the actual augmented certificate, including scalar phases

L contains A and A+g Br. The parent's five augmented generators, after the
fixed positive time-unit scaling, differ from these only by scalar identity
blocks. Every supplied tree has at least two leaves, so those scalar blocks
drop out of its commutators. The parent's certified d^2-1 tree evaluations
therefore lie in L and span su(d) x {0}. This step uses both X and Y controls;
no assertion is made that a single Z control has the same certificate.

Moreover B_(+X)+B_(-X)=(-2i I,0), so L contains the first scalar direction.
It follows that u(d) x {0} is contained in L, and thus (W,I) belongs to K for
every full target W in U(d). Existence of a matrix logarithm establishes this
last inclusion. The algorithm below does not request a computable logarithm or
a branch choice for it.

Using full U(d), rather than silently removing a trace, is deliberate. The
literal Rs scalar and all scalar port actions remain inside each physical
propagator and its elapsed-time recurrence. A target global phase may be
included in W. This differs from the parent's explicit separate comparison
phase convention; it supplies no license to discard scalar energy terms.

## 4. A terminating qualitative search and actual-duration comparison

Restrict amplitudes to rationals in (0,a0], all hold and wait durations to
nonnegative rationals, and use the fixed cubic ramps above. Dependence of a
finite product of propagators on these parameters is continuous, so the closure
of this countable family is the same K. Fairly enumerate all finite such words,
including ray choices. For any fixed positive rational eta, search, with
precision dovetailed across words, for strict certified inequalities

  ||U(T)-W|| < eta,        ||exp(-iHT)-I|| < eta.

The pair (W,I) is in K, with arbitrarily small error, so the search terminates.
One can use certified Frobenius upper bounds as sufficient tests: convergence
in operator norm implies convergence in Frobenius norm in fixed dimension.
All matrix entries, durations, and piecewise-polynomial controls are computable.
Certified quadrature/product propagation is possible in finite dimension. For
example a left-frozen step of length Delta on a ramp has Duhamel error at most
S0 ||Cr|| Delta^2/2; summing steps plus certified matrix-exponential errors
gives an explicit convergent enclosure. Free and hold segments use their
constant generators. No exact equality or exact-zero oracle is required.

The second inequality records the word's actual duration, so

  ||U(T)-W exp(-iHT)|| < 2 eta.

To require T>=Tmin>0, prepend a fixed computable positive free wait t_pre>=Tmin.
The desired remaining pair is (W,I) exp(-t_pre A), which belongs to K. Density
then again supplies a finite word. The search can instead enumerate words with
this fixed prefix and test the same final pair. The fixed prefix need not be
a rational approximation to any matrix-dependent recurrence.

This existence and search argument establishes no useful worst-case time or
precision complexity. The bracket certificate at each selected lambda and the
computability oracles are supplied inputs. Physical plant evolution during
the mathematical search remains a separate chronological obligation.

## 5. Output window, positivity, and common instantaneous added strength

Choose a positive rational Lambda<=1 with Lambda w b<=epsilon/4. This is always
possible for finite computable w and b, using upper bounds if needed. If w b=0,
any positive rational Lambda<=1 works; an implementation can simply choose a
small bound using 1+w b and need not decide whether w b equals zero. The
parent's finite interpolation selector produces an actual rational
lambda in [Lambda/2,Lambda) with the same nonzero augmented bracket determinant.
No assumption lambda T<<1 is used. Choose positive rational eta<=epsilon/8.

After the returned control ends, u=0. For 0<=s<=w,

  U(T+s)=exp(-is HP) U(T),
  ||U(T+s)-exp[-i(Rs+lambda j0)s] exp(-isH) W exp(-iTH)||
      <=2 eta + lambda s ||Jbar|| <= epsilon/2.

Thus the complete channel trace-norm discrepancy is at most epsilon, uniformly
over arbitrary passive references and all old inputs. This is the usual
2||U-V|| bound for unitary channels acting on density operators. Scalar phases
during the runtime were controlled in the full U(d) search; the displayed
post-completion scalar phase is tracked explicitly. This is not the earlier
compiler's chi(T+s) formula with its parameters simply reused.

All physical generators are positive as whole operators: H+Rs I>=0, J>=0,
Cr>=0. There is no claim that every old local summand is positive. For the
parent's path J=sum_edges(I-SWAP), each bond has norm 2 and at most two such
bonds meet a site. With lambda<=1 the added incident path norm is at most 4;
the sole port contribution has norm <=2g. Representing the literal scalar
reserve as one onsite Rs I gives a conservative added incident strength bound

  J_added <= Rs+4+2g,

independent of epsilon. This does not count old H a second time or replace it.
The bound is conditional on the supplied path geometry and port availability.
The fixed scalar slew bound implies ||dC/dt||<=2S; no cap on second or higher
derivatives is claimed.

## 6. What remains open

This is an externally controlled compiler ingredient. Its controller, timing,
coefficient access, and output-window isolation have not been autonomously
realized. It does not establish a static positive ordinary-NN qubit Hamiltonian
with a common local strength cap implementing this word while retaining every
controller output. The existing clock and mediator may still require growing
couplings, even when a waveform has bounded slew. Failure of that sufficient
recipe to give a cap would not prove impossibility for other mechanisms.

No independent check, numerical sanity check, Lean proof, new physical
identification, native state preparation, or retained audit status is claimed
by this initial root proposal. Novelty is limited to a candidate fixed-slew
interface sharpening of the existing actual-time conditional compiler; the
compact-control ingredients themselves are standard mathematical machinery.


---

## Immutable source body: exposed_comparison_and_minimum_time_corollary

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# Source-exposed comparison of the two fixed-slew proofs

Disposition: no load-bearing mathematical defect found in the root's conditional qualitative construction at the identified bytes. Its down-ramp quotient and first-centre argument work. Its coherent scalar-phase contract is different from the original independent proof and must remain explicit. This is source-exposed review, not a new protected derivation, a compiler execution or an audit verdict.

## Sources and scope

I read the complete root `DERIVATION.md`, 11,481 bytes, SHA256 `c46422d545bf1b8eaa72345ed4cffe293e073da1cc4aa1903661fd7ff3771e6e`, after my original freeze. The root's `INITIAL_FREEZE.json`, SHA256 `d0d4dc6619d9452b9b975612c973e13e3dac2faed3cdd5483801371aab7552bf`, contains that matching member identity. The freeze helper is provenance only and was not inspected. Exposure began at `2026-10-15T23:52:01.651089+00:00`; captures are under this directory's `source_at_launch/`.

The compared independent proof remains unchanged at SHA256 `c6bf17a1e80e05dd7121031c3497d8c2149198e24f7ba0e4e289270540f93ff5`, under original freeze SHA256 `cf182b8f14d130ff4d845e78cf986e00ff625a33037b24c655470d3393479ee5`. Its complete parent-source and instruction coverage remains in the original `SOURCE_COVERAGE.md`. Both proofs use the same fixed computable augmented polynomial certificate and literal complete H. I read no other worker's result. The root's report of its own favorable read was not used as a mathematical premise.

## 1. Down-ramp conjugation quotient is valid

Use the root's notation A=(-i HP,-i H), B_r=(-i C_r,0), delta=3a/(2S0), and let U_a,D_a be the actual up/down-ramp propagators. The chronological formula

    P_a(t)=D_a exp[t(A+a B_r)] U_a

is correct, including t=0. In the compact reachable closure K, inversion gives

    P_a(t) P_a(0)^-1 = D_a exp[t(A+a B_r)] D_a^-1.

Positive t and group inversion supply both signs of t, so X_a=Ad_(D_a)(A+aB_r) lies in the root's Lie algebra L. These inverses are closure statements; they are not negative physical waits.

The down-ramp area is a delta/2. Unitary Duhamel gives

    ||D_a-exp(delta A)|| <= ||B_r|| a delta/2
                           = (3||B_r||/(4S0)) a^2.

Consequently

    ||Ad_(D_a)A-A||/a <= (3||A||||B_r||/(2S0)) a -> 0.

Also ||D_a-I|| <= delta (||A||+a||B_r||), so Ad_(D_a)B_r -> B_r. The exact decomposition

    (X_a-A)/a = (Ad_(D_a)A-A)/a + Ad_(D_a)B_r

therefore tends to B_r. Real linearity and norm closure of L complete the argument. The factor ||B_r||=2 for a positive Pauli ray is retained in these bounds. For each selected lambda, A is fixed during this limit; no uniform-in-lambda runtime estimate is needed.

The independent proof obtains the corresponding port directions by a different calculation: its interaction-picture weak-bump endpoint differs from exp(beta delta^2 B) by at most beta||A||delta^3. Both calculations meet fixed first-derivative caps by lowering amplitude with width. Neither establishes a hard bandwidth or higher-derivative cap.

## 2. Full U(d) first-centre accessibility is valid

The root's physical t0 A and t0(A+g B_r) differ from the corresponding parent traceless augmented generators only by central identity blocks. For the inactive leaf, the extra first scalar is -i t0(h0+Rs+lambda j0)I; for an active leaf it includes -i t0 g I as well. The second extra scalar is always -i t0 h0 I. Every supplied tree has at least two leaves, so these central differences vanish in its commutators. The same certified basis of su(d) x {0} therefore lies in L.

In addition,

    B_(+X)+B_(-X)=(-2i I,0).

This is a real-linear Lie-algebra sum implemented in closure by sequential controls, not simultaneous activation of both positive rays. It supplies the first scalar direction; together with the certified basis it gives u(d) x {0}. Compact-group recurrence supplies inverses of scalar directions just as it supplies other inverses. The nonnegative instantaneous physical coefficient does not obstruct full phase accessibility modulo 2pi over unrestricted positive time.

Thus (W,I) belongs to K for every computable full W in U(d). This argument does not need a computable logarithm branch or a supplied determinant lift. The parent's determinant lift remains part of the separate independent proof's interface.

The root's scalar coefficient cap a0 and scalar slew S0 correspond to operator caps 2a0 and 2S0. To meet arbitrary specified operator caps C_max,S_max, choose a0<min(g,C_max/2) and 0<S0<=S_max/2. The strict computable choices and the quotient proof are unchanged.

## 3. The coherent phase contracts must not be conflated

The independent proof searches in the traceless pair and restores the actual scalar action. Its comparator is

    V_SU(s)=exp[-i((Rs+lambda j0)(T+s)+A_s+theta)]
            exp(-isH) W exp(-iTH).

The root instead searches the full physical pair near (W,I), including the first runtime scalar and the full second H scalar. Its comparator is

    V_full(s)=exp[-i(Rs+lambda j0)s] exp(-isH) W exp(-iTH).

The root's full-phase runtime search justifies this different convention. It does not remove Rs, h0 or the positive-ray scalar energy: those terms are inside every physical propagator and recurrence. At the same formal T,A_s,W, these two comparator formulas differ by exp[-i((Rs+lambda j0)T+A_s+theta)], a scalar constant over the output window. They define the same density-operator channel, but their coherent operator-norm targets can differ substantially. A word certified under one search cannot simply inherit the other's coherent phase bound.

Both keep the order exp(-isH) W exp(-iTH), the actual returned time, and the path's full runtime evolution. Neither assumes lambda T small. The independent SU(d) proof is the direct compatible continuation of the parent's printed chi(T+s) convention. If the root version is published as well, its full-phase target and stronger scalar recurrence condition need their own statement and attribution.

## 4. Effective enumeration and robustness qualification

The root's rational amplitudes give rational delta because S0 is rational; rational hold/wait lengths and the fixed cubic ramps form an effective countable family. Continuity of each finite-word propagator in its finitely many parameters makes its closure equal to the real-parameter K. Dovetailing certified propagation precision across words avoids being trapped at an equality threshold. A strict witness exists because (W,I) is in K, and full finite-dimensional Frobenius tests are sufficient. The per-ramp left-freezing error S0||C_r||Delta^2/2 is valid. Certified finite-product evaluation must retain exponential approximation and roundoff amplification; exactly unitary numerical approximants are unnecessary. The root's prose allows this standard enclosure implementation.

The root's displayed epsilon window bound is a **nominal** result. Additional actual full-space generator error costs 2E_int in the complete trace bound. To reuse the parent's actual-defect contract, allocate it explicitly. For example, eta=epsilon/8, the parent's selector with lambda||Jbar||w<=epsilon/64, and E_int<=epsilon/64 give the same conservative 9epsilon/16 bound as the independent proof. All faults share that one integrated budget. Peak positivity and delivered waveform cap compliance are not implied by an integrated defect allowance alone.

Neither proof provides a polynomial bound on search, precision, pulse count, duration or accumulated scalar/norm action. The root's added incident-strength estimate Rs+4+2g is consistent with the supplied path geometry and a single onsite representation of the literal scalar reserve; it does not bound an autonomous clock or mediator, nor make each old local block positive.

## 5. Separate minimum-runtime corollary

The root's optional T_min prefix is valid with a supplied computable finite T_min, or a supplied computable upper bound. Choose a fixed positive rational tau>=T_min. A fixed computable tau also suffices. For the root pair, the suffix target is

    (W,I) exp(-tau A),

which lies in K. Chronological execution of the prefix first gives suffix times exp(tau A), so the root's multiplication order is correct. Enumerating suffixes and testing the complete prefixed pair terminates. This enforces a lower bound on T, not an arbitrary prescribed completion time.

The same corollary can be added **separately** to the unchanged independent proof. With its traceless A and G, set Z=diag(Wtilde,I), F_pre=exp(tau A), and search for a suffix near Z F_pre^-1. This target is a computable member of G because G is a group. Test the total pair F_suffix F_pre against Z at the original tolerance. Then T=tau+T_suffix>=T_min, both cap conditions and all zero endpoint conditions persist, and the exact scalar ledger remains

    chi(T+s)=(Rs+lambda j0)(T+s)+A_s+theta.

The prefix contributes no port area, but contributes its full H, reserve and path time and phase. Calibration and action use the increased actual T+w. This is a source-exposed corollary, not content retroactively present in the original freeze. It preserves the no-polynomial-bound qualification and adds no autonomous controller claim.

## Evidence limit

This comparison checks the complete root argument analytically against the original proof and the pinned parent contracts. No new numerical pulse run, external theorem lookup, formal proof, independent-model replication or audit occurred. Original frozen files were preserved; only this separate exposed-comparison directory was written. The separate comparison freeze records exact source and deliverable identities, not scientific status.
