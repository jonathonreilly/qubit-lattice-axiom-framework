lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T17:34Z

# gap-cuttyp-max (queue row 936): the typical-environment cut gap (CUT-TYP)

Author: Claude Fable 5.2, max effort, on the Mac mini worker, pinned at commit 933258061.
Proof item on the crux (flux half). Research-stage working state. Nothing here grants status.
Labels used on every statement: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric, never a proof step), OPEN.
"READ" means read at the pinned commit and not re-proved here.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read the inputs in full: `library/gap-oddgap-max.md` Sections 6-7 (row 930) and the check
   `library/gap-oddgap-check-astra.md` (row 933). Duplicate check for (CUT-TYP) and (LSI-weak) in
   `library/open-core.md` and the FINISH rows. Fix notation.
2. STEP 1 of the row, part a: write (CUT-TYP) as an odd Poincare constant of the cut links in a quenched
   environment; identify the model exactly (which links, which couplings, which symmetry survives).
3. STEP 1 of the row, part b: the effective 2D coupling at 4D beta 2.3-2.6; comparison with the 2D O(4) / SU(2)
   principal chiral gap (implied by, implies, independent); is the environment in a regime with a known convergent
   expansion. Literature check on the placement.
4. STEP 2 of the row, attack 1: Ward identity for the whole-cut rotation with an environment defect; name the
   exact step where U(1) fails.
5. STEP 2, attack 2: two-scale argument (rotation mode against local modes) and disorder-averaged second moments.
6. STEP 2, attack 3: concentration over environments for the e^(-cN) rate.
7. STEP 3 of the row: the smallest unproved inequality, one solvable-model test that could refute it, and a
   precise (LSI-weak) with a verdict on which is easier. A GUIDE run only if memory allows.
8. Result section and the RESULT line.

## Log

- 2026-11-14T05:34Z: file created before any reading of the inputs. No earlier run of this item exists at the pinned
  commit (`library/gap-cuttyp*` did not exist).
- 2026-11-14T05:50Z: step 1 written (Section 1).
- 2026-11-14T06:10Z: step 2 written (Section 2: Proposition M, the exact cut model).
- 2026-11-14T06:35Z: steps 3 and 4 written (Section 3: placement and literature; Section 4: CAP, RARE-P, LOC).

## 1. Inputs read, duplicate check, notation (step 1)

**Read in full (READ):** `library/gap-oddgap-max.md` lines 1-100 and 323-620 (Sections 4-7 of row 930, Claude
Fable 5.2 max); `library/gap-oddgap-check-astra.md` (row 933, Codex gpt-6-astra xhigh, 502 lines, reconstructed by
the lead from the event log; its header says one small edit after the logged read is not recorded).

**Duplicate check (rule 0a).** `grep -n -i "CUT-TYP\|LSI-weak\|cut gap\|chiral" library/open-core.md`: no hit.
In `FINISH.md` the terms occur in rows 930 (source), 936 (this row), 937 (its check) and row 742 (line 819, a
literature row: Kovacs hep-lat/9603022 reduces the 2D SU(2) chiral-model gap to unproved Z_2 vortex inequalities).
`library/gap-direction-max.md:85` lists (CUT-TYP) as an unchecked item of row 930 and does not attack it. No other
row attacks (CUT-TYP) or (LSI-weak). I proceed.

**Credit.** Transfer-operator frame: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text
(SA 2313-2394, GL8 and GL10, as located by checks 927 and 933). Theorem R, Lemma CUT, Proposition RARE, (CUT-TYP),
(LSI-weak): row 930 (Claude Fable 5.2), checked line by line by Codex in row 933 with corrections. Row 922 (Claude
Opus 5.5) for the even two-slice law and the odd criterion.

**What the check (row 933) changes in what I use.**
- CUT HOLDS: for odd gauge-invariant F, E|grad_v F|^2 >= E[F^2 sum_k gamma_k(env_k)]. No independence of cuts used.
- RARE HOLDS as an implication with g_0, alpha > 0 and 0 < delta < 1/2.
- The uniform-rotation distinction HOLDS only as algebra of the spatial action: it is not an invariance statement
  for the full conditional two-slice law (the kernel factor), and a discrete stabilizer gives no quantitative gap.
- FAILS: "locked U(1) winding lines force unbounded susceptibility as N grows" (strip counterexample). I do not
  use that claim. The U(1) witness that stands is the soft toron: gamma_k = mu_0(tau)/(2N) for every environment.
