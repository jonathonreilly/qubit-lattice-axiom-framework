# PRE-STATED — independent hostile review of SPHERE55

UTC: 2026-10-29 03:57:15 (tool clock, before derivations). Target: `SPHERE55.md`, including overriding errata E10–E13. Initial exposure: heading/string search, then E8–E13; no derivation or check has yet been performed. The source's approximate ~04:00 timestamp is not treated as an execution receipt.

Write scope: this file only. No git, no audit ledgers, no snapshots, no whole-file PROOF.md read. Exact rational/symbolic arithmetic in plain Python only. Locate source claims by string first; report line numbers from the inspected text. The two discretionary reads are the mandatory science methodology and its review-loop procedure; named scientific sources and named sp55_kill/sp55_seam check scripts are the scientific read scope. Unread criterion/output artifacts will not be represented as verified.

Targets and refutation criteria, stated before working:

1. T1: independently test radial topology, seam incidence for arbitrary radii, positivity and reflection pairing of all claimed RP planes, and compatibility of the local-spacing coupling rule with those pairings. One explicit permitted radius, cell, or reflection with the wrong topology/weight suffices to refute a universal assertion.
2. Check scripts: inspect their actual predicates and controls. Distinguish finite-sample checks from general proofs; identify circular, vacuous, unsatisfiable, or non-discriminating predicates. Do not infer preregistration from a PASS or a timestamp in prose.
3. T2: reconstruct the exact Haar integration identity, lattice transport and flux split, dilation cancellation, covariance disintegration, and E10's corrected quantifiers. A missing operator/contact term, unsupported cancellation, or allowed measure violating the stated bound refutes the corresponding implication.
4. T3: trace every consumer of separated N5, including observables touching or crossing the seam and reflections through the poles. Test whether the claimed restricted input actually reaches all claimed conclusions.
5. T4/T5: rebuild the group contraction and RP limit, and separate finite-R inputs from R-uniform ones. Test whether “all coarse fields” and moment hypotheses are really stated and sufficient, and whether “purely ultraviolet” overstates the conditional result.
6. Recompute seam Chern–Simons parity and its gauge variation; test the replacement exclusion mechanism with the actual seam field content.
7. Check symbol identities, frozen versus variable scales, inherited NOT-VERIFIED items, and any concrete PROOF.md line citations encountered. A stale citation or unstated domain restriction is a finding, not silently repaired evidence.

Finding verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED will be restricted to what is re-derived here; a conditional implication does not establish its inputs. Findings will be appended as they are established, followed by a summary table and exactly what may be banked.


## Finding 1 — digital ball and incidence bounds survive independent attack

**CONFIRMED; claim status PROVEN.** Source: `SPHERE55.md:129`, “Lemma 1.1”; `SPHERE55.md:755`, “E5”.

For a retained cube with centre ak, the whole box with half-widths a(|k_i|+1/2) is retained by coordinate down-closure. If q=tp is retained with t>1, p is strictly inside that box in every coordinate, including zero coordinates. Therefore a boundary ray cannot have a second retained point beyond it. Compactness, an interior neighbourhood of 0, and closedness of the boundary then give a positive continuous radial function: a convergent sequence of radial endpoints has its only possible limit at the unique endpoint in the limiting direction. Radial rescaling, extended by 0 at the origin, is a ball homeomorphism. This proof does not use vertex-link Euler characteristics or Moise's theorem.

Independently enumerate the nonempty proper down-sets I of the three transverse binary choices at an edge. There are exactly **18**, with cut-edge counts distributed as **{3: 2, 4: 9, 5: 6, 6: 1}**. Each boundary 3-face is precisely one edge of this cut. Thus 3<=k_e<=6 for every admitted radius. Around a square the analogous nonempty proper down-set of two binary choices has 1, 2, or 3 retained cubes; a non-boundary square has all 4. The enumeration used only `itertools`, integer comparisons and bit operations in an inline Python command; it did not reuse the author's face-count implementation. E5's cycle argument is also consistent with these cases.

The strict seam depth follows from an excluded neighbour cube with a vertex outside B_R at distance <=2a from the common boundary vertex. The generic-radius assumption supplies |v|<R. The incidence statements are bankable; the next finding limits their conversion into physical weights.

## Finding 2 — a constant-beta incidence formula was promoted to the variable-coupling action

**REFUTED as an exact numerical weight statement; claim status GAP (repair given).** Sources: `SPHERE55.md:162`, “beta_Q := 2N/G(a Omega(z_Q))^2”; `:166`, “beta^ = (beta/4) k_e”; `:184`, “every crossing weight is >= (3/4) beta”; E5's final weight bounds at `:768`; summary row 4 at `:683`. The symbol table at `:740`, “beta: the bulk bare coupling”, does not select a common evaluation point for this spatially varying quantity.

The actual formula is

    beta_hat_(e x I) = (1/4) sum_{c boundary 3-face containing e} beta_c,

not k_e beta/4 with one prescribed bulk beta. Here is an exact permitted counterexample in units of a, at R/a=23/10. Take the edge with doubled midpoint (-3,-3,-1,0), varying in the fourth coordinate. Its three incident boundary 3-faces have doubled centres

    (-3,-2,0,0), (-2,-3,0,0), (-2,-2,-1,0).

Their squared centre radii are **13a^2/4, 13a^2/4, 9a^2/4** and their conformal factors are **529/427, 529/427, 529/377**. Direct independent cube enumeration gives k_e=3. Writing beta(s)=2N/G(s)^2, the corrected weight is exactly

    [2 beta(529a/427) + beta(529a/377)] / 4.

On the weak branch of G-pert, d(G^-2)/dlog s<0, so this is strictly less than **(3/4) beta(a)**, and also less than (3/4) beta(529a/427). Thus the error cannot be repaired by silently using the equatorial bulk value beta(a).

