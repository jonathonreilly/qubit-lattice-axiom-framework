---
title: Joint-code energy moments for the conditional strong spectral bus
claim_id: bus_joint_energy_moments_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: same-installed-generator joint-code first and second moments and variance under the qualified strong spectral bus premises
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: conditional mathematical corollary with explicit full-space reserve and precision allowances; no native or measured-energy identification
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: ["strongly_regular_bus_bounded_theorem_note_2026-10-15"]
runner: scripts/bus_joint_energy_moments_2026_10_16.py
next_trace_action: bind actual final canonical review, run scoped source-integrity integration, then regular publication and independent retained audit
---

Claim type: bounded_theorem

The joint old/source code comparator of the qualified strong spectral bus has uniformly bounded first and second moment errors for the same installed nominal Hamiltonian. The bounds hold at all real times and yield a statewise variance bound. An additional positive smallness choice can meet independent moment tolerances while preserving the parent's finite-window state contract at the resulting actual duration. This does not establish laboratory measured energy, preparation work, or an accuracy-independent total-energy bound.

Qualified source acceptance is `530e64f0a12506eb1f99f84ceb4ac2ab3b55e2f9b518b4121a46f2e9f4cae74a`, recorded 2026-10-16T01:38:37.798475Z; controlling qualifications are `bdb0e8d2b513a4b318ad54a6c2627ec4f911fd6f700a962dd659ef1338f2712f`. The complete original proposal and exposed review follow unchanged. Their historical pending-status sentences remain literal history. Source acceptance does not accept this new wrapper, canonical integration, publication or retained status.

## Exact contract

Use the parent's complete finite code inclusion J, including all old factors, bus vacuum and every symmetric excitation sector of every source. Arbitrary code inputs and correlated passive references are allowed. The same actual installed static nominal generator appears in both moments:

```
K = K0 + xi V + xi^2 A2 + R(xi)I,
K0 J = J F,   J*J = I,   J*VJ = 0,   [F,D] = 0,
C_xi(t) = exp[-it R(xi)] J exp[-it(F+xi^2 D)],
A_xi(t) = exp(-itK)J,    C_xi(0)=J.
```

The full counterterm A2 preserves bus vacuum, and the bus-vacuum block of V is zero. These additional premises remove the cubic compression; J*VJ=0 alone does not. All operators are Hermitian as specified in the sources, all actual reserves remain installed, and A2 need not preserve source symmetry. The comparator retains joint source evolution and its correlations; it is not an unchanged free-source product or a dressed physical input.

Writing F_R=F+R(xi)I and A_c=J*A2J gives

```
J*KJ   = F_R + xi^2 A_c,
J*K^2J = F_R^2 + xi^2[J*V^2J + {F_R,A_c}] + xi^4 J*A2^2J.
```

The quartic term includes the positive off-code contribution
`J*A2^2J - A_c^2 = [(I-JJ*)A2J]*[(I-JJ*)A2J]`.
The anticommutator includes `2R(xi)A_c`. Neither term disappears by a scalar phase or source-symmetry projection.

For v>=||V||, a2>=||A2|| and f_R>=||F||+R(xi), the complete code operator errors obey

```
E1(t) <= 2 xi^2 a2,
E2(t) <= 2 xi^2[v^2+2 f_R a2] + 2 xi^4 a2^2.
```

They hold for every real t because the leading F_R terms commute with the code propagator, while the exact physical evolution conserves J*K^jJ. For each density input, a bound B_N>=||K|| gives variance discrepancy at most E2+2B_N E1. Variance is not a linear operator. These all-time moment statements do not extend the parent's state approximation beyond its proved interval 0<=t<=T+w.

## Loads, quantifier order and precision

The complete physical-space load allowance is

```
B_N = h+R_s+(3b-2)M_E+q(3N-2)M_E+J1+qN J2,
Fbar_N = h+qN M_E+R_s+(b-1)M_E+J1/2+qN J2,
C2_N = v^2+2 Fbar_N a2+a2^2,   J1=J2=1/t_*.
```

It pays the old norm, actual positive reserves, every bus/source block and off-code counterterm load. B_N can grow with source length N. The inherited common added incident cap `J_*=R_s+7M_E+J1+J2` is not a common global energy or action bound.

After N, all spectral/calibration data, full-space corrector bounds and load/moment coefficients are bounded, add to the parent's positive xi constraints

```
xi <= sqrt(delta1/[2(a2+1/t_*)]),
xi <= sqrt(delta2/[2(C2_N+1/t_*^2)]),   xi<=1.
```

