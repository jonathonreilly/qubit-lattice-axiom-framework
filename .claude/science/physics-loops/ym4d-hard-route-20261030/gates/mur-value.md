Provenance: Codex (gpt-6-astra), high effort; checkout `74c632467f9921adc168ca4103a695edec9570f6`. Research value and novelty check for FINISH row 390, not an audit; no scientific status is granted.

# MUR value check

## 1. Correct: the counterexample

**ADVANCE for the literal correction; CORRECT-NO-ADVANCE for a claimed failure of a downstream theorem.** The counterexample is correct under the normalization cited by the account. It refutes an extra assertion about representatives. It does not refute the curvature/current conclusions used later.

Sources below are Ethan Sussman and Levent Alpoge's outline and complete account, with Claude and Codex as authors of their text, at `31a47c543775`. `SA` means `YM4_sketch_500.tex`; `I`, `II`, `III` mean the corresponding complete-account files. Line numbers refer to those raw files. The gauge construction is Tadeusz Bałaban's. Each source file was fetched once. Searches served navigation only; all mathematical reasoning below is by hand.

There is no `library/prior/mur-value.md` at this checkout. The registry already records MU-BLOCK-A and MU-BLOCK-C under `mu-radii` (`library/open-registry.md:319–320`). This report checks the requested candidate; it does not reopen that owner's repair lane. At this checkout the counterexample is in `library/mu-radii.md` §4.3, lines 648–725, rather than §2. The corrected formulas are in §§4.1–4.2, lines 446–646. The specified external paper folder is absent here; I do not claim a fresh inspection of Bałaban's printed pages. Their formulas are available in the account, and the prior page inspection is recorded in `gates/mur-gate.md:29–35`.

**Which fields are compared.** I:38515–38527 explicitly calls \(U_k(V_0)\) the axial minimizer. Its fine tree bonds equal one; see I:130021–130052. In contrast, I:154169–154182 and 154193–154230 use the exponential potential of the complex-background construction. Under the cited Bałaban construction this is the Landau representative before axialization. Their own earlier reading of CMP 109 (3.38) is decisive:

> “We set \(g_{\langle3.38\rangle}:=u_j\bar u_j^{-1}\).” — I:29234–29239.

Here only \(\bar u_j\), the extension of the values of \(u_j\) at the block centers, is block-constant. I:154355–154366 instead makes the whole acting gauge block-constant. I:154419–154425 also changes the quoted lowercase \(u_j\) into uppercase \(U_j\). These are incompatible readings of the same cited identity.

**Redo of (21)–(22).** Let \(T=\operatorname{diag}(1,-1)\), let \(h\) be the fine spacing, and set

\[
\mathcal U_a(x,x+he_1)=e^{ihaT},\qquad
\mathcal U_a(x,x+he_\mu)=1\quad(\mu\ne1),\qquad 0<|ha|<\pi.
\]

All factors commute. Every contractible plaquette product is exactly one, and the Wilson current is exactly zero. A local averaging path with endpoint displacement \(se_1\) has transport \(e^{isaT}\). Hence the group averages, on their identity branch, give the constant connection at the averaged spacing. The potential is constant, so all its differences and its divergence vanish in the variable region. For a local box the fixed fine shell is included in the datum, rather than set to zero. A zero-average gauge parameter \(\lambda\in N(Q')\) vanishes on that shell. Thus \(\Delta\lambda\) is supported within one lattice step of the variable region, where all incident bonds exist and the constant potential has \(D^*A=0\). Consequently \(\langle D^*A,\Delta\lambda\rangle=0\). Since \(R\) projects onto \(\Delta N(Q')\), this proves \(RD^*A=0\). This spells out the boundary qualification in the earlier check (`mur-gate.md:44`).

Use the normalized Landau-to-axial map of the cited construction, and call the axial image \(W_a\). Define the outer raw datum by \(D_a=-i\log M_{\rm outer}W_a\), including its shell. This detail matters: the raw averages of the Landau and axial fields need not be identical. Also, Bałaban's normalization is by gauge averages; “root normalization” in `mu-radii.md:676–699` must not impose an additional, incompatible normalization. All these finite chart operations are analytic at \(a=0\), and \(D_0=0\). Thus \(D_a\to0\). Choose nonzero \(a\) sufficiently small for the fixed box and its admitted chart. The field has zero action and solves the constrained critical equations. The cited uniqueness of the normalized small Landau solution identifies \(\mathbf U[D_a]=\mathcal U_a\). This uses that uniqueness input, not a computed solution or a newly proved version of Bałaban's theorem.

