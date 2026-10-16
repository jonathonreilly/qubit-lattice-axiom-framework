---
claim_id: preparation_angle_energy_moments_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
canonical_parent_binding_complete: true
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Preparation-angle errors and energy moments: bounded conditional theorem

Claim type: bounded_theorem. Current surface: conditional support; actual source and canonical review evidence must accompany integration, and independent audit remains pending.

Primary runner: `scripts/preparation_angle_energy_moments_2026_10_16.py` (source-integrity metadata only; no scientific replay).

## Question and accepted scope

How accurately must the angles in the supplied sine-state preparation be calibrated to control battery energy moments, and can a small full-output error alone control preparation work uniformly in battery size? The accepted analytical result gives a preparation-specific reverse-hybrid bound and a finite lower family. The complete original argument, exposed review and controlling root qualifications follow unchanged. The last body controls the original phrase “positive perturbation”: the increment is positive and the complete actual pulse stays positive; the additive residual is indefinite.

The sole direct mathematical parent is [local conserving preparation](LOCAL_CONSERVING_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md), pinned at SHA256 `6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f`. Only its prefix preparation is used. Its finite-lift dependencies remain transitive; Git ancestry and interacting candidates add no premise here. This packet contains no extension of the runtime protocol.

Use one battery with M >= L, gap Delta > 0 and independent exact vacuum. The old/reference input is arbitrary, the old finite self-adjoint K is exactly decoupled from the battery, and K >= 0 is additionally needed for positivity of the complete free generator. The specified ordered first flip and conditional rotations have exact 2pi reserves, carriers, envelopes, clocks and endpoint number phase. Faults are real deterministic angle changes delta_i only; eta = sum_i |delta_i|. The vacuum trajectory reaches prefixes through L, but no invariance of the full prefix subspace for arbitrary battery inputs is asserted. All gates act on their full physical supports; no projection discards a bad output.

## Bounds and their conventions

The full vector/isometry error is at most eta, and the unhalved joint trace error is at most 2eta, including any reference. For this nonoverlapping angle-only family the integrated full-operator Hamiltonian residual is eta. At a reverse hybrid, earlier gates are nominal and later gates actual. The exact response is

    w_i [A_i - f(i)] [sin^2(theta_i + delta_i) - sin^2(theta_i)].

For positive integer r, the dimensionless raw moment error is bounded by

    B_r(L,eta) = 2sqrt(2) L^(r-1/2) eta + L^r eta^2.

The variance bound has different constants:

    |Delta Var(B)| <= 6sqrt(2) L^(3/2) eta + 3L^2 eta^2.

Physical battery raw moments multiply by Delta^r, and variance by Delta^2. The complete free energy F0 = K + Delta B retains all binomial cross moments:

    |Delta <F0^r>| <= sum_(k=1)^r binom(r,k)
                       |<K^(r-k)>| Delta^k B_k(L,eta).

Only the stated actual product structure makes old K unchanged and covariance zero. It also makes the complete F0 variance error equal the battery-energy variance error. Coupled or initial faults reopen that argument and can involve width M, not just L. The L = 1 upper bound is conservative.

For dimensionless tolerance t_r, a sufficient raw-moment allocation is the minimum of t_r/[4sqrt(2)L^(r-1/2)] and sqrt[t_r/(2L^r)]. For variance tolerance t_v it is the minimum of t_v/[12sqrt(2)L^(3/2)] and sqrt[t_v/(6L^2)]. Physical tolerances first divide by the appropriate Delta power. These are sufficient allocations, intersected with the standing per-angle restriction; eta <= 1 is one sufficient way to enforce it. They are not budgets additional to the output error already spent.

At fixed Delta and L = Theta(epsilon^-1), O(epsilon) accuracy in mean energy or signed work has sufficient total eta = O(epsilon^(3/2)); raw second moment or variance has eta = O(epsilon^(5/2)). Conservative uniform allocations to L angles add one power of epsilon. Necessity of those uniform, second-moment or variance allocations is not claimed.

## Positive complete controls and work

For |delta_i| <= 1 the complete actual generators retain the 2pi reserve, stay positive and have norm below Q_* = 6pi. With the literal rotating carrier, a sufficient slot length is

    h >= max(4hbar Q_*/g, sqrt(8pi hbar Q_*/sigma), 8pi Delta/sigma).

The local driven norm and derivative then obey g/2 and sigma/2. L serial slots and one parallel final-phase slot fix tau = (L+1)h before the endpoint phase is selected; all M phase controls are paid globally as well as locally. A positive delta does not make delta nY a positive operator. The latter has both signs, although the complete pulse is positive. The witness therefore says nothing about a fault class requiring positive additive Hamiltonian errors.

Controls vanish at the same F0 endpoints and the battery starts in vacuum. Signed net modeled preparation work is Delta <B>, with error Delta Delta<B>. This does not price absolute work, temporary control-energy load or microscopic controller outputs; the reserves remain installed and counted separately.

For even L = 2n >= 16 the middle-angle linear response is at least sqrt(L)/192, and the finite remainder gives Delta<B> >= sqrt(L)delta/384 for 0 < delta <= 1/(384sqrt(L)). For even L >= 384^2, epsilon = 1/L and delta = epsilon give vector error <= epsilon but work error >= Delta sqrt(epsilon)/384. For an unhalved trace target epsilon, use delta = epsilon/2 and the denominator becomes 768. This establishes the worst-case square-root-L mean sensitivity for this circuit. It does not exclude signed compensation, other schedules or resources, feedback, or conserving error classes.

## Evidence, status and release boundary

The root accepted the proposal after a same-selected-model, source-exposed analytical review with prior preparation/integration exposure. This was not blind replication, formal verification or an empirical calibration. No scientific computation or fixture replay was performed for the result or this packaging task. The provenance primary verifies byte identities, source membership, receipt linkage and scope fields only; invoking its canonical entry point refuses until the actual source, base and canonical review evidence is bound.

