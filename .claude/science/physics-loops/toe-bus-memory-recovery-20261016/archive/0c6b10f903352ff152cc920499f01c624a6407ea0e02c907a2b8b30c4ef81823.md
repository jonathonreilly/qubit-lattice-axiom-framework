---
title: Installed-bus preparation with literal and evolved memory contracts
claim_id: bus_installed_preparation_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
conditional_surface_status: supplied driven preparation with two distinct complete memory-output contracts
status: proposed_retained
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
upstream_dependencies:
  - strongly_regular_bus_bounded_theorem_note_2026-10-15
runner: scripts/bus_installed_preparation_2026_10_16.py
next_trace_action: independent retained audit; current source remains conditional-support
---

Claim type: bounded_theorem.

An already installed finite bus can be prepared by supplied positive complementary controls, matching SWAPs into fresh memory, and local source rotations. The complete original old/controller/reference input is retained. Two conditional theorems have different memory contracts: the original fast-ramp construction retains the literal relabelled input Q; the fixed modeled per-site slew construction retains a specified additional memory unitary U_E. The second theorem does not satisfy the first theorem's memory contract without an additional condition or a paid inverse operation. Both preserve the complete literal old Hamiltonian and all actual scalar reserves.

This canonical wrapper packages accepted arguments without changing them. The source-only wrapper/code was separately accepted at SHA256 2a3a63df329ab362081fe3c8f65cffcffb29b644398a70ace2c396a332db3990; actual canonical review and execution evidence is recorded in the bound packet. The original preparation source acceptance is SHA256 `28bef1945c65f807be837286d6e795d888f3d8b9ebb75024ac26ee0084409641`; the bounded modeled-slew acceptance is `b237e6550c7b500ff48cdaa2cd30e50cf4895205a610e8feb677da085bf82473`. Their complete controlling qualifications occur below. The two original mathematical source acceptances do not themselves approve the wrapper/code, canonical integration, publication or retained status; the separate source-wrapper review is identified above. Original pending statements and null fields remain unchanged historical records.

## 1. Parent, inputs and supplied controls

The sole external mathematical parent is the [qualified strongly regular bus theorem](STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md), exactly 83,919 bytes at SHA256 `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b`. The slew result also uses the original preparation theorem reproduced in this same note. Older finite-reservoir and compensation papers are credited methodological/exposure sources preserved with the original author packet; their native-supplier conclusions are not imported. The two new constructions rederive the matching-SWAP, phase and Duhamel arguments they use. No quantitative-resource, positive-bias or joint-energy theorem is an additional mathematical parent here. In particular, this packet does not prove preparation for a positive-bias extension by association with its Git base.

Fix the complete finite old plant D and literal onsite/nearest-neighbor Hamiltonian H, including original apparatus and memories. Retain arbitrary correlations with the installed bus/source register C and passive reference R. The inherited runtime domain requires a simple complete old spectrum, distinct positive gaps, a designated local Hermitian port B with all energy-basis off-diagonal entries nonzero, the parent's complete-space separation/calibration, and its vacant exterior embedding and isolation. A single available port does not supply those conditions.

For effective selection supply computable names or equivalent certified access for the actual finite matrices, spectra/isolation data, positive blocks and scalars, target data, positive time unit t_*, and finite window upper bound. Bounds alone are not matrix names. The parent's exact-L theorem needs its stated support/phase data. For arbitrary computable Hermitian L, retain the separately attributed rational-Hermitian approximate-target repair rather than an exact-zero oracle. Strict rational majorants and strict positive choices avoid discontinuous ceilings/equality tests. None of these existence/search statements supplies efficient conditioning or runtime.

Write the actual installed addition as A=sum_j h_j, with supplied coefficients c_j satisfying 0<=h_j<=c_j I. Put C0=sum_j c_j and assume the sums of c_j incident at each site are bounded by the parent's fixed J_*. The c_j are the actual coefficients chosen for the following physical complements, not replacement phases chosen after the fact:

```
K=H+A,
Gamma_j=c_j I-h_j >=0,       Gamma=C0 I-A.
```

Every original h_j and every literal H term remains installed with coefficient one; the added controls are Gamma_j on their original onsite/edge supports. Their negative nonscalar pieces are an extra physical control permission. Fresh E has n_C=b+qN qubits, initially globally independent vacuum, zero storage drift, and an accessible disjoint nearest-neighbor matching with every C qubit. Here q=d(d-1)/2, b=2(d-1)+4q, N>=2 and n_S=qN counts source qubits. The proof supplies a matching for the parent's displayed bus geometry, conditional on actual vacancy and isolation. All E outputs are retained as consumed memory; arbitrary D/C/R correlations are transferred, never reset or discarded. Its input dimension is 2^n_C and its possible stored entropy is n_C log 2.

## 2. Exact stages and the two release contracts

Use symmetric smooth ramps u from 0 to 1 and back, durations r_on,r_off, with a full matching-SWAP stage t_s and source-rotation stage t_p between them. All stages count toward

```
tau=r_on+t_s+t_p+r_off,
alpha_on=r_on/2,        alpha_off=r_off/2,
A_u=t_s+t_p+(r_on+r_off)/2.
```

The modeled driven generator is H+(1-u)A+u C0 I+G(t). Matching pulses proportional to I-SWAP with total coefficient integral pi/2 give the full SWAP with no additional scalar. A source rotation uses the positive local logarithm

```
Q_phi=(pi/4)(I+cos(phi)Y-sin(phi)X),
exp(-iQ_phi)|0>=exp(-i pi/4)(|0>+exp(i phi)|1>)/sqrt(2).
```

Let Q denote the exact relabelling of the original D/C/R input into D/E/R; Omega_phi is bus vacuum times all equatorial sources. With tensor order understood explicitly through this relabelling, the two ideal release isometries are

```
V_Q = exp(-i Phi_Q) Omega_phi tensor [(exp(-i tau H) tensor I_ER)Q],
Phi_Q=C0 A_u+pi n_S/4;

V_U = exp(-i Phi_U) Omega_phi tensor [(exp(-i tau H) tensor U_E tensor I_R)Q],
Phi_U=C0 A_u+R(alpha_on+alpha_off)+pi n_S/4.
```

The R in Phi_U is the actual reserve in the following full-space decomposition, not the passive reference register:

```
A=R I+A_C+xi V_p,
A_C=A_0+xi V_s+xi^2 A2,
A_0=H_bus+sum_l(omega_l N_l+L_l),
U_E = relabelling of exp(-i alpha_on A_C) from C to E.
```

The second comparison keeps all of A_C during the first ramp, then transfers its evolved input to memory. On the final ramp it keeps A_0. The density-counterterm A2 is its entire physical operator, including off-code action. To obtain release phase phi_l, the slew construction applies gate phase phi_l+omega_l alpha_off: the final free source evolution subtracts omega_l alpha_off. The original fast-ramp construction applies phi_l directly and pays its final-ramp defect. These are different comparisons of the same supplied-control architecture, not interchangeable notations.

For initial full-state readiness error eta_ready and complete preparation-generator error E_p(t), the uniform unhalved trace errors obey

```
e_Q <= eta_ready+C0 r_on+Gbar r_off+2 integral_p ||E_p(t)||dt,
Gbar >= ||A J_Omega||;

e_U <= eta_ready+xi r_on||V_p||
         +r_off(xi v+xi^2 a2)+2 integral_p ||E_p(t)||dt,
v>=||V_p+V_s||,        a2>=||A2||  (full physical space).
```

The corresponding nominal isometry defects are half the displayed ramp terms. Every reference is retained. The additive-complement error shorthand 2 nu A_u is valid only if nu bounds ||delta Gamma|| in energy units. A dimensionless relative coefficient bound nu instead costs 2 nu ||Gamma|| A_u. Integrated error control does not establish pointwise amplitude or derivative bounds.

## 3. Strength, modeled slew and ordering of resources

The common incident modeled strength is 2J_*+g, counting installed and complementary channels separately and the local matching/rotation pulse. For the literal-Q sufficient construction, one may take r_on=e/(4C0), r_off=e/(4Gbar), eta_ready<=e/4 and integral_p||E_p||<=e/8, with positive majorants if needed. This makes e_Q<=e but can require increasingly fast ramps. It proves no accuracy-independent slew bound for that contract.

For the evolved-memory construction supply smooth flat-ended ramp F and a positive unit-integral bump chi. Let m_F bound |F'|, m0 bound chi and m1 bound |chi'|. For fixed g,S_*>0, choose

```
r_on,r_off >= m_F J_*/S_*,
t_s >= max(pi m0/g, sqrt(pi m1/S_*)),
t_p >= max(pi m0/(2g), sqrt(pi m1/(2S_*))).
```

The disjoint stages then have incident modeled strength <=2J_*+g and sum of incident first-derivative norms <=S_*. Flat endpoints handle joins. The global derivative norm can grow with apparatus size. The claim concerns the specified mathematical waveform, not hard bandwidth, a microscopic controller, or physical implementation slew. Actual implementation caps require separately supplied pointwise amplitude/derivative control or slack; the integrated error budget is insufficient.

First fix N and all finite unscaled bus, calibration and counterterm data. Then reduce positive xi further, retaining all original bus inequalities. For example,

```
xi <= e/[8(1+r_on||V_p||+r_off v)],
xi^2 <= e/[8(1+r_off a2)],
eta_ready<=e/4,       integral_p||E_p||<=e/8
```

give e_U<=3e/4. Fixed durations do not imply a polynomial total runtime: smaller xi increases T=t_*/xi^2, and constants may depend severely on N. After the final xi, recompute T, source and gate phases, actual R,C0,U_E,Phi, readiness tolerance, and storage/calibration over the full actual lifetime. Optional moment accuracy can be fixed noncircularly before xi using beta_bar=||H-aI||+(n_C+1)J_* as a uniform bound on ||K-aI||. This overcounts rather than deletes local reserves.

The original driven schedule also has a global action bound ||Gamma||A_u+pi n_C+(pi/2)n_S and variation bound 2C0+2g(n_C+n_S). These are modeled generator quantities; the external work identity for this driven model is not a physical energy supply, microscopic power bound or thermodynamic preparation cost.

## 4. Release-to-runtime composition and chronology

For t=T+s measured from release, 0<=s<=w, retain the parent's

```
T=t_*/xi^2,
phi_l=arg L_ab-arg kappa_ab+omega_l T,
chi(t)=R(xi)t+c_old xi^2 t+theta0.
```

Preparation time tau is not added to omega_l T. The final phase is Phi_Q+chi(t) or Phi_U+chi(t), respectively. The old factor in both complete comparators is

```
exp(-isH) W exp[-i(T+tau)H],
```

acting on Q together with I_E or U_E and reference identity. All source outputs retain their parent's exp(-it omega_l N_l) evolution and all bus outputs remain in the comparison. The actual elapsed time is tau+T+s. No original scalar in H, ramp reserve, rotation phase or runtime reserve is removed.

If delta_bus is the parent's complete trace error and e_r=integral_0^(T+w)||E_r(t)||dt is the runtime calibration budget, the direct telescope is e_p+delta_bus+2e_r, with e_p chosen for the relevant memory contract. For the exact-target parent, e_p<=epsilon/8, delta_bus<=3epsilon/4 and e_r<=epsilon/16 suffice. For its computable rational-Hermitian repair, choose ||M-L||<=epsilon/32, work at epsilon/2, preparation allowance epsilon/16 and runtime integral epsilon/32; target replacement adds epsilon/16, giving total <=9epsilon/16. All finite data and phases are those for the final chosen M and xi.

The ideal tau-aged old/reference marginal differs from the actual release marginal. Replacing the direct comparator by a product built from that actual marginal can add a further e_p; it is not a free substitution. U_E acts on a passive reference during runtime and must remain in the output. It can be omitted only if scalar on the supported input or if an actual inverse operation with its own support, error, timing and cost is supplied.

## 5. Full physical release moments

For each length-N source define the actual nearest-neighbor density D_l=sum_(j=1)^(N-1)n_j n_(j+1), f_l=a_l N_l+b_l D_l, a_l=omega_l+xi^2 u_l and b_l=xi^2 v_l. For N>=2, independently of source phase and the signs of counterterms,

```
mu_l=a_l N/2+b_l(N-1)/4,
Var(f_l)=a_l^2 N/4+b_l^2(5N-7)/16+a_l b_l(N-1)/2,
c=R+sum_l mu_l,
J_Omega^* K J_Omega=H+cI,
J_Omega^* K^2 J_Omega=(H+cI)^2
  +[sum_l Var(f_l)+(xi^2/2)sum_l r_l^2]I+xi^2 v_p^2 B^2,
G_Omega^2=c^2+sum_l Var(f_l)
  +xi^2[v_p^2||B||^2+sum_l r_l^2/2] <= C0^2.
```

No symmetric projection is inserted between K factors, and no [H,B] or [H,B^2] commutation is assumed. On ideal release, rho_D(tau)=exp(-i tau H)sigma_D exp(i tau H), so the ordinary mean is Tr(H sigma_D)+c and variance is

```
Var_sigma_D(H)+sum_l Var(f_l)
 +xi^2[v_p^2 Tr(B^2 rho_D(tau))+sum_l r_l^2/2].
```

These ordinary D/C moments are identical under V_Q and V_U because E is not measured by K. If a reference-valued moment retains E, its ideal operator changes by conjugation with U_E (and identity on other retained reference factors). Thus the unchanged ordinary numbers do not establish an unchanged complete-output or E-valued moment contract.

