# Independent pre-exposure response check

This proof and executable stage used only the neutral contract, before any author SCALAR_RESPONSE or MATTER_CLOCK note/code/result exposure. Root remains author. This is a conditional mathematical and numerical equation check, not formal audit or observational validation.

The complete derivation is INDEPENDENT_PROOF_v1.md; DUST_SYSTEM_SUPPLEMENT_v1.md records the explicit physical velocity divergence and full equations. The gravitational normalization is declared M^2 R/2 because the neutral prose does not specify the coefficient of R. Translation is required if the author uses M itself for that coefficient.

The independently derived scalar/Hamiltonian elimination is

    chi_ddot+(3H-alpha v)chi_dot+(K^2+mu-alpha F)chi
      =(6M^2 alpha H+4v)P_dot
       +(2M^2 alpha K^2+6M^2 alpha H^2-alpha v^2-2F)P.

Here F=V_phi+rho A_phi, mu=V_phiphi+rho A_phiphi at fixed bare proper density, and r=A rho. The last coefficient may use Friedmann to become 2M^2 alpha K^2+2alpha V-2V_phi; the eliminated curvature is V_phiphi-alpha V_phi+r alpha_phi. This identity is necessary, not a full normal-mode solution or automatically a measured Yukawa pole.

With a^2 x_dot=grad U and theta=-K^2 U, proper bare-number contrast obeys delta_dot=-theta+3P_dot and theta_dot+(2H+alpha v)theta=K^2(P+alpha chi). Momentum is P_dot+HP=(v chi-rU)/(2M^2). The spatial trace follows from momentum, Euler and background equations, while the Hamiltonian residual propagates as C_dot+3H C=0 under the original coupled equations. Coordinate-number contrast shifts delta by 3P in both equations; it leaves the elimination identity unchanged.

The conformal potentials are Psi_J=P+alpha chi and Phi_J=P-alpha chi, hence slip=alpha chi/P where P is nonzero. Matter-clock conversion d tau=A dt gives damping 3H/A=3(H_J-alpha v/A), with eliminated curvature (mu-alpha F)/A^2. Actual perturbed proper clocks additionally carry the lapse. No minimum, static positive-dust Minkowski limit, chosen history, or empirical source supplier was imposed.

The independent executable passed 27 controls: direct metric determinant/wave variation, ADM spatial/extrinsic/energy variations, exact symbolic elimination and clock map, dust conventions and Hamiltonian propagation, followed by one finite double-precision rolling background with three modes and 35 saved epochs (105 mode epochs). The original scalar, continuity, Euler and momentum equations were integrated; the eliminated identity was checked as a residual, not used as the evolution law. The original Hamiltonian supplied initial density only. Maximum Friedmann and Hamiltonian residuals are 7.77e-16 and 3.79e-16; eliminated and matter-clock residuals are 9.56e-17 and 8.35e-17. These finite algebraic/ODE residuals are not observed or certified trajectory precision. The slip-ratio identity has a 4.10e-11 cancellation residual near small P; its large dynamic/proxy differences are not physical signal significance.

For a well-separated initial example k=0.5, P=-1.6e-5 and chi=1.05e-4 give slip=-1.68, while the naive fixed-bare static proxy is 0.07874474214079606. This full linear initial-value fixture shows that the static proxy is not an identity; it does not establish a physically realized background, stability, or empirical exclusion. The source inputs and all stdout/stderr are retained. No failed control or tool run occurred in this stage. Execution exit 0, 1.2100778752937913 seconds of a 120-second cap, bytecode disabled.

The next step is author-source correspondence after this freeze. All original proof, code, output and receipt bytes must remain immutable; any later finding belongs in a versioned supplement.
