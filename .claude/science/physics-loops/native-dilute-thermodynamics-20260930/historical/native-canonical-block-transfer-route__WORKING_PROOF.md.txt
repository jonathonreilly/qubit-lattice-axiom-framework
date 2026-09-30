# Exact particle-number transfer of the native dilute upper

Root authored mathematical candidate, 2026-09-30T13:02:27.527171+00:00. Awaiting focused independent check. The actual supplied M2 Hamiltonian, all previously checked hypotheses and fixed positive mu,tau are retained. No theorem about condensate order, physical preparation, source or clock is asserted.

## 1. Statement and actual inputs

On the cubic torus of V=L³ sites write E_L(N) for the lowest energy of the ACTUAL H0 in its exact integer number sector N,0<=N<=V. Each such sector is nonempty in the full qubit tensor product. The actual source gives

 H0,L=sum_x h_x,L,   [H0,L,N]=0,
 supp h_x,L subset x+[-2,2]³,  ||h_x,L||<=h*=182mu+240tau.   (1)

These statements follow from the explicit onsite/attraction/triple/gradient grouping, not a continuum replacement. For L>=5 that grouping has the stated distinct-site convention. H0,L>=0. No positivity of individual h_x is needed below.

Let t0=min_(||z||=1) T0[z tensor z]>0, with the checked full physical N4 threshold form and its actual incoming normalization. For each fixed unit complexz and finite physical compact correctionchi, set tchi=E_z(chi)>0. The checked variational construction supplies actual normalized states tau_ell(u) on every periodic block sideell>=Lchi, satisfying uniformly in ell

 Tr tau_ell(u) H0,ell /ell³ <=(tchi/2)u4+Dchi |u|6,
 |Tr tau_ell(u) N/ell³-2u²|<=Bchi u4.                       (2)

The constants are finite at fixedchi, although they need not stay bounded when chi improves. Density is continuous in u because the finite-volume state is an exact unitary applied to Omega. For any accuracy one may choose fixed z,chi with tchi<=t0+accuracy. Equation(2) is an existing provisional input, not reproved or replaced by a bosonic state here.

The new claim is a canonical UPPER for every integer sequence N_L/L³->rho at fixed0<rho<1. For each fixedchi and all sufficiently smallrho,

 limsup_(L->infinity) E_L(N_L)/L³
                 <=(tchi/8)rho²+Cchi rho³.                  (3)

Combining(3) with the checked actual all-state dilute LOWER t0/8 yields: for every family of integer sequences N_L(rho) with N_L(rho)/L³->rho at each fixed positive rho,

 lim_(rho down0) liminf_(L->infinity) E_L(N_L(rho))/(L³rho²)
 =lim_(rho down0) limsup_(L->infinity) E_L(N_L(rho))/(L³rho²)
 =t0/8.                                                     (4)

There is no assertion here that the two thermodynamic envelopes coincide at each fixed nonzero rho. A single unrestricted joint L,rho limit is not claimed. Odd N is permitted; no pair-parity projection is made.

## 2. Tune the actual finite-block mean by continuity

Fixchi and write B=Bchi,D=Dchi,t=tchi. Assume 0<rho<=min(1/2,1/B); the known B is positive. Let v=u². At v=rho/4 the upper density bound from(2) is

 2v+Bv²=rho/2+B rho²/16<rho.

At v=rho the lower density bound is2rho-B rho²>=rho. The intermediate-value theorem therefore gives some actual u_ell with

 Tr tau_ell(u_ell)N/ell³=rho,   rho/4<=v_ell<=rho.             (5)

Neither uniqueness, monotonicity nor differentiability is used. The uniform remainder then implies

 |v_ell-rho/2|<=B rho²/2,
 v_ell²<=rho²/4+(B/2)rho³+(B²/4)rho4,
 v_ell³<=rho³.

Since B rho<=1, its energy e_ell obeys

 e_ell:=Tr tau_ell(u_ell)H0,ell/ell³
      <=t rho²/8+[D+3tB/8]rho³.                             (6)

Thus Cchi=Dchi+3tchi Bchi/8 suffices. This tuning occurs independently on each finite block size but with the SAME error constants. The proof does not project a variable-number trial onto a presumed typical number.

## 3. Number-sector block transfer lemma

Fix any ell>=5, put m=ell³, and let tau be any density matrix of the actual periodic block with exact MEAN particle number rho m,0<rho<1. Let e=Tr tau H0,ell/m. Then for EVERY sequence of integers N_L with N_L/L³->rho,

 limsup_L E_L(N_L)/L³ <= e+24h*/ell.                         (7)

Here is a constructive proof. Dephase tau in the block number sectors. Since N and H commute this changes neither mean nor energy. Write the dephased state as sum_(k=0)^m p_k tau_k, where tau_k is a normalized density in the exact k sector when p_k>0. For p_k=0 choose any density in that nonempty sector. Hence

 sum p_k k=rho m,   sum p_k E_k=m e,
 E_k=Tr tau_k H0,ell,   |E_k|<=h*m.                          (8)

Tile the large torus by B_L=floor(L/ell)³ disjoint contiguous ell-cubes and let R_L=V-mB_L be the unfilled sites. R_L/V->0 at fixedell. Reserve r_L complete cubes, leaving B'_L=B_L-r_L regular cubes. The precise vanishing reservation will be specified below.

