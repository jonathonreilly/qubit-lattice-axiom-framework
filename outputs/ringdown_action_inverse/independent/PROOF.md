# Independent canonical derivation and correspondence

The complete canonical note, primary, helper, controls and cache were inspected. The formulas of the previously independent proofs below correspond to canonical equations1-13. The canonical unit makes the unsigned path-error integral explicit, distinguishes ideal continuum identities from finite-grid tests, preserves rest-linearization as a premise, and identifies the static derivative comparison as generator-side verification. No mathematical premise was silently weakened in integration.

The primary imports and executes both mathematical bodies directly; source hashing and output aggregation are new packaging. Four declared predicate strengthenings replace trivial literal/object comparisons with actual rank loss, integrated zero excitation, recomputed Q and differentiated conjugate-force transformation. AST-normalized comparison diffs are stored separately. They are representation evidence rather than proof.



# Independent derivation before implementation inspection

At a clamp, d/dt(T_xdot)-T_x+V_x+D_xdot equals k wddot -tau' wdot²/2 +U'+B'w+C'w²/2+nu wdot. Thus k' and M' vanish, and the negative inertia-gradient sign is required. Set w=w0+z with w0=-B/C. The linear coefficient is G=B'+C'w0. z=c exp(lambda t)+conjugate with lambda+lambda*=-Gamma, lambda lambda*=O. Squaring z gives mixed coefficient 2|c|²; squaring zdot gives mixed coefficient 2O|c|². Hence f=(G+nu lambda+k lambda²)c, h=(C'-tau'O)|c|²=tau O'|c|² and g=(C'-tau'lambda²)c²/2. The real cos/sin convention gives f=(a_cos-i a_sin)/2.

Linearization at a rest equilibrium, in independent x,w coordinates, gives hidden tau s²+gamma s+C and reciprocal off-diagonal N(s)=k s²+nu s+G in both equations. Coefficient gradients of kinetic/damping functions multiply background velocities and vanish. Schur elimination gives Z=P-N²/[tau(s-lambda)(s-lambda*)]. The residue is -N(lambda)²/[tau(2lambda+Gamma)]. Modulus of the complex square is |N|², so Kspec=|N|²/tau. Multiplying by h/|f|² proves Q=O' wherever N and c are nonzero. Analytic polynomial P cannot change this residue. Dynamic stiffness is crucial: its inverse has a different pole structure.

For Gamma>0, omega>0, the constant, fundamental conjugates, mixed real decay and second-harmonic conjugates have distinct complex exponents. A cubic output has exponents with real part -3Gamma/2 and frequencies ±omega,±3omega and cannot merge with the six included exponents. Quadratic output epsilon z² shifts h by 2epsilon|c|² without changing the equilibrium linear operator; its Q shift is 2epsilon/tau. Gamma=0 merges h with offset. N(lambda)=0 cancels the hidden pole; zero c kills extraction. These are genuine exclusions.

Time-origin changes multiply h and |f|² by exp(-Gamma t0). Observed X=g_x x+o_x, Y=g_R R+o_R gives Knew=|g_R/g_x|K and Qnew=|g_R/g_x|Q/g_R=Q/g_x only for positive product g_R*g_x. Hidden constant affine changes only reparameterize the action. A common time rescaling transforms O and Q by the same inverse-square rate factor; environment-dependent clocks need additional corrections.

For A=2lambda+Gamma, product perturbation gives |delta(A rho)| <=(2Lmax+Gmax)e_rho+Pmax(2e_lambda+e_Gamma)+(2e_lambda+e_Gamma)e_rho. Reverse triangle yields the K bound. D=|f|² has error <=2Fmax e_f+e_f²; N=Kh has error <=Kmax e_h+Hmax e_K+e_K e_h. True denominator lower bound and quotient subtraction yield equation10. Neither error independence nor stochastic interpretation is required. Bounds on true values and certified extraction errors are indispensable.

For interval width h and midpoint m, integrate |Q(x)-Q(m)|<=L|x-m| to get Lh²/4. Measurement errors integrate as h e_Q. Summing proves the integral envelope for ordered a<b; a reverse-oriented integral requires positive widths and orientation applied to the sum. No finite sample set supplies the missing Lipschitz certificate.

