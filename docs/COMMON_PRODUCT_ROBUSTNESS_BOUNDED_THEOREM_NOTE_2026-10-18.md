# Finite-horizon robustness of the common-product single-control apparatus

Status: conditional robustness theorem for a supplied finite positive local Hamiltonian. The parent construction has an ordinary program qubit, one path head, blank apparatus and a common complete output. This note permits bounded changes to its listed local matrices, including changes that conserve neither head number nor the program or record-X axes. Multi-head leakage is included in the output error. It does not derive the physical supply of those matrices, initialization or readout. The result is a finite-horizon error guarantee, not permanent halt or reset.

The exact nominal apparatus and all inherited preparation, normalization, phase, resource and finite-window premises are those of the [single-control bounded theorem](COMMON_PRODUCT_SINGLE_CONTROL_BOUNDED_THEOREM_NOTE_2026-10-18.md), PR9712 at `abcec11eb9dbbd585c530f8003d0b0c18d703612`. Its complete-output and absolute record-branch conclusions are used at half the requested accuracy. No scattering identity of a perturbed device is assumed.

## 1. Admissible positive local matrices

Let the nominal finite Hamiltonian be H=sum_l h_l, with the parent's exact listed block convention: 126+4ell physical qubits, 164+4ell positive blocks, combined source blocks, combined mediator/program blocks, and sixteen separately listed vacancy blocks. All full-support norms below include vacuum, one-head and multiple-head local sectors. Write

    h_l = c_l I + A_l,       w_l = ||h_l||.

For eight core vacancies c_l=b; for eight writer vacancies c_l=(sqrt(2)-1)j. For every other block c_l=0. The vacancy remainder is -c_l n_v; all other A_l=h_l. Every remainder conserves head number and annihilates its local head vacuum for every local program/record state.

Fix 0<=delta<=1/2. Replace each listed block on the same support by a static self-adjoint matrix h'_l=c'_l I+A'_l satisfying:

1. h'_l is positive on the complete local Hilbert space.
2. A'_l annihilates local head vacuum for every program/record fiber state.
3. c'_l=0 if c_l=0, and |c'_l-c_l|<=delta c_l otherwise; these are real scalars on the whole fiber.
4. ||A'_l-A_l||<=delta w_l on the complete local support.

Different replacements may be chosen adversarially within this class; statistical cancellation is not used. Neither head-number, program-basis nor record-X conservation is required for the replacement. Positivity, scalar vacuum action and unchanged support remain substantive conditions. An arbitrary entrywise perturbation need not satisfy them. Admitting these supplied matrices is an explicit apparatus premise wherever the underlying physical framework allows a narrower exact block family; it does not change an axiom.

The [vacuum-preserving source](../outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/PROPOSAL.md) states this class and proofs in full. The [head-conserving matrix source](../outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/PROPOSAL.md) preserves the intermediate, narrower result. The [scalar-block source](../outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/PROPOSAL.md) treats its special case h'_l=(1+theta_l)h_l with |theta_l|<=delta. That special case keeps within-block coefficient correlations; the larger class does not require those correlations.

## 2. Why the error does not sum over apparatus length

The scalar part is

    c = 8b+8(sqrt(2)-1)j,
    c' = sum_l c'_l,       |c'-c| <= delta c.

Set K=H-cI and K'=H'-c'I. On the full finite head Hilbert space, label occupation basis states by subsets Z of head sites and tensor the complete program/record fiber and any passive reference. Let Pi_1 select exactly one head. For each local head-site support S_l, excluding P/R, define

    Pi_l^in = sum_(v in S_l) |{v}><{v}| tensor I_fiber,
    Q_l^out = sum_(empty != Z subset S_l) |Z><Z| tensor I_fiber.

The output projection requires every head outside S_l to be vacant. It does not merely require some head locally present. For E_l=A'_l-A_l, vacuum annihilation kills one-head inputs outside S_l. On inputs inside S_l, locality keeps outside heads vacant and self-adjoint vacuum annihilation excludes the empty output. Therefore

    E_l Pi_1 = Q_l^out E_l Pi_l^in.

With L_head=max_v sum_(l:v in S_l) w_l, the input sum is bounded by sum_l w_l Pi_l^in <= L_head Pi_1. The output sum obeys sum_l w_l Q_l^out <= L_head I: for each nonempty Z its eigenvalue is sum_(l:Z subset S_l)w_l, bounded by the incident load of any v in Z. Empty Z has eigenvalue zero. Shared program/record qubits are fiber coordinates, not extra head positions.

