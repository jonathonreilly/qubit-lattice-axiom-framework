---
title: Restricted static ferromagnetic spin source with bounded added incident strength
claim_id: restricted_static_ferromagnetic_spin_source_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied coherent spin source and exact resonance implement a single-qubit target with bounded added incident sums and explicit sufficient resource powers
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: one controlled old qubit with genuinely decoupled spectators; supplied preparation, geometry, timing, isolation and calibration; no generic coupled-plant realization
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
status: proposed_retained
upstream_dependencies: []
runner: scripts/restricted_static_ferromagnetic_spin_source_2026_10_15.py
next_trace_action: bind actual final canonical review, execute scoped source-integrity integration, then regular publication and independent retained audit
---

Claim type: bounded_theorem

For one controlled old qubit with genuinely decoupled spectators, a supplied coherent ferromagnetic source on an added nearest-neighbor chain implements the specified single-qubit unitary with the full old/source/reference output retained. A single accuracy-independent cap bounds the added incident block norms. The particular source-size and coupling choices give sufficient upper powers N=O(epsilon^-2), T=O(epsilon^-5), full norm O(epsilon^-2), and norm action O(epsilon^-7). These are conditional construction bounds, not resource lower bounds, optimality, generic coupled-plant controllability or native preparation.

The primary theorem is author sections 2–6, qualified by root's final decision and the exposed reconciliation. The independently frozen derivation checks this restricted construction with its own constants and finite implementation. Author section 8 remains a separate conditional finite-matrix implication; sections 9–10 remain architecture proposals and a diagnostic of sufficient clock estimates. The exact author, independent and exposed bodies follow once each without alteration. Their historical status language and proposed extensions are not new acceptance claims.

Qualified source acceptance is SHA256 `32d142a282e1347449f9de98f5749c03f9d9a78dccca4c86608f472401ed7aa2`, recorded at 2026-10-16T00:19:01.165638+00:00. Its controlling final qualifications have SHA256 `dcab7a72c287fe9cd06b2de4997d35051aa67e425be9d6c8703055edae44ba11`. The filename's date identifies this campaign's publication proposal; it does not backdate that acceptance. Source acceptance does not accept this wrapper, canonical integration, publication or retained status. The unexecuted integrity primary checks source/recovery and receipt metadata only; it cannot certify mathematics, general reachability or physics.

## 1. Restricted plant and supplied physical interface

The complete literal old Hamiltonian is

```
H = h_c I + omega n_p + H_rest,      n=(I-Z)/2,
```

where H_rest acts only on old factors genuinely disjoint from controlled qubit p. Every old input and arbitrary correlated passive reference are allowed. Old spectator evolution remains part of H throughout. The target is W_p tensor I_rest with a supplied decomposition

```
W_p = exp(i theta0) exp[-i theta G_phi0],
G_phi0 = r cos(phi0)X_p + r sin(phi0)Y_p + z Z_p,
r>=0, r^2+z^2=1, 0<theta<=pi.
```

The theta=0 case is separately free old evolution with its matching comparison phase. A fixed theta=pi decomposition has exp(-i theta0)W_p=-I and retains that minus sign. It cannot use the same free-old coherent comparator. An explicit reparameterization of theta0 changes the comparison phase; alternatively the actual rotation realizes the fixed decomposition. The main construction includes theta=pi.

Supply fixed J_F>0, time unit t0>0, finite observation window w>=0, exact graph access, and an available exterior neighbor/ray from p. Append source sites a_1,...,a_N with only p-a_1 and a_j-a_(j+1), giving N new sites, N new edges, new degree at most two and exactly one old/new adjacency. No old site moves, is reset or becomes a new source site. With spectators the available ray is an explicit premise. All unlisted interactions must actually be isolated or included in the full-space defect budget.

Source product preparation with the selected complex phase, coefficient access, timing and isolation are supplied. The fixed literal H, target and geometry do not change with accuracy. A static installed runtime Hamiltonian is constructed; no physical preparation supplier, switch, clock or permanent stopping mechanism is inferred. The self-contained restricted proof below uses finite spin addition, swap comparison and Duhamel identities proved in the preserved bodies. Earlier compiler/mediator/clock references in the unaccepted architecture discussion are historical context, not mathematical parent edges of this restricted theorem. PARENT_BINDING therefore has no external mathematical parents.

## 2. Literal positive blocks and scalar accounting

With sigma_+=|1><0|=(X-iY)/2 and sigma_-=|0><1|, define

```
N_A = sum_j n_(a_j),
L_F = J_F sum_(j=1)^(N-1)(I-SWAP_(a_j,a_(j+1))),
V = sigma_+^p sigma_-^(a_1)+sigma_-^p sigma_+^(a_1),
A = 2rV+zZ_p,              ||V||=1.
```

Choose q>0 and r_omega=max(0,-omega). The nominal full generator is

```
K = H + R_s I + L_F + sum_j[omega n_(a_j)+r_omega I_(a_j)]
      + 2qr(V+I_(p,a_1)) + q(zZ_p+|z|I_p).
```

Each added block is positive. Their norms are |omega| for a source onsite block, 2J_F for a ferromagnetic edge, 4qr for the port edge, 2q|z| for the old onsite rotation, and R_s for the reserve installed onsite at p. If whole-generator positivity is desired, supply R_s>=||H||. If it is not desired, R_s=0 is allowed without that whole-generator conclusion. Every old term remains; there is no -H compensation.

Two different scalar ledgers must be retained:

```
R = R_s+N r_omega+2qr+q|z|,
s_K = s_H+R_s+N|omega|/2+(N-1)J_F/2+2qr+q|z|.
```

R is the exact scalar extracted when writing K=R I+F+L_F+qA, F=H+omega N_A. s_K is the normalized full trace. The scalar in the ferromagnetic edge decomposition is physically installed; L_F as a whole annihilates the symmetric comparison state. Thus it contributes to literal norm/action accounting without an extra L_F phase on that state. H's scalar already appears in the full H flows. Negative omega requires the N r_omega reserve; the growing total reserve is not removed by a local incident cap.

## 3. Full-space gap, resonance and bare-input reduction

Let P_sym be the source symmetric projector, Q_sym its complement. The accepted all-sector bound, for N>=2, is

```
L_F >= gamma_N Q_sym,        gamma_N=2J_F/N^2.
```

The proof uses the unitary-product telescoping identity to compare every transposition with its adjacent path:

```
I-s_ij <= 4(j-i) sum_(k=i)^(j-1)(I-s_k).
```

Summing gives edge coefficient 2N k(N-k)<=N^3/2. The complete-graph sum is C_N=N(N+2)I/4-S^2; finite addition of N spin-1/2 factors identifies its kernel as the symmetric subspace and gives C_N>=N Q_sym. These two finite operator inequalities yield the displayed gap on the whole source Hilbert space. A one-excitation gap alone would not suffice for the coherent product input.

The restricted plant gives the exact identities [F,L_F]=[F,A]=0. Port exchange conserves n_p+N_A; source swaps conserve N_A, and H_rest is genuinely disjoint. Consequently

```
exp(-itK)=exp(-itR) exp(-itF) exp[-it(L_F+qA)].
```

This holds for either sign of omega with no rotating-wave or large-field approximation. A generic coupling to p destroys the stated commutator premise; the result does not supply a replacement resonance argument.

Set P=I_old tensor P_sym, Q=I-P, and let R_F be L_F inverse on Q extended by zero on P. Then ||R_F||<=1/gamma_N. With A_P=PAP restricted to Ran(P), X=R_F QAP and Z=P-qX,

```
(L_F+qA)Z-ZqA_P = q^2(XA_P-AX).
```

Integrating this exact residual and retaining both differences between bare and corrected endpoints gives

```
||exp[-it(L_F+qA)]P-P exp(-itqA_P)||
    <= 6q/gamma_N+18tq^2/gamma_N.
```

The input remains the supplied bare symmetric state, not a prepared dressed state. The independent proof derives the closely related integration-by-parts estimate 2qa(1+qat)/gamma_N with the exact a=||A||=sqrt(4r^2+z^2)<=2. Its separate parameter choices are retained in its body. This wrapper uses the author's v=3 constants and accuracy allocation throughout; it does not splice the two recipes.

## 4. Complete moving source output and actual-time target

Prepare the supplied source

```
|Alpha_phi> = [(|0>+exp(i phi)|1>)/sqrt(2)]^tensor N,
|Alpha_phi(t)> = exp(-it omega N_A)|Alpha_phi>.
```

Symmetry gives P_sym sigma_±^(a_1) P_sym=S_±/N. Its mean old generator is G_phi, and the complete isometry residual is exactly r/sqrt(N):

```
||(A_P-G_phi)(|Alpha_phi> tensor I_old)||=r/sqrt(N).
```

This is a full source/output-vector bound, not only a reduced old channel calculation. Duhamel bounds the collective evolution error by tq/sqrt(N). Select T=theta/q, then phi=phi0+omega T modulo 2pi. Exact conjugation establishes

```
exp(-iHT) exp(-i theta G_phi)
    = exp(-i theta0) W exp(-iHT).
```

At every t=T+s, 0<=s<=w, compare the full output isometry with

```
V_s = exp[-i(R(T+s)+theta0)] |Alpha_phi(T+s)>
          tensor exp(-isH) W exp(-iTH).
```

The source factor equals |Alpha_(phi0-omega s)> in this convention and generally moves across the window. Every old/source factor and passive reference is retained. The old drift acts before W and afterward in the displayed order. The complete isometry error is at most

```
E_iso <= (6+18q(T+w))q/gamma_N + q(T+w)/sqrt(N) + qw.
```

The last term charges the continuing target rotation during the finite observation window. There is no final halt, decoupling, source reset, source reuse or discard. The global phase is tracked even though conjugation of a density operator removes it; coherent equality cannot silently change it.

## 5. Solved accuracy, resources and actual error budget

For 0<epsilon<=1 write A_theta=1+theta and take the author's exact-real choices

```
N = max(2,ceil[(8A_theta/epsilon)^2]),
gamma_N = 2J_F/N^2,
q = min{epsilon/[8(t0+w)], epsilon gamma_N/[8(6+18A_theta)]},
T = theta/q,              tau=T+w.
```

