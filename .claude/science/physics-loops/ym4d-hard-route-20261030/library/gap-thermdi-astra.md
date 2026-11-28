# Repo search

Research decision probe for FINISH row 905 (gap-thermdi-astra), started 2026-11-13. Target: box-uniform mean transport (THERM-DI) on the coupling or pin path, sufficient to carry GLUE-1 from the proved range into the band. Research text only; no scientific status is granted. Computations may guide or refute and do not discharge any claim.

Author: Codex (row 905 assignment: gpt-6-astra, max). No independent check. The result is OPEN for the actual SU(2) transport bound; the new calculations and their precise limits are below.

## Step 1 — entry and prior-work gate

- READ: `library/prior/gap-thermdi-astra.md` was checked first and is absent in this checkout.
- READ: The source/ownership checks and bounded searches requested at entry are recorded in Steps 2–3. The supplied SA commit cannot be independently recovered from its plain source directory.

## Step 2 — source and ownership gate

READ: checkout HEAD is `a0a0097b5fec1587e5899c59597ffb44c652fcec`, branch `lanework`. The supplied SA directory is a plain source directory, not a Git checkout; `31a47c543775` is the supplied provenance, not a revision independently recovered there. GOAL and FINISH's specified sections were read. The sparse checkout lacks SCIENCE_WORKFLOW; its current map, RULES, and research procedure were read through `origin/main` in the full repository.

The five searched refs resolve to:

| Ref | Revision |
|---|---|
| origin/main | 7fc6b1a3e6444d74c873c3ffc111b9ad0f4fe172 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Searches used bounded `git grep -n -i -E ... -- '*.md' '*.tex' | head` across all five refs. Initial wide terms (`mean.*transport`, `Feynman.Hellmann`, `sum.rule.*plaquette`) filled the cap with other objects; they establish no absence. The narrower search `THERM-DI|GLUE-1|VIR-log|NOCRIT|thermal transport|thermal mean|Michael.*sum.rule|sum.rule.*thermal` returned only unrelated thermal-current and electric-defect notes, with no exact target-label hit. Those notes concern three-spin currents or electric penalties, not a normalized Wilson thermal trace. A gauge-specific method search follows below.

READ: the dated prior digest's scope and recovery decision (lines 1–53 and 499–530), together with a search of its headings and target terms, concern RG admission and history suppliers. No THERM-DI supplier was found there. Searches of `open-registry.md`, `open-core.md`, and `l17c.md` for THERM-DI, GLUE-1, NOCRIT, VIR-log, thermal, pin path, and coupling path found no ownership hit. The assigned row 905 remains the exact probe; row 898 supplies its proposal, not its proof.

READ: `gap-next3-max.md:508–518` asks for a mean inequality and explicitly calls the SU(2) pin transition statement GUIDE. Its C8 (`346–347`) recalls Michael-type lattice sum rules without reading them. No physical lattice-spacing derivative will be imported from that recollection. The directly defined derivative here will be thermal time at fixed spatial lattice box.

## Step 3 — exact prior results reused, not re-derived

The completed five-ref query `(Wilson|Yang.Mills|gauge).{0,90}(Feynman.Hellmann|thermal sum|coupling transport)|(Feynman.Hellmann|thermal sum|coupling transport).{0,90}(Wilson|Yang.Mills|gauge)` returned no hits. A broader Villain query found the finite-clock covariance/scaling/transfer notes on main and several PR refs, then reached its cap. Those concern a different, finite-clock law; no exhaustive absence claim follows. The current library points to this actual method predecessor:

