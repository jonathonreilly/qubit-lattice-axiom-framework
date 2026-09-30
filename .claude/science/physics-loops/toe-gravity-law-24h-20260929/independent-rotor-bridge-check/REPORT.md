# Independent check of the full original rotor process/energy bridge

The frozen bridge proof is supported within its fixed-volume, fixed-horizon, supplied-law scope. I independently recover the finite birth bound, normalized full history instrument, agreement of the low-order cutoff words with the **correct** cutoff loss, the weighted Dyson estimates, all energy/current constants, and the stated composition with the retained-battery finite-grid apparatus. No blocking mathematical error was found.

The conclusion remains an approximation of binned original records and final states at a fixed finite number of passive grid observations, together with energy and target-current moments. It is not exact autonomous timestamp generation, spatially local energy supply, irreversible autonomous storage, or pointwise convergence of the apparatus's instantaneous battery current. The supplied initial preparation, quantum process interpretation, dynamics and apparatus resources are not framework premises derived here.

This is focused independent evidence, not a formal review/audit PASS. Coverage binds `rotor-process-energy-bridge/REPORT.md`, SHA256 `f8d902e18bc95ed146cda93cc0c83c81b6fa13f57379514e871b0ee90d14e28c`. No author implementation was imported or executed. All new files are in this directory.

## Refreshed sources and actual model

Before serious reuse I fetched main and queried the actual proposal head. Main remained `e75578f7136401d4bd750131671aed9212c06291`; PR9345 remained open at `fe51bf1728b625dc0133256f43e7783afb11f7d8`. I read the complete landed common-law and pair-form arguments, the finite-energy-supply argument, and the finite-grid marked-process argument, repairing a truncated output by reading the operational assumptions separately. The one-time clock's sections 1–5 were read as context; its reduced one-time conclusion alone is not used as a substitute for the finite-grid theorem. The actual PR9345 law, original instruments, preparation and local incidence bounds were read at that head. Its band/response theorem is not required here. The prior unrestricted-record-count source's fixed-graph cutoff argument was inspected; its prepared-count conclusions are not imported.

The source law acts on a fixed finite even cubic torus, with all A sites occupied in the P carrier, hard-core charges, integer rotor fields and physical Gauss constraint. Starting from the actual `Ω` (A charges plus, B empty, field zero), keep

\[
h=KD+A,\quad A=\delta H_4,\quad
H_4=-2\sum_{\{a,c\}:d(a,c)=2}(F_cF_aP)^\dagger(F_cF_aP),
\]

\[
D=\sum_{a\to b:q_b=0}E_{ab}(E_{ab}-q_a),\quad
L_m=\sqrt\kappa\,B_m,\quad B_{ab,\sigma}=Pj_{ab,\sigma}F_aP.
\]

The coherent instrument is the original unnormalized sign sum for each edge. It must not be replaced by separately recorded signs. Conversely the resolved instrument keeps its original edge/sign labels. The proof applies to either fixed choice.

The predecessor already supplies a mathematical rotor semigroup and strong fixed-graph cutoffs. The additional issue checked here is the labeled continuous-history estimate with coercive moments, followed by a finite-apparatus composition. No broad novelty conclusion follows from this source inspection.

## Grading, local norms, and the finite-dimensional cutoff

An outward hop removes one A occupation and fills an empty B site. A subsequent creation on another empty endpoint refills the same A site and fills another B site. Thus each original `B_m` raises `N_B` by exactly two. Both terms of a coherent sign sum have the same grade. Each pair operator `S_ac` raises this count by two and its adjoint lowers it by two, so `S_ac†S_ac` preserves it. The diagonal electric term and every `B_m†B_m` also preserve it. These are exact operator grading identities on all later sectors, not only prebirth rates.

There are `N=L³/2` B sites. Starting at grade zero, every nonzero `j`-birth trajectory has `N_B=2j`, hence `j≤M=N/2`. At grade `N` every birth operator vanishes. The proof allows stalled lower-grade histories and contains no reverse recorded event. Projection by a field radius commutes with the grading and preserves the same bound.