- The flat-cut correlation length "comparable to 20" at beta 2.3 is a recalled number, not an estimate (row 933).

**Notation (from row 930, fixed here).** Spatial box B = L_1 x L_2 x L_3, periodic, N = L_2 L_3; time extent a
even. T the transfer operator, A^s the kernel of T^s. J the centre flip of the direction-1 links of one cut
x_1 = const of a slice; P_e = (1 + C)/2 with C f = f o J; E_s the kernel of T^s P_e. For 1 <= s <= a - 1:
w_e^(s)(u, v) = E_s(u, v) E_(a-s)(u, v)/Z_e, the even law of the slices at times 0 and s. cut_k = the N
direction-1 links of slice v at x_1 = k; env_k = all other links of u and v; nu_k(. | env_k) the conditional law
of cut_k; J_k the flip of cut_k; gamma_k(env_k) the odd Poincare constant of nu_k(. | env_k) on (S^3)^N:

  gamma_k := inf over f on (S^3)^N with f o J_k = -f of  E_(nu_k) sum_(b in cut_k) |grad_b f|^2 / E_(nu_k) f^2.

(CUT-TYP)_s: there are g_0 of order L_1 and c > 0 with w_e^(s)( sum_k gamma_k(env_k) < g_0 ) <= e^(-cN) for
2 <= s <= a/2 at beta 2.3 to 2.6. (LSI-weak)_s: w_e^(s) has a log-Sobolev constant alpha >= C L_1/N on
gauge-invariant functions. Seed box: L_i = 20, a = 10, beta = 2.3, N = 400.

## 2. STEP 1a: the cut model, exactly (step 2)

Conventions. A unit quaternion is an element of SU(2) = S^3 in R^4, and <a, b> := (1/2) tr(a b^*) is the R^4
inner product. The Wilson weight of a plaquette is exp(beta (1/2) tr U_p). Lambda = L_2 x L_3 is the transverse
lattice. xi_x (x in Lambda) is the cut link from (k, x) to (k+1, x) in slice v. g_xy and h_xy are the transverse
links of slice v over the bond <xy> of Lambda at the layers x_1 = k and x_1 = k+1. t_x, t'_x are the temporal
links at (k, x) and (k+1, x) leaving time s, and xi^+_x, xi^-_x are the direction-1 links over x at times s+1, s-1.

### 2.1 Proposition M (PROVED; identities, no estimate)

