# Full original rotor process to a finite energy supplier

This conditional construction supplies a fixed-volume, finite-horizon bridge that the finite-dimensional apparatus theorems need. The rotor-to-cutoff comparison retains **all original marks, all later births and continuous waiting times**, with the actual final conditional quantum state. Weighted versions control system energy and the original generator's energy-source current, including their second moments. Composing with the landed autonomous apparatus gives **binned** original records at finitely many passive grid observations. It does not give an exact timestamp clock, a spatially local supplier, or pointwise agreement of the autonomous apparatus's instantaneous battery current.

This is author mathematics, awaiting an independent check. No axiom, primitive, physical reservoir, rate, state or heat/stress identification is adopted. `CONTRACT.md` fixed the comparison before computation. `SOURCES.json` binds actual sources and `check.py` provides small algebra/constant controls, not a torus simulation.

## 1. Actual model and prior-source boundary

Use the supplied finite even cubic torus `L≥24`, `N=L³/2` A vertices and equally many B vertices, with `6N` oriented A-to-B links. Keep all physical Gauss-law charge/field states in the all-A-occupied P space, integer fields, tensor hard-core charges, the actual Ω (all A plus, B empty, field zero), and fixed `K,δ,κ>0`. The complete common-limit law is

\[
h=KD+A,\quad A=\delta H_4,
\quad H_4=-2\sum_{\{a,c\}:d(a,c)=2}(F_cF_aP)^\dagger(F_cF_aP),
\]
\[
D=\sum_{a\to b:q_b=0}E_{ab}(E_{ab}-q_a),
\quad L_m=\sqrt\kappa B_m,\quad B_{ab,\sigma}=Pj_{ab,\sigma}F_aP.
\tag{1}
\]

Choose **one** original instrument: the `12N` resolved labels `σ=±`, or the `6N` coherent labels with `B_ab,c=B_ab,++B_ab,−`. No destination or hidden sign is additionally measured. The original waiting-time law uses `−ih−Γ/2`, `Γ=Σ L_m†L_m`, on every later sector; it is not replaced by the prebirth scalar loss.

The finite-energy-supply, autonomous-one-time-clock and finite-grid-process notes of September 24 were read in full. Their battery lifts, supplied clocks and finite-dimensional process estimates are prior machinery, not a new result here. The landed unrestricted-record-count note already passes box compressions to the common rotor semigroup by strong Dyson convergence, and already notes bounded total birth count. The charged finite-link note gives quantitative Hamiltonian-only flux truncation for a different supplied CAR law. Neither argument is imported as a full marked-process/energy estimate. The addition here is the explicit graded, labeled-history Dyson comparison and its weighted bounds for (1), followed by a scoped composition with the existing apparatus theorem. No exhaustive novelty claim is made.

The actual PR9345 source remains separately supplied at `fe51bf1728b625dc0133256f43e7783afb11f7d8`. Its original process is kept. The proof below also follows directly from the landed common-law and pair-form definitions plus the explicitly supplied Ω; it needs no unmerged band or response estimate.

The actual PR9314 cube proof and PR9316 cubic preparation/escape argument were also inspected. They contain strong-electric sector reductions, and PR9316 uses a factorial tail for periodifying its projected one-pair stencil. Those are relevant precedents for the method; no sector projection, rare-birth scaling, or omitted later-event remainder from those arguments is used below.

## 2. Count grading, full-carrier bounds and field range

Let `N_B` count occupied B sites. Each outward `F_a` empties one A and fills one B; its adjoint reverses those counts. A birth `j_ab,σ` fills both empty endpoints. Therefore

\[
[N_B,F_a]=F_a,\quad [N_B,j_{ab,\sigma}]=j_{ab,\sigma},
\quad [N_B,B_m]=2B_m,
\]
\[
[N_B,D]=[N_B,H_4]=[N_B,\Gamma]=0.
\tag{2}
\]

The reverse paths inside `S_ac†S_ac` can move or exchange occupied B sites, but their net B count is zero. Reverse jumps `B_m†` do not occur as recorded events; their presence inside the loss does not lower the trajectory grade. From Ω every `j`-event history lies in `N_B=2j`, so

