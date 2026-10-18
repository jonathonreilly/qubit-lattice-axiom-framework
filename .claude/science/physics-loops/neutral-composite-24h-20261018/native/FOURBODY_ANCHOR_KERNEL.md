# Root exact on-shell contact kernel at native T-junction anchor

This is a coefficient-level plane-wave contact kernel, not an exact four-body scattering amplitude or decay rate. Two native N4 bound features at Q=(0,pi,0), Eb=-3sqrt2, have pair host coefficients (unnormalized) f((x,y),(X,Y))=0 unless|Y-y|=1, and then (-1)^min(y,Y) r^|X-x| with r=1/sqrt2. The native attached y-ray length2 coefficient is g=-r f_root. Original ground readout is leading-dark at this anchor; do not claim a measured scalar coupling here.

Restrict output four-singleton states S to a common z layer. Host-host amplitude of Bdag² is A(S)=2sum_threepairings f_ij f_kl. The action of K8 on this output receives four-singleton hopping (every mixed XX/YY swap -1) and six-spin host-ray inputs: 4sum_adjacent_y_pairs g_ij f_remaining. The latter contains two vertical endpoints and the factor2 from Bdag². No other flip number contributes to this output.

Using the exact two-body equation, ray terms cancel the pair bound-energy terms. Only forbidden cross-pair hops remain:
 R(S)=[(K8-2Eb)P8Bdag²]_S=4sum_(i->j occupied nearest xy neighbors) f(j,k) f(j,l),
 wherek,l arethetwoother sites. The sum is directed. This is the actual projected native contact residual in this output channel, not a supplied potential. It can be checked directly against the full finite-bit K1 action including6flipinputs.

Choose outgoing two momenta +(theta,0) and two -(theta,0), where c=cos theta=3sqrt2/4-1. Totalmomentum0=2Q modulo2pi and free four-singleton energy-8(c+1)=2Eb. Use unnormalized symmetrized plane factor
 F(S)=sum_(two-site subsets T) exp[i theta(2sum_(i in T)x_i-sum_(i in S)x_i)].
Its six terms are real in total. Fix translation normalization of the contact kernel by
 Kcontact=lim [sum_allunorderedS F(S)R(S)]/(numberxytranslations),
 equivalently(1/4)sum_(S containsorigin)F(S)R(S). Both sums concern a commonlayer. No crosssection normalization is inferred.

Anchor eachdirectedcontacthop atj=0, i=d nearestneighbor. Then
 Kcontact=4sum_d sum_(k<l; k,l not0,d) f(0,k)f(0,l)F({0,d,k,l}).
LetA0=sum_x r^(2|x|)=3, A2=sum_x r^(2|x|)cos(2theta x)=(1-r4)/(1-2r²cos2theta+r4).
Summingthetwo y signs makes sum_k f(0,k)e^(i theta x_k)=0 before exclusions. For d=±ex, allowedS_theta=0,Q0=2A0,Q2=2A2. For d=±ey, exclusionofdremoves±1, soS_theta²=1,Q0=2A0-1,Q2=2A2-1.
The unorderedk,l sum of F is cos(theta d_x)[3S_theta²-Q2-2Q0]. Therefore
 Kcontact=48-16(1+c)A2-32(1+c)A0,
 approximately -59.49879, strictlynonzero. Geometric sums convergeabsolutely; no infinitevolume truncation neededfornonzerocertificate.

This establishes a native on-shell Born/contact numerator to a compatible free breakup channel. Exact outgoing four-body distorted states, repeated collisions and full-H corrections are not included. Nonzero Born numerator doesnotprove nonzero exactS, loss ofanembeddedstate or a lifetime. The incomingcompositesareanchor-sized, not the divergentnearthresholdfeature; extensionto bnearbc isopen. Continuityto smallb might preserve numerator but must check movingchannel andnormalization beforeclaim. Allmodeldevelopment, noempiricaldata.
