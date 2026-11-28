# Repo search

Written by OpenAI Codex (GPT-6; the exact deployment identifier and effort
are not exposed to this session). The task's `astra` filename is preserved.
Research check at `1f517fa35faaa9d4ff4728cbd6eb08549ef99df3`, not an audit.
This file grants no status and claims no mass gap. It does not check the
whole Yang--Mills construction, prove the infrared inputs, or use a run as
proof.

The target-specific prior digest is absent. The supplied November 8 digest
records searches of main and PRs 10114, 10133, 10134 and 10141, but its named
targets are earlier RG interfaces, not the present ultraviolet-rigidity
check. No matching row was found by searching `open-registry.md` for
`gap-uv`, `gap-compact`, `uv.rigid`, `rigidity`, `recurrence` and `Liouville`.
This is a check of row 1028, not a new attack on another row's open problem.
The relevant prior work identified by row 1028 is row 1017's engine and its
cross-provider correction at item 20. Those sources were used directly.

The November 8 digest was read in full. Its two closest outside-lane
hits were reopened at source after fetching the requested refs:

| Source checked | Closeness to this task |
|---|---|
| main `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`, `docs/PERIODIC_FINITE_CLOCK_VILLAIN_COVARIANCE_AND_OBSERVABLE_MASSLESSNESS_BOUNDED_THEOREM_NOTE_2026-09-14.md:79–94` | A finite-clock Villain model and its cochain conventions; a comparison model already cited by R, not a proof of ultraviolet rigidity or FV. No import. |
| PR 10114 `f76f6c649cff7dffbab664d8976e680e8f287fe9`, `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | A one-step plaquette witness, not the global seed or a critical-element theorem. No import or rederivation. |
| Local R253, R280–282 and the existing Codex check at 387–404 | Exact prior constant examples and correction of the erroneous boundary-condition inference; reused, not claimed new. |
| Local `gap-crux-skeleton-check-astra.md:305` | Exact prior frozen-group formula and spatial-triple interpretation; credited in item 2. |

No claim is made that this narrow check repeated the lead's full search
of all five refs. No target-specific “Repo prior work” line occurs in
row 1028. Its author itself reports a local-only search at U862–866.
The earlier RG-interface hits do not duplicate this requested check.

The mandatory FINISH-row read exposed the row 1030 result summary. Thus this
is not a blind check. Its detailed Claude report remains unopened until the
verdicts below have been written. Agreement alone will not count as evidence.

Sussman--Alpoge source credit: Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their text, commit `31a47c543775`. Both requested
sources were downloaded once into the newly created directory
`/tmp/sa-gap-uv-rigidity-check-astra.b6Y6KG/`. Only indexed excerpts are used.

## Working checkpoint

1. Done: fixed the engine's domain, normalization and relevant prior results.
2. Done: checked FV, CONST and TS by hand, including smallest-torus cases.
3. Done: checked ALPHA/KEPT, REC/REC+, and the numbered implications.
4. Done: saved the verdicts before opening the detailed Claude check.
5. Done: recorded disagreements, accepted corrections and final disposition.

No check obligation remains in this assignment. The unchanged open science
obligations are (LIOU), (BDD-Delta) and (W); they were not attacked.

Source text is unchanged. No numerical or symbolic proof run is planned.

## My verdicts, written before reading the Claude report

Here `U` means `gap-uv-rigidity-max.md`; `R` means
`gap-compact-rigidity-max.md`. Line numbers refer to the pinned checkout.
The numbered statements below include each clause of the named propositions.
HOLDS means the written implication holds with its named imports. It does
not certify those imports' physical application.

### 1. FV, U541–636 — HOLDS

The normalization agrees exactly with `gap-crux-restate.md:31–45`:
Haar probability, action `sum(1-tr(U_p)/2)`, and the infimum over all
rectangular tori. No thermodynamic-limit identification is needed.
Finiteness of that infimum follows from `-12 beta <= F/N <= 0`.

Line-by-line checks:

| Lines / step | Verdict and check |
|---|---|
| 553–563, geometry and (4.1) | HOLDS. The comb has N−1 edges. Quaternion distance equals the operator norm, and the action is half its square. |
| 565–570, A1 | HOLDS. The radial Haar integral and `1-cos(phi)>=2phi²/pi²` give the displayed Gaussian integral and coefficient. |
| 572–580, A2 | HOLDS. The least nonzero lower coordinate makes both transverse links tree edges. Each selected plaquette has only its upper mu-edge and possibly its lower mu-edge outside the tree. Their heights differ by one. Two selected plaquettes cannot share the same upper mu-edge; a putative different selected edge has the wrong direction or is the lower mu-edge with a different lower corner. |
| 582–586, A3 | HOLDS. Reverse height order removes one link from one remaining weight. Translation and inversion invariance give I(beta) at each integration. Dropped weights are at most one. |
| 588–591, A4 | HOLDS. Take n to infinity in the upper bounds for the infimum f. The negative sign of log I does not reverse that limiting argument. |
| 595–599, B1 | HOLDS. Rooted tree transports set every tree link to one. Conditional on tree links, the other link changes preserve product Haar measure. No division by a stabilizer occurs. |
| 601–609, B2–B3 | HOLDS. Each face is a commutator of the relevant commuting holonomies. Four-factor telescoping bounds its distance by 4r and its action by 8r². |
| 611–614, B4 | HOLDS. The cap lies in angular radius pi/3 for r<=1. Integrating `sin(t)>=2t/pi` gives `v(r)>=8r³/(3pi³)>r³/12`. |
| 616–627, B5 | HOLDS. Each angle grid has at least `pi/(2delta)` points and each axis coordinate at least `1/(2delta)`. Distinct axes differ by at least delta; `sin(theta)>=1/sqrt(2)` gives separation. Distinct angles on one axis also give separation. The chosen wrapping links exist and lie outside the tree. Open balls are disjoint even at equality 2r. |
| 629–632, B6 | HOLDS. The exponent of r is `3(3N+1)-6=9N-3`. Setting `r=beta^(-1/2)` gives precisely the displayed beta power. |
| 634–636, final subtraction | HOLDS. The bulk beta powers cancel to `(3/2)log beta`. The constants fit below `59N+11`. |

Here is a hand check of the harmless decimal margins, without using the
author's guard run. From `pi<22/7`,
`(pi/2)^5<(11/7)^5<(31/10)^2`: the last integer comparison is
`16,105,100<16,151,527`. The exponential series through degree four at
57/50 is `3.10709734>3.1`, so `log 3.1<1.14`.
The series through degree six at 5/2 is `553405/46080>12`.
The series through degree five at 7/5 exceeds four. Thus
`48+3log12+3.42<58.92<59` and `6log4+log12<10.9<11`.

**Smallest torus and zero modes.** At n=3 the tree has 80 links, the
slice 244 links, and the shelling 136 plaquettes, from the displayed
polynomials. No enumeration is needed. The linearized flat complex gives
the following separate check of the dimensional explanation at U640–645.
At a noncentral commuting flat point, the adjoint coefficients split into
one trivial real character and a charged real plane. The latter complex
is contractible: one nontrivial holonomy makes its corresponding difference
invertible, giving a contracting homotopy by contraction in that direction.
The trivial character contributes four harmonic one-forms. Gauge
directions have dimension `3N-1`; fixing the tree removes `3N-3` of them.
Hence the slice kernel has dimension `4+2=6`. At a central flat point all
three characters are trivial: harmonic dimension twelve, gauge dimension
`3N-3`, and slice kernel dimension twelve. For N=81 the slice dimension is
732, with generic rank 726 and central rank 720. These are dimension
identities, not a rank computation. The singular kernel causes no defect
in a lower bound built using the regular six-dimensional family.

U640–647 remains an explanation and a conjectured sharper asymptotic;
the packing proof does not prove an upper bound or a log-log term.
U673–678 correctly limits the proved divergence to fixed n as beta grows.
It does not establish divergence after taking the continuum limit at fixed
physical L.

### 2. FRZ, U688–717 — HOLDS, clauses (i)–(iv)

Tree gauge gives exactly `|G|^(N-1)c_4(G)` flat configurations. Shelling
sets every interior link to one; flat faces then make each wrapping
holonomy constant and force them to commute. This proves (i), including
unequal sides. The flat configurations give `f>=-3log|G|`. Taking beta to
infinity first at any fixed torus gives the reverse limsup bound with
error `log(c_4/|G|)/N`; then let N grow. This justifies (ii) without
interchanging limits. Subtract at fixed N for (iii).

For (iv), count pairs consisting of a commuting triple and an element
fixing that triple. Their number is c_4, so orbit counting gives c_4/|G|.
Q_8 has two central elements and six elements with centralizer C_4:
`8,40,176,736`. In 2T the remaining sixteen elements have centralizer C_6:
`24,168,1008,5856`. Division gives 92 and 244; Z_2 gives 8.
The recursions are small exact arithmetic. The frozen formula was already
credited in U877 to `gap-crux-skeleton-check-astra.md:305`; it is not a new
formula of this check. No finite-beta Peierls claim is inferred.

### 3. CONST, U727–740 — HOLDS, with its stated domain

(i) HOLDS for a function constant on **all** of DD^4, with
`log m<=D_0`. Fix B and use the atomic spectral representation from
`gap-dichotomy.md:131–134` (the D8 repair). A finite constant trace at
arbitrarily large dyadic T forces the lowest level to zero. Dominated
convergence at one positive time makes the trace tend to the integer
multiplicity m of that level. Thus `e^c=m`. Any finite positive level
would add a strictly positive term, contradicting the constant trace.
Now `s=m-1>=1/5041` forces m>=2. Conversely R253 supplies these limits;
their gap is zero, all engine inequalities hold, and all center signs
may be positive. (ii) HOLDS directly from the finite bound D_0.
(iii) HOLDS as the structural assertion with some sufficiently large
D_0; for a *fixed* D_0 retain the restriction in (i).

U742–757 does **not** prove multiple distinct objects for each prescribed
finite diagonal value c. Constants with different m have different c,
and adding constants gives another constant. Correct text:
“REC fixes only the diagonal values. The remaining candidate set consists
of critical elements with that diagonal. This note neither proves that
this set is a singleton nor constructs distinct members for each c.
Photon members remain conditional.” Verdict: HOLDS AFTER CORRECTION.

### 4. TS, U462–498 — HOLDS

For every finite j each factor has a simple leading eigenvalue one.
At a spatial box B the other eigenvalues are
`exp(-eps_j |B|/u_j^4)` (m_0−1 copies) and
`exp(-|B|/(rho u_j)^4)` (p−1 copies); the product takes all pairwise
products. Symmetry holds, `0<=log Z<=log(m_0 p)`, and f=0 by sending
the volume to infinity. The choice `u_j=12*2^j` satisfies both grids.
Set every center action equal to the identity; this satisfies the kept
grading, positivity and vacuum-sign conditions, without asserting a
Wilson realization or a faithful center representation.

The continuum expression at U469–471 follows at every fixed x. For
`y=(L/rho)^4`, differentiating
`h(y)=log p-log(1+(p-1)e^(-y))` gives
`0<=h'(y)<=(p-1)`, independently verifying the stated plateau bound.
The BDD bound is evaluated at y>=1. U478 uses l=L/l_1; writing that unit
explicitly gives `S_1=(m_0-1)exp(-eps_j(L/l_1)^4/2)`.

