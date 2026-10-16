# Sparse compilation of the buffered-prefix conserving unitary

**Proposed conditional extension; acceptance of this source and its local-control parent is pending.** The specific buffered-prefix unitary does admit an explicit polynomial gate-count supplier for fixed old-qubit count q, under the parent's connected-path and full-SWAP permissions. The count below is derived from the actual selected basis states and the elementary synthesis argument, not from the ambient Hilbert-space dimension. It uses one clean synthesis ancilla. The nominal laboratory duration is O(epsilon^-4), with fixed incident strength and slew, while classical compiler runtime is not claimed efficient.

The mathematical parents are the frozen local-control derivation SHA256 `c7f0e58c79b7e05f7fe79374a8bbe52a290c0371392a0b0ddcdb98d3dbb49e60` and Bai–Marvian [arXiv:2309.11051v3](https://arxiv.org/pdf/2309.11051v3), particularly the elementary exchange identities, split-control recursion and single-ancilla phase mechanism. The root proposal and review directories remain unread. All permissions and physical supplier qualifications of the local-control parent remain in force. In particular full SWAP is an additional supplied positive edge interaction; strict-path XY+Z alone is not substituted for it.

## 1. Exact support and block count

Retain the parent's notation

    M=L+2q,       n=q+M=L+3q,       m=n+1,
    d=2^q,       a_count=M-q+1=L+q+1,       L>=1,q>=1.       (1)

Here n is the number of old-plus-reservoir qubits; m includes one synthesis ancilla. For an old computational bit string x of weight w(x), the selected basis vector in total-number sector a is

    b_(a,x) = x tensor 1^(a-w(x)) 0^(M-a+w(x)),
                    q<=a<=M, x in {0,1}^q.               (2)

All displayed prefix lengths lie between zero and M. Every such bit string has weight a. Distinct pairs (a,x) give distinct computational basis vectors, since the old substring determines x and the total weight determines a. Thus the exact size of the **selected** basis set is

    D_selected=(L+q+1)2^q.                                (3)

The target U_L(V) is the direct sum of a_count copies of the same d-dimensional V on these blocks, and the identity everywhere else, including nonprefix reservoir configurations and incomplete prefix sectors. The top block a=M is included even though the parent's initial sine packet never occupies it; deleting it would change the specified full unitary.

If “active” means basis columns actually changed by V, let r(V) be the number of x with V|x> != |x>. Then the exact minimal changed-column count is a_count r(V). It can be zero for V=I. Testing those equalities from arbitrary computable entries is not assumed decidable. The supplier uses the unconditional selected count (3), with no support oracle. The nonzero entries of U_L(V)-I are exactly repeated copies of V-I, so their count is a_count times the nonzero-entry count of V-I when that latter count is supplied.

For two basis strings in the same selected block,

    h(b_(a,x),b_(a,y))=h(x,y)+|w(x)-w(y)|<=2q.             (4)

The equality holds because two prefix strings differ on precisely the difference of their lengths. The distance is even because total weights agree. This uniform bound removes a possible accuracy-dependent cost from the intermediate logical basis-state routing.

## 2. A full block needs at most d(d-1)/2 special two-level gates and one phase

Let p=d(d-1)/2. A fixed lower-triangular elimination order turns any V in U(d) into

    G_p ... G_1 V = diag(1,...,1,det V),                  (5)

where each G_j acts on two basis rows and its nontrivial 2x2 block is in SU(2). To eliminate entries a,b in a pivot row and a lower row, take, for r=sqrt(|a|^2+|b|^2)>0,

    g=(1/r) [[conj(a),conj(b)],[-b,a]].                    (6)

It has determinant one and maps (a,b)^T to (r,0)^T. If r=0 the finite-real construction uses identity. Previously cleared columns remain zero on both affected rows. After a column is cleared, unitarity makes the surviving nonnegative pivot equal to one. The final upper-triangular unitary is therefore the displayed diagonal. Its last phase is det V because every elimination has determinant one.

Consequently V=G_1^* ... G_p^* D_V. For each sector a, apply the same p ordered 2x2 matrices to the pairs b_(a,x),b_(a,y) and apply det V to b_(a,11...1). Each such pair has distance at most 2q by (4). There are at most a_count p special two-level factors and **a_count** residual basis phases. There is no d-fold phase overcount and no attempt to apply a d-dimensional decomposition to the entire exponentially large physical space.

Equation (6) is a finite-real formula, not a claim that an exact zero pivot is decidable from a computable oracle. Section 7 gives a finite-error certificate selection that avoids such decisions and any discontinuous choice of Euler angles.

## 3. Explicit elementary base count, including inverse gates and phases

The alphabet used before nearest-neighbor routing consists of

    A_ij=exp(i pi R_ij/4),    R=(XX+YY)/2,
    Z_j(phi)=exp(i phi Z_j),    -pi<=phi<=pi.               (7)

Only the forward A gate is primitive; A^*=A^7 and iSWAP^*=A^6 are counted as seven and six forward gates respectively. A^8=I exactly. All angles can be reduced by multiples of 2pi without an extra scalar. We do not assign a unit cost to an inverse absent from this alphabet.

Write S=diag(1,i). Whenever S and S^* occur below, replace them by exp(-i pi Z/4) and exp(+i pi Z/4). Their omitted individual scalar factors exp(+i pi/4) and exp(-i pi/4) occur in conjugate pairs and cancel **exactly in each displayed construction**. This cancellation is proved at the logical-word level; the positive-pulse reserve phase of the parent is still paid separately.

For D_12=(Z_1-Z_2)/2, direct restriction to the single-excitation sector gives

    R_12=S_1^* A_12 D_12 A_12^* S_1.

Hence E(theta)=exp(i theta R) uses S_1^*, A, two opposite local Z rotations of angle theta/2, A^*, S_1: six letters if A^* were allowed, and **12 letters** in (7).

For three qubits define

    F=iSWAP_13 iSWAP_23^* iSWAP_12.

The primary exchange identity, checked directly in the finite discriminator, is

    F^* S_3^* R_23 S_3 F = Z_1 R_23.                     (8)

Since R_23 commutes with Z_1 R_23,

    C_b(theta)=E_23(theta/2) F^* S_3^*
                  E_23((-1)^b theta/2) S_3 F             (9)

is exp(i theta R_23) when qubit 1 equals b and identity when it equals 1-b, for either b=0 or b=1. F and F^* together contain three iSWAPs and three inverses, costing 3*2+3*6=24 forward A gates. The two general E factors cost 24, and S_3/S_3^* cost two onsite letters. Thus (9) costs at most **50 elementary gates**.

Conjugating by S_2 and S_2^* converts the internal X rotation to a Y rotation. Every SU(2) matrix has an X-Y-X Euler decomposition. Applying its three controlled rotations costs 3*50+2=**152 gates**, for either control bit. The circuit is exactly the desired controlled special two-level matrix, including its action on every other computational basis state. This reconstructs the constant rather than importing a generic O(1).

A controlled iSWAP on control bit 1 is cheaper: in (9), theta=pi/2 makes the two E factors A and A^7. The count is 24+1+7+2=**34**. The inverse controlled iSWAP has the same cost, with those two factors exchanged. These 34-gate circuits are the only controlled iSWAP cases needed in section 5.

## 4. Many controls require no extra ancillas

Consider a determinant-one two-level gate on two n-qubit strings of distance two. Relabel their two differing positions as target qubits; the remaining k=n-2 positions give a specified control pattern c. Relabeling here assigns gate operands; physical routing of the resulting elementary gates is counted in section 6.

For any U in SU(2), choose A_0,B_0 in SU(2) with

    A_0 B_0 A_0^* B_0^*=U.                               (10)

For completeness, write U=cos(theta)I+i sin(theta) v.sigma with unit v; choose a unit w perpendicular to v, set A_0=cos(theta/2)I+i sin(theta/2)v.sigma and B_0=i w.sigma. Conjugation by B_0 reverses v.sigma, so the commutator is A_0^2=U. For U=I or -I use respectively (A_0,B_0)=(I,iX) or (iZ,iX). This is a finite-real existence construction; no continuous globally chosen spectral frame is promised.

Split c into disjoint patterns c1,c2 of lengths floor(k/2),ceil(k/2). On every control-basis sector,

    Lambda^c(U)=Lambda^c1(A_0) Lambda^c2(B_0)
                   Lambda^c1(A_0^*) Lambda^c2(B_0^*).     (11)

If both patterns match, (10) acts; if either does not, the remaining pair cancels. This proof does not require or introduce a temporary Boolean flag or another clean ancilla. The same two target qubits carry all four operations.

Let T(1)=1 and, for integer k>=2,

    T(k)=2T(floor(k/2))+2T(ceil(k/2)).                     (12)

It counts the single-control leaves. Induction gives

    T(k) <= (9k^2-1)/8 for odd k,
    T(k) <= (9k^2-4)/8 for even k.                        (13)

The base k=1,2 is exact. For even k, use 4T(k/2)<=4[9(k/2)^2-1]/8. For odd k, the two children have opposite parity, so their two subtractions add to 2(1+4)/8; simplifying yields the first line. Therefore a distance-two special gate on n>=3 qubits costs at most

    B(n)=152 T(n-2) <=171(n-2)^2                          (14)

letters in (7). The actual integer recurrence is a reproducible count certificate. The proof does not silently treat an arbitrary controlled SU(2) as one controlled XY rotation.

## 5. General selected pairs and the single clean phase ancilla

If two same-weight strings b,b' differ in 2t positions, list l_1,...,l_t where b has 1 and b' has 0, and r_1,...,r_t with the opposite values. Successive exchanges of l_j,r_j turn b into b'. For j=1,...,t-1 replace exchange j by iSWAP on l_j,r_j controlled by l_(j+1)=1. On the evolving b branch that control remains one; on b' it is zero. Thus their product K satisfies

    K|b>=i^(t-1)|b_tilde>,     K|b'>=|b'>,
    h(b_tilde,b')=2.                                       (15)

For a desired U(b,b'), the matrix W=K U(b,b') K^* is a distance-two special gate; its 2x2 matrix includes the conjugation by diag(i^(t-1),1). This phase must be included. Then U(b,b')=K^* W K. K's permutations on all other states cancel because W is identity off its two-dimensional support. The cost is

    B(n)+68(t-1) <= B(n)+68(q-1)                         (16)

for every selected pair in (2), by (4). This is logical basis-state routing, before spatial routing.

For the residual phase z=det V on b_a=b_(a,11...1), add one ancilla A initially zero. This bit string always has a 1 in the first old position because q>=1. Let b'_a be b_a with that bit cleared. For a real theta with exp(i theta)=z, use

    P_a(theta)=exp{i theta[|b_a,0><b_a,0|
                            -|b'_a,1><b'_a,1|]}.          (17)

The two displayed m-qubit strings have equal weight a and distance two. Their nontrivial diagonal matrix has determinant one, so (14), with m=n+1, implements it using B(n+1)=152T(n-1) gates. On **every** data input with A=0, it multiplies exactly b_a by z and returns A=0. It acts as identity on all other A=0 data strings. Its action when A=1 is not required to be identity; it is included in the full physical unitary.

All a_count phases can reuse the same clean ancilla. In this chosen construction their partners are distinct because their prefix lengths differ. Even shared partners would merely accumulate commuting diagonal phases on A=1 and would not invalidate the A=0 isometry. No erasure or discarded register is used. The special two-level factors on the data do not logically act on A, and spatial routing later restores its wire after each gate.

Combining (5), (16) and (17) gives an exact conserving elementary word C satisfying

    C J_A = J_A U_L(V).                                   (18)

There is no unknown global scalar in (18). The target fixes the all-zero data state, the logical base constructions preserve their exact scalar, and the residual determinant phase is applied explicitly. In particular a scalar already present in V is not lost: it changes the selected block matrices and their decomposition while the off-block identity remains intact.

## 6. Quantified count on the physical path

Before spatial routing, a sufficient integer elementary-gate bound is

    G0 = a_count { p [152T(n-2)+68(q-1)] +152T(n-1) }.      (19)

This upper bound does not require checking whether a Givens factor or determinant phase is identity. It can be obtained from integer q,L alone.

Route each arbitrary-pair A gate on the supplied m-site path by moving one operand to its neighbor with full adjacent SWAPs, applying A, and undoing the route. At most 2(m-2)+1=2n-1 elementary physical gates are used for a pair gate. Onsite Z gates require one. Consequently

    G <= Gbar=(2n-1)G0                                   (20)

is a safe fully quantified physical count; an emitted list can use the tighter G_onsite+(2n-1)G_pair or its actual distances. All these full SWAP gates are the parent's supplied positive singlet-exchange controls, not gates synthesized by strict-path XY+Z alone.

Using (14), an explicit polynomial bound is

    Gbar <= (2n-1)(L+q+1)
          {p[171(n-2)^2+68(q-1)] +171(n-1)^2}.            (21)

For L>=1 define the fixed-q constant

    K_q=2(3q+1)(q+2)
            {171(p+1)(3q+1)^2+68p(q-1)}.

Then

    Gbar <= K_q L^4.                                     (22)

This bound follows from n<= (3q+1)L and L+q+1<=(q+2)L; it does not follow merely from a polynomial active dimension. It is loose and is not an optimality claim. If q grows, d=2^q and K_q are not uniform constants.

## 7. Finite-error compiler and certificate without pivot or phase oracles

There are two distinct interfaces.

**Exact finite-real interface.** Supplied exact SU(2) matrices/angles in (5), (10) and the Euler decompositions, plus a real representative of the determinant phase, yield (18) and counts (19)–(22). These real choices exist. No assertion that their discontinuous exact branches are computable from arbitrary computable V is needed for this existence statement.

**Effective finite-error interface.** Suppose V is supplied as a computable d-by-d unitary with certified matrix-entry enclosures, and choose a positive rational eta_C within the requested budget. Effective pulse and scalar evaluation additionally require computable energy/time constants with certified enclosures. There is no spectral-data selection here: the computational basis and all Hamming weights are fixed, while exact matching to the physically identified Delta remains supplied. The bound G0 is independent of V. Enumerate all words of length at most G0 in the finite operand alphabet (7), with each onsite angle on a sufficiently fine finite grid in [-pi,pi]. For instance choose grid mesh at most eta_C/[8 max(1,G0)]. An exact word supplied by (18) has a rounded word whose operator distance is at most eta_C/8, by telescoping unitary factors and ||exp(i phi Z)-exp(i phi' Z)||<=|phi-phi'|. Identity factors may be omitted; the bound is on length, not on the number of nonzero angles. All A gates remain exact in the mathematical word.

Verify a word by a certified **operator-norm** bound on

    E = C J_A - J_A U_L(V),                              (23)

accepting only a strict bound below eta_C. There is no freely optimized output phase; (23) tests the exact scalar convention. The search is finite in its word/angle choices. To avoid waiting forever on a failing candidate, evaluate successive uniform refinement levels over all candidates, or dovetail the strict certificates. At least one word has a strict margin, hence is eventually certified. This establishes a finite-error algorithm under computable-input oracles, not an efficient compiler.

An operator-norm certificate is itself computable without equality or spectral-degeneracy decisions. Approximate the finite matrix residual with a certified operator-norm error, and bound its norm from above using, for an integer k>=1,

    ||E|| <= Tr[(E^*E)^k]^(1/(2k)).                       (24)

The right side decreases toward ||E|| as k increases. Concretely, form a complex-rational matrix E_hat and a proved bound ||E-E_hat||<=delta; accept the rational strict inequality Tr[(E_hat^*E_hat)^k]<(eta_C-delta)^(2k), with rational eta_C-delta>0. Increasing k and refining delta eventually certifies the word with a strict margin. This uses the adjoint, the entire input isometry and all output rows. A plain full-matrix Frobenius test with the same coarse grid is not substituted: its dimension factor could destroy the margin.

The target-entry precision does not acquire a hidden exponential factor merely because the physical matrix is large. The direct-sum structure gives

    ||U_L(V_hat)-U_L(V)||=||V_hat-V||<=d delta_v           (25)

when every entry differs by at most delta_v; off-block identity agrees exactly. Thus delta_v<=eta_C/(32d) suffices as one input-error allocation. Numerical evaluation of an entire 2^m-dimensional word may require enormous storage and arithmetic, including matrix-entry precision with O(m) extra bits if using dimension-dependent norm conversions. Those are internal computation costs; no polynomial classical runtime or memory is claimed. Requested physical control angles, after a word is certified, need only the per-gate tolerances of the parent.

A complete emitted certificate should contain q,L, the selected-block indexing, the exact integer T/G0/Gbar values, the rounded word and operand list, its norm bound in (23), the input matrix enclosure/error contribution, the routed full-SWAP list, the actual gate count, and every logical/positive-pulse scalar. This note proves existence of such a finite certificate supplier; it does not fabricate a target-specific certificate for unspecified V.

## 8. Consequences for real duration, precision, energy and work

Use exactly the positive generators and cosine pulses of the parent. No new local gate permission is added. Its constants are Q_*=6pi and a fixed slot length

    h>=max(4 hbar Q_*/g, sqrt(4pi hbar Q_*/sigma)),         (26)

where g and sigma are accuracy-independent energy and energy/time bounds. Forward A and onsite Z words, followed by full-SWAP routing, are already in that physical alphabet.

One may use the actual routed count G, or pad with zero pulses to exactly Gbar slots. With padding the declared duration

    tau=(Gbar+1)h                                         (27)

is fixed from q,L before any target-dependent angle is chosen. The extra slot is the parent's simultaneous onsite phase correction. Let x=Delta tau/hbar, choose rational r with |r-x/(2pi)|<=1/4, k=floor(r)+2 and lambda=2pi k-x. Then 3pi/2<lambda<=9pi/2. At the declared endpoint the complete nominal propagator is

    U_lab(tau)=exp[-i(E0 tau/hbar+Phi)] C,                 (28)

where Phi is pi/4 times the number of forward A gates plus sum|phi| for the elementary onsite Z gates. Routing SWAPs have exactly cancelling endpoint reserve/exchange scalars, but their positive energy and work costs count. Since the logical certificate (23) uses phase one, no unknown zeta occurs in (28). For a rounded word, Phi is computed from that actual word, not from an unrounded ancestor.

The parent proves, with all S/B/A/R outputs retained,

    e_joint <=4pi q/(L+1)+epsilon_p+2eta_C+2eta_H+2eta_t.   (29)

Take its solved allocation L>=max(1,ceil(20pi q/epsilon)-1), epsilon_p<=epsilon/5 and eta_C,eta_H,eta_t<=epsilon/10. An effective selection need not decide the exact ceiling of a computable real: find a rational rho within 1/4 of x_e=20pi q/epsilon and set L=floor(rho)+2. Then x_e+3/4<L<=x_e+9/4, so the allocation holds and L<=(20pi q+3)/epsilon for 0<epsilon<=1. Define A_q=20pi q+3 and C_q=K_q A_q^4. Then

    Gbar<=C_q epsilon^-4,
    tau<=h(C_q epsilon^-4+1).                             (30)

These are explicit polynomial **nominal laboratory resource** bounds for fixed q,E0,Delta,g,sigma and the supplied physical graph permissions, starting with the supplied ready state and compiled schedule. They do not bound preparation time or the search/oracle walltime in section 7.

For physical coefficient requests use the parent with Gbar in place of G, including the idle time in its static-error integral:

    b <= hbar eta_H_budget/(3 tau),
    delta_Q,delta_lambda <= eta_H_budget/[3(Gbar+m)],
    |area_error| <= eta_H_budget/[3Q_*(Gbar+m)],
    |endpoint_time_error| <= hbar eta_t/(E0+m Delta).       (31)

Here b bounds additional static Hamiltonian error; the old K remains literal. The pulse generator and area formula requires the same pulse shape/support, as stated in the parent; additional shape/overlap error must be integrated separately. Actual positivity, incidence and slew are separate supplied calibration conditions, not consequences of small operator error. For explicit epsilon-only sufficient requests, put D_q=A_q+3q+1. Then m<=D_q/epsilon and tau<=h(C_q+1)epsilon^-4. With eta_H_budget=eta_t=epsilon/10, it suffices to request

    b_* = hbar epsilon^5/[30h(C_q+1)],
    delta_* = epsilon^5/[30(C_q+D_q)],
    area_* = epsilon^5/[30Q_*(C_q+D_q)],
    time_* = hbar epsilon^2/[10(E0+D_q Delta)].            (31a)

The first three bound the respective errors above and the last bounds endpoint time error. For the positive onsite generator Q_phi=abs(phi)I-phi Z, a physical angle error at most delta_*/2 ensures generator error at most delta_*. If each of the M+1 new free onsite fields has its own error, a sufficient per-field request is b_*/(M+1)=O(epsilon^6), since b is a global static-norm budget; the old K is unchanged. These are sufficient tolerances, not necessary lower bounds.

Evaluation of the final compensating lambda to delta_lambda=O(epsilon^5) has its own cancellation-sensitive arithmetic. Since tau and k are O(epsilon^-4), sufficient input requests are delta_Delta=O(epsilon^9) and delta_pi=O(epsilon^9), with explicit safe inequalities

    tau delta_Delta/hbar <=delta_lambda/4,
    2|k| delta_pi <=delta_lambda/4,                        (32)

and the remaining half of the allowance assigned to time/unit arithmetic and cross terms. Choose h as a fixed certified rational upper bound if an exactly specified rational schedule is wanted; then tau=(Gbar+1)h has no numerical angle dependence. If hbar is itself represented by an oracle, its reciprocal error must also be included. Global phase reporting needs the E0 tau/hbar and Phi errors explicitly: delta_E0<=hbar eta_phase/(3tau), plus corresponding bounds on tau/hbar and on sum|phi|. A grid of rational multiples of pi makes Phi a known rational multiple of pi; it does not make physical pi calibration exact.

The powers in (31)–(32) mean O(log(1/epsilon)) requested bits for these fixed finite physical numbers, with constants depending on the stated data. They give no bound on arbitrary computable-oracle response time or on numerical conditioning of an unverified branch-selection implementation. The finite grid/certificate selection bypasses the latter as an existence issue.

### A concrete optional model of pulse start-time error

The angle and area requests alone do not certify pulse-support timing. The default formulas above assume the prescribed slot supports, with other waveform errors charged by the parent's integrated norm condition. The following guarded variant prices one explicit alternative rather than silently treating a per-slot clock error as only an endpoint error.

Add one idle h slot before the circuit and one after the final phase pulse. Then tau_g=(Gbar+3)h; compute lambda using this full tau_g. The same endpoint identity (28) holds with tau_g, because every free interval is retained in the commuting F evolution. Suppose each nonzero pulse has the prescribed width/shape but its start is shifted by s_j, with |s_j|<=delta_s<h/2. The guard slots keep all actual pulse supports inside the common declared interval [0,tau_g]. For the final parallel layer the same bound may be imposed separately at each site.

The zero-extended cosine envelope obeys integral|f_h'|=4/h. Translation therefore gives an additional propagator-error bound

    eta_shift <= (4Q_*/h)(Gbar+m)delta_s.                 (33)

Take delta_s<=h eta_H_budget/[8Q_*(Gbar+m)], and spend the other half of eta_H_budget on the coefficient/shape-free part of (31), using tau_g. This is a sufficient absolute start-time request of order epsilon^5. If a separate model has same-sign period errors accumulating over Gbar+1 starts, a sufficient per-period request for its start-time component is delta_s/(Gbar+1)=O(epsilon^9); width/shape changes still need their own integral bound. There is no claim that pulse-area precision alone implies these timing bounds.

At most two neighboring serial pulse supports overlap when delta_s<h/2; during the final layer, at most one such serial pulse and one onsite pulse meet at a given site. If each actual pulse's positive integrated generator, including its area factor, has norm <=Q_*, then (26) bounds each pulse by g/2 and sigma/2. The overlapping sum is thus bounded by g and sigma at each site. Adding the parent's allowed new static-field error still fits Delta+2g. This is an explicit accuracy-independent cap/slew statement for this start-shift model. Its two added idle slots change only the constant in the O(epsilon^-4) duration and static/phase precision formulas: replace C_q+1 by C_q+3 where appropriate, and halve the coefficient error allocation. No microscopic clock or drift model is thereby supplied.

Other prices remain explicit:

* Added sites are M+1=O(epsilon^-1), including the clean ancilla. The reservoir's initial mean and variance are those of the supplied sine packet: mean Delta[q+(L-1)/2], variance at most Delta^2(L-1)^2/4. Its full physical dimension is 2^M; no small-dimensional hardware encoding is inferred from D_selected.
* The ideal common added incident cap remains Delta+g/2, with the parent's stated calibrated headroom Delta+2g and slew sigma. The global nominal installed norm remains at most E0+m Delta+m g/2=O(epsilon^-1). All positive reserves count.
* The ideal prescribed-drive net work is zero because every control commutes with the matched total free energy. Its absolute work is at most g(Gbar+m)=O(epsilon^-4); the coarser calibrated bound is sigma h(Gbar+m). This is a work functional of externally prescribed controls, not a microscopic finite driver returned to its initial state.
* Whole-system energy moments and covariances remain in the parent's conservation law. Trace proximity does not make individual battery energy transfer or moment error vanish. Supplied preparation and phase readiness, external clock/control outputs, native autonomy, permanent halt and indefinite reuse remain outside this result.

## 9. Decisive finite evidence and its limits

The named executable risk was the exchange-conjugation/control-bit sign and the six-letter variable-XY reduction, which determine the 152 and 34 constants. One exact SymPy source, SHA256 `2ede311427e4e765dfa0f75ac3ad7feeb4af31f5873f42a5bb1c787216c7d565`, was independently written without importing parent checker code. It checks the generator identity (8), both control-bit values, the variable-XY generator conjugation, the forward-A inverse powers, a non-real SU(2) split-control example, a complex d=4 Givens decomposition, clean-ancilla diagonal phases with a shared partner, and the integer q=2,L=1 prefix support.

The successful run returned exact squared Frobenius residual **16** for a wrong-S-adjoint mutant and **32/5** for an omitted-commutator-inverse mutant, so these checks distinguish the relevant errors. The complex four-dimensional example uses six determinant-one eliminations and leaves residual phase -i. The selected-prefix case contains 16 selected states in four sectors, with maximum internal Hamming distance four. Complete source-at-launch, launcher, argv/cwd, limits and both streams are retained.

The first launcher failed in preexec_fn before the scientific source began; no mathematical result is attributed to it. That receipt and streams are preserved. The retry removed the attempted address-space limit, retained a 90-second wall timeout and 60-second CPU limit, ran the same source once, and finished in about 1.48 seconds with exit code zero. The exact preexec failure cause was not exposed, so it is not attributed to a particular resource limit as a proven diagnosis.

This is author-produced exact finite evidence, not independent acceptance and not a general compiler proof. The general block, recurrence, routing, phase and quantifier arguments are the analysis above. The primary paper is used with its actual hypotheses and circuit identities; no full revalidation of all its unrelated sections is claimed. The next useful independent check is to inspect (19) against a generated elementary list for a complex two-old-qubit target, including the sector determinant phase and the spatial SWAP count. No such end-to-end compiler run is claimed in this packet.

## 10. Source status and exposure

This is an exposed continuation by the author of the local-control and earlier reservoir parents. Their source status is not promoted. The exact parent bytes were pinned and copied; no parent freeze was edited. The same inherited model and reasoning effort were preserved, with no delegation. The root proposal and review directories were not read.

The earlier parent intentionally made no polynomial runtime claim. This note proposes a new, separately reviewable count supplier under its same restricted permissions. The broad general-H problem, a strict XY+Z-only path, and access through only one old port are not covered by the count. There is no universal negative claim or claim that failure of another architecture is established.

Only this assigned new directory was written. Canonical sources, Git, PRs, audit/cache/lock state, prompts and axioms were not changed. Root owns acceptance and publication. The final freeze binds source and actual evidence, not a desired verdict.