Necessary compatibility is not sufficiency, uniqueness, empirical validation or an action derivation. Reciprocity, single quadratic hidden mode, Rayleigh form, calibrated work coordinate/force and rest-equilibrium response are adopted. Arbitrary ringdown preparation does not remove linear-response preparation obligations. No material defect identified in the note before implementation inspection.


# Independent derivation before implementation

Let a=2lambda+Gamma, n=N(lambda). The parent residue is rho=-n²/(tau a). With f=nc and g=(C'-tau'lambda²)c²/2, S=-2a rho g/f²=(C'-tau'lambda²)/tau=O'+(tau'/tau)(O-lambda²). Q=O'. Since lambda=-Gamma/2+i omega and O=Gamma²/4+omega², L=O-lambda²=2omega²+iGamma omega is nonzero. Thus r=(S-Q)/L is real tau'/tau and cancels the complex preparation exactly, including its phase.

For w=v+F(x), wdot=vdot+F'xdot. Cross kinetic coefficient becomes k+tau F'; choose F'=-k/tau. The remaining visible kinetic coefficient is M-k²/tau. Rayleigh coefficients become nu+gamma F' and d+2nu F'+gamma F'², with gamma unchanged. V has new B=B+CF and U=U+BF+CF²/2. At fixed x, hidden equilibrium shifts by -F, yielding Gnew=G+CF'=G-Ck/tau. Hence Nnew=N-k(s²+Gamma s+O). Congruence preserves positive kinetic and positive-semidefinite dissipation matrices. Generalized visible force gains F' times the hidden Euler-Lagrange/Rayleigh equation, zero only for no hidden drive. The pole coupling and clamped observed coefficients are invariant.

In k=0 chart, any nonzero smooth n²=-tau a rho has a smooth square root on a connected interval; exactly two global branches. Real G,nu uniquely interpolate n at nonreal lambda: nu=Im(n)/omega, G=Re(n)-nu Re(lambda). Integrating r determines positive tau up to a constant; then C=tau O and gamma=tau Gamma. Full Z determines the real quadratic polynomial P, if it exists, and hence M,d,P0. Positivity is an independent constraint, not a consequence of pole fits.

Let equilibrium w0 satisfy w0'=-G/C and E'=R0. V=E+C(w-w0)²/2 yields B=-Cw0 and U=E+Cw0²/2. At equilibrium V_x=E', V_xw=-Cw0'=G and V_xx=E''+Cw0'²=R0'+G²/C. Thus static condition P0=R0'+G²/C is necessary and supplies exactly the missing curvature for sufficiency. It is equivalent to Z(0)=R0'. With c=f/n, h_pred=tau Q |f/n|²=h and g_pred=tau S (f/n)²/2=g. Full six-mode closure then reproduces each whole clamped force record, not just these coefficients. This constructs an action realizing the exact rest-response/clamped-ringdown surface. It says nothing sufficient about arbitrary imposed moving histories or models outside the class.

Uniqueness in the reduced chart follows: equal r implies constant tau ratio; n scales by its positive square root and a global sign; G,nu inherit that scale, while N²/tau fixes P. w0 and E leave translation and energy constants. Restoring arbitrary F returns kinetic-cross coordinate freedom. Environment-dependent hidden rescaling generally leaves the functions-of-x-only kinetic class and is not used.

For y=j(x), conjugate force R_y=R_x/j'. Linearizing at rest gives Z_y=Z_x/j'²-R0 j''/j'³. The extra term is analytic, so rho_y=rho_x/j'², f_y=f/j', h_y=h/j', g_y=g/j'. Since K_y=K/j'², Q_y=Q/j'; S_y=S/j'; L unchanged, r_y=r/j'. This holds also for orientation reversal. A force channel left untransformed is not work-conjugate.

Product telescoping bounds the complex numerator perturbation by twice the difference of expanded positive-radius products in (12). |delta(f²)|<=2Fmax e_f+e_f² and |f²|>=Fmin² give its quotient bound. |delta L|<=e_O+2Lmax e_lambda+e_lambda² then proves (13) with true |S-Q| bound and lower margin. No stochastic independence is used. Integrated log-inertia uncertainty uses the unsigned path integral of e_r (min to max endpoints), plus normalization and other calibration errors. Square-root comparison requires a consistent branch and nonzero |nhat+n|; otherwise a small squared perturbation can hide a branch flip.

No material mathematical defect identified before code inspection. Rest linearization, continuum functions, full rational/polynomial closure, signed physical port calibration and certificates remain premises.
