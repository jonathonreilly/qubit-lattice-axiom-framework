# Canonical thermodynamic existence from the checked block lemma

Root author composition; independent check pending. The contract was frozen
before this proof. This is not part of the already frozen native milestone.
No new calculation or numerical run is used.

## Actual inputs and domains

Keep precisely the supplied qubit Hamiltonian H0,L(mu,tau) and number N on
periodic L^3-site cubes, fixed mu,tau>0. The complete actual source and the
checked block proof give H0,L=sum_x h_x,L with radius two and
||h_x,L||<=h*=182mu+240tau, [H0,L,N]=0, H0,L>=0. All integer number sectors
0,...,L^3 exist in the FULL qubit tensor product. These are mathematical
features of the supplied law, not derived axiom selection.

Let E_L(n) be the minimum in its EXACT n sector, and let e_L(rho) minimize
Tr Gamma H0,L/L^3 over all density matrices with Tr Gamma N=rho L^3.
The actual mean-composition proof section2 and its focused receipt establish

 sup_(0<=r<=1/2) |e_L(r)-e(r)| ->0,                         (1)

where e is continuous and convex on that closed interval. It follows from
uniform compact-chemical-potential convergence of g_L and the explicit
slope bound0<=nu<=2h*. No fixed-number conclusion was used to prove (1).

The independently checked sector block-transfer lemma, sections3-4 of
WORKING_PROOF in native-canonical-block-transfer-route, states: for ANY fixed
ell>=5, ANY block density matrix tau with EXACT mean rho ell^3,0<rho<1,
and EVERY integer sequence n_L/L^3->rho,

 limsup_(L->infinity) E_L(n_L)/L^3
       <= Tr tau H0,ell/ell^3 +24h*/ell.                   (2)

This lemma's hypotheses are broader than the particular unitary trial used
in its original dilute application. Its proof dephases tau into actual
number sectors, rounds their finite block frequencies, and reserves a
vanishing fraction of physical sites to match each n_L exactly. It applies
even when a sector of zero probability is populated by rounding: that sector
exists independently and any normalized state there suffices. Mixed states
inside a fixed sector are valid exact-sector variational competitors.

For clarity the needed uniformity is only fixed ell,rho followed by L->infinity.
If m=ell^3, the count-rounding error is bounded by2m^2. The reservation uses
q=min(rho,1-rho)>0 and at most ceiling((|n_L-rho L^3|+2m^2+2)/(qm))+1
complete cubes. Its fraction tends to zero for each fixed ell,rho. The true
versus artificial-periodic seam norm is at most24h*floor(L/ell)^3 ell^2
plus h* times leftover sites. This is why (2) treats all side lengths and
both parities. Neither a simultaneous vanishing rho nor an efficient physical
preparation is a conclusion of that construction.

## Exact fixed-density limit

Fix0<rho<1/2 and any sequence0<=n_L<=L^3 with r_L=n_L/L^3->rho.
Every exact-sector density matrix is admissible for the mean constraint at
r_L. Thus, for every L,

 E_L(n_L)/L^3 >= e_L(r_L).                                  (3)

Eventually r_L lies inside[0,1/2]. Uniform convergence (1) and continuity of
e at rho imply e_L(r_L)->e(rho), so the canonical liminf is at least e(rho).
The moving-density step uses uniform convergence, not a pointwise limit
at rho substituted for a different finite-volume density.

For each FIXED ell choose a minimizer tau_ell for e_ell(rho). Such a density
matrix exists: its finite-dimensional positive trace-one, exact-mean
constraint set is nonempty and compact. Noninteger rho ell^3 is allowed
for THIS block mean constraint. It does not relax the final exact n_L
constraint, which the block lemma implements deterministically.

Apply (2) to this tau_ell. For every fixed ell>=5,

 limsup_L E_L(n_L)/L^3 <= e_ell(rho)+24h*/ell.               (4)

The left side is independent of ell. Send ell to infinity AFTER the
thermodynamic limsup. Equation (1) at fixed rho gives the upper bound e(rho).
Combining with (3) proves

                  lim_L E_L(n_L)/L^3=e(rho).                (5)

No canonical limit, sector concentration or equivalence of ensembles was
assumed. The equality is an energy variational statement and may be realized
by phase-separated block trials; it does not identify a state or phase.

One can also record the directly equivalent compact-density uniformity:
for any0<a<b<1/2,

 max_(n: a<=n/L^3<=b) |E_L(n)/L^3-e(n/L^3)| ->0.            (6)

If (6) failed, choose a violating subsequence L_j,n_j. Compactness gives a
further subsequence with n_j/L_j^3->rho in[a,b]. The proof (3)-(4) applies
unchanged along this subsequence (or extend it to a full integer sequence).
Equation (5) and continuity of e contradict the fixed positive discrepancy.
The interval is bounded away from zero; (6) has no claimed convergence rate.

## Ordered dilute consequence and remaining scope

The separately checked full threshold/dilute mean theorem gives

 e(rho)=t0 rho^2/8+o(rho^2),       rho down0.                 (7)

Composing ONLY AFTER (5), for every family of integer sequences
n_L(rho)/L^3->rho at each fixed0<rho<1/2,

 lim_(rho down0) [lim_(L->infinity) E_L(n_L(rho))/(L^3 rho^2)]
                         =t0/8.                            (8)

Unlike the previously stated two-envelope consequence, (8) has an actual
inner limit. The extra mathematical input is absent: the general already
checked lemma (2) suffices once applied to true finite-block mean minimizers
rather than only the unitary trial. The new composition and quantified
conclusion still require their own independent check before reuse.

Equation (5) itself uses no threshold theorem or dilute expansion; only
the actual finite-range number-conserving carrier, (1) and (2). Equation (8)
additionally inherits every supplied-law and threshold hypothesis of (7).
The stronger all-positive-density and endpoint versions are not asserted
here. No unrestricted joint rho,L limit follows: the seam and reserved-volume
arguments take L at fixed ell,rho, then ell, while (8) takes rho last.

This extension neither proves ODLRO, condensate polarization, uniqueness,
a gap, sound or relativistic dispersion, a physical source/record observable,
a selected Hamiltonian, nor a current axiom contradiction. No existing
review unit or PR is silently enlarged. Exact input hashes remain in the
contract freeze; no physical law or empirical value has changed.
