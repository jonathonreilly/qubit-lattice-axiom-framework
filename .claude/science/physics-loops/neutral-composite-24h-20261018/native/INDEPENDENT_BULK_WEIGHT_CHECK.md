# Uniform slab source-weight route: independent check

Disposition: PASS as a constructive route, with the explicit local-pattern step below. The constants can be very small but are independent of transverse volume. No clustering or uniform positive excitation gap is required. No shared/canonical edits.

Let K=D-h sum_p P_p, D=-g E, g,h>0, in the connected all-positive row/column-X configuration space. The normalized ground amplitudes a(s) are strictly positive. All plaquette flips commute and are involutions. Fix p and minimize r(s)=a(ps)/a(s), writing m=r(s0). The two ground equations give exactly

 [D(ps0)-D(s0)]m
 =h sum_q [r(qs0)-m]a(qs0)/a(s0).

Each summand is nonnegative at this minimizer. For q=p, r(ps0)=1/m and a(ps0)/a(s0)=m, so the contribution is h(1-m^2). Since m<=1 by the reciprocal pairing,

 B m>=h(1-m^2),
 m>=(sqrt(B^2+4h^2)-B)/(2h)>0

for any uniform upper bound B on |D(ps)-D(s)|. The proposed B=32g is valid but unnecessarily conservative: an ordinary square plaquette has at most eight boundary edges, each E product changing by at most two, so B=16g suffices. Open boundaries only reduce this count. The reciprocal pairing also gives r(s)<=1/m, uniformly for every s and every plaquette p, using a common bound m0 depending only on g,h.

## Local-pattern probability: supply this step explicitly

The row/column constraints do not prevent prescribing a pattern on a fixed interior patch. Choose an auxiliary row and column outside the patch. For each patch site, a four-corner rectangle flip toggles that site and three auxiliary sites while leaving the other prescribed patch sites unchanged. Each such rectangle is a product of a bounded number of elementary plaquette flips, since the patch and anchors have fixed size. Hence every configuration can be mapped to one with all spins positive on the four sites of p and all their edge neighbors using at most K0 plaquette flips, with K0 independent of volume. The number of choices of such maps/preimages is bounded by a fixed constant depending only on the patch.

Along each path, squared amplitudes change by at least m0^(2K0). Summing over initial configurations and bounding the finite preimage multiplicity gives probability at least epsilon0>0 for the prescribed all-positive patch. On that event, flipping an interior plaquette changes E by -16 (eight boundary edges). This proves a uniform lower bound on the expectation of (E(ps)-E(s))^2. The construction is applied to plaquettes a fixed distance from the boundary; they number a positive fraction of the area for sufficiently large open boxes, or all plaquettes on sufficiently large tori. Any remaining finitely many small R>=3 can be handled separately using the already established strict positivity. A global all-positive configuration probability is neither needed nor asserted.

## Exact spectral moments

Let dmu(omega) be the positive spectral measure of (E-<E>)g at excitation energy omega=K-e0>=0, and Mj=integral omega^j dmu. Then

 M1=(1/2)<[E,[K,E]]>
   =(h/2) sum_(p,s) a(s)a(ps)[E(ps)-E(s)]^2.

The signs and factor one-half are correct. Using a(ps)>=m0 a(s) and the pattern probability above proves M1>=c1 A, where A is transverse area (or a comparable count of bulk plaquettes).

The exact third-moment identity is

 M3=(1/2)<[E,[K,[K,[K,E]]]]>.

The outer commutator has the displayed positive sign. In the ground spectral basis its two terms are respectively +sum omega^3|E_ng|^2 and -sum omega^3|E_ng|^2. Since K and E are sums of bounded finite-range terms, expanding the fourfold nested commutator leaves only connected support sequences. Each initial edge has a bounded number of such sequences, with fixed order and bounded local norms. Therefore the OPERATOR NORM of this nested commutator is at most C3 A; in particular 0<=M3<=C3 A. No decay-of-correlations premise enters.

Holder's inequality gives M1<=M0^(2/3) M3^(1/3), so

 M0>=M1^(3/2)/sqrt(M3)>=c0 A.

This proves an extensive variance/source-weight lower bound. For the periodic-height-four original coefficient source qO=-3(E-<E>)g, multiply by nine; for the open-height-four variant use (8/3)^2 instead. The constants remain coefficient-model constants and do not by themselves control a simultaneous microscopic lambda/R limit.

## Finite upper-frequency window

Choose a fixed Omega with C3/Omega^2<=c1/2. Then

 integral_(omega>Omega) omega dmu<=M3/Omega^2<=c1 A/2,
 integral_(0,Omega] omega dmu>=c1 A/2,
 mu((0,Omega])>=c1 A/(2Omega).

