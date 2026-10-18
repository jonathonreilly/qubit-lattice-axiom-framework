# Focused fixed-order slow-host and scalar-graph check

Disposition: PASS for the strict leading slow-host dissipation and the stated scalar symmetry reduction; PASS for finite-support intercomponent vertices at each fixed order under the connected local-coefficient convention. This does not certify the entire fixed-order pole synthesis (in particular its fast-host continuation step), or a full microscopic pole.

## Exact strict dissipation, without quadrature

Let H0 be nearest-neighbor hopping -1 on Z², with symbol h(k)=-2(cos kx+cos ky). Use the outgoing boundary value G=(E+i0-H0)^-1. At E=-2 its Fermi curve is regular: the critical energies are -4,0,4. Its on-site density is strictly positive, so Im g00<0.

The five removed sites decompose under the square group into A1 spanned by c=delta0 and s=(delta_ex+delta_-ex+delta_ey+delta_-ey)/2, plus B1 and the two-dimensional vector representation. H0 c=-2s gives

 g_cs=(1-E g_cc)/2,
 g_ss=(E² g_cc-E)/4,
 det G_{c,s}=(E g_cc-1)/4.

At E=-2 this determinant is nonzero. These signs agree with the root proof. Each other hole representation has a nonzero Fermi-curve form factor (cos kx-cos ky, sin kx, or sin ky); their spectral densities are strictly positive, so their scalar Green eigenvalues cannot vanish. Thus the entire five-site hole Green matrix is invertible. For the A1 calculation only the displayed two-dimensional block is needed.

Let A=(delta_2ex+delta_-2ex+delta_2ey+delta_-2ey)/2 and let h denote the hole subspace. The compressed Green function is the exact Schur complement

 G^punct_AA=G_AA-G_Ah G_hh^-1 G_hA.

Set b=G_hh^-1 G_hA and w=A-sum_h b_h delta_h. Then G w has zero hole components, whence w†G w=G^punct_AA. Consequently

 -Im G^punct_AA = pi integral_BZ |Ahat(k)-bhat(k)|² delta(E-h(k)) dk/(2pi)².

This identity remains valid for complex b: it uses w† Im(G) w, not a mistaken bilinear square of the outgoing amplitudes. By square symmetry b lies in span{c,s}. Write u=cos kx, v=cos ky. On the E=-2 curve u+v=1, the Fourier hole correction is therefore constant, whereas

 Ahat=cos(2kx)+cos(2ky)=2(u²+v²)-2=-4uv.

This is not constant on the curve: it equals 0 at (u,v)=(1,0), and -1 at (u,v)=(1/2,1/2). Both are regular points of the energy curve, and continuity gives arcs of positive measure on which no single constant cancels this function. The integral is strictly positive. Hence Im Sigma0=Im G^punct_AA(-2)<0 analytically, without numerical values. In particular Sigma0 cannot equal -1.

The unperturbed outgoing local Green functions admit continuation through a small neighborhood of this regular energy; the nonzero finite hole determinant preserves it under the puncture. Small fixed-range bulk changes and small finite contacts preserve regularity and local invertibility for a sufficiently small common neighborhood, with constants allowed to depend on the fixed order. This is a local outgoing continuation, not the bounded physical resolvent across continuous spectrum.

## Scalar graph and physical symmetry

The uniform polarized background and compact even-relative-plane-parity E8 configuration space are indispensable premises. The compact configurations consist of two columns with a common interval. Under the physical square rotation (spatial quarter-turn combined with spin-Z rotation), their relative phase is (-1)^ell. Thus physical scalar states at ell=1 transform as orbital B1, provided the stated even coordinate-reflection character is also imposed. Quarter-turn character alone would not distinguish B1 from B2.

At ell=1 the normalized relative form factor is d=(delta_ex+delta_-ex-delta_ey-delta_-ey)/2, Fourier cos kx-cos ky. The zero-transverse-COM relative hopping is -2; zero-longitudinal-COM endpoint moves give -2. The scalar adjacent-column chain is E_ell=(|x,ell>+(-1)^ell |y,ell>)/sqrt(2), ell>=2, and couples to d with -2. There is exactly one such adjacent scalar arm. B1 wavefunctions vanish at the origin and their neighboring amplitudes sum to zero. Removing the origin therefore has no effect within this orbital symmetry sector for symmetry-preserving hopping. The other compact separations are not removed by symmetry: they remain the slow/closed channels of the synthesis.

At ell=2 the physical scalar has orbital A1, giving the punctured-cross slow host and axial source A used above. The scalar identification and normalizations agree with the independently checked native two-wall and axial two-channel derivations. They do not imply a scalar particle or a selected equilibrium background.

## Fixed-order support assertion

In the supplied zero-block local homological convention, each fixed-order coefficient is a sum of translates of connected clusters with a bounded support diameter/cardinality rho_m. This is the crucial input; a statement about arbitrary block-unitary gauges would not suffice.

A matrix element changing the column pair for a long common interval must change a number of spins growing with ell, hence is impossible for ell beyond the fixed cluster bound. A matrix element changing interval length for columns at arbitrarily large transverse separation must touch both separated endpoint spins in one connected cluster, hence is impossible beyond the transverse bound. Therefore transitions between the ell=1 and ell=2 hosts, between their associated distinct long arms, or from the retained graph into the other compact separations have both bounded ell and bounded relative separation. After all COM translations are quotiented, their support is finite-dimensional. This proves finite rank at each fixed m, not a uniform finite rank as m tends to infinity.

Far from this finite region, host coefficients are finite-range translation-invariant; long-arm coefficients are finite-range Toeplitz plus affine diagonal, as established in NATIVE_FINITE_RANGE_ARM_STRUCTURE.md. The extensive affine term is not a bounded contact perturbation and must remain in the arm Hamiltonian. The finite-rank claim applies to crosscomponent couplings and exceptional boundary terms, not to that tension or to bulk dispersion changes.

Read: root synthesis steps 3 and 6; NATIVE_FINITE_RANGE_ARM_STRUCTURE.md; FROZEN_ARM_ELIMINATION_PROOF.md; /private/tmp/neutral-bulk-two-wall-channel-check.md; /private/tmp/neutral-axial-two-channel-check.md; /private/tmp/neutral_slow_host.py. No repository changes; no empirical input used in the strict-sign proof.

Root synthesis SHA256: 416275b6943bde8cfa4679df0489ca8cb09c31648b36abcacf5b39833fdc78e1
