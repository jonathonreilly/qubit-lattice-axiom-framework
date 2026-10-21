# Positive local matrix replacements with a vacuum-preserving head structure

New bounded author extension requiring a distinct check. The length-independent perturbation argument for scalar block weights extends to admissible positive matrix replacements on the same listed supports. The replacements need not preserve the program basis, record-X sectors, onsite/hopping ratios or other within-block tuning. They must preserve head number and have a scalar action on local head vacuum, with explicit local norm and scalar-error bounds. These are substantive admissibility premises, not a claim that arbitrary independent matrix entries can be varied in a symmetric box.

This source preserves frozen scalar-weight proposal321867 unchanged and reconstructs the broader lemma directly. Its scalar theorem is a special case. ROOT proposed the admissibility conditions and cap estimate; this is exposed author continuation, not independent review or a native-law derivation.

## 1. Nominal object and admissible replacement class

Use the exact finite one-control record device76b5, with the combined source blocks and combined mediator/program blocks, eight separately listed core vacancies and eight writer junction vacancies. All head sites and the single P and R are unchanged. The finite inventory is126+4ell qubits and164+4ell positive listed blocks. Denote the nominal blocks by h_l and their full-support norms by w_l=||h_l||.

Write each nominal block on its local support as

    h_l=c_l I+A_l,

where c_l=b for each of the eight core vacancies, c_l=(sqrt(2)-1)j for each of the eight writer vacancies, and c_l=0 for every other block. For a vacancy A_l=-c_l n_v; all other A_l=h_l. Every A_l annihilates the local head vacuum for all local program/record states and conserves the number of local heads.

Fix0<=delta<=1/2. A replacement is any self-adjoint matrix

    h'_l=c'_l I+A'_l                                      (1)

on the SAME listed local support, satisfying all the following conditions:

1. h'_l is positive on its complete support. No selected one-head or prepared-fiber positivity shortcut is used.
2. h'_l conserves total head number. Because its support is local and every other head is untouched, this is equivalent to conservation of head number on its support.
3. A'_l annihilates the local head-vacuum subspace for EVERY program/record fiber state on that support. Thus the vacuum action of h'_l is precisely the scalar c'_l I on that whole fiber.
4. c'_l=0 when c_l=0, and |c'_l-c_l|<=delta c_l for a vacancy. These numbers are real and are scalar on the local fiber.
5. On the FULL local Hilbert space, ||A'_l-A_l||<=delta w_l.

All replacements are static. They may be chosen separately and adversarially within these conditions, without statistical independence or cancellation. There is no requirement that they commute with P, with X_R or with one another. An occupied mediator may now drive a small coherent rotation of P, or an occupied terminal may act on a different record axis; these effects must obey (1)--(5) and will remain in the output error.

Positivity and conditions2--3 are membership requirements, not consequences of condition5. In particular nominal blocks often have zero eigenvalues, so a small unrestricted Hermitian error can leave the positive cone. No new support, head-changing process, arbitrary fiber-only vacuum Hamiltonian or initial-state error is covered. This defines a supplied local-matrix variation of the installed apparatus. If a more restrictive physical framework permits only the original exact block forms, admitting these replacement matrices is an additional explicit apparatus premise; it is not silently deduced from that framework or installed as a new axiom here.

## 2. Scalar separation and the full-fiber support lemma

Let H=sum_l h_l, H'=sum_l h'_l, and

    c=sum_l c_l=8b+8(sqrt(2)-1)j,
    c'=sum_l c'_l, Delta c=c'-c,
    K=sum_l A_l, K'=sum_l A'_l,
    E_l=A'_l-A_l, Delta K=sum_l E_l.                       (2)

Then H=cI+K and H'=c'I+K' exactly, with

    |Delta c|<=delta c.                                  (3)

Both head-vacuum restrictions are scalar on the entire P/R fiber. In particular no uncontrolled program-relative vacuum phase has been classified as a scalar.

Both Hamiltonians preserve the finite one-head space

    H_1=ell²(head sites) tensor C²_P tensor C²_R.

