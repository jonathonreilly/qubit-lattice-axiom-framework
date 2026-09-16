# Working target: retain the fermion energy in the first vacuum correction

The logarithmic bare-photon inverse norm in BLOCK03 is not by itself the denominator of a vacuum correction. The current acts on the filled Weyl sea and creates a particle-hole pair. Keeping that energy may give a volume-uniform first perturbative coefficient per unit volume. This is a proposed next derivation, not a nonperturbative phase theorem.

Reference: periodic cubic lattice, unit Maxwell dispersion omega(k)=|2sin(k/2)|, zero photon mode omitted; paired free two-band Wilson sectors, b=0, zeta=1/2,

    h(p)=sin px sigma1+sin py sigma2
         +(5/2-cos px-cos py-cos pz)sigma3.

Weyl nodes are (0,0,+/-pi/3), with linear nondegenerate cones. Fill the negative band; at exact finite-volume nodes choose any rank-one occupation in the zero eigenspace. The choices should disappear in the per-volume limit, but this must be proved.

With midpoint link phases, the Hermitian vertex j_i(p,k)=-partial_i h evaluated at the midpoint for each directional hopping term satisfies the exact lattice Ward identity

    sum_i 2sin(k_i/2) j_i(p,k)=h(p)-h(p+k).

For x and y directions its operator norm is exactly one; the z norm is at most one. Let M_i be its negative-band to positive-band matrix element and P_T(k) the real midpoint transverse projection. For one species the first correction norm per volume, after removing the factor g^2, is

    (1/(2V^2)) sum_(k != 0,p)
      [M(p,k)^* P_T(k) M(p,k)]
      /[omega(k)(omega(k)+epsilon(p)+epsilon(p+k))^2].

The second-order energy density uses the first power of the last denominator. Paired species add orthogonal particle-hole channels. This formula needs a direct Fock/sign/normalization check.

Proposed uniform proof: finite Weyl nodes imply epsilon(p)>=c dist(p,nodes). Grid counting gives N_L(epsilon<=r)/V <=C r^3+C/V. Hence

    (1/V)sum_p [omega+epsilon(p)]^-2 <= C+C/(V omega^2).

The local vertex numerator is at most3. The double sum is bounded by C[(1/V)sum_k omega^-1+(1/V^2)sum_k omega^-3], which is uniformly bounded in3D since the second term is O(log L/V). The exceptional exact fermion node occupations therefore cause a vanishing correction. The photon-soft part below lambda should obey C lambda^2+C(1+log(L lambda)_+)/V, and vanish after the volume limit then lambda->0.

A successful proof would show that the coupled free vacuum has a finite first perturbative norm density despite the bare-photon inverse failure. It would not construct a convergent perturbation series, a global infinite-volume vacuum vector, a fixed-g phase, or a running charge. Subsequent current correlations, counterterms and compact nonperturbative defects remain to be controlled.
