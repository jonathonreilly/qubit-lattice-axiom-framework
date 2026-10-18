# Neutral free-band spectra: positive measures, moments and single-energy tests

Scope: fixed number-conserving quadratic H, a specified stationary state/ensemble, and a declared neutral bilinear probe. No microscopic interaction or scalar identification is inserted. These statements do not exclude exact flat-band transitions or closed-operator exceptions.

## Conventions and momentum orientation

Let

    H=sum_k c_k^dagger h(k)c_k,
    O_q=sum_k c_(k+q)^dagger M_q(k)c_k,
    N_c=number of original cells.

Diagonalize h(k) with eigenvectors |u_nk>, energies epsilon_nk. Define

    B_mn(k,q)=<u_m,k+q| M_q(k) |u_nk>,
    Delta_mn(k,q)=epsilon_m,k+q−epsilon_nk.

For a Hermitian real-space probe, O_q^dagger=O_(−q) requires

    M_(−q)(k+q)=M_q(k)^dagger.

O_q at nonzero q need not itself be Hermitian. Never silently replace the −q channel by q unless a symmetry actually identifies their spectra.

Use delta functions normalized to integrate to one; thus structure factor is the Fourier transform divided by 2pi. Set hbar=1. The connected dynamic structure factor is

    S_q(omega)=(1/N_c) sum_if p_i |<f|delta O_q|i>|²
                                  delta(omega−[E_f−E_i]),
    delta O_q=O_q−<O_q>.

It is a nonnegative measure on the full real frequency axis. In a stationary pure ground state it has no negative-frequency support. Subtracting the mean removes its disconnected elastic contribution but need not remove every zero-energy transition within a degenerate eigenspace.

## Free quasifree ensemble formula

For a stationary grand-canonical quasifree state with occupations f_nk,

    S_q(omega)=(1/N_c) sum_kmn
        f_nk [1−f_m,k+q] |B_mn(k,q)|² delta(omega−Delta_mn).

This is the connected Wick formula; add |<O_q>|² delta(omega)/N_c if using the unconnected definition. At zero temperature with a specified Slater ground state, only occupied-to-empty transitions remain. In a finite-size fixed-number thermal mixture or parity-projected ensemble, unrestricted Wick factorization is not automatic: use the many-body spectral definition or the correct joint occupation probabilities. Quadratic dynamics alone does not make an arbitrary state quasifree.

Normalize per original cell, including any supercell factor. If a supercell contains r original cells, a momentum average whose weights sum to one is multiplied by 1/r, not by one. Count each actual orbital/band degeneracy once.

## Retarded spectral weights and finite temperature

Choose the retarded correlator

    chi_q^R(t)=−i theta(t) <[delta O_q^dagger(t),delta O_q(0)]>/N_c.

With Fourier factor exp(+i omega t), its spectral representation is

    chi_q^R(omega)=(1/N_c) sum_if
        (p_i−p_f)|<f|O_q|i>|² / [omega−(E_f−E_i)+i0].

For the free thermal state this is

    chi_q^R(omega)=(1/N_c) sum_kmn
        [f_nk−f_m,k+q]|B_mn|²/[omega−Delta_mn+i0].

Accordingly rho_q(omega)=−Im chi_q^R(omega)/pi. It is nonnegative at omega>0 in equilibrium, nonpositive at omega<0; it is not a positive measure over all frequencies. Define J_q as its restriction to strictly positive frequencies.

For a thermal equilibrium state and a number-conserving O_q,

    S_(−q)(−omega)=exp(−beta omega) S_q(omega),
    rho_q(omega)=[1−exp(−beta omega)] S_q(omega).

The first relation uses O_(−q)=O_q^dagger; without that identification write S_(O_q^dagger)(−omega). Chemical potential cancels because O_q conserves number. At T=0 with a ground-state ensemble, J_q=S_q on strictly positive frequencies. At finite T they differ by the displayed thermal factor.

A zero-frequency thermal covariance can appear in S_q while disappearing from the retarded commutator spectrum. Do not divide by 1−exp(−beta omega) at omega=0 and claim to recover that elastic weight. The isothermal static susceptibility can contain a separate zero-frequency population contribution not obtained by a naive isolated dynamical limit.

## Zeroth, first and second moments

For the full connected structure-factor measure define

    mu_n=integral_(all frequencies) omega^n S_q(omega) d omega.

Let L X=[H,X]. For a stationary state [rho,H]=0,

    mu_0=<delta O_q^dagger delta O_q>/N_c,
    mu_1=<delta O_q^dagger [H,delta O_q]>/N_c,
    mu_2=<[H,delta O_q]^dagger [H,delta O_q]>/N_c.

More generally mu_n=<delta O_q^dagger L^n delta O_q>/N_c. The second-moment identity uses stationarity and cyclicity. The Liouvillian is self-adjoint under (A,B)_rho=Tr(rho A^dagger B) on its supported operator space.

For the free Wick formula the corresponding moments are simply

    mu_n=(1/N_c) sum_kmn f_nk(1−f_m,k+q)|B_mn|² Delta_mn^n.

