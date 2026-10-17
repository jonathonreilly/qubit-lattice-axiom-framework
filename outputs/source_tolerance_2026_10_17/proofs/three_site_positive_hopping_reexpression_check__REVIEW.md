# Positive hopping re-expression: distinct algebraic check

**Conditional support; no necessary correction found.** The seven-block source is exactly the checked six-block source plus the explicit identity Csrc=kappa+a1+a2 on the full qubit Hilbert space. Independent hopping-amplitude variation removes the old decomposition's hopping-dependent occupation adjustments, while preserving identity detunings and introducing an actual tuple-dependent physical global phase. This is not a native supplier or full robustness theorem.

Read complete target `three_site_positive_hopping_reexpression/PROPOSAL.md`, SHA256 `9fa50cd2da480d59765aa5fbd7c556728a08ac4c385234dc055c26220b93a5d4`. Reused the complete perturbed attachment `f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d` and its distinct check `0fd4a54559c48af641f9c90baa326e78a7bcc51f9428d0384ab6c7cc0252447d`, which was fully read in the preceding coherent task. Their performance domains and physical identification premises remain conditional.

## All pair sectors and full operator equality

On |00> and |11>, X_uv vanishes and P_a equals a times the identity. On span{|10>,|01>} its matrix is [[a,−a],[−a,a]], with eigenvalues 0 and 2a. Thus the full pair spectrum is {a,a,0,2a}, P_a is positive for a>0, its norm is 2a and it preserves head number. In particular the vacuum energy is a, not zero. The local pair identity tensored with every other subsystem is the full apparatus identity; it is not a projector onto the one-head sector.

Collecting the OLD six blocks gives the coefficient j at n_p, 2j+d2 at n2, 2j+d1 at n1 and 2j+d0 at n0. Their three hopping terms are −kappa X_2p, −a2 X_12 and −a1 X_01. This collection uses ordinary operator addition and is valid on multiple-head states as well as vacuum. The new three P blocks give these same hoppings plus (kappa+a1+a2)I; the four occupations give exactly the same number terms. Therefore Hsrc_new−Hsrc_old=Csrc I on the entire Hilbert space.

The shared background is added once on both sides. This proves Hnew=Hold+Csrc I, with no commutation hypothesis concerning actual K or any internal contacts. Consequently the exact unitary relation exp(−itHnew)=exp(−itCsrc)exp(−itHold) holds for all real times. There is no rotating-frame approximation or deletion of the scalar.

## Compression, variations and phase

Compress to all three source heads blank, retaining the port and every other degree of freedom. Each source exchange vanishes under that compression, while each P block leaves its amplitude times the retained identity. The new occupations on s0,s1,s2 vanish; j n_p remains. The compressed source contribution is exactly j n_p+Csrc I. Subtracting Csrc from the full operator therefore recovers precisely the previously checked emitter-free background, not a changed endpoint diagonal.

For each positive actual amplitude tuple, the centered new operator equals the old compensated source FAMILY with that same tuple. Keeping the new occupations fixed at 2j+d_i and j does not require a compensating minus change when a hopping varies. The algebraic comparison family still contains the old adjusted occupations, but the proposed new implementation does not. This distinction is correctly drawn.

The result does not eliminate the need to supply fixed occupations, identity detunings, small diagonal disorder relative to lambda, the restricted source coefficient domain or the new local blocks themselves. Positivity of P_a alone holds more widely than the checked performance domain; no expanded performance domain follows. The positive occupation assumptions are sufficient within the stated perturbation regime, including negative d_i.

The physical scalar is c_att_old+Csrc(actual). Literal W, K and old aging are unchanged. If the tuple is uncertain, a phase-sensitive vector-map theorem against one nominal phase cannot be concluded: the discrepancy exp(−itCsrc(actual)) versus exp(−itCsrc(nominal)) may be large. A family target using the actual scalar is correct. Global-phase invariance of channel predictions does not remove this qualification from the campaign's complete vector metric. The proposal explicitly retains it.

## Resources and finite interfaces

Replacing six blocks by the listed three P blocks and four occupations adds exactly one unmerged positive block. Sites, head edges and product preparation do not change. Therefore the stated M+238 heads, M+243 physical qubits, M+239 edges and 2M+282 blocks follow. This is a count for the explicit decomposition; no minimality is asserted. The new j n_p is the replacement for the structured source block's previous port diagonal, not an extra duplication of an unchanged background term.

Each P block has norm 2a. Summing its incident norms and the positive occupations gives exactly the four displayed source contributions:

    s0: 2j+d0+2a1;
    s1: 2j+d1+2a1+2a2;
    s2: 2j+d2+2a2+2kappa;
    p: j+2kappa.

Background incidence at p is still separately owed. Assigning a local block's full norm to both endpoints is conservative bookkeeping; the globally constant part does not justify dropping it from these declared block-norm sums. Old source-load numbers cannot simply be reused for the changed decomposition.

The finite and infinite devices receive the SAME Csrc because the only replacement is at the finite source prefix. Their unitary difference is multiplied by a common unit phase, leaving its norm unchanged. Likewise Hnew−(E_e+Csrc)=Hold−E_e, so moments and windows transfer with shifted physical centers. Keeping unshifted centers instead would be wrong. These exact identities license reuse of the previously checked cut and moment interfaces within their original hypotheses; they supply no new temporal or tolerance estimate.

## Exposure and limits

Root authored this new re-expression. I authored the perturbed attachment, reviewed nominal attachment/inverse work and checked the subsequent perturbed outgoing bridge. The perturbed attachment has the distinct review pinned above; I do not independently recertify my own construction here. This review directly reconstructs the NEW four-sector block identity, full-space scalar relation, compression, tuple dependence and counts/loads. It is source-exposed same-model checking, not blind or model-diverse independence.

The positive-local-Hamiltonian realization of I−X remains supplied, not derived from native primitives or introduced as a physical axiom. No claim of practical coefficient supply, full-device robustness, permanent halt, irreversible capture or reset/reuse follows. No scientific execution, numerical tolerance test, sweep, dynamics, W/Git/PR/checkpoint/prompt/axiom/model change or delegation occurred. Only this review was created.