The improved local hop norm can be derived directly by a rectangular Schur bound. At fixed initial B occupation `o`, each source word has at most `6−o` outgoing destinations and each target word at most `o+1` predecessors. Nonzero coefficients are unit rotor permutations, so

`||F_a||²≤max_o (6−o)(o+1)=12`.

Gauss restrictions only delete incidences. Spectator A vacancies do not change these local degrees. Consequently `||−2S_ac†S_ac||≤288`. Each cubic A site has 18 distance-two A neighbors, hence `9N` unordered pairs, giving `v=2592δN`.

A fixed resolved birth map has norm at most five; the two sign outputs are orthogonal in the root A charge. Therefore the coherent norm is at most `5sqrt(2)`, and either label convention obeys `Σ||L_m||²≤g=300κN`. The actual source admits sharper bounds, but none is needed for the claimed constants. Orthogonality is used for the loss bound, without discarding coherent amplitudes in the jump output.

With `r=Σ|E_e|`, `Q=1+r`, every integer electric summand is nonnegative. For `r≥1`, `D≤r²+r≤2r²`; it is zero at `r=0`. Thus `D≤2Q²`, even though D does not control all occupied-link directions. The bounded perturbation theorem gives self-adjoint `h` on `Dom D`, with `h+vI≥0`.

Use the full radius projection `Π_R=1_(r≤R)`, not an energy-window projection. Then

`h_R=Π_RhΠ_R`, `L_(m,R)=Π_RL_mΠ_R`, `Γ_R=Σ L_(m,R)†L_(m,R)`

are finite-dimensional, with dimension at most `6^N(2R+1)^(6N)`. The positive shift `h_R^+=h_R+vI` has norm at most `bar h_R=2KR²+2v`. The constant shift leaves generator energy changes and the dissipative energy current unchanged.

Crucially,

\[
\Pi_R\Gamma\Pi_R-\Gamma_R
=\sum_m\Pi_RL_m^\dagger(I-\Pi_R)L_m\Pi_R\ge0.
\tag{1}
\]

Using the left compression as the no-event loss, while using compressed recorded jumps, would introduce an unrecorded probability sink. The bridge uses `Γ_R`, so it is a new trace-preserving original-label process, not a survival postselection.

## History normalization and coefficient agreement

Let `S_t=exp[(-ih−Γ/2)t]`. Bounded loss is a dissipative perturbation of the self-adjoint Hamiltonian. On a common core,

\[
\frac{d}{dt}\|S_t\psi\|^2=-\sum_m\|L_mS_t\psi\|^2.
\]

Approximation extends the integrated identity to arbitrary initial Hilbert vectors. Iterating it after each jump telescopes the survival loss against the next-event gain. In this preparation the remainder after `M` events is zero, since all further jumps vanish at maximum grade. Therefore the sum of the ordered-time integrals of `||K_j(t,m)Ω||²`, for `0≤j≤M`, is exactly one. This independently proves the trajectory-stack normalization, without replacing the loss by a prebirth scalar or assuming a Poisson count law. The cutoff has the same argument because its loss is exactly `Σ L_R†L_R`.

Take the interaction picture of KD. The bounded insertion is `G(t)=exp(iKDt)(−iA−Γ/2)exp(−iKDt)`, with norm at most `a=v+g/2`. The electric group is diagonal, so it preserves both radius and grade. Strong measurability/continuity on vectors suffices for the Dyson integrals; norm continuity of electric conjugation on the full rotor space is unnecessary.

A jump word shifts radius by at most two. An A word or a loss word shifts it by at most four; for a loss word the two internal jumps each cost two. Thus every intermediate and final configuration in an `n`-insertion, `j`-jump word lies at radius at most `4n+2j`, starting from Ω. If this is no larger than R, each inserted projection acts as the identity, including the middle projection in `L_R†L_R`. The full and cutoff coefficients agree pointwise in all time arguments and labels. The diagonal electric phases agree too. This proves the claimed comparison with the actual `Γ_R`, rather than only with a compressed old no-event generator.

