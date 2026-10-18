# Independent spatial response and sector-pairing check

Reviewed `native/compass_stationary_spatial.py`. Its cross-source reconstruction and conserved-sum reasoning are correct within the numerical Lanczos approximation and declared stationary selected-sector benchmark.

## Spectral cross reconstruction

Let v=(C−<C>)g, b_x=(e_x−<e_x>)g, L=H−E0 and f_eta(lambda)=lambda/(lambda²+eta²). With Lanczos columns Q starting at q0=v/||v|| and tridiagonal T, the desired real cross inverse moment is

I_x= <v,f_eta(L)b_x> = <b_x,f_eta(L)v>.

The projected approximation is ||v|| e0^T f_eta(T) Q^T b_x. The script saves every q_k overlap with all source vectors, diagonalizes T=U diag(lambda) U^T, and computes e0^T f_eta(T) as `(u[0]*f(en)) @ u.T`. Multiplication by the overlap array and ||v|| is therefore correctly normalized and indexed. Hermiticity justifies the source interchange for these real matrices/vectors. For general complex states one must use conjugate inner products and specify the desired real or complex response.

The object is a cross regularized inverse moment, not necessarily positive: its spectral weights are products of two different transition amplitudes. A signed spatial profile is fully consistent with that definition. A usual static ground-state response convention adds the factor two discussed in the previous report; it must not be silently read as a universal potential or interaction strength.

## Conservation control

The definition e_x=half the sum of incident native bonds counts every open-graph bond exactly twice before the half factor. Thus sum_x e_x=H even at faces, edges and corners. It follows that

sum_x b_x=(H−<H>)g,

which is zero for an exact eigenvector and has norm equal to its energy residual for an approximate normalized eigenvector. This explains the reported approximately 2.61e−13 norm. Consequently the exact mixed inverse moments sum to zero; the projected approximation inherits this identity to the size of the source-sum residual. The control validates normalization and conservation, but it does not certify convergence of each individual spatial entry. A uniformly applied source proportional to H cannot generate transitions in an exact eigenstate.

Agreement between 32 and 64 steps is useful numerical convergence evidence, not a rigorous error bound. The nonmonotonic center/face/edge/corner pattern belongs to this finite open graph and chosen source. It does not establish 1/r behavior, a bulk long-range force, or universal coupling.

## Independent small native-graph check

`/private/tmp/native-spatial-small-control.py` uses explicit 256-dimensional Pauli matrices for the independent eight-site native graph of the preceding report. For a central C source and the existing local energy at the added corner, eta=0.1 gives:

- full eigenbasis cross moment: 0.05901679785489236;
- independent quadratic polarization: 0.059016797854892444;
- the script's Lanczos cross reconstruction: 0.059016797854892354, terminating after six steps.

This tests the reconstruction, normalization, and cross sign with a nonzero separated source. It does not independently reproduce the root's 27-site corner numerical value; no large eigensolve or 64-step large-system repetition was performed.

## Exact 32-to-16 sector survey reduction

On the odd open 3x3x3 cube, an individual X-plane product commutes with H and every X-plane-pair stabilizer. Its intersection with each Z plane contains three sites, so conjugation sends each of the three Z-plane generators to its negative. It therefore maps sector (z0,z1,z2;x0,x1) unitarily to (z0 xor 1,z1 xor 1,z2 xor 1;x0,x1), preserving its full Hamiltonian spectrum. Choosing representatives with first Z sign zero covers all 32 sectors with exactly 16 representatives and misses none. This is a pair equivalence, not a claim that all representatives are equivalent or that the all-plus one is lowest.

The individual X-plane also preserves each native local energy bond and the central composite by the same commutation geometry. Corresponding eigenstates can therefore have identical mapped observables/response data across each paired sector; arbitrary numerical choices inside degeneracies still need matching if comparing individual eigenvectors.
