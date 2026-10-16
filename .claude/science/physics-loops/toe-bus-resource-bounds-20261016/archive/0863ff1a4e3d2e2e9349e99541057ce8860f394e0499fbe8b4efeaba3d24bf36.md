---
title: Positive static-bias transfer with occupied-path and box suppliers
claim_id: positive_bias_suppliers_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
conditional_surface_status: conditional full-output transfer with positive additions on supplied occupied paths and qualified padded boxes
status: proposed_retained
audit_required_before_effective_retained: true
bare_retained_allowed: false
canonical_parent_binding_complete: true
upstream_dependencies:
  - strongly_regular_bus_bounded_theorem_note_2026-10-15
runner: scripts/positive_bias_suppliers_2026_10_16.py
next_trace_action: current-main/cumulative-stack integration checks and independent retained audit remain separate
---

Claim type: bounded_theorem.

A fixed positive nearest-neighbor chain can supply arbitrarily small strong spectral biases for an arbitrary computable old Hamiltonian on the same finite qubit path. Under the qualified routed-bus hypotheses, attenuation and endpoint compensation then recover the literal old dynamics over a finite observation window with all old, reference and controller outputs retained and a common accuracy-independent added incident-strength cap. A rectangular-box reduction is available only with explicit filler, corner-access, occupied-edge-control and exterior-vacancy premises. No native hardware supplier, favorable runtime, global-energy bound or generic single-port implication follows.

This is a new source-only wrapper around unchanged mathematical bodies. The four qualified source acceptances are transfer `8353563cf50ce83eaf16c1fcb68776051721f95d58ccf5804733869947c7bc0b`, explicit edge `440ae5bf806f3487a273e3c1092f9b65c1c186afccb649323996805d09881357`, occupied path `382531923d20c156d6d05b6a440b26ac11af64e934950738e14fbd452c9a24e4`, and box `89eec7c08dbbeedfe0ca311d1dcc4065a125870b6c59ea4829afccd105fee80f`. Their exact final qualifications are reproduced below. These decisions do not accept this wrapper, its new code, canonical integration, publication or retained status. Historical pending statements remain original text; the later path and box acceptances govern the present composition.

## 1. Exact parent, complete inputs and scope

The direct mathematical parent is the qualified strongly-regular-bus note, repository source [strongly regular bus bounded theorem](STRONGLY_REGULAR_BUS_BOUNDED_THEOREM_NOTE_2026-10-15.md), 83,919 bytes, SHA256 `1733b2962df77699f6dcf13538916cc0a9780802ea82a93a8c56c373a717700b`. Its publication record identifies regular PR9631 and head `68c531309ac6dae96289aab964213b8c5f55969b`; this is exact parent provenance, not a new local base or current HEAD observation. Its exact-target support qualification and separately attributed rational-Hermitian repair remain controlling. Older compiler, mediator and Lie-certificate material mentioned in historical bodies is context or a statement of supplied interfaces, not an independently imported theorem conclusion for this composition. The exact source/archive map records those distinctions; Git ancestry is not a mathematical dependency rule.

Fix the complete old plant, all original apparatus and memories included, and its literal computable onsite/ordinary-nearest-neighbor Hermitian H in fixed physical units. Supply a computable target unitary W, a dimensionless local Hermitian port B, a fixed positive time unit t_*, a finite window w with computable upper bound, and computable names for the full matrices and finite installed block/reserve data, or effective access sufficient for the stated certified operations. Norm majorants alone do not provide these names. Without effective data, keep fixed-instance existence distinct from an algorithm. Reference factors are arbitrary and passive. No old factor is initialized, discarded, reassigned or silently excluded to improve the spectrum.

Additional permissions are material: install the specified positive additions on existing old sites and edges, attenuate them to chosen positive strengths, maintain their calibration throughout the actual lifetime, and supply the parent's actual vacant bus embedding, source preparation, phase/timing reference and isolation. A single accessible port does not entail old-edge control or vacant exterior corridors. The mathematical arbitrary-H Gram statement by itself does not waive the parent's physical locality and decomposition conditions.

## 2. Positive transfer and the order of choices

Write a permitted bias as C=sum C_alpha, with supplied reserves r_alpha making each C_alpha+r_alpha I positive; R_C=sum r_alpha and J_C is the maximum incident sum of these positive block norms. The physical addition is lambda(C+R_C I). The original theorem assumes one supplied strong point H+C: simple complete energies, distinct positive pair gaps, and all energy-basis off-diagonal entries of B nonzero. It does not infer that point from Lie controllability. Section 3 supplies a different sufficient route that need not have a strong point at lambda=1.

Let d be the full old dimension, m=d(d-1), and

```
F_j(lambda)=ad_(H+lambda C)^(j+1) B,       j=0,...,m-1,
p_H(lambda)=det[Tr(F_j(lambda)^* F_k(lambda))]_(j,k).
```

This is a real nonnegative polynomial of degree at most D=m(m+1). Its positivity is equivalent to the stated strong conditions: the signed nonzero energy differences must provide m distinct modes and every corresponding B entry must be nonzero. The complex Hilbert-Schmidt adjoint is essential. If p_H(1)>0, the polynomial is not zero; D+1 distinct rational nodes in any sufficiently small positive interval cannot all vanish. Dovetailed certified lower bounds detect a strictly positive node without an equality oracle. Neither conditioning nor efficient search follows.

Choose lambda sufficiently small that lambda w a_C<=epsilon/16, where c_C is a supplied computable scalar and a_C>=||C-c_C I||. The physical scalar lambda R_C is separately paid for the whole lifetime. The finite-window comparison is

```
||e^(-iu(H+lambda C))-e^(-i lambda c_C u)e^(-iuH)||
    <=lambda u a_C,                  0<=u<=w.
```

Endpoint compensation does not assume lambda T is small. Uniform source-length, complete-space gap, calibration region, response and corrector bounds are first obtained for the whole Hermitian target ball ||M||<4. Then choose xi and T=t_*/xi^2. Only after the actual T is fixed, search rational Hermitian M with ||M||<4 and

```
||e^(-iM)-U_T||<epsilon/16,
U_T=e^(iT(H+lambda C)) W e^(-iTH).
```

An existential Hermitian logarithm of norm at most pi and rational density prove termination; no discontinuous logarithm branch or exact-zero decision for arbitrary computable entries is required. Rational M has decidable support. Later target-dependent calibration remains inside the already established uniform region. Strict rational witnesses avoid equality tests at computable boundaries. Arbitrarily tiny choices do not imply a stated favorable asymptotic runtime.

For t=T+u, the complete ideal output is

```
e^(-i chi(t)) Phi(t) tensor [e^(-iuH) W e^(-iTH)],
chi(t)=R_total t+c_M xi^2 t+lambda c_C u.
```

The bracket acts on the entire old/reference input with reference identity; Phi(t) retains every bus and source factor and its actual comparison evolution. R_total is the sum of all actual installed reserves, including lambda R_C when required. There is no additional lambda c_C T in chi: U_T compensates the complete biased evolution through T. This bookkeeping does not remove the physical scalar installed throughout [0,T+w]. The accepted transfer allocation gives unhalved trace error at most 7epsilon/8 under its full preparation and generator-error budgets. Both old time flows, the full window, source fluctuations and bare-input corrector errors remain those of the parent proof. An integrated generator-error allowance alone does not imply a pointwise incident-strength cap.

## 3. A fixed positive supplier on an occupied path

Assume all n old qubits lie on a specified ordinary-nearest-neighbor Hamiltonian path, with the endpoint used as the port, and that the following additional onsite and edge blocks are permitted there. For each fixed n, a computable finite chain A_n with simple energies, distinct positive gaps and every off-diagonal entry of B_n=I+X_n+Z_n nonzero is constructed once, independently of H, W and accuracy.

Start A_1=Z_1, B_1=I+X_1+Z_1. Given A on d levels, append

```
A'=A tensor I+omega I tensor Z+g B tensor X,
omega>old spectral range,       g>0.
```

At g=0, only two copies of each old gap and d copies of 2omega repeat. The second-order difference between the two sign branches is

```
D_a=sum_b 4omega |B_ab|^2/[4omega^2-(E_a-E_b)^2].
```

For d>=3 a unique old gap from row a to a third index supplies a pole absent from row b, so D_a-D_b is not the zero rational function. For the first d=2 step, the specified diagonal squares 4 and 0 give D_a-D_b=4/omega; the identity in the starting B matters. Choose a rational omega avoiding finitely many zeros. The new endpoint port I+X+Z has nonzero same-level opposite-sign transitions at order zero. For distinct old levels, its same-sign first-order coefficient is `B_ab 4sigma omega/[4omega^2-(E_a-E_b)^2]`, and its opposite-sign coefficient is `-2sigma B_ab/(E_a-E_b+2sigma omega)`. Both are nonzero.

The unchanged chain proof supplies explicit Riesz-projector and Cauchy remainder bounds and strict rational g thresholds preserving every transition and splitting every repeated gap. This is an analytic all-n induction, not numeric genericity. Certified strict searches are computable from the constructed data but have no efficient resource bound.

The actually added chain is positive block by block:

```
C_n=A_n+R_n I,
R_n=1+sum_(j>=2) omega_j+3sum_(j>=2)g_j,
C_n=(I+Z_1)+sum_(j>=2) omega_j(I+Z_j)
       +sum_(j>=2)g_j[3I+(I+X_(j-1)+Z_(j-1))X_j].
```

Each edge block has minimum eigenvalue (2-sqrt(2))g_j and norm (4+sqrt(2))g_j. With w_1=1,w_j=omega_j and e_j=g_j, taking e_1=e_(n+1)=0, the incident load is bounded by

```
J_C=max_j [2w_j+(4+sqrt(2))(e_j+e_(j+1))].
```

Both incident path edges count. The identity R_n is already physically present in these blocks: use C=C_n and R_C=0 in the transfer, avoiding double payment. H retains coefficient one; no -H cancellation is introduced.

For this fixed supplier, the leading coefficient of p_H(s) is exactly p_C>0, with degree D=m(m+1). The signed-gap Vandermonde proves positivity of p_C. Thus p_H is nonzero for every H even when H+C_n itself fails to be strong. D+1 small positive rational nodes and strict positivity selection supply H+sC_n in the transfer's required window budget. The preserved exact discriminator H=-C_2 has p_H(1)=0 and a positive small-node witness; the theorem does not assume p_H(1)>0. Norm bounds may use h+||C_n|| uniformly for s<=1. The common added cap includes sJ_C, with J_C fixed for the fixed path. Nothing here states a uniform cap as n or the complete old plant changes.

## 4. Explicit two-qubit Heisenberg edge

On exactly two old neighboring qubits, retain H=3I+XX+YY+ZZ and permit the added positive blocks 2lambda(I+YY),8lambda(I+ZZ). Their sum is lambda C with C=10I+2YY+8ZZ; each endpoint receives the full added incident load 20lambda. The four energies in the ordered Bell basis are

```
0, 4+4lambda, 4+16lambda, 4+20lambda.
```

All positive gaps are distinct for lambda>0 except lambda=1/3,1/2. The local B=(X+2Y+3Z) tensor I has six nonzero lower-triangular entries 3,2i,-1,1,-2i,3. Its diagonal entries are zero, consistent with the parent's off-diagonal premise. An identity-shifted port is a different optional operator, not a silent repair.

For 0<lambda<=1/4, both minimum gap and distinct-gap separation equal 4lambda, ||H_lambda||<=9, and each endpoint's added load is <=5. Here R_C=0, J_C=20, c_C=a_C=10 in the fixed energy unit. Actual scalar action 10lambda(T+w) remains paid. Taking lambda strictly below min(1/4,epsilon/[16a_C(t_*+w_bar)]) pays the window defect. The same actual-T chronology and phase above apply; the resulting conditional cap can be written 5+R_s+7M_E+2/t_* with fixed R_s>=9 and the parent's fixed coefficient-box majorant M_E. Shrinking gap 4lambda can force severe runtime and precision costs.

Access to the anisotropic YY and ZZ blocks on this existing edge is an extra permission. Onsite control or an isotropic exchange path does not imply it. Arbitrary passive reference inputs are allowed, but interacting spectators may not be removed to retain the four-dimensional spectrum. This exact example does not claim the chain theorem for a different physical access domain.

## 5. Qualified rectangular-box reduction and correlated fillers

For a box {0,...,a-1}x{0,...,b-1}x{0,...,c-1}, a,b,c>=1, define the two-dimensional snake S by increasing y and traversing x forward on even y, backward on odd y. Traverse S on even z and reversed S on odd z. Consecutive layers join at equal x,y; all sites occur once. Reflection in chosen coordinate axes, followed if needed by reversal of the entire path, gives a Hamiltonian path ending at any chosen corner. The proof covers every side-length-one case. Corner choice and physical availability are distinct: at an upper corner the outward direction may be positive, and an existing interior port is not relocated by drawing a path.

To use the box as the complete old path, supply actual qubits on genuinely vacant filler sites, all required occupied-site and edge additions, an accessible chosen corner, and the parent's vacant exterior bus embedding and isolation. Arbitrary occupied graphs do not automatically have a Hamiltonian path, and occupied sites cannot be overwritten. Fix the box independently of accuracy; all its qubits count in the plant dimension and resources.

For idle, decoupled fillers F and original plant O, take

```
H_S=H_O tensor I_F,       W_S=W_O tensor I_F,
e^(-iuH_S) W_S e^(-iTH_S)
   =[e^(-iuH_O)W_O e^(-iTH_O)] tensor I_F.
```

This operator identity holds on every correlated OFR state, including mixed states. The full comparator retains F and passive R; tracing out F or replacing it with a product is not the theorem. The complete isometry bound tensors with reference identity and gives unhalved trace error at most twice its operator-norm error, uniformly over those inputs. Additional supplied preparation error is paid in the parent's full-state budget.

A separately root-attributed extension allows a known computable decoupled filler drift H_F. It explicitly changes the full comparator:

```
H_S=H_O tensor I+I tensor H_F,
e^(-iuH_S) W_S e^(-iTH_S)
   =[e^(-iuH_O)W_O e^(-iTH_O)] tensor e^(-i(T+u)H_F).
```

This is not the frozen idle-filler identity claim. The actual drift, its norm and any scalar cost enter the complete plant ledger. Couplings between O and F invalidate this factorization and require a different full-plant target. The preserved GHZ/Z_F example gives orthogonal full outputs when a nonidle filler evolution is silently dropped. It is a narrow comparator counterexample, not an architecture no-go.

## 6. Supporting negative findings and evidence limits

The fixed-bias continuing-window argument rules out only endpoint compensation followed by passive continuation with a fixed nonscalar bias on a positive window. Attenuation is precisely the successful route used here; switching, continuing compensation and other architectures remain outside that failed route.

