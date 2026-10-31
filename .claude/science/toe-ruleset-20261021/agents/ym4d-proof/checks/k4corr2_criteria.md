# K4CORR2 numerical registration

Registered before the checker is created or run. Written proofs do not need
pre-registration under PROCESS_LIGHT. Exact integers and rational arithmetic
are the only permitted arithmetic for scientific acceptance decisions.

1. Enumerate labelled Wick pairings for the five degree lists for n=2,4:
   (4,2,...,2), (3,3,2,...,2), (3,2,...,2,3), (2,...,2,4),
   (2,...,2,3,3). Count connected pairings, both permitting and excluding
   contractions within a vertex. Compare against an independent
   partition/Mobius calculation of connected counts. All comparisons must
   agree exactly. Ghost pairings are a subset of these bosonic majorants;
   do not label the counts actual YM tensor amplitudes.
2. The external-only counts without self-contractions must be 0 and 6
   for n=2, and 288 and 360 for n=4. The quartic bulk star with one
   leg to each of four distinct external vertices must have 1152 pairings.
   Degree and derivative counting must give UV powers 4n,4n,4n+4,
   4n+4,4n+8 for the five bare families.
3. Verify the rational vertex-majorant ledger and its substitution into
   the external-only and bulk-star bounds. Verify the simplified expressions
   for the partial coefficient bounds as polynomial identities in N and d,
   not floating evaluations at selected N. They must not be presented as
   bounds for omitted diagrams or the renormalized full coefficient.
4. Verify the heat-regulator free-limit majorants for every
   0<delta<=2^-20 using endpoint inequalities and positive monomials.
   The resulting free two- and four-point coefficients must be at least
   half their respective CUMUL lower bounds. Check the conversion of
   absolute diagram bounds into a finite-regulator ratio bound exactly.
5. Verify Taylor-remainder rational factors for singularity degrees
   0,1,2 and the star-integral constant. These are local estimates, not
   a completed forest estimate.
6. Independently form the order-x expansion of P/Q^2, x=h^2, and check
   c=a4-2a2. Verify the positivity margins for |c|x<1/2 and a uniform
   remaining ratio error at most 1/4, and the separate two-point margin.
   Verify the conditional FLOW reciprocal estimate as a polynomial
   inequality on its entire declared domain. A finite-regulator bound
   growing as delta decreases does not pass the uniform YM target.
7. Mutation controls must detect omission of the repeated-cubic 1/2,
   use of disconnected pairings as connected, replacement of the ratio
   coefficient by a4-a2, and treating the bare cutoff majorant as uniform.
8. Scientific completion criteria are separate from algebra checks:
   all counterterms, internal collision regions, volume removal and
   original-operator matching must be bounded before declaring a finite
   uniform Cbar or a positive YM coupling window. Missing estimates are
   OPEN / not passed, even if every algebra assertion passes.

Resource requirements: one serial numerical child, no pools; nice >=10;
OPENBLAS_NUM_THREADS, OMP_NUM_THREADS, MKL_NUM_THREADS,
VECLIB_MAXIMUM_THREADS and NUMEXPR_NUM_THREADS all 1; native memory free
percentage >=30; all three load averages <8; monitored combined RSS
<800 MiB, strictly below 1 GB; no RLIMIT_AS or other virtual-memory cap.
Hold a new k4corr2 numerical lock plus the existing k4corr, k4match,
cumul and combo numerical locks opened read-only. Check resources before,
during and after execution. A guard failure is recorded as a failed run;
do not weaken a guard to obtain a pass. Preserve every attempted run.
