# Arbitrary coherent backgrounds within one protected polarity

Separate extension under PROTECTED_POLARITY_CONTRACT.md. The fixed-background proof remains unchanged. This removes its global A+ and single-background restrictions, but keeps ONE fixed polarity and explicit local support conditions. It is an eigenvector exclusion, not a concentration theorem about the actual source.

## 1. Class and completed background

Fix sigma=+1 or -1 on a safe even torus L>=8. A physical W=1 basis word with hole h belongs to P_sigma when:

    every occupied A at graph distance <=2 from h has charge sigma;
    every B at graph distance <=3 from h is occupied;
    every immediate B neighbor of h has charge sigma.       (1)

All far charges and B masks are arbitrary. At fixed physical odd NB=k, summing Gauss fixes total charge n. Since n is even and k is odd, k<=n-1, so every such word has a B vacancy somewhere. Complete the hole with sigma and call the resulting full A charge pattern alpha; call the B charge/vacancy pattern chi. Then

    sum alpha + sum chi = n+sigma.                        (2)

Let A_sigma(alpha)={a:alpha_a=sigma}. For a fixed pair (alpha,chi), the actual one-hole words lie at those positions in A_sigma(alpha), since removing sigma restores the physical charge in (2). Embed C^(A_sigma(alpha)) into the corresponding physical fiber by I_(alpha,chi), and extend its coordinate vectors by zero to all of C^A. Let F_(alpha,chi) be the subset obeying (1).

At fixed sigma, different completed pairs have orthogonal physical input sectors. More importantly they also have orthogonal OUTGOING sectors below: from an output with hole a, completion by the same fixed sigma reconstructs a unique alpha, and its literal B pattern reconstructs chi.

## 2. Full columns, including the zero extension

Use the same actual connection A_e and geometric K_(sigma A), with edge entries exp(i sigma A_ab). The canceled original H2 gives, on the declared supported columns,

    H I_(alpha,chi) P_F
       = I_(alpha,chi) P_(A_sigma) T_(sigma A) P_F,
    T_(sigma A)=K_(sigma A)* K_(sigma A).                 (3)

Indeed every negative same-hole first hop is blocked by the full distance-three B neighborhood. A return fills the hole from sigma and returns to the unique newly emptied B site, yielding diagonal six. Every shared-B hole move fills h with sigma and empties an A_a of charge sigma, because a is at distance two. It restores the same B charge and preserves the completed alpha. Its actual phase is exp(i sigma A_hb-i sigma A_ab). More distant rows cancel in the original block identity. Thus no additional charge or background output is omitted in (3).

The geometric matrix T has range two in A-to-A graph distance. If a is not in A_sigma(alpha), it is neither a protected h nor at distance two from one, by (1). Hence

    (1-P_(A_sigma)) T_(sigma A) P_F =0.                   (4)

Equation (4) is why the auxiliary zero extension supplies no unproved boundary condition. It is an exact geometric zero, not a replacement of a physical charge row by a forbidden state.

## 3. Coherent direct sums and the common actual phase set

Let psi be an actual H(theta) eigenvector supported entirely in P_sigma. Decompose it by the completed backgrounds, psi=sum_(alpha,chi) I_(alpha,chi)u_(alpha,chi), each u=P_Fu. At fixed finite graph this is a finite orthogonal sum. Equations (3) and the outgoing uniqueness in section 1 show that the eigen equation separates in each completed background. Equation (4) upgrades each separated equation to the full geometric one

    T_(sigma theta) u_(alpha,chi)=lambda u_(alpha,chi)     (5)

on C^A, including its identically zero coordinates outside A_sigma(alpha).

For completeness the fixed-background proof supplies a common full-measure phase set. For each a in A define O_a(theta) with rows e_a* T_theta^r, r=0,...,n-1. At the physical flat connection phi, the eigenvalues are [2 sum_i cos(k_i-phi_i)]^2, distinct generically modulo the simultaneous pi shift. Every Fourier eigenvector has nonzero value at EVERY a. Thus the SAME flat point makes every det O_a nonzero by its Vandermonde formula. The Laurent polynomial product over all a is nonzero; its zero set has Haar measure zero. Replacing theta by sigma theta preserves Haar measure and nonzeroness. No independent configuration-edge parameters are used.

Choose a vacancy v of chi and one adjacent A vertex a_0. It is outside F, so u(a_0)=0 whether or not a_0 belongs to A_sigma(alpha). Equation (5) makes every row of O_(a_0)(sigma theta) vanish on u. On the common full-measure set it is invertible. Therefore every u_(alpha,chi)=0.

Consequently, for each fixed polarity sigma and almost every physical cycle phase, no nonzero actual H2 eigenvector is entirely supported in P_sigma. The statement allows arbitrary coherent sums over the far A charges and B charge/occupancy masks that obey (1). By finite-fiber self-adjointness it also excludes an invariant subspace contained wholly in that support class. It gives no rate or size-independent lower bound.

## 4. Remaining mixed columns

The fixed polarity in section 1 is load-bearing. If sigma varies, the same actual outgoing word with a hole at a has two different possible completions alpha_a=+ and alpha_a=-. Opposite-polarity input sectors can therefore feed the SAME mixed-star outgoing charge/field row. Their amplitudes are not orthogonal merely because their protected input supports were orthogonal. Moreover T_(-theta) is the complex conjugate of T_theta on physical phases, so their spectra agree; at flat phase k->-k gives the same equality. Independent spectral nondegeneracy within each polarity cannot separate those signs.

This proof does not exclude an eigenvector combining both polarities, nor one with a nonmonochromatic local A cone or an empty B site in the distance-three shell. Such columns can also feed the outgoing rows of protected inputs. It does not bound a protected initial vector's projection onto an extended invariant dark module. Actual source-history image density, full Laurent observability, long-age absorption, finite-spin transfer and continuously forced microscopic residence remain open.