| Source read | Exact statement and proximity |
|---|---|
| `origin/main:docs/NATIVE_GAUGE_TRANSFER_BLOCK_HELLMANN_MONOTONICITY_RUNG_EIGHT_BOUNDED_NOTE_2026-06-12.md:45–141` | Finite SU(3) packet-block identity `d log(lambda_i)/d beta = <u_i,(J-I)u_i> + <E_beta u_i,D'_beta E_beta u_i>/lambda_i`; its two-state difference is the proposed monotonicity test. The source explicitly does **not** prove eventual monotonicity. Same derivative method, different operator and no thermal or box-uniform inequality. |
| `gap-glue-max.md:205–209`; check `gap-glue-check-astra.md:440–460` | `X(beta,t;b^3)=6tb^3 int_0^beta [u_ev,t(s)-u_inf(s)] ds`. This already supplies the coupling plaquette identity, including the signed twist mixture. Reused below. |
| `gap-glue-max.md:270–279`; check `gap-glue-check-astra.md:334–400` | `-E'_j/E_j<=C` implies `S_ev(beta_1,t;B)<=S_ev(beta_0,t exp(-C Delta beta);B)`. The corrected seed construction uses starting shape `(n,(4n)^3)`. This is conditional transport, not a supplier of C. |
| `gap-next3-check-astra.md:220–245` (row 902) | The **mean** differential inequality gives the same comparison along `t'=Ct`, with fixed spatial box, fixed invariant sector and differentiated traces justified. Already done; not re-proved here. |
| `gap-next3-check-astra.md:247–269` | The fundamental pin breaks pure-gauge centre flips. HL supplies a full pinned partition function, not an invariant even-sector trace. The U(1) transfer bridge is not supplied there. These conclusions are reused, not new claims of row 905. |
| `gap-exit-max.md:463–513` (row 861) | `d_h log A_T(h)=4\|T\|e_T(h)`; HL integrates it to `log Z_T=6 beta \|T\|-4\|T\|int_0^infinity e_T(h)dh`. Local comparison holds for `beta<2/9` or `h>24 beta`. This supplies the pin derivative, not transport through the remaining strip. |
| `gap-vir-sc.md:65–106` (row 710, Claude Fable 5.2) | After vacuum subtraction, `-beta E'_j <= E_j/log(4/beta)+beta \|B\|(9+12/log(4/beta))`. Its finite-box bound is `K_B=1/[beta log(4/beta)]+\|B\|(9+12/log(4/beta))/m_B`. It is not box-uniform. Its electric-only Proposition EL does give a uniform rate. |

**Overlap decision:** the identities, characteristic comparison, and pin-sector defect are already covered. The assigned **decision about a box-uniform mean rate** is explicitly OPEN in row 902. Only that uncovered probe continues. No new lane on the covered results is opened.

Outline search used `sa-index/README.md`, chunk files, and `obligations.md`, with thermal, transfer, GL8, mass gap, pinning, Villain and Hellmann terms. Neighbour rows were read at chunk 02:94–105 and obligations:20–28,1493–1501. The cited source is SA:2195–2257,2313–2335: positive SU(2) one-link Fourier coefficients and `Z_s(0)=Tr L^s` (GL8). These are cited constructions, not rebuilt. SA:31871–31882 explicitly separates a mass gap from scalar reconstruction. The CA full index search found no thermal/pin/Villain/Hellmann supplier; its mass-gap hit is a conditional scalar-decay proposition. None is THERM-DI. Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their account. Balaban's UV estimates are not an infrared thermal derivative bound.

# THERM-DI decision probe

The sum rules and tests below leave a box-uniform **relative** bound OPEN. The coupling inequality survives these tests as an SU(2) conjecture. The pin version needs the full-trace repair, whose starting family is supplied in Step 7.

## Step 4 — C8 with the actual derivatives

Use `t` for the thermal time called `a` in GLUE-1, `h` for pin strength, and `B=b^3` for the fixed spatial box. Neither derivative below changes lattice spacing or differentiates the integer box size. `PROVED` below means a written argument in this research note, not checked or retained status.

### 4.1 Coupling path — READ identity, exact relative-bound target

Let `P_ev` be the pure Wilson centre-even projection. Set

\[
 Z_{\rm ev}(t)=\operatorname{Tr}(P_{\rm ev}T_\beta^t),\quad
 X_\beta(t)=\log Z_{\rm ev}(t)-t\log\lambda_0(\beta),\quad
 H_\beta=-\log(T_\beta/\lambda_0)\big|_{\rm ev}.
\]

For integer `t`, reuse row 895 and its check. If `u_ev,t` is the average **signed** plaquette in the positive mixture of the eight temporal-twist partition functions, and `u_inf` is the infinite-time plaquette average on the same spatial box, then

