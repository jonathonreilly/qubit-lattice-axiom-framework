# Independent review of the generic finite-channel packet bridge

**Disposition: no blocking mathematical finding for the stated conditional theorem.** The all-future half-line bound (33), and the finite-support and finite-horizon extensions, follow under the supplied finite-matrix, channel-gap, uniform inverse and phase certificates. I reconstructed the load-bearing estimates below rather than treating the companion algebra check as a proof of the theorem.

This disposition concerns a conditional mathematical model. It does not certify any concrete scattering fit, interval, readiness implementation, strict two-body hardware, arbitrary-accuracy family, or retained status. No result from my separate capped-point search is used as a premise here.

## Source and coverage

The complete **599-line** [THEOREM.md](sources/THEOREM.md) was read at SHA256:

~~~
fffd7d405935226aba4a5e6528112b984b6dde4580747641159f554e97e2189a
~~~

Its original path is /Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261016_230727/finite_channel_wavepacket_bridge/THEOREM.md. All line references below refer to that pinned version. The complete companion column_norm_check.py, launcher, stdout/stderr, receipt and manifest were also read and frozen in sources/; identities are in [SOURCE_PINS.json](SOURCE_PINS.json).

The necessary mathematical premises are explicit within the note: finite selfadjoint \(B,V_0,V_1\); an isometric source-vacuum embedding; actual asymptotic eigenvalues \(b_j\); exactly reducing projections; one common compact kinetic interval inside \((0,\pi)\); one open channel per relevant block and incident energy; a positive uniform closed-channel gap; a positive uniform smallest singular value of the actual matching matrix; and a common-phase target certificate. Literal old aging additionally requires (4). The earlier one-channel notes are declared contextual, not imported terminal lemmas. I did not independently re-review them or rely on them: the current note rederives the needed arguments.

The physics claim reviewer skill and necessary proof-search/focused-review instructions were read from the identified local correlation_worktree methodology snapshot, associated with c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc. Exact path hashes are recorded. The workflow identity reused from the campaign is 71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3. No network freshness claim is made. The explicit inherited-model/effort instruction controls over the skill's older default; no override or delegation was used.

## One nonblocking clarification

At lines 59–61, \(v\) equals \(\min_I E'\), while lines 219–220 say that \(k_0=\pi/2,\ \sigma\le\pi/6\) permits \(v=\sqrt3J\). For \(\sigma<\pi/6\), the exact minimum is \(2J\cos\sigma>\sqrt3J\). Every estimate remains valid with the conservative lower bound. A narrow clarification is to define **any certified \(0<v\le\min_I E'\)**, or say “one may replace \(v\) by the lower bound \(\sqrt3J\)” in the example. This is a notational inconsistency, not a failure of the advertised bound or a reason to defer the conditional theorem.

## Reconstructed mathematical checks

### Matching, convention, derivative bounds and flux

Lines 100–175 are consistent with the full half-line recurrence. There are \(2d+1+(d-1)=3d\) unknowns. With \(z=e^{ik}\), the open recurrence at site 2 reduces to

\[
 (z+z^{-1})(z^{-2}+r z^2)-(z^{-3}+r z^3)=z^{-1}+rz.
\]

The closed recurrence gives \((q+q^{-1})\alpha-q\alpha=q^{-1}\alpha\). These are exactly the third line of (11), including its incoming term and closed-root exponent. The first two rows enforce the interaction sites. The free entrance condition is \(z+r/z=0\), so \(r_0=-z^2\), matching (7) and (30).

