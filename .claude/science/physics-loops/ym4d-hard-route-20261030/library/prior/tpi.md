# TPI-FREE: prior-work digest before tasks 13.1–13.2

Codex, 2026-11-08. Research text, not an audit; grants no status.
Checkout: `6e8679a00ee6642b94862bbdcc451629ae604b14`.
SA means Sussman–Alpoge's `YM4_sketch_500.tex`; CA-II means
`theorem_0_complete_account_raw_II.tex`, supplied at `31a47c543775`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, and Tadeusz Balaban for the cited free-field machinery.

**Result.** The finite Gaussian algebra is already available and checked
in P3. P3 also carries the desired background estimate as an explicit
conditional input. The remaining task is its application to TP1's precise
tower, scales, admissible tori and terminal background. It is not another
proof of orthogonal conditioning or of P3's conditional inequality.
The newer outline also states the coarse residual estimate explicitly;
see §6 before launching any proof work.

`library/prior/tpi-prior.md` is absent. `library/open-registry.md:501`
assigns this package to `TP1-FREE`, owner `TP1`, status `OPEN`:
“the bound on R_j is additional to a bound on the slices.” Searches of
that registry, `open-core.md`, `l17c.md` and FINISH found no separate owner
of this residual join. This digest does not launch its proof lane.
`cp-triage.md:621–630,661–673` explicitly requests identification and units,
“not another proof of that bound.” The older `port-map.md:43,46,151`
calls FREE proved there; P3's retained hypotheses qualify that shorthand.

## 1. Exact consumer contract and convention

`tp1.md:9–11,41,52,71–87` fixes odd L, M=L^{m_0}≥5,
compatible physical torus side ℓ=2L^m, m≥m_0, cutoff a=L^{-K},
and **TP1 spacing** a_j=L^j a, 0≤j≤K. A plaquette index includes
one fixed orientation for each of the six coordinate planes.
All constants must be independent of K, j, volume, position and the test
pair, after fixing the construction parameters. This is the free,
one-colour **unit-coupling** covariance P of the standard Gaussian on
E=ran d_1, with plain coordinate inner products. Running factors x_i^{-1}
belong to (2.6), not to G_i or R_j.

The minimal free package, for every compatible torus, is

\[
 R_0=P,\quad G_i\succeq0\ (1\le i\le K),\quad R_j\succeq0,\quad
 P=\sum_{i=1}^{j}G_i+R_j\quad(0\le j\le K),
\]
\[
 |G_j(p,q)|\le C(a/a_j)^4e^{-\delta d_{\mathbb T}(x_p,x_q)/a_j},
 \qquad |R_j(p,q)|\le C(a/a_j)^4\quad(1\le j\le K). \tag{FREE}
\]

The terminal background **R_K is retained**, not set to zero. At K,
a_K=1 in TP1 units, so the requested upper bound is Ca^4=CL^{-4K}.
Stopping the Gaussian model at a zero terminal *field* does not make
the unconditioned terminal *covariance* vanish. `tp1.md:87` says
“The source decomposition does not say R_K=0.”

The source convention is explicit, rather than a choice of any convenient
positive slices. SA:7634–7649 defines the plaquette averaging map A^{(j)},
W_j=E⊖(E∩ker A^{(j)}), and states
“F=P_{W_K}F+sum …” at 7644. SA:26028–26036 gives the equivalent dictionary

\[
 R_j=C^{\mathrm{bg}}_{K,K-j}=P_{W_j},\qquad
 G_j=\mathcal C_{(j)}=R_{j-1}-R_j.
\]

SA:32521–32524 fixes its own physical a_s=L^{-s} and fine spacing
η_j=L^{-j} in level-j units. Thus its a_{K-j}=a_j of TP1 and
η_j=a/a_j. Its printed slice bound at 7646 and 26138 uses
η_{j-1}^4 and range a_{K-j+1}, hence TP1's a_{j-1}.
This is precisely a fixed one-level shift: for fixed L, multiply the
constant by L^4 and adjust the decay rate. `tp1.md:77` permits this.
That permission does not permit changing the underlying block map.