For beta>=||K-aI|| and trace error e_p, centered mean, centered second-moment and variance errors are bounded by beta e_p, beta^2 e_p and 3 beta^2 e_p, respectively; reference-valued linear moments obey beta^j e_p. Runtime integrated generator error adds 2 beta e_r and 6 beta^2 e_r to mean/variance allowances. These bounds concern the same full installed K. Uncentering restores all actual reserves. They do not identify a measured hardware energy observable or bound total stored energy independently of N.

The accepted reviewer/root refinement is

```
||(I-P_sym)D_l Alpha_l||^2=(N-2)(N+1)/(16N).
```

Replacing D_l by its symmetric-code compression therefore omits b_l^2 times this amount from the second moment for N>2. It vanishes at N=2. Phase choices differing by pi give orthogonal pure preparations with the same first two moments. Separately, a bus vacuum/one-excitation superposition acquires memory phase exp(-i alpha_on nu), producing literal-versus-evolved memory trace distance 2|sin(alpha_on nu/2)| while ordinary release moments agree. The latter discrepancy extends to sufficiently small positive xi by continuity of U_E at fixed data and the analytic weak-ramp estimate; it does not require a limit of the rapidly T-dependent source phase.

## 6. Evidence, attribution and unresolved suppliers

All scientific executions are historical and preserved with original source-at-launch, launchers, actual argv/cwd/exit, full streams and source maps. The author ran one exact dimension-64 compression discriminator; it is not a calibrated routed-bus instance. The exposed reviewer independently wrote an exact Gaussian-rational sparse-column checker for ten one-to-three-source fixtures, N=2..40 occupation statistics, full finite SWAP basis action and phase orientation. A separate reviewer provenance run checks hashes and four in-memory tamper cases only. The slew reviewer wrote one floating-point dimension-128 complete-isometry discriminator at xi=0. Its correct comparison error is about 5.6e-15; wrong memory, phase and reserve alternatives have order-one errors. This is not a positive-xi runtime simulation, pulse integration, interval proof or physical derivative measurement. The full analytic arguments establish the conditional families.

The selected preparation histories report no failed scientific executions; rejected formula/comparator alternatives are retained as scoped supporting findings, not fabricated failed process runs or broad no-go results. The qualified bus parent's earlier real failures remain in its existing archive; this packet captures the exact parent note/qualifications and does not recursively copy or revalidate that prior publication archive. Source/body/receipt manifests distinguish scientific evidence, provenance recordings, methodological exposure and publication context.

Checks are source-exposed and same-model, with the original authorship/read exposure preserved. The root read the original author's checker before its independent reconstruction; the original exposed reviewer did not semantically inspect or import that checker. The slew reviewer knew the new proposal and preparation result. There is no new blind or model-family-independent replication, whole-parent validation or retained audit. This packaging worker reads the historical checkers without changing their original exposure descriptions.

Fresh globally independent purity, actual complementary controls, matching access, timing/phase references, exterior isolation and long-lived passive memory remain supplied. A microscopic drive/controller F would need its own ready state, complete output comparator, error/energy/covariance ledger and preparation; it is not included merely by writing a classical waveform. No native preparation, autonomous schedule, physical drive-energy result, final halt, reset/reuse, favorable global-energy or total-runtime theorem follows. No old scientific code is run in this packet. Its primary verifies provenance only and requires actual source/base/canonical review evidence. Provenance success is not a scientific verdict; publication and independent retained audit remain separate.

## 7. Immutable arguments and controlling qualifications

The following seven bodies are copied byte for byte, once each. BODY_MAP.json records exact offsets, lengths and source hashes; ARCHIVE_INDEX.json recovers the necessary original source packets and complete actual evidence. The later two root acceptances govern present composition while historical pending/null records remain unchanged. New wrapper prose is not retroactively covered by either source acceptance.


<!-- BEGIN UNCHANGED BODY original_preparation -->
# Conditional preparation and release for the installed strong-spectral bus

**Disposition: the existing preparation contracts do not by themselves supply this bus's initial state. A conditional finite preparation interface can nevertheless be closed by applying their paid-compensation method to the bus's actual positive blocks.** The construction below retains every old term, arbitrary initial old/controller/reference correlations, the complete finite memory output, both switching ramps, the actual elapsed time, all scalar phases, and the full installed first and second energy moments. It has one common incident-strength cap for the explicitly modeled preparation and runtime generators. Fresh purity, positive complementary interactions, phase-referenced controls, isolation, calibration and an external schedule remain supplied. A microscopic controller with its own complete outputs and energy is an additional interface, not a conclusion of a prescribed time-dependent Hamiltonian.

This is a source-exposed continuation by the author of the earlier bus and static-transfer arguments. It is not fresh independent parent validation, retained audit, native preparation, autonomous scheduling, permanent halt or reusable-memory construction. The compensation, reservoir SWAP and Duhamel method are reused from the already checked preparation notes. The new work is their compatible application to the literal bus, its product source target, its full off-code moment terms and its preparation-to-runtime chronology.

## 1. Exact sources and the interface they leave open

The accepted canonical bus source is `STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md`, 83,919 bytes, SHA256 `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b`. Its root acceptance is `cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726`; controlling qualifications are `a182e0074ac9b8ed1d9e9e57627d289754252e2969446099ed502e229bf61880`. The full underlying author argument is unchanged at `855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2`. Its strong spectral and geometry premises remain conditions. The more recent quantitative selection acceptance `810d46f26c0883a470c010783fe310e0e0af9ee1a82f025ac32893bf45294fff`, qualifiers `1aab69f2d3407be3718e91a3b7e61ef0f24426691b69c3d97682de5893106386`, is context only: it supplies no preparation resource and is not used to derive this result.

The relevant existing preparation sources, all in the same worktree's `docs/`, are:

* `INSTALLED_BACKGROUND_AUXILIARY_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md`, SHA256 `7d48af3dc97630d1adc21ac6cbce02fe602aeea14d4b81e2edad54944c9cb021`. Its actual consumer is a binary vacuum instrument for a specified mediator, with a supplied clean pointer and reader. Its fast-pulse and finite-recurrence suppliers pay the complete installed drift and elapsed control time. They do not assert an arbitrary-input replacement by this bus's equatorial product state. The finite recurrence does not itself preserve free old evolution for its entire waiting time in the required order.
* `INSTALLED_GENERATOR_PREPARATION_READINESS_BOUNDED_THEOREM_NOTE_2026-10-15.md`, SHA256 `cdb42d6682ee56968c20229b2e012a23afc6de75bceab0f42f06bc94b95a4fe6`. Its coercivity and vacuum-moment identities belong to `H+cI+Delta L+sqrt(Delta)V`, including its literal paired ports. They cannot be imported into this bus by renaming symbols. Even on their own domain they require a supplied expectation certificate and a separate instrument; they do not create coherence, a phase reference, purity or the intended old input.
* `COMPENSATED_FINITE_RESERVOIR_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md`, SHA256 `d28bb8d6a39ffcdce60f61fb47414abdcdd00e2cbbbb32013c4f8277b2a72ac8`. Its complete central proof supplies the useful method: positive termwise complements, full SWAP into retained pure memory, paid ramps and actual free-old time. Its one-head target, boundary-specific full norm and entry residual are not bus constants.
* Its parent `FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md`, SHA256 `3560cefa1c9a9e8064a11d2fc683bedd0cab3109905df5bffecdbe1999ad15ad`, supplies the already checked full-output SWAP contract and finite-memory accounting. No old checker is replayed.

Complete argument/partial-source coverage and immutable identities are recorded separately. The installed-local-reset note was inventoried but is not imported: no Markov bath, damping law or reset action theorem is used. No later padding result is used. A scalar energy certificate or a successful router-vacuum test is not a replacement for the source preparation contract; section 8 gives a bus-specific exact discriminator.

## 2. Literal bus and additional supplied resources

Use units hbar=1 without changing the old physical units. Let D be the complete finite old plant, C every new bus and source qubit, and R an arbitrary passive reference. Let `n_C=b+qN`, `n_S=qN`, with `b=2(d-1)+4q`, `q=d(d-1)/2`, `N>=2`, as in the bus source. Fix one entire accepted finite bus instance, including its selected coefficients, xi, runtime `T=t_*/xi^2`, target L and phases phi_l. Its actual installed generator is

    K=H+A,
    A=sum_j h_j >=0,
    0<=h_j<=c_j I,     C0=sum_j c_j>0.                 (1)

Here the h_j are the actual positive added onsite/edge blocks in bus section 10, including the old-port reserve R_s I, every bus exchange reserve, every source field and ferromagnetic block, the port/source perturbation reserves and both onsite/pair counterterm reserves. No literal old H term is included among h_j or altered. The c_j may be their explicit norm bounds from that ledger; choose those bounds so the supplied incident sums obey

    max_x sum_(j:x in support h_j) c_j <= J_* .       (2)

The accepted cap proof supplies such a ledger. For example, the port uses `c_j=2xi v_p||B||`, a source transfer `2xi r_l`, a ferro edge `2J_F`, and a reserved counterterm `xi^2|u_l|` or `xi^2|v_l|`. The reserve R_s has c_j=R_s. Thus `||A||<=C0<infinity` and `C0<=(n_C+1)J_*`; only the old site p and C support these added terms. C0 is a global sum, not a common global-energy cap.

Supply the following **additional** physical interfaces:

1. On each already used support, an independently driven positive complement

       Gamma_j=c_j I-h_j >=0,   ||Gamma_j||<=c_j,
       Gamma=sum_j Gamma_j=C0 I-A.                  (3)

   This requires the negative nonscalar part of each h_j, including the old-port B coupling, signed source density terms and exchange axes. Positivity of Gamma_j does not physically supply those couplings. The original h_j remain installed. In particular no -H is added.
2. One fresh reservoir qubit e(v) per C qubit, a disjoint ordinary-neighbor matching, ready state `|0_E>` independent of the arbitrary initial sigma_DCR, and engineered `H_E=0` with no unlisted couplings during the declared interval. The complete E output is retained. Joint ready-state error is allowed below; a dirty or merely marginally characterized E is not the exact premise.
3. The finite positive matching SWAP controls and onsite phase-referenced rotations specified below, with a fixed chosen per-site margin g>0, a known finite schedule, a common phase convention and full-space implementation/error certificates. Neither an internal clock nor a microscopic drive is derived.

For the bus's explicit coordinate embedding, a matching is available geometrically without moving old sites: for each core/backbone point `(x,0,0)` take `(x,1,0)`; for each routing leaf `(x,-1,0)` take `(x,-2,0)`; for each source point `(x,-1,-j)` take `(x,-2,-j)`. All x are negative, so these sites avoid the old nonnegative box. The two memory classes have different y; within a class x,z distinguish them. They avoid all C sites and every pair has L1 distance one. They may have extra geometric adjacencies, including to old sites near the boundary; all unlisted interactions require explicit isolation/calibration. A merely supplied alternative embedding of the bus tree does not automatically supply this matching. In that case matching vacancy is an additional premise. There are n_C extra memory sites and n_C selected matching edges; no extra old reset port is assumed.

## 3. Exact finite schedule and phases

Let w be the existing compensation note's nonnegative symmetric C-infinity bump on [0,1], normalized to integral one: `b(x)=exp[-1/(x(1-x))]` for 0<x<1 and zero otherwise, and `w=b/integral_0^1 b`. Set `F(x)=integral_0^x w`, extended by zero/one outside the interval. Its checked bounds are

    m0=||w||_infinity<=3sqrt(e),
    m1=||w'||_infinity<=48sqrt(e),
    integral F=1/2,   integral |w'|=2m0.             (4)

Here e is Euler's number. These exact computable profiles are supplied waveforms; approximation errors are charged. Choose positive finite durations r_on,t_s,t_p,r_off and `tau=r_on+t_s+t_p+r_off`. The compensation envelope u rises as F over r_on, stays one through the two pulses, and falls as 1-F over r_off. Then

    A_u=integral_0^tau u=t_s+t_p+(r_on+r_off)/2.       (5)

During the first plateau use full qubit SWAP S_v on each matching pair,

    G_s(t)=gamma(t) sum_(v in C)(I-S_v),
    gamma(t)=pi w(t/t_s)/(2t_s).                     (6)

The pairs are disjoint, their positive blocks commute, and `exp[-i(pi/2)(I-S_v)]=S_v` exactly, including the deterministic scalar. This is full SWAP, not excitation exchange.

During the second plateau rotate only the n_S source qubits. Define

    Y_phi=cos(phi)Y-sin(phi)X,
    Q_phi=(pi/4)(I+Y_phi)>=0,    ||Q_phi||=pi/2,
    G_p(t)=w(t/t_p)/t_p sum_(l,j) Q_(phi_l)^(l,j).  (7)

Since `Y_phi|0>=i exp(i phi)|1>`,

    exp(-iQ_phi)|0>=exp(-i pi/4)
                       (|0>+exp(i phi)|1>)/sqrt(2).

Thus all routers/core sites remain vacuum and the final C vector is

    |Omega_phi>=|0_bus> tensor product_l |Alpha_l(phi_l)>.

The full modeled Hamiltonian throughout preparation is

    K_prep(t)=K+u(t)Gamma+G(t)
            =H+(1-u(t))A+u(t)C0 I+G(t),          (8)

where G is zero on ramps and equals (6),(7) on the plateaus. K is installed throughout. At both endpoints u=G=0, so the full generator is again K, extended by identity on E. Every added control block is positive; K is positive by its already paid reserve, so K_prep is positive. No positivity of the separate original H is needed.

