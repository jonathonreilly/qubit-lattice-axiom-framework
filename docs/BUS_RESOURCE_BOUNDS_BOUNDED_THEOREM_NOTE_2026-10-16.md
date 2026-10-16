---
title: Conditional bus duration and precision bounds for fixed plants and shrinking admissible bias
claim_id: bus_resource_bounds_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
conditional_surface_status: fixed finite data and graph, supplied controls and certified numerical access
status: proposed_retained
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
upstream_dependencies:
  - strongly_regular_bus_bounded_theorem_note_2026-10-15
  - accuracy_scaled_compiler_bounded_theorem_note_2026-10-15
  - positive_bias_suppliers_bounded_theorem_note_2026-10-16
  - bus_installed_preparation_bounded_theorem_note_2026-10-16
runner: scripts/bus_resource_bounds_2026_10_16.py
next_trace_action: independent retained audit; current source remains conditional-support
---

Claim type: bounded_theorem.

This canonical packet packages three accepted conditional conclusions. A fixed complete strong plant and fixed routed bus admit an explicit nominal duration and numerical precision prescription. Its duration exponent survives the separately supplied bounded-slew preparation with evolved memory. A different theorem makes the autonomous runtime uniform along a supplied shrinking admissible bias. The shrinking-bias theorem does not establish preparation before that runtime or memory recovery afterward. All three keep the literal old Hamiltonian and every old/controller/reference output.

The main source acceptances are fixed-plant d02d9205f451d73da584581970ff333ffd6d87a53a695c1e1b992db9ec615edd, preparation/resource a522894a6c0817ce3f7ea63fa10bae4f250d119ad908fb0d16e67376f19a0c6d, and shrinking-bias aba5f356e130166caf0884c9693152c13fd826b8ebd74b137445028e29ab435d. Their complete controlling qualifications and accepted arguments are copied unchanged below. Historical pending statements in those bodies remain historical; later acceptance controls their scoped use. Those mathematical acceptances do not themselves approve the wrapper/code, a canonical binding, a publication or retained status. The separate source-wrapper/code review is SHA256 c24d1edf46634d1de6dd5507e29e279a98e9632dff3893aebf5d805e6eff82d9. The primary inspects provenance only and requires separately captured canonical review and base evidence.

## 1. Dependencies and exact conditional domain

The external mathematical sources are the [qualified strongly regular bus theorem](STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md), the coefficient-extraction grid in the [accuracy-scaled compiler](ACCURACY_SCALED_COMPILER_BOUNDED_THEOREM_NOTE_2026-10-15.md), and the qualified transfer/positive-direction scope of [positive bias suppliers](POSITIVE_BIAS_SUPPLIERS_BOUNDED_THEOREM_NOTE_2026-10-16.md). PARENT_BINDING.json records their exact source identities and the passages actually used. The first source is bus1733b296; the second is c0332b37. No claim is imported because it happens to be a Git ancestor. The joint-energy publication is not a mathematical parent of these duration theorems.

Two accepted source refinements are necessary and are reproduced in the immutable supporting archive: the reachable-envelope corrector d83e5d3c and quantitative bias selection 810d46f2. Their complete proofs, exposed checks and controlling qualifications are available through ARCHIVE_INDEX.json. They are not new external canonical nodes. The preparation composition also requires the original installed-preparation acceptance28bef194 and evolved-memory slew acceptance b237e655. Exact arguments, qualifications and actual relevant historical evidence are archived directly. The [installed preparation theorem](BUS_INSTALLED_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-16.md) is now actually published as PR9640 at commit d0421bc43e396592aa5c66e2858138b1fb02f808, with canonical note SHA256 0c6b10f903352ff152cc920499f01c624a6407ea0e02c907a2b8b30c4ef81823. Its actual publication/attachment and selected publication-phase receipt/streams are captured. Earlier pending draft fields remain unchanged in source records; ACTUAL_BINDING.json separately records the actual resource integration Git base.

Fix the complete finite old dimension d>=2, local port B, nearest-neighbor geometry, finite window, physical time unit and stated target bounds. The fixed-plant theorem assumes a simple complete old spectrum, distinct positive gaps and every energy-basis off-diagonal B entry nonzero, plus certified fixed positive cone boxes, routing and calibration data. Its constants need not be uniform over different strong plants. If a fixed bias has already been included in the declared plant, the fixed-plant flow refers to that entire declared Hamiltonian; this does not remove a continuing bias from an otherwise unbiased target.

For shrinking bias, supply computable full H,C,B,W and decomposition/reserve data, norm bounds, a positive rational a0<=p_C for the complex Krylov Gram, and actual permission to add and attenuate the stated positive onsite/occupied-edge bias blocks. Computable names are necessary for an effective procedure; norms alone are insufficient. The fixed positive-chain construction is one separately qualified supplier on its occupied-path access domain. Lie controllability or one accessible port does not supply those additions, the strong direction, a Hamiltonian path, vacant exterior geometry or isolation. No padding conclusion is newly imported.

No physical axiom or primitive is added. Native purity, phase references, control hardware, timing, calibration, isolation and storage remain supplied conditions or unresolved physical tasks. A bit request is not a physical supplier and does not bound an arbitrary computable oracle's response time.

## 2. Corrector and selection qualifications that govern every resource bound

Use H1 subset H2 reducing the unperturbed generator, with VJ in H1, VH1 in H2 and A2J in H2. Only the Q/P separation on H2 and the classified nonzero P/P divisors are needed. The corrector equations, residuals R3/R4, V and A2 bounds remain full-space. Perturbed dynamics need not preserve H2. In particular the inverse is inclusion_g1(c+L restricted to g1)^(-1)projection_g1 on the one-action reducing source envelope, not a possibly undefined full-source inverse. The one-hole representation computes its actual reached coefficient and retains all symmetric excitation sectors.

The quantitative bias rule uses the accepted upper-half nodes lambda_j=Lambda[1/2+j/(2(D+1))], D=d(d-1)[d(d-1)+1], and A_D=[4(D+1)]^D/D!. For L=a0 Lambda^D/A_D, evaluations have absolute error <=L/8 and the strict rule is p_hat-L/8>L/2. It supplies a selected point in [Lambda/2,Lambda), with transition/gap/separation lower bounds proportional to Lambda^(D/2). The older proposal's interior grid is not mixed into this rule. No leading-term-dominance, equality oracle, or claim at every small bias is used.

Both refinements have limited historical finite corroboration. Those checks are not new runs here and do not prove the resource asymptotics. The restricted-inverse example permits an exterior pole, not deletion of a reached resonance. The quantitative two-level check discriminates adjoint/grid/factor errors, not every higher-dimensional physical premise.

## 3. Fixed-plant duration and preparation composition

Put q=d(d-1)/2, n=N+1, a=2q+6, k=3q+1, r=ak and p=q+3r+2a=18q^2+65q+30. Fixed certified constants give N=O(epsilon^-2), xi=c epsilon n^(-p), T=t_*/xi^2 and

    T=O(epsilon^[-(72q^2+260q+122)]).

For q=1 this sufficient exponent is454. The routed graph is fixed while source length grows. The tree cofactor supplies |G_l|>=c_G n^(-r); dimension and a gap alone would not supply that response lower bound. Full A2=O(n^(2r+a)), endpoint correctors and separate xi R3/xi^2 R4 terms are paid before selecting T. Actual incident norms have one accuracy-independent cap. Global norm/reserve bounds are O(n) and second-moment bounds O(n^2), not bounded total energy.

The evolved-memory preparation supplies positive complementary controls and an accessible disjoint nearest-neighbor matching into fresh independent vacuum memory, isolated with zero storage drift. Arbitrary correlations of the original old/controller/reference input are retained in that memory. It fixes its modeled ramp/gate durations using that same uniform incident cap. Its constant total duration tau and a smaller fixed prefactor c pay e_rel=epsilon/(24 B_beta^2 n^2), because p-r>=2 and 2p-2r-a>=2. Joint readiness and full integrated generator error supply the remaining preparation allowances. The complete comparator retains U_E, the actual preparation scalar Phi, every memory output and old flow

    exp(-isH) W exp[-i(T+tau)H].

It does not satisfy the older literal-Q memory contract, furnish an inverse U_E or reset consumed memory. Gate axes include +omega alpha_off. Runtime source phases include +omega T without an extra +omega tau. T, source/gate phases and actual reserve scalars are recomputed after the final c choice. Upper norm bounds never replace actual scalars in an amplitude comparator.

Centered release mean/second-moment errors are <=epsilon/24 and variance error <=epsilon/8 in fixed declared energy units, relative to the ideal released Omega with the tau-aged old marginal and the actually installed K. The full off-code square is retained. E-valued moment operators remain conjugated by U_E. These are release allowances, not a theorem that arbitrary target moments at runtime have error epsilon. The direct internal trace budget is11epsilon/12. A rational-target repair needs its separate allocation; internal epsilon/2 and ||M-L||<=epsilon/4 give23epsilon/24, and its moments concern the M-dependent installation.

Preparation term, phase-axis and independent product-memory requests can be O(epsilon n^-3); correlated readiness needs the joint condition directly. All formerly looser timing/phase/implementation budgets must actually be tightened. Modeled incident strength2J_*+g and slew S_* are fixed, but physical amplitude/derivative certificates are additional requirements. Reserving half an amplitude ceiling requires it already to be at least2(2J_*+g); decreasing xi cannot remove the fixed base strength. Integrated norm error does not certify pointwise slew or hard bandwidth. The total nominal duration tau+T has the same sufficient exponent.

## 4. Shrinking-bias uniform runtime is a distinct theorem

Let Lambda=lambda0 epsilon, kappa=q(2q+1) and zeta=c_z Lambda^kappa<=1. For m=2(d-1), put tau_h=4m^2-10m+10, g=tau_h(m-1)+6k, u=g+2 and v=3u+8. The uniform cone uses pole offsets proportional to zeta^4, positive weights bounded below by a constant times zeta^2, and routing rho=rho0 zeta^6 n^(-a). Fixed-node Jacobi weight derivatives are O(zeta^-2); moving nodes are outside that derivative statement. Determinant bounds separately pay arithmetic conditioning and positive hopping margins.

The complete bounds include D=O(zeta^-4), V=O(zeta^-u n^r), full A2=O(zeta^[-(2u+4)]n^(2r+a)), R3=O(zeta^[-(3u+8)]n^p) and R4=O(zeta^[-(4u+12)]n^(q+4r+3a)). Taking xi=c_xi epsilon zeta^v n^(-p) yields

    T=O(epsilon^-P),  P=2+4p+2 kappa v.

At d=2 the sufficient exponent is1078. This conditionally discharges the earlier fixed-plant equation36 uniformity obligation; it does not turn the earlier pointwise proof into a uniform one by assertion. No favorable complexity in old qubit count, practical efficiency or total compiler wall time is claimed.

Select the entire uniform design and T before the rational Hermitian target. Then approximate U_T=exp(iT H_lambda)Wexp(-iTH) by exp(-iM), with exact rational M, ||M||<4 and strict certified margins. Do not differentiate a logarithm branch or the discrete selection, or recompute T from smaller later constants. In this interaction-frame convention the source phase realizes M directly; adding the inherited +omega T factor would double-count a conjugation. At t=T+s the actual scalar is

    chi(t)=R_total t+c_M xi^2 t+lambda c_C s.

There is no additional lambda c_C T. Bias reserves act for all T+s in R_total; only the continuing nonscalar window cost is paid by lambda w||C-c_C I||. No lambda T smallness is assumed. The old target remains exp(-isH)Wexp(-iTH), with all freely rotating sources, bus outputs and arbitrary references retained.

Initial readiness and long-time full-generator calibration remain supplied. Chronological preparation would add biased old aging, its memory and phase contract and corresponding budgets. The fixed-plant preparation result does not establish that composition for this shrinking family. No shrinking-bias preparation, recovery, autonomous scheduling, halt or reuse is claimed here.

## 5. Effective requests, historical evidence and publication boundary

The shrinking-bias input requests are proportional to epsilon^3 zeta^(9u+40)n^[-(2p+3r+2a+1)] in a certified old-energy chart, with one more zeta factor for original matrix data. One-hole entry rounding divides operator allowances by its dimension; its normalized quadratic form may use the exact factor N/(N-1). Rational inverse evaluation, positive moment minors and source-coordinate guard bits pay internal conditioning. Strict rational majorants/minorants and finite witness margins avoid computable-real ceiling/equality shortcuts. No arbitrary over-small chosen xi is called a proof of the displayed sufficient power.

All source amplitudes, positive blocks and actual scalar reserves are included; literal H is not physically rounded, canceled or slowed. The source coefficient request, phase/timing request, internal arithmetic request, nominal experimental duration and oracle/design time are separate budgets. Their meaning remains conditional even when requested bit counts are polynomial or logarithmic.

The exact growing-path example with fixed gap but response at most2^-N N^[-(N-1)] excludes an inference from dimension/gap alone. The continuing fixed nonscalar-bias window example excludes endpoint recalibration as a solution to that specific holding error. Neither is a broad physical no-go or a no-go PASS. Historical failures, interruptions and pending fields remain in their unchanged source records. The accepted main resource results are analytical, with zero new scientific executions; historical parent finite programs are archived with original launch/execution evidence, not replayed.

SOURCE_MANIFEST.json, BODY_MAP.json, ACTUAL_EVIDENCE.json and ARCHIVE_INDEX.json distinguish exact inputs, unchanged bodies, immediate freezes and full actual selected process receipts/streams. This is a nonrecursive selected source closure. Read coverage and same-model/source-exposure limits are explicit; source acceptance and metadata integrity are not independent retained audit. The actual preparation parent is bound. Original source records retain their null resource base/root-wrapper-review/canonical-publication fields. ACTUAL_BINDING.json and its separate review receipts record the later canonical evidence; publication and retained audit remain separate. No new physical supplier, measured-energy identification, global-energy improvement or retained status follows from this package.

## Immutable accepted arguments and controlling qualifications

The following bodies retain their original bytes and historical statuses. Supporting-parent arguments and qualifications are in the immutable archive with exact original-path mappings.


<!-- Immutable source: reachable_bus_resource_candidate/DERIVATION.md -->

# Conditional resource bound for a fixed strong plant and a fixed routed bus

Status: exposed source proposal, not an acceptance, publication or retained audit. This is a continuation by the same model and the earlier bus/transfer author. It uses the root-qualified reachable-envelope replacement, including its mandatory restricted source inverse. The parent proof is reused at its pinned identity, not claimed to have received a fresh independent review here. Source identities and read coverage are in SOURCE_MANIFEST.json; the complete dependency ledger was recorded in LEDGER.md before this derivation. No scientific program was executed for this task.

## 1. Result and exact scope

For one fixed finite old plant H on d>=2 levels, a fixed accessible one-qubit Hermitian port B, a fixed target logarithm L, time unit t_*>0 and finite observation window w>=0, the accepted bus construction with the accepted reachable-envelope replacement has the following **conditional quantitative refinement**. Assume the parent's strong spectral hypotheses, supplied vacant geometry, fixed positive-width cone-valid parameter boxes and computable strict fixed-data certificates. Controller preparation, timing, coefficients and isolation retain their parent's explicitly supplied status. For an effective prescription take epsilon to be a supplied positive rational; a smaller rational within a fixed factor of any other requested positive tolerance changes only constants. Every old H term stays literal. Let

    q=d(d-1)/2,  m=2(d-1),  b=m+4q,
    a=2q+6,  k=3q+1,  r=ak,
    p=q+3r+2a=18q^2+65q+30.

There are fixed, certified finite constants C_N,C_T,J_* independent of 0<epsilon<=1 for which the finite positive nearest-neighbor controller can be selected with

    N=O(epsilon^-2),  added sites=b+qN,
    T <= C_T epsilon^[-(72q^2+260q+122)],             (1)

and added incident strength at most J_*. Its nominal all-output isometry, including arbitrary old/reference inputs, approximates the parent's actual-time target

    exp(-isH) W exp(-iTH),  0<=s<=w,                (2)

with the explicit controller and scalar comparator below. The entire stipulated epsilon budget, including supplied preparation and full-generator implementation tolerances, can be met. For q=1 the sufficient power in (1) is454. This is a conservative power, not an optimum or a practical efficiency claim.

Finite absolute data-precision requests and exact source-representation arithmetic bit sizes can also be bounded by polynomials in 1/epsilon. The physical input and local coefficient requests given below need only O(log(1/epsilon)) bits for fixed certified data; an explicit conservative allowance for badly conditioned intermediate source coordinates is polynomial in N. These are requests and finite arithmetic bounds, **not a wall-clock bound for arbitrary computable-data oracles**, a preparation protocol, or an efficient full compiler theorem.

The result is pointwise in the fixed strong plant. It does not establish the same power with a uniform constant for shrinking H+sC, nor for T-dependent targets without the separately stated uniform target certificate. It does not cover a bus graph growing with N. These distinctions matter mathematically, not merely terminologically.

All powers are in dimensionless N and epsilon. Constants carry the energy/time units dictated by the displayed expressions. When bounding a numerical magnitude by1, use any fixed declared energy/time units for representation; no physical rescaling of H is performed.

## 2. Fixed certificates and a uniform calibration neighborhood

Order the supplied simple old energies E_0<...<E_(d-1). Every positive gap omega_l is distinct, and every off-diagonal B_ab is nonzero. Fix certified positive lower bounds beta_0<=min_(a!=b)|B_ab| and gamma_PP for the nonzero second-order P/P differences classified in the parent. They include E_a-E_b, omega_l-omega_l', and E_a-E_b +/- omega_l when nonzero. No arbitrary integer relation among all code energies is classified or needed.

The parent pole-cone construction provides m disjoint positive intervals for mu_j, avoiding every old Bohr difference, and a positive solution

    w=(F_+^-1 y,0)+lambda c_weight,
    y_a=(L_aa-L_00)/t_*.

