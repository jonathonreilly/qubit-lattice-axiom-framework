# Energy control upgrades the edge-face limit to electric Gauss mean square

**Status:** proposed conditional extension, pending controls and independent
check. **Date:** 2026-09-21. **Dependency:**
`DIMER_EDGE_FACE_GAUSS_QUANTUM_LIMIT.md`, SHA-256
`a6759908ef27e5f2990c7f20d4615aa4166d9a33bec66ea4b4e8143c22f01824`.

The primary note proves convergence of bounded field words. The extra energy
argument here, rather than bounded convergence alone, also controls the
electric constraint in mean square. All volume, state, architecture and
microscopic-interpretation limitations of that note remain in force.

## Initial and conserved energy

On a link block, ||Q_K|| and ||P_K|| are at most sqrt(K/2): these are the
spin-K/2 components multiplied by sqrt(2/K). The same bound holds on the
common Fock extension. Since the number of edges and nonzero incidence
entries is fixed, ||H_K||<=B_L K. Put epsilon=K^-1/6 and delta=K^-1/3.

Let psi_epsilon and its normalized physical projection phi_K be as in the
primary note, and E_T=<psi_T,H_T psi_T>. The full canonical energy is

    <psi_epsilon,H psi_epsilon>=E_T+(dim Z)epsilon^2/4.

The weighted difference bound (10), the state-moment bound (11), and the
projection estimate (12) give

    |<phi_K,H_K phi_K>-E_T|
      <= |<psi_epsilon,(H_K-H)psi_epsilon>|
         +2||H_K|| ||phi_K-psi_epsilon||
         +(dim Z)epsilon^2/4
      <= A[K^-1 epsilon^-4+epsilon^2]
      <= A delta.                                  (A1)

Both vectors have norm one, so the middle term uses the ordinary bounded
operator expectation inequality. The linear-in-K Hamiltonian norm is needed
here; the projection error alone would not justify an energy statement.
The exact finite-qubit evolution conserves the left energy. The reduced
canonical evolution conserves E_T. Thus (A1) holds at every time, without
claiming H_K approaches H in global operator norm.

## Quantitative recovery of quadratic fields from their characteristic functions

For a single Heisenberg Weyl operator with real test z, the proof of the
primary note can be kept polynomial in ||z||. The two evolution differences
cost at most A delta independently of z. The linear-Weyl Duhamel term costs

    A K^-1 epsilon^-3 ||z||(1+||z||)^3,

because conjugation by the canonical Weyl operator translates Q,P linearly.
The squeezed-sector phase costs at most A epsilon^2 ||z||^2. Constants may
depend on the fixed field map, L, psi_T and time interval, but not K or z.
Since K^-1 epsilon^-3=K^-1/2<=delta, for either the commuting vector of
transverse electric components E_(T,K) or the commuting magnetic components
B_K this gives the sufficient bound

    |chi_K(z,t)-chi_T(z,t)|<=A delta(1+||z||)^4,
    |t|<=T.                                        (A2)

Different link momenta commute, as do different link coordinates, so these
two field families separately have ordinary joint spectral distributions.
No joint commutativity of E and B is assumed. The canonical fourth moments
of both families are bounded uniformly on the fixed time interval.

For a commuting vector X and 0<a<=1 define the bounded nonnegative function

    F_a(X)=[1-exp(-a||X||^2)]/a.

It satisfies 0<=F_a(X)<=||X||^2. In the canonical state,

    <F_a(X)> >= <||X||^2>-(a/2)<||X||^4>.            (A3)

The Gaussian Fourier representation

    exp(-a||X||^2)= E_(z~N(0,2a I)) exp(i z.X)

and (A2) imply

    |<F_a(X_K)>-<F_a(X_T)>|<=A delta/a,              (A4)

because E(1+||z||)^4 is bounded for a<=1 in the fixed finite dimension.
This step uses all real tests through their explicitly bounded polynomial
dependence; pointwise characteristic convergence without that control would
not give the rate in (A4).

## Electric constraint bound

The real orthogonal edge decomposition T plus Z gives exactly

    H_K = [||E_(T,K)||^2+||B_K||^2]/2
          +||E_(Z,K)||^2/2.

Apply (A3)-(A4) separately to transverse E and B, whose reduced total energy
is E_T. Positivity gives

    <[||E_(T,K)||^2+||B_K||^2]/2>
       >= E_T-A[a+delta/a].                         (A5)

Subtract (A5) from the conserved-energy estimate (A1). Choosing
a=sqrt(delta)=K^-1/6 yields

    sup_(|t|<=T) <||E_(Z,K)(t)||^2> <= A K^-1/6,
    sup_(|t|<=T) <||d_0^T E_K(t)||^2> <= A_L K^-1/6. (A6)

The harmonic electric components are included in Z and obey the same
control. The root-mean-square sufficient rate is K^-1/12. Magnetic divergence
and its zero harmonic flux are already exact at finite K. None of these
bounds asserts that electric Gauss commutes with the finite-K Hamiltonian.

The argument supplies a uniformly finite-energy sequence of actual qubit
states approaching the zero-charge observable sector over finite times.
The large number of Fock quanta in squeezed gauge coordinates does not
force a divergent physical energy because those coordinates lie in ker C.
The correlated state preparation and collective microscopic interactions
remain supplied structures; neither is produced by the permanent-record
formation process in this construction.
