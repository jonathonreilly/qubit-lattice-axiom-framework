# Active-energy continuation: registered arithmetic check

Source: 25a86977f538eb6bb104f097c435b44fd42138b7.
Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01.
Written before executing the check. No numerical run has yet occurred.

Scope: the exact quadratic scalar reduction of the one-step SU(2)
problem at the identity, not a nonlinear SU(2) simulation. The analytic
candidate is the missing local/global tail in the literal (Resp).
This does not test or refute AE-R, Lemma J with an additive tail,
or any uniform frozen-data estimate.

For L=3,5,7 with M=12 parent blocks, and L=5 with M=16, put a single
nonzero block mean at j=M/2 on a periodic chain of ML fine sites.
Minimize sum_n (h[n+1]-h[n])^2/2 with the M prescribed block means.
Use exact rational arithmetic and two separate systems:

1. Fine-site Laplacian plus block-mean KKT equations.
2. Derived interface-slope system
   b p[j-1]+a p[j]+b p[j+1]=mu[j]-mu[j-1], where
   b=(L^2-1)/(6L) and a=L-2b.

Required equalities: all fine KKT equations and all block means;
agreement of every fine slope with the linear interpolation of p;
agreement of the energy computed from h and from those slopes.
All comparisons are exact equality of fractions, with no tolerance.

Candidate discriminator: p[0] is exactly nonzero, and every interface
slope is nonzero, even though block means on the local patch
j=-2,-1,0,1,2 vanish. The free-edge minimizer on that patch is zero:
zero is feasible and the nonnegative quadratic energy vanishes there.
If any required equality or nonzero condition fails, report it as a
failure of this check and investigate, preserving the first output.

Controls: for L=3,M=12 solve all-zero means and all-one means; h must
be identically 0 or 1, respectively, and all slopes must vanish.

These small rings do not realize the full brick/r_lift geometry. The
analytic formula must cover arbitrary even M, allowing a compatible
torus and a source beyond the actual finite patch. The passage from
the quadratic minimizer to a nonlinear SU(2) lift is a separate
analytic argument; this runner provides no evidence for that passage.

Run only after successful numeric-lock acquire, with nice, one BLAS
thread, and a 2 GiB process memory limit plus RSS self-checks. Stdlib
only; no process pool. Save preflight, acquire, run and release output.