P3 uses attachment points, while TP1 uses barycentres
(`p3-free.md:170–180`; `tp1.md:11`). This bounded displacement only changes
fixed slice constants; it does not change the plaquette random variables.
Use periodic distance for global kernels and TP1's Euclidean lift on the
contractible test patch (`tp1.md:17`). Physical covariance density is a^{-4}P,
not P: SA:1686–1693. The residual target is a bound on raw entries,
equivalently |a^{-4}R_j|≤Ca_j^{-4}.

### Every use of (2.3) in TP1

| Lines in `tp1.md` | Use |
|---|---|
| 94–101; 313–325, (2.6), (5.3) | Positivity realizes independent Gaussian slices. Their shared tail has covariance C_{>max(j,l)}; the half-square identity gives (5.3). The model omits R_{k_1} deliberately. |
| 329–340 | The slice estimate gives the separated bound \(\lvert C_{>j}\rvert\le Cx^{-1}(a/r)^4\) and the early-slice tail D^4e^{-cD}. These allow replacement of early-index kernels by C_{>k_0}. |
| 342–359, (5.4) | The exact split retains R_{k_1}. Its bound gives \(\lvert R_{k_1}\rvert\le C(a/r)^4(DL^{-n})^4\), hence the last term of ε_ker. The middle-slice estimate also bounds the error from replacing x_i^{-1} by x^{-1}. |
| 361–369 | (5.4) replaces the squared kernels by x^{-2}P^2 in the early-level contribution, after recombining the profiles. |
| 371–385, (5.5) | Without separation of the enlarged profiles, summing the slice amplitudes gives \(\lvert C_{>v}\rvert\le Cx^{-1}(a/a_v)^4\). Support counting then bounds the late-level contribution. |

These are all direct mathematical uses. (2.4), separately, supplies the
continuum/Riemann-sum step at 389–397. FREE is assumed by Lemma 5.2
at 305–310 and Theorem 3.1 at 191. Downstream, Lemma 5.5 uses Lemma 5.2
(`tp1.md:465–474`); state transfer and the continuum/witness conclusions
inherit that dependence. The constants are fixed before later cutoffs
and volumes (`tp1.md:186–187`). The source table at 590 and definition
list at 613–614 explicitly record the residual correction.

`gates/tp1-gate.md`, “Lemma 5.2” and “Use of hypotheses”, reports a
line-by-line check by Claude, first failing step none, including (5.4)'s
terminal term. It checks the implication under FREE; it does not prove FREE.

## 2. What SA and the complete account already supply

**Exact free covariance: proved algebra.** CA-II:69516–69565 gives
P_ex=d_1 Δ_1^+ d_1^*, identifies it as the orthogonal projection onto
ran d_1, and gives the Green-function formulas. Its diagonal is
(1−|F|^{-1})/2. The proof begins: “The standard Gaussian law on a subspace
V … has covariance … Π_V.” Constant two-forms are excluded; potential
gauge directions need not be inverted to define this curvature law
(SA:1686). This gives positivity, not the small factor L^{-4j}.

**Gaussian squares and positivity: proved algebra.**
CA-II's `8.1:lem-kernel-positivity`, 69682–69837, computes the covariance
of Gaussian half-squares and the nonnegative squared-covariance kernel
for nonnegative tests. P3 §§1–3 ports this with its finite proofs checked.
Background specialization retains the free-potential/block realization.
Positivity of this quadratic-observable kernel must not be confused with
entrywise nonnegativity of a curvature covariance.

**Background and finite tower: proved conditional algebra.**
CA-II:69600–69659 defines A_B=E[A|B], F_B=dA_B and
C^bg=Cov(F_B), and splits P_ex=C^bg+C^fl. CA-II:69849–69912 proves
the finite orthogonal tower. Its last difference includes the conditional
mean at the final nontrivial sigma algebra, because the next sigma algebra
is declared trivial. It does not discard the last covariance.
The final paragraph, 69903–69911, identifies these with Balaban's actual
steps by the flat-step/free-field statement, “proved in this book as an
implication”. CA-II:145580–145582 also lists that identification as
“printed without proof” in Balaban CMP 95 §1, “cited as printed”.
These are qualifications on the identification, not failures of finite
Gaussian orthogonality.