Thus a fixed finite upper-frequency window contains an extensive amount of positive excitation weight. This establishes no volume-uniform strictly positive lower frequency cutoff: the available argument permits some or much of that weight to approach zero. It also does not identify a single mode, a gap, a lifetime, a bulk scalar, or a thermodynamic limiting measure. It does rule out interpreting all source weight as a bounded number of corner contributions if these uniform estimates are retained.

## Quantitative 5x5 patch and constants: confirmed

Root's explicit construction improves the abstract pattern step. In a 5x5 patch, the 16 elementary plaquettes with lower-left coordinates 0,...,3 in each direction act on the upper-left 4x4 site bits by an invertible triangular binary map: each site bit receives its own lower-left plaquette bit plus only preceding coordinate bits. The fifth row/column carry the parity adjustments. For each prescribed 16-bit pattern alpha, the unique correcting flip subset T_alpha bijects its configuration class onto the all-zero class. The 16-bit patterns correspond bijectively to the 16-plaquette subsets.

With the sharper B=16g, let m=(sqrt((16g)^2+4h^2)-16g)/(2h). Each path uses |T_alpha| flips, so P_alpha<=m^(-2|T_alpha|)P_zero. Summing all patterns gives

 P_zero >=(1+m^-2)^(-16)=[m^2/(1+m^2)]^16=:p0.

The central plaquette with sites (1,1),(2,1),(1,2),(2,2) and its eight external edge-neighbor sites lie in the prescribed 4x4 region. On the zero/all-plus event, |Delta E|=16. Thus M1>=a N_cov with a=128 h m p0, where N_cov counts plaquettes admitting this patch. On a sufficiently large periodic torus N_cov=R^2. For open boxes one can use N_cov=(R-4)^2 and then a fixed area fraction for sufficiently large R; do not replace this by R^2 without that qualification.

For A=i[K,E], write A=sum_p A_p. Only eight boundary edges contribute, giving ||A_p||<=16h and support in a 4x4 box. At most 48 edge terms and 48 plaquette terms can meet that box (both are conservative counts). Hence ||[K,A_q]||<=1536 h(g+h), with support in a 6x6 box. A_p can meet this enlarged support only for at most 81 relative anchors. Therefore

 M3=(1/2)<[A,[K,A]]>
 <=(1/2)*81*2*(16h)*(1536h(g+h))*N
 =1,990,656 h^2(g+h) N.

The A identity has the positive sign and equals the earlier E triple-commutator moment. These are norm bounds and need no clustering. For periodic geometry, b=1,990,656 h^2(g+h), M0>=a^(3/2)N/sqrt(b); with Omega=sqrt(2b/a), M0((0,Omega])>=aN/(2Omega). For open geometry first replace a by its uniform covered-area fraction. The constants are tiny but strictly positive and explicit. A sequential fixed-R microscopic transfer followed by R growth remains distinct from a uniform joint lambda/R theorem.

## Stronger periodic-torus bound from the variational energy: confirmed

PASS; this replaces the very small local-pattern constant for the native periodic slab. The uniform all-positive X configuration is an allowed all-row/column-positive trial with E=Nb and zero plaquette-flip expectation. Thus e0<=-g Nb. Since e0=-g<E>-h<P>,

 <E>>=Nb-(h/g)<P>>=Nb-(h/g)Np.

Both inequality signs are correct; only <P><=Np is used. On the square torus Nb=2Np. Define B_p as the sum of the eight edge products crossing the boundary of plaquette p. Flipping p gives Delta E=-2B_p. Every edge crosses the boundary of exactly four plaquettes, so sum_p B_p=4E. (Edges belonging to a plaquette's perimeter have both endpoints flipped and are not in its crossing-boundary sum.)

The amplitude-ratio bound then gives

 M1 >=2 h m sum_p <B_p^2>
    >=(2 h m/Np)[sum_p <B_p>]^2
    >=2 h m(8-4h/g)^2 Np,

provided h/g<2. This condition ensures the lower bound on sum_p <B_p> is positive before squaring; without it the last step would not be licensed. Quantum variance positivity and ordinary Jensen/Cauchy over p justify the middle step without translation-invariant ground expectations or clustering.

For native periodic-height-four g=5,h=4, the sharper ratio bound gives m=(sqrt(80^2+4*4^2)-80)/8 approximately .0498756, and a=2hm(8-4h/g)^2 approximately 9.193. The conservative M3 bound b=1,990,656 h^2(g+h) remains valid. Thus the earlier M0 and finite-upper-window formulas apply with this much larger a. Omega=sqrt(2b/a) is about 7.9e3 in coefficient units, or about 62 Jz lambda^4 in physical energy units at leading order. This is still a low physical energy scale in the sequential weak-coupling limit, but is a broad window, not a pole location or sharp spectral threshold.

This shortcut is stated for the periodic transverse torus; open boundaries require their altered edge-incidence accounting or the earlier covered-patch bound. It uses the original fixed native ratio h/g=.8, not an additional tunable coupling assumption.