For any admissible extraction, the second factor disappears because
k_i tends to infinity. If `gamma_i=eps_(j_i)16^k_i` stays above a positive
number on a subsequence, choose one fixed large m; its thermal sum falls
strictly below 1/5041, contradicting H2. Thus gamma_i tends to zero and
the only possible limit is log m_0. Conversely k_i=i and
`eps_(j_i)<=16^(-3i)`, with j_i increasing, meet H1 and H2 eventually at
each fixed m. This proves nonemptiness and the asserted singleton Omega.
All CE properties, including its spectral form and engine inequalities,
are retained. TS refutes UV-KEPT at both its limiting ultraviolet value
and every finite-size value, since each finite-size value exceeds log m_0.

### 5. ALPHA, U204–229 — HOLDS, clauses (i)–(iii)

Use OM(a) with its existing repair: its diagonal selection must force
both j and k to infinity (`gap-compact-rigidity-check-astra.md:231–240`).
The nested nonempty compact tail closures give alpha(E). Applying sigma
or its inverse shifts each witnessing time by one, proving equality of
the image and alpha(E). Compactness lifts every scalar subsequential
limit to an orbit subsequential limit; continuity gives the converse.
Thus the scalar cluster set is exactly Lambda(alpha(E)). A singleton
cluster set of a bounded sequence is equivalent to convergence.
(iii) is membership in the already closed Omega, not a new extraction
principle. Its physical lengths are `2^k_i l_1 -> infinity`, even when
the limit object's scale index tends to minus infinity afterward.

