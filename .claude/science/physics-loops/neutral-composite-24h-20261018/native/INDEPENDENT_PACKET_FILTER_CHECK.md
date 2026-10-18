# Sine packet, normal-form mode weight and finite-time filter

The proposed concentration exponent and conditional normal-form mode-weight coefficient check. The spectral and dynamical conclusions require the uniform source/fiber assumptions explicitly stated below. No repository files were changed.

## Exact Fourier concentration

Remove the alternating phase from f_j and let a_j=sqrt(2/(M+1)) sin(pi j/(M+1)) on1<=j<=M, zero outside. Its norm is one. It is the lowest Dirichlet eigenvector of the nearest-neighbor discrete Laplacian, so Parseval gives

integral 4sin²((q-pi)/2)|fhat(q)|² dq/(2pi)
= sum_j |a_(j+1)-a_j|²
=4sin²(pi/[2(M+1)]).

This includes both endpoint differences to the zero exterior. On the complement of |q-pi|<=lambda eta (distance understood modulo2pi), the integrand multiplier is at least4sin²(lambda eta/2). Thus the exact concentration bound is the ratio of these two sine-squared quantities. For M of order lambda^-3/2 and eta=lambda^1/8 it is O(lambda^(3/4)). The same argument works for discrete ring momenta if the zero-extended packet fits without an unintended boundary overlap.

## Mode weight

In the main window |kappa|=|pi-q|/lambda<=eta, assume a uniform normal-form fiber construction, persistence of the isolated upper eigenprojection, and uniform convergence of the dressed source to -2lambda E1. Then its mode residue tends uniformly to15/16 and the packet's contribution from that window is

(15/4+o(1))lambda²,

since the packet mass there tends to one. This establishes a lower contribution. For equality for the entire selected mode/filter, also bound the spectral contribution outside that window: a uniform O(lambda²) total source weight per momentum makes it at most O(lambda²)*O(lambda^(3/4)), hence negligible. An O(1) bound alone would yield O(lambda^(3/4)), too large. Higher-band/source-dressing contributions must likewise be shown negligible in the selected frequency window.

The needed source estimate concerns its action on the chosen normal-form vacuum, not merely its operator norm. An l2-normalized packet does not automatically have a volume-independent operator norm. The previously derived coefficient and few-wall energy bounds do not by themselves prove this source estimate; it needs the corresponding translation-covariant dressed-source calculation or a direct norm bound.

Choose a smooth compactly supported scaled frequency cutoff chi((omega-8)/lambda²) equal to one near9/16 and with support separated from the other upper eigenvalue and host continuum at kappa0. Uniform fiber separation then keeps it valid across the shrinking main window. This is a filtered mode signal, not an exact delta-function assertion. Finite rings need sufficiently fine momentum spacing, packet size and spectral approximation consistent with the simultaneous limit.

## Time-domain comparison

With Fourier conventions absorbed into a fixed constant, the time kernel is

K_lambda(t)=lambda² exp(±i8t) chihat(lambda² t).

Since chi is smooth and compactly supported, chihat is Schwartz. If the fixed-packet dynamical comparison holds for all real t as

|C_exact(t)-C_D(t)|<=C M lambda^(n+1)(1+|t|)²,

then direct integration gives

|filtered_exact-filtered_D|
 <=C' M lambda^(n-3),

using the finite zeroth and second moments of |chihat|. At n=7 and M~lambda^-3/2 this is O(lambda^(5/2))=o(lambda²). No sharp time cutoff is needed for this mathematical bound; a polynomial bound may be loose at enormous t but remains integrable against the rescaled Schwartz kernel.

For an explicitly finite-duration experiment/filter, truncate at |t|<=T(lambda)lambda^-2. If the normal-form source has total spectral weight O(lambda²), its discarded correlation tail is bounded by O(lambda²) times the integral of |chihat(s)| over |s|>T. Hence any T→infinity gives relative tail error tending to zero. The exact-minus-normal-form tail can be controlled by the preceding polynomial comparison and Schwartz second moment. A slowly increasing T, such as a logarithm, is compatible with the finite-window worst-case estimate lambda^(1/2) T²→0 after division by signal lambda².

However, Schwartz decay plus only a bare O(M) correlation bound does NOT justify an arbitrary slowly growing T: O(M) times a logarithmically small Fourier tail need not be o(lambda²). Either use the source-sensitive normal-form estimate together with the dynamical comparison as above, or choose and quantify a sufficiently large T with stronger decay information. Fixed T generally leaves a small fixed relative leakage and does not prove the exact15/4 asymptotic coefficient unless the full kernel is retained.

## Prepared-state distinction

The chosen vacuum is stationary for D, so its normal-form correlation has a positive spectral measure. Its dressed image need not be stationary for exact H. The exact-H object controlled here is consequently a filtered correlator of an explicitly prepared state; it must not automatically be called a positive stationary spectral weight or an exact equilibrium pole. The comparison can show that this finite-time signal is close to the positive normal-form prediction without making either stronger claim.