\[
j\le M:=N/2.
\tag{3}
\]

This is a pathwise maximum for the supplied unperturbed law, not just a bound on its expected count. It is not a claim that every trajectory reaches M births; stalled lower-count histories remain allowed. Arbitrary record-erasing or energy-injecting external interventions are outside the comparison.

Use the full field radius `r(E)=Σ_e|E_e|` and coercive weight `Q=1+r(E)`. This weight includes occupied-link fields that the masked D no longer controls. A hop shifts one link by one; a B word shifts radius by at most two; an H4 word and a Γ word by at most four. Diagonal electric evolution changes neither field support nor `N_B`.

On the full physical P carrier, `||F_a||²≤12`: at neighbouring B occupancy `o`, its source/target incidence degrees are at most `6−o` and `o+1`. This count includes both charges and rotor permutation shifts. Thus `||−2S_ac†S_ac||≤288`, and there are `9N` pairs. A resolved B has norm at most five. The two sign outputs of a fixed edge are orthogonal in the root charge, hence the coherent B has norm at most `5√2`. For either stipulated instrument we may use

\[
\|A\|\le v:=2592\delta N,
\quad \sum_m\|L_m\|^2\le g:=300\kappa N,
\quad a:=v+g/2.
\tag{4}
\]

Every integer summand of D is nonnegative, and `D≤2r(E)²≤2Q²`. Thus h is self-adjoint on `Dom D`, with `h+vI≥0`. We do not assume that D controls every later field direction.

## 3. Finite process, with its correct boundary loss

Let `P_R=1_(r(E)≤R)` inside the physical P space and use

\[
h_R=P_R hP_R,\quad L_{m,R}=P_R L_mP_R,
\quad \Gamma_R=\sum_m L_{m,R}^\dagger L_{m,R}.
\tag{5}
\]

These define a finite, trace-preserving original-label jump process on `P_R`. Its boundary amplitudes and rates change, but it is not postselection on surviving trajectories. In particular **Γ_R is not replaced by P_R ΓP_R**: their difference is the positive missing boundary jump flux. Compressing the old no-event generator alone would lose probability. The construction preserves Gauss and (2), and still has at most M recorded births.

A sufficient dimension and Hamiltonian-norm bound is

\[
d_R\le6^N(2R+1)^{6N},\quad
0\le h_R^+:=h_R+vI,\quad
\|h_R^+\|\le\bar h_R:=2KR^2+2v.
\tag{6}
\]

The global radius projection is a finite mathematical approximation, not a spatially local interaction implementation. Using the full field radius avoids assuming that a bounded energy window is finite dimensional: the masked D loses control of occupied-link field directions after births.

## 4. Exact-timestamp history comparison

For `j≤M`, original labels `m_1,…,m_j` and ordered times `0<t_1<…<t_j<T`, let `K_j(t,m)` be the product of the actual no-event propagators and `L_m` insertions, with final no-event evolution to T. Stacking them in the direct sum of history `L²` spaces defines the usual trajectory isometry `V_T`. Its norm identity is trace preservation of the bounded-jump law. The cutoff defines `V_(T,R)` in the **same** history space after embedding its final system. The classical output is the measured history, with its conditional final system state; its norm is the integral trace norm for this classical-quantum instrument. Exact continuous timestamps are meaningful in this mathematical comparison.

In the interaction picture of KD, the no-event perturbation is the bounded, strongly continuous family

\[
G(t)=e^{iKDt}(-iA-\Gamma/2)e^{-iKDt},\quad \|G(t)\|\le a.
\]

Strong measurability suffices for its Dyson integrals; no rotor-wide norm continuity is assumed. The cutoff obeys the same bound and commutes with the electric free group. Write `V_T^(n)` for terms with a total of n bounded no-event insertions across all dwell intervals. For fixed jump times, summing the interval allocations gives `T^n/n!`. Stacking the original marks has norm at most `g^(j/2)`, and the ordered j-time simplex has volume `T^j/j!`. Consequently, with

\[
x=aT,\quad y=gT,\quad
b_M(y)=\left(\sum_{j=0}^M y^j/j!\right)^{1/2},
\quad b=1+2M,
\]