The separately root-attributed Heisenberg appendix proves a second narrow implication failure. Three positive generators can generate u(4), with the preserved exact determinant -4 certificate, while no static Hermitian bias confined to one designated qubit supplies the bus's all-transition condition for any one-qubit port. Common SU(2) rotation reduces the bias to cI+rZ; either the spectrum is degenerate or the distinct |00>,|11> eigenstates have zero one-qubit transition. Genuine old-edge biases, extra-site biases, larger ports and different architectures escape the quantified family. The explicit edge example uses one such stronger permission.

The historical static-bias no-go submission remains FAIL/partial-narrowing: its checklist does not have a publication-gate PASS, five architecture families and exhaustive historical echo coverage are not closed. This packet does not promote it to a broad no-go or claim unrelated alternatives must fail. These counterexamples are exactly scoped supporting findings of a positive conditional theorem.

All scientific executions are historical. Transfer checks include finite complex Grams, exclusions, calibration samples and a rational-certified post-time target witness; they do not simulate a complete accuracy family. Edge checks are exact four-dimensional algebra. Chain checks include bounded exact perturbative identities, a p_H(1)=0 discriminator, and separately labeled noncertified high-precision samples; the exposed reviewer checks a noncommuting example. Padding enumerates finitely many boxes and tests exact correlated-state identities; the universal geometry is proved analytically. The two structural-equality diagnostic failures and their corrected exact simplifications remain in the archived evidence. No historical executable is replayed here.

The same model and effort were retained. Review exposure and prior parent authorship differ across packets and remain recorded; there is no new independent model-family status, blind example selection, or fresh independent recheck of every parent. The historical padding review's pending-chain sentence remains unchanged. Later root acceptance supports the present conditional composition, not a retrospective edit of that history.

The new primary and its scoped corruption controls check exact source bytes, intervals, recovery and metadata only. Their outcomes are not theorem tests, a favorable scientific PASS total or retained-audit verdicts. Actual source-at-launch packaging receipts are separate from historical scientific receipts. Native source preparation, calibrated small coefficients, actual release time and lifetime isolation, measured-energy identification, readable records and reset/reuse remain open. A common incident cap is not a global norm, energy, action, runtime or precision bound. No scientific executable, publication, canonical binding or editable-prompt change occurs in this draft.

## 7. Immutable bodies and controlling qualifications

The following original bodies occur exactly once, without rewriting historical statuses or phases. BODY_MAP gives byte intervals and source hashes. SOURCE_MANIFEST and ARCHIVE_INDEX recover the selected original freezes, reviews, launch sources, receipts, streams and failures. Hash verification is provenance, not a substitute for reading the proofs. The parent note is an exact external dependency with a recovery snapshot; this source-only draft has no actual local base observation or canonical root-review approval.


---

## Unchanged source: transfer_author

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Fixed-bias window obstruction and transfer by attenuating a supplied bias

Status: exposed author continuation and conditional theorem proposal. The frozen routed-bus argument remains a provisional dependency pending independent review; this note does not upgrade its status. The fixed-coefficient transfer and the attenuated-bias construction below are different claims. Keeping a nonscalar bias at full strength generally obstructs arbitrary accuracy on a fixed positive observation window. If scaling the added bias blocks is admissible, one supplied strongly regular bias direction suffices to construct small strongly regular biases, and the complete conditional transfer can then be made noncircular.

The exact parent is `strongly_regular_bus_candidate/DERIVATION.md`, 40,500 bytes, SHA256 `855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2`, frozen at 2026-10-16T00:44:47.390997Z. It is preserved unchanged. Its complete argument was read; the actual-time, corrector and resource parts were reread for this task. Source identities, exposure and read limits are recorded separately. Before this freeze the root also reported a proposed rational-Hermitian support repair from its pending checker. Only that message was received, not the checker's source. Sections 3 and 5 give the explicit bounded-log search and support prescription used here; they are not presented as independent confirmation of that message.

## 1. Premises and the two distinct questions

Fix the complete finite old qubit plant, literal computable H, arbitrary old/reference input, target unitary W, physical time unit t_*>0, and finite window w>=0. Preserve every term of H with coefficient one. Retain the old-port/vacant-exterior geometry of the bus parent, every controller output, and its supplied state/calibration/isolation conditions.

Supply a Hermitian old bias C with an actual finite old onsite/NN decomposition

    C=sum_alpha C_alpha,
    C_alpha+r_alpha I >=0,       r_alpha>=0,
    R_C=sum_alpha r_alpha,
    J_C=max_v sum_(alpha incident on v)||C_alpha+r_alpha I||.

These reserves are real installed blocks, not a formal subtraction. All quantities are finite and computably bounded. Supply one local Hermitian port B such that H+C has simple complete energies, distinct positive pair gaps, and B_ab!=0 for every off-diagonal pair in that energy basis. If every diagonal B_aa is also nonzero, that stronger condition is harmless but unnecessary here. No statement that the original augmented Lie certificate supplies such C or B is made.

For the *unchanged-bias question*, C stays installed at coefficient one throughout the experiment. Section 2 proves endpoint transfer with a fixed-window defect, and an explicit counterexample rules out a vanishing defect for this route in general.

For the *attenuated-bias question*, one may choose a constant 0<lambda<=1 for each accuracy instance and install the static positive blocks

    lambda(C_alpha+r_alpha I).

Their total unreserved addition is lambda C, reserve lambda R_C, and incident load at most lambda J_C. This scales added bias blocks only, never H. The ability to choose those added coefficients is explicit. If C is an immutable original term or must remain at coefficient one, this second construction is unavailable. Section 6 shows that, given the supplied strong point H+C, no additional hypothesis of strong regularity at every small lambda is needed.

Write H_lambda=H+lambda C; use lambda=1 for the unchanged-bias question. Set

    c_C=(lambda_max(C)+lambda_min(C))/2,
    C_0=C-c_C I,
    a_C=||C_0||=(lambda_max(C)-lambda_min(C))/2.

Choosing this scalar for the comparison does not remove any installed scalar or reserve. Its full physical cost remains in the above blocks.

## 2. Correct endpoint algebra and the window obstruction

There are two related target unitaries, which should not be conflated. If the bus theorem is written with its own gate G_T, its endpoint is G_T exp(-iT H_lambda). The gate required to reproduce W exp(-iTH) is therefore

    G_T=W exp(-iTH) exp(iT H_lambda).              (1)

The corresponding **interaction-frame** target is

    U_T=exp(iT H_lambda) W exp(-iTH)
       =exp(iT H_lambda) G_T exp(-iT H_lambda).    (2)

Thus the expression exp(iT H_lambda)Wexp(-iTH) is not itself the gate G_T in the original bus comparator. Below we construct the mean interaction directly to approximate U_T, which gives the same correct ordering without ambiguity.

Suppose an ideal interaction-frame rotation has implemented U_T at time T, and its additional action during the window tends to zero as in the bus holding estimate. At t=T+s its old endpoint-anchored comparator is

    exp(-isH_lambda) W exp(-iTH).                 (3)

Relative to the desired exp(-isH)Wexp(-iTH), a scalar phase lambda c_C s removes only the identity part of the continuing bias. Duhamel gives

    ||exp(-isH_lambda)-exp(-i lambda c_C s)exp(-isH)||
        <=lambda s a_C.                          (4)

This bound is independent of W and T because the right endpoint factor is unitary. Consequently fixed C permits arbitrarily accurate endpoint transfer, but the direct window estimate retains lambda w a_C in isometry norm, or 2lambda w a_C in trace norm. At fixed lambda=1 and w>0 this term does not vanish as the bus error is reduced.

There is a genuine route obstruction, not just an inadequate upper bound. Let U_s and V_s be the unitary channels generated by H+C and H. For any endpoint channel A and desired endpoint channel B, the triangle inequality and unitary invariance imply

    ||U_s B-V_s B||_diamond
        <=||A-B||_diamond+||U_s A-V_s B||_diamond.  (5)

Therefore any comparator which simply continues under H+C has worst error across 0 and s at least half the channel distance between those two drifts. The same conclusion follows with the supremum of trace distance over old/reference states. Controller comparison phases cannot change this reduced-old lower bound.

Concrete counterexample: one old qubit, H=0, C=Omega n with Omega>0, W=I, B=X+Z/3, and w=pi/Omega. C is an actual positive onsite block, H+C has simple energies and one distinct positive gap, and B has nonzero off-diagonal entries (and nonzero diagonals). At an exact corrected endpoint the old input |+> is still |+>, but continuation for s=w gives |-> up to phase. Its trace distance from the desired |+> is 2. Even allowing an endpoint compromise, (5) gives worst error at least 1. A bus family whose residual and extra holding rotation tend to zero cannot remove this lower bound while keeping that full bias on.

More generally, if w>0 and the two drift channels agree at every s in [0,w], differentiation at s=0 gives [C,rho]=0 for every matrix rho, hence C is scalar. Thus any fixed nonscalar C has a positive projective/channel window defect somewhere in every positive window. This is a statement about the continuing-bias route. It does not rule out a different autonomous device that actively compensates or switches the bias, and it is not a universal impossibility theorem. In the counterexample, simply omitting C already realizes the trivial target.

## 3. A computable bounded approximate logarithm without a branch or zero oracle

For any computable finite unitary U and any eta>0, one can find a rational Hermitian matrix M in a supplied computable orthonormal basis such that

    ||M||<L_max=4,       ||exp(-iM)-U||<eta.       (6)

Here rational means real rational diagonal and rational real/imaginary parts off diagonal, with Hermiticity imposed exactly. Enumerate these matrices and dovetail certified strict tests of the two inequalities in (6). The finite-dimensional spectral theorem supplies *existentially* a Hermitian logarithm L0 with ||L0||<=pi and exp(-iL0)=U. Rational Hermitian matrices are dense; approximating L0 sufficiently closely gives both strict inequalities, using the finite Hermitian Duhamel bound

    ||exp(-iM)-exp(-iL0)||<=||M-L0||.

Since pi<4, a strict interior witness exists, and the dovetailed search terminates. Matrix exponentials and norms have computable certified enclosures in finite dimension. A candidate lying exactly on a test boundary need not be decided and cannot block the search. No branch of a principal logarithm, exact spectral projection at a unitary branch cut, or equality test for arbitrary computable complex entries is required.

The support of M is decidable because its entries are rational. For M_ab!=0, M_ab/|M_ab| is computable; for M_ab=0 set its source coefficient to zero and choose any supplied source phase. This distinction is essential: the analogous support test for an arbitrary exact computable logarithm is not justified. Fixed-target finite-real existence with an exact L and effective approximation by (6) are different assertions.

The search in (6) will be run on U_T only *after* T is fixed. Uniform bus bounds over the whole Hermitian ball ||M||<=4 make that ordering possible.

## 4. Uniformizing the bus construction over a bounded Hermitian ball

Fix for this section a strongly regular drift H_lambda, its port B, a source size N and the target bound L_max=4. All constants below may depend on H_lambda and N; none depends on a subsequently selected M with ||M||<=L_max. They need not stay bounded as lambda tends to zero, except for the base incident coefficients discussed in section 7.

Use the bus parent's notation k=d-1, m=2k, q=d(d-1)/2, b=m+4q and R=4q routing edges. Its diagonal target differences range in the fixed box

    y_a=(M_aa-M_00)/t_*,       |y_a|<=2L_max/t_*.

The parent's positive-cone matrices F_+,F_- and strictly positive null vector c_weight are independent of y. Its exact zero-routing weights have the form

    w(y)=(F_+^{-1}y,0)+beta c_weight.             (7)

On a small closed cone-valid box of core energies, choose beta sufficiently large that every weight is bounded below by a common positive number for every such y. This is constructive: bound ||F_+^{-1}|| and the target box, and divide the resulting possible negative component by a certified positive lower bound on each component of c_weight. All weights and their sums then have finite uniform upper bounds. The same beta works throughout a smaller closed core-energy box. The resulting actual Jacobi core has those fixed eigenvalues for every y.

The full zero-routing Q/P separation can now be selected exactly as in the parent, after N is fixed. It depends on the core energies, router frequency and ferromagnetic scale, but not the weights or target y. It may be computed at any fixed dummy weights, for example the y=0 solution: zero-routing isospectrality makes the certificate valid for every target in the box. The finite affine exclusions are nontrivial, and the terminating strict-gap search yields delta_0>0. A branched XY bus is still not treated as free fermions: only the zero-routing core path has that representation.

Hold the negative-side weights fixed after these spectral parameters are selected. The positive-side center x0(y) in (7) ranges over a compact set strictly inside the positive orthant. Choose one radius r>0 whose balls around all centers lie inside a fixed compact positive box X. On X choose common bounds S_min>0, S_max, and M_J for the Jacobi derivatives. The parent's moment-Gram/Vandermonde bounds make these computable; no exact target support is needed here.

Set delta_C=min_(a,b,j)|E_a-E_b-mu_j|>0. Choose a preliminary routing cap with nu-3rho-omega_max>=Delta_R>0, and retain the parent's positivity condition 3rho<mu_min/2. Its uniform Schur-resolvent constants on X can be taken to be

    C0=4sqrt(k)S_max||B||^2/delta_C^2,
    C1=k||B||^2(4/delta_C^2+12S_max M_J/delta_C^3).

Select a single rho>0 satisfying those conditions and

    R rho<delta_0/2,
    e=rho^2/Delta_R<=delta_C/2,
    ||F_+^{-1}|| C0 e<=r/2,
    ||F_+^{-1}|| C1 e<=1/2.                     (8)

For each y the same contraction map, centered at x0(y), has a positive fixed point x*(y) in its ball. The parent gives exact diagonal calibration there. The full Q/P gap is at least delta=delta_0/2 for **every** positive weight choice in X: at zero routing the core is isospectral, and the complete qubit routing perturbation has norm <=Rrho. Thus simultaneous calibration does not invalidate the already chosen uniform gap.

There is also a positive uniform lower bound on every root-to-leaf response. Let t_min>0 bound all Jacobi core off-diagonal entries below on X. Explicitly, write Delta_j for the j-by-j moment Gram determinant, with Delta_0=1. The jth Jacobi off-diagonal square is Delta_(j+1)Delta_(j-1)/Delta_j^2. The parent's positive Vandermonde-minor lower bounds on each Delta and finite moment upper bounds therefore give a computable positive t_min, uniformly on X. Let D_bus bound ||B_bus-omega_l I|| above for all l and x in X. The unique path to leaf l contains all m core vertices, 3l backbone vertices and its leaf; hence it has m-1 core hoppings, 3l+1 router hoppings and b-m-3l-1 off-path vertices. The exact tree cofactor identity gives

    |G_l| >= g_l,min
       :=t_min^(m-1) rho^(3l+1)
           Delta_R^(b-m-3l-1)/D_bus^b >0.         (9)

Every off-path component is a high-frequency router subtree; its eigenvalue distance from omega_l is at least Delta_R. The denominator bound is |det(B_bus-omega_l I)|<=D_bus^b. Equation (9) uses no compactness assertion about an unverified nonzero response and has the correct units of inverse energy. Very small g_l,min makes runtime large, not local strength large.

Let v_p,min=sqrt(S_min), v_p,max=sqrt(S_max). For the source attached to pair a>b, define the finite target-independent bound

    r_l,max=2L_max/[t_* v_p,min |B_ab| g_l,min].   (10)