(M1) **Four-term form of the even law.** Z_e w_e^(s)(u, v) = (1/4) sum over (eps, eps') in {0,1}^2 of
W(u, v; eps, eps'), where W is the 4D Wilson weight on the a-periodic lattice, integrated over all links outside
the slices 0 and s, with the sign of beta reversed on the N temporal (0,1)-plaquettes over cut k between times
s-1 and s (if eps = 1) and between times s and s+1 (if eps' = 1).

(M2) **The conditional law of the cut.** nu_k(d xi | env_k) is proportional to

    exp( beta sum over bonds <xy> of Lambda of <xi_x, g_xy xi_y h_xy^(-1)> ) Phi_env(xi) d xi,
    Phi_env(xi) = integral mu_bulk(d omega) cosh( beta sum_x <xi_x, H^-_x(omega)> ) cosh( beta sum_x <xi_x, H^+_x(omega)> ),

where H^+_x = t_x xi^+_x t'_x^(-1) and H^-_x (the same with the links towards time s-1) are unit quaternions,
omega is the set of links outside the slices 0 and s, and mu_bulk is the positive measure with the Wilson weight
of every plaquette that contains no link of cut k of slice s. mu_bulk depends on env_k and not on xi.

(M3) **Local factor.** The first factor is the two-dimensional O(4) model on Lambda (4 neighbours, unit spins in
R^4) at coupling beta_sigma = beta, in the convention exp(beta_sigma sum s_x . s_y), with the SO(4) connection
R_xy s = g_xy s h_xy^(-1). Equivalently: the SU(2) x SU(2) principal chiral model with g acting on the left and h
on the right. Continuum normalisation: 1/g_sigma^2 = beta, so g_sigma^2 = 0.43 at beta 2.3 and 0.38 at 2.6.

(M4) **Symmetries of the local factor.** Site rotations xi_x -> A_x xi_x B_x^(-1) change (g, h) by a gauge
transformation of each layer. The local factor depends on (g, h) only up to such transformations. It is invariant
under xi_x -> a_x xi_x b_x^(-1) exactly when a is covariantly constant for g (a_x g_xy = g_xy a_y) and b for h.
So its symmetry group is the product of the centralisers of the holonomy groups of the two layers, modulo the
common centre. Flat layers: SO(4). Both holonomy groups inside one-parameter subgroups: at least U(1) x U(1).
A layer whose holonomy group is non-abelian: only {+-1} from that layer.

(M5) **Planted structure.** env_k has the marginal law of w_e^(s) and xi the conditional law. So for every
measurable f >= 0, E_env E_(nu_k(.|env)) f(xi, env) = E_(w_e^(s)) f. The disorder is not independent of the spins:
(xi, env) is a sample of the gauge theory, and the quenched model is its posterior.

(M6) **Three-dimensional array.** The direction-1 links over cut k at all a times are an O(4) model on
Z_a x Lambda at coupling beta: the bonds along Lambda carry the connection (g, h) of that time, the time bonds
carry (t, t'). nu_k is the law of the layer at time s, with the layer at time 0 fixed and all else integrated.

Proof. (M1) E_s(u, v) = (1/2)(A^s(u, v) + A^s(u, Jv)) and E_(a-s)(u, v) = (1/2)(A^(a-s)(v, u) + A^(a-s)(Jv, u)).
A^s(u, v) A^(a-s)(v, u) is the 4D weight with the slices 0 and s fixed and the rest integrated (Z = Tr T^a is the
4D partition function; this does not depend on how the spatial weight is split between consecutive kernels).
Replacing v by Jv in one factor changes the sign of the cut links in the plaquettes of that factor. A spatial
plaquette contains zero or two links of cut k, so it does not change. A temporal (0,1)-plaquette over the cut
contains one, so its sign changes. J at another cut differs by a central gauge transformation.
(M2) In W, collect the plaquettes that contain a link xi_x of the cut: four spatial ones, (1/2) tr(xi_x h_xy
xi_y^(-1) g_xy^(-1)) = <xi_x, g_xy xi_y h_xy^(-1)> for the four neighbours y, and two temporal ones,
(1/2) tr(xi_x t'_x (xi^+_x)^(-1) t_x^(-1)) = <xi_x, H^+_x> and the same below. All other plaquettes make mu_bulk.
The sum over (eps, eps') of exp(beta sum_x [(-1)^eps <xi_x, H^-_x> + (-1)^eps' <xi_x, H^+_x>]) is 4 cosh cosh.
(M3) is the definition of the O(4) model. (M4): the weight of a bond is <a_x xi_x b_x^(-1), g a_y xi_y b_y^(-1)
h^(-1)>; it equals <xi_x, g xi_y h^(-1)> for all xi iff a_x^(-1) g a_y = +-g and b_x^(-1) h b_y = +-h with equal
signs; a sign that is not constant is a Z_2 gauge transformation and is absorbed. (M5) is the definition of a
conditional law. (M6) lists the plaquettes that contain a direction-1 link over cut k. QED

### 2.2 Remarks (what the row's description leaves out)

1. **The cut is not a two-dimensional model.** Each cut link has four spatial plaquettes and two temporal ones.
   Phi_env carries the two temporal ones. It is a mixed Laplace transform of the law of the staple field H under
   mu_bulk, so log of each cosh-free component is convex in xi; it is not small and not local.
2. **Conditioning on the 4D environment instead is fatal (PROVED observation).** Given all links other than the
   cut, the law of the cut is the local factor times (1/4) sum of exp(beta sum_x <xi_x, +-H^-_x +-H^+_x>): a
   symmetric mixture of models in external fields of size up to 2 beta per site. The components with fields H and
   -H are concentrated near opposite configurations. So the time neighbours have to be integrated, as in (M2).
3. **U(1) in the same form.** For U(1) the local factor is the XY model with the U(1) connection g_xy - h_xy; its
   holonomy is abelian, so by (M4) the uniform rotation is a symmetry for every environment. That is the U(1)
   fact test of row 930 in the language of (M4).

### 2.3 Sizes at beta 2.3 to 2.6 (hand arithmetic; the recalled inputs are marked)

- Coupling: beta_sigma = 2.3 to 2.6 on a 20 x 20 torus.
- Flat reference (g = h = 1, Phi = 1). The two-loop formula with the exact mass gap of the O(4) model (Hasenfratz,
  Maggiore, Niedermayer 1990; recalled, not re-derived) is xi = 0.0416 (pi beta)^(-1/2) exp(pi beta). It gives
  xi = 21 at beta 2.3 and 51 at beta 2.6 (GUIDE; exp(7.226) = 1374, exp(8.168) = 3526). So the flat cut is
  ordered across the 20 x 20 cross-section, and its odd gap is at the rotor scale, a few times 1/N (ARGUED).
- Character ratio of one bond: u = I_2(beta)/I_1(beta) = 1.0054/2.0978 = 0.479 at beta 2.3 (series by hand).
  With the connective constant mu = 2.64 of the square lattice: mu u = 1.26 > 1, and mu u^2 = 0.61 < 1.
- Typical environment: every plaquette of the 4D theory has (1/2) tr U_p near 0.60 at beta 2.3 and 0.67 at 2.6
  (recalled Monte Carlo values, GUIDE). By (M5) the bond energies <xi_x, R_xy xi_y> of the planted cut have this
  mean too. The holonomy (g_P, h_P) of the connection round one plaquette of Lambda is a pair of rotations with
  half-angle near 53 degrees each. So the connection is far from flat at the scale of one plaquette.

## 3. STEP 1b: placement against the 2D O(4) / SU(2) chiral gap, and the literature (step 3)

### 3.1 Lemma W (PROVED): no connection brings beta >= 1 inside a single-site or spectral criterion

Let A_R be the operator (A_R c)_x = sum over the four neighbours y of R_xy c_y on (R^4)^Lambda (L_2, L_3 >= 3).
For every SO(4) connection R: lambda_max(A_R) - lambda_min(A_R) >= 4.

Proof. A_R is symmetric, tr A_R = 0 and tr A_R^2 = sum_x sum_(y ~ x) tr(R_xy R_xy^T) = 16 N on a space of
dimension 4N. For eigenvalues in [lambda_min, lambda_max] with mean 0, the mean square is at most
-lambda_min lambda_max. So -lambda_min lambda_max >= 4, and the width is at least 2 (-lambda_min lambda_max)^(1/2)
>= 4. QED

Use. Bauerschmidt and Bodineau (arXiv:1712.03676, J. Funct. Anal. 276 (2019); abstract read, proof not re-read)
prove a uniform log-Sobolev inequality for the O(n) model when the positive definite coupling matrix has largest
eigenvalue below n. On unit spins the coupling matrix beta (A_R - lambda_min) gives the same measure, and its
largest eigenvalue is beta times the width. By Lemma W the condition reads beta < 1 at best, for every
connection. The single-site Dobrushin estimate has the same threshold at degree 4 (scaled from the six-neighbour
statement READ in check 933 Section 5: influence beta/4 per neighbour). Both criteria also ignore Phi_env. So at
beta 2.3 to 2.6 the cut model is outside every criterion of this kind by a factor 2.3 or more, and frustration
cannot repair that: these criteria bound sizes of couplings, and frustration acts by interference between paths.

### 3.2 Verdict on the comparison (the row's STEP 1 question)

**(CUT-TYP) is logically independent of the mass gap of the flat 2D O(4) / SU(2) chiral model.** Reasons:

1. *Not implied by it.* The flat gap is a statement about one environment (g = h = 1) and about Phi = 1. One
   environment is a null set, and (CUT-TYP) may discard a set of weight e^(-cN). The flat gap also has the wrong
   size: where it holds it is of order 1/chi(beta), and chi is of order xi^2 with xi = 21 to 51 (Section 2.3).
   That is below 1/100, against the order-one gap per cut that (CUT-TYP) asks.
2. *Does not imply it.* (CUT-TYP) says nothing on the flat environment, and nothing in infinite volume.
3. *The flat model is the worst case, not the model case* (ARGUED). By (M4) the flat layers are the environments
   with the largest symmetry group, SO(4), hence with a rotor mode. A typical environment has holonomy half-angles
   near 53 degrees per plaquette, and by (M4) no continuous symmetry.
4. *What is the right comparison class.* The local factor in a typical environment is a non-abelian gauge glass
   on a planted (Nishimori-type) line (M5), at temperature 1/beta = 0.43 in units of the bond energy, and with
   the extra non-local factor Phi_env. It is not weakly coupled: a spin in a typical local field (four neighbours,
   field length about 2 beta) is polarised at about I_2/I_1(4.6) = 0.7.
5. *Is the environment in a regime with a known convergent expansion?* No. Lemma W excludes the single-site and
   spectral criteria. The walk (high-temperature) expansion has mu u = 1.26 > 1 at beta 2.3. What a typical
   environment adds is a second-moment statement: two walks with different enclosed area carry different
   holonomies, and the diagonal sum has mu u^2 = 0.61 < 1 (GUIDE, not an expansion: the quenched partition
   function stays in the denominator). No theorem turns this into a quenched gap.

So (CUT-TYP) is neither a corollary nor a strengthening of the open 2D chiral gap. It is a statement about a
frustrated planted model at intermediate coupling. It is open for a different reason: no method controls a
quenched non-abelian model at beta above 1, and Phi_env makes the model non-local.

### 3.3 Literature check on the placement (three searches, 2026-11-14; abstracts only unless said)

- Bauerschmidt, Bodineau, arXiv:1712.03676: used in 3.1. It is the one criterion I found that sees cancellation
  between ferromagnetic and antiferromagnetic couplings (it covers the SK model at beta < 1/4). It does not reach
  beta 2.3 by Lemma W.
- Cesi, Maes, Martinelli, "Relaxation of disordered magnets in the Griffiths' regime", CMP 188 (1997) 135-173
  (mp_arc 96-299), and CMP 189 (1997) 323-335 for two-dimensional Ising systems: in a quenched random system the
  relaxation is almost surely faster than any stretched exponential, and it is not uniformly exponential; rare
  regions whose couplings equal the pure values carry the slow modes (Bray and Rodgers 1988; the rare-region
  statement is from a review's account, not from the papers' text). This is the known form of the obstruction
  in Section 4.1: a quenched gap is governed by the worst rare region.
- Two-dimensional gauge glass (random-phase XY): the physics literature finds no glass order at positive
  temperature, by numerics and gauge-symmetry arguments; it is disputed by a minority and is not a theorem.
  Nishimori-line identities (Nishimori 1981; Ozeki and Nishimori 1993 for gauge glasses, recalled) are exact
  consequences of the planted structure (M5); they bound order parameters, not spectral gaps.
- Kovacs, hep-lat/9603022 (row 742): the flat 2D chiral gap reduced to unproved Z_2 vortex inequalities. Flat case.
- Not found: any rigorous result on a random-connection (frustrated) O(N) or chiral model at beta above the
  single-site threshold; any quenched Poincare bound for a gauge glass. No search of the Sussman-Alpoge account
  was needed for this section: their text is at weak coupling along the RG, and this is a fixed-cutoff statement
  at beta 2.3 (as rows 899, 922, 930 say of this lane).

## 4. A weaker pair of inputs: Lemma CAP and Proposition RARE-P (step 4; PROVED implications)

### 4.1 Why the rate e^(-cN) is the wrong demand (ARGUED)

Take an environment that is flat (pure gauge in both layers) on a patch of area A of Lambda. The test function
f = sum over x in the patch of <xi_x, Q> is odd, E|grad f|^2 <= A, and E f^2 = Q.(sum_(x,y) E[xi_x (x) xi_y])Q.
If the patch is ordered, E<xi_x, xi_y> >= m^2 on it, the best Q gives E f^2 >= m^2 A^2/4, so
gamma_k <= 4/(m^2 A). A flat tube of cross-section A along direction 1 makes every cut bad at the threshold
4/(m^2 A), and it costs e^(-C A L_1), not e^(-cN). So, for a threshold g_0 = c_0 L_1:

    w_e^(s)( sum_k gamma_k < c_0 L_1 ) >= exp( -C' L_1/c_0 )     (ARGUED),

and RARE then needs alpha ln(1/delta) >= 2 g_0, that is alpha >= 2 c_0^2/C': a volume-free constant, not the toron
scale L_1/N. Not proved: the order in the patch (it needs a lower bound on quenched correlations with Phi_env
present; a flat patch in slice v does not make the integrated slabs flat). At the seed box N = 20 L_1, so the
two rates differ only in the constant. As a statement uniform in the cross-section, (CUT-TYP) with the rate
e^(-cN) is doubtful, and (LSI-weak) at the scale L_1/N would then not suffice.

### 4.2 Lemma CAP (PROVED)

Let Bad be a measurable set of pairs (u, v) with G >= g_0 off Bad (G = sum_k gamma_k). Suppose there are
kappa > 0 and 0 <= delta' < 1 with

    (CAP)  E[h^2 1_Bad] <= kappa^(-1) E|grad h|^2 + delta' E[h^2]

for every Lipschitz h >= 0 that is gauge invariant in each slice and Theta-even (expectations under w_e^(s)).
Then lambda_s >= (1 - delta')/(1/g_0 + 1/kappa).

Proof. Let F be odd, m = E F^2, D = E|grad F|^2. By CUT, E[F^2 1_(Bad^c)] <= D/g_0. h = |F| is Lipschitz, gauge
invariant, Theta-even, and |grad h| <= |grad F| almost everywhere. So E[F^2 1_Bad] <= D/kappa + delta' m. Add. QED

RARE (row 930) is CAP with kappa = alpha ln(1/delta)/2 and delta' = ln 2/ln(1/delta).

### 4.3 Proposition RARE-P (PROVED implication): the even gap in place of the LSI and of the rate

Let lambda_e be the Poincare constant of w_e^(s) on gauge-invariant Theta-even functions, and let
w_e^(s)(G < g_0) <= delta < 1/2. Then

    lambda_s >= (1 - 2 delta)/(1/g_0 + 2/lambda_e).

More generally, for delta < 1 and eta > 0 with (1 + eta) delta < 1:
lambda_s >= (1 - (1 + eta) delta)/(1/g_0 + (1 + eta)/(eta lambda_e)).

Proof. For even h >= 0: h^2 <= (1 + 1/eta)(h - E h)^2 + (1 + eta)(E h)^2. So E[h^2 1_Bad] <=
(1 + 1/eta) Var(h) + (1 + eta) delta (E h)^2 <= ((1 + eta)/(eta lambda_e)) E|grad h|^2 + (1 + eta) delta E[h^2].
This is (CAP) with kappa = eta lambda_e/(1 + eta) and delta' = (1 + eta) delta. Apply Lemma CAP; eta = 1. QED

Reading. No large-deviation rate and no log-Sobolev input: a fixed fraction of good environments is enough. The
price is the cap lambda_s <= about lambda_e/2: RARE-P gives an odd gap of the order of min(g_0, lambda_e), not
of order L_1. In Theorem R this gives p <= (theta/(1 + theta))^(a/2 - 1) with theta = 2 beta^2 Gamma/lambda_s of
order one: decay of the flux weight in the time extent a, not the seed-box number (the seed needs
lambda_0 >= 78.4 Gamma_0, and nothing suggests lambda_e is that large).

Fact tests. U(1), Model G at s = a/2: every environment has gamma_k = mu_0(tau)/(2N) (check 933), so G < g_0
everywhere for g_0 above the toron scale, delta = 1, and the hypothesis fails. Frozen groups in the single-link
heat-bath form: cut gaps 0. So the pair passes the fact test through its first input. The second input,
(EVEN-PI)_s: lambda_e >= lambda_e0 > 0, is an even-sector statement. Its relation to the glue half of rows
929/934 is not checked here.

### 4.4 Corollary LOC (PROVED implication): what gives order L_1

Suppose that for each k there are a set Bad_k of pairs (u, v) with gamma_k >= gamma_* off Bad_k, and a set N(k)
of links of the two slices, such that each link lies in at most n_0 of the sets N(k), and

    (LOC-CAP)  E[h^2 1_(Bad_k)] <= kappa_1^(-1) E|grad_(N(k)) h|^2 + delta_1 E[h^2],   delta_1 < 1,

for every h as in (CAP). Then lambda_s >= L_1 (1 - delta_1)/(1/gamma_* + n_0/kappa_1).

Proof. For odd F, by the proof of CUT for one cut, E sum_(b in cut_k) |grad_b F|^2 >= E[F^2 gamma_k] >=
gamma_* (m - E[F^2 1_(Bad_k)]) >= gamma_* ((1 - delta_1) m - kappa_1^(-1) E|grad_(N(k)) F|^2). Sum over k: the
left sides add to at most D, and the last terms to at most n_0 D/kappa_1. Solve for m. QED

Reading. Order L_1 needs the bad event of one cut to be left by moving links near that cut, at an order-one
rate kappa_1. The proof of RARE-P gives (LOC-CAP) from two local inputs: a Poincare constant of the conditional
law of the links of N(k) given the rest, and a bound delta < 1/2 on the conditional weight of Bad_k, both
uniform in the links outside N(k). The uniformity is the open part (it is a background-uniform statement on a
block, the wall W1 of row 930 at block scale).
