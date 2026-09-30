# Boundary ledger and scale pricing — unfinished route

Author analytic work; no computation, independent check or result closing the contract. Existing source/check premises are unchanged. Root pauses this route to independently check the new compatible periodic collision step before substantial reuse.

## An exact safe diagonal lower boundary

For a vertex cube Lambda retain actual complete S/W rows whose entire physical support is in Lambda. Dropping other positive rows is a lower comparison. It is NOT valid simply to replace each physical m_x by the number m_int of occupied neighbors in Lambda in Ddiag: phi(m)=(m-1)(m-2)/2 has phi(0)=1 but phi(1)=phi(2)=0.

For a center x in Lambda let q_x be the number of its18 actual graph neighbors outside Lambda and m=m_int. Define

 d_Lambda(x)=n_x min_{0<=j<=q_x, j integer} phi(m+j).

This operator is diagonal on the physical cell and pointwise <=n_x phi(m_x) for every full exterior configuration, including coherent states after expectation. It is nonnegative. If q_x=0 it is the original phi(m). If q_x>0, the minimum is0 when m=0,1,2 (for m=0 choose j=1); for m>=3 it is phi(m). In particular the only change from using phi(m_int) is removing the isolated-particle penalty at boundary centers m=0. The external neighbors are optimized only for a lower comparison, not changed in the original law; no assumption says their optimizing occupations can be simultaneously realized.

For a disjoint vertex tiling, sum complete positive S/W rows and mu sum d_Lambda(x) is an exact operator lower bound on H. Each retained row appears once and each occupied center is assigned once. A regularization split (1-epsilon)(S+W)+epsilon a Egrad15+mu D may similarly retain complete internal gradient rows, using the actual simultaneous gradient comparison. This is a positive physical-cell decomposition with free boundary defects, NOT the periodic law or the desired fullT0 coefficient.

The new cell form has exact zero-energy boundary singleton vectors: one occupied site x with q_x>0 and no other particles is annihilated by every pair row and has d_Lambda(x)=0. Products of separated nongraph boundary sites are also zero if all have no internal graph neighbor. Therefore a naive use of the old periodic rank-binomial(n+4,4) gap is invalid on this cell. A theorem may still compare bulk soft-pair occupation while retaining a boundary environment; these modes have no bulk pair count and do not refute such a comparison.

Translation averaging bounds expected particles in a width-w boundary strip by C w/ell times total expected N (plus incomplete tiling remainder). This controls a particle fraction, not the energy of deleting those particles or the norm of a global no-boundary projection. Treating it as an energy bound would repeat the existing incompatible-cell mistake.

## Direct smooth localization has a priced cost

For any real multiplication partition on configurations sum_sigma chi_sigma(S)^2=1, the exact quadratic-form identity is

 sum_sigma E(chi_sigma psi)-E(psi)
 =-1/2 sum_(S,T) H_ST conjugate(psi_S) psi_T
                           sum_sigma[chi_sigma(S)-chi_sigma(T)]^2.

Diagonal entries cancel. The sign is not necessarily positive because this physical Hamiltonian need not be stoquastic. Absolute values and |psi_S psi_T|<=(|psi_S|^2+|psi_T|^2)/2 give an upper error bounded by one-half the weighted absolute row sum. For a conventional smoothly labeled particle-cell partition of scale ell, each nonzero local pair move changes at most4 sites by bounded distances. Its squared partition distance is O(ell^-2). Every occupation has at most9N occupied graph edges, and each has only a fixed number of outgoing pair moves with fixed mu,tau coefficients. Hence the standard absolute-row-sum estimate costs C N/ell^2.

This is the cost of that estimate, not a lower bound on the optimal localization error. At density rho it is C rho/ell^2 pervolume. To make that bound o(rho^2) requires ell*rho^(1/2)→infinity. The existing finite periodic band theorem uses theta/Delta=O(n^2/ell), with n of order rho ell^3 in a typical cell. To have its displayed small-band estimate vanish requires rho^2 ell^5→0. These sufficient conditions cannot hold together: ell≫rho^-1/2 and ell≪rho^-2/5. Thus that particular bound cannot complete the cell proof; this is not a theorem that all localization, a relative many-particle gap, Dyson replacement or the desired EOS is impossible.

## Live exact missing lemmas and strength

A. Prove a fullT0 lower form for bulk soft-pair occupation in the safe open-cell form while retaining its boundary singleton/environment sectors. This is strictly more structured than merely positing a boundary condition, but currently target-equivalent to the missing physical boundary comparison at the leading coefficient.

B. A direct compatible collision-row packing could bypass cells: assign every complete positive row at most once to a nearby four-particle cluster, including its nonmatching responses, then show its soft boundary flux gives the full T0 replacement. Pair selection that depends on row input changes creates a guard cost; independent minimization of spectator fibers is not allowed. The full flux/packing estimate is unproved and target-equivalent.

C. Improve the localization error using actual low-energy cancellations, or prove a relative gap above a many-particle background. Neither follows from the current absolute fixed-cell gap. A small norm loss of the compatible map is not kinetic intertwining.

D. Two-scale scattering replacement before localization may soften the potential and change the competing scale bounds. Its Dyson-style hypotheses must be derived for the actual nine-component pair kinetic form and all physical matchings; the usual scalar continuum lemma cannot simply be cited as this law.

E. Keep global periodic geometry and prove a density-uniform compatible expansion directly, avoiding a physical-cell lower decomposition. Fixed-n or n<=sqrt(logL) convergence is insufficient at fixed rho as L→infinity, but it could be an ingredient in a new multiscale proof.

These are research obligations, not a negative-claim packet or shipped no-go. No useful route is ruled out globally; no axiom pressure follows. The proof target and optional supplied premises are unchanged.
