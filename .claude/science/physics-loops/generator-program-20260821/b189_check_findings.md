# Block 189 adversarial check — derived gauge quotient on the site-OS physical space

Audit method: independent exact-SymPy rebuild from the construction in the task. Scientific reads were restricted to `scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py`; only its permitted `cover_embedding`, `cover_index`, and `block105.shear_hodge` APIs were used. No supervisor scratch file was read. Every equality and sign decision below is exact; no floating-point value enters a decision.

## C1 — grading and global spatial shifts

**Verdict: CONFIRMED.** With $U_x:e_{t,x}\mapsto e_{t,x+1}$, the exact commutator $[U_x,d_K]$ has 64 nonzero entries, rank 16, and time-pair support

\[
\{(0,0),(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7)\}.
\]

Thus its support is entirely intra-slice. With $V_{\mathrm{glob}}:x\mapsto x+2$ on every slice, $[V_{\mathrm{glob}},Q]=0$ exactly (0 nonzero entries). The odd shift fails: $[U_x,Q]$ has 64 nonzero entries and exact rank 8.

The independent control also closes: $\operatorname{rank}Q=32$; the $8\times8$ core Gram is symmetric; and its eight leading principal minors are respectively

1. `250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479`
2. `9699265179160355495171233606378759680576921193642386633764164130236400111062250000/65542091681979044701359795584266761562795513633598145522262137753727157320281821073`
3. `353644672418414022914464425566377270915654077424463797672617912778254783017125000000/6838224898819813663841872005958498789718331922438739849489349705638866747082736665283`
4. `731532015717321164785349369079666981568307603751142634551353335912643729687500000000/37550252514571959241798349787105440722488384065321501278774850137981847225208711863747`
5. `106686008017084203077801056058148690365327519581372351912870977930134460301989218750000000000000/36656348246255818726406955224816021523556522632232798498998085956974608046400338916272318652442131`
6. `841735761720241585216954497623165448466402887037992491960332330772351840056394749953125000000000000000000/1883353887222747383088069687328317898320467000822076903017257403075849372483368962731187619993061966804280177`
7. `33947577405628588759402644155672737009285916836360219602324377757327093398437500000000000000000000000/1253063131884728797796453551116645308263783766348687227556392151081736109436705896694070272783141694480559`
8. `838707309443042031875048052416041488487432656958511417047078368969433593750000000000000000000000000000/392208760279920113710289961499509981486564318867139102225150743288583402253688945665243995381123350372414967`.

Every numerator and denominator is positive, so Sylvester's criterion verifies positive definiteness without eigenvalues or floating point.

## C2 — single-slice twist table

**Verdict: CONFIRMED-WITH-CORRECTION.** None of the eight $V_t$ is an exact symmetry. Each exact defect $V_tQV_t^T-Q$ has rank 4. The complete nonzero-entry and time-pair table is:

| $t$ | nnz | exact ordered time-pair support |
|---:|---:|---|
| 0 | 96 | `{(0,1),(0,2),(0,6),(0,7),(1,0),(2,0),(6,0),(7,0)}` |
| 1 | 64 | `{(0,1),(1,0),(1,2),(2,1)}` |
| 2 | 80 | `{(0,2),(1,2),(2,0),(2,1),(2,3),(3,2)}` |
| 3 | 64 | `{(2,3),(3,2),(3,4),(4,3)}` |
| 4 | 64 | `{(3,4),(4,3),(4,5),(5,4)}` |
| 5 | 64 | `{(4,5),(5,4),(5,6),(6,5)}` |
| 6 | 80 | `{(0,6),(5,6),(6,0),(6,5),(6,7),(7,6)}` |
| 7 | 64 | `{(0,7),(6,7),(7,0),(7,6)}` |

This confirms every numerical count and support claimed. The correction is terminological: if “temporal bond” means an elementary nearest-slice bond, the phrase is too narrow. The supports for $t=0,2,6$ contain separation-two pairs such as $(0,2)$ and $(0,6)$. What is exactly true is that every supported ordered pair contains the twisted slice $t$, and the action's Hodge multiplication extends the support to temporal range two.

## C3 — OS-compatible subgroup and covariance transport

**Verdict: CONFIRMED.** The base action obeys

\[
P_sQP_s=Q^T
\]

exactly. For every $t\in\mathbb Z_8$, $V_tV_{-t}$ commutes exactly with $P_s$; the tests for all eight labels return zero commutator (the duplicated labels give the same reflected pairs). The fixed-slice singles $V_0$ and $V_4$ also commute exactly with $P_s$.

The structural statement follows algebraically. For real orthogonal $V$ with $VP_s=P_sV$,

\[
\begin{aligned}
P_s(VQV^T)P_s
 &=V(P_sQP_s)V^T\\
 &=VQ^TV^T\\
 &=(VQV^T)^T.
\end{aligned}
\]

As a nontrivial instance, $V=V_1V_7$ commutes with $P_s$, its twist differs from $Q$ in 128 entries, yet $P_s(VQV^T)P_s=(VQV^T)^T$ holds exactly. Thus OS covariance is transported even when exact action invariance is absent.

## C4 — core action