For k<m set n_k=floor(B'_L p_k), and set n_m=B'_L-sum_(k<m)n_k. All n_k are nonnegative integers and sum to B'_L. Since each of the first m errors lies in(-1,0] and their opposite sum is the last error,

 sum_k |n_k-B'_L p_k|<=2m,
 |sum_k k n_k-B'_L rho m|<=2m²=:D_m,
 |sum_k n_k E_k-B'_L m e|<=2h*m².                            (9)

The inequalities deliberately overcount. In particular the last sector can be used for rounding even when p_m=0; no nonexistent conditional state is needed because tau_m was chosen above. Put exactly n_k of the regular cubes in state tau_k. Each product term is in one precise TOTAL number sector, despite possible mixing within each tau_k.

Let d_L=N_L-rho V, q=min(rho,1-rho)>0. For large L choose, for example,

 r_L=ceil((|d_L|+D_m+2)/(q m))+1.                            (10)

Then r_L/B_L->0 because d_L=o(V), while eventually r_L<B_L. Let U_L=R_L+r_L m be the number of reserved/unfilled sites. It satisfies q U_L>|d_L|+D_m+1. If N_reg=sum k n_k, equations(9)-(10) give

 0<=N_L-N_reg<=U_L.                                        (11)

Indeed N_L-N_reg=rho U_L+d_L-(N_reg-rho m B'_L), and both its lower bound and its distance from U_L are positive by the choice of q U_L. The difference is an integer. Fill exactly that many of the U_L free sites in a computational product state and leave the others empty. Every integer between0 and U_L is possible on actual M2 sites. The resulting full density matrix is supported in EXACT sector N_L, with no postselection, no normalization loss and no use of canonical pair commutation relations.

The construction may choose different reservations and block assignments for different N_L. This is a variational existence argument, not an efficient physical state preparation. At small fixedrho the constant reservation can be large; rho is held fixed while taking L->infinity, exactly as required.

## 4. All actual seams are priced

Compare the actual large-torus Hamiltonian with the tensor sum of periodic block Hamiltonians on all B_L cubes, acting by zero on the leftover sites. If a cube center is at least two coordinate steps from every cube face, its actual h_x equals the corresponding periodic-block h_x. At most

 ell³-(ell-4)³<=12ell²

centers per cube fail this condition. Every mismatched actual and block term has norm at most h*. Terms centered on R_L leftover sites contribute at most h*R_L. Consequently

 ||H0,L-sum_(all B_L cubes) H0,ell^(cube)||
                    <=24h* B_L ell²+h*R_L.                  (12)

This is a direct operator-norm comparison of the ORIGINAL finite-range terms. It includes actual physical edges across all seams, outer periodic wraparound and the internal periodic wraparound terms that were artificially introduced for block energies. It does not discard a positive interaction or assume a low-density boundary state.

The r_L reserved cube states have energy bounded above by h*m each. Combining(9),(12) for the exact-sector trial gives

 E_L(N_L)<=B'_L m e+2h*m²+h*r_L m
                          +24h*B_L ell²+h*R_L.             (13)

At fixedell,rho, the error2h*m²/V and reserved volume fraction vanish, B'_L m/V->1 and B_L ell²/V->1/ell. This proves(7), including arbitrary nondivisible L and either particle parity. No exchange of global and block limits occurred.

## 5. Remove block boundaries and take the dilute limit in order

Apply(7) to the tuned tau_ell from(5), using(6). For every fixedchi, fixed smallrho, every sufficiently largeell and every N_L/V->rho,

 limsup_L E_L(N_L)/V
       <=tchi rho²/8+Cchi rho³+24h*/ell.

The left side has no ell dependence. Taking ell->infinity AFTER the thermodynamic limsup proves(3). The trial parameter and state may depend on ell; the bound(6) does not. Then take rho down0 at fixedchi, obtaining a limsup coefficient at most tchi/8. Finally improve the compact threshold correction and coherent direction to t0. Divergent Bchi,Dchi with that improvement are harmless because their rho limit was already taken for each fixedchi.

For the lower side use the completed actual PARTICLE_TAIL_AND_LOWER_COMPOSITION, source2e4d9f8b/receipt124091e9. Its finite-volume estimate applies to every density matrix. In an exact N_L sector its density is N_L/V and tends to rho. At each fixed mesoscopic choice its finite-volume remainder vanishes in the thermodynamic limit; replacing N_L/V by rho is ordinary continuity of that explicit polynomial bound. The subsequent fixed-m,large-K,small-eta parameter choices and final rho limit are precisely those of that source. Hence it gives the lower coefficient t0/8 for these same integer families. This combines with(3) to give(4).

This application does not infer the lower coefficient from the trial, does not use a periodic fixedN4 gap at finite density, and does not assume fragmented many-pair states are coherent. The lower theorem's finite-mode argument supplied that last minimization independently.

## 6. Status and limits

The new step is elementary but necessary: an actual finite-range qubit block transfer turns the supplied uniform mean-density trial into exact-number thermodynamic upper bounds. Its scope is an ordered canonical DILUTE asymptotic, not an exact finite-density energy function or all-order expansion. The all-state lower and full threshold definition remain provisional source-bound checked inputs; a focused independent check of this transfer is still required before reuse.

No new numerical run was performed or needed. The proof gives explicit rounding, seam and density-tuning bounds rather than treating finite numerics as thermodynamic evidence. No change to the Hamiltonian, primitive registry, axiom memo, state-selection rule, record process or gravitational source is introduced. A physical collective spectrum and permanent-record observable remain harder open questions. No current axiom inconsistency follows from this optional model's success.