**Slices: stated with cited/sketched analytic inputs.**
SA:7634–7649 and 26028–26036 identify nested curvature projections.
The proof pointer SA:7873 says “The only property … to be analysed is
its decay”, assigned to (1c) at identity. SA:26133–26154 factors the
slice through H_{j-1} C_j^tr H_{j-1}^*, states its exponential bound,
and describes the centered-block, mesh-uniform bootstrap. The index
(`chunk-07.md:111–114,173`; `chunk-24.md:45–50`;
`obligations.md:1329`) classifies the analytic part as sketched/cited.
Thus the slice estimate is not an unconditional new theorem established
by this digest.

**The full free continuum comparison already has a written proof.**
SA:1714–1731 states the volume-uniform a^{-4}P comparison with errors
(a/r)^{1/2}+(r/ℓ)^4. The proof ends at 1992–2017: “This proves
eq:lcc-main.” The index, chunk 02:39–40, marks it proved in detail.
Do not open a fresh lane for that kernel or its tensor constant.
It concerns the full P, not the coarse background R_j.

**The residual estimate is already asserted in the extraction.**
SA:26162 says the summed slices give C^bg_{K,s} minus
C^bg_{K,s−n}, “the subtracted term is ≤ CL^{-4k_1}”.
Since k_1 is a block level, this is exactly the required raw scale power.
The paragraph does not supply a separate all-level, compatible-volume
proof of that assertion. CA-II:69925–69965 supplies the stronger
conditional background estimate discussed next.
Neither orthogonality alone nor estimates for only G_1,…,G_K bound
the remaining R_K. One must bound that last background or invoke a
proved further decomposition which includes and controls it.

CA-II:145173–145218 explicitly labels the source lemma “Proof outstanding”.
Its weaker age amplitudes do not supply TP1 REG/AMP. At 145220–145222,
the continuum-background lemma says “The statement and proof … are not
written out here.” That is distinct from SA's written full-P comparison.

## 3. Existing repository suppliers and their limits

**P3: checked port of finite algebra and conditional bounds.**
`library/port/p3-free.md:453–460` already gives

\[
 |C^{\mathrm{bg}}(p,q)|\le C_u\eta^4(1+|x_p-x_q|)^{-4},\qquad
 |C_i^{\mathrm{step}}(p,q)|\le
 C_u\eta^4L^{-4i}e^{-\delta_\square|x_p-x_q|L^{-i}}.
\]

It expressly calls this “an application of a named hypothesis”.
CA-II:70002–70016 says (h1) supplies both bounds “for these kernels”.
The antecedents retained at P3:168–184,287,337–339,586–596 are:

| Input | What remains to be supplied when applying it |
|---|---|
| H-BG | The specified massless potential law, gauge/zero-mode convention, actual block map, conditional mean/minimizer identification, and Cov(dA)=P_ex. |
| H-TOWER | Equality of the finite conditional-expectation covariances with Balaban's unit-coupling flat RG steps. |
| H1-MIN | Linear-minimizer estimates and the free-current operator theorem, on its admitted geometry and parameter domain, including the displayed bounds for these covariance kernels. P3 retains this operational consequence as an assumption. |
| H3-CONT | A quantitative continuum comparison for the **background** squared kernel, with distance and depth floors. Tensor algebra alone does not prove it. |

H2-FLUX is also retained for P3's flux/lower-bound conclusions; it is
not needed just to apply the displayed upper bound. H3-CONT likewise
is not needed for the residual upper bound. CA-II:68722–68728 and
P3:343–344 fix η=L^{-k_0} and lengths in level-k_0 cells.
The intended substitution is k_0=j, η=a/a_j and x=x_phys/a_j.
After the covariance identification, dropping the spatial factor gives
the target directly, including on the diagonal. Check this substitution
at every admitted level, not just at the witness depth.

`gates/p3-free-gate.md` reports Claude's line-by-line check, first failing
step none. P3:592–596 incorporates it. It specifically says “(a) holds
only as the H1-MIN assumption”. Older “not yet checked” sentences at
P3:3,590 are superseded by that change log, not by a new check here.
The check also retains H-BG/H-TOWER and H3-CONT. Its mass-upper-bound
repair C1 is unrelated to the residual estimate.