Here delta1 has energy units and delta2 has energy-squared units. The positive slack in the denominators is mathematical, not new hardware. The choice yields E1<=delta1 and E2<=delta2. Variance accuracy follows by allocating delta2 and delta1 against E2+2B_N E1. Compute the **new actual** T=t_*/xi^2, every source input phase, comparator scalar phase, both literal old-H flows and every physical timing/calibration budget at that T. A promise valid only for an earlier shorter run is insufficient. No favorable runtime, precision or search bound follows.

The strong-spectrum, all-port-transition, computable-data and vacant-geometry premises remain inherited from the sole mathematical parent. They are not inferred from a generic Lie certificate. The parent's separately attributed rational Hermitian M repair governs effective target approximation; all moment equations then concern the actual M-designed device and its own K,V,A2,D,R. Certified rational upper rounding avoids an exact-ceiling oracle.

Preparation trace error e may add B_N e and B_N^2 e to the first two moment errors. A normalized isometric numerical comparator error zeta may add 2 B_N^j zeta. General rounded matrices need their own norm/normalization allowance. Trace readiness alone does not establish moment accuracy. Different physical generators or release states have different conserved constants; long-time coefficient errors and physical calibration remain explicit obligations.

## Evidence and publication boundary

The unchanged proposal is 7,871 bytes, SHA256 `86a830e180dae0afba7d13f64bb0d906096e307eb5e3dc5d6e43bf1b52d794c1`; the unchanged exposed review is 19,400 bytes, SHA256 `498017c60000572ea30408602904cacbafde77e41dc167012a1fb66ac0d582b1`. The reviewer executed one independently assembled exact dimension-32 discriminator, retaining all source sectors. It detects omitted quartic leakage, reserve cross terms, a forbidden cubic term and failure of the commuting-code premise. It is not the full calibrated routed bus or an all-parameter computational proof. This was source-exposed same-model recomputation, not blind or model-family replication.

The historical child argv includes `-B`. The secondary launcher annotation omitted that interpreter flag; the original receipt and explicit retrospective disclosure remain unchanged. Historical failed source-location/directory attempts and the truncated read are preserved in SOURCE_EXPOSURE. There was no failed scientific execution in this moment-check packet and no science replay during packaging. The primary checks source identities, exact body recovery, historical receipt linkage and later actual binding only; metadata checks do not prove the mathematics.

The sole direct mathematical dependency is the qualified strong spectral bus source, acceptance `cc2e519d8c4de174cc98137a8f9c5e2ae7df6a782adfd93d7389d1eac346c726`. Its regular PR9631 publication receipt records HEAD `68c531309ac6dae96289aab964213b8c5f55969b` and canonical note SHA256 `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b`. That is dependency publication provenance, not an observation of this draft's future integration base. The original parent qualifications, including missing failed launchers and invalid first-seal history, remain binding through that dependency.

Native formation/release, source preparation, isolation, calibrated long-time evolution, operational energy measurement, work, stopping, records and reset/reuse remain open. The frozen source review and actual local base bind separate evidence. Final canonical review, primary execution, publication and retained audit remain distinct gates. No physical axiom or editable prompt changed.

---

## Immutable source body: root_proposal

# Joint-code moment comparison for the conditional fixed-strength bus

Status: root mathematical proposal, not yet independently checked or accepted. It depends conditionally on the exact algebra and error bounds in strongly_regular_bus_candidate/DERIVATION.md, SHA256 855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2, whose own exposed check is still pending. It is not a theorem for the original generic Lie-certificate domain. The purpose is to retain source energy recoil in a finite comparison without propagating the complete high sector.

## 1. Exact objects and scope

Use the parent's actual finite source length N, bus, code isometry J, code generator F and secular D. On the full physical Hilbert space,

    K = K0 + xi V + xi^2 A2 + R(xi) I,
    K0 J = J F,  J*J=I,  J* V J=0,  [F,D]=0.

Here J includes bus vacuum and all symmetric source sectors, with identity on every old factor. A2 is the actual source-only counterterm, not its projection; it preserves bus vacuum but may leave source symmetry. V changes bus excitation by one when applied to a vacuum vector. All reserves are the actual installed R(xi), not norm bounds. Define

    U_c(t)=exp[-it(F+xi^2 D)],
    C_xi(t)=exp[-it R(xi)] J U_c(t).