Choose an allowed inner depth \(n=1\) and an interior level-one tree bond \(b\parallel e_1\) in \(X^{\sim-2}\), with \(X^{\sim5}\subset\square_0\). Such a bond exists in a spanning tree of the block. The inner axial minimizer has value one on \(b\). If \(v\) is constant on this block, both endpoints have the same value and

\[
\mathcal U_a^v(b)=v e^{ihaT}v^{-1}\ne1.
\]

Indeed, equality to one would imply \(e^{ihaT}=1\), contrary to \(0<|ha|<\pi\). This holds for complex invertible \(v\) as well as unitary \(v\), and for either inverse convention. It disproves (a) at arbitrarily small real data. Shrinking a positive radius cannot fix it.

For (c), take the torus base \(V_0=1\) and a sufficiently small constant real top perturbation in direction one. Its normalized Landau field is the same flat constant connection. The torus has no boundary divergence, and the same interior tree bond gives the contradiction. No wrapping set is needed. The current identities happen to be zero equals zero in this example; it is the configuration identity that fails.

Changing the intended representative to an axial one would require changing or justifying the background construction and its potential bounds. It is not a defense of the cited Landau normalization. Conversely, the example does not disprove equality up to a general small gauge transformation. The account itself explicitly distinguishes these representatives at I:41527–41537: the axial configuration, brought to Landau gauge, equals the exponential of the potential.

## 2. Load-bearing: uses and repairs

**The nesting relation is load-bearing; block constancy of its acting gauge is not.** Two direct estimates use (a) or (c). Both survive the corrected identities with the same numerical factors. The literal statements and their repeated descriptions need repair.

### 2.1 Replacement text and its cost

Replace the sentence at I:154355–154359 and lines (a), (c) of `4.31:eq-window-counting-nesting-c` as follows. Retain their domains, quantifiers, background inputs and scale conventions:

> There are generally non-block-constant \(G^{\mathbb C}\)-valued gauge transformations \(g_X\) and \(h_X\), with
> \[
> \begin{aligned}
> U_n(X,M^n\mathbf U[D])&=\mathbf U[D]^{g_X},&
> J_n(X,M^n\mathbf U[D])&=(L^n\xi)^3\operatorname{Ad}(g_X)J^\xi(\mathbf U[D]),\\
> U_n(X,M^nW)&=W^{h_X},&
> J_n(X,M^nW)&=(L^n\xi)^3\operatorname{Ad}(h_X)J^\xi(W),\\
> \|g_X^{\pm1}\|&\le1+c_u\beta,&
> \|h_X^{\pm1}\|&\le1+c_u(B_3w_s+C_{19}\rho_s).
> \end{aligned}
> \]
> The constants are fixed before the radii. In Bałaban's action convention the relative gauge in the local identity is \(u_j\bar u_j^{-1}\); only \(\bar u_j\) is block-constant. Under the opposite composition convention use the corresponding ordered relative product.

These are `mu-radii.md` (14), (18), (19), including their radius conditions, not a claim that arbitrary gauges satisfy those bounds. Real restriction and uniqueness identify the inner axialized field; holomorphic continuation gives the identity at complex data. The inputs retained by that argument are the admitted minimizer charts, real restriction/uniqueness and the complex-twist averaging bound. This report does not discharge their general outstanding uniqueness/locality lemma.

Here is the uniform gauge-cost calculation behind the repair. A descending tree path has at most \(dL\) bonds per level (I:129550–129559). For local data the logarithm of a level-\(m\) tree variable is bounded by \(C_AK_W\beta s_m\), where \(K_W\ge2C_{19}B_0\), \(s_m=L^m\xi\), and \(C_A\) is the admitted averaging constant. Their relative tree-product identity (I:130055–130083, 130150–130190) therefore gives