**FP1: checked classical precision package, with a narrower scope.**
`fp1.md:9–50,91–102,145–168,170–262` defines the actual plain derivative,
the energy E_k(a)=min_{P^[k]w=a}||dw||², the soft-contour pivot precision,
and proves uniform current-scale gap and exponential kernels. It proves
equality of plain and straight **curvature minima**, in both directions,
by correcting gradients; it does not equate the two averaging maps.
Theorem 1 is uniform in depth and compatible tori. Lemma 7 includes
periodization and flat holonomies. These are existing linear suppliers.

`fp1.md:50,86–89,247–262,468–498` limits the conclusions to the stated
operators: current-lattice differences are not mesh-uniform physical
Green-density estimates. Identification with a nonlinear background
Hessian requires a stationary lift. The actual interacting energy,
counterterms and changed complex domains are not supplied.
`gates/fp1-gate.md` reports Claude's check, first failing step none;
the applied fixes and frozen status are at FP1:488–498.
Do not silently promote FP1 to all of H1-MIN or to TP1's REG/G-ID.

**Balaban: use the existing quotations, not an alleged new paper reading.**
`lit-balaban.md:6–13` is a search record: “no Balaban text reached”,
and its Balaban statements are “unchecked”. Its lines 34–35,85–86,145
locate CMP 95 (1.103), Proposition 1.2, (1.110), and CMP 96 Lemma 2.1,
(2.59)–(2.61), for the flat minimizer/decay machinery. SA:26141 quotes
H_k=GQ^*(QGQ^*)^{-1} and exponential bounds for G and ∇G, then explains
the centered-block adaptation. P3:287–327 and CA-II:69849–69912 attribute
the unit-coupling tower to CMP 95 (1.16)–(1.19), used in CMP 109.
Those quotations give the method and the attribution. They do not
independently verify Balaban's hypotheses for TP1 or erase its terminal
background. No Balaban paper was accessed in this task.

## 4. Structure of R_j and the scaling route

**Yes, on the identified free tower R_j is a covariance.** More precisely,
with Y_j=E[F|A^{(j)}F]=P_{W_j}F, it is Cov(Y_j)=P_{W_j}.
This is the background which remains after j steps, lifted back to bare
plaquettes. It is not the covariance of F−Y_j (that is P−R_j), nor the
coarse field covariance before lifting. These identifications are already
SA:7641–7649 and 26020–26036, and P3's F4/finite-tower construction.

Consequently \(0\le R_j(p,p)\) and
\(\lvert R_j(p,q)\rvert\le\sqrt{R_j(p,p)R_j(q,q)}\). P3:464–470 explicitly proves this
covariance inequality, including zero variance. A **uniform diagonal**
bound R_j(p,p)≤C L^{-4j} therefore suffices. Positive semidefinite does
not mean all off-diagonal entries are nonnegative. The elementary
projection bound R_j≤P≤I gives only R_j(p,p)≤1; it loses the required
power. A dimension/rank average is not a bound at every plaquette.

**Scaling is a route, not a discharge.** In level-j units the fine mesh
is η_j=a/a_j. A raw plaquette curvature is η_j² times the curvature
in those physical units; its covariance therefore has factor η_j⁴.
This is the origin of P3's factor and SA:26137–26141's minimizer factor.
One still needs a bounded rescaled diagonal for the actual minimizing
background, uniformly in mesh, volume and position. The blocked Gaussian
has the induced constrained quadratic action; it is not automatically
a fresh nearest-neighbor Maxwell law. Merely saying “four-dimensional
scaling” does not establish that bound. P3's conditional C^bg estimate
already supplies it once its identifications and hypotheses hold.

The terminal level presents the same question on the remaining coarse
torus. Declaring its sigma algebra trivial would integrate out its field,
changing the stopping convention. CA-II's completed finite tower includes
that last difference; TP1's finite sum through K does not include it.
This is why a slice-tail sum through K cannot replace a bound on R_K.

## 5. Minimal next statement, route and first hard step

**Prove only the FREE join in §1**, with the displayed dictionary
R_j=C^bg_{K,K-j}, G_j=R_{j-1}−R_j and the agreed one-level shift.
State each remaining supplier hypothesis explicitly if it remains open.
The all-level residual upper estimate needs H-BG/H-TOWER and the
applicable upper-bound content of H1-MIN, not a new H3-CONT proof.
The continuum full-P comparison is prior work. REG, AMP and the
Gaussian source-energy identification are separate tasks.