C_xi is exactly an isometry from the complete code, and C_xi(0)=J. It retains joint old/source evolution and source correlations. It is not the parent's product mean-field target and is not a dressed initial state. The physical nominal evolution is A_xi(t)=exp(-itK)J. The parent's bare-code estimate gives ||A_xi(t)-C_xi(t)|| <= xi C_corr on 0<=t<=T+w, T=t_*/xi^2. That input/operator estimate also holds after tensoring an arbitrary passive reference.

The first and second moments below are those of the very same physical K. Moment differences mean operator norms on the full code, so they imply uniform expectation bounds for all code/reference density inputs. Conservation under A_xi gives A_xi(t)*K^j A_xi(t)=J*K^j J.

## 2. Projected moments and exact cancellation

Write A_c=J*A2 J, V_2=J*V^2 J, A_2=J*A2^2 J, and F_R=F+R(xi)I. Then

    J*K J = F_R + xi^2 A_c,
    J*K^2 J = F_R^2
        +xi^2 [V_2 + {F_R,A_c}] +xi^4 A_2.       (1)

To check the expansion: K0 J=JF and its adjoint eliminate both linear V cross terms by J*VJ=0. They convert the K0/A2 cross terms to {F,A_c}. The scalar adds the remaining 2R A_c. Both cubic terms J*VA2J and J*A2VJ vanish because A2 preserves bus vacuum and V changes its excitation by one. This selection rule concerns the actual full-space A2, including its off-symmetric action. The quartic term is J*A2^2J, generally not (J*A2J)^2. No positivity or invariance of A2 on the code is asserted.

Since U_c commutes with F_R, the leading terms in (1) cancel exactly in C_xi(t)*K^j C_xi(t)-J*K^jJ. For bounds v>=||V||, a2>=||A2|| and f_R>=||F||+R(xi),

    E1(t) <= 2 xi^2 a2,
    E2(t) <= 2 xi^2 [v^2+2 f_R a2] +2 xi^4 a2^2. (2)

These inequalities hold for every real t, independent of the parent's finite state-comparison window. Their derivation uses ||U*XU-X||<=2||X||, ||V_2||<=v^2, ||A_2||<=a2^2 and ||A_c||<=a2. They do not identify C_xi with actual full evolution outside that window. For any fixed density input, if B>=||K|| then the variance discrepancy is at most E2+2B E1, since each mean has magnitude at most B.

In particular, retaining the joint code dynamics can carry finite energy transfer between old plant and source. Replacing it by an unchanged free source product erases that transfer and does not inherit (2).

## 3. A cap-compatible choice of xi with separate units

The parent first fixes N, all bus/source spectral data, calibration, r_l, counterterms and finite corrector bounds, then chooses xi. Thus v and a2 are finite and known before this additional refinement, although they can be enormous and N-dependent. Further decreasing xi preserves all parent state, window and incident-load inequalities; the duration and phases must be recomputed at the actual xi.

For an explicit xi-independent bound on f_R, let q be the number of sources, b the number of bus sites, and M_E the parent's uniform bound on positive base onsite frequencies, hoppings and J_F. Its physical load choices are xi ell_V<=J1 and xi^2 ell_2<=J2, with J1=J2=1/t_*. They imply

    R(xi) <= R_s+(b-1)M_E+J1/2+qN J2,
    ||F|| <= h+qN M_E.

Indeed R_bus has b-1 edges, ell_V=2R_V, and R_A2<=sum_l[N|u_l|+(N-1)|v_l|]<=qN ell_2. Set

    Fbar_N=h+qN M_E+R_s+(b-1)M_E+J1/2+qN J2,
    C2_N=v^2+2 Fbar_N a2+a2^2.

For xi<=1, (2) becomes E2<=2xi^2 C2_N. Choose independent positive moment tolerances delta1 (energy) and delta2 (energy squared). In addition to all parent conditions, require

    xi <= sqrt[delta1/(2(a2+1/t_*))],
    xi <= sqrt[delta2/(2(C2_N+1/t_*^2))].          (3)

This has a strictly positive finite solution with dimensionless ratios even if a2=0. It guarantees E1<=delta1 and E2<=delta2 uniformly in t. State comparison and finite-window target accuracy continue to follow from the parent's conditions at the new actual duration. A bound on the full installed positive-block sum is

    B_N = h+R_s+(3b-2)M_E+q(3N-2)M_E+J1+qN J2. (4)