The parent's exact coefficient r_l(M) obeys this bound. Full Q/P separation bounds each source resolvent (L_l+lambda_j-omega_l)^(-1) by 1/delta, as proved there by comparison with an allowed code state. Consequently its self-energy coefficients satisfy

    |A_l|,|B_l|<=r_l,max^2/delta,
    |u_l^ct|<=r_l,max^2/(N delta),
    |v_l^ct|<=2r_l,max^2/(N delta).               (11)

This includes the nonsymmetric source resolvent; it is not a one-particle substitute for full separation. Valid uniform complete-space and positive incident-load bounds are therefore

    v_bar=v_p,max||B||+sum_l r_l,max >=||V||,
    a2_bar=3 sum_l r_l,max^2/delta >=||A2||,
    ell_V,bar=2v_bar,
    ell_2,bar=5 max_l r_l,max^2/(N delta).        (12)

The exact paid counterterms and their actual scalar reserves still depend on M and are installed as in the parent; they have not been deleted by the bounds (11).

The parent's connected-transition gap gamma_PP depends only on H_lambda's simple energies and distinct pair gaps, not M. It classifies the possible nonzero changes E_a-E_b, omega_l-omega_l', E_a-E_b+/-omega_l. It does not classify arbitrary integer relations among all code energies. With D_c=d(N+1)^q, uniform corrector majorants are

    z1=sqrt(D_c) v_bar/delta,
    d_bar=v_bar z1+a2_bar,
    z2=sqrt(D_c)d_bar(1/delta+2/gamma_PP),
    r3_bar=v_bar z2+a2_bar z1+z1 d_bar,
    r4_bar=a2_bar z2+z2 d_bar,
    C_bar=2(z1+z2)+(t_*+w_bar)(r3_bar+r4_bar),   (13)

where w_bar>=w. These are the parent's column/Frobenius bounds, now uniform over every bounded target M. Its complete-source fluctuation coefficient also satisfies

    B_M=(1/t_*) max_a sqrt(sum_(b!=a)|M_ab|^2)
          <=L_max/t_*,                          (14)

because each row Euclidean norm is at most ||M||. Thus N, the bus spectral/routing parameters and xi can all be selected before M or U_T is known. This closes the target/time circularity at the level of the stated finite constructive bounds, conditional on the bus algebra.

## 5. Direct interaction-frame implementation and exact choice order

Use the parent's calibrated diagonal and source terms with entries of M itself. Their exact second-order code generator is

    D=c_M I+sum_a M_aa/t_* |a><a|
       +sum_(a>b)[kappa_ab |a><b|S_(l,-)/N+h.c.],
    |kappa_ab|=2|M_ab|/t_*.

For each decidably nonzero rational M_ab choose the source's unit phase

    exp(i phi_l)=(M_ab/|M_ab|)(kappa_ab^*/|kappa_ab|).  (15)

For M_ab=0 its actual source coupling is zero and its phase is arbitrary. Then the mean generator is M/t_* directly, not a time-conjugated logarithm. Equivalently, in the original bus theorem use L_gate=exp(-iT H_lambda)M exp(iT H_lambda). Its diagonal and off-diagonal magnitudes are those of M, and its phase factor exp(-i omega_l T) cancels the theorem's exp(i omega_l T). Its support is still determined by rational M. This explains (15) without invoking an exact-support test for the generally nonrational entries of L_gate.

The following order is noncircular for an already fixed strongly regular H_lambda:

1. Fix a desired error tolerance, L_max=4 and w_bar. Choose N using (14).
2. Select the cone energy box, full Q/P separation, common rho and all bounds (8)–(14), uniformly for the entire bounded target ball.
3. Choose xi>0 using those uniform constants and load bounds; define T=t_*/xi^2.
4. Only now compute U_T in (2), and run the strict rational-Hermitian search (6). It terminates with ||M||<4 and the chosen eta_log error.
5. Solve the already certified contraction for this M, set its exact source magnitudes and counterterms, and choose the decidable phases (15). These actual coefficients satisfy the bounds used in step 3, so T is not recomputed.
6. Supply the stated controller input and physical calibration. All design/search is before the declared experiment timeline. Evolution of the old plant during design would require the separate chronological input contract already present in the parent.

Hardware, reserves and controller phases may depend on the selected M and hence on T. That dependence is consistent: the previously selected T is justified by bounds uniform in M. No implicit equation T=f(T) remains.

Let Phi(t) be the full parent controller vector: bus vacuum times every freely evolving source product state at actual time t. Let

    R_total=R_s+lambda R_C+R_bus(M)
                   +xi R_V(M)+xi^2 R_A2(M).

All reserve terms are their actual installed values. At t=T+s, the complete nominal output isometry differs from

    exp[-i(R_total t+c_M xi^2 t)] Phi(t)
                  tensor exp[-it H_lambda]exp(-i xi^2 t M/t_*)

by at most

    xi C_bar+(t_*+w_bar)L_max/(t_*sqrt(N)).       (16)

This is the parent's complete-output reduction plus fluctuation bound, with identity on an arbitrary passive reference. The final scalar-adjusted original-H comparator is

    exp[-i chi(t)] Phi(t)
                     tensor exp(-isH)Wexp(-iTH),
    chi(t)=R_total t+c_M xi^2 t+lambda c_C s.    (17)

The additional terms in isometry error are respectively the continuing mean rotation, approximate log and nonscalar bias:

    E_iso <= xi C_bar
        +(t_*+w_bar)L_max/(t_*sqrt(N))
        +xi^2 w L_max/t_*+eta_log+lambda w a_C. (18)

There is no extra lambda c_C T in (17): U_T compensates the entire biased evolution through T, including its scalar part. The scalar lambda c_C s is only the window comparison. The physical bias reserves lambda R_C remain in R_total for the full duration T+s. All scalar parts of the literal H remain in its two displayed old time evolutions. Normalized trace gains the actual contribution lambda[s_C+R_C], s_C=Tr(C)/d, in addition to the parent's full ledger; nothing is silently discarded.

At w=0, (18) proves arbitrarily accurate endpoint transfer with the unchanged bias lambda=1. At w>0 it gives an explicit conditional transfer whenever lambda w a_C is sufficiently small. It does not turn a fixed nonzero a_C into an all-accuracy fixed-window theorem. No assumption that lambda T is small is used: U_T compensates the full biased aging through T, even when the eventual runtime grows much faster than 1/lambda.

## 6. A supplied strong bias direction produces arbitrarily small strong biases

This new algebraic lemma avoids assuming that generic controllability supplies a bias. It uses the particular supplied pair (C,B) whose strong point at lambda=1 is already a premise.

Let n=d(d-1), A_lambda(X)=[H+lambda C,X], and form the n Krylov vectors in the complex Hilbert–Schmidt space

    F_j(lambda)=A_lambda^(j+1)(B),    j=0,...,n-1.

Define their Gram determinant

    p(lambda)=det[Tr(F_i(lambda)^* F_j(lambda))]_(i,j=0,...,n-1).  (19)

For real lambda, p is a real nonnegative polynomial with computable coefficients and degree at most

    D=n(n+1).                                    (20)

Indeed F_j is polynomial of degree at most j+1. A determinant product has degree at most sum_i[(i+1)+(sigma(i)+1)]=n(n+1). Complex conjugation affects coefficients, not the real variable lambda.

At a simple-energy point, in the old energy-operator basis |a><b| the nonzero components are

    (F_j)_ab=(E_a-E_b)^(j+1) B_ab,       a!=b.

If all nonzero pair differences Delta_ab are distinct and all B_ab are nonzero, the square n-by-n column matrix is a nonzero diagonal factor diag(Delta_ab B_ab) times a Vandermonde matrix in the distinct Delta_ab. Its Gram determinant is strictly positive. In particular p(1)>0 under the supplied strong-point premise.

Conversely, p(lambda)>0 forces all the strong conditions. If an old energy is degenerate, the nonzero-eigenvalue subspace of A_lambda has dimension d^2-sum_r m_r^2<n, where m_r are its energy multiplicities. Every F_j lies in that subspace, so its rank is below n. If energies are simple but nonzero differences repeat, the Krylov span has dimension at most the number of distinct nonzero eigenvalues of A_lambda, again below n. With all differences distinct, any vanishing B_ab removes the corresponding eigenoperator component and again lowers the rank. Therefore

    p(lambda)>0
      iff H+lambda C has simple energies, distinct positive gaps,
             and all off-diagonal B_ab nonzero.  (21)

The sign-paired nonzero differences do not cause a rank defect: positive and negative gaps are distinct for a simple spectrum, and the Krylov span is taken over the complex Hilbert–Schmidt space. The diagonal part of B is automatically killed by the first commutator.

Because p(1)>0, p is not the zero polynomial. For any positive rational Lambda<=1, use the D+1 distinct rational nodes

    lambda_j=Lambda j/(D+2),       j=1,...,D+1.  (22)

At least one node has p(lambda_j)!=0 because a nonzero degree-at-most-D polynomial cannot vanish at all D+1 nodes. Since p is nonnegative, that value is positive. Refine certified evaluations at all nodes in parallel/dovetail until one strict positive lower bound is obtained. The procedure terminates without deciding zero at any other node. This supplies an actual lambda in (0,Lambda) with a strict strong-regularity certificate. It can be arbitrarily small, although no favorable conditioning or search precision is promised.

The resulting simple spectrum can be isolated by computable finite eigenvalue enclosures. Rank-one spectral projectors and a computable eigenbasis can then be obtained by choosing a coordinate with certified nonzero projection and normalizing; distinct-gap and nonzero-matrix-element certificates can be refined from (21)'s guaranteed strict properties. No exact-energy-degeneracy oracle is needed at the chosen node.

Thus the positive result requires only one supplied admissible strong bias direction and the admissibility of scaling its added blocks. It does not assert that an arbitrary original H admits such a direction on the available old geometry, nor that the original Lie certificate implies one.

## 7. Complete accuracy family and one common incident cap

Assume attenuation is admissible. Fix once and for all finite bounds h>=||H|| and c_bound>=||C||. All H_lambda with 0<lambda<=1 have norm <=h+c_bound and positive gaps <=2(h+c_bound). Choose the cone pole offsets below 1/t_*; then core eigenvalues can always lie below 2(h+c_bound)+1/t_*. Choose the router-frequency interval, ferromagnetic-scale interval and preliminary routing cap from fixed finite energy bounds above these values. For example a router interval above 4(h+c_bound)+4/t_*, a ferromagnetic interval [1/t_*,2/t_*], and rho<=1/t_* suffice as outer bounds before the smaller target-specific restrictions. Hence one finite M_E bounds every base onsite and edge coefficient uniformly in lambda, N and epsilon, even though gaps and responses can become arbitrarily small.

Choose fixed R_s>=h+c_bound, J1=J2=1/t_*. Counting the actual bias blocks as well as the full parent ledger gives the common added incident bound

    J_*=J_C+R_s+7M_E+J1+J2.                      (23)

The lambda-scaled bias load is <=J_C. The fixed reserve R_s, source fields, ferromagnetic edges, bus onsite/hopping reserves, weak port/source blocks and xi^2 counterterm reserves are all counted. No old term is removed and no strong counterterm is ignored. The fixed tree geometry and old site occupancy are unchanged; only the source lengths grow. As in the parent, a perturbed implementation needs the actual incident budgets or explicitly charged fixed slack in addition to an integrated generator-error bound.

For each 0<epsilon<=1, the complete order is:

1. Choose a rational Lambda>0 no larger than

       min{1, epsilon/[16(t_*+w_bar)(a_bar+1/t_*)]},

   where a_bar>=a_C is fixed and finite. Run (22) to choose a strong lambda<Lambda. Then lambda w a_C<=epsilon/16. Only the added C blocks are attenuated.
2. Use L_max=4 and choose an integer

       N>=max{2,[16(t_*+w_bar)L_max/(t_*epsilon)]^2}.

   Rational upper bounds may be used to choose the integer without a boundary equality test.
3. Treat this certified H_lambda as the current drift. Perform the uniform construction of section 4, including all full-gap and counterterm bounds, before a target logarithm is selected.
4. Choose a positive rational xi no larger than

       min{1,
           epsilon/[16(C_bar+1)],
           sqrt[epsilon t_*/(16(t_*+w_bar)(1+L_max))],
           J1/(ell_V,bar+J1),
           sqrt[J2/(ell_2,bar+J2)]}.             (24)

   All right sides are positive computable reals; a certified smaller positive rational can be found. Set T=t_*/xi^2.
5. Compute U_T, find rational Hermitian M satisfying (6) with eta_log<epsilon/16, and instantiate the exact calibrated controller and phases as in section 5. The earlier constants bound this actual M, so no runtime revision is needed.

All five terms in (18) are <=epsilon/16. Thus the complete nominal isometry error is <=5epsilon/16 and the corresponding trace-norm error, uniformly with arbitrary reference, is <=5epsilon/8. An actual initial state within epsilon/8 of the supplied controller product tensored with its exact unconditional old/reference marginal contributes at most epsilon/8. A self-adjoint complete-generator calibration satisfying

    integral_0^(T+w)||E(t)||dt<=epsilon/16

contributes at most epsilon/8 in trace norm. The total is <=7epsilon/8<epsilon. The unspent slack does not silently supply an arbitrary timing/release uncertainty; any additional error must have its own bound. Exact nominal initialization/generator set these allowances to zero.

The physical source phases and precision are supplied after T is known, as in the parent. No source formation law, isolated old-neighbor supplier, native clock, or long-runtime calibration mechanism has been derived. Coefficients may be extremely small or require extreme precision. Added-source size is explicitly chosen above; no polynomial runtime, inverse-gap, polynomial-grid evaluation precision or total design-complexity claim is made.

## 8. Disposition and precise remaining boundary

For an unchanged non-scalar C at coefficient one, this note proves a conditional endpoint transfer and exposes the fixed positive-window defect. The one-qubit example refutes the assertion that merely replacing the endpoint target closes the full-window task. Scalar C is the special case whose continuing action is absorbed by the explicit comparison phase.

For a scalable added bias direction C whose point H+C is already strongly regular for the supplied port, equations (19)–(24) give a conditional all-accuracy original-H transfer with one common incident cap. The proof explicitly orders N, small bias, uniform bus constants, xi/T and the time-dependent rational logarithm. This is an attenuated-bias construction, not a claim that full-strength C disappears from the window.

The original generic Lie-certificate problem remains open at the premise: it has not been shown to supply one admissible strongly regular old bias direction on the available geometry. If such a direction is absent or attenuation is forbidden, alternatives include an actual autonomous bias switch or a continuing compensator whose full-space error, output and local cost are proved. No such switching/compensation construction is supplied here. The exact unresolved design equation for keeping full C while removing its window action is a post-endpoint old interaction that tracks the inverse relative drift exp(i(H+C)s)exp(-iHs), uniformly on [0,w], with all controller outputs and costs paid; endpoint calibration alone does not solve it.