The last observation is about the sampling scales. It does not prove that
no ultraviolet-derived invariant could constrain those infrared objects.

### 6. KEPT, U233–252 — HOLDS, clauses (1)–(4)

(1) is the scalar cluster-set identity. For (2), choose any alpha-limit
point; all its shifts stay in that same alpha-limit set. For (3), apply
this to the coordinate at (1,1,1,1) and CE's critical bounds. For (4),
nonempty Omega forbids both a finite value outside the interval and
divergence; empty Omega makes each universal assertion vacuous.
U252 is a necessary condition, not a sufficient one: merely attaining
c somewhere in Omega does not prove ASY on every alpha-limit set.

### 7. REC, U256–284 — HOLDS, clauses (i)–(iv)

“Bounded gaps” must mean syndetic in Z, as the cited OM proof establishes:
some fixed positive length meets the return set in **every** integer
interval. A bounded set has no such property. For each translated
functional `Lambda o sigma^s`, choose shrinking basic neighborhoods of E
and returns tending to the specified end. Their functional values tend
to `Lambda(sigma^s E)`. If the one-ended limit exists, it must equal that
value. This proves (i) and (ii). Apply to every coordinate for (iii).
Without convergence, the same returns put every orbit value in each
one-ended scalar cluster set, proving the inf/liminf and sup/limsup
equalities in (iv). Uniform recurrence is stronger than needed for
(i)–(iii); recurrence toward the selected end suffices.

