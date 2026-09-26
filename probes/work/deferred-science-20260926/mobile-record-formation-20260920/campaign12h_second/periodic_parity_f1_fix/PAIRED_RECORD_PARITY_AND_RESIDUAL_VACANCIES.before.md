# Direction-count parity and a macroscopic Gauss bound

2026-09-21, root derivation. Conditional identities for the supplied reciprocal
six-direction matching model on an even periodic N^3 torus, N>=4. This is
neither an axiomatic conclusion nor a microscopic or macroscopic wave result.
The formation process's density scaling remains an empirical/proof obligation.

## A rate-independent finite-volume constraint

Let M_i be the number of dimers parallel to coordinate i, equivalently the
number of records with content +e_i. Let V_0 be the set of vacant sites.
For each coordinate the following congruence is exact:

    M_i = sum_{x in V_0} (x_i mod 2)   (mod 2).                (1)

To prove it, sum x_i mod 2 over all occupied vertices modulo two. An i-dimer
contributes one; another-axis dimer contributes zero. The sum over all sites
is N^3/2, an even integer, so the occupied sum equals the vacant sum modulo
two. Periodic edges also connect opposite coordinate parities because N is
even. No rate, ergodicity, locality or equilibrium hypothesis enters.

In particular, every full matching has all three M_i even. If there are
exactly two vacancies and all three M_i are odd, the two vacant sites have
opposite parity in every coordinate. They cannot be nearest neighbors.
Any conservative record rearrangement preserving the six immutable contents
also preserves M_i, so this remains true after every such rearrangement,
including nonlocal ones. Paired births require adjacent vacancies. Thus this
sector can never form the last pair while retaining this encoding, matching
relation and birth event. This is a statement about this specific supplied
class, not a prohibition on changing the encoding, adding other birth rules,
or obtaining an asymptotically source-free field.

The sector exists on every even N>=4. Start from the fully x-columnar matching,
with edges joining x-even sites to their x+1 neighbors. In the cube {0,1}^3
remove its four x dimers and insert the three-edge hexagon pattern
100--110, 010--011, 001--101. The result has two vacancies 000,111 and counts

    (M_x,M_y,M_z)=(N^3/2-3,1,1),

all odd. This is a specification of a matching, not an allowed conversion
of already formed columnar records: that conversion would change contents.
The specified matching is reachable from empty by forming precisely its
edges, with positive finite-volume probability under the positive birth
rates. Conservative motion may continue forever, but no final birth occurs.
No lower bound uniform in N on that history's probability is asserted.

This parity obstruction is distinct from a local-support jam. In the pilot,
N4_jam_extended_s21092102 ended with counts (12,10,9), two vacancies, and no
enabled event. Those parities are (0,0,1), so (1) does **not** explain that
observed jam. The initial idea that this particular endpoint might have all
three counts odd was checked and rejected. Conversely, several subsequent
screen states have all three counts odd and two vacancies while retaining
positive conservative activity. They exhibit the rate-independent obstruction
without being frozen configurations. The underlying final states and rate
checks are preserved, not replaced by a universal jamming explanation.

## Few vacancies suffice for an asymptotic transverse constraint

For the same standard dimer field B_i(x)=sigma_x[n_i(x)-1/6], define normalized
Fourier components by V^(-1/2) sum_x exp(-ik.x) B_i(x), V=N^3. At any nonzero
lattice momentum k, put d_i(k)=1-exp(-ik_i). The exact microscopic identity is

    d(k).B_hat(k)=q_hat(k),
    q_hat(k)=-V^(-1/2) sum_{x in V_0} sigma_x exp(-ik.x).

The Hermitian longitudinal projection is onto the complex vector conjugate
to d, not onto d itself:

    B_hat_L = conjugate(d) q_hat / ||d||^2,
    ||B_hat_L||^2 = |q_hat|^2 / ||d||^2
                  <= |V_0|^2 / [N^3 * 4 sum_i sin^2(k_i/2)]. (2)

This is a deterministic bound on every matching. At fixed K in 2pi Z^3
with K!=0 and k=K/N, its denominator is asymptotic to N |K|^2.
Consequently m_N=|V_0|=o(sqrt(N)) implies B_hat_L(K/N)->0.
For random states, E[m_N^2]=o(N) suffices for mean-square convergence.
The observation extends to finitely many fixed momenta by summing bounds.
For exactly two vacancies it is O(N^-1), uniformly in their separation,
orientation, stochastic history or equilibration status.

This does not prove that a formation process has the required vacancy bound.
A fixed small vacancy *density* is insufficient; it allows an extensive m_N.
The bound does not control transverse covariances, guarantee a nonzero field
limit, establish a Coulomb phase, identify the staggered field physically,
or yield wave propagation. It also does not remove the two microscopic
charges or establish the quantum Gauss constraint. It shows why failure of
exact finite-volume full packing alone does not refute a macroscopic
transverse-field route in three dimensions.

The next useful test is the scaling of residual vacancy counts and actual
conservative state exploration, with local-support cages separated from the
parity obstruction. This is more informative than treating every nonfilled
run as the same failure or automatically requiring exactly zero vacancies.