Here bus onsites/positive edges cost bM_E+2(b-1)M_E; source fields/ferromagnetic edges cost qNM_E+2q(N-1)M_E; the total weak positive V blocks cost at most J1; and all positive counterterms cost at most qNJ2. Equation (4) bounds ||K||, not thermodynamic work. It also charges scalar reserves. The incident cap remains J_*=R_s+7M_E+J1+J2. No favorable upper bound on the added duration or coefficient precision follows from (3).

For variance accuracy delta_var, one can select delta2<=delta_var/2 and delta1<=delta_var/(4B_N), with compatible units, before (3). This is not obtained from state error alone.

## 4. What is reduced and what remains expensive

The propagated code has dimension d(N+1)^q and its generator D is exactly the parent's displayed complete code operator, including every source sector and compensated self-energy. At fixed old plant q is fixed, so this dimension is polynomial in N; it can be enormous as a function of the old plant. There is no high-block propagation in C_xi. Computing/certifying the parent's complete Q/P gap and corrector constants still involves a potentially expensive finite search or complete-space bounds. This proposal does not solve that design cost or provide an implemented numerical propagation package.

Numerical approximation of C_xi must itself be an isometry if one uses the simple bound 2B_N^j zeta for an operator-norm evaluation error zeta. A physical preparation trace error e may cost B_N e or B_N^2 e in moments. Any changed physical generator has different moments; long-time calibration, release, spectral support and clock/energy identification remain separate obligations.

The controller source input still has the parent's T-dependent phases and remains supplied. Exact existence and an effective finite-precision target selection must retain the parent's eventual review qualification at zero target entries. No native preparation, permanent stopping, reset/reuse, laboratory energy observable or generic coupled-plant theorem is inferred.

## 5. Verification status and next decisive check

This is an analytic root derivation from the stated conditional parent, with no new scientific executable run. A separate check should recompute the cubic selection rule with off-code source counterterms, all reserve factors, both moment expansions and the resource quantifier order. A finite full-matrix example should compare J*K^2J with (1) and deliberately omit J*A2^2J or a reserve term to ensure the check distinguishes the equations. More check counts do not establish the all-parameter theorem. A defect must narrow the claim rather than be hidden by the parent's state error.

No canonical files, physical axioms or editable prompts were changed by this proposal.

---

## Immutable source body: exposed_review

# Independent recomputation of the joint-code moment proposal

Status: exposed, same-inherited-model mathematical recomputation. The exact root proposal and conditional bus arguments were read before this derivation. This is not a blind derivation, a different-model replication, a retained audit, or a physical energy/preparation theorem. All source identities and coverage are preserved separately.

## 1. Conclusion and premises

The proposed compressed moments, uniform-in-time bounds, load-based full norm allowance, and additional positive `xi` choice are correct under the stated bus hypotheses. No load-bearing defect was found. The quartic contribution from off-code counterterm action is essential; the exact finite check below detects its omission. The supplied reserve must remain in the second-moment cross term even though the comparator's scalar phase cancels from expectation values.

The precise mathematical result concerns the **same installed nominal static generator**

\[
 K=K_0+\xi V+\xi^2 A_2+R(\xi)I,
\]

and the original isometric code inclusion \(J\), including every old factor, bus vacuum, and every symmetric excitation sector of every source. Its algebraic premises are

\[
 K_0J=JF,\quad J^*J=I,\quad J^*VJ=0,\quad [F,D]=0,
\]

with all indicated generators Hermitian. In addition, let \(P_b\) project to bus vacuum, including *all* source states. The actual source-only counterterm preserves this space and

\[
 A_2P_b=P_bA_2P_b,\qquad P_bVP_b=0.                 \tag{1}
\]

These conditions hold for the parent's displayed source density counterterms and bus-creating port/source perturbations. Merely knowing \(J^*VJ=0\) would not suffice to remove a cubic term after an off-code source excursion; the stronger bus-vacuum selection rule (1) is used.

Define

\[
 U_c(t)=e^{-it(F+\xi^2D)},\quad
 C_\xi(t)=e^{-itR(\xi)}JU_c(t).
\]

Then \(C_\xi(t)^*C_\xi(t)=I\) and \(C_\xi(0)=J\) exactly. It propagates joint old/source states and retains their correlations. All operator statements below tensor with arbitrary passive reference identities without changing their bounds.

The compressed-moment lemma itself does not need a spectral gap. The parent's complete Q/P separation and corrector are required to make this comparator a state approximation for its desired gate on \(0\leq t\leq T+w\), \(T=t_*/\xi^2\). This review does not weaken or replace those parent premises. The root's subsequently supplied qualified source acceptance was read as provenance and scope information, not used as a substitute for the following recomputation.

