# Two explicit finite reflection-kernel matrices

The supplied model is pure U(1), beta=0, with normalized Haar link measure and the flat plaquette weight 1(|arg U_p|<delta). Time has two open slices; link reflection exchanges them across their connecting temporal links. Spatial boundary configurations are restricted to strictly admissible plaquettes. No matter determinant, overlap operator, continuum limit or arbitrary geometry is included.

Integrating the crossing temporal links gives

K(u,v)= integral dg product_(spatial links l) 1(|wrap(u_l-v_l+(dg)_l)|<delta).

One redundant global gauge angle integrates to one. Positive-half spatial weights are one on the strictly admissible configurations used below. Thus these formulas describe the specified finite crossing kernel. They do not classify other weights or reflection geometries.

## T22 geometry and exact rational value

The spatial slice has four sites (i,j), i,j in {0,1}, eight oriented links and periodic spatial boundary conditions. Write its link tuple as (a00,a01,a10,a11,b00,b01,b10,b11), with a[j,i] the x-link beginning at (i,j) and b[i,j] the y-link. For x in {0,delta/12} and s in {-11delta/12,0,11delta/12}, choose

u(x,s)=(x,0,s+x,-s,0,0,0,0).

Its plaquettes are (-s,s,s,-s); both row Wilson angles are x and both column Wilson angles zero. All six configurations have plaquette margin at least delta/12.

For 0<delta<pi/4 the interval reduction has no winding contribution. In a gauge with one fixed angle, opposite links restrict the four row/column gauge differences to centered intervals. Their widths for a pair of configurations are a,a,w,w, where w=2delta and a=w-|x-x'|. The only relation between those four differences has determinant-one coordinates; integrating three independent differences is the convolution of their four interval indicators at sigma=s-s'. Therefore

K(u(x,s),u(x',s'))=(2pi)^(-3) B4(s-s';a,a,w,w),

B4(z;l1,l2,l3,l4)=1/6 sum_(epsilon_i=+/-1) (product epsilon_i) [z+(sum epsilon_i l_i)/2]_+^3.

Order configurations by x first and increasing s. For c=(1,-9/5,1,-1,9/5,-1), exact rational arithmetic gives

c^T B4 c = -delta^3/100.

At delta=3/5 this is -27/12500; the normalized crossing-kernel value includes the positive factor (2pi)^(-3). Homogeneity of the four-box convolution is degree three. The primary checks the normalized coefficient with exact fractions and supplies the complete matrix and exact congruence pivots. This is an explicit value for a specified matrix, not a general theory exclusion.

## O12 geometry and finite inertia

The open spatial strip has two squares sharing one edge, six vertices and seven links. Orient the shared link so its contribution to the two plaquette angles has opposite signs. Integrating a spanning tree leaves the two plaquette differences F1,F2 and five independent Haar angles. With B=1_[-delta,delta] and T3=B*B*B,

K(phi,phi')=(2pi)^(-5) integral_(-delta)^delta T3(F1-e) T3(F2+e) de,

T3(z)=1/2 sum_(epsilon_i=+/-1) (product epsilon_i) [z+delta sum epsilon_i]_+^2.

At delta=3/5 take all16 pairs of plaquette angles in {-11/20,-11/60,11/60,11/20} squared. Each angle has margin1/20. The no-winding condition delta<pi/3 holds. Breakpoints occur where either truncated quadratic changes branch. On each resulting interval the integrand has degree at most four; rational Boole quadrature is exact. A symmetric rational Schur-congruence reduction has15 positive and1 negative nonzero pivots. The positive Haar factor changes no inertia. The primary prints the full matrix and pivots; it makes no claim about larger strips or infinite volume.

## Smooth test-function interpretation

The point configurations lie strictly inside the admissible set. The crossing kernel is continuous: the difference of two products of bounded indicators is bounded by the sum of their individual differences, and each shifted interval boundary has Haar measure proportional to the shift. Smooth nonnegative normalized bump functions supported around each configuration therefore approximate the finite matrix quadratic form. Gauge averaging the bumps preserves support and the quadratic form because K is invariant in each argument.

For T22, if every link angle in each bump differs from its center by at most epsilon, each plaquette changes by at most4epsilon, so epsilon<delta/48 preserves admissibility. Each pairwise link difference changes by at most2epsilon. The eight-factor union bound gives |Delta K|<=16epsilon/pi. With S=sum|c_i|=38/5 and q=delta^3/[100(2pi)^3], choosing additionally epsilon<q*pi/(32S^2) makes the quadratic-form error less than q/2. Such smooth bumps have a strictly negative value for this finite kernel. The same continuity argument applies to the finite O12 matrix and its negative rational congruence direction.

The explicit matrix identities and construction are live. Any promotion to an exclusion of a broader family of theories, weights, geometries, dimensions, matter prescriptions or infinite-volume limits requires its own hypotheses and review packet; none is asserted here. Historical NT2 universal wording and numerical O22/O1L searches are retained in exact recovery, not used as premises of these identities.