\[
\|g_X^{\pm1}\|\le
\exp\!\left(dLC_AK_W\beta\sum_{m<n}s_m\right)
\le e^{C_tK_W\beta},\qquad C_t=\frac{dLC_A}{L-1},
\]

since \(s_n\le1\). For \(0\le x\le1/2\), the power series gives \(e^x\le\sum_{q\ge0}x^q\le1+2x\). Increase \(c_u\) to at least \(2C_tK_W\) and decrease \(\beta_W\) within the admitted charts. This yields the displayed local bound on the whole path, not only at its endpoint.

For the global field use its real axial base \(U_0\). Its inherited tree variables are one. The complex-twist bound gives the analogous tree logarithm bound \(C_AC_{19}\rho_s s_m\), hence \(\|h_X^{\pm1}\|\le e^{C_tC_{19}\rho_s}\). Choose one real-base chart radius before \(w_s,r_s\), and impose `mu-radii.md` (17): \(C_{19}\rho_s<a_{98}/2\) and \(C_AC_{19}\rho_s<r_g/2\), together with its real-base admission ceiling. Here \(a_{98}\) and \(r_g\) are the positive averaging and minimizer-chart thresholds. Enlarge \(c_u\) once more if needed. The same series estimate proves (18). Paths remain inside individual structure blocks, so neither the volume nor wrapping adds a factor.

