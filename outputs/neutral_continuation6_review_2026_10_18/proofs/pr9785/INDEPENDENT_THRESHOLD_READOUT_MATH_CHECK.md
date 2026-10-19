<!-- Original PR9785 source SHA256 85fd0ffd5348e5c555df0803cdfde15dac01833a835ee44a28448d1f2242a409. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Original-readout threshold measure: independent check

Disposition: PASS for the coefficient spectral-measure scaling limit, including the threshold neighborhood and bound atom. The microscopic transfer paragraph is outside this focused check and is being checked separately. Read /tmp/neutral_threshold_readout_root.md and reused the verified exact cavity expansion. No shared/canonical edits.

## Exact root resolvent and normalization

Let f=(-1,b) in the normalized even root basis and define mu as its spectral measure for the complete host-plus-rays coefficient operator. Then m(z)=f^T(z-H)^(-1)f has negative imaginary part in the upper half-plane. Algebraically

 R=(G^-1-sigma I)^-1=sigma^-2 T-sigma^-1 I,
 T=(A+2DD^T/g)^-1,

and the rank-one inverse formula gives exactly

 m=sigma^-2 f^T A^-1 f-sigma^-1 f^T f
   -2sigma^-2(f^T A^-1D)^2/(g+q),
 q=2D^T A^-1D.

The transpose/square is correct for the analytic resolvent and real f. No absolute square belongs inside this complex identity. Invertibility of A on the shallow-bound energy scale follows from its simple small edge eigenvalue of order 1/log(1/delta); its energy variation is exponentially smaller.

At the bound root q=-g~c log(1/delta). Dominance of the critical eigenvector v gives A^-1D~qv/[2(v.D)]. Thus, writing ell=log(1/delta),

 N/ell^2 -> c^2(f.v)^2/[2sigma^2(v.D)^2]=c W0.

This agrees exactly with the previously checked bound-residue coefficient W0=c(f.v)^2/[2sigma^2(v.D)^2]. The regular term is O(ell), hence vanishes after division by W0 ell^2. This argument uses the nonzero critical source overlap; otherwise the normalization and limit would change.

## Complex scaled transform

For every fixed z in the upper half-plane, locally uniformly in z,

 g(Eh+delta z)+q(Eh+delta z)=c log(-z)+o(1).

The branch of log(-z) has argument in (-pi,0). The retarded sign is therefore correct. For the rescaled positive measure

 nu_delta(B)=mu(Eh+delta B)/(W0 delta ell^2),

its Stieltjes transform is exactly m(Eh+delta z)/(W0 ell^2), not delta times that expression. Consequently

 integral dnu_delta(s)/(z-s) -> M(z)=-1/log(-z).

The root draft's displayed cancellation of delta is correct. On the positive axis, log(-s-i0)=log s-i pi. Hence -Im M(s+i0)/pi=1/[(log s)^2+pi^2]. At z=-1, log(-z)=-(z+1)+O((z+1)^2), so M has residue +1. Near z=0, M tends to zero and has no threshold atom. There is no other negative-axis singularity.

## Positive-measure convergence, including s=0

Pointwise real-axis densities alone would not prove the desired limit. The locally uniform complex-transform convergence plus positivity does, with the following direct argument.

At z=i, -Im M_delta(i)=integral (1+s^2)^-1 dnu_delta(s) is uniformly bounded. This supplies uniform mass bounds on every compact interval and a uniform weighted tail bound. For a compactly supported continuous test F, integrate the Poisson-smoothed measures against F:

 integral F(x)[-Im M_delta(x+i eta)]dx/pi
 =integral (P_eta*F)(s)dnu_delta(s).

For fixed eta>0, complex convergence gives convergence of the left side. The difference between the right side and integral F dnu_delta tends to zero uniformly in delta as eta down to zero: on a fixed larger compact interval, use uniform continuity of F, the approximate-identity property, and the uniform local mass bound; outside that interval, the Poisson tail is bounded by C_F eta/(1+s^2), controlled by the weighted bound. The same reasoning applies to the limiting Herglotz measure. This proves vague convergence on every compact real interval, including intervals crossing zero and containing the bound atom, without presuming a pointwise density bound at zero.

The measure represented by -1/log(-z) is

 nu=delta_(s=-1)+1_(s>0) ds/[(log s)^2+pi^2].

Its continuum has infinite total mass but finite integral against (1+s)^-1 at infinity, so its ordinary Stieltjes transform is well-defined. The density and pole follow from the preceding boundary values; any additive real constant is fixed to zero by decay along the negative real axis. A possible linear Herglotz term is also absent since Im M(iy)/y tends to zero. These observations verify the transform identification rather than merely naming a continuity theorem.

Therefore for every compactly supported continuous F (and hence every smooth such F),

 integral F((e-Eh)/delta)dmu(e)/(W0 delta log^2(1/delta))
 ->F(-1)+integral_0^infinity F(s)ds/[(log s)^2+pi^2].

The bound mass and continuum belong to the same original root-source spectral measure; this is stronger than choosing a normalized bound vector. The source's physical leading factor lambda multiplies the measure by lambda^2, and the physical energy rescaling must separately include Jz lambda. No additional factor of two from the inversion-even convention appears: the normalized two-root basis and W0 already use that convention.

This result is a threshold scaling law for the coefficient observable response. It does not by itself transfer to the full microscopic Hamiltonian, prove a microscopic isolated atom, or establish a prepared particle, lifetime, or scalar interpretation. In any later microscopic transfer, an atom in this scaling limit may represent weight in a shrinking window rather than an exact finite-lambda eigenvalue.
