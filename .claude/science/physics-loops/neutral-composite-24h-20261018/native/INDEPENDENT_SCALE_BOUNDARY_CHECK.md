# Independent overall-scale boundary check

The scaling argument is correct under its stated fixed-state and fixed-geometry premises. It does not establish a pole or a bulk gap.

Set hbar=1, H_J=J H_1 with J>0, rho_J=rho_1 as a dimensionless state (for Gibbs states this means beta_J J fixed), and A_J=J^a A_1, B_J=J^b B_1. Then A_J(t)=J^a A_1(Jt). With chi_AB(t)=i theta(t) Tr rho [A(t),B],

chi_AB(t;J)=J^(a+b) chi_AB(Jt;1).

Changing integration variable u=Jt in the Fourier transform gives

chi_AB(omega;J)=J^(a+b−1) chi_AB(omega/J;1).

The same formula holds at complex frequency z with Im z>0 and z/J on the right. In particular, fixed numerical broadening eta at different J does not compare the same dimensionless regulator: it must be scaled as eta/J. Static CC, Ce and ee limits scale respectively as J^−1, J^0 and J, only if the corresponding limits exist and are taken consistently. The probe source's units must track the observable to which it couples.

For a genuine pole with dimensionless dispersion Omega_1(q)^2=Delta_1^2+v_1^2 q^2+..., Omega_J=J Omega_1. Both the gap and lattice-coordinate velocity scale by J, so the associated continuum pole range v_J/Delta_J=v_1/Delta_1 is invariant. This is the range inferred from that pole approximation, not a general proof of the full spatial response's asymptotics when other singularities or channels contribute.

In an omega-squared denominator convention, CC susceptibility scaling gives a numerator proportional to J. For the chosen +i commutator convention and Fourier factor exp(i omega t), a positive spectral transition is written as 2 Delta |A_0n|²/[Delta²−(omega+i0)²]. Thus a positive numerator Z_1 can be used in

chi_CC ~ J Z_1/[J² Omega_1(q)²−(omega+i0)²].

If the denominator is instead (omega+i0)²−J² Omega_1², the residue carries the opposite sign. This is only a sign-convention clarification; the proposed J scaling is unaffected. A residue defined with a first-order omega−Omega denominator has different scaling, so specifying the omega-squared convention is essential.

With lattice spacing a_lat restored, physical velocity is a_lat J v_1/hbar and frequency gap J Delta_1/hbar. Their ratio is a_lat v_1/Delta_1. Reducing J at fixed a_lat therefore slows the signal and gap together without increasing its physical range. Holding the speed fixed while reducing J would require changing a_lat or dimensionless model/state data, violating the fixed-geometry/fixed-state shortcut; changing those data may be a legitimate separate hypothesis but is not a derivation from J alone.

Exact eigenvectors and equal-time dimensionless correlations do not change under positive global J rescaling when the same state is selected. Degenerate eigenstates still require a fixed selection prescription; one cannot silently switch within a degenerate manifold. At fixed physical temperature, beta J changes and a new state or phase can arise, outside this particular argument. An actually gapless model remains gapless for every positive J, and J=0 is a singular zero-dynamics limit rather than an established finite-speed massless mediator.

The note correctly avoids extrapolating the finite 27-site gap to the bulk. The outstanding requirements remain an established dimensionless long-range channel, physical clock/ruler identification, and an actual matter/environment coupling; global energy rescaling supplies none of these by itself.
