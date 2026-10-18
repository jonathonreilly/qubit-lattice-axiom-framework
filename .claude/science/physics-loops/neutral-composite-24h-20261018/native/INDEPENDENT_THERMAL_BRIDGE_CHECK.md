# Native compass first thermal energy–composite response

Independently checked the root's `native/compass_thermal_bridge.py/json` with the previously independent binary-symplectic Pauli representation. Root multiplication functions were not imported. `/private/tmp/native-thermal-bridge-check/check.py` and `result.json` reproduce **every displacement coefficient through derivative order4**, including all57 nonzero order4 entries, and the conservation sums.

## Definition and exact coefficients

With normalized tracial state, D=i[H,.], and physical local energy e_r=K/2 times the six incident Pauli bonds, define

    F_n(r)=tr[H {D^n C0,e_r}]/2,
    F_r(t)=tr[H {C0(t),e_r}]/2.

At K=1:
- F0(0)=3; F0(r)=1/2 at the six nearest neighbors; zero elsewhere.
- F1=F3=0.
- F2(0)=−48; F2(r)=4 at the twelve face diagonals; zero elsewhere.

The root stores twice F_n, so its onsite values6 and−96 have the correct normalization. Every nearest bond belongs to two local-energy densities with coefficient K/2; that half is essential.

Fourier transforming the order2 coefficient gives

    F2(q)=−48+16 sum_(a<b)cos(q_a)cos(q_b)
         =−16 |q|²+O(|q|^4).

Coordinates here use unit lattice spacing; restoring a physical spacing changes the small-q units. This is a short-time response coefficient, not a dispersion relation or Laplacian field equation.

## Sign of the retarded coefficient

Use the declared convention

    chi_C,e(r,t)=i theta(t)<[C0(t),e_r]>_beta,

for a probe term −f(t)e_r. The beta0 trace of a commutator vanishes. The beta1 coefficient is zero by the exact tracial mixed-correlation obstruction already established.

For A=C0(t), B=e_r, trace cyclicity gives exactly

    d/dt tr[H{A,B}]
      =i tr[H²[A,B]],
    tr[H²[A,B]]=−i d/dt tr[H{A,B}]=−2i F'_r(t).

Expanding the Gibbs numerator to beta² therefore yields

    chi_C,e(r,t)=beta² theta(t) F'_r(t)+O(beta³).

Partition-function normalization contributes nothing at this order because the lower commutator coefficients vanish. The sign is positive in front of F', agreeing with the root. The minus sign from the previous beta1 autocorrelation formula must not be reused here.

Since F(t)=F0+t²F2/2+..., the first time term in the beta² coefficient is

    chi_C,e(r,t)=beta² theta(t) K^4 t
                   [−48 delta_(r,0)+4 1_(r face diagonal)]
                   +O(beta² t³)+O(beta³),

where the last remainder is understood at fixed t. The exact reflection symmetry makes this mixed retarded response even in beta when its Gibbs expansion is analytic, so O(beta³) is conservative; no odd-beta term is needed. No numerical finite-beta/time validity window has been certified by these coefficients alone.

The K power is K^(n+2) in F_n: one K from H, one from e, and n from D^n. Thus F2 carries K^4 and F0 carries K². C is the unscaled distance-two Pauli pair sum throughout.

## Uniform energy conservation

Sum_r e_r=H. For n>=1,

    sum_r F_n(r)=tr[H² D^n C0]=0,

by trace cyclicity and commutation of H² with H. The observed order2 sum is −48+12*4=0; all computed higher positive orders also sum to zero. F0 instead sums to6K², consistent with tr(H² C0).

More strongly, in any stationary Gibbs state,

    sum_r chi_C,e(r,t)=i theta(t)<[C0(t),H]>_beta=0

exactly at every time, since the density matrix commutes with H. A spatially uniform probe −f(t)H only rescales the closed-system Hamiltonian; an equilibrium state remains stationary under that change. The q0 dynamical null is not a failure of the local finite-q coefficient.

## Equilibrated static response is different

A bath-maintained, isothermal equilibrium derivative under H->(1−f)H is generally nonzero: it changes the Gibbs parameter to beta(1−f). For a local C0,

    d< C0 >/df |_0 = −beta d< C0 >/d beta
                    = beta Cov_beta(C0,H).

Here <C0>_beta=3 beta² K²+O(beta³), because tr(H C0)=0 and tr(H² C0)=6K². Thus the isothermal uniform derivative starts at −6 beta² K², while the isolated q0 retarded response remains exactly zero. This difference is the equilibration/ensemble distinction, not an inconsistent sign or normalization.

The finite-q retarded coefficient is an explicit response channel within the supplied interacting compass Hamiltonian and supplied thermal preparation. It does not add a microscopic interaction, identify a physical temperature, establish a scalar pole, or connect to cosmological/observational calibration.
