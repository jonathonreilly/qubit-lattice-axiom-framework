---
claim_id: original_microscopic_local_output_limit_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied compensated finite-spin GKSL law from bare Omega at fixed positive K, delta and kappa, volume-uniform local defect and first-field bounds, original same-state amplitude/gain and finite-history balances, subsequential local trajectory compactness with a Holder 1/5 modulus, true spin-to-rotor original gain-current and finite-register identification, the complete dissipative functional on neutral tests in exact normal-form coordinates, and quantitative full quantum/original-timestamp output comparison to the true W0 rotor target when n=o(S^(1/3)). No arbitrary-volume full quantum limit, energy convergence or physical law selection is asserted."
upstream_dependencies:
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
  - finite_rate_repeated_record_formation_bounded_theorem_note_2026-09-24
  - bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
  - local_pair_form_and_general_graph_magnetic_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/original_microscopic_local_output_2026_09_30.py
---

# Original microscopic outputs and a growing-volume quantum limit

**Type:** bounded_theorem
**Status:** conditional-support; supplied model, unaudited.
**Date:** 2026-09-30

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
target_blocker_text: Volume-uniform local microscopic-to-effective original marked process from bare Omega at fixed physical couplings
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: extend the full quantum comparison beyond the explicit growing-volume window and control unbounded energy
conditional_surface_status: supplied compensated finite-spin law, bare Omega, original instruments and coupled resource scaling
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: uniform local output bounds and an explicit growing-volume full quantum and original-record comparison under supplied hypotheses
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The actual microscopic original-mark process has uniformly tight local quantum outputs on every fixed physical horizon, even while its Hamiltonian and bare jump coefficients diverge. Along subsequences its capped, binned local histories and quantum states converge uniformly in time. Their original post-mark gain currents converge strongly in time-integrated trace norm to the actual rotor source word evaluated in the same limiting joint state. The finite history marginal satisfies the corresponding exact balance. The proof also identifies the complete dissipative functional on bounded neutral tests in an exact local normal form. Its microscopic test is explicitly dressed.

A second regime gives a quantitative full comparison: when the number n of A sites satisfies n=o(S^(1/3)), the entire microscopic quantum state and original finite-volume timestamp instrument approach the true compensated W0 rotor target on each fixed physical horizon. Its error is bounded explicitly below. This restricts how volume grows; it does not replace the arbitrary-volume local statements. The theorem is conditional on the supplied law and preparation. Beyond this window, the fast hole-supported Hamiltonian and its field-weighted holding response remain open. The field weights used in the proofs do not replace the source energy.

## Supplied law, records and order of limits

Let Lambda be an even cubic torus of side L>=64, with bipartition A,B and n=|A|. Larger even periods in each direction are permitted. Each vertex has the **supplied qutrit** basis |0>,|+>,|->, charge q=diag(0,1,-1), occupancy n_x=q_x^2 and hard-core annihilator a_(x,c)=|0><c|. Each oriented nearest-neighbor link has integer spin S>=1, electric operator E=S_z and normalized shifts

    U^[+1]=S_+/sqrt(S(S+1)),  U^[-1]=(U^[+1])*.

These are partial shifts with their true boundary zeros, not inverses. On a link x->y a hop of charge c from x to vacant y uses U^[-c]. The selected physical subspace is

    G_x=div E_x+1_A(x)-q_x=0.

The hopping Hamiltonian is T=-sum_a(F_a+F_a*), where F_a is the unsigned sum of legal outward hops from a in A to its six B neighbors. Hops conserve total record count and Gauss. A resolved original birth on the oriented edge e=(x->y) is

    j_(e,c)=a_(x,c)* a_(y,-c)* U^[c],  c=+1,-1.

Choose separately either both resolved labels (e,c), or the single **unnormalized coherent** edge label e with j_e=j_(e,+)+j_(e,-). Its two signs remain coherent within that mark. These are different instruments even though their total loss operators agree. Births act only on two empty endpoints, add two occupied sites, and preserve Gauss. The source has moving hard-core charges; the theorem does not silently grant additional permanent internal labels to those moving charges. The history register below copies the original jump outcomes.

Put w_a=1-n_a, W=sum_a w_a, Cspin=S(S+1), and

    Q_a=product_(c in A, c!=a, dist(c,a)<=2) n_c,
    D_(a,S)=diag(F_a*F_a),
    D_(a,infinity)=n_a sum_(b~a)(1-n_b),
    C_S=sum_a [F_a*F_a-D_(a,S)+D_(a,infinity)] Q_a.