The original proposal's pending status and the exposed review's pending root disposition remain historical records. Root acceptance `d32049fc5fe1f8ec166d333ace01e5b1738991e51773eebb5085eeff172ecec4` and the final controlling qualifications below supersede those statuses for the source mathematics only. The first root metadata recorder failed on the review seal filename; its exit 1 source and full streams remain beside the successful distinct v2 exit 0 record. Neither supplies a verdict on this new wrapper or primary.

Vacuum, isolation, exact gap, phase-locked quadratures, timing and external control remain supplied. Diagonal phase errors can preserve B moments while damaging the coherent output. Generic faults, native sources, autonomous preparation/release/halt, microscopic work storage and indefinite reuse remain outside the theorem. The frozen source packet retains its historical null wrapper/source, base, canonical and publication fields. Current source/canonical review and base evidence are bound separately; publication and retained status require their later actual paths. Formal retained status requires the independent audit path.

## Preserved complete mathematical record

The following three bodies are verbatim. Read the final controlling qualifications together with the original and the exposed review.


<!-- Unchanged complete source: original_proposal -->

# Sine preparation: angle-error bounds for work and moments

Status: proposed conditional analytical result, pending a separate mathematical check. This concerns the supplied driven prefix preparation in the local conserving preparation note, exact SHA256 6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f. It does not change that note or its qualifications. The later interacting preparation and coherent runtime fault proposals motivate the question but are not premises of the proof below. This is original finite-dimensional algebra; no scientific program or historical fixture has been executed for it.

The question is quantitative: under a particular coherent angle-error model for the existing sine preparation, how accurately are the preparation work and energy moments reproduced? A sum of small local rotation errors gives a better bound than a generic trace-distance estimate, but does not give a reservoir-size-independent first-energy coefficient. The claimed rates below concern this schedule and this fault class, not every possible preparation procedure or every local Hamiltonian error.

## 1. Physical protocol, input and fault model

One battery contains M>=L qubits, L>=1, with number operator B=sum_j n_j and physical free term Delta B, Delta>0. Initially it is exactly vacuum, independently of the unknown old register and any passive reference. The old generator K is an arbitrary supplied finite decoupled self-adjoint operator; take K>=0 when imposing the parent's positivity contract. No battery/old interaction is present during preparation. The old/reference state is arbitrary. All battery, old and reference outputs are retained.

Let p_m=1^m 0^(M-m), including p_0=vacuum, and

    b_m=sqrt(2/(L+1)) sin(pi m/(L+1)),  1<=m<=L,
    w_i=sum_(m=i)^L b_m^2,
    beta=sum_(m=1)^L b_m p_m.

The nominal circuit flips the first site by exp[-i(pi/2)Y_1], then applies exp[-i theta_i n_i Y_(i+1)], i=1,...,L-1, where

    cos(theta_i)=b_i/sqrt(w_i),
    sin(theta_i)=sqrt(w_(i+1)/w_i).

Use the parent's actual positive integrated generators 2pi I+(pi/2)Y_1 and n_i(2pi I+theta_i Y_(i+1)), absolute-time rotating carriers, fixed slot durations, and final battery number-phase cancellation. The integer-spectrum reserve exponentials are exactly identity on the full local Hilbert spaces. The full physical carrier and phase schedule is retained, not replaced by an abstract gate count. After the declared duration tau_p the old propagator is exactly E_p=exp(-i tau_p K/hbar), by disjoint support. The final free generator is the same F0=K+Delta B as at admission; all added controls vanish at both endpoints.

The only imperfections considered in the new estimate are real fixed angle changes delta_0 in the flip and delta_i in conditional rotation i. The 2pi reserves, carriers, envelopes, clock, endpoint cancellation, isolation and all other terms remain exact. Let

    eta=sum_(i=0)^(L-1) |delta_i|.

This is a supplied structural fault model, not a conclusion from trace distance or arbitrary coefficient error. For example, the actual pulse differs by hbar f(t) delta_i times the appropriately rotated Y or nY, so its integrated full-operator discrepancy is |delta_i|. Pulses are sequential, giving total dimensionless discrepancy eta. The perturbation has support at most two sites and changes battery number by at most one. During preparation the *nominal* controls themselves change B; runtime charge-conservation theorems cannot simply be reused here.

For a concrete positive strength/slew realization impose |delta_i|<=1 and use a common Q_*=6pi and

    h_p >= max(4 hbar Q_*/g,
               sqrt(8pi hbar Q_*/sigma), 8pi Delta/sigma).

Then the actual Q blocks remain positive, have norm <=Q_*, and their number commutators have norm <=pi. For f=(1-cos(2pi t/h_p))/h_p, the actual pulse norm is <=g/2 and its derivative is <=sigma/2: the envelope contribution is <=2pi hbar Q_*/h_p^2 and the carrier contribution <=2pi Delta/h_p. The final exact phase layer uses its separately supplied parent bounds. This choice reserves room for the actual angle deviations; it does not infer positivity or slew from a small integrated error. Slot durations can remain fixed as L grows. The full incident/free-energy ledger and supplied rotating quadratures remain physical premises.

The actual circuit is unitary on the entire battery, including all off-prefix inputs. The statements below are about its specified vacuum input domain. Prefix preservation on that domain does not discard the off-prefix output of an arbitrary error model.

## 2. Exact distribution and complete state error

With a correct first flip, arbitrary real conditional angles a_i give the prefix probabilities

    P_a(m)=cos^2(a_m) product_(j<m) sin^2(a_j), m<L,
    P_a(L)=product_(j<L) sin^2(a_j).

Each prefix amplitude has one circuit path, so this formula holds even when some sines or cosines are negative. There is no incoherent measurement or reset. A faulty initial flip leaves vacuum probability sin^2(delta_0) and multiplies all nonzero-prefix probabilities by cos^2(delta_0). The final number-phase layer changes none of these probabilities. Sites beyond L remain vacant in this fault model.

Unitary telescoping or Duhamel gives the complete isometry estimate

    ||U_actual J0 - (E_p tensor |beta>)|| <= eta,

