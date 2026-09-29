# Energy suppliers for the original cubic birth instrument

This route gives two concrete, differently scoped results. First, an exact original mark on **all prebirth inputs** cannot be implemented by an independent stationary apparatus using additive energy conservation and energy-invariant record readout. Second, a coherent, normalizable positive-energy battery gives an explicit approximation to the complete original **conditional first-event instrument**, with both marked-state and mean-energy error bounds. A time-independent one-shot Hamiltonian executes that approximation at a specified readout time. This does not construct the unchanged ongoing Poisson instrument or a spatially local supplier.

These are conditional model results. No carrier, battery, clock, coupling, quantum premise or energy interpretation is adopted as a native axiom, and no formal audit verdict is issued.

## Prior art and exact sources

The repository already contains the general energy-translation machinery, finite coherent ladders, supplied autonomous history clocks and finite-grid marked-process estimates. In particular:

- `FINITE_ENERGY_SUPPLY_FOR_MARKED_COLLISION_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md` constructs buffered positive finite ladders, an energy-conserving unitary lift, original-mark collision approximations, and a shared-battery composition identity.
- `AUTONOMOUS_FINITE_CLOCK_FOR_THE_ORIGINAL_REDUCED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md` supplies a positive time-independent program Hamiltonian, with global payload couplings and explicit finite-horizon error.
- `FINITE_AUTONOMOUS_MARKED_DYNAMICS_UNDER_GRID_OBSERVATIONS_BOUNDED_THEOREM_NOTE_2026-09-24.md` strengthens that finite-dimensional result to original binned marks and a fixed number of causal interventions. It explicitly excludes exact timestamps and irreversible flags.
- The September 7 shared-battery transport and local-quench finite-ladder notes distinguish a controlled battery from a freely evolving battery, and prove locality/energy-defect estimates for their particular native CAR carrier.
- The actual-cube apparatus-coherence and no-first-birth apparatus notes already study stationary-apparatus restrictions, counted coherence resources, and one-input state-preparation relaxations in the microscopic cube.

Thus neither “add a coherent battery” nor the generic lift/clock construction is novel here. The present work applies the covariance discriminator to the full original PR9345 common-limit marks using the independently checked Laurent compression. It also supplies an explicit state-class and energy-moment bridge for the **unbounded rotor** first-event operation; the landed finite-dimensional diamond bounds cannot simply be asserted for that carrier.