### 8. REC+, U903–910 — HOLDS

The continuous functional is bounded on compact Omega. Eventual monotony
on either half-orbit gives a finite limit at that end. REC then makes
the whole scalar orbit constant. No monotony before the chosen half-orbit
is needed.

### 9. A1, U316–350 — numbered clauses HOLDS; extension needs correction

(1) HOLDS by KEPT(1). (2) HOLDS by KEPT(2)–(3). The single extraction
of E' converges on all diagonal coordinates, so it supplies the one
sequence plateau for every fixed integer m. (3) HOLDS for the **fixed**
bound D_0 chosen at U316 and c outside its interval (or for divergence).
CR, on its repaired domain, identifies emptiness with the repaired W
(`gap-zd-astra.md:413–418`). Changing D_0 may change whether a finite c
is outside the interval; the divergence version has no such dependence.

**FAILS at U326–327:** a twist ratio is not shown to be a continuous
function of the datum in Omega. LV determines unsigned levels and their
thermal sums and gaps (R394–398). It does not determine their center
signs. For the very same constant trace 3, three even levels give twist
ratio 1; signs (+,+,−), with the vacuum positive, give ratio 1/3.
Both obey the stated nonnegative twisted-sum bound. They also arise as
limits of `diag(1,e^(-qT),e^(-qT))` with these two commuting gradings as
q tends to zero. Assign the same choice to each nontrivial pair twist
to preserve the required axis symmetry. Thus even well-definedness on
unsigned Omega fails, before continuity can be considered.

Correct text: “KEPT applies to each specified continuous functional on
Omega, including s_*(1) and z_*(1). For twist ratios, first enlarge the
compact space to include their limiting coordinates, prove its closedness
and shift invariance, and apply KEPT there.” This is not needed for A1's
numbered claims about D.

### 10. A2, U354–369 — HOLDS, clauses (i)–(ii)

For (i), take a fixed m and eps. Eventually j_i exceeds j_eps,
`L=2^(k_i+m)l_1` exceeds L_eps, and H2 at m+R_eps activates PLATEAU.
Passing to the limit and then eps to zero proves the assertion. (ii) is
A1(2). PLATEAU is only a sufficient condition for UV-KEPT here. Neither
its necessity nor equivalence is proved. U366–369 must not be read as
asserting that necessity, or as proving a statement about a running
coupling from an identity for D alone.

### 11. TWO, U379–406 — HOLDS on its stated conditional domain

(i) HOLDS. The bound at the least side controls each rectangular
coordinate. At every fixed B and dyadic T the same bound at T/2 controls
the spectral tail, so diagonal extraction gives the full trace identity.
S0-Z makes all these lattice sizes legal eventually. (ii)'s liminf and
limsup inequalities HOLD. Its following sentence describes a *subsequential*
continuum ultraviolet behavior. A claimed common ultraviolet limit
requires the liminf and limsup to agree as L tends to zero, or a separate
uniform estimate; these inequalities alone do not give it.

(iii) HOLDS by the repaired UF. A seed at a fixed negative dyadic scale
would propagate to l_1 and contradict the UF subsequence. (iv) HOLDS:
choose the late orbit times first. At each such time only finitely many
coordinates and physical sizes are imposed. Convergence along J', BDD's
limsup bounds, and UF then permit one increasing j_n satisfying all of
them. This proves membership in Omega with j_n,t_n tending to infinity.
Compact tail closures give nonemptiness, closedness and invariance.
Neither S0-Z nor TH-Z is supplied for Wilson by this check.

### 12. EXCL, U408–417 — HOLDS, clauses (i)–(ii)

The proof of REC for the coordinate Lambda_D needs no compactness once
recurrence toward minus infinity and the scalar limit are hypotheses.
For divergence, returns to the unit-coordinate neighborhood of radius
one are impossible sufficiently far toward minus infinity. This proves
exactly the two assertions, with no claim about arbitrary nonconstant D.

### 13. A3, U419–424 — HOLDS AFTER CORRECTION

First unsupported inference: U420–421, “not the same at all sizes”
therefore “not recurrent.” EXCL needs a one-ended limit or divergence.
Nonconstancy alone is not that hypothesis. TWO(ii) also supplies only a
subsequential envelope, and TWO(iv)'s forward-limit conclusion requires
the failed-seed and BDD hypotheses.