For strictly positive retarded spectral moments define instead

    R_n=integral_(0,infinity) omega^n J_q(omega)d omega
       =(1/N_c) sum_(k,m,n:Delta>0)
          [f_nk−f_m,k+q]|B_mn|² Delta^n.

These are nonnegative-weight moments; they are NOT generally the same as mu_n or full-axis retarded moments. At zero T with no elastic weight they coincide with the ground-state structure-factor moments. At finite T the positive-frequency selection and thermal factor must remain explicit.

The full-axis retarded first moment can be expressed by a double commutator. With the above conventions,

    integral_(all omega) omega rho_q(omega)d omega
        =<[O_q^dagger,[H,O_q]]>/N_c.

For a Hermitian probe this equals twice the full structure-factor first moment in a stationary state; for general q it combines the q and −q structure-factor first moments. Do not insert a factor two into one channel without verifying the relevant symmetry.

## Exact single-energy criterion

For any nonnegative spectral measure with finite mu_2 and mu_0>0, define

    bar_omega=mu_1/mu_0,
    variance=mu_2/mu_0−bar_omega²
            =(1/mu_0) integral (omega−bar_omega)² S(omega)d omega >=0.

Variance is zero **if and only if** that measure is supported at one energy bar_omega (up to null weights). Zero total weight makes the normalized variance undefined; it is not evidence for a mode.

For a specified pure energy eigenstate |i>, using an unconnected or correctly connected O as chosen,

    variance=0 iff (H−E_i−bar_omega) delta O_q|i>=0,

provided delta O_q|i> is nonzero. Thus the probe-created vector lies entirely in one eigenspace. Degeneracy within that energy is allowed. If the state is not an energy eigenstate, this vector formulation needs replacement by the stationary mixed-state Liouvillian statement below; do not assign one E_i to a mixed ensemble.

For a stationary mixed state and the full positive structure-factor measure,

    variance=0 iff ([H,delta O_q]−bar_omega delta O_q) rho^(1/2)=0.

This follows because the numerator is the squared Hilbert-Schmidt norm of that operator, divided by N_c. It constrains transitions from every state with nonzero statistical weight. At positive temperature with full-rank rho it is a global operator eigenrelation; in a restricted ground-state sector it is only a supported relation.

The same measure theorem applies to R_n and J_q, but then it says only that **positive-frequency commutator weight** has a single energy. It says nothing about negative-frequency or zero-frequency structure-factor transitions. It is incorrect at finite T to turn variance(J_q)=0 into the assertion that O_q acting on every thermal state has just one energy difference.

A strictly positive variance rules out 'all this probe's weight is a single pole'. It does **not** rule out an isolated pole plus a continuum. Conversely, a small variance does not prove a pole: a narrow continuum can have arbitrarily small variance. The exact bound

    weight(|omega−bar_omega|>=delta)/total_weight <= variance/delta²

quantifies concentration but not isolation.

## Operator closure as a strong check

For the bilinear probe,

    [H,O_q]=sum_k c_(k+q)^dagger
          [h(k+q)M_q(k)−M_q(k)h(k)] c_k.

A sufficient global condition for one energy difference is

    h(k+q)M_q(k)−M_q(k)h(k)=omega_q M_q(k)

for all k, with omega_q independent of k and nonzero spectral weight in the specified state. A ground-state-supported condition can be weaker: the equality need hold only on the occupied-to-empty matrix elements that actually carry weight. Exact parallel/flat band differences and symmetry-generated ladder operators can meet such conditions in a free theory. They must not be excluded in advance.

At q=0 the total density has M=I, so [H,Nhat]=0. Its dynamical commutator spectrum is zero. Its connected finite-T grand-canonical structure factor can have an elastic Var(Nhat) delta(omega), while in a fixed-N state that connected weight vanishes. An elastic conserved quantity is not a finite-frequency propagating scalar excitation.

## A rigorous useful discriminator for the actual lattice

1. Specify the state/ensemble, filling, operator, cell normalization and q. Compute the full band-transition weights, not just energies near a selected cone.
2. Independently check zeroth/first/second moments by the operator formulas; this catches missing bands, occupation factors, q orientation and normalization errors.
3. Separate elastic weight. Test whether a nonzero inelastic positive measure has exactly zero variance, or exhibit an analytic nonzero variance/failed supported closure. Numerical near-zero needs precision/error control, especially at degeneracies.
4. If variance is positive, separately test for an isolated component rather than declaring that no pole exists.
5. For a thermodynamic isolated free mode, establish a delta-function component with nonvanishing normalized weight and a spectral gap to all other supported transitions on an open q region, with bounds uniform in system size. Alternatively prove an exact closure/constant-transition-energy relation. A finite momentum grid produces discrete poles automatically and proves neither delta weight nor spectral isolation in the continuum limit.
6. For a scalar-like candidate also check its spatial symmetry, dispersion, residue, finite-q persistence, and how the microscopic observable couples to matter. This identifies a free neutral mode at most; it does not establish universal conformal coupling, nonlinear self-consistency, a gravitational role or the environmental-to-cosmological bridge.

No additional interaction is needed to run these discriminators, and no blanket free-mode prohibition is used.