Valid universal bounds use extrema over the incident cells:

    (k_e/4) beta_min <= beta_hat <= (k_e/4) beta_max.

For monotone G-pert, global sufficient bounds are **(3/4) beta(2a) <= beta_hat_cross <= (3/2) beta(a)**. Boundary squares likewise use a sum of m_D+2 actual cell weights. The constant-beta formulas become exact only in the frozen-coupling counting model, or with an explicitly edge-dependent average beta_e. Positivity, reflection pairing and exclusion of the beta_cross=0 counterexample survive. A quantitative comparison with a local bulk value needs this correction and a bound on profile variation.

## Finding 3 — both scripts reproduce, but several advertised checks cannot decide their claims

**CONFIRMED for reproduction only; REFUTED for the claimed scope of the individual predicates below.** Sources: `checks/sp55_kill.py:79–82,101–102,120–125`; `checks/sp55_seam.py:59,109,114–120`; `SPHERE55.md:121`, “Controls fired”, and `:145`, “Cell-level facts”.

Both scripts were executed with `python3 -B`, with no file output. Both printed `VERDICT: PASS`. The Killing script reported multipliers **2, 3, 14** at R=1,3/2,7 and all four controls fired. The seam script reproduced all five listed radii, including **896 of 5232** seam vertices of valence 8 at R/a=61/10. These numbers are not refuted. These are rational/integer finite checks, not general proofs.

Predicate audit:

- K1's sphere/hemisphere equations, K2's differentiated pullback metric, K3's divergence/conformal-Killing equations, K4's metric Killing equation, K5's equatorial expression and K6's inversion equation can fail under changed formulas. K7 fits a proportionality first, but then tests the independently specified value 2R; the final test makes it discriminating. The C3 no-op is indeed cosmetic: the subsequent diagonal comparison decides that control.
- K6's second comparison is a literal algebraic identity: `R - (-X5[4])` equals `R + X5[4]`, with the same numerator. It contributes no independent test of reflection transport.
- **C4 does not test non-radiality.** At R=1, c=e_1, x=e_1/2 the exact boost is **(5/4)e_1**, while its tested right side is **(1/2)e_1**. Thus C4 fires although the field is radial. The corrected test is a nonzero wedge component v_i x_j-v_j x_i. A valid explicit non-radial witness is x=e_2/2, c=e_1, where v=(3/4)e_1 and v wedge x has component **3/8**. This refutes the predicate's evidentiary interpretation, not generic non-radiality of boosts inside the equator.
- The seam script's `positive` is forced by its own construction: every square in `cellsD` was collected from a cube, and every edge in `cellsB` from a boundary 3-face. Hence m_in_D>=1 and k_e>=1 already hold for every nonempty constructed example. No actual beta_Q or signed action weight is supplied to this gate. Even the deliberately pinched two-cube control reports positivity=True.
- The seam final `ok` tests H(4), down-closure, the Euler counts, square incidence, vertex-link Euler characteristic, k_e>=3 and this tautological positivity. It does **not** test k_e<=6, the reported boundary weight range, absence of deficient non-boundary squares, generic-radius exclusion, valences, or RP. Those values are printed. The independent proof in Finding 1 supplies the incidence bounds; the runner alone does not.
- C1 and C2 do discriminate their named down-closure and pinch defects. C3 is a positive calibration case. Euler characteristic 2 alone is not a proof that every vertex link is a sphere; the ball proof is the needed evidence. The script candidly excludes its S7 arithmetic identity from evidence.

**NOT-VERIFIED:** criteria-before-execution provenance. The two discretionary reads were used for the required methodology/procedure. I did not read the separate criteria files or archived output files; a prose timestamp, E7 or E13 is not an independently verified preregistration receipt. No preregistration claim is banked.

## Finding 4 — the five reflection-positivity planes are valid for the corrected weights

**CONFIRMED; claim status PROVEN for gauge-invariant half-algebra observables.** Sources: `SPHERE55.md:259`, “Reflection positivity across the equator”; `:297`, “The four great spheres through the poles”.