**Verdict: CONFIRMED.** In the $t$-major core order

\[
((1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)),
\]

$W_1^2=W_2^2=I_8$ and $W_1W_2=W_2W_1$ exactly. The simultaneous shift satisfies

\[
(W_1W_2)^TK(W_1W_2)-K=0_{8\times8}.
\]

Neither generator is individually invariant. Both $W_1^TKW_1-K$ and $W_2^TKW_2-K$ have exactly 32 nonzero entries and exact rank 4. The combined defect has 0 nonzero entries.

## C5 — invariant quotient

**Verdict: CONFIRMED.** The exact projector

\[
\Pi=\frac{(I+W_1)(I+W_2)}4
\]

has rank 4. SymPy's default `columnspace()` order gives the basis $B=(b_1,b_2,b_3,b_4)$, in the C4 core order, with

\[
\begin{aligned}
b_1&=(1/2,0,1/2,0,0,0,0,0)^T,\\
b_2&=(0,1/2,0,1/2,0,0,0,0)^T,\\
b_3&=(0,0,0,0,1/2,0,1/2,0)^T,\\
b_4&=(0,0,0,0,0,1/2,0,1/2)^T.
\end{aligned}
\]

Here $B^TB=I_4/2$, so $\det(B^TB)=1/16$. The quotient Gram $K_{\rm inv}=B^TKB$ is exactly

\[
\begin{pmatrix}
\frac{21963305608532250}{98338455418123687}&-\frac{1668901104000}{24167720672923}&-\frac{6968252744640000}{98338455418123687}&\frac{943847791250}{24167720672923}\\
-\frac{1668901104000}{24167720672923}&\frac{21963305608532250}{98338455418123687}&\frac{943847791250}{24167720672923}&-\frac{6968252744640000}{98338455418123687}\\
-\frac{6968252744640000}{98338455418123687}&\frac{943847791250}{24167720672923}&\frac{15357851117106250}{98338455418123687}&0\\
\frac{943847791250}{24167720672923}&-\frac{6968252744640000}{98338455418123687}&0&\frac{15357851117106250}{98338455418123687}
\end{pmatrix}.
\]

The first minor therefore matches the supervisor's value exactly. All four leading minors are

1. `21963305608532250/98338455418123687`
2. `436272390996572018995584314062500/9670451814022299931794587630473969`
3. `988031356039629755460576499986328125000000/165618270654292302550203905627153987721012841`
4. `2198952681327212186709224903107443847656250000000000/2836414688995746959145683979271775764957689091340617249`.

They are exactly positive, so the restriction is symmetric positive definite by congruence/Sylvester, with no eigenvalue approximation. In this basis,

\[
\det K_{\rm inv}
=\frac{2198952681327212186709224903107443847656250000000000}
{2836414688995746959145683979271775764957689091340617249}.
\]

The basis-independent determinant density is

\[
\frac{\det(B^TKB)}{\det(B^TB)}
=\frac{35183242901235394987347598449719101562500000000000000}
{2836414688995746959145683979271775764957689091340617249}.
\]

## C6 — reading-fence attack

**Verdict: CONFIRMED-WITH-CORRECTION.**

1. **Automatic positivity:** yes. The supplied supervisor claim explicitly concedes this. Once $K\succ0$ and $B$ has full column rank, $y^TB^TKBy=(By)^TK(By)>0$ for every nonzero $y$. Thus positivity of the four-dimensional restriction is not a new dynamical or gravity theorem.
2. **Nonautomatic derived content:**
   - The selected even-shift family is executable: eight commuting slice involutions generate 256 explicitly testable site permutations. This measures a chosen finite transformation family; calling it *gauge* is a physical interpretation, not an algebraic output.
   - The grading distinction is measured in this model: the odd-shift/differential commutator has 64 entries, rank 16, and only intra-slice support; the global even shift commutes with $Q$, while the odd shift has a 64-entry, rank-8 $Q$-commutator. “Forced” is therefore valid only relative to the stipulated parity grading and constructed action, not as a general law.
   - The $W_1W_2$ invariance theorem is a genuine exact identity for the displayed core; the two individual failures are independently measured.
   - The four-dimensional invariant sector is genuinely explicit: projector rank 4, an exact basis, and an exact restricted Gram are all computed rather than assumed.
3. **Gravity-specific content:** none is derived. The construction has a finite site action, an OS reflection, a positive core form, chosen site shifts, and a uniform block-volume parameter. It supplies no gravitational lapse function, shift vector, Hamiltonian constraint, momentum/diffeomorphism constraint, first-class constraint algebra, Dirac closure, ADM phase space/history transporter, or proof that the selected transformations are redundancies of physical states. Consequently “gauge quotient,” “physical space,” “Hamiltonian-constraint direction,” and “gravity constraint quotient” remain readings/candidate labels.

The comparative phrase “the corpus's first” is not verifiable under the mandated one-script read fence and receives no audit confirmation. The defensible claim is narrower: this is an executable finite algebraic candidate for such a reading, not an executable derivation of a gravity constraint quotient.

## C7 — exact-symmetry stabilizer in the 256-element group

