lead: anthropic/claude-fable-5-2/medium laptop-subagent
row: 1066

# gap-aniso-trajectory (FINISH row 1066)

## Plan (at most eight steps; one step per response; each result is appended here)

1. Read row 1066 in FINISH.md in full. Record the question, the files, the five tasks, the kill tests, the stop condition and the marks.
2. Repo-first check: grep open-core.md, parts/gap.md and the FINISH rows for each statement. Record which rows already cover what. Check whether row 1067's reading file is present.
3. Read the files the row names. Record the definitions and the facts used later.
4. Task 1.
5. Task 2 and task 3.
6. Task 5: the first lemma of the seed, tried by hand; the first failing line of the route.
7. Task 4: the kill tests, each with its outcome; compact U(1) first.
8. Summary table of marks, then the RESULT line.

## Step log

### Step 1 result: what row 1066 asks (read in full, FINISH.md L1147)

- **Question.** Does the region R of row 1053 section 4.2 contain a family of anisotropic Wilson couplings with fixed renormalized anisotropy that reaches an isotropic continuum limit? If so, does the anchor's gap pass to that limit, or to the isotropic band, by a statement that is not the crux?
- **Tasks.** (1) State V2 exactly, with the corrections of row 1061, as a chain to a mass-gap theorem; name the consumer. (2) The matching, without the assumption at L183 of row 1053; unknown prefactors and subleading logarithms kept; decide whether R meets a family of fixed renormalized anisotropy; say which step is perturbative (Karsch) and which is not. (3) The bridge: state it; decide whether it contains (W), CR or (PHYS-SEED). (4) Kill tests on file; compact U(1) in the same region and its layer phase first. (5) If V2 survives, the first lemma, tried by hand; if it dies, the counterexample or the first failing line.
- **Stop condition.** V2 is proved to rename an open statement, or a counterexample is built, or the first lemma is written and tried.
- **Marks.** PROVED, ARGUED, OPEN, FAILS. Negatives are scoped to what is proved.

### Step 2 result: repo-first check (what the lane already holds)

Searches run inside this checkout only (`grep -i` over `FINISH.md`, `library/`, `parts/`).

- `library/open-core.md`: no hit for "anisotrop". Its label CR (L92) is a statement of the T0 lane (outside minimizer bounds). It is not the gap lane's Theorem CR. No line there covers V2.
- `parts/gap.md` L153 (row 1053 with checks 1061, 1062): V2 is recorded as an OPEN uncompleted proposal. The lead follows check 1061. Gap-lane objects used below, from `parts/gap.md`: (W) (L22-24), (PHYS-SEED) and the fixed-coupling (SEED) with a carry (L25-27), Theorem CR with (LIOU) (L139), T_JW-lat (L152; defined in `library/gap-wall-assumptions-opus.md` L485).
- FINISH rows that mention the objects: "Karsch": rows 711, 995 (sum rules; no anisotropic matching used). "layer phase", "Fu and Nielsen": only the reading row 992 (`library/prior/gap-3dmix-read-opus.md` L209-214: from memory, not read; one numerical 5D paper, Knechtli, Luz and Rago). "renormalized anisotropy", "Klassen": no hit before rows 1066, 1067. "(BR-L)": rows 1053, 1061, 1062. "Orland": rows 688, 1053, 1061, 1062.
- Nearest items already on file, not redone here: Lemmas FACE-LIM, ANCH, RIG, FACE-MW, Proposition ITER (row 1053, checked by rows 1061, 1062); the verdict on V1, FAILS at (BR-L) (holds in both checks); the k = 1 split (row 859; rows 988, 992: the path from zero temporal coupling); the one-loop coefficients N/(8 pi) and 11 N/(24 pi^2) (checked in rows 1061, 1062).
- Not on file: any statement about the renormalized anisotropy; any matching for the 2 + 2 split; any statement on the transverse correlation length in R; the bridge of V2 as an exact statement. These are the work of this row.
- **Row 1067** (`library/prior/gap-aniso-read-luna.md`): ABSENT in this checkout. I do my own short source check in step 3 and say what was and was not read.
- `scripts/lab_ops.py`: ABSENT in this checkout. No numeric run is made in this row (none is needed; see step 7).

### Step 3 result: what the named files give, and my own short source check

**From row 1053 (`library/gap-wall-vectors-max.md`).**
- Setting (3.2): lattice Z^2 x Z^2, points (u, x); u longitudinal (directions 0, 1), x transverse (directions 2, 3). Plaquette types L (planes (0,1)), T (planes (2,3)), M (mixed). Wilson weight exp(sum_p beta_type(p) x_p), x_p = (1/2) tr U_p. Couplings (beta_L, beta_M, beta_T).
- Face model M(beta_M, beta_T): the limit beta_L to infinity (Lemma FACE-LIM). Variables Phi_l(u) in SU(2), l a transverse link. Group G = SU(2)^(transverse sites), g independent of u.
- Lemma ANCH: M(beta_M, 0) is a product over transverse links of two-dimensional O(4) models ("sheets") with coupling beta_M. Corollary ANCH-W as corrected by rows 1061, 1062.
- V2 (3.3): there is eps > 0 with exponential clustering in R = { beta_T xi_2(beta_M)^2 <= eps, beta_L >= xi_2(beta_M)^2/eps }. Consumer as written there: "a continuum limit taken inside R".
- Kill test as written (4.2, L183): on the classical family (xi^2 beta, beta, beta/xi^2) "the sheets then have two-dimensional coupling g(a_perp) at the scale a_perp", so beta_T xi_2^2 = (4/g(a_perp)^2) exp(8 pi/g(a_perp)^2).

**From check 1061 (`library/gap-wall-vectors-check-astra.md`, gpt-6-astra, sections 4 and 5).**
- The one-loop numbers hold as leading exponentials only: log l_2 = pi beta + lower order, log l_4 = (3 pi^2/11) beta + lower order, each in its own units. Unknown prefactors and subleading logarithms must be kept.
- L183 is a matching assumption. The anchor has bare stiffness beta_M at the spacing a_long. With tree coefficients, beta_T xi_2^2 is (beta/xi^2) e^(2 pi beta) up to factors, and xi^2 = (beta/eps) e^(2 pi beta) puts the point in R. So the tree equations do not exclude R.
- The dimensional scaling of 6.6 is classical engineering, not a blocking flow.
- Verdict there: V2 is an uncompleted proposal. R is not proved. No Lorentz-invariant trajectory in R is built. The trajectory question is open.
- Attribution: the four-dimensional anchor is the lambda to 0 point of Orland 2008 (arXiv:0801.0389), after H. and E. Verlinde and I. Aref'eva; the transverse lattice is Bardeen, Pearson and Rabinovici's. Orland's regime in 2 + 1 dimensions needs (g'_0)^2 << g_0^(-1) exp(-4 pi/(N g_0^2)). He proposes, and does not establish, a link to the isotropic theory.

