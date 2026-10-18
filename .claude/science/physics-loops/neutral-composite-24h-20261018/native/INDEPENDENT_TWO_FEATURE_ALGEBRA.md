# Independent two-pair spin algebra and native-profile scaling check

Read `/tmp/neutral_pair_algebra_root.md`. The exact norm formula and Fourier/asymptotic prefactors are correct. A periodic center-phase convention requires the twist qualification below.

## Exact hard-core spin norm

Let Bdagger=sum_(i<j) f_ij s_i^- s_j^-, sum|f_ij|^2=1, and Phi symmetric with Phi_ij=f_ij/sqrt(2), zero diagonal. Then rho=Phi Phi dagger has trace one. For four distinct sites the coefficient of the computational four-flip state is exactly

2(f_ij f_kl+f_ik f_jl+f_il f_jk).

Comparison with the canonical-boson pair state gives canonical norm 2+4Tr(rho^2). Its forbidden repeated-site configurations have amplitudes 2sqrt(2) f_ij f_ik for a double occupancy at i and distinct j,k, and 2f_ij^2 for double occupancies at both i,j. Their total norm is

4 sum_i d_i^2-4 sum_(i<j)|f_ij|^4,
d_i=sum_j|f_ij|^2=2rho_ii.

Subtracting gives exactly

||(Bdagger)^2 vac||^2
=2+4Tr(rho^2)-16sum_i rho_ii^2+4sum_(i<j)|f_ij|^4.

This includes interference between all pair partitions of the same four sites. Independent random complex controls for N=4,5,6,8 directly sum the four-site amplitudes and agree within2e-15; script `/private/tmp/neutral_pair_algebra_control.py`.

## Translation-covariant prefactors

For Phi_ij=exp[iQ.(i+j)/2] phi(i-j)/sqrt(V), with normalized even relative wavefunction and phi(0)=0, the row density is rho_ii=1/V. With the compatible discrete Fourier convention phihat(k)=sum_r exp(-ik.r)phi(r), Parseval is (1/V)sum_k|phihat|^2=1. The singular values of Phi are |phihat|/sqrt(V), giving

Tr(rho^2)=V^-2 sum_k|phihat(k)|^4.

Also sum_(i<j)|f_ij|^4=(2/V)sum_r|phi(r)|^4. Thus

||(Bdagger)^2 vac||^2=2+4P-16/V+(8/V)sum_r|phi(r)|^4

has all factors correct.

### Periodic boundary phase

If Q_a=2pi m_a/L_a with an odd m_a, exp[iQ.(i+j)/2] alone is not periodic when one spin index crosses the seam. The relative wavefunction must obey the compensating twist phi(r+L_a e_a)=exp[-iQ_a L_a/2]phi(r)=(-1)^m_a phi(r). Its Fourier mesh is correspondingly shifted by half a reciprocal-grid step. This is a coordinate/gauge constraint, not an additional physical flux.

Alternatively choose even m_a, so the midpoint phase and a periodic phi are separately well-defined. That coarser allowed COM mesh still has spacing O(1/L) and does not change the campaign's threshold-mesh estimates. Using a periodic phi with an odd-m midpoint phase without this correction would not represent the intended translation-covariant native state. The norm/purity formulas remain valid with the compatible twisted Fourier mesh.

## Near-threshold native host profile

For the normalized host component, phi has relative z=0, so its Fourier transform is independent of kz. The kz sum still gives the three-dimensional normalization P=(1/V) times the two-dimensional Fourier average of |phihat|^4; it does not replace V by transverse area.

Near the quadratic minimum, write phihat approximately A/(delta+2kx^2+2bky^2). Direct integration gives

integral d^2k/(2pi)^2 (delta+2kx^2+2bky^2)^-2=c/delta,
integral d^2k/(2pi)^2 (delta+2kx^2+2bky^2)^-4=c/(3delta^3),
c=1/(8pi sqrt(b)).

Normalization fixes |A|^2=delta/c at leading order. Therefore P~1/(3c Vdelta). The numerator's cavity corrections and phi(0)=0 constraint reside in subleading/high-momentum pieces; applying this asymptotic requires the previously derived nonzero infrared coefficient and dominance of the normalized infrared host profile. A finite mesh must resolve sqrt(delta), with image/quadrature errors controlled.

Since sum|phi|^4<=1, the two explicit hard-core terms are O(1/V), smaller than P by a factor O(delta). Hence the stated host-only result follows:

||(Bdagger)^2 vac||^2=2+4/(3c Vdelta)[1+o(1)].

The asymptotic leading excess is positive; at general finite profiles the exact hard-core corrections can instead reduce the norm. On V~lambda^-12 and delta=lambda^alpha, the leading excess scales lambda^(12-alpha).

## Scope