All quantities are finite and q>0. Since q(T+w)<=A_theta, the three terms in E_iso are each at most epsilon/8. The uniform complete isometry bound is therefore 3epsilon/8, and the ideal complete unhalved trace bound is 3epsilon/4. Require the actual initial complete state to be within epsilon/8 unhalved trace distance of the source product tensored with its exact unconditional old/reference marginal. Also require one shared full-generator allowance

```
integral_0^tau ||K_actual(t)-K|| dt <= epsilon/16.
```

Full-space Duhamel and unitary invariance then give total complete unhalved trace error at most 3epsilon/4+epsilon/8+2(epsilon/16)=epsilon. Timing, scalar, coefficient and omitted-edge errors share the actual budgets; a switch or fixed-target timing discrepancy gets no separate free allowance.

With fixed supplied data, these specified choices give N=O(epsilon^-2) and T=O(epsilon^-5). The literal nominal full norm obeys

```
||K|| <= ||H||+R_s+N|omega|+2J_F(N-1)+6q = O(epsilon^-2),
tau ||K|| = O(epsilon^-7).
```

Since q<=1/t0, added incident sums are at most R_s+6/t0 at p, |omega|+4J_F at an interior source site, and |omega|+2J_F+4/t0 at a_1. The single fixed cap J_*=R_s+|omega|+4J_F+6/t0 therefore suffices for this entire accuracy family. It is not a constant total norm, total reserve, runtime or precision bound. The literal graph includes every local block used in these sums.

For the displayed 8N+8 physical Pauli/identity coefficient slots, a sufficient common coefficient error is epsilon/[16 tau(8N+8)] when that is the entire defect allocation. Its inverse scales as O(epsilon^-8) for this recipe. Other faults must share the allowance. An integrated norm defect alone does not preserve positivity of perturbed blocks: enforce a positive parameterization or pay the separately stated local reserve margins and their scalar/action costs. Norm action is not identified with thermodynamic work or a native physical energy observable.

## 6. Separately attributed finite-precision refinement and degeneracies

The exact-real ceiling and minimum above prove existence and sufficient resource powers. They are not by themselves a total finite-precision algorithm for arbitrary real inputs: exact ceiling at a possible integer boundary cannot generally be decided from computable-real approximations. The exposed comparison supplies an effective refinement under additional certified computable-data and strict-positive-bound premises.

For b=[8(1+theta)/epsilon]^2, obtain a rational upper enclosure u with b<=u<=b+1/2, and set N=max(2,ceil u), so N<b+3/2. With this actual N, let m be the positive minimum in the q formula. Refine certified rational bounds 0<L<=m<=U<=2L and choose q=L. Then m/2<=q<=m. Every accuracy inequality survives, and N and 1/q stay within the constants needed for the stated upper powers. Arbitrarily oversized N or arbitrarily tiny q would not preserve those upper claims.

Compute actual T=theta/q and the complex initial phase exp[i(phi0+omega theta/q)] from the selected values. This does not require a discontinuous decision about a chosen modulo-2pi representative. Finite timing or state approximation must satisfy the already stated physical budgets. Oracle cost, native synthesis of these data and source preparation remain unpriced.

For r=0, z=±1, the port vanishes and the exposed comparison gives a separate improvement: N=1 suffices, the endpoint rotation is exact, and the continuing-window error is 2|sin(qs/2)|<=qw. Its T=O(epsilon^-1) choice for w>0 and fixed-q exact endpoint for w=0 are special-case sufficient bounds, not general optimality. They preserve the theta=pi sign for the fixed supplied decomposition. The theta=0 free-old shortcut uses its matching theta0 phase and does not divide by a vanishing rotation angle.

## 7. Separate conditional lemma and unaccepted architectures

Author section 8 proves only the following finite-matrix implication under all its stated hypotheses. For K(xi)=K0+xi V+xi^2 A2+R(xi)I, supply an isometry J with K0J=JF, F=H+H_C, vanishing first-order code block, full complement/code spectral separation and its spectral data. Supply Hermitian D commuting with F and correctors Z1,Z2 solving

```
K0 Z1-Z1 F=-VJ,
K0 Z2-Z2 F=JD-VZ1-A2J.
```

The displayed blockwise inverse formula and D's resonant diagonal compatibility are required, not optional assumptions inferred from a first-order code. With Z=J+xi Z1+xi^2 Z2, the exact residual is xi^3 R3+xi^4 R4, where R3=VZ2+A2Z1-Z1D and R4=A2Z2-Z2D. Bare endpoints give the explicit finite error including 2xi||Z1||+2xi^2||Z2|| and time times residual norms. At T=t_*/xi^2 this can be made small by choosing xi using the full supplied constants.

Its additional source fluctuation bound B/sqrt(N), phase-independent hardware and bounds, compatible complete old target logarithm, actual-time phases, and fixed base/local incident bounds are all separate premises. Choosing N and then xi under those premises is not a realization of a bus satisfying them, a favorable general runtime power or a theorem for arbitrary coupled H. The restricted theorem above does not require this second-order lemma.

Sections 9–10 are retained as historical source text: a proposed bus with unresolved full-spectrum/self-energy/calibration obligations and a diagnostic of sufficient tape/clock estimates. They are not accepted general realizations. This package does not independently validate their cited parent clock proofs. No new strongly regular bus, routed-bus or correlated-energy candidate is a dependency or was inspected. The restricted resonance limitation and unresolved architecture obligations are not impossibility results about other mechanisms.

## 8. Evidence, independence and integration boundary

The independently frozen derivation predates its first author-proof exposure. The exposed comparison is explicitly later. Both use the selected model and shared architecture, converge on the same swap/Casimir gap proof, and use closely related corrector/integration-by-parts reductions. These are not two disjoint proofs or different-model-family replication. Their finite implementations differ: author Pauli Kronecker matrices and checker computational-basis transitions.

Author evidence records 12 finite cases, 36 full-isometry observations, an empty failure list and actual exit 0. Its captured source, launcher, launch/result files and full streams remain exact. Independent evidence reports 18 finite predicates and three detected deliberate defects. Its original launch file lacks cwd and process exit. The exposed manifest retrospectively transcribes the actual command, cwd, session 27634 and tool exit 0; it explicitly lacks a resolved interpreter and exact exit timestamp. The original incomplete launch record is preserved, not repaired into a fictitious contemporaneous receipt. Neither program instantiates the enormous small-epsilon resource recipe, proves the all-parameter inequalities or tests native hardware. No scientific program is rerun in this packaging.

BODY_MAP identifies the three complete byte intervals; SOURCE_MANIFEST and CHECK_RECEIPTS preserve exact selected recovery and the different evidence schemas. Original freezes/coverage are retained, with content deduplicated by hash. Their historical instruction and upstream-source references are not recursively copied. The controlling final qualifications explicitly correct the preliminary scalar shortcut; both texts remain recoverable with their chronology intact.

The frozen-draft review is captured separately from the required final canonical review and actual integration outcomes. The raw-draft review and final canonical review must link identical body names/sizes/hashes while separately binding their possibly different offsets. Actual local base and frozen-draft review are bound separately; final canonical review, primary/cache/check outputs, publication and retained audit remain distinct gates. The proposed primary checks exact bytes and actual captured metadata, emits only metadata assertion counts, and fails while its base/review binding is null. No metadata PASS count is a physics claim.


---

## Immutable source body: author_restricted_body

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# A bounded-strength weak-coupling route, with a complete one-qubit test case

Status: original source proposal, author-checked only. This is not an independent check, accepted result, retained audit, native state supplier, or proof of the full arbitrary-plant target. The complete theorem below is restricted to one controlled old qubit with a single Bohr frequency (and arbitrary decoupled old spectators). The final sections expose the equations still needed for the general coupled plant. A restricted construction is a discriminator for a mechanism; it does not replace the task's general compiler contract.

