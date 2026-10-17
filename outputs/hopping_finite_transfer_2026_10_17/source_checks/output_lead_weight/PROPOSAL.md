# Output-lead-only weight for finite transfer

Status: proposed analytical refinement, requiring another selective checker. For the same nominal converted graph, exact cap and seed, for every integer M>=1, a>0 and real t,

    ||U_infinity(t)V_seed-embed U_M(t)V_seed||
      <=min{2, exp[-a(M-1)]
                [exp(2j sinh(a)|t|)-1]/[2 sinh(a)]}.       (1)

At a=1 and any independently supplied horizon 0<=t<=2T, a simpler ceiling is

    min{2, 1.2 exp[-M+4j T sinh(1)]}.                     (2)

This bounds complete finite/infinite evolution. It neither establishes temporal escape in the infinite apparatus nor selects an onset, optimized length, physical units or practical implementation.

## Sources, exposure and role

Root explicitly proposed the output-only weighting, its candidate formula and the illustrative pair below. I independently reconstructed the algebra after that exposure; this is AUTHOR work, not an independent review or independent-origin claim. I previously authored bandcenter_resources_check/REVIEW.md and hopping_only_finite_transfer_check/REVIEW.md. Another checker is required before treating this new refinement as selectively checked.

The frozen resource proposal is ../bandcenter_resources/PROPOSAL.md SHA256 96d6fdfa01631c17bd43c62c3a11f8754d2b31836740cc11f5a663172e3b37e7, and my resource review is SHA256 01b87c7557a3d7c6c34f6a2cb1b6d7bfb61416cf3ca1d982e6aa704280352efd. Both were reread fully in the preceding coherent task. The hopping-only argument was fully read as ../hopping_only_finite_transfer/PROPOSAL_v1.md SHA256 4c790286d6db32784bc892eff3c21b5674104fc205719229dcbce6296f4d98cd; I verified its only final-source change is the scalar/K clarification, giving final PROPOSAL.md SHA256 9797cfa1090d58216655c80f79a8ce0fcee493c706f5028e61150d0815db278e. My appended final-source review has SHA256 f47de4c7d6a20b547b365b105abaa70ca124071998ec58aeac6dab4c5e7bf664. These identities provide the explicit graph, nominal j, full shared internal fiber and cap identity. Canonical ancestor identity and exposure limits are recorded in the resource review and are reused, not newly recertified.

Applicable unchanged AGENTS/workflow/reviewer instructions from the immediately preceding task are reused. No scientific program, numerical experiment, solver, search over parameters, new agent, model override, W/Git/PR/checkpoint/prompt edit or publication was performed. The only writes are the requested final-source qualification in my preceding review and this new author proposal. No temporal candidate has been read or accepted here.

## 1. Exact compression and modified weight

Use the one-head space ell2(V) tensor H_internal, with one shared old/source fiber, and tensor any passive reference. The finite retained graph has new-output sites n=0,...,M-1. The prescribed cap j n_(M-1) is exactly the compression of the deleted Q(-j) bond onto zero omitted occupation, so

    H_M=P H_infinity P on ran(P).

The only cross-boundary head edge is between new-output n=M-1 and n=M, with scalar hopping -j times the internal identity. All diagonal blocks, common scalar and old/source dynamics agree between the two models on retained sites.

Define f=0 on every retained vertex except the new-output ray; on that ray define f(n)=n for n=0,...,M-1. In particular the first new-output vertex n=0, both old-J buffers, both converter neighborhoods up through n=0, both arms, the whole input stub and emitter all have weight zero. Let

    W_a=sum_x exp[a f(x)] |x><x| tensor I_internal.

This is a bounded invertible operator for each finite M and a. It is an analytical device, not a change to the physical Hamiltonian or device. It commutes with every fixed-head internal block. Since the seed is at the emitter, W_a V_seed=V_seed. The last retained output vertex has weight factor exp[a(M-1)]. This f is intentionally not distance from the emitter; no distance formula is invoked to improve its last-site value.

Every edge in the finite core, input or old buffers has delta f=0. Both converters also have delta f=0: on the output side the converter joins an old endpoint to new n=0. Only bonds joining new-output n to n+1 have nonzero delta f, equal to +/-1. All such bonds have hopping magnitude exactly j.

## 2. Weighted generator bound independent of core hopping

Set H_a=W_a H_M W_a^-1. For any off-diagonal head block H_xy=H_yx^*,

    [Im H_a]_xy=sinh[a(f(x)-f(y))] H_xy/i.

All onsite terms are still self-adjoint and contribute zero to Im H_a. Edges with delta f=0 also contribute zero, irrespective of their strength or internal structure. Thus Im H_a is supported only on the finite new-output path. Each vertex meets at most two of its bonds, giving absolute block row and column sums at most

    2j sinh(a).

