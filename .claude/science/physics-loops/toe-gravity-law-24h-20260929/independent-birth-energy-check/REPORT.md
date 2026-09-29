# Independent reconstruction: original first-birth energy on the cubic rotor model

This focused check supports the reported all-first-wait positivity **within the supplied finite-torus common-limit law**. A separately written literal hop/adjoint/inverse-mark implementation reproduces every coefficient of all three magnetic Laurent polynomials, the first ten-vector constant matrix, the electric increment identity, and the resulting power bound. This is mathematical checking, not a formal audit verdict, a microscopic energy ledger, or adoption of this carrier as native M2.

## Source and independence boundary

The checked author report is `../independent-matter-route/REPORT.md`, SHA256 `44762076d6fbc200ca88a7171541d7e109be7ed307ccee2d44e20f8df2fc0653`. Its claims and displayed expected numbers were disclosed before this check, so this is not a blind check of those numbers. The independent program was written without reading or importing the author's programs or Laurent coefficient file. Only after completing its calculation was every coefficient compared with the frozen author output; all 855 coefficients match exactly. The author files remained byte-identical through that comparison.

Actual PR9345 was read, not a proxy: `gh pr view 9345` returned head `fe51bf1728b625dc0133256f43e7783afb11f7d8`, title “Control local original-record response under the complete birth law,” and state OPEN. The source definitions and preparation proof were read with `git show` at that exact head from:

- `docs/CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md`;
- `docs/CUBIC_ONE_PAIR_BAND_ACTUAL_FIRST_BIRTH_LIMIT_AND_ELECTRIC_EXCITATION_BOUNDED_THEOREM_NOTE_2026-09-26.md`.

The actual common-law, pair-form and energy/power parent notes were read at the author's bound revision `d84eacf1cb9388f424f7037b5bbdf18f9be8fca7`. They remain byte-identical at the refreshed `origin/main` read during this check, `e75578f7136401d4bd750131671aed9212c06291`. The PR sources remain separately bound provisional inputs. `SOURCE_IDENTITIES.json` records all exact filenames, SHA256s, source revisions, live PR metadata and frozen author-file hashes. The campaign's selected science/procedure base remains `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`; this is not a claim that the campaign working HEAD equals that SHA. Working HEAD when the inputs were frozen was `cf1d11b09361351d49360c5211bf41f9161f07fd`.

## Mathematical family and observable

The family is a finite even cubic torus of side (L\ge24), (N=L^3/2) A sites, oriented A-to-B edges, tensor hard-core matter (q=0,\pm1), integer rotors, all A occupied, and Gauss law \(\operatorname{div}E=q-1_A\). These are supplied structures. There are no exchange signs. With (K,\delta,\kappa>0),

\[
h=KD+\delta H_4,\quad
D=\sum_{a\to b:q_b=0}E_{ab}(E_{ab}-q_a),\quad
H_4=-2\sum_{\{a,c\}:|a-c|_1=2}S_{ac}^{*}S_{ac},\qquad
S_{ac}=F_cF_aP.
\]

An outward (F_a) moves (q_a) to an empty neighboring B, empties a, and shifts (E_{ab}) by (-q_a). Its adjoint returns that particle and shifts E by (+q_a). The original (j_{ab,\sigma}) fills two empty endpoints with (\sigma,-\sigma), shifting (E_{ab}) by (\sigma). Keep the exact original (B_{ab,\sigma}=Pj_{ab,\sigma}F_aP) and (B_{ab,c}=B_{ab,+}+B_{ab,-}), without rescaling the coherent mark.

The initial Ω has all A plus, all B empty and E=0. The normalized actual no-birth state is
\(\phi_s=e^{-ih_{\rm pre}s}\Omega\), up to the irrelevant scalar phase. The observable is

\[
Q_m(s)=\frac{\langle B_m\phi_s,hB_m\phi_s\rangle}{n_m}
          -\langle\phi_s,h_{\rm pre}\phi_s\rangle,
\qquad n_\pm=5,\quad n_c=10.
\]

The quantifier is every finite first waiting time on each stated finite torus, with no strong-electric hierarchy required. It is not every possible prebirth state and not an assertion about later-birth inputs.

## Original-mark normalization and interference

Fix a=0,b=e1. For each of the five (d\sim0,d\ne b),

\[
B_{0b,\sigma}\phi
=\sum_{d\ne b}|q_{\sigma,d}\rangle
 U_{0b}^{\sigma}U_{0d}^{-1}\phi .
\]

These five matter words are distinct, and the two signs have distinct matter words. Consequently (B_\sigma^*B_\sigma=5I), (B_c^*B_c=10I) on the whole prebirth sector, for arbitrary rotor states there. This is not an assumption of independent destination records. The original superposition remains intact.

