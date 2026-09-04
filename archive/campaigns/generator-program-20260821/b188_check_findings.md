# Block 188 adversarial check — thick-seam wall and site-adapted OS positivity

## Scope and exact-method guard

I rebuilt the $32\times32$ objects from the stated $\mathbb Z_8\times\mathbb Z_4$ rules.  The only repository source inspected was `scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py` (the b187 mirror); I used only its `cover_index`, `cover_embedding`, and exposed `block105.shear_hodge` API.  All decisions below use SymPy integers, rationals, exact radicals, exact ranks/determinants, and exact symmetric-congruence elimination.  No floating-point value is used in a verdict.

## A1 — reflection split

**Verdict: CONFIRMED.**  For $\theta(t)=-1-t\pmod 8$, direct reconstruction gives

\[
PQP-Q^T=0_{32},\qquad \operatorname{nnz}(PQP-Q^T)=0.
\]

Equivalently, after ordering the negative half by $\theta$, the negative-negative block is exactly the transpose of the positive-positive block.

## A2 — LINK seam operator

**Verdict: CONFIRMED.**  The exact paired seam matrix $C_{a b}=Q_{a,\theta b}$ is symmetric, has rank $16$, inertia

\[
\operatorname{In}(C)=(8,8,0),
\]

and time-pair support exactly

\[
\{(0,0),(0,1),(1,0),(2,3),(3,2),(3,3)\}.
\]

For spatial Fourier label $p=0,1,2,3$, the near block in order $(0,1)$ is

\[
\begin{pmatrix}
-601/576 & (65/1152)(-i)^p\\
(65/1152)i^p&0
\end{pmatrix},
\]

while the far block in order $(3,2)$ has the same form with $w_p=i^p$.  Thus 

\[
|w_p|=1,\qquad \det B_p=-\left(\frac{65}{1152}\right)^2=-\frac{4225}{1327104}<0
\]

for every block in every sector.  There are eight indefinite $2\times2$ blocks in total.

## A3 — three proposed repairs

**Verdict: CONFIRMED-WITH-CORRECTION.**  The stated sign fingerprint is correct, but it is a sequence of **leading-principal-minor signs**, not the inertia.  In every sector $p=0,1,2,3$, the raw Hermitian $4\times4$ Gram has leading-minor signs

\[
(+,+,-,+)
\]

and true inertia $(2,2,0)$.  With $a=-601/576$, $b=65/1152$,

\[
\delta=\sqrt{a^2+4b^2}=\frac{\sqrt{365426}}{576},\qquad
S=\frac{2C-aI}{\delta},
\]

the congruence $SKS$ again has leading-minor signs $(+,+,-,+)$ and inertia $(2,2,0)$.  Moreover

\[
\operatorname{rank}(SK-KS)=4
\]

in every sector, so neither $SK$ nor $KS$ is Hermitian (and in the real sectors neither is symmetric).

The seam modulus is exactly

\[
|C|=SC=\frac{aC+2b^2I}{\delta},\qquad C^2=aC+b^2I.
\]

It is symmetric positive definite, has rank $16$, and

\[
\det |C|=b^{16}=\left(\frac{65}{1152}\right)^{16}>0.
\]

Replacing both paired action cross blocks by $|C|$ preserves reflection covariance.  Its exact sector action determinants are

\[
\det Q^{\rm pol}_{p=0,2}=
\frac{4384437304032745240319804044070026581721}
{71911150569763408538286482364825600000000},
\]

\[
\det Q^{\rm pol}_{p=1,3}=
\frac{591876159383851368080611208940582281086889}
{647200355127870676844578341283430400000000},
\]

so the polar action is nonsingular.  Nevertheless its real-sector Gram still has leading-minor signs $(+,+,-,+)$ and true inertia $(2,2,0)$ for both $p=0,2$.  The modulus repair therefore fails.

## A4 — site reflection applied to the LINK glue

**Verdict: CONFIRMED.**  For $\theta_s(t)=-t\pmod8$,

\[
\operatorname{nnz}(P_s QP_s-Q^T)=240.
\]

The LINK-glued action is not site-reflection covariant.

## B1 — site-adapted Hodge image

**Verdict: CONFIRMED.**  With the unflipped image block,

\[
P_sHP_s-H=0_{32},\qquad \operatorname{nnz}(P_sHP_s-H)=0.
\]

Replacing its shear by $-c$ gives exactly

\[
\operatorname{nnz}(P_sH_{\rm flip}P_s-H_{\rm flip})=64.
\]