with the same actual old/reference factor and the parent's exact scalar convention. The positive reserves remain fixed and therefore introduce no unreported new scalar. For mixed old/reference input the unhalved complete trace error is <=2eta. These inequalities alone would yield the coarser moment bound L^r eta; the following argument uses the specified error structure.

## 3. A hybrid proof of the moment bound

Let f be any function on {0,...,L} with f(0)=0 and range contained in [0,F]. For controlled rotation i form a hybrid with all earlier gates nominal and all later gates actual. Its incoming continuation weight is exactly w_i. Stopped prefixes m<i will never be touched again. Conditional on continuing past site i, the later actual gates produce a distribution on {i+1,...,L}; write its f-expectation as A_i. Conditional on stopping, the value is f(i). Both lie in [0,F]. The change caused by replacing only theta_i with theta_i+delta_i is exactly

    w_i [A_i-f(i)]
       [sin^2(theta_i+delta_i)-sin^2(theta_i)].                 (1)

The suffix can be arbitrary within the actual angle-error circuit; no ideal state is reinserted after a faulty gate. Taylor's theorem with |(sin^2)''|<=2 gives

    |sin^2(theta_i+delta_i)-sin^2(theta_i)|
       <= |sin(2theta_i)| |delta_i|+delta_i^2,
    w_i sin(2theta_i)=2 b_i sqrt(w_(i+1)).

Since b_i<=sqrt(2/(L+1)), w_(i+1)<=1, the absolute contribution of (1) is at most

    2 F sqrt(2/(L+1)) |delta_i| + F delta_i^2.

Replace gates in reverse chronological order, so each difference has precisely the nominal prefix and actual suffix just described. At the last comparison replace the first flip; its error in f-expectation is at most F sin^2(delta_0)<=F delta_0^2. Summing yields

    |<f(B)>_actual-<f(B)>_ideal|
      <=2 F sqrt(2/(L+1)) sum_(i=1)^(L-1)|delta_i|
                                      +F sum_(i=0)^(L-1)delta_i^2
      <=2 F sqrt(2/(L+1)) eta+F eta^2.                    (2)

The bound also covers L=1: the conditional sum is empty and the exact flip error is quadratic. The last line is deliberately less sharp in that case.

Take f(m)=m^r, r a positive integer, F=L^r. Define

    B_r(L,eta)=2 sqrt(2) L^(r-1/2) eta+L^r eta^2.

Then

    |<B^r>_actual-<B^r>_ideal|<=B_r(L,eta).               (3)

The actual physical rth raw battery-energy moment error is <=Delta^r B_r. In particular the first-energy coefficient grows as sqrt(L), whereas a generic full trace bound has coefficient L. This improvement is specific to the prefix-angle model and its exact vacuum. It is not a theorem for arbitrary local perturbations.

Both means lie in [0,L], hence the dimensionless variance error is at most

    B_2+2L B_1 <=6 sqrt(2) L^(3/2) eta+3L^2 eta^2.       (4)

Multiply by Delta^2 for battery-energy variance. The old distribution of K is unchanged by its disjoint evolution. Old/battery covariance is zero for this exact product input and product dynamics; no such covariance conclusion is asserted for generic correlated preparation errors. Full-F0 moments use the actual binomial cross terms with old K and retain its supplied norm/moments.

For several isolated, independently initialized branches with gaps Delta_j, lengths L_j and deterministic angle errors eta_j, the mean-energy bounds add:

    |Delta <sum_j Delta_j B_j>| <=sum_j Delta_j B_1(L_j,eta_j).

This does not replace a quantum controller or an arbitrary correlated fault process by classical independent angles. Higher joint moments require the explicit cross terms; the single-branch result (3) is the primary statement.

## 4. Work and sufficient calibration prices

Because the actual controls vanish at both endpoints, coherent prescribed-drive work is exactly the change of F0 expectation. Its old contribution is zero, while the initial battery energy is zero. Therefore the difference between actual and nominal *net preparation work* is exactly Delta times the mean-number error in (3). This is neither an absolute-work bound nor a microscopic driver-energy construction. Positive scalar reserves still contribute during the pulse and their full load/variation costs are paid even though their endpoint phases are identity.

For a dimensionless rth-moment tolerance t_r>0, one sufficient choice is

    eta <= min(t_r/[4 sqrt(2) L^(r-1/2)],
               sqrt(t_r/[2 L^r])).                      (5)

The first and second terms in (3) then each cost at most t_r/2. For L=Theta(epsilon^-1), Delta fixed, and an O(epsilon) physical mean or raw-moment allowance, sufficient total angle actions are O(epsilon^(r+1/2)). Thus the mean/work request is O(epsilon^(3/2)); the raw second-moment and variance request is O(epsilon^(5/2)). A common bound on each of O(L) angles must also pay the gate count: sufficient per-angle requests are O(epsilon^(5/2)) for mean/work and O(epsilon^(7/2)) for second moment/variance. Constants and physical units are set using (3)-(5), not by exponents alone.

These are total error allocations, not free extra budgets. The same angle discrepancy also contributes to the full-output error. Other control, phase, timing, vacuum or isolation errors must be allocated separately or compared through an alternative complete-generator bound without double counting. A pure final diagonal phase error does not alter B moments, but it can still spoil the full packet state and must meet its separate output budget. A generic residual outside the present circuit class receives the ordinary full-resource growing-width allowance; it cannot be relabeled as an angle error to use (2).

## 5. A matching first-order growth witness

The sqrt(L) coefficient cannot be replaced by an L-independent constant for all these preparation circuits and arbitrarily small single-angle errors. This is a statement about this particular fault interface, not a prohibition on other calibrated or robust preparation methods.

Set L=2n with n>=8 and perturb only controlled rotation i=n by a positive delta. All other gates, the initial flip, the clock, the reserves and endpoint controls remain exact. By the sine symmetry,

    w_(n+1)=1/2,
    b_n>=1/sqrt(2n+1).

Let D be the nominal conditional remaining mean beyond n, minus n:

    D=(sum_(m=n+1)^(2n)(m-n)b_m^2)/w_(n+1).