## 2. Exact compression of K and K squared

Put

\[
 A_c=J^*A_2J,\quad V_c^{(2)}=J^*V^2J,\quad
 S_c=J^*A_2^2J,\quad F_R=F+R(\xi)I.
\]

Because \(K_0\) is Hermitian, invariance implies \(J^*K_0=FJ^*\), as an identity on the complete physical space. Therefore

\[
 \boxed{J^*KJ=F_R+\xi^2A_c,}                       \tag{2}
\]

and full expansion gives

\[
\begin{split}
 J^*K^2J={}&F_R^2+\xi J^*\{K_0+RI,V\}J
       +\xi^2\big[V_c^{(2)}+\{F_R,A_c\}\big]\\
       &+\xi^3J^*\{V,A_2\}J+\xi^4S_c.
\end{split}
\]

The linear term vanishes since its two summands are \(F_RJ^*VJ\) and \(J^*VJF_R\). For the cubic term, \(A_2J\) is in bus vacuum even if it leaves source symmetry; applying \(V\) takes it to a one-bus-excitation space orthogonal to \(J\). Thus \(J^*VA_2J=0\); Hermitian adjunction gives \(J^*A_2VJ=0\). Consequently

\[
 \boxed{J^*K^2J=F_R^2+
 \xi^2\big[V_c^{(2)}+\{F_R,A_c\}\big]+\xi^4S_c.}  \tag{3}
\]

This confirms the root proposal including all reserve factors. In particular the anticommutator contains \(2R(\xi)A_c\). The normalized trace scalar of the full Hamiltonian is a separate ledger; no trace normalization or phase convention removes this term.

Let \(P=JJ^*\) and \(Q=I-P\). The exact identity

\[
 S_c=A_c^2+(QA_2J)^*(QA_2J)                       \tag{4}
\]

shows why replacing \(S_c\) by \(A_c^2\) is generally wrong. The omitted matrix is positive semidefinite. It can be nonzero while the counterterm preserves bus vacuum: the leakage in (4) can lie entirely in nonsymmetric source sectors. No invariance of source symmetry under \(A_2\) is needed or assumed.

The source ferromagnetic terms vanish on the initial code as full operators, together with their scalar/nonidentity pieces. Their absence from \(F\) is not an arbitrary scalar subtraction. Equation (3) also explains why source energies reached by \(A_2J\) do not supply an extra \(K_0A_2\) term after compression: the exact invariance identity already fixes that cross term. The off-code action is still paid by (4).

## 3. Uniform first, second, and variance comparison

Since \([F,D]=0\), \(U_c(t)\) commutes with \(F_R\) for every real \(t\). The actual scalar \(R(\xi)\) is constant in time for each installed device. From (2),

\[
 C_\xi(t)^*KC_\xi(t)-J^*KJ
    =\xi^2\big[U_c(t)^*A_cU_c(t)-A_c\big].        \tag{5}
\]

The \(F_R^2\) term in (3) is also invariant. Let \(v\geq\|V\|\), \(a_2\geq\|A_2\|\), and \(f_R\geq\|F\|+R(\xi)\). The reserve is nonnegative in this physical family. Using \(\|U^*XU-X\|\leq2\|X\|\),

\[
\begin{split}
 E_1(t)&:=\|C_\xi(t)^*KC_\xi(t)-J^*KJ\|
       \leq2\xi^2a_2,\\
 E_2(t)&:=\|C_\xi(t)^*K^2C_\xi(t)-J^*K^2J\|\\
       &\leq2\xi^2\big[v^2+2f_Ra_2\big]+2\xi^4a_2^2.           \tag{6}
\end{split}
\]

For clarity, the anticommutator has norm at most \(2f_Ra_2\); conjugation minus its initial value costs another factor two. The quartic term uses the **full** norm allowance \(a_2\), not merely \(\|A_c\|\).

For \(A_\xi(t)=e^{-itK}J\), exact static conservation gives \(A_\xi(t)^*K^jA_\xi(t)=J^*K^jJ\). Thus (6) compares the comparator with the conserved bare moments of the same generator. For any fixed code/reference density input, both means have magnitude at most \(B\) when \(B\geq\|K\|\). Its variance discrepancy therefore satisfies

\[
 |\operatorname{Var}_{C_\xi(t)}(K)
       -\operatorname{Var}_{J}(K)|
 \leq E_2(t)+2B E_1(t).                          \tag{7}
\]