The sources above were read at refreshed main `e75578f7136401d4bd750131671aed9212c06291`; working bytes matched. The selected campaign procedural base is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`, not a claim about working HEAD. The independently reconstructed input packet is `../independent-birth-energy-check/`, with its coefficients and source identities frozen in this route's `SOURCE_IDENTITIES.json`. That packet bound the actual PR9345 head `fe51bf1728b625dc0133256f43e7783afb11f7d8`, not a proxy. The compression and prebirth geometry can also be derived self-containedly from the landed common-law/pair-form definitions and explicitly supplied Ω; no PR band or record-response theorem is used below.

## Model and stationary-apparatus discriminator

Keep the supplied finite even torus (L\ge24), (N=L^3/2), integer rotors, hard-core charges, physical Gauss law, all-A-occupied P space, and

\[
h=KD+\delta H_4,\qquad
H_4=-2\sum_{\{a,c\}:d(a,c)=2}(F_cF_aP)^*(F_cF_aP),
\qquad B_{ab,\sigma}=Pj_{ab,\sigma}F_aP.
\]

The coherent original mark is the unnormalized (B_{ab,c}=B_{ab,+}+B_{ab,-}). Let (h_{\rm in}) be h on the prebirth sector, (h_{\rm out}) h on the full one-pair sector, and (n_\pm=5,n_c=10). The exact identity (B_m^*B_m=n_mI) holds on all prebirth rotor inputs.

The discriminator assumes all of the following, rather than deriving them:

1. The apparatus is initially independent of the system and its full initial state satisfies ([\sigma_R,H_R]=0). Every clock, program or phase reference is counted in R.
2. Its unitary strongly commutes with the **additive** endpoint energy (h+H_R).
3. Each fixed mark's readout effect commutes with apparatus energy; time translation does not relabel the mark.
4. Its selected reduced CP map equals a nonzero scalar multiple of (B_m\rho B_m^*) on every prebirth input, not merely on Ω or on its actual waiting-time orbit.

Commuting the total time-translation unitary through the apparatus evolution, stationary initial state, readout and partial trace proves covariance of each marked map:

\[
\mathcal J_m(e^{-ith_{\rm in}}\rho e^{ith_{\rm in}})
=e^{-ith_{\rm out}}\mathcal J_m(\rho)e^{ith_{\rm out}}.
\]

Two nonzero one-Kraus maps agree on all inputs only when their Kraus operators differ by a scalar phase. Hence continuity and the time-translation group law imply

\[
e^{-ith_{\rm out}}B_m e^{ith_{\rm in}}=e^{-i\omega_mt}B_m,
\qquad
h_{\rm out}B_m-B_mh_{\rm in}=\omega_m B_m.                 \tag{1}
\]

The generator equation is interpreted on the finite-field core, and on the mapped energy domain when extended. Multiplying by (B_m^*/n_m) gives the necessary scalar compression

\[
G_m:=\frac1{n_m}B_m^*h_{\rm out}B_m-h_{\rm in}=\omega_mI. \tag{2}
\]

This is stricter than a positive mean-energy cost on one input. An arbitrarily energetic but stationary reservoir does not evade covariance.

## Exact failure of that necessary condition

The checked compression is

\[
G_m=K\Delta D_m+\delta A_m,
\]

where \(\Delta D_m\) is diagonal in the prebirth integer-field basis and (A_m) is the complete magnetic Laurent polynomial, including every coherent interference term. Let z have the four A-to-B edge coefficients

\[
\begin{array}{c|r}
((-2,0,0),(-2,-1,0))&-1\\
((-2,0,0),(-1,0,0))&+1\\
((-1,-1,0),(-2,-1,0))&+1\\
((-1,-1,0),(-1,0,0))&-1.
\end{array}
\]

It is a nonzero divergence-free elementary circulation. For **each** original minus, plus and coherent mark on ((0,e1)), the full polynomial has (c_{m,z}=2/5). Therefore

\[
\langle z|G_m|0\rangle=\frac25\delta\ne0.              \tag{3}
\]

The electric term cannot cancel this off-diagonal element, for any (K>0). Equivalently the normalized physical finite-field states
\(\psi_\pm=(|0\rangle\pm|z\rangle)/\sqrt2\) have compression expectations differing by (4\delta/5), although their electric-field probability distributions agree. Equations (2)-(3) refute the stationary class for every original mark when (\delta>0).

The check reads the provisional independently reconstructed coefficient file and verifies this exact coefficient for all three marks using fractions. It does not fit a frequency from a mean, neglect the electric gate, or infer an intertwiner from unavailable inverse operators.

The scope is essential: this does not rule out matching only Ω's orbit, an initially correlated apparatus, nonstationary coherent resources, an energy-sensitive/noninvariant readout, or a different total energy with a changing interaction-energy contribution. It is not an exhaustive supplier no-go.

A stationary implementation can instead resolve energy-transfer frequencies and then hide that extra label. In a finite spectral comparator, this replaces (B\rho B^*) by \(\sum_\omega B_\omega\rho B_\omega^*\), deleting the cross-frequency terms. Keeping the same printed mark name does not restore those terms. In fact its first loss can still equal (n_mI), so correct first rates alone would not verify the original instrument. For the actual unbounded rotor, such spectral formulas need their spectral-integral meaning; no discrete Bohr expansion is assumed without justification.

## A coherent battery for the original conditional first event

Let the output include one zero-energy label for each **original** mark. Define

\[
W=\frac1{\sqrt{60N}}\sum_m B_m\otimes|m\rangle,
\qquad W^*W=I.                                         \tag{4}
\]

Dephasing only the original mark label gives the complete conditional first-event instrument: resolved labels have probability (5/(60N)), coherent labels (10/(60N)). In the coherent case the two sign amplitudes stay together inside (B_m). The factor in (4) is the original conditional-event normalization, not a changed jump rate. This construction by itself does **not** supply the rate (60\kappa N) or a waiting-time clock.

Start with an auxiliary energy line (L^2(\mathbb R,dE)), (H_R=E), and (T_u\beta(E)=\beta(E-u)). The standard spectral lift, understood through its bounded Fourier fibers, is

\[
\widetilde W=\iint P_{\rm out}(d\epsilon')W P_{\rm in}(d\epsilon)
                      \otimes T_{\epsilon-\epsilon'},
\qquad
\widetilde W(\tau)=e^{-i\tau h_{\rm out}}W e^{i\tau h_{\rm in}}.
                                                               \tag{5}
\]

The fibers are isometries. With Fourier convention (e^{i\tau E}), (H_R=-i\partial_\tau); differentiation shows that (5) strongly intertwines total additive energy. Its reduced channel is the integral of the original isometry conjugated by these energy phases, weighted by (|\widehat\beta(\tau)|^2). This is a coherent-resource construction, not a stationary reservoir and not a secular decomposition into additional measured marks.

The uncapped line is only an intermediate construction, since its energy is unbounded below. The positive cap below removes that defect at a quantified error. A formal zero-width Fourier packet at \(\tau=0\) would reproduce W exactly, but corresponds to a nonnormalizable energy reference. No finite sine packet is relabeled as that ideal state.

## Uniform bounds for the actual unbounded rotor inputs

Let \(\phi_s=e^{-ish_{\rm in}}\Omega\). The bounds below hold for all real s, and hence all physical first waits (s\ge0). The checked prebirth geometry gives

\[
h_{\rm in}=KD-618\delta NI+\delta V,\quad
\|V\|\le24N,\quad
\|V\Omega\|^2=48N,
\]

so, by conservation of the graph norm of (KD+\delta V\),

\[
K\|D\phi_s\|\le\delta\sqrt{48N}+24\delta N.             \tag{6}
\]

For a normalized resolved branch map (V_m=B_m/\sqrt{n_m}), the electric commutator acts on each of its orthogonal destination words by the previously derived multiplier

\[
-\sum_{x\in\{b,d\}}\sum_{c\sim x}E_{cx}^2
 -(1-\sigma)(E_{0b}+E_{0d}).
\]

Its absolute value is at most (2D+2) on prebirth divergence-free fields: the removed squares are at most D and (2|E_{0b}+E_{0d}|\le D+2). This also bounds the coherent branch by orthogonality.

For the magnetic commutator only the 264 overlapping pairs survive. Independently of total volume, \(\|F_a\|^2\le12\): with o occupied B neighbors, the outward incidence degree is (6-o), the inverse degree at most (o+1), and ((6-o)(o+1)\le12). Each pair term has norm at most 288, while its prebirth restriction has norm at most 72 by its (35) or (34+U+U^*\) form. Thus the commutator on a normalized first mark is bounded by (264(288+72)=95040). Combining with (6), and stacking the original labels with their exact weights, gives

\[
\|(h_{\rm out}W-Wh_{\rm in})\phi_s\|\le C,
\quad
C=\delta\bigl(95040+48N+2\sqrt{48N}\bigr)+2K.            \tag{7}
\]

This deliberately loose constant is a fixed-volume bound, not a claimed optimal or local-density resource cost.

There are (9N) pair terms. Since (D\ge0), the common energy shift

\[
h^+=h+2592\delta NI\ge0
\]

works on the whole physical P space. The commutator (7) is unchanged by it. In the prebirth sector,

\[
\|h^+_{\rm in}\phi_s\|=J,
\quad J=\delta\sqrt{(1974N)^2+48N}.                      \tag{8}
\]

Consequently every Fourier fiber of (5) on these inputs has output (h^+\)-norm at most (C+J). These are norm/moment bounds on the actual states, not a finite rotor cutoff or a borrowed finite-dimensional operator norm.

Choose the normalizable sine energy packet

\[
\beta_{w,E_0}(E)=\sqrt{2/w}\sin[\pi(E-E_0)/w]\,1_{[E_0,E_0+w]}(E).
\]

Its mean energy is (E_0+w/2), and Plancherel gives
\(\int\tau^2|\widehat\beta(\tau)|^2d\tau=\pi^2/w^2\). Integrating the derivative of (5), using (7) at (s-\tau\), and then pure-state trace distance proves the complete marked-output bound

\[
e_w\le\frac{2\pi C}{w}.                                \tag{9}
\]

This is uniform over the actual first-wait orbit and its mixtures. It is not a diamond bound over all unbounded-energy inputs.

## Positive bounded-energy cap, real refusal and energy accuracy

Fix (E_0,w,A>0), set (E_{\rm cap}=E_0+w+A), and use the actual battery (L^2([0,E_{\rm cap}])\) with multiplication Hamiltonian E. This is a positive **bounded-energy**, infinite-dimensional continuous battery. It is not a finite-qubit apparatus. The prepared sine packet lies entirely inside its cap.

Let P project the full energy line to that interval and set (C_b=P\widetilde W P). This is a contraction strongly intertwining the positive additive energies. Complete it by the exact Julia unitary

\[
U_b=\begin{pmatrix}
\sqrt{I-C_b^*C_b}&-C_b^*\\
C_b&\sqrt{I-C_bC_b^*}
\end{pmatrix}.                                         \tag{10}
\]

The first input summand is the ready prebirth code; the second is the accepted one-pair/original-label code. The top output is a genuine refusal outcome. Functional calculus of the intertwining relation proves that (10) is unitary and strongly commutes with the direct-sum additive energy. On other physical codes it may be extended by identity. No periodic wrap, negative energy level, or discarded probability is hidden in this completion.

For the input \(\phi_s\beta\), the uncapped output total energy is at least (E_0\). A negative final battery energy therefore requires (h^+_{\rm out}>E_0\), so its probability is at most ((C+J)^2/E_0^2\). A final battery energy above (E_{\rm cap}\) requires initial (h^+_{\rm in}>A\), so its probability is at most (J^2/A^2\). Thus the **actual refusal probability** obeys

\[
p\le\frac{(C+J)^2}{E_0^2}+\frac{J^2}{A^2}.              \tag{11}
\]

Gentle projection plus the retained refusal gives

\[
\|\text{implemented marked output}-\text{original first-event output}\|_1
\le e_w+2\sqrt p+p.                                    \tag{12}
\]

The target is embedded with zero probability in the extra refusal label. At finite resources this is an approximation to the original instrument, not an exact claim with a renamed refusal. Each original accepted label and its sign coherence remain unchanged in the target comparison.

Trace closeness alone would not control the rotor energy. Here both the accepted output and the target have second (h^+\) moment at most ((C+J)^2\). Put (e_a=e_w+2\sqrt p\). Spectral truncation at energy M gives an accepted mean-error bound (Me_a+2(C+J)^2/M\); minimizing it yields (2\sqrt2(C+J)\sqrt{e_a}\).

For the refusal branch, write (R=\sqrt{I-C_b^*C_b}\) and let \(\mathcal K=h^+_{\rm in}+E_B\). It commutes strongly with R. Since (h^+_{\rm in}\le\mathcal K\) and (0\le R\le I\),

\[
\langle R\psi,h^+_{\rm in}R\psi\rangle
\le E_0p+(J+w)\sqrt p,
\qquad \psi=\phi_s\beta.
\]

To see the last step, subtract (E_0\) from \(\mathcal K\), use \(\|(\mathcal K-E_0)\psi\|\le J+w\), and \(\|R^2\psi\|\le\sqrt p\). Thus the full mean-energy comparison, including refusal, is

\[
|\langle h\rangle_{\rm implemented}-\langle h\rangle_{\rm target}|
\le2\sqrt2(C+J)\sqrt{e_a}+E_0p+(J+w)\sqrt p.             \tag{13}
\]

The common scalar shift cancels between the normalized complete outputs. Exact additive conservation in (10) gives the matching battery/system mean-energy ledger, independently of this approximation estimate.

For example take (E_*=C+J\), (w=\lambda E_*\), (E_0=A=\lambda^3E_*\), (\lambda\ge1\). Then (p\le2\lambda^{-6}\), marked trace error tends to zero, and (13), divided by (E_*\), is at most

\[
2\sqrt2\sqrt{2\pi/\lambda+2\sqrt2/\lambda^3}
 +2/\lambda^3+\sqrt2(1+\lambda)/\lambda^3\longrightarrow0.
\]

Every member has a normalizable battery state and finite positive energy cap; the cap and prepared mean grow like (\lambda^3\). That is a sufficient family, not a necessary resource lower bound. An independent arithmetic example at (L=24,K=\delta=1\) gives (C=427970\), (J\approx13644288.0122\), and a deliberately large cap (\approx2.2711\times10^{10}\) for marked trace error below .01. Its size is not a practical implementation claim.

## Time-independent one-shot Hamiltonian, and its exact limitation

The conserving unitary can be executed by a supplied autonomous one-shot coupling rather than an externally switched pulse. Let \(\mathcal K\) be the positive direct-sum system/battery energy in (10), fix readout time (t_*\), put (g=\pi/(2t_*)\), and set

\[
V_*=e^{i\mathcal Kt_*}U_b,\qquad
Q=|1\rangle\langle0|\otimes V_*+|0\rangle\langle1|\otimes V_*^*,
\qquad H_{\rm one}=\mathcal K+g(I+Q).
\]

Here (Q^2=I\), \([Q,\mathcal K]=0\), and (H_{\rm one}\ge0\). From the ready two-state clock \(|0\rangle\), evolution at (t_*\) gives \(|1\rangle U_b\psi\) up to a scalar phase: the programmed (e^{i\mathcal Kt_*}\) cancels exactly the free evolution counted in the total Hamiltonian. Both additive energy and interaction energy are separately conserved. The bounded coupling has norm g (apart from its harmless positive scalar), but its payload operator is global and engineered.

This is a time-independent supplied Hamiltonian with a specified observation time, recurrence and reversible flags. It is not an endogenous exponential waiting-time process. In particular a battery freely evolving during an unknown first wait shifts its Fourier phase; blindly reusing the same fixed lift then gives (e^{-ish_{\rm out}}W\Omega\), rather than the desired (W e^{-ish_{\rm in}}\Omega\), in the sharp-reference limit. The landed clock notes already warn about this distinction. Uniform approximation for the **input family** \(\phi_s\) is not permission to reset or rephase an actual ongoing battery for free.

## Locality, exact tests and terminal gap

The original B is local and its first energy commutator has the explicitly counted 264-pair support. The spectral lift, its cap/refusal square root, and the one-shot payload (V_*\) are generally spatially global. Higher commutators spread through the interacting lattice. The September 7 CAR local-quench estimates do not automatically apply to these rotor words; a locality approximation must control its energy defect as well as its state error. No spatially finite-support synthesis or uniform bounded-density apparatus has been proved here.

`check.py` verifies the three exact covariance witnesses from the frozen full polynomial. A separate exact 12-dimensional positive-ladder Julia fixture checks unitarity, additive-energy commutation, a real lower-boundary refusal of probability 1/2, retained sine-battery coherence, and direct battery/system energy balance. Its 24-dimensional two-state clock checks the involution and energy commutation underlying exact arrival at (2\pi\). The sine packet examples have trace error (1-\cos[\pi/(L_B+1)]\), energy gain 1/2 and battery change -1/2; they test the construction, not the PR rotor dynamics. Resource arithmetic and the convergence bound above are also executed. Each run took under one second, with capped threads; no large rotor simulation or heavy job was launched.

The exact remaining supplier target is a local, time-independent model including all energetic references and readout, whose process marginal approximates or equals the **unchanged full PR9345 original marked law**, with its waiting times, later births and retained battery correlations, and with controlled energy/current accounting on stated domains. For finite-horizon approximations, it needs a justified rotor-to-apparatus error, both marked-process and energy-moment control, and an explicit clock/renewal budget. The existing finite-dimensional global clock theorem is relevant prior art, not that missing rotor/locality lemma. This terminal gap is target-equivalent to the requested ongoing autonomous event-energy supplier, but much narrower than the full gravity/TOE task.

The stationary all-input class is excluded by (3); coherent supplied resources remain a constructive route. Neither the positive first-event system-energy increment nor this exact apparatus ledger identifies physical heat, absorbed light, a selected reservoir, or a stress tensor.