\[
\|Q^p V_T^{(n)}\Omega\|
\le b_M(y)(b+4n)^p x^n/n!,\qquad p=0,1,2,\ldots.
\tag{7}
\]

The same estimate holds for the cutoff. This estimate may be very loose, but is independent of R. It bounds all later sectors, including electric directions unconfined by D.

All coefficients with `4n+2j≤R` agree between the two processes: every prefix and every internal factor in `L_R†L_R` stays inside the projection. This uses the actual loss (5). Choose

\[
R=2M+4r+8,\quad r\ge0,
\quad Y_{p,r}=b_M(y)\sum_{n=r+1}^\infty (b+4n)^p x^n/n!,
\quad X_p=b_M(y)\sum_{n=0}^\infty (b+4n)^p x^n/n!.
\tag{8}
\]

The extra eight units will also cover the current boundary below. Coefficient agreement and two tail bounds give

\[
\|Q^p(V_T-V_{T,R})\Omega\|\le2Y_{p,r},
\quad \|Q^p V_T\Omega\|,\|Q^pV_{T,R}\Omega\|\le X_p.
\tag{9}
\]

In particular the complete original history/final-state error is

\[
\eta_R\le\min\{2,4Y_{0,r}\}.
\tag{10}
\]

The estimates hold uniformly for `0≤t≤T` by using T on the right. Coarsening times or histories only decreases the process error. No individual rare-history conditional error is inferred by division by its probability.

All series are explicit. For example

\[
X_2=b_M(y)e^x[(b+4x)^2+16x],
\]
\[
Y_{2,r}=b_M(y)[b^2\mathcal T_{r+1}(x)
 +(8b+16)x\mathcal T_r(x)+16x^2\mathcal T_{r-1}(x)],
\quad \mathcal T_k(x)=\sum_{n\ge\max(k,0)}x^n/n!.
\tag{11}
\]

The tails `Y_(p,r)` tend to zero for fixed graph, parameters and horizon as r grows; `X_p` remains a fixed moment bound. This is an explicit replacement for qualitative trace convergence, not a volume-uniform theorem.

## 5. Energy and the actual source-current form

On `Dom Q²`, define the original total energy-source form

\[
\mathcal P=\sum_m\left(L_m^\dagger hL_m
-\tfrac12\{L_m^\dagger L_m,h\}\right).
\tag{12}
\]

This is the adjoint dissipator applied to h; its expectation is the instantaneous system-energy injection rate on the states covered by the weighted bounds. It is not assumed positive after later births. It is a symmetric finite-word operator on this domain; its second moment below means the well-defined squared norm `||mathcal P ψ||²`, without asserting a particular self-adjoint extension. Define `mathcal P_R` analogously from (5); to avoid confusion, in this section write `Π_R` for the field projection and `mathcal P_R` for that current.

For any bounded field-range-s operator O, its radial block decomposition has `2s+1` components of norm at most `||O||`. Therefore

\[
\|Q^p O\psi\|\le(2s+1)(1+s)^p\|O\|\,\|Q^p\psi\|.
\tag{13}
\]

For `p=2`, the factors are 45 for each jump and 225 for Γ. Applying this to the three terms of (12), including the unbounded electric term, gives

\[
\|h\psi\|\le2K\|Q^2\psi\|+v\|\psi\|,
\quad
\|\mathcal P\psi\|\le g[316K\|Q^2\psi\|+2v\|\psi\|].
\tag{14}
\]

The cutoff has the same bounds. Set

\[
S_h=2KX_2+v,\qquad S_P=g(316KX_2+2v).
\tag{15}
\]

These bound first energy/current vector norms and hence their second moments on the entire actual ensemble. They also supply the domain justification for the energy derivative: the bounded finite-shift terms preserve each coercive graph norm by the same convergent weighted Dyson series. The statement is about this actual input evolution, not arbitrary trace-class states.

Let

\[
E_h=4KY_{2,r}+3vY_{0,r},\qquad
E_P=4g(316KY_{2,r}+2vY_{0,r}).
\tag{16}
\]

Then the full versus actual cutoff energy/current comparisons obey