For m in {ceil(3n/2),...,floor(7n/4)} there are at least n/8 terms, m-n>=n/2, and sin^2(pi m/(2n+1))>=sin^2(pi/8)>1/8. Thus

    sum_(m=n+1)^(2n)(m-n)b_m^2
       >=n^2/[64(2n+1)]>=n/192,
    D>=n/96=L/192.

The exact mean difference is

    Delta_mu=w_n D [sin^2(theta_n+delta)-sin^2(theta_n)].  (6)

Its derivative at zero is

    a=2 b_n sqrt(w_(n+1)) D>=sqrt(L)/192.

The same Taylor remainder and w_n D<=L give

    Delta_mu>=sqrt(L)delta/192-L delta^2.

Consequently, for 0<delta<=1/(384 sqrt(L)),

    Delta_mu>=sqrt(L)delta/384.                          (7)

This is an exact analytic witness; no numerical asymptotics are substituted for the inequalities. It uses one positive onsite-controlled rotation perturbation with charge bandwidth one, complete integrated Hamiltonian discrepancy eta=delta, a fixed support of two sites, and fixed strength/slew headroom as in section1. All endpoints restore the same F0. It does not violate a runtime theorem whose nominal plateau conserves charge: here the later ideal number-changing preparation gates amplify a change in continuation probability.

For example choose epsilon=1/L along even L>=384^2 and delta=epsilon. The complete vector error is <=epsilon and the physical residual action is epsilon, yet the preparation-work error is at least Delta sqrt(epsilon)/384. Thus neither that state estimate nor a bounded-bandwidth global residual budget alone implies O(epsilon) work accuracy for this nonconserving preparation schedule. In the small-error worst-case class, (7) matches the sqrt(L) dependence of (3) up to constants. Known signed calibration errors may be corrected; number-conserving fault classes, other schedules, feedback, different ready resources and different observables change the problem. None is excluded.

## 6. Evidence and remaining decisions

The proof above uses the exact existing prefix preparation and finite hybrid/telescoping algebra. No new spectral supplier, physical axiom, audit verdict or numerical experiment is imported. The next check should reconstruct the hybrid distribution for arbitrary real faulty angles, the treatment of the first flip and the lower-bound arithmetic, and verify that the physical waveform/endpoint/load assumptions really realize the stated error model. Full output, net work, absolute work, raw moments and covariance must remain distinct.

The proposed calibration sharpening is conditional on exact independent vacuum and the declared classical angle-error interface. Native rotating controls, actual error certification, a microscopic work reservoir, arbitrary interacting preparation faults, autonomous release, record formation and indefinite reuse are still separate physical questions. This result does not establish those suppliers or close the full physical-realization objective.


<!-- Unchanged complete source: exposed_analytical_review -->

# Source-exposed check: preparation angle errors, work and moments

The proposed moment upper bounds, variance constants, positive actual pulse realization and first-order lower-bound family survive this analytical check under the declared independent-vacuum and deterministic angle-error model. I found no blocking algebraic defect in equations (1)–(7). This supports a conditional preparation-specific result, subject to root's disposition; it is not a retained audit or a physical supplier certificate.

One wording correction should accompany further use. Source line 150 calls the witness a “positive ... perturbation.” The angle increment is positive, and the **complete actual pulse generator** is positive, but the additive difference `delta nY` is indefinite: its nonzero eigenvalues are `+delta` and `-delta`. A precise replacement is: “one positive angle increment of an onsite-controlled rotation, with the complete actual integrated generator remaining positive.” The witness does not establish the same obstruction in a class requiring the additive Hamiltonian perturbation itself to be positive. No source file was edited.

Two quantitative boundaries also matter in reuse. Equation (5) prices raw moments; a variance tolerance needs the constants from equation (4), given explicitly below. The single-angle witness matches the first-mean coefficient's `sqrt(L)` growth in the small-error worst-case class. It does not establish necessity of the stated uniform per-angle allocation, raw-second-moment allocation, or variance allocation, nor rule out other preparation methods.

## Source and exposure

The complete 158-line proposal is `PROPOSED_LEMMAS.md`, 14391 bytes, SHA256 **fd847fb098e1fa15f13a309065e99065128c2be6adaf2a6c336c3a38e5a9aced**, in source freeze **b2546340ec39a575f6bc97f37f56cc05cf4d381086d7d6298b6edb4dcde0f2ef**. Its source manifest is **f0417ca63a827426d0e70058341a46e4dafc61f1f8d4a975d5ee30c8acda787a**. Line references below refer to that unchanged captured proposal.

The sole mathematical parent is the existing local conserving preparation note, 170504 bytes, SHA256 **6db93809f12315668f720006c6a443301ad682381ce5629c173b1ff1c6d66a7f**. The relevant preparation construction, exposed review and controlling qualifications were reread, including the carrier sign, `[n,Y]=iX`, phase slot, exact input domain and drive-work distinction. The parent's runtime synthesis theorem is unnecessary for this new proof. Its two context candidates are not imported, and their derivations were not newly read or checked here.

This reviewer already participated in the earlier preparation exposed check and subsequent packet/integration work. The new proposal was read before this reconstruction. This is a same-selected-model, source-exposed mathematical check, not blind independence, independent experimental evidence or an independent reexecution of the parent's fixture. No new scientific computation and no historical scientific replay were needed. The evidence is the analytic reconstruction below; metadata execution verifies only identities, capture and review scope.

## 1. Domain, complete amplitudes and arbitrary reference input

Use `Y|0>=i|1>`, so `exp(-iaY)|0>=cos(a)|0>+sin(a)|1>`. Put `a_i=theta_i+delta_i` for the conditional gates. With the first flip still correct, the actual ordered circuit on vacuum produces

```
sum_(m=1)^L t_m(a) p_m,
t_m(a) = cos(a_m) product_(j<m) sin(a_j),        m<L,
t_L(a) = product_(j<L) sin(a_j).
```