**From check 1062 (`library/gap-wall-vectors-check-opus.md`, Claude Opus 5.5, J2 and J7).**
- With R's own xi_2 and the classical relation beta_T = beta_M/xi^2: in R, xi_2(beta_M) a_long <= (eps/beta_M)^(1/2) a_perp. It keeps the verdict FAILS (S0). The lead follows check 1061.
- The disagreement between the checks is one point: check 1062 identifies a_perp/a_long with the bare ratio (beta_M/beta_T)^(1/2). Check 1061 says this identification is not proved. Step 5 below is about that point.

**Own short source check (row 1067 is absent).** Metadata and abstracts only. Folders `/tmp/row1066-lit-a`, `-b` (arXiv API: refused twice with "Rate exceeded"; nothing read), `/tmp/row1066-lit-c` (three arXiv abstract pages, read by `python3 -I /tmp/row1066-scripts/abs.py`). No paper was downloaded. Nothing is committed.

| Source | What it holds for this row | Read state |
|---|---|---|
| F. Karsch, "SU(N) gauge theory couplings on asymmetric lattices", Nucl. Phys. B 205 (1982) 285 | One-loop (background-field) derivatives of the space-like and time-like couplings with respect to xi = a/a_tau at xi = 1; their sum is b_0 = 11 N/(48 pi^2). The split is 3 + 1 (one fine direction). Domain: g to 0 at fixed xi, so every bare plaquette coupling is large. Values for SU(2), c_sigma' = 0.11403 and c_tau' = -0.06759 (sum 0.04644 = 22/(48 pi^2)): RECALLED by me, not read. | abstract as read by row 711 (`library/prior/gap-vir-lit.md` L31); numbers recalled |
| T. Klassen, "The anisotropic Wilson gauge action", Nucl. Phys. B 533 (1998) 557, arXiv:hep-lat/9803010 | "the determination of the renormalized anisotropy xi as a function of the bare anisotropy xi_0 and the coupling"; a parametrization "for 1 <= xi <= 6 and 5.5 <= beta <= infinity" (SU(3), 3 + 1), which "incorporates the known one-loop result". It solves "how to choose the bare anisotropies if one wants to take the continuum limit at fixed renormalized anisotropy". Numerical. The renormalized anisotropy is defined by comparing a physical quantity (the heavy-quark potential) in the two directions. | abstract read |
| P. Dimopoulos, K. Farakos, S. Vrentzos, arXiv:hep-lat/0607033 | The 4 + 1 anisotropic compact U(1) model has a "Layer phase, in which the forces in the 4-D subspace are Coulomb-like while in the transverse direction (fifth dimension) the force is confining"; it is "separated from the strongly coupled phase by a weak first order phase transition" and from the five-dimensional Coulomb phase by a second-order transition. Mean field and Monte Carlo. | abstract read |
| Y. Fu, H. B. Nielsen, Nucl. Phys. B 236 (1984) 167 | The layer phase was proposed there: layers must be able to carry a Coulomb phase, so for compact U(1) the layers are four-dimensional. | RECALLED, not read |
| J. Engels, F. Karsch, K. Redlich, arXiv:hep-lat/9408009 | Non-perturbative derivatives of the SU(2) couplings for thermodynamics. Not used. | abstract read |
| P. Hasenfratz, A. Hasenfratz (Lambda-parameter ratios, the Hamiltonian limit xi to infinity of the 3 + 1 split has finite one-loop coefficients) | Used only as a contrast in step 5. | RECALLED, not read |

Not found by me, not searched beyond the above: one-loop anisotropy coefficients for a 2 + 2 split; any rigorous result on the renormalized anisotropy; any rigorous result on anisotropic or layered lattice gauge theory. Row 1067 is the reading of record for these.

### Step 4 result (task 1): V2 stated exactly, as a chain

**Objects.**
- W(beta_L, beta_M, beta_T): the anisotropic Wilson SU(2) model above, on boxes, tori and their infinite-volume limit states.
- G_beta(u, u') = E[s(u) . s(u')] for one sheet (the two-dimensional O(4) model with coupling beta). Posted theorems (OpenAI; Ding, Huang and Yang; GIVEN, unrefereed, read by the lane only): G_beta(R) <= A e^(-mR) for every beta.
- X(beta): a **mixing length of the whole sheet**. Definition (MIX): for all bounded sheet functions F, H with supports at distance d, abs(Cov(F, H)) <= C_F C_H e^(-d/X(beta)), uniformly in the box and in boundary pins, with C_F depending on F through its support size and sup norm only. X >= xi_2. For SU(2), (MIX) with X finite at every beta is the mixing bound of OpenAI's O(4) text as rows 1009 and 1010 read it (reading only; not checked in the lane). **Correction to row 1053's R:** R must be written with X, not with the two-point length xi_2. Reason: test K1 in step 7 (a product sheet).
- R_eps = { (beta_L, beta_M, beta_T) : beta_T X(beta_M)^2 <= eps and beta_L >= X(beta_M)^2/eps }.
- For a coupling point P with a translation-invariant limit state: l_par(P) and l_perp(P) are the correlation lengths of gauge-invariant local observables under longitudinal and transverse translations, each in its own lattice unit. That is, 1/l is the supremum of the exponential rates that hold for all such observables. Values lie in [0, infinity].
- **Renormalized anisotropy:** xi_R(P) = l_par(P)/l_perp(P), when both lie in (0, infinity). This is the definition by a physical quantity measured in both directions (as Klassen does with the potential). On a family that restores isotropy, a_perp/a_long = xi_R (1 + o(1)) for every such definition. The **bare anisotropies** are xi_MT = (beta_M/beta_T)^(1/2) and xi_LM = (beta_L/beta_M)^(1/2). Classically both equal a_perp/a_long.