Let J append the ready E vacuum, and let Q relabel the complete original C register as E, including all its D/R correlations. The comparison evolution generated by `H+u C0 I+G` commutes with H on D and has the exact endpoint isometry

    V_prep = exp(-i Phi_prep) |Omega_phi> tensor
                       [(exp(-i tau H) tensor I_ER) Q],
    Phi_prep=C0 A_u+pi n_S/4.                      (9)

This contains the actual entire preparation time tau. The parallel SWAP has no additional endpoint phase. Its nonzero integrated Pauli scalar is not deleted; its nonscalar exponential combines with it to give exact SWAP. E is generally dirty and correlated at the output.

## 4. Full-output ramp, calibration and release bounds

Set `G_Omega=||A J_Omega||`, where J_Omega appends the entire product C state and is identity on D. Section 7 gives an explicit phase-independent value. Choose a certified upper bound `Gbar>=G_Omega`; the always valid positive choice is Gbar=C0. A sharper certified enclosure can be capped by C0.

The actual-minus-comparison generator is `(1-u)A`. In the Duhamel integral, the comparison input during turn-on is arbitrary on D,C,R, so use the full bound `||A||<=C0`. The plateau residual is zero. During turn-off the comparison state is exactly Omega_phi tensored with an arbitrary aged D,E,R state, so use G_Omega. Unitarity of the propagator on the other side of the integral gives

    ||U_prep(tau)J-V_prep||
       <=[C0 r_on+Gbar r_off]/2,
    ||rho_prep-V_prep sigma V_prep^*||_1
       <=min(2,C0 r_on+Gbar r_off).               (10)

The bound holds for arbitrary initial D/C/R correlations and all controller sectors. It does not assume that the actual state follows the comparison's vacuum or symmetric sector. This is precisely the checked compensation argument with the bus's own full and prepared-state norms.

If actual ready input is within eta_ready of sigma_DCR tensor vacuum_E, and the full implemented generator differs by a Hermitian E_p(t), then

    e_p <= eta_ready+C0 r_on+Gbar r_off
                         +2 integral_0^tau ||E_p(t)||dt.   (11)

One explicit allocation for any desired e>0 is

    r_on=e/(4C0),  r_off=e/(4Gbar),
    eta_ready<=e/4,   integral ||E_p||<=e/8,       (12)

which gives e_p<=e. All durations remain finite and positive. If both ramp denominators use C0 the same conclusion holds. Choosing smaller e to meet moment tolerances changes the ramps and calibration, not the peak heights.

Unlisted reservoir interactions, waveform errors, phases, switching, and any leakage outside code belong to the **full** E_p. A common coefficient error in Gamma bounded by nu contributes `2nu A_u`; separately certified block errors cost `2 A_u sum_j||delta Gamma_j||`. Shared envelope error costs `2||Gamma|| integral|delta u|`. A source phase perturbation delta phi has

    ||Q_(phi+delta)-Q_phi||
       =(pi/2)|sin(delta/2)|<=(pi/4)|delta|,

so the rotation's trace budget is at most `(pi/2)sum_(l,j)|delta phi_(l,j)|`. Coefficient/envelope cross terms must also be included; these separate formulas are not permission to omit them. A common time translation of a control envelope is bounded using its total variation below. An unknown extra post-preparation wait d>=0, if compared to the same bare Omega and further free H aging, costs at most `2Gbar d`; it cannot be hidden by changing the input state. A wrong-time full-output comparison can instead use `2||K|| |d|`. All such time is included in the old evolution or its explicit error allowance.

The release occurs after both ramps and both pulses, when preparation controls are zero. If storage on E has a bounded omitted generator nu over the preparation/runtime observation duration, its additional contribution is at most twice the integrated full norm, e.g. `2nu(tau+T+w)`. The large T can therefore demand very small storage/calibration error.

## 5. Common incident cap, action, scalar and work ledgers

Choose a fixed computable `mbar0>=m0`, and set

    t_s=pi mbar0/g,      t_p=pi mbar0/(2g).         (13)

These pulse durations need not shrink with accuracy. The maximum SWAP load per endpoint is `pi m0/t_s<=g`; the maximum source rotation load is `pi m0/(2t_p)<=g`. During either plateau the installed bus load is <=J_* and the separately counted complement load <=J_*. The pulse stages do not overlap. Therefore the actual **modeled** added incident load, including old-port reserve and both installed/complement channels, obeys

    J_prep<=2J_*+g,      J_runtime<=J_* .          (14)

This is a common finite bound independent of requested accuracy on the conditional bus family. It is not inferred from algebraic cancellation: both h_j and Gamma_j are counted. It excludes the pre-existing old H load exactly as the bus cap does. A perturbed physical implementation additionally needs this pointwise load certificate or fixed slack; an integral error bound alone is insufficient.

Let `C_Gamma=||Gamma||<=C0`, and `S_Gamma=sum_j||Gamma_j||<=C0`. Complete global upper prices are

    peak added controls <= C0+g n_C,
    integral ||u Gamma+G|| <= C_Gamma A_u+pi n_C+(pi/2)n_S,
    sum of local complement actions = S_Gamma A_u,
    integral ||d(u Gamma+G)/dt||
       <=2C_Gamma+2n_C pi m0/t_s+n_S pi m0/t_p
       <=2C0+2g(n_C+n_S).                         (15)

The peak derivative contributions are bounded by

    C_Gamma m0/min(r_on,r_off),
    n_C pi m1/t_s^2,
    n_S pi m1/(2t_p^2),                           (16)

for compensation, SWAP and source rotations respectively. These finite slew costs can grow with accuracy. No common derivative bound is asserted. If such a bound is imposed, its compatibility with (12) is an additional design equation; shortening ramps cannot bypass it.

Let s_H and s_A be the normalized traces of H and A on their complete carriers. The instantaneous scalar coefficient of the actual generator is

    s_H+s_A+u(C0-s_A)
      + n_C gamma(t)/2                 [SWAP interval]
      + n_S pi w(t/t_p)/(4t_p)         [rotation interval]. (17)

Only one pulse term is present at a time. The respective pulse scalar integrals are `pi n_C/4` and `pi n_S/4`. Equation (9)'s comparator phase `C0 A_u+pi n_S/4` is a different ledger. All literal H scalar phases remain in exp(-i tau H), and the runtime reserve R remains in the bus's chi(t). No upper bound is substituted for an actual phase coefficient: the chosen c_j are actual installed complement coefficients, hence C0 is actual.

For the finite closed driven model, controls vanish at both endpoints, so

    Tr[K rho(tau)]-Tr[K rho(0)]
       =integral_0^tau Tr[rho(t) d(u Gamma+G)/dt]dt. (18)

Its absolute value is bounded by (15)'s variation, not assumed negative. Initial K covariance for arbitrary correlated sigma is retained:

    Var_sigma(K)=Var_sigma(H)+Var_sigma(A)
       +Tr sigma {H-<H>I,A-<A>I}.                (19)

During the pulse, with h>=||H||, `P=h+C0+g n_C` bounds the full generator norm; positivity gives `0<=mean<=P`, raw second moment <=P^2 and variance <=P^2. Exact variances include all noncommuting covariance terms. These are engineered-generator/work allowances for an external drive, not the energy cost or state construction of a microscopic power supply.

## 6. Exact runtime composition and noncircular choice order

Write `t=T+s`, `0<=s<=w`, measured from the completed release. The bus's nominal reference-complete isometry estimate on a bare Omega input applies with E and the original R both retained as reference. Applied to (9), it gives the complete preparation-plus-runtime comparator

    exp[-i(Phi_prep+chi(t))] |0_bus>
      tensor [product_l exp(-it omega_l N_l)|Alpha_l(phi_l)>]
      tensor [(exp(-isH) W exp[-i(T+tau)H] tensor I_ER)Q],
    chi(t)=R(xi)t+c_old xi^2 t+theta0.            (20)

Every factor of E is retained, generally correlated with D/R. All controller outputs and the original arbitrary reference remain. The two free old flows are in their actual order. With `T_total=T+tau`, this is exactly the requested old target `exp(-isH) W exp(-i T_total H)` at total laboratory time T_total+s. No clock aging is relabeled as a new unknown input, and no preparation interval is omitted. The phase `+omega_l T` in the bus's source prescription remains correct: the prepared source state is defined at runtime origin tau. Adding `+omega_l tau` to that prescription without changing the target would be a different phase convention and generally wrong.

If the bus's nominal complete trace error on product input is delta_bus and the runtime full-generator error has integral e_r, then the actual complete output error against (20) is

    <=min(2,e_p+delta_bus+2e_r).                  (21)

This follows directly by applying the actual runtime unitary to the preparation error and using the uniform bus isometry estimate on the ideal product comparator. The preparation's ideal old/E/reference state is the explicitly aged Q sigma Q*, not necessarily the actual release marginal. That actual marginal is within e_p of it by contraction. If a consumer insists on the parent sentence phrased against the *exact actual* unconditional marginal, its preparation product distance is <=2e_p; the marginal shift must then be charged separately. The direct telescope (21) avoids double-counting and proves the desired original-input target, without claiming those marginals are exactly equal.

For exact-target existence, use the parent's resource selection at epsilon: `delta_bus<=3epsilon/4`, choose `e_p<=epsilon/8`, and `e_r<=epsilon/16`, giving epsilon. For effective arbitrary computable targets, preserve the accepted rational-log repair: approximate L by rational Hermitian M in the supplied energy basis within epsilon/32, run the bus at epsilon/2, and use preparation <=epsilon/16 and runtime integral <=epsilon/32. The full bus allowance is then <=epsilon/2, and replacing exp(-iM) by exp(-iL) costs <=epsilon/16, hence <=9epsilon/16. Decidable rational support and the accepted unit complex phase prescription remain required; no exact-zero oracle is inserted.

The choices have no preparation/runtime circle. First fix the plant/target and construct the finite bus using its existing order: N, separated spectrum, routing/calibration, counterterms/correctors, xi, T. Its Hamiltonian, norms, C0, G_Omega and incident cap do not depend on the final coherent phases. Select phase-independent preparation error/moment allowances and durations next. Finally set the source rotation axes to the bus's T-dependent phases. There is no required equation making tau determine T or vice versa. The global scalar Phi_prep and actual total old time are then computed from the chosen schedule. Exact known timing is a supplied condition; uncertainty is priced by (11) and the explicit release allowances.

This theorem is on the accepted strong-spectral H domain. If an application uses a separate static bias so the bus drift is H+C, its existing finite-window transfer conditions and continuing-bias error remain necessary. This preparation argument alone does not turn that biased runtime into literal-H evolution or establish a generic Lie-to-static theorem.

## 7. Complete installed release moments

The moment calculation must use the physical K, including off-code source density interactions. Write the actual reserve as R=R(xi), and for source l define

    a_l=omega_l+xi^2 u_l,  b_l=xi^2 v_l,
    D_l=sum_(j=1)^(N-1) n_(l,j)n_(l,j+1),
    f_l=a_l N_l+b_l D_l,
    mu_l=a_l N/2+b_l(N-1)/4,
    v_l^mom=a_l^2 N/4+b_l^2(5N-7)/16
                              +a_l b_l(N-1)/2.           (22)

The moment superscript distinguishes v_l^mom from the source counterterm coefficient v_l. On the coherent product vector, the occupation distribution is independent Bernoulli(1/2). Consequently `Var(N_l)=N/4`, `Var(D_l)=(5N-7)/16` and `Cov(N_l,D_l)=(N-1)/4`. To verify the middle identity, each bond indicator has variance3/16, adjacent bond covariance1/16 and disjoint bonds zero covariance. There are N-1 bonds and N-2 adjacent pairs. This proves (22) for every N>=2, including negative b_l.

The unreserved bus Hamiltonian annihilates bus vacuum. Every source ferro sum annihilates its identical product vector. The port/source perturbation creates one bus excitation. Its port output is at c1 and each source output at its different u_l, hence those outputs are pairwise orthogonal. They are also orthogonal to the bus-vacuum H/f_l output. Therefore the exact operator compressions are

    J_Omega^* K J_Omega = H+c I,
    J_Omega^* K^2 J_Omega
       =(H+c I)^2+v0 I+xi^2 v_p^2 B^2,
    c=R+sum_l mu_l,
    v0=sum_l v_l^mom+(xi^2/2)sum_l r_l^2.        (23)

No commutation of H with B is used. The old field appears in the first square exactly; no symmetric-code projection is inserted between the two K factors. All values are phase-independent. In particular

    G_Omega^2=||J_Omega^* A^2 J_Omega||
       =c^2+sum_l v_l^mom
            +xi^2[v_p^2||B||^2+(1/2)sum_l r_l^2].       (24)

This is positive for the present bus and is <=C0^2 by (1). The scalar c includes the actual R. A certified upper enclosure of the square root suffices for Gbar; C0 is always a valid fallback.

Let rho_D(tau)=exp(-i tau H) sigma_D exp(i tau H). The exact ideal release moments on the SAME installed K are

    mean_*=Tr(H sigma_D)+c,
    Var_*=Var_(sigma_D)(H)+sum_l v_l^mom
       +xi^2[v_p^2 Tr(B^2 rho_D(tau))+(1/2)sum_l r_l^2]. (25)