Thus the site reflection requires the unflipped image.

## B2 — site-odd differential

**Verdict: CONFIRMED.**  Exact entrywise tests give

\[
P_sD_sP_s=-D_s.
\]

Also $D_s=d_K$ on the full $\{1,2,3\}\times\{1,2,3\}$ restriction and on the unordered bond pairs $\{0,1\}$ and $\{3,4\}$: both restricted differences have zero nonzeros.  Globally,

\[
\operatorname{nnz}(D_s-d_K)=24,
\]

with time-pair support exactly

\[
\{(0,0),(4,4),(5,4),(5,5),(6,6),(7,7)\}.
\]

## B3 — site reflection covariance

**Verdict: CONFIRMED.**  Directly,

\[
P_sQ_sP_s-Q_s^T=0_{32}.
\]

The action is not itself symmetric: $\operatorname{nnz}(Q_s-Q_s^T)=144$.  The claimed property is the exact reflected-transpose covariance, not ordinary Hermiticity.

## B4 — empty site cross-half block

**Verdict: CONFIRMED.**  The full $12\times12$ block, without first imposing the $\theta_s$-paired ordering, obeys

\[
Q_s[\{1,2,3\}\times\mathbb Z_4,\{5,6,7\}\times\mathbb Z_4]=0.
\]

This is exact support emptiness, not cancellation: the three corresponding restrictions of $mH$, $HD_s$, and $-D_s^TH$ separately have nonzero counts $(0,0,0)$.  Consequently the paired $C_s$ is identically zero.

## B5 — site OS Gram positivity

**Verdict: CONFIRMED.**  The $8\times8$ $\{1,2\}$ core Gram is symmetric and has the following eight exact leading principal minors (all numerators and denominators are positive):

\[
\begin{aligned}
\Delta_1={}&\frac{250811603701251182926764176363850176714557920003089965221914456500}{666495028860293624372300921944800123265476111209829299156533225479},\\
\Delta_2={}&\frac{9699265179160355495171233606378759680576921193642386633764164130236400111062250000}{65542091681979044701359795584266761562795513633598145522262137753727157320281821073},\\
\Delta_3={}&\frac{353644672418414022914464425566377270915654077424463797672617912778254783017125000000}{6838224898819813663841872005958498789718331922438739849489349705638866747082736665283},\\
\Delta_4={}&\frac{731532015717321164785349369079666981568307603751142634551353335912643729687500000000}{37550252514571959241798349787105440722488384065321501278774850137981847225208711863747},\\
\Delta_5={}&\frac{106686008017084203077801056058148690365327519581372351912870977930134460301989218750000000000000}{36656348246255818726406955224816021523556522632232798498998085956974608046400338916272318652442131},\\
\Delta_6={}&\frac{841735761720241585216954497623165448466402887037992491960332330772351840056394749953125000000000000000000}{1883353887222747383088069687328317898320467000822076903017257403075849372483368962731187619993061966804280177},\\
\Delta_7={}&\frac{33947577405628588759402644155672737009285916836360219602324377757327093398437500000000000000000000000}{1253063131884728797796453551116645308263783766348687227556392151081736109436705896694070272783141694480559},\\
\Delta_8={}&\frac{838707309443042031875048052416041488487432656958511417047078368969433593750000000000000000000000000000}{392208760279920113710289961499509981486564318867139102225150743288583402253688945665243995381123350372414967}.
\end{aligned}
\]

Hence the core inertia is $(8,0,0)$.  I independently certified both singular extensions by exact congruence, rather than by treating zero leading minors as sufficient.  After permuting the same $\{1,2\}$ core first, each extended Gram has block form

\[
M=\begin{pmatrix}K_c&B\\B^T&D\end{pmatrix},\qquad
\begin{pmatrix}I&0\\-B^TK_c^{-1}&I\end{pmatrix}
M
\begin{pmatrix}I&-K_c^{-1}B\\0&I\end{pmatrix}
=\operatorname{diag}(K_c,D-B^TK_c^{-1}B).
\]

The Schur complement is identically zero entrywise in both cases: it is $0_4$ for slices $\{1,2,3\}$ and $0_8$ for slices $\{0,1,2,3\}$.  Therefore the true inertias are

\[
\operatorname{In}K_{\{1,2,3\}}=(8,0,4),\qquad
\operatorname{In}K_{\{0,1,2,3\}}=(8,0,8).
\]