The block Schur bound therefore proves ||Im H_a||<=2j sinh(a). This is not a claim that ||H_a|| is small. B, all contacts and all physical source loads remain present. K need not commute with those interactions; nothing in the argument factors exp(-itK) from the evolution.

For y(s)=W_a U_M(s)V_seed v, with arbitrary unit old/reference input v,

    d||y(s)||²/ds=2 <y(s),Im H_a y(s)>.

The same norm bound in both time directions and Gronwall imply

    ||W_a U_M(s)V_seed||<=exp[2j sinh(a)|s|].

Projection onto the last retained head position, keeping its entire internal fiber, yields

    ||P_last U_M(s)V_seed||
       <=exp[-a(M-1)+2j sinh(a)|s|].                     (3)

This is an operator statement before any column decomposition. It holds with arbitrary passive-reference entanglement and includes source/emitter/complementary amplitudes during the entire evolution.

## 3. One-cut Duhamel and M=1

On the common infinite space set H_dec=H_M direct_sum [(I-P)H_infinity(I-P)]. Compression ensures H_infinity-H_dec consists only of the two adjoint cut-edge orientations. The decoupled evolved seed stays retained, so only the retained-to-omitted orientation acts. Its norm on that seed map is exactly

    j ||P_last U_M(s)V_seed||.

Unitarity of the full infinite evolution in Duhamel's formula and (3) give

    error <=j exp[-a(M-1)] integral_0^|t|
                                      exp[2j sinh(a)s] ds,

which is (1). The factor j cancels the 2j in the integral denominator, leaving 1/[2 sinh(a)], not 1/[j sinh(a)] or an extra factor two. The universal ceiling 2 follows because both evolved seed maps are isometries. The exact Duhamel identity includes returns from the omitted output tail and all spectral components; no leakage-only approximation is used.

When M=1, W_a=I throughout the retained apparatus. Its actual weighted imaginary part is zero, which certainly satisfies the conservative 2j sinh(a) bound. The last weight is one, the cap identity still holds, and (1) is valid. In that special case unitarity gives the sharper elementary error<=min{2,j|t|}; the proposed exponential ceiling remains a valid, looser bound. No positive lead length is silently assumed by the weighted argument. For every M, as t tends to zero the integral expression is regular, and at t=0 the exact error is zero.

## 4. Sufficient horizon relation and transparent arithmetic

With a=1, |t|<=2T, and exp(x)-1<=exp(x), equation (1) implies

    error <=[e/(2 sinh1)] exp[-M+4j T sinh1].

The prefactor is 1/(1-e^-2). Since e>5/2, it is <25/21<1.2. This proves (2). For any supplied epsilon_tr>0 a sufficient condition is

    M>=4j T sinh1+log(1.2/epsilon_tr), integer M>=1.     (4)

This condition is sufficient, not optimized; a can also be left arbitrary in (1). Relative to the prior hopping-only leading horizon coefficient .15, the new coefficient is 4j<.012, so the ratio of those leading coefficients exceeds 12.5. Additive offsets and prefactors differ, and no minimum-size ratio is inferred. The earlier Chebyshev and general hopping-only estimates remain available as separate bounds.

For a transparent CONDITIONAL illustration only, take the root-supplied hypothetical horizon parameter T=10^17 and output count M=1.5*10^15. This does not assert that the infinite device escapes by T. Using only j<.003 and sinh1<1.2 gives

    -M+4j T sinh1 < -1.5*10^15+1.44*10^15=-6*10^13,
    transfer <1.2 exp(-6*10^13) on 0<=t<=2*10^17.

For example sinh1<1.2 follows from e<11/4, hence e^-1>4/11 and sinh1<105/88<1.2; these are loose analytic inequalities, not a numerical solver result. Thus the displayed pair would make finite transfer negligible relative to ordinary fixed tolerances if that horizon were separately justified. No device is allocated, no resource optimum is claimed, and this illustration does not accept any temporal candidate. At this M the physical counts are still M+194 head qubits, M+198 total qubits and M+223 positive blocks in the checked decomposition.

## Remaining independent obligations

The proposed improvement changes only the analytical weight. It makes no alteration to couplings, initial product seed, shared internal registers, cap or output comparator. A complete infinite-output error, including its source/emitter/complementary coordinates and onset/window, must be established separately. If available, it adds to (1) by triangle inequality with the same normalized infinite output packet and prescribed scalar phase/old aging. Passive-reference tensoring preserves the bound; unhalved trace distance is at most twice the total operator error. No projection, finite-waveform renormalization, postselection, drive, capture or permanent finite halt is inferred.

The decisive new check is whether the output-only f has delta f=0 on every non-new-output installed edge, and whether the resulting 2j sinh(a) imaginary-part bound and single-cut integral have the stated factors. This proposal must receive a different checker; my prior review of the broader method is not independent verification of this authored refinement.