Replace the corollary by: “For a continuum datum E_c furnished by TWO,
if D_Ec tends to a finite c at minus infinity and is not identically c
on dyadic scales, or if it tends to infinity there, E_c is not recurrent
toward minus infinity. Under TWO(iv)'s additional hypotheses its forward
limit set lies in Omega. A nonempty bounded Omega cannot retain a
divergent D law. A finite ultraviolet law is retained exactly under
A1(1); this is not ruled out in general.”

This proves the correction, not a blanket impossibility of enriching CE.
The same missing hypothesis affects U528, U855–858, U939 and U1012–1014.

### 14. CR-1, U426–438 — HOLDS

The forward direction is TWO's extraction on G_0, where BDD supplies all
needed coordinate bounds. To define a thermal sum its half-time must
also lie in G_0, exactly as the statement requires. For the converse,
a fixed PHYS-SEED with a strict uniform margin propagates to every
sufficiently large fixed dyadic size. Any continuum subsequence inherits
that strict upper bound and cannot have all thermal sums at least 1/5041.
The same finite-window diagonal choice embeds its forward limit set in
Omega. A nonempty compact invariant subset contains a minimal set, so
it contains a uniformly recurrent element. No full-grid S0-Z is used.

### 15. MON+, U445–458 — HOLDS AFTER CORRECTION of scope

The proof is sound under **TWO(iv)**, which supplies precompactness of
the forward orbit; TWO(i)–(ii) alone do not. State that hypothesis
explicitly. A bounded eventually nonincreasing scalar sequence tends to
its tail infimum. Continuity identifies every omega-limit value with
that number. Invariance then gives the same value on every shifted
limit object, proving the diagonal assertion.

U456 extends the inequality too far: eventual monotony proves
`c_IR<=D_Ec(2^t)` only for t>=t_0 (or b>=b_0). It gives no bound by
earlier ultraviolet values. Correct text: “The inequality holds in the
range of assumed monotony. If monotony holds at every scale, it also
holds against each earlier value and its ultraviolet limit.”
The claim that a monotone is the *only* possible transmission mechanism
is not proved by this proposition.

### 16. Finite-value strength claim, U302–304 and U1053–1056 — FAILS

The first overstatement is U302: “not a weaker statement than the wall”
without the outside-range qualification. U1056 repeats it explicitly
for both cases. For finite c inside the interval, W implies UV-KEPT
vacuously, but the reverse implication can fail.

Use the already supplied A_(m,eps) family, in units u_j, with
`Z_j(n)=1+(m-1)exp(-eps_j |n|/u_j^4)` and eps_j tending to zero.
The TS argument with its second factor omitted proves
`Omega(log m)={log m}`. Every fixed physical size has continuum value
log m, PHYS-SEED fails, and BDD holds. Thus UV-KEPT(log m) is true
and W is false. This uses a prior example, not a new attack.

Correct text: “For c outside the fixed critical interval, or for a
divergent law, UV-KEPT is equivalent to W given BDD. For c inside the
interval it is a necessary condition for W and can be strictly weaker;
one must additionally exclude recurrent critical elements with that
diagonal value.” The source does not prove the finite-c condition for
Wilson, but that does not make the two abstract statements equivalent.

### 17. Product and obstruction comparisons, U502–519 — HOLDS conditionally

For the product with A_(m,eps_j), `eps_j u_j^4 -> 0` keeps its thermal
sum at least m−1 in every fixed physical-size limit. Its D lies between
zero and log m. Thus, **if X has BDD**, the product also has BDD, fails
PHYS-SEED and has nonempty Omega. FV's fixed-n lower bound survives
addition of this nonnegative D. A divergent UV-KEPT assertion then fails
by KEPT. A uniform seed in X makes its contribution vanish along a
common blow-down sequence, as the corrected PT-inf(ii) states.
U508's literal “yes” about an arbitrary product limit having a limit at
minus infinity is not established without such a seed or another
convergence hypothesis; the following example proves only that case.

D2's actual statement (`gap-tiltproof-max.md:240–242`) has a supremum
over tilts in its hypothesis; UV-KEPT does not. No D2 numerical value is
used. SHEET's uniform-coupling-field restriction is likewise a domain
restriction, not a refutation of every periodic-partition-function
argument. NP already supplies finite contracting histories without a
seed (`gap-crux-exercise4-max.md:383–390`); the new note reuses that
device, rather than proving a new universal impossibility theorem.

### 18. Controls and Gaussian remark, U648–669, U790–820 — HOLDS AFTER CORRECTION

The displayed **abelian Gaussian count**, conditional on its specified
compact zero-mode measure and the recalled determinant asymptotic, has
the stated powers. The net determinant power is `-(d-2)/2`; its
`2log n` contribution, the gauge factor `-d log n/2`, and the holonomy
factor `d(d/2-1)log n` sum to `(d-1)(d-4)log n/2`.
The uncancelled beta power is `(d-1)/2`. This checks the algebra, not
the determinant asymptotic, its uniform error, the compact Villain
identification, or the SU(2) extrapolation. Those are not proved here.