Define B psi=(sqrt(w_l)Pi_l^in psi)_l, D=direct_sum_l E_l/w_l, and A(x_l)=sum_l sqrt(w_l)Q_l^out x_l, omitting zero blocks. Then B*B and AA* are the two projection sums, ||D||<=delta, and ADB=(K'-K)Pi_1. Hence

    ||(K'-K)Pi_1|| <= delta L_head,
    L_head = D1+2b.

This is a rectangular norm into the full physical output space, not a bound on K'-K over arbitrary extensive head inputs. It needs no mutual commutativity or perturbed head-number conservation.

A mediator attains the last incident norm sum. Core endpoints have load 6b+4j, writer heads at most (4+sqrt(2))j, and sources/caps/rays at most 5j. Since j<=b/8 and D1>16b, none exceeds D1+2b. The combined source has full norm 3j: its double-occupation eigenvalue is 3j, while its one-head matrix is [[j,-gamma],[-gamma,2j]] with 0<gamma<=j. Using only its selected one-head norm would misstate the physical accounting.

This bound also holds on vacuum-plus-one-head inputs because every remainder annihilates global head vacuum. It has no block-count or ray-length factor. The eventual runtime still enters the evolution bound.

For t>=0, use Duhamel with the actual FULL propagator on the left and the nominal one on the right:

    [exp(-itK')-exp(-itK)]Pi_1
      = -i integral_0^t exp(-i(t-s)K') (K'-K) exp(-isK)Pi_1 ds.

Only the nominal right trajectory must remain one-head. The actual left propagator is unitary on all head sectors. Consequently, for all real t,

    ||[exp(-itH') - exp(-it(c'-c))exp(-itH)]Pi_1||
        <= min{2, delta L_head |t|}.

If the original target phase is retained, as below, the bound is

    ||[exp(-itH') - exp(-itH)]Pi_1||
        <= min{2, delta L_head |t| + 2|sin((c'-c)t/2)|}
        <= min{2, delta(L_head+c)|t|}.

These operator estimates include arbitrary passive references, coherent program/record errors and all extra-head leakage. They do not compress the actual Hamiltonian to one head. A common scalar cancels for density channels, but no relative program, path or record phase is discarded. The nominal target is not fitted to the perturbed device.

## 3. Nontrivial positive examples and the incident cap

For a nominal real bond Q_j, in the local basis 00,10,01,11, independently choose a,d,k in [0,delta] and r in [-2delta,2delta]. Keep vacuum energy zero and use

    one-head matrix: j [[1+a, -(1-k)], [-(1-k), 1+d]],
    double-occupation energy: j(2+r).

The one-head determinant is j^2[(1+a)(1+d)-(1-k)^2]>=0 and its diagonals are positive. The double-occupation energy is at least j. The difference norm is at most 2delta j=delta||Q_j||, by the one-head absolute row sums and the double-sector bound. This is a real positive example with independently variable onsite, hopping and double-occupation values. It is a one-sided admissible domain, not a full symmetric entrywise neighborhood around a singular positive matrix.

For a head-conditioned mediator n_m B, a real orthogonal conjugation B'=O(s)BO(s)^T is positive and satisfies ||B'-B||<=2||B|| |s|. Thus |s|<=delta/2 is admissible and generally rotates the program basis. The same construction for B=j(I+X_R) allows record-terminal matrices not commuting with X_R. These are mathematical examples of supplied local matrices, not physical production protocols.

A genuine positive number-changing example is also available. Let S=(|10>+|01>)/sqrt(2), A=(|10>-|01>)/sqrt(2), D=|11>, and D_s=cos(s)D-sin(s)S. The nominal Q_j=2j|A><A|+2j|D><D| can be replaced by

    h'_bond=2j|A><A|+2j|D_s><D_s|.

This real two-qubit matrix is positive, annihilates |00>, and has difference norm 2j|sin(s)|<=delta||Q_j|| for |s|<=delta. Its S/D matrix element is -2j sin(s)cos(s), nonzero when 0<|s|<=delta<=1/2, so it genuinely mixes one and two heads. The attempted rotation of A with D would instead leave Q_j unchanged because both have energy 2j; that failed example is preserved in the source. This construction does not supply a native production mechanism.

For every block,

    ||h'_l|| <= (1+2delta)||h_l||.

This pays both scalar and remainder changes. The parent's choice D1=Lambda/8 gives a nominal incident norm sum strictly below Lambda/2 at every physical qubit, including the shared program load 4(D1-2b) and record load 8j. Therefore the replacement still obeys the all-qubit cap strictly below Lambda for delta<=1/2. No further energy rescaling is needed. Moreover,

    L_head+c = D1+10b+8(sqrt(2)-1)j
        < (25+sqrt(2))Lambda/128 < Lambda/4.

## 4. Simultaneous complete-output and record guarantees

Given 0<epsilon<=1, instantiate the parent's logarithmic source policy at tau=epsilon/2. All nominal parameters, cutoff normalization, budgets and ell are recomputed as prescribed there; in particular j=Lambda tau^2/(8*10^10). Define

    T = 7ell/(8j),       t_minus = 3ell/(4j),
    delta_safe = min{1/2, epsilon/(Lambda T)}.

For any admissible replacements with delta<=delta_safe, the fixed nominal-phase perturbation error is less than epsilon/4 throughout [0,T]. The seed remains the parent's ordinary program input, one dual-rail path head at the I emitters, blank R and all other heads vacant, with arbitrary logical/reference entanglement. Initial-state error is not part of this theorem.

Let E denote that input isometry. The normalized complete nominal target on [t_minus,T] is

    T_nom(t) = exp(-ict) J_F[beta_F(t) tensor C tensor |1>_R],

where C applies X_path for program0 and I_path for program1, beta_F is the common positively normalized nominal outgoing packet on F sites 1..ell, and J_F sets every other head to vacuum. The parent error at tau is less than 3epsilon/16. Hence

    sup_[t_minus,T] ||exp(-itH')E-T_nom(t)|| < 7epsilon/16.

Every apparatus output, the program and all multi-head sectors are retained. The complete unhalved output-channel discrepancy is less than 7epsilon/8<epsilon, including arbitrary references. For clarity, define Pi_good to require record1, EXACTLY ONE total head on retained F sites, and every other head vacant, with identity on P/reference. Its probability exceeds 1-(7epsilon/16)^2 on this window, whose relative width is 1/6. This follows from the normalized complete target, not by dividing a small branch error by success probability.

For the entire horizon [0,T], retain the SAME unnormalized nominal target

    V_nom(t) = exp(-ict) J_F[B_fin(t) tensor C tensor |1>_R],
    B_n(t) = (-i)/sqrt(2pi) integral
                 exp(i[n+ell+57]k-it E_nom(k)) g(k) dk,
    B_fin = P_(1<=n<=ell) B.

The parent branch error is less than epsilon/4. Projection of the perturbed complete evolution adds less than epsilon/4, so

    sup_[0,T] ||P_R1 exp(-itH')E-V_nom(t)|| < epsilon/2.

Both maps are contractions, giving unhalved subnormalized-channel/diamond discrepancy less than epsilon. No early branch target is replaced by zero, no rare branch is normalized, and no commutation of P_R1 with H' is assumed. The ideal branch trace remains the input-independent nominal ||B_fin(t)||^2. Program and record rotations and record1 events with multiple heads are charged in these bounds. In addition, throughout [0,T], the probability of leaving the one-head sector is bounded by (delta L_head T)^2<(epsilon/4)^2: project the actual-phase comparison onto the complement of Pi_1, which annihilates the nominal evolution. This is included in the complete error, not an additional budget. Global head vacuum remains reducing, so leakage from a one-head input cannot be to zero heads.

## 5. Resource meaning and verification limits

The nominal family at tau=epsilon/2 has ell=Theta(epsilon^(-11/2)) and T=Theta(Lambda^-1 epsilon^(-15/2)), with the parent's explicit large constants. Consequently the sufficient matrix-error parameter is delta_safe=Theta(epsilon^(17/2)). This is a tolerance allowance, not a necessary precision, optimal bound or fabrication cost. It avoids an extra factor of apparatus length in the generator norm; the growing runtime still tightens it.

In the scalar-weight special case only, gamma=Theta(Lambda epsilon^(7/2)) has an induced correlated allowance delta_safe gamma=Theta(Lambda epsilon^12). That statement is not an independent weak-hop perturbation with its source diagonals fixed, and is not the definition of the broader matrix class.

The [scalar review](../outputs/common_product_robustness_2026_10_18/source_checks/scalar_weights/REVIEW.md), [head-conserving matrix review](../outputs/common_product_robustness_2026_10_18/source_checks/local_matrix/REVIEW.md) and [vacuum-preserving review](../outputs/common_product_robustness_2026_10_18/source_checks/vacuum_preserving/REVIEW.md) provide selective distinct checks of the changed load-bearing arguments. The [source manifest](../outputs/common_product_robustness_2026_10_18/SOURCES.json) pins complete source bytes and inherited evidence; the [integration record](../outputs/common_product_robustness_2026_10_18/INTEGRATION_RECORD.md) states exposure and integration scope. Checks are source-exposed, same-model and share inherited ancestry; they are not blind replication, model-diverse confirmation, a new full dynamical simulation or retained audit.

Unwanted supports, creation of heads from local vacuum, nonscalar head-vacuum fiber terms, nonpositive blocks and initialization errors lie outside this class. Head-number changes from an already occupied local region are covered; arbitrary vacuum-creating noise is not. Native Hamiltonian/coefficient/Record identification, blank-state and readout supply, literal old-processor transfer, permanent storage, irreversible capture and reset/reuse remain unresolved. No theorem is extended past its finite useful horizon and no universal impossibility conclusion is asserted.