\[
|\langle h\rangle-\langle h_R\rangle_R|\le4S_hY_{0,r},
\quad
|\langle h^2\rangle-\langle h_R^2\rangle_R|\le2S_h E_h,
\tag{17}
\]
\[
|\langle\mathcal P\rangle-\langle\mathcal P_R\rangle_R|
\le2S_PY_{0,r}+E_P,
\quad
|\langle\mathcal P^\dagger\mathcal P\rangle
-\langle\mathcal P_R^2\rangle_R|\le2S_P E_P.
\tag{18}
\]

Here and below second energy moments are quadratic forms on `Dom h`; the required fourth field moment is already derived by (9) with p=2, rather than assumed separately. To prove the bounds, first use (9) and (14). On an embedded cutoff vector, `h−h_R=(I−Π_R)AΠ_R`; this vanishes away from a boundary strip of width four. Its tail norm is at most `vY_0`, yielding `||hV−h_RV_R||≤E_h`. The current has field range at most eight. Its full and cutoff expressions agree on `Π_(R−8)`. Each has the relative bound (14), so the boundary difference costs at most `2g(316KY_2+2vY_0)`; adding the weighted vector difference gives `E_P`. Difference-of-squares and Cauchy–Schwarz prove (17)-(18). The first energy expectation uses the exact compression identity `Π_RhΠ_R=h_R`.

The same inequalities hold for **energy/current-weighted history measures** in total variation: insert any bounded real history function `|f|≤1` in the history Hilbert space. It commutes with the final system operators and changes none of the norm bounds. Thus the statement does not merely compare unconditioned scalar averages while ignoring which original marks occurred.

## 6. Composition with the existing finite apparatus theorem

Fix q passive grid observations, retaining the original event flags and a final system output. No intermediate operation acts on the rotor system; arbitrary final bounded tests are allowed. Such observations are a subset of the tester class in the landed finite-grid theorem. The complete continuous-history bound (10) therefore applies after binning and retaining all q passive observations. It does not establish uniformity over arbitrary unbounded-energy rotor interventions.

Apply the existing theorem to the finite system `(h_R^+,L_m,R)`, retaining its original label grouping and coherent sign sums. Its finite-battery width `L_B`, collision step `τ=T/n`, squared-sine clock width w and buffer R_clock give

\[
\nu\le4q e_{clock}+q\eta_{L_B}+T\tau c_{mark},
\quad c_{mark}=7g^2+4\bar h_R g,
\quad \eta_{L_B}\le4\pi/(L_B+1).
\tag{19}
\]

The remaining clock formulas are precisely the landed theorem: `c1=(2+cos(2π/(w+1)))/3`, `2J_clock c1=1/τ`, `a_clock=2J_clock T`, `R_clock≥8a_clock`, and
`e_clock≤2√(τg)(w+Tσ_V)+4exp(a_clock)a_clock^(R_clock)/R_clock!`.
The same battery, clock, flags and their correlations remain throughout; no real reset or free rephasing is made.

For an explicit sufficient prescription, take `n≥8`, `w=ceil(n^(1/3))`, `R_clock=ceil(16n)`. Since `c1≥1/2` and `σ_V≤20/[τ(w+1)²]`,

\[
e_{clock}\le44\sqrt{Tg}\,n^{-1/6}+4e^{-7n}.
\]

For a desired apparatus error `ν0>0`, it suffices to choose

\[
n\ge\max\{8,2Tg,(704q\sqrt{Tg}/\nu_0)^6,
4T^2c_{mark}/\nu_0,64q/\nu_0\},
\quad L_B+1\ge64q/\nu_0.
\tag{20}
\]

Round n upward to a multiple of the prescribed common grid denominator when needed. The last term safely controls the exponential boundary contribution using `e^(7n)≥7n`; the constants are intentionally loose.

The complete rotor-versus-apparatus binned-process error is at most `η_R+ν0`. The finite-system observable bound

\[
\|\mathcal P_R\|\le\bar p_R:=g[316K(1+R)^2+2v]
\tag{21}
\]