Variance is a state-dependent nonlinear quantity; (7) is uniform over the allowed states, not a purported linear variance operator.

Equations (5)–(7) hold for **all real times**. This does not extend the parent's state-isometry approximation beyond \([0,T+w]\): agreement of two moments does not establish agreement of states. These bounds do not multiply the parent's ordinary state error by a growing energy norm. They instead cancel the exactly conserved leading code energy before estimating the remaining terms.

This cancellation explains the importance of retaining joint source dynamics. A free unchanged source product with a non-energy-commuting old gate need not conserve \(F\); it does not inherit (5) or (6). The initial product phases can depend on \(T\), because the operator estimates are uniform on the entire code and hence on every such input.

## 4. Full physical norm and reserve bounds from the actual loads

Use the parent's \(q=d(d-1)/2\) sources, common length \(N\), fixed bus size \(b=2(d-1)+4q\), and common base energy bound \(M_E\). The bus alone is a tree with \(b-1\) edges. A reserved bus exchange block has norm \(2|t_e|\). A source ferromagnetic block \(J_F(I-\mathrm{SWAP})\) has norm \(2J_F\). Each source field has norm \(\omega_l\leq M_E\). Hence the total base added-block allowances are

\[
 bM_E+2(b-1)M_E=(3b-2)M_E,
 \quad qNM_E+2q(N-1)M_E=q(3N-2)M_E.              \tag{8}
\]

The parent's actual weak reserve and positive-block load are

\[
 R_V=v_p\|B_p\|+\sum_l r_l,\qquad \ell_V=2R_V.
\]

Therefore all weak positive blocks together have norm sum \(\xi\ell_V\leq J_1\), whereas their scalar reserve alone satisfies \(\xi R_V\leq J_1/2\). This factor two is required.

For source counterterm coefficients \(u_l,v_l\), the complete positive onsite/edge block norms are \(\xi^2|u_l|\) and \(\xi^2|v_l|\). With \(\ell_2=\max_l(|u_l|+2|v_l|)\),

\[
\begin{split}
 \sum_l\big[N|u_l|+(N-1)|v_l|\big]
    &\leq qN\ell_2,\\
 \xi^2R_{A_2}&\leq\xi^2qN\ell_2\leq qNJ_2.       \tag{9}
\end{split}
\]

Here the scalar reserve uses only negative parts and is no larger than the first sum; the total reserved counterterm block norm sum is bounded by the same \(qNJ_2\). No projection to a low-excitation source sector was used.

Since \(\|H\|\leq h\), \(R_s\geq h\), and \(R_{\rm bus}\leq(b-1)M_E\), equations (8)–(9) prove

\[
\begin{split}
 R(\xi)&\leq R_s+(b-1)M_E+J_1/2+qNJ_2,\\
 \|F\|&\leq h+qNM_E,\\
 \overline F_N&=h+qNM_E+R_s+(b-1)M_E+J_1/2+qNJ_2,\\
 \boxed{B_N}&=h+R_s+(3b-2)M_E+q(3N-2)M_E+J_1+qNJ_2
              \ \geq\|K\|.                     \tag{10}
\end{split}
\]

Thus the root's displayed `Fbar_N` and `B_N` are valid. The fixed old \(H\) need not have a positive decomposition into its own channels: its norm is paid by \(h\), and the added scalar by \(R_s\). They are not quietly combined into an assumption of separately positive old terms.

The same installed-block accounting retains the parent's incident bound

\[
 J_*=R_s+7M_E+J_1+J_2,
 \qquad J_1=J_2=1/t_*.
\]

This is a cap on **added incident norms**, including positive reserves. It is not an accuracy-independent bound on the total norm \(B_N\), total energy, preparation work, or norm-time action. The total bound in (10) can grow with \(N\).

## 5. Joint choice of state and moment accuracy

Fix an instance in this order: target (or qualified rational target), state accuracy and source size \(N\); finite spectral choices and full separation; routed calibration, amplitudes and full counterterms; corrector/load bounds. At that point \(v,a_2,C_{\rm corr},\ell_V,\ell_2\) are finite and independent of the subsequent \(\xi\) and source phases. They may be enormous and \(N\)-dependent.

Set

\[
 C_{2,N}=v^2+2\overline F_N a_2+a_2^2.
\]

For \(0<\xi\leq1\), equations (6) and (10) give \(E_2\leq2\xi^2C_{2,N}\). In addition to the parent's five positive upper bounds, impose