The routed-bus parent's independent review is still pending. Any defect found there affects this conditional continuation. The present new lemmas and uniformization also require independent assessment. No canonical files, Git/PR state, prompts, axioms, other chats, locks or previous freezes were changed. Only this assigned output directory was written.


---

## Unchanged source: occupied_path_author

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Positive old-path bias supplying a strong spectral point

Status: exposed proof development and analytic stress test of a root-proposed induction. The construction below completes that induction under explicit old-site/path-edge access. It is a conditional mathematical supplier, not a blind derivation, a retained audit result, a proof of the original access axioms, or a physical preparation/energy theorem. The disclosed proposal and exact qualified parents are pinned in `SOURCE_MANIFEST.json`.

## 1. Statement and access premises

Fix an ordered path through all n>=1 old qubits, with its last site available as the parent's local port. All numerical energy coefficients below are expressed in one fixed positive energy unit. On every site and every edge of this **existing occupied old path**, permit adding the positive onsite and two-site blocks displayed below, with positive rational coefficients that may be attenuated. This is additional interaction access. It is not inferred from access to a single old port, a Lie-algebra certificate, or vacant exterior sites. If the occupied graph has no specified Hamiltonian path, this theorem makes no graph-reduction claim. Extra original old edges/terms can remain: the arbitrary old H in the final algebraic step is retained literally.

There is a rational real-symmetric nearest-neighbor Hamiltonian A_n and fixed endpoint operator

    B_n=I+X_n+Z_n

such that A_n has simple spectrum, distinct positive pair gaps, and every off-diagonal energy-basis element of B_n is nonzero. A positive sum of allowed blocks C_n=A_n+R_n I has the same properties. Its coefficients and incident load are finite and fixed once n and the selected path are fixed; they do not depend on the later accuracy parameter or on the arbitrary original H.

For every computable Hermitian H on these sites and every positive computable upper bias budget Lambda, one can find a positive rational s<Lambda for which H+s C_n has those same strong properties for the same endpoint B_n. No premise that H+C_n is strong is needed. This last construction retains every original H term with coefficient one; C_n is constructed independently of H, and no -H cancellation is performed.

With the qualified static-bias transfer and bus premises, this supplies the missing strong-bias direction on this access domain. It does not supply the parent's vacant exterior geometry, initialized sources, long-time calibration, timing, isolation, operational energy interpretation, readable records, or reset/reuse.

## 2. Induction and all zero-coupling gap classes

Start with A_1=Z and B_1=I+X+Z. The eigenvalues are +1,-1; there is one positive gap, and the off-diagonal port entry is 1. Suppose A on d=2^k dimensions already has the stated properties, with eigenpairs (E_a,|a>) and endpoint B. Choose omega larger than the old spectral range r=max E_a-min E_a, and define

    H_0=A tensor I+omega I tensor Z,
    V=B tensor X,
    A'(g)=H_0+gV,
    O=I tensor (I+X+Z).

The zero-coupling eigenvectors |a,sigma>, sigma=+1,-1, have energies e_(a,sigma)=E_a+sigma omega. They are simple. Every cross-sign positive gap is

    2omega+E_a-E_b > r,

whereas every same-sign positive gap is at most r. Thus the two classes cannot collide. Among cross-sign gaps, nonzero ordered differences E_a-E_b are all distinct, while a=b gives precisely d copies of 2omega. Every old positive gap appears precisely twice, once in each sign sector. These are all repeated positive gaps. This classification uses omega>r, not merely absence of level degeneracy.

First-order energy shifts vanish because X has zero diagonal in the Z basis. With the convention that d_(a,sigma) is the coefficient of g^2, not the second derivative itself, elementary second-order perturbation gives

    d_(a,sigma)=sum_b |B_ab|^2/(E_a-E_b+2sigma omega),
    D_a=d_(a,+)-d_(a,-)
       =sum_b 4omega |B_ab|^2/[4omega^2-(E_a-E_b)^2].       (1)

The b=a term is included. Omitting it would break the first induction step.

The two copies of an old positive gap E_a-E_b split at order g^2 by D_a-D_b. The d cross-sign gaps initially equal to 2omega acquire order-g^2 coefficients D_a. Therefore pairwise distinct D_a split every repeated class.

## 3. A rational omega with all splitting coefficients distinct

For d>=3, fix a!=b and choose c different from both. In D_a-D_b, the summand involving the unordered old pair {a,c} has a pole at omega=|E_a-E_c|/2 with residue |B_ac|^2/2, which is nonzero. No term in row b has that pole: uniqueness of all positive old gaps says that only the unordered pair {a,c} has this absolute difference, and b is not an endpoint of that pair. No other term in row a cancels it. Thus D_a-D_b is a nonzero rational function of omega.

The pole is outside the selected interval omega>r. Its role is to prove a rational-function identity is nonzero, not to place the device close to a resonance. A nonzero rational function has finitely many real zeros away from its poles. There are only finitely many pairs a,b. Hence every open interval above r contains omega for which all D_a differ; rational choices are dense and also exist.

The first step has d=2 and needs a separate argument. In the Z eigenbasis the diagonal entries of B_1 are 2 and 0 and both off-diagonal moduli are 1. The off-diagonal contributions to D_+-D_- cancel, while the diagonal ones give

    D_+-D_-=4/omega !=0.                         (2)

The general d=2 assertion would be false for a port with equal squared diagonal entries. The particular base is essential; after it, the qubit induction has d>=4 and the pole argument applies.

For effectiveness, choose a rational interval (L,L+1) with L>r, enumerate its rational points, and dovetail strict tests |D_a-D_b|>0 for every pair. At least one rational point passes. The input A at every induction stage is rational symmetric; simple algebraic eigenvalues and their rank-one projections are computable. The weights |B_ab|^2 can equivalently be computed as Tr(P_a B P_b B), avoiding an eigenvector-phase convention. Certified strict tests terminate at a good point, without deciding zero at a bad point. No lower bound on the good point's separation or complexity is asserted.

## 4. Explicit analytic neighborhood and energy remainders

This section supplies a quantitative analytic neighborhood rather than an appeal to numerical genericity. Fix a chosen omega. Let gamma>0 be a certified lower bound on the minimum spacing of the e_(a,sigma), and let beta>=||B|| be a rational bound (beta=3 suffices here). Put

    rho=gamma/(16 beta).

