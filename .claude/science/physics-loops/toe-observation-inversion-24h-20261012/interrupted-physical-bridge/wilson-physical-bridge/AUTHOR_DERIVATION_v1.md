# Author physical bridge: on-shell one-loop check and radiation formula

Working derivation, not an empirical exclusion. Target is TARGET.md. The direct on-shell algorithm was written and executed before the focused checker's first structural message. This text was frozen after that message; the final texts are not mutually blind. The raw numerical implementation and first result precede exposure and are retained.

## Coulomb and Feynman on-shell representations

Let h_p=d_p.Gamma, d_p=(sin p,m+W_p), E_p=|d_p|, n_p=d_p/E_p, with m>0 and a=w=1 at the expansion point. The external spin average is Tr(P_p X)/2. For q=p-k, link vertices are J_i=alpha_i cos(p_i-k_i/2)+beta sin(p_i-k_i/2). Write omega=|hat k|, hat k_i=2 sin(k_i/2), P^T_ij=delta_ij-hat k_i hat k_j/omega^2. The order-e^2 on-shell Hamiltonian shift is the sum of

T(p)=integral sum_i P^T_ii [-n_pi sin p_i+n_p4 cos p_i]/(4 omega),
C(p)=integral n_p.n_q/(2 omega^2),
X(p)=integral [S_plus/(E_p-E_q-omega)+S_minus/(E_p+E_q+omega)]/(4 omega),

all with measure d^3k/(2pi)^3. Define V_i=(cos(p_i-k_i/2) e_i,sin(p_i-k_i/2)), C_V=sum_ij P^T_ij V_i.V_j, b_pi=n_p.V_i, b_qi=n_q.V_i. Then S_plus=C_V(1-n_p.n_q)+2 b_p.P^T.b_q and S_minus=2C_V-S_plus. These follow from exact projectors and positive/negative occupied-band residues. The second transverse denominator is not discarded. The Coulomb exchange includes the filled-band and equal-time convention used in the previously checked mass calculation; changing normal-ordering would change the supplied action convention.

A separate Feynman-gauge representation uses all three spatial polarizations and subtracts the temporal identity current. Thus S_plus^F=2-4 n_p.n_q+2 sum_i b_pi b_qi and S_minus^F=4-S_plus^F. Its seagull replaces P^T_ii by1; it has no separate C. The two integrated on-shell answers should agree by the link Ward identity. At m=p=0 their scalar limit must reproduce C_W. Numerical agreement alone is not a gauge proof, but tests an independent frequency/residue representation of the physical projection.

Let dE(p) denote these coefficients with the overall e^2 stripped. Rest-mass calibration introduces delta m_bare=-e^2 dE(0) beta. Hence the remaining projected shift is

    dE_cal(p)=dE(p)-(m+W_p)/E_p dE(0).

In particular the additive critical mass cannot be inserted into an uncorrected free spectrum while keeping its self-energy scalar out. At fixed x=|p|/m and m->0, compute

    K(m,x)=[E_p dE(p)-(m+W_p)dE(0)]/|p|^2.

The initial x=2,m=.001,order16 cube-sector quadrature gives K=-.133086079429869 in Feynman and -.133086079429877 in Coulomb gauge. The two full shifts and rest shifts agree separately. A mass/quadrature sequence is running. This is an author synthetic calculation, not nature data, and the convergence target is the previously checked local Delta_f. A proof must control the Lorentz-invariant continuum remainder and analytic continuation, rather than using the numerical limit as that proof.

The formal local projection after photon normalization is delta c=e_R^2(Delta_f-Delta_gamma/2)+O(e_R^4) for a=1. Continuing the separately fixed bare curve a^2=1-m_bare through its critical mass adds e_R^2 C_W/2 to delta c at this order. The physical mass is calibrated, and e_R is the charge calibration; no relative-speed datum has been used. Gauge cancellation, charged-state infrared meaning, finite-cutoff corrections and higher-order bounds remain obligations. This formula alone is not an experimental prediction.

## Unstable local branch and width

For the conditional leading local EFT h=c alpha.p+beta M and omega=k (photon clock units), let c>1, delta=c^2-1, E=sqrt(M^2+c^2 p^2). The physical transverse vertex is c alpha.epsilon. The charged sector's lower spectral edge includes electron-plus-photon states; minimizing E(q)+|p-q| gives a photon-slope edge above p_*=M/(c sqrt(delta)). The high-energy electron-like branch is then unstable, not the lowest stable charged state.

For electron emission p->q=p-k, the exact local shell has

    z=cos(theta)=[E+delta k/2]/(c^2 p),
    0<k<K=2(c^2 p-E)/delta,

and exists iff p>p_*. Initial-spin-averaged, final-polarization-summed canonical golden rule gives

    dGamma/dk=alpha/[p E c^2] [B-E delta k+delta(c^2+1)k^2/4],
    B=c^2 delta p^2-M^2,
    Gamma=alpha/[p E c^2] [B K-E delta K^2/2+delta(c^2+1)K^3/12],
    Power=alpha/[p E c^2] [B K^2/2-E delta K^3/3+delta(c^2+1)K^4/16].

The current trace is 2c^2[1-(M^2+c^2 p_parallel q_parallel)/(E(E-k))]. Angular coarea has Jacobian (E-k)/(c^2 p k), giving the displayed normalization. As M/p->0 and delta->0 at fixed positive margin, Gamma~(2/3)alpha delta p and Power~(7/24)alpha delta p^2. The shell-derived closed expressions apply to the supplied local EFT at tree level; using delta generated at one loop is a reorganized expansion, with the omitted higher-order corrections still to be bounded. No all-orders physical survival theorem is asserted.

## Unresolved observational contract

Direct laboratory time-of-flight is a promising measurement because it avoids astrophysical source-lag assumptions. Its detector response and beam survival must nevertheless be modeled. Magnetic rigidity can calibrate momentum without E=p for an isotropic minimally coupled dispersion, but large lattice anisotropy and apparatus details remain relevant. The cutoff and lattice orientation are not calibrated by the preceding two constants. An arbitrary high-cutoff choice, truncation-error cap or stable-pole assertion cannot be silently used to claim the human target closed. Next: independently verify the on-shell continuum subtraction and radiation formulas, obtain the primary laboratory response and determine a defensible calibration region or state the remaining cutoff obstruction.