For fixed jump times, summing all allocations of n bounded insertions over the `j+1` dwell intervals gives exactly `T^n/n!`; this is the multinomial formula for the sum of their lengths. Summing squared label norms is bounded by `g^j`; the ordered jump-time simplex has volume `T^j/j!`. Cauchy–Schwarz in this history space gives, for the piece of total bounded-insertion order n,

\[
\|Q^p V_T^{(n)}\Omega\|
\le b_M(gT)(1+2M+4n)^p(aT)^n/n!.
\tag{2}
\]

The same estimate holds for the cutoff, for every nonnegative integer p. It controls all later sectors and unconstrained electric directions.

Put `b=1+2M`, `x=aT`, `y=gT`, and use the author's `X_p,Y_(p,r)` sums with `R=2M+4r+8`. Subtracting the two Dyson expansions cancels every term through n=r. Each remaining expansion costs its own tail, yielding

`||Q^p(V−V_R)Ω||≤2Y_(p,r)` and `||Q^pVΩ||,||Q^pV_RΩ||≤X_p`.

The classical-quantum instrument estimate can be obtained directly, avoiding any formal trace-class “diagonal density matrix” on a continuous history space. For the unnormalized final vectors `u(ω),v(ω)` indexed by histories,

\[
\int\|uu^\dagger-vv^\dagger\|_1d\omega
\le(\|u\|_{L^2}+\|v\|_{L^2})\|u-v\|_{L^2}
\le4Y_{0,r}.
\]

Both histories have norm one, and trace distance is at most two. This recovers `eta_R≤min(2,4Y0)`, including the actual unnormalized conditional final states. It gives no probability-independent bound after normalization of a rare individual history. Binning/copying passive records contracts this comparison.

## Weighted operators and all energy/current constants

For an operator with radial range s, decompose it as `O=Σ_(d=−s)^s O_d`, where `O_d` changes the radius by d. Within one d, input and output radial blocks are mutually orthogonal, so `||O_d||≤||O||`. On those blocks the weight ratio is at most `(1+s)^p`. Hence

\[
\|Q^pO\psi\|\le(2s+1)(1+s)^p\|O\|\,\|Q^p\psi\|.
\tag{3}
\]

This proves the exact factors 45 for a range-two jump at p=2 and 225 for a range-four loss. Cutoff projection preserves these estimates. The energy bound is `||hψ||≤2K||Q²ψ||+v||ψ||`.

For the original source-current form

\[
\mathcal P=\sum_m L_m^\dagger hL_m-\tfrac12\Gamma h-\tfrac12h\Gamma,
\]

the three electric contributions are bounded by `90Kg`, `Kg`, and `225Kg` times `||Q²ψ||`, respectively. Their sum is precisely **316Kg**. The bounded A contributions cost at most `2vg||ψ||`. Thus

`||mathcal P ψ||≤g(316K||Q²ψ||+2v||ψ||)`.

The same bound holds for the finite current. This symmetric finite-word expression is defined on `Dom Q²`; no choice of a self-adjoint extension of the unbounded current is required. Its second moment is the form `||mathcal P ψ||²`. The actual trajectory ensemble has the needed fourth field moment by (2) at p=2. The stronger estimates for all p also show that the chosen initial evolution has all such moments; arbitrary trace-class inputs are not asserted to have them. Weighted-space convergence and preservation under the bounded shift terms justify the source-current energy derivative for this input, with the Hamiltonian part conserving its own energy.

Write `φ=VΩ`, `χ=V_RΩ`, and `S_h=2KX2+v`, `S_P=g(316KX2+2v)`. Normalization, rather than the loose X0 bound, gives `||hφ||,||hχ||,||h_Rχ||≤S_h` and the analogous original/cutoff current bounds by `S_P`.

On an embedded cutoff vector, `(h−h_R)χ=(I−Π_R)Aχ`. It only sees the cutoff boundary strip of width four. The low-order expansion of χ has no support there; the remainder has norm at most Y0. Combining this with the weighted vector difference gives exactly