Both are PSD of rank $8$, exactly as claimed.

## B6 — reconstructed one-step transfer

**Verdict: REFUTED.**  Use the time-major core basis

\[
((1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)).
\]

Let $K_c$ be its Gram, let $L_{ab}=\langle e_a,Ue_b\rangle_K$ with $Ue_b$ on slices $\{2,3\}$, and define the induced quotient operator by the nondegenerate pairing equation

\[
K_cT_{\rm recon}=L,\qquad T_{\rm recon}=K_c^{-1}L.
\]

The pairing matrix is not symmetric; an exact witness is

\[
L_{01}-L_{10}=
\frac{444512097856708184009271627180561519494827562500}
{6777562511292598590019138125314219038186300704417}\ne0.
\]

Consequently $T_{\rm recon}$ is neither ordinarily symmetric nor self-adjoint in $K_c$.  Explicitly,

\[
(T_{\rm recon})_{04}-(T_{\rm recon})_{40}
=-\frac{36147224953677877}{173502507678051605}\ne0,
\]

and $K_cT_{\rm recon}-T_{\rm recon}^TK_c=L-L^T\ne0$.  The exact characteristic polynomial is

\[
\frac{f_1(\lambda)f_2(\lambda)f_4(\lambda)}
{909868946516229671852878125},
\]

where

\[
\begin{aligned}
f_1&=1553815\lambda^2+922978\lambda-1581193,\\
f_2&=7769075\lambda^2+9188446\lambda-7905965,\\
f_4&=75372031215225\lambda^4+159030179762040\lambda^3\\
&\quad+205233213680578\lambda^2-70021643952600\lambda+27721850465625.
\end{aligned}
\]

Exact Sturm counts give one negative root and one root in $(0,1)$ for each quadratic, while $f_4$ has zero real roots.  The four real eigenvalues from the quadratics are

\[
\frac{-461489\pm4\sqrt{166865843651}}{1553815},\qquad
\frac{-4594223\pm2\sqrt{20632230001526}}{7769075}.
\]

Thus the spectrum consists of two eigenvalues in $(0,1)$, two negative real eigenvalues, and four nonreal eigenvalues.  The proposed OS transfer candidate is not positive and does not have the asserted self-adjoint contraction property.

## B7 — parameter robustness

**Verdict: CONFIRMED.**  At each of

\[
(m,c)=(1,5/13),\qquad (m,c)=(9/20,3/5),
\]

the action is nonsingular and obeys $P_sQ_sP_s=Q_s^T$ exactly.  It is not ordinarily Hermitian in either case: $\operatorname{nnz}(Q_s-Q_s^T)=144$.  The full $\{1,2,3\}$-to-$\{5,6,7\}$ cross block remains exactly zero, while every tested OS Gram is real symmetric.  For both parameter pairs the exact inertias are

\[
\begin{array}{c|c}
\text{slices}&\text{inertia }(n_+,n_-,n_0)\\ \hline
\{1,2\}&(8,0,0)\\
\{1,2,3\}&(8,0,4)\\
\{0,1,2,3\}&(8,0,8).
\end{array}
\]

Hence B3--B5 are robust at both requested exact parameter points.

## B8 — SITE core versus landed LINK core

**Verdict: CONFIRMED-WITH-CORRECTION.**  Both $8\times8$ objects are positive definite with inertia $(8,0,0)$, but they are neither equal nor diagonally congruent.  In the time-major bases $\{1,2\}\times\mathbb Z_4$ (SITE) and $\{0,1\}\times\mathbb Z_4$ (LINK), their exact first-column fingerprints are:

\[
K_{\rm SITE}[:,0]=\begin{pmatrix}
250811603701251182926764176363850176714557920003089965221914456500/666495028860293624372300921944800123265476111209829299156533225479\\
774833910662796135694483493696668873001809419538422287711000/14205832190043984576428606303574399967292796027235954966356187\\
46903749731650120248627253265305983346914154983251844819009440000/666495028860293624372300921944800123265476111209829299156533225479\\
1187132577286994426496920262756457880345118140021489216641000/14205832190043984576428606303574399967292796027235954966356187\\
45243129796157828506011517780799130427560426045000/526487826141479099111591830856964110926716018451721\\
10378264178929891064842192311513337941218949507643561405120000/163798237616194058582526645845367442434376041093592848158400891\\
29370615639054097534690042758335199669140592195000/526487826141479099111591830856964110926716018451721\\
2415710633754753658482663318099644761602729144101047732782500/163798237616194058582526645845367442434376041093592848158400891
\end{pmatrix},
\]

