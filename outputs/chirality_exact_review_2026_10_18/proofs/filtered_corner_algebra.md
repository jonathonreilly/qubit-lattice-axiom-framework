# Supplied filtered-corner algebra

Take canonical fermions on a periodic cubic lattice and the ungauged continuous-time walker h(k)=sum_a sigma_a sin(k_a). Corner labels v are in (Z2)^3, k=pi v, and the velocity determinant has sign (-1)^|v|. This is a statement about these zeros. Translation by(1,1,1) has symbol exp(i sum k_a), which equals that sign at the corners but is neither Hermitian nor an involution over the full Brillouin zone.

Two real, scalar, cubic-covariant finite filters are

f_NN(k)=(1-sum_a cos k_a)/2,
f_F1(k)=1-sum_a sin²(k_a/2) product_(b!=a) cos²(k_b/2).

At a corner, f_NN=|v|-1, while f_F1 is zero exactly on the three weight-one corners and one on the remaining five corners. Each is a finite trigonometric polynomial, so its position-space convolution has finite support. With z_a=sin²(k_a/2), f_F1=1-sum_a z_a product_(b!=a)(1-z_b): the subtracted sum is the probability of exactly one success in three independent Bernoulli variables. Thus f_F1>=0, and equality requires one z_a=1 and the other two zero. This proves its full-zone zero set directly rather than by a sampled grid.

At k=(pi,0,0)+q, f_F1=|q|²/4+O(|q|⁴), whereas f_NN=(-q_x²+q_y²+q_z²)/4+O(|q|⁴). The latter has additional zeros away from its target corners.

For chi_x=sum_y F_(x-y) psi_y, the canonical anticommutator is

{chi_x,chi_y†}=rho_(x-y), rho_r=(1/N)sum_k |f(k)|² exp(ik.r),

with identity on the spin/flavour indices. Filtered fields are not canonical independent modes unless rho is the identity kernel. Normal ordering and Fierz contractions must retain this rho, including lower-grade terms.

For a polynomial interaction built with every fermion leg filtered, {psi_(k0),chi_x†}=0 and {psi_(k0),chi_x}=0 whenever f(k0)=0. An even interaction therefore commutes with psi_(k0). At a walker corner h(k0)=0 as well, so this elementary mode decouples exactly in this supplied ungauged model. This does not show a gap in the complementary sector, absence of composite channels, or persistence under generic gauging/perturbations.

Momentum conservation for corner quartics is XOR addition in (Z2)^3. The finite table may enumerate light·mirror³, light³·mirror and light²·mirror² labels, but a forbidden elementary momentum channel does not exclude composites or a many-body phase. The original anomaly arithmetic checks selected cyclic subgroups; it is not a complete bordism or dynamical proof.
