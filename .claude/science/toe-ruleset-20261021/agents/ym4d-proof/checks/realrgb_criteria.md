# REALRGB preregistered checks

Written before the check implementation and its first execution. These are
exact finite algebra/geometry regressions, not numerical Yang–Mills evidence.
The mathematical results require the written proofs and independent review.

1. For derivative orders 0–4, the partition formula for derivatives of an
   exponential with every positive-order log-derivative bounded by B must
   equal the complete Bell polynomials
   `1; B; B+B^2; B+3B^2+B^3; B+7B^2+6B^3+B^4` exactly.
2. Reciprocal derivative majorants computed by differentiating `D*(1/D)=1`
   must equal the partition formula with coefficient `number_of_blocks!`:
   `1; B; B+3B^2; B+9B^2+13B^3; B+21B^2+78B^3+75B^4`.
3. Leibniz convolution of the two preceding families must give quotient
   majorants
   `1; 2B; 2B+6B^2; 2B+18B^2+26B^3;
   2B+42B^2+156B^3+150B^4`.
   Their fourth Taylor sum at jet weight 1 and B=1 must be `117/4` exactly.
4. Logarithmic derivative majorants from the moment/partition formula must
   be `B; B+2B^2; B+6B^2+6B^3; B+14B^2+36B^3+26B^4`.
5. On the four-dimensional block torus of side 7, the hole
   `{-1,0,1}^4` must have 81 vertices, its closed face-neighbourhood 297,
   and saturation of the adjacent singleton `(2,0,0,0)` 82 vertices.
6. All source-input hashes must agree before and after the run. The initial
   manifest is an identity record, not evidence for a mathematical claim.

Acceptance requires exact equality for every executed check; no tolerances,
fitted constants, or post-hoc threshold changes. A failed assertion is a
failed check. A resource refusal is reported separately, never as a pass.

Execution must hold the exclusive `checks/realrgb_check.lock`, run under
`nice -n 10`, use Python `-B`, and set BLAS/OpenMP/Accelerate/NumExpr thread
variables to 1. No pools. At startup and between checks: all reported load
averages below 8, system free memory at least 30%, RSS below 1,000,000,000
bytes using `resource.getrusage` (macOS bytes), and observed niceness at
least 10. Do not use RLIMIT_AS. If any guard or nice fails, report it and
do not weaken it. No physical simulation or parameter sweep is planned.
