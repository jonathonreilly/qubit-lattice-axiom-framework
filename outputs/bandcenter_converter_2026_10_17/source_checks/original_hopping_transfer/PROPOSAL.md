# Original PR9672 apparatus: shorter finite output at the unchanged onset

Status: proposed application requiring a distinct independent check. The generic hopping-only lemma received its separate selective check while this application was being drafted; that status is recorded below and is not a self-review of either proof.

For the ORIGINAL apparatus without converters, retain the checked onset T=3e17 and choose ONE finite output length

    M=6e16.

The proposed hopping-only finite-transfer bound is <.001 uniformly through 2T=6e17. Consequently the already published nominal/fixed-spectrum complete finite error ceilings .001320/.001347 are preserved on [3e17,6e17], with the same nominal targets and product seed. The previous output length was 1.5e19; the new proposed M is exactly 250 times smaller. The sufficient onset, coefficients, supplied precision family and infinite-device theorem are unchanged. This is still an astronomical dimensionless apparatus, not a practical or native implementation claim.

## 1. Sources and exposure

Read the necessary original graph, positive-block, cap, count and distance argument at lines594–652; the fixed-spectrum physical block and actual endpoint shift at lines2100–2147; and the endpoint-forcing complete bounds/finite comparison at lines2284–2304 of

`correlation_worktree/docs/REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md`.

Verified file SHA256 `71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff`. The assigned published head is `e0835b2d048c9fa25bf8f1371993af628702e275` (PR9672), a root-provided Git identity; no Git operation or fresh remote claim is made. Relevant original coefficient/filter/endpoint-forcing arguments were also read in the immediately preceding coherent task at this same file revision. The preserved source theorem remains conditional on its own inherited calibration and physical premises.

The generic new lemma is my `../hopping_only_finite_transfer/PROPOSAL.md`, now SHA256 `9797cfa1090d58216655c80f79a8ce0fcee493c706f5028e61150d0815db278e`. Its initial version `4c790286d6db32784bc892eff3c21b5674104fc205719229dcbce6296f4d98cd` is preserved as PROPOSAL_v1.md. After drafting this application I read the FULL separate selective check `../hopping_only_finite_transfer_check/REVIEW.md`, SHA256 `d5ad6794b64d652bfbb4e80a8b172ccff1416d8e1fe726f6e592909e90d9bc8a`, and the complete one-paragraph source diff. The only change clarifies that K remains inside the noncommuting onsite dynamics; exp(-itK) is not factored from the interacting evolution. The independent check supports the mathematical lemma with that prose clarification. I verified both final hashes. I am the generic author and the author of this application, not its checker. The application below remains unreviewed. No converter scattering or mass theorem is imported into its graph-locality proof.

Applicable previously read instructions/workflow are reused. No scientific execution, parameter sweep, solver, new agent, model change, W/Git/checkpoint/prompt edit or publication occurred. There is no runner change or claim of fresh arithmetic execution. All substitutions below are explicit elementary inequalities. This file is the sole deliverable.

## 2. Original graph and exact output cut

Use the original two45-site arms, four-edge junction square, input sites m=0,...,ell with ell=20, adjacent emitter at input m=21, and output sites m=0,...,M-1. No converter, old-J extension buffer or new-j lead is installed. Every ordinary lead hopping remains -J, with J=.030021107107032.

The original source/old qubits remain one shared four-qubit internal system. In the one-head sector B and the clock-conditioned source contacts preserve head position, even though they act nontrivially and may not commute on the internal fiber. They create no head path through the source.

The emitter-to-input-port-origin distance is ell+1=21. The junction takes two edges from input origin to output origin. Hence the first omitted output vertex m=M is distance

    d=M+23,

and the last retained output vertex is distance

    L=M+22.

There is one cut edge, joining output m=M-1 to m=M, of magnitude J. The finite physical cap is J n_(M-1). Compression of the removed Q(-J) bond onto a blank omitted site leaves exactly this onsite term. Thus the finite one-head Hamiltonian is the exact compression P H_infinity P, including unchanged boundary diagonal2J and internal blocks. The same cap works for M=1, though the selected M is much larger.

Counts from this explicit original graph are

    head qubits = 90 arms +21 input +1 emitter +M output=M+112,
    physical qubits =M+116,
    head edges =88 arms +4 junction +20 input +1 emitter
                                     +(M-1) output=M+112.

The fixed-spectrum family has the same graph and counts. Passive reference qubits are not counted as apparatus qubits.

## 3. Original hopping ceiling, nominal and fixed-spectrum family

Decompose H=D+A in the head basis, keeping ALL onsite blocks, shared B, source contacts, diagonal compensations and common scalars in D. Each head-hopping block is a scalar times the internal identity. Its absolute row-sum ceiling is

    C=.075.

Explicit checks:

- Ordinary old lead/arm rows: 2J<.062.
- Junction arm-end and port-start rows: J+sqrt(2)J<.031(1+1.415)=.074865<.075.
- Filter rows: J+t_filter=J(1+S0/C0)<.031(1+.5/.9)<.049.
- Input endpoint: J+kappa0<.03100001; emitter: kappa0=1e-8.
- Arm entrance and finite output endpoint rows are smaller.

The large source/internal hopping h and contact loads are in D because they do not change head position. This does not erase those physical loads; it keeps their evolution unitary inside each head block. No scalar cancellation among hopping signs is needed.