\[
 \partial_\beta X_\beta(t)
 =6t|B|[u_{{\rm ev},t}-u_\infty].                 \tag{C8-beta}
\]

Equivalently it is the thermal expectation of the total plaquette score minus `t/N` times its expectation on the long torus, as `N->infinity`. Subtracted constants in `exp[-beta sum(1-x_p)]` cancel. The long torus is taken at **fixed B** before any box limit.

For real `t>=4`, the spectral extension has

\[
 U_\beta(t):=-\partial_tX_\beta(t)
 =\frac{\operatorname{Tr}_{\rm ev}(H_\beta e^{-tH_\beta})}
        {\operatorname{Tr}_{\rm ev}e^{-tH_\beta}}\ge0.
\]

Thus the desired inequality at integer times is precisely

\[
 6|B|[u_{{\rm ev},t}-u_\infty]\le c(\beta)U_\beta(t). \tag{B}
\]

At noninteger times there is no literal torus with `t` time slices. Use the spectral score
`Tr_ev(T^(t-1) T')/Tr_ev(T^t)-lambda_0'/lambda_0` in place of the left side. Differentiated traces are part of the domain; row 710 supplies their finite-box control for the Wilson interval below 4. An identity at integer times alone does not justify the continuous characteristic argument.

### 4.2 Pin path — PROVED full-trace formulation; no even-sector transport

At fixed `beta`, write

\[
 Z_h(N;B)=\int\exp\{\beta\sum_p x_p+h\sum_\ell x_\ell\}\,dU,
 \qquad x_\ell=\tfrac12\operatorname{tr}U_\ell.
\]

Let `v_h,N` average the pin observable over **all** `4N|B|` oriented links. On a rectangular torus different orientations need not have equal expectations. Finite-volume differentiation gives

\[
 \partial_h\log Z_h(N;B)=4N|B|v_{h,N}.            \tag{P1}
\]

Dividing each link weight by its one-link integral subtracts the same scalar from both volumes and changes none of the following differences. This is exactly HL's derivative, with its one-link centering cancelled.

For completeness the full pinned trace has a positive transfer realization. On `L^2(SU(2)^E)`, let `R(g)` be the spatial vertex-gauge action. Here `C_beta` uses the unshifted one-link kernel `exp(beta x(UV^-1))`; it is the product convolution of SA GL3 multiplied by `exp(3 beta |B|)`. Define

\[
 Q_h=\int\prod_{x\in B}e^{h x(g_x)}R(g)\,dg,
 \quad
 M_h(U)=\exp\!\left\{\frac\beta2\sum_{p\ {m spatial}}x_p(U)
                   +\frac h2\sum_{\ell\ {m spatial}}x_\ell(U)\right\},
 \quad T_h=M_h C_\beta Q_h M_h.                    \tag{P2}
\]

`Q_h>=0`: decompose the compact vertex-group representation into irreducibles; each central Fourier coefficient of `e^(h x)` is nonnegative by SA GL3 (at zero only the trivial representation survives). `C_beta` commutes with `R(g)`, so it commutes with `Q_h`; their product is positive. Multiplication by `M_h` preserves positivity. `C_beta` is trace class and the other factors are bounded for fixed B and finite parameters. Integration of one slab's temporal links gives `C_beta Q_h`; multiplication around the time circle gives `Z_h(N;B)=Tr T_h^N`. Its continuous kernel is strictly positive, so the top eigenvalue is simple, as in the unpinned transfer construction. Here no gauge projection is imposed for `h>0`.

Explicitly, its kernel is `M_h(U) M_h(V)` times
\[
 \int\prod_x e^{h x(g_x)}
       \prod_{\ell=(x,y)} e^{\beta x(U_\ell g_y V_\ell^{-1}g_x^{-1})}\,dg.
\]
The factors in the second product are exactly the temporal plaquettes of one slab. The two half spatial/pin weights join once per slice in the trace.

