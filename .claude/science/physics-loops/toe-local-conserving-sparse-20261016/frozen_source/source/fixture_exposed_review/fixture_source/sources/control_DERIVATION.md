# A conditional local, conserving endpoint with positive bounded controls

**Proposed source theorem; not independently reviewed or accepted.** On the explicitly strengthened geometry and gate permissions below, a finite coherent reservoir and supplied positive nearest-neighbor controls implement an arbitrary unitary on the old qubits at a declared laboratory endpoint, uniformly on arbitrary old/reference inputs and retaining every reservoir and ancillary output. The old Hamiltonian remains literally installed. The common added incident-strength bound and the slew bound do not grow with accuracy. The number of sites, duration, energy and precision requests do grow and are accounted for below.

The finite spectral lift is existing mathematics, already present in the repository; it is not this note's discovery. The new interface proposed here is its local driven implementation for **identical qubit energy gaps**, with an explicit noncircular endpoint phase correction. The result requires full SWAP access in addition to XY and onsite phase controls. An ancillary path attached to only one old site does not by itself give the required access to all old qubits. No native preparation, microscopic model of the external driver, autonomous timing, permanent halt or indefinite repeatability is asserted.

## 1. Sources and exact domain

The pinned predecessor is `finite_energy_reservoir_candidate/DERIVATION.md`, SHA256 `ee90d960f0db9f30c861d837c53e306a50a855c7af251a748e655749a8a9a195`; its relevant finite-block, full-output, energy and phase arguments were refreshed. It explicitly identifies the earlier canonical finite-energy-supply note as the source of the lift. Its unresolved local implementation interface is the present target.