Corrections needed for the six control rows:

1. **U(1), one coupling (U792):** keep the limit-existence and boundedness
   hypotheses. The Gaussian formula removes a leading log n term in four
   dimensions; its O(1) remainder does not prove exact independence of n
   (U665). It also does not identify a finite lattice value with c_inf.
2. **U(1), beta_j tending to infinity (U793):** branch II and empty Omega
   follow *if* the indicated lower asymptotic is uniform at the physical
   sizes and along candidate blow-down sequences, respectively. Fixed-n
   divergence alone proves neither. Keep this a conditional GUIDE claim.
3. **Frozen Q_8 and 2T (U794):** FRZ is the beta-to-infinity limit at fixed
   lattice torus. A finite-beta infinite-size plateau is a different
   claim and remains the named Peierls belief. “Literally kept” is valid
   for the ideal frozen constant, not proved at finite beta.
4. **Product (U795):** retain X's BDD premise from U506. Without it the
   cited existence theorem does not supply nonempty Omega.
5. **TS (U796):** HOLDS, as item 4 proves.
6. **Five dimensions, fixed beta (U797):** its ultraviolet column uses a
   beta-to-infinity bound while the row fixes beta. Replace that column
   by “fixed-n beta-to-infinity divergence is argued separately.” The
   claimed infrared growth requires a large-n estimate at fixed beta.
   Abelian Gaussian arithmetic does not by itself justify its coefficient
   or the bounded remainder for nonabelian SU(2).

The fair GUIDE correction is therefore: “The displayed Gaussian model
suggests failure of BDD for these varying-beta/five-dimensional regimes.
If matching uniform asymptotics hold in the named interacting models,
they lie in branch II.” This does not prove their branch membership.
R294 already has the boundedness proviso for varying-beta U(1); R270 and
R300 infer nonempty Omega from massless gluons without that proviso.
The latter inference needs correction independently of the new heuristic.
`gap-phys-seed.md:336` discusses U(1) at one coupling. That U(1) sentence
is not contradicted by a varying-beta family. Its blanket statement
including five dimensions is the part the proposed GUIDE change addresses.

### 19. Logical tool, summaries and route screening — mixed verdicts

U781–786 HOLDS: under UV-KEPT, REC restricts every recurrent candidate
to the stated diagonal value, and LIOU asks that no such candidate exist.
This is an implication, not proof of its premise for Wilson.

U288–295 (C1–C3) HOLD with the explicitly named compactness and BDD
premises and the distinction between fixed-n and physical-volume UV
laws. U296–299 (C4) requires correction: ALPHA identifies where the
limit is sampled; it does not classify all possible ways ultraviolet
facts could imply an infrared constraint. C5 holds by TS; C6 is
corrected in item 16.

U921 and U951/U1036–1038 do not prove that a useful functional **must
not be additive**. A product test requires selectivity against the
product. An additive functional can change its ultraviolet value when
a factor is added; sharing D's leading divergence does not show equality
of every other functional. Correct text: “A proposed functional must
supply a proved separation from the comparison product.” No such
functional is constructed here, but none is ruled out merely by
additivity. Likewise U1042–1049's blanket “do not pursue” restrictions
are not consequences of ALPHA for every possible ultraviolet input.
These are proposed route choices, not proved exclusions.

The application “with the SU(2) free value” at U1008–1010 and U1053
must say **fixed-lattice divergent law**, or explicitly assume a matching
physical-volume ultraviolet law. FV does not supply the latter. The
formal assertion A1(3) for the divergent law remains valid regardless.
Descriptions of “no massless particle” at U121 and U990 are motivation,
not a theorem identifying W with an infinite-volume physical spectrum.

### 20. Source and coverage record

The source U1–1165 was read line by line in bounded ranges. All named
lemmas and every numbered clause are addressed above. Planning/history
paragraphs U1–74, U138–199, U759–775, U860–897, U953–984 and
U1159–1163 were read as provenance. Historical run claims were not
verified; their scratch files are outside this run's allowed scratch
directory and are not proof inputs. U1095–1115 and the RESULT inherit
the corrections above. U1074–1089 assigns work to the lead; no such
edit is performed. This is not a new attack on W, BDD or LIOU.

The relevant prior sources were checked at the exact ranges used:
R133–262, R278–304, R350–380, R390–398; the existing R check's items
11, 14, 19, 20 and the Opus R check at 129–141; the settings and repaired
definitions in `gap-dichotomy.md:75–188`; and the repaired W at
`gap-zd-astra.md:403–420`. The frozen formula was already in the
earlier Codex check at `gap-crux-skeleton-check-astra.md:305`.

