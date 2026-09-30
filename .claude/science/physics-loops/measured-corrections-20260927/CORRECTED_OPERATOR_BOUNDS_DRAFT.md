# Fixed-case errors for the complete first-order operator

Extension of SPECTRAL_CERTIFICATES_DRAFT.md, still a supplied closed-square calculation. Instead of certifying floating expectation shifts, define the infinite approximate operator H0+xH1 by its closed quadratic form on D(n), for K,delta>0 and0<=x<1/4. Its diagonal is4K(1−2x)n²−4delta(1−2x), and its adjacent entry is t_n=−2delta(1−2x)+4Kx n(n+1).

On finite-support vectors the off-diagonal quadratic form is bounded above in absolute value by sum_n(|t_n|+|t_(n−1)|)|psi_n|². Since |n(n+1)|+|(n−1)n|=2n² for every integer n, this yields lower bound

 H0+xH1 >= 4K(1−4x)n²−8delta

in quadratic-form sense. There is also an upper bound by a constant times n²+I. For x<1/4 these bounds make the shifted form norm equivalent to the D(n) norm. Finite support is dense in that norm; completing it defines a closed semibounded form, whose associated self-adjoint operator has compact resolvent. This statement defines the form realization; it does not infer a global effective Hamiltonian equivalence to the microscopic model.

For the two tails |n|>=L+1 the same form bound is t_Lower=4K(1−4x)(L+1)²−8delta. Their coupling to the retained subspace has equal squared boundary magnitude t_L², because t_(-L−1)=t_L. The same positive-resolvent argument as the rotor certificate gives

 0<=Sigma(E)<= [t_L²/(t_Lower−E)] Pi_boundary

for E<t_Lower. Exact rational pivot counts of the two bounding finite matrices therefore certify infinite approximate-operator eigenvalue indices and intervals. The check fails on x>=1/4, nonpositive tail gap, zero pivots or differing sandwich counts.

At L30 this encloses seven approximate energies at width2e-9, for S20,50,120 and each of the two existing parameter ratios x=delta/[K S(S+1)]. Combining these intervals with the independently constructed finite-spin intervals bounds the actual errors in six low excitation gaps. The conservative maximum absolute gap-error upper bounds are:

| delta/K (K=1) | S20 | S50 | S120 |
|---|---:|---:|---:|
| 1 | .004987235265 | .000136754425 | .000004229203 |
| 31.607246 | 6.647658236470 | .281239142371 | .009192992163 |

Each decimal is rounded upward from the exact rational result in corrected_operator_error_bounds.json. These are certified finite-case discrepancies conditional on the exact operator reductions and certificate implementations. They are not an O(x²) bound for every S. They also do not enclose arbitrary measured-device error, calibration uncertainty, offset charge or resonator effects. No S was selected by fitting a measured higher transition.

Independent validation of this additional form/tail extension remains pending. It shares the tail-sandwich method with the rotor reference but has unbounded adjacent coefficients, so the coercive form argument is necessary and must not be skipped.
