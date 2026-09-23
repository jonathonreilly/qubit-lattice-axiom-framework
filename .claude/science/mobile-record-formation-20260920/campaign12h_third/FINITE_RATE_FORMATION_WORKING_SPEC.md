# Working route: a finite nonzero record-formation limit

2026-09-22. Working specification, not a frozen theorem or independently checked.
Root's next positive route after the charged-band calculation.

On a three-site star with central A and two B leaves, hard-core charges0,+,-,
Gauss divE+1_A-q=0 and unit rotor links imply E_(A->B)=-q_B. Total charge1.
Initially central +, both leaves vacant. Use H=Delta N_B+tT; within each fixed
record number its density evolution equals H'=Delta(1-n_A)+tT after subtracting
Delta(N-1). Both generators give identical number-block-diagonal marked histories
because jumps raise N by2 and the Hamiltonian conserves N.

The physical charge1 basis has three N1 states (record at A/B1/B2) and three
N3 states (one minus among three fully occupied sites). H' has energyDelta for
the two empty-A intermediates, energy0 for the central N1 state and all N3.
Hopping only couples central state to each leaf with amplitude-t.
Per vacant A-B edge use the coherent charge-pair jump with amplitude sqrt(beta).
From the intermediate on one leaf, the other edge's birth maps to the sum of
two N3 states (new center +/- with matching opposite charge on other leaf).
The filled states are absorbing. Resolved charge channels form a distinct
instrument with the same no-event loss.

Proposed scaling epsilon=t/Delta ->0, Delta=delta epsilon^-4,
t=delta epsilon^-3, beta=kappa epsilon^-2, delta,kappa>0.
No-event excited denominator Delta-i beta, beta/Delta=O(epsilon^2).
Effective per-edge jump amplitude sqrt(beta)t/(Delta-i beta) ->sqrt(kappa).
Total production hazard from the central state tends4kappa. Survival candidate
exp(-4kappa T), with nonzero macroscopic birth probability. Conditional final
charge state retains the instrument-dependent coherence. Microscopic birth
coefficient diverges; this is not the earlier fixed/vanishing-rate theorem.

The bright no-event 2x2 matrix is [[0,-sqrt2 t],[-sqrt2 t,Delta-i beta]].
Its slow eigenvalue is (Delta-i beta)/2 - sqrt((Delta-i beta)^2/4+2t^2)
with the branch continuous at t=0. It has real shift~-2t^2/Delta and imaginary
part~-2 beta epsilon^2 ->-2kappa, giving probability decay4kappa.
The divergent real shift is scalar in the surviving N1 code; there are no
N1/N3 coherences for the declared initial condition and number-raising jumps.
Need a complete finite-time density/instrument comparison, not only this
eigenvalue heuristic. Initial undressed transient should be O(epsilon).

Large-volume extension is OPEN: in the all-A-filled code with some B records,
second-order two-hop record exchanges have scale h=t^2/Delta, far faster than
the fourth-order gauge loops. A number-energy offset removes scalar sector
energies but not these non-scalar fast matter terms. The small star alone
does not resolve a finite-density matter-field limit, photon preservation or
autonomous energy/fuel costs. Reiter-Sorensen effective-operator literature
may provide context; any imported theorem needs checked hypotheses.

Analytic route now worked out, needs written proof and checked numerical source.
Write u=epsilon², z=Delta-i beta, r=sqrt(2)t, D=sqrt(z²+4r²) with D~z,
lambda_s=-2r²/(z+D), lambda_f=z-lambda_s.
Exact a=(lambda_f e^-i lambda_s tau-lambda_s e^-i lambda_f tau)/D,
b=r(e^-i lambda_s tau-e^-i lambda_f tau)/D.
S=|a|²+|b|². N1 density is |a A+b bright><...|;
absorbed density is exactly (1-S)sigma for all times.
sigma_coherent=[[2,1,1],[1,1,0],[1,0,1]]/4 in negative-at-A/B1/B2 order;
sigma_resolved=diag(1/2,1/4,1/4).
No N1/N3 coherences arise. Exact limit rho0=e^-4kappa tau |A><A|+
(1-e^-4kappa tau)sigma. Full trace norm error exactly
sqrt((S-s0)²+4s0|b|²)+|S-s0|, hence O(epsilon).

gamma=-2 Im lambda_s=4kappa+O(u), eta=-2 Im lambda_f=2beta-gamma,
pref=2 beta r²/|D|²=4kappa+O(u). Exact event density
pref[e^-gamma tau+e^-eta tau-2e^-beta tau cos(Re D tau)].
All-time L1 bound against 4kappa e^-4kappa tau:
(|pref-4kappa|+|gamma-4kappa|)/gamma + pref/eta+2pref/beta = O(u).
Event edge marks have probability1/2 and fixed conditional charge states,
so the full marked output-state law inherits this bound, not merely a count.
The exact mean clock appears to be
Delta²/(4 beta t²)+beta/(4t²)+1/beta
=1/(4kappa)+epsilon²/kappa+kappa epsilon⁴/(4delta²);
derive by a 2x2 Lyapunov equation and check independently.

Energy cost in the original Delta N_B Hamiltonian:
E(tau)/Delta ->2(1-e^-4kappa tau); microscopic energy per created pair diverges.
Subtracting the number offset is a density proof device, not a supplied
autonomous energy-conserving reservoir. No finite resource/TOE conclusion.