Across the equator the crossing links form a matching. Gauge transformations at their north endpoints set each to 1 without a determinant, preserve product Haar measure and preserve gauge-invariant half-algebra observables. A crossing plaquette becomes W(W')^-1. For c>=0,

    exp(c Re tr(W W'^dag))

has a power-series expansion into monomials P(W) conjugate(P(W')) with nonnegative coefficients: expand the two bilinear terms of Re tr separately. Products preserve this form. Reflection-equal within-half actions then turn the integral into a nonnegative sum of absolute squares. The variable cell weights satisfy equality under reflection because the two copies have identical chart radii; only positivity, not a constant-beta formula, is needed.

For x_mu=0, all chart vertices have nonzero half-integer x_mu/a. Crossing chart edges are a matching between +/-a/2; each prism link preserves x_mu. A prism square over a crossing chart edge has two such matching edges, which gauge-fix to 1, leaving the two reflected prism links as W(W')^-1. Ordinary chart squares have the same standard crossing form. The radial beta_Q values are reflection paired. Thus all four pole-centred coordinate reflections are exact RP planes at every admitted cutoff. This does not prove RP for nonlocal smearing across the plane, nor continuum moment bounds.

## Finding 5 — exact Ward algebra survives; the chosen current and its expansion are additional content

**CONFIRMED; claim status PROVEN for the finite-cutoff identities, CONDITIONAL for the expansion/vanishing claims.** Sources: `SPHERE55.md:315`, “The exact identity”; `:351`, “Theorem 3.3”; `:379`, “Exact split”; E9; `CODEX_REVIEW_ROTDEF.md`, “The blanket contact exclusion loses derivatives of the source”.

On the finite compact configuration group, integrate div(F exp(-S_action) Xi). The result is

    E[Xi F] = E[F (Xi S_action - div Xi)].

The same identity for F=1 makes E[W]=0, so this is exactly Cov(F,W). No spatial boundary conclusion follows merely from this configuration-space identity. If two seam cutoffs equal 1 on every link read by F, the two Xi F agree pointwise; hence their Ward covariances agree, while W itself need not agree pointwise. The product of centred observables causes no problem: differentiate its centring constants when differentiating F_s; the identity remains exact.

The discrete product rule is

    D_mu(chi v^nu) = (D_mu chi) v^nu + chi(x+a e_mu) D_mu v^nu.

For the quadratic boost D_mu v^nu=partial_mu v^nu+(a/2)partial_mu^2 v^nu. Writing w_mu,nu=partial_mu v^nu-delta_mu,nu div(v)/4, symmetry of T gives the antisymmetric contribution

    sum_(mu<nu) w_mu,nu [chi(x+a e_mu)-chi(x+a e_nu)] T_mu,nu.

This verifies E9's transpose/sign correction. All cutoff-difference terms have stencil support in the seam transition region (possibly one stencil spacing beyond where 0<chi<1). There is no second, independent outer radial cutoff. There are still fluxes through two surfaces separating each cap from the seam. Pairing these surfaces does not make their sum small without transparency.

For any specified T, defining B=W+T_chi and seam insertion S_seam=-T_chi makes the advertised split an identity. It **does not check** that B has no leading dimension-5 current or other low-dimensional term: the same definitional equality passes for a wrong T. The identity's own renormalized symmetric current, its coefficients, the displayed O(a) forward-difference Hessian term for boosts, and all source contacts must be controlled in W1/W3. These are not certified by the algebra. In particular, a contact c delta(x-y) partial_mu X_mu,nu(y) is symmetry allowed; integration against v^nu f differentiates f and need not vanish. The source now correctly includes that obligation instead of repeating the earlier blanket contact exclusion.

**CONFIRMED; claim status PROVEN** for the geometry and classical profile variation (`SPHERE55.md`, “Killing fields”, “T4 in detail”). With D=R^2+|x|^2, differentiating X gives dX.dX=(2R^2/D)^2 dx.dx. For the boost,

    partial_mu v_nu = 2 c_mu x_nu + 2(c.x) delta_mu,nu - 2 x_mu c_nu,
    div v = 8(c.x),    v.log(Omega) = -2(c.x).

Thus the metric Lie derivative vanishes. Its pushforward is exactly 2R times the stated ambient rotation. Varying (1/4) integral u(x) F^2 by delta A=i_v F yields the constant-coupling stress contraction, whose trace vanishes in dimension 4, and the explicit term -(1/4) integral (v.u)F^2. Since u=G(a Omega)^-2, this is +(1/16) integral (du/dlog s)(div v)F^2, with the derivative kept inside the integral when it depends on x.

For G-pert, direct implicit differentiation gives

    du/dlog s = -2 beta_0/[1-beta_1/(beta_0 u)]
              = -2 beta_0 - 2 beta_1 G^2 - (2 beta_1^2/beta_0)G^4 - ... .

The quantum scale-response subtraction and the identification of its residual with the coefficient of the renormalized trace operator are **NOT-VERIFIED**. In particular, neither the Haar identity nor this derivative computes the exact nonperturbative step-scaling response. The order G^4 is formal under matching of the first two coefficients; it is not an established W0 bound.

## Finding 6 — the covariance inequality is valid; E10 is essential and does not prove its inputs

**CONFIRMED; claim status PROVEN for the inequality and CONDITIONAL implication.** Sources: `SPHERE55.md:432`, “Lemma 3.5”; `:485`, “N5-cond”; `:813`, E10; E6.

Let H=E[F|W_s], M=E[J|W_s]. Total covariance is E Cov(F,J|W_s)+Cov(H,M). For a deterministic scalar c,

    |Cov(H,M)| <= sqrt(Var F) sqrt(E|M-c|^2)
               <= sqrt(Var F) sqrt(sup_V E[|M-c|^2|V]).

Take the infimum over c. This requires a globally common c, not a separately chosen c(V). For real seam insertions the square in the source is correct; for complex ones it must be an absolute square. For the tested F, division by Z_e^2 and SRC-E give exactly the sufficient N5a/N5b implication. At s=l_0, the second factor is inf_c sup_V |E[J|V]-c|; E6 correctly removes the spurious factor 2.

E10 properly replaces the false pointwise scale-s moment bound with a bound on the **integrated, coefficient-weighted insertion**. The scaling estimates can be rebuilt, conditionally: an insertion of dimension d integrated over an m-dimensional region, with correlation range s and covariance of size s^-2d, has standard deviation of order Vol_m^(1/2) s^(m/2-d). This gives

    bulk: a^2 s^-4;    dilation: c_4 s^-2;    displacement seam: a s^(-7/2).

These formulas assume the conditional covariance integration estimate and its all-background uniformity; dimension counting alone proves neither. The withdrawn choice s proportional to a^(1/2) produces **a^(-3/4)** for the seam, not a vanishing a^(1/2); even the bulk factor is then order **1**. The necessary power separations are s/a^(2/7)->infinity, s/a^(1/2)->infinity, and s/|c_4|^(1/2)->infinity, strengthened as necessary for the actual logarithmic factors. With renormalized separated covariance bounded by exp(-m d/s)s^-K, any s->0 kills that term. An unrenormalized a^-K prefactor would require the separately stronger relation involving log(1/a). E10 acknowledges this distinction.

For the s=l_0 alternative, “bounded-curvature backgrounds only” must not weaken the quantifier from **every coarse V** to a selected small-field subset. An existential interpolator does not identify the RG conditional background or bound its quantum insertions (see Finding 11). This remains an open all-background hypothesis.

## Finding 7 — a separated two-point Ward theorem does not establish OS1 on the local algebra

**REFUTED as the stated full-algebra implication; claim status GAP.** Sources: `SPHERE55.md`, “Observable” in §3.3 (F_s is a centred product of two separated energy smearings); “Theorem 3.6 (fixed-R symmetry restoration for the tested pair)”; §5.1 “on the algebra generated by ... (and products)”; §6 “every subsequential continuum limit omega_R is invariant”; §7 rows 24–26.

W1, W3, N5 and SRC-E are formulated for that two-point F_s. Integrating the exact Ward identity proves invariance of those tested connected two-point functions, along the support-admissible orbit. Neither moment bounds nor the phrase “algebra generated” extends that conclusion to every product. No Gaussianity or determination of the state by its two-point function is assumed. The one-point and all higher-product Ward estimates are also needed.

An exact logical counterexample to the moment-extension step: on four signs x_i in {-1,+1}, set

    p(x) = [1+(1/2)x_1 x_2 x_3]/16.

Every mean and every distinct-pair correlation is zero; all moments are bounded by 1, and the entire two-point matrix is invariant under permutations. Yet E[x_1 x_2 x_3]=**1/2**, while E[x_1 x_2 x_4]=**0**. Swapping 3 and 4 is not a symmetry of the state. This finite example refutes the inference from pair data plus arbitrarily good moment bounds; it is not presented as a Yang–Mills counterexample.

There is a second overstatement: the sentence “Integrating along one-parameter subgroups gives every element of SO(5) directly” exceeds the support restriction. The later scope remark correctly admits that a path taking the support across the equator is not covered. Only local Killing transport within the caps and full SO(4)_poles transport there have been supplied conditionally.

**Repair:** require W1/W3/N5 and the necessary normalizations/moments for a determining family containing constants, single smearings, and every finite product, uniformly along each permitted group path, including contact configurations among insertions. This is a real enlargement of the source estimates. After that enlargement, separated-from-the-seam N5 suffices geometrically for the flat limit: every fixed finite collection of compact supports and every fixed translation/rotation path fit near the pole once R is large. Contact between observables and each other is distinct from contact with the equator. Full finite-R SO(5) invariance, or conjugating equatorial RP through the observation region, still needs seam-contact control.

## Finding 8 — the Chern–Simons parity correction is right, but it does not establish a single-field seam

**CONFIRMED; claim status PROVEN for the stated local, single-connection defect class.** Sources: `SPHERE55.md:512`, “Chern-Simons on the seam”; `PANEL_P4.md:318`, “excluded by theta_eq symmetry”.

The equatorial reflection restricts to the identity on every tangent vector of the equator. Pullback therefore preserves the tangential connection and its CS 3-form on an independently fixed orientation of S^3. A term integral CS(A) is theta_eq-even. P4's asserted oddness is refuted.

For delta A=D epsilon, variation of CS(A) is an exact 3-form dQ_2(epsilon,A), by expanding 2 tr(delta A wedge F)-d tr(A wedge delta A) and using D F=0. Consequently variation of integral c(x) CS(A) is -integral dc wedge Q_2. Arbitrary local A and epsilon force dc=0 for this lone local CS term. A coordinate reflection of R^4 induces an orientation-reversing map of its boundary S^3 (the outward normal transforms with it). For constant c it sends the CS integral to its negative. Exact coordinate reflection invariance therefore forces c=0, since the functional takes continuously variable small values; this is not merely a statement modulo a winding number.

For a single SU(N) connection, gauge-invariant local polynomial terms of dimensions 1–3 vanish: the first curvature has dimension 2, its single trace and single differentiated traces vanish, and two curvatures already have dimension 4. CS is the exceptional connection-dependent term dealt with above. This counting excludes that local obstruction **after** the single-connection description is justified. With two boundary connections and a transporter h, the invariant tr((D_i h)^dag D_i h), dimension 2, is allowed. Thus this exclusion cannot bootstrap transparency from the original seam action.

## Finding 9 — “no jump mode survives the first RG step” is not what the soft kernel proves

**REFUTED in its literal finite-step form; NOT-VERIFIED as an asymptotic transparency mechanism. Claim status GAP.** Sources: `SPHERE55.md:527`, “Why N5 should hold”; specifically “No jump mode survives the first RG step” and “the level-1 field is single-valued”; §1.6 “Kernel”.

At every finite cutoff and positive finite coupling, both the Wilson density and every normalized soft-kernel factor are strictly positive on the compact link configuration spaces. Integrating their product gives a strictly positive coarse density on **all** coarse link configurations. The coarse complex still has north links, south links and crossing variables. In particular, open sets with a mismatch between the two sides have positive probability after one step. No exact constraint or elimination of the two-sided degrees of freedom has occurred. A concentration/irrelevance statement at later scales would be a different assertion and needs a quantitative estimate.

Even granting the claimed probabilistic crossing-plaquette fluctuation O(g), a smooth-side expansion gives a(A_i^- - A_i^+) in the plaquette logarithm after setting the crossing transporter to 1. A plaquette logarithm O(g) supplies only a jump estimate **O(g/a)**, not o(1) in physical units. A fixed blocking factor L does not cure this as a->0. The source's inference to immediate single-valuedness is therefore unavailable. This leaves the dimension-2 matching operator active until controlled by N5-RG/N5-op.

E11's corrected comparison is **CONFIRMED as tree-level dimensional arithmetic, not as an RG theorem**. A jump smooth at scale ell has seam cost (beta_cross/a)|J|^2 ell^3 and bulk cost beta_bulk |J|^2 ell^2; their ratio is

    lambda_seam(ell) = (beta_cross/beta_bulk)(ell/a).

Thus the strong-stiffness criterion is beta_cross/beta_bulk >> a/ell. Positive weights alone do not imply it: a positive sequence beta_cross/beta_bulk=(a/ell)^2 gives lambda_seam=a/ell->0. E11 must also replace the preceding absolute claim that only an exactly zero coefficient can reach the decoupled limit. The specified ordinary-strength seam has the requisite tree-level ratio after Finding 2's weight correction, but positivity and relevance do not exclude a competing nonperturbative interface flow.

## Finding 10 — the hierarchy changes the meaning of ell_0 by a factor of two

**REFUTED as a literal common-scale identification; claim status GAP (harmless repair available).** Sources: `SPHERE55.md:224`, “a_n = l_0 (chart units)”; `:429`, “V = the RG field at the fixed physical scale l_0”; §1.4 “LOCAL PHYSICAL SPACING”; §6 “no ... scales above l_0”.

The hierarchy's terminal chart spacing is ell_0. Its actual local physical spacing is **Omega(x) ell_0**, which reaches **2 ell_0** at the pole, not ell_0. The same issue applies to the intermediate symbol s when it is switched from chart spacing to physical scale. The metric is explicit, so this is an exact factor, not an asymptotic uncertainty.

To keep an ultraviolet ceiling ell_UV in physical units, choose the coarsest chart spacing ell_UV/2 (and state weak-coupling control throughout the resulting physical interval [ell_UV/2,ell_UV]), or instead declare the physical ceiling to be 2 ell_0 and assume control through that scale. This does not force an infrared input, but “g(ell_0) is small” at one reading must not silently discharge the other reading. Constants attached to W, S, Theta and the four meanings of s also need the distinctions listed in §8; the still-unresolved beta comparison in Finding 2 is the more consequential collision.

## Finding 11 — all-background conditional hypotheses are a legitimate sufficient form, not a proved ultraviolet classification

**CONFIRMED as a conditional architecture; NOT-VERIFIED for every required estimate. Claim status CONDITIONAL / OPEN.** Sources: `SPHERE55.md`, §3.5 “What enters”; §4.5 “INCLUDING large coarse fields”; §5.4 “The background is bounded for EVERY V”; §6 “The first non-UV item”; E10(5). Inherited source: `CODEX_REVIEW_UNIV.md`, “Edge holonomies versus prescribed branch/transition data”.

The covariance bound indeed eliminates any need to know the coarse marginal law if its conditional terms are bounded uniformly for **every** V and the required observable moments exist. There is no hidden expectation over a typical subset in that implication. Conversely, replacing the supremum by a small-field assertion leaves the complementary event entirely uncontrolled; its probability and correlation with the observable must then be bounded explicitly. Large-field probability control might repair this without a mass gap, so failure of a uniform bound would not by itself prove infrared decorrelation logically necessary.

The bounded-curvature interpolation can be rebuilt: choose bounded Lie-algebra logarithms of the coarse edge holonomies, place each along a disjoint thin tube in the middle of that edge with a smooth longitudinal bump of unit integral, and set the connection to zero near vertices. Its holonomy is the prescribed edge matrix; its curvature consists of transverse bump derivatives of size O(ell_0^-2). The construction has no volume-dependent constant on a regular coarse grid. But it is existential, can be discontinuous as a function of V, and need not be an RG minimizer or the background of the conditional measure. It supplies **no** bound on conditional fluctuation Hessians, source insertions, partition functions or moments.

Conditioning on all coarse fields does not literally make the fine marginal in a neighbourhood depend only on the local geometry. Fine variables outside that neighbourhood remain integrated and coupled to it. Quantitative locality/conditional decay would justify a uniform estimate; it is an input to prove. In particular a bound uniform in V at each fixed R can still have a constant growing with R. U-mom's separate R-uniform quantifier cannot be dropped on the basis of geometric interpolation.

There is also an explicit quantifier gap in the input list: §3.5 W3 bounds the **unconditional** number C(s), and SRC-E bounds the **unconditional** fine-field variance. Unlike W1/N5, their displayed statements are not supremum-over-V estimates. U-mom-cond is a separately stated sufficient strengthening. To make §6's all-conditional reading concrete, one must give, for example, sup_V |E[Xi F_s-partial_s F_s | V]|/Z_e^2 -> 0 uniformly along the path, with the centring constants and moment dependence controlled, and prove the required conditional moment bounds. Calling the unconditional estimates ultraviolet does not perform that conversion. The abstract implication can assume the stronger versions, but the current displayed W3/SRC-E statements do not establish that they are independent of the coarse law.

The three inherited analytic items remain **NOT-VERIFIED / OPEN**:

1. P4 S4(a): the slowly varying coupling extension, including uniform large-background and source control; “moderate” is not an estimate.
2. P4 S4(b)'s conclusion: N5, including a quantitative suppression of the two-sided matching mode, renormalized conditional decay, and conditional-mean oscillation. Excluding a CS term proves none of these.
3. UNIV55's W0 rate: nonperturbative Lambda-matching and the dilation/source normalization. The formal derivative comparison in Finding 5 is its available algebra, not an achieved O(g_bare^2) or O(G^4) bound.

Thus “all inputs are ultraviolet” is defensible only in the explicitly stated operational sense “these sufficient estimates integrate fine scales with arbitrary coarse fields fixed.” It is not an established fact that the estimates hold, that their constants are controlled, or that currently banked small-field estimates imply them. No actual Yang–Mills OS1 result follows yet.

## Finding 12 — the fine-field moment hypotheses may make the proposed reduction vacuous

**NOT-VERIFIED; claim status OPEN, with a concrete obstruction to the supplied justification.** Sources: `SPHERE55.md:452`, “SRC-E (sphere): Var(F_s)/Z_e^4 bounded”; `:599`, “U-mom”; `:605`, “no zero mode”; `CODEX_REVIEW_ROTDEF.md:155`, “SRC-E is stronger than coarse moments”.

Separation of f and g does not remove contact singularities from Var(Otil(f) Otil(g)): squaring repeats both supports. Nor does centring subtract a variance. E10 repairs insertion conditional means, but leaves this fine-field variance hypothesis untouched. Ordinary nonzero separated-correlation normalization is not automatically compatible with it.

An exact bounded-coarse Gaussian control makes the distinction explicit, without a simulation or a Yang–Mills assumption. In each of two disjoint unit blocks let M=n^4 fine cells, a=1/n, let xi_i be independent standard Gaussian variables, and let the coarse variable X take 0 and 1 with probability 1/2, shared by both blocks. Put

    H_i = n^2 xi_i + X,
    O_B = n^-4 sum_(i in B) [H_i^2 - E H_i^2].

The coarse background is bounded for every X. Conditional on X,

    E[O_B|X] = X^2-1/2,
    Var(O_B|X) = 2n^4+4X^2.

The two blocks are conditionally independent. Using E[xi^2]=1, E[xi^4]=3 gives exactly

    Var(O_B) = 2n^4 + 9/4,
    Cov(O_B,O_C) = 1/4,
    Var(O_B O_C) = 4n^8 + 9n^4 + 9.

For the last identity, E[O_B^2|X]=2n^4+4X^2+1/4; square and average over X, then subtract (1/4)^2. A normalization preserving the nonzero separated covariance cannot bound these ordinary fine-field variances. Scaling Z_e like n^2 would bound the single-field variance but send the separated covariance divided by Z_e^2 to zero. This is an exact logical counterexample to inferring these fine-field moment bounds from bounded coarse backgrounds; it is not a counterexample to Yang–Mills existence.

The corresponding local dimension-four power count is the same: a positive covariance singularity of order |x-y|^-8 in four dimensions gives a radial variance integral proportional to

    integral_a^d r^3 r^-8 dr = (a^-4-d^-4)/4.

This is conditional power counting for the Yang–Mills observable, not a proved YM short-distance lower bound. It identifies the needed reconciliation: construct a useful nontrivial renormalized observable with the **actual** fine-field L^2/L^n bounds being used, or reformulate the covariance estimate with conditional/coarse observables and controlled contact extensions. Counterterm-subtracted Schwinger distributions cannot simply be substituted for ordinary positive-measure variances in Cauchy–Schwarz. Fixed positive-time smoothing would itself require a new half-algebra locality/RP argument.

**This is the single most dangerous unverified item in this review:** simultaneous nonvacuity of SRC-E/U-mom and a nonzero separated normalization. The seam's all-background transparency remains a second major open obligation, but even a transparent seam would not repair incompatible moment and normalization premises.

## Finding 13 — an unsigned conditional non-triviality witness can average to the free value

**REFUTED under the stated unsigned reading; claim status GAP.** Source: `SPHERE55.md:608–610`, “differs from its calibrated free value by >= eta” and “inf_V of the conditional deviation >= 2 eta”. If “deviation” is intended to mean one fixed signed deviation, that missing convention is precisely the repair.

Take V=+1 or -1 with equal probabilities and conditional signs X,Y with

    P(X=x,Y=y | V=v) = [1+(v/2)xy]/4.

Both conditional means vanish, so their oscillations and their coarse covariance are exactly zero. The conditional connected correlations are +1/2 and -1/2. Relative to calibrated value 0 and eta=1/4, the absolute conditional deviation is **1/2=2 eta for every V**, yet the unconditional connected correlation is **0**, not at least eta away from that value.

A valid sufficient replacement chooses a single sign sigma in {+1,-1} and assumes

    inf_V sigma [Cov(X,Y|V)-C_free] >= 2 eta,
    |Cov(E[X|V], E[Y|V])| <= eta.

Total covariance then gives sigma[Cov(X,Y)-C_free]>=eta. Alternatively prove a noncancelling averaged witness directly. A uniformly signed witness passes to the R-limit; arbitrary absolute conditional deviations need not. This affects non-triviality, not the geometric OS1 passage.

## Finding 14 — the flat-limit geometry and pole-centred RP work with the repaired algebra premise

**CONFIRMED; claim status CONDITIONAL.** Sources: `SPHERE55.md:581`, “Geometry of the contraction”; `:592`, “What passes by compactness”; `PANEL_P4.md:111`, local-to-global moment estimate; `CODEX_REVIEW_TQ.md:628`, “Sphere route”. The full-algebra premise is the strengthened one in Finding 7, not a conclusion of the current pair theorem.

Set z=2x. Then g_R=(1+|z|^2/(4R^2))^-2 delta, and for c=e/(2R^2),

    v^z(z) = e + [(e.z)z - (|z|^2/2)e]/(2R^2).

Thus bounded finite-time flows converge with their derivatives on compact sets to translations. Rotations fixing the pole and coordinate reflections act exactly linearly in z. For supports in a fixed compact set, the complete finite translation/rotation path stays inside a cap far from the seam for sufficiently large R. This verifies why separated-from-the-seam estimates suffice **for those paths and all required products**, even though they do not imply full global SO(5) invariance at fixed R.

At each cutoff the coordinate RP inequality holds for strictly local gauge-invariant polynomials whose support is a positive distance from the plane. The clover stencil stays in the same half for small enough a. Common moment bounds allow these finitely many products to pass to the continuum and then to the flat limit. Full local SO(4) invariance transports a coordinate RP plane to every plane through the pole; translation invariance transports these to affine hyperplanes. The reflection invariance of the finite regulator also passes, supplying improper rotations. Equatorial RP and seam-contact estimates are unnecessary in this argument. No such transport is justified for the full half-algebra from two-point symmetry alone.

Given all-orders, position-uniform local moment bounds, choose a smooth unit-cube partition of unity and write f=sum_Q f chi_Q. For k>4, the local seminorms are bounded by C(1+|Q|)^-k times a Schwartz seminorm of f. Minkowski and Holder sum this absolutely, producing the same factorial-in-n moment growth with a Schwartz seminorm. This establishes the asserted local-to-global regularity and equicontinuity without clustering. A diagonal subsequence on a countable dense test algebra, extended by those bounds, then passes the symmetry and RP identities. U-alg must supply common maps/subtractions, not just common names for them.

Ward errors and N5 may have constants depending on R when a->0 is completed first for each R. Uniform local moments and algebra compatibility are needed for the subsequent R-limit; a uniformly signed non-triviality witness is additionally needed to retain non-freeness. No mass gap or unique state is obtained, and equality with a flat-torus selection is unverified. These are the correct limits of the inherited conditional compactness argument.

## Finding 15 — the seam has no uniform lower physical edge length

**CONFIRMED for the missing lower bound; NOT-VERIFIED for any use of uniform physical shape regularity.** Source: `SPHERE55.md:178–180`, the chordal-length formula and “O(1)-distorted cell structure”. The source proves an upper O(a) thickness, not two-sided metric comparability.

Let q=R/a=m+1/2+1/(2m), and take the corner v/a=(m+1/2,1/2,1/2,1/2) of the retained cube centred at (m,0,0,0)a. It is a boundary vertex, |v|^2/a^2=m^2+m+1, and

    q^2-|v|^2/a^2 = (m+1)^2/(4m^2) > 0.

The generic-radius condition holds for this sequence. The crossing chord has

    length(C_v)/a = 2q [q^2-(m^2+m+1)]/[q^2+(m^2+m+1)] ~ 1/(4m) -> 0.

Choose a=R/q at fixed R to obtain this collapse in the actual continuum limit. Thus “O(1)-distorted” cannot be banked as a uniform positive lower bound on physical aspect ratios or as a uniformly regular metric cellulation. This does not invalidate the combinatorial Wilson measure or its RP proof. N5-RG needs estimates for the stated combinatorial defect or a proof insensitive to this metric degeneration; a standard regular-cell estimate cannot be silently imported.

## Additional construction and scope checks

**CONFIRMED / PROVEN, within the local polynomial class:** `SPHERE55.md`, §3.4 “Hom_H(A, Sym^2 A) = 0”. An independent exact enumeration of the 384 signed permutations gives multiplicities **0,1,1** for A=Lambda^2 R^4, the scalar, and the determinant representation in Sym^2 A. For a signed permutation h the calculation uses chi_A(h)=((tr h)^2-tr(h^2))/2 and chi_Sym2A(h)=(chi_A(h)^2+chi_A(h^2))/2, with integer matrix-action traces. It did not reuse the author's representation script. Equivalently, the possible dimension-four bilinear with two free distinct indices contracts to tr(F_mu,rho F_nu,rho), which is symmetric rather than antisymmetric. Total inversion acts on a local polynomial of canonical dimension d as (-1)^d and on A as +1, excluding odd d there. These statements classify the stated constant-tensor polynomial class; they do not compute the nonperturbative insertion coefficients or source-contact distributions.

**CONFIRMED / PROVEN for seam-kernel bookkeeping, NOT-VERIFIED for its analytic RG adequacy:** `SPHERE55.md`, §1.6 “Properties”. Integrating each normalized k_c over V_c gives 1, so the fine marginal is unchanged. Every path transporter has the same endpoint gauge transformation, as does their average; a two-sided Haar change proves gauge covariance of its normalization. A graph automorphism permutes all shortest paths, proving equivariance for the seam family; reflection reverses a crossing transporter's orientation. Odd L makes coarse vertices fine vertices and retained coarse cubes unions of retained fine cubes. A coarse ordinary edge has a straight path of L fine edges. For a coarse crossing endpoint within 2La of the sphere, moving outward in a coordinate of maximal absolute value reaches the fine boundary in O(L) edges: if R>=4La that coordinate is at least R/4 and the radial deficit is at most 2La; if R<4La the whole radius is O(La). Down-closure makes the available coordinate segment contiguous. Reflection of this path and one fine crossing edge give the required O(L) seam path. Thus shortest paths are graph-local even though physical edge lengths need not be uniformly comparable. The inherited bulk S4' family and its full analytic bounds were not re-established from PROOF.md here.

**CONFIRMED / CONDITIONAL:** `SPHERE55.md`, §4.2 “Slab independence”. For two cutoffs equal to 1 on the observable's link dependence, Cov(F,W_chi)=Cov(F,W_chi'). Substituting W=B+S_seam gives exactly the stated difference of seam covariances as the opposite difference of bulk covariances. Independence in the limit requires W1 for both cutoff choices, not merely this equality. Since the construction is equivariant and linear in v, reflection sends S_seam(v) to S_seam(theta_*v): equator-even for pole rotations and equator-odd for boosts. Zero crossing weights give independent hemispheres and the stated covariance factorization; nonvanishing needs the separated witness, as E3 correctly admits. For the strictly positive action of this paper that factorization counterexample is excluded, but transparency is not thereby proved.

Read/provenance boundary: the target and the named predecessor reviews/PANEL_P4 were read by located excerpts; the two named check scripts were inspected and executed. The only discretionary source reads were SCIENCE_WORKFLOW.md and its review-loop SKILL.md. No PROOF.md contents, snapshots, audit ledgers, criterion files, or external papers were read. The target contains a PROOF.md locating string in its input list, but no numeric PROOF.md line citation was used or found to certify; no assertion that all historical citations are current is made. Source-line anchors in this review were checked by string match after writing. The last target erratum located is E13. No git, source edits, subagents, or additional deliverables were used.

## Summary table

| Finding | Review verdict | Claim status and exact boundary |
|---|---|---|
| 1 | CONFIRMED | PROVEN: digital 4-ball, boundary sphere, depth bound, all-radius incidence 3<=k_e<=6 |
| 2 | REFUTED | GAP: one constant beta does not equal the spatially weighted action; use incident-cell sums/extrema |
| 3 | REFUTED for the identified predicates; CONFIRMED for executions | PROVEN limited reproductions; K6 subcheck and positivity are identities, C4 is not a radiality test; preregistration NOT-VERIFIED |
| 4 | CONFIRMED | PROVEN: equatorial and four coordinate RP planes for the actual positive, paired weights |
| 5 | CONFIRMED for identities | PROVEN algebra/classical formulas; quantum current expansion and W0 remain OPEN |
| 6 | CONFIRMED | PROVEN covariance inequality; CONDITIONAL vanishing with E10's integrated, renormalized inputs |
| 7 | REFUTED | GAP: pair symmetry does not imply symmetry of the full local algebra or global fixed-R SO(5) |
| 8 | CONFIRMED | PROVEN: CS is theta_eq-even and excluded by coordinate reflections in the stated single-connection local class |
| 9 | REFUTED literally; NOT-VERIFIED asymptotically | GAP: a finite soft-kernel step retains full support; first-step gluing is not established |
| 10 | REFUTED | GAP: chart ell_0 has pole physical spacing 2 ell_0; fix the scale convention |
| 11 | NOT-VERIFIED for the estimates | CONDITIONAL architecture; all-background/all-radius estimates remain OPEN |
| 12 | NOT-VERIFIED | OPEN: useful normalization compatible with the required fine-field moments; exact obstruction to a compactness shortcut |
| 13 | REFUTED for unsigned deviations | GAP: conditional witness needs a common sign or a direct averaged bound |
| 14 | CONFIRMED conditionally | CONDITIONAL: flat contraction, local-to-global bounds and RP transport with a full determining algebra |
| 15 | CONFIRMED for degeneration; NOT-VERIFIED for regularity import | PROVEN absence of a uniform lower physical edge length; no uniform-shape theorem banked |
| Inherited S4(a), S4(b) conclusion, W0 rate | NOT-VERIFIED | OPEN: varying-coupling analysis, seam transparency and nonperturbative dilation matching |

Numerical corrections and accepted numerical errata:

| Assertion tested | Correct value or statement |
|---|---|
| Exact crossing weight k_e beta/4 and lower bound 3 beta(a)/4 | (1/4)sum_c beta_c; bounds 3 beta(2a)/4 and 3 beta(a)/2 on the weak monotone branch. The k_e=3 example is [2 beta(529a/427)+beta(529a/377)]/4. |
| Terminal “physical ell_0” | Omega ell_0, reaching 2 ell_0; use chart ell_UV/2 for ceiling ell_UV. |
| C4 firing as evidence of non-radiality | At x=e_1/2 it compares 5e_1/4 with e_1/2 but the wedge is 0. A genuine witness x=e_2/2 has wedge component 3/8. |
| Absolute conditional gap >=2 eta implies gap >=eta | With eta=1/4, conditional gaps +/-1/2 average to 0; impose one fixed signed deviation. |
| E10's withdrawn s proportional to a^(1/2) rate | Seam a^(-3/4), bulk a^0; s must be asymptotically larger than a^(2/7), a^(1/2), and abs(c_4)^(1/2), with logarithmic margins. This confirms E10, not a new refutation of its corrected premise. |
| E11's withdrawn absolute stiffness threshold | (beta_cross/beta_bulk)(ell/a)>>1. Positive but a-dependent crossing weights can still decouple. |
| E6's removed factor 2 | Coefficient 1 multiplying sqrt(Var F) inf_c sup_V abs(E[J given V]-c). |
| Uniformly comparable physical crossing length, if intended | No positive multiple of a works: the explicit generic sequence has length(C_v)/a ~1/(4m)->0. |

## Exactly what may be banked

1. **PROVEN:** the stereographic geometry and Killing-field normalizations; the half-shifted digital ball and boundary sphere; the all-radius incidence counts; the upper seam-depth bound. Incidence-to-weight conversion must use the actual beta_Q sum. This supplies a positive, reflection-paired lattice action, not a transparent continuum seam or a uniformly regular physical mesh.
2. **PROVEN:** finite-cutoff reflection positivity on the gauge-invariant local half-algebras for the equator and all four coordinate great spheres through the poles. The pole-centred planes can be used in the flat limit without moving observables through the equator.
3. **PROVEN:** Haar Ward integration, cutoff independence of the tested covariance, the exact discrete flux split, the corrected covariance inequalities, the limited polynomial selection rule, the classical profile derivative, and the CS parity/exclusion calculation with its single-connection qualification. The split itself does not verify the current, its quantum coefficients, source contacts, or seam transparency.
4. **CONDITIONAL:** W0/W1/W3/N5/SRC-E in their complete corrected forms imply the tested pair's local Killing-transport identities. To bank symmetry of a state, supply the corresponding estimates for a determining algebra of all finite products. Separated-from-the-seam estimates then suffice for the compact-support paths used at the pole in the flat limit.
5. **CONDITIONAL:** with that full-algebra invariance, compatible nontrivial observable maps and position/radius-uniform moments, diagonal limits inherit Euclidean invariance, RP, permutation symmetry and the specified regularity bounds. A uniformly signed quantitative witness preserves non-freeness. Ward-error constants need not be uniform in R when a->0 is taken first.

Nothing here banks W0, W1, W3, N5, SRC-E, U-mom, a viable common renormalized algebra, U-NT, a Yang–Mills OS0–OS3 state, a mass gap, or equality with a flat-torus selection. The primary unresolved nonvacuity test is whether the ordinary fine-field moment hypotheses and a nonzero separated-correlation normalization can hold simultaneously.
