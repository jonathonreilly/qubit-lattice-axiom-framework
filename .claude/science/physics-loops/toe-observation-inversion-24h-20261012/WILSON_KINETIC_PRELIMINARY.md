# Provisional kinetic matching continuation — not yet independently checked

Author scratch derivation, 2026-10-12. Same literal-link continuous-time Wilson U(1) model as TARGET.md. No use of the provisional mass coefficient is needed in these integrals. This extends the interaction-matching residual only; no physical inference or theorem-facing use until checked. Treat the bare mass m>0 below as an infrared regulator and specify the order of limits: external frequency/momentum derivatives at fixed m, then m tends to zero. The primary bare action has a=w=1 in this limit. Mass subtraction, optional preservation of a^2=1-m_bare, and physical pole interpretation must be handled separately.

## Fermion linear inverse-propagator coefficients

Set W=sum(1-cos k_i), M=m+W, E^2=sum sin^2 k_i+M^2, omega^2=2W. Let deltaD=e^2[i gamma_0 p_0 Z_t+i sum gamma_j p_j Z_s+scalar+...]. Spatial cubic symmetry makes the integrated Z_s the average of three directions. This is an expansion around Euclidean p=0 at fixed regulator m; do not call its finite-m pole speed without further argument.

For general external p, the exchange coefficient along i gamma_j has numerator
 N_0=2(p_0-k_0),
 N_j=[3-cos(2p_j-k_j)]sin(p_j-k_j)-M(p-k)sin(2p_j-k_j)
 over R=(p_0-k_0)^2+E(p-k)^2 and photon K^2=k_0^2+omega(k)^2.
At p=0,
 A_j=1-2cos^2 k_j+3cos k_j-2M cos k_j,
 B_j=2sin^2 k_j(M-3+cos k_j)(M+cos k_j).
Frequency integrals are
 I1=1/[2E omega(E+omega)],
 I2=(2E+omega)/[4E^3 omega(E+omega)^2].
Then Z_t=integral[-2I1+4E^2 I2], Z_s=integral[mean(A)I1+mean(B)I2-1/(4omega)]. The last term is the derivative of the literal-link seagull, not an arbitrary counterterm. Therefore
 Z_s-Z_t=integral[(mean(A)+2)I1+(mean(B)-4E^2)I2-1/(4omega)]
 with d^3k/(2pi)^3. At m=0 the leading infrared logarithm cancels after continuous-frequency integration and cubic averaging; fixed-m versus exactly massless limits still require a check.

## Photon electric and magnetic coefficients from filled-band response

Let d=(sin k_1,sin k_2,sin k_3,M), n=d/E, v_i=partial_i d=(cos k_i e_i,sin k_i), g_i=partial_i E=n.v_i=sin k_i(cos k_i+M)/E. Here v_i is a Clifford coefficient vector; g is the group velocity. The interband current strength is S_i=tr[P_+J_i P_-J_i]=2(1-g_i^2).

Supply the filled negative-band vacuum, ordinary response/quantization and temporal gauge continuation. The small external-frequency kernel at zero photon momentum is the static-subtracted interband response
 Pi_ii(Omega,0)-Pi_ii(0,0)=e^2 integral S_i Omega^2/[E(Omega^2+4E^2)].
Thus the electric coefficient averaged over i is
 Z_E=integral [1-mean(g_i^2)]/(2E^3).

For a static transverse photon in x direction with polarization y (x!=y), the vertex is independent of k_x, and the exact bubble can be symmetrized at internal p plus/minus external k_x/2. Let u=n.v_y=g_y, n'=partial_x n, n''=partial_x^2 n, E''=partial_x^2 E. Expanding the subtracted bubble gives
 Z_B,xy=integral { [|n'|^2+u(n''.v_y)-(n'.v_y)^2]/(2E)+(1-u^2)E''/(4E^2) }.
At fixed m>0, integration by parts on the periodic Brillouin torus gives the equivalent expression
 Z_B,xy=integral [1-2h^2+6h g_x g_y-5g_x^2 g_y^2]/(2E^3), h=sin k_x sin k_y.
Check this equality numerically before relying on it. Average the six ordered x!=y pairs for cubic convergence. A finite static-subtracted bubble at decreasing external momentum is an independent control of this derivative expression.

The individual Z_E and Z_B have an infrared logarithm as m tends to zero. Their difference must use a consistent regulator and order of limits. At exactly m=0 the leading difference of the integration-by-parts density is (5sum n_i^4-3)/(12|k|^3), whose spherical average vanishes but whose absolute integral diverges. Blindly dropping the origin or using an unqualified massless tensor quadrature is therefore insufficient. In the continuum small-m region the angular-average difference includes m^2 k^2/[6(k^2+m^2)^(7/2)], with finite full radial integral 1/(60pi^2). This is a warning about noncommuting limiting/derivative operations, not a separately claimed physical counterterm. A gauge- and model-consistent matched subtraction or explicit fixed-m limit is required.

If these coefficients and the pole/gauge matching are established, the candidate relative velocity at order e^2 would involve (Z_s-Z_t)-(Z_B-Z_E)/2, with any deliberately chosen bare speed shift stated separately. Along the earlier bare matching curve a^2=1-m_bare, a critical bare mass of order e^2 would itself shift a at this order. Do not insert the unverified mass coefficient, declare a speed exclusion, or equate Euclidean off-shell coefficients to a finite-m observable silently.