At `h=0`, `Q_0=P` is gauge averaging, and `M_0` commutes with it. The nonzero spectrum of `T_0` is the ordinary pure-gauge spectrum; all extra gauge directions have eigenvalue zero. This gives a full-trace endpoint, not an even-sector family at positive h. The already established centre-flip defect in row 902 remains.

Define `X_h(t)=log Tr T_h^t-t log lambda_0(h)` and `U_h(t)=-partial_t X_h(t)`. At integer `t`, differentiating the simple top eigenvalue, or taking the long-time limit of (P1), yields

\[
 \partial_hX_h(t)=4t|B|[v_{h,t}-v_{h,\infty}].     \tag{C8-pin}
\]

For example, derivative convergence follows by separating the simple top eigenspace in `Tr(T_h^(N-1)T_h')`; the remaining term decays relative to `lambda_0^(N-1)` at fixed B. All finite-box kernels and derivatives are bounded on compact parameter intervals.

The forward path to the target is `s=h_0-h`, **not** increasing h. Its required relative bound is

\[
 4|B|[v_{h,\infty}-v_{h,t}]\le c_h(h)U_h(t).       \tag{P}
\]

The sign is opposite to the increasing-pin derivative. At real times use the spectral score as above. A bound (P) for this **full trace** would give `S_ev<=S_full` at `h=0`. It requires a starting full-trace seed family and an integrable `c_h` through `0<h<=h_0`. Step 7 supplies the starting family by composing HL2 with the trace algebra. The integrable relative bound remains OPEN.

### 4.3 What C8 does and does not buy

PROVED reduction: the numerator in (B) or (P) is an expectation difference, with its extensive vacuum term subtracted. The denominator is a thermal excitation energy. Positivity of each measure and boundedness of a plaquette/pin observable give no relative estimate when that energy is small. In particular, bounding the two expectations separately leaves a factor `|B|`; row 710 already exhibits that precise loss. Michael's or Karsch's physical anisotropy sum rules are not used. The prior literature digest `prior/gap-vir-lit.md:21–33` only read abstracts and supplies no rigorous THERM-DI constant.

## Step 5 — does taking the mean evade a closing level?

### 5.1 The actual ratio — PROVED

For a fixed invariant trace family put `E_0=0` and `E_j>0` for its excited energies. Wherever the differentiated traces converge,