`||hφ−h_Rχ||≤4KY2+3vY0=:E_h`.

Every term of the current has radial range at most eight. The original and actual cutoff current expressions coincide on `Π_(R−8)`, including all internal loss projections. The remainder of χ outside that smaller radius has weighted norm at most Yp. Applying (3) to both current expressions costs `2g(316KY2+2vY0)`, and applying it to `φ−χ` costs the same amount. Thus

`||mathcal P φ−mathcal P_R χ||≤4g(316KY2+2vY0)=:E_P`.

Finally, exact energy compression gives `⟨χ,hχ⟩=⟨χ,h_Rχ⟩`; Cauchy–Schwarz then yields the four stated bounds:

\[
|\Delta\langle h\rangle|\le4S_hY0,\qquad
|\Delta\langle h^2\rangle|\le2S_hE_h,
\]

\[
|\Delta\langle\mathcal P\rangle|\le2S_PY0+E_P,\qquad
|\Delta\langle\mathcal P^\dagger\mathcal P\rangle|\le2S_PE_P.
\tag{4}
\]

For the first current bound, split the difference as `⟨φ−χ,Pφ⟩+⟨χ,Pφ−P_Rχ⟩`; this explains why its second term is E_P rather than another S_P factor. The second-moment inequalities are differences of squared vector norms. Multiplication by any real history function with absolute value at most one commutes with final system operators and changes none of these arguments. Thus the same bounds apply to total variation of the corresponding energy/current-weighted history measures, not only to unconditional averages.

## Finite-grid retained-battery composition

The correct predecessor is the finite-grid marked-process theorem, including its specified Julia collision completion, squared-sine clock and correlated-payload interval estimate. The older one-time sine-packet theorem alone would not justify observations. The actual grid theorem retains the same physical battery, clock and flags; product reference states appear only in a hybrid comparison, not as real resets or rephasings.

Here the allowed rotor testers only read/copy completed event bins and perform a final bounded system test. There are no intermediate energy-injecting operations on the unbounded rotor. The full-history cutoff comparison therefore descends to this tester class. Apply the finite-dimensional apparatus theorem to `(h_R^+,L_R)`, using the safe upper bounds `bar h_R` and g in place of its exact operator norms. The condition `tau g≤1/2` and the marked-bin estimate survive that replacement.

I rechecked its constants: the Julia completion has full-space distance at most `2sqrt(tau g)` from the identity; the joint clock interval error is at most `4e_clock`; the same-battery hybrid costs `q eta_L`; and the original marked-bin comparison costs `T tau(7g²+4bar h_R g)`. These are process bounds with original mark grouping, not conclusions inferred from reduced-channel convergence.

For `n≥8`, `w=ceil(n^(1/3))`, `R_clock=16n`, the supplied packet has `c1≥1/2`, `J_clock≤n/T`, and

`sigma_V≤20/[tau(w+1)²]`.

For example the latter constant follows from `4π²sqrt(2)/3<20`. The packet term is bounded by `44sqrt(Tg)n^(−1/6)`. The boundary factorial bound with `R_clock≥8a_clock` and `a_clock≥n` gives the stated `4exp(−7n)`. For positive T the prescription (20) makes the four apparatus-error contributions at most `nu0/4`, `nu0/28`, `(11/56)nu0`, and `nu0/4`, using `π<22/7`. Their sum is at most **`(41/56)nu0<nu0`**. Zero horizon is the trivial identity case. Refinement must respect the prescribed grid denominator, as the report states.

Thus the rotor/apparatus binned process error is at most `eta_R+nu0`. The four finite observables have norms bounded by `bar h_R`, `bar h_R²`, `bar p_R`, `bar p_R²`, with `bar p_R=g[316K(1+R)²+2v]`. Their apparatus errors are those norms times nu0. Choosing r first and nu0 afterward proves simultaneous process and moment accuracy with finite resources.

