# Weighted finite-output transfer with exact internal dynamics

Status: conditional mathematical support, prepared for integration review. The finite-transfer argument and the original-apparatus application below have received the selective analytical checks listed in the appendix. This note supplies no retained audit status or new temporal theorem.

For the original autonomous endpoint apparatus, the already established onset T=3*10^17 and complete finite error ceilings .001320 (nominal) and .001347 (supplied fixed-spectrum family) are preserved with one fixed output length M=6*10^16. The previous sufficient output length was 1.5*10^19. Their ratio is 250; neither size is claimed minimal or practical. The improvement follows by bounding propagation using head-moving hoppings while retaining all noncommuting internal dynamics exactly.

No novelty of weighted propagation methods is claimed. The contribution here is their exact-cap, complete-state application to this endpoint device and the resulting smaller sufficient finite length. Related particle-transport locality work includes [Faupin, Lemm and Sigal, On Lieb-Robinson bounds for the Bose-Hubbard model](https://arxiv.org/abs/2109.04103). Only its abstract was consulted for positioning; no result or constant is imported. The required bound is proved below.

## 1. A weighted single-cut theorem

Let H be a bounded self-adjoint operator on l2(V) tensor K, where V is a graph of head positions and K is the shared internal Hilbert space. Write

    H=D+A,  D=direct_sum_x D_x,  D_x=D_x*,
    A_xy=A_yx*,  A_xx=0,

with off-diagonal blocks supported on installed graph edges. No commutativity between the D_x or their internal constituents is assumed. The shared internal system occurs once; this head-coordinate representation does not duplicate physical registers.

Let P retain a finite set of head vertices, and let H_P=P H P on its range. Suppose precisely one installed edge joins retained vertex b to omitted vertex c, with block norm ||A_cb||<=q. Let S be an isometric seed map supported in P. For any real f on the retained vertices that vanishes on the head support of S, define, for a>0,

    W_a=diag_x(exp(a f(x))) tensor I_K,
    L=f(b),
    gamma_a=sup_x sum_(y retained)
          |sinh(a(f(x)-f(y)))| ||A_xy||.

Assume gamma_a is finite. Symmetry supplies the same column bound. Then, for every real t,

    ||exp(-itH)S-embed exp(-itH_P)S||
      <=min{2, q exp(-aL) Phi(gamma_a,|t|)},              (1)

where Phi(g,t)=(exp(gt)-1)/g for g>0 and Phi(0,t)=t. The statement holds for every passive reference tensor factor, without dependence on its dimension.

**Proof.** On the finite retained space W_a is bounded and invertible. Put H_a=W_a H_P W_a^-1. Its onsite part is D_P and is self-adjoint. For each off-diagonal block,

    [Im H_a]_xy=sinh(a(f(x)-f(y))) A_xy/i.

The block row/column bound gives ||Im H_a||<=gamma_a. For any unit seed input v and y(s)=W_a exp(-isH_P)Sv,

    d||y(s)||²/ds=2<y(s),Im H_a y(s)>.

Since W_a S=S, Gronwall in either time direction gives

    ||W_a exp(-isH_P)S||<=exp(gamma_a |s|),
    ||P_b exp(-isH_P)S||<=exp(-aL+gamma_a |s|).          (2)

Here P_b retains the entire internal fiber, not a chosen internal output state. Form the bounded self-adjoint direct sum H_dec=H_P direct_sum [(I-P)H(I-P)]. The evolved decoupled seed has zero omitted component. Consequently only the retained-to-omitted orientation of the cut acts on it, and

    ||(H-H_dec)exp(-isH_dec)S||
       <=q ||P_b exp(-isH_P)S||.

Duhamel, unitarity of the full H evolution and integration of (2) prove (1). The reverse edge supplies no extra factor two because it acts on zero omitted amplitude. The universal ceiling 2 follows from the two isometric evolutions. For t<0 the same argument uses the reversed integration interval. The definition of Phi covers gamma_a=0 and t=0 exactly. Tensoring each operator with a passive-reference identity preserves its norm and every step. This is a complete state-map estimate, including later returns from omitted sites, not merely a leakage-probability bound. ∎

The cap hypothesis is substantive. For a physical exchange bond

    Q(-q)=q(n_b+n_c)-q(a_b* a_c+a_c* a_b), q>=0,

compression onto blank omitted occupation leaves q n_b. Deleting the bond and adding precisely this cap realizes H_P. Otherwise a changed boundary diagonal would create additional Duhamel forcing. Unmatched boundary terms are not covered by (1).

## 2. Two useful weight choices

If the seed is at a vertex e and the absolute hopping row sums obey sum_y||A_xy||<=C, take f(x)=dist(e,x) on the seed connected component of the installed infinite graph, and f=0 on any other retained components. The cut vertex in this corollary lies in the seed component; disconnected components carry no evolved seed amplitude. Each edge has |delta f|<=1, so gamma_a<=C sinh(a). If the retained cut vertex has distance L, (1) becomes

    transfer <=min{2,q exp(-aL)
              [exp(C sinh(a)|t|)-1]/[C sinh(a)]}.        (3)

For C=0 there is no head hopping; the continuous Phi convention applies. Arbitrarily strong bounded onsite dynamics do not enter C. This mathematical fact neither removes their physical loads nor asserts a small norm for the full Hamiltonian.

There is also an output-ray corollary. Suppose a uniform output path n=0,...,M-1, M>=1, attaches to the rest of the retained graph only at n=0. Its internal edges and unique cut edge to n=M have magnitude q>0, and its cap realizes exact compression. Require the seed support to lie in the nonoutput graph and/or at n=0. Set f=0 throughout the nonoutput graph and f(n)=n on the ray, so W_a S=S as required by (1). Only output-path edges contribute to Im H_a, so gamma_a<=2q sinh(a) and L=M-1. Hence

    transfer <=min{2, exp[-a(M-1)]
                     [exp(2q sinh(a)|t|)-1]/[2sinh(a)]}. (4)

At a=1 and |t|<=2T, T>=0, this implies

    transfer <=min{2,1.2 exp[-M+4qT sinh1]}.              (5)

Indeed e/(2sinh1)=1/(1-e^-2)<25/21<1.2. For M=1 the weight is identically zero, its actual imaginary part vanishes, and (4) remains valid; the sharper bound min{2,q|t|} follows directly. If q=0 the cut is absent and the error is zero. These corollaries require no scattering completeness or absence of point spectrum. No new original-apparatus size is selected using (4) or (5) in this note.

## 3. Original apparatus and supplied family

The application uses the original graph and coefficients in [the original endpoint theorem](REAL_ENDPOINT_AUTONOMOUS_OUTPUT_BOUNDED_THEOREM_NOTE_2026-10-17.md), SHA256 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff, associated with PR9672 head e0835b2d048c9fa25bf8f1371993af628702e275. Its exact Hamiltonian, delivered emitter/blank-head/source-vacuum product seed, original spectral/calibration premises and temporal theorem remain supplied conditional dependencies.

There are two 45-site arms, a four-edge junction square, input sites 0,...,20, one adjacent emitter and output sites 0,...,M-1. No converter or additional buffer is installed. The head graph has M+112 vertices and M+112 edges; four shared old/source qubits give M+116 physical qubits. Passive references are not apparatus qubits.

The emitter is 21 edges from input origin, the junction requires two edges to output origin, and the last retained output is M-1 further edges away. Thus L=M+22 and the first omitted vertex is at distance M+23. There is exactly one cut of magnitude J=.030021107107032. The physical cap J n_(M-1) preserves the original endpoint diagonal 2J and realizes exact compression, including at M=1.

A uniform hopping ceiling is C=.075:

| Head row | Sum of hopping magnitudes | Ceiling |
|---|---:|---:|
| Ordinary arm/lead | 2J | <.062 |
| Junction | J(1+sqrt(2)) | <.074865 |
| Filter | J(1+S0/C0) | <.049 |
| Input endpoint | J+kappa0 | <.03100001 |
| Emitter | kappa0 | 10^-8 |

Here kappa0=10^-8, C0>.9 and S0<.5 are the original fixed half-angle data; entrance and capped-output rows are smaller. All source hopping, B and head-conditioned contacts preserve head position and belong to D. Their large incident loads remain unchanged.

For the supplied fixed-spectrum orientation family, kappa_a/kappa0 lies in [1-10^-6,1]. Its actual emitter/endpoint block is

    [[E0+Delta,-kappa_a],[-kappa_a,J-Delta]],
    Delta<=0, |Delta|<8.4e-21.

The actual endpoint diagonal is 2J-Delta. The emitter hopping changes but never increases; all bulk/filter/junction/output hoppings and the cut remain unchanged. Thus C=.075, cut magnitude J and cap compression hold uniformly for the family. Both shifted diagonals stay exactly in D; there is no approximation that drops their accumulated phase at long times.

## 4. Checked finite choice at unchanged onset

Applying (3) with a=1 gives, for 0<=t<=2T,

    transfer <=[J e/(C sinh1)]
                    exp[-(M+23)+.15 T sinh1]
             <2 exp[-(M+23)+.15 T sinh1].                (6)

The prefactor bound uses J<.031 and e/sinh1<2.5. Keep the existing checked onset T=3*10^17 and choose the single finite length M=6*10^16 before delivery. Since sinh1<1.2,

    -(M+23)+.15 T sinh1 <-6*10^15-23,
    transfer <2 exp(-6*10^15-23)<.001                   (7)

through the whole interval [0,6*10^17]. Even 2exp(-23)<2^-22<.001 suffices, so no huge exponential is numerically evaluated.

The cited original endpoint-forcing theorem supplies complete infinite-device errors <.000320 nominal and <.000347 uniformly over the supplied fixed-spectrum family for t>=3*10^17. The family uses its fixed nominal output target. Reusing precisely those premises and adding (7) yields

| Device | Complete finite operator error on [3*10^17,6*10^17] | Unhalved trace ceiling |
|---|---:|---:|
| Nominal | <.001320 | <.002640 |
| Supplied fixed-spectrum family | <.001347 | <.002694 |

The comparator is the same normalized infinite output packet embedded in the common infinite space. It retains its full complex profile, common scalar phase, prescribed exp(-itK)W aging, blank nonoutput registers and arbitrary passive reference. It is not renormalized to fit the finite ray, projected or postselected. All source/emitter outputs and exterior point or other spectral mass already charged by the infinite theorem remain charged. The factor-two trace estimate follows from the pure-state inequality and extends through purification to reference-assisted channel comparison.

Only a common scalar can be factored from the exact interacting evolutions. K and other onsite operators remain in D; no commutation or factorization of exp(-itK) from those evolutions is assumed. The weighted norm calculation is a proof device for the same static Hamiltonian, not a drive or switching protocol.

The old sufficient M=50T=1.5*10^19 and new M=6*10^16 have output-length ratio 250 exactly. Physical counts change from 1.5*10^19+116 to 6*10^16+116, whose ratio is slightly below 250. This compares two sufficient choices with different slack. The leading coefficient ratio between the old radius-18 Chebyshev condition and (6) is 36/.15=240; neither ratio determines optimal size. No new onset, precision contract, native supplier, physical-unit assignment, capture/reset/reuse or permanent finite halt follows.

## Appendix: source inventory and verification limits

The preparation used the following frozen analytical sources and reviews. Paths below are relative to [the preserved source checks](../outputs/hopping_finite_transfer_2026_10_17/source_checks/); [the manifest](../outputs/hopping_finite_transfer_2026_10_17/SOURCE_MANIFEST.json) records their exact bytes and original recovery paths. Full identities distinguish the author text from its check.

| Source | SHA256 |
|---|---|
| hopping_only_finite_transfer/PROPOSAL.md | 9797cfa1090d58216655c80f79a8ce0fcee493c706f5028e61150d0815db278e |
| hopping_only_finite_transfer_check/REVIEW.md | f47de4c7d6a20b547b365b105abaa70ca124071998ec58aeac6dab4c5e7bf664 |
| original_hopping_transfer/PROPOSAL.md | a7ef8d4ba3d1c9e35e9de7c5ca5e8f66b4cc5af3f105570e43935868d1fed8a7 |
| original_hopping_transfer_check/REVIEW.md | 591e7e993db00432a30ccd9049444720f4f404d1db1e681b787b67fcbe3a0f9f |
| output_lead_weight/PROPOSAL.md | 58f99248986aebe14b4cd87f46237a293ed0c86ab720dd37a497c5b2a64a06cf |
| output_lead_weight_check/REVIEW.md | 1c72e347fed86c96fcc491c550c136d08f3b7720d52ec1534af94066056d59dd |

The general method was checked by a different author from its proposal; the original-architecture application received a separate checker; the output-only specialization received a different checker who had authored the broader method. Checks are therefore source-exposed selective analytical reconstructions with overlapping ancestry, not blind/model-diverse validation or repeated independent certification of every premise. The present note's author checked the generic lemma and authored the output-only specialization, and has read the original application and its full review plus the output-only review. The root's requested synthesis and accepted-source list are exposed inputs. This publication synthesis is itself author work for separate integration review.

Canonical graph/coefficient/cap passages previously read at the stated source identity were reused. The fixed-spectrum construction at lines 2100–2147 and endpoint-forcing complete bounds at lines 2284–2304 were read directly for this synthesis; the canonical hash was verified unchanged. The PR/head association is root-supplied provenance, not a new remote verification. The inherited calibration and temporal derivations were not rerun or independently recertified here.

No new runner, simulation, numerical experiment, parameter sweep or solver was used; inequalities in this note are analytical substitutions. No retained audit verdict is granted. No converter complete-output theorem or unreviewed spectral/temporal composition is imported. The source packet remains the recovery record for the explicit checks; this note does not duplicate its converter construction. No W, Git, model, prompt or checkpoint was changed while authoring this note. Publication and integration review remain separate actions.