From \(|s|\ge2+g/J\), the chosen root is real, nonzero and uniformly inside the unit disk. Differentiating \(q+q^{-1}=s\), with \(s'=-2\sin k\), gives the stated \(q'=2\sin k\,q^2/(1-q^2)\) and \((q^{-1})'=-2\sin k/(1-q^2)\). Both root signs are covered; the gap prevents a branch change.

The combined \((x_0,x_1)\) derivative-input group has norm bound \(2J\), because that derivative map is block diagonal. The \(r\) column has norm \(\sqrt5J\), and the \(\alpha\) group has norm at most \(2J/(1-\kappa^2)\). Cauchy–Schwarz over these groups gives \(J\sqrt{4+5+4/(1-\kappa^2)^2}\), exactly (13). The right-hand side and its derivative have norms \(\sqrt2J\) and \(\sqrt5J\). Then \(z'=M^{-1}(d'-M'z)\) proves (14) from the uniform inverse certificate. A central inverse or nonsingular grid would not suffice; the note correctly demands more.

The entrance current vanishes because the site-0 equation has a selfadjoint diagonal matrix. The recurrence conserves it. Orthogonality of internal eigenvectors removes cross-channel terms, and real closed roots contribute no imaginary current. The open contribution is \(2J\sin k(|r|^2-1)\), proving \(|r|=1\). No fitted modulus normalization or missing velocity ratio appears.

### Entire localized output and its derivative

At site 0, \(\|c_0\|\le X_0+2\) and \(\|c'_0\|\le2X_1\). At site 1 the corresponding bounds are \(X_0+2\) and \(2X_1+2\); the latter 2 counts both differentiated plane waves. Orthogonality of the closed internal vectors gives

\[
 \sum_{\ell,m\ge0}|\alpha_\ell|^2|q_\ell|^{2m}
 \le \frac{\|\alpha\|^2}{1-\kappa^2}.
\]

The differentiated coefficient tail is bounded by \(X_1/\sqrt{1-\kappa^2}\), and the differentiated root tail by
\[
 X_0Q_1\sqrt{\frac{1+\kappa^2}{(1-\kappa^2)^3}}.
\]
Adding the finite-site and tail bounds proves (17). The uniform geometric majorants justify differentiation in the \(\ell^2\) norm. Thus \(C_j\) includes every interaction-site amplitude and closed-channel tail; no source output is discarded. The no-closed-channel convention at line 163 consistently deletes these tail terms.

### Packet estimates and column operator norms

Integration by parts gives
\[
 |a_u(n)|\le
 \frac{F_1+(E_2/v)F_0}{\sqrt{2\pi}(n+vu)}.
\]
For the reflected wave replace \(F_1\) by \(F_1+L_jF_0\). Zero traces of \(f\in W^{1,1}_0(I)\) remove endpoint terms. For \(a=vu\ge1\),
\[
 \sum_{n\ge0}(n+a)^{-2}\le a^{-2}+a^{-1}\le2/a,
\]
which proves (21), including its \(\pi\) factor. The parabolic packet has the normalization and \(F_0,F_1\) in (18).

The localized Bochner integral obeys
\[
 \left\|\frac1{\sqrt{2\pi}}\int fC_j e^{-isE}\,dk\right\|
 \le
 \frac{F_1C_{0,j}+F_0C_{1,j}+(E_2/v)F_0C_{0,j}}
 {\sqrt{2\pi}\,v|s|}.
\]
The \(E_2/v\) inside the numerator comes from differentiating \(1/E'\); the outer factor is \(1/(v|s|)\). Both are correctly present.

Within each reducing block, a Hilbert–Schmidt estimate gives \(\sqrt{\sum_jD_j^2}\), because localized error columns may align. Distinct blocks have orthogonal input and output subspaces, giving the maximum of the group bounds. In contrast, the open columns \(b_s^j\otimes u_j\), and the phase-mismatch columns in (31), are orthogonal. The uses of a maximum in (21)/(31) and the grouped square sum in (22) are correctly distinguished. The companion example addresses this risk without purporting to prove the scattering theorem.

### Exact isometry and full old aging

The open synthesis maps are Fourier restrictions with bounded energy multiplier \(E(k)+b_j\). The localized synthesis is a bounded Bochner integral with that bounded multiplier. Hence each full stationary packet is strongly differentiable in \(\ell^2\), and the coordinate recurrence proves \(i\partial_s\Psi_s=H\Psi_s\). Bounded selfadjointness gives (24), without any scattering-completeness assumption.

The full-line incoming wave has norm 1 by Parseval. At time \(-T\), its negative-site tail is nonstationary and tends to zero, so its half-line norm \(A_T\) tends to 1. The reflected and localized incoming errors vanish in operator norm by (21)/(22). Thus \(\Gamma_{-T}^*\Gamma_{-T}\to I\). Meanwhile \(\Psi_s^*\Psi_s\) is constant. The factors \(e^{iTD_b}\) are unitary, so the norm distance of this constant Gram matrix to \(I\) tends to zero. This proves exact isometry (25) for every \(s\).

Error columns are not silently assumed orthogonal in this argument; their full operator error has already been bounded by the grouped \(D\). There is also no missing density-of-states factor: integration uses common kinetic momentum \(k\), and normalization is derived from the unit incoming coefficient and Parseval.

The exact aging identity follows from
\[
 \Psi_{-T}=\Gamma_{-T}e^{iTD_b},\quad
 \Psi_s=\Gamma_s e^{-isD_b}
 \quad\Longrightarrow\quad
 e^{-i(T+s)H}\Gamma_{-T}=\Gamma_s e^{-i(T+s)D_b}.
\]
This preserves the full elapsed time \(t=T+s\), even when the interactions do not commute with \(K\). If (4) holds, \(D_b=K+b_\Omega I\) in the selected basis and the diagonal \(S\) commutes with \(K\). Equation (34) retains both \(e^{-itK}\) and \(e^{i\gamma-itb_\Omega}\). No scalar in the actual \(b_j\) may be deleted when identifying \(b_\Omega\). The free reflection phase and positive-real clock normalization are explicit; no input-dependent global phase is used.

### Preparation, complete-output error and bound states

The difference between \(\Gamma_{-T}\) and \(a_{-T}\otimes\iota\) is at most \(\delta_{\rm in}\). Exact isometry and reverse triangle inequality imply \(|A_T-1|\le\delta_{\rm in}\). Normalizing the common clock costs this amount again, proving (29).

The free packet \(a_s+b_s^0\) has norm 1 by the same normalization argument, or by the sine transform. Normalizing \(b_s^0\) therefore costs at most \(\|a_s\|\). The future comparison pays one incoming-wave term, one clock-normalization term, the full localized term and phase mismatch. This proves (32), then (33) by propagation of (29) and exact aging. The final \(3D\) is \(2D\) from preparation plus \(D\) from the future localized component.

The time prescription (35) is sufficient: its second and third entries bound the escape terms by \(\epsilon_e/2\) each; its fourth and fifth bound the two parts of \(\delta_{\rm in}\) by \(1/8\) each. Its second entry also ensures the outgoing norm lower bound.

At every fixed clock coordinate the incoming packet at \(-T\) tends to zero by nonstationary phase. The reflected and localized pieces vanish in norm. Bounded packet norms extend this to weak convergence against all \(\ell^2\) vectors; a column phase \(e^{iTb_j}\) preserves that convergence. The magnitude of the overlap with any bound eigenvector is constant under (24), hence must vanish. Thus \(P_{\rm pp}\Gamma_{-T}=0\), and (29) proves (36). Neither completeness nor absence of bound states is required. The note correctly treats this bound-state amplitude as already included in the preparation error and restricts the claim to the infinite apparatus.

Tensoring a passive reference preserves every operator bound. For the complete-output isometries \(U,V\), splitting \(U\rho U^*-V\rho V^*\) into two terms gives \(2\|U-V\|\), capped at 2, for every normal input density. No source trace or postselection enters.

### Finite support and finite horizon

For \(n>2JT\), the preparation phase derivative has magnitude at least \(n-2JT\), and its second derivative is bounded by \(2JT\). This yields line 445. With \(d=N-2JT\ge\max(1,2JT)\), each coefficient is bounded by \((F_1+F_0)/[\sqrt{2\pi}(n-2JT)]\); the reciprocal-square sum proves (39). Formula (40) gives discarded norm at most \(\eta_p/4\). Normalization costs at most \(2(\eta_p/4)/(3/4)=2\eta_p/3\le\eta_p\), and the retained norm is at least \(3/4-1/8=5/8\). This remains a common product preparation, with uniform propagated error. Any additional \(\eta_a\) must be an actual preparation-isometry error in the appropriate infinite or embedded finite output space; no native emission algorithm is supplied.

The enclosure in (41) follows from \(0\le h_0\le4J\), the spectral bounds on \(B\), and perturbation norm \(\max(\|V_0\|,\|V_1\|)\) from their disjoint clock supports. Both centered, scaled Hamiltonians are selfadjoint contractions. The finite compression retains diagonal \(2J\) at the final site; the stated positive-bond endpoint adjustment is consistent.

Starting on sites \(0,\ldots,N-1\), reaching site \(M\) takes \(d_M=M-N+1\) hops. Diagonal and internal terms cannot shorten it. Polynomial actions agree for degrees \(k<d_M\). The Chebyshev expansion contributes a factor 2, and the difference of two contraction images another factor 2, producing the factor 4 in (42). From the generating function on \(|z|=e^\mu\),
\[
 |J_k(x)|\le e^{-\mu k+x\sinh\mu},\qquad x\ge0.
\]
The geometric sum gives (42), and (43) makes it at most \(\zeta\) throughout the specified horizon. The proof uses the full \(B,V_0,V_1\), with no old-\(K\) factorization. Its comparison with a half-line target after embedding the finite output is explicit. It does not claim persistent accuracy for a fixed finite clock beyond that horizon.

## Executable checks and limits

[checks.py](checks.py) performs exact local calculations with SymPy:

- Reconstructs the bulk-to-matching recurrences and free 3-by-3 solution. Substituting the wrong constant \(r_0=-1\) gives scaled entrance residual \(8i/5\), after dividing by \(J\), at \(z=(3+4i)/5\). Omitting the incoming third-row term leaves residual \((0,0,-J/z)\).
- Checks both closed-root derivative identities, the geometric derivative sum and the parabolic-packet constants.
- Applies the column-error example directly to an aligned normalized input: squared error \(4/5\) exceeds the individual-column value \(2/5\). This differs from the author's Gram eigenvalue computation.
- Uses \(B=\operatorname{diag}(1,3)\), \(J=1/4\), \(V_0=X/3\), \(V_1=Z/5\), with \([B,V_0]\ne0\). For \(N=2,M=4\), exact polynomial actions agree in degrees 0, 1 and 2. At omitted-hop degree 3, the scaled-power amplitude is \(-27/10648\), and the \(T_3\) amplitude is \(-27/2662\). An off-by-one extension of the equality is rejected.

The successful run used a **15 CPU-second / 30 wall-second cap**, maximum matrix dimension **14**, and exited 0 in **0.6858055843040347 seconds**. Python was 3.13.5 and SymPy 1.14.0 on macOS 26.6.2 arm64. [EXECUTION.json](EXECUTION.json) records commands, source identities and output hashes. [check_stdout.json](check_stdout.json) is the complete output, including versions; stderr is empty.

An initial run exited 1 because a SymPy Kronecker product was immutable and the checker tried to edit it. Exact source, stdout/stderr and receipt are retained in attempt_1/. Converting that toy Hamiltonian to a mutable matrix fixed the harness; no theorem coefficient, assertion or target was weakened.

These executable checks do not numerically validate all future times or any concrete interval. Generalized-eigenfunction normalization, strong dynamics, operator estimates, bound-state treatment and the Chebyshev tail were checked analytically above. This is not proof-assistant verification and does not apply audit status. Concrete use still requires the note's listed obligations, particularly a common-band matching inverse and common-phase residual in the same reflection convention.

All writes are confined to this review directory. No source theorem, shared checkpoint, prompt, axiom, audit, Git state, PR or other chat was changed. No network calls or unrelated point-search reruns were made.