On a charged outward hop from a along edge e, let k=-q_a if a is its initial endpoint and k=+q_a otherwise. Then the exact diagonal difference is

    D_(a,infinity)-D_(a,S)
      =Cspin^-1 sum_(b~a) n_a(1-n_b) E_e(E_e+k).

The expression includes blocked spin-boundary paths with their zero amplitude. The gate commutes with its bracket. All its terms preserve each A occupancy, count and Gauss. Normalized shifts have norm at most one, ||F_a||<=6 and ||C_a||<=48, uniformly in S. On integer fields E(E+k)>=0. These are the actual compensation and microscopic instrument from the [local compensation source](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md) and [original finite-rate formation source](FINITE_RATE_REPEATED_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md), with the fast coefficient specified here:

    H_(epsilon,S)=delta epsilon^-4 [W+epsilon T+epsilon^2 C_S],
    L_(epsilon,mu)=sqrt(kappa) epsilon^-1 j_(S,mu),
    d rho/dt=-i[H_(epsilon,S),rho]+sum_mu D[L_(epsilon,mu)]rho,
    D[L]rho=L rho L*-(L*L rho+rho L*L)/2.                     (1)

Fix positive K,delta,kappa and use the coupled family

    epsilon^2 S(S+1)=delta/K,  S integer -> infinity.        (2)

The initial state is the **bare** product Omega: every A site plus, every B site empty, every link E=0. It is physical. No dressed preparation, equilibrium ensemble or field-moment hypothesis is supplied. At finite S,L all generators are finite matrices and all marked processes are their exact quantum-jump instruments. The proof retains every later birth, recycling term, loss and coherent mark cross term.

For the volume-uniform local claims1–6, observation data are fixed before this joint limit: horizon T0<infinity, a finite quantum region X of sites/links, a finite monitored A-center pattern F, finitely many deterministic time bins, and total count cap M. The classical word stores original labels, bin tags and their order until a single absorbing overflow symbol. After overflow the system and all physical jumps continue. This is an output coarse-graining, not stopped dynamics. Its exact CP append has Kraus operators |append(mu,z)><z|, one for each old word z; their adjoint products sum to identity, including noninjective overflow. Bins label events; no clock implementation is asserted.

Use the integer E basis to embed finite-spin link spaces into ell2(Z). For any sequence S->infinity and arbitrary growing safe tori, all fixed regions and necessary local supports must eventually embed without aliasing. No fixed-volume limit is taken first. Fixed-torus estimates preceding the local extraction are uniform in S and L. Constants in claims1–6 may depend on fixed geometry/couplings/horizon/circuit order and are independent of volume and spin. Claim7 instead states its explicit powers of the total n and permits the whole original finite-volume output, including timestamps. All constants are constructive bounds, not numerical resource or physical calibration claims.

## The output theorem

Write rho for the actual microscopic ensemble and eta for its exact joint history/system state. Let Gamma_(epsilon,L),X,Z be its marginal on X and one fixed history specification Z. The following claims form one source argument; the five owned proof appendices below supply every new load-bearing derivation.

1. **Defects, physical fields and original count tightness.** There is epsilon0>0 such that

       Tr rho(t)W/n <=C epsilon^2(1+t),
       Tr rho(t)sum_e|E_e|/n
                <=C(t+t^2)+C epsilon^2(1+sqrt(1+t)).       (3)

   Each original center's total microscopic intensity is at most C kappa(1+t), and E N_F([s,t])<=C kappa |F| integral_s^t(1+u)du. In particular overflow probability is at most C_T |F|/(M+1). Local field tails are <=C_T |E_X|/R. These are unconditional bounds in the full original ensemble; they are not conditional hazard estimates.

2. **Original amplitude and gain, in the same state.** Define on the full finite-spin carrier

       Bhat_mu=j_mu F_a,   B_mu=sqrt(kappa) Bhat_mu,
       A_mu=sqrt(kappa) epsilon^-1 j_mu.

   For each original mark at a,

       integral_0^T0 ||(epsilon^-1 j_mu-Bhat_mu)rho(t)^(1/2)||_2^2 dt
                                           <=C epsilon^2(1+T0)^2,
       integral_0^T0 ||A_mu eta(t)A_mu*-B_mu eta(t)B_mu*||_1 dt
                                           <=C epsilon(1+T0)^2. (4)

   The second assertion holds for every positive extension having the same actual system marginal, including the original register and passive reference factors. It survives the actual append CP map and finite direct sums over the original labels. It compares quantum gain currents in the same state, not two independently evolved laws. At Omega, the bare j vanishes but Bhat does not; no pointwise time assertion is being made.

