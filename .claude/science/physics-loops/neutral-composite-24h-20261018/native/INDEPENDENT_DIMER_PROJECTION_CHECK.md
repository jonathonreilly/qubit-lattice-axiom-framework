# Independent even-dimer projection and leakage check

Let P be the tensor product of the even-parity subspaces span{|00>,|11>} of disjoint nearest x dimers. In this basis intra-dimer XX becomes tau_x and either physical Z becomes tau_z. Therefore for K=−J,

PHP = −J sum_d tau_x(d) −2J sum_d tau_z(d)tau_z(d+ez).

The two parallel physical z bonds produce the factor two. Every inter-dimer x bond and every y bond flips parity in each of two dimers, so has zero PHP matrix element. This is an exact compression, not an invariant-sector Hamiltonian: QHP is nonzero.

## Analytic leakage count
For the product dimer trial with s=sin(2theta), all even dimers have XX=s, YY=−s and unit norm. Leakage bond images with distinct pairs of odd dimers are mutually orthogonal.

For Lx>=6 and other lengths avoiding repeated-neighbor dimers:

* Inter-dimer x bonds: N/2 distinct parity-pair sectors, each image norm squared one, contribution N/2.
* y bonds: two parallel physical bonds connect each neighboring pair of dimers. Their overlap is the product of intra-dimer YY expectations, s^2. There are N/2 such dimer pairs, each with combined squared norm 2+2s^2, contribution N(1+s^2).
* x and y images occupy different odd-dimer pairs and have zero overlap. z and intra-x bonds stay in P.

Consequently ||QHP psi||^2/N = J^2(3/2+s^2). At s=1/4 this is 25J^2/16, independently of the logical projected calculation.

On Lx=4, the two inter-dimer x bonds can connect the same pair of logical dimers across the periodic seam. Their overlap is s^2, adding Ns^2/2 to the squared leakage. Thus at the optimum the L4 leakage is 51J^2/32. This explains the finite-size discrepancy without a convergence assumption.

## Projected variance
Write m^2=1−s^2 and h=−J(sum X+2sum ZZ) on N/2 logical sites. The connected-pair count per logical site gives

Var(h)/(J^2 N/2) = (1−s^2) +4(1−m^4)+8(m^2−m^4)−8s m^2.

The terms are single-X variance, individual ZZ variance, adjacent-ZZ covariance, and X/ZZ symmetrized covariance. At s=1/4 this equals 1/64, so Var(PHP)/N=J^2/128.

Because psi lies in P, the exact orthogonal decomposition is

Var(H)=Var(PHP)+||QHP psi||^2.

The resulting bulk total is 201NJ^2/128. L4 is 205NJ^2/128.

Independent script `/private/tmp/native-projection-check.py` computes the projected-chain covariance directly using 2x2 logical matrices and compares the separate physical 4x4-dimer calculation. It obtains projected variance 0.0078125 per site on L4 and L6, leakage 1.59375 on L4 and 1.5625 on L6, matching these exact counts to floating precision.

## Interpretation
The projected chain spectrum is a useful variational/compression object. It is not the native Hamiltonian's excitation spectrum: the chosen subspace is not invariant and leakage is not perturbatively small in the supplied model. At the optimized trial, leakage is 200 times the projected variance and accounts for 200/201 of total bulk variance. Both terms scale with J^2, so taking a smaller overall J does not improve their relative separation. An added parity penalty or other new scale would change the model and must be declared rather than silently used to justify projected modes. None of this excludes native collective excitations; it excludes identifying them directly with this unprotected projected-chain spectrum.