Opposite signs also have zero **Hamiltonian** cross compression. D is matter-diagonal. In every (S_{ac}^*S_{ac}) path, both outward hops precede both returns. An initially occupied B site cannot receive an outward hop. During returns its charge can stay or be removed, but cannot be replaced by the opposite charge. The fixed b is occupied with opposite signs in the plus/minus original outputs. Therefore

\[
B_-^*H_4B_+=B_+^*H_4B_-=0
\]

on prebirth inputs for every rotor field, not just at E=0. The exact program also computes and checks both complete cross-sign Laurent blocks as empty. Same-sign destination interference is retained; in particular the plus block's (-186) off-diagonal constants are not omitted.

## Full magnetic operator and support cancellation

Define the prebirth rotor operator

\[
A_m=\frac1{n_m}B_m^*H_4B_m-H_{4,\rm pre}.
\]

The mark is supported on the root star. A pair whose two centers both lie outside the root together with its 18 distance-two A neighbors has disjoint star support. On the P space the pair term has a local extension; the global P notation adds no remote operation. Such a pair term commutes with B and B*, and the prebirth sector is invariant under it. Its contribution to (A_m) cancels as an operator, including every plaquette translation, by (B_m^*B_m=n_mI). Cross-sign remote terms vanish by the zero loss cross term. Thus only the 264 unordered pairs having at least one endpoint in those 19 centers need be computed. No magnetic projection (P_0), field cutoff, D-sector deletion or scalar-only remote cancellation is used.

The independent algorithm applies (F_a,F_c,F_c^*,F_a^*) literally to each first branch. It then applies (j_{0b,\sigma}^*) and the return hop (F_0^*), retaining only exact prebirth matter words and recording their net electric shift. This is different from forming pair-output Gram matrices. All amplitudes are integers until the final normalization. The near calculation examined 152,028 returned paths. An additional 774 disjoint pairs examined 275,820 returned paths and gave zero for **every** residual coefficient. That shell is a check on the analytic disjoint-support argument, not a replacement for it.

Every surviving word is a divergence-free integer circulation, has its reverse with the same rational coefficient, and uses vertices in ([-2,2]^3). The full relevant pair path supports lie within the radius-five coordinate patch, with no alias at (L\ge24). The unfolded calculation therefore applies to every stated torus, including harmonic flux sectors of the prebirth space.

Write (A_m=a_mI+\sum_{z\ne0}c_{m,z}U^z). The exact reconstruction gives:

| Mark | (a_m) | (\sum_{z\ne0}|c_{m,z}|) | Operator lower bound |
|---|---:|---:|---:|
| minus | 12172/5 | 3624/5 | 8548/5 |
| plus | 8452/5 | 3912/5 | 908 |
| coherent | 10312/5 | 3768/5 | 6544/5 |

There are 284 nonconstant words, hence **285 total words including the constant**, for each mark. This resolves any ambiguity in the shorthand “284 words.” The full coefficient files agree exactly with the author's frozen files. The coherent polynomial is coefficientwise half the sum of the two resolved polynomials.

The operator bounds follow directly from unitary rotor translations and the triangle inequality. They do not require small fields, a special rotor wave function or a floating momentum grid.

At zero initial field the nonconstant shifts have zero expectation. The independent full ten-vector constant matrix has, in each sign block, diagonal (2444) for (d=-e1) and (2432) for the four transverse feet. The minus block has zero off-diagonal constants; every plus off-diagonal constant is (-186); the cross-sign block is zero. Its normalized sign sums reproduce the displayed (a_m).

## Electric compression and actual waiting-time symmetry

Let E be any divergence-free prebirth integer field. For one branch (\sigma,d), b and d become occupied, so all six electric terms ending at each are removed. The two rotor shifts themselves end at those newly occupied B sites and therefore contribute to no remaining D term. Only the root charge changes, from +1 to (\sigma). Before using Gauss,

\[
\Delta D_{\sigma,d}(E)
=-\sum_{x\in\{b,d\}}\sum_{c\sim x}E_{cx}(E_{cx}-1)
 +(1-\sigma)\sum_{y\sim0,\ y\notin\{b,d\}}E_{0y}.
\]

At each empty prebirth B, (\sum_{c\sim x}E_{cx}=0); at the root (\sum_yE_{0y}=0). Therefore, exactly,

\[
\boxed{\Delta D_{\sigma,d}(E)
=-\sum_{x\in\{b,d\}}\sum_{c\sim x}E_{cx}^{,2}
 -(1-\sigma)(E_{0b}+E_{0d}).}
\]

The checker separately evaluated the original masked D before/after all ten branches on 31 integer divergence-free fields, each constructed from 375 plaquettes, for 310 exact branch comparisons. This includes nonzero fields on and around the birth star. The symbolic derivation above supplies the general quantifier beyond these finite checks.

D is matter-diagonal, so no destination or cross-sign interference is missing from this compression. Average the five branches for a resolved mark, or the ten for the coherent mark.

In the prebirth matter sector, (D=\sum_eE_e^2). Independent local geometry enumeration found six A partners with one shared B and twelve with two, with two-hop diagonal counts 35 and 34 respectively. It reconstructs