3. **Cumulative means and bounded-history balance.** For each original mark,

       sup_(t<=T0) |E N_mu([0,t])-kappa integral_0^t Tr rho Bhat_mu*Bhat_mu|
                                           <=C epsilon^2(1+T0)^2. (5)

   Deterministic bounded-variation time weights cost |f(T0)|+Var f. For every bounded real function g of the entire fixed capped/binned original word, with b interior bin boundaries,

       sup_(t<=T0) |E g(Z_t)-g(empty)
          -kappa integral_0^t sum_(mu in F)
            Tr eta(s)[Bhat_mu*Bhat_mu tensor (T_(mu,s)g-g)] ds|
          <=C_F ||g|| [epsilon^2(1+T0)^2+epsilon^3(1+b)].    (6)

   T_(mu,s) is the exact append on classical functions. Constants do not grow with cap dimension. The quantum/history correlations are retained on the right. This is not a closed classical Markov law.

4. **Local trajectory compactness and true rotor word passage.** On the common output carrier,

       ||Gamma_(epsilon,L)(t)-Gamma_(epsilon,L)(s)||_1
                       <=C epsilon+C |t-s|^(1/5),            (7)

   and the output family is pointwise totally bounded in trace norm. Hence every joint sequence admits a subsequence converging uniformly on [0,T0], simultaneously on a countable exhaustion of X at a **fixed register specification**. The limit Gamma_X,Z(t) is positive, trace one, classically block diagonal, locally normal, compatible under quantum partial traces, supported on occupied A sites and Holder continuous with exponent 1/5. Local Gauss constraints persist wherever their full stars are included, since their bounded spectral projections are preserved under the limit. No global trace-class density on the infinite tensor product is asserted.

   Let B_(infinity,mu)=sqrt(kappa)j_(infinity,mu)F_(infinity,a) be the original unit-rotor word, with the same label. If X' contains X and its source support, the actual gain current tends along that same subsequence to

       J_mu,X,Z(t)=Tr_(X' outside X)
                  [B_(infinity,mu) Gamma_X',Z(t) B_(infinity,mu)*]

   strongly in L1([0,T0];trace class). The definition is independent of sufficiently large X'. This also holds after the actual append and for finitely many original labels. The limit uses the true common-carrier bound

       (B_(S,mu)-B_(infinity,mu))* (B_(S,mu)-B_(infinity,mu))
                    <=C_mu S^-1(1+sum_(e in source support)|E_e|). (8)

   Set tau=Tr_quantum Gamma and nu_mu(t;z)=Tr[B_(infinity,mu) Gamma_z B_(infinity,mu)*]. The exact limiting register equation is

       tau(t)-tau(0)=integral_0^t sum_(mu in F)(App_(mu,s)-I)nu_mu(s)ds. (9)

   It follows by passing the exact finite-epsilon register equation through the L1 gain limit. The register marginal is Lipschitz, since nu_mu(z)<=||B_(infinity,mu)||^2 tau(z). The local quantum trajectory need not be Lipschitz. Different overflow specifications have only the consistency maps actually supplied by their output definitions; no inverse or nonexistent coarse-graining map is assumed.

5. **Complete dissipative functional on neutral tests, with its exact coordinate boundary.** There is an exact finite-depth local circuit Y of order six, acting trivially on registers, for which sigma=Y eta Y*. For every bounded neutral local/register test O, [W,O]=0, let D'_epsilon* be the full rotated original dissipative part and D_B* the complete dissipative expression with B_mu in the same coordinates and the same append. Then

       sup_(t<=T0) |integral_0^t Tr sigma(s)
                          [D'_epsilon*O-D_B*O] ds|
          <=C_(X,F)||O||[epsilon(1+T0)^2+epsilon^3(1+b)].   (10)

   No W grade is observed. Both losses and all coherent recycling terms are included. On the comparison side only, physical-coordinate return costs O(epsilon^2). Thus the equivalent physical identity has **D_micro*(Y* O Y)** on its microscopic side. Replacing this by D_micro*O is not licensed by ||Y*OY-O||=O(epsilon), because the microscopic dissipator is large. The theorem does not add a fast-Hamiltonian cancellation to (10).

6. **Actual linear post-event field gain.** For a fixed finite link set E_Z in the post-event output put Q_Z=1+sum_(e in E_Z)|E_e|. The actual original gain G_A=A_mu eta A_mu* obeys

       integral Tr[Q_Z G_A] <=C_(Z,mu,T0),
       integral ||Q_Z^(1/2)(G_A-G_B)Q_Z^(1/2)||_1
                                      <=C_(Z,mu,T0) sqrt(epsilon), (11)

   where G_B=B_mu eta B_mu*. The proof pays the exact finite-spin output price 1+|E_Z|S against the squared error in (4). Original append commutes with this physical weight; arbitrary field-changing postprocessing is outside (11). In particular the original event gain mass outside |E_Z|<=R is O(1/R) and its projected trace-norm tail is O(1/sqrt(R)). A bounded first weighted moment alone does not imply uniform integrability of that weighted moment itself.

7. **Full quantum and original-record limit in an explicit growing-volume window.** Let P=1_(W=0), A1=Pi1 T P, M1=A1* A1 and Z1=Pi2 T Pi1 A1. The true canonical finite-spin target has jumps sqrt(kappa)B_(mu,S), B_(mu,S)=-P j_mu Pi1 T P, and Hamiltonian

       h_eff,S=K D+delta H4,S,
       H4,S=M1^2-{M1,P C_S P}/2
                 +A1* (Pi1 C_S Pi1) A1-Z1*Z1/2.          (12)

   D is the exact diagonal sum in the compensation identity. Its rotor target retains these original marks and has

       h_eff,infinity=K D-2delta sum_(unordered dist(a,c)=2)
                                    (F_c F_a P)*(F_c F_a P).

   For finite T0 there are c0,C_T0 independent of n,S and register size such that, if epsilon n^2<=c0, the actual microscopic output from bare Omega and this rotor target obey

       sup_(t<=T0) ||Output_micro,S(t)-Output_eff,infinity(t)||_1
         <=C_T0[epsilon n^3+epsilon^2 n^6+n^6/(S(S+1))].  (13)

   Output means the complete original finite-volume marked timestamp instrument jointly with final quantum density, using its integrated trace norm on the actual time simplexes. Both resolved and unnormalized coherent alternatives retain all their original cross terms. It includes the global final state and every finite original register by forgetting outputs. There are at most floor(n/2) original marks by Ntot conservation between jumps and Ntot+2 per mark; no artificial occupation or record cap is imposed. The proof treats arbitrary finite bins with constants independent of their number, then refines them. It does not compare normalized outputs conditioned on arbitrarily rare histories.

   Under (2), n=o(S^(1/3)) makes (13) vanish. For example safe even L(S)=2 floor(S^(1/12)/2) gives n=O(S^(1/4)) and error O_T0(S^-1/4). This is an explicit joint scaling, not an unspecified diagonal subsequence. The result identifies the full target in this window while leaving arbitrary-volume local quantum-law identification and unbounded-energy convergence open.

## Proof architecture and complete owned derivations

Claims1–6 use finite-volume microscopic estimates followed by local compactness. Claim7 uses a direct quantitative finite-volume comparison. Neither argument assumes an infinite-volume microscopic generator or a fast dissipative gap. The following are current scientific supporting proofs owned by this note and declared primary inputs. They are not independent premise notes or historical exemptions.

- [Local normal form, defects and first field moments](proofs/original_microscopic_output_2026_09_30/normal_form_and_moments.md): finite-color local homological recursion, complete original defect drift with two coherence corrections, bare preparation, physical translation localization and field-displacement bounds. The exact negative-grade budget is derived, not assumed.
- [Original amplitude, gain and bounded-history balances](proofs/original_microscopic_output_2026_09_30/original_gain_and_history.md): the full first derivative including grade -2, translation-covariant physical truncation before volume division, coherent source algebra, gain factorization and correlated copies of the monitored pattern for arbitrary history tests.
- [Local trajectory compactness and the original rotor gain limit](proofs/original_microscopic_output_2026_09_30/local_trajectory_and_rotor_limit.md): the enlarged electric halo, two-sided hole support, complete registered jumps, all-spin cutoff compression, Holder optimization, common-carrier word bound and trace-class limit of the exact register equation.
- [Neutral dissipative functional and linear event-field gain](proofs/original_microscopic_output_2026_09_30/neutral_dissipator_and_linear_field_gain.md): the neutral test domain for negative-grade losses, full original cross corrections, dressed physical test, and weighted event gain.
- [Quantitative growing-volume quantum and original-record comparison](proofs/original_microscopic_output_2026_09_30/growing_volume_quantum_and_record_limit.md): the canonical ground-band rotation, exact Sylvester correction of the full off-diagonal loss, polynomial total-field displacement moment, complete spin-boundary comparison, and register-independent timestamp refinement.

Here is the dependency order. The finite-order circuit and exact grade inverse give the defect estimate. Defects plus bounded field-displacement commutators give (3). The integrated negative-grade budget, returned through a translation-covariant physical first-order truncation, gives (4); its full first derivative has a hole-supported remainder. The same complete cross corrections and physical translation symmetry give (5)-(6). Defects and first fields give (7) by electric cutoff. Equations (4), (7), (8) identify the limiting gains and (9). Equations (4) and the local rotated rare-hole bound control the complete neutral losses in (10). Equations (3)-(4) plus the exact spin-box price give (11). None of these dependencies assumes the conclusion of the full microscopic-to-effective quantum limit. Claim7 has a separate quantitative proof from the landed canonical coefficients and local rotor pair form. It uses the small total perturbation epsilon n, exact Hamiltonian band separation and a target-state displacement moment; it does not assume an all-state fast absorption gap or a local microscopic energy estimate.

All uses of locality concern full gain/loss maps or exact finite circuit cones. Electric conjugation on the unbounded rotor algebra is not assumed norm continuous. The arbitrary-volume local compactness proof uses bounded local words and first-moment quadratic-form inequalities. The growing-volume comparison separately proves a fourth total-field displacement moment for its rotor target. No external Lieb-Robinson theorem for an unbounded law is invoked. The finite circuit method has a landed antecedent in the `UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md`; its recursion is restated and proved in the owned normal-form appendix, including the supplied compensation.

## Imports, antecedents and precise remaining obligation

The full one-site framework algebra is M2(C). The qutrit matter, spin-link tensor carrier, staggering, charge/Gauss sector, Born/GKSL dynamics and original marks, time parameter, positive couplings, compensation, bare Omega and scaling (2) are separately supplied mathematical inputs here. This note neither derives them from the four axioms nor adopts them as approved primitives. The registry's scale-reference, kinetic-isotropy and realized-state primitives do not supply this dynamics, probability instrument or preparation. No empirical value is fitted or calibrated.

The landed local compensation note proves a fixed-graph microscopic approximation followed by a spin/rotor limit and explicitly leaves its growing-volume limit separate. The landed uniform local ring note supplies a volume-uniform statement under a dressed preparation and a birth rate decreasing with epsilon; its final scope leaves bare preparation and fixed-rate dynamics open. Their exact arguments were read. Claims1–6 handle bare Omega and the actual epsilon^-1 original jump amplitudes on common physical times with arbitrary safe volume growth. Claim7 quantitatively extends the [canonical fixed-graph elimination](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md), retaining its exact ground-band convention. The [landed local pair form](LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md) gives the extensive rotor interaction used to derive its polynomial total-field moment. The explicit powers in (13), rather than an implicit graph constant, justify that restricted joint limit.

Open original-record thermodynamic and autonomous-supplier proposals concern effective laws or engineered apparatus. They are relevant prior scope, not premises of this microscopic argument. Every new proof needed here is present in this unit. Prior focused campaign checks are recorded solely as recovery provenance; they are not the formal source review of this composed unit.

Outside the explicit volume window, a complete local quantum-law theorem would additionally identify the fast hole-supported Hamiltonian/holding contribution, combine it with the actual coherent loss in physical coordinates, and prove uniqueness of the resulting compatible local evolution. The present first-field bound allows second moments growing with S and supplies no uniform electric-energy integrability, quadratic hole-weighted source bound, or passive feedback estimate. Claim7 gives complete finite-volume uncapped original histories and integrated timestamp/quantum convergence only in its stated window. Arbitrary-volume local full-history identification, spatial boundary independence, a permanent autonomous register, native carrier realization, physical source/clock selection and a TOE conclusion are not supplied. These are explicit unproved consumers, not negative theorems excluding other mechanisms.

## Evidence and reproducibility

Primary runner: `scripts/original_microscopic_local_output_2026_09_30.py`. It checks bounded exact source-word, spin-boundary, register and cutoff controls, with expected values derived separately in the milestone packet. Its output is `outputs/original_microscopic_local_output_2026_09_30.json`; its actual execution cache is `logs/runner-cache/original_microscopic_local_output_2026_09_30.txt`. Neither a finite control nor a historical focused check proves the analytic quantifiers above. Current execution and mutation results are recorded only after they are actually run.

The owned packet is `.claude/science/physics-loops/original-microscopic-output-20260930/`. It binds actual source/input identities, method/axiom scope, the original immutable derivations and controls, all failed or corrected evidence, full source disposition, and the eventual independent review. Historical bytes have exact recovery mappings; stale fixture claims are not reclassified as current proof. Source review and combined integration validation are separate handoff requirements.
