<!-- Original PR9797 source SHA256 a44cb57253507bb13e92844a06e1864b6522748ba069ce12d4d26586a43e8c2d. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# A nonvanishing response density in the native slab coefficient model

Status: bounded-support. This result applies at the native ratio g=5,h=4,
without the auxiliary small-u expansion. It concerns the periodic transverse
R by R four-layer slab. Take R>=13 for the explicit local-word bound below.
Let N=R^2, E=sum nearest-neighbor Z_i Z_j in the rotated column basis,
P=sum elementary four-spin X plaquettes, and K=-gE-hP. These are precisely
the derived native coefficients; no new physical interaction is introduced.
Use the all-row/column-positive block. Its strictly positive ground has the
same original-readout response as every global ground, as proved in
FOUR_LAYER_COLLECTIVE_PROOF.md. Write its amplitudes a(s)>0 and energy e0.

## 1. Uniform local amplitude ratio

Fix a plaquette flip p and r(s)=a(ps)/a(s). Let m_actual=min_s r(s).
All plaquette flips commute, including in this symmetry block. Subtracting
the ground equations at s and ps, at a minimum of r, gives

 [D(ps)-D(s)] m_actual
 =h sum_q [r(qs)-m_actual] a(qs)/a(s)
 >=h(1-m_actual^2),

where D=-gE and the q=p summand is displayed separately. A plaquette changes
eight boundary edges, each by at most two, so |D(ps)-D(s)|<=16g. Therefore

 m_actual>=m=2h/[sqrt((16g)^2+4h^2)+16g].

The inverse flip gives the upper bound 1/m. This bound is independent of R,
requires no correlation-length premise, and is valid at h/g=4/5.

## 2. An extensive first spectral moment

Let mu_E be the positive excited spectral measure of (E-<E>)g, with moments
M_j=int omega^j dmu_E. Exact ground-state identities give

 M1=(1/2)<[E,[K,E]]>
   =(h/2) sum_p,s a(s)a(ps)[E(ps)-E(s)]^2.

Let Bp be the sum of the eight edge products across the boundary of p.
Then E(ps)-E(s)=-2Bp(s). The ratio bound implies
M1>=2hm sum_p <Bp^2>.
The uniform Z-basis configuration in this rotated notation (the original
logical-X-polarized vacuum) is a variational state with energy -2gN. Since
<P><=N, the actual ground satisfies <E>>=N(2-h/g). Each edge belongs to
four plaquette boundaries, so sum_p Bp=4E. Jensen and h/g<2 imply

 M1>=a N, a=2hm(8-4h/g)^2.

At the native ratio, m=0.04987562112089027 and a=9.193074485002494.
This eliminates a possible vanishing first-moment density without assuming
independent features, a Gaussian state, or clustering.

## 3. A volume-independent upper bound on the third moment

Set A=i[K,E], which is Hermitian. Then

 M3=(1/2)<[A,[K,A]]>
   =(1/2)<[E,[K,[K,[K,E]]]]>.

Nested commutators of local operators involve connected local supports,
so their norm is at most a constant times N. A conservative hand bound is
M3<=1,990,656 h^2(g+h) N: each A_p has norm<=16h and a 4 by 4 support box;
[K,A_p] has norm<=1536h(g+h) and a 6 by 6 box; at most 81 other A_q boxes
intersect it. This bound alone suffices for strict nonvanishing density.

The replay also computes a sharper exact native integer-word bound. Let E0
be the two positive-direction edges anchored at the origin and
B0=(1/2)[E,[K,[K,[K,E0]]]]. Its translates sum to the M3 operator. Expand
in X^x Z^z words, using the exact multiplication sign (-1)^(z dot x').
The three inner commutators contain 8,76,524 nonzero words; the final density
contains 3336. The sum of absolute coefficients of B0 is exactly 9,003,008.
Every word is unitary, hence its norm is one even if its XZ convention has
an imaginary phase. Triangle inequality gives

 M3<=b N, b=9,003,008.

The support of this finite nested expression lies within a fixed box of
width at most ten, so R>=13 avoids identification across that support.
The integer calculation on R13 and R17 is the same local algebra, not a
floating eigensolver fit. It is a norm upper bound, not the actual M3 value.

## 4. Positive weight per unit area

Holder interpolation gives M1<=M0^(2/3) M3^(1/3). Consequently

 Var(E)/N=M0/N>=a^(3/2)/sqrt(b)>0.00928960.

For Omega=sqrt(2b/a), the first moment above Omega is at most M3/Omega^2,
so M1((0,Omega])>=aN/2. Thus

 mu_E((0,Omega])/N >= a/(2Omega)>0.00328437,
 Omega<1399.518.

These deliberately broad bounds do not locate a narrow line or a positive
lower spectral gap. Arbitrarily low frequencies are included. The original
uniform source obeys (O-<O>)g=-3(E-<E>)g, so its weight is nine times larger.
The response therefore cannot disappear merely because the transverse slab
area grows. This statement is about an integrated neutral response, not a
single quasiparticle residue.

## 5. Microscopic meaning and order of limits

The native microscopic energy scale is J lambda^4/128 and source weight
scale lambda^8/(128^2 V), V=4N. The coefficient result gives a strictly
positive normalized response density in the ordered limit: first lambda->0
at each fixed R, then R grows. For example the coefficient window upper
energy is below 10.934 J lambda^4, and its leading original normalized source weight is at least
[9a/(8*128^2*Omega)] lambda^8 > 4.510e-7 lambda^8, independent
of area in this ordered-limit sense. Smooth approximations to the
window, or fixed-R windows with endpoints outside the spectrum, implement
the previously proved microscopic transfer.

No uniform joint lambda,R error was proved. The window includes zero as a
limit point; it supplies no R-independent positive lower energy edge. A
thermodynamic sharp pole, three-dimensional propagation, scalar Lorentz
transformation, universal matter coupling, cosmological background and
source/detector identification remain unproved. The gain is narrower and
exact: the native slab's original neutral response has a nonvanishing area
density at the physical coefficient ratio, without an added interaction or
assumed clustering.