The supplied fixed-spectrum orientation family has

    kappa_a/kappa0 in [1-1e-6,1],
    emitter/endpoint block [[E0+Delta,-kappa_a],
                            [-kappa_a,J-Delta]],
    Delta<=0, |Delta|<8.4e-21.

It is NOT literally true that every hopping is unchanged: the emitter edge changes from kappa0 to kappa_a. All bulk, filter, junction, lead and cut-edge hoppings are unchanged, and the changed emitter magnitude never exceeds kappa0. Thus the SAME C and cut magnitude J hold uniformly for the whole family. The diagonal changes +Delta and -Delta are retained in D and commute with the head-position weight; no smallness approximation to their time evolution is made. The full physical scalar c_new, graph, seed and final nominal target remain those of the checked corollary.

## 4. Application of the proposed weighted lemma

For each member, exact cap compression ensures that the finite and infinite retained onsite blocks are identical. In the interaction picture the retained edge is

    exp(isD_x) H_xy exp(-isD_y)

in BOTH devices at the SAME time s, with norm |h_xy|. Arbitrary internal/source/reference states and noncommuting D_x,D_y therefore satisfy the generic lemma's hypothesis. The weight exp[a dist(seed,x)] commutes with the full onsite part and has edge gradient at most one.

Conditional on the generic weighted-generator/Duhamel lemma, the complete evolution difference on the seed subspace satisfies, for a>0,

    E_transfer(t)
      <=min{2, J exp[-a(M+22)]
                    [exp(C sinh(a)|t|)-1]/[C sinh(a)]}.       (1)

The one cut edge acts only from the retained last-site amplitude in the Duhamel forcing; the reverse orientation annihilates the finite state outside its support. The bound is on the entire finite/infinite state operator, including source and old/reference amplitudes. No extra old-column overlap factor is needed for this transfer step.

Set a=1 only; no weight optimization or parameter sweep is performed. Since exp(x)-1<=exp(x), d=M+23 and t<=2T,

    E_transfer(t)
      <=[J e/(C sinh1)] exp[-(M+23)+.15 T sinh1].             (2)

Use J<.031, C=.075 and e/sinh1=2/(1-e^-2)<2.5 (because e>5/2). The prefactor is <2. This differs from the converter application: the cut magnitude is J, not j, so its .1 prefactor is NOT reused.

## 5. One transparent finite choice at the existing T

Keep the ALREADY checked endpoint-forcing onset

    T=3e17,
    choose integer M=6e16.

Using sinh1<1.2,

    .15 T sinh1 <.18 T=5.4e16,
    -(M+23)+.15 T sinh1 <-6e15-23.

Therefore uniformly for 0<=t<=6e17,

    E_transfer(t)<2 exp(-6e15-23)<.001.                       (3)

There is no need to compute an enormous exponential: exp(1)>2 gives 2exp(-23)<2^-22<1/1000, already sufficient without using the additional6e15 margin. This round-number M is a sufficient example, not a minimum or an optimized graph size.

The original checked infinite-device endpoint-forcing theorem gives, for every t>=3e17, complete nominal error<.000320 and fixed-spectrum-family error<.000347, with the latter compared to its FIXED nominal target. Adding (3) yields, for the SAME finite graph chosen before delivery and all t in[3e17,6e17],

    nominal finite error <.001320,
    fixed-spectrum-family finite error <.001347.

The unhalved trace-distance ceilings remain .002640 and .002694 respectively. The nominal infinite target is embedded in the common infinite space; it is not renormalized to the shorter finite output or postselected. The exact common scalar and exp(-itK)W aging remain for the full elapsed time. Arbitrary passive references are preserved.

These conclusions use the separately checked generic lemma and still require this application's distinct check. The unchanged original radius-18 Chebyshev criterion remains a checked fallback, but it alone does not certify this smaller selected M.

## 6. Resource comparison and limits

The published sufficient output length at this SAME onset was

    M_old=50T=1.5e19.

The proposed M_new=6e16 satisfies M_old/M_new=250 exactly. Total physical qubits change from1.5e19+116 to6e16+116; their ratio is slightly below250 because of the unchanged additive116. Head qubits and head edges both become6e16+112. No source, old, input or emitter qubit has been removed or duplicated. Local positive blocks and the original fixed-spectrum supply contract are unchanged except for shortening the uniform output and moving its required cap.

The 250-fold comparison is between these TWO transparent sufficient choices. The generic leading Chebyshev-versus-hopping coefficient improvement is240; the selected published M=50T contained additional slack, so there is no contradiction and no optimality claim.

No new runtime reduction, infinite-output theorem, exact finite permanent halt, reuse/reset operation, physical-unit assignment, native supplier or fabrication-tolerance result is proved here. The dimensionless output remains enormous. The only proposed improvement is a smaller sufficient finite graph for the already established horizon and error pair.

The next selective check should verify the original graph/cap and L=M+22, the uniform family hopping ceiling despite its changing emitter edge, the original J cut prefactor, and the fixed T/M substitution. It must keep the generic lemma's separate completed review distinct from this unreviewed application and from the previously checked temporal theorem. Root also mentioned a possible output-coordinate-only weight being authored elsewhere; it is not read, used or assumed here, and the selected result uses only the checked global C=.075 lemma.