**The chain V2.**
1. **(S), the seed. OPEN.** There are eps > 0, c > 0, C such that at every P in R_eps the limit state is unique and clusters exponentially on gauge-invariant local observables. Quantitative form **(S-q)**: l_par(P) <= X(beta_M)/c, and truncated correlations at transverse distance t are at most C_F C_H (C eps)^t. Inputs: Lemmas FACE-LIM and ANCH (row 1053, PROVED, checked); (MIX) (GIVEN, reading only); a convergent expansion about the anchor (OPEN; step 6 tries its first two orders).
2. **(T), the trajectory. Decided in step 5: none inside R_eps.** A sequence P_j in R_eps with l_par, l_perp to infinity and xi_R fixed (or bounded), whose limit is O(4) invariant.
3. **(B), the bridge. Stated in step 5.** Needed because (T) fails. A statement that carries clustering from R_eps to the isotropic model at a coupling of the band, or to an isotropic continuum limit.
4. **Consumer.** Lattice form: T_JW-lat of row 1052 (`library/gap-wall-assumptions-opus.md` L485) at one coupling, then the lane's carry to finer cutoffs (row 978, conditional), then T_JW with T0's data. On tori with flux sectors: the fixed-coupling (SEED) of `parts/gap.md` L25-27, hence (PHYS-SEED) and (W). Continuum form: a gapped O(4)-invariant continuum limit of anisotropic lattices, plus (UNIV-aniso): this limit is the theory that the Sussman-Alpoge account, after Balaban, builds on isotropic lattices. (UNIV-aniso) is OPEN and not on file; the account has no anisotropic version.

(Journal volume and page data in the table of step 3 are recalled, except what the abstract pages show.)

### Step 5 result (tasks 2 and 3): the matching, the trajectory question, the bridge

#### 5.1 R in bare variables (PROVED; algebra only)

**Lemma BARE.** P lies in R_eps if and only if xi_MT >= (beta_M/eps)^(1/2) X(beta_M) and xi_LM >= X(beta_M)/(eps beta_M)^(1/2).
Proof. beta_T X^2 <= eps reads beta_M/beta_T >= beta_M X^2/eps. beta_L >= X^2/eps reads beta_L/beta_M >= X^2/(eps beta_M). QED

**Corollary BARE-1 (PROVED).** The classical family (xi_0^2 beta, beta, beta/xi_0^2) lies in R_eps exactly when xi_0 >= X(beta) max((beta/eps)^(1/2), (eps beta)^(-1/2)). So R_eps contains bare families with beta to infinity. This is check 1061's remark, and it HOLDS. It is also check 1062's inequality, read as a statement about the **bare** ratio: in R_eps, X(beta_M) <= (eps/beta_M)^(1/2) xi_MT.

So both checks are right about what they prove. Check 1062 bounds the bare ratio. Check 1061 says the bare ratio is not yet the physical ratio a_perp/a_long. What decides the row is the renormalized anisotropy.

#### 5.2 The decision without any matching (PROVED GIVEN (S-q))

**Proposition PERP-BD.** Assume (S-q) with C eps < 1. Then for every P in R_eps: l_perp(P) <= 1/log(1/(C eps)). Hence:
(a) no sequence in R_eps has l_perp to infinity;
(b) on a sequence in R_eps with xi_R bounded, l_par = xi_R l_perp is bounded, so the longitudinal cutoff is not removed either;
(c) on a sequence in R_eps with l_par to infinity, xi_R >= l_par log(1/(C eps)) to infinity.
Proof. (S-q) gives the transverse rate log(1/(C eps)) for every gauge-invariant local observable. (a), (b), (c) are the definition of xi_R. QED

**Reading.** An isotropic continuum limit needs l_perp to infinity: if l_perp stays bounded, the transverse lattice is seen at the scale of the correlation length, and no rotation that mixes a longitudinal with a transverse direction can act on the limit. So:

> **Answer to the row's first question (PROVED GIVEN (S-q)).** R_eps contains no family of anisotropic Wilson couplings with fixed, or bounded, renormalized anisotropy that reaches a continuum limit, and no family at all that removes the transverse cutoff. R_eps meets the level set { xi_R = k } of a large renormalized anisotropy only in its coarse part, l_perp <= 1/log(1/(C eps)) < 1 for small eps.

**Scope.** This rests on (S-q), which is V2's own seed in the form that a convergent expansion about the anchor gives. If (S-q) is false, V2 has no seed in R_eps and the question is empty. If only a clustering statement with an unknown transverse rate holds in R_eps, the proposition is not available, and 5.3 is the argument on file. Support for the form (C eps)^t: Lemma PERP of step 6 (PROVED on finite boxes at beta_L = infinity) shows that the transverse covariance vanishes to order t in beta_T.

What a limit inside R_eps does give (ARGUED): with beta_M to infinity it is a continuum limit in the longitudinal directions only. The transverse lattice stays, with spacing above the correlation length. That is the transverse-lattice theory of Bardeen, Pearson and Rabinovici in Orland's weakly coupled regime: sheets with a small coupling. It is not O(4) invariant and is not the target.

#### 5.3 The matching, with the assumption of L183 removed (ARGUED; the perturbative and non-perturbative steps are named)

Block the longitudinal directions by a factor b and keep the transverse lattice. Write beta_M(b), beta_T(b), beta_L(b) for the couplings of the blocked model at the longitudinal scale b a_long.

**(a) Counting (exact).** A blocked transverse plaquette term collects b^2 sites u. A blocked longitudinal plaquette covers b^2 plaquettes. This gives the classical factors b^2 beta_T and beta_L/b^2 and leaves beta_M (row 1053 6.6 as corrected by check 1061).