**Verdict: CONFIRMED.** I swept all $2^8=256$ patterns exactly. Writing a pattern as $\xi_0\xi_1\cdots\xi_7$, with `1` meaning the $+2$ shift is applied on that slice, the complete stabilizer is

\[
\operatorname{Stab}(Q)=\{00000000,\;11111111\}\cong\mathbb Z_2.
\]

Its order is exactly 2, generated by the uniform global even shift. All 32 reflection-even patterns $\xi_t=\xi_{-t}$ were included in the sweep, and only the two uniform patterns stabilize $Q$. No adjacent two-slice pattern is an exact symmetry. Thus OS compatibility of a twist is much weaker than membership in the exact stabilizer.

## C8 — volume/lapse probe at $v=4/5$

**Verdict: CONFIRMED-WITH-CORRECTION.** Replacing both positive-half blocks and their unflipped $P_4$-images by `shear_hodge(5/13,4/5)` leaves $Q_{4/5}$ invertible with exact rank 32. OS covariance survives exactly:

\[
P_sQ_{4/5}P_s=Q_{4/5}^T.
\]

The new core Gram is symmetric and its eight exact leading minors are

1. `24715720213831754178702311739545467697276090227783924526046520521190218548500000/57111230204920766372338894470060259410335864240898818757195087147309010366920717`
2. `9036305880642581802819738259389379890190939973860603816468448799789079784361533977564375688888954800000000/46351151204959960247936294548352633483077975537207906663230442911237757508318906212287753531286751307009963`
3. `866511588306607751500755555047659615318506845924876468765075752485051165163723102224449392711160000000000000/10923421300635563965096986748561770624178709568268663336967974379415031519460488897362480582206577724685347947`
4. `88693962002087062259754501059571634303385858842239944744910009491609207214214264757790954700000000000000000000/2574286286516447907774523210411057277098115888255314993078785962082142428086188550145091257206683483784180332843`
5. `4289389116840762067393428071593631781684223520842063794528323600642694853573183418645650000000000000000000000000/780008744814483716055680532754550354960729114141360442902872146510889155710115130693962650933625095586606640851429`
6. `10407781389856141714624956959415856270343858132540361991792374538198713168877417790575000000000000000000000000000000/11580789834260639732278688869806809120101945157656778495778942759247171294828079345413263478411531794174348796721166363`
7. `1391677535220177998591495862580405348009987102543650913397163957824727645937500000000000000000000000000000000000/24278385396772829627418634947184086205664455257142093282555435553977298312008552086820258864594406277095070852664919`
8. `4236019225502007147029090945324275896806052921963099191657129333961597656250000000000000000000000000000000000000000/909735379202474698969003670105934894212452802940371377390634725643083345049272455245241919915216997609029399920207179849`.

All are positive, so the $v=4/5$ core remains positive definite exactly. The combined core shift also remains an exact invariance:

\[
(W_1W_2)^TK_{4/5}(W_1W_2)=K_{4/5},
\]

with 0 defect entries. The correction is interpretive: this is clean first data for a **uniform Hodge-volume direction**. Calling that dial a gravitational lapse or Hamiltonian-constraint direction requires an absent bridge theorem; the one-point calculation does not supply it.

## Overall verdict

**CONFIRMED-WITH-CORRECTION.** Every exact algebraic/numerical claim in C1–C5 and both fresh computations C7–C8 survives the independent rebuild. C2 needs a range-two-support wording correction. C6 is the substantive boundary: the finite invariant-sector construction is executable, but its identification as a gravity gauge quotient is not derived. C8 likewise probes a uniform Hodge-volume dial, not a demonstrated gravitational lapse. No repo file was modified.

## Five-line stdout

```text
B189 OVERALL: CONFIRMED-WITH-CORRECTION
CONTROL/C1: Q rank=32; core PD=True; even/odd shift result exact
C2-C3: all defect counts/supports match; OS transport identity exact
C4-C7: W12=True; quotient rank/PD=4/True; stabilizer order=2
C8: v=4/5 covariance/core-PD/W12=True/True/True
```

## Ten-line summary

1. The independent rational rebuild gives `rank(Q)=32`, a symmetric core Gram, and eight positive exact Sylvester minors.
2. C1 is confirmed: the grading defect is intra-slice; the global even shift is exact; the odd shift is not.
3. C2's eight nnz counts and ordered supports match exactly; “bond” should be replaced by temporal-range-two coupling.
4. C3 is confirmed algebraically and computationally: all reflection-even shifts preserve the OS covariance relation.
5. C4 is confirmed: `W1` and `W2` commute and square to one; only their product preserves the core Gram.
6. C5 is confirmed: the invariant projector has rank 4 and the stated first quotient minor matches exactly.
7. C6 confirms that restriction positivity is automatic; the measured novelty is finite symmetry algebra, not gravity dynamics.
8. C7 gives the full stabilizer `{00000000,11111111}`, the diagonal global `Z2`, of exact order 2.
9. C8 confirms covariance, core positivity, and combined-shift invariance at `v=4/5`, but only for a volume dial.
10. Overall: all exact mathematics survives; the gravity/gauge/lapse language remains an explicitly unproved reading.