Arbitrary D/E/R correlations do not invalidate this compression calculation. The B^2 expectation need not be time invariant under H and is evaluated at the actual tau. The raw second moment is `mean_*^2+Var_*`; scalar R is never removed. These moments can grow with n_S, even though incident strength remains bounded. There is no bounded-total-energy claim.

For any fixed scalar a used only to center estimates, choose `beta>=||K-aI||`, for example `||H-aI||+C0`. Complete release trace error e_p implies

    |mean_actual-mean_*|<=beta e_p,
    |Tr[(K-aI)^2(rho_actual-rho_*)]|<=beta^2 e_p,
    |Var_actual(K)-Var_*|<=3beta^2 e_p.           (26)

The variance estimate follows by expanding the centered squared means, each bounded by beta. Raw moments use the restored a-dependent terms or ||K||. For a retained passive Q=ER (or R alone), duality also yields

    ||Tr_DC[((K-aI)^j tensor I_Q)(rho_actual-rho_*)]||_1
         <=beta^j e_p,   j=1,2.                  (27)

These are linear reference-valued mathematical moments, not physical measurements or conditional variances. Given desired positive mean/variance tolerances E_mu,E_var, choose the e in (12) additionally no larger than `E_mu/beta` and `E_var/(3beta^2)`. This selection occurs after K is fixed and changes only preparation accuracy. Thus no hidden moment-accuracy circularity occurs.

After release, exact K evolution conserves the actual K moments. Runtime generator error with integral e_r changes their comparison with that exact evolution by at most `2beta e_r` for the mean and `6beta^2 e_r` for variance, using trace contraction/Duhamel. Comparing against the approximate bus product output instead also pays its explicit beta-weighted delta_bus. A small channel error alone does not provide a fixed moment tolerance as the family norm grows.

## 8. Exact obstructions to careless composition and one new check

An installed mean certificate does not set the source phase. For any one source, phi and phi+pi give orthogonal single-qubit states and hence orthogonal full source products. With identical old state and bus vacuum, (23) shows the complete installed first and second moments are identical for all phases. Their full-state trace distance is2. Thus even both these moments cannot select the needed T-dependent source input. This rejects a particular inference from the current readiness source; it is not a universal preparation obstruction.

Nor can the physical source counterterm be replaced by its symmetric-code compression when computing moments. For N=3,

    D=n1 n2+n2 n3,
    P_sym D P_sym=Nhat(Nhat-1)/3 on the code,

but on an equatorial product the physical Var(D)=1/2, whereas the variance of the compressed operator is5/12. The missed squared residual is1/12. First moments agree. This distinction is why (22) uses the full NN operator.

Analytical findings were frozen before constructing the new check, in INITIAL_FINDINGS_FREEZE.json. One exact SymPy discriminator builds the full 64-dimensional operator for one old qubit, two distinct bus sites and a three-qubit source. It uses complex noncommuting `H=Y+2Z`, `B=I+X`, explicit positive reserves, ferro edges, weak port/source interactions and signed source density counterterms. It verifies the full compensation identity, both operator compressions (23), and (24), using 64-by-2 prepared-state columns. A mutant replacing D by its symmetric-code expression preserves the mean and loses exactly `(xi^2 v)^2/12=4/352947` from every old-vector second moment. The phase rotation orientation is also checked. This is a finite algebra fixture, not an execution of the complete routed bus, pulse propagation or an accuracy family.

The one execution ran Python3.13.5/SymPy1.14.0, began `2026-10-16T03:41:40.514160+00:00`, ended `2026-10-16T03:41:41.387663+00:00`, and exited zero in about0.871 seconds. Child/outer limits were30/40 seconds and matrix dimension64. The executable source at launch has SHA256 `1c1677df40bb9a5861b7b29a1ca5f301c4adbe632d329d85e2d9b30cae1ceea5`; stdout `28436b704dc0879135b3963ff7a891ea110af0a00a979e27e418a0982285e957`; stderr is empty. Source, launcher, exact argv/cwd, limits and full streams are preserved in check_run. No failed scientific launch or old-program rerun occurred. The finite check supplements the general analytic proof; it is not its premise.

## 9. The physical premise that remains

Within the declared driven D/C/E model, equations (9)–(27) close a precise installed-bus preparation/release interface. They replace an assumed T-dependent coherent source product by phase-invariant fresh vacuum memory plus explicitly phase-dependent local controls and paid positive compensation. Information formerly in C is stored, not erased. No postselection or unretained failure branch is used. The native supply of purity has not been solved.

The complete quantum outputs modeled here are D,C,E,R. A classical waveform specification has no microscopic quantum drive output in this Hamiltonian model. To claim a fully physical all-output supplier, an additional apparatus F must be specified, with a ready state, a complete implementation channel close to this driven isometry tensored with a specified retained F output, its actual free evolution after release, and its preparation/runtime energy and storage budget. If the supplied ideal F output is independent, its mean and variance add to (25); otherwise its covariance and full joint target must be supplied. Moment error bounds then use the total generator norm. A reduced D/C channel or an unobserved driver cannot establish that stronger contract. None of these apparatus data are derived by (18)'s external-work identity.

At the finite mathematical level, the essential extra control premise is actual supply of the complementary interactions (3), not an energy certificate. If those interactions are unavailable, (8)'s exact compensated plateau is unproved and this route does not close. Fast uncompensated pulses and the existing recurrence method remain different conditional possibilities, with their own strength, literal-time and control-supply obligations. Their absence here is not a no-go theorem.

The original memory E is consumed after one use. It has dimension 2^n_C and can receive n_C log(2) entropy from an independent maximally mixed C. Exact unitary replacement of arbitrary orthogonal C inputs requires at least that environment dimension by preservation of inner products; this is the existing reservoir parent's exact-information argument, not a new approximate lower bound. Its stipulated zero generator is not a zero thermodynamic preparation cost. A later restoration process, permanent records, a physical reader, an autonomous external scheduler and indefinite storage/reuse are all outside this result. No broad physical-realization claim follows from finite-window approximation.

Only this assigned directory was written. No canonical source, Git/PR state, audit, cache, graph, lock, editable prompt, axiom, publication or other-chat state was changed. Root controls scientific acceptance and any publication. Exact pins, read coverage, exposure and the final freeze accompany this one source proposal.

<!-- END UNCHANGED BODY original_preparation -->

<!-- BEGIN UNCHANGED BODY original_exposed_review -->
# Independent mathematical review: installed bus preparation and release

**Result: the new composition is supported within its declared conditional driven-model scope. No blocking mathematical defect was found in the frozen candidate.** This supports a root decision about this source revision; it is not root acceptance, publication approval, a formal audit verdict, or independent revalidation of the entire inherited runtime-bus theorem.

The examined source is the complete 279-line `DERIVATION.md`, SHA-256 `71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29`, frozen by the author at 2026-10-16T03:53:54.446682Z. Its `FREEZE.json` SHA-256 is `ff5073ee47aac64e332b47938c29774f3b4aa6ccfc8ed7b14011e29587eaeeb3`. Both are captured under this review directory's `sources/`. The live originals still matched the captured source hashes at 04:10:30 UTC.

The load-bearing conclusions checked here are:

- Full matching SWAP transfers the complete arbitrary D/C/R state into D/E/R while preparing pure C; the old free flow includes every preparation stage.
- The runtime comparator has old factor `exp(-isH) W exp[-i(T+tau)H]`, with the runtime source phase still containing `+omega_l T`. Preparation time must not be inserted a second time into that phase.
- The common modeled added incident cap is `2J_*+g`, with both original and complementary channels counted. Complements, fresh memory, timing, phase references, isolation and pointwise implementation control remain supplied.
- The physical NN density terms give the full first/second release moments for every N>=2, including when `[H,B]` and `[H,B^2]` are nonzero. No symmetric projection may be inserted between the two K factors.
- The construction closes an externally driven D/C/E interface. It does not derive native purity or a microscopic quantum controller with its own output and energy budget.

There is one nonblocking notation clarification at candidate line 121. The shorthand `2 nu A_u` is valid if nu bounds the full additive operator error `||delta Gamma||`. If nu denotes a dimensionless common amplitude error in `(1+delta a)Gamma`, the corresponding bound is `2 nu ||Gamma|| A_u`. The candidate's general full-generator bound (11) is correct and already covers either case; the shorthand should name its norm/units before independent reuse. This review uses the additive operator-norm interpretation and makes no claim that a scalar coefficient alone bounds a large generator.

## Exact source coverage and inheritance

The root of the reviewed author packet is
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bus_installed_preparation_candidate`.
The root of this independent output is
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/bus_preparation_exposed_check`.

| Source | SHA-256 | Actual semantic coverage |
| --- | --- | --- |
| `DERIVATION.md` | `71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29` | Complete lines 1-279 |
| `FREEZE.json` | `ff5073ee47aac64e332b47938c29774f3b4aa6ccfc8ed7b14011e29587eaeeb3` | Complete inventory/status; provenance only |
| `sources/bus_note.md` | `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b` | Lines 24-65, 297-324, 438-527, 583-669, 772-789; additional whole-file keyword search used for navigation |
| `sources/compensated_reservoir.md` | `d28bb8d6a39ffcdce60f61fb47414abdcdd00e2cbbbb32013c4f8277b2a72ac8` | Lines 325-625 and 769-847, complete |

The exact source paths, byte lengths, captures and instruction hashes are in `SOURCE_MANIFEST.json`. Applicable captured planning instructions and the campaign science workflow were read; the local workhorse skill supplied the bounded-check and evidence discipline. The inherited model and reasoning effort were retained. No further agents or external chat tools were used.

The accepted runtime-bus estimate is an explicit premise of this review. I checked the statement, literal generator, phase/chronology, ledger and target-refinement sections needed for composition. I did not independently redo its spectral construction, gap selection, calibration, Sylvester correctors, or retained-status history. Nor did I inspect the full other preparation papers summarized in the candidate's opening comparison. Those comparison claims are not prerequisites for the constructive proof checked here.

The scientific independence is limited and disclosed. This is a separate child context in the same inherited model family, exposed to the complete candidate derivation and its reported checker design/results. An initial file inventory computed hashes of all author-packet files, including the author's checker bytes. That was byte access for hashing, not semantic inspection or execution. The author's `check_release_moments.py`, copied executed source, launcher and result contents were never inspected or executed. This review imports none of that code. The complete general derivation below was fixed in `ANALYTIC_FINDINGS.md` before constructing the new checker; its separate pre-computation freeze remains preserved.

## Independent derivation

The following is the complete analytic argument frozen before the independent computation. Its scope statements use the source exposure already described above.

This file records the derivation reached before writing or running the independent algebra checker. The candidate under review is `DERIVATION.md`, SHA-256 `71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29`. The initial conclusion is that its mathematical preparation/release composition is valid under its explicitly supplied driven-model premises. This is neither root acceptance nor an audit verdict.

## 1. Full SWAP with arbitrary correlations

For arbitrary basis labels `d,c,r`, the matching unitary satisfies

    S_CE (|d,c,r> tensor |0_E>) = |0_C> tensor |d,c_E,r>.

Linearity proves the identity for every vector, including vectors entangled between D,C,R. Applying it to matrix units proves the corresponding identity for every mixed input. Thus the map called Q is an isometric relabeling, not a partial trace or replacement of the old marginal. Every original C correlation is transferred to E. There is no need for sigma_DCR to factor. The exact ready-E premise is global independence from DCR; a marginally pure E already implies such independence, but a merely approximate marginal certificate has no stated trace-error conversion here.

Each SWAP is generated exactly by the positive operator `(pi/2)(I-S)` because its eigenvalues on the symmetric/antisymmetric subspaces are 0/pi. Its exponential is S, with no leftover scalar. For `Y_phi=cos(phi)Y-sin(phi)X`, direct action gives `Y_phi|0>=i exp(i phi)|1>`. Therefore the positive source pulse `Q_phi=(pi/4)(I+Y_phi)` gives `exp(-iQ_phi)|0>=exp(-i pi/4)|alpha_phi>`. The phase from all source rotations is `pi n_S/4`.

The comparator generator `H+u(t)C0 I+G(t)` has commuting H and controller parts. The complete preparation endpoint is consequently

    exp[-i(C0 integral u + pi n_S/4)]
       |Omega_phi> tensor (exp(-i tau H) tensor I_ER) Q.

All four stages, including both ramps, contribute to tau. The comparator's source is stationary on the release ramp; the actual residual source evolution on that ramp is paid in the error bound.

## 2. Duhamel, positivity, and physical load

The literal old H is untouched. From `0<=h_j<=c_j I`, each separately installed complement `Gamma_j=c_j I-h_j` is positive, has norm at most c_j, and has the same declared support. Their sum is exactly `C0 I-A`. The actual generator is `H+(1-u)A+u C0 I+G`; the difference from the comparator is `(1-u)A`.

Duhamel evaluated on the comparator input uses the full norm `||A||<=C0` before the SWAP. After the two pulses it uses `||A J_Omega||=G_Omega`, uniformly in the arbitrary aged D,E,R vector. Multiplication by `exp(-itH)` on the old input does not change that operator norm. The plateau residual is zero. Since each ramp has integral `(1-u)=r/2`,

    ||U_prep J - V_prep|| <= (C0 r_on+G_Omega r_off)/2.

Purification converts this to a full-output unhalved trace bound `C0 r_on+Gbar r_off`; adding an initially certified trace error and twice the integrated full Hermitian generator error gives equation (11). No actual-state code-invariance assumption is used.