At each step only the continuing branch has the active control site occupied and its target initially empty. A branch stopped at an earlier position has zero on every later control site and is left alone. The amplitudes can be negative; distinct stopped prefixes are orthogonal eigenvectors of B, so their probabilities are squares, not an incoherent approximation. The normalization telescopes: if `T_m=product_(j<m) sin^2(a_j)`, then `t_m^2=T_m-T_(m+1)` for `m<L`, while `t_L^2=T_L` and `T_1=1`.

The faulty first flip adds exactly

```
C_actual p_0 = -sin(delta_0) p_0
                +cos(delta_0) sum_(m=1)^L t_m(a) p_m.
```

All later controlled rotations leave `p_0` alone. Thus its probability is `sin^2(delta_0)` and every nonvacuum-prefix probability is multiplied by `cos^2(delta_0)`, as stated at lines 41–46. For `L=1` the conditional product is empty and this two-state formula is exact. The states beyond site L remain vacant throughout this ordered preparation from vacuum.

This is a statement about the reachable states from the specified vacuum. It need not assert that the entire prefix subspace is invariant under each conditional gate on arbitrary battery inputs: flipping a target inside a longer initially occupied prefix can create a nonprefix string. The actual gates remain unitary on the whole battery, and their full operators are used in the error estimate. No off-prefix output is traced out or declared absent for generic faults.

During preparation the actual Hamiltonian is a sum of a fixed old operator and battery-only controls. Hence, for every old/reference density operator, including entangled ones,

```
rho_SBR(tau_p) = (E_p tensor I_R) rho_SR (E_p* tensor I_R)
                  tensor |beta_actual><beta_actual|,
E_p = exp(-i tau_p K/hbar).
```

The arbitrary-input quantifier is on the old/reference factor, not on the battery preparation input. Arbitrary finite decoupled self-adjoint K is sufficient for factorization; K>=0 is additionally needed when asserting positivity of the complete free-plus-control generator. The equal-gap runtime assumptions and runtime buffers are not imported. The preparation itself uses only L sites plus idle sites, so `M>=L` is enough for this standalone calculation; it does not establish a conserving runtime with that smaller buffer.

## 2. Full-output error and the literal positive pulse model

For either `A=Y` or `A=nY`, `||A||=1` and

```
||exp[-i(theta+delta)A]-exp(-i theta A)|| <= |delta|.
```

Unitary product telescoping on the complete physical space gives `||C_actual-C_nominal||<=eta`. The same exact old propagator and final battery phase convention apply to both circuits. Restriction to the vacuum-input isometry and extension by any passive reference preserve the bound. For the induced channels the unhalved trace error is at most `2eta` (and at most two trivially). Thus source lines 48–52 have the correct vector and trace constants. A trace statement with tolerance epsilon rather than vector tolerance epsilon must retain that factor two.

The pulse reserve has not been removed in this calculation. Onsite blocks are

```
Q_0(delta)=2pi I+(pi/2+delta_0)Y,
```

with eigenvalues `2pi +/- (pi/2+delta_0)`. A conditional block has a zero control-zero block and the two eigenvalues `2pi +/- (theta_i+delta_i)` on its control-one block. For `|delta_i|<=1`,

```
|theta_i+delta_i| <= pi/2+1 < pi,
Q_actual >= 0,
||Q_actual|| <= 5pi/2+1 < 6pi = Q_*.
```

The same inequalities cover the first flip. The reserve commutes with its rotation, and `exp(-i2pi I)=exp(-i2pi n)=I` on the entire local spaces. Actual angle changes therefore create no additional reserve scalar. In contrast, the additive error block `delta_i nY` is generally indefinite, as noted above.

Let `R_B(t)=exp(-it Delta B/hbar)`. The actual laboratory pulse is

```
H_c(t)=hbar f_h(t-t_j) R_B(t) Q_actual R_B(t)*.
```

Conjugating by the adjoint free propagator gives interaction-picture control `hbar f_h Q_actual`, with the literal free term still installed. Directly `[n,Y]=iX`, and the conditional reserve commutes with B, so

```
||[B,Q_actual]|| = |theta_i+delta_i| <= pi
```

(replace theta_i by pi/2 for the first flip). Consequently

```
dot H_c = hbar f_h' R_B Q_actual R_B*
             - i f_h R_B [Delta B,Q_actual] R_B*,
||H_c|| <= 2 hbar Q_*/h,
||dot H_c|| <= 2pi hbar Q_*/h^2 + 2pi Delta/h.
```

The three lower bounds in source lines 32–33 give respectively `g/2`, `sigma/4` and `sigma/4`. Their sum is `sigma/2`; the new `8pi Delta/sigma` requirement correctly enlarges the parent's nominal carrier allowance. The cosine envelope has integral one, maximum `2/h`, derivative maximum `2pi/h^2`, and both it and its derivative vanish at each endpoint. Positivity, support and actual derivative bounds follow from this particular family, not from Duhamel smallness.

For this q=1 preparation there are L rotation slots and one final simultaneous M-site phase slot, so `tau_p=(L+1)h` is fixed before the phase coefficient is chosen. The parent's rational-enclosure choice gives `lambda in (3pi/2,9pi/2]` and `Delta tau_p/hbar+lambda=2pi k`. The phase layer therefore gives

```
exp[-i(Delta tau_p/hbar)B] exp(-i lambda B) C_actual = C_actual
```

on the full battery. No commutation of the number-changing C_actual with B is used. Its duration is unchanged by the angle errors. The simultaneous phase-layer norm scales with M; local caps do not turn that into a constant global load. The input vacuum, isolation, rotating quadratures, clock, physical Delta and exact phase correction remain supplied.

Finally, the actual-minus-nominal Hamiltonian in one rotation slot is exactly `hbar f_h delta_i R_B A_i R_B*`. Because `f_h>=0`, `integral f_h=1` and `||A_i||=1`, its dimensionless integrated full-operator norm is `|delta_i|`. Nonoverlapping slots sum to eta. This establishes the claimed residual action and its support/bandwidth without replacing physical operators by a prefix-space proxy.

## 3. Reverse hybrid identity and moment constants

