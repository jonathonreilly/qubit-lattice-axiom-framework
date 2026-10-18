# Exact dressed source packets

Let c_j=Z_(j,z)Z_(j,z+2), and C_w=sum_j w_j c_j for finite real weights. No source term is appended to H. In the exact normal form H'=U_m H U_m^dagger, retain Ctilde_w=U_m C_w U_m^dagger exactly.

For each fixed-support c_j, the joint mixed-word expansion used to bound U_m H U_m^-1 also bounds its conjugation. Each word with n commutators has support size at most2+n s, and the factorial majorant has positive convergence radius. Multiplying the summand by that support size is only an extra polynomial in n and preserves convergence on a smaller lambda disk. Thus one obtains a decomposition Ctilde_j=sum_Y C_(j,Y) with sum_Y |Y| ||C_(j,Y)||<=C_m, uniform in j and volume, also with an exponential diameter weight. This is an interaction decomposition bound, not a false finite-support assertion about Ctilde_j.

Apply the established finite-support dynamical bound to every C_(j,Y) and sum absolutely. For B_m=2N+D_m, epsilon=lambda^(m+1),

    ||tau_H'(t)Ctilde_w-tau_Bm(t)Ctilde_w||
    <=C_m ||w||_1 epsilon |t| (1+lambda|t|)^3.

For any initial physical density matrix rho, transform rho'=U_m rho U_m^dagger and use this SAME rho' for both evolutions. Since ||Ctilde_w||=||C_w||<=||w||_1, the unsymmetrized two-time correlation difference is bounded by

    C_m ||w||_1^2 epsilon |t| (1+lambda|t|)^3.

The commutator/retarded-response difference has the same bound with factor2. Centering by the same initial mean changes only constants. No stationarity or ground-state premise is needed for this finite-time comparison, but neither is a physical initial state derived.

At m20, t=O(lambda^-4), L=O(lambda^-2/3) source sites, weights1/sqrt(L) give ||w||_1²=L and errorO(lambda^(22/3)). Unweighted weights1 give L² and errorO(lambda^(20/3)). Both are o(lambda^6). This does not identify a physical detector, prove a spectral pole, or certify any numerical lambda as inside the asymptotic radius. All D1..D20 remain in the reference evolution. Dropping their unknown high-order terms is a different uncontrolled step; the result only makes the actual normal-form remainder and exact-source dressing manageable at polynomial times.
