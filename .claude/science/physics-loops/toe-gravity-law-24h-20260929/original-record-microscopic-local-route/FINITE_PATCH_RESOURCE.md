# Explicit finite-patch spin resource for the separate target transfer

This appendix strengthens the finite-patch step of frozen SPIN_TARGET_LOCAL_LIMIT.md. It concerns only the effective spin target versus the original rotor target, not the fast microscopic generator. It supplies a conservative finite tolerance procedure. No large numerical experiment is needed.

Let a finite canonical patch have n_A center summands in the decomposition used there, retaining the common electric flow KD. Set

    beta=n_A(7920delta+160kappa),
    mu=n_A(50000delta+2000kappa),  C=S(S+1).

Both interaction-picture trace generators have norm<=beta. For rho whose two field legs have total absolute field at most s, and S>=s+8, their difference obeys

    ||(V_S(t)-V_rotor(t))rho||_1
                    <=mu (s+8)^2/C ||rho||_1.        (R1)

This is a restricted-input estimate, not the false global claim ||U_S-U||->0. The common diagonal electric orbit preserves the input cap exactly, so the same bound holds at every interaction-picture time.

Here is explicit source-word accounting for(R1). Each normalized spin shift differs from its unit rotor shift by at most d=(s+8)^2/C on every intermediate field of a word of length at most four. The inequality follows from

    |sqrt(1-z)-1|=z/(1+sqrt(1-z))<=z,
    0<=z=E(E+/-1)/C<=1.

There are six edge maps in F_a, each of whose two charge blocks has orthogonal input and output support. Thus ||(F_(a,S)-F_a)Pi_s||<=6d, with the same estimate for the adjoint after the cap margin. All F norms are<=sqrt(12). A four-F Gram word therefore differs by at most4*6*(sqrt(12))^3 d=288sqrt(12)d. The pair coefficient2delta and nine pair shares per center give5184sqrt(12)delta d. The19 anticommutator corrections vanish in the rotor target and each has restricted norm<=72delta d; their total is1368delta d. Since5184sqrt(12)+1368<20000, the Hamiltonian commutator difference is bounded by40000delta d per center, below the50000delta allowance in mu.

For an original resolved jump B=jF, ||B||<=3 and ||(B_S-B)Pi_s||<10d; for a coherent edge, ||B||<=sqrt(18) and the difference is<15d. These follow from ||j||<=1 or sqrt(2), the6d F difference and ||F||<=sqrt(12). The adjoint has the same bounds with the stated margin. Keeping both recycling and loss, a Lindblad difference has trace norm at most4 b d_B on capped inputs, where b is the common jump norm and d_B its capped difference. The sum over12 resolved labels is<=1440kappa d; the sum over6 coherent labels is<=360sqrt(18)kappa d<2000kappa d. This proves(R1) with the exact instruments, including their different coherent outputs.

Starting from Omega, an interaction-generator insertion changes the absolute field on either density leg by at most four. Expand the two bounded interaction-picture evolutions through order n0. At every intermediate input of a term of order n<=n0, the cap is at most4n. Telescoping its n ordered generator factors and using(R1), for S>=4n0+8,

    sup_(t<=T)||rho_(S,patch,t)-rho_(rotor,patch,t)||_1
      <= (mu/C) sum_(n=1)^n0
             n(4n+8)^2 beta^(n-1) T^n/n!
          +2 sum_(n>n0)(beta T)^n/n!.                (R2)

The common final electric unitary does not change trace norm. All omitted terms are priced by the absolutely convergent bounded-generator Dyson tail. This argument does not impose a physical electric cutoff or alter any process event.

For desired patch error eta, first choose finite n0 making twice the factorial tail<=eta/2. Then choose integer S>=4n0+8 whose C makes the first term<=eta/2. This is an explicit finite algorithm. The patch was chosen from the source-localization tail independently of total torus volume. Combining(R2) with that tail therefore supplies an actual uniform-volume spin resource, although the resulting bound is extremely conservative. The finitely many smaller tori can be priced by the same finite-patch formula on their actual periodic graphs.

For finite-region marked outputs the frozen proof already supplies a common history dominating measure, a factorial record-number tail, finite local spatial approximation and fixed-word convergence. An explicit tolerance algorithm first truncates that common history tail, then applies the same capped-word estimate to each remaining finite product of no-monitored-event propagators and the actual B maps. There are finitely many mark labels and word lengths after that cut; timestamp integrals have finite simplex volumes. This gives a finite resource procedure without exchanging the spin threshold with volume or exposing a coherent sign. No additional uniform microscopic timestamp conclusion is inferred.