For a conditional gate i, retain all earlier gates nominal and all later gates actual. Immediately before gate i the nominal state is

```
sum_(m<i) b_m p_m + sqrt(w_i) p_i.
```

The later actual suffix fixes every `p_m` with `m<=i`. Applied to `p_(i+1)`, it yields a normalized vector `chi_i` supported on `p_(i+1),...,p_L`. Define `A_i=<chi_i|f(B)|chi_i>`. These supports are disjoint eigenspaces for diagonal f(B), so no cross term survives in this expectation. The contribution of the continuing branch after angle a is exactly

```
w_i [ f(i) cos^2(a) + A_i sin^2(a) ].
```

Subtracting a=theta_i from a=theta_i+delta_i proves equation (1), including its sign. A_i depends on the actual suffix, not on the changed angle a or an artificially reset ideal battery. Comparing all nominal gates to all actual gates in order `L-1,L-2,...,1,0` produces precisely these hybrids.

Taylor's theorem gives

```
|sin^2(theta+delta)-sin^2(theta)|
 <= |sin(2theta)| |delta| + delta^2,
```

since the second derivative is `2cos(2theta)` and its absolute value is at most two. The coefficient for a nominal gate is

```
w_i sin(2theta_i)=2 b_i sqrt(w_(i+1))
                 <=2 sqrt[2/(L+1)].
```

Together with `|A_i-f(i)|<=F` and `w_i<=1`, this gives the contribution in line 69. At the final hybrid comparison, only the first flip changes: if `E_a f` is the actual conditional circuit's nonvacuum f-expectation, the exact difference is `-sin^2(delta_0) E_a f`. It is bounded by `F delta_0^2`, since f(0)=0. Therefore

```
|Delta<f(B)>|
 <=2F sqrt[2/(L+1)] sum_(i>=1)|delta_i| + F sum_i delta_i^2
 <=2F sqrt[2/(L+1)] eta + F eta^2.
```

This proves equation (2) for arbitrary real angle errors; the separate physical cap certificate uses `|delta_i|<=1`. No cancellation of different errors is assumed. Setting `f(m)=m^r`, `F=L^r`, and replacing `sqrt(L+1)` by the smaller `sqrt(L)` proves equation (3) with the displayed `2sqrt(2)` constant. For L=1 the actual raw moment difference is exactly `-sin^2(delta_0)` for every positive integer r; the displayed linear term is merely conservative.

As a second analytical check, the same exact distribution has tail probabilities

```
P_actual(B>=k)=cos^2(delta_0) product_(j<k) sin^2(a_j), 1<=k<=L,
E_actual f(B)=sum_(k=1)^L [f(k)-f(k-1)] P_actual(B>=k).
```

For f(m)=m this reconstructs the mean as a sum of continuation probabilities. It gives the same first-flip factor and the same single-angle tail response used in the lower witness, without a moment comparison inferred solely from a target state.

Let mu and nu denote the first and second raw number moments. Since both means are in [0,L],

```
|Delta Var(B)| <= |Delta nu| + |mu_actual+mu_ideal| |Delta mu|
                <= B_2+2L B_1
                =6sqrt(2) L^(3/2) eta+3L^2 eta^2.
```

Thus equation (4) is correct. Raw physical-energy moments multiply B_r by `Delta^r`, and variance multiplies by `Delta^2`. Under this exact product dynamics the old K distribution is unchanged and its covariance with B is zero, even when the old register is entangled with R. For clarity, the full endpoint raw-moment error obeys

```
|Delta <(K+Delta B)^r>|
 <=sum_(k=1)^r binom(r,k) |<K^(r-k)>| Delta^k B_k(L,eta).
```

This uses product structure and commuting factors; it is not a replacement of the full generator by its battery part. In particular the full F0 variance error here equals `Delta^2 Delta Var(B)`, since the old variance is identical and the covariance vanishes. Neither simplification applies to a generic coupled or initially correlated preparation fault.

## 4. Work, calibration and what is sufficient

For the closed finite quantum model driven by the prescribed classical H(t), the Schrödinger equation gives `d Tr[rho(t)H(t)]/dt=Tr[rho(t) dot H(t)]`. With controls zero at both endpoints, the actual work functional is the change of the same F0 expectation. The old contribution is unchanged and the initial battery is vacuum, so

```
W_actual = Delta <B>_actual,
W_actual-W_ideal = Delta Delta<B>.
```

This is a signed net preparation-work identity. The integral of the absolute instantaneous work rate, temporary control-energy loads and microscopic actuator energy are different quantities. Identity and controlled reserves remain installed and paid in the parent's load/variation bounds, even though their integrated endpoint phases are one. None of these formulas includes a microscopic clock/controller output that the model does not supply.

Equation (5) correctly allocates half the raw-moment tolerance to each term of B_r. For a **dimensionless variance tolerance** t_v, an explicit corresponding sufficient request is

```
eta <= min(t_v/[12sqrt(2) L^(3/2)], sqrt[t_v/(6L^2)]).
```

For a physical mean/work allowance t_E use `t_1=t_E/Delta`; for a physical raw rth-moment allowance t_(E,r) use `t_r=t_(E,r)/Delta^r`; for a physical variance allowance use `t_v=t_(Var,E)/Delta^2`. Retain the standing per-angle condition `|delta_i|<=1` for the concrete pulse caps; equation (5) alone does not impose it for an arbitrarily large tolerance. Intersecting with `eta<=1` is one simple sufficient way to guarantee it.

When `L=Theta(epsilon^-1)`, Delta is fixed and the requested physical allowance is O(epsilon), the linear term asks for total eta of order at most `epsilon^(r+1/2)`. The quadratic condition asks for `epsilon^((r+1)/2)` and is weaker at small epsilon for r>=1. Thus the proposed mean/work `epsilon^(3/2)` and second-moment/variance `epsilon^(5/2)` sufficient total requests are correct. With L angle parameters, a common bound satisfying `L max_i |delta_i|<=eta` adds one epsilon power, giving the stated `epsilon^(5/2)` and `epsilon^(7/2)` sufficient per-angle requests. These are worst-case allocations with appropriately small constants, not universal optimality statements.