\[
 R_B(s,t):=\frac{\partial_sX}{-t\partial_tX}
 =\frac{-\sum_{j>0}E'_j(s)e^{-tE_j(s)}}
        {\sum_{j>0}E_j(s)e^{-tE_j(s)}}.            \tag{R}
\]

This is an **energy-weighted** average of `-E'_j/E_j`. The Boltzmann normalization cancels. It need not bound every level. But suppression of one low mode in the numerator also suppresses the same mode in the denominator. That cancellation is the failure mechanism tested below.

There is a useful precise distinction. If (THERM-DI) holds throughout the parameter interval for all `t>=t_*(B)`, its already-proved characteristic comparison implies

\[
 m_B(s_1)\ge e^{-I}m_B(s_0),\qquad
 I=\int_{s_0}^{s_1}c(s)\,ds,                    \tag{G}
\]

where `m_B` is the lowest positive energy in the trace family. This follows without following individual levels: for any trace time `t_0`,

\[
 e^{-tm_B}\le S_B(t)
 \le e^{-(t-t_0)m_B}S_B(t_0),\qquad t\ge t_0,
\]

so `-log S_B(t)/t -> m_B`; apply this to the characteristic comparison. Crossings and multiplicities cause no problem. Hence a uniform initial gap and a same-sector gap tending to zero along a sequence of boxes force

\[
 I_B\ge\log\frac{m_B(s_0)}{m_B(s_1)}\longrightarrow\infty. \tag{cost}
\]

This is a conditional obstruction to finite-cost transport, not a proof of gap closure for SU(2). It also shows why absence of a transition is weaker than the desired quantitative relative bound.

The seed consumer needs less than all times: it is enough to control `4<=t<=b/24`. On that restricted domain one cannot take `t->infinity` at fixed b. Thus (G) is not asserted from the restricted hypothesis alone. The following counterexample works even on that domain.

### 5.2 An exact mean counterexample at the seed shape — PROVED

For each integer `b>=96`, put `0<=s<=1` and

\[
 E_b(s)=\sqrt{(1-s)^2+b^{-2}},\qquad
 T_b(s)=\tfrac12\begin{pmatrix}
 1+e^{-E_b(s)}&1-e^{-E_b(s)}\\
 1-e^{-E_b(s)}&1+e^{-E_b(s)}
 \end{pmatrix}.
\]

This is a real-analytic family of strictly positive symmetric kernels. Its eigenvalues are `1` and `exp(-E_b)`, and its vacuum is simple. Thus

\[
 X_b(s,t)=\log(1+e^{-tE_b(s)}),\qquad
 R_b(s,t)=\frac{1-s}{(1-s)^2+b^{-2}}.              \tag{CE}
\]

At `s=1-1/b`, `R_b=b/2`, independently of t. In particular take `b` a multiple of 24 and `t=b/24`. This violates every fixed C on precisely the required aspect ratio. Moreover

\[
 \int_0^1 R_b(s,t)\,ds=\tfrac12\log(b^2+1)\to\infty.
\]

At the initial point the gap is at least one; at the endpoint the gap is `1/b` and `S_b(1,b/24)=exp(-1/24)`. Thermal averaging has removed no singular cost. Setting `h=1-s` gives the same example on a decreasing pin coordinate.

Scope: this is a two-state transfer family, not the four-dimensional Wilson or Villain measure and not a construction with spatial axis exchange. It refutes an inference from positivity, analyticity and taking the thermal mean alone. It does **not** refute THERM-DI for SU(2). All arithmetic and eigenvalues are displayed; no numerical run enters.

### 5.3 What the U(1) transition test establishes

ARGUED application of the stipulated closing-level test: suppose the U(1) path starts with a box-uniform gap in the sector being transported, and at a finite parameter has `m_b->0` in that same sector. Then the all-time version cannot have finite box-uniform integrated C, by (cost). If the photon level obeys `E_b<=kappa/b` and the initial thermal sums vanish along the enlarged seed family, the restricted seed-shape version fails too: characteristic transport would give `S_final(b/24;b^3)->0`, whereas this one mode contributes at least `exp(-kappa/24)`. No numerical critical coupling or transition order is required.

The failing mechanism is a loss of **relative** energy control, `-E'/E`, as the soft sector closes. It can occur in a narrowing parameter interval; every finite box can remain analytic and strictly gapped. On a pin path the identical statement uses `s=h_0-h`; the integral must include the closing point or endpoint. Reparametrizing to make a coefficient bounded does not help if the new path has infinite integrated cost.

READ / OPEN boundary for the actual Villain model: `prior/gap-lit-u1.md` credits Fröhlich and Spencer's high-coupling nonsummability theorem and an existential transition. The newer `gap-tu-retry.md:207–255` gives nonsummability of the plaquette score in every periodic local limit, but explicitly supplies a **Langevin**, not transfer, bridge. Row 902 already records this distinction. Neither the supplied sources read here nor the above two-state example proves the required centre-even finite-box transfer closing/scaling statement for compact Villain U(1). That application remains conditional on the task's closing-level premise. The Gaussian photon dispersion is GUIDE for that application, not an exact replacement for the interacting compact model.

**Decision from this step:** a genuinely closing sector defeats mean transport as well as levelwise transport. It does not decide whether the SU(2) sector closes. The comparison cannot be used to discard a specifically SU(2) estimate merely because a generic argument would also apply to U(1).

## Step 6 — the three requested controls

### 6.1 SU(2), leading strong coupling — READ coefficient; GUIDE transport

`gap-seed-sc.md:183–191` already computes the first winding coefficient. When all spatial sides exceed four, the `3|B|` minimal cycles are contractible plaquettes. Their tube contribution is centre-even. The resulting leading thermal model is

\[
 S_*(\beta,t;B)=3|B|(\beta/4)^{4t},\qquad
 E_*(\beta)=4\log(4/\beta).
\]

For `X_*=log(1+S_*)`, direct differentiation gives

\[
 \frac{\partial_\beta X_*}{-t\partial_t X_*}
 =\frac1{\beta\log(4/\beta)}.                    \tag{SC}
\]

The multiplicity cancels. This is PROVED algebra for the displayed leading model and GUIDE for the actual theory. The exact source coefficient is at integer time and fixed box; it does not bound derivatives of the remainder uniformly in box and time. It is not a controlled approximation at `beta=0.36`, still less throughout `[2.3,2.6]`.

An actual uniform comparison in a solvable SU(2) variant is already supplied by row 710, Proposition EL: with spatial plaquettes omitted, for `0<beta<=2`,

\[
 c_{\rm EL}(\beta)=
 \frac{1+\beta^2/6}
 {\beta[\log(4/\beta)-\beta^2/8]}.
\]

READ: it bounds every level and hence the thermal mean. It passes the algebraic test but is a different action. The full Wilson estimate retains the volume term recorded in Step 3.

### 6.2 Z2 at large beta — READ fixed-box control; ARGUED derivative test

Reuse `gap-es1-opus.md:126–168`, especially Lemma Z2-c; do not redo its flat-holonomy count. With `q=exp(-2 beta)`, its finite transfer matrix is, up to a scalar,

\[
 T=D^{1/2}KD^{1/2},\quad D(\sigma)=q^{f(\sigma)},\quad
 K=\bigotimes_{\ell}\begin{pmatrix}1&q\\q&1\end{pmatrix},
\]

restricted to gauge-invariant functions. There is exactly one flat vector in each electric sector. On the even sector the limiting matrix has rank one, and the source proves

\[
 S_{\rm ev}(t;B)\le d_0[2(1+q)^{N_B}q^4]^t
 \quad\hbox{if }(1+q)^{N_B}-1<1/2.              \tag{Z2}
\]

This is a fixed-box result; its smallness condition depends on the number of links `N_B`.

The derivative test can be read without mistaking an upper bound for a derivative bound. Put `r=exp(-beta)`. Every matrix entry above is polynomial in r. In the even sector the top eigenvalue is a simple nonzero root at `r=0`, hence analytic there. For each fixed integer t, `S_ev` is analytic in r, vanishes at zero, and is positive for `r>0`. Its first nonzero Taylor term is `c r^k`, with `c>0,k>0`. Therefore

\[
 \partial_\beta X_{\rm ev}=-k c r^k(1+O(r))<0
\]

for sufficiently large beta at this fixed B and t. The inequality passes there with `C=0`. This is an ARGUED application of the finite transfer identification used by the source and simple-root analytic perturbation. It gives no uniform onset in B or t and no bound across the transition from strong coupling.

Nor does it exempt all finite groups. The existing Q8/2T even flat degeneracy in row 902 survives centre projection. That already-refuted exemption is not restored here.

### 6.3 Two-dimensional heat-kernel gauge theory — PROVED exact control

The area-only spectral form is recorded for Wilson weights in `gap-form-exercise.md:514–524` (there marked recalled). Here the heat-kernel normalization makes the test exact. Define its one-plaquette character expansion by

\[
 K_\beta(g)=\sum_{j\in\frac12\mathbb N_0}(2j+1)
 e^{-j(j+1)/(2\beta)}\chi_j(g),\qquad\beta>0.
\]

On a spatial circle with b links, gauge-invariant functions are class functions of the total holonomy: gauge fixing a spanning path leaves one link, with residual conjugation. Their orthonormal basis is `chi_j`. Integration of one link against `K_beta` multiplies its spin-j matrix coefficient by `exp[-j(j+1)/(2 beta)]`, directly by character orthogonality. Applying this to the b links gives

\[
 E_j(\beta;b)=\frac{b j(j+1)}{2\beta},\qquad
 X(\beta,t;b)=\log\sum_j e^{-t b j(j+1)/(2\beta)}.
\]

The SU(2) centre-even trace uses integer j only. Either trace obeys the exact identity

\[
 \partial_\beta X=-\frac{t}{\beta}\partial_tX.    \tag{HK}
\]

All differentiated series converge, since their terms are a polynomial in j times `exp(-c j^2)` on compact positive parameter/time sets. Thus `C=1/beta_0` suffices on any `[beta_0,beta_1]`, uniformly in b; the sharper integrated cost is `log(beta_1/beta_0)`. The full U(1) two-dimensional heat-kernel trace has the same calculation with `j(j+1)` replaced by `n^2`. Being abelian does not by itself fail THERM-DI; the four-dimensional closing-sector mechanism matters.

**Control decision:** none of these three tests refutes a specifically four-dimensional SU(2) inequality on a finite positive coupling interval. None supplies its constant. The Villain closing-sector test refutes a common transport argument across that closing sector, subject to the precise bridge in Step 5.3. It is not a counterexample in SU(2).

## Step 7 — the repaired pin path has a supplied starting family

PROVED composition from READ HL2 and the trace algebra; this resolves the starting-family question left in Step 4.2. Fix `beta>0`, choose `h_0=78 beta`, and put

\[
 \Phi_h(n)=16\log Z_h(n^4)-\log Z_h((2n)^4),\qquad
 d_n=n/2-5/2,\qquad n\ge8.
\]

Normalizing the four link weights per site cancels in Phi. HL's pin differentiation, followed from h to infinity, gives

\[
 \Phi_h(n)=-4(2n)^4\int_h^\infty[e_n(q)-e_{2n}(q)]\,dq.
\]

The upper endpoint is zero because the normalized measure concentrates at the all-identity configuration. HL2 (`gap-exit-max.md:483–497`) therefore gives

\[
 0\le\Phi_{h_0}(n)\le
 \delta_n:=4608\beta n^4\frac{2^{1-d_n}}{d_n-1}\longrightarrow0. \tag{PIN-start}
\]

The nonnegative sign and the next step require no centre symmetry. The full pinned partition function is symmetric in all four axes and has the positive trace realization (P2) in each axis. Apply precisely Theorem D(a,b), `gap-crux-restate.md:90–104` (their proofs use only these facts), to obtain

\[
 X_{h_0}(n;(2n)^3)\le\delta_n.
\]

Lemma E', as stated in `gap-seed-shape.md:58–70`, enlarges one side from `2n` to `4n` at time n with factor four. Three enlargements give

\[
 g_n^{\rm pin}:=X_{h_0}(n;(4n)^3)\le64\delta_n\to0.
\]

Thus the pin repair is concrete: its starting full-trace family follows from the existing strongly pinned estimates and the positive transfer construction. Its missing input is (P) through the remaining pin interval with finite box-uniform integrated cost. At the unpinned endpoint its full seed would also bound the centre-even sum. This is a stronger consumer than the proposed glue-only family, and it remains OPEN.

## Step 8 — exact surviving crux and decision

### 8.1 Coupling statement that would suffice — OPEN

Choose a fixed `0<beta_0<0.3609` in the supplied proved region. The surviving question is whether there are `beta_1 in [2.3,2.6]` and a finite `C>=0` such that, for **every integer b>=96**, every real `4<=t<=b/24`, and almost every `beta in [beta_0,beta_1]`,

\[
 \partial_\beta X_{\rm ev}(\beta,t;b^3)
 \le -C t\,\partial_tX_{\rm ev}(\beta,t;b^3).    \tag{THERM-DI-beta}
\]

The same statement with `C` replaced by a nonnegative box-independent integrable `c(beta)` suffices. The derivatives and traces are those in Step 4. This asks neither a supremum over external fields nor a bound on every eigenvalue. At integer times it is exactly (B); at noninteger times it requires the spectral-score version. No value of C, and no integrable majorant, has been obtained for the actual Wilson interval.

The corrected row-896/902 consumer is precise. Set `I=int c`, `M=exp(I)`. From the supplied strong-coupling seed and SH/E', use the already-established family
`g_n=X_full(beta_0,n;(4n)^3)->0` along the supplied seed enlargement sequence. Put `a_1=ceil(Mn)` and `b=24a_1`. The characteristic stays in `n<=t<=b/24`, so

\[
 X_{\rm ev}(\beta_1,a_1;b^3)
 \le[8(M+1)]^3g_n.                               \tag{consumer}
\]

Choose n with the right side at most `log(11/10)`. This gives exactly GLUE-1. This is the prior conditional consumer, now with its sufficient derivative domain stated; it is not a new seed proof at order-one coupling.

### 8.2 Pin statement that would suffice — OPEN

At one fixed `beta_1 in [2.3,2.6]`, take `h_0=78 beta_1` and the full trace from (P2). Ask for a nonnegative `c_h` with
`int_0^h_0 c_h(h)dh<infinity`, independent of b, such that

\[
 -\partial_hX_h(t;b^3)
 \le-c_h(h)t\,\partial_tX_h(t;b^3)               \tag{THERM-DI-pin}
\]

for the same b and t domain and almost every `0<h<=h_0`. A finite constant is a stronger sufficient version. Use `g_n^pin` from (PIN-start) in (consumer). The endpoint follows by continuity at `h=0`: `Q_h->P` in operator norm, `T_h->T_0` in trace norm, and integer powers and the simple top eigenvalue converge. The endpoint full trace bounds `S_ev`. The pure-gauge centre-even trace at positive pin is not the object in this repaired statement.

### 8.3 Decision, with its limits

- **PROVED:** the relative-rate formula (R), finite-cost gap obstruction with its all-time hypothesis, and the explicit counterexample (CE), including on the seed shape. Mean averaging does not evade a closing soft sector in these precise senses. The heat-kernel control (HK) shows that a box-uniform inequality can hold in an exact gauge model.
- **READ:** coupling C8, conditional transport and its corrected seed consumer, HL/HL2, the volume-loss estimate, the pin-sector defect, and the finite-group scope corrections. These were already in the repository and are credited above.
- **PROVED given those READ inputs:** the full pinned transfer construction, pin C8 with the correct orientation, and its strongly pinned starting seed family. They identify a valid replacement for the broken even-sector pin proposal.
- **ARGUED:** failure of finite-cost transport for the stipulated U(1) closing sector; the actual Villain transfer application still needs the stated bridge. The fixed-box Z2 large-beta derivative test passes, with no uniform transition claim.
- **GUIDE:** the leading SU(2) estimate (SC) as a statement about the actual interacting theory, and photon finite-size scaling when used for compact Villain. No numerical proof or numerical job was run.
- **OPEN:** THERM-DI-beta and THERM-DI-pin for SU(2), any uniform C or finite integrated substitute through the unproved region, and GLUE-1 at a coupling in the band. The tests do not justify declaring these SU(2) inequalities false. They also do not supply them. The literal centre-even pin path was already invalidated by row 902.

The decision probe therefore leaves a **surviving, specifically SU(2), OPEN crux**, not a generic new transport theorem. An identity for plaquette or pin differences does not bound their ratio to the thermal energy. The decisive next input would be a uniform bound on (R), equivalently (B) or the repaired (P), in the actual measure. Repeating positivity, analyticity, or the same sum rule would not address that input. No continuum or first-passage conclusion follows from a finite bare-coupling interval.

## Final checkpoint and verification

Source checkpoint: the lane and five repository refs are pinned above; SA supplied provenance is `31a47c543775`. The actual CA index mass-gap hit was checked at CA-III:108223–108271: `10.7:prop-clustering-mass-gap` **assumes** a positive gap in its second clause to deduce reflected decay. It provides no gap or transport estimate. Balaban's cited UV-stability material (`lit-balaban.md:147`) is credited as background and supplies no input to this probe. No Balaban paper was fetched or represented as read.

Only this research file was written. Checks are the displayed hand calculations, source comparisons, and a self-read of the final text; no independent check or audit was run. Relevant completed results were reused as inputs. The open obligations and the next discriminating input are in Step 8.3. Work is local and uncommitted; no queue, registry, ledger, source manuscript, remote ref, or scientific status was changed.

RESULT: THERM-DI survives only as the explicitly stated OPEN SU(2) crux; a closing sector forces divergent all-time transport cost, and the literal even-sector pin path is invalid, while a full-trace pin repair has a supplied starting seed but no uniform rate through the remaining strip; GLUE-1 in the band remains OPEN.
