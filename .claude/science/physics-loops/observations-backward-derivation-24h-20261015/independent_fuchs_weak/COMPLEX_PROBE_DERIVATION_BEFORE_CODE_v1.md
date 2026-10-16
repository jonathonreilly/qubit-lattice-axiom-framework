# Independent complex-probe supplement, frozen before implementation access

This is a focused mathematical extension of the already frozen first-pass
check. I read only the v2 source note, complex-probe note and complex-probe
plan before writing this proof. No author runner, control output, development
output, raw acquisition receipt or raw trace has been opened. The separate
snapshot binds the exact source bytes. This is not empirical validation or a
formal audit status.

## Source delta

The v1 to v2 delta has exactly the two qualified prose replacements: equation
(4) now specifies f=0, and full real column rank gives uniqueness conditional
on consistency, or unique least squares. No displayed equation changed.
Both qualifications resolve the issues recorded before the first-pass code.

## Independent derivative and adjoint derivation

Let tau=t-t0, let kappa be a real constant within the window, and put
g=exp(-i kappa tau). Since g'=-i kappa g and g''=-kappa^2 g,

    (p g)' = (p' - i kappa p) g,
    (p g)'' = (p'' - 2 i kappa p' - kappa^2 p) g.

If p=p'=0 at the endpoints, the complex window w=p g has w=w'=0 there.
The elementary product identities

    (w z)' = w' z + w z',
    (w z' - w' z)' = w z'' - w'' z

use no conjugation and remain valid for complex functions. Hence the original
bilinear moments and the equation R=a B+i nu C+b U hold without modification.
The original proof is over the complex numbers; it did not require w real.
A sesquilinear convention also works if all three weights w,w',w'' are
conjugated consistently. Mixing conjugated C,U with unconjugated D,E does
not implement either convention. Reversing kappa everywhere merely chooses
a different valid probe; a sign-error control must instead use derivatives
that do not differentiate the chosen w.

This rule uses the source phase only to select a numerical constant kappa.
The plan declares one affine least-squares slope over all recorded times,
and both this constant slope and zero are used within every window. No
derivative of that constant is needed. A time-varying modulation phase psi
would add -i psi'' p to the second derivative; replacing kappa by kappa(t)
in the displayed constant formula would not generally be valid.

For u=exp(i sigma t), choosing kappa=sigma gives

    integral w u = exp(i sigma t0) integral p.

With unit-integral p this has unit magnitude. This proves the limited
"can prevent cancellation" claim for a stipulated monochromatic input.
It does not promise improved rank or conditioning on arbitrary data, and
it does not make photodiode phase a measured physical force phase.

## Rank limit survives arbitrary complex probes

If z=A u and u'=i sigma u, integration by parts still gives
D=-i sigma C and E=-sigma^2 C, even for complex w. Therefore every complex
row equals U times the fixed row

    ((1+sigma/Omega) A, i A, 1, i).

Real and imaginary parts of any number of those rows span at most two
dimensions over the reals. With any nonzero U, columns U and i U make that
rank exactly two. Adding zero and matched-slope probes cannot distinguish
all four real coefficients in this limiting case. Reusing observations in
several probes also creates correlated summaries; a data-selected phase
slope adds dependence on input noise. The source preserves these limits.

## Frozen decisive fixtures and controls

The supplement will use only synthetic functions, with no author code import:

1. Symbolically differentiate p exp(-i kappa tau), verify endpoints and the
   missing term for a varying modulation phase.
2. Use the first-pass polynomial fixture: Omega=5, gamma=2, omega0^2=49,
   b=(3+2i)/7, z=1+2i+(2-i)t+(1+3i)t^2+(2+i)t^3/5, and compute u from the
   differential equation. Integrate at 64-point Gauss-Legendre nodes on
   [j,j+1], j=0,1,2,3, with p=140 tau^3(1-tau)^3 and kappa=0,2,-3/2.
   Check the bilinear weak residual, rank-four recovery, and a consistently
   conjugated convention. Keep the full physical homogeneous addition
   (2+i) exp(lambda+ t)+(-1+2i) exp(lambda- t), with
   lambda+-=-1-5i+-4 sqrt(3)i; do not fit or subtract it.
3. At nonzero kappa, deliberately omit the modulation derivative terms,
   reverse only their linear-in-kappa signs, and mix conjugation conventions.
   Each must produce a measurable residual on at least one stipulated
   manufactured window. These are synthetic negative controls, not edits
   of root sources.
4. Use u=exp(2it), z=(2+i)u with arbitrary complex probes. Check D and E,
   exact row-factor rank two, numerical singular values, and matched-probe
   U=exp(2i t0). Compare with unmodulated cancellation at sigma=40 on [0,1].

Numerical checks will use absolute tolerance 1e-10 plus relative tolerance
2e-10; negative controls will require residual greater than 1e-5. All owned
calculations have a 120-second limit and complete preserved stdout/stderr.
No author implementation or output will be read before these independent
supplement outputs are frozen.