\[
H_{4,\rm pre}=-618NI+V,\qquad
V=-2\sum_{6N\ {m elementary\ plaquettes}\ p}(U_p+U_p^*),
\qquad\|V\|\le24N.
\]

The prebirth Hamiltonian and Ω are invariant under even-sublattice translations, proper cubic rotations, and the **unitary** field inversion (|E\rangle\mapsto|-E\rangle). Proper rotations and translations act transitively on the (6N) oriented A-to-B edges; field inversion takes each plaquette shift to its adjoint. Thus every finite waiting-time state has

\[
\langle E_e\rangle_s=0,\qquad
\langle E_e^2\rangle_s=\frac{\langle D\rangle_s}{6N}.
\]

There are twelve distinct removed edges for any branch, so every original mark has the exact expectation

\[
\frac{\langle B_m\phi_s,DB_m\phi_s\rangle}{n_m}
-\langle D\rangle_s=-\frac{2\langle D\rangle_s}{N}.
\]

The total original loss is (60NI) on the prebirth sector for either instrument. Hence normalization removes the scalar no-jump decay and leaves precisely the unitary prebirth evolution used above; this is the actual first-wait law, not an imposed surrogate. Since \(\langle\Omega,V\Omega\rangle=0\), conservation of the prebirth energy gives

\[
K\langle D\rangle_s=-\delta\langle V\rangle_s\le24\delta N,
\quad
K\langle\Delta D_m\rangle_s\ge-48\delta.
\]

## Positivity, power and domains

Combining the independently reconstructed magnetic bounds with that exact electric estimate gives, for every finite first wait,

\[
Q_-(s)\ge\frac{8308}{5}\delta,\qquad
Q_+(s)\ge860\delta,\qquad
Q_c(s)\ge\frac{6304}{5}\delta.
\]

The initial values are the magnetic constants times \(\delta\). Summing the actual adjoint-dissipator contributions on the prebirth state,

\[
\mathcal P(s)=\kappa\sum_m
\left(\langle B_m\phi_s,hB_m\phi_s\rangle
-\operatorname{Re}\langle B_m\phi_s,B_mh\phi_s\rangle\right)
=60\kappa NQ_c(s).
\]

Here h preserves the prebirth sector and (B_m^*B_m=n_mI) there, so the loss term has not been dropped. Translation/rotation symmetry makes the corresponding edge quantities equal; (Q_c=(Q_-+Q_+)/2) follows from the vanishing full-Hamiltonian cross block. For either the resolved or coherent instrument,

\[
\boxed{\mathcal P(s)\ge75648\kappa\delta N,\qquad
\mathcal P(0)=123744\kappa\delta N.}
\]

The integer multiplication operator D is self-adjoint and H4 is bounded on each fixed finite graph. Ω lies in \(\operatorname{Dom}D\), and the prebirth unitary preserves that domain. Every first branch has a finite rotor translation and its postbirth electric quadratic form is bounded by a constant times (1+D_{\rm pre}); pointwise the corresponding postbirth D itself has the same quadratic bound. Thus the normalized first outputs lie in the required energy domain, and every displayed energy/power expectation is defined. For interpreting the power as an instantaneous ordinary energy derivative, the supplied Ω also has all electric moments: bounded finite rotor shifts preserve each finite-graph polynomial electric graph norm under the interaction-picture expansion. This supplies the weighted-domain control needed beyond bare trace-norm continuity. No assertion is made that a finite shift preserves the full degenerate D-domain on arbitrary later matter inputs.

## Exact scope and remaining obligations

The checked result resolves the narrow all-first-wait positivity question for the supplied common-limit model. It does not establish a closed reservoir energy ledger, a uniform microscopic-limit energy derivative, native selection of Ω/H4/the birth instrument, a calibrated physical clock, heat/work/absorption, or a later-birth ensemble sign. The actual later inputs can leave this special sector and need their own electric and interference calculation. Nor does this prove an infinite-volume globally first event. Those are additional physical or mathematical obligations, not gaps in the displayed finite-prebirth inequality.

The optional stronger large-R preparation estimates, the PR's 11,322-state band and record-response calculation, and the matter/gravity cross-bracket claims elsewhere in the author report were not independently rerun here. The parent common-limit theorem is a supplied dependency, not rederived in this check. No claimed equality or positivity above depends on those unrerun numerical components.

Reproduction: run `check.py` with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1`, then `PYTHONDONTWRITEBYTECODE=1 python3 prebirth_geometry.py`. The main run took 37.54 seconds, used only Python's standard library and one process, and retained every exact Laurent coefficient in `coefficients.json`. `results.json`, `prebirth_geometry.json`, `comparison.json`, `run.log` and the hash manifests contain the evidence. The deadline and absence of a stop sentinel were checked before the work. No heavyweight quotient reconstruction, other-directory writes, GitHub mutation or audit operation was performed.
