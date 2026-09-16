# A macroscopic physical source costs only a vanishing fraction of self-energy

Personal derivation, 2026-09-15. This concerns individual component source
weights in the exact two-defect representation on Z^4. It supplies no
all-order connected response or physical state theorem by itself.

## 1. Source potentials on the infinite lattice

Let f be a smooth compactly supported real continuum two-form, and use
h_a(p)=a^2 f(a midpoint(p)), with 0<a<=1. Write

    u_e=G_1 D* h_a, u_m=G_3 B h_a,
    P=D G_1 D*, Q=B* G_3 B,

where G_r is the infinite cubic Hodge Green multiplier. The following
uniform estimates hold, with C_f depending only on fixed smooth norms of f:

    ||u_e||_infinity+||u_m||_infinity <= C_f a,
    ||nabla u_e||_infinity+||nabla u_m||_infinity <= C_f a^2.  (1.1)

The norms sum the finitely many cell orientations; nabla denotes forward
unit lattice differences. These are real field estimates, not a uniform
complex analyticity strip for arbitrary plaquette arguments.

Here is a Fourier proof with the infrared factor explicit. For k in the
Brillouin zone, the Laplacian symbol is
lambda(k)=4 sum_i sin^2(k_i/2), comparable to |k|^2. The multiplier of
G_1 D*, or G_3 B, has norm at most lambda(k)^(-1/2). Multiplication by
one lattice difference makes it bounded. Poisson summation for the
sampled smooth source gives hhat_a(k) as a^-2 times rapidly decaying
Fourier transforms fhat((k+2pi l)/a), with harmless cell-center phases.
For the central l=0 term,

    integral |k|^-1 a^-2 |fhat(k/a)| dk <= C_f a,
    integral a^-2 |fhat(k/a)| dk <= C_f a^2.

The singularity |k|^-1 is integrable in four dimensions. Noncentral alias
terms have |k+2pi l| bounded below by a constant times 1+|l|, except at
irrelevant boundary identifications where it is still bounded away from
zero for l!=0. Choosing a Schwartz decay order greater than 6 bounds their
summed contribution by O(a^4) in either integral. Fourier inversion proves
(1.1). No value is assigned to the single zero-frequency multiplier point.

## 2. Closure improves the small-component bound

For a finite conserved integer electric component j, let m=||j||_1.
Every oriented total sum vanishes:

    sum_x j_i(x)=0.                                    (2.1)

This follows by summing (D_0* j)(x) x_i=0 by parts; finite support makes
the operation legitimate. The component's diameter is at most m. For an
anchor x0, subtract u_e,i(x0) separately in each orientation and apply the
second estimate of (1.1) along unit paths. Together with the first estimate,

    |<j,u_e>| <= C_f min(a m, a^2 m^2).                (2.2)

Increasing C_f absorbs the four directions and fixed cell offsets. For a
finite closed magnetic three-form q, dualize to a finite conserved dual
one-current. The same total-sum and diameter argument gives

    |<q,u_m>| <= C_f min(a m, a^2 m^2), m=||q||_1.      (2.3)

In terms of any finite fillings D* S=j, B n=q, these are precisely the
physical source pairings

    <S,Ph_a>=<j,u_e>, <n,Qh_a>=<q,u_m>.

They are filling-independent. The a^2 m^2 term also follows from the local
area bound and ||Ph_a||_infinity+||Qh_a||_infinity=O(a^2), but that term
alone would grow quadratically in arbitrarily large component mass. The
am estimate is what keeps the complete component sum controlled.

## 3. Exact self-weight reserve for bounded complex physical sources

Let U_j=g<j,u_e>, V_q=b<q,u_m>, with g=N/sqrt(beta), b=2pi sqrt(beta).
The single component twists in the physical characteristic identity are
exp(-z U_j) for an electric sign and exp(-i z V_q) for a magnetic sign.
For |z|<=R, (2.2)-(2.3) imply the bounds

    |exp(-z U_j)| <= exp(C_f R g a m_j),
    |exp(-i z V_q)| <= exp(C_f R b a m_q).              (3.1)

Since E_e>=m_j/16 and E_m>=m_q/16, for the exact weights
w_e=exp(-g^2 E_e/2), w_m=exp(-b^2 E_m/2), we obtain

    w_e |exp(-z U_j)| <= w_e^(1-eta_e),
       eta_e=32 C_f R a/g,
    w_m |exp(-i z V_q)| <= w_m^(1-eta_m),
       eta_m=32 C_f R a/b.                            (3.2)

At fixed finite parameters and fixed R, both losses tend to zero as a->0.
For a<=min(g,b)/(64 C_f R), both are at most 1/2, so the source-modified
component weights are bounded by the half-self-weight measures already
used in the frame and sine-operator estimates. There is no extra
volume-dependent or root-area exponential factor. The R=0 case is trivial.

For every integer k>=2, the anchored-frame inequality additionally gives

    integral |g<S,Ph_a>|^k nu_e(dS)
         <= g^k M_e(k) ||Ph_a||_k^k,
    integral |b<n,Qh_a>|^k nu_m(dn)
         <= b^k M_m(k) ||Qh_a||_k^k.                  (3.3)

These are the existing finite anchored moments. The l2 projection bound
and the bounded-symbol Fourier estimate ||Ph_a||_infinity+||Qh_a||_infinity
=O(a^2) give ||Ph_a||_k^k+||Qh_a||_k^k=O(a^(2k-4)) by interpolation.
In particular third and fourth source moments are O(a^2)
and O(a^4). Formula (3.2) permits the same conclusion with a bounded
complex z twist, using half-self-weight moments.

## 4. Boundaries and the unresolved connected estimate

This proof is on the infinite lattice. A finite free box may have magnetic
components meeting its boundary whose dual current is relative rather
than a finite conserved current on Z^4. Its oriented total can then be
nonzero. One must first pass to the matched infinite-volume objects or
prove an appropriate boundary estimate; (2.3) is not a uniform theorem
for those finite relative components. The selected-state and limit-order
obligations are unchanged.

The small component moments in (3.3) are not the third/fourth cumulants
under the interacting defect law. To use them for Gaussianity, one still
needs a uniform bound connecting its connected source derivatives to
these anchored marks. Neither a growing source disk nor a finite-order
coefficient calculation supplies that bound. In particular, a naive
volume times Cauchy estimate with radius O(a^-1) does not make a fourth
derivative vanish in four dimensions. The closure-improved marks must
survive the actual connected expansion.

This gives a source-specific reserve to combine with the signed sine
operator estimate. It removes one unnecessary all-microscopic-source
requirement without weakening the desired physical observable.