The source boundary is the composition at W commit `9ca474a32b3a4799d2d14cfee7580d77750422b4`, canonical SHA256 `baea95d22b229fad3c0aa166bff5608f9edfe7ea973ff0252fbc5cd9b1389007`. The frozen main and instruction identities supplied by the root are `bbada1fe09b2d10d610560864d86b68c24a59713` and `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. SOURCE_COVERAGE.md records exact read scope. No new root candidate or other worker's derivation has been consulted before freezing this proposal.

## 1. Task and mechanism

The requested general target, for a fixed finite plant and target W, is a family K_epsilon of static ordinary nearest-neighbor qubit Hamiltonians, with every literal old term in H physically present and one accessible old/new adjacency. At its own actual returned duration T and for all 0<=s<=w, the complete output must approximate a stated controller vector tensored with

    exp(-isH) W exp(-iTH),

including an explicit scalar phase, uniformly over arbitrary old/reference inputs. All added local blocks, counterterms and positive reserves must obey one incident-load cap J_* independent of epsilon. Added sites and runtime may grow. Supplied initialization, coefficients and calibration do not become native physical suppliers.

The proposed change of mechanism is to use a large, low-energy ferromagnetic spin register as a coherent source and make its one physical port coupling weak. The source's collective signal remains finite after projection, while its fluctuation on a spin-coherent product state is O(N^-1/2). A shrinking ferromagnetic gap is paid by making the port coupling smaller, rather than increasing any edge penalty. In the exactly resonant one-qubit test case, useful rotation time is O(q^-1), so leakage error is O(q/gamma_N), not O(q^2 T) with an independently faster-growing compiler duration. The full accuracy inequalities can then be solved.

This is different from rescaling H. The old generator has exactly its original coefficient, and a uniform source field at the same frequency keeps the old/source exchange resonant. The output is at the actual physical time T; only added couplings are weakened.

## 2. Restricted theorem: hypotheses, geometry and installed terms

Fix physical time unit t0>0, ferromagnetic coefficient J_F>0, window w>=0 and literal old qubit Hamiltonian

    H = h_c I + omega n_p,   n_p=(I-Z_p)/2,

with arbitrary real h_c, omega. Arbitrary additional old factors may be retained provided H=H_rest+omega n_p with H_rest acting on those factors alone, and W=W_p tensor I_rest. The proof uses this actual decoupling condition; an interaction between p and the rest is not covered. Every old/reference input, including entangled inputs, is allowed.

Supply a target decomposition

    W = exp(i theta0) exp[-i theta (r cos(phi0) X_p
                                   + r sin(phi0) Y_p + z Z_p)],
    0<theta<=pi,  r>=0,  r^2+z^2=1.

This is a fixed target datum. The scalar case theta=0 has the exact free-old solution, with comparison phase theta0 and no source; it is handled separately and is never inserted into a division by T. A pure Z target r=0 is permitted by the formulas below.

The occupied old set has an accessible exterior neighbor of p, and an unoccupied exterior ray extending from it. Append N qubits a_1,...,a_N on that ray, with only edges p-a_1 and a_j-a_(j+1). Existing sites are not moved, vacated, reset or identified with new ones. For the single-qubit plant an empty ray is automatic in the admitted infinite lattice; with spectators it is an explicit geometry condition. The added graph has N new sites, N new edges, new degree at most two, and exactly one old/new adjacency. All unlisted interactions are actually isolated or charged in the full-space calibration bound.

Let sigma_+=|1><0|=(X-iY)/2, sigma_-=|0><1|=(X+iY)/2, and

    N_A = sum_j n_(a_j),
    L_F = J_F sum_(j=1)^(N-1) (I-SWAP_(a_j,a_(j+1))),
    V = sigma_+^p sigma_-^(a_1) + sigma_-^p sigma_+^(a_1),
    A = 2r V + z Z_p.

Thus ||V||=1, ||A||<=2r+|z|<=3. Fix R_s>=||H|| if whole-generator positivity is wanted; it is an explicitly installed scalar onsite on p. If that additional positivity is not required, R_s=0 is allowed. Put r_omega=max(0,-omega). For a positive q selected below, install

    K = H + R_s I
        + L_F + sum_j [omega n_(a_j)+r_omega I_(a_j)]
        + 2qr (V+I_(p,a_1))
        + q(z Z_p+|z|I_p).                              (1)

Every added block in (1) is positive. Source onsite blocks have norm |omega|; ferromagnetic edges have norm 2J_F; the port edge has norm 4qr; and the added nonscalar old onsite block has norm 2q|z|. R_s has norm R_s and is counted at p. Every literal old H term remains, and no -H compensation is present.

The actual extracted scalar reserve is

    R = R_s + N r_omega + 2qr + q|z|.                   (2)

It is not an upper bound substituted for a phase. The full normalized scalar of the installed generator is

    s_K = s_H + R_s + N|omega|/2
          + (N-1)J_F/2 + 2qr + q|z|,                 (3)

where s_H is the normalized trace of the complete literal H. The scalar (N-1)J_F/2 in the edge decomposition is physically present; its action cancels with the nonidentity part on the symmetric comparison state, because L_F annihilates that state. Equation (2) does not erase the other scalar terms in (3).

## 3. A full-space ferromagnetic gap bound

Let P_sym project the N source qubits onto their completely symmetric subspace and Q_sym=I-P_sym. The following bound is on the entire qubit Hilbert space:

    L_F >= gamma_N Q_sym,       gamma_N=2J_F/N^2,      N>=2.   (4)

Here is a self-contained comparison proof. Write s_k for the adjacent swap k,k+1 and s_ij for a general transposition. The latter is a product of 2(j-i)-1 adjacent swaps, each used at most twice. For any product U_1...U_L of unitaries,

    U_1...U_L-I = sum_r U_1...U_(r-1)(U_r-I).

Cauchy-Schwarz on this telescoping sum, together with
||(I-s)psi||^2=2<psi,(I-s)psi>, gives

    I-s_ij <= 4(j-i) sum_(k=i)^(j-1) (I-s_k)          (5)

as a quadratic-form inequality. The coefficient of an edge k after summing (5) over i<j is

    4 sum_(i<=k<j)(j-i) = 2N k(N-k) <= N^3/2.

Consequently

    C_N := sum_(i<j)(I-s_ij) <= (N^3/2) sum_k(I-s_k). (6)

For S=(1/2)sum_j (X_j,Y_j,Z_j), direct Pauli expansion gives

    C_N = [N(N+2)/4]I-S^2.

The N spin-1/2 tensor representation has total spins S=N/2,N/2-1,...; this follows by successively adding one spin-1/2. The S=N/2 representation is exactly the symmetric subspace. On its orthogonal complement the largest Casimir is (N/2-1)(N/2), so C_N>=N Q_sym. Combining with (6) proves (4). The common kernel is also directly seen to be symmetric: every positive adjacent-swap block must annihilate a zero vector, and adjacent swaps generate all permutations.

The proof does not use a one-excitation gap or presume that the source remains in one excitation sector. The prepared coherent state occupies many sectors. The bound is deliberately loose; no exact chain-gap formula is imported.

## 4. Exact resonance and a bare-input corrector

Set F=H+omega N_A, with identity factors understood. Then

    [F,L_F]=[F,A]=0.                                  (7)

Indeed the port exchange conserves n_p+N_A, every source swap conserves N_A, and Z_p commutes with both field parts. H_rest commutes because it is actually disjoint from p. Thus

    exp(-itK)=exp(-itR) exp(-itF) exp[-it(L_F+qA)].      (8)

No large-field approximation, rotating-wave approximation, rescaling of H or limit omega->0 is used.

Now put P=I_old tensor P_sym, Q=I-P, and define R_F as the inverse of L_F on Q, extended by zero on P. From (4), ||R_F||<=1/gamma_N. Regard P as the inclusion of its range. Define

    A_P=PAP restricted to Ran(P),
    X=R_F Q A P,       Z=P-qX.

Since L_F X=QAP and L_F P=0, direct multiplication yields the exact residual

    (L_F+qA) Z - Z q A_P = q^2 (X A_P-A X).            (9)

With v=3, ||X||<=v/gamma_N, ||A_P||<=v. Integrating (9) and retaining both corrected-versus-bare endpoints gives, for every t>=0,

    ||exp[-it(L_F+qA)]P-P exp(-itq A_P)||
      <= 2qv/gamma_N + 2tq^2 v^2/gamma_N
      <= 6q/gamma_N + 18tq^2/gamma_N.                 (10)

This is a finite bare-input estimate. It does not require preparation of Z or a dressed state and does not claim a full-space effective Hamiltonian. Its domain is every old state tensored with a symmetric source; the inverse and installed blocks remain full-space objects.

## 5. Complete controller output and collective fluctuation

For a phase phi define the normalized source product

    |alpha_phi>=(|0>+exp(i phi)|1>)/sqrt(2),
    |Alpha_phi>=|alpha_phi>^tensor N,
    |Alpha_phi(t)>=exp(-it omega N_A)|Alpha_phi>.

This state is supplied. It is not the output of an inferred cooling or preparation process. As operators on the symmetric code, permutation symmetry gives the exact projected boundary operators

    P_sym sigma_+^(a_1) P_sym = S_+/N,
    P_sym sigma_-^(a_1) P_sym = S_-/N,
    S_+=sum_j sigma_+^(a_j),  S_-=sum_j sigma_-^(a_j).

Hence the mean-field old generator is

    G_phi = r cos(phi) X_p+r sin(phi)Y_p+z Z_p,
    ||G_phi||=1.                                     (11)

The useful residual estimate is a bound on the entire source/output vector, not only on a reduced old channel:

    ||(A_P-G_phi)(|Alpha_phi> tensor I_old)||
       = r/sqrt(N) <= 1/sqrt(N).                     (12)

For phi=0, write e_j for the product with the jth |+> replaced by |->. The e_j are orthonormal, and

    (S_--N/2)|+>^N = (1/2)sum_j e_j,
    (S_+-N/2)|+>^N = -(1/2)sum_j e_j.

The source residual in A_P is therefore r/N times sum_j e_j tensored with sigma_+-sigma_-, whose old operator norm is one. This proves (12) at phi=0. A uniform Z rotation on source and old qubit gives the same norm for any phi. The z Z_p term is exact and contributes no residual. Duhamel then gives

    ||exp(-itq A_P)(|Alpha_phi> tensor I_old)
       - |Alpha_phi> tensor exp(-itqG_phi)|| <= tq/sqrt(N). (13)

Choose T=theta/q and phi=phi0+omega T, modulo 2pi, as supplied initial-state data. This choice is made after q and T are fixed; it does not change any coefficient magnitude or bound used to choose q. Exact conjugation gives

    exp(-iHT) exp(-i theta G_phi)
       = exp(-i theta0) W exp(-iHT).                  (14)

The order is important. At t=T+s, (8), (10), (13) and the additional rotation over s imply a complete-isometry comparison with

    V_s = exp[-i(R(T+s)+theta0)] |Alpha_phi(T+s)>
              tensor exp(-isH) W exp(-iTH),          (15)

and error

    E_iso <= (6+18q(T+w))q/gamma_N
             + q(T+w)/sqrt(N) + qw.                 (16)

Equation (15) retains every source qubit and its full phase. Its source factor generally moves during the observation window. The old h_c scalar, or H_rest scalar, is already in the two literal H flows; it is not dropped or counted again. There is no postselection, discarded output, permanent stopping or returned initial source claim.

## 6. Solved accuracy, resource and incident-load inequalities

Fix 0<epsilon<=1 and write A_theta=1+theta. Choose exactly

    N = max(2, ceil[(8 A_theta/epsilon)^2]),
    gamma_N=2J_F/N^2,
    q = min{ epsilon/[8(t0+w)],
             epsilon gamma_N/[8(6+18A_theta)] },
    T=theta/q,       tau=T+w.                        (17)

All choices are strictly positive for theta>0. Because qw<=epsilon/8<=1,
q(T+w)=theta+qw<=A_theta. The three terms in (16) are each at most epsilon/8. Therefore

    sup_(0<=s<=w) ||actual isometry - V_s|| <=3epsilon/8. (18)

Tensoring any retained passive reference preserves this operator bound. Conversion to complete unhalved trace distance costs at most two, so ideal-input/ideal-generator error is <=3epsilon/4. If the actual initial complete state differs by at most epsilon/8 in unhalved trace distance from |Alpha_phi><Alpha_phi| tensored with its exact unconditional old/reference marginal, and the actual-minus-nominal generator defect satisfies

    integral_0^tau ||K_actual(t)-K|| dt <=epsilon/16,  (19)

then contractivity and full-space Duhamel give total unhalved trace error

    3epsilon/4 + epsilon/8 + 2(epsilon/16) = epsilon. (20)

All state/calibration quantities in this statement are supplied conditions. Any fixed-target timing error or preparation-to-runtime switch needs its own resplit allowance; it is not free in (20).

The minimal ceiling and minimum in (17) give finite sufficient upper prices

    N=O(epsilon^-2),
    T=theta max{8(t0+w)/epsilon,
                8(6+18A_theta)/(epsilon gamma_N)}=O(epsilon^-5),
    ||K|| <= ||H||+R_s+N|omega|+2J_F(N-1)+6q=O(epsilon^-2),
    tau ||K||=O(epsilon^-7),                        (21)

with fixed-data constants. These are construction upper bounds, not lower bounds or optimality claims. For example N<=C_N epsilon^-2 with C_N=64A_theta^2+2, and substituting this upper bound into the displayed maximum proves the runtime power. No source-design oracle-time bound is inferred.

Since q<=1/t0, the incident added block-norm sum at old p is at most R_s+6/t0. At an interior source site it is at most |omega|+4J_F. At a_1 it is at most |omega|+2J_F+4/t0. Thus the single fixed cap

    J_* = R_s+|omega|+4J_F+6/t0                     (22)

bounds every added incident load for every epsilon. Each physical identity reserve is included. Dividing one large interaction into counted channels is not used. The total number of sites, total source field energy and full norm may diverge while (22) remains fixed.

For an explicit coefficient precision allowance, a conservative count of 8N+8 new physical Pauli/identity slots covers (1) and its collected representations. Giving these slots absolute errors at most epsilon/[16 tau(8N+8)] suffices for (19) when no other defect spends it. The inverse allowance has sufficient order epsilon^-8. Old-background, scalar, omitted-edge or state-preparation faults must share the appropriate existing budget. Positivity under faults requires positive parameterizations or separately paid local margins; the integral norm condition by itself does not guarantee positive actual blocks.

The theorem proves a conditional, common-strength, complete-output runtime construction on its stated restricted plant. It supplies no physical state-selection law, source cooling, formation time, detector identity, reuse or general arbitrary-plant compilation.

## 7. Why this proof does not already solve the arbitrary coupled plant

The decisive exact identity is (7). For a coupled plant it becomes

    [H+omega N_A, V]
      = ([H,sigma_+^p]-omega sigma_+^p) sigma_-^(a_1)
        + ([H,sigma_-^p]+omega sigma_-^p) sigma_+^(a_1), (23)

which need not vanish. A one-qubit port operator generally has several Bohr-frequency components and can couple to nonsymmetric source excitations. Simply applying (10) with the original H in the slow block would introduce duration-dependent commutator costs, and it is not the proof above. The old polynomial Lie certificate does not assert the single-frequency relation in (23).

Nor can the existing waveform compiler simply be run at a small port amplitude and inserted into (17). Its runtime, conditioning and slew must then be rederived as functions of that amplitude. The scale separation used in (17) depends on the fixed accumulated action qT=theta. A compiler with T growing faster than q^-1 can invalidate it.

The unresolved generic statement is therefore not a claim that bounded-strength controllers are impossible. It is the missing construction for simultaneous, controlled Bohr-frequency components with a one-edge old port and all controller outputs retained. The next section gives a finite algebraic target for such a construction, rather than hiding it inside an asserted source law.

## 8. A precise general reduction: second-order resonant collective sources

This section separates a proved finite-matrix implication from an uncompleted physical design. The implication is useful because its small-parameter choice is made after the finite source size and all inverse gaps are known. A small inverse gap then makes runtime large; it need not make a local coefficient large.

Use a dimensionless weak parameter xi, distinct from the energy q in sections 2–6. Suppose a proposed finite NN controller has

    K(xi)=K0+xi V+xi^2 A2+R(xi)I,                   (24)

where K0 has an invariant code inclusion J, with K0 J=J F and
F=H+H_C on that code. The literal old H is contained with coefficient one in K0. All matrices in the following conditions are actual finite complete matrices, not projected replacements for physical generators. Suppose:

1. J is an isometry, J^* V J=0, and the spectrum of QK0Q restricted to Ran(Q) is disjoint from the spectrum of F, where Q=I-JJ^*. Exact degeneracies inside F are allowed and retained. Every Q resolvent below means that restriction, extended by zero off Ran(Q).
2. A Hermitian D commuting with F and maps Z1,Z2 solve the finite equations

       K0 Z1-Z1 F = -VJ,
       K0 Z2-Z2 F = JD-VZ1-A2J.                    (25)

3. There are supplied pure controller states |Alpha_phi> in the code and a known scalar c such that, uniformly over the needed phase choices and all old inputs,

       ||[D-cI-G_phi](|Alpha_phi> tensor I_old)|| <=delta_N,
       G_phi=(1/t_*) exp(iHT) L_W exp(-iHT),
       W=exp(i theta0)exp(-iL_W),                  (26)

   with t_*>0 fixed, bounded Hermitian L_W, and T=t_*/xi^2. The hardware and bounds used to choose xi must be independent of those final phase choices. H_C's free evolution and every output factor are retained.
4. The base incident load of K0-H is at most a fixed J0 independent of N and epsilon. The actual V and A2 have known finite incident-load bounds ell_V(N), ell_2(N). Their positive block reserves are represented by the actual R(xi), and included in those load bounds; any source-code scalar canceled in an effective calculation is still physically charged.

Condition (25) is a finite algebra problem, not a simulated-time promise. Let Pi_E be F's exact eigenspace projectors. The first equation has the explicit solution

    Z1 Pi_E = (E-QK0Q)^(-1) Q V J Pi_E.             (27)

The necessary diagonal-block choice in the second is

    D = sum_E Pi_E J^*(VZ1+A2J) Pi_E.              (28)

For Hermitian V,A2 the displayed D is Hermitian: each block uses one Hermitian resolvent at real E. Once (28) is chosen, the second equation has zero right-hand side in equal-energy P/P blocks; its Q/P and unequal-energy P/P blocks are solved by the nonzero corresponding energy differences. Choosing the equal-energy P/P part of Z2 to be zero gives a finite computable solution when the spectral data and separation certificates are supplied. No polynomial complexity or large gap is asserted.

For Z(xi)=J+xi Z1+xi^2 Z2, exact multiplication gives

    [K(xi)-R(xi)I] Z(xi)-Z(xi)[F+xi^2D]
      =xi^3 R3+xi^4 R4,
    R3=VZ2+A2Z1-Z1D,
    R4=A2Z2-Z2D.                                  (29)

Set x_j=||Z_j||, r_j=||R_j||. The same two-endpoint Duhamel argument as (10) now gives the complete bare-code error through T+w:

    E_red <=2xi x1+2xi^2 x2+(T+w)(xi^3 r3+xi^4 r4)
           <=xi C_corr,N,
    C_corr,N=2(x1+x2)+(t_*+w)(r3+r4),  0<xi<=1.  (30)

The explicitly evaluated corrector constant C_corr,N may be enormous and depend on N, the fixed plant and a spectral certificate.

Because [F,D]=0, free old/source evolution can be factored before applying (26). The mean-field error through T+w is at most (t_*+w)delta_N. Stopping the additional effective old evolution at T costs at most xi^2 w ||L_W||/t_*. The controller comparator is its exact free vector exp(-iH_C(T+s))|Alpha_phi>; its phase contains R(xi)(T+s), c xi^2(T+s), and theta0. At endpoint (26) gives exactly the required old ordering. The source initial phases may depend on the already selected T, as in (14), but the proof constants must not acquire a hidden T dependence through that choice.

In particular, if the missing physical design supplies delta_N<=B/sqrt(N), with B fixed independently of N and xi after the plant/bus certificate is selected, one may first choose

    N >= [8(t_*+w)B/epsilon]^2,

then evaluate all finite matrices and constants, and finally choose xi>0 satisfying

    xi C_corr,N <=epsilon/8,
    xi^2 w ||L_W||/t_* <=epsilon/8,
    xi ell_V(N) <=J1,
    xi^2 ell_2(N) <=J2,
    xi<=1,                                        (31)

for any fixed J1,J2>0, with zero-denominator cases omitted. These are finitely many upper constraints on xi and have a strictly positive solution. The resulting cap is J0+J1+J2, and runtime is t_*/xi^2. The three ideal isometry errors are <=3epsilon/8; the same state and full-generator allowances as (19)–(20) finish the trace contract. Thus small denominators are compatible with a common local cap in this finite-matrix implication. No favorable runtime power is promised for (31).

This conditional reduction is not itself the missing construction. Conditions (26) and the uniform-base part of condition 4 must be established for actual qubit NN blocks, and the source phases must realize the full target without changing the constants after xi was selected.

## 9. Proposed NN realization of the reduction, and the exact open equation

One candidate begins with a coupled plant H whose eigenvalues E_a are simple, whose positive gaps E_a-E_b are all distinct, and whose one local Hermitian port operator B_p has nonzero matrix elements B_ab between every pair. These are additional mathematical conditions on H, not consequences established here from the supplied polynomial Lie certificate. The original task includes plants where they fail. Even a proof under them would therefore need an additional spectral regularization argument before replacing the generic compiler theorem.

For each positive Bohr gap omega_l=E_a-E_b, append a long ferromagnetic source chain with uniform field omega_l and a coherent symmetric input. Append a fixed finite qubit XY bus, with vacuum input, between p and the source endpoints. A comb layout in three dimensions can have exactly one old/new adjacency, source chains on disjoint exterior rays and degree at most three. All bus coefficients and source fields are bounded by fixed plant-dependent constants; chain lengths grow. The common old/bus coupling and bus/source couplings are multiplied by xi. Positive reserves must be added locally. This is a proposed architecture, not a checked layout/calibration certificate.

Let B_bus be the bus's positive one-excitation matrix, with a root a adjacent to p and source attachment sites u_l. The interaction is schematically

    V = v_p B_p X_a
        + sum_l r_l [sigma_+^(u_l)sigma_-^(source_l,1)
                     +sigma_-^(u_l)sigma_+^(source_l,1)].     (32)

Each term is an actual two-qubit edge. r_l may be real with sign carried by the supplied coherent source phase. Projection of a source boundary lowering operator is S_(l,-)/N_l. At exact old/source resonance, the second-order plant/source cross coefficient contains

    beta_l = -v_p r_l B_ab
                    [(B_bus-omega_l I)^(-1)]_(a,u_l).       (33)

The convention in (32) has one allowed ordering for source lowering/bus creation followed by bus annihilation/plant raising, so (33) has no automatic factor of two. Its Hermitian reverse is supplied by the reverse transition. This coefficient formula still needs to be checked against the full chosen bus/source spectrum, rather than against a one-excitation inverse alone. Nonsymmetric source sectors and every bus excitation sector are included in (25)–(28).

Plant self-energies, which cannot be discarded, have diagonal entries of the form

    d_a = v_p^2 sum_(b,j)
                  w_j |B_ba|^2/(E_a-E_b-mu_j),              (34)

where mu_j and w_j>0 are the bus energies and root spectral weights. Source self-energies must either be retained in the controller comparison and analyzed or canceled by actual paid xi^2 A2 blocks. For an SU(2)-invariant ferromagnetic chain, a plausible route is to show that the projected source self-energy is a quadratic polynomial in its total excitation number. Such a polynomial can be represented by projected onsite and NN density interactions because

    P_sym sum_j n_j P_sym = N_A,
    P_sym sum_(j=1)^(N-1) n_j n_(j+1) P_sym
          = N_A(N_A-1)/N.                                (35)

These are identities on the symmetric code. The second follows by averaging every distinct pair in a symmetric state. It does not prove the asserted degree-two form of the resolvent self-energy; that is an explicit remaining lemma, including all coefficients and scalar reserves. A large effective source counterterm is not ignored: xi^2 times its actual physical local coefficients must satisfy (31), and its full-space norm enters (29)–(30).

For a target logarithm L_W, the concrete unclosed calibration equation is

    sum_E Pi_E J^*[V Q(E-QK0Q)^(-1)Q V+A2]J Pi_E
       = cI + sum_a (L_W)_(aa)/t_* |a><a|
           + sum_(a>b) [g_ab |a><b| S_(ab,-)/N_ab + h.c.]
           + E_N,                                      (36)

with |g_ab|/2=|(L_W)_(ab)|/t_* and

    ||E_N (|Alpha_phi> tensor I_old)|| <=B/sqrt(N),        (37)

uniformly in the phase choices needed at the actual time T. Here Pi_E is F's exact code eigenspace projector at energy E, as in (27)–(28). The left side is exactly D from (28); the right side is an operator on the same code. Controller-only scalars and all physical block reserves must be listed separately. Initial phases can then give the factors exp[i(E_a-E_b)T] needed in (26); they change no interaction magnitude.

The diagonal part of (36) asks whether a positive root spectral measure can produce every requested difference d_a-d_0 while keeping all response factors in (33) nonzero and the complete P/Q separation positive. Near a distinct gap E_a-E_0, the corresponding column of (34) has a pole in its a component. Taking bus energies on both sides suggests spanning the diagonal differences by positive weights plus a scalar. That suggestion is not a solved simultaneous inverse-spectral/geometry theorem. A root-to-endpoint Green entry of an irreducible Jacobi chain is nonzero away from its poles, but attaching many sources at different sites and satisfying (34) at the same time needs an actual certificate; one cannot attach arbitrarily many counted source edges to a single bus qubit.

The complete remaining obligations for this route are therefore:

- Derive the strong spectral addressability needed above, or replace it by a degeneracy-aware construction that works for every admitted polynomial Lie certificate, while retaining the original H and any added perturbation's final-window action.
- Solve (33)–(37) with actual finite ordinary NN qubit blocks, one old port, bounded base coefficients, all source self-energies and scalar/positive reserves paid, and a full-spectrum separation certificate for (25).
- Prove a fluctuation bound with B fixed before xi is selected. In particular, do not let an uncharged N-dependent small denominator destroy (37).
- Check the complete corrected operator algebra and its phase convention independently before any downstream acceptance.

Once those obligations are met, (27)–(31) supply a concrete accuracy/runtime/local-strength recipe. They are not met by merely naming the source “classical,” by a first-order rotating-wave statement, or by the one-particle transfer coefficient alone. The present note leaves them open.

## 10. A separate alternative and the inherited clock diagnostic

A different possible route is an autonomous program tape whose weak port contacts each deliver a small coherent action. A useful target would be a complete-output fluctuation estimate proportional to the square root of the number of contacts, while the desired action is linear in that number. For arbitrary coupled H, the contacts also need resonant phase control or a full augmented actual-time compilation. No finite qubit NN tape Hamiltonian with that complete retained-output estimate is supplied here. This is an alternative mechanism and an exact proof target, not a claimed construction or native supplier.

There is also a simple diagnostic for attempts to reuse the parent binomial clock unchanged. Each positive parent clock edge has norm Omega(n+1), Omega=pi/(2tau). A common incident cap therefore requires at least

    pi(n+1)/(2tau) <=J_*.

The parent's sufficient global clock choice also requires

    n >= L_C^2 tau^4/(2eta_X^2).

Together they require

    L_C^2 tau^3 <= (4J_*/pi) eta_X^2,                (38)

up to the harmless stronger integer endpoint term. Thus lengthening that clock does not alone solve the resource problem; the actual waveform's L_C and tau must satisfy (38) jointly. For example a truly slow weak envelope with L_C=O(tau^-2) can satisfy this inequality as tau grows, whereas blindly padding a fixed-slew waveform cannot. This is a compatibility test for those sufficient estimates. It is not a necessary error lower bound for every binomial clock, every waveform placement, or every possible autonomous architecture. No universal impossibility claim is made.

## 11. Evidence, scope and freeze boundary

The one-qubit argument in sections 2–6 and the finite-corrector implication in section 8 were derived here from displayed finite-dimensional identities. Their checks are author algebra and a complete cold read. One bounded dense author sanity run also checked twelve restricted cases, N=2 through 6, total Hilbert dimension at most 128, including omega<0 and a pure Z target. All 36 complete-isometry comparisons lay below the displayed bounds; direct physical scalar, exact-resonance, corrector-identity and fluctuation checks had no recorded failure. The raw results, executable source at launch, exact command, streams and limits are in CHECK_EVIDENCE.md and its linked files. These finite floating-point cases do not prove the asymptotic recipe, the gap for arbitrary N, the general reduction or the proposed bus equations. Source hashes and copying establish provenance only. No independent checker, retained audit, native physical implementation or general source-state formation law has been supplied by this note.

The exact original generic target remains open in this proposal. The useful completed result is a common-strength, all-output, finite-window test construction with a solved epsilon recipe and literal old aging. The useful general reduction is a finite Sylvester/coupling/collective-fluctuation certificate with a solved small-parameter implication. A failed candidate equation, missing spectral premise or future counterexample must be preserved; it cannot be replaced by a claim that the requested universal construction exists or is impossible.

This worker writes only its assigned directory. It does not modify W/C source, Git state, PRs, canonical runners/caches/graphs, locks, audit verdicts, axioms or editable prompt files. All source comparison with the root or other workers is deferred until this argument is frozen.


---

## Immutable source body: independent_restricted_body

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# Independent derivation: a bounded local ferromagnetic source

Status: provisional conditional mathematical result, independently derived
from the supplied architecture. No retained or audit status is claimed. The
primary worker's proof, resource exponents, scripts, and results were not read.
The complete source/exposure record is in `EXPOSURE.json`; the final source
identity and freeze time are in `FREEZE.json`.

## Exact question and result

Let the controlled old qubit be `p`, with literal old Hamiltonian

\[
 H=h_c I+\omega n_p+H_{\rm rest},\qquad n=(I-Z)/2,
\]

where `H_rest` acts only on decoupled old spectators. No restriction is placed
on the old/reference input, including entangled inputs. Fix `J_F>0`,
`r>=0`, `r^2+z^2=1`, `0<theta<=pi`, `phi_0`, `theta_0`, and a finite window
`w>=0`. The source contains precisely the chain `a_1,...,a_N`, with only the
edge `p-a_1` connecting source to old qubits. Define

\[
\begin{split}
 L&=J_F\sum_{j=1}^{N-1}(I-S_{j,j+1}),\\
 V&=\sigma_+^p\sigma_-^{a_1}+\sigma_-^p\sigma_+^{a_1},
 \quad \sigma_+=|1\rangle\langle0|,\\
 A&=2rV+zZ_p,\qquad a=\|A\|=\sqrt{4r^2+z^2}\le2,\\
 K&=H+L+\omega N_A+qA+RI,\quad N_A=\sum_j n_{a_j},\\
 R&=R_s+N\max(0,-\omega)+2qr+q|z|,\qquad R_s\ge\|H\|.
\end{split}
\]

The source input is supplied, not generated by this theorem:

\[
 |\alpha_\phi\rangle=
 2^{-N/2}(|0\rangle+e^{i\phi}|1\rangle)^{\otimes N}.
\]

For `N>=2`, put `Delta_N=2J_F/N^2`, choose any `q>0`, and set
`T=theta/q`, `phi=phi_0+omega T` modulo `2pi`. If `J_phi` embeds every old
input as `Alpha_phi tensor input`, then the following complete isometry
bound holds uniformly for `0<=s<=w`, with `t=T+s`:

\[
\begin{split}
&\left\|e^{-itK}J_\phi-
 e^{-i(Rt+\theta_0)}
 \left(e^{-i\omega tN_A}|\alpha_\phi\rangle\right)
 \otimes\left(e^{-isH}W e^{-iTH}\right)\right\|\\
&\qquad\le
 \underbrace{\frac{2qa}{\Delta_N}
       [1+a(\theta+qw)]}_{\text{finite-gap reduction error}}
 +\underbrace{\frac{r(\theta+qw)}{\sqrt N}}_{\text{source fluctuation}}
 +\underbrace{qw}_{\text{continued action in the terminal window}},
 \tag{1}\\
&W=e^{i\theta_0}e^{-i\theta a_{\phi_0}},\qquad
 a_\varphi=r\cos\varphi X+r\sin\varphi Y+zZ.
\end{split}
\]

The tensor expression in (1) denotes the corresponding map from old input
space to source-plus-old output space. Every output is retained. Tensoring
both maps with any reference identity leaves the bound unchanged. The bound
is on vectors/isometries with the displayed literal phases; no quotient by
global phase or reduced-state comparison is used.

For `0<epsilon<=1` and any fixed cap `Q>0`, one explicit sufficient choice is

\[
\begin{split}
 N&=\max\left\{2,\left\lceil
       \frac{9r^2(\theta+1)^2}{\epsilon^2}\right\rceil\right\},\\
 q&=\min\left\{Q,\frac{\epsilon Q}{3(1+Qw)},
 \frac{\epsilon J_F}
 {3a[1+a(\theta+1)]N^2}\right\}. \tag{2}
\end{split}
\]

These choices make (1) at most `epsilon`. For fixed `r>0` and the other fixed
parameters, they give sufficient asymptotic scalings
`N=Theta(epsilon^{-2})`, `q=Theta(epsilon^5)`,
`T=Theta(epsilon^{-5})`. They are sufficient bounds, not optimality claims.
No added local block norm or incident sum of added block norms diverges as
`epsilon -> 0`. Source size, run time, total Hamiltonian norm, negative-omega
scalar reserve, and calibration requirements are not bounded by that claim.

## 1. An all-sector gap bound proved by swap comparison

Let `P` be the projection onto the fully symmetric source subspace, tensored
with the identity on all old/reference systems, and let `Q_P=I-P`. Because
every adjacent-swap term is positive semidefinite and adjacent swaps generate
all permutations, `ker L=ran P`.

Here is a full-Hilbert-space gap proof; it does not replace the chain by its
one-excitation sector. On the source alone write

\[
 D=\sum_{k=1}^{N-1}(I-S_{k,k+1}),\qquad
 C=\sum_{i<j}(I-S_{ij}).
\]

The long transposition `S_ij` has an adjacent-transposition word of length
`2(j-i)-1`, in which each path edge occurs at most twice. For a product of
unitaries `U_1 ... U_m`, the telescoping identity

\[
 I-U_1\cdots U_m=\sum_{\ell=1}^m
 U_1\cdots U_{\ell-1}(I-U_\ell)
\]

and Cauchy-Schwarz give

\[
 \|(I-S_{ij})v\|^2
 \le4(j-i)\sum_{k=i}^{j-1}\|(I-S_{k,k+1})v\|^2.
\]

Since each swap is a self-adjoint involution,
`||(I-S)v||^2=2<v,(I-S)v>`. Summing the preceding inequality yields

\[
 \langle v,Cv\rangle\le
 \sum_{k=1}^{N-1}
 4\!\sum_{i\le k<j}(j-i)\,
 \langle v,(I-S_{k,k+1})v\rangle
 \le\frac{N^3}{2}\langle v,Dv\rangle, \tag{3}
\]

because `sum_{i<=k<j}(j-i)=Nk(N-k)/2` and `k(N-k)<=N^2/4`.

For qubits, with total spin `S_tot=(1/2)sum_j sigma_j`, the elementary
spin-swap identity gives

\[
 C=\frac{N(N+2)}4 I-S_{\rm tot}^2.
\]

The spin-addition decomposition of `N` spin-half representations has total
spins `N/2,N/2-1,...`. Its maximal-spin component is exactly the symmetric
subspace. On any other component, the Casimir difference is at least

\[
 \frac N2\left(\frac N2+1\right)
 -\left(\frac N2-1\right)\frac N2=N.
\]

Equivalently, `C>=N(I-P)`. Combining this with (3) proves

\[
 L=J_F D\ \ge\ \frac{2J_F}{N^2}(I-P)=\Delta_N Q_P. \tag{4}
\]

This argument covers every source excitation sector simultaneously. It uses
finite-dimensional spin addition only to bound the complete-graph swap sum;
no chain spectral-gap theorem or unproved equality of sector gaps is used.
All later denominators use the conservative bound (4).

## 2. Long-time leakage control without a perturbative spectrum assumption

The following elementary integration-by-parts estimate is useful here. Let
`L>=Delta Q_P`, `LP=0`, `A=A^*`, `||A||<=a`. For `t>=0`,

\[
 \left\|e^{-it(L+qA)}P-e^{-iqtPAP}P\right\|
 \le\frac{2qa}{\Delta}(1+qat). \tag{5}
\]

To prove it, define the reduced inverse on `ran Q_P` and

\[
 B=(L|_{Q_P})^{-1}Q_PAP,\qquad
 LB=Q_PAP,\qquad \|B\|\le a/\Delta.
\]

Put `U(t)=exp[-it(L+qA)]` and `U_P(t)=exp[-iqtPAP]P`. Duhamel gives

\[
 U(t)P-U_P(t)=-iq\int_0^t U(t-u)LB U_P(u)\,du.
\]

For `F(u)=U(t-u)B U_P(u)`, direct differentiation gives

\[
 F'(u)=iU(t-u)LB U_P(u)
       +iqU(t-u)(AB-BPAP)U_P(u).
\]

Integration by parts therefore bounds the Duhamel term by
`2q||B||+q^2 t(||A||+||PAP||)||B||`, proving (5). This estimate does not
assume `q<Delta`, a perturbed gap, or that the evolution remains in a chosen
excitation sector. Small `q/Delta` is used only when choosing resources to
make its error small. In this problem `A^2=4r^2 V^2+z^2 I`, since
`{V,Z_p}=0` and `V^2` is the one-excitation projector of the two port qubits.
Thus the stated `a=sqrt(4r^2+z^2)` is exact.

## 3. The source is quantum: its complete-isometry fluctuation is explicit

Define `S_-=sum_j sigma_-^{a_j}` and `S_+=S_-^*`. Symmetry gives the exact
compressed local operators

\[
 P\sigma_\pm^{a_1}P=\frac1N S_\pm P,
\]

and hence, on `ran P`,

\[
 A_P=PAP=\frac{2r}{N}
  (\sigma_+^pS_-+\sigma_-^pS_+)+zZ_p. \tag{6}
\]

The collective expression (6) is an analysis of a subspace of the installed
nearest-neighbor Hamiltonian; it is not an extra installed interaction.

On `Alpha_phi`,

\[
 \langle S_-\rangle=\frac N2e^{i\phi},\qquad
 \langle S_+\rangle=\frac N2e^{-i\phi},\qquad
 \|(S_\pm-\langle S_\pm\rangle)\alpha_\phi\|=\frac{\sqrt N}{2}. \tag{7}
\]

The variance in (7) follows by expanding the independent product-state
expectations: each qubit contributes `1/2-1/4=1/4` and cross covariances
vanish. With `J_phi:psi -> Alpha_phi tensor psi`, equations (6)-(7) imply the
exact operator-norm residual

\[
 \|A_PJ_\phi-J_\phi a_\phi\|=\frac r{\sqrt N}. \tag{8}
\]

Indeed, split an arbitrary old/reference input into its `p=0` and `p=1`
components. The two fluctuation terms land in orthogonal `p=1` and `p=0`
spaces, respectively, each with squared coefficient `r^2/N`. This proves
(8) even with arbitrary spectator/reference entanglement; no assumption that
the source stays classical is made. A second Duhamel estimate gives

\[
 \left\|e^{-iqtA_P}J_\phi-J_\phi e^{-iqt a_\phi}\right\|
 \le\frac{qtr}{\sqrt N}. \tag{9}
\]

Combining (4), (5), and (9), and using `PJ_phi=J_phi`, proves

\[
 \left\|e^{-it(L+qA)}J_\phi-J_\phi e^{-iqt a_\phi}\right\|
 \le\frac{2qa}{\Delta_N}(1+qat)+\frac{qtr}{\sqrt N}. \tag{10}
\]

## 4. Literal drift, source phase, and terminal-window ordering

The total number `n_p+N_A` commutes with both `L` and `A`; decoupled
`H_rest` commutes with them as well. Consequently,

\[
 e^{-itK}=e^{-iRt}e^{-it(H+\omega N_A)}e^{-it(L+qA)}. \tag{11}
\]

This exact factorization is why neither sign nor size of `omega` enters a
gap denominator. The phase convention can be checked directly from
`sigma_+=|1><0|`:

\[
 e^{iTH}\sigma_+^p e^{-iTH}=e^{i\omega T}\sigma_+^p,
 \qquad
 e^{iTH}a_{\phi_0}e^{-iTH}=a_{\phi_0+\omega T}=a_\phi. \tag{12}
\]

Thus the desired old map at `t=T+s`, after multiplying by `exp(+itH)`, is

\[
 e^{iTH}e^{-i\theta_0}W e^{-iTH}=e^{-i\theta a_\phi}. \tag{13}
\]

This identity respects the requested order `exp(-isH) W exp(-iTH)`.
The scalar `theta_0` cancels exactly against the displayed scalar prefactor
in the target, without changing the literal `h_c I` or `R I` terms.

The ideal compressed evolution in (10) has angle `qt=theta+qs`. Because
`a_phi^2=I`,

\[
 \|e^{-i(\theta+qs)a_\phi}-e^{-i\theta a_\phi}\|
 =2|\sin(qs/2)|\le qs. \tag{14}
\]

Apply (10)-(14), preserve the exact freely rotating source state
`exp(-i omega t N_A)Alpha_phi`, and maximize over `s` to obtain (1).
In particular the source at `T+s` is `Alpha_(phi_0-omega s)` exactly in
the comparison map, with no additional phase from the use of `n=(I-Z)/2`.

## 5. Local norms, positivity, and resource accounting

The actual installed blocks and their norms are

| Block | Norm | Positive semidefinite? |
|---|---:|---|
| `J_F(I-S_{j,j+1})` on a chain edge | `2J_F` | yes |
| `omega n_{a_j}+max(0,-omega)I` on one source site | `|omega|` | yes |
| `2qr(V+I)` on the sole port edge | `4qr` | yes |
| `q(zZ_p+|z|I)` on the old port | `2q|z|` | yes |
| fixed `R_s I` on the old system | `R_s` | yes |

The old `H` is unchanged and `H+R_s I>=0`. The displayed decomposition sums
to the literal `K`. The identity reserves may be represented on the listed
supports; they do not introduce hidden edges. For `q<=Q`, every added block
norm is bounded by

\[
 \max\{2J_F,|\omega|,4Qr,2Q|z|,R_s\},
\]

independent of `epsilon` and `N`. Even a convention that bounds the *sum* of
norms incident to each site is satisfied, for example by the uniform bound

\[
 B_{\rm incident}=4J_F+|\omega|+4Qr+2Q|z|+R_s. \tag{15}
\]

Each interior source site has only its two chain edges and its onsite block;
`a_1` additionally has the single port edge, and old `p` has that edge and
the control onsite block. Bound (15) deliberately overestimates some cases.
If `R_s I` is booked as a scalar block on `p`, (15) also covers it.

For (2), `qw<=epsilon/3<=1`. The three terms in (1) are individually at
most `epsilon/3`, by the three respective choices in (2). All parameter
choices are strictly positive where required. If `omega<0`, the *total*
scalar `R` grows as `N|omega|`; it is a sum of bounded onsite reserves.
An assertion that the total added norm stays bounded would be false and is
not part of the result.

## 6. Edge cases and limits of the conclusion

* **`r=0`.** Then `z=+1` or `-1`, `A=zZ_p`, and the port block vanishes.
  The source decouples exactly, so `N=1` suffices and no gap or large source
  is required. At `s=0` the target is exact for every `q>0`; over the window
  the exact error is `sup_(0<=s<=w) 2|sin(qs/2)|<=qw`. For `w>0`, taking
  `q=min(Q,epsilon/w)` suffices, giving `T=O(epsilon^{-1})`. For `w=0`, any
  fixed `q<=Q` works exactly.
* **`w=0`.** Equation (1) has no continued-action term. The general
  construction still converges. No finite-time exact realization is claimed
  when `r>0`.
* **Either sign of `omega`, including zero.** Equations (11)-(13) hold
  without change; the source onsite reserve has norm `|omega|`. There is no
  assumption that the old drift is removable or that its scalar is ignored.
* **Scalar target.** Under the stated `0<theta<=pi`, `W` is scalar exactly
  when `theta=pi`. The proof still works for a supplied `r>0`, but its
  resource exponents are not necessary lower bounds for this target. If a
  different axis representation of the same scalar `W` is allowed, choose
  `r=0,z=1,theta=pi` and use the exact endpoint construction above. If the
  assignment fixes `r,z` in `K`, that change is a different implementation,
  not a claim about the fixed one. Also, the required literal rotating-frame
  endpoint is `-I`, not `I`: simply doing nothing would miss the specified
  global phase in the complete-isometry target.
* **Preparation and calibration.** The exact product input, `omega`, `q`,
  the equatorial phase `phi_0+omega theta/q`, and timing are supplied data.
  The theorem does not derive preparation, autonomous timing, coefficient
  accuracy, or a robust implementation cost for those data. Slow operation
  and large `N` can make those tasks demanding. The claimed boundedness is
  specifically of added local Hamiltonian norms and incident sums.

## Independent-check coverage and open obligations

The all-sector gap, the integration-by-parts leakage bound, the collective
fluctuation norm, the rotating-frame identity, and the local reserve norms
are proved above. The assumptions are precisely the supplied finite qubit
Hamiltonian architecture and prepared source state, plus ordinary linear
algebra and finite spin addition. No empirical prediction or new framework
axiom is inferred.

The finite checks beside this note are supplementary attempts to falsify
implementation mistakes. They do not certify an all-`N` theorem.
Their source-at-launch hash, full outputs, and deliberate incorrect variants
must be inspected before citing them. The primary derivation remains unseen
until this result is frozen, so this note does not confirm its exact text,
constants, or complete dependency closure. Parent reconciliation and any
independent landing review remain separate work. No editable prompt file,
Git/PR, cache, graph, audit state, or other worker artifact was changed.


## Finite falsification checks actually run

`finite_checks.py` was run under Python 3.13.5, NumPy 2.4.4, and SciPy 1.17.1.
`FINITE_CHECK_LAUNCH.json` records its source and note hashes before the run;
matching byte copies are preserved under `source_at_launch/`. The final note
adds this evidence report and fixes notation and a units convention after
the run. The numerical source was not tuned after seeing the results.
`FINITE_CHECK_FULL.log` and `FINITE_CHECK_RESULTS.json` preserve all records.

The computational-basis builder explicitly constructs the entire source
Hilbert space and the entire source-plus-port Hamiltonian. Its isometry
comparison uses both old basis columns and the largest singular value, so
it covers every old input and its reference extension for each sampled
parameter/time case. It does not truncate excitation sectors or evolve only
the symmetric source. Continuous-time uniformity comes from the proof, not
from the time samples.

* Full source spectra for `N=2,...,8` have nullity `N+1` and smallest
  positive eigenvalue above `2J_F/N^2`. For example, at `N=8,J_F=1`,
  the measured gap is `0.1522409349774265` versus the conservative lower
  bound `0.03125`.
* Direct literal-Hamiltonian isometry tests at `N=2,4,6,8`, including
  positive, negative, and zero `omega`, satisfy the bound at all sampled
  times. For the `N=8,omega=-0.07` case, the largest sampled error is
  `0.2249220166211364`, below `0.2824050731710368`. These are modest-size
  checks and are not a numerical demonstration at asymptotically tiny error.
* The incorrect carrier sign yields error `1.1010184842566808` and the
  omitted factor of two at the port yields error `0.358846828843374`, both
  exceeding the same correct-architecture bound `0.28236602724966253`
  by the predeclared margin `0.05`. The baseline error is
  `0.22491434490190917`. The target source in the phase-mutant comparison
  is built from that mutant's actual supplied source, so this probe detects
  the old gate-phase error rather than a trivial mismatched source input.
* Deleting the middle chain edge at `N=6` changes source kernel dimension
  from the required `7` to `16`, and is rejected.
* The two pure-Z signs and the scalar-target pure-Z case match the exact
  window error `2|sin(qs/2)|` to less than `9.7e-15` in the tested cases.

All 18 predeclared finite predicates passed; the three deliberately
incorrect variants were detected. That count reports executed checks, not
independent scientific votes or an audit verdict. The proof above is the
all-parameter argument. No external literature was consulted and no
different-model-family independence is claimed.


---

## Immutable source body: exposed_reconciliation_body

Historical source retained exactly; the current source-acceptance qualifications above govern its interpretation.

# Exposed comparison of the ferromagnetic-source proposal

This is a separate reconciliation after the independent result was frozen at
2026-10-16T00:01:25.736644Z. Author-source exposure began at approximately
2026-10-16T00:03:08Z. Original author and independent files were not modified.
`MANIFEST.json` records exact source identities, recoverable copies, coverage,
and the retrospective execution transcription below. `FREEZE.json` identifies
this comparison. No scientific calculation was rerun during reconciliation.

## Disposition and exact accepted scope

The author's sections 2–6 establish the stated restricted single-qubit
conditional theorem. I found no consequential mathematical defect in its
all-sector gap proof, bare-input reduction, complete source-output estimate,
literal drift/phase ordering, exact-choice resource powers, or incident-load
accounting. This agrees with the independently frozen derivation. Acceptance
here means a scoped mathematical check of the displayed source, not retained
audit status, a physical supplier, or a general coupled-plant result.

The accepted premises are:

* The literal old Hamiltonian is `h_c I+omega n_p`, possibly with genuinely
  decoupled old spectators, and the target acts only on `p`.
* The exact appended graph is one nearest-neighbor source chain, one old/new
  edge, and the explicitly assumed available exterior ray. Every old,
  source, and reference output is retained.
* The source product state, target decomposition, coefficients, timing,
  initial phase selected after the duration, and state/calibration tolerances are supplied.
  For the task's positive whole-generator variant, take `R_s>=||H||`.
* The error window is fixed and finite. Source size, total norm, duration,
  scalar reserve, and precision costs may grow; the bounded quantity is
  the sum of norms of added blocks incident to any one site.

Two presentation boundaries should be made explicit when packaging this
result: the `theta=pi` scalar target retains a literal minus sign for the
given decomposition, and an effective computable implementation of the
resource recipe needs certified rounding with quantitative slack. Neither
point refutes the author's exact-real mathematical formulas. Section 3
below supplies a rounding construction that preserves their powers.

The author's section 8 remains a conditional second-order finite-matrix
implication. Its algebra is consistent under its listed hypotheses; those
hypotheses have not been realized by the single-qubit theorem. Section 9
remains a proposed general bus with unresolved equations. Neither is included
in the accepted physical single-qubit construction, and no general compiler
or generic-plant claim is accepted here.

## 1. Source-bound comparison of the single-qubit argument

The author source checked in full has SHA-256
`47cda48195580320d92851332bce37d09f8703294acadb571b69d0dc23a48c15`.
The independently frozen source has SHA-256
`687a28553a1588265906ca0e64a8a18c8caf18027003343aed5708b43b2a0222`.
Both hashes still match their original freezes.

| Obligation | Author result | Independent comparison |
|---|---|---|
| Entire-source gap | `gamma_N=2J_F/N^2`, section 3 | Same swap-comparison/Casimir proof was independently obtained; no sector substitution occurs. |
| Symmetric-space reduction | Bare corrector `Z=P-q R_F QAP`; error `6q/gamma_N+18tq^2/gamma_N` | My integration-by-parts bound is `2qa/gamma_N+2tq^2 a^2/gamma_N`, with `a=sqrt(4r^2+z^2)<=2`. The author's `v=3` is conservative and valid. |
| Quantum-source fluctuation | Exact residual `r/sqrt(N)`, then bounded by `1/sqrt(N)` | Agrees with the independent vector residual, including arbitrary old/reference inputs. |
| Resonance and frame | `[H+omega N_A,L_F]=[H+omega N_A,A]=0`; `phi=phi0+omega T` | Exact for the actual decoupled plant. Both signs of `omega` are covered. No rotating-wave approximation is used. |
| Literal target | Equation (15), including `R(T+s)+theta0` | Matches the required order `exp(-isH) W exp(-iTH)` and the freely evolving complete source. |
| Uniform error | Equation (16) | Conservative relative to the independent bound, with the same three error sources. |
| Exact choices | Equation (17) | They imply each isometry term is at most `epsilon/8`; hence `3epsilon/8`. |
| Trace and fault budget | Equations (19)–(20) | A factor two converts isometry error to unhalved trace distance. The supplied initial-state `epsilon/8` and generator integral `epsilon/16` spend the remaining `epsilon/4` correctly. |
| Fixed-data powers | Equation (21) | For the specified minimal ceiling and exact minimum: `N=O(epsilon^-2)`, `T=O(epsilon^-5)`, `norm(K)=O(epsilon^-2)`, and `(T+w)norm(K)=O(epsilon^-7)`. These are sufficient upper bounds. |
| Local load | Equation (22) | Every positive reserve is counted. The claimed common incident sum cap is valid. |

The common gap proof deserves a precise independence statement: the separate
contexts independently produced the same swap-comparison argument. They are
not two mathematically disjoint proofs of that lemma. The author's corrected
embedding and my integration by parts also express closely related exact
identities. The finite implementations differ: the author builds Pauli
Kronecker matrices; my frozen check builds computational-basis bit transitions.
The independent source was frozen before exposure to the author's text or
numerical outputs. No different-model-family independence is claimed.

## 2. Edge cases, literal scalars, and incident-load accounting

**Scalar target.** The author's line 33 correctly gives an exact free-old
solution for a decomposition with `theta=0` and its matching comparison
phase `theta0`. However, within the theorem's `0<theta<=pi` domain,
`theta=pi` is also scalar. Keeping that decomposition fixed gives

    exp(-i theta0) W = -I.

The target in the rotating frame is therefore `-I`, not `I`. Dropping the
interaction merely because `W` is scalar misses the literal isometry phase.
The main construction and equation (15) already retain this sign correctly;
this is a needed explicit boundary, not a defect in their proof. Rewriting
the same scalar `W` with `theta'=0` requires `theta0'=theta0+pi`, which changes
the explicitly stated comparison phase. That is legitimate only when such
reparameterization is allowed. Alternatively `r=0,z=1,theta=pi` gives the
correct fixed-decomposition endpoint by an actual old `Z` rotation.

**Pure Z.** At `r=0`, `z=+1` or `-1`, the port vanishes and the source is
exactly free. The author's large `N` and conservative bounds remain valid.
They are unnecessary: `N=1` suffices, endpoint error is zero, and the exact
window error is `sup_(0<=s<=w) 2|sin(qs/2)|`. For `w>0`, choosing
`q=min(Q,epsilon/w)` gives a sufficient `O(epsilon^-1)` duration; for `w=0`,
fixed positive `q` is exact. This improvement does not contradict the
author's explicitly nonoptimal upper bounds.

**Negative omega and scalar normalization.** Each source onsite block has
norm `|omega|` and extracted reserve `max(0,-omega)`. The actual `R` in
equation (2) is therefore correct for both signs, including zero. The
separate normalized-trace scalar in equation (3) is also correct:
`tr(I-SWAP)/4=1/2` per ferromagnetic edge. That scalar does not add an extra
phase to the comparison, because the full edge operator annihilates the
symmetric source. The literal old scalar is already in the two old flows.

**References and spectators.** The estimates are operator bounds on the
complete isometry; tensoring an arbitrary passive reference preserves them.
Actual decoupling, rather than merely omitting a spectator from a test, is
what permits `H_rest`. The finite tests contain only the controlled qubit,
but the analytical tensor-factor argument covers the stated spectators and
arbitrary entanglement. A coupled old spectator is outside the theorem.

**Incident sum.** At `p`, the added sum is at most
`R_s+4qr+2q|z|<=R_s+6/t0`; at a source interior site it is
`|omega|+4J_F`; at `a_1` it is `|omega|+2J_F+4/t0`.
The author's `J_*=R_s+|omega|+4J_F+6/t0` bounds all of them. Identities are
included on their physical local supports, and no apparent strength reduction
is achieved by splitting one large block into separately counted channels.
For `omega<0`, total `R` grows with `N`; that does not violate this local cap.
As the author correctly states, a small full-generator defect does not by
itself preserve positivity of each actual faulty block. Positive
parameterizations or explicitly paid margins are a separate condition.

## 3. Exact resource existence versus a computable selection algorithm

The exact ceiling and minimum in author equation (17) are well-defined
mathematical choices, and their asymptotic upper bounds are valid as written.
They are not, by themselves, a total finite algorithm on arbitrary real
inputs. Ceiling is discontinuous at integers, so even a computable real
argument does not generally permit computing its exact ceiling from a
Cauchy name. The hypotheses also explicitly allow arbitrary real fixed
data; no computability theorem can be inferred for noncomputable inputs.
The same caveat applies to my independent note's exact-real formula if it
is interpreted as an algorithm rather than an existence construction.

A narrow, effective repair preserves both accuracy and the stated powers.
Assume the fixed numerical data and target decomposition have certified
computable-real representations, with the declared strict positive
quantities effectively bounded away from zero when needed. Work in the
declared physical units. Let

    b = [8(1+theta)/epsilon]^2.

Compute a rational upper enclosure `u` with `b<=u<=b+1/2`, and set

    N=max(2,ceil(u)).

This ceiling is of a rational number, so it is decidable. It satisfies the
required lower bound and `N<b+3/2` in the present `epsilon<=1,theta>0`
domain. Thus `N=O(epsilon^-2)` still holds. Using this actual `N`, compute
certified enclosures for the positive real

    m = min{epsilon/[8(t0+w)],
            epsilon (2J_F/N^2)/[8(6+18(1+theta))]}.

Refine them until rational numbers `L,U` satisfy

    0<L<=m<=U<=2L.

Positivity of `m` guarantees termination. Choose the exact rational `q=L`.
Then

    m/2<=q<=m,

so every error inequality remains valid and `T=theta/q<=2theta/m`.
The powers in (21), and the inverse coefficient-precision allowance
`O(epsilon^-8)` at author line 216, are preserved up to fixed constants.
The phase can be supplied via the computable complex value
`exp[i(phi0+omega theta/q)]`; there is no need to decide a discontinuous
exact representative modulo `2pi`.

In contrast, “choose any sufficiently small rational `q`” proves finite
existence but does **not** preserve those resource upper bounds. One may
choose a positive rational smaller than both `m` and
`2^(-ceil(1/epsilon))`; its duration is at least
`theta 2^(ceil(1/epsilon))`. Similarly an arbitrary integer much larger than
the required source lower bound need not retain the site power. The
constant-factor lower bound on the chosen `q`, and bounded overshoot of
`N`, are the missing quantitative safeguards in such an implementation.

This comparison does not claim the author used that incorrect arbitrary
choice: the displayed author formula explicitly uses the minimum and
minimal ceiling. It identifies the safeguard required if those exact-real
choices are replaced by an executable approximation. No coefficient or
state-preparation supplier is thereby derived.

## 4. Separate treatment of sections 8–10

I read these sections completely; they are not silently included in the
single-qubit acceptance. In section 8 the two Sylvester equations, the
spectrally diagonal formula for `D`, and the exact residual expansion
(27)–(29) are algebraically consistent when the listed full-spectrum
separation, isometry, Hermiticity, and zero-code-block hypotheses hold.
The estimate (30) follows from both bare/corrected endpoints and
`T=t_*/xi^2`. Mean-field factorization additionally uses `[F,D]=0` and
the independently supplied uniform residual (26). The trace allowance then
has the same interpretation as in the single-qubit proof.

That is a finite-matrix implication with strong supplied conditions. A
computable solution also needs the effective spectral data and separation
certificates the text names. In particular, equality of code energies and
their exact degenerate eigenspaces cannot be discovered generically by
floating-point thresholding. No favorable runtime power is asserted for
its arbitrarily small `xi`, so the single-qubit polynomial-runtime claim
must not be transferred to (31).

Section 9 does not establish those physical hypotheses. Its complete
spectral separation, source self-energy representation, simultaneous
calibration (33)–(37), phase-uniform fluctuation constant, and admissible
bus/geometry certificate remain open exactly as the author states. A
one-excitation Green function cannot supply the required all-sector
resolvent claim. No acceptance of the proposed bus coefficient or its
inverse-spectral realization follows from this comparison.

Section 10's tape is another proposal. Its inherited binomial-clock
diagnostic is read as a compatibility statement about cited sufficient
estimates; I did not independently validate the cited parent theorem or
grant a new general clock result. The source-copy inventories are not
coverage of those parent mathematical arguments.

## 5. Executed evidence and verification limits

The entire author `finite_check.at_launch.py` was read, as were the complete
stdout, empty stderr, launch/result receipts, evidence report, and launcher.
The executed source is a self-contained scientific implementation using
NumPy/SciPy and no imported repository theorem code. Its hash is
`317e24380e9f3c942d5a10c667c3c484ccf3108d69979cbc52799def5ba5dab5`.
The launcher actually copies that source before execution and records cwd,
command, return code, streams, and before/after source identity.

The evidence report accurately describes the recorded 12 cases, 36 time
observations, scalar/resonance/corrector/fluctuation checks, negative-omega
case, and pure-Z case. Its displayed maxima and stated limits agree with
the complete recorded output. Those author checks do not implement the
asymptotic resource recipe, prove the infinite family, or establish the
general reduction's physical hypotheses. My earlier frozen 18 checks
remain separate corroborating finite evidence, with their declared mutation
probes; no new scientific execution occurred in this reconciliation.

### Retrospective transcription of the independent check's tool execution

This paragraph and the corresponding manifest fields are a transcription
from this worker's existing conversation tool record, **not a launch-time
receipt and not a replay**. The original independent launch JSON records
`argv=["finite_checks.py"]`, source hashes, versions, and its program-recorded
launch time, but omits cwd, resolved interpreter path, and process exit.
It is preserved unchanged.

The actual `exec_command` invocation was:

    command: python3 finite_checks.py > FINITE_CHECK_FULL.log 2>&1
    cwd: /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261015_224023/ferromagnetic_source_independent_check
    yield_time_ms: 1000
    max_output_tokens: 1000

The initial result returned running process session `27634`. A subsequent
`write_stdin` poll of that session with empty input, `yield_time_ms=1000`,
and `max_output_tokens=1000` returned `exit_code=0` and empty tool output
(the process streams had been redirected to the log). Its tool chunk ID
was `b96549`. The launch program itself recorded
`2026-10-15T23:57:43.250083+00:00`; the polling call ran alongside a clock
read returning `2026-10-15 23:58:18 UTC`. That clock reading is not an exact
process-exit timestamp. The resolved path behind shell command `python3`
was not recorded by that invocation and is not reconstructed here.

This supplies the requested available execution facts while preserving the
provenance limitation. It does not strengthen a numerical sanity check into
proof, change its original receipt, or manufacture missing launch fields.

## Coverage, preservation, and remaining action

The author's `DERIVATION.md` lines 1–383, evidence report, all 124 lines of
executed finite source, full raw streams, launch/result records, source
coverage and source manifest, freeze, and launcher were read completely.
All 16 files named in the author's original freeze and all 18 files named
in the independent original freeze matched their recorded hashes at
comparison capture. Reading the author's source manifest does not mean
that I read or accepted every copied parent proof; they are unnecessary
for the self-contained sections 2–6 checked here. Instruction reads from
the original task are reused under their unchanged snapshot identities.

No author, root, original independent, prompt, Git, PR, audit, lock, or other
chat artifact was changed. New files are confined to this
`exposed_comparison/` directory. The parent may use the accepted restricted
mathematics while preserving the scope and effective-selection boundaries
above. Any packaging edits need their actual final-source confirmation;
this comparison does not automatically cover future changed bytes.