At any site, the installed h_j ledger and the independent complement ledger each cost at most J_*. A matching SWAP has norm `2gamma`, and a source pulse has norm `pi w/(2t_p)`. Their stages are disjoint. The chosen durations make either pulse load at most g, so the common modeled added incident bound is `2J_*+g`. This counts the two channels despite their algebraic cancellation. It does not constrain a microscopic drive or infer a pointwise implementation cap from an integrated error bound. The latter requires the separately stated slack/certificate.

The global sum C0 may grow with size. It obeys `C0<= (n_C+1)J_*` by summing the incident ledger over C and the unique old port, since every term is counted at least once. The memory matching in the explicit embedding is injective, avoids C and the nonnegative old box, and uses unit L1 edges; its extra geometric adjacencies still need isolation.

The pulse action and variation follow from `||I-S||=2`, `||Q_phi||=pi/2`, `integral w=1`, and `integral |w'|=2m0`. They give the candidate's equations (15)-(17). The complete generator norm is at most `||H||+C0+g n_C`, since `||(1-u)A+u C0 I||<=C0`. The endpoint work identity is the finite closed driven identity `d Tr(rho K_prep)/dt=Tr(rho dot K_prep)`. Its variation bound does not construct a power supply or prove cooling.

## 3. Literal time, source phase, and the exact marginal

The inherited bus estimate is uniform over the old input and a passive reference. At release, its reference can be ER. Its old comparator `exp(-isH) W exp(-iTH)` acts on `exp(-i tau H)Q sigma Q* exp(i tau H)`. The two consecutive right-hand H flows combine to

    exp(-isH) W exp[-i(T+tau)H] Q.

The target thus uses the original input and the actual total time `T+tau+s`. It does not require preparation to preserve the old state rather than its free H aging.

The parent phase prescription fixes `G_phi=exp(iHT)L exp(-iHT)/t_*` with runtime origin at release. Preparation supplies that phase at release. Therefore its `+omega_l T` remains correct; using `T+tau` in that phase generally inserts an extra H-conjugation of W. H aging before release is already on the input side of the runtime map and must not be counted again in the control phase.

Applying the actual runtime unitary to the preparation error, then comparing to the nominal bus unitary, proves total trace error `e_p+delta_bus+2e_r`. The ideal aged old/ER state is not asserted to equal the actual release marginal. If one rewrites the premise as a product with the exact actual marginal, a separate marginal-shift cost is necessary. The candidate states this distinction correctly.

The exact-target allocation is `epsilon/8+3epsilon/4+2(epsilon/16)=epsilon`. For the inherited rational target refinement at working tolerance epsilon/2, nominal bus error is `3epsilon/8`, preparation error `epsilon/16`, and runtime error `2(epsilon/32)`, totaling epsilon/2. Approximating L by M within epsilon/32 adds at most epsilon/16 in full trace norm, yielding 9epsilon/16. This relies on the inherited rational-support repair; the new preparation theorem does not prove the parent bus's spectral/calibration construction.

## 4. Full installed moments from a Gram operator

This derivation does not expand K squared or insert a code projection. Apply K once to the prepared embedding J. Split its image by orthogonal bus sectors:

    KJ psi = |0_bus> tensor [H+R+sum_l f_l] (psi tensor Alpha)
             + xi v_p |1_c1> tensor (B psi tensor Alpha)
             + xi sum_l r_l |1_ul> tensor
                    (psi tensor sigma_-^(l,1) Alpha).

The bus vacuum and the c1/u_l single-excitation states are mutually orthogonal. Bus hopping/onsite terms annihilate the vacuum. Every source ferromagnetic term annihilates the identical source product before K acts, even for complex phase. All reserve constants are in the actual R. The f_l include the literal NN source density operator; f_l Alpha need not be symmetric.

Since K is Hermitian, `J* K^2 J = (KJ)*(KJ)`. In the vacuum sector H acts on D and f_l on different source factors. Writing `mu_l=<f_l>` and `v_l^mom=<f_l^2>-mu_l^2` gives `(H+cI)^2+sum v_l^mom I`, where `c=R+sum mu_l`. The port sector gives `xi^2 v_p^2 B^2`. Each source sector gives `xi^2 r_l^2/2`, because `||sigma_- alpha||^2=1/2`. This proves both operator compressions (23) for arbitrary old dimension, any number of distinct source attachment sites, every N>=2 and arbitrary phase. There is no H/B commutation assumption.

For one length-N source, let independent fair bits X_j have K_s=sum X_j and D_s=sum X_j X_(j+1). Then

    E K_s=N/2,      E D_s=(N-1)/4,
    Var K_s=N/4,   Var D_s=(5N-7)/16,
    Cov(K_s,D_s)=(N-1)/4.

The D variance has N-1 terms of variance 3/16 and N-2 unordered adjacent pairs of covariance 1/16. The covariance with K_s has two endpoint contributions of 1/8 per bond. Thus the candidate's equation (22) follows for all real a_l,b_l, including negative b_l. These are full NN moments, not symmetric-code moments.

Subtracting the H column from KJ proves

    J* A^2 J = [c^2+sum_l v_l^mom+(xi^2/2)sum_l r_l^2]I
                    +xi^2 v_p^2 B^2.

Its largest eigenvalue is the scalar term plus `xi^2 v_p^2 ||B||^2`, proving (24). The source variances are nonnegative even when their displayed cross coefficient is negative. The independently known global norm bound provides `G_Omega<=C0`.

With rho_D(tau)=exp(-i tau H)sigma_D exp(i tau H), H moments are conserved by the ideal preparation. Tracing the two compressions therefore gives (25), with `Tr(B^2 rho_D(tau))` at the actual release time. This generally differs from its value on sigma_D. Arbitrary D/ER correlations do not alter this unconditional expectation calculation; they are still present in the full target.

For a fixed center a and beta>=||K-aI||, trace duality bounds the centered first/raw-second differences by beta e and beta^2 e. The difference of the two squared centered means is at most 2 beta^2 e, proving the 3 beta^2 e variance bound. Duality against an arbitrary norm-one reference observable gives the reference-valued bound (27). These linear operators are not conditional variances or measurement channels.

## 5. A general off-code discriminator derived here

On the symmetric source code, `P_sym D_s P_sym=K_s(K_s-1)/N`. For a binomial K_s, factorial moments give

    Var[K_s(K_s-1)/N]=(N-1)(2N-1)/(8N).

For example, `(K_s)_2^2=(K_s)_4+4(K_s)_3+2(K_s)_2` and `E(K_s)_j=(N)_j/2^j` establish this directly. Its mean and covariance with K_s equal those of D_s. Hence the squared off-code residual on the coherent source is exactly

    ||(I-P_sym)D_s Alpha||^2
       = Var(D_s)-Var[K_s(K_s-1)/N]
       = (N-2)(N+1)/(16N).

It vanishes at N=2 and is positive at every N>=3. Replacing physical D_s by the compressed expression consequently loses `sum_l b_l^2 (N-2)(N+1)/(16N)` from the second-moment compression while preserving the first moment. At N=3 this reduces to the candidate's 1/12 residual. This is the planned planted defect for the independent checker.

## 6. Scope and limits at this stage

Fresh purity, globally controlled ready-state error, positive complementary couplings on all named supports, phase-referenced rotations, complete matching SWAPs, vacant memory sites, isolation, complete generator calibration, fixed timing, and zero/passive retained E remain premises. So do the accepted runtime bus's spectral, geometry and effective-target hypotheses. The external drive has no quantum output in the prescribed time-dependent model; a microscopic F with a ready state, complete retained output and energy/covariance ledger is an unresolved stronger interface. No autonomous or reusable supplier, native purity theorem, thermodynamic cost theorem, permanent halt, or generic Lie-to-static realization follows.

The source's broad comparison sentences about other preparation papers are not independently established here: only the named bus and compensated-reservoir premise sections were inspected. They are not needed to prove the new conditional construction. The independent check inherits the same model family and is source-exposed. No formal retained status follows.

The author's checker was not semantically inspected or executed. An initial inventory hashed all files in its directory, including its checker; this is disclosed byte access. The complete candidate derivation exposed the author's checker design and reported results in section 8. Our checker will instead use pure-Python exact Gaussian rational bitstring actions and a combinatorial state-count recurrence, with no imported author code or expected output files.


## Independent exact-arithmetic execution

One substantive algebra execution was performed, using Python 3.13.5 and standard-library `Fraction` arithmetic for exact Gaussian rationals. The new `independent_bitstring_check.py` constructs K's action on computational-basis source vectors directly, stores sparse output columns, and forms their exact Gram matrices. It does not construct or import the author's SymPy matrix. It also obtains source occupation statistics from an exact integer recurrence over `(occupied sites, occupied adjacent bonds, final bit)`, rather than enumerating a matrix for each N.

The complete executed source is `run_001/executed_source.py`, SHA-256 `52643e77065591b7440040f54c325500ae9b17bf13f81b5bca4f09ee094fccbd`. The actual run began 2026-10-16T04:07:53.155192Z, ended 04:07:58.116883Z, took about 4.961 seconds, and exited 0 under a 60-second child limit. The launch record includes the actual Python executable, argv, cwd, copied source, source hash, source/premise manifest and the frozen analytic-findings hash. Full stdout is 9,528 bytes, SHA-256 `160e6f51eddb8f2c01b1b7d34c510b8f875ca5b4bab0e8fe4f3a2df57abde107`; stderr is empty. I read the complete stdout. The launch and execution records, launcher-at-launch and full streams are in `run_001/`.

Its discriminating checks were:

- Exact occupation recurrence for every N from 2 through 40. It recovered the full NN variance, mixed covariance and the general off-code residual derived above. Omitting adjacent-bond covariance fails for every N>=3.
- Ten exact local-operator fixtures: `(number of sources,N)=(1,2),(1,3),(1,4),(1,6),(1,8),(2,2),(2,3),(2,4),(3,2),(3,3)`. Their old plant has two qubits, with complex Hermitian `H=X0/2+Y0 Z1/3+2 Z0 X1/5+7 Z1/11` and local `B=I/2+Z0/3`. The checker explicitly finds `[H,B^2]` nonzero. Sources use phases i, -1 and -i, and counterterm signs vary. The largest fixture has 15 total qubits but needs only 2,816 nonzero KJ coordinates per old column. Every first/second compression and A-squared compression agrees exactly, and the resulting G-squared is below the explicit C0-squared bound.
- A planted replacement of D by `Nhat(Nhat-1)/N` preserves the first compression and loses exactly `sum b_l^2 (N-2)(N+1)/(16N)` from each diagonal of the second. For example the three-source N=3 fixture loses `200/2381643` per old vector. The checker also rejects replacing the physical second compression by the square of the first.
- Exhaustive 32-basis-input verification of the full D/C/R-to-D/E/R SWAP embedding for a two-qubit controller, including the linear extension to all coherences. A source-rotation check with unit phase `3/5+4i/5` rejects the opposite phase orientation.

These fixtures exercise the local release algebra; their source frequencies and coefficients are not asserted to solve the inherited full bus calibration. They are not full routed-bus runs, pulse propagation, a proof by finite sampling, an error-family test, a microscopic controller model, or a formal proof certificate. The arbitrary-N and arbitrary-input conclusions rest on the explicit analytic derivation.

One separate provenance-only execution in `run_002_provenance/` compared captured sources to the live original bytes, checked the scientific execution source/streams/argv/cwd, and rejected four in-memory tamper probes: changed candidate bytes, changed bus-note bytes, changed compensation-note bytes, and changed scientific stdout. It exited 0 at 04:10:30.631502Z; its source-at-launch, argv/cwd, actual exit and full streams are retained. These checks establish matching evidence identities only. No source or stream file was altered by the tamper probes, and no mathematical result follows from their success.

No failed scientific execution or broad test replay occurred. No author program was rerun. No canonical source, Git state, publication, lock, audit record, physical axiom or editable prompt was changed. Only the assigned independent-check directory was written.

## Remaining obligations and recovery

The unresolved physical obligations are the ones the candidate names: fresh independent pure E, actual availability of all signed nonscalar complement interactions, complete positive SWAP/rotation controls and their phase references, memory vacancy and isolation, full-generator calibration over the potentially long preparation/runtime interval, sufficient slew, known external scheduling, passive memory storage, and a complete microscopic driver F if such an all-output claim is later requested. The initial old input remains arbitrary; no target-specific old-state supplier has been constructed or assumed.

This is a finite, single-use, externally driven conditional supplier. Memory is consumed. The complete installed moments may grow with apparatus size; bounded incident strength does not bound total energy or establish thermodynamic preparation work. Existing strong-spectral/geometry restrictions remain. A native or autonomous general-realization claim would need additional arguments and evidence.

For recovery, start with `REVIEW.md`, then inspect `ANALYTIC_FINDINGS.md`, `run_001/executed_source.py` and its full stdout, and `SOURCE_MANIFEST.json`. `FREEZE.json` identifies the final immutable review packet. Reopen the affected review if the candidate/premise bytes or the meaning of the supplied controls change. The root's acceptance decision remains separate.

<!-- END UNCHANGED BODY original_exposed_review -->

<!-- BEGIN UNCHANGED BODY original_root_reconstruction -->
# Root reconstruction before the separate preparation review

This source-exposed reconstruction concerns candidate DERIVATION.md SHA256
71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29.
The root read the complete candidate and author discriminator. These are
analytical checks, not an additional scientific execution or blind validation.
The separate reviewer was sent the statement and necessary parent premises,
without the author's numerical implementation. Its findings are still pending.