Retain (S1), now with this \(c_u\), and choose \(w_s,r_s\) afterwards. All new ceilings are upper bounds with fixed positive thresholds. Their existing choice argument at I:154950–155038 still applies. The path radius at I:155965–155974 already includes \(\beta_W\) and \(1/(10c_u)\); changing these fixed constants only changes \(c_R\) and the derived \(C'_5\). It does not change cutoff dependence or the factor \(L^{-4t}\).

### 2.2 Complete direct-use ledger for the defective assertion

I searched all four source files for the exact definition/equation labels, (N1)–(N3), the nesting phrase, CMP 109 (3.38), and block-constancy descriptions, including line breaks. I read the matching mathematical passages. The following are all direct occurrences of this §4.31 assertion and its relevant immediate consumers. A citation to the surrounding definition alone need not use its nesting clause.

| Place | What it uses | Disposition |
|---|---|---|
| I:154338–154404; explanation at 154419–154427 | States (a)/(c), small-gauge bounds and block constancy; attributes (a) to (3.38). | **Literal assertion fails.** Substitute §2.1. In the quotation restore lowercase \(u_j\), and explain that the exponential field is acted on by the relative product. |
| I:154681–154705, `4.31:prop-fixed-depth-convergence` | Explicitly assumes (I9), namely (N1)–(N3). | **Repair premise; conclusion survives conditionally.** Assume the replacement identities. The original is an implication with a false extra hypothesis, not a demonstrated false convergence conclusion. |
| I:154958–154980, 155025–155038 | Chooses radii using \(c_u,\beta_W\). | **Survives with repaired constants.** Rechoose fixed constants and then radii as above. |
| I:155242–155261 and 155387–155429, `4.31:lem-background-membership` | (c)/(N3) proves hereditary curvature and current condition (iv), for all allowed \(X,n\). | **Repair identity and delete “block-constant” at 155402; estimate survives.** Replace \(\bar u^{-1}\) by \(h_X\). The proof itself derives plaquette covariance for an arbitrary gauge at 155405–155409. |
| I:155455–155513, `4.31:rem-non-minimiser-data` | Explains why nesting, rather than a bare datum bound, supplies cutoff-uniform condition (iv). | **Survives.** The replacement still compares with \(W\), with uniform gauge cost. No claim here needs block constancy. |
| I:155855–155870 and 155957–156038, `4.31:prf-marginal-minimiser-path` | (a)/(N1) supplies membership throughout the complex \(\tau\)-disc. | **Repair identity and delete “block-constant” at 156010; estimate survives.** Replace \(\bar u^{-1}\) by \(g_X\), retaining the path minimum. |
| I:156045–156060 | Adjacent (b)/(N2) identifies the endpoint with \(\psi(1)\). | **Survives through the weaker equality (20).** It needs equality of gauge-invariant values, not block constancy or the separate bound \(2\) on \(\bar u_1\). See below. |
| I:156150–156159 and 156210–156230, `4.31:rem-marginal-uniformity` | Repeats that the gauge bound is uniform in \(n\), then concludes cutoff independence. | **Delete “block-constant” at 156211; conclusion survives.** The geometric sum in §2.1 supplies the same uniformity; update \(c_R,C'_5\). |
| I:156342–156354, 156403–156411, 156447–156486, `4.31:prf-tube-analyticity` | Uses background membership and the marginal bound to extend and sum the local pieces. | **Survives as the same implication.** The input bounds survive. The cancellation \(L^{4t}L^{-4t}=1\) is unchanged. |
| I:156520–156548 and 156677–156707, couplings/densities and normal-family lemmas | Inherit the proposition's hypotheses; the latter uses tube analyticity. | **Survive conditionally.** Replace the inherited nesting premise. No new gauge step occurs here. |

For clarity, the two direct inequalities can be checked without any regularity of the gauge. A plaquette based at \(x\) transforms by conjugation with \(g(x)\); the intermediate endpoint factors cancel. If \(\|g^{\pm1}\|\le1.1\), this costs at most \(1.1^2=1.21\). For (N1), the curvature bound becomes \(1.21\alpha'\xi^2<\alpha_{0,j}\xi^2\), since \(\alpha'\le\alpha_{0,j}/(2B_3)\) and \(B_3\ge1\). Its current is bounded by \(1.21(2/3)\alpha'(L^n\xi)^3\le1.21(2/3)\alpha'(L^n\xi)^2\), exactly as at I:156017–156035. For (N3), the curvature bound becomes \((1.21/2)\alpha'_0\xi^2<\alpha'_0\xi^2\), and the current estimate at I:155417–155425 uses the same \(L^n\xi\le1\). Thus deleting block constancy changes none of these conclusions.

For (N2), write the repair at its actual use as

\[
f(W,J^\xi(W))
=f(W^g,\operatorname{Ad}(g)J^\xi(W))
=f(\mathbf U[D],J^\xi(\mathbf U[D])).
\]

The local class is invariant under all complex gauges (I:153964–153970). Use the orbit identity and continuation, or the real-slice reduction already given at I:154407–154417. For the latter, use the actual holomorphic datum \(D(B)\) and a strict bound \(2c_{\rm av}C_gMh_s<\beta_W\) on the whole \(4r_s\)-ball (`mu-radii.md:630–639`). This ensures both sides are holomorphic. Their identity principle then applies. This repairs the consumed equality only; it does not establish the stronger standalone norm-\(2\) assertion for arbitrary gauges. That separate issue is MU-GAUGE-2, owned by `mu-radii` (registry line 321).

The other whole-definition references are harmless: I:155039–155050 reads the window clause; I:156348–156351 reads counting and real gauge covariance. The constant-conjugation proof at I:154250–154300 uses (181), not the faulty (a)/(c). The caveat at I:154826–154855 changes none of the use ledger.

### 2.3 CA-II, CA-III, the outline, and other block-constant gauges

There is **no direct reference to §4.31's nesting assertion or its (a)/(c) in CA-II, CA-III or SA**. This is a textual dependency finding, not a claim that the rest of their construction is independent of background estimates. The related uses below survive this correction. Their other hypotheses and declared proof gaps remain in force.

| Place | Relation to the candidate and disposition |
|---|---|
| I:29234–29239; 31073–31132; 33678–33691; 33757–33772 | Already use the relative product, with both factors, and pay its conjugation cost. **Unaffected.** I:32419–32423 cites this nesting input; I:10600–10608 only names its cube-gauge floor. |
| I:45162–45201 | States arbitrary-subdomain uniqueness/locality as **proof outstanding**. It cites the actual (3.38), not the faulty later restatement. **Unaffected and still outstanding in their text.** This candidate does not solve it. |
| I:121185–121199, 121220–121233, 121435–121476; 123123–123132; 144931–144933 | Stage composite entries use the relative product or its stated conjugate, with a conditioning bound. They distinguish \(u_\ell\) from \(\bar u_\ell\). **Unaffected.** The full-datum conditioning input is explicitly marked incomplete. |
| I:129543–129559; 130055–130083; 130178–130190 | Define block roots and prove the relative gauge is a tree product, with an explicit warning to follow the action convention. **Already supply the mechanism of the correction.** |
| II:35710–35724 | Uses (3.38) expressly “modulo gauge.” **Unaffected.** No block-constant acting gauge is claimed. |
| II:44414–44427, 44446–44460 | Retains the regauging \(u_B\), then cites (3.38) for potential bounds. **Unaffected by this correction.** Whether those separately cited potential estimates have the required radii is a different question, already treated by `mu-radii` §5. |
| SA:9693–9716; 9776–9783; 9913 | Distinguishes the axial continuation \(\Phi\) from its Landau pair \((\mathcal H,u)\); restriction is modulo residual gauge. **Unaffected.** These are their stated/sketched constructions, not a new proof supplied here. |
| SA:7800; 26511–26514 | Uses regularity/uniqueness for nesting, and nesting/localization in a common box gauge for a curvature decomposition. **Unaffected by removal of the false block-constancy assertion.** No claim that this check completes those arguments. |
| SA:7673; 8735–8760; 9558–9566 | Uses block-constant gauges for gauge-fixing invariance and for flattening a field **already in its prescribed block-axial representative**. **Unaffected.** In particular, the flat Landau counterexample cannot be substituted for that axial representative. |

The remaining gauge-related occurrences of block constancy concern **extensions of gauge transformations of the data**, namely CMP 102b (181). This is different from regauging a Landau field to its axial representative. They must not be changed to nonconstant maps indiscriminately:

| Occurrences | Use; effect of the candidate |
|---|---|
| I:16751–16760, 16816–16826 | Data-gauge covariance and exact invariance at a fixed block. **Unaffected.** |
| I:17611–17628, 17833–17847, 17975–18008 | Frame/base-change identities between axial charts. They separately retain the Landau-to-axial factor \(g\). **Unaffected.** |
| I:18653–18678, 19174–19185, 19235–19248 | Fine axial frame and its covariance; again a separate \(g'\) is retained. **Unaffected.** |
| I:38579–38589, 41527–41537, 42405–42418 | Gauge extension of the axial minimizer; the last passage expressly writes \(\Xi=v\tilde u\), with \(v\) the Landau-to-axial change. **Unaffected; further evidence that the missing factor is known elsewhere.** |
| I:82044–82054, 82899–82912, 83310–83317 | Derived frame entries transform by the block extension of a data gauge. **Unaffected.** |
| I:85058–85062, 94347–94357, 95031–95045 | Rotated kept slots and the extension factor in a product \(\mathfrak u^C\tilde v\). **Unaffected.** |
| I:98826–98836 | Covariance of extension formed from coarse averages. **Unaffected.** |
| II:43328–43339, 43549–43558, 43836–43845 | Working/native data transformations use the block extension in (181). **Unaffected.** |

I:36060–36065 explicitly says no such factor acts in that construction. I:153629–153636 explicitly allows arbitrary gauges in plaquette covariance. Neither is a use of the false assertion. III:37440–37447 concerns a scalar lift; II:94538–94589 concerns a scalar quadratic form. SA:682 concerns the range of a scalar projection. These are not the disputed lattice gauge transformation. Other “block constant” hits denote numerical constants, not constant maps. No additional gauge-constancy consumer was found.

## 3. Already known: what their text does and does not record

**The correct mechanism is already theirs. The local inconsistency is not expressly acknowledged.** It would be misleading to offer the relative gauge identity as new mathematics.

1. **CA-I already writes the correction.** Besides I:29234–29239, I:33684–33691 gives
   \[
   U_n^{\mathfrak r}(Z;M^{\boldsymbol\cdot}\mathcal U)
   =(\mathcal U|_Z)^g,\qquad g=u_j\bar u^{-1}.
   \]
   I:121436–121442 retains both factors too. I:130188–130190 calls the acting element a “conjugation-free tree product equal to the identity at roots.” Identity at roots is not constancy on blocks. Thus even the structural explanation predates the candidate.

2. **Their outline distinguishes the representatives.** SA:9699–9704 writes
   \(\Phi(B)=(e^{i\eta\mathcal H(B)}U_0)^{u_B}\).
   Its restriction formula at SA:9778–9780 ends “modulo \(\mathcal G^{\rm res}(\mathbf B')\).” The explanation at SA:9913 uses criticality and uniqueness. Nothing in these passages says the Landau-to-axial gauge is block-constant. SA:7683 likewise distinguishes the axial field \(U\) and \(W=U^{u^{-1}}\).

3. **They already mark the general missing proof.** I:45162–45177 labels `4.13:lem-minimizer-unique` “Proof outstanding.” Its locality clause requests (3.38) on arbitrary subdomains. I:45179–45201 explains the missing admission, uniqueness and locality work. The end lists repeat “Uniqueness and locality of the constrained minimiser — proof outstanding” (I:166621; III:111211–111212). These are broader obligations, not an acknowledgment that §4.31 dropped a gauge factor. They must not be presented as newly discovered gaps. The stage-gauge bound is separately marked incomplete at I:121443–121451 and 123129–123132.

4. **Their nearby caveats do not correct this error.** I:154851–154853 excludes the general complex implication (i)–(iii) ⇒ (iv) for non-minimizers. I:155455–155513 explains the nonuniformity of a datum-only argument and still relies on the nesting identity. Neither flags its block-constant requirement as false. The §4.31 theorem expressly takes nesting as input (I:154697–154700); that is a limitation on what is proved, not a correction of the stated input. The outline's Package A list at SA:32909 names 1a.3.2 and 1a.3.5, and SA:7683 marks the Landau-gauge items to be proved. These do not record this particular transcription error.

The full-read index led to these passages: chunks 07–09 and their neighboring rows; `obligations.md` entries for 7683, 7705, 9693–9697, 9776, 9913 and 32909; the CA 4.12–4.19 index's uniqueness/locality entry; and the CA full index's §4.31 entries. Searching the four sources for the faulty phrase, the relevant labels, both factors and correction/caveat terms found no express withdrawal of §4.31(a)/(c). This is the scope of the novelty finding; it is not a full rereading of the account.

## 4. Value from the authors' side

**Rating: actual error with no consequence for the identified downstream conclusions.** More precisely: a false extra representative assertion, caused by a transcription/normalization slip, whose removal preserves every identified consumer after the fixed constants and radii are chosen as above. It is not merely an interchangeable symbol: no block-constant gauge can satisfy the printed equality in the example. It is also not a new missing theorem. The correct factor and the reason for it already appear repeatedly in their work.

As an author, I would want this as a short consistency erratum, with the internal cross-reference and the statement that the bounds survive. I would not regard it as the larger contribution sought in FINISH row 390. It neither changes a downstream conclusion nor closes their marked uniqueness/locality problem. **Do not promote it as a proof-breaking error or a new repair theorem.** Its value is that it gives an unambiguous edit, supported by a tiny exact counterexample. It could be bundled with another substantive contribution; it does not justify a long separate submission. Nothing has been sent.

The most useful one-paragraph report would be:

> In your complete account, §4.31, I:154355–154376 and 154397–154404 require the gauge relating the Landau background to the local axial minimizer to be block-constant. This drops the Landau-to-axial factor retained in your own reading of Bałaban (3.38), I:29234–29239 and 33684–33691. A flat diagonal field with fine links \(e^{iha\operatorname{diag}(1,-1)}\) in one direction, \(0<|ha|<\pi\), makes the issue explicit: an inner axial tree bond is one, whereas block-constant conjugation cannot turn that nonidentity link into one. Please replace the acting gauge by the relative gauge \(u_j\bar u_j^{-1}\), with the order appropriate to the action convention, and remove “block-constant” from its descriptions at I:155402, 156010 and 156211; also restore lowercase \(u_j\) in the quotation at I:154423. The curvature/current arguments at I:155387–155429 and 156008–156038 require only a gauge and its inverse bounded by \(1.1\). The relative tree-product bound you give at I:130055–130190 supplies that cost after adjusting the fixed smallness constants, so these conclusions survive. This is a local consistency correction, not a new obstruction to your argument.

Checked line by line by Codex (gpt-6-astra).