**(b) The sheet window (PERTURBATIVE: asymptotic freedom of the two-dimensional O(4) model; not a theorem).** While beta_T(b) << beta_M(b) and beta_L(b) >> beta_M(b), the sheets fluctuate independently at the scales between a_long and b a_long. Then:
- the stiffness runs by the two-dimensional law. I define beta_M(b) by X(beta_M(b)) = X(beta_M)/b. With X(beta) = K_2 beta^(-1/2) e^(pi beta) (1 + o(1)) (two-loop form for n = 4; K_2 unknown; recalled) this is beta_M(b) = beta_M - (1/pi) log b - (1/(2 pi)) log(beta_M/beta_M(b)) + o(1);
- each sheet field is renormalized, Phi = z(b) Phi_blocked, z(b) = (beta_M(b)/beta_M)^(3/4) (1 + O(1/beta_M(b))). This is the square root of the short-distance law G(r) proportional to beta(r)^((n-1)/(n-2)), n = 4 (Brezin and Zinn-Justin; recalled). At first order, z = 1 - (3/(4 pi beta_M)) log b;
- the transverse plaquette is a product of four fields on four different sheets, so beta_T(b) = K_T b^2 beta_T (beta_M(b)/beta_M)^3, K_T an unknown constant of order one.
**This factor is what L183 dropped.** At one loop it reads: the bare ratio and the renormalized ratio differ by xi_MT = xi_R (1 + (3/(2 pi beta)) log xi_R + ...). The coefficient grows like log xi_R.

**(c) Where Karsch's coefficients stand (PERTURBATIVE; domain stated).** Karsch's one-loop coefficients are for the 3 + 1 split, at fixed xi, for g to 0. Every bare plaquette coupling is then large. In the 3 + 1 split the coefficients stay bounded as xi grows (the Hamiltonian limit; Hasenfratz and Hasenfratz; recalled), because the fine direction is one-dimensional and has no logarithm. In the 2 + 2 split the fine directions are two-dimensional, and (b) shows that the matching coefficients grow like log xi. So the expansion parameter of a Karsch-type relation in the 2 + 2 split is (1/(pi beta)) log xi, and its domain is log xi << pi beta, that is xi << X(beta) up to powers of beta. By Lemma BARE every point of R_eps has xi_MT >= (beta_M/eps)^(1/2) X(beta_M). **So no point of R_eps lies in the domain of a one-loop anisotropy matching.** In R_eps the bare transverse coupling is below eps X^(-2), far inside strong coupling, and the sheets reach their own strong coupling before the transverse scale. I know no published 2 + 2 coefficients (not searched beyond step 3).

**(d) The two ways the window ends (NON-PERTURBATIVE).**
- **Case (i): the sheets become massive first.** beta_M(b) falls to order one at b of order X(beta_M) while beta_T(b) is still small. The input here is the two-dimensional gap, a non-perturbative fact (the posted theorems). Then the blocked model is a set of massive sheets with a small coupling, and the transverse correlation length is below one lattice unit (5.2). By (b), case (i) holds when K_T beta_T X(beta_M)^2 beta_M^(-3) is small. This contains R_eps. (So the region where the seed is expected is larger than R_eps by the factor beta_M^3. ARGUED; not used.)
- **Case (ii): the sheets couple first.** At some b_* the blocked transverse coupling reaches the blocked stiffness: beta_T(b_*) = beta_M(b_*) =: beta_*. From there the model is four-dimensional with all blocked couplings near beta_*, the renormalized anisotropy is xi_R = K_R b_*, and the four-dimensional law takes over. If beta_* is large, the remaining matching is of Karsch's kind with bounded coefficients (perturbative). The statement that this four-dimensional model then has a finite correlation length of order exp((3 pi^2/11) beta_*) transverse units is **not** perturbative: it is the mass gap of the isotropic theory at weak coupling.

**(e) The corrected formula.** In case (ii), b_*^2 beta_T K_T (beta_*/beta_M)^3 = beta_* and X(beta_M) = b_* X(beta_*). So

  beta_T X(beta_M)^2 = (1/K_T) beta_* (beta_M/beta_*)^3 X(beta_*)^2 = K beta_M^3 beta_*^(-3) e^(2 pi beta_*) (1 + o(1)),   beta_M = beta_* + (1/pi) log xi_R + lower order,

with K > 0 unknown. Row 1053 had (4/g^2) exp(8 pi/g^2) = beta_* e^(2 pi beta_*). The leading exponential is the same. The power is different, and there is a new factor (beta_M/beta_*)^3 >= 1 that grows with the anisotropy. Check 1061 said that a large anisotropy makes the missing logarithm more important. That holds, and the logarithm pushes the family further out of R_eps.

**(f) Decision (ARGUED).** A family with fixed xi_R that restores isotropy at weak transverse-scale coupling is case (ii) with beta_* to infinity. On it beta_T X(beta_M)^2 >= K e^(2 pi beta_*) to infinity. So it leaves R_eps as soon as K e^(2 pi beta_*) > eps, that is at beta_* of order one or below, whatever the unknown constants are. Inside R_eps the model is in case (i). This agrees with 5.2 and does not use it. What is perturbative: (b), (c), and the Karsch-type step in (ii). What is not: the two-dimensional gap that ends case (i); every statement at a scale where a blocked coupling is of order one; the four-dimensional correlation length in (ii).

**Mark for task 2.** No family of fixed renormalized anisotropy inside R_eps reaches a continuum limit: PROVED GIVEN (S-q) (5.2); ARGUED without it (5.3). The renaming argument of row 1053 4.2 is replaced, not repaired: its formula is corrected in (e), and its conclusion that a trajectory must leave R holds on these two grounds.

#### 5.4 The bridge (task 3)

Since no continuum limit lies inside R_eps, the chain needs a transport out of R_eps. Two exact forms.

**(BR-iso)_beta, lattice form.** "For one point P_0 in R_eps and the isotropic point P_1 = (beta, beta, beta): if (S) holds, then every limit state at P_1 clusters exponentially on gauge-invariant local observables." Here beta is a coupling at which no theorem gives clustering; for the lane, a coupling of the window 2.3 to 2.6 or above.

**(BR-cont)_k, continuum form.** "On the level set xi_R = k, parametrized by s = l_perp in [s_0, infinity), the gap in units of one fixed physical scale is bounded below, uniformly in s; and (UNIV-aniso) holds."