On the circle of radius gamma/3 around each e_i, the H_0 resolvent has norm at most 3/gamma. For complex |g|<=rho, a Neumann series gives

    ||(z-A'(g))^(-1)|| <= (3/gamma)/(1-3/16),
    ||P_i(g)|| <=16/13<2,
    ||P_i(g)-P_i(0)|| <=3/13.                   (3)

Here P_i(g) is the contour integral of the resolvent. The contours are disjoint. The projections are analytic and remain rank one, since their ranks are locally constant and equal one at zero. Thus each enclosed eigenvalue lambda_i(g) is analytic. These statements also follow directly from the convergent contour Neumann series, so no unquantified perturbative threshold is being used.

For completeness, normality of H_0 implies that any spectrum of H_0+gV lies within beta|g| of its old spectrum: outside those disks, the same inverse Neumann criterion holds. The disks are disjoint here and each contour contains one branch. Consequently

    |lambda_i(g)-e_i|<=beta|g|.

Conjugation by I tensor Z changes g to -g while fixing H_0. Uniqueness of the enclosed eigenvalue then gives lambda_i(g)=lambda_i(-g). Only even powers occur. Solving the first-order eigenvector equation and substituting into its next order gives (1). Cauchy's coefficient estimate on |g|=rho, using |lambda_i(g)-e_i|<=beta rho, now yields for real |g|<=rho/2

    lambda_i(g)=e_i+g^2 d_i+r_i(g),
    |r_i(g)| <= C_E |g|^4,
    C_E=2 beta/rho^3.                            (4)

Indeed the even-power tail is at most beta rho (|g|/rho)^4/[1-(|g|/rho)^2], bounded by the displayed allowance. The factors have the correct energy dimensions when g,omega,A are measured in the same fixed units.

Let delta_D>0 be a certified lower bound on min_(a!=b)|D_a-D_b|. Let tau>0 be a certified lower bound on the separation between any two *distinct values* among the zero-coupling positive gaps. The explicit classification in section 2 determines their repeated classes; no equality oracle for unspecified spectra is needed. There are finitely many strict differences to certify.

For real g, a gap changes by at most 2 beta |g| and the difference of two gaps by at most 4 beta |g|. Thus previously distinct gap values remain distinct if g<tau/(8 beta). A difference between two initially equal gaps is g^2(D_a-D_b) plus at most 4 C_E g^4. It is nonzero if

    g^2 < delta_D/(8 C_E).                       (5)

The radius condition in (3) also keeps the eigenvalues simple and ordered as at zero. Equations (4)-(5) therefore prove all positive gaps distinct for every sufficiently small positive g, with an explicit finite sufficient threshold.

## 5. Endpoint transitions, including conjugates and a uniform remainder

Use the convention B_ab=<a|B|b> and Delta=E_a-E_b. The first-order correction to |a,sigma> is

    sum_c [B_ca/(E_a-E_c+2sigma omega)] |c,-sigma>.

The bra correction uses its complex conjugate. For a!=b, differentiating the matrix element of O at zero gives

    same sign sigma:
      B_ab[1/(Delta+2sigma omega)+1/(-Delta+2sigma omega)]
      =B_ab 4sigma omega/(4omega^2-Delta^2),

    opposite signs sigma,-sigma:
      B_ab[(1-sigma)/(Delta+2sigma omega)
           -(1+sigma)/(Delta+2sigma omega)]
      =-2sigma B_ab/(Delta+2sigma omega).         (6)

These formulas include the identity in O; its two first-order terms cancel by orthogonality. Both coefficients are nonzero. For a=b and opposite signs, the zeroth-order transition is 1. These cases exhaust all off-diagonal new-state pairs. No assumption about old diagonal B_aa is used in (6).

A phase-independent analytic way to bound the remainder is to use the scalar

    h_ij(g)=<i|P_i(g) O P_j(g)|j>.

It is holomorphic on the same disk and |h_ij(g)|<=4 o for o>=||I+X+Z|| (take o=3). Its zeroth/first coefficients are those just calculated. For real g, P_i(g) is an orthogonal rank-one projection; (3) implies the overlaps with the old vectors are nonzero. Thus h_ij(g)!=0 is equivalent to a nonzero actual energy-basis transition. No nonholomorphic eigenvector normalization is slipped into the complex Cauchy estimate.

For |g|<=rho/2, Cauchy's estimate gives

    |h_ij(g)-h_ij(0)-g h'_ij(0)| <=8 o g^2/rho^2,
    |h_ij(g)-h_ij(0)| <=8 o |g|/rho.            (7)

Let kappa>0 be a certified lower bound on the moduli of all coefficients (6). A sufficient simultaneous choice is

    0<g<min{rho/2, tau/(8 beta), sqrt[delta_D/(8 C_E)],
             kappa rho^2/(16 o), rho/(16 o)}.    (8)

For transitions whose zeroth coefficient vanishes, (7) leaves at least half the nonzero linear term. For the remaining opposite-sign/same-a transitions, it leaves modulus at least 1/2. Together with section 4 this completes the induction. Every quantity bounding g is positive and computably certified after omega is fixed. A strictly smaller positive rational can be selected, so A' again has rational entries. No floor/ceiling of an arbitrary computable real or equality test at a threshold is required.

As an alternative effective termination argument, the analytic proof ensures a nonempty interval of good g; the finite complex Krylov positivity test in section 7 can be dovetailed over positive rational g tending to zero. Equation (8) is a more explicit sufficient construction. Neither method promises useful conditioning or polynomial complexity.

## 6. Actual positive blocks, support and scalar accounting

Writing omega_j,g_j for the choices made when attaching site j>=2, the unreserved chain is

    A_n=Z_1+sum_(j=2)^n omega_j Z_j
             +sum_(j=2)^n g_j (I+X_(j-1)+Z_(j-1)) X_j.

Install instead the following fixed positive bias blocks:

    onsite at 1: I+Z_1;
    onsite at j>=2: omega_j(I+Z_j);
    edge {j-1,j}: g_j[3I+(I+X_(j-1)+Z_(j-1)) X_j].         (9)

The first two types are positive semidefinite. Since ||I+X+Z||=1+sqrt(2)<3, the edge bracket has minimum eigenvalue 2-sqrt(2)>0 and norm 4+sqrt(2). The I tensor X_j part is contained in the edge support; it is not a hidden longer-range coupling. Summing (9) gives exactly

    C_n=A_n+R_n I,
    R_n=1+sum_(j=2)^n omega_j+3 sum_(j=2)^n g_j.            (10)

All identities in (9) are local installed reserves. They shift energies but leave gaps and energy eigenvectors unchanged. Every A_n term has zero full trace, hence Tr(C_n)/2^n=R_n. The bias is nontrivial even for n=1 and has a finite actual incident norm sum. If w_1=1 and w_j=omega_j, and e_j=g_j is the edge joining j-1 to j with e_1=e_(n+1)=0, its exact decomposition gives

    J_C=max_(1<=j<=n) [2w_j+(4+sqrt(2))(e_j+e_(j+1))].     (11)

This cap is independent of the later target accuracy. It need not be bounded uniformly in n, total norm, numerical precision or runtime.

For the static-bias parent's notation, use C=C_n with each summand (9) already positive and additional r_alpha=0, hence R_C=0. The reserve R_n is inside C_n and is not paid a second time in R_C. Alternatively one could use unreserved A_n and explicit R_C=R_n, but then all drift and scalar conventions must change consistently. This note uses the first convention throughout.

## 7. A leading Gram coefficient supplies small strong H+sC_n

Let d=2^n, m=d(d-1), and write ad_G(X)=[G,X]. In the complex Hilbert-Schmidt space form the m columns

    F_j(s)=ad_(H+sC_n)^(j+1)(B_n), j=0,...,m-1,
    p_H(s)=det[Tr(F_i(s)^*F_j(s))]_(i,j=0)^(m-1).        (12)

For real s this is a nonnegative real polynomial. Its degree is at most D=m(m+1), since column F_j has degree at most j+1 and each determinant product has total degree sum_i[(i+1)+(pi(i)+1)]=m(m+1). Crucially its leading column coefficient is ad_Cn^(j+1)(B_n). Therefore the coefficient of s^D is exactly

    p_C=det Gram{ad_Cn^(j+1)(B_n)} >0.             (13)

There are no lower-column terms of the same total degree to cancel this coefficient. In a C_n energy basis, the m nonzero-difference rows of the column matrix are

    Delta_ab B_ab (1,Delta_ab,...,Delta_ab^(m-1)), a!=b.

They form an invertible diagonal matrix times a Vandermonde matrix with distinct real nodes. This proves p_C>0. Thus p_H has **exact degree D**, independently of H, even if p_H(1)=0. The addition of the scalar R_n in C_n changes neither these commutators nor p_C.

For any Hermitian G, positivity of this Gram is equivalent to the strong conditions. A degeneracy with energy multiplicities r_l leaves the nonzero adjoint-eigenspace dimension d^2-sum_l r_l^2<m, so the columns cannot be independent. If energies are simple but a nonzero difference repeats, a single starting vector B has at most one Krylov direction in that whole adjoint eigenspace; the number of distinct nonzero differences is then below m. If all those differences are distinct but some B_ab=0, the corresponding eigenoperator is missing. Conversely, the Vandermonde calculation proves positivity when all three strong conditions hold. The positive and negative differences are separate nodes, and the span is complex; no mistaken real-Hermitian rank restriction is used.

Given a positive computable Lambda, first select a rational 0<Lambda_0<=Lambda. At the D+1 distinct positive rational nodes

    s_j=Lambda_0 j/(D+2), j=1,...,D+1,           (14)

not all p_H can vanish: a nonzero polynomial of degree D has at most D distinct real roots. Since each value is nonnegative, at least one is strictly positive. Dovetail certified interval evaluations at these finitely many nodes until a positive lower bound appears. Computable names for H and all required quantities, not just norm bounds, are needed for this effective assertion. Zero values at other nodes need never be decided.

The selected H+sC_n is computable with a certified simple spectrum. Its eigenvalues and rank-one projectors can be isolated; selecting a coordinate of each projector with certified positive norm supplies a computable normalized eigenvector. Strict gap and port certificates can then be refined. No uniform lower bound on any resulting separation, required precision or design time is claimed.

## 8. Composition with the qualified transfer, without new cancellation

Construct C_n once and fix finite norm/load bounds. For each target accuracy choose Lambda as small as the qualified static-bias window budget requires, and use (14) to select a strong s. This replaces only the parent's premise p(1)>0; its conclusion of arbitrarily small strong biases and all subsequent target-uniform construction remain applicable. Every literal term of H stays present with coefficient one, and only the positive added blocks s times (9) are attenuated. Their incident load is at most J_C for s<=1.

In the parent's notation set H_s=H+sC_n, c_C=(lambda_max(C_n)+lambda_min(C_n))/2, and a_C=(lambda_max(C_n)-lambda_min(C_n))/2. The window defect is bounded by s w a_C after its explicit scalar comparison. The exact order remains: select s and certified H_s; choose N and all bounds uniformly over the rational-Hermitian target ball ||M||<4; choose xi and actual T=t_*/xi^2; only then find a rational Hermitian M approximating

    U_T=exp(iT H_s) W exp(-iT H).

The post-time target/calibration cannot be used to retroactively change T. All finite design and preparation precede the declared experiment input; any old evolution during design requires the parent's separate chronological input contract. The complete comparator retains every bus/source output and every old/reference factor, with literal old flows exp(-iuH) W exp(-iTH), 0<=u<=w. Its scalar phase is exactly the qualified parent's

    chi(T+u)=R_total(T+u)+c_M xi^2(T+u)+s c_C u.             (15)

Here R_C=0 by the convention in section 6. There is no extra s c_C T: the interaction-frame target already compensates H_s through T. The actual scalar contribution s R_n inside H_s has not been deleted from the hardware, trace ledger, or synthesis target.

The parent's bound remains

    E_iso <= xi C_bar+(t_*+w_bar)4/(t_*sqrt(N))
                +xi^2 w 4/t_*+eta_log+s w a_C.            (16)

Its prescribed choices make each term <=epsilon/16, nominal trace-norm error <=5epsilon/8, and total <=7epsilon/8 after the separately supplied preparation and integrated-calibration allowances. The common incident cap is J_C+R_s+7M_E+J1+J2, with the same fixed finite base bounds and full positive reserves as the parent. Spectral separations can shrink as s does; the parent allows that by shrinking xi and increasing actual duration. No upper bound on that duration, phase precision, coefficient search, preparation work or total energy follows here.

The proof is valid for w=0 as well as w>0 and for scalar targets; neither case requires cancelling H. A fixed nonzero bias is not asserted to disappear during a positive window. No old-site addition permission, occupied Hamiltonian path, or exterior preparation/calibration mechanism is inferred from the original single-port hypotheses.

## 9. Analytic stress tests and evidence boundary

In the displayed two-level base, simply deleting the identity from the old endpoint B does not work. For a generic d=2 pair, equal squared diagonal entries make D_a-D_b identically zero despite nonzero off-diagonal B; the second-order argument would then not establish splitting. The complex conjugation in (6), the b=a contribution in (1), and the quartic energy remainder are all retained. The Cauchy estimates use holomorphic projectors rather than incorrectly treating normalized complex eigenvectors as holomorphic.

The static-bias parent's supplied-point premise p(1)>0 is unnecessary for this stronger direction: H=-C_n makes H+C_n scalar and destroys strong regularity at s=1, while p_H(s)=(s-1)^D p_C is positive at every s!=1. This is a stress example for the leading-coefficient proof, not a design that sets C=-H; the actual supplier was fixed without reading H. No commutation between a general H and C_n is used in the leading-coefficient argument: mixed commutator words have lower powers of s, and the unique highest-power word uses C_n at every step.

One bounded author-check execution is attached. A complete 6-by-6 characteristic determinant with a genuinely complex Hermitian old port independently extracts all six second-order energy coefficients and agrees exactly with (1). Dropping the diagonal terms gives exact nonzero residuals. Complete projector-derivative matrices verify all 24 distinct-old-label transition slopes, including the complex opposite-sign example -2/9-2i/9; a reversed sign gives a nonzero residual. An independent 80-digit eigensolver samples three successively halved g values; those samples are numerical checks, not rigorous interval bounds.

For the rational two-qubit choice omega=3, g=1/10, exact Krylov arithmetic gives p_C>0. Deleting the identity from the old coupling port gives Krylov rank 8 rather than 12, an even characteristic polynomial, and hence a failed strong-point mutant. This g is a separately certified finite witness; it is not claimed to satisfy the deliberately conservative sufficient threshold (8). For H=-C_2, direct exact Grams give p_H(1)=0 and p_H(1/7)>0, and agree with the degree-156 homogeneity identity. Full values, executable bytes and complete receipts are in `AUTHOR_CHECK.md` and `check_run_01/`.

These finite checks do not establish the all-n theorem by enumeration. The universal result is the analytic induction and polynomial argument above. This packet does not independently revalidate all historical bus/controller executions, confer retained status, or identify K with a laboratory energy observable. No editable prompts or physical axioms changed.


---

## Unchanged source: explicit_edge_author

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# A positive bias on the existing Heisenberg edge supplies a strong spectral point

Status: exposed author derivation with a bounded exact algebra check. This note proves a finite-dimensional spectral proposition for the specified two-qubit plant. Its possible autonomous-controller consequence remains conditional on the separately frozen bus and static-bias-transfer arguments and their physical premises. It does not upgrade those arguments, assert independent acceptance, or infer an admissible bias from generic Lie controllability.

The answer to the bounded algebra question is positive. The proposed edge bias has an explicit positive local decomposition. At coefficient one the energies are `0,8,20,24`; the six positive gaps are distinct, and the proposed one-qubit port has a nonzero matrix element for every off-diagonal transition. More strongly, every `0<lambda<=1/4` works, with minimum positive gap and minimum separation between distinct positive gaps both exactly `4lambda`. Installing and attenuating that particular anisotropic bias on the already occupied old edge is an additional physical permission.

All numerical generator coefficients below are in the fixed physical unit already used to specify the parent `H`. If that unit is denoted `E_u`, multiply every displayed Hamiltonian, gap and incident-strength number by `E_u`; `lambda` is dimensionless and `B` is dimensionless. This is notation for the fixed original units, not an accuracy-dependent rescaling of `H`. Expressions involving time use those same units, with `hbar=1` as in the parents.

## 1. Exact proposition and explicit domain

Let two already present old qubits occupy neighboring sites `p,q`, with `p` the designated port. Write `AA=A_p tensor A_q`, and let `I` denote the identity on the complete four-dimensional old plant. Preserve the literal old operator

    H=3I+XX+YY+ZZ.

Assume that one may **add**, on this same old edge, the two static blocks

    lambda C_Y=2lambda(I+YY),
    lambda C_Z=8lambda(I+ZZ),       lambda>0.       (1)

Their sum is `lambda C`, where

    C=10I+2YY+8ZZ,
    H_lambda=H+lambda C,
    B=(X+2Y+3Z)_p tensor I_q.                    (2)

No coefficient or term of the literal old `H` is removed, attenuated, or globally rescaled. The expressions `XX+(1+2lambda)YY+(1+8lambda)ZZ` below are only algebraic totals of the old and added blocks.

**Proposition.** For every `lambda>0`, `H_lambda` has simple energies. For every

    lambda>0,    lambda not in {1/3,1/2},          (3)

its six positive pair gaps are distinct and every off-diagonal energy-basis matrix element of `B` is nonzero. At every `0<lambda<=1/4`,

    min_(a>b)(E_a-E_b)=4lambda,
    min_(distinct positive gaps g,h)|g-h|=4lambda,
    min_(a!=b)|B_ab|=1,
    ||B||=sqrt(14),
    ||H_lambda||=4+20lambda<=9.                 (4)

The added incident block-norm load at **each** old endpoint is exactly `20lambda`, at most `5` on this interval. Every added block in (1) is positive on the entire two-qubit Hilbert space. The proposition is uniform over arbitrary old states and any passive reference because it is an operator statement on the entire old space; no Bell-state preparation is assumed.

Here “every transition” means every **off-diagonal** pair. The proposed `B` has zero energy-basis diagonals. That satisfies the actual premise in the frozen bus and transfer notes. Section 4 separately gives a one-qubit identity shift if a consumer explicitly asks for every matrix entry, including diagonals, to be nonzero.

## 2. Positive local decomposition and literal scalar cost

The tensor Pauli operators square to `I` and have eigenvalues `+1,-1`. Hence `I+AA` is positive with spectrum `0,0,2,2`. Therefore

    C_Y=2(I+YY)>=0,     ||C_Y||=4,
    C_Z=8(I+ZZ)>=0,     ||C_Z||=16.              (5)

Both are ordinary two-qubit nearest-neighbor blocks on the same existing edge. This is not a decomposition over additional physical neighbor channels. Both norms count at both endpoints, giving `20lambda` incident load. The sum itself has norm `20`, as the exact spectrum below confirms, so treating it as one positive edge block gives the same load.

The specified mathematical old operator also admits the finite positive edge-block decomposition

    H=(I+XX)+(I+YY)+(I+ZZ).                      (6)

Consequently a positive decomposition of the total operator is the three blocks in (6) plus the two added blocks in (1). Their block norms are respectively `2,2,2,4lambda,16lambda`. Equation (6) distributes the already present `3I`; it introduces no additional scalar. If a physical old-term ledger separately declares each bare Pauli summand as an immutable nonpositive channel, (6) does not by itself authorize changing that channel convention. The present added blocks are individually positive regardless of that convention; a stronger rule on separately positive literal old channels remains a separate supplied premise.

The added scalar coefficient is exactly

    Tr(lambda C)/4=10lambda.                    (7)

It is physically installed in (1), not dropped as an irrelevant phase. Those `2lambda I` and `8lambda I` are already paid. In the notation of the frozen transfer note one may take its bias blocks `C_alpha` to be `C_Y,C_Z`, with `r_alpha=0`, hence

    R_C=0,   J_C=20,   c_C=10,
    ||C-c_C I||=10.                              (8)

The last norm is a comparison bound; subtracting `10I` for that bound does not subtract it from the physical generator. Further bus, weak interaction or calibration reserves, if used, must be paid separately according to the parent construction. Equation (5) does not supply them.

## 3. Complete energies and every positive gap

Use the ordered orthonormal Bell basis

    |0>=|psi->=(|01>-|10>)/sqrt(2),
    |1>=|psi+>=(|01>+|10>)/sqrt(2),
    |2>=|phi+>=(|00>+|11>)/sqrt(2),
    |3>=|phi->=(|00>-|11>)/sqrt(2).               (9)

The following table follows by applying each Pauli tensor to these four vectors; it also lists all old and bias eigenvalues.

| a | Vector | XX | YY | ZZ | H | C | H+lambda C |
|---|---|---:|---:|---:|---:|---:|---:|
| 0 | psi- | -1 | -1 | -1 | 0 | 0 | 0 |
| 1 | psi+ | 1 | 1 | -1 | 4 | 4 | 4+4lambda |
| 2 | phi+ | 1 | -1 | 1 | 4 | 16 | 4+16lambda |
| 3 | phi- | -1 | 1 | 1 | 4 | 20 | 4+20lambda |

All three tensor Pauli operators commute, so this is a simultaneous diagonalization, valid for every real `lambda`. For `lambda>0` the four listed energies are strictly increasing. In particular, the positivity of `C` is exact, with eigenvalues `0,4,16,20`; its maximum eigenvector is also the maximum eigenvector of `H_lambda`, proving the exact norm in (4).

At `lambda=1`,

    H+C=13I+XX+3YY+9ZZ,
    (E_0,E_1,E_2,E_3)=(0,8,20,24).              (10)

Here are all six positive gaps, with the corresponding transition entries derived in section 4.

| Pair (a,b), a>b | E_a-E_b | Value at lambda=1 | B_ab | abs(B_ab)^2 |
|---|---:|---:|---:|---:|
| (1,0) | 4+4lambda | 8 | 3 | 9 |
| (2,0) | 4+16lambda | 20 | 2i | 4 |
| (3,0) | 4+20lambda | 24 | -1 | 1 |
| (2,1) | 12lambda | 12 | 1 | 1 |
| (3,1) | 16lambda | 16 | -2i | 4 |
| (3,2) | 4lambda | 4 | 3 | 9 |

At coefficient one their sorted list is `4,8,12,16,20,24`, proving distinctness. For the whole positive half-line, split the six affine functions into

    A={4+4lambda,4+16lambda,4+20lambda},
    D={4lambda,12lambda,16lambda}.              (11)

Within either set no two members coincide at a positive `lambda`. A cross equality has the form `4+a lambda=b lambda`, with `a` in `{4,16,20}` and `b` in `{4,12,16}`. A positive solution requires `b>a`. The only possibilities are

    4+4lambda=12lambda  at lambda=1/2,
    4+4lambda=16lambda  at lambda=1/3.           (12)

This exhausts all fifteen pair comparisons and proves (3), including the exact exceptional strengths. The energies remain simple at both exceptions; only the distinct-positive-gap condition fails. At `lambda=0` the original triplet degeneracy returns. This failed endpoint and the two failed interior strengths are retained rather than concealed by a genericity statement.

For `0<lambda<1/3` the sorted gap list is

    4lambda < 12lambda < 16lambda < 4+4lambda
            < 4+16lambda < 4+20lambda.          (13)

Its five adjacent differences are

    8lambda, 4lambda, 4-12lambda,
    12lambda, 4lambda.                          (14)

At `0<lambda<=1/4`, `4-12lambda>=4lambda`; every other adjacent difference is also at least `4lambda`, with equality attained. Any nonadjacent difference is a sum of adjacent positive differences. This proves the second equality in (4) on the entire interval, not merely at sampled points. The first follows from (13). Including the negative gaps or zero in the separation calculation cannot lower the resulting `4lambda` bound: opposite-sign nonzero gaps differ by at least `8lambda`, and the distance to zero is at least `4lambda`. Zero itself is of course the repeated diagonal commutator eigenvalue, not a distinct transition.

For rational `lambda` all these energies and gaps are exact rationals. The full old basis in (9) is explicit. No exact-equality oracle for arbitrary computable coefficients is being used. This finite fact does not by itself certify the full controller Q/P spectral separation or its off-code inverses.

## 4. Exact local port matrix and the diagonal caveat

On the basis (9), direct application of the one-site Pauli operators gives

    X_p|psi->=-|phi->,    X_p|psi+>=|phi+>,
    Y_p|psi->= i|phi+>,   Y_p|psi+>=-i|phi->,
    Z_p|psi->= |psi+>,    Z_p|phi+>=|phi->.

The remaining actions follow by Hermiticity, or by the same two-component calculation. Thus

              [  0    3   -2i   -1 ]
    B_Bell =  [  3    0    1    2i ] .           (15)
              [ 2i    1    0     3 ]
              [ -1  -2i    3     0 ]

The six lower-triangular entries, in the order of the preceding table, are

    3, 2i, -1, 1, -2i, 3.                      (16)

They do not depend on `lambda`. Every absolute value is at least one. Since the one-site Pauli matrices anticommute in pairs,

    (X+2Y+3Z)^2=(1+4+9)I=14I,                  (17)

and `||B||=sqrt(14)`. These statements concern a single designated one-qubit Hermitian operator, not independent access to multiple old ports.

All four diagonal entries of (15) are zero, since each Bell vector has maximally mixed one-qubit marginal. The frozen bus premise needs all off-diagonal entries nonzero and expressly does not require nonzero diagonals. If the intended domain instead literally demands **all** sixteen entries nonzero, the unmodified proposed `B` fails that stronger wording. There is an explicit local repair:

    B'=I_p+X_p+2Y_p+3Z_p,                       (18)

with diagonals one and unchanged off-diagonal entries, norm `1+sqrt(14)`. If a positive local operator is wanted as well, take

    B_+=sqrt(14)I_p+X_p+2Y_p+3Z_p>=0,           (19)

whose eigenvalues are `0,2sqrt(14)` and whose Bell diagonals are `sqrt(14)`. Its norm is `2sqrt(14)`. Those are explicitly different designated port operators with their full scalar and norm cost. The proof does not silently replace the supplied `B` or omit the identity contribution from any installed port interaction.

The Bell basis is only a mathematical representation. No part of this derivation initializes, measures, discards, or moves an old qubit. Tensoring the operator identities with any reference identity preserves them exactly.

## 5. Relation to the precise onsite-only obstruction

The supplied parent probe proves a narrower obstruction for this same literal `H`: every static Hermitian bias confined to one old qubit can be rotated by a common spin rotation to `cI+r Z_p`, `r>=0`, because the isotropic `H` is invariant under that rotation. At `r=0` the triplet is degenerate. At `r>0`, the old vectors `|00>` and `|11>` are eigenvectors with distinct energies `4+c+r` and `4+c-r`; every one-qubit operator on either old site has zero matrix element between them, because the other factor is orthogonal. If additional energy degeneracies occur, simplicity already fails. Therefore no such one-site bias can supply the stated all-transition local port.

The parent script also reports an exact full `u(4)` bracket certificate for three positive generators, with determinant `-4`. This note read that complete source and receipt/streams but did not rerun or independently validate that Lie certificate. The present spectral proof does not depend on its rank calculation. The obstruction mechanism just restated follows directly from the displayed symmetry and product eigenvectors.

The new addition `2YY+8ZZ` is a two-qubit anisotropy. It splits the old triplet into three Bell eigenvectors rather than retaining a pair of fully polarized product eigenvectors along a one-site bias axis. The three Pauli components of `B` connect the three perfect matchings of these four Bell states; with all three coefficients nonzero, all six transitions occur. This explains why the successful edge bias does not contradict the onsite-only result.

An isotropic added path bond alone would not produce this anisotropy: on the two-qubit edge,

    I-SWAP=(I-XX-YY-ZZ)/2.                      (20)

An addition proportional to (20) changes the three tensor Pauli coefficients equally. It is therefore not the operation (1). Permission to install a particular positive exchange path does not automatically authorize the independent positive `YY` and `ZZ` blocks required here.

## 6. Actual geometry and the extra installation permission

The currently verified accuracy-scaled compiler source, SHA256 `c0332b37e159ecf6aaa70143f65793ee424c3df3a77e8840df91043ddf47bde2`, states in its supplied-interface section (line 38):

> The path may add interactions on existing old edges; it does not create a spare physical neighbor at a saturated site.

The same complete passage retains every original factor and requires a supplied positive ordinary-NN path and accessible one-port control. It refers to that path and its complete geometry; it does not establish an unrestricted ability to add every anisotropic old-edge Hamiltonian.

The currently verified polynomial mediator source, SHA256 `d0c250c80d25065d7b2667f22d83d53ef43419088fa7484f1c157a6408ac177f`, root section 1 (lines 364–403), assumes a nonnegative old box with accessible corner `p=(0,0,0)`. It places its first new site at `(-1,0,0)` and charges or supplies isolation of unlisted interactions. The frozen bus continuation uses the same kind of exterior premise, with one old/new edge.

For this explicit two-qubit instance one can take

    p=(0,0,0),     q=(1,0,0).                   (21)

The old edge `p-q` already supports the original Heisenberg interaction. Both blocks (1) are supported on exactly this edge and add no sites and no graph adjacency. The first bus site, if the conditional bus is used, lies at `(-1,0,0)` and is a separate physical site whose vacancy/accessibility must be supplied. The bias does not make that neighbor vacant. Old qubits remain in place; there are no erased fillers or reassigned occupied sites.

Accordingly the additional physical hypothesis is precise: **the hardware permits adding the positive blocks (1) with the chosen common static coefficient on the existing old edge while retaining the old generator, and permits choosing that coefficient arbitrarily small and calibrating it for the complete duration.** This is compatible with the geometric support restriction of ordinary NN interactions but stronger than the parent probe's onsite-only control domain. Geometry alone does not supply the required interaction coefficients, preparation, isolation, or calibration.

The new old-edge load is fully counted in (5), including its scalar. It is finite at coefficient one and bounded by five on the small interval. It is not spread over uncounted channels or hidden in the old generator's strength ledger.

## 7. What this supplies to the conditional original-H transfer

This section is a conditional substitution into the frozen transfer source, not a new verification of the whole autonomous construction. The exact transfer source is `static_bias_transfer_candidate/DERIVATION.md`, 29,555 bytes, SHA256 `500797910300ef142abfeaf9d74ad93a418d770829818ca87db748d4759425a6`. Its routed-bus dependency has SHA256 `855ee2555465e460147dfd6512ce7c942a4d851e3aee552e2675ff19550980d2`. Both are unchanged.

The present result supplies the formerly hypothetical strong bias datum `(C,B)` for this particular two-qubit plant **if** installation (1) is allowed. It further replaces the transfer note's generic finite polynomial search for a small strong `lambda` by the explicit interval (4). It does not supply a bias for any other plant or enlarge the original physical domain by logical implication.

For desired tolerance `0<epsilon<=1`, fixed positive time unit `t_*`, and certified finite window bound `w_bar>=w`, choose any certified positive rational

    lambda <= min{1/4, epsilon/[16 a_C(t_*+w_bar)]},
    a_C=10 E_u.                                (22)

One may choose a strictly smaller rational to avoid deciding equality with a computable boundary. Every such choice is already strongly regular by (4), and

    lambda w a_C <= epsilon/16.                 (23)

This makes only the **added** bias small. There is no assumption that `lambda T` is small.

For clarity, the endpoint correction required by the transfer remains

    G_T=W exp(-iTH) exp(iT H_lambda),
    U_T=exp(iT H_lambda) W exp(-iTH).            (24)

The first is the gate in a comparator `G_T exp(-iT H_lambda)`; the second is the interaction-frame target. The transfer source selects source size and uniform bounds for every Hermitian approximate logarithm of norm at most four, then selects `xi` and `T=t_*/xi^2`, and only then approximates `U_T` by `exp(-iM)` with rational Hermitian `M`. Thus this substitution does not reintroduce a circular choice of target and time or a zero/support oracle for arbitrary computable logarithm entries.

The finite-window estimate still has the explicit term

    ||exp(-isH_lambda)-exp(-i10lambda E_u s)exp(-isH)||
        <= 10lambda E_u s,       0<=s<=w.        (25)

It follows by Duhamel from (8). Here `H` and `C` actually commute, but commutation does not make the continuing nonscalar bias disappear. At fixed full strength its window defect cannot be declared arbitrarily small by endpoint correction alone; the frozen source preserves that failed route. Equation (22) is how the present small-bias family pays the window term.

Using the transfer source's own notation, the complete comparator remains

    exp[-i chi(t)] Phi(t) tensor exp(-isH) W exp(-iTH),
    t=T+s,
    chi(t)=R_total t+c_M xi^2 t+10lambda E_u s, (26)

with identity on the arbitrary passive reference. `Phi(t)` includes **every** controller factor and its actual comparison evolution. `R_total` includes all actual bus and interaction reserves; the bias-specific `R_C` is zero because its full scalar is already in the positive blocks (1). There is no omitted `10lambda E_u T`: `U_T` in (24) compensates the complete biased evolution through `T`, including its scalar, while the physical scalar action is still installed and paid for the entire lifetime.

The bias contributes at most `5 E_u` added incident strength on the small interval and `10lambda E_u(T+w)` scalar action. The drift norm is at most `9 E_u`, and the port norm stays `sqrt(14)`. Conditional on the parent's uniform base-generator construction, one may therefore use a common finite cap of the form

    J_* = 5 E_u + R_s + 7 M_E + 2/t_*,         (27)

with fixed `R_s>=9 E_u` and a fixed base coefficient bound `M_E` chosen as in the transfer source. The first term explicitly counts the existing-edge addition. Formula (27) is a substitution in that conditional proof, not a direct numerical construction of the full controller here. The source and routing coefficients, every weak counterterm/reserve, output fluctuation, full Q/P inverse, and calibration allowance still require the parent's proof. The shrinking separation `4lambda E_u` may force extremely long runtimes and extreme precision. No polynomial runtime, native physical supplier, or uniform conditioning claim is made.

## 8. Actual check evidence and preserved limits

One exact author check was executed. It forms the literal `4x4` matrices, applies the explicit Bell transform, checks the positive decompositions, computes all six symbolic affine gaps and their only two positive collision strengths, verifies every entry of (15), and proves the interval bounds by checking endpoints of the relevant affine functions. It also checks the exact norms/scalars and the optional identity-shifted port spectra. No floating-point eigensolver, propagation experiment, genericity search, bus simulation, or arbitrary-computable equality test is used.

The saved executable is `exact_bell_probe.py`, 8,038 bytes, SHA256 `c2729513574cf2695180cb946b6f3674d360814a5eec83c48f7af12a80b7fc74`. The recorder copied it to `runs/exact_bell_probe/executed_source.py` **before** launch and ran that copy. Source and executed-copy hashes match.

The actual command and working directory are recorded in `runs/exact_bell_probe/EXECUTION.json`. The executable was `/opt/homebrew/opt/python@3.13/bin/python3.13`, using Python 3.13.5 and SymPy 1.14.0. The run began at `2026-10-16T01:43:45.787554+00:00`, ended at `2026-10-16T01:43:46.781448+00:00`, and exited zero after approximately `0.9934` seconds. Its limits were a 40-second child alarm, a 50-second outer timeout, and matrices of dimension at most four. No timeout occurred.

All 62 saved assertions passed. Full stdout is 6,207 bytes, SHA256 `eef262f0a6c2793346ef187364b9e6fd5bceaed76e1ea2d281d746cfa6898751`; full stderr is empty, SHA256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`. Both streams were read completely. The count is bookkeeping, not independent evidence. The handwritten finite-dimensional proof above is the argument; the computation is a same-author consistency check with full source and streams preserved. There were no failed scientific executions for this candidate. An initial read used the wrong relative path for the parent's receipt; it returned file-not-found, and the actual `N/runs/heisenberg_static_port_probe/EXECUTION.json` was then located and read. That was a source-location correction, not a calculation result.

The exact source manifest records the parent probe/receipt/streams, current source hashes and read coverage, instruction identities, and the two unchanged previous freezes. No source from the root's other new candidates or other workers' scientific results was inspected. The root's proposed `(H,C,B)` triple was supplied in the task and is explicitly treated as exposed input.

## 9. Remaining physical and review obligations

The mathematical spectral obligation for this one triple is closed by sections 2–4, subject to ordinary checking of the displayed finite identities. The following separate obligations remain:

1. **Old-edge installation and attenuation.** Supply the positive anisotropic blocks (1), not merely a one-site control or isotropic exchange path. Preserve every literal old term and charge both blocks at both endpoints.
2. **Occupied-site geometry.** Supply the actual accessible old port and vacant exterior sites if attaching the bus; the bias adds no vacancy. Retain all old factors and charge omitted couplings or provide isolation throughout the complete runtime.
3. **Controller theorem dependence.** The frozen routed-bus and transfer constructions, including full-space Q/P separation, resolvent cancellation, simultaneous calibration, all-output fluctuation and the positive-reserve ledger, remain separate provisional dependencies. This `4x4` calculation is not their independent audit or full-device simulation.
4. **State, calibration and chronology.** Supply the controller state, coefficients, timing and full-lifetime accuracy at the actual chosen `T`; no source preparation or native timing mechanism is furnished here. Long biased aging is compensated by (24), not silently omitted. The window term and phases are paid by (22)–(26).
5. **Domain boundary.** No implication from the original generic Lie certificate to an admissible strong old bias has been proved. The parent onsite-only obstruction remains valid within its own domain. This explicit old-edge extension gives one successful example in a stronger supplied domain.

Only this assigned output directory was written. Prior freezes, source notes, Git/PR state, canonical files, prompts, axioms, caches, graphs, locks and other chats were not changed. Root owns any independent acceptance and publication decision.


---

## Unchanged source: box_exposed_review

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Exposed check of the box-padding proposal

Status: conditional mathematical review of the exact root proposal. The path construction and arbitrary-correlated-filler comparator identity below are valid. Composition with the positive-chain supplier remains conditional on that separately pending source result and on the unchanged qualified static-bias/bus premises. This is not a retained audit or a derivation of physical control access.

Two qualifications must be explicit. First, an arbitrary chosen corner need not have a globally negative-coordinate outward edge; the lower corner does, and other corners have the appropriate signed outward directions. Second, the chosen corner must actually be available as the parent's local port, including its permitted old/new coupling. A vacant exterior neighbor alone does not provide that interface, and an originally designated interior port cannot simply be relabeled as the corner.

## 1. Exact path for every positive side length

Let the filled box be

    Q={0,...,a-1} x {0,...,b-1} x {0,...,c-1},
    a,b,c positive integers, M=abc.

A translation of these coordinates handles any lattice location. Define a two-dimensional list S of length ab by rows y=0,...,b-1. At even y list x=0,...,a-1; at odd y list x=a-1,...,0. Every point of the a-by-b rectangle occurs exactly once. Within a row successive sites differ by one x edge. Between rows, the ending and starting x coordinates agree: they are a-1 after an even row and 0 after an odd row. The join is exactly one y edge.

At even z append S at height z. At odd z append the complete reversed list S at height z. Consecutive layers therefore meet at the same (x,y) coordinate: an S ending meets the first point of reverse(S), and conversely. Each such join is one z edge. Distinct layers are disjoint, and each exhausts its plane. The resulting list v_0,...,v_(M-1) is a nearest-neighbor Hamiltonian path starting at (0,0,0).

An explicit coordinate formula, useful for checking implementations, is the following. For 0<=i<M let

    z=floor(i/(ab)), r=i mod (ab),
    j=r if z is even, and j=ab-1-r if z is odd,
    y=floor(j/a), k=j mod a,
    x=k if y is even, and x=a-1-k if y is odd.

Then v_i=(x,y,z). Its final point is

    (a-1,b-1,c-1) if c and b are odd;
    (0,b-1,c-1)   if c is odd and b is even;
    (0,0,c-1)     if c is even.

All these are corners, but that second endpoint need not be any separately prescribed corner.

For a prescribed corner kappa, choose epsilon_x,epsilon_y,epsilon_z in {0,1} with kappa_l=epsilon_l(L_l-1), where (L_x,L_y,L_z)=(a,b,c). On a singleton axis choose epsilon_l=0. Define the lattice reflection

    R_kappa(x)_l=x_l if epsilon_l=0,
                    L_l-1-x_l if epsilon_l=1.

The reversed reflected list

    p_i=R_kappa(v_(M-1-i)), 0<=i<M,              (1)

is a Hamiltonian path whose **last** site is kappa. Reflections and reversal preserve nearest-neighbor adjacency and bijectivity. This is coordinate ordering of physical sites, not a physical movement or swap of qubits.

All side-length-one cases are covered without a separate parity assumption. If a=1, rows have one point and their joins are y edges. If b=1, each plane is one x row, alternately traversed between z layers. If c=1, there is only the two-dimensional snake. If two lengths are one, the construction is an ordinary line; if all three are one, it is the single vertex. The formula never divides by zero, since a and ab are positive. Singleton-axis reflections are the identity, so duplicate coordinate descriptions of corners cause no additional condition.

## 2. Exterior direction and port availability

For each axis l, a corner with kappa_l=0 has the outside neighbor kappa-e_l; a corner with kappa_l=L_l-1 has the outside neighbor kappa+e_l. If L_l=1, both are outside. Thus every corner has an outward lattice direction. In particular the lower corner (0,0,0) has all three negative-axis neighbors outside Q.

It is false that every arbitrary corner has a negative-coordinate outward neighbor. In a 2-by-2-by-2 box, the upper corner (1,1,1) has all three negative-axis neighbors inside the box. One may choose the lower corner when a fixed negative-coordinate route is required, or reflect/translate the bus construction and require the corresponding signed corridor. Changing coordinates does not establish physical vacancy or control permission in the reflected region.

Being outside the selected box is a geometric statement, not a vacancy or isolation certificate. The separate bus/source corridor geometry must be genuinely vacant, large enough for its accuracy-dependent source lengths, and covered by the isolation contract. No occupied outside site may be silently removed. Any actual original coupling across the box boundary must be included in the retained plant, or an independently supplied physical decoupling mechanism is needed; this review supplies none.

The chain endpoint operator is B=I+X+Z at kappa. If kappa is a filler site or a different old site, the parent local-port interface must be supplied there, including the allowed coupling across the chosen old/new edge. Permission to add blocks on interior path edges does not by itself grant an exterior port block. If the original premise supplies only one particular interior port, the padding argument has not moved that permission to a corner.

## 3. Exact arbitrary-correlated-filler comparator identity

Let O be all original old factors and F every other physical factor in the box, including all existing qubits and all newly supplied filler qubits. Every such factor is retained. Let S=O tensor F, with external passive reference R arbitrary. If F is empty, its identity is one-dimensional and all formulas reduce to the unpadded case. Tensor ordering by geometric path versus the grouped O,F order is only a canonical permutation of labels; conjugating all displayed operators by that permutation gives the physical site representation without moving any qubit.

The displayed reduction requires the literal **bare** drift

    H_S=H_O tensor I_F,
    W_S=W_O tensor I_F.                          (2)

The idle-filler condition means that uncontrolled filler drift and uncontrolled O/F or outside couplings are absent in this bare generator. It does not forbid the deliberately installed positive path-bias blocks from interacting with F during the experiment. Those additions and their reserves remain part of the actual controlled generator.

For every real T,u, the exponential power series (or spectral calculus) gives

    exp(-iuH_S) W_S exp(-iT H_S)
      =[exp(-iuH_O) W_O exp(-iT H_O)] tensor I_F.          (3)

This exact operator identity is independent of the input state and of any correlations. It does not assume W_O commutes with H_O. It retains both literal old time flows and all literal scalar parts of H_O.

Let C denote every actual bus/source output, excluding the fillers which are in S. Write the parent's complete comparator isometry at t=T+u as

    B_t=e^(-i chi(t)) |Phi_C(t)> tensor U_S(T,u),
    U_S(T,u)=exp(-iuH_S) W_S exp(-iT H_S).

For any possibly entangled pure |psi>_OFR, (3) gives exactly

    (B_t tensor I_R)|psi>
       =e^(-i chi(t)) |Phi_C(t)> tensor
           [(U_O(T,u) tensor I_F tensor I_R)|psi>].       (4)

For every mixed density rho_OFR, including classical and quantum correlations, the corresponding density comparator is exactly

    |Phi_C(t)><Phi_C(t)| tensor
       [(U_O tensor I_FR) rho_OFR (U_O^* tensor I_FR)].    (5)

In particular, the joint FR marginal is unchanged and the full correlations with O undergo precisely the specified local O unitary. No filler is traced out, reset, measured, replaced by a marginal, or assigned a pure state. No computable description of the arbitrary input density is needed for this uniform state assertion.

If A_t is the exact physical isometry from the supplied controller input and the parent's bound is ||A_t-B_t||<=delta, tensoring I_R preserves that norm. For every rho_OFR,

    ||(A_t tensor I_R)rho(A_t^* tensor I_R)
           -(B_t tensor I_R)rho(B_t^* tensor I_R)||_1
        <=2 delta.                              (6)

The imported dynamic approximation is asserted only on the parent's actual observation window 0<=u<=w. The exact algebraic factorization (3) itself holds for all times; it does not extend that physical approximation window.

To prove this, insert (A-B)rho A^*+B rho(A^*-B^*) and use trace-norm submultiplicativity, ||rho||_1=1 and both isometries' norm one. The same proof holds with arbitrary finite reference dimension. A controller initialization error eta in trace norm adds at most eta by unitary invariance. Once the parent's bounds are computed for the full S, arbitrary O/F/R correlation requires no additional source-size or accuracy factor. The enlarged dimension of S itself is still paid in those parent resources.

The controller still must have the parent's specified phase-referenced initial state, approximately product with the **unconditional full S/R marginal**. Arbitrary filler input does not provide a prepared bus/source state or permit hidden initial C/S correlations. All design and filling precede the declared experiment input; preserving a state through physical filling/design itself requires the separate chronological input contract.

## 4. What fails without idle fillers

Equation (3) is not valid after merely assigning unknown physical filler terms to notation. For the decoupled sum H_O tensor I_F+I_O tensor H_F, the right side instead contains exp[-i(T+u)H_F]. A non-scalar such factor is not a global comparison phase and generally changes correlations. Actual O/F couplings generally destroy even that simple factorization; no such factorization may be assumed without a separate proof.

For an exact discriminator, take H_O=0, W_O=I, one filler with H_F=Z, and T+u=pi/2. The full unitary includes -i Z_F. On the correlated state (|000>+|111>)/sqrt(2) of O,F,R, it produces an orthogonal vector to the claimed identity-filler output, so their trace-norm distance is 2. This refutes only using the displayed idle-filler identity for a nonidle physical filler. It does not rule out a separately constructed and paid active compensation scheme.

One can instead include every actual filler drift/coupling in H_S and apply a suitable full-plant theorem, if its other premises hold. The resulting target comparator is then exp(-iuH_S)(W_O tensor I_F)exp(-iTH_S), which is generally different from (3). A known scalar filler term can be included in the physical scalar ledger and comparator phase consistently; no unrecorded scalar subtraction is authorized here. The present padding proposal assumes (2) rather than supplying physical cancellation of a different bare drift.

### Separately attributed decoupled-drift extension

After the initial review draft, root suggested retaining a known decoupled filler drift explicitly. This is a separate extension, not a replacement of the frozen idle-filler proposal. If the literal drift is

    H_S=H_O tensor I_F+I_O tensor H_F,

the two summands commute and W_S=W_O tensor I_F commutes with the filler summand. Direct multiplication of the factored exponentials proves

    exp(-iuH_S) W_S exp(-iT H_S)
      =U_O(T,u) tensor exp[-i(T+u)H_F].          (7)

Equations (4)-(6) therefore remain valid with that actual filler unitary in place of I_F, on arbitrary correlated O/F/R inputs. The filler/reference marginal now undergoes its specified free F evolution. This explicitly changes the full comparator and cannot in general be replaced by an identity-filler contract; scalar or special-time simplifications require their actual phase/time accounting. No pure or known filler state is needed. For effective composition, the actual H_F needs a computable name and norm bound, its full scalar and energy contributions must remain charged, and it must have no unaccounted coupling to O or outside. The pending chain theorem applies algebraically to this full H_S if its other assumptions hold. This observation does not supply a native drift, control, calibration or preparation mechanism. No additional scientific execution was needed for the exact tensor identity (7).

## 5. Scope comparison and conditional composition

The scope changes relative to the parent must be retained explicitly:

| Item | What the padding step requires | What the earlier parent does not supply |
|---|---|---|
| Complete plant | Every qubit in the chosen box becomes a retained S factor | Permission to erase occupied sites or omit unknown drift |
| Filler availability | Missing sites genuinely admit a physical qubit; existing fillers are retained | A formation law or cost-free addition of physical factors |
| Bare drift | The full S drift is exactly H_O tensor I_F for identity-filler output | Idleness inferred from a tensor symbol |
| Old interactions | The displayed positive onsite/path-edge blocks can be added throughout the box | That control family from one port or isotropic exchange alone |
| Port | The chosen corner has the required B and old/new coupling access | Automatic relocation of a given interior port |
| Exterior | The routed bus/source region is vacant and isolated for each required source size | Vacancy inferred merely from being outside this box |
| Inputs | Arbitrary O/F/R input is retained; controller input satisfies the parent's preparation contract | Ready controller phases, long-time calibration or release timing |

Conditionally apply the frozen chain supplier with n=M physical box sites and the path (1). Its positive C_S and leading Krylov coefficient then apply to H_S, including all idle-filler degeneracies, without requiring the bare H_S itself to be strong. Use W_S=W_O tensor I_F as the full target. The ensuing static-bias construction retains H_O with coefficient one, pays every added onsite/path block and local scalar reserve, and yields (4)-(6) with the parent's unchanged actual-time phase.

This does not independently accept the chain theorem: its exact frozen proof is a pending external dependency for this composition. The geometry and tensor identities themselves are established above independently of its spectral induction. The root proposal must not be read as a theorem under the earlier single-port interface alone.

The box, its M sites and C_S must be fixed for the original plant before accuracy is varied. All |F| filler factors count toward the enlarged physical system: newly introduced fillers are added resources, while preexisting fillers remain retained resources. Mathematical grouping with the old input does not remove their cost. The local incident cap remains the chain/transfer cap for this fixed enlarged plant. Its constants, the dimension 2^M, source count and later runtime can be much larger than for the unpadded plant. No favorable overhead, energy cost, initialization mechanism or efficient algorithm is proved. A changing box family would require a new uniform-cap argument.

No energy-moment guarantee follows merely from the tensor identity or trace-norm closeness. Any such corollary must use the actual extended static generator, its reserves and its actual initial joint state, with the relevant moment-weighted estimates. Physical preparation, calibrated actual duration, isolation, measured-energy identification, records and reset/reuse remain supplied or unresolved as in the parent.

## 6. Finite check and disposition

The universal path proof is the row/layer adjacency and bijection argument, including all singleton axes. One deterministic execution checked all 125 boxes with side lengths 1 through 5 and all their distinct coordinate corners: 729 paths, including 61 shapes with a singleton axis. It detected an omitted-layer-reversal mutant. Exact matrices verified (3)-(4) on a noncommuting old gate/drift and a three-way correlated input, detected correlation erasure, and produced the nonidle-filler counterexample above. These checks expose finite mistakes; they do not replace the universal proof. Execution results and limits are recorded in `CHECK_EVIDENCE.md` with actual source-at-launch and complete receipts.

The proposal is mathematically usable as a conditional padding reduction with the outward-direction correction and explicit corner-port, idle-filler, whole-path-control and exterior premises. It is not a derivation of those physical premises from the original interface, and the pending chain source remains pending. No source outside this output, original chain freeze, physical axiom or editable prompt was changed.


---

## Unchanged source: narrow_onsite_obstruction_appendix

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Separately attributed single-port static-bias counterexample

This appendix reviews a parent-supplied root proposal, exposed after the main transfer proof had been read and the main reviewer execution completed. It is not an author-transfer claim or a blind independent discovery. Source: `root_probe_at_launch/heisenberg_static_port_probe.py`, 3,667 bytes, SHA256 `5e8b4df1f4e341df3d54eeccb436765c7422331fd2911c9b63fc0807e245af22`; exact original execution source, receipt and complete streams are captured in the same directory and identified in ROOT_PROBE_CAPTURE.json. No earlier two-axis probe was read, executed or used as a dependency.

The proposed implication failure is correct at the stated mathematical scope: a complete two-qubit plant can have full Lie algebra from positive port generators while no Hermitian static bias confined to one designated qubit yields the bus parent's all-transition condition for any one-qubit port operator. The exact proof and independent recomputation follow. This is not a global physical no-go, an audit verdict or a general impossibility for static controllers. See NO_GO_DISCIPLINE_CHECKLIST.md for scope stress tests and the incomplete publication-packet gate.

Let two adjacent old qubits carry

    H=3 I⊗I+X⊗X+Y⊗Y+Z⊗Z.

Its singlet eigenvalue is zero and its triplet eigenvalue is four, so H is positive. The two supplied additions I⊗I+X⊗I and I⊗I+Z⊗I are positive, each with eigenvalues zero and two. Therefore H and the two H-plus-addition generators are positive actual generators on the same old plant.

The root output supplies 16 integer coefficient columns in the Pauli basis and corresponding nested Hermitian brackets i[A,B]/2. I independently parsed each finite expression using only the three named 4-by-4 generators, multiplied exact Kronecker matrices, and recovered coefficients via Tr(PA)/4. Every supplied column matches exactly; their determinant is -4 and rank 16. The generated real Hermitian bracket space is therefore all Hermitian 4-by-4 matrices, equivalently u(4) under multiplication by i. This verifies the explicit certificate, not merely a numeric rank threshold.

Now let C be **any** Hermitian bias supported on the first qubit. Write C=cI+r n·sigma with r>=0 and a unit n when r>0. A common rotation U⊗U sends n·sigma to Z while preserving H, since the isotropic coupling commutes with all sigma_a⊗I+I⊗sigma_a. The independent exact check verifies those three commutators; exponentiating them covers global SU(2). A one-qubit operator remains a one-qubit operator under this common rotation, whether supported on the first or second old qubit.

If r=0, H+C retains its triplet degeneracy, violating the required simple spectrum. If r>0, in the aligned frame the two exact eigenstates |up up> and |down down> have respective energies 4+c+r and 4+c-r. These are distinct. Every one-qubit B has zero matrix element between them: the untouched qubit contributes the orthogonal overlap <up|down>=0. The exact matrix check verifies this for the identity and all six one-site Pauli operators, which span the possible one-qubit choices. If any other energy degeneracy occurs, simple spectrum already fails. Otherwise these two product states are forced eigenvectors up to phase and their zero transition violates the all-off-diagonal condition. Changing eigenbasis phases cannot repair it.

This argument covers every scalar part, amplitude and Bloch direction of C in the designated single-qubit family, and every Hermitian one-qubit B. It does not merely test a finite list of axes. In particular no supplied point H+C with the bus strong conditions exists in this restricted bias family. Thus the transfer theorem's positive-polynomial premise p(1)>0 is unavailable here; its implication from an existing strong point is not contradicted.

The limits are material:

* Additional-site or genuine two-qubit biases are outside this counterexample's quantified C family.
* A multi-qubit port can connect the forbidden pair; for example <up up|X⊗X|down down>=1. This defeats the particular local-port selection rule but is not a complete compiler construction.
* Time-dependent controls can exploit commutators, as the exact full Lie certificate already shows. The argument does not constrain such a sequence to one static biased spectrum.
* An autonomous switch or continuing compensator introduces a different mechanism and requires its own complete output/error/cap proof.
* A realization not using the all-transition bus hypothesis may bypass this premise entirely.

Those escapes are not ruled out. The negative conclusion remains a counterexample to the single-port static-bias implication, not to the broader existence of an admissible C with arbitrary old onsite/NN support or to arbitrary architectures.

Independent execution: `appendix_run`, started 2026-10-16 01:27:46.404648 UTC, finished 01:27:47.005145 UTC, exit 0, 60-second limit. Main executable SHA `1645915aeae9419253035a28e0ba71dbcd9d1c407628e70c213c76d37e486a2f`; exact input root stdout SHA `e88c992762f2ad7e0f746d2d5d8adf0bbba5bd61690197241addae9007c32dd4`. The full source, launcher, input, raw streams and receipts survive in the run directory. This is a source-exposed exact recomputation by the same model, not a new model family or retained audit.


---

## Unchanged source: transfer_acceptance_qualifications

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Qualified static-bias transfer

The root accepts the positive attenuated-bias transfer as a conditional mathematical source result. The complete author argument, author executable/launcher and actual evidence, complete exposed review and Heisenberg appendix, both reviewer executables/launchers and complete streams were read. The unchanged qualified bus parent is reused at its exact source identity. This acceptance executes no scientific program and confers no retained audit or native physical status.

For effective termination, explicitly supply computable names for H, C, W, the local B, t_* and the finite installed decomposition/reserve data, or effective access sufficient for the stated certified computations. A computable norm majorant alone is insufficient. Without these names, distinguish fixed-instance mathematical existence from an algorithmic construction. Preserve the extra hypotheses that the bias consists of admissible old onsite/nearest-neighbor blocks, can be attenuated, and has one supplied strong spectral point. The theorem does not derive that point from the original full Lie certificate.

The positive proof uses the complex Hilbert-Schmidt Krylov Gram polynomial, its degree bound n(n+1), and a finite dovetailed strict-positivity search. It proves arbitrarily small positive strong biases from a single supplied strong point. Degenerate energies, repeated gaps and zero local-port transitions are distinguished. No conditioning, precision or efficient-search guarantee is inferred.

Choose a uniform target ball before the actual runtime: common source length, complete-space separation, contraction region, response lower bounds, counterterm/corrector bounds, xi and T precede the rational-Hermitian target search. The fixed-point calibration afterward remains inside those bounds. The post-T rational logarithm search uses an existential logarithm only to prove density of strict witnesses; it does not require deciding a logarithm branch or arbitrary zero support. Retain the exact interaction-frame order and the scalar phase R_total(T+s)+c_M xi^2(T+s)+lambda c_C s. No extra lambda c_C T may be added; the actual positive bias reserve is separately charged for the whole duration.

The finite checks include exact complex Krylov examples, explicit repeated-gap and missing-port exclusions, one-particle calibration samples and one rational-certified post-time logarithm witness. They do not execute the complete controller or replace the uniform analytic proof. The first reviewer's false structural-equality diagnostic is preserved and resolved by exact entrywise simplification in the second execution. It was not an overwritten scientific assertion failure.

The fixed-bias continuing-window argument is a narrow failed route: endpoint compensation followed by passive full-bias continuation cannot remove a nonscalar drift on a positive window. Attenuation, switching and continuing compensation are separate alternatives. The separately root-attributed Heisenberg appendix establishes one implication counterexample: positive-generator full u(4) controllability does not guarantee the bus's all-transition condition after a bias confined to one designated qubit. The analytic SU(2)/support proof and independently reconstructed exact determinant -4 certificate cover that family. Extra-site/two-qubit biases, larger ports, timed controls and other autonomous architectures are not excluded.

Those counterexamples are preserved as checked source evidence. The exposed no-go checklist explicitly has no publication-gate PASS and does not close five architecture families or an exhaustive historical echo search. This acceptance does not upgrade that procedural status, widen a narrow counterexample into a physical impossibility, or require unrelated alternatives to fail before pursuing the positive transfer. Any later publication must preserve the exact scope and resolve its applicable packet obligations honestly.

The common added incident cap pays the bias blocks and positive reserves; it does not bound global energy, runtime, action or precision. Exact old/reference marginal, prepared source phases, calibrated observation duration and continued isolation remain supplied. Integrated generator error alone is not a pointwise incident cap. Physical preparation, timing, operational energy identification, records and reset/reuse are unresolved. No physical axioms or editable prompts changed.


---

## Unchanged source: edge_acceptance_qualifications

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Controlling qualifications for the explicit old-edge bias

Accept the exact two-qubit spectral proposition and its stated conditional substitution. H=3I+XX+YY+ZZ remains literal; the added positive blocks are 2lambda(I+YY) and 8lambda(I+ZZ). Installation, independent attenuation and full-time calibration of those anisotropic blocks on an existing old edge are supplied physical permissions. A first-site-only control or an isotropic path does not imply them. The earlier onsite-only obstruction remains valid.

The four energies are 0,4+4lambda,4+16lambda,4+20lambda. Every lambda>0 except 1/3 and 1/2 has distinct positive gaps, and B=(X+2Y+3Z) tensor I connects every off-diagonal pair. Its energy diagonals vanish; optional identity shifts are different ports. On 0<lambda<=1/4 both the minimum positive gap and distinct-gap separation equal 4lambda, added incident load is <=5 at each endpoint and drift norm <=9. Old block-sum strength, operator norm, added load and scalar action remain distinct. Actual scalar 10lambda is paid through the full lifetime.

The complete old plant for this proposition is exactly two qubits, with arbitrary passive reference. Do not omit interacting spectators or fillers to retain this spectrum. Bus geometry, complete old/source/reference outputs, computable target data, source preparation, timing, isolation and calibration remain inherited conditional premises. The transfer compensates the full biased drift through T and pays the remaining window defect; it assumes no small lambda*T. Source size, runtime, global energy/action and precision are not bounded favorably by the common incident cap.

Evidence: an exact author run plus a separately reconstructed same-model equation-level calculation sealed before candidate inspection. Equations and intended purpose were supplied; this is not independent example selection, blind task framing or model-family replication. The reviewer first encountered a structural-equality assertion failure, then used entrywise exact simplification; both captured sources, launchers, receipts and full streams remain. The interval and conditional substitution were separately checked after exposure. Neither this acceptance nor provenance checks are retained-audit verdicts or physical hardware tests. No scientific executable was replayed by root.


---

## Unchanged source: chain_acceptance_qualifications

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Controlling qualifications for the positive occupied-path supplier

Accept the finite constructive spectral theorem on the stated domain. A specified nearest-neighbor Hamiltonian path passes through every old qubit and ends at the designated port. The physical interface must permit installing and attenuating the displayed positive onsite and edge blocks on that occupied path. Neither a single accessible port, a Lie-algebra certificate nor vacant exterior space supplies those permissions. All original factors and every literal H term stay present with coefficient one.

The rational positive C_n and local B_n=I+X_n+Z_n are constructed independently of original H, target and accuracy. The induction uses the special two-level base, every repeated-gap class, the nonzero rational pole argument, complex-parameter Riesz projectors and explicit Cauchy remainders. Certified strict choices of omega and g terminate without arbitrary equality or support oracles. The exact complex Hilbert-Schmidt Gram has degree D=m(m+1), m=d(d-1), and strictly positive leading coefficient determined by C_n, for arbitrary noncommuting computable Hermitian H. Testing D+1 rational nodes by strict dovetailing yields arbitrarily weak strong H+sC_n without a coefficient-one strong-point premise.

The spectral assertion permits arbitrary Hermitian H on the finite space. Physical composition additionally requires the qualified parent's locality/positive-decomposition convention for original H, complete computable data including W, exterior geometry and all source-state, phase, timing, isolation and calibration suppliers. Positive local reserves R_n remain installed and counted; R_C=0 only because they are already inside C_n. The fixed finite incident cap may depend badly on n and the chosen chain. It is not a uniform n-family, runtime, precision, global energy/action or design-complexity bound.

The transfer still chooses the small bias, uniform target-ball bounds, N, xi and actual T before computing its rational Hermitian target. Both literal old-time flows, every source/controller/reference output, continuing-window defect and complete scalar phase remain. No small s*T assumption or cancellation of literal H is introduced. The examples with deleted identity and H=-C_n remain failed shortcuts/stress cases, not the actual design. No arbitrary occupied-graph reduction or later box-padding extension is imported into this frozen theorem.

Evidence is exposed same-model proof development plus a separate adversarial reconstruction. The reviewer recorded proof findings before accessing the candidate check code, but had read the candidate's own check summary. The reviewer authored earlier bus/transfer proposals, so this is not fresh independent validation of those parent proofs; their separately qualified results are reused. Candidate exact dimensions4/6 tests, numerical80-digit samples and reviewer exact dimension2 noncommuting-H discriminator have different stated scopes. The general theorem is the analytic argument, not finite enumeration or PASS counts. Root read complete arguments, source, launchers, actual receipts and full streams, and independently checked the quantitative bounds and Gram/phase reasoning; no scientific program was replayed. Native preparation, measured-energy identification, records, reset/reuse and retained audit remain open.


---

## Unchanged source: box_acceptance_qualifications

Historical source text; the controlling qualifications and current source-only wrapper distinguish its status.

# Controlling qualifications for the padded-box reduction

Accept the explicit finite rectangular-box path and full-output tensor reduction on their stated domain. The row/layer snake, complete layer reversal, reflected reversed order and singleton-axis cases prove a Hamiltonian path ending at any specified corner. A globally negative-coordinate outward direction is available at the lower corner, not at every arbitrary corner. For another corner the appropriate signed exterior corridor must actually be vacant and isolated. The endpoint must have the required physical local port B=I+X+Z and old/new coupling permission. Neither coordinate relabeling nor interior path access relocates an original interior port or grants exterior coupling access.

Every actual qubit in the fixed box is retained as part of S=O tensor F. Missing sites require genuine physical availability. The complete box, every filler and the chosen path are fixed for the old plant before varying accuracy. Added positive onsite and path-edge blocks, their scalar reserves and full input data remain supplied and charged. The original drift is not removed or assigned coefficient zero. Unknown outside qubits or boundary couplings cannot be erased by choosing a box.

For the identity-filler comparator the literal bare drift is H_S=H_O tensor I_F. The exact output on arbitrary correlated O/F/R input is the literal two-old-flow comparator U_O(T,u) tensor I_F tensor I_R, together with every bus/source output and the complete physical phase. The parent isometry error delta gives trace-norm error at most 2 delta uniformly in the passive reference; controller initialization error eta adds eta. No known or pure filler input is required, and no filler is reset, discarded, measured or replaced by a marginal. The controller still requires its parent's phase-referenced state approximately product with the unconditional S/R marginal. Physical filling or design performed after input preparation requires a separate chronological contract.

The separately root-attributed decoupled-drift extension assumes the actual known computable sum H_O tensor I_F + I_O tensor H_F, without unaccounted O/F or outside coupling. Its comparator includes exp[-i(T+u)H_F] on F, with actual scalar and energy costs; it does not supply identity-filler output. The full correlations evolve by that stated local unitary. The exact GHZ/Z-filler example with trace distance 2 preserves the limit of the identity-filler claim. These formulas do not rule out separately supplied and paid compensation mechanisms.

At the review's own freeze the chain dependency was marked pending. Preserve that historical statement unchanged. This later root decision explicitly composes with the separately qualified positive-chain acceptance 382531923d20c156d6d05b6a440b26ac11af64e934950738e14fbd452c9a24e4, whose own bus/static-transfer dependencies and qualifications remain in force. Neither the padding proof nor its finite checker independently revalidates the spectral induction. The accepted parent can be applied to the complete S and W_O tensor I_F, including bare filler degeneracies. No new claim is inserted into the original chain freeze.

The finite enumeration covers 125 boxes, 729 distinct corner paths, 61 singleton-axis shapes and a layer-reversal mutant. Exact small matrices cover a noncommuting old gate/drift, retained correlated full output, correlation erasure and the nonidle-filler counterexample. The universal statements rest on the path and operator arguments. Root read the full scoped arguments, mathematical exposure, checker, launcher, actual receipts and complete streams, checked the tensor/trace-norm and geometry steps, and verified immutable member/source hashes without replaying science. The check is exposed and same-model; its author also developed the chain candidate. It is not blind review, new independent parent verification or retained audit.

The fixed enlarged plant pays its full dimension 2^M and all actual sites; the incident cap may depend badly on that fixed plant. No favorable geometry overhead, preparation mechanism, runtime, precision, global energy/action bound or energy-moment theorem follows. Native phase-referenced sources, full-time isolation/calibration/timing, measured-energy identification, records and reset/reuse remain supplied or unresolved.