For block l let S_l contain only its HEAD sites, not any P or R site. Define the one-head projection

    Pi_l=sum_(v in S_l)|v><v| tensor I_(P,R).

If the sole head is outside S_l, its local head configuration is vacuum, so A_l and A'_l annihilate that vector by condition3 and the nominal property. Self-adjointness also kills the reverse matrix elements. Since head number is conserved, they do not map a one-head state to a different head-number sector. Therefore, as operators on H_1,

    E_l=Pi_l E_l Pi_l,
    |<psi,E_l psi>|<=delta w_l <psi,Pi_l psi>.             (4)

This proof holds with arbitrary program, record and passive-reference entanglement. It does not require E_l positive or P/X_R conservation. For a mediator/program replacement S_l is just its mediator head; for a terminal/record replacement S_l is just its terminal head. The shared P or R never supplies an additional moving-head coordinate or a factor counting fiber dimension.

Define the nominal head incident norm sum

    L_head=max_(head v) sum_(l:v in S_l) w_l.

Summing absolute quadratic forms gives

    |<psi,Delta K psi>|
       <=delta sum_v [sum_(l:v in S_l)w_l]
                              ||(<v| tensor I)psi||²
       <=delta L_head ||psi||².

Since Delta K is self-adjoint,

    ||Delta K||_(H_1 tensor ref)<=delta L_head.            (5)

There is no sum over the apparatus length. Overlapping supports and noncommuting fiber errors do not invalidate the absolute-form argument. It also works on vacuum-plus-one-head, since every remainder annihilates head vacuum. It is not asserted on unrestricted extensive head occupation.

For the actual nominal block inventory, use the full norms recorded by checked76b5 and reconstructed in the author precursor321867: head bonds2|a|, onsite occupations their coefficients, mediator/program blocks D1-2b, terminal/record blocks2j, vacancies their c_l and combined sources3j. The last value includes vacuum0, double occupation3j and one-head matrix[[j,-gamma],[-gamma,2j]], with0<gamma<=j. Thus all local components, including source diagonals and record contacts, are paid by full-support norms.

The head loads are D1+2b at a mediator,6b+4j at a core endpoint, at most(4+sqrt(2))j at writer heads and at most5j at the sources/caps/ordinary rays. Since eta=b/D0<=1/8, zeta=D0/D1<1/2, j=eta b<=b/8 and D1>16b, the mediator load dominates. Hence

    L_head=D1+2b.                                        (6)

The larger shared-P incident sum4(D1-2b) is required for the physical cap below, but is not the head-occupancy constant in (5). All P matrix errors nevertheless appear in (5) through their actual fiber operator norms.

## 3. The scalar-weight theorem is included, but correlations can be removed

For a scalar weight h'_l=(1+theta_l)h_l, |theta_l|<=delta<=1/2, choose c'_l=(1+theta_l)c_l and A'_l=(1+theta_l)A_l. The nominal A_l have norm w_l for both vacancy and nonvacancy cases, so condition5 holds. All other conditions hold. Thus frozen321867's concrete tolerance family is contained in the new class; no extra approximation term is added on top of that scalar result.

The new class is genuinely broader. Here is an explicit real two-head bond example. In the ordered local basis00,10,01,11, take the nominal Q_j with vacuum0, one-head matrix j[[1,-1],[-1,1]] and double-occupation energy2j. Choose INDEPENDENT parameters

    a,d,k in[0,delta], r in[-2delta,2delta],

and define the replacement with vacuum0, no head-number-changing matrix elements,

    one-head matrix j[[1+a,-(1-k)],[-(1-k),1+d]],
    double-occupation energy j(2+r).                    (7)

Its one-head diagonals are positive and its determinant is

    j²[(1+a)(1+d)-(1-k)²]>=0,