**Proposition REN (PROVED; it is a statement about what the chain contains).**
(1) (S) and (BR-iso)_beta give T_JW-lat at the coupling beta at one cutoff. Given (S), (BR-iso)_beta is equivalent to that conclusion. In torus form with the flux sectors, the conclusion is the fixed-coupling (SEED) at beta, which with the carry of row 978 is a sufficient form of (PHYS-SEED), hence of (W) (`parts/gap.md` L25-27).
(2) (BR-cont)_1 is the isotropic statement itself. (BR-cont)_k for k not 1 contains the gap of the continuum theory, by (UNIV-aniso).
(3) V1's open pair gives V2's bridge: R_eps contains the face points (infinity, beta_M, beta_T) with beta_T <= eps X^(-2); so (FACE-SG) for beta_T in [eps X(beta)^(-2), beta] together with (BR-L) of row 1053 3.2 gives (BR-iso)_beta. V2 adds the seeded corner to V1 and removes none of V1's open statements.
Proof. (1) and (2) are the definitions of T_JW-lat, (SEED) and (UNIV-aniso). (3): follow the face from the edge of R_eps to beta_T = beta, then lower beta_L from infinity to beta; the two statements give clustering along that path. QED

**Is there a mechanism that makes the bridge less than the target?** V2 names none. I looked for one and found none:
- A soft bridge (clustering persists along a path of couplings, with no group-dependent input) is false: compact U(1) is a counterexample (step 7, Proposition U1-BR).
- Monotonicity in the couplings: for U(1) Ginibre's inequality makes Wilson loops increase with every coupling, so it bounds the tension at the isotropic point from above. It is the wrong direction, and for SU(2) no such inequality is on file.
- A blocking flow in the transverse scale: inside R_eps it runs toward the anchor (case (i)). The bridge runs against it, from l_perp below 1 to l_perp to infinity, through the scales where the blocked couplings are of order one. That is a (K-flow) statement in the sense of lead rule W2. V2 supplies no step for it.
- The two-dimensional theorems cross the two-dimensional band of one sheet. They say nothing at scales where the sheets are coupled at order one.

**Verdict for task 3.** The bridge is an open statement that contains T_JW-lat at one coupling, and in torus form the fixed-coupling (SEED), hence (PHYS-SEED) and (W) given the carry. I did not show that it contains (LIOU) of Theorem CR. So **V2 FAILS as a route by S0, as V1 did at (BR-L)**: PROVED as a containment (Proposition REN); the absence of a cheaper mechanism is ARGUED and is scoped to the four items above. This is a verdict on V2 as proposed. It is not a statement about every use of anisotropic lattices.

### Step 6 result (task 5): the first failing line of the route; the first lemma of the seed, tried by hand

#### 6.1 The first failing line

V2 as a route dies at row 1053 L138: "Consumer: a continuum limit taken inside R." There is none (5.2, 5.3). The next line that the chain then needs is the bridge, and it contains the target (Proposition REN). The counterexample to the soft form of the bridge is in step 7.

What is left of V2 is the seed (S): a positive control, with no consumer toward (W). The row asks for a first lemma tried by hand. I take the first lemma of (S) on the face beta_L = infinity. Rule 0a: no row covers it (step 2; row 1053 4.2 says of the anchor region "not proved here").

#### 6.2 Lemma PERP (PROVED): at the anchor, transverse covariances vanish to the order of the transverse distance

**Setting.** The face model M(beta_M, beta_T) on a finite box Lambda_long x Lambda_perp with free boundary. E_0 is the anchor expectation: a product over transverse links l of sheet measures mu_l (Lemma ANCH). X_T = sum over transverse plaquettes p and sites u of x_p(u), x_p(u) = (1/2) tr G_p(u). E_t has density e^(t X_T)/E_0[e^(t X_T)] with respect to E_0, t = beta_T.

For a set P of transverse plaquettes and a set A of transverse links, let cl_P(A) be the smallest set of links that contains A and contains the boundary of every p in P that meets it. For link sets A, B let d(A, B) be the least size of a set P with cl_P(A) meeting B.

**Statement.** Let F be a bounded function of the sheets on the links of A, and H of the sheets on the links of B. Then for every k < d(A, B): (d/dt)^k Cov_t(F, H) at t = 0 is zero. So Cov_t(F, H) = O(t^(d(A, B))) as t to 0, on each finite box.

**Proof.** All functions are bounded and the box is finite, so t to Cov_t(F, H) is real-analytic. For the tilted family E_t the joint cumulants obey (d/dt) kappa_t(F_1, ..., F_n) = kappa_t(F_1, ..., F_n, X_T) (differentiate log E_0[exp(sum s_i F_i + t X_T)] in the s_i at s = 0, then in t). So (d/dt)^k Cov_t(F, H) at 0 is kappa_0(F, H, X_T, ..., X_T) with k entries X_T. By multilinearity it is the sum over (p_1, u_1), ..., (p_k, u_k) of kappa_0(F, H, x_(p_1)(u_1), ..., x_(p_k)(u_k)). Fix one term and let P = {p_1, ..., p_k}, C = cl_P(A). Since k < d(A, B), C does not meet B. Split the entries into two groups: F and the x_(p_i) with boundary inside C; H and the x_(p_i) with boundary disjoint from C. By the definition of the closure, every p_i is in one of the two groups. The first group is a function of the sheets on C, the second of the sheets off C. Under the product measure E_0 the two groups are independent, and a joint cumulant of two independent non-empty groups is zero. QED

Remarks. (1) The lemma is blind: it holds for every compact group, U(1) included. That is right, because it concludes nothing about a gap. (2) It is a finite-box statement. The constants in O(t^d) are not uniform in the box. Uniformity is the content of (S). (3) Lean form: the cumulant derivative identity, multilinearity, and vanishing of mixed cumulants of independent families.

#### 6.3 The second order by hand, and the first open line of (S)

Take a transverse plaquette p with boundary links 1, 2, 3, 4, and G_p(u) = Phi_1(u) Phi_2(u) Phi_3(u)^(-1) Phi_4(u)^(-1) (up to the orientation convention). Let F depend on sheet 1 only and H on sheet 2 only. Then d = 1.

**Claim S2 (PROVED on a finite box).** Cov_t(F, H) = c_2 t^2 + O(t^3), with

  c_2 = (1/16) sum over u, u' of G(u, u')^2 tr( <F ; Phi_1(u')^(-1) Phi_1(u)>_0 <H ; Phi_2(u) Phi_2(u')^(-1)>_0 ),

where G is the two-point function of one sheet on Lambda_long and <F ; A>_0 = E_0[F A] - E_0[F] E_0[A] is a matrix.