This controls one vacuum two-pair norm for an operator built from existing spins. It is neither an operator-norm bosonic commutator theorem nor a finite-density many-feature limit. Four distinct spin flips can have fewer than eight longitudinal walls if they share a column at nearby layers; no N=8 projection was made in this algebra. Projection would change the norm and needs a separate calculation.

The full native bound feature also includes interval rays with different spin-flip number. Their omitted norm may be small in delta yet much larger than the tiny1/(Vdelta) algebra correction along the chosen growing boxes. Therefore a small single-feature host omission alone does not transfer this precise two-feature correction to the full branch. Multi-feature errors and cross terms must be bounded at the actual target scale. No dynamical interaction, scattering, source/detector bridge, or empirical scalar field follows from this exact host-pair algebra.

## Follow-up: complete K1 string operator, two-copy control

Checked the appended full-string construction in `/tmp/neutral_pair_algebra_root.md`. Its combinatorial bounds are sound for the stated canonical all-lowering extension, after the interval cutoff and compatible periodic COM convention.

Let eta^2 be the normalized one-feature ray probability, and split Bdagger=B_Hdagger+B_Rdagger. Each host support has two distinct columns at one layer; each ray support has two adjacent columns occupied on one common interval of length ell>=2. Products with overlapping spin sites vanish because (s_i^-)^2=0. For disjoint supports the output is determined by their union. Thus for two coefficient families c,d,

||B_cdagger B_ddagger vac||^2
<=sum_U M(U) sum_(A disjoint B, A union B=U)|c_A d_B|^2,

where M(U) counts ordered admissible decompositions with A belonging to the first family. Complex phases do not affect this Cauchy-Schwarz bound.

### Host-ray count

The union cardinality determines ell. For ell=2, its six sites admit at most choose(6,2)=15 choices of the host pair, after which the ray is fixed. This bound deliberately includes choices that violate the actual host/ray geometry, so is conservative.

For ell>=3, exactly the two ray columns can contain at least three occupied sites: the host contributes at most one site to each of its two distinct columns. The ray column pair is therefore identifiable from the union. In either ray column the occupied set differs from its length-ell interval by at most one host site. There are at most two candidate length-ell intervals per column, hence at most four common choices (indeed this is conservative). The host is fixed by the complement. Thus M_HR<=15 uniformly and

||B_Rdagger B_Hdagger vac||<=sqrt(15) eta sqrt(1-eta^2).

### Ray-ray count

For two ray supports, let S=ell_A+ell_B=|U|/2. At most four columns are occupied. Choose the first ray's two columns in at most six ways, then its interval's ordered start/end among at most2S occupied longitudinal coordinates, yielding at most24S^2 possibilities. Once that ray is specified, the second is its complement; imposing its actual geometry can only reduce the count. This counts ordered decompositions, as required, including interchange of the two rays where appropriate.

Therefore

||B_Rdagger^2 vac||^2
<=24 sum_(A,B)(ell_A+ell_B)^2 |c_A|^2|c_B|^2
<=96 mu_2 eta^4,

where mu_2 is the conditional ray second length moment. The geometric ray ratio uniformly below0.6 gives a uniform finite mu_2. Hence the ray-ray norm is O(eta^2), with no volume factor.

### Comparison with the normalized host operator

Write B_Hdagger=sqrt(1-eta^2) B_hatHdagger. The exact host norm is bounded by sqrt(6), using its canonical-boson upper bound. Since lowering strings commute, including the zero products from overlap,

B_full dagger^2-B_hatH dagger^2
=-eta^2 B_hatH dagger^2+2B_Hdagger B_Rdagger+B_Rdagger^2.

The resulting vacuum-vector difference is O(eta), and both vacuum-vector norms remain bounded. Their squared norms therefore differ by O(eta) as well. With eta=O(sqrt(delta)log(1/delta)), the complete canonical string operator satisfies a two-copy norm tending to2 when delta->0 and Vdelta->infinity, given the established host-profile asymptotic.

The leading host purity correction must not be advertised as the leading correction for the complete operator: the O(eta) bound can be much larger. This extension proves convergence to2, not the finer full-mode coefficient.

### Periodic tails and interpretation

Cutting ray lengths below Lz/4 makes start/end interval representation unambiguous even for intervals crossing a coordinate seam; use cyclic endpoints and the chosen short oriented arc. The weighted geometric tail controls the S^2 factor in the ray-ray bound, so the omitted tails remain exponentially small at the two-copy level, rather than relying only on a one-feature norm estimate. The accepted even-COM-index convention eliminates the separate midpoint-phase ambiguity.

This is a defined all-lowering extension of a one-feature state, not a uniquely selected dynamical field away from vacuum. It establishes neither a projected N=8 norm, a CCR operator bound, finite-density statistics, an eigenstate of a multi-feature Hamiltonian, nor an actual-ground spectral statement. Within those limits, the proposed full-string two-copy control closes the previously flagged host-only normalization gap.