Select a closed rational Cartesian box strictly inside those intervals, together with fixed high router-field and positive ferromagnetic intervals for nu and J_F. All side lengths are at least a certified w_0>0. A single lambda gives uniformly positive weights on the box. Choose a common radius r_x>0 for the positive-side weight ball, small enough to retain uniform lower bounds on every weight and S=sum w_j, and uniform upper bounds. This can be done before N because the parent construction explicitly proves uniform positivity on a compact smaller box. Merely saying that a point is interior would not give a quantitative box; the box and strict bounds are required certified data here.

This choice can cover the rational target approximations used later. For ||L||<=L_max, ||y||<=2sqrt(d-1)L_max/t_*. If A_max bounds ||F_+^-1|| and c_min is a uniform positive lower bound for every component of c_weight, choose lambda with lambda c_min>=A_max(2sqrt(d-1)L_max/t_*)+w_min+2r_x. This gives the same positive-weight neighborhood for that whole bounded target class; finite upper weight bounds follow from the same formula. No support-dependent denominator in L is needed for calibration.

The core Gram formulas give uniform finite derivative bounds. In particular set p_j=w_j/S and require p_j>=p_0>0, |mu_j-mu_i|>=delta_mu>0, and |mu_j|<=M_0 with M_0>=1 in the fixed energy unit. Let D_j be the j-by-j Gram determinant of1,x,...,x^(j-1), D_0=1. Cauchy-Binet and Hadamard give, for1<=j<=m,

    d_j:=p_0^j delta_mu^[j(j-1)] <= D_j
       <= u_j:=M_0^[j(j-1)],                    (3)
    d_0=u_0=1.

Keeping just one j-support Vandermonde minor proves the lower bound; the product of the diagonal moments proves the upper bound. The adjacent Jacobi hopping is

    t_j=sqrt(D_(j+1)D_(j-1))/D_j
       >=sqrt(d_(j+1)d_(j-1))/u_j,
    t_core:=min_(1<=j<m) sqrt(d_(j+1)d_(j-1))/u_j>0. (4)

The same determinant lower bounds control all derivatives of the finitely many Gram expressions on this fixed ball. Thus the parent's M_J,C_0,C_1, ||F_+^-1||, S_max, v_min<=sqrt(S), and delta_C=min|mu_j-z| over old differences z admit fixed certified bounds. Router field separation gives a fixed Delta_R>0 for nu-3rho-omega_max. Fixed high derivatives needed to bound calibration sensitivity can be bounded by further differentiation of these same finite rational/square-root formulas with their positive denominators. Their sizes may be extremely unfavorable, but they do not depend on N.

Take a fixed positive preliminary routing cap rho_cap such that all of

    3rho_cap<mu_min/2,
    e_cap=rho_cap^2/Delta_R<=delta_C/2,
    ||F_+^-1|| C_0 e_cap<=r_x/2,
    ||F_+^-1|| C_1 e_cap<=1/2                     (5)

hold uniformly on the box, with the router-field bound also enforced. The parent's exact calibration is the unique fixed point of its contraction with constant at most1/2. The parameters vary over a fixed compact domain, so (3)-(5) give a uniform majorant for that map's parameter derivatives. Consequently perturbing its fixed inputs by eta perturbs the fixed point by at most a fixed constant times eta: compare the two fixed-point equations and absorb the contraction term. This proves the fixed calibration Lipschitz bound used later. It is not inferred from polynomial matrix dimension.

## 3. Polynomial restricted gap and a finite grid with margin

Put n=N+1, N>=2. The accepted source envelopes G_j are the spans of at-most-j-site operator actions on the tensor symmetric source code. They reduce source number, adjacent permutations and independent global source SU(2). The actual branched bus reduces its at-most-j-excitation space B_j. Therefore

    H_j=old tensor B_j tensor G_j,  j=1,2,
    D_c=d n^q,
    dim H_2 <= d B_2 n^q [1+4qN+16 binom(qN,2)],
    B_2=1+b+binom(b,2).                           (6)

These are the reducing envelopes from the accepted replacement. They contain VJ, VH_1 and A2J in the required order. Perturbed evolution is not required to stay in H_2. Let

    C_M=d^2 B_2(1+4q+8q^2),
    M_N=C_M n^(2q+2).                            (7)

This upper-bounds the number of Q/P energy-difference forms between H_2 intersect Q and the complete code. At zero routing such a form is

    f=sum_(j in S)mu_j+r_R nu+J_F alpha
       +(E_b-E_c)+sum_l omega_l z_l.              (8)

Here |S|+r_R<=2, alpha is an eigenvalue of the unit-scale source Laplacian on the reducing envelope, 0<=alpha<=2q(N-1), and |z_l|<=N. A Q vector has bus excitation or alpha>0. The accepted adjacent-permutation argument gives

    L_unit >= ell^-2(I-P_sym), ell=N(N-1)/2,
    min(1,ell^-2)>=n^-4.

Thus some freely variable coefficient in each relevant form (8) has magnitude at least n^-4. The slab-volume calculation now gives, with

    d_0=w_0/(8C_M),
    Delta_N=d_0 n^-a,  a=2q+6,                  (9)

a point where all Q/P differences exceed2Delta_N in absolute value: the union of the closed slabs |f|<=2Delta_N occupies at most half the box. P/P pairs are not included in that slab argument.

There is also a bounded finite-grid prescription, stronger than an unquantified dovetail. The infinity-norm Lipschitz constant in the m+2 freely variable coordinates is at most

    L_N=2+2q(N-1).

Choose a rational Cartesian mesh of maximum spacing Delta_N/(4L_N), including the endpoints of the box. A nearest grid point to the strict witness still has all differences greater than7Delta_N/4. At every grid point compute spectral enclosures whose error in a Q/P difference is at mostDelta_N/4, and accept only a certified lower bound greater thanDelta_N. A witnessing grid point passes; ties or undecidable equalities at other points cannot block a finite scan. There are at most O(n^[(a+1)(m+2)]) grid points, since m+2 is fixed. This counts candidate points, not oracle wall-clock time.

For example individual old-energy errors eta_E perturb the offset in (8) by at most (2+2qN)eta_E when omega_l is formed from the same old energies. Requested eta_E=O(Delta_N/n) suffices. The purely source eigenvalues can be enclosed to O(Delta_N) using the exact reduced matrices described in section10. The source forms use the complete reducing envelope, including internal degeneracies. No exact equality test on arbitrary computable plant entries is introduced.

Select a fixed positive rational rho_0 so small that rho_0<=rho_cap and R rho_0<=d_0/4, where R=4q is the exact number of routing edges. Prescribe

    rho_N=rho_0 n^-a.                            (10)

This is both an upper and a lower quantitative prescription. It is not the unspecified output of a potentially excessive small-parameter search. The complete many-qubit routing perturbation has norm <=R rho_N. Restricting cannot increase that norm. The calibrated bus therefore retains restricted Q/P separation

    delta_N >= c_delta n^-a,  c_delta=d_0/2.       (11)

The zero-route spectrum is independent of the positive calibrated weights, so (11) survives the exact contraction adjustment. Only the open core at rho=0 is treated by its path free-fermion identity; the branched bus at rho>0 is never assigned a free-fermion spectrum.

## 4. Lower bounds for every routed response

The actual geometry is fixed: m core vertices, a3q-vertex backbone, and q leaves. The path from the old-adjacent core root to leaf l crosses m-1 core edges and3l+1 routing edges. Its number of vertices is m+3l+1. All off-path vertices, numbering4q-3l-1, belong to high-energy router subtrees. There are no off-path core vertices.

For G_l=[(B_bus-omega_l I)^-1]_(1,u_l), the exact tree cofactor identity gives the product of the path hoppings times all off-path determinants, divided by the full determinant, up to an irrelevant real sign. Every off-path eigenvalue is at leastDelta_R above omega_l. Let a fixed C_det>=||B_bus||+omega_max bound the full determinant's spectral factors. Equations(4) and(10) then imply

    |G_l| >= g_l n^[-a(3l+1)],
    g_l=t_core^(m-1) rho_0^(3l+1)
           Delta_R^(4q-3l-1)/C_det^b>0.

In particular, with k=3q+1, r=ak and g_0=min_l g_l,

    min_l |G_l| >= g_0 n^-r.                     (12)

For l=q the off-path count is q-1, including the earlier leaves; for q=1 it is zero. These counts include the initial core/backbone attachment and the final leaf edge.

The full one-particle resolvent at any old difference also has a fixed upper bound C_R. This follows from the router Schur inverse with ||R_router||<=Delta_R^-1 and ||R_core,corrected||<=2/delta_C: its block inverse has norm at most (1+rho_cap/Delta_R)^2(2/delta_C)+Delta_R^-1, enlarged if necessary. Equation(12) is a lower bound for a specific inverse entry, which does not follow from this upper operator-norm bound alone.

Cancellation has been excluded using the actual unique path and the high-energy off-path determinants. An arbitrary interior Jacobi response, a graph with multiple paths, or an N-dependent route length does not inherit (12). Section12 gives an exact discriminator for the latter issue.

## 5. Source amplitudes, the restricted inverse and full counterterms

The exact amplitude formula is

    r_l=2|L_ab|/(t_* v_p |B_ab G_l|)

for the pair matching l, including r_l=0 if L_ab=0. Hence fixed constants C_r,C_V give

    r_l<=C_r n^r,
    ||V||<=v_p||B||+sum_l r_l<=C_V n^r.           (13)

There are q source/leaf couplings and one old port coupling, so no extra factor N belongs in (13).

The source self-energy coefficients are A_l and B_l of the parent, with the mandatory inverse replacement from the accepted reachable proof. In detail, for c=lambda-omega_l use

    T_c=inclusion_g1 (c+L restricted to g1)^-1 projection_g1,

where g1 is the one-source one-action reducing envelope. The restricted Q/P gap makes this inverse exist, by the accepted complete-SU(2)-multiplet comparison. It commutes with the ladder, equals1/c on the symmetric sector, and produces exactly the parent's quadratic self-energy on the symmetric source. A full-source inverse may fail and is neither used nor asserted.

There is a convenient numerically stable joint formula avoiding individual one-particle eigenvectors. The complete one-hole sector lies in g1 and has dimension N. In its standard hole-position basis, L_hole is the open-path graph Laplacian, ||L_hole||<=4. Set

    eta_N=sqrt[N/(N-1)](e_1-N^-1 ones), ||eta_N||=1,
    U_l=B_bus tensor I_N+I_b tensor J_F L_hole-omega_l I.

Every denominator in U_l is among the reached source/bus comparisons, so ||U_l^-1||<=delta_N^-1. The exact formulas are

    A_l=-r_l^2 <u_l|(B_bus-omega_l)^-1|u_l>,
    B_l=-r_l^2 <u_l tensor eta_N|U_l^-1|u_l tensor eta_N>.

The normalization of eta_N is the factor N/(N-1) in the parent's highest-weight coefficient. Therefore

    |A_l|<=C_r^2 C_R n^(2r),
    |B_l|<=C_r^2 c_delta^-1 n^(2r+a).             (14)

Install the actual counterterm coefficients

    u_l=-A_l/N,  v_l=-(B_l-A_l)/N.

Their unreserved **full-space** operator A2 is the sum of N onsite terms and N-1 adjacent pair terms per source. Consequently

    ||A2||<=sum_l[N|u_l|+(N-1)|v_l|]
          <=sum_l(2|A_l|+|B_l|)<=C_A n^(2r+a),   (15)
    ell_2=max_l(|u_l|+2|v_l|)<=C_loc n^(2r+a-1). (16)

The inequality1/N<=2/n was used in(16). No projection of A2 is substituted for its full norm. A2J can leave H_1; its leakage into H_2 is part of the accepted corrector. Positive reserve blocks are accounted for in section8.

## 6. Full corrector bounds, with powers kept separate

The accepted replacement supplies full-space identities for Z1,Z2, although the Sylvester inverse is only needed on the reducing envelope. With D_c=d n^q, gamma_PP fixed, and(11),(13),(15), the parent's Frobenius estimates give

    ||Z1||<=C_1 n^x,  x=q/2+r+a,
    d_bound=||V|| bound * ||Z1|| bound + ||A2|| bound
             <=C_d n^(q/2+2r+a),
    ||Z2||<=C_2 n^y,  y=q+2r+2a,                (17)
    C_1=sqrt(d) C_V/c_delta,
    C_d=C_V C_1+C_A,
    C_2=sqrt(d) C_d(c_delta^-1+2/gamma_PP).

For residual estimates we can improve on using the coarse d_bound for D. The exactly canceled and calibrated secular D equals c_old I, the diagonal L_aa/t_*, and the finite sum of resonant old-pair/source terms. Their coefficients satisfy |kappa_ab|=2|L_ab|/t_* exactly. Since ||S_-/N||<= (N+1)/(2N)<=3/4, a uniform bound is

    ||D||<=D_0,
    D_0=S_max||B||^2 C_R+2||L||/t_*
               +(3/(2t_*))sum_(a>b)|L_ab|.       (18)

The first two terms bound |c_old| plus the target diagonal. There is no inverse G_l remaining in(18).

Use the actual full residuals

    R3=VZ2+A2Z1-Z1D,
    R4=A2Z2-Z2D.

Triangle inequalities, including their actions outside H_2, give

    ||R3||<=C_3 n^p,  p=q+3r+2a,
    ||R4||<=C_4 n^h,  h=q+4r+3a,                (19)
    C_3=C_V C_2+C_A C_1+C_1 D_0,
    C_4=C_A C_2+C_2 D_0.

For example A2Z1 has exponent q/2+3r+2a<=p. No invariance of H_2 under V or K0+xi V+xi^2 A2 is assumed.

The exact two-endpoint Duhamel estimate, for t<=T+w and T=t_*/xi^2, is

    error_corrector <= 2xi||Z1||+2xi^2||Z2||
                     +(t_*+w)(xi||R3||+xi^2||R4||). (20)

It is useful to retain the separate powers in(20); replacing all of them by xi times a common bound loses unnecessary powers of N. Set

    xi=c_xi epsilon n^-p.                        (21)

Because p>=x, 2p>=y and 2p-h=q+2r+a>0, each term in(20) is bounded by its fixed constant times c_xi epsilon or c_xi^2 epsilon^2. Let

    A_corr=2C_1+2C_2+(t_*+w_bar)(C_3+C_4),

where w_bar is a fixed certified upper bound for w. Choose a fixed positive rational c_xi no larger than

    1,
    1/[8(A_corr+1)],
    1/sqrt[8(1+w_bar||L||/t_*)],
    J1/(2C_V+J1),
    sqrt[J2/(C_loc+J2)],                        (22)

with J1=J2=1/t_*, using strict rational lower roundings. Equations(20)-(22) give error_corrector<=epsilon/8, xi^2 w||L||/t_*<=epsilon/8, xi ell_V<=J1 for ell_V=2||V|| bound, and xi^2 ell_2<=J2. The latter follows since2p>2r+a-1. Choosing a certified smaller c_xi does not change its independence from epsilon.

## 7. Closing the accuracy/runtime inequalities in order

Choose a fixed rational C_N>=1 and

    C_N >= [8(t_*+w_bar)B_*]^2,
    B_* >= t_*^-1 max_a sqrt(sum_(b!=a)|L_ab|^2),
    N=max(2,ceil(C_N epsilon^-2)).               (23)

A positive B_* avoids any zero decision. The parent's all-output coherent-source fluctuation is then at mostepsilon/8. The corrector and holding-window errors are each at mostepsilon/8 by section6. Purification and the full-isometry inequality give trace error at most3epsilon/4, with the entire controller and arbitrary passive reference retained. A supplied initial trace error at mostepsilon/8 relative to the controller product and its exact unconditional old/reference marginal, and supplied full-generator error satisfying

    integral_0^(T+w)||E(t)||dt<=epsilon/16         (24)

add epsilon/8 each, for total trace error at mostepsilon.

The order is noncircular: fixed certificates first; N; a finite-grid zero-route choice; prescribed rho_N; exact contraction calibration; amplitudes and one-hole counterterms; the fixed majorants above; xi; T; and finally source phases. Neither the initial source phases nor T changes any coefficient, gap or norm estimate already used.

Since n<= (C_N+4)epsilon^-2,

    T=t_* c_xi^-2 epsilon^-2 n^(2p)
      <=t_* c_xi^-2(C_N+4)^(2p)epsilon^[-(2+4p)]. (25)

Expanding p=q+(2q+6)(9q+5) gives18q^2+65q+30, hence(1). This is a nominal autonomous runtime bound in the unchanged physical time units. It excludes the time taken by a supplied oracle or an unspecified preparation procedure.

For arbitrary computable L without decidable support, use the parent's accepted rational Hermitian approximation M in the supplied old-energy basis. One may run this theorem with internal tolerance epsilon/2 and ||M-L||<=epsilon/4; the unitary discrepancy contributes at mostepsilon/2 in trace norm. All fixed norm majorants may be taken uniformly for ||M||<=||L||+1. The rational support and normalized unit phases are decidable, so the discontinuous exact-L phase selection is avoided. The changed constant epsilon/2 does not change any exponent. This effective repair is separate from fixed exact-L existence with supplied support/phase; no exact-zero oracle is inferred.

## 8. Positive blocks, incidence, total resources and phases

Retain exactly the parent's physical installation:

* fixed onsite reserve R_s on the old port;
* positive bus edge t_e T_e+|t_e|I and positive bus onsite fields;
* source omega_l n and J_F(I-SWAP) blocks;
* positive port xi[v_p B X+v_p||B||I] and source-edge xi r_l[T+I];
* counterterms xi^2[u_l n+max(0,-u_l)I] and xi^2[v_l nn+max(0,-v_l)I].

