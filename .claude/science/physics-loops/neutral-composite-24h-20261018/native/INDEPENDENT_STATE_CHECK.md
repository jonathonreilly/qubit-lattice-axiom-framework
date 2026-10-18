# Independent product and dimer state check

The stated energy and composite expectations check. All statements concern the supplied native compass Hamiltonian, not a derived cosmological state.

## Uniform products
For a pure uniform product with Bloch vector n, |n|=1, H=K sum_(x,a) sigma_x^a sigma_(x+ea)^a has expectation NK. On a simple periodic cubic lattice with lengths at least three,

Var(H)/(NK^2)=1+sum_a n_a^4.

An independent connected-pair count gives: individual bond variances 3−sum n_a^4; same-axis overlapping unordered bond pairs, including their factor two, 2(1−sum n_a^4); different-axis overlapping pairs −8 sum_(a<b) n_a^2 n_b^2=−4(1−sum n_a^4). Their sum is the expression above. Disjoint bonds have zero covariance. This lies between 4/3 and 2. For K nonzero the finite-volume pure state is not an energy eigenstate, hence its density matrix is nonstationary. This variance statement by itself is not a proof about an infinite-volume state's local dynamics. Length-two duplicate-bond conventions require separate counting.

## Dimer trial
For psi=cos(theta)|00>+sin(theta)|11>, let s=sin(2theta), m=cos(2theta). Its one-site Bloch vector is (0,0,m), while intra-dimer XX=s, YY=−s, ZZ=1. Tile disjoint nearest x bonds, with even x length. There are N/2 intra-x bonds. All other x and all y Hamiltonian bond means vanish; every z bond joins different dimers and has expectation m^2. Therefore for K=−J<0,

E/N=−J[1−s^2+s/2] >= −17J/16,

with equality within this trial family at s=1/4. This is the minimum of the family, and provides an upper bound on the actual ground energy, not a lower bound on it.

For C=sum_(x,a) sigma_(x−ea)^a sigma_(x+ea)^a, x-distance-two endpoints never belong to one adjacent x dimer when even Lx>=4. Thus the x and y contributions have zero mean, and the z contribution is m^2 per site. For other lengths at least three, C/N=15/16 at the optimum. Lx=4 can repeat operator words in C without changing this expectation; coincident endpoints at length two are excluded. Direct four-dimensional matrix multiplication independently verified XX=1/4, YY=−1/4, ZZ=1, ZI=sqrt(15)/4.

## Stronger separability result
Every site-factorized state, even with nonuniform mixed one-site Bloch vectors n_x, obeys

sum_(x,a) n_x^a n_(x+ea)^a <= sum_x |n_x|^2 <= N,

by uv <= (u^2+v^2)/2 and periodic bond counting. Thus E>=−JN for every product state. Convexity extends this bound to every fully site-separable density matrix. The dimer trial's energy −17JN/16 is therefore an exact energy entanglement witness: the finite-volume ground state cannot be fully site-separable. This is stronger than comparison only against aligned products.

## Independent variance cross-check
The separate implementation `/private/tmp/native-product-variance-check.py` uses explicit 4x4 dimer matrices, not the root Pauli-word implementation. It multiplies each pair of Hamiltonian bond operators locally in each dimer and sums their connected expectations; bond pairs with disjoint dimer supports vanish exactly by product factorization. At s=1/4 it gives

- L=4: Var(H)/(NK^2)=1.6015625=205/128;
- L=6: Var(H)/(NK^2)=1.5703125=201/128.

These are independent floating-point confirmations of the proposed exact rational values, not a separate rational-arithmetic certificate. The L4 wrap correction is real and should not be discarded. The nonzero variance establishes that the optimized trial is not stationary on these volumes. An infinite-lattice coefficient requires the local support/count argument or a sufficiently large wrap-free calculation, not simply assuming finite-size convergence.

## Physical scope and next step
The trial breaks one-step x translation, cubic rotation, and (with the usual axial-spin representation) time reversal because m is nonzero. Symmetry averaging preserves its energy and scalar C mean, and still violates the separable energy bound, but does not make the state stationary. Energy dephasing preserves energy but need not preserve C=15/16 per site.

The firm next step is to exploit the separability bound as a benchmark for entangled variational states or prepared-state dynamics. It removes fully separable states as ground-state candidates in this ferromagnetic branch. It does not establish the dimer state as the ground state, a preparation/selection mechanism, a scalar pole, or a coupling to a cosmological scalar.
