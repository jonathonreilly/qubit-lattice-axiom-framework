# Precomparison: fixed-density canonical limit

Frozen before opening the new WORKING_PROOF. The parent brief disclosed the
proposed target and mechanism: apply the previously checked general block
transfer to a finite mean-energy minimizer, use uniform mean convergence for
the moving-density lower bound. Thus this is an independent composition check
with explicit method exposure, not blind discovery. I authored the old mean-
energy composition and parts of its lower input, and independently checked the
root's earlier block transfer. I also authored the recent integrated native
source. Those roles do not become independent validation of all input theorems.
The new proof's stated expected SHA72a793b3 is brief exposure only at this stage.

Only the new CONTRACT and actual old inputs/checks were read for this PRE:
the complete landed native density source, old mean composition and root
receipt, old block-transfer proof and my full receipt, and the mean source
binding file. The old mean and block proofs were read in full again. No new
proof/code has been opened or run. The selected methodology closure7146 and
its previously read focused-check rules remain unchanged. This is not formal
review or an audit.

## First-principles reconstruction

Use the actual finite qubit tensor product with N spectrum 0,...,V. The actual
Hamiltonian conserves N and is a sum of translated terms supported within
radius two, each of norm at most h*=182mu+240tau. Positivity and the vacuum
are given by the actual displayed SOS. These are the relevant carrier facts;
no dimer subspace, independent-pair map or continuum approximation is needed.

At every finite block side ell, the density matrices of trace one and exact
mean Tr(N Gamma)=rho ell^3 form a nonempty compact set. Nonemptiness follows
already from a vacuum/full-occupation mixture for every real rho in[0,1].
The linear energy minimum e_ell(rho) is attained. The minimizer need not be
pure, translation invariant, concentrated in one number sector, or near the
unitary trial. Number dephasing preserves its mean and energy.

The old general transfer lemma has a stronger domain than its old application:
for ANY fixed block density matrix with mean rho ell^3,0<rho<1,

 limsup_(L->infinity) E_L(N_L)/L^3
 <=Tr(H_ell Gamma)/ell^3+24h*/ell

for every integer sequence N_L/L^3->rho. Its proof uses only finite-sector
probabilities, the norm bound, and physical occupation capacity; it never uses
the old trial parameter or its fourth-order expansion. Consequently selecting
an actual e_ell(rho) minimizer for each fixed ell is legitimate. One obtains

 limsup_L E_L(N_L)/L^3 <=e_ell(rho)+24h*/ell.

The left side is independent of ell. First L tends to infinity for each fixed
ell,rho, then ell tends to infinity. The checked mean theorem gives
 e_ell(rho)->e(rho). Hence the upper limit is at most e(rho).

For the lower, put rho_L=N_L/L^3. Every exact-sector density matrix is an
admissible state in the mean problem at rho_L, so
 E_L(N_L)/L^3>=e_L(rho_L).
For fixed rho in(0,1/2), rho_L is eventually in[0,1/2]. The old uniform
convergence there and continuity of the convex limit e imply
 e_L(rho_L)->e(rho).
The lower and upper identify one limit independent of the integer sequence.
No uniform choice of block minimizer as ell varies is needed.

## Physical integer and seam checks to repeat against the new proof

Dephasing produces probabilities p_k and states tau_k in every physical sector
0<=k<=m, including arbitrary legal choices when p_k=0. With B' regular cubes,
round k<m down and assign the remaining cube count to k=m. Then the total
probability-count discrepancy is <=2m, number error <=2m^2, and energy error
<=2h*m^2. These estimates do not depend on the block state or its variance.

At fixed rho put q=min(rho,1-rho)>0 and d_L=N_L-rho V=o(V). Reserve
 r_L=ceil((|d_L|+2m^2+2)/(q m))+1
whole cubes, in addition to the uncovered sites. The free-site count U obeys
 qU>|d_L|+2m^2+1. Thus the required integer remainder lies in[0,U]. Filling
literal qubit sites realizes every such integer, including odd numbers even
when all original occupied block sectors were even. At fixed m,q, r_L/B->0.
The state remains normalized and has exact number, with no postselection.

Comparing actual H_L to periodic block copies costs at most
 24h*B ell^2+h*R_L
in operator norm: both the original seam terms and the added periodic ones
are included. This is independent of density and state, with no assumption
that a removed interaction is positive. Reserved and uncovered site energies
then vanish per volume at fixed ell,rho. The seam term vanishes only after
ell tends to infinity. Neither nondivisible L nor sector parity is a loophole.

## Uniform corollary and scope tests

For a compact K inside(0,1/2), convergence should be uniform over integer
sectors whose density lies in K. If not, choose violating L_j,N_j and a
subsequence rho_j->rho in K. Complete those prescribed integers to a full
sequence approaching rho by choosing nearest integers at other volumes.
The every-sequence theorem forces the violating subsequence's energy to
e(rho); continuity forces e(rho_j)->e(rho), a contradiction. This establishes
absolute energy-per-volume convergence, without a finite-size rate.

Applying the already checked e(rho)=t0 rho^2/8+o(rho^2) AFTER the fixed-rho
limit gives an actual inner limit in the ordered dilute statement. This is
not a uniform relative error after division by rho_L^2 for rho_L->0. The
reserve estimate contains 1/q, and the proof first fixes rho. No arbitrary
simultaneous dilute/volume limit, unique phase, condensate, polarization or
smooth thermodynamic function follows. Equality to a convex mean function
is consistent with phase coexistence and spatial block mixtures.

The new fixed-density equality needs the finite-range/all-sector transfer and
uniform mean convergence; the detailed threshold and all-state lower proofs
are dependencies only for the later coefficient t0/8, already supplied by the
checked mean theorem. I will not relabel rereading this composition as an
independent reproof of those deeper author inputs. No scientific computation
is needed: the discriminating points are quantifiers, the actual integer
capacity and the state-independent operator-norm seam bound.
