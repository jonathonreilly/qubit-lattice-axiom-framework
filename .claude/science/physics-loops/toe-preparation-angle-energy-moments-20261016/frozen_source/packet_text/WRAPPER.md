---
claim_id: preparation_angle_energy_moments_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
canonical_parent_binding_complete: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Preparation-angle errors and energy moments: bounded conditional theorem

Claim type: bounded_theorem. Current surface: source-only conditional support, with canonical integration and independent audit pending.

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

The root accepted the proposal after a same-selected-model, source-exposed analytical review with prior preparation/integration exposure. This was not blind replication, formal verification or an empirical calibration. No scientific computation or fixture replay was performed for the result or this packaging task. The proposed primary verifies byte identities, source membership, receipt linkage and scope fields only; invoking its canonical entry point refuses while unbound.

The original proposal's pending status and the exposed review's pending root disposition remain historical records. Root acceptance `d32049fc5fe1f8ec166d333ace01e5b1738991e51773eebb5085eeff172ecec4` and the final controlling qualifications below supersede those statuses for the source mathematics only. The first root metadata recorder failed on the review seal filename; its exit 1 source and full streams remain beside the successful distinct v2 exit 0 record. Neither supplies a verdict on this new wrapper or primary.

Vacuum, isolation, exact gap, phase-locked quadratures, timing and external control remain supplied. Diagonal phase errors can preserve B moments while damaging the coherent output. Generic faults, native sources, autonomous preparation/release/halt, microscopic work storage and indefinite reuse remain outside the theorem. New wrapper/source review, Git base, canonical parent binding and review, canonical primary execution, publication and retained audit are unset. Formal retained status requires the independent audit path.

## Preserved complete mathematical record

The following three bodies are verbatim. Read the final controlling qualifications together with the original and the exposed review.