The same eta is already spent in the full-output error. It is not an additional independent budget to add a second time. A final exact-in-form diagonal phase error preserves B's distribution, but can violate the coherent packet/output target. Vacuum, carrier, timing, reserve, isolation or coupled-controller errors that leave this angle class require their own complete error and growing-observable-width estimates. For such faults the physical width can be M, not the vacuum-prefix support width L.

## 5. Explicit growth witness and all constants

For `L=2n`, reflection `b_m=b_(2n+1-m)` splits the probabilities equally into the first and last n indices, so `w_(n+1)=1/2`. Also

```
b_n=sqrt[2/(2n+1)] sin[pi n/(2n+1)] >=1/sqrt(2n+1),
```

because `n/(2n+1)>=1/4` and is below 1/2. The proposed tail-displacement D is positive.

For n>=8, the integer interval from `ceil(3n/2)` through `floor(7n/4)` has cardinality at least `n/4-1>=n/8`. Each such index lies between n+1 and 2n and satisfies `m-n>=n/2`. Its angle is between pi/2 and 7pi/8, so

```
sin^2[pi m/(2n+1)] >= sin^2(pi/8)
                      =(2-sqrt(2))/4 >1/8,
b_m^2 >=1/[4(2n+1)].
```

Multiplying these three bounds gives exactly

```
sum_(m>n) (m-n)b_m^2 >=(n/8)(n/2)/[4(2n+1)]
                       =n^2/[64(2n+1)] >=n/192.
```

The last inequality uses `3n>=2n+1`, valid already for n>=1. Dividing by `w_(n+1)=1/2` yields `D>=n/96=L/192`.

Only gate n is altered, so all prefix and suffix factors in the hybrid calculation are nominal. Equation (6) is exact, with `A_n-n=D`. Its derivative is

```
a=2 b_n sqrt(w_(n+1)) D
 >=sqrt(2) L/[192sqrt(L+1)] >=sqrt(L)/192,
```

where the final inequality is `2L>=L+1`. Taylor's lower bound and `0<w_n D<=L` now give

```
Delta_mu >=sqrt(L)delta/192-L delta^2.
```

For `0<delta<=1/[384sqrt(L)]`, the subtracted term is at most `sqrt(L)delta/384`. Equation (7), including its positive sign and constant 384, follows. No asymptotic integral or numerical estimate was substituted for the finite sums. The positivity/cap certificate above applies because these deltas are below one.

With even `L>=384^2`, `epsilon=1/L` and `delta=epsilon`, the small-delta condition is exactly `sqrt(L)>=384`. The full vector error is at most epsilon, eta equals epsilon, and

```
W_actual-W_ideal >=Delta sqrt(epsilon)/384.
```

If instead one fixes the unhalved trace target to epsilon, choosing `delta=epsilon/2` under the same L restriction yields trace error at most epsilon and work error at least `Delta sqrt(epsilon)/768`. Either version rules out a reservoir-size-independent first-energy coefficient for this fault interface. It does not challenge a nominal-runtime theorem assuming charge conservation: the preparation suffix changes number and amplifies a continuation-probability error.

For sufficiently small total budgets, taking the single allowed delta equal to eta shows why the mean coefficient's `sqrt(L)` dependence is needed in a uniform worst-case guarantee for this circuit. The witness alone supplies no matching necessity theorem for every gate's precision, variance, higher moments or different algorithms. Known signed errors, other schedules, feedback, different ready resources and conserving errors remain outside that claimed obstruction.

## Disposition and limits

The proof is complete for the stated deterministic angle family and exact vacuum product domain, including arbitrary passive references, L=1 for the upper bounds, and the explicit even-L lower-bound family. Preserve the positive-angle-versus-positive-operator distinction at line 150. Use the variance-specific constants when prescribing a variance tolerance. No other correction to the displayed bounds is identified here.

No numerical experiment, general fault simulator, historical fixture, audit runner, canonical integration phase, Git mutation, publication, prompt edit or axiom edit was performed. No claim of independent blind replication, formal verification, hardware calibration, microscopic work-device closure, arbitrary interacting preparation faults, autonomous timing/release or indefinite reuse follows. The raw packet retains its original pending status; root source acceptance and any later publication remain separate actual decisions.

Reopen this check if the input readiness, angle-only error model, old/battery isolation, prefix order, reserve coefficients, rotating-carrier sign, endpoint phase/timing, supplied strength/slew, observable, or requested necessity quantifier changes. The source manifest's two context candidates were not proof premises, so this check neither accepts nor rejects them.


<!-- Unchanged complete source: controlling_root_qualifications -->

# Controlling qualifications: preparation angle errors and energy moments

Root accepts equations(1)-(7) of proposal fd847fb0 as conditional analytical results after exposed review2c12dc8f. Original proposal and review remain unchanged. The wording correction, quantitative distinctions and supplied physical premises below control future use. This is not retained audit or a hardware calibration result.

## Exact class and preparation-specific bound

The sole mathematical parent is local conserving preparation6db93809. This theorem uses its prefix preparation, not its runtime synthesis claims. Use one M>=L battery prepared from independent vacuum, the specified ordered flip and conditional rotations, exact reserves/carriers/envelopes/timing/endpoint phase, and real deterministic angle errors delta_0,...,delta_(L-1). The old/reference input is arbitrary, but the battery input is not. Actual old/battery dynamics are exactly decoupled. An arbitrary finite self-adjoint old K factors out as E_p; positivity of the total free generator additionally requires the stated K>=0. Idle sites remain included in full outputs and energy. M>=L here does not establish a runtime protocol with smaller buffers.

The actual vacuum trajectory only reaches prefixes of lengths0 throughL. This is not a claim that every conditional gate leaves the entire prefix subspace invariant on arbitrary battery inputs. Each gate remains a unitary on its full physical support; no output projection is used. The exact probability distribution, including signs of amplitudes and the faulty first-flip vacuum component, underlies the proof.