\[
K_{\rm LINK}[:,0]=\begin{pmatrix}
4465961414671029642827787914210419072833144728317065801107200/8932040001245962023277146780748464953706237777456506835365883\\
237199564912808874288440000/14520536702961580008309728577\\
1050948337543418959578631742021612834631611209918484431840000/8932040001245962023277146780748464953706237777456506835365883\\
237199564912808874288440000/14520536702961580008309728577\\
884535857098605641362785476810185931418341453076888306712000/4809560000670902627918463651172250359687974187861195988273937\\
-133999780279657615139374728088991301241486528062776063680000/4809560000670902627918463651172250359687974187861195988273937\\
570999549556604484506923829414943352824825024895486427800000/4809560000670902627918463651172250359687974187861195988273937\\
632211391070468212788858632570132708297186122854934282256000/4809560000670902627918463651172250359687974187861195988273937
\end{pmatrix}.
\]

There is also a short exact obstruction to any diagonal congruence.  For the index triangle $(0,1,4)$,

\[
\operatorname{sgn}(K_{01}K_{14}K_{40})=-1\quad\text{for SITE},\qquad
\operatorname{sgn}(K_{01}K_{14}K_{40})=+1\quad\text{for LINK}.
\]

A real or Hermitian diagonal congruence multiplies this triangle product by a positive square, so it cannot change that sign.  These are genuinely different positive objects.

## B9 — alternatives for $A_s$

**Verdict: CONFIRMED-WITH-CORRECTION.**  Including the fixed-slice spatial entries adds $8$ entries to $A_s$, supported on $(0,0)$ and $(4,4)$, but they cancel exactly in the oddization:

\[
D_s^{\rm include}=D_s,\qquad Q_s^{\rm include}=Q_s.
\]

The open-half choice $A_s^{\rm open}=d_K|_{\{1,2,3\}^2}$ is genuinely different.  Relative to the default it removes $8$ bond entries from $A_s$, changes $D_s$ at $16$ entries, and changes $Q_s$ at $64$ entries.  It does **not**, however, break covariance or positivity:

\[
P_sQ_s^{\rm open}P_s=(Q_s^{\rm open})^T,
\]

the action is nonsingular, its full strict cross-half block is still zero, and its Gram inertias are again

\[
(8,0,0),\qquad(8,0,4),\qquad(8,0,8)
\]

on $\{1,2\}$, $\{1,2,3\}$, and $\{0,1,2,3\}$, respectively.  Therefore the default and fixed-edge-including choices give the same $Q_s$; the open choice gives a different $Q_s$ but preserves the tested OS covariance/positivity conclusions.

## Overall verdict

**CONFIRMED-WITH-CORRECTION.**  The thick LINK seam wall (A1--A4), the site-adapted covariance/empty-cross construction (B1--B4), the exact rank-eight SITE positivity (B5), and its two requested parameter perturbations (B7) all survive.  Three precision corrections are required: A3's $(+,+,-,+)$ is a leading-minor-sign fingerprint rather than an inertia; the reconstructed one-step transfer in B6 fails symmetry, Gram self-adjointness, positivity, and real-spectrum contraction; and the open-half $A_s$ choice changes $Q_s$ but surprisingly retains the tested covariance and PSD inertias.  The SITE and LINK positive cores are genuinely inequivalent under diagonal congruence.

## Ten-line summary

1. A1: LINK reflection covariance is exact: $PQP=Q^T$.
2. A2: the seam has rank $16$, support on the two stated thick blocks, and inertia $(8,8,0)$.
3. A3: all three seam repairs fail; $(+,+,-,+)$ denotes leading-minor signs, while sector inertia is $(2,2,0)$.
4. A4: site reflection of the LINK action fails at exactly $240$ entries.
5. B1--B3: the unflipped SITE Hodge is invariant and yields exact reflected-transpose covariance.
6. B4: the full strict cross-half action block is zero term-by-term, not by cancellation.
7. B5: the SITE core is PD; its 12- and 16-dimensional extensions are PSD with rank $8$.
8. B6: the reconstructed shift has two positive, two negative, and four nonreal eigenvalues and is not self-adjoint.
9. B7--B8: robustness holds at both parameter points, but SITE and LINK cores are genuinely different.
10. B9: fixed-slice edges cancel from $D_s$; open-half $A_s$ changes $Q_s$ yet preserves covariance and the three inertias.