The imported circuit-existence theorem is Bai–Marvian, [*Synthesis of energy-conserving quantum circuits with XY interaction*, arXiv:2309.11051v3](https://arxiv.org/pdf/2309.11051v3), Theorem 1 and equation (2). In the form used here, XY exchange and continuous local Z rotations, with one initially zero ancilla, realize conserving unitaries up to a global phase and return that ancilla. The theorem initially allows arbitrary pairs. The paper's pages 3–4 explicitly distinguish a strict nearest-neighbor path with XY+Z alone from access to full SWAP; Corollary 3 includes SWAP. This distinction is a hypothesis here, not an inferred implementation of SWAP by path XY+Z. Its circuit count is not used as a numerical certificate. The imported theorem and the following wrapper remain separately identifiable.

The scoped Markdown search under `W/docs`, excluding audit and work-history directories, found no occurrence of the paper identifier, author pair or title pattern. It does not prove repository-wide absence. A corrected receipt preserves an initially overescaped numeric search alternative. The known spectral-lift duplication is acknowledged irrespective of that search.

Fix q>=1 old qubits S, with supplied, physically identified energy operator

    K = E0 I + Delta N_S,     N_S=sum_(j=1)^q n_j,
    n=|1><1|=(I-Z)/2,        E0>=0, Delta>0.                  (1)

Keep Planck's constant hbar explicit; Schrödinger evolution is exp(-itH/hbar). No old term in (1) is deleted, multiplied by an accuracy-dependent coefficient, or assigned a different energy zero. Let V be any supplied unitary on S, with its scalar phase included. R is an arbitrary passive reference, possibly entangled with all of S.

The additional supplied physical conditions are:

* A finite simple nearest-neighbor path containing every old qubit, M new reservoir qubits and one new synthesis ancilla. Each path edge permits the positive generators in section 4; each site permits its onsite generators. More generally a supplied connected finite routing graph works with its actual routing lengths, but no graph-independent constant is asserted. Occupied-site permission for these new interactions, including old-old edges if used, is explicit.
* All new qubits have the installed onsite energy Delta n, with the same physical gap as (1). The reservoir's prepared coherent state and the ancilla's zero state are supplied at laboratory time zero and independent of S/R. Their preparation and phase-reference costs are not derived here.
* Calibrated, externally timed, nonnegative pulses of the explicitly listed generators are available. Full SWAP exchange is included as a separate interaction permission. The actuator, clock and their output states are external to the finite quantum model proved below.

These are conditional control permissions, not new framework axioms. The proof neither infers them from generic controllability nor substitutes a branched XY/free-fermion model.

Throughout, positive means positive semidefinite. No strictly positive identity floor is assumed and then omitted from the accounting.

## 2. Identical-gap reservoir and the complete finite unitary

Choose an integer L>=1 and set

    M=L+2q,       n_sys=q+M,       m=q+M+1.                  (2)

Use the unary reservoir code

    |r>_B = |1>^r |0>^(M-r),       0<=r<=M,
    H_B=Delta sum_(j=1)^M n_j.                             (3)

Its code energy is exactly Delta r; its full physical Hilbert space is retained. For each k=0,...,q let P_k project onto the old Hamming-weight-k subspace. For an integer a with q<=a<=M, the subspace

    F_a = direct_sum_(k=0)^q [P_k S tensor |a-k>_B]

is a complete copy of S. Its actual total energy is E0+Delta a. Identify it with S and let U_L(V) act as V on it. On all other unary-code energy subspaces and the whole orthogonal complement of the unary code, set U_L(V)=I. Thus U_L(V) is a unitary on all n_sys physical qubits, and

    [U_L(V), K+H_B]=0.                                     (4)

No cyclic shift, discarded boundary or unspecified noncode output is used. Repeated total energies outside these chosen subspaces are harmless: the chosen blocks refine energy eigenspaces. All relevant weights and degeneracies here are known integers; no exact-real spectral equality oracle is invoked.

Supply the normalized coherent vector

    beta_L = sqrt(2/(L+1)) sum_(r=q)^(q+L-1)
                  sin(pi(r-q+1)/(L+1)) |r>_B.              (5)

For every old input weight k, the occupied total labels r+k lie in [q,L+2q-1], contained in the complete interval [q,M]. Hence the actual action on every prepared input is

    U_L(V)(psi tensor beta_L)
       = sum_(l,k) P_l V P_k psi tensor T^(k-l) beta_L,     (6)

where the bilateral shift T is only a proof device. All actual final ladder values in (6) lie in [0,M]. The new synthesis ancilla A starts in |0>, with H_A=Delta n_A.

## 3. Uniform full-output approximation

For the zero-extended sine packet,

    d_L=||(T-I)beta_L||=2 sin(pi/[2(L+1)]).

The path eigenvector identity gives <beta_L,T beta_L>=cos(pi/(L+1)); translating the support does not change it. Telescoping shifts gives ||(T^k-I)beta_L||<=k d_L. With the bilateral controlled shift C_+=sum_k P_k tensor T^k, orthogonality of the P_k gives, even with an arbitrary reference,

    ||(C_+-I)(psi_SR tensor beta_L)|| <= q d_L.

Equation (6) equals C_+^*(V tensor I)C_+ on the prepared subspace. Inserting V tensor beta_L between its two factors proves the isometry bound

    ||U_L(V)J_beta - J_beta V|| <= 2q d_L.                (7)

Here J_beta adjoins beta_L; the notation respects the chosen ordering of tensor factors. Purification gives the **unhalved** joint trace bound on S/B/R

    error <= 4q d_L <= 4pi q/(L+1).                        (8)

The comparator returns beta_L in product form. The actual reservoir generally changes and remains correlated with S/R; no subsystem is traced out in (8). Exact return is not claimed. The bound is uniform in V, the old state and the dimension of R. For fixed q, M=O(epsilon^-1) suffices for this part of the error, independently of compilation cost.

## 4. Circuit certificate and positive local gate realizations

Apply the imported conserving circuit theorem to U_L(V) on n_sys qubits. For precise finite accounting use a circuit C and a unit scalar zeta satisfying

    || C J_A - zeta J_A U_L(V) || <= eta_C,                (9)

where J_A appends |0>_A. The exact existence theorem permits eta_C=0. The gate list specifies every pair, every onsite angle and zeta; a finite-precision certificate may instead establish strict (9). A matrix residual certificate on the full input isometry, rather than a reduced channel or selected test states, is the controlling requirement.

Take the arbitrary-pair elementary list from the theorem to consist of sqrt(iSWAP)=exp(i pi R_xy/4), R_xy=(XX+YY)/2, and exp(i phi Z), with -pi<phi<=pi. Route each two-qubit gate by adjacent **full** SWAPs: move one logical qubit next to the other, apply the gate, and undo the movement. On a path of m sites, one such gate uses at most 2(m-2)+1 physical gates. Onsite gates require no routing. Undoing each route restores all physical wire assignments, including unknown inputs and the coherent reservoir; this is an exact permutation identity on the full Hilbert space.

Let the resulting adjacent/onsite list have G gates. Record its actual gate list and count before using the duration below. If the original list has G_1 onsite and G_2 pair gates, the safe explicit bound is

    G <= G_1 + (2m-3)G_2.                                 (10)

For an elementary desired gate g, the following dimensionless positive Q implements it, with the stated scalar:

| Desired gate | Positive integrated generator Q | exp(-iQ) |
|---|---|---|
| sqrt(iSWAP) | (pi/4)(I-R_xy) | exp(-i pi/4) sqrt(iSWAP) |
| exp(i phi Z) | abs(phi) I-phi Z | exp(-i abs(phi)) exp(i phi Z) |
| full SWAP S_w | (pi/2)(I-S_w) | S_w |

R_xy has eigenvalues -1,0,0,1. S_w has eigenvalues +/-1. Thus these Q are positive semidefinite and have norms at most pi/2, 2pi and pi respectively. Every identity reserve in this table is a real installed pulse term and is included in its norm. In particular

    I-S_w = (I-XX-YY-ZZ)/2

is an allowed positive singlet projector times two; its ZZ component is an additional interaction beyond path XY+Z. This is the precise gate-permission enlargement. Positivity does not make it a consequence of the weaker permission.

Let Phi be pi/4 times the number of sqrt(iSWAP) gates plus sum|phi| over the onsite rotations, counted in the routed list. Full SWAP contributes no endpoint scalar in this convention: its reserve gives exp(-i pi/2), while exp(i pi S_w/2)=i S_w, so the two scalar factors cancel exactly. Its reserve energy and work still count. The product of these positive gate propagators is exactly exp(-i Phi) C.

### Effective certificate selection versus finite-real existence

No numerical G, zeta or control-angle certificate has been produced for an unspecified input V. For supplied computable V and Delta, a terminating but potentially enormous prescription is available from the imported universality theorem: enumerate finite words with rational onsite angles, the exact sqrt(iSWAP) gate, and a rational-angle candidate scalar. Dovetail finite-precision interval evaluations of the full residual in (9), accepting only a certified upper bound strictly below eta_C>0. Rational angles are dense; a finite exact word from the theorem and its global phase can be approximated with a margin. Consequently some word certifies. A Frobenius bound on the isometry residual suffices; there is no need to decide whether any entry is exactly zero. Route the returned word and retain its actual finite certificate.

This proves effective termination under computable input oracles and the imported theorem. The later effective pulse/scalar prescription also requires computable timing, energy and unit constants with certified enclosures; it is not an exact-real oracle supplied by the circuit theorem. It supplies neither an efficient synthesis algorithm nor an oracle-walltime bound. For arbitrary supplied noncomputable V the statement is finite-real existence only. The paper's asymptotic gate bound and its sparse-support refinement are not converted here into numerical counts or a polynomial-in-accuracy runtime claim.

## 5. Fixed strength and slew, with a noncircular laboratory endpoint

Fix desired positive constants g (energy units) and sigma (energy/time units), independent of epsilon. Set Q_*=6pi. Choose one supplied duration h satisfying

    h >= max(4 hbar Q_*/g, sqrt(4pi hbar Q_*/sigma)).       (11)

For a slot of length h use

    f_h(t)=(1-cos(2pi t/h))/h,       0<=t<=h,
    H_control(t)=hbar f_h(t) Q.                            (12)

Outside its slot the pulse is zero. Its area is one, its maximum is 2/h and its derivative maximum is 2pi/h^2. Both pulse and derivative vanish at either endpoint. Hence every local pulse has norm at most g/2 and derivative norm at most sigma/2. The reserves in Q count in these bounds.

Execute the routed gates serially in G such slots. Reserve **one more slot** for simultaneous onsite number phases on all m qubits. Fix

    tau=(G+1)h,          x=Delta tau/hbar.                  (13)

Now, and only now, choose a rational r satisfying |r-x/(2pi)|<=1/4, set k=floor(r)+2 and set

    lambda=2pi k-x.                                       (14)

The floor is of a rational, hence decidable; no exact-real rounding oracle is used. The inequalities give 3pi/2<lambda<=9pi/2<Q_*. During the final slot apply Q=lambda n at each site. These simultaneous onsite pulses satisfy the same **per-site** strength/slew bounds. Their global norm, which is not their incident norm, grows with m. Since the duration of that slot was fixed before lambda was selected, (13)–(14) are not a target/duration fixed-point equation. Approximate evaluation of lambda is priced in section 7.

The full installed free Hamiltonian is

    F=K+H_B+H_A=E0 I+Delta N_tot.                          (15)

All table generators and all final generators commute with F. F remains present throughout every ramp, slot and routing SWAP. Thus the complete laboratory propagator is exactly

    U_lab(tau)
       = exp[-i E0 tau/hbar] exp[-i(x+lambda)N_tot]
                          exp(-i Phi) C
       = exp[-i(E0 tau/hbar+Phi)] C.                       (16)

The integer spectrum of N_tot, not an energy rescaling or a discarded drift interval, proves the last equality. The positive final pulses add forward number phase until an integer multiple of 2pi is reached. They do not remove K from the generator. If lambda n is expanded as (lambda/2)(I-Z), its identity and Z phases are both already included in exp(-i lambda N_tot); neither is discarded separately. The old scalar E0 tau/hbar is retained. Define

    gamma=exp[-i(E0 tau/hbar+Phi)] zeta.                    (17)

For every pure old/reference input the vector comparator is

    gamma (V tensor I_R)|psi_SR> tensor beta_L tensor |0>_A,

and its vector error is at most 2q d_L+eta_C. Mixed-input joint trace error is at most 4q d_L+2eta_C. The scalar in V is already part of V; (17) is the additional implementation scalar, not permission to erase the target's phase.

The ideal **added** incident local norm is bounded by Delta+g/2 at any site: the new fixed field is at most Delta, and at most one serial interaction or one final onsite pulse is active there. Old sites retain their original Delta n as old terms; counting Delta there again only enlarges this safe bound. The literal E0 identity is old, not an unpriced new reserve. The ideal added incident slew is at most sigma/2. With independently certified local calibration headroom, section 7 gives Delta+2g and sigma as safe common bounds. Parallel final pulses are counted per site and globally; no unbounded port load is split into fictitious channels.

This is an externally scheduled endpoint. If every control is off after tau, then at tau+s the comparator becomes

    gamma [(exp(-isK/hbar)V) tensor I_R] psi_SR
               tensor exp(-isH_B/hbar)beta_L tensor |0>_A. (18)

The same ideal error bound holds for any specified s, since the subsequent actual evolution is exactly free. The old extra phase exp(-isE0/hbar) is inside (18). This does not keep the reservoir stationary or establish a halt or a fresh ready state for another gate.

## 6. Energy, scalar reserves and external work accounting

The retained quantum model is S+B+A+R. The externally prescribed actuator is not a modeled extra reservoir. For every time-dependent ideal pulse schedule above, [H_lab(t),F]=0. Therefore the **entire distribution of F**, including all moments, is conserved exactly at all times, not only at tau. The Hamiltonian H_lab(t)=F+H_control(t) is positive semidefinite because E0>=0, Delta>0 and every pulse is positive.

Initially A has zero energy and

    mu_B=Delta [q+(L-1)/2],
    Var(H_B)=Delta^2 (2/(L+1)) sum_(a=1)^L
                (a-(L+1)/2)^2 sin^2(pi a/(L+1))
              <=Delta^2 (L-1)^2/4,
    0<=H_B<=M Delta I,     <H_B^2>=mu_B^2+Var(H_B).        (19)

The initial total mean is Tr(K rho_S)+mu_B and its variance is Var_(rho_S)(K)+Var(H_B). All final covariances are retained. Conservation gives the exact mean balance

    change <H_B+H_A> = -change <K>.                       (20)

In the exact compilation A returns to zero. With approximate compilation its energy remains part of (20). For joint trace error e relative to the comparator, the difference between the actual old energy transfer and that of V is at most (q Delta/2)e. The product comparator's unchanged battery mean cannot justify discarding the actual finite energy transfer: the reservoir's range M Delta grows with accuracy.

If moment accuracy is separately required, for any actual observable O its expectation error is at most ||O-cI|| e; for O=(H_B+H_A)^p the safe centered range bound is ((M+1)Delta)^p e/2. This may fail to vanish with the state-error schedule and must be budgeted separately. Conservation of F moments is exact and does not imply independent conservation of reservoir moments.

There is also an explicit classical work functional for this supplied drive:

    W_drive = integral Tr[rho(t) dH_lab(t)/dt] dt.

Within one serial slot the expectation of Q is constant because the only nonconstant term is proportional to Q and [F,Q]=0. The same statement holds for the sum of commuting final onsite Q's. Since every pulse begins and ends at zero,

    W_drive=0,
    integral |Tr[rho(t) dH_lab(t)/dt]| dt
       <=(4 hbar/h)[sum_(j=1)^G ||Q_j|| + m lambda]
       <= g(G+m).                                        (21)

For the last inequality use the headroom choice (11), so 4 hbar Q_*/h<=g. Each slot has positive work during its rising half and compensating negative work during its falling half; the peak temporarily stored control energy is at most g/2 for a serial slot and m g/2 for the final parallel slot. Identity reserves contribute to this real work and its scalar phase. The global peak installed energy is bounded by E0+m Delta+m g/2, while the local incident cap remains fixed.

Equation (21) prices the state-dependent work functional of the externally prescribed Hamiltonian. It does **not** construct a finite microscopic clock/actuator returning its own state, bound its work fluctuations or preparation energy, or identify a source of phase coherence. A closed conservative dilation of the driver itself is a further problem; it is not solved by zero net value of this work functional.

For a calibrated schedule with the same active supports, all pulses zero at the endpoints and actual incident slew <=sigma, the coarser robust absolute-work bound is sigma h(G+m). If the same physical F is installed, its net work differs from zero by at most m Delta eta_H, using the centered range of F and the Duhamel estimate below. If every actual perturbation commutes with F, that net work is exactly zero. These statements do not cover a different physical energy observable silently substituted for F.

## 7. Physical calibration, phase readiness and an error allocation

Let an actual preparation satisfy

    ||rho_initial - rho_SR tensor beta_L beta_L^* tensor |0><0|_A||_1
          <=epsilon_p,                                   (22)

uniformly in the supplied unknown rho_SR. This includes all initial unwanted correlations and phase errors. Let an actual calibrated Hamiltonian on the same time interval satisfy

    eta_H=(1/hbar) integral_0^tau ||H_actual(t)-H_lab(t)||dt. (23)

The Duhamel bound gives operator error <=eta_H and joint trace error <=2eta_H. It does not require a known old state. It also does not by itself guarantee positivity, locality, strength or slew: actual admissibility must be certified separately by the supplied control families and local bounds. For example, parameterized positive pulses with added incident norm errors <=g/2, incident derivative errors <=sigma/2, and new static field errors <=g give the safe common cap Delta+2g and slew sigma. A safe corresponding global installed norm is E0+m Delta+2mg. The old K itself remains literal; (23) must not redefine the target K to absorb an old drift change.

For concrete numerical requests, suppose the actual pulse in slot j is hbar (1+a_j) f_h(t) Q_tilde_j with the same prescribed shape and support, generator norm error delta_j and actual generator norm <=Q_*. Suppose the final onsite angle error on each site is at most delta_lambda, its common shape is multiplied by 1+a_f, and the additional static Hamiltonian error is <=b. Then a sufficient integrated error bound is

    eta_H <= tau b/hbar
             + sum_(j=1)^G (delta_j+Q_* |a_j|)
             + m(delta_lambda+Q_* |a_f|),                 (24)

with an additional integrated term if shapes, overlaps or edge orientations differ beyond this description. Uniform requests

    b <= hbar eta_H_budget/(3 tau),
    delta_j,delta_lambda <= eta_H_budget/[3(G+m)],
    |a_j|,|a_f| <= eta_H_budget/[3Q_*(G+m)]                (25)

spend at most eta_H_budget in (24). Exact conservation holds for the ideal matched-energy model. It also holds for actual perturbations commuting with the same physically identified F. Arbitrary noncommuting errors satisfy the state bound, not an exact conservation claim. A physical mismatch of reservoir gaps must not be called exact conservation of its different measured free energy.

The final lambda can be requested to the absolute accuracy in (25). From lambda=2pi k-Delta tau/hbar, evaluation requests for Delta and tau must account for tau delta_Delta/hbar, Delta delta_tau/hbar and their cross term. The integer k is fixed from the coarse certified rational in (14); refining the final angle does not require selecting a discontinuous principal argument. The large value of k requires enough precision in pi to control 2k delta_pi as well. Computable pi has effective evaluation; arbitrary supplied physical coefficient-oracle walltime is not bounded here.

If the reported endpoint has an additional timing error t_e after all pulses are off, take

    eta_t <= (E0+m Delta)|t_e|/hbar.                       (26)

This conservative vector bound includes the old scalar. A tighter density-only bound may remove E0, but no such removal is used in the displayed budget. Timing jitter during pulses belongs in (23), not solely in (26).

For phase readiness, an aged reservoir beta_theta=exp(-i theta N_B)beta_L changes the target of the lift to

    V_theta=exp(-i theta N_S) V exp(+i theta N_S).           (27)

Thus a phase reference error is physically relevant. A known age t has theta=Delta t/hbar; it can be incorporated before circuit selection by compiling exp(+i theta N_S) V exp(-i theta N_S). If the comparator retains the actual beta_theta, the additional target trace error is at most 2q|theta|. If the comparator requires beta_L itself, apply (22) instead: its readiness trace error is at most 2 sigma_N |theta|<= (L-1)|theta|, where sigma_N is the square root of the finite variance in (19) divided by Delta. These are alternative comparison conventions, not errors to double count. Preparing the sine amplitudes, their phases and the initial product with S/R remains supplied.

Combining all errors, for arbitrary rho_SR and retaining S/B/A/R,

    trace error <= 4pi q/(L+1)+epsilon_p
                         +2eta_C+2eta_H+2eta_t.            (28)

For 0<epsilon<=1, one sufficient solved allocation is

    L >= max(1,ceil(20pi q/epsilon)-1),
    epsilon_p<=epsilon/5,
    eta_C, eta_H, eta_t <= epsilon/10.                    (29)

Choose L, construct the finite lift, select/certify the circuit, route and count G, choose h once from fixed g/sigma, set tau, choose k/lambda, then request coefficients and timing to (25)–(26). This is the complete order of choice; no target depending on an unknown duration is passed back into the compilation. The scalar gamma in (17) is retained as a unit complex number. Any desired tolerance for reporting that scalar adds the corresponding bound on E0 tau/hbar, Phi and zeta; a global phase error affects the vector comparator even though it cancels from (28).

## 8. Resource and limitation ledger

| Resource or promise | Explicit price or qualification |
|---|---|
| New qubits | M+1=L+2q+1, including one synthesis ancilla |
| Reservoir code dimension | M+1; full physical reservoir dimension 2^M retained |
| Total modeled qubits | m=L+3q+1 |
| Coherent initial energy/moments | Equation (19), not a free readiness supplier |
| Added incident strength/slew | Ideal Delta+g/2, sigma/2; stated calibrated headroom Delta+2g, sigma |
| Global nominal installed and pulse energy | E0+m Delta+m g/2; real reserves retained |
| Actual laboratory duration | tau=(G+1)h for the returned routed gate certificate |
| Routing | Equation (10), with full SWAP as an additional interaction |
| Integrated calibration | Equations (24)–(25); precision requests depend on actual G and tau |
| Complete output and target phase | Equations (17), (18), (28); no partial trace used |
| Drive work functional | Net zero in ideal model, absolute work bounded by (21) |
| Microscopic driver, clock and preparation | Supplied/open physical interfaces; no native closure |
| Effective synthesis | Terminating certificate search for computable input, no efficient walltime or polynomial accuracy-cost claim |

Only the new sites and reservoir energy are explicitly polynomial in 1/epsilon here. No inference from dimension to runtime is made. The paper has more structured synthesis results; extracting and checking a concrete sparse-code compiler with a certified count is a useful next task, not a result silently imported into this ledger.

If the only permitted controlled edges form an ancillary path touching old qubit 1 while old qubit 2 has no controlled edge or transverse onsite control, the Hamiltonian factors across qubit 2, with a diagonal one-qubit factor there. For q=2 its n_2 expectation is constant. V=I_1 tensor X_2 on an initial |0>_2 instead requires a |1>_2 output, giving trace distance 2 on that qubit. This is an exact witness that the weaker access description does not imply the present geometry. It does not rule out enlarging access, adding old interactions, or a different architecture.

## 9. Failed shortcuts and narrow negative-claim discipline

The following are scope tests within a positive conditional construction, not a general no-go submission. The no-go-discipline skill was applied to prevent the geometry and gate caveats from becoming broader impossibility claims. No five-family negative packet, negative audit status or publication is requested.

* **N1, actual routes:** strict-path XY+Z alone was screened against the paper's explicit qualification; full positive SWAP is the successful enlarged route here. A coherent-reservoir endpoint without local synthesis is the known predecessor, insufficient by itself for the requested implementation. Adding an unpriced negative free drift was rejected in favor of the paid phase layer. An ancilla with access to every chain site is an alternative permission in the primary source, not investigated here. These are the actual routes; no five failed families are invented and no negative-packet PASS is claimed.
* **N2, dependence:** no independent-wall count is asserted. Connectivity and full-SWAP access enter the single routing permission. Coherent readiness and calibrated timing enter the supplied driven model; their mutual derivability is not established.
* **N3, hidden conditions:** exact equal gaps, physical identification of energy, control access at every path site, the full SWAP generator, the one clean ancilla, coherent initial product, pulse calibration, imported circuit theorem and optional computable-input oracles are all explicit. None follows from a generic Lie certificate.
* **N4, matching:** the paper's caveat concerns XY+Z with the ancilla confined to the same strict path. The two-old-qubit witness concerns an actually disconnected control site. Neither is applied to the successful full-SWAP connected-path permission.
* **N5, resolution:** the old-site witness is a factorization calculation for that stated geometry. Gate positivity, commutation and local cap calculations apply per generator and per site; the full-output estimate applies to the entire finite S/B/A/R model. There is no assertion about all spatial architectures or a fundamental energy-conservation obstruction.
* **N6, partial closure:** the positive exchange permission and explicit phase slot close the local endpoint interface conditionally without changing axioms. They do not retire physical preparation or driver suppliers. No claim that a new axiom is required is made.
* **N7, steelman:** a more economical sparse-code compiler, another connected graph with certified routes, or supplied ancilla access outside a strict path may reduce resources or avoid this particular full-SWAP assumption. Those possibilities remain open. They do not invalidate the displayed conditional schedule; they defeat any attempted universal obstruction based on its caveats.
* **N8, prior echo:** the exact finite-reservoir predecessor already separates an abstract conserving gate from physical local control and timing. This note uses a restricted homogeneous-energy domain and stronger supplied controls to address that interface. Its old general-H absence of a local construction is not treated as an impossibility result.

No scientific numerical runner was launched. The independent checks still required before acceptance are the finite-block/reference proof, gate and routing phases, the fixed-slot endpoint identity and the physical scope of the supplied control graph. A useful next finite discriminator is a nontrivial two-old-qubit target with complex amplitudes: certify its complete isometry, include both full SWAP and a fermionic-SWAP mutant, and verify (16) with an elapsed phase not equal to a multiple of 2pi. That proposed check has not been executed and is not evidence in this packet.

## 10. Exposure and handoff

The author previously constructed the exposed reservoir and bus/preparation/memory notes. This is same-model continuation, not an independent validation of those parents. The root's separate `local_conserving_control_root_proposal` was not read. The primary paper's theorem statements, path qualification and relevant synthesis argument were inspected; the entire 38-page paper and all circuit identities were not independently re-proved. Consequently the circuit theorem remains an attributed imported premise, and the explicit finite certificate (9) is the effective acceptance interface.

Only this assigned directory was written. Existing freezes, canonical notes, worktrees, Git, publication, audit files, locks, prompts and axioms were not changed. The source manifest distinguishes current reads from earlier author exposure. The final freeze binds the proposed source and provenance; it is not a scientific acceptance or a claim of independent review.