since a,d>=0 and0<=k<=1/2. Its double-occupation energy is at least j>0. Thus it is positive on all four local states. Its difference from Q_j has one-head matrix j[[a,k],[k,d]], whose norm is at most its largest absolute row sum, at most2delta j; the double-sector difference is at most2delta j. Therefore

    ||h'_bond-Q_j||<=2delta j=delta||Q_j||.              (8)

Here c'=c=0, so (8) is condition5. The two onsite values, hopping magnitude and double-occupation energy can vary independently within the displayed one-sided domain. Their original Q relation is not retained. All matrices are real, act on the same two qubits and conserve local head number. No complex coupling or three-qubit primitive is required for this example.

The domain in(7) is deliberately not a full symmetric entrywise neighborhood. For instance subtracting an arbitrarily small positive amount from one nominal one-head diagonal, without compensation, makes the expectation on the nominal symmetric zero mode negative. Such a matrix is outside this positive class. This is a local example explaining the positivity condition, not a no-go for other physical implementations or perturbation budgets.

A second example shows why P/X_R conservation is not hidden in the lemma. For a nominal mediator block n_m tensor B, where B is its positive diagonal2-by-2 program matrix, let O(s)=[[cos s,-sin s],[sin s,cos s]] and replace B by O(s) B O(s)^T. This remains positive, real and head-conditioned, with the same vacuum action. Since ||O(s)-I||<=|s|,

    ||O(s)BO(s)^T-B||<=2||B|| |s|.

Thus |s|<=delta/2 satisfies condition5 and generally introduces program off-diagonal matrix elements. The same real orthogonal conjugation of B=j(I+X_R) gives admissible record-terminal replacements that generally do not conserve X_R. These examples need no preassigned initial fiber eigenstate. Their resulting relative phases and fiber rotations are charged by (5), not declared harmless. They are examples of permitted supplied matrices, not a claim that a native mechanism produces the rotations.

## 4. Perturbed full-space incident cap

By condition5 and the scalar condition,

    ||h'_l-h_l||<=delta w_l+|c'_l-c_l|
                       <=delta(w_l+c_l)<=2delta w_l,
    ||h'_l||<=(1+2delta)w_l.                            (9)

For nonvacancy blocks the sharper factor1+delta holds. The uniform1+2delta is sufficient and counts scalar changes rather than discarding them. With the one-control cap choice D1=Lambda/8, the maximum nominal incident sum over ALL physical qubits is strictly below Lambda/2, including the shared program and shared record. Thus, for delta<=1/2,

    sum_(l incident v)||h'_l||
       <=(1+2delta)sum_(l incident v)w_l<Lambda           (10)

at every qubit. Positivity of h'_l is already required separately. No extra energy/time rescaling is needed beyond the parent's quarter-energy/fourfold-time implementation choice. A nominal design without the Lambda/2 margin would need its own reserve.

The same parameter domain gives, using b<Lambda/128 and j<Lambda/1024,

    L_head+c=D1+10b+8(sqrt(2)-1)j
        <[(25+sqrt(2))/128]Lambda<Lambda/4.             (11)

This coarse bound remains about nominal coefficients. Conditions1--5 and (10) do not require the perturbed matrices to admit any newly tuned global b,D0,D1,j representation.

## 5. Evolution and fixed phase on the entire physical fiber