\[
 \xi\leq\sqrt{\frac{\delta_1}{2(a_2+1/t_*)}},
 \qquad
 \xi\leq\sqrt{\frac{\delta_2}{2(C_{2,N}+1/t_*^2)}}.              \tag{11}
\]

Here \(\delta_1>0\) has energy units and \(\delta_2>0\) has energy-squared units. All ratios in (11) are dimensionless. The added denominators are mathematical positive slack, not newly installed physical terms. They handle \(a_2=0\) or vanishing quadratic coefficients without a zero denominator. A strictly positive \(\xi\) satisfying the finite collection exists and gives \(E_1\leq\delta_1\), \(E_2\leq\delta_2\) at all times. For variance tolerance \(\delta_{\rm var}>0\), choosing \(\delta_2\leq\delta_{\rm var}/2\) and \(\delta_1\leq\delta_{\rm var}/(4B_N)\) proves (7) within \(\delta_{\rm var}\). Separate first/second tolerances can be enforced simultaneously by taking the smaller budgets.

For a family with growing \(N\), simply saying \(\xi\to0\) would not be sufficient: the coefficients in (6) can grow. The explicit instance-dependent conditions (11) pay that growth. With positive computable input tolerances and certified coefficient bounds, a positive rational \(\xi\) can be found strictly below all these positive computable upper bounds. No bound on search time, required precision, or resulting duration follows.

After decreasing \(\xi\), set the **new actual** \(T=t_*/\xi^2\). The original error estimates continue to hold because

\[
\begin{split}
 \text{bare-code error}&\leq\xi C_{\rm corr},\quad0\leq t\leq T+w,\\
 \xi^2(T+s)B_L/\sqrt N
     &=(t_*+\xi^2s)B_L/\sqrt N\leq(t_*+w)B_L/\sqrt N,\\
 \text{window error}&\leq\xi^2w\|L\|/t_*.
\end{split}                                                     \tag{12}
\]

The first and third bounds improve when \(\xi\) is reduced, while the fixed upper bound on the second is unchanged. Both incident loads also decrease. The original finite-time corrector remains applicable at the longer actual duration because its derivation already substitutes \(T=t_*/\xi^2\): the cubic residual integrated to that duration is order \(\xi\), not an unpriced fixed-time estimate.

For each active source the actual input phase must be recomputed as

\[
 \phi_l=\arg L_{ab}-\arg\kappa_{ab}+\omega_lT,
\]

or by the parent's qualified computable unit-ratio formulation. The target comparator phase must likewise be recomputed as

\[
 \chi(T+s)=R(\xi)(T+s)+c_{\rm old}\xi^2(T+s)+\theta_0.          \tag{13}
\]

The free source factors and both literal old-H flows use the same new physical time. Hardware coefficients, calibration, \(D\), and the finite corrector constants do not depend on these final source phases. Holding an earlier \(T\) or phase while shrinking \(\xi\) would not establish the parent target contract.

Longer runtime tightens physical integrated calibration and timing requirements; these must be supplied again at the new duration. A promise previously made only through a shorter duration cannot simply be reused. The nominal mathematical compatibility in (12) is not a native long-time calibration/preparation supplier.

## 6. Scope, effectiveness, and remaining costs

The comparator propagates the code of dimension \(d(N+1)^q\). There is no high-block propagator in its definition. For fixed old plant, \(q\) is fixed and this dimension is polynomial in \(N\); no polynomial dependence on old-qubit count, runtime, precision or gap-search cost is implied. Certifying full separation and obtaining corrector bounds can still require expensive complete-space calculations. The present proof does not replace those tasks by one-excitation checks.

The parent construction requires the complete old simple spectrum, distinct positive gaps, nonzero off-diagonal energy-basis entries of the designated local port operator, computable spectral data and vacant routed geometry. The original generic Lie-certificate domain is not thereby covered. The algebraic moment lemma is reusable under its own premises, but it does not construct a gate for plants outside the parent's domain.

Exact-target existence and effective target compilation remain distinct. The parent's qualified acceptance does not accept a uniform zero-support/arg decision for arbitrary computable \(L\). For an effective approximate-output version, use its separately attributed rational Hermitian \(M\), with \(\|M-L\|\leq\epsilon/32\), rational support, and working tolerance \(\epsilon/2\). The extra target trace cost is at most \(2\|M-L\|\), so the qualified parent budget remains at most \(9\epsilon/16\). Apply (2)–(13) to the **actual** device designed for \(M\), including its actual \(A_2,V,D,R\); do not identify its generator with the hypothetical exact-L device. Further reducing \(\xi\) preserves that state budget and independently pays the requested moment tolerances.

