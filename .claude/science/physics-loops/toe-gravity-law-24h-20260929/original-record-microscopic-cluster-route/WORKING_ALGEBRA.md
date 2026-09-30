# First source-moment mechanism, before control

Candidate, not yet a completed theorem. Put K_def=W+N_B. Since every original birth removes one A hole and adds one B occupant, [K_def,j_m]=0. Total N and W determine K_def=N-N_A+2W. A finite-color Hamiltonian normal form through order three can arrange

    H'=delta epsilon^-4 W+delta epsilon^-2 D2+O_local(1),
    [D2,W]=[D2,N]=0,
    J_m=j_m+epsilon j_(1,m)+O_local(epsilon^2).

Here the O_local(1) term includes all physical order-one terms rather than dropping them. Normal-form W-preserving Hamiltonians commute with K_def. For ANY bounded f(K_def), the coefficient of the cross-jump drift is

    D_cross(j_m,j_(1,m))^* f(K_def)
       =1/2[f(K_def),X_m],
    X_m=j_m^*j_(1,m)-j_(1,m)^*j_m,

because bare j_m commutes with f(K_def). X_m is anti-Hermitian, has W grades+/-1, and preserves N. This is a commutator identity for this observable algebra, not a claim that the entire cross dissipator is Hamiltonian.

Let X=sum_m X_m and I_W invert [W,.] off grade zero. The local anti-Hermitian generator

    S_loss=(i kappa/(2delta)) I_W(X)

obeys [S_loss,W]=-i kappa X/(2delta). An additional local unitary frame Z=exp(epsilon^3 S_loss), implemented as a finite-color product, introduces

    i[delta epsilon^-1[S_loss,W],f(K_def)]
                     =-(kappa/(2epsilon))[f(K_def),X],

canceling the entire epsilon^-1 cross-jump drift. The leading epsilon^-2 Hamiltonian and bare dissipator both annihilate f(K_def). The remaining action on exp(theta K_def), normalized on both sides by exp(-theta K_def/2), should be a bounded local interaction of strength C_theta, hence <=C_theta N_A I. Unlike an additive extensive observable corrector, unitary conjugation preserves positivity at arbitrary volume.

The prospective Gronwall bound is for the positive tilted observable in this frame. Returning to the physical count and pricing the bare preparation requires a separate small-gate inequality, not ||Y-I||=O(epsilon) globally. A useful local lemma to prove is

    U^* exp(theta K_loc) U
        <=exp(c epsilon^2) exp(theta' K_loc), theta'>theta,

for a local near-identity unitary U, finite matter-count spectrum of K_loc, and sufficiently small epsilon independent of electric dimension. The zero-count block changes its weighted norm only at second order; the positive-count block has a fixed gap after the theta' tilt, and its O(epsilon) off-block term is absorbed by that gap. A finite number of disjoint gate layers then gives exp(C_theta N_A epsilon^2), not an uncontrolled extensive norm error.

If all uniform locality/positivity details work, this would give

    E_micro exp(theta K_def(t))
          <=exp[C_theta N_A(t+epsilon^2)].

This would quantitatively suppress dense GLOBAL sectors on a common short physical time. For example full B with W=2 has K_def=N_A+2. Combining its Chernoff bound with the checked O(epsilon^2) hole density could yield a vanishing bound uniform over volume for its instantaneous weight. It would NOT by itself control fast integrated field influence or LOCAL dense islands in much larger systems. Those remain the priority next steps; no local cluster tail is presumed.
