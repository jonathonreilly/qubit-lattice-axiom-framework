# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Root corrected-fast Schur derivation

Assume the corrected-arm strip lemma in [CORRECTED_FAST_STRIP_PROOF.md](CORRECTED_FAST_STRIP_PROOF.md). All transposes below are analytic bilinear transposes, not conjugate transpose, since this is outgoing continuation.

Contact-resummed host Green matrix in (d,d2) basis is Gh=[[G,c],[c,b]], with G=-i log(1/lambda)/pi+O(1), c=1/2+O(lambda log), b=19lambda/16+O(lambda²log). The native host-arm connection is W with rows w=(-2,-lambda/4), u=(-lambda,0). Native slow A2,D2 vertices are vA=(-d2,-e1), vD=(0,-2e1).

Write W^T Gh W=G ww^T+E, E=c(wu^T+uw^T)+b uu^T=O(lambda). Absorb E into gtilde=(I-gE)^-1g. Since g bounded, gtilde=g+O(lambda); alpha=w^T gtilde w has Im bounded below and modulus bounded away from zero. Thus

Raa=gtilde + G gtilde w w^T gtilde/(1-G alpha)

is uniformly bounded, Raa w=gtilde w/(1-G alpha)=O(1/log), and w^T Raa w=alpha/(1-G alpha)=O(1/log). Because e1=-w/2+O(lambda)e2, Raa e1=O(1/log)+O(lambda), and e1^T Raa e1=O(1/log)+O(lambda²). The transpose symmetry is used here, not positivity of the outgoing full resolvent.

After eliminating the host, the A2 effective arm forcing is
rA=-e1-W^T Gh e_d2=-e1-cw-bu=O(lambda log),
while rD=-2e1. The induced slow matrix is
M_AA=b+rA^T Raa rA=O(lambda),
M_AD=rA^T Raa rD=O(lambda),
M_DD=4 e1^T Raa e1=O(1/log).
Hence ||M||=O(1/log), and the correction in slow units is lambda M=O(lambda/log). This restores the same small Schur parameter used by the previous exact-partial-pole Rouche comparison, now with complete projected native fast K2. The slow pole displacement remains O(Jz lambda^5/log) within this specified coefficient model. Native slow K4 bulk shift and higher/cross-boundary terms remain separate.

Original leading readout is -sqrt2 lambda d. Its slow induced amplitude divided bylambda² is -sqrt2 Vslow^T R e_d. Using
Raa W^T Gh e_d=Raa(Gw+cu),
A component=-c+rA^T Raa(Gw+cu)=-1/2+O(lambda log),
D component=-2e1^T Raa(Gw+cu)=-1+O(1/log)+O(lambda log).
Therefore the leading source limit remains (1,2)/sqrt2, with logarithmic convergence in the D component. This derives that limit from the same native projected vertices; it does not identify an empirical detector or establish the full dressed native source remainder.

These bounds are uniform on the compact lower disks around the partial Airy pole only if the arm strip lemma's eta/f bounds and host outgoing branch conditions hold there. Independent Schur and strip checks completed: [Schur report](INDEPENDENT_CORRECTED_FAST_SCHUR.md), [strip report](INDEPENDENT_CORRECTED_FAST_STRIP.md). No real-axis pointwise limit or full-H resonance claim.