adds respectively `bar h_R ν0`, `bar h_R² ν0`, `bar p_R ν0`, and `bar p_R² ν0` to (17)-(18). Choose r first, then `ν0` small relative to all four norms and requested tolerances. This proves simultaneous process, first-moment and second-moment approximation with explicitly finite resources.

There are at most `d_R−1` distinct positive spectral gaps. The prior supply uses that many ladders, dimension `(L_B+2)^(number of gaps)`, with mean energy `(L_B+1)Σ gaps/2≤(L_B+1)(d_R−1)bar h_R/2`. There are n zero-free-energy but pure blank flags, each with the original mark alphabet plus a blank label, and clock dimension `n+w+2R_clock+1`; `J_clock≤n/T` and its prepared interaction energy is at most `2n/T`. These are supplied resources, not efficiency claims or finite-density limits.

Between observations the apparatus exactly balances finite-system and battery mean energy. Passive flag dephasing commutes with their additive free energy, so it preserves that ensemble balance too, although it can change program interaction energy and has an external readout cost. Endpoint energy bounds therefore control the cumulative battery/rotor ledger and interval-averaged transfer. The bounded observable `mathcal P_R` is the **target finite generator's** source current. Its measured expectation and second moment are approximated at the grid times; the theorem does not equate it pointwise with the autonomous apparatus's instantaneous battery-current operator. Uniform state closeness alone cannot establish convergence of time derivatives.

The existing finite clock remains recurrent with reversible flags and external observation times. It approximates bins (including multiple-event bins or complete ordered mark words), not exact continuous timestamps or irreversible autonomous records.

## 7. Explicit evaluation without large Hilbert spaces

The tail and resource choices can be certified with integer arithmetic. Let `X=ceil(x)`, `Y=ceil(y)`, `k=r+1≥max(1,6X)`, and `P2=(b+4X)²+16X`. Since the weighted-tail term ratio is at most one half for `n≥k`, `k!≥(k/e)^k`, and `e<3`,

\[
X_2\le2^{Y+2X}P2,\quad
Y_{0,r}\le2^{1+Y-k},\quad
Y_{2,r}\le(b+4k)^2 2^{1+Y-k}.
\tag{22}
\]

Increasing k makes every bound in (10), (17) and (18) small; integer coefficient bit lengths certify this without evaluating enormous exponentials. `check.py` evaluates one deliberately loose `L=24,K=δ=κ=T=1` resource example and a finite grid choice, together with local count/field-range algebra and the correct boundary-loss discriminator. No matrix on the actual torus is constructed.

The executed example has `M=3456`, `v=17915904`, `g=2073600`, `x=18952704`, `k=336531472` and radial cutoff `R=1346132804`. All five rotor bridge errors in (10), (17), (18) are certified below `2^(-100)` by integer inequalities. The loose encoding bound is 1,347,840 system qubits. Choosing three passive observations and `ν0=1/[1000(1+bar h_R²+bar p_R²)]` makes each apparatus process/moment contribution less than `1/1000`. The sufficient collision count has 382 decimal digits and the clock dimension 384; the battery gap-count bound is `2^1347840−1`. These deliberately enormous numbers demonstrate a finite construction with disclosed cost, not a feasible design or lower bound.

The exact controls checked 9,720 legal original B words, three successive local star births followed by a vanishing fourth, 1,220 four-hop return paths (896 move B occupations while preserving their count), and 41 field-safe Dyson word comparisons with nontrivial electric phases. A separate graded one-rotor fixture detects the missing positive boundary flux if `P_R ΓP_R` is incorrectly used. That fixture is an algebra control, not a replacement for the actual source law. The standard-library run took about 0.11 seconds and reported `TOTAL: PASS=6 FAIL=0`; `results.json` and `run.log` contain the exact values and resource integers.

## 8. Remaining scope

This closes a mathematical finite-horizon rotor-to-finite-system process/moment bridge for the specified initial preparation and supplied law, subject to independent confirmation of this new proof. It does not select that law, prove a spatially local or sustainable reservoir, give uniform infinite-volume/infinite-time bounds, price a physical irreversible reader, or identify a gravitational stress tensor. General energy-injecting rotor testers, exact autonomous event times, and pointwise autonomous-current convergence require additional results. None is smuggled into the finite-dimensional apparatus composition.