These include all added one-/two-qubit blocks and all positive reserves. There is one old/new edge. The full unreserved old H is not replaced, canceled or slowed. With the parent's fixed M_E for all base terms,

    J_*=R_s+7M_E+J1+J2                          (26)

is an epsilon-independent added incident cap. It may depend on the complete fixed plant, target and certificates. Actual implementations need the same pointwise local cap or a separately fixed additional slack; the integrated bound(24) alone does not imply a pointwise cap.

The total added sites and edges are b+qN. A fixed normalized local operator dictionary has at most C_terms n coefficients for a fixed C_terms. The full installed generator has ||K||<=C_K n and total reserve magnitude O(n) for fixed data, since each of O(n) local blocks has a fixed incident bound. Total energy/norm/resources are not claimed bounded. The unscaled counterterm sums can be much larger; the factors xi^2 are essential to the installed bound.

In particular the mathematical installed first and second energy moments satisfy |Tr(rho K)|<=C_K n and Tr(rho K^2)<=C_K^2 n^2 for every normalized state. These are operator bounds, not measured-energy identifications or native preparation certificates. Any more specific prepared-state moments and release phases must be recomputed for the selected N, xi and T.

Use the **actual** installed scalar

    R(xi)=R_s+sum_(bus edges)|t_e|
           +xi[v_p||B||+sum_l r_l]
           +xi^2 sum_l[N max(0,-u_l)+(N-1)max(0,-v_l)].

At t=T+s the full comparator is

    exp[-i(R(xi)t+c_old xi^2 t+theta_0)] |0_bus>
      tensor (tensor_l exp(-it omega_l N_l)|Alpha_l(phi_l)>)
      tensor [exp(-isH)W exp(-iTH)],              (27)

where e^-iL=e^-i theta_0 W and

    exp(i phi_l)=(L_ab/|L_ab|)
                (conj(kappa_ab)/|kappa_ab|) exp(i omega_l T)

on supplied nonzero support, with the rational-M alternative above. The zero-coupling phase is arbitrary. Formula(27) retains the entire freely rotating source state and all old scalar phases. The installed reserve is not replaced by an upper majorant in this phase. There is only a finite holding window, no permanent halt, disposal of outputs or reset/reuse conclusion.

## 9. Explicit physical-data precision requests

Take a fixed normalized dictionary for the finitely many types of onsite/edge terms. If every installed dictionary coefficient has absolute error at mosteta_loc, the full norm error is at mostC_terms n eta_loc. Thus it suffices to request

    eta_loc <= epsilon/[16 C_terms n(T+w)].       (28)

Using(25), a fixed small c_loc>0 makes

    eta_loc=c_loc epsilon^3 n^[-(2p+1)]          (29)

sufficient. Positivity-preserving installation uses upward reserve rounding with its errors charged in(28); a fixed pointwise incident slack covers those roundings if needed. Literal old H is not approximated physically by this numerical step. Missing interactions/isolation errors must separately fit the same full-generator budget.

Here is a concrete sufficient request on fixed finite numerical inputs. Treat the supplied old energy-basis data E_a,B_ab,L_ab, t_* and the fixed certificate constants as inputs; eigenbasis extraction from fixed H, if needed, has a fixed conditioning constant under its simple-spectrum certificate. At a selected rational grid point, and within the certified compact neighborhoods of section2, errors eta in these fixed inputs and calibrated one-particle entries cause O(eta) errors in B_bus and v_p. The contraction comparison proves this assertion for its exact calibrated solution. Grid selection itself is discontinuous; this statement applies **after** a certified grid point has been selected, not to a putative differentiable grid-selection map.

The one-particle resolvent identity, with fixed C_R, gives |delta G_l|<=C eta. Require this to be at most half the lower bound(12). The amplitude formula then gives

    |delta r_l| <= C n^(2r) eta.                (30)

The joint one-hole matrix has ||U_l^-1||<=c_delta^-1 n^a and ||delta U_l||<=C eta, since ||L_hole||<=4 independently of N. The resolvent identity gives ||delta U_l^-1||<=C n^(2a)eta once the perturbation is smaller than half the gap. Hence

    |delta A_l|<=C n^(3r)eta,
    |delta B_l|<=C[n^(3r+a)+n^(2r+2a)]eta
                    <=C n^(3r+2a)eta.          (31)

The constants include bounded target and old-port factors. Division by N and multiplication by xi or xi^2 can only improve the conservative estimate that **every installed coefficient** has error at most C n^(3r+2a)eta. The function max(0,-x) used in reserves is1-Lipschitz, so does not introduce a hidden sign-conditioning cost. Therefore the following fixed prescription suffices, after reducing c_in for the finite constants and initial neighborhoods:

    eta_in=c_in epsilon^3 n^[-(2p+3r+2a+1)].     (32)

It implies(29), the source/bus inverse stability conditions, the Green sign certification condition, and the O(n^-a/n) gap-search input accuracy. The corresponding requested absolute bit count can be

    r_in=ceil[C_in+3 log2(1/epsilon)
                        +(2p+3r+2a+1)log2 n].   (33)

Constants C_in,c_in are fixed certified quantities, not uniform over all strong plants. The fixed-point iteration count needed to reach an assigned coefficient tolerance is O(log(1/tolerance)) because the contraction constant is at most1/2. Each step still queries supplied computable quantities, whose actual response time is unbounded by this statement.

Source phase evaluation also needs a long-time allowance. On one product source an error delta_phi changes its vector norm by at most N|delta_phi|; summing q sources gives the conservative qN bound. The factors exp(i omega_l T) therefore require frequency/time-product precision O(epsilon/n). A fixed old-frequency error eta contributes O(T eta), and t_* error contributes O(xi^-2 eta) to T when xi is the selected exact rational. Equation(32) is smaller than a fixed multiple ofepsilon/[n(T+w)] and epsilon xi^2/n, so it covers these requests after a fixed budget subdivision. Computing a unit phase for rational M can avoid an argument branch: use M_ab/|M_ab|, the fixed B_ab unit phase and the certified real sign of G_l. If M is on a dyadic mesh of size O(epsilon), every nonzero |M_ab| is at least a fixed multiple ofepsilon, and any remaining phase normalization requests add only O(log(1/epsilon)) bits. For exact L the support/phase remains a supplied condition unless this repair is used.

Large T has O(log(1/epsilon)) integer bits for fixed q. A separate actual release-time uncertainty Delta_t costs at most2||K|| |Delta_t| in trace norm, so an O(epsilon/n) timing tolerance suffices for a specified allocation. This is a demanded physical timing accuracy, not a supplier of that accuracy. All phase, coefficient and timing sub-budgets can be allocated by replacing16 in(28) with a fixed larger constant; the powers are unchanged.

## 10. Reduced source representation and intermediate arithmetic precision

Polynomial Hilbert-space dimension alone is not a numerical conditioning proof. The accepted binomial-basis refinement gives a specific representation that can be bounded independently of the supplied plant entries. Use unnormalized Dicke vectors and local matrix units. Their Gram entries are integer binomial counts, with absolute value at most2^(qN); the number of candidate labels is at mostC_G n^(q+2), for fixed C_G. Exact rational rank selection chooses an independent subset of size g<=C_G n^(q+2). Its Gram matrix G is positive definite with integer determinant at least1. Thus, with B_G=g 2^(qN),

    lambda_max(G)<=B_G,
    lambda_min(G)>=B_G^[-(g-1)].                 (34)

This may be exponentially poor conditioning, and is explicitly paid. Here is one concrete arithmetic prescription, with no unspecified condition-number oracle. Put H_G=2^(qN), Q=(g H_G)^g and Q'=(g Q)^g. Every Gram minor has absolute value at mostQ, and every nonzero principal minor is a positive integer. In the exact rational factorization G=L D L^T, ratios of principal minors give Q^-1<=D_j<=Q, and the bordered-minor formulas give |L_ij|<=Q. Since L is unit triangular, its inverse entries are cofactors and satisfy |(L^-1)_ij|<=Q'. Let C=L^-T D^-1/2; then C^T G C=I and every entry obeys |C_ij|<=C_max:=Q' Q.

For the unit source Laplacian or source number matrix, let S_ij be its unnormalized matrix elements. Counting its local terms gives |S_ij|<=H_S:=(2qN+1)H_G. Approximate each positive number D_j^-1/2 by a rational within eta_s; carry all subsequent products with the exact rational L^-T and S exactly. The resulting C_tilde satisfies max|C_tilde-C|<=Q' eta_s. If this entry error is eta_C<=1, then

    ||C_tilde^T S C_tilde-C^T S C||
        <=g^3 H_S (2C_max+1) eta_C.