For the published-text comparison I used the SA-index introduction,
chunk 01's theorem row and neighbors, chunk 06's first-passage/dilation
and theorem rows, chunk 20's RF35 row and neighbors, and the matching
obligations entries. The source reads were SA66–73, 101–130,
6844–6869, 6937–6960 and 21518–21534. These show that the stated
short-distance normalization concerns **correlations**, and the exact
dilation changes units. Neither displayed assertion supplies a UV-KEPT
law for D. The first-passage definition is a definition; the dilation
identity has its displayed direct proof; the ultraviolet correlation
clause remains part of the outline's conditional program.

CA-I4209–4240 was located through `ca-full/index.tsv` and its neighboring
rows. It explicitly cites Balaban's ultraviolet-stability theorem with
small effective couplings through K. I use that passage only to check
the scope of U198 and its source attribution, not as a proved BDD or
UV-KEPT input. No item 4.12–4.19 argument is used, so no passage in
that specialized index was needed. Searches of the outline chunks,
obligations and CA statement index for the present alpha-limit,
recurrence, critical-element and frozen-value labels returned no match.
This is a bounded locator result, not a claim that the books contain no
related argument anywhere. No Balaban page or additional paper is imported.

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, receive credit for these definitions and source statements.
Claude Fable 5.2 receives credit for U and the earlier engine R; the
earlier Codex and Claude checks receive the specific prior credit above.

**Pre-comparison verdicts complete.** The detailed row 1030 report has
not yet been opened. The following section will compare it with the
verdicts already written here.

## Comparison with the Claude check

I then read `gap-uv-rigidity-check-opus.md:1–520` in full. Below `O`
denotes that report. My pre-comparison file was saved separately with
SHA-256 `93f47c79770f84009f5fba692fef4a723898e3881b3b3e44a9e09cd6f8613c6f`.
That snapshot records the verdicts before this reading; it does not
remove the previously disclosed exposure to the FINISH summary.

We agree on FV, its normalization and constants, FRZ, CONST, ALPHA,
KEPT, REC, REC+, A1's numbered assertions, A2, TWO's numbered conditional
assertions, EXCL, CR-1 and the TS limit. We also agree on the missing
limit hypothesis in A3, the unproved multiplicity of candidates at a
fixed finite c, and the two citation repairs for the GUIDE correction.
The same zero-mode/cohomology method appears in both reports; provider
diversity is not a second independent mathematical method there. My
separate rational margins replace the decimal estimates, and the TS
plateau bound was checked by differentiation.

These are all substantive disagreements and corrections to my initial
verdicts found in the comparison:

| Issue | Claude's line | Resolution, with source line |
|---|---|---|
| Finite c is said not to be weaker than W | O333 correctly calls the inside-range case a plateau rather than W, but O449/O472 and O510–514 accept the route summary without this defect. | **This check is right about U302 and U1056.** The one-factor A_(m,eps) example in item 16 has UV-KEPT true and W false. Keep the outside-range equivalence; correct the inside-range claim. |
| Twist-ratio continuity on unsigned Omega | No separate verdict at U326–327; O449 reports no failing line for the full check. | **This check is right.** LV determines levels, not their signs. The trace-3 example in item 9 disproves determination by unsigned data. This is an additional missed defect, not disagreement with O's correct A1(1)–(3) proof. |
| A3's hypothesis and blanket conclusion | O355–361 adds the limit, then says it is already present because link (a) posits an ultraviolet value, and leaves the “cannot be strengthened” conclusion unchanged. | **Claude is right that a limit must be added; this check is right that more qualification is needed.** U319's fixed-size value does not assert a limit of D_Ec at minus infinity. U320's limsup limit is not a two-sided squeeze for E_c. The corrected conditional in item 13 is justified; the blanket finite-c prohibition is not. |
| MON+ and its ultraviolet inequality | O373–378 accepts MON+, and calls its following necessity language a reading. | **Both proofs of the conditional limit statement are right; this check is right about U456.** Monotony only for t>=t_0 bounds only that tail. Neither a “reading” label nor TWO(iv) extends the inequality to ultraviolet times. Explicitly import TWO(iv), and require all-scale monotony for the all-scale inequality. |
| Physical UV and GUIDE control scope | O334–336 applies FV as the SU(2) ultraviolet case; O402–420 endorses the GUIDE branch changes. O410–411 says D does not depend on n. | **The conditional Gaussian power count and Claude's citation repairs are right. This check's narrower scope is required.** FV is fixed-n only; the two limits in U319–323 remain distinct. An O(1) remainder permits n dependence. U797's fixed-beta row cannot use beta-to-infinity divergence as its ultraviolet value. Uniform interacting-model asymptotics remain unproved. These points do not refute the proposed GUIDE conjecture. |
| Additivity and general route exclusions | O436 leaves U1–U5 as unchecked readings; O513 nevertheless says source W2 items (1), (3), (4) can go in unchanged, including its registry entry. | **This check is right to withhold that blanket endorsement.** U951's necessary nonadditivity condition is not proved: an added factor can change an additive functional's ultraviolet value. U1042–1049's universal exclusions also exceed ALPHA. Keep the exact sampled-scale and product counterexample statements. |
| TS's starting scale; convergence versus monotony | O235–236 rounds rho l_1 up to P. O229 says the continuum expression is increasing in j. | **Claude is right about the scale, correcting my initial item 4:** U477 must use `L_0=2^ceil(log_2 rho) l_1`, since rho need not be dyadic. The same D_0 works. Final TS verdict: HOLDS AFTER CORRECTION of this bound's domain. **This check is right about O229:** eps_j merely tends to zero and need not decrease; replace “increasing” by “converging.” No TS conclusion changes. |
| Change of unit | O431–433 and O495 restrict U682 to dyadic changes. | **Claude is right; this was missing from my initial verdicts.** For a power-of-two unit change reindex k and discard finitely many terms. A general reference-change ratio changes the grid, so identity of these Omega spaces is not proved. Final verdict for U682's unrestricted sentence: HOLDS AFTER CORRECTION to dyadic unit changes. |