For the actual positive bus blocks, let A=sum h_j, 0<=h_j<=c_j I.
The supplied complements sum to C0 I-A, C0=sum c_j. Thus the physical
generator H+A+u(C0 I-A)+G differs from H+u C0 I+G by (1-u)A.
This does not delete installed terms. Both channels have local load at most
J_*; disjoint pulse terms add at most g. The cap 2J_*+g follows on every
site including the old port and new memory sites. An integral error allowance
alone would not establish this pointwise bound for a perturbed implementation.

The comparison pulse acts only on C,E and commutes with H on D, even on an
entangled DCR input. Its disjoint SWAPs transfer the entire C input to E.
The subsequent positive source rotation has exp(-i pi/4) times the required
equatorial vector on each source qubit; the parallel SWAP endpoint has no
remaining scalar. Comparison evolution therefore has exactly the stated
phase C0*A_u+pi*n_S/4, complete Q output, and exp(-i tau H) acting on D.
In the Duhamel integral use ||A||<=C0 before the SWAP and ||A J_Omega||
after the rotation. The intervening plateau has zero residual. Integrating
the two symmetric ramps gives operator error (C0*r_on+Gbar*r_off)/2,
then trace error C0*r_on+Gbar*r_off. No actual intermediate code invariance
or exact actual release marginal is needed.

For the new moment identity, decompose K J_Omega into orthogonal bus sectors.
Its vacuum part is H on D plus R and the independent source random variables
f_l=a_l N_l+b_l D_l. The port part has one excitation at c1 and amplitude
xi*v_p B; each source part has an excitation at its distinct u_l, with norm
squared xi^2*r_l^2/2. All cross terms between these bus sectors vanish.
The ferromagnetic source term kills the identical product vector, so it
contributes nothing to K J_Omega, even though it need not kill f_l Omega.
This suffices because J*K^2 J=(KJ)^*(KJ); commuting K through a projection
would be an invalid alternative argument.

For independent Bernoulli occupations x_j with mean1/2, Nhat=sum x_j and
D=sum x_j*x_(j+1): Var(Nhat)=N/4. A bond has variance3/16. Neighboring
bonds have covariance E[x_j*x_(j+1)*x_(j+2)]-1/16=1/16; disjoint bonds
have zero covariance. Therefore Var(D)=3(N-1)/16+2(N-2)/16=(5N-7)/16.
Each of a bond's two sites has covariance1/8 with that bond, yielding
Cov(Nhat,D)=(N-1)/4. Consequently Var(a Nhat+b D) is exactly equation22,
including signed b. Independent sources add their variances. The vacuum
contribution to the square compression is (H+cI)^2+sum Var(f_l) I,
and the orthogonal excitations add xi^2*v_p^2 B^2 and
(xi^2/2)*sum r_l^2 I. This proves equation23 without [H,B]=0.

Apply the same orthogonal decomposition to A J_Omega to obtain a scalar
c^2+sum Var(f_l)+(xi^2/2)*sum r_l^2 plus xi^2*v_p^2 B^2. Its norm is
the displayed equation24 because the scalar is nonnegative and B^2>=0.
This uses the complete physical NN density operator. At N=3, replacing
D by Nhat(Nhat-1)/3 subtracts exactly 1/12 from its product-state variance.
No amount of preserved first-moment data justifies that substitution.

Actual old aging preserves H moments but can change B^2 expectation, hence
equation25 must use rho_D(tau), not the original sigma_D, in that term.
Centered first/second moments are Lipschitz in full trace distance with
constants beta and beta^2. Bounding the difference of squared centered means
by 2 beta^2 e gives the stated 3 beta^2 e variance allowance. The analogous
reference-valued linear moment bound follows by duality, not a conditional
variance argument. The external-drive work identity prices only the specified
driven generator and supplies no microscopic driver energy.

Finally, the bus acts on the ideal release input, with E,R retained. Its old
factor is exp(-isH) W exp(-iTH) exp(-i tau H), which equals
exp(-isH) W exp(-i(T+tau)H). The source phase is set at the release origin;
adding omega*tau without changing the definition would be a different target.
Composition costs e_p+delta_bus+2e_r by one telescope. Requiring a product
against the exact actual release marginal instead costs up to2e_p and must
not be silently substituted. Durations can be chosen after the bus instance
because its phase-independent norms determine preparation allocations; the
axes are then assigned the already determined T-dependent source phases.

No load-bearing defect was found in this reconstruction. Final acceptance
awaits the separate scoped check. Conditional fresh pure memory, the actual
complement controls, reference phase, schedule, calibration, isolation and
specified microscopic drive outputs remain open physical suppliers. The
existing accepted bus, compensation and finite-memory contracts remain
provisional dependencies pending their independent retained audit. This is
not a new autonomous construction, native-energy identification, permanent
halt, reader, thermodynamic erasure theorem or reusable-memory supplier.

<!-- END UNCHANGED BODY original_root_reconstruction -->

<!-- BEGIN UNCHANGED BODY original_controlling_qualifications -->
# Qualified acceptance of installed-bus preparation and release

This accepts a conditional externally driven preparation and release composition at candidate SHA-256 71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29. It is a source-side research decision, not retained status, an audit verdict, publication approval or an observed implementation. The inherited runtime bus remains the qualified theorem in PR9631, canonical note SHA-256 1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b. No autonomous microscopic preparation claim follows.

The accepted construction starts with the actual positive installed addition A=sum_j h_j and supplied positive complementary blocks Gamma_j=c_j I-h_j on the same supports. It retains arbitrary old/source/reference input by transferring the full original apparatus C to fresh independent vacuum memory E with matching SWAPs. Every E qubit is retained in the output as consumed memory. All preparation stages contribute to tau and to the old free flow. The accepted added incident cap is 2 J_*+g, counting both installed and complementary channels. Fresh purity, matching geometry, isolation, the phase reference, timing and pointwise implementation control remain premises.

The ideal comparator is exp(-i Phi)|Omega_phi> tensor the complete relabelled old input after exp(-i tau H), with Phi=C0 A_u+pi n_S/4. The preparation trace budget is eta_ready+C0 r_on+Gbar r_off+2 integral ||E_p(t)||dt. The candidate's line-121 shorthand 2 nu A_u is accepted only when nu bounds the additive operator norm ||delta Gamma||. If nu instead bounds a dimensionless relative coefficient error, the bound is 2 nu ||Gamma|| A_u. This qualification controls over the ambiguous shorthand; the frozen candidate is preserved unchanged. Integrated error control alone does not establish pointwise incident-load slack.

The runtime phase is still phi_l=arg L_ab-arg kappa_ab+omega_l T. Preparation time tau must not be added again to omega_l T. The old output comparator is exp(-i sH) W exp[-i(T+tau)H], with elapsed time T+tau+s. The ideal release marginal and the actual release marginal are distinct. The direct preparation/runtime telescope costs e_p+delta_bus+2 e_r; switching to a product comparator built from the actual release marginal can cost a further e_p.

Release moments use the full physical nearest-neighbour density term, never a projection between the two K factors. For N>=2 and f=a sum n_j+b sum n_j n_(j+1), mu=aN/2+b(N-1)/4 and Var(f)=a^2 N/4+b^2(5N-7)/16+ab(N-1)/2. With c=R+sum mu_l, the first compression is H+cI. The second is (H+cI)^2+sum Var(f_l) I+(xi^2/2)sum r_l^2 I+xi^2 v_p^2 B^2. No commutation of H and B or B^2 is assumed. Statewise release variance uses B^2 evaluated in the aged old marginal after time tau. The full added-generator column bound G_Omega^2=c^2+sum Var(f_l)+xi^2[v_p^2||B||^2+sum r_l^2/2] is at most C0^2.

For a centered full-generator norm bound beta, trace preparation error e_p costs beta e_p in the first moment, beta^2 e_p in the second and 3 beta^2 e_p in variance. Runtime integrated operator error e_r gives the corresponding 2 beta e_r and 6 beta^2 e_r mean/variance allowances. All scalar reserves remain in uncentered physical moments. Identical low moments do not certify source phase: phases differing by pi give orthogonal preparation states while retaining those moments.

The independent checker additionally derives ||(I-P_sym) D_nn Omega||^2=(N-2)(N+1)/(16N). This formula is accepted as a reviewer-derived refinement, with a separate root algebraic reconstruction. It is zero at N=2 and positive for N>2; multiplying by b^2 gives the omitted second-moment contribution. It is not attributed to a generic simulator or to the original N=3 author fixture.

Evidence consists of the complete candidate, necessary unchanged parent premises, a root reconstruction frozen before receiving the separate review result, the complete source-exposed review, and one independently written exact Gaussian-rational bitstring execution. The reviewer saw the candidate and its reported fixture; it did not semantically read or import the author's checker. The root had already read the author checker before its own reconstruction. Both agents use the user's selected model; this is not model-family independence. The separate run checks ten one-to-three-source fixtures, an occupation recurrence for N=2..40, complete finite SWAP basis action and the rotation phase. It does not propagate the full pulse schedule, simulate the full routed bus, prove arbitrary-dimensional runtime dynamics computationally, or provide a laboratory validation. The analytic arguments carry the family-level claim. A second execution checks provenance and four in-memory tamper probes only.

Native complementary controls, fresh purity, controller and clock energy, phase references, long-time calibration, full quantum controller records, final halt, reset/reuse and measured-energy identification remain open. No science was merged and no editable prompt file was changed by this acceptance.

<!-- END UNCHANGED BODY original_controlling_qualifications -->

<!-- BEGIN UNCHANGED BODY slew_proposal -->
# Proposed bounded-slew preparation with explicit memory evolution

Unaccepted root derivation. This revisits the fast-ramp obstruction in the accepted installed-bus preparation source71e9ec89 (root acceptance28bef194). It uses the same positive complementary controls and fresh memory premises. It does not supply native purity or a microscopic controller. No scientific program has been executed for this proposal.

The accepted parent runtime bus is canonical note1733b296, PR9631. On the complete old plant D and apparatus C, write the actually installed positive addition in the more detailed form

    K = H + A,
    A = R I + A_C + xi V_p,
    A_C = A_0 + xi V_s + xi^2 A2,
    A_0 = H_bus + sum_l(omega_l N_l + L_l),
    V_p = v_p B_p X_c1,
    V_s = sum_l r_l(sigma_+^(u_l) sigma_-^(a_l1)+h.c.).

Every operator except H and V_p acts solely on C. R is the actual complete reserve. A itself remains the original sum of positive local h_j, with supplied positive complements Gamma_j=c_j I-h_j, C0=sum_j c_j and Gamma=C0 I-A. Retain the parent per-site cap for the sums of c_j and complement norms. Let E be the complete matched fresh independent vacuum memory with zero uncoupled generator, and retain it in the final output. Arbitrary D/C/R input correlations are allowed.

Use the same four-stage schedule: raise u from0 to1, execute simultaneous matching SWAPs on C/E, rotate the source qubits into equatorial product states, lower u from1 to0. During every stage the actual nominal Hamiltonian is

    K_prep(t) = H + (1-u(t)) A + C0 u(t) I + G(t).

The gate pulse G vanishes during the two ramps and u=1 during both gate stages. No original H is subtracted. Assume a fixed smooth monotone shape F with F(0)=0,F(1)=1, flat endpoints, F(s)+F(1-s)=1 and sup|F'|=m_F. The integrals of f=1-u on the ramps are alpha_on=r_on/2 and alpha_off=r_off/2.

During the on-ramp, compare with H+f A_C+[R f+C0 u]I, dropping only xi f V_p. H and A_C act on disjoint factors, so this comparison is exact apart from a Duhamel operator error at most

    xi alpha_on ||V_p||.

The apparatus evolves by U_C=exp(-i alpha_on A_C). Matching SWAP transfers that complete evolved apparatus to E. This changes the ideal memory-output contract: if Q is the literal C-to-E relabelling of the original full input, the ideal old/reference/memory state is built from (I_D tensor U_E tensor I_R) Q (its adjoint), where U_E is the same A_C evolution relabelled onto E. Do not silently call this Q or discard E. U_E is unitary and depends on the actual installed generator; input information is retained but no memory reset/reuse is claimed. No physical inverse of U_E is requested.

The two middle gate stages have exactly H+C0 I+G(t). The full matching SWAP and positive source rotations are therefore the same exact gates as in the accepted candidate, commuting with old H. Their scalar rotation phase is pi n_S/4, where n_S=qN.

On the off-ramp compare with H+f A_0+[R f+C0 u]I. The retained full-space perturbation is f[xi(V_p+V_s)+xi^2 A2]. Let v>=||V_p+V_s|| and a2>=||A2|| be the parent full-space majorants. The operator error is at most

    alpha_off (xi v+xi^2 a2).

The bus vacuum and symmetric equatorial sources under A_0 evolve by ordinary source phases: exp(-i alpha_off omega_l N_l) sends phi_tilde_l to phi_tilde_l-omega_l alpha_off, while H_bus annihilates bus vacuum and L_l annihilates every symmetric source. Hence choose the *gate-stage* rotation angle

    phi_tilde_l = phi_l + omega_l alpha_off,

where phi_l is exactly the required runtime release phase, including +omega_l T. This extra known ramp correction must not change the runtime formula itself or insert tau into omega_l T.

Combining all stages gives a complete-output comparator at release:

    exp(-i Phi) |Omega_phi>_C tensor
      [exp(-i tau H)_D tensor U_E tensor I_R] Q,

with tau the duration of all four stages and

    Phi = C0 integral u(t)dt + R integral(1-u(t))dt + pi n_S/4.