The likely route is to match the actual centered plain/soft-contour flat
step to the straight/tree curvature conditioning. Reuse FP1's equal
curvature minima and P3's Gaussian algebra. Then apply the existing
background estimate in level-j units for every j, including K.
If its admitted-domain check fails, isolate that missing supplier
statement; do not claim that scaling alone repairs it.

**First hard step:** write and justify the equality of the actual flat
step's induced curvature law with the orthogonal increment
P_{W_{j-1}}−P_{W_j}, including closed forms, harmonic modes, gauge
integration and normalization on the compatible torus. Distinguish
this from equality of variational minima. Then verify the upper-bound
supplier's all-level domain and units. Main risks are an incorrect
slice identification, a counting/physical-adjoint normalization error,
and accidentally discarding the terminal projection.

## 6. Newer outline: additional prior work to reuse

Optional source: `YM4_1400.tex`, supplied at `2bc0658f9`, at the exact
scratchpad path in the task. Only `rg -n` with bounded context was used.
Its relevant findings are:

| Lines | Statement and short quote |
|---|---|
| 4329–4340 | Defines the plaquette average, nested W_j, and explicitly retains **F=P_{W_K}F+Σ C_(j)F** at 4335. The slice estimate is at 4337; 4340 identifies the model with the linearization at identity. |
| 100448–100456 | Repeats the background-difference slices, “covariances of mutually independent pieces”. |
| 100989–101032 | States the slice factorization and bound at 100992–100994, then supplies a more detailed centered-block argument through the joint strong inverse. At 101026: “constants are uniform in the fine subdivision and in the volume”; 101027: “A raw bare plaquette curvature is h² d_h H_h”. Its referenced strong-inverse theorem was not checked in this digest. |
| 101043–101077 | Gives an explicit flat curvature comparison between plain/soft-contour and straight/tree laws, handling coarse closed forms, constants, gradients and normalized linear gauge integration. At 101075: “the same bare slice … in either gauge”. This already addresses the proposed first hard step; trace its premises before attempting an original proof. |
| 101079–101085 | Gives the fine fluctuation-complement bound and the scale sum recovering power-law decay. This is not alone a terminal-background estimate. |
| 102258–102281 | Defines its **G_j=C^bg_{K,K-j}** (this G_j is TP1's R_j), writes F_{j-1}=F_j+Z_j, and distinguishes zero terminal field from covariance subtraction: G_j°=G_j−G_{k_1}. It telescopes half-squares and states “the coarse covariance bound gives” \(\lvert G_{k_1}(p,q)\rvert\le CL^{-4k_1}\) at 102280–102281. |
| 102282–102291 | Retains both the product with the coarse covariance and its square in the smeared error, rather than dropping the terminal contribution. |
| 109003–109021 | Also gives P_ex=P_{E_C}+P_{E_perp} and independent Gaussian summands. This is the full/constrained-curvature split, not an estimate of TP1's multiscale terminal residual. |

Thus neither the free decomposition, the terminal residual's existence,
nor its claimed scale power is new. The newer text also contains a
substantial proposed identification argument. This digest did not check
its strong-inverse suppliers or find a separately verified theorem matching
every TP1 level and torus, particularly j=K. The next lane should first
trace those existing arguments. If they cover the full contract, port
and apply them; stop the original-proof attack. No novelty or closure
claim follows from the bounded searches recorded here.

**Recovery checkpoint.** Only this digest was written. No numerical or
computer-assisted proof, audit, proof lane, registry/status change or
external post was performed.
The supplied SA and CA-II files match P3's SHA-256 identities:
`d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`
and `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f`.
The index README, neighboring rows in chunks 02/07/24/30, obligations
and CA full-index rows were used before their cited excerpts. Existing
Claude checks are reported as records, not repeated independent checks.
The entry-point workflow file is absent in this pinned checkout.
Open decisions: exact flat-law identification and its supplier premises;
uniform admission at all levels; terminal background; unit conversion.

Digest by Codex (gpt-6.1-sol).