All finite operators are self-adjoint and both evolutions preserve H_1. Duhamel and (5) imply, for every real t and every passive reference,

    ||exp(-itK')-exp(-itK)||<=min{2,delta L_head |t|}.

Restoring the true scalars gives the actual-phase comparison

    ||exp(-itH')-exp(-it Delta c)exp(-itH)||
                          <=min{2,delta L_head |t|},     (12)

and, when the nominal phase is kept fixed,

    ||exp(-itH')-exp(-itH)||
      <=min{2,delta L_head |t|+2|sin(Delta c t/2)|}
      <=min{2,delta(L_head+c)|t|}.                       (13)

The norm2 cap uses unitarity. These are whole one-head/fiber bounds, not estimates only on a favorable program or record branch. There is no spectral-completeness assumption about the perturbed device. Even if matrix errors break nominal matching, introduce new reflection or alter localized components, their entire finite-time effect is paid by Duhamel.

The extra scalar in(12) may be used only with its explicitly stated phase convention. The bounds below use (13) and the original nominal target; no phase measurement or fitted correction is required. For density channels the common scalar cancels, but relative program/record phases remain in Delta K and cannot be omitted. In contrast to scalar weights, P itself may fail to be conserved under (1); the final coherent-program error is bounded, not asserted identically zero.

## 6. Same simultaneous complete-output and absolute-flag guarantee

For0<epsilon<=1 construct the NOMINAL one-control logarithmic family at accuracy tau=epsilon/2, as in canonical02b432 from checked76b5/716038. This includes h=eta²=zeta=tau/10^5, D1=Lambda/8, j=Lambda tau²/(8*10^10), the prescribed positive cutoff normalization, source ratio rho=alpha tau sqrt(h), recomputed budgets and ell. Put

    T=7ell/(8j), t_minus=3ell/(4j),
    delta_safe=min{1/2,epsilon/(Lambda T)}.              (14)

Take any collection satisfying conditions1--5 with0<=delta<=delta_safe. Equation(11) gives delta(L_head+c)T<epsilon/4. Keep the identical nominal seed E: ordinary input P, one path head over the two I emitters, blank R and all other heads vacant, with arbitrary program/path/reference entanglement. No preparation error or calibration change is introduced in E.

The nominal final-output target is

    T_nom(t)=exp(-ict)J_F[beta_F(t) tensor C tensor|1>_R],

where C is the controlled C0=X_path,C1=I_path operation, beta_F is the common positively normalized nominal outgoing vector on F sites1<=n<=ell, and J_F makes all other heads vacant. The nominal bound is<3epsilon/16 on[t_minus,T]. Applying (13) to E and then the triangle inequality gives

    sup_(t_minus<=t<=T)||exp(-itH')E-T_nom(t)||
                           <7epsilon/16<epsilon/2.      (15)

This includes every output and any incorrect final P state; the program is not traced out. Both maps are isometries, so the unhalved complete output-channel discrepancy is<7epsilon/8<epsilon with arbitrary references. The target is the nominal packet, not a fitted perturbed packet. Its normalization and relative window width1/6 are supplied by the nominal theorem and are unaffected as definitions by replacement of H.

For the whole finite horizon retain ONE unnormalized target

    V_nom(t)=exp(-ict)J_F[B_fin(t) tensor C tensor|1>_R],
    B_n(t)=(-i)/sqrt(2pi) integral
                 exp(i[n+ell+57]k-itE_nom(k))g(k)dk,
    B_fin=P_(1<=n<=ell)B,

at every t in[0,T]. The nominal branch bound is<epsilon/4. Projecting the full difference (13) by the fixed mathematical P_R1 cannot increase its norm. Consequently

    sup_(0<=t<=T)||P_R1 exp(-itH')E-V_nom(t)||
                                    <epsilon/2.         (16)

No assumption that P_R1 commutes with H' is used; it generally does not even for the original writer. Both branch maps are contractions, so the unhalved subnormalized-channel/diamond discrepancy is<epsilon. Ideal trace remains the nominal input-independent ||B_fin(t)||². No early target is set to zero, and no small success probability is divided out.

On the final window the normalized target in(15) lies in record1 and retained F support, with all remaining heads vacant. Orthogonal projection therefore gives both record1 and joint record1/retained-F success probability strictly greater than1-(7epsilon/16)². This high-success conclusion comes from (15), not from an unjustified normalization of (16). It is uniform over the same arbitrary passive references.

The invariant one-head sector is sufficient for all these estimates even though the local matrices may change program or record states. Those changes need no additional decoder: their discrepancy from the original complete target is explicitly bounded by (13)--(16). The finite-horizon conclusion is not extended past T; the all-time unitary difference bound itself grows linearly and eventually becomes trivial.

## 7. Tolerance order and remaining physical scope

For the checked logarithmic nominal family at tau=epsilon/2,

    ell=Theta(epsilon^(-11/2)),
    T=Theta(Lambda^-1 epsilon^(-15/2)).

Thus the sufficient local-matrix parameter in(14) is delta_safe=Theta(epsilon^(17/2)). This now means ||A'_l-A_l||<=delta_safe||h_l|| on every complete listed support, with the separate scalar/vacuum, positivity and conservation conditions. It no longer means that all entries within a block have the same fractional error. It also does not give an unconstrained entrywise box: the admissibility tests remain essential, particularly near zero eigenvalues.

There is no extra factor proportional to ell in the generator estimate; the growing physical horizon T still tightens the required tolerance. Fixed prefactors and small nominal coefficients remain relevant. The estimate is sufficient and not optimal; it bounds the full one-head space rather than using the small actual mediator population to relax local errors. No fabrication precision cost, native coefficient supplier or metrology protocol is established by a matrix-norm allowance.

Conditions outside this class require a different analysis. A head-number-changing term destroys the invariant one-head argument; a nonscalar head-vacuum program/record term violates (2)--(4); a new support can change the occupancy-load sum; a nonpositive replacement is not an allowed positive apparatus block. These are explicit proof boundaries, not universal impossibility statements. No disconnected-bank example is needed to conclude that such errors are unproved here, and no permanent-halt inference is made.

## 8. Sources, exposure and check obligation

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. The unchanged initiating scalar source is common_product_single_control_robustness/PROPOSAL.md,3218676f11bbc39ecfcf3c84a568a2ffc8107a7b303f349195394a338b2b0623, authored and fully read immediately before this task, hash refreshed unchanged. Its distinct check was not supplied at this assignment; the new proof reconstructs rather than presumes acceptance of its load-bearing lemma.

The nominal apparatus and performance premises are unchanged:

- common_product_single_control_router/PROPOSAL.md:76b5fd9bdf7a1609dfbc981211a508991a6a24c53686e26f28907210007e1b01; distinct review549bf5e4862f9ad384fddaca6b6e73ae6c4da74c397b981c93a2d16473b418d0.
- common_product_logarithmic_flag_policy/PROPOSAL.md:7160387f62fdb71afadd3e30a37bf93d9dd566c9bfd9a3739177331bb68254a8; distinct reviewd1787938d55970246d222b91df1824c165bf16b58924cd7f5f3936a6d5cc16b3.
- common_product_single_control_publication/NOTE.md:02b43286a352594910b14e3dcbc2a5181d86f1ad806d1585c547f67138567cde, hash refreshed unchanged; integrated nominal source, not an additional independent check.

These proofs/checks were fully read at their exact pins during the immediately preceding coherent tasks. Their staged writer/finite/flag inventories retain the recorded source qualifications. No changed nominal premise was imported. ROOT supplied the generalized replacement conditions, cap factor and request for a nontrivial example; the author reconstructed the support proof without P/X_R conservation, the positive bond domain, real fiber rotations, full cap and complete target transfer after that exposure.

The decisive distinct check is whether conditions1--5 really imply E_l=Pi_l E_l Pi_l on the entire one-head/P/R/reference space for each actual local support. A reviewer should test head-conditioned noncommuting fiber examples, vacancy scalar changes and the combined source block, then independently verify the full-support positivity/norm of(7), the(1+2delta) cap reserve and nominal-phase budget. Any hidden program conservation, selected-fiber positivity or entrywise-box inference would be a defect. Neither the scalar precursor nor agreement with ROOT is independent evidence for this extension.

Only common_product_local_matrix_robustness/PROPOSAL.md was created. Frozen321867 and all nominal sources remain unchanged. No scientific executable, numerical solver/sweep/simulation, W/Git/checkpoint/axiom/editable-prompt/model modification, publication or delegation occurred. The result is a supplied-matrix robustness candidate pending distinct review, not a retained theorem, native realization, old literal processor transfer, preparation/readout supplier, indefinite herald, capture/reset or permanent halt.