**Proof.** First order. Each sheet measure is invariant under Phi_l to -Phi_l on the whole sheet (an element of O(4)). x_p(u) is odd under the flip of sheet 3, and F, H do not depend on sheet 3. So kappa_0(F, H, x_p(u)) = 0. For a plaquette q other than p, Lemma PERP gives 0, since q does not contain both links 1 and 2 (two plaquettes of Z^2 share at most one link). Second order. A pair (p, q) with q not p has a link of q outside the boundary of p; flipping its sheet gives 0. A pair without p is 0 by Lemma PERP. So c_2 = (1/2) sum over u, u' of kappa_0(F, H, x_p(u), x_p(u')). All moments with an odd number of x vanish and Cov_0(F, H) = 0, so kappa_0(F, H, x, x') = E_0[F~ H~ x x'], F~ = F - E_0 F, H~ = H - E_0 H. Write x_p(u) = <M(u), N(u)> with M = Phi_1 Phi_2, N = Phi_4 Phi_3, and <a, b> = (1/2) tr(a b^(-1)) the inner product of unit quaternions in R^4. Sheets 3 and 4 are independent of everything else. The matrix E_0[N(u) (x) N(u')] on R^4 is invariant under N to g N h (left invariance of sheet 4, right invariance of sheet 3), so it is (c/4) times the identity, with c = E_0<N(u), N(u')> = (1/2) tr(E_0[Phi_4(u')^(-1) Phi_4(u)] E_0[Phi_3(u) Phi_3(u')^(-1)]) = G(u, u')^2 (each expectation is G times the identity, as in Corollary ANCH-W). So E over sheets 3, 4 of x x' is (G^2/4) <M(u), M(u')>. And <M(u), M(u')> = (1/2) tr(Phi_1(u')^(-1) Phi_1(u) Phi_2(u) Phi_2(u')^(-1)); the first two factors depend on sheet 1, the last two on sheet 2, and the sheets are independent. Collect: (1/2)(1/4)(1/2) = 1/16. QED

**What it shows (the try).**
- With only the decay of the two-point function (the statement of Ding, Huang and Yang, and of OpenAI's O(n) text), the best bound is abs(c_2) <= (1/2) sup abs(F) sup abs(H) sum over u, u' of G(u, u')^2. The sum grows like the area of Lambda_long. So two-point decay does not bound even the second order uniformly in the box.
- With (MIX), abs(<F ; Phi_1(u')^(-1) Phi_1(u)>_0) <= C_F e^(-dist(supp F, {u, u'})/X). Then abs(c_2) <= C_F C_H sum over u, u' of G(u, u')^2 e^(-(d_F + d_H)/X) <= C'_F C'_H X^2 sum over r of G(r)^2 <= C''_F C''_H X^4. So the second order is at most a constant times (beta_T X^2)^2, uniformly in the box. This is the small parameter in the definition of R_eps, found by hand at the first non-zero order. (With the short-distance law of 5.3 (b) the sum over r of G(r)^2 is of order X^2 beta_M^(-3), which is where the extra factor of 5.3 (d) comes from. ARGUED.)
- **First open line of (S):** (MIX) for the sheet, with constants depending on the observable as stated, for insertions Phi(u')^(-1) Phi(u) at arbitrary distance; and then the bound of the k-th order by C^k (beta_T X^2)^k with no factorial, that is a convergent polymer expansion in the plaquette activities e^(t x_p(u)) - 1 around a mixing product measure. (MIX) is GIVEN only as a reading (rows 1009, 1010). The convergence is OPEN. Neither is tried further here: (S) has no consumer after 5.4.

**Mark.** Lemma PERP: PROVED. Claim S2: PROVED on finite boxes. The uniform second-order bound: PROVED GIVEN (MIX) up to the elementary sums (written as estimates, constants not tracked: ARGUED at that level). (S) and (S-q): OPEN.

### Step 7 result (task 4): the kill tests

Tests in the form of the lane's kill sheet (`library/gap-invent-selective-max.md` L52-63). A model refutes a claim only if the hypothesis holds there and the conclusion fails. A pass is no support. Two objects are tested: the seed (S) with Proposition PERP-BD, and the bridge (BR-iso).

#### 7.1 Compact U(1) in the same region, and the layer phase (first control)

Replace SU(2) by U(1). The sheets are plane-rotator models with coupling beta_M.

**Facts used.** (F1) For small beta_M and beta_T the face model of U(1) is a compact spin system on Z^4 with finite-range interactions of small strength, so it has a unique Gibbs state with exponential clustering (Dobrushin's uniqueness theorem; recalled). (F2) At large beta the plane rotator has no exponential bound on its two-point function (Frohlich and Spencer 1981, as cited in the lane, row 1007 B(3)). (F3) Isotropic compact U(1) at very large beta is in the Coulomb phase: no exponential clustering (Guth; Frohlich and Spencer; in the lane for Villain at beta at least 2^14, `parts/gap.md` test table).

**The seed under U(1).** X_U1(beta_M) is infinite at large beta_M by (F2). So R_eps for U(1) is empty there (it forces beta_T = 0), and the seed claims nothing. At small beta_M the U(1) region is not empty and U(1) does have a gap there by (F1), at least on the face. So no step of (S) gives U(1) a gap where it has none. The step that separates the groups is "X(beta_M) is finite at every beta_M": a theorem-grade difference (F2 against the posted O(4) theorems). Lemma PERP and Claim S2 hold for U(1) and conclude no gap. **Pass.**

**U(1) at the bare couplings of SU(2)'s region (large beta_M, small beta_T, beta_L = infinity; ARGUED).** At beta_T = 0 the sheets are in the Kosterlitz-Thouless phase. The mixed loop has expectation G(R)^T with G a power of R. The transverse plaquette term cos(theta_1 + theta_2 - theta_3 - theta_4) is a product of four vertex operators, each of dimension 1/(4 pi beta_M) at the Gaussian level, so its dimension is 1/(pi beta_M) < 2: it is relevant. So a small beta_T does not leave decoupled critical sheets; it leads to the four-dimensional Gaussian behaviour of row 1053 6.6 (curl correlation abs(u)^(-4), no gap). So in this corner U(1) has no gap and no stable layer phase is expected. This agrees with Fu and Nielsen's criterion as I recall it: a layer phase needs layers that carry a Coulomb phase, four-dimensional layers for U(1). The numerical layer phase is in the 4 + 1 model (Dimopoulos, Farakos and Vrentzos, abstract read).

**What the layer phase teaches for the bridge (GUIDE).** In the 4 + 1 U(1) model an anisotropic corner is a phase of its own, separated from the isotropic weak-coupling phase by a transition. So "the anisotropic corner and the isotropic point are joined without a transition" is a claim with content. It is false in an abelian relative. For SU(2) in the 2 + 2 split it is believed (Orland posits a crossover) and not proved. The bridge contains it.

**Proposition U1-BR (PROVED GIVEN (F1) and (F3)): the soft bridge is false.** Let B_soft be the statement "for a compact gauge group, if the limit state clusters exponentially at one point of the face with small beta_T, then every limit state clusters exponentially at each isotropic point (beta, beta, beta)". Then B_soft is false for U(1).
Proof. By (F1) the hypothesis holds at a face point with beta_M, beta_T small. By (F3) the conclusion fails at beta at least 2^14 (Villain form; for the Wilson form the same is the published theorem as recalled). QED
So a proof of (BR-iso) must use the group between the two points. It cannot be continuity, analyticity on a neighbourhood, or any property that U(1) shares.

#### 7.2 The table

| Test | Seed (S), Proposition PERP-BD | Bridge (BR-iso) |
|---|---|---|
| K1 Lemma PT (product with a massless factor) | With row 1053's R (two-point length of the SU(2) sheet) the seed is expected to be false for gauge group SU(2) x U(1) (ARGUED, by 7.1: the U(1) factor has no gap at large beta_M and small beta_T; theorem-grade only for its charged two-point function at beta_T = 0), while the SU(2) length is finite. With R_eps written with the mixing length X of the whole sheet (step 4), X is infinite for the product and the hypothesis is void. **Pass after this correction.** | The conclusion step must read the whole state space. No step is given. |
| K2 Proposition NP | No induction on D. Not engaged. | Not engaged. |
| K3 Theorem D2, K3' slab | (S) is stated for limit states of the constant-coupling model. It is not a supremum over tilts or over pinned interior link sets. Pass in that form. It must not be widened to pinned transverse link sets. | No statement to test. |
| K4 Lemma SHEET, fixed-b form | The class is beta_L >= X(b)^2/eps, beta_M in [0, b], beta_T <= eps X(b)^(-2). It is not all coupling fields: beta_L is bounded below, so the tube of Lemma SHEET (large coupling on the sides, zero elsewhere) is not in it. Cut-outs with beta_M = 0 on a set are sub-sheets; the posted O(n) theorem is uniform over them (as row 1007 reads it). Pass, ARGUED. | (BR-iso) is stated for constant couplings only. |
| K5 compact U(1) | Pass (7.1). | **The soft form is refuted (Proposition U1-BR).** |
| K6 frozen Q_8, 2T | The sheets order at large beta_M (Peierls), the two-point function does not decay, X is infinite, R_eps is empty there. Void. | These groups do not bind T_JW-lat (row 1052 6c). They bind a torus form with flux sectors. |
| Pin(2) of Lemma EVEN (GUIDE) | At large beta_M the component orders and the circle part is a plane rotator: no exponential bound, X infinite. Void. | Expected false for Pin(2) at large beta (belief). A proof must use non-commuting infinitesimal rotations between the two points. |
| K7 five dimensions (2 + 3 split) | The anchor and R_eps exist verbatim; (S) is blind to d_perp. Consistent, since R_eps is far from the isotropic point. In 5.3 the dimension enters only at the last step of case (ii): the correlation length of the four-dimensional model at weak coupling. In five dimensions that length is infinite. | False in the 2 + 3 split at weak isotropic coupling (GUIDE, numerics). A proof must read d_perp = 2. |
| K8 refilling | No field is refilled. Not engaged. | Not engaged. |
| Lemma CEN+ | The only rigid group used is G on the face, a group of gauge transformations. No conflict. | No rigid map is proposed. |
| Lemma WN | At finite beta_L the in-plane links are not flat. The second inequality of R_eps keeps the accumulated in-plane fluctuation over one correlation area at most eps. So the fixed cost of Lemma WN is the reason for that inequality. Pass, ARGUED. | Outside R_eps the cost is not small. No step is given. |
| K9, S0 | Not a renaming: (S) is a new positive statement. It has no consumer toward (W). | **FAIL (S0): Proposition REN.** |
| K9, S1-S4 | S1 yes (through the posted theorems, which use the rotations of S^3). S2: a rate, 1/X(beta_M) longitudinal. S3: yes with X of the whole sheet. S4: constant couplings, or the restricted class of K4. | S1-S4 cannot be judged: no mechanism. |

**Numeric run.** None. `scripts/lab_ops.py` is absent in this checkout, and no test above needs a number. No guide script was written.

**Verdict of the kill pass.** The seed passes every test, after one correction to the definition of R (K1). The bridge fails S0, and its soft form is refuted by U(1). K7 and Pin(2) say what a future bridge must read: the dimension d_perp = 2 and the Lie algebra.

### Step 8 result: summary, marks, hand-over, RESULT

Written at 2026-11-17T00:23Z (`date -u`). Claude Fable 5.2 medium, one laptop subagent, no further subagent. Only this file was written. Nothing was committed or pushed. No numeric run. Not checked by anyone.

#### 8.1 Plain report

The question was whether the anisotropic corner R, where the sheets of the anchor are decoupled, holds a road to the isotropic continuum theory. It does not. Inside R the transverse correlation length stays below one transverse lattice unit. So a limit inside R removes the longitudinal cutoff only; it is a transverse-lattice theory, not a rotation-invariant one. A family with fixed renormalized anisotropy passes through R only in its coarse part and then leaves it. To go on, the route needs a bridge from R to the isotropic model, and that bridge contains the target at one coupling. V2 names no mechanism for it, and compact U(1) refutes every mechanism that does not use the group. So V2 fails as a route, in the same way as V1. The matching that row 1053 assumed at L183 is now written out: it dropped a field-renormalization factor, which changes a power and not the exponential, and which works against the route. Karsch's one-loop coefficients do not apply anywhere in R. What stays is the seed in R as a positive control, with its first lemma proved and its first open line named.

#### 8.2 Marks

| Item | Mark | Where |
|---|---|---|
| Lemma BARE, Corollary BARE-1 (R in bare variables; both checks reconciled) | PROVED | 5.1 |
| Proposition PERP-BD (no continuum limit, and no fixed renormalized anisotropy with diverging lengths, inside R_eps) | PROVED GIVEN (S-q) | 5.2 |
| The matching without L183: beta_T X(beta_M)^2 = K beta_M^3 beta_*^(-3) e^(2 pi beta_*), beta_M = beta_* + (1/pi) log xi_R + lower order; decision that a fixed-xi_R family leaves R_eps at beta_* of order one | ARGUED | 5.3 |
| No point of R_eps is in the domain of a one-loop (Karsch-type) anisotropy matching | ARGUED | 5.3 (c) |
| Proposition REN (the bridge contains T_JW-lat at one coupling; in torus form (SEED), hence (PHYS-SEED) and (W) given the carry; V1's open pair gives V2's bridge) | PROVED | 5.4 |
| V2 as a route to the gap | FAILS (S0 at the bridge; scoped to V2 as proposed and to the four mechanisms examined) | 5.4, 7.2 |
| Proposition U1-BR (the soft bridge is false) | PROVED GIVEN the cited U(1) theorems | 7.1 |
| Lemma PERP (transverse covariance vanishes to the order of the transverse distance, face, finite box) | PROVED | 6.2 |
| Claim S2 (second-order coefficient) | PROVED on finite boxes | 6.3 |
| Uniform second-order bound of order (beta_T X^2)^2 | PROVED GIVEN (MIX), constants not tracked | 6.3 |
| (S), (S-q): the seed in R_eps | OPEN (first open line: (MIX) as stated, then convergence of the expansion) | 4, 6.3 |
| (MIX) for the O(4) sheet | GIVEN as a reading only (rows 1009, 1010) | 4 |
| (BR-iso), (BR-cont), (UNIV-aniso) | OPEN; (BR-iso) and (BR-cont) contain the target | 5.4 |
| U(1) in the corner: transverse coupling relevant, no stable layer phase in the 2 + 2 split | ARGUED | 7.1 |
| Correction to row 1053: R must use the mixing length of the whole sheet | ARGUED (test K1) | 4, 7.2 |

#### 8.3 Hand-over to the lead

- `parts/gap.md` L153 can read: V2 is no longer an open route. The seed (S) is an open positive control. The trajectory question of check 1061 is answered: no continuum limit inside R (given (S-q); argued without it). The bridge contains T_JW-lat at one coupling (Proposition REN).
- The disagreement between checks 1061 and 1062 is settled this way: check 1062's inequality is true for the bare ratio (Lemma BARE); check 1061 is right that this is not the physical ratio; the physical statement is Proposition PERP-BD.
- This row needs a check. The items a checker should take first: the cumulant argument of Lemma PERP; the constant 1/16 in Claim S2; the exponent 3 and the two-loop form in 5.3 (b) (both recalled); Proposition U1-BR's use of Dobrushin's theorem for (F1).
- When row 1067 arrives, compare: Karsch's numbers and domain (recalled here); whether any 2 + 2 anisotropy coefficients are published; what is known of a layered phase for SU(2); any rigorous result. A published 2 + 2 matching that contradicts the logarithmic growth of 5.3 (c) would reopen 5.3, not 5.2.
- Not proposed: a proof row on (S). It has no consumer after 5.4. It would become useful only with a bridge mechanism that reads the group and d_perp = 2.

#### 8.4 Strong words, read against the run

"No family", "no continuum limit" in 5.2: conditional on (S-q), and said so. "FAILS" for V2: a containment (PROVED) plus the absence of a mechanism among four examined (ARGUED); it is not a statement about anisotropic methods in general. "Refuted" for the soft bridge: by U(1), given cited theorems. Nothing here says that the anchor region is gapped; that is (S), OPEN.

**Credits.** F. Karsch (anisotropy coefficients); T. Klassen (renormalized anisotropy); P. Hasenfratz and A. Hasenfratz; P. Orland (the weakly coupled anisotropic regime, 2006 to 2008), after H. and E. Verlinde and I. Aref'eva; W. Bardeen, R. Pearson and E. Rabinovici (transverse lattice); Y. Fu and H. B. Nielsen, and P. Dimopoulos, K. Farakos and S. Vrentzos (layer phase); J. Frohlich and T. Spencer, A. Guth (U(1)); R. Dobrushin; J. Ginibre; E. Brezin and J. Zinn-Justin; OpenAI, and J. Ding, F. Huang and P. Yang (two-dimensional O(n) theorems, posted, unrefereed); T. Balaban, and J. Sussman and L. Alpoge's account (the isotropic construction that (UNIV-aniso) refers to); rows 1053, 1061, 1062 of this lane.

RESULT: Row 1066 (Claude Fable 5.2 medium, laptop subagent, unchecked): V2 FAILS as a route to the gap, by S0 at its bridge, as V1 did at (BR-L). The region R holds no continuum limit and no family of fixed renormalized anisotropy with diverging lengths: PROVED GIVEN the quantitative seed (S-q) (Proposition PERP-BD: transverse correlation length below one lattice unit in R), ARGUED without it by the matching with L183 removed (corrected formula beta_T X^2 = K beta_M^3 beta_*^(-3) e^(2 pi beta_*); the dropped factor is the fourth power of the sheet field renormalization; Karsch's one-loop coefficients apply nowhere in R). The bridge out of R contains T_JW-lat at one coupling, and in torus form (SEED), hence (PHYS-SEED) and (W) given the carry (Proposition REN, PROVED); its soft form is refuted by compact U(1) (Proposition U1-BR, PROVED GIVEN the cited U(1) theorems); no selective mechanism is named. PROVED by hand: Lemma BARE, Lemma PERP (transverse covariances vanish to the order of the transverse distance at the anchor), Claim S2 (second-order coefficient; uniform bound of order (beta_T X^2)^2 GIVEN sheet mixing). OPEN: the seed (S) in R as a positive control (first open line: sheet mixing (MIX), then convergence), (BR-iso), (UNIV-aniso). One correction to row 1053: R must be defined with the mixing length of the whole sheet (test K1). Row 1067 was absent; own source check was abstracts only; no numeric run; (W) does not move.