The source size only needs to exceed a certified sufficient bound. Certified rational upper rounding with bounded additive excess avoids treating the exact ceiling of an arbitrary computable real as a universally computable operation. Nominal phases for nonzero rational support use unit ratios; zero entries have zero source coupling and a specified arbitrary phase. Neither choice adds a moment error because the estimates are uniform on the whole code.

A numerical isometry within norm \(\zeta\) of \(C_\xi(t)\) adds at most \(2B_N^j\zeta\) to the \(j\)-th moment bound, \(j=1,2\). A general rounded matrix needs a normalization/norm allowance before invoking that estimate. At long times, coefficient error must also be propagated through the actual code evolution rather than declared a harmless phase. No implemented numerical propagation or coefficient-oracle complexity theorem is supplied here.

For actual preparation trace-norm error \(e\), first- and second-moment errors can cost \(B_Ne\) and \(B_N^2e\). The state-level preparation tolerance alone therefore does not prove moment accuracy. The supplied initial source phases, exact unconditional old/reference marginal, release, continued isolation, and full-generator calibration remain separate conditions. A different physical generator or release state has different conserved moment constants. An integrated perturbation bound does not itself imply a pointwise incident-strength cap. Laboratory measured-energy identification, native source formation, thermodynamic work, permanent stopping, readable records and reset/reuse remain unresolved.

## 7. Exact finite discriminator and verification limits

One independent exact algebra fixture was executed. It uses one old qubit, one bus qubit and an \(N=3\) source, hence full dimension 32 and code dimension 8. Bit-transition assembly constructs the complete operators; no author/reviewer scientific code was imported. It keeps every source excitation sector and a literal old scalar. The counterterm is

\[
 A_2=-\frac27N_s+\frac49(n_1n_2+n_2n_3),
\]

which preserves bus vacuum while failing to preserve source symmetry. The actual fixture reserve is \(11/5+(19/15)\xi+(6/7)\xi^2\). It is paid separately from the full source/old operators.

Exact symbolic multiplication verified (2)–(3) as polynomial matrix identities, not only at sampled \(\xi\). It found

\[
 S_c-A_c^2=\operatorname{diag}(0,0,32/729,0,0,0,32/729,0).
\]

At \(\xi=1/5\), deleting that quartic contribution gives a matrix-entry discrepancy \(32/455625\). Omitting only the reserve cross term gives an independent entry discrepancy \(-5224/91875\). Both deliberately wrong formulas are detected.

An inadmissible counterterm with an added bus-X term makes the cubic compression nonzero, exhibiting the importance of (1). An old-only swap not commuting with \(F\) changes the leading mean by 2 even at \(\xi=0\), exhibiting the importance of \([F,D]=0\). These are premise discriminators, not counterexamples within the stated theorem.

A nontrivial exact unitary swapping a degenerate joint-code pair commutes with \(F\). The fixture checks the first/second moment inequalities using the stronger Frobenius-norm test, and checks a variance discrepancy exactly: it is \(3/625\), below the displayed allowance. This unitary can be generated within an equal-F block. The fixture does **not** claim that its arbitrary discriminating counterterm and code unitary are the calibrated parent's particular \(D\) and hardware. It tests the compressed-moment lemma, not the parent's full routed realization or state-corrector estimate.

The run used Python 3.13.5 and SymPy 1.14.0, exact rational/Gaussian-rational arithmetic and \(\sqrt3\), with no floating tolerance. It exited 0 in 1.1781459576450288 seconds; stderr is empty. Main executed-source SHA-256 is `e6b59e5008c14ef15412f79e7a8bfb19526bad3d5d6a40626c7b510109b543fa`. Full source-at-launch, launcher bytes, source manifest, actual child argv/cwd, timestamps, exit and complete streams survive. The launcher-argv annotation needs the explicit interpreter-flag clarification in `SOURCE_EXPOSURE.md`; no receipt was rewritten and no successful science rerun was used to improve provenance.

These finite discriminators support the checked algebra and expose plausible omissions. They do not prove the all-parameter theorem by enumeration, establish the full routed-bus gap, or validate a physical energy supplier. The all-time inequalities follow from the preceding analytic identities. The new moment proposal can be accepted as this conditional mathematical corollary if its source, target-effectiveness and physical-supplier qualifications remain attached; formal retained status remains outside this review.


Direct mathematical parent: [Strongly regular bus bounded theorem](STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md).