Thus eta_s<=tau/[4 g^3 H_S (2C_max+1)Q'] is sufficient for operator error at mosttau, with slack. It suffices to enclose those square roots to the following explicit absolute bit request, for0<tau<=1:

    B_N=qN+ceil(log2(g+1))+ceil(log2(2qN+1))+2,
    P_N=32(g+1)^2 B_N,
    internal bits=P_N+ceil(log2(1/tau))+20.       (35)

Indeed log2 Q<=g B_N, log2 Q'<=g log2(g)+(g^2)B_N, and the logarithm of the denominator in the preceding eta_s bound is below P_N+20. All pivot rational encodings have polynomial bit length by the same minor bounds. Rational square-root bisection needs no extra supplied oracle. The exact rational output matrix can be used directly for certified spectral enclosures, paying its proved operator error. The bound is polynomial, O(n^(2q+5)), and is not optimal. It is an additional precision request on algebraic arithmetic, distinct from(33).

The reduced unit Laplacian and number matrices are assembled from exact integer/rational actions on the labels; swaps permute those labels, and number acts by the known grading. They can therefore be converted to certified orthonormal coordinates to operator error tau with(35). Alternatively one can use exact generalized characteristic polynomials and rational root isolation separately in each number block; internal repeated roots are handled by exact polynomial gcds, not by oracle equality tests. The source operator is constructed before combining the numerical old data. Its physical operator norm is O(n), so errors in scalar old/frequency coefficients amplify by O(n), not by the exponentially bad coordinate condition number. This ordering justifies the separate external-data request(33).

For the finite grid, take tau a fixed small multiple ofDelta_N/n, refine finite spectral enclosures until their certified difference error is at mostDelta_N/4, and use the strict acceptance margin of section3. Since the exact rational source matrices have degree and coefficient bit sizes polynomial in N, their algebraic enclosures can be requested to this polynomial/logarithmic precision without exponentially many physical source vectors. This supplies a finite numerical prescription and polynomial bit bounds. It does not certify a practical implementation or a polynomial wall-clock bound for the arbitrary old-data oracles, the fixed cone-certificate discovery, or physical preparation.

The corrector matrices need not be numerically assembled to choose xi: equations(17)-(22) are certified upper bounds. If they are assembled for a finite case, the restricted Sylvester separation and classified P/P divisors must be used; a full-source inverse or an exact full-F degeneracy oracle is still forbidden.

## 11. Shrinking static bias: the exact remaining uniformity obligation

The accepted quantitative positive-bias selection gives, at selected H+sC points with0<s<=Lambda, explicit lower bounds on old transition magnitudes, nonzero gaps and signed-gap separation of the form constant timesLambda^(D_bias/2), with fixed finite D_bias. It also gives requested input precision. It does not itself bound every subsequent bus-design constant.

This note gives T<=C(H+sC,L,certificates)epsilon^[-(72q^2+260q+122)] pointwise. To set Lambda=O(epsilon) and conclude a polynomial family bound one must additionally prove, for a consistent selected family and bounded target logarithms, inverse-polynomial lower bounds in Lambda on

    w_0, delta_C, delta_mu, p_0, t_core, v_min,
    rho_0, g_0, gamma_PP, beta_0, c_xi,

and polynomial upper bounds on the fixed calibration derivatives, resolvent/Gram constants, weight majorants, target-uniform cone lambda and every constant entering(22). Some of these follow from others; this is a sufficient dependency package, not a claim that they are independent. The precise unresolved inequality is

    C_T(Lambda)=t_* c_xi(Lambda)^-2
                    [C_N(Lambda)+4]^(2p)
                <= C Lambda^-z                 (36)

for fixed finite C,z with the chosen family and uniform target certificate. The old determinant/gap bounds supply only part of that package; no derivation of all its remaining terms is made here. In particular a T-dependent transfer logarithm needs uniform bounds over its bounded target class before selecting xi and T. An endpoint transfer still must pay the finite-window old-bias defect as in the separately qualified transfer result.

Possible next routes are to propagate the quantitative spectral lower bounds through the explicit pole-cone and Gram formulas, or to design a different core with uniform rational certificates. The absence of(36) in this derivation is an open estimate, not a counterexample or a universal impossibility claim.

## 12. Exact discriminator: dimension and gap do not suffice for growing routes

Let A_N be the N-vertex path adjacency and B_N=4I+N^-1 A_N. At frequency1,

    B_N-I=3I+N^-1 A_N >=(3-2/N)I>=2I, N>=2.

Thus this one-particle family has polynomial dimension, bounded coefficients and a fixed spectral gap. Its endpoint inverse entry is exactly, up to sign,

    [(B_N-I)^-1]_(1,N)=N^[-(N-1)]/det(B_N-I).

Since every eigenvalue of B_N-I is at least2,

    |[(B_N-I)^-1]_(1,N)|<=2^-N N^[-(N-1)].       (37)

This is superpolynomially small. It directly discriminates against inferring polynomial runtime from polynomial reachable dimension or a polynomial gap alone. No numerical test is needed: the determinant cofactor and eigenvalue inequalities prove(37). It is not a counterexample to the fixed-bus result, whose maximum routing path length k is independent of N.

## 13. Verification limits and handoff

The independent work in this continuation is the fixed-graph response lower bound, complete power ledger, simultaneous parameter/error choices, finite-grid margin and precision separation. The parent lemmas, quantum dynamics identities and qualified source inverse are reused. Existing checker programs were not rerun; no numerical PASS result is offered as proof of the asymptotic conclusion. The exact growing-path calculation is the new analytic discriminator. No claim is made of fresh independent validation of the earlier self-authored bus.

All editable prompt files changed: none. Only the assigned source directory was written. No canonical/audit/claim graph/lock/cache/Git/PR state was changed. Root should review the new uniform fixed-data bounds, arithmetic conditioning allowance and exponent accounting before accepting this refinement. Native coherent preparation, vacuum routing, actual phase/timing/isolation, calibration over the long runtime, any microscopic controller-energy supplier, permanent stopping and reset/reuse remain their existing explicit physical obligations.

<!-- Immutable source: reachable_bus_resource_root_review/FINAL_QUALIFICATIONS.md -->

# Qualified fixed-plant resource theorem

The complete derivation ce3ddd3ad376016f391992b30485454378607e6953fddcdeb2ecea702777d875 is accepted as a conditional nominal-duration and precision-request refinement of the fixed strong spectral bus, using the accepted reducing-envelope replacement. It is unpublished and not independently retained. No physical observation or practical efficiency is asserted. The conclusion fixes the full old strong plant H, accessible B, d and q=d(d-1)/2, graph, time unit, window and target-bound certificate before epsilon tends to zero.

The fixed positive-width spectral box, positive weight ball, inverse bounds and derivative bounds are supplied or computably certified quantitative data. Their existence is justified by the parent's explicit cone and finite Gram formulas, not by an unquantified successful point. The candidate makes the compactness dependence explicit: a common lambda controls the bounded target diagonal; positive weighted Vandermonde minors bound all Jacobi denominators and core hoppings. Shrinking these boxes once retains positive lower bounds and the contraction factor at most1/2. All resulting constants may be extremely large functions of the fixed plant.

Root had separately frozen CONDITIONAL_LEDGER.md fbd9c447 before receiving or reading this worker's resource result. That independent derivation agreed on a=2q+6, route length3q+1, r=a(3q+1), the full counterterm bound and conservative Z1/Z2 bounds. It used a larger common residual exponent and therefore a weaker epsilon power. The present worker's two improvements are checked and accepted: use the exactly canceled secular D, whose norm is uniformly bounded by its finite target form; retain xi R3 and xi^2 R4 separately in Duhamel. The earlier conservative bound is not a contradictory empirical result or an executed failure.

For n=N+1, the reducing-envelope/code dimension product is O(n^(2q+2)). Every zero-routing Q/P affine form has a coefficient at least n^-4; the supplied box therefore admits a gap at least a constant times n^-a. The finite grid has a strict margin and polynomial cardinality for fixed coordinate dimension, so no zero decision or uncontrolled dovetail is needed. Prescribing rho=rho0 n^-a both preserves this gap and supplies a lower bound on routing amplitude. The tree cofactor has3l+1 routing edges and4q-3l-1 off-path router vertices for leaf l. Positive lower bounds on core hoppings and high-energy off-path determinants, together with an upper determinant bound, give |G_l|>=g0 n^-r. This uses the actual fixed tree; a resolvent norm upper bound alone would not suffice.

The one-source inverse is explicitly the qualified reducing-envelope inverse. The full source inverse may be singular and is never substituted. Its one-hole implementation U_l=B_bus tensor I+I tensor J_F L_hole-omega_l I has polynomial dimension and the required restricted gap. The normalized one-hole vector has unit norm. The full physical counterterms obey ||A2||=O(n^(2r+a)) and incident coefficient load O(n^(2r+a-1)); their off-code action is retained.

The exponents are x=q/2+r+a for Z1, y=q+2r+2a for Z2, p=q+3r+2a for R3 and h=q+4r+3a for R4. Root checked p-x=q/2+2r+a>0, 2p-y=q+4r+2a>0, and 2p-h=q+2r+a>0. Thus xi=c_xi epsilon n^-p controls both endpoint corrections, xi R3, xi^2 R4, the finite holding-window term and the positive-block incident loads with a fixed sufficiently small c_xi. The uniform D bound follows from |kappa_ab|=2|L_ab|/t_* and ||S_-/N||<=(N+1)/(2N)<=3/4; the Hermitian old-pair block has norm |kappa_ab| ||S_-/N||, not an extra factor of two. Source fluctuation fixes N=O(epsilon^-2). Expanding p gives18q^2+65q+30 and T=O(epsilon^[-(72q^2+260q+122)]). For q=1 the sufficient exponent is454. These are sufficient upper bounds, not optimal scaling or a useful hardware estimate.

Preparation trace error, full-generator integrated error and timing/phase accuracy remain supplied budgets. The literal old H is not approximated physically. Per-local-coefficient request epsilon/[constant*n*(T+w)] controls the full generator, while pointwise load slack is an additional requirement. Fixed-input request eta_in=c_in epsilon^3 n^[-(2p+3r+2a+1)] pays the inverse-response derivative, one-hole resolvent conditioning and source-phase frequency-time product. It is applied after a strictly certified grid point; the selected grid-point map is not asserted differentiable. Exact-L support and phase remain supplied unless the separately scoped rational-M approximation is used. Upward reserve rounding and actual scalar phase are charged. All claimed logarithmic external bit requests are for fixed certificates and finite-dimensional data, not for the time an arbitrary computable oracle takes to answer.

Root also checked the separate exact Gram-conditioning argument. The local-matrix-unit/unnormalized-Dicke basis is real integer-valued; a full-rank Gram minor has positive integer determinant at least1. Bounds on its principal and bordered minors control rational LDL factors and their inverses. Approximate positive inverse square roots only, then carry rational products exactly. The displayed g^3 H_S(2C_max+1) entry-error bound follows from Frobenius norm bounds on both matrix factors. The conservative internal precision request in equation35 dominates these finite logarithmic denominators and is polynomial in N. This is a finite arithmetic precision prescription; no implemented algorithm, practical cost or oracle walltime was tested.

The analytical path family B_N=4I+N^-1 A_N has a fixed one-particle gap but endpoint response at most2^-N N^[-(N-1)], by an exact cofactor and eigenvalue bound. It is accepted only as a counterexample to inferring response or runtime bounds from dimension and gap alone on growing paths. It does not refute the fixed-bus theorem or establish a general physical impossibility.

The full argument, dependency ledger, exposure statement and evidence statement were read. All21 frozen member identities and15 live/captured sources are verified by the accompanying bookkeeping execution. No scientific computation was run by this worker or root for the resource theorem. The worker is the earlier bus author and uses the same model; there is no fresh independent revalidation of that parent. Independence here is the separately frozen root resource derivation and subsequent full argument check, with the already qualified parent and envelope premises reused. Historical parent scientific executions remain in their own source packets.

The shrinking-bias family remains open: the complete constant package must satisfy the explicit equation36 uniformly as Lambda tends to zero. Existing old spectral/transition lower bounds alone do not prove this. A target depending on the selected T requires the uniform bounded-target certificate before selecting T and the later rational approximation; no circular selection is accepted. Native purity, complementary controls, phase references, calibration over the long runtime, controller energy and records, physical measured-energy identification, permanent halt and reset/reuse remain unresolved or supplied. No editable prompt file changed.

<!-- Immutable source: bus_preparation_resource_root_proposal/PROPOSED_LEMMAS.md -->

# Proposed composition: fixed-plant resource bound with preparation and modeled slew

Status: unaccepted root proposal, written before the requested separate check. This composes already qualified conditional sources; it is not native preparation or an audit verdict. Fixed finite strong plant H,B, fixed old geometry, q=d(d-1)/2>=1, fixed target/window and fixed spectral/routing certificate package only. The shrinking-bias family is a different open question.

Sources:
- reachable_bus_resource_root_review/QUALIFIED_ACCEPTANCE.json d02d9205f451d73da584581970ff333ffd6d87a53a695c1e1b992db9ec615edd and its FINAL_QUALIFICATIONS.md.
- reachable_bus_resource_candidate/DERIVATION.md ce3ddd3ad376016f391992b30485454378607e6953fddcdeb2ecea702777d875.
- bus_preparation_root_review/QUALIFIED_ACCEPTANCE.json28bef1945c65f807be837286d6e795d888f3d8b9ebb75024ac26ee0084409641 and controlling qualifications.
- bus_bounded_slew_preparation_root_review/QUALIFIED_ACCEPTANCE.json b237e6550c7b500ff48cdaa2cd30e50cf4895205a610e8feb677da085bf82473 and controlling qualifications.

## Proposed resource composition

Let n=N+1, a=2q+6, r=a(3q+1), p=q+3r+2a. The fixed-plant resource theorem supplies N=O(epsilon^-2) and the feasible choice
xi=c epsilon n^-p, T=t_*/xi^2,
with complete unscaled bounds v<=C_v n^r, a2<=C_A n^(2r+a), fixed ||V_p||, and a common positive-block incident cap J_*. Every constant depends on the fixed certificate package, not N or epsilon in(0,1]. Its duration exponent is4p+2=72q^2+260q+122. All prior strength, spectral, window, arithmetic and calibration conditions remain in force.

Use the bounded-slew preparation comparator that retains U_E, not literal Q. Fix g>0 and S_*>0, and fix the parent waveforms and durations r_on,r_off,t_s,t_p using the uniform J_*. Their sum tau is constant in N and epsilon. Using half the desired physical amplitude/derivative allowance for the modeled schedule is permissible if separately certified implementation slack is desired, but implementation derivative control is an independent premise.

The weak part of the preparation trace error is bounded by
C_1 xi n^r+C_2 xi^2 n^(2r+a)
<=C_1 c epsilon n^(-(p-r))+C_2 c^2 epsilon^2 n^(-(2p-2r-a)).
Here p-r=q+2r+2a>=2 and2p-2r-a=2q+4r+3a>=2. Thus even after demanding an extra n^-2 in the preparation trace allowance, a sufficiently small positive constant c works uniformly for all N>=2 and epsilon<=1. Reducing c only multiplies T by a fixed factor; the exponent4p+2 and prior feasible constraints are unchanged.

The complete input has n_C=O(n) apparatus sites and an equally sized fresh memory. With the uniform incident cap, the actual installed runtime K obeys beta_bar=||H-a_old I||+(n_C+1)J_*<=b n for a fixed b>=1, for a fixed chosen centering a_old. This is a global norm upper bound, not a globally bounded Hamiltonian or energy claim.

For an optional dimensionless release-moment tolerance epsilon, define e_rel=epsilon/(24 b^2 n^2). Choose the weak residual sum<=e_rel/2 by the constant c above, the joint readiness error<=e_rel/4 and2 integral||E_p||<=e_rel/4. Then e_p<=e_rel and the additional preparation errors relative to the *ideal released Omega with the tau-aged old marginal* obey
|Delta centered mean|<=beta_bar e_p<=epsilon/24,
|Delta centered second moment|<=beta_bar^2 e_p<=epsilon/24,
|Delta variance|<=3 beta_bar^2 e_p<=epsilon/8.
The respective units must be restored by fixed energy scales if dimensional tolerances are requested. These are preparation-to-release allowances only. They do NOT say that arbitrary later target moments are epsilon-accurate merely by applying a global trace-to-moment estimate to the runtime compiler. That stronger estimate could impose an incompatible N requirement. Exact joint-energy structure or a distinct runtime moment theorem is needed for that different question.

The direct complete-output trace telescope with parent runtime budget3epsilon/4, implemented runtime cost<=epsilon/8 and e_p<=epsilon/24 is at most11epsilon/12. The prepared output includes U_E and the old flow becomes exp(-isH)W exp[-i(T+tau)H]. All E outputs remain stored and retained; none are reset or traced out. The preparation cost tau is constant, so total nominal duration tau+T has the same polynomial upper exponent, under the same fixed-family conditions.

## Precision requests and unclosed physical costs

For O(n) bounded local preparation terms and constant tau, a sufficient additive per-term operator error request is O(epsilon n^-3), which makes the global integrated error O(epsilon n^-2). The joint readiness tolerance may similarly be supplied by O(epsilon n^-3) per-site trace errors for a product of fresh memory qubits, via the tensor-product telescope. Readiness for a correlated implementation must satisfy the joint bound directly; no product premise may be inferred.

For n_S=qN source gates, ||Q_theta-Q_theta'||<=(pi/4)|theta-theta'|. Hence a common gate-axis error O(epsilon n^-3) suffices for the same preparation budget. The required off-ramp correction omega alpha_off adds only fixed-duration frequency sensitivity; the dominant omega T phase accuracy is already charged in the resource theorem. Recompute T, final runtime phases, off-ramp gate phases and actual reserves after the final c is selected. Actual scalar preparation phase Phi and U_E are retained in the amplitude comparator; reserve upper bounds must not replace actual chosen scalars there.

Because n=O(epsilon^-2), these additional numerical requests use O(log(1/epsilon)) bits for the fixed family. The parent's polynomial internal arithmetic precision can be tightened by these polynomial factors without changing its polynomial nature. This does not certify any arbitrary computable oracle's wall time, continuous waveform generation, physical preparation fidelity, derivative noise, or autonomous clock complexity. No actual scheduler is constructed here.

Physical pointwise amplitude and derivative bounds require their own incident certificates; small integrated perturbation alone gives neither. No claim of low total reserve/energy is made: whole-system strengths and energy moments can grow with n. Storage during T and final halt/reset/reuse remain unsupplied. Changing the memory comparator is essential to the accepted preparation result and remains essential in this composition.

## Intended check

Check the powers and choice order, parent norm premises, global-to-incident distinctions, exact preparation phase/memory contract, the release-only moment scope, and whether the additional precision requests truly leave the already conditional fixed-family polynomial exponent unchanged. No new numerical run is required unless it resolves a concrete gap. A source-exposed same-model check is useful but is not blind replication or retained audit.


<!-- Immutable source: bus_preparation_resource_exposed_check/REVIEW.md -->

# Exposed check of the fixed-plant resource/preparation composition

Disposition: the proposed nominal-duration exponent survives the accepted evolved-memory preparation, including its stronger release-only moment allowances. I find no load-bearing algebraic defect in this composition. Acceptance must retain the conditions below. In particular, no arbitrary prescribed strength ceiling, physical derivative certification, runtime target-moment theorem, native preparation, efficient oracle, or autonomous clock is supplied by this result.

This is a same-model, source-exposed analytical check of proposal SHA256 `625b1f6f9496fd4acea138f0b25b56afa8f0e90265b5bcdcabcdcd88a660e990`. The author is the root; the reviewer previously checked the bounded-slew preparation used here. It is a fresh check of the composition, not fresh independent validation of every parent. No scientific program was run or replayed. Exact controlling sources and read/reuse coverage are in `SOURCES.json` and `SOURCE_COVERAGE.md`. Root owns acceptance; this review is neither publication nor retained audit.

## 1. Premises actually imported

The resource source is the complete derivation `ce3ddd3a...`, qualified by acceptance `d02d9205...` and its controlling qualifications `e50497e7...`. It fixes a finite strong old plant, port, geometry, target/window and quantitative spectral/calibration certificate package before varying accuracy. In particular, it supplies fixed-width cone boxes, strictly positive weights and fixed core hopping bounds, a fixed routed bus, the qualified reducing-envelope inverse, full counterterm norms, and separate physical-data versus internal arithmetic precision bounds. The source does not supply these constants uniformly for a shrinking-bias family.

The preparation source is acceptance `b237e655...` with qualifications `1c3714fa...`, the proposed argument `6e094766...`, and my prior review `a1b9ef46...`; the original installed-preparation source and its qualifications remain dependencies. These sources retain the actual old H and positive reserves, full joint input and all memory outputs. Their comparator includes the entire evolved memory unitary U_E. The older literal-Q memory contract is not recovered by this composition. The bus note remains exactly `1733b296...`; its full-gap requirement is replaced only through the separately qualified reachable-envelope/resource dependency.

Use n=N+1 with N>=2, q=d(d-1)/2>=1, and the supplied bounds

    a=2q+6, r=a(3q+1), p=q+3r+2a,
    v<=C_v n^r, a2>=||A2|| with a2<=C_A n^(2r+a),
    ||V_p||<=C_p, xi=c epsilon n^-p, T=t_*/xi^2.

The constants are fixed-family constants. In particular A2 is the complete unreserved physical-space counterterm, not its code compression. The source inverse is the qualified compressed inverse, not a claimed everywhere-invertible full-source resolvent. All positive reserve blocks and the literal full old H remain in the installed K.

## 2. Noncircular choice of the preparation allowance

Fix the resource certificate package and its uniform incident bound J_*. Choose g,S_*>0 and the accepted smooth ramp/gate shapes. The accepted inequalities choose r_on,r_off,t_s,t_p from J_*,g,S_* and shape constants only. Thus tau=r_on+r_off+t_s+t_p is constant across N and epsilon. Shrinking xi within the parent feasible range preserves J_* and these same durations.

There are n_C=b_bus+qN apparatus sites. For any fixed old centering a_old, choose a fixed B_beta>=1 such that

    ||K-a_old I|| <= ||H-a_old I||+(n_C+1)J_*
                   <= B_beta n.

For example enlarge B_beta beyond ||H-a_old I||+(b_bus+q+1)J_* in the chosen fixed energy unit. This overcounts incident positive blocks, including the old-port reserve. Fresh memory has zero runtime Hamiltonian in the stipulated isolated model; tensoring its identity does not change this norm. This bound is available before final xi and does not substitute B_beta n for any actual reserve in a phase.

The accepted unhalved trace estimate gives the weak preparation cost

    E_weak <= xi r_on C_p+r_off(xi C_v n^r+xi^2 C_A n^(2r+a))
           <= A c epsilon n^-(p-r)+B c^2 epsilon^2 n^-(2p-2r-a),
    A=r_on C_p+r_off C_v, B=r_off C_A.

There is no factor N missing in v: the parent has q source/leaf couplings and one old port coupling, while all N onsite and pair counterterms are already counted in a2. The half-ramp integral and the factor two in the trace/isometry inequality have already canceled in this formula.

Direct expansion gives

    p-r=q+2r+2a>=2,
    2p-2r-a=2q+4r+3a>=2.

Consequently, for 0<epsilon<=1,

    E_weak <= (A c+B c^2) epsilon n^-2.

Let c_0 be any feasible fixed parent prefactor. A fixed positive rational lower rounding of

    min(c_0, 1, 1/[96 B_beta^2(A+1)],
                  sqrt(1/[96 B_beta^2(B+1)]))

ensures E_weak<=epsilon/(48 B_beta^2 n^2). No accuracy-dependent further reduction in c is needed. This explicitly proves the asserted extra n^-2 without weakening the runtime exponent. All old constraints are monotone under this reduction: corrector, window, and installed weak/counterterm loads become smaller. The calibrated unscaled amplitudes and counterterms are unchanged by this final reduction.

The order is therefore: fixed uniform certificates and majorants; fixed preparation durations and B_beta; choose N from the runtime source; choose the certified grid point, routing, calibration, unscaled amplitudes/counterterms; choose the fixed common c using these uniform majorants; select xi; then recompute T and every actual phase/reserve. The c formula may equivalently be selected earlier because its majorants are uniform. It must not be estimated from a subsequently changed actual beta or phase. A T-dependent target needs its own bounded-target certificate before these choices; the present result does not manufacture one.

## 3. Release moments and the complete output

Put e_rel=epsilon/(24 B_beta^2 n^2). Supply joint readiness error<=e_rel/4 and preparation implementation cost 2 integral||E_p||<=e_rel/4. The weak estimate above gives e_p<=e_rel. These are demands on the complete joint state and full-space generator, including unwanted storage/control couplings; they are not consequences of a local calibration slogan.

For A_K=K-a_old I with beta=||A_K||, trace duality yields

    |Delta <A_K>|<=beta e_p<=epsilon/(24 B_beta n)<=epsilon/24,
    |Delta <A_K^2>|<=beta^2 e_p<=epsilon/24.

Since each centered mean has absolute value at most beta,

    |Delta Var(K)| <= |Delta <A_K^2>|+
                       |Delta <A_K>|(|<A_K>_1|+|<A_K>_2|)
                    <=3 beta^2 e_p<=epsilon/8.

These are ordinary scalar moments relative to the ideal released Omega and the tau-aged ideal old marginal. Fixed energy units or separately declared fixed moment scales are necessary for dimensionful tolerances. The operator-square bound includes the full off-code A2^2 contribution: no projection or removal of that term occurs. If moment operators retain E as a reference, the previously required U_E conjugation remains; ordinary D/C moments alone are insensitive to U_E.

The ideal preparation isometry is

    exp(-i Phi) Omega_phi tensor [(exp(-i tau H) tensor U_E tensor I_R) Q],
    U_E = relabelled exp(-i alpha_on A_C),
    A_C=A_0+xi V_s+xi^2 A2, alpha_on=r_on/2, alpha_off=r_off/2,
    Phi=C0[t_s+t_p+(r_on+r_off)/2]+R(r_on+r_off)/2+pi n_S/4.

Here R and C0 are actual installed data. The SWAP contributes no extra endpoint scalar. Gate axes use phi_l+omega_l alpha_off; runtime phi_l retains +omega_l T and receives no additional +omega_l tau. This tracks the off-ramp free source phase and the large on-ramp C evolution exactly. Approximation of coefficients must pay the change in this full comparator or be absorbed into the certified full generator error; it cannot silently delete U_E.

After preparation E is a passive reference for the accepted bus theorem. Its arbitrary-input guarantee applies to all D/E/R correlations. The old output is exactly the stipulated comparator exp(-isH)W exp[-i(T+tau)H]. All memory outputs are retained, and no inverse U_E or reset is inserted. The parent runtime trace budget 3epsilon/4, implemented runtime cost<=epsilon/8, and e_p<=epsilon/24 sum to 11epsilon/12. This uses the ideal aged old marginal, not a replacement by the imperfect actual release marginal without its extra shift allowance.

The release allowances must not be advertised as epsilon accuracy of arbitrary runtime target energy moments. Applying beta^2 times the coarse runtime trace error would introduce growing n^2 and does not prove that statement. Exact joint-energy structure or a distinct moment theorem is needed. No such theorem is imported here.

## 4. Duration and precision ledger

The polynomial identities are

    r=6q^2+20q+6,
    p=18q^2+65q+30,
    4p+2=72q^2+260q+122.

The parent's n<=(C_N+4)epsilon^-2 therefore gives

    T<=t_* c^-2(C_N+4)^(2p) epsilon^-(4p+2).

Adding the fixed tau changes only the constant since epsilon<=1. For q=1 the same sufficient exponent is454. This bounds nominal physical durations in the unchanged old-H time units. It is not an overall compiler wall-time bound or an efficient preparation implementation.

There are O(n) modeled local preparation terms. For constant tau, additive operator error delta per term gives O(n delta) integrated error, so delta<=k epsilon n^-3 suffices with a fixed small k. This includes scalar errors and compensating blocks when written in a normalized local dictionary. Relative coefficient errors still need the multiplying operator norm. With independent fresh memory and product per-site readiness states, the tensor-product trace telescope similarly makes O(epsilon n^-3) per-site error sufficient. This product conclusion requires independence from the old/apparatus/reference state as well as among the fresh sites; arbitrary correlated readiness must satisfy the joint trace premise directly.

For n_S=qN simultaneous gates the accepted bound ||Q_theta-Q_theta'||<=(pi/4)|theta-theta'| gives total O(n delta_theta); delta_theta=O(epsilon n^-3) suffices. The new off-ramp phase term omega alpha_off has only fixed-time sensitivity. Long-time omega T requires the tighter gate-axis precision too, rather than merely citing its former O(epsilon/n) allocation.

This tightening is available without changing T: resource equation(32) requests

    eta_in=c_in epsilon^3 n^-(2p+3r+2a+1).

Multiplication by T=O(epsilon^-2 n^(2p)) gives phase error

    O(epsilon n^-(3r+2a+1))=O(epsilon n^-3),

because 3r+2a+1>=3. After choosing the smaller c, reduce the fixed precision prefactor if needed to pay its c^-2 constant. Direct phase evaluation, explicit timing specifications and any other previously looser sub-budgets must likewise actually be tightened by n^-2 where needed. Such requests remain polynomially small and use O(log(1/epsilon)) absolute bits for this fixed family. They do not follow automatically from a previous successful run. Normalized target phases retain the exact-support premise or the separate rational-Hermitian repair; near-zero support is not decided by this composition.

The parent's internal arithmetic bound P_N+log(1/tolerance)+20 remains polynomial after these polynomial tolerance tightenings. It is explicitly distinct from the O(log(1/epsilon)) external-data requests and from arbitrary computable-oracle wall time. Phase references, numerical time accuracy, storage and waveform generation are still supplied capabilities, not consequences of a bit-count formula.

The quoted 11epsilon/12 trace budget applies to the chosen exact target in the internal compiler. If the separate rational-M repair is used, its discrepancy from the requested L still needs its own allocation. For example run the whole composition at internal tolerance epsilon/2 with ||M-L||<=epsilon/4; the trace bound is then at most11epsilon/24+epsilon/2=23epsilon/24. Uniform fixed target-norm certificates remain required, and the exponent is unchanged. Release moments refer to the actually chosen M-dependent installed K and its ideal release, not to equality with moments of a hypothetical L-dependent installation.

## 5. Strength, slew and residual qualifications

The accepted modeled incident strength is at most 2J_*+g and modeled incident derivative norm sum at most S_*, with disjoint stages and flat joins. These constants are independent of accuracy, although whole-system norms, reserves and derivative norm can grow with n. The waveform/geometry hypotheses and independent matching access remain prerequisites.

One wording qualification is necessary: reserving half a *physical amplitude* ceiling is possible only if that ceiling already accommodates the modeled bound with this slack. An arbitrarily small prescribed ceiling cannot be met merely by decreasing xi, because the base positive bus/source terms do not vanish. For example requiring physical strength ceiling>=2(2J_*+g) supplies the stated half-budget convention. Longer durations can reduce the modeled derivative cost; they do not reduce the fixed base amplitude. This qualification leaves the stated existence of a fixed accuracy-independent cap intact.

Integrated implementation error controls trace error, not pointwise amplitude or derivative. A high-frequency perturbation can have a small integral norm and an arbitrarily large derivative. Thus physical strength/slew claims need their own pointwise incident certificates or slack. A first-derivative cap is not a hard bandwidth cap. No claim is made that constant nominal tau supplies hardware parallelism, pure memory, calibration references, autonomous scheduling, storage for T, or final halt/reset/reuse. The mathematical K moments are not a laboratory energy identification.

The fixed-plant exponent, complete evolved-memory output, and release-only moment allowances are supported under these unchanged premises. Shrinking-bias uniformity, arbitrary runtime target-moment accuracy from the global trace estimate, literal-Q memory recovery, and physical supplier costs remain open or outside scope. No failed route from the parents is repaired merely by this composition.

## 6. Evidence and change record

All new scientific checking above is analytical. No new numerical fixture was warranted: the deciding risks reduce to the accepted full-space inequalities, explicit exponent identities and precision ledger. Scientific executions:0. Historical checks remain at their original frozen scopes; none were replayed or promoted to new asymptotic evidence. Source capture and final hashing are bookkeeping only.

The complete new proposal and complete resource derivation were read; acceptance/qualification texts were read; the exact unchanged preparation and bus portions recorded in SOURCE_COVERAGE were reused. The source pins were checked before capture and again when sealing. The copied historical freeze files are provenance records, not a claim that every transitive archive member was re-read. No canonical, Git, PR, audit, lock, cache, graph, axiom or publication state was modified. Editable prompt files changed:none. Only this assigned review directory was written.

The task was interrupted before source capture and sealing. The earlier three-file partial packet is preserved byte-for-byte under interrupted_original, with the root recovery source and identities in INTERRUPTION_RECOVERY.json. It had no completed manifest or freeze and evidences no scientific execution. The resumed metadata-only run is recorded with actual source at launch and full streams. The only scientific-prose addition after recovery is the explicit rational-M budget clarification in section4; it changes neither the disposition nor the exponent.

<!-- Immutable source: bus_preparation_resource_root_review/FINAL_QUALIFICATIONS.md -->

# Qualified source acceptance: preparation and fixed-plant resource composition

The root accepts the conditional composition in proposal625b1f6f and exposed reviewf4b8ca6c, subject to this controlling qualification. This is an unpublished mathematical result for continued research, not a retained audit, physical implementation or empirical prediction. The earlier proposal's pending language is preserved as history.

Fix the complete finite strong plant, port, geometry and quantitative certificate package of resource acceptance d02d9205 and qualifications e50497e7. Import the installed-preparation acceptance28bef194 and bounded-slew acceptance b237e655 only with their controlling qualifications. The reducing-envelope inverse remains mandatory; full physical A2 and full residual norms are used. No shrinking-bias uniformity is inferred here.

For n=N+1, a=2q+6, r=a(3q+1), p=q+3r+2a, the resource choice xi=c epsilon n^(-p) has enough slack to pay a preparation trace allowance proportional to epsilon n^(-2). Indeed p-r=q+2r+2a and 2p-2r-a=2q+4r+3a are both at least2. With A=r_on C_p+r_off C_v, B=r_off C_A and beta<=B_beta n, the review's explicit positive fixed c below c_0,1,1/[96 B_beta^2(A+1)] and sqrt(1/[96 B_beta^2(B+1)]) pays the weak ramp half of e_rel=epsilon/(24 B_beta^2 n^2). The remaining halves are actual joint readiness and full-space implementation premises. All constants and uniform target bounds precede the final choice of xi. Recompute T=t_*/xi^2, phases and actual reserves after that choice.

The accepted preparation contract retains U_E, with the actual scalar Phi and gate correction +omega alpha_off. Runtime phase contains +omega T, without +omega tau. Old flow is exp(-isH) W exp[-i(T+tau)H]. All D/E/R correlations and memory outputs remain. Literal-Q memory recovery, inverse U_E and reset are not furnished. Ordinary release moments are relative to the ideal Omega and tau-aged old marginal for the actually installed K; E-valued moments retain U_E conjugation. Centered first/second-moment errors are at most epsilon/24 and variance error at most epsilon/8 in fixed declared energy units. These are preparation-to-release allowances, not accuracy of arbitrary target moments at runtime. The full off-code square is retained.

The direct internal trace budget is11epsilon/12. An approximate rational target has a separate external budget. For example use internal tolerance epsilon/2 and ||M-L||<=epsilon/4 under uniform bounded-target certificates, giving23epsilon/24. Its release moments concern the M-dependent K, not a different L-dependent installation. Exact-support or the separately qualified rational-target construction remains necessary.

Fixed modeled ramp/gate durations give constant tau and total duration tau+T=O(epsilon^(-[72q^2+260q+122])). This exponent is454 when q=1 and is sufficient, not optimal or practical. Additional preparation term, gate-axis and product-memory tolerances of order epsilon n^(-3) are achievable as numerical requests with polynomially growing bit counts. Product readiness requires independence from the complete old/apparatus/reference state; otherwise the joint condition must be supplied directly. Old-data precision times T already has sufficient n powers, after tightening its fixed prefactor. Any loose direct phase/timing or implementation sub-budget must actually be tightened; merely citing the old run is insufficient. Internal exact arithmetic requests and arbitrary computable-oracle wall time remain distinct.

Modeled incident strength2J_*+g and derivative bound S_* are accuracy independent. Reserving half a prescribed physical amplitude cap requires that cap already be at least2(2J_*+g). Shrinking xi cannot remove the fixed base strength. Full integrated generator error does not imply pointwise strength, derivative or hard bandwidth bounds; independent physical certificates remain required. Global norms, reserves and moments can grow with N. Purity, matching/complement controls, phase references, storage for T, autonomous scheduling, physical energy identification and final halt/reuse remain supplied or open.

The root wrote the proposal before the separate exposed check and reconstructed the powers, noncircular constant choice, trace/moment inequalities, phase ordering and precision tightening. The complete proposal and final review were read; previous complete reads at unchanged parent identities are reused. The reviewer previously checked the preparation parent and is the same model, so this is source-exposed checking with shared premises, not blind or cross-family replication. No scientific computation was run or replayed. The single actual metadata capture and all source identities are separately verified by record_acceptance.py. Its receipt is provenance, not proof. The usage interruption and three original partial files remain preserved. No editable prompt files changed.

<!-- Immutable source: shrinking_bias_resource_candidate/DERIVATION.md -->

# A polynomial resource extension along a supplied admissible shrinking bias

Status: exposed mathematical continuation proposed for root review. The fixed-plant resource result is qualified-accepted, but this new uniform extension is not. The author previously authored the bus and transfer candidates; this is not fresh independent parent validation. Exact source identities, coverage and exposure are recorded separately. No scientific program was run.

## 1. Conditional conclusion

Fix finite Hermitian H,C,B on the complete d-dimensional old plant, d>=2. Supply the actual admissible finite onsite/nearest-neighbor decomposition of the added bias C, its positive reserves, and permission to attenuate those added blocks. Supply the bus parent's one-qubit port B, occupied/vacant geometry and isolation premises. The old H terms remain literal with coefficient one. Supply a positive rational a_0 no larger than p_C, the complex Krylov Gram determinant for C,B and hence the leading coefficient of the accepted bias polynomial. No assumption that Lie controllability supplies such a C is made.

For the effective prescription, supply computable names for H,C,B,W,t_*, the finite decomposition/reserve data and the quantitative certificates used below. Norm majorants alone do not supply those names. Without effective access, distinguish the finite-real existence statement from a computable prescription and precision requests.

Fix finite upper bounds on ||H||, ||C||, ||B||, a physical time unit t_*>0, a finite observation window w, and a computable target unitary W. Preparation, phase reference, release, coefficients and full-generator calibration retain their explicitly supplied physical status. For a positive rational accuracy epsilon<=1, the accepted selected-point spectral estimates can be propagated through the entire bus construction. A sufficient nominal autonomous runtime is

    T=O(epsilon^-P),                              (1)
    P=2+4p+2 kappa v,
    q=d(d-1)/2,  m=2(d-1),  k=3q+1,
    a=2q+6,  r=ak,  p=q+3r+2a,
    tau=4m^2-10m+10,
    g=tau(m-1)+6k,
    u=g+2,  v=3u+8,
    kappa=q(2q+1).

All constants behind O depend only on the fixed original quantitative certificates, geometry, time/window and the fixed bounded target class, not epsilon or the selected bias node. For d=2, q=1, this sufficient exponent is1078. It is not optimized and has no practical-efficiency interpretation.

The source length is N=O(epsilon^-2), the bus graph is fixed, and the added incident cap is one finite epsilon-independent J_*. All positive bias blocks, old-port additions, source/router interactions, counterterms and reserves are included. The complete output comparator retains every controller output and arbitrary old/reference input and uses the literal-H target

    exp(-i sH) W exp(-iTH), 0<=s<=w.              (2)

Explicit polynomial precision requests are given in section9. They do not bound the wall-clock time of arbitrary computable oracles, discovery of the supplied C/certificates, or a physical preparation/timing/calibration procedure. The new content closing equation36 of the fixed-H note is a uniform positive-cone construction, a weighted-QR Jacobi derivative bound, and propagation of their powers through the complete ledger.

All numerical comparisons with1 are in fixed declared reference units, exactly as in the quantitative parent. Energy/time units carried by fixed constants are retained. There is no rescaling of the physical H.

## 2. Selected-point certificate and the small parameter

Use the accepted upper-half interpolation grid, not the different grid in the exposed ancestor. Put n_b=d(d-1)=2q, D_b=n_b(n_b+1), and kappa=D_b/2=q(2q+1). With fixed norm bounds K>=max(1,||H||+Lambda_0||C||), b>=max(1,||B||), the accepted result supplies a rational node

    Lambda/2<=lambda<Lambda,
    H_lambda=H+lambda C,

where every nonzero old energy gap, separation between distinct signed nonzero gaps, and every off-diagonal |B_ab| is bounded below by a fixed positive constant times Lambda^kappa. Select a fixed positive rational c_z sufficiently small that

    zeta=c_z Lambda^kappa<=1                     (3)

is a simultaneous lower certificate for these three quantities for every allowed Lambda. Such c_z follows directly from the explicit factors in equations5 and12 of accepted review b654e30c. Their constants use a_0, the fixed norm bounds, d and the canonical interpolation coefficient A_D; no limiting leading-term-dominance assertion is used. The selected node's positivity margin is certified at a fixed requested evaluation precision, despite arbitrary noncommuting H,C.

In particular the old positive gaps are at least zeta, their pairwise separations are at least zeta, and the nonzero second-order P/P divisors classified in the bus are at least zeta. Longer accidental sums of code frequencies need not be classified. The exact old energy basis is computable on each selected point; quantitative input precision is addressed later without assuming an equality oracle.

Choose once a positive rational lambda_0 so that Lambda=lambda_0 epsilon is at most min(1,Lambda_0) and

    Lambda w a_C <= epsilon/64,
    a_C=||C-c_C I||,
    c_C=(lambda_max(C)+lambda_min(C))/2.          (4)

A supplied upper bound on a_C suffices, for example the fixed bound on ||C||. To avoid a zero decision one may take lambda_0<=1/[64(t_*+w_bar)(c_bound+1/t_*)], additionally bounded by1 and Lambda_0, with rational lower rounding. Then zeta is exactly a fixed positive constant times epsilon^kappa. The notation lambda denotes the selected bias coefficient; it is distinct from the positive cone multiplier used below.

The physical premise is permission to add lambda(C_alpha+r_alpha I) for the actual bias blocks. It is not permission to attenuate any old H term or an assertion of new old-edge access. Write R_C=sum r_alpha and J_C for the fixed reserve and incident-load ledger of that supplied decomposition.

## 3. Uniform positive cone with bounded upper weights

Let ell=d-1, and label the ground-to-excited positive gaps Delta_a=E_a-E_0, a=1,...,ell. Set beta_a=|B_0a|^2. Then

    zeta^2<=beta_a<=b^2.

For the bus cone functions

    F_c(mu)=sum_j |B_jc|^2/(E_c-E_j-mu)
                   -sum_j |B_j0|^2/(E_0-E_j-mu),

the only positive pole at Delta_a in this ell-vector is beta_a e_a/(Delta_a-mu). Choose a fixed rational

    0<delta_0<=1/[256(d+1)(b^2+1)],
    delta=delta_0 zeta^4.                        (5)

Choose the two mu intervals around Delta_a-delta and Delta_a+delta, with every actual pole offset d_a^-,d_a^+ between3delta/4 and5delta/4. They can be rational boxes: approximate each Delta_a within delta/32 and take a rational interval of radius delta/8 around each approximate center shifted by +/-delta. Each interval has width delta/4 and lies within the stated offset range. This requires only an explicit O(delta) energy precision, no exact rationality of the old energies.

All other old Bohr differences are separated from these poles by at least zeta/2. After removing the named pole, every component's regular remainder has magnitude at most4b^2/zeta, by bounding the two column sums by b^2. Define diagonal matrices

    D_+=diag(d_a^-/beta_a),
    D_-=diag(d_a^+/beta_a),
    V_+=F_+ D_+,  V_-=F_- D_-.

Consequently

    ||V_+-I||_infinity<=1/16,
    ||V_-+I||_infinity<=1/16.                   (6)

Indeed each normalized remainder is at most5b^2 delta/zeta^3, and the row has ell entries. Equation5 supplies a stronger bound than required. Therefore V_+ is invertible, ||V_+^-1||_infinity<=16/15, and

    M_c=-V_+^-1 V_-,
    ||M_c-I||_infinity<=2/15<1/4.

Thus every component of M_c ones lies between3/4 and5/4. The positive kernel vector

    c_weight=(D_+ M_c ones,D_- ones)

satisfies [F_+ F_-]c_weight=0 and the explicit component bounds

    9delta/(16b^2)<=c_weight,j<=25delta/(16zeta^2). (7)

All later targets will be rational Hermitian M with ||M||<4. Let Y=8/t_* so that y_a=(M_aa-M_00)/t_* obeys ||y||_infinity<=Y. Also

    ||F_+^-1||_infinity<=4delta/(3zeta^2).

Choose a fixed L_0 satisfying

    L_0 >= (16b^2/9)(4Y/3+4),
    A_weight=L_0 zeta^-2.

Set the zero-route weights

    w(y)=(F_+^-1 y,0)+A_weight c_weight.          (8)

Equations7-8 show every component is at least4delta_0 zeta^2 and at most a fixed constant C_w. This is uniform over the entire target ball and the entire mu box. The potentially large multiplier A_weight does not create a large physical spectral weight: its kernel vector shrinks at the same time. Hold the negative-side weights fixed and let the positive weights vary in a Euclidean ball of radius

    r_x=delta_0 zeta^2.

On these balls, all weights are at least3delta_0 zeta^2 and at most a fixed enlarged C_w. Hence

    c_S zeta^2<=S=sum_j w_j<=C_S,
    c_v zeta<=v_p=sqrt(S)<=C_v,
    p_j=w_j/S>=c_p zeta^2.                      (9)

The core nodes have bounded upper magnitude M_0, pairwise separation at least c_mu zeta^4, and distance from every old Bohr difference at least c_pole zeta^4. Their least positive value is at least zeta/2. Here and below c_*,C_* are positive fixed computable constants assembled from the original certificates and the displayed finite inequalities; none depends on epsilon, N, the selected node or target M. They can be replaced by certified rational lower/upper bounds. In particular c_pole is a positive pole-separation constant, distinct from the bias scalar c_C in4. No compactness constant with an unspecified shrinking dependence remains in this step.

## 4. Jacobi derivatives and hoppings

The following derivative bound is the useful additional estimate. For fixed distinct real nodes mu_j and positive weights w_j, form the square weighted Vandermonde

    V_(j,k)=sqrt(w_j) mu_j^(k-1), 1<=j,k<=m.

Its real QR decomposition V=Q R with positive diagonal R has orthogonal Q. The Jacobi matrix from Gram-Schmidt is J=Q^T diag(mu) Q. Fix the nodes and differentiate with respect to w_i. Then dV=E V dw_i, where E has only its ith diagonal entry1/(2w_i). Write Omega=Q^T partial_i Q, which is skew symmetric. Differentiating QR and multiplying by R^-1 gives

    Q^T E Q=Omega+(partial_i R)R^-1.

The last term is upper triangular. Thus Omega's strict lower triangle equals that of the symmetric matrix Q^T E Q, its upper triangle is the negative transpose, and its diagonal is zero. Therefore

    ||Omega||<=||Omega||_F<=sqrt(2)||E||_F
                              =1/(sqrt(2)w_i),
    ||partial_i J||<=2||J||||Omega||
                     <=sqrt(2)M_0/w_i.          (10)

This proof uses neither a lower Vandermonde determinant nor a general ill-conditioned QR perturbation assertion. The fixed-node derivative has special multiplicative row structure. By9,

    M_J=max_i ||partial_i J||<=C_J zeta^-2.       (11)

Variation of the nodes is not covered by10; numerical grid-node choices will be exact rationals and held fixed during calibration sensitivity analysis.

For hopping lower bounds the Vandermonde determinants are still paid. Let D_j be the normalized moment Gram determinant, D_0=1. Cauchy-Binet and9 give

    D_j>=c_j zeta^(4j^2-2j),
    D_j<=C_j, 1<=j<=m.                           (12)

The lower exponent is2j+4j(j-1), from the weights and squared node differences. Hadamard supplies the fixed upper bound from M_0. Since

    t_j=sqrt(D_(j+1)D_(j-1))/D_j,

each core hopping satisfies t_j>=c_j' zeta^(4j^2-2j+4). With m>=2 and tau=4m^2-10m+10, all core hoppings obey

    t_j>=c_t zeta^tau.                           (13)

Their upper bounds and all core onsite fields stay bounded by M_0. The derivative and hopping estimates solve different problems; neither is substituted for the other.

## 5. Restricted gap, explicit routing and simultaneous calibration

Use the accepted reducing-envelope spaces, not a full-source spectral exclusion. Put n=N+1, B_2=1+b_bus+binom(b_bus,2), b_bus=m+4q. The accepted dimensions give

    D_c=d n^q,
    dim H_2<=d B_2 n^q[1+4qN+16binom(qN,2)],
    M_N<=C_M n^(2q+2),
    C_M=d^2 B_2(1+4q+8q^2).                     (14)

Every zero-route Q/P affine difference has a freely varying coefficient at least n^-4. This follows from the accepted adjacent-swap source gap and the presence of a bus excitation or a nonsymmetric source state. The mu box has widths delta/4; choose fixed router and ferromagnetic intervals with positive fixed widths. A common lower width is c_box zeta^4. The slab argument and the finite-grid margin of the accepted fixed-H resource note therefore give

    delta_zero>=c_gap zeta^4 n^-a,
    a=2q+6.                                     (15)

There is a fully finite search: the affine-form Lipschitz constant in these parameters is at most2+2q(N-1); a mesh at most a fixed multiple of zeta^4 n^[-(a+1)] has a witnessing strict margin. Its cardinality is at most a fixed multiple of zeta^[-4(m+2)]n^[(a+1)(m+2)], a loose polynomial bound. The old spectral and source-enclosure requests needed to certify the differences are O(zeta^4 n^[-(a+1)]). No exact full-code degeneracy oracle is used.

Choose fixed high router energies so their separation Delta_R above all positive gaps is bounded below by a positive fixed constant. For example a fixed interval above2K+2 in the declared units suffices after a fixed routing cap; choose the ferromagnetic interval once as well. The parent's Schur correction has size e<=rho^2/Delta_R. Its actual cone-calibration bounds become, by9-11,

    ||F_+^-1||<=C_A zeta^2,
    C_0<=C_0' zeta^-8,
    C_1<=C_1' zeta^-14,
    delta_C>=c_pole zeta^4,
    r_x=delta_0 zeta^2.                          (16)

Prescribe one routing value

    rho=rho_0 zeta^6 n^-a,                       (17)

where rho_0 is a sufficiently small fixed positive rational. A single such constant satisfies every parent condition simultaneously:

* R rho<=delta_zero/4, R=4q, because zeta^6<=zeta^4;
* 3rho<mu_min/2 because mu_min>=zeta/2;
* e<=delta_C/2;
* ||F_+^-1|| C_0 e<=r_x/2, whose left side is O(rho_0^2 zeta^6 n^-2a);
* ||F_+^-1|| C_1 e<=1/2, whose left side is O(rho_0^2 n^-2a).

For an explicit sufficient choice, take rho_0 strictly below the minimum of the fixed preliminary router cap, c_gap/(4R), 1/12, sqrt(c_pole Delta_R/2), sqrt(delta_0 Delta_R/(2C_A C_0')), and sqrt(Delta_R/(2C_A C_1')), with certified rational lower rounding. All right-hand prefactors are given by the preceding certificates. Thus the exact contraction has factor at most1/2 uniformly over every selected plant, target ball and N. It gives an actual positive calibration solution, not an approximate residual in place of one.

The zero-route many-body spectrum is weight independent. Complete routing perturbation norm is at most R rho, including the branched qubit interactions. The restricted Q/P gap after calibration is consequently

    delta_QP>=c_delta zeta^4 n^-a.               (18)

Only the open core at zero routing is represented by free fermions. No branched XY free-fermion claim is used. Exterior full-source resonances remain possible and irrelevant only in the qualified reducing-envelope sense.

## 6. Responses, counterterms and full correctors

The fixed root-to-leaf-l path contains m-1 core edges and3l+1 routing edges. All4q-3l-1 off-path vertices are in high-energy router subtrees. The exact unique-path cofactor,13,17 and a fixed upper determinant bound yield

    |G_l|>=c_l zeta^[tau(m-1)+6(3l+1)]
                         n^[-a(3l+1)].

Set k=3q+1, r=ak, g=tau(m-1)+6k. Since zeta<=1 and n>=1,

    min_l |G_l|>=c_G zeta^g n^-r.                (19)

The one-particle resolvent upper bound from the same Schur formula is C_R zeta^-4. The lower response estimate uses the particular unique path and its off-path determinants; an inverse operator-norm upper bound alone would not establish it. Graph size/path length stays fixed while sources grow.

For ||M||<=4, v_p>=c_v zeta and |B_ab|>=zeta, so the literal amplitudes satisfy, with u=g+2,

    r_l=2|M_ab|/(t_*v_p|B_abG_l|)
                       <=C_r zeta^-u n^r,
    ||V||<=C_V zeta^-u n^r.                     (20)

There is one old port and q source edges; no N factor is hidden in V. Let U_l=B_bus tensor I_N+I tensor J_F L_hole-omega_l I on the complete one-hole sector, with ||L_hole||<=4. The accepted restricted-source inverse, not an assumed full-source inverse, gives ||U_l^-1||<=delta_QP^-1. The unit normalized highest-weight hole vector gives the exact coefficient B_l as a quadratic form of U_l^-1. Hence

    |A_l|<=C zeta^[-(2u+4)] n^(2r),
    |B_l|<=C zeta^[-(2u+4)] n^(2r+a).

For the actual counterterms u_l^ct=-A_l/N and v_l^ct=-(B_l-A_l)/N,

    ||A2||<=C_A2 zeta^[-(2u+4)] n^(2r+a),
    ell_2<=C_loc zeta^[-(2u+4)] n^(2r+a-1).      (21)

These are full-space norms and physical local coefficients. A2J may leave the first envelope and its off-code action is retained. The mandatory source inverse is inclusion_g1(c+L|g1)^-1 projection_g1. Its one-hole formula is valid because the entire hole sector lies in g1. The formula is never identified with a possibly singular inverse on the full source.

The corrector's column/Frobenius estimates and gamma_PP>=zeta give

    ||Z1||<=C_1 zeta^[-(u+4)] n^x,
    x=q/2+r+a,
    d_bound<=C_d zeta^[-(2u+4)]n^(q/2+2r+a),
    ||Z2||<=C_2 zeta^[-(2u+8)] n^y,
    y=q+2r+2a.                                  (22)

After exact source cancellation and diagonal calibration, the secular D has the same target form as in the accepted fixed-H theorem. Here its scalar c_M need not be uniformly bounded: the root resolvent may cost zeta^-4. The correct bound is

    ||D||<=C_D zeta^-4.                          (23)

This is sufficient. For the actual full-space residuals

    R3=VZ2+A2Z1-Z1D,
    R4=A2Z2-Z2D,

one obtains

    ||R3||<=C_3 zeta^[-(3u+8)] n^p,
    p=q+3r+2a,
    ||R4||<=C_4 zeta^[-(4u+12)] n^h_4,
    h_4=q+4r+3a.                                (24)

The terms VZ2 and A2Z1 have the same worst zeta power3u+8. The term Z1D is smaller. A2Z2 controls the stated R4 power. These are not compressed residual norms; perturbed dynamics need not preserve H_2.

## 7. A uniform xi, runtime and incident cap

Choose N=max(2,ceil(C_N epsilon^-2)) with a fixed rational C_N>=max(1,[64(t_*+w_bar)4/t_*]^2), using a certified rational upper majorant. Let v=3u+8 and prescribe

    xi=c_xi epsilon zeta^v n^-p,
    T=t_*/xi^2.                                 (25)

All constants in21-24 have been separated from their zeta,n powers. Put A_corr=2C_1+2C_2+(t_*+w_bar)(C_3+C_4) and J1=J2=1/t_*. Choose a fixed positive rational c_xi below the minimum of1, 1/[64(A_corr+1)], 1/sqrt[64(1+4w_bar/t_*)], J1/(2C_V+J1), and sqrt[J2/(C_loc+J2)], again with certified lower rounding. The actual corrector estimate is

    2xi||Z1||+2xi^2||Z2||
        +(t_*+w_bar)(xi||R3||+xi^2||R4||).       (26)

Its zeta exponents after25 are respectively2u+4,4u+8,0,2u+4, all nonnegative. Its n exponents are nonpositive because p>=x, 2p>=y and2p-h_4=q+2r+a>0. Thus a fixed c_xi makes26 at mostepsilon/64. It also makes the finite mean-holding error xi^2 w*4/t_* at mostepsilon/64 and

    xi ell_V<=J1, ell_V=2||V|| bound,
    xi^2 ell_2<=J2.

The load zeta powers are v-u=2u+8 and2v-(2u+4)=4u+12. No unbounded local term is suppressed only in prose.

Every base core/router field or hopping, source frequency and J_F lies in a fixed bounded interval: H_lambda has uniformly bounded norm, all mu lie below2K+1, and rho is bounded above by fixed rho_0. Choose fixed M_E for their actual positive onsite/edge blocks and a fixed old reserve R_s>=||H||+Lambda_0||C||. Including the actual attenuated bias blocks gives a common added incident bound

    J_*=J_C+R_s+7M_E+J1+J2.                     (27)

There is exactly one old/new bus edge. The bias's allowed occupied-old-edge additions are a separate stated premise, not a consequence of port controllability. Positive bus/port/source reserves and the positive blocks built from negative counterterms are the same actual blocks as in the accepted parent. Pointwise implementation slack must be separately charged if a perturbed realization is also claimed to obey27.

Since n=O(epsilon^-2) and zeta=c_z lambda_0^kappa epsilon^kappa,

    T=t_*c_xi^-2 epsilon^-2 zeta^-2v n^2p
      <=C_T epsilon^[-(2+4p+2kappa v)].          (28)

For example C_T=t_*c_xi^-2(c_z lambda_0^kappa)^-2v(C_N+4)^2p is an explicit sufficient fixed prefactor, enlarged by certified rational rounding if required.

This explicitly discharges equation36 of the fixed-H note on the supplied admissible-bias domain. Its prefactor is computed from the fixed original certificates via the positive lower/upper bounds above. The only growing installed resources in this ledger are the number of sites, duration and precision demands; the incident cap stays fixed. Global added norm/energy and total reserves are bounded only by O(n), and second moments by O(n^2), from the actual sum of O(n) bounded local blocks. These are mathematical operator bounds, not a physical energy-measurement identification.

## 8. Noncircular target transfer, window and exact phases

All bounds through28 hold uniformly over ||M||<=4 and were obtained before selecting M. The complete choice order is therefore:

1. Fix original certificates and epsilon. Select Lambda=lambda_0 epsilon, the certified bias node lambda, and zeta.
2. Select N, rational cone box/grid point, restricted gap and rho, using only the target norm bound4.
3. Use the uniform majorants to fix xi and T by25.
4. Form the actual interaction-frame unitary

       U_T=exp(iT H_lambda) W exp(-iTH).

   Find rational Hermitian M in the selected old-energy basis with ||M||<4 and ||exp(-iM)-U_T||<epsilon/64.
5. Instantiate the already uniformly certified exact calibration, source amplitudes/counterterms and controller phases for that M. Do not recompute T from these actual smaller constants.

The bounded-log existence and decidable-support construction is reused from the qualified transfer source. It can also be made a fixed finite search: a Hermitian logarithm with norm<=pi exists. Choose a dyadic mesh spacing between epsilon/(2048d) and epsilon/(1024d), anchored at zero, and impose Hermiticity exactly. Rounding the real/imaginary entries of that logarithm yields operator error belowepsilon/128 and norm below4 with a fixed slack. Scan the finite grid of integer mesh multiples in a fixed entry box containing[-pi,pi], evaluating the norm and exponential with fixed certified error smaller thanepsilon/512; a strict threshold at epsilon/64 accepts a witness. Points on boundaries are simply not accepted. This avoids a logarithm branch, an arbitrary equality oracle and an uncontrolled support decision. The fixed dimension makes its grid polynomial in1/epsilon, although no practical search cost is claimed.

For every decidably nonzero M_ab choose

    exp(i phi_l)=(M_ab/|M_ab|)
                         (conj(kappa_ab)/|kappa_ab|),
    kappa_ab=-v_p r_l B_ab G_l.                  (29)

Set the coupling to zero and choose any phase on zero entries. The mean generator is M/t_* directly. This is equivalent to the original bus theorem with its conjugated gate logarithm; the apparent exp(i omega_l T) source-phase factor cancels that conjugation. It is not legitimate to confuse U_T with the original gate G_T=W exp(-iTH) exp(iTH_lambda). The interaction-frame order here implements the correct endpoint exactly up to the approximate logarithm.

Let Phi(t)=|0_bus> tensor tensor_l exp(-it omega_l N_l)|Alpha_l(phi_l)>, retaining every source and bus output. Use the actual installed reserve

    R_total=R_s+lambda R_C+R_bus(M)
                  +xi R_V(M)+xi^2 R_A2(M).

At t=T+s the scalar-adjusted comparator for2 is

    exp[-i chi(t)] Phi(t)
                     tensor [exp(-isH)Wexp(-iTH)],
    chi(t)=R_total t+c_M xi^2 t+lambda c_C s.    (30)

It acts on the complete arbitrary old input with identity on any reference. There is no additional lambda c_C T: U_T compensates the entire biased aging through T, including its scalar part. The physical bias reserves lambda R_C act for the full T+s and remain in R_total. Literal old scalar parts remain in both displayed H evolutions. No assumption lambda T<<1 is made or needed.

The five isometry errors are the full corrector26, complete-source fluctuation, mean holding rotation, approximate logarithm, and continuing nonscalar bias lambda w a_C. Choose the fixed constants as above so each is at mostepsilon/64. Their total trace contribution is at most10epsilon/64. The supplied initial state may have trace error at mostepsilon/8 relative to the specified controller product tensored with its exact unconditional old/reference marginal; there is no postselection or replacement of that marginal. A self-adjoint error E(t) of the complete installed generator, including omitted interactions, may satisfy integral_0^(T+w)||E(t)||dt<=epsilon/16. Its full-output trace cost is at mostepsilon/8. The initial-state cost is also at mostepsilon/8. A separately allocated release-time/phase tolerance can use the remaining slack; it is not supplied for free. Thus the stipulated overall epsilon can be met with all outputs retained.

For comparison, keeping a fixed nonscalar C at coefficient one retains the earlier finite-window obstruction. H=0, C=Omega n, W=I and w=pi/Omega sends an endpoint-corrected |+> to |-> under the continuing bias. Endpoint recalibration cannot remove that defect. This result pays it by4 and explicit admissible attenuation, not by deleting the bias after T or assuming a native switch.

## 9. Concrete precision requests and their uniform dependence

The remaining numerical estimates use a selected strictly certified rational grid point. The grid-selection map is not claimed differentiable. The base node, router, ferromagnetic and routing values are exact rational design data; their physical rounding is charged in the installed coefficient budget.

There are at most C_terms n entries in a fixed normalized local operator dictionary and ||K||<=C_K n for the complete installed generator. To achieve integrated generator error of a fixed fraction of epsilon, it suffices to request each installed coefficient to absolute accuracy

    eta_loc=c_loc epsilon^3 zeta^(2v)n^[-(2p+1)], (31)

with fixed c_loc sufficiently small. Indeed n(T+w)eta_loc<=C epsilon. Upward reserve roundings, omitted couplings and timing errors need allocations within the full-generator/initial-state budgets; positivity and pointwise incident slack are independently checked. Numerical approximation does not replace literal H physically.

For clarity, the dependence of calibration on supplied old-energy-basis data is now priced explicitly. Let eta bound errors in the finite E_a,B_ab,target entries and fixed time data, while holding the selected rational mu,nu,J_F,rho,zeta fixed. Work within a certified fraction of the strict margins. The pole denominators are >=c zeta^4, beta_a>=zeta^2, D_+/-=O(zeta^2), F_+=O(zeta^-4), and F_+^-1=O(zeta^2). Direct differentiation of the finite rational formulas gives

    delta F=O(zeta^-8 eta),
    delta D_+/-=O(zeta^-2 eta),
    delta V_+/-=O(zeta^-6 eta),
    delta c_weight=O(zeta^-4 eta),
    delta w_-=O(zeta^-4 eta).                   (32)

The last estimate is sharper than using the whole c_weight vector: w_-=A_weight D_- ones, with A_weight=L_0 zeta^-2 fixed. The calibrated positive-side Jacobian is F_+ plus the routed correction and has inverse norm at most2||F_+^-1||=O(zeta^2), by the contraction. At fixed positive-side x, variations of w_- change J by O(zeta^-6 eta) using10. One-particle resolvents have norm O(zeta^-4), so the direct variation of the calibration equation is O(zeta^-14 eta). Multiplying by the inverse calibrated Jacobian gives

    delta x=O(zeta^-12 eta),
    delta B_bus=O(zeta^-14 eta),
    delta v_p=O(zeta^-13 eta).                   (33)

These are local uniform bounds, integrated along the short input segment. Small eta keeps that segment inside a fixed fraction of the positive-weight and pole margins. All factors are explicit powers; no unpriced higher derivative or a global smooth selection theorem is used. The contraction and inverse-Jacobian comparison can equivalently prove33 by subtracting the two equations.

The resolvent identity then gives

    delta G_l=O(zeta^-22 eta),
    delta r_l=O(zeta^[-(2u+20)]n^(2r) eta).       (34)

For the second estimate use19, v_p>=c zeta and |B_ab|>=zeta. The relative Green error costs zeta^[-(g+22)]n^r eta and dominates the relative port and B errors. On the joint one-hole matrix, the same numerator error from33 and18 give

    ||delta U_l^-1||=O(zeta^-22 n^(2a) eta).

Differentiating the exact quadratic forms consequently bounds every A_l/B_l variation by

    C zeta^[-(3u+24)] n^(3r+2a) eta.             (35)

For example2r_l delta r_l times the inverse contributes zeta^[-(3u+24)]n^(3r+a); the inverse variation contributes zeta^[-(2u+22)]n^(2r+2a). Equation35 bounds both. Divisions by N and physical factors xi,xi^2 only improve the conservative bound on installed coefficients. Reserve functions max(0,-x) are1-Lipschitz.

Let Q_prec=2p+3r+2a+1. A sufficient request on the supplied old-energy-basis numerical data is

    eta_in=c_in epsilon^3 zeta^(9u+40)n^-Q_prec. (36)

This is31 times the inverse Lipschitz allowance in35, because2v+3u+24=9u+40. Reducing the fixed c_in enforces every positive-neighborhood and inverse-stability condition used in32-35, the Green sign margin, and the smaller spectral-grid enclosure budget. It also pays phase-frequency products: eta_in is smaller than a fixed multiple ofepsilon/[n(T+w)] and epsilon xi^2/n. No inverse of an unclassified full-source operator is evaluated.

If the data are initially supplied as original matrix entries H,C,B rather than in the selected energy basis, one additional zeta factor suffices. The selected old energy gaps are >=zeta. Isolated rank-one spectral projectors vary by O(eta_matrix/zeta), as follows by integrating the resolvent identity on a circle of radius proportional to zeta. For each projector select a coordinate column with norm at least1/(2sqrt(d)), possible because one diagonal is at least1/d; a finite coarse strict test chooses a chart. Normalize that column to obtain an eigenvector with fixed positive chart overlap. This avoids a global eigenvector-phase selection. Within that chart the eigenvectors, transformed B and target matrices have Lipschitz constant O(zeta^-1). Thus it suffices to request

    eta_original=c_orig epsilon^3
                          zeta^(9u+41)n^-Q_prec. (37)

The selected bias node and chart are certified discrete choices; differentiation across their boundaries is not asserted. The preceding threshold accuracy is sufficient to select them with margin. All constants in36-37 are functions of fixed original certificates.

The late target U_T can be evaluated to O(epsilon) because Hermitian Duhamel gives error at most T times the Hamiltonian input error, plus the W error and fixed norm times the T error. Requests36-37 are smaller than the requisite O(epsilon/(T+1)); the additional basis conversion is already priced. For a concrete matrix exponential evaluation, scale time by a power of two S=O(T+1) until the exponent norm is bounded, approximate the unitary short step to O(epsilon/S), and square. The telescoping error is at most S delta exp(S delta), so O(log(T+1)+log(1/epsilon)) requested arithmetic bits suffice in fixed dimension with a fixed extra rounding allowance. A finite Taylor bound supplies the short step. No branch of a logarithm is evaluated.

On the rational M grid, every nonzero entry has modulus at least the mesh spacing. Computing M_ab/|M_ab| thus needs only the corresponding O(log(1/epsilon)) additional bits. B_ab/|B_ab| costs at most one zeta inverse, already covered, and the sign of the real G_l is certified by19 and34. The complete product-source norm changes by at most qN times an individual phase error, so require per-source phase accuracy O(epsilon/n). A release-time error costs at most2||K|| |Delta_t| in trace norm; O(epsilon/n) is a sufficient demanded timing tolerance. These are physical requests, not preparation or clock suppliers.

Since zeta is proportional to epsilon^kappa and n=O(epsilon^-2),37 requests at most

    C+[3+kappa(9u+41)+2Q_prec]log2(1/epsilon)     (38)

absolute bits, with rounding and fixed constants added. Equation31 requests O((P+3)log(1/epsilon)) bits. These rates can be enormous in d and certificates. Their meaning is strictly requested precision, not the time an arbitrary computable oracle takes to deliver those bits.

The accepted integer/binomial source basis remains applicable. Its exact rational rank selection and LDL arithmetic need no new data oracle. The conservative internal guard precision32(g_src+1)^2[qN+ceil log2(g_src+1)+ceil log2(2qN+1)+2], where g_src=O(n^(q+2)), is unchanged. Add the logarithm of the desired spectral tolerance, now O(log(1/zeta)+log n). Thus internal source-coordinate requests remain O(n^(2q+5)+log(1/zeta)), polynomial in1/epsilon. The old source coordinate conditioning is not ignored or confused with old-data oracle running time.

The remaining calibration arithmetic also has a finite polynomial precision prescription. For the m-by-m core, m is fixed, the moment determinants have the explicit lower bounds12, S>=c_S zeta^2, and every numerator is a bounded-degree polynomial in bounded nodes and weights. Evaluating the finite rational/square-root Gram formulas with certified enclosures therefore costs only an additional fixed multiple of log(1/zeta)+log(1/tolerance) bits; the multiplier is obtained by counting those fixed operations and their displayed denominator powers. Evaluate the contraction to a prescribed absolute map error e_map and iterate until the geometric tail is no larger than e_map. Its fixed-point error is then at most a fixed multiple of e_map. For example e_map<=c zeta^2 eta_in, with a sufficiently small fixed c, makes the Jacobi arithmetic error at mosteta_in by10, below the input sensitivity allowance33. This gives O(log(1/e_map)) iterations, without asserting an oracle-time bound.

For the one-hole inverse, its dimension D_h=b_bus N is polynomial. Round its entries to rationals with operator error at most delta_QP^2 tau_inv/4 and at most delta_QP/4, where tau_inv is the required inverse accuracy. The resolvent identity then gives inverse error at mosttau_inv, and the rounded Hermitian matrix has gap at leastdelta_QP/2. Its determinant has absolute value at least(delta_QP/2)^D_h. Exact rational adjugate/determinant evaluation or pivoted rational elimination avoids an unjustified floating-point inversion. With a common dyadic entry denominator, the integer bit sizes are O(D_h[B_entry+log(D_h+1)+1]), where B_entry=O(log n+log(1/zeta)+log(1/tau_inv)); a conservative larger polynomial bound is equally sufficient. One explicit sufficient choice is tau_inv<=c eta_loc zeta^(2u)n^(-2r), which pays the r_l^2 multiplier in every self-energy, with fixed c from20. All such requests are inverse polynomials by31-37. These arithmetic requests remain polynomial after zeta is tied to epsilon; they do not call a full-source inverse, construct exponential source vectors or assume a favorable arbitrary-oracle runtime.

## 10. Preserved failures, scope and handoff

The prior fixed-H proof did not by itself justify uniformity. In particular its c_M bound and the parameter-box width shrink here: c_M can grow as zeta^-4 and the box width is O(zeta^4). Treating either as a fixed constant would be an invalid shortcut. They are explicitly paid in15,23-28. Merely invoking compactness on each selected plant would not produce1.

The old growing-path counterexample also remains: B_N=4I+N^-1 A_path has a fixed spectral gap at frequency1 but endpoint inverse entry at most2^-N N^[-(N-1)]. Polynomial dimension and spectral gap alone do not bound routed response. This construction avoids that failed inference only because the bus graph and maximum path length are fixed; every routed product is explicitly in19.

The physical premise that survives is the supplied admissible bias direction with nonzero leading determinant, including its occupied-old-site/edge access and attenuation. No proof here manufactures it from the original generic Lie-control premise. No native supplier of coherent source purity/phase, vacuum routers, release timing, isolation, energy or long-time calibration is added. No halt, disposal of controller outputs, reset or reuse is concluded. A preparation timeline before runtime must obey its separately qualified chronological contract; offline design time is not silently identified with the experiment's T.

All new load-bearing reasoning is analytical. The source selection/transfer/corrector identities are reused at exact qualified parent identities. There is no new numerical PASS claim, scientific execution, old checker rerun or independent parent validation. Root should check the QR derivative, cone-weight scaling, calibration sensitivity and exponent propagation before accepting this extension. Only the assigned source directory was written; editable prompts changed: none.

<!-- Immutable source: shrinking_bias_resource_exposed_check/REVIEW.md -->

# Exposed check: Jacobi weight derivatives and shrinking-bias precision

Disposition: the two requested steps are supported under the stated post-selection margins and qualified parent premises. I find no counterexample or load-bearing power error in them. The fixed-node Jacobi estimate admits a separate proof with the stronger bound M_0/w_i. Section9's input-precision exponent is sufficient for the recomputed calibration, response, full counterterm and phase sensitivities. This is scoped support, not acceptance of the entire new theorem or fresh validation of its spectral-selection, envelope, transfer and physical premises.

This review is source-exposed, same-model and analytical. The root supplied the finished argument and requested an adversarial check; the reviewer had previously checked related preparation/resource results. No numerical or symbolic scientific program was run. The only executable work was source-identity capture and final metadata hashing. There is no retained-audit claim, model-family replication, or desired-outcome assumption.

## 1. Exact sources and limits

The only source files read for this task were:

* Complete final DERIVATION.md, 37212 bytes, SHA256 `2bfb24cce9760be23d750b3b2a190b3110bc0326c035488aae004d1de7849a74`.
* Its SOURCE_MANIFEST.json, 11765 bytes, observed SHA256 `f1c98369443cf21b9751fbe46296f0c3231850fd3d3bd15552b6c3b290787583`, read for identity/exposure. Its listed23 dependencies were not opened by this task, nor was its complete historical archive validated.
* Accepted fixed-plant FINAL_QUALIFICATIONS.md, 7196 bytes, SHA256 `e50497e74e2022f97e6b1a42ff8bf176c2c7b30cd16b68d22b18f503457e541b`, read completely.

Full original paths, exact captures and per-source coverage are in SOURCE_IDENTITIES.json. The author's freeze was not read; it was outside the requested read set. These three captures are the recovery sources for this review. Existing qualified premises are reused only at the scope explicitly stated in the final derivation and qualifications. In particular, a supplied admissible attenuable C with its leading-determinant certificate is not manufactured from Lie controllability, and the required source inverse remains the qualified reducing-envelope inverse.

## 2. Separate fixed-node proof, including normalization

Fix m distinct real nodes mu_j and positive raw weights w_j. Let p_0,...,p_(m-1) be the orthonormal real polynomials, with positive leading coefficients, for

    <f,g>_w = sum_j w_j f(mu_j)g(mu_j).

Write P_(j,k)=p_k(mu_j), W_d=diag(w_j), and D_mu=diag(mu_j). Since the nodes are distinct, the square evaluation matrix is invertible and

    P^T W_d P=I,  P P^T=W_d^-1,
    J=P^T W_d D_mu P=P^-1 D_mu P.

J is the usual Jacobi matrix; multiplication by x and polynomial degree imply its tridiagonal form, and the leading-coefficient convention gives positive adjacent hoppings. It is orthogonally similar to D_mu via W_d^(1/2)P, so ||J||<=M_0 whenever max|mu_j|<=M_0.

Differentiate only w_i. Set

    T_i=P^-1(partial_i P),  u_i=P^T e_i,  A_i=u_i u_i^T.

The derivative of a degree-k polynomial has degree at most k, so T_i is upper triangular in ascending degree order. Differentiating orthonormality gives

    T_i+T_i^T=-A_i.

Completeness gives ||u_i||^2=(P P^T)_ii=1/w_i. Also J u_i=mu_i u_i, so A_i commutes with J. Define Omega_i=T_i+A_i/2. It is skew symmetric, its strict lower triangle is A_i/2, and its upper triangle is the negative transpose. Differentiating the similarity J=P^-1 D_mu P now yields

    partial_i J = [J,T_i]=[J,Omega_i].

Moreover,

    ||Omega_i||_F^2
      = (1/4)[(||u_i||^2)^2-sum_k(u_i,k)^4]
      <= 1/(4w_i^2).

It follows that

    ||partial_i J|| <= 2||J|| ||Omega_i|| <= M_0/w_i.

This is stronger than the author's sqrt(2)M_0/w_i and establishes the required O(zeta^-2) bound when every raw weight is at least c zeta^2. No Vandermonde inverse norm or node-separation factor entered this derivative estimate. For a finite perturbation, integrate on a positive-weight segment and sum the m coordinate bounds; m is fixed.

Regularity is not an extra assumption. The weighted Vandermonde has full rank. Its Gram matrix is positive definite, its positive Cholesky factor R is smooth on that open cone, and Q=V R^-1 is the unique positive-diagonal QR factor. Consequently the polynomial coefficients and the derivatives above exist smoothly for positive weights with the nodes held fixed. Numerical evaluation may be poorly conditioned; the derivative identity does not license uncontrolled floating-point QR. The separate moment-minor arithmetic bounds remain necessary.

Normalization also introduces no missing factor. Replacing raw weights by probabilities w_j/S scales V by S^-1/2 and R by the same factor, leaving Q and J unchanged. When differentiating normalized V with respect to a raw w_i, the row-scaling derivative acquires the extra scalar term -I/(2S). Its orthogonal conjugate is still scalar, so it contributes no skew part. The author's raw-weight derivative is therefore the derivative of the normalized Jacobi construction as well.

Boundary: this proof does not control moving nodes. Its use in section9 is legitimate only because mu,nu,J_F,rho,zeta and the selected bias/grid/chart choices are held fixed after strict certification. Differentiating a grid-selection map or applying this bound to arbitrary Vandermonde perturbations would be a different, unjustified claim.

## 3. Recomputed old-data propagation

Use eta for a simultaneous absolute error in the finite old-energy-basis data E,B,M,t_* at a fixed certified design point. Constants below depend on the fixed original certificates and fixed dimension. All line segments must stay within a fixed fraction of the pole, positivity and gap margins. I first recompute the Lipschitz powers; section4 checks that the proposed eta is small enough for those margins.

With d_a=Delta_a-mu_j=O(zeta^4), beta_a>=zeta^2 and beta_a bounded above,

    delta beta=O(eta),
    D=d_a/beta_a=O(zeta^2),
    delta D=O(zeta^-2 eta).

The last estimate includes both delta d/beta and d delta beta/beta^2; the latter is no worse than O(eta). Every pole denominator is at least c zeta^4. Direct differences of the finite resolvent fractions therefore give

    delta F=O(zeta^-8 eta), F=O(zeta^-4),
    delta(F D)=O(zeta^-6 eta).

The normalized cone matrices V_+,V_- have uniformly bounded norms and V_+^-1 is uniformly bounded. Thus the variation of -V_+^-1 V_- is O(zeta^-6 eta). Multiplying by D gives

    delta c_weight=O(zeta^-4 eta).

For the negative weights one must use their more specific formula, rather than that full-vector bound:

    w_-=L_0 zeta^-2 D_- ones,
    delta w_-=O(zeta^-4 eta).

Here the positive multiplier and zeta are fixed design data. This distinction in the author's equation32 is valid and matters for the subsequent exponent.

For the calibrated positive weights x, the full derivative in x is F_+ plus its routed correction. The accepted contraction hypothesis gives inverse norm O(zeta^2). At fixed x, the preceding delta w_- changes the Jacobi matrix by O(zeta^-6 eta), using the separately proved weight derivative. The unperturbed one-particle resolvent has norm O(zeta^-4). Its variation costs two resolvents, hence O(zeta^-14 eta). Changes in S=sum w, B and the old frequency arguments give weaker powers. The calibration equation has the structure S times a finite B-weighted root resolvent, minus the prescribed target diagonal differences. Its direct input variation at fixed x is therefore O(zeta^-14 eta).

Multiplication by the calibrated inverse Jacobian yields

    delta x=O(zeta^-12 eta),
    delta B_bus=O(zeta^-14 eta),
    delta v_p=O(zeta^-13 eta).

The final estimate uses v_p=sqrt(S)>=c zeta. These are local finite Lipschitz estimates, not merely formal derivatives at one point: the contraction/implicit-function argument has a common interior margin and the estimates can be integrated along the small input segment. No higher derivative is required.

Two resolvent factors then give

    delta G_l=O(zeta^-22 eta).

Since |G_l|>=c zeta^g n^-r and u=g+2, the relative Green error is at most O(zeta^-(u+20)n^r eta). It dominates the relative v_p error O(zeta^-14 eta), the B error O(zeta^-1 eta), and the fixed time-data error. From

    r_l=2|M_ab|/(t_*v_p |B_ab G_l|)

one obtains

    delta r_l=O(zeta^-(2u+20)n^(2r) eta).

This bound does not divide by |M_ab|. At a zero target entry, use the Lipschitz inequality ||M_ab|-|M'_ab||<=|M_ab-M'_ab|. A relative-amplitude derivative through a zero entry would be invalid, but the stated absolute bound remains valid there.

For the one-hole inverse, delta U_l=O(zeta^-14 eta) and ||U_l^-1||=O(zeta^-4 n^a). The resolvent identity gives

    ||delta U_l^-1||=O(zeta^-22 n^(2a) eta).

The self-energy variations are bounded by r_l delta r_l times the inverse and r_l^2 times its variation. Their two worst orders are

    O(zeta^-(3u+24)n^(3r+a) eta),
    O(zeta^-(2u+22)n^(2r+2a) eta).

The claimed common upper bound O(zeta^-(3u+24)n^(3r+2a) eta) dominates both. This validates equation35 for A_l and B_l without dropping the nonsymmetric one-hole component.

For completeness, summing the actual counterterm blocks gives the full-space perturbation estimate

    ||delta A2||
       <=sum_l [N|delta u_l^ct|+(N-1)|delta v_l^ct|]
       <=sum_l [2|delta A_l|+|delta B_l|].

Thus the same self-energy bound controls the complete unscaled A2 error; there is no extra missing N and no projection onto the source code. The conservative per-installed-coefficient bound used in section9 is safe. Positive reserve maps max(0,-x) are1-Lipschitz, and all of their actual multiplicities must still be included in the local dictionary or full norm sum. Multiplication by xi and xi^2 only improves these conservative installed-error bounds.

## 4. Precision, stability neighborhoods and phases

Write Q_prec=2p+3r+2a+1 and v=3u+8. Multiplying the proposed input tolerance by the preceding worst coefficient sensitivity gives exactly

    [epsilon^3 zeta^(9u+40)n^-Q_prec]
       [zeta^-(3u+24)n^(3r+2a)]
      =epsilon^3 zeta^(2v)n^-(2p+1).

This is the claimed eta_loc. The O(n) local dictionary and T=O(epsilon^-2 zeta^-2v n^2p) consequently give n(T+w)eta_loc=O(epsilon), with a sufficiently small fixed prefactor. Literal old H is not physically replaced by its numerical approximation.

The required small neighborhoods are also paid. Sufficient sample conditions are eta much smaller than zeta^4 for poles, zeta^14 for the positive-weight margin after calibration, zeta^18 n^-a for the one-hole inverse, zeta^(u+20)n^-r for the sign/nonzero Green margin, and zeta^4 n^-(a+1) for the old-frequency contribution to the spectral-grid margin. The proposed exponent9u+40 and n exponentQ_prec dominate these conditions; for d>=2, u>=32. The fixed prefactor c_in can therefore enforce all of them together. This does not require moving a certified discrete choice as the input enclosures are refined.

The scalar and phase terms are not exceptions to the error accounting. Actual reserve perturbations are part of the full generator and hence paid over T by eta_loc. The secular scalar c_M is a root-resolvent quadratic form plus a target diagonal constant. The same estimates give delta c_M=O(zeta^-22 eta); its phase multiplier xi^2(T+s) is bounded by t_*+w. Frequencies in the complete freely rotating source state cost O(n(T+w)eta). In fact

    n T eta_in
       =O(epsilon zeta^(3u+24)n^-(3r+2a))
       <=O(epsilon).

The exact sign of the real G_l is certified by the already paid nonzero margin. Phase normalization of B_ab costs one zeta inverse. On the exact rational target grid every nonzero |M_ab| is at least a fixed multiple of epsilon; its normalized phase can be computed to O(epsilon/n), including that inverse-epsilon factor, with the stated logarithmic bit requests. Exact support is decided from rational entries, not floating estimates. An argument representative is unnecessary.

The original-matrix request with one additional zeta factor is sufficient for local energy-basis conversion. Isolated spectral projectors have O(eta_matrix/zeta) variation. A coordinate-column chart with a fixed positive overlap has a uniformly bounded normalization denominator, so the same order controls eigenvectors and transformed fixed bounded matrices. Each chart and the bias node must be selected by a strict certified test and then held fixed; no globally smooth eigenvector phase choice is being asserted.

One distinction is essential: U_T depends on old data with a T factor, whereas a *selected rational M* is exact design data. The proof must not differentiate a branch of log(U_T), or assume the finite-grid selection map is Lipschitz. Instead compute certified enclosures for U_T, choose an exact rational M by the strict norm/exponential predicate, and charge its separate approximation residual. The proposed original-data tolerance is smaller than what that U_T evaluation needs, even after basis conversion: (T+1)eta_original/zeta=O(epsilon) with large remaining slack. Subsequent calibration uses that exact M; the old-data calibration error is governed by eta_in, not by an unpriced derivative of a selected logarithm. This is the order actually stated in sections8-9 and is sufficient.

Arithmetic precision must be implemented with norm-aware allowances. When entrywise rounding a D_h-dimensional one-hole matrix, divide the requested operator error by at least D_h; this adds only O(log n) bits. The author's inverse-rounding prescription then gives the desired inverse error by the resolvent identity. The normalized one-hole vector introduces no hidden conditioning: its quadratic form may be evaluated exactly as N/(N-1) times the quadratic form of the rational vector e_1-ones/N, so no numerical normalized-vector error need be introduced. Alternatively charge that vector's approximation with its r_l^2||U_l^-1|| multiplier. Both are inverse-polynomial requests.

The separate moment-minor formulas and contraction error allowance cover core arithmetic; the fixed-node derivative alone would not. The independent source-coordinate precision remains the qualified integer/binomial arithmetic premise. External logarithmic bit requests, internal polynomial guard precision, and arbitrary-oracle response time are different assertions. Nothing here proves a physical scheduler, calibration supplier or polynomial oracle wall time.

## 5. Target order, time and remaining boundaries

The chronological target order is consistent. The effective old evolution at T is e^(-iTH_lambda)e^(-iM). With e^(-iM) approximating

    U_T=e^(iTH_lambda) W e^(-iTH),

the endpoint is W e^(-iTH), as required. Holding for s yields e^(-isH_lambda) W e^(-iTH), up to the separately paid mean-holding term. Factoring C=c_C I+(C-c_C I) gives the scalar e^(-i lambda c_C s) and the residual window cost lambda s a_C. Therefore the displayed +lambda c_C s in chi is correct, and no extra +lambda c_C T belongs there. Bias reserves remain in R_total for the entire T+s.

The phase rule without an extra e^(i omega_l T) is also consistent with this interaction-frame M: its direct mean is M/t_*. Reintroducing the original gate-frame phase factor without the matching conjugation would double-count it. Runtime T must be selected from the uniform target-ball bounds before the rational-M search and must not be reset from smaller, later target-dependent constants. The finite logarithm-grid search has a genuine witness margin: rounding a norm<=pi Hermitian logarithm gives norm<4 and an exponential discrepancy strictly below the acceptance threshold. Approximation errors in U_T, its exponential and the norm predicate need a fixed subdivision of that margin.

No assumption lambda T is small is needed. The nondiminishing fixed-bias window obstruction remains, as does the growing-path response counterexample. Neither is refuted by this conditional supplied-direction, fixed-bus construction. The specific arithmetic check of the displayed exponent for d=2 gives m=2,q=1,r=32,p=113,tau=6,g=30,u=32,v=104,kappa=3 and P=1078; this is an algebraic consistency check, not validation of every imported spectral lemma.

The requested derivative and precision steps therefore support the proposed uniform extension *conditional on the other stated and qualified hypotheses*. The scope does not extend to a generic Lie-control premise, unsupplied old-edge bias access, an inverse on the full source Hilbert space, a growing bus route, an unknown-target logarithm continuity theorem, a physical precision supplier, preparation before T without its chronological contract, or halt/reset/reuse.

## 6. Evidence and handoff

No scientific execution or old-program replay occurred. No actual failed computation or counterexample was produced; the rejected inferences above identify precise scope boundaries, not empirical failures. The independent work is the weighted-polynomial derivative proof, recomputation of the sensitivity chain and its stability/phase budgets, and the target-order check. Root retains responsibility for the remaining full-argument review and acceptance.

PROGRESS_01.md preserves the intermediate analytical checkpoint. Source capture and final freeze verify only the three selected text identities and this local packet. No canonical, Git, PR, audit, cache, graph, lock, axiom, publication or other-chat changes were made. Editable prompt files changed:none. All writes stayed in the assigned exposed-check directory.

<!-- Immutable source: shrinking_bias_resource_root_review/FINAL_QUALIFICATIONS.md -->

# Qualified source acceptance: uniform resources for a supplied shrinking bias

The root accepts the conditional result in final derivation2bfb24cc, with the scoped exposed review and the qualifications here. It closes the fixed-plant resource note's equation36 uniformity obligation on the explicitly supplied admissible-bias domain. It does not prove that the required bias/control exists for an arbitrary old plant, furnish a native implementation, identify measured physical energy or ratify retained status. Publication remains pending.

Fix the complete finite old dimension d, original H,C,B, full onsite/nearest-neighbor decomposition and positive reserves for C, actual permission to attenuate those added blocks, port/geometry/isolation and fixed bus graph. Supply a positive rational lower certificate for the complex Krylov Gram determinant of C,B, fixed norm/time/window bounds, and the qualified source/calibration premises. The literal H terms remain at coefficient one. Computable names for all finite data are necessary for the effective prescription; norm bounds alone are insufficient. The qualified reducing source inverse is mandatory, while V,A2 and residual norms are on the full physical space. No branched qubit spectrum is replaced by a free-fermion spectrum.

The selected-point separation bound zeta=c_z Lambda^kappa, Lambda=lambda_0 epsilon, kappa=q(2q+1), follows from the separately accepted quantitative selection. The positive pole cone is then rebuilt uniformly: delta proportional to zeta^4, positive raw weights bounded below by a fixed multiple of zeta^2 and above by a fixed constant, a target ball of fixed norm, and a parameter ball of radius proportional to zeta^2. Core norm is bounded, hopping lower bounds are explicit, and the routed coupling rho=rho_0 zeta^6 n^(-a) has an explicit fixed positive prefactor. This pays the shrinking spectral margins and calibration Jacobian without an unspecified compactness constant.

The key fixed-node Jacobi derivative is supported by two arguments. The author's weighted-QR calculation gives sqrt(2)M_0/w_i. The separate exposed check uses weighted orthogonal polynomials: differentiating their triangular change of basis gives T+T^T=-u_i u_i^T, completeness gives ||u_i||^2=1/w_i, and [J,u_i u_i^T]=0 leaves a skew commutator with norm at most M_0/w_i. Root reconstructed this argument and its signs. Raw-weight normalization adds only a scalar term and does not change J. Smoothness follows from positive Gram/Cholesky factors at distinct fixed nodes. This bound does not apply to moving nodes or arbitrary Vandermonde perturbations; arithmetic conditioning still requires the separate moment-minor bounds.

With q=d(d-1)/2, m=2(d-1), a=2q+6, k=3q+1, r=ak, p=q+3r+2a, tau_h=4m^2-10m+10, g=tau_h(m-1)+6k, u=g+2 and v=3u+8, the complete norm ledger gives

 V=O(zeta^(-u)n^r), A2=O(zeta^(-(2u+4))n^(2r+a)),
 Z1=O(zeta^(-(u+4))n^(q/2+r+a)),
 Z2=O(zeta^(-(2u+8))n^(q+2r+2a)), D=O(zeta^(-4)),
 R3=O(zeta^(-(3u+8))n^p),
 R4=O(zeta^(-(4u+12))n^(q+4r+3a)).

The choices N=O(epsilon^-2) and xi=c_xi epsilon zeta^v n^(-p) pay all four corrector terms, source fluctuation and finite holding error. In particular the secular scalar D is not treated as fixed. A sufficient nominal autonomous duration is T=O(epsilon^-P), P=2+4p+2 kappa v, with explicitly bounded prefactor. For d=2, P=1078. This is a very loose sufficient bound for fixed complete d and fixed graph, not practical efficiency, favorable scaling in old qubit count, or total compiler wall time. The common added incident cap is accuracy independent; whole-system norm/reserves and second moments can grow as O(n) and O(n^2).

The final old target is chosen only after the uniform runtime: U_T=exp(i T H_lambda) W exp(-i T H), followed by a strict finite-grid selection of exact rational Hermitian M with norm<4. Approximation enclosures must use an explicit fixed subdivision of the displayed witness margin. The ensuing coefficients, exact support and phases use that chosen M. Do not differentiate a logarithm branch or the discrete grid-selection map, and do not recompute T from smaller later target-dependent constants. In this interaction-frame convention the source phase realizes M directly; an extra inherited omega*T factor would double-count the conjugation. The actual scalar contains R_total(T+s)+c_M xi^2(T+s)+lambda c_C s. There is no additional lambda c_C T. Continuing nonscalar bias is paid only over the finite observation window; no lambda*T smallness is assumed.

The separate check recomputed the full sensitivity chain: pole/calibration weights, Jacobi entries, Green responses, couplings, one-hole inverse, complete A2 and actual reserves. The proposed eta_in proportional to epsilon^3 zeta^(9u+40)n^(-(2p+3r+2a+1)) yields installed local error proportional to epsilon^3 zeta^(2v)n^(-(2p+1)). Original-matrix requests include one more zeta factor for the fixed spectral chart. These tolerances also preserve the pole, weight, gap and Green sign margins. Discrete bias/grid/node/chart choices remain fixed after strict certification. The chosen rational M is exact data; certified evaluation of U_T and its separate target discrepancy are different from calibration sensitivity at fixed M.

Required arithmetic qualification: divide operator-error allowances by the matrix dimension when rounding entries of the one-hole matrix, which adds only logarithmic bits. Its inverse can be computed with rational elimination/adjugates at the explicit gap, without a hidden floating inverse assumption. Evaluate the normalized one-hole quadratic form as N/(N-1) times that of e_1-ones/N, or explicitly pay vector approximation error. Core Gram arithmetic, contraction iteration error, internal source-coordinate guard bits, phase normalization and timing precision all retain their stated budgets. Bit-count bounds and polynomial internal requests do not bound the response time of arbitrary computable input oracles or build physical calibration hardware.

The direct complete-output trace allowance includes the actual unconditional old/reference marginal, all controller outputs, initial readiness, complete integrated generator error and separate release/phase tolerances. Initial preparation is not supplied by this result. Composing a chronological preparation must account for its extra old aging, memory output and phase convention; the fixed-plant preparation/resource acceptance is not automatically a shrinking-bias preparation theorem. Autonomous scheduling, physical controls/phase/purity/isolation, final halt and reuse remain open or supplied. The fixed nonscalar-bias finite-window counterexample and the growing-route small-response counterexample remain intact.

Evidence: root froze an independent pre-result sketchb544c0e4 without sharing it with the author, fully read the original33807-byte argument and complete final change, and hand-checked the cone powers, routing lower bound, corrector exponents, late target order and precision neighborhoods. The finished author argument is37212 bytes. Root then read the entire separate exposed review, including its different derivative proof and full precision recomputation. The author is a same-model continuation; the checker is source-exposed, same-model and shared prior premises. Neither is a blind replication or fresh validation of every parent. All checking here is analytical: zero new scientific executions and zero historical program replays. Root source identity checks cover33candidate members/23live sources and9review members/3review sources. Usage-interruption originals remain preserved. Metadata counts establish provenance only. No editable prompt files changed.