One wording clarification is advisable: the battery uses at most `d_R−1` distinct positive **excitation energies above the minimum eigenvalue**, not all pairwise Bohr differences (which can be more numerous). This is exactly the source construction's spectral basis and is sufficient for its energy-translation lift. Each excitation energy is at most `bar h_R`, so the stated dimension and mean-energy upper bounds follow. No estimate here assumes an efficient diagonalization or efficient apparatus preparation.

The battery/system additive free energy is exactly conserved between observations. Passive flag dephasing commutes with that free energy, so its ensemble balance also survives these observations. It can alter program interaction energy and has an external readout cost. Therefore endpoint estimates control cumulative ensemble transfer and interval-averaged transfer. The bounded observable `P_R` is the target finite generator's source current. Process/state approximation controls its tested moments at grid times, **not** the derivative of the actual apparatus battery energy at each instant. The frozen report correctly preserves this distinction.

Exact continuous timestamps occur only in the mathematical rotor/cutoff comparison. The autonomous apparatus approximates binned outputs—either the specified multiple-event symbol or complete finite ordered mark words—with the source theorem's finite-grid comparison. Its flags remain physically reversible and its finite clock recurrent. Neither future inaccessible flags nor a physical irreversible reader have been assumed available for free.

## Explicit tails, independent controls and limits

The factorial tails are sufficient without evaluating huge exponentials. For `X=ceil(x)`, `Y=ceil(y)` and `k=r+1≥max(1,6X)`, the weighted p=2 term ratio is bounded by `x(n+1)/n²≤1/3` for n≥k. The factor-one-half tail bound is therefore conservative. Using `k!≥(k/e)^k`, `e<3`, `b_M(y)≤2^Y`, and `e^x≤2^(2X)` recovers all three inequalities (22). This proves convergence at fixed graph, parameters and horizon. It supplies no bound uniform in volume or time.

The one independent computation took **0.160 seconds**, peak RSS **20,267,008 bytes**, with threads capped at one. It was priced below five seconds and 100 MB. It did not simulate the torus or execute an author runner. It checked:

- all **9,720** legal local original B words, including both charges/signs, their exact Gauss increments, field range two and increase of B occupation by two;
- the actual local incidence and global counting constants used above;
- **104** exact graded one-rotor word comparisons with the correct cutoff loss and nontrivial electric phases, 93 yielding nonreal final vectors; a separate graded forward equation verifies history normalization, and a boundary fixture distinguishes actual cutoff loss zero from incorrectly compressed old loss two;
- the weighted constants and the proposed large resource example using integer coefficient bit lengths, without instantiating huge powers or Hilbert spaces.

The one-rotor fixture is explicitly an algebra control, not the physical source model. The all-word conclusion follows from the support proof above, not from those 104 samples. The full history normalization follows from the survival/jump telescoping argument, not from the fixture alone.

For `L=24,K=delta=kappa=T=1`, the independently verified parameters are `M=3456`, `v=17915904`, `g=2073600`, `x=18952704`, `k=336531472`, `R=1346132804`. Strict log2 upper bounds for the process, energy first/second, and current first/second errors are respectively `−334457868`, `−294478807`, `−294478745`, `−294478771`, and `−294478688`; all are far below `−100`. The loose encoding bound is **1,347,840 system qubits**. Rounding n to a multiple of three for observations at `T/3,2T/3,T` still gives a **382-digit** collision count and **384-digit** clock dimension. These numbers verify finiteness at the declared, deliberately impractical scale; they are not lower bounds or feasibility claims.

`check_bridge.py`, `results.json`, `results.txt`, `SOURCE_BINDINGS.json`, and `MANIFEST.json` preserve the code, receipts and exact source coverage. No independent claim is made about the source's microscopic-to-rotor error, band/response theorems, other proposal proofs, or physical selection. The supported bridge is for the actual fixed preparation and law, all original later births, fixed finite horizon and passive finite-grid composition. Sustainable/local reservoirs, arbitrary unbounded-energy interventions, irreversible autonomous records, exact clocks and a gravitational stress identification remain separate tasks.