For mixed arbitrary inputs this denotes conjugation on the retained D/E/R state, tensored with the pure C state; the scalar phase is meaningful only at the isometry/amplitude level. The proposed trace error bound is

    e_p <= eta_ready
           + xi r_on ||V_p||
           + r_off (xi v+xi^2 a2)
           + 2 integral ||E_p(t)||dt.

It avoids multiplying the two ramp widths by C0 because the large C-only evolution is either retained exactly in memory or propagated explicitly on the prepared state. The full residual A2 is still paid, including off-code leakage. This is a different comparator from the earlier literal-relabelled-memory version; the difference is material and must remain visible.

For fixed positive modeled slew allowance S_* per incident site, the ramps can have fixed positive durations independent of epsilon and N. If the sums of complement norms incident to any site are bounded by J_*, choose r_on,r_off>=m_F J_*/S_*. This bounds sum ||dot(u Gamma_j)|| by S_*. There is no gate pulse during these ramps.

Let a smooth nonnegative unit-integral bump chi have sup chi=m0 and sup|chi'|=m1. A matching SWAP pulse with integrated coefficient pi/2 multiplying I-SWAP has maximum incident norm pi m0/t_s and derivative pi m1/t_s^2. A source rotation pulse with integrated Q_phi=(pi/4)(I+cos(phi)Y-sin(phi)X) has norm bound pi m0/(2t_p) and derivative pi m1/(2t_p^2). Thus it suffices to choose

    t_s >= max(pi m0/g, sqrt(pi m1/S_*)),
    t_p >= max(pi m0/(2g), sqrt(pi m1/(2S_*))).

These gates use disjoint site matchings or independent onsite rotations. Their amplitudes and slew bounds do not depend on the source phase. During the gate plateaus the complement is constant. Therefore the complete modeled addition retains incident norm at most2J_*+g and incident derivative norm at most S_*, with smooth endpoints. This is a bound on the supplied Hamiltonian schedule, not hard spectral bandwidth or microscopic drive energy.

After N, calibration, v,a2 are chosen, an additional smallness condition on xi ensures the displayed preparation error. Taking r_on,r_off as fixed schedule constants, one can impose, for example, xi<=e/[8(1+r_on||V_p||+r_off v)] and xi^2<=e/[8(1+r_off a2)], along with readiness and implementation budgets. Recompute T=t_*/xi^2, runtime source phases, gate-stage ramp corrections and calibration precision afterward. Phase choice does not change any Hamiltonian norm or slew bound. A polynomial fixed-plant bound, if independently accepted, survives such polynomial extra constraints; that is presently a dependency, not a proved claim of this proposal.

The old marginal of the comparator at release remains exp(-i tau H) rho_D exp(i tau H), because U_E is on retained memory. Hence the accepted complete release-moment formulas remain valid for the ideal product source state and the aged old marginal. Actual moment errors use the new e_p, with the same full physical generator norm allowances. Later runtime output is compared to exp(-isH) W exp[-i(T+tau)H] on the old factor, with the same explicit U_E on memory. Neither identical moments nor memory unitarity certifies microscopic preparation or reuse.

Open checks: all factors and signs in the two ramp Duhamel bounds, exact transfer of arbitrary correlated input, phase and scalar ledgers, per-site derivative accounting, dependence of J_* and chosen ramp widths on the actual construction, and compatibility of changed memory comparator with downstream uses. Independent checking is required before acceptance. No no-go result is asserted.

<!-- END UNCHANGED BODY slew_proposal -->

<!-- BEGIN UNCHANGED BODY slew_exposed_review -->
# Exposed review: bounded modeled slew with evolved retained memory

**Disposition:** the proposed four-stage preparation works as a conditional external-control construction with fixed **per-site modeled** strength and first-derivative bounds, subject to the parent's supplied complements, fresh independent memory, matching, timing, phase and isolation premises. The ramp error factors, source-phase sign and scalar ledger are correct. The ideal memory output is materially changed to `U_E Q`; this does not establish the parent's literal-Q memory-output contract. Root owns acceptance.

This review concerns proposal SHA256 `6e09476675188bc8053e2b3b00095db3eb5e1ebf59c816c923da0675a33edc44`, 7,516 bytes, frozen by `2d9e190795cb86de679ee01850039f59405bd9745a3931e09955ef7f9bc33e1c`. Its preparation premise is candidate `71e9ec899920fdbb9af3ef56176550bffdfb8d8b77a300d6caa560a90009af29`, with controlling root acceptance `28bef1945c65f807be837286d6e795d888f3d8b9ebb75024ac26ee0084409641` and qualifications `1c94a58239c1bd9d168c837cf961522264a1f2d1705f3897ef541a3c8ced788e`. The unchanged canonical runtime bus has SHA256 `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b`. This is exposed same-model checking, not a retained audit, blind replication or physical realization.

## 1. Reconstructed stage comparison

Use the actual finite installed decomposition

`A=R I+A_C+xi V_p`, `A_C=A_0+xi V_s+xi^2 A2`.

R is the actual reserve, not a norm bound. Every term of A_C acts only on C; only V_p couples D to C. The actual positive complements still give

`K_prep=H+f A+C0 u I+G`, `f=1-u`.

Take a symmetric smooth monotone ramp F, flat at both endpoints, with `F(s)+F(1-s)=1`. Both ramp integrals of f equal half their duration, denoted alpha_on and alpha_off. Their u integrals are also half their duration.

On the first ramp use the comparison generator

`H+f A_C+(R f+C0 u)I`.

H and A_C commute because they act on different registers; A_C itself is fixed during the ramp. Its exact endpoint unitary is

`exp[-i(R alpha_on+C0 r_on/2)] exp(-i r_on H) tensor exp(-i alpha_on A_C)`.

The omitted operator is **only** `xi f V_p`. Its complete operator-norm Duhamel error is at most `xi alpha_on ||V_p||`, without requiring H to commute with V_p, or requiring the input on D/C/R to factorize. No strong C-only term has been discarded or replaced by a projected action.

During the SWAP and rotation stages u=1 exactly, so the Hamiltonian is `H+C0 I+G`. The disjoint full SWAPs commute with H. Their endpoint is exactly SWAP because

`exp[-i(pi/2)(I-S)]=exp(-i pi/2) exp(i pi S/2)=S`.

They transfer the **entire** initial apparatus, after its U_C evolution, into E. More precisely, for `U_C=exp(-i alpha_on A_C)`, the matching-SWAP identity on every input vector is

`S_CE (U_C |psi>_C tensor |0>_E) = |0>_C tensor U_E |psi>_E`,

extended linearly with identity on D and R. Thus all original entanglement and mixtures are transferred, with U_E acting on the relabelled C factor. This is not a fresh pure E output or a physical inverse operation on E.

The source rotation gate has

`Q_theta=(pi/4)(I+cos(theta)Y-sin(theta)X)`,

`exp(-i Q_theta)|0>=exp(-i pi/4)(|0>+exp(i theta)|1>)/sqrt(2)`.

There are n_S such qubits, so their endpoint scalar is `exp(-i pi n_S/4)`. There is no additional endpoint SWAP scalar. The nonzero integrated scalar of the SWAP Hamiltonian is already included in the exact identity above and must not be counted a second time.

On the last ramp compare with

`H+f A_0+(R f+C0 u)I`.

The omitted **full-space** operator is `f[xi(V_p+V_s)+xi^2 A2]`. The comparison has bus vacuum and symmetric source product state. On this state the unreserved bus Hamiltonian vanishes, each ferromagnetic L_l vanishes, and the source field evolves its phase by

`exp(-i alpha_off omega_l N_l)|Alpha_l(theta)> = |Alpha_l(theta-omega_l alpha_off)>`.

The positive sign in the required gate setting is therefore correct:

`theta=phi_tilde_l=phi_l+omega_l alpha_off`.

There is no extra scalar here in the parent's fixed convention `(|0>+exp(i phi)|1>)/sqrt(2)`. The actual perturbed trajectory need not remain in vacuum or a symmetric source subspace: all of its deviation is bounded using the full residual norm. In particular A2 is not compressed between code projectors.

The resulting complete endpoint comparison is exactly

`V_new = exp(-i Phi) |Omega_phi>_C tensor [(exp(-i tau H)_D tensor U_E tensor I_R)Q]`,

`Phi=C0 A_u+R(alpha_on+alpha_off)+pi n_S/4`,

`A_u=t_s+t_p+(r_on+r_off)/2`, `tau=r_on+t_s+t_p+r_off`.

This equals the root's integral formula. All H phases remain in its actual free flow; all on-ramp A_C phases remain in the full U_E. C0 is the actual chosen sum of complement coefficients, even when those coefficients were chosen as conservative norm bounds. Using a different upper bound for C0 or R in Phi would change this amplitude-level assertion.

## 2. Error factors and arbitrary correlated inputs

Let `v>=||V_p+V_s||` and `a2>=||A2||` be complete-space bounds. The last ramp has operator-norm error at most `alpha_off(xi v+xi^2 a2)`. A stagewise unitary telescope therefore gives

`||U_prep J-V_new|| <= xi alpha_on||V_p||+alpha_off(xi v+xi^2 a2)`.

Applying the isometry-to-unhalved-trace-norm inequality contributes a factor of two. Adding the initial joint readiness error and the full implemented-generator error gives

`e_p <= eta_ready + xi r_on||V_p|| + r_off(xi v+xi^2 a2) + 2 integral ||E_p(t)||dt`.

The factors in the proposal are correct. This holds uniformly over arbitrary old/apparatus/reference input states and arbitrary entanglement: the norm estimate is for the complete input isometry, and tensoring a passive reference does not change its operator norm. A scalar phase has no effect on a density operator but is retained in the isometry ledger.

The accepted preparation qualification about implementation error remains controlling. An additive bound on the **operator** error is what enters the integral. A relative coefficient error in a complement instead carries the complement's operator norm; no `2 nu A_u` shortcut is justified for a dimensionless relative nu. Unlisted E storage dynamics and couplings also remain part of the complete error budget, including the subsequent long runtime.

## 3. Per-site strength and derivative accounting

During a ramp, every installed h_j is static and the gate pulse vanishes. At site x,

`sum_(j incident x) ||d(u Gamma_j)/dt|| <= |u'| sum_(j incident x)||Gamma_j|| <= (m_F/r) J_*`.

Thus `r_on,r_off >= m_F J_*/S_*` suffices for the stated per-site slew allowance. This is independent of N and requested accuracy **because** the parent supplies one uniform incident bound J_* across the finite bus family and xi is chosen within that family’s strength constraints. A single-instance bound that grows with N would not establish this conclusion. The actual parent positive-block ledger bounds the sums of c_j, hence also the complement norms, uniformly after its weak-coupling constraints.

For a fixed nonnegative smooth unit-integral bump chi, the matching SWAP block is

`[pi chi(t/t_s)/(2t_s)] (I-S)`.

Since `||I-S||=2`, its incident peak norm and derivative are at most `pi m0/t_s` and `pi m1/t_s^2`. Each matching endpoint meets only one such pulse. The onsite source gate is `chi(t/t_p) Q_theta/t_p`, with `||Q_theta||=pi/2`, so its bounds are `pi m0/(2t_p)` and `pi m1/(2t_p^2)`. Both are independent of theta.

The displayed choices

`t_s >= max(pi m0/g, sqrt(pi m1/S_*))`,

`t_p >= max(pi m0/(2g), sqrt(pi m1/(2S_*)))`

are consequently correct. The complement is constant during each pulse plateau. The two gate stages do not overlap. With the parent's flat compactly supported bump, pulse values and derivatives vanish at their boundaries and the complete schedule joins smoothly. The start and end preparation controls and their first derivatives are zero.

Counting the original positive blocks **and** the complement channels gives the common incident norm bound `2J_*+g`; the derivative bound is S_* because only a ramp or one gate stage changes at a time. The old H is unchanged and has zero time derivative. E sites acquire only their matching pulse in the modeled schedule.

These are per-site bounds. The global `||dK_prep/dt||` can grow with the number of simultaneously driven sites. They are not hard bandwidth, microscopic-drive energy, or a derivative bound on unspecified implementation errors. To promote nominal bounds to a perturbed physical implementation, separate pointwise incident amplitude **and derivative** slack/certificates are required; small integrated `||E_p||` alone supplies neither.

## 4. Choice order and moment accuracy

For the accepted finite construction, N, the free spectral parameters, routing, calibration, unscaled V and A2, and their finite norm bounds are fixed before xi. The parent allows further reduction of xi. The uniform J_*, chosen g and S_*, and fixed waveform bounds then permit fixed r_on,r_off,t_s,t_p independent of N and accuracy. In particular the ramp durations do not have to shrink as the preparation error tolerance shrinks.

Writing `b1=r_on||V_p||+r_off v`, `b2=r_off a2`, the proposal's additional constraints imply

`xi b1 <= e/8`, `xi^2 b2 <= e/8`.

For example the accepted allocations `eta_ready<=e/4` and `integral||E_p||<=e/8` then give `e_p<=3e/4<=e`. The allocation is conservative, not a missing factor. Intersect these restrictions with every runtime/cap requirement and `xi<=1`; every bound is strictly positive for finite supplied data. The unscaled coefficients need not be small.