For the twist issue one can even keep the center representation fixed.
Take the unsigned trace `1+2t+s`, with `t=exp(-eps_j |n|/u_j^4)` and
`s=exp(-|n|/u_j^4)`, and a fixed flip `C=diag(1,1,-1,1)`.
Use transfer eigenvalues `(1,t,t,s)` on one subsequence and `(1,t,s,t)`
on another. The unsigned data are identical. Both signed traces are
positive: respectively `1+s` and `1+2t-s`. Along the same kind of
admissible scale separation as TS, t tends to one and s to zero.
The unsigned limit is log 3 in both cases, while the twist ratios tend
to 1/3 and 1. Assign all three commuting flips equal to C; the pair
twist functions are symmetric. Thus the defect is not cured by fixing
the underlying grading space. The missing object is the signed limit
coordinate in the topology, not another use of LV.

For the fixed-c family issue, O187–194 and O474–480 correctly retract
the claimed construction of multiple candidates. My item 3 adds that
even a photon candidate needs its *same diagonal value* matched to c;
existence of some photon limit alone is not that matching. This is a
sharpening of the agreed repair, not a contrary verdict on CONST.
O139's `beta=4/g²` is a conventional alternative coupling normalization;
the account at SA6854 uses `beta=g_0^(-2)`. A fixed normalization factor
only adds a constant to the logarithm and leaves FV's coefficient intact.
O260–267's additional sketch is outside the checked source U and is
not used to discharge anything in this report.

I therefore disagree with O449, O472 and its RESULT's global “first
failing line none.” The earliest explicit logical overclaim identified
here is U302, repeated at U1056; U326–327 is a separate failed extension.
The main named proofs do not require either sentence. The two useful
repairs newly accepted from Claude are the dyadic starting scale for
TS and the restriction on changing units. The source remains unedited.

## Final disposition

All requested numbered clauses have verdicts above. FV, CONST, FRZ,
REC/REC+, ALPHA/KEPT, A1/A2, TWO, EXCL and CR-1 hold on their stated
conditional domains. TS's construction and limit hold after rounding
its starting scale to P. A3, MON+'s scope, the physical interpretation,
the finite-c candidate remark and the GUIDE comparisons need the written
corrections. The finite-c strength claim and twist-continuity extension
fail as stated. These defects require changes to the research summary;
agreement on the core lemmas does not validate the broader route ban.

No mathematical computation, numerical test, symbolic solver, enumeration
or formal checker was run. Downloads, source searches, hashes and file
operations were only bookkeeping. The external-paper proofs, the author's
guard run, the full CE/CR dependency closure, Wilson's physical-volume UV
law, the interacting control-model asymptotics, and the new sketch in O
were not independently verified. No status file, source proof, registry,
FINISH row, audit record or remote post was changed. The only repository
output is this file, on local branch `codex/gap-uv-rigidity-check-astra`.
It is uncommitted and unpushed. The checked source's Git blob remains
`64761d824d369c5a9f2dca878f35da62044db6a9`, identical to the pinned commit.

RESULT: Research check of row 1028: core lemmas HOLD; TS, A3 and MON+ require the stated domain/scope corrections; U302/U1056's finite-c strength claim and U326–327's twist-continuity extension FAIL. Claude comparison and accepted corrections are recorded. No mass gap or status is claimed; (LIOU), (BDD-Delta) and (W) remain open.