Let eta=sum_i|delta_i|. Full circuit telescoping gives vector/isometry error at most eta and unhalved joint trace error at most2eta. The actual integrated full-operator Hamiltonian residual equals eta for the stated nonoverlapping angle-only slots. At each reverse hybrid, earlier gates remain nominal and later ones actual, so the incoming continuing weight is w_i. The exact response of a diagonal f(B) is

    w_i[A_i-f(i)] [sin^2(theta_i+delta_i)-sin^2(theta_i)].

For f(0)=0 and0<=f(m)<=F on0,...,L, the source's bound follows without replacing the actual suffix by a fresh ideal state. Thus for positive integer r,

    |Delta <B^r>| <= B_r(L,eta)
       :=2sqrt(2)L^(r-1/2)eta+L^r eta^2,
    |Delta Var(B)| <=6sqrt(2)L^(3/2)eta+3L^2 eta^2.

Upper bounds include L=1, where the displayed linear term is conservative. Physical raw-energy moments multiply B_r by Delta^r; energy variance multiplies the variance bound by Delta^2. The old K distribution is identical and covariance zero only because the actual dynamics retain exact product structure. For complete F0=K+Delta B, retain the binomial cross-moment terms:

    |Delta <F0^r>| <= sum_(k=1)^r binom(r,k)
                         |<K^(r-k)>| Delta^k B_k(L,eta).

The complete F0 variance error equals the battery-energy variance error in this particular exact product class. Generic initial/coupled faults require actual covariance and full width, potentially M rather than L. Context interacting-preparation and runtime-fault candidates are not premises of this proof.

## Physical positivity and the correction

For |delta_i|<=1, each complete actual generator has its original2pi reserve and is positive, with norm below Q_*=6pi. The derivative includes the rotating-carrier term and satisfies the stated cap for

    h>=max(4hbar Q_*/g, sqrt(8pi hbar Q_*/sigma),
                                      8pi Delta/sigma).

This yields local driven norm<=g/2 and derivative<=sigma/2; the final phase layer is also paid per site and globally over all M sites. Actual positivity/support/slew follow from this specified family, not from a general integrated-norm bound. Vacuum, isolation, exact free gap, phase-locked quadratures and timing remain supplied.

Proposal line150's phrase positive perturbation must mean a positive angle increment. The complete actual pulse generator remains positive, but its additive difference delta nY has eigenvalues plus and minus delta and is indefinite. Correct downstream wording to: one positive angle increment of a controlled rotation, with the complete actual integrated generator remaining positive. No obstruction is proved for a class requiring the additive Hamiltonian perturbation itself to be positive. The immutable original wording is retained solely as historical source, controlled by this correction.

## Calibration, work and the sharpness family

For a dimensionless raw-moment tolerance t_r, a sufficient request is

    eta<=min(t_r/[4sqrt(2)L^(r-1/2)],sqrt[t_r/(2L^r)]).

For a dimensionless variance tolerance t_v use the distinct constants

    eta<=min(t_v/[12sqrt(2)L^(3/2)],sqrt[t_v/(6L^2)]).

Divide physical tolerances by the appropriate Delta power. Intersect with the standing per-angle condition; eta<=1 is one simple sufficient global guarantee of |delta_i|<=1. These allowances are not additional independent budgets on top of the already spent output eta.

At fixed Delta and L=Theta(epsilon^-1), O(epsilon) mean/work accuracy has the displayed sufficient total request eta=O(epsilon^(3/2)); raw second moment or variance accuracy has eta=O(epsilon^(5/2)), with appropriately small constants. The conservative uniform per-angle allocations add one power, epsilon^(5/2) and epsilon^(7/2), respectively. These are sufficient worst-case allocations, not universal optimized necessities.

Controls vanish at the same F0 endpoints, old K-energy is unchanged and initial battery is vacuum. Therefore signed net modeled preparation work is Delta<B> and its error is Delta Delta<B>. This identity does not include microscopic controller outputs, absolute work or temporary control-energy load. Reserves remain installed and counted in those separate ledgers.

For even L=2n>=16 the exact middle-gate perturbation has response coefficient at least sqrt(L)/192. The checked finite sums and Taylor remainder give Delta<B>>=sqrt(L)delta/384 for0<delta<=1/(384sqrt(L)). Taking even L>=384^2, epsilon=1/L and delta=epsilon yields vector error<=epsilon with work error>=Delta sqrt(epsilon)/384. For an unhalved trace target epsilon instead, delta=epsilon/2 gives trace error<=epsilon and work error>=Delta sqrt(epsilon)/768. Every other physical premise of the specified pulse family remains enforced.

The witness shows that a reservoir-size-independent mean-energy coefficient cannot be inferred from this preparation's small integrated/full-output error. It supports the square-root-L growth of the worst-case linear mean coefficient for this circuit. It does not prove necessity of every per-angle, raw-second or variance allocation, and does not exclude known signed compensation, other schedules, different resources, feedback or conserving error classes. Runtime charge-conservation bounds do not apply backward through a number-changing preparation suffix without a new argument.

## Evidence and limits

Root read the complete proposal and exposed review, checked the reverse hybrid, exact distribution, physical carrier derivative, mean/variance and full-F0 expansion, finite lower-witness arithmetic and its trace convention. The check is same-selected-model and source-exposed; the reviewer had prior preparation/integration exposure. It is not blind or empirical replication. No scientific computation, old fixture replay or formal verification was needed or performed for this result. Captured metadata verifies source identities and complete packet membership only.

An exact-in-form diagonal phase error preserves B moments but can still spoil the coherent output. Reserve, timing, carrier, vacuum, isolation, controller coupling and generic local faults need separate budgets. No native source, autonomous preparation/release/halt, microscopic work storage or indefinite reuse is established. Any change to this fault class, input domain, observable or necessity quantifier reopens the proof obligation. No canonical acceptance, publication, audit verdict or editable prompt/axiom change is implied by this source decision.


Publication scope remains conditional support under the premises and verification limits above; retained status requires the independent audit path.
