# CHARGE numerical criteria (registered before any numerical experiment)

Optional finite checks, if resource guards permit:

1. For N=2,3 and even torus sides, evaluate the Wilson action along the
   explicit single-link SU(2) perturbation of RENEW's g-flux field. Agreement
   with the analytic six-plaquette formula must be within 1e-10 at each
   registered angle 0, 0.01, -0.01. The action difference is expected to be
   positive; this checks the claimed positive local mode, not full stability.
2. For N=2,3 and the periodic deformation
   U_1(x)=exp(i(pi*x_2+eta*(-1)^x_2)H), H=diag(1,-1,0,...),
   U_2=U_3=U_4=I, every 12 plaquette action must agree within 1e-10 with
   2(1+cos(2eta))/N at eta=0,0.01,-0.01. Total action decreases at
   nonzero eta. This tests the coherent negative mode, not a Gaussian
   determinant or an all-cut estimate.
3. Finite geometric sums of descendant volumes for L=3,5 and depths
   1,2,4 must agree with (1-L^(-4*(R+1)))/(1-L^(-4)) within 1e-12.
   This is an arithmetic check only, not a matched-reference theorem.

Execution requires the established numerical lock, effective nice priority,
all BLAS/OMP thread counts one, peak RSS below 1 GB, load below 8 and at
least 30% memory free. No pools and no RLIMIT_AS. Failure of any guard means
no numerical experiment runs; report the failure. No post-hoc probe may be
reported as preregistered. Written mathematics and deterministic source
bookkeeping do not depend on these optional computations.