After the final xi is selected, recompute T=`t_*/xi^2`, runtime phase `phi_l` with its existing **+omega_l T**, gate phase `phi_l+omega_l alpha_off`, the actual R and C0, U_E, Phi, and all accuracy/installation budgets that depend on that hardware and time. Do not insert tau into omega_l T. A_C and the physical runtime norms do not depend on the final coherent phases, while the gate norms do not depend on their axes; no phase-duration fixed point occurs.

For separately requested moment tolerances, avoid selecting e using an unknown future beta(xi). One simple noncircular refinement is to use the parent ledger's uniform bound

`beta_bar = ||H-aI|| + (n_C+1)J_* >= ||K(xi)-aI||`

for all subsequently reduced admissible xi. Choose e additionally below `E_mean/beta_bar` and `E_var/(3 beta_bar^2)` before choosing xi (or use positive guarded upper bounds in a trivial zero case). Then the accepted first/second/variance error estimates apply with the new e_p. This is a reviewer clarification of the ordering, not a need to hold the old numerical T fixed after tightening preparation accuracy.

The conditional mathematics permits arbitrarily small xi. It does not make readiness, coefficient precision, long-time storage or a microscopic scheduler native. No total polynomial bound is established here. Preservation of an independently accepted polynomial bound would require all newly inserted coefficients, requested error budgets and prior construction factors to satisfy that bound; it is not inferred merely from fixed-duration ramps.

## 5. The memory comparator cannot be silently inherited

The prior accepted preparation result targets `Q sigma Q*` in memory, aged only on D. The new result targets

`(exp(-i tau H) tensor U_E tensor I_R) Q sigma Q* (...)^*`.

Unless U_E is a scalar on the supported input space, these define different complete-output channels. A unitary on a retained output cannot be discarded because it is known or reversible in principle. No implementation of its inverse is supplied here. A consumer requiring the literal-Q memory record must be changed explicitly or charged a separate, generally order-one discrepancy.

This distinction is not repaired by equal release moments. Ordinary moments of K on D/C only see the aged old marginal, because the ideal C state is Omega and U_E acts on E. Thus the accepted physical K and K^2 compressions and scalar mean/variance formulas apply unchanged, with the same off-code source-density term and `B^2` evaluated at the actual tau-aged old marginal. The actual release marginal is only within e_p of that ideal marginal, not exactly equal to it.

Reference-valued moments that retain E, however, have their **ideal operators conjugated by U_E**. Their norm-error bounds continue to hold relative to the new ideal state; their values are not generally identical to the old comparator's. A consumer of complete D/E/R correlations must likewise use the new state.

After release, E remains a passive retained reference with its supplied zero generator. Applying the uniform runtime bus estimate to the new ideal product state gives

`exp[-i(Phi+chi(t))] |0_bus> tensor [product_l exp(-it omega_l N_l)|Alpha_l(phi_l)>]`

`tensor [(exp(-isH) W exp[-i(T+tau)H] tensor U_E tensor I_R)Q]`,

with `t=T+s`. The direct trace telescope remains `e_p+delta_bus+2 e_r`. If a formulation instead uses the exact actual release marginal, the same additional marginal-shift allowance as in the accepted parent is needed. Nothing makes the changed memory output interchangeable with Q.

## 6. One actual finite discriminator

I wrote a new 128-dimensional complete-isometry calculation on one old qubit, one bus qubit, two source qubits and all three matching memory qubits. It does not import or replay an author checker. Its purpose is to discriminate the memory and phase conventions, not simulate a full strong-spectral runtime bus.

The test is at the commuting `xi=0` boundary. Here both proposed weak-ramp errors are exactly zero and the stage propagators follow analytically from the ramp integrals; no numerical integration or guessed ramp trajectory is involved. It uses `H=.36 X+.27 Z+.23 I`, omega=.9, positive bus field 1.7, source ferromagnetic coefficient .4, actual reserve R=2.3 and C0=6.6. The source generator includes its actual adjacent swap. The ramp durations are .8 and 1.2, alpha_on=.4 and alpha_off=.6, and total tau=4.4. The specified release phase .37 therefore requires gate phase .91. Full matching SWAPs are constructed as computational-basis permutations, and all 16 old/apparatus input columns are propagated with the memory initially vacuum.

The new complete comparator agrees with the directly composed stage isometry to about **5.6e-15**. Replacing U_E by identity gives isometry error **1.2884**; the overlap is not a scalar matrix (nonscalar norm **.7311**), so this is not merely an arbitrary global phase. Reversing the off-ramp phase correction gives error **1.1430**; omitting it gives **.6377**. Omitting the R ramp contribution to Phi gives amplitude error **1.8255**. The first and second physical-moment operator compressions for the two different memory comparators nevertheless agree to within **4.4e-15**.

An analytic density-level example makes the same distinction: superpose initial apparatus bus vacuum and one bus excitation (or correlate these two alternatives with orthogonal old states). On the first ramp their relative memory phase is `exp(-i alpha_on nu)`. The resulting pure-state trace distance from literal memory transfer is `2|sin(alpha_on nu/2)|=2|sin(.34)|`, despite identical ordinary D/C release moments. This is an order-one memory change. The memory unitary U_E(xi) is continuous in xi for fixed finite unscaled coefficients, and the common prepared C phase cancels when comparing the two memory targets. Together with the uniform analytic weak-ramp error, this rules out silently replacing U_E by identity with an O(xi) error for all sufficiently small positive xi. This argument does not assume that the rapidly T-dependent gate phases have a limit as xi tends to zero. The test does not set a physical runtime T at xi=0.

The one execution exited zero in about 1.55 seconds, with a 30-second limit. The full executable, launcher, source manifest, actual argv, timestamps, launch and execution receipts, and complete stdout/empty stderr are retained in `run_001/`. Source SHA256 is `06a3997e6b9be89e1121da9e305f6f555f5553fe776b5a256d695f576fa4372b`; launcher SHA256 is `0253310d6c5383415cb59061f7fbdef14d8e6d51ca9cd150ee078f09a439794c`. This is floating-point corroboration of exact finite stage identities, not an interval-certified family theorem or a numerical positive-xi slew test. The general proof and analytic derivative estimates above carry those claims. No execution failed and no tuning rerun occurred.

## 7. Qualified conclusion

The construction permits fixed positive ramp and gate durations, a fixed per-site modeled strength cap and fixed per-site modeled slew cap, while retaining all D/C/E/R outputs and charging only the stated weak ramp residuals. It does so with a **different, explicit memory-output contract**. The original preparation theorem's fast-ramp sufficient estimate for its literal memory comparator remains unchanged; this proof does not establish a bounded-slew version of that same contract.

The native supply of complements, fresh purity, phase/timing references, isolation, matching controls, microscopic drive outputs/energy and eventual memory reset remains open. Independent actual derivative control is needed for a physical implementation claim. Old H is never rescaled or subtracted, all scalar reserves are retained, and the old-time ordering includes the entire preparation interval. No canonical file, Git/PR state, audit, cache, graph, lock, axiom or editable prompt was changed. Root should decide acceptance using this corrected scope; no publication approval is implied.

<!-- END UNCHANGED BODY slew_exposed_review -->

<!-- BEGIN UNCHANGED BODY slew_controlling_qualifications -->
# Controlling qualifications for preparation with bounded modeled slew

This is a conditional theorem in the supplied externally controlled finite bus model. The root accepts the new proposal together with the exposed review below; this is neither an independent retained audit verdict nor a native realization.

The proposal is PROPOSED_LEMMAS.md SHA2566e09476675188bc8053e2b3b00095db3eb5e1ebf59c816c923da0675a33edc44. The separate review is REVIEW.md SHA256a1b9ef4621b2a4a420d86f30c16449273d0a0a4bc46f22d078a4b2884cbda1d1. Its22-member freeze is6794345fce3b8f11bb990512de09c1f40893f290d00d8e0032005ed783757525. The accepted driven preparation28bef194 and its qualifications1c94a582, and runtime bus1733b296, remain dependencies at their exact identities.

## Accepted endpoint and error

Write the actual added generator as A=R I+A_C+xi V_p, with A_C=A_0+xi V_s+xi^2 A2 acting only on C. Every reserve scalar is actual installed data. During a ramp the positive complementary controls yield H+f A+C0 u I, f=1-u. The first comparison retains all of A_C and omits only xi f V_p. Since H and A_C act on separate registers, its endpoint factors exactly. A matching SWAP transfers the entire evolved C input to retained E, including arbitrary D/C/reference correlations. On the final ramp retain A_0 and bound the full omitted xi(V_p+V_s)+xi^2 A2 in operator norm. No code projection of A2 is substituted.

For symmetric ramps, alpha_on=r_on/2 and alpha_off=r_off/2. The ideal release isometry is
exp(-i Phi) Omega_phi tensor [(exp(-i tau H) tensor U_E tensor I_R)Q],
where U_E is the relabelled exp(-i alpha_on A_C),
tau=r_on+t_s+t_p+r_off and
Phi=C0[t_s+t_p+(r_on+r_off)/2]+R(r_on+r_off)/2+pi n_S/4.
The full SWAP endpoint has no additional scalar phase. Set each gate phase to phi_l+omega_l alpha_off because the final free source field subtracts omega_l alpha_off. Runtime phi_l retains its original +omega_l T; no +omega_l tau is inserted.

The uniform unhalved trace error is at most
eta_ready+xi r_on||V_p||+r_off(xi v+xi^2 a2)+2 integral||E_p||,
where v>=||V_p+V_s|| and a2>=||A2|| on the entire physical space. The factor two from the isometry bound cancels the half-ramp integrals. Initial fresh independent E readiness and every omitted storage/control coupling remain explicit premises or error costs. Relative coefficient errors require the multiplying operator norm. Small integral error is not a derivative bound.

## Fixed per-site modeled bounds

Use a uniform parent incident bound J_* on the sums of positive block coefficients, hence complementary-block norms, throughout the subsequently reduced xi family. Fix smooth ramp F with maximum derivative m_F and positive unit-integral gate bump chi with maxima m0 and m1 for its value and derivative. Then
r_on,r_off>=m_F J_*/S_*,
t_s>=max(pi m0/g,sqrt(pi m1/S_*)),
t_p>=max(pi m0/(2g),sqrt(pi m1/(2S_*)))
give incident modeled strength at most2J_*+g and incident first-derivative norm sum at most S_*. Ramps and the two gate stages are disjoint. Flat endpoints make the joins smooth.

This is a per-site derivative statement; the global derivative norm can grow with the number of driven sites. Physical implementation strength and derivative caps need independent pointwise slack or certificates. No hard bandwidth, microscopic controller-energy, autonomous scheduling or physical slew claim follows.

Fix N and all finite unscaled data before reducing xi further. The displayed positive smallness bounds make the weak ramp errors as small as requested without shortening these fixed durations. Recompute T=t_*/xi^2, source/gate phases, actual R,C0,U_E,Phi, accuracy and long-time storage/calibration costs after the final xi choice. Optional moment accuracy can be chosen noncircularly using the uniform beta_bar=||H-aI||+(n_C+1)J_* upper bound before selecting xi. It safely overcounts incident positive blocks, each added block meeting C, and the parent already charges reserves. Do not infer a polynomial total duration just from fixed ramp times; composition with the separately accepted resource result needs its own complete cost analysis.

## Changed memory contract and moment scope

U_E is part of the complete output. This theorem does not meet the prior literal-Q memory contract unless U_E is scalar on the supported input, or an actual inverse operation and its costs are separately supplied. All D/E/R correlations must be compared with the evolved-memory ideal state. No known unitary is erased by a convention change.

Ordinary release K and K^2 moments acting on D/C are unchanged from the accepted formulas, evaluated on the tau-aged ideal old marginal. Their means and variance are insensitive to a unitary on E. Reference-valued moment operators retaining E instead acquire conjugation by U_E. The actual release marginal differs from the ideal by at most the preparation trace allowance. Runtime composition uses the passive E reference and gives the direct bound e_p+delta_bus+2e_r, with old flow exp(-isH)W exp[-i(T+tau)H] and U_E explicitly retained. Changing to an actual-release-marginal comparator requires the parent's additional shift allowance.

The reviewer supplied a useful discriminator: an initial bus-vacuum/one-excitation superposition acquires relative memory phase exp(-i alpha_on nu), and literal versus evolved memory trace distance2|sin(alpha_on nu/2)| can be order one while ordinary release moments agree. This persists for sufficiently small positive xi by continuity of U_E at fixed finite unscaled data and the weak-ramp bound. No limit for the rapidly T-dependent gate phase is required.

## Evidence and unresolved suppliers

The root proposed the analytic lemmas before receiving the separate review. The check is source-exposed, same-model and aware of the preparation candidate; it is not blind or a different-family replication. The root read the complete review, executable, launcher, source coverage, actual launch/execution records and full streams; the22 freeze members, six original/captured source identities and actual execution pins are checked by the acceptance recorder.

One separately written floating-point128-dimensional complete-isometry calculation at xi=0 corroborates phase/memory conventions. It reports approximately5.6e-15 correct-comparator error; literal-memory, reversed gate-phase and omitted-reserve alternatives fail by order-one amounts. It is not a positive-xi runtime simulation, numerical ramp integration, interval proof or physical slew measurement. General validity rests on the complete-space Duhamel and stage-factorization argument. Root executes no new scientific program in accepting it.

Native supply of positive complements, fresh purity, matching access, phase and timing references, isolation, long-time memory storage, microscopic control outputs/energy, final halt and reset/reuse remains open. No model override, axiom change, editable prompt change, audit application or scientific merge is authorized by this acceptance.


<!-- END UNCHANGED BODY slew_controlling_qualifications -->
