lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T23:53Z

# Literature search: the large-field position and the four lanes of sa-map Section 5

Queue row 74, `lit-large-field`. Pinned at commit 199fac1cb. Finished 2026-11-02.

Author: Anthropic claude-opus-5-5, effort high, Mac mini worker, started
2026-11-02T11:53Z. Same-model reading: not independent in model, not a gate, not
an audit, no status. A literature search finds statements and proofs. It
verifies nothing. Every statement listed below is **unchecked here** until it is
rebuilt by hand in `library/` and gated, per "Build on published work" in
FINISH.md.

## 0. Scope and how the search ran

The four statements are the four lanes of `library/sa-map.md` Section 5, all
written in the symbols of Sussman and Alpoge's outline `YM4_sketch_500.tex`
at `31a47c543775` (cloned read-only to a scratch directory; this was still the
head of `main` on 2026-11-02):

- **S1 (`sa-floor`).** Floor screening and renewed tests of the R operation:
  a new mark pays outside the old floor F (l. 18334-18415), and item (4) of
  "One action and many claimants" (l. 17712).
- **S2 (`sa-seam-response`).** Healing across seams. A layered,
  seam-crossing response bound (their A3, (1b) Theorems 3-4, l. 9693-9745),
  which feeds the ten-term remainder R_X of Prop 2.8 and the resummation of
  Prop 2.10.
- **S3 (`sa-order`).** One simultaneous order of constants (C4, Theorem 2.11,
  l. 19435-19470).
- **S4 (`sa-count`).** The genealogy count (Prop 2.6, l. 17719; count over
  generations l. 18475-18604) and the label sum with the logarithm (Prop 2.13).

Sources searched: Balaban's series (CMP 85-122, plus his later N-vector
large-field papers); Dimock's expositions (Balaban RG I-III; scalar QED_3;
QED_3 I-III); Balaban-Feldman-Knörrer-Trubowitz (bosonic many-body); Balaban-
Imbrie-Jaffe and King (Higgs); Magnen-Rivasseau-Sénéor (YM_4 with an infrared
cutoff); Federbush (phase cells); Gawedzki-Kupiainen; Brydges and
Bauerschmidt-Brydges-Slade (large-field regulators); recent probabilistic and
stochastic-quantisation work (Chatterjee, Cao, Chevyrev, Chandra-Hairer-Shen);
the Sussman-Alpoge repository (YM4 outline, YM3_I/II, QED3, QCD3, and the raw
Theorem 0 account); the two other public projects its README lists
(`marikgoldstein/scalar-qed-existence`, `pmaronow/3d-ym-torus`); arXiv and
news for anything since mid-2026.

**Access.** arXiv full texts were downloaded to a scratch directory outside the
repository and read as text; no PDF is committed. **Balaban's CMP papers (all
of 95-122) are behind a bot check at Project Euclid and a paywall at Springer
from this machine; per the rules I stopped there.** Everything said below about
the inside of CMP 122a/b comes either from the abstracts or from secondary
accounts (the outline's own page citations, Dimock's remarks), and is labelled
so. A reader with library access should check those page claims first.

**Other news.** OpenAI announced on 2026-10-26 a claimed existence proof for
four-dimensional Yang-Mills (with a Lean formalisation reported done
2026-10-16). Nothing of it is public: per news reports the artefacts are
withheld pending a review panel. It gives us nothing to read or credit. The
Sussman-Alpoge README refers to it and says their work continues.

## 1. What the main sources do with large fields (one paragraph each)

Line numbers are lines of the named text file. Page numbers of arXiv papers are
pages of the arXiv PDF.

- **Balaban, CMP 122a (1989, 175-202) and 122b (1989, 355-392).** The only
  published R operation for gauge fields. Not readable here (bot check). From
  the abstracts: 122a "construct[s] the renormalization operation of the
  expressions connected with the large field regions", and 122b "conclude[s]
  the discussion of the basic properties and bounds for the R operation",
  completing UV stability of the 4D pure gauge theory "as formulated in
  Theorem 1". The outline's own description of what Balaban does, with page
  numbers, is at outline l. 17288-17316 and l. 17784 (paraphrased in Sections
  2 and 5 below). **We have not checked those page claims.**
- **Balaban, "The large field renormalization operation for classical N-vector
  models", CMP 198 (1998) 493-534**, with the N-vector series (CMP 167, 182,
  196) before it. A second, later published R operation, for a model whose
  field is compact like a gauge field. The abstract says it "improves the
  bounds" on large-field densities so that the inductive hypotheses can be
  proved. Paywalled here. It is the closest published thing to the R operation
  that is not 122a/b, and anyone with access should read it next to 122a/b:
  it is written ten years later and may be more explicit on the cases that
  122a p. 183 leaves out.
- **Dimock, "The renormalization group according to Balaban" I-III**
  (arXiv 1108.1335, 1212.5562, 1304.0705; Rev. Math. Phys. 2013, J. Math. Phys.
  2013, Ann. Henri Poincaré 2014). These are expository, for scalar phi^4_3,
  with complete proofs. The large-field regions are **nested and decreasing**,
  Lambda_0 ⊃ Omega_1 ⊃ Lambda_1 ⊃ ... ⊃ Omega_k ⊃ Lambda_k (II, eq. (145), p. 20).
  They are separated by 5[r_j] layers of cubes, with r_k = (-log lambda_k)^r
  (II, (147)-(148)). II, Remark 3 after Theorem 3.1 (p. 31) says: "in
  Balaban's models these R_k terms get additional contributions from a
  recycling operation that converts some large field contributions back to
  small field contributions (the 'R-operation'). This difficult step is not
  necessary for this model."
- **Dimock, QED_3**: scalar QED (arXiv 1502.02946, JMP 2015), "Ultraviolet
  regularity for QED in d=3" (1512.04373, JMP 2018), "Multiscale block
  averaging for QED in d=3" (1712.10029, 2020), and "Ultraviolet stability for
  QED in d=3" (2009.01156, AHP 23 (2022)). A complete large-field analysis for
  an **abelian gauge field in Balaban's formalism**. Again the regions are
  nested and decreasing (2009.01156, l. 155 and Appendix A), with no R
  operation. 1712.10029 Section 3 gives a readable re-derivation of Balaban's
  multiscale gauge-field Green's functions and minimisers on nested regions
  (see S2).
- **Sussman-Alpoge YM3_I** (`YM3/YM3_I.tex`, same repository and commit). It
  has a written large-field history sum for SU(2) YM_3: Section "Summing the
  large-field histories", l. 62325-62848. The regions only grow:
  Z_t ⊂ Z_{t+1} (l. 62425). Nothing is healed or dropped out. No R operation
  occurs in YM3_I, YM3_II, YM3_main, QED3 or QCD3_M1/M2 (grep for R operation,
  drop-out, healed, genealogy: no hits).
- **Sussman-Alpoge "complete account of Theorem 0"**
  (`theorem_0_complete_account_raw_{I,II,III}.tex`, about 424,000 lines,
  same commit). This is a longer raw YM4 text than the 500-page outline and has
  fuller versions of several Package C items. It labels its own gaps:
  "Stated; proof incomplete", "Proof outstanding". It is relevant to S3 and S4
  (below) and was **not** read through, only located by grep.
- **Magnen-Rivasseau-Sénéor, "Construction of YM_4 with an infrared cutoff",
  CMP 155 (1993) 325-383** (TeX on mp_arc 92-38, readable). This is a
  continuum phase-space expansion with a regularised axial gauge. Large-field
  regions are made rare by "the positivity of the axial gauge at large field",
  and are dressed by background-dependent propagators and a determinant that
  they control (TeX l. 120-170). Because of the infrared cutoff they never
  face large-field volume growing over infinitely many coarser scales, so they
  have no analogue of R, of healing or of a genealogy count. They remark that
  their solutions "reinforce our belief that [Balaban's] solutions are
  correct".
- **Balaban-Feldman-Knörrer-Trubowitz**, bosonic many-body (arXiv 1609.00968,
  AHP 2017, and companions). They say a factor per point of the large-field
  region is "reasonable" but **not proved**, and that large-field control "is
  still to be completed". This is a negative data point: outside Balaban's own
  gauge and N-vector papers, nobody has published a recycling-type
  large-field step.
- **Other projects in the Sussman-Alpoge README.** `pmaronow/3d-ym-torus`
  (Aronow-Lopatto, 3D SU(2) on a torus, Balaban methods; README points to a
  newer five-part version, "2610.00506-2610.00512", whose server I did not
  identify or read). `marikgoldstein/scalar-qed-existence` (King's U(1)
  Higgs_3 programme). Both are superrenormalizable and three-dimensional. From
  their READMEs, neither discusses an R operation. Not read further.
- **Probabilistic and stochastic-quantisation work** (Chatterjee's survey;
  Cao-Chatterjee; Chandra-Chevyrev-Hairer-Shen, arXiv 2202.13359; the 2D
  Yang-Mills measure papers) and **Bauerschmidt-Brydges-Slade** (large-field
  regulators for unbounded spins). None of it has a statement on large-field
  regions of 4D lattice gauge RG. **Null result** for all four lanes; recorded
  so that nobody repeats it.
- **Older constructive work.** Balaban credits "Gallavotti and co-workers" as
  the nearest earlier idea of R (outline l. 17290; this is presumably
  Benfatto-Cassandro-Gallavotti-Nicolò-Olivieri-Presutti-Scacciatelli, CMP 59
  (1978) and CMP 71 (1980), for scalar fields). Also Federbush's phase-cell
  Yang-Mills series, and Gawedzki-Kupiainen. Located only, not read; none is
  known to contain a statement of the four kinds below.

## 2. S1, `sa-floor`: floor screening and renewed tests

**Statement** (sa-map Section 5, Lane 1). A component X is treated by R at
level m with preparation bottom m_flat, an old floor F and a waiting collar.
Take any field compatible with the stored variables and **arbitrary inside F**.
If the unspent energies in X^+ \ F are below c l_m^{2p_1-8r}, then every test
of the operation passes. In particular, outside F,
|d U-hat(p) - 1| <= C(varsigma + R_m^2 eps_m e^{-delta_0 M R_m}) L^{-2j(p)}
(outline l. 18334-18415, display "floor-screening").

**Closest published statements.**

1. *Balaban avoids the statement.* According to the outline (l. 17300,
   unchecked), CMP 122a pp. 181-183 "removes from the region on which R acts
   any component in which a test of some stage fails", and 122b (1.102) keeps
   T_k(Y) where the last test fails. On that account Balaban never re-tests a
   component that has an old large field inside it, and the outline's "three
   fates" (healed, island, drop-out, with renewed tests after a drop-out) are
   its own addition (l. 17300 lists them among the things it "must prove").
   **No published statement of renewed tests beside an old floor was found.**
2. *Dimock and YM3 avoid it too.* In Dimock I-III, Dimock QED_3 and SA YM3_I,
   the large-field regions are monotone (they shrink in Dimock, grow in YM3).
   A region once large is never tested again, so there is no old floor inside
   a newly tested window.
3. *The analytic core has a published scalar and abelian analogue.* Dimock II
   Section 3.1.6 (pp. 23-24, eqs. (168)-(174)) replaces the background
   phi_{k,Omega} by a field phi_{k,Omega(Lambda*_k)} built on a buffer of
   [r_k] layers. By construction it "depends only on Phi_k", that is, it does
   not read the fields of the old large-field region. The difference is put in
   the "tiny remainder" R_{k,Pi} of Theorem 3.1 (item 6) and paid by decay
   across the buffer times the crude large-field bound on the outside fields.
   Dimock QED_3 (2009.01156) does the same for an abelian gauge field. Its
   random-walk expansions are built from local inverses
   S_{k,Omega}(box, A) that "only depend on A in Omega_1(box) ∩ Omega_1"
   (1712.10029, Lemma 6, p. 14). That locality is exactly what lets an estimate
   ignore the field beyond a collar. Of these, only the decoupling-by-buffer
   device is published. The non-abelian, nonlinear stage background beside an
   **arbitrary** SU(2) field in F is not.
4. *The minimiser in a box.* Outline Prop 2.4 cites Balaban 122a
   Proposition 1 (a box minimiser with exterior data within eps of 1, Hessian
   >= cM^{-5} in axial gauge). The hypothesis is small exterior data. The floor
   claim needs the opposite: no hypothesis on F, and a collar of fixed width
   in place of smallness there.
5. *Continuum analogue (method only).* Small-energy regularity for
   Yang-Mills connections is local. Uhlenbeck (CMP 83, 1982), and Råde and
   Groisser-Parker on annuli (as reported in arXiv math/9903021 and
   2609.16655; originals not read), give curvature bounds on an annulus of
   small energy whatever lies inside it. This supports the outline's sentence
   "it does not require a small field inside the floor" for critical points. It
   says nothing about the constrained, averaged stage background.

**Proof accessible?** Dimock's buffer device: yes, arXiv, complete. Balaban
122a/b: not from here. The outline's own text is a sketch (one paragraph per
claim).

**What it changes about the lane.** The lane should not look for a published
proof: there is none. Two concrete reuses shorten it. (a) **Rewrite the
floor-screening display as a Dimock-type decoupling.** Define the stage
background on a buffer so that it reads no variable in F (Dimock II (168)-(170)
with the old floor in the role of the old large-field region), and move the
difference into a remainder paid by e^{-delta_0 M R_m}. Gauge fields are
bounded, so the "crude bound on the outside field" that Dimock needs is free;
what is needed is that the buffer's random-walk expansion converges with
local inverses that do not see F. Dimock 1712.10029 Lemmas 5 and 6 are the
template. (b) The kill tests of sa-map Lane 1 stay as they are. In particular,
(b) a Z_2 vortex sheet whose Dirac 3-chain cannot be chosen inside F is not
addressed by any source found: Dimock's models are abelian or scalar, and
YM3_I never re-tests. That test should run first.

## 3. S2, `sa-seam-response`: healing across seams, layered background response

**Statement** (sa-map Lane 2). On a separated nested sequence (Omega_j) of any
depth k, with several seams (the outline's "seams" are the boundaries
d Omega_{j+1} between consecutive layers, l. 9599), at V_0 = 1, the Landau-pair
response to a unit datum at a top bond c decays as C(L) e^{-c delta_0 d_B(y, y_c)}
in the layer-weighted norms, with C and delta_0 independent of k, the regions
and the volume. The nonlinear form between two critical backgrounds then
feeds (REL-D) and the ten-term R_X of Prop 2.8.

**Closest published statements.**

1. **Balaban, CMP 96 (1984) 223-250**, "Propagators and renormalization
   transformations for lattice gauge theories II", with CMP 95 (1984) 17-40.
   Multiscale propagators G_{k,Omega} and minimisers H_{k,Omega} on nested
   sequences of regions, with random-walk expansions whose decay is in the
   multiscale distance d_Omega. The constants are uniform in k because they
   are the constants of Balaban's induction. The outline itself uses 95
   ((1.103), Prop 1.2, (1.110)) for the **single-region** decay of H_j
   (l. 26141). It cites 96 only for Balaban's reading of "bonds of Lambda_j"
   (l. 9625). Its raw account takes "the block size M of the propagator papers
   and the gap number R_1" and "[B-CMP96, Lemma 2.1]" and "(2.59)" as inputs
   to its order of constants (raw I, l. 19391-19449). So the multiscale
   version is in the literature, and the SA texts already lean on it, but the
   500-page outline does not state it as the source of A3.
   **Not readable here.**
2. **Balaban, CMP 99 (1985) 389-434** (propagators in a background field)
   and **CMP 102 (1985) 277-309** (the variational problem and background
   fields). These are the non-abelian, background-field and nonlinear versions
   on the same nested sequences, the published counterpart of the second half
   of Lane 2 (the response between two critical backgrounds, and the minimiser
   identification). Not readable here.
3. **Dimock, 1712.10029, Section 3.7** (pp. 38-40). This is a readable, complete
   re-derivation for an abelian gauge field in d = 3 on nested
   Omega_1 ⊃ ... ⊃ Omega_k. The Landau-gauge multiscale minimiser is
   A_{k,Omega} = H_{k,Omega} A_{k,Omega} (Lemma 12; (236)). Its kernel obeys
   |H_{k,Omega}(b, b')|, L^{-(k-j)} |d H_{k,Omega}(b, b')| <= C L^{3(k-j')} e^{-gamma d_Omega(b, b')}
   for b in delta Omega_j and b' in delta Omega_{j'} ((301)). Summed, this
   gives the layer-weighted sup bound (303). The proof goes through a random
   walk for G_{k,Omega}, then local inverses N_{k,Omega}(box) of
   Q G Q^T with a convergent expansion (296)-(300), then their composition.
   Dimock credits Balaban [5]-[9], [11] (CMP 95, 96, 98, 99a, 99b, 102b).
   Lemma 2.1 of Balaban CMP 96 is the convolution inequality for d_Omega that
   absorbs L^{|j-j'|} (1712.10029 (97)). Dimock also proves local regularity
   of these minimisers (Theorem 1, p. 43, (327)): constants depending only on
   L, any k.
4. **The outline's own identification.** Outline (1b), Remark after
   Theorem 3 (l. 9700 ff.): the Landau pair (H, u) and the comb-slice pair
   (A^c, h) are gauge transforms of each other. They are **equal at
   V_0 = 1**, and "R^c is the projection that belongs with Balaban's
   propagators". At the flat background, therefore, the Lane 2 response is
   the comb-slice (Balaban) multiscale response, up to the outline's node
   conventions. It omits inward bonds at every level, and states that this
   agrees with CMP 96 (2.3) read on bonds, l. 9625.
5. **Dimock II, Theorem 2.2** (p. 18). The scalar multiscale Green's function
   on nested regions has a random-walk expansion and bounds
   C L^{-2(k-j')} e^{-gamma_0 d_Omega(y, y')/4} on value, gradient and Hölder
   derivative. This is the simplest complete model of the argument.
6. **MRS, CMP 155** (TeX l. 140-160). A background-dependent gauge and
   propagator for fine small-field regions sitting under coarse large-field
   boxes, with the determinant of the change of normalisation controlled. It
   is a published continuum analogue of the "dressing" that a healed component
   undergoes. It uses a different mechanism and does not apply directly.

**How close.** The linear flat statement of Lane 2 is, up to the outline's
centred blocks, nodes and weights, the multiscale kernel bound of Balaban
CMP 96, and Dimock (301)-(303) is the same theorem in d = 3 for U(1). The
dimension enters only through the volume factors L^{d(k-j')} and the
convolution lemma. **Healing** proper (Prop 2.8's ten-term R_X and Prop 2.10's
resummation) has no published counterpart outside Balaban 122a/b.

**What it changes about the lane.** (a) Its kill test should be aimed at the
one place where the outline differs from Balaban: the Landau-pair gauge with
node factors at junction nodes and the projection R in place of R^c. At V_0 = 1
these coincide (outline's Remark), so a depth-growing counterexample at the
linear flat level would contradict Balaban CMP 96 and Dimock (301). That makes
it unlikely, and the lane can **prove** the flat linear statement by porting
Dimock 1712.10029 Section 3.7 to d = 4 and SU(2) at V_0 = 1 (three abelian
copies), with credit, instead of searching for a counterexample there. (b) The
real open content moves to the curved, nonlinear part: the response between
two critical backgrounds, and the identification of the iterated trial with
the class minimiser. The literature for that is Balaban CMP 99 and 102b
(inaccessible here). Our Example E of `library/rel-phi-c.md` is a statement
about one gauge. Before the lane uses (REL-D), it should check whether
Balaban's multiscale Landau gauge, which Dimock writes as a minimiser of
||delta A||^2 under the constraints (1712.10029 l. 3554), is a gauge in which
Example E's contour averages stay bounded. That is share-check item (b).

## 4. S3, `sa-order`: one simultaneous order of constants

**Statement** (sa-map Lane 3). Every condition on constants stated anywhere in
the outline admits one simultaneous choice in the order of l. 19465-19470
(C4, Theorem 2.11). Decide ACYCLIC, with the choice, or name the first circle.

**Closest published or written statements.**

1. **Sussman-Alpoge raw account, Chapter 2, Sections 2.2-2.4**
   (`theorem_0_complete_account_raw_I.tex`):
   - Definition (H1)-(H7) (l. 1126);
   - Definition of caps (l. 1246);
   - the stage notations 2.3;
   - **Lemma "The order of choice has no cycle and is one-sided (no caps)"**
     (l. 1958). Its proof is by attaching each condition to the latest letter
     it reads, (P1)-(P2);
   - **Proposition "The conditions of Theorem 0 can be met"** (l. 2271).

   This is the statement Lane 3 asks for, already written by the same authors
   for a longer YM4 text. Its own labels: it assumes **(A1)**, "Consistency
   of the displayed order with hypothesis (H3) (stated; proof incomplete)".
   The enumeration fails only at the constants (B_W, delta_W) and mu_0 of two
   kernel estimates. It also assumes **(A2)**, "M-independence of the
   random-walk constants (stated; proof incomplete)": M-independence "is
   proved for the kernel estimates on the whole lattice; what is missing is
   the local version, on the one family of cells". One Stage-0 window opens
   on the unproved inequality kappa' > 5/12, which is "not a condition of
   Theorem 0" (l. 1395, 1903). The raw account also has per-chapter order
   remarks (raw I l. 19375, 60718, 61439, 125065, 151763, 163075; raw II
   l. 25480, 33314, 48614; raw III l. 40764, 45744, 63930), and
   "A coupling ceiling implying every floor" (raw I l. 166227).
2. **Sussman-Alpoge YM3_I, Proposition II-202-29, "A common choice of
   constants"** (l. 63071 ff.). This is the 3D analogue, stated with a written
   proof: integer exponents r >= 2 and p_0 >= 6r + 1 first, then geometry
   and radii, then the regular-term bounds, then the coupling last. Its
   history sum needs 2 p_0 > 3r + 2 or 2 p_0 > 4r + 1 (l. 62571 ff.).
3. **Dimock II, Theorem 3.1** (p. 31), and III. "L sufficiently large, M
   sufficiently large (depending on L), lambda_k sufficiently small (depending
   on L, M)", with integer exponents p, r fixed first. This is the published
   model of the order for a large-field Balaban step. It is short because
   there is no R operation and no healing.
4. **Balaban's papers** each state the order they need (for example L > 11,
   (1 + 7 beta_s) L^{-2} <= 1 from CMP 109, quoted at raw I l. 1915-1918). The
   outline lists "an order of the constants that contains no circle" among the
   things it adds to Balaban (l. 17300), so on its own account no single
   published order covers CMP 109-122 together.

**Proof accessible?** Raw account: yes, but its two key inputs are labelled
incomplete by its authors. YM3_I: yes, a written proof for 3D. Dimock: yes,
complete, for phi^4_3.

**What it changes about the lane.** The lane should **start from raw I
Lemma 2.4 and Prop 2.4**, not from a blank table. Concretely:
- map the outline's order at l. 19465-19470 onto the raw account's stages;
- check that the conditions sa-map lists (2p_1 - Cr > p_0, q > p_0 + 2r,
  2p_1 - 8r > p_0, q - p_0 > 2, kappa_0 > 4, p_R >= 3/2, a rho >= C log L,
  eps-bar <= c(L)/frak-M, c_a >= C(b) log L) appear in the raw account's
  enumeration;
- concentrate on (A1) and (A2). (A2) is a statement we can test: random-walk
  constants of the local kernel estimate on one family of cells, uniform in
  the cube size M. It is the same kind of claim as our `fan-ext` gate's open
  tension (growth near log L on a 3D fan).

A circle, if any, is most likely there: a constant fixed "after M_1 and
before M" whose local proof needs M large.

## 5. S4, `sa-count`: the genealogy count and the label sum with the logarithm

**Statement** (sa-map Lane 4). Outline Prop 2.6 (l. 17719-17793) covers the
count, the ledger and the credit, with the contraction
O(u) ⊂ C(u) ⊂ O(u)^[e] and the count over generations (l. 18475-18604). It
should hold with constants free of the history and the number of steps, and
with it Prop 2.13: C M^4 R-check_t^5 log x_t <= (1/2) c p_0(g_t) pays every
site cost. The case that matters is regions that join repeatedly with no new
creation (Balaban 122b p. 387).

**Closest published or written statements.**

1. **Dimock III, Section 3** (arXiv 1304.0705, pp. 19-23, l. 2249-2800).
   The sum over decreasing region sequences Pi = (Lambda_0, Omega_1, ...,
   Lambda_{N+1}) is rewritten as a sum over **creation sets** P_j, Q_j, R_j
   (unions of cubes) that determine Omega_j and Lambda_j recursively by
   enlargement rules (Omega^c_{j+1} = (Lambda-bar_j)^{c,5*} ∪ P^{5*}_{j+1},
   ...). Each created cube carries the small factor of a failed test. This is
   a complete, published count of large-field histories with monotone
   regions.
2. **Sussman-Alpoge YM3_I, Section "Summing the large-field histories"**
   (l. 62325-62848). This is Dimock's scheme (same names P, Q, R) for SU(2)
   YM_3, with explicit constants:
   - **Prop II-75-45** (l. 62428): later volume is charged to creations,
     sum_n r_n |Z_n ∩ X|_n <= 48^3 sum_t n_t^cr(h; X) sum_{n>=t} r_n. The
     proof is a chain-and-collar geometric argument, dimension 3 (the 48^3
     comes from (44L/(L-1))^3).
   - **Lemma II-75-82** (l. 62505): the entropy of histories with given
     creation sets is at most prod_t 2^{n_t^bit #W_t}.
   - **Lemma II-75-99 and Prop II-75-106** (l. 62592-62705): the gain
     c p_0(g_t)^2 per created cell absorbs volume and entropy, so that
     sum_h F(h) <= prod_t (1 + zeta_t)^{#P_t}.

   Every step is written out and readable by hand. The regions grow
   monotonically (Z_t ⊂ Z_{t+1}), so **joins happen, but there is no healing,
   no drop-out and no renewed wait**. The joining problem of Balaban's p. 387
   does not arise.
3. **Balaban 122b pp. 384-387** (through the outline, l. 17784, unchecked).
   He proves (1.80) by induction on j and, inside a step, on the number of
   regions that join. On a join he frees the reserve
   2p_0(g_{j(X)}) + 2p_0(g_{j(Y)}) - 2p_0(g_{j(Z)}) >= c p_0(g_j) to pay
   for the renewed wait. This rests on a containment claim on p. 387 ("after
   n_1 further hull operations, n_1 < 10, ..."), which the outline says can
   fail depending on grid position, and it gives a one-coordinate example.
   This is the only published treatment of joins with healing. Not readable
   here.
4. **Sussman-Alpoge raw account.** Raw I Section 4.15:
   - "Creation cubes along histories without large-field actions" (l. 51129);
   - "The waiting rule" (l. 51178), k - s >= N_k;
   - "Every top large-field component contains a creation cube" (l. 51845),
     conditional on two descriptions of regions (a), (b);
   - Section 4.18, "graded count" (l. 55608).

   Raw II Section 8.6 labels several of the needed steps as open in its own
   words:
   - "Later steps do not read earlier healed islands. Stated; proof
     incomplete at the step marked (*)" (l. 103387);
   - "Conditional rarity of simultaneous creations. Proof outstanding"
     (l. 106171);
   - "Survival bound for long-lived creations. Proof outstanding"
     (l. 106818);
   - "Translation covariance of the label histories. Stated; proof incomplete"
     (l. 107738).

   It explicitly does **not** use "the argument of [B-CMP122b, p. 387]",
   (1.76) or (1.84) (raw II l. 14624-14628).

**Why the 3D count does not transfer as it is (my reading, unchecked).** In
YM3_I the remaining number of steps is bounded by the log-coupling,
K - j + 1 <= y_j = log x_j (Lemma II-75-37), because the 3D coupling is
superrenormalizable (x_{j-1} = L(x_j + b_j)). So the charge for later volume,
sum_{n>=t} omega_n (M R-check_n)^3, is polylogarithmic in x_t, and
p_0(g_t)^2 absorbs it (Lemma II-75-99). In 4D the inverse coupling changes
only by about b (the one-loop coefficient) per step, so the number of
remaining steps K - t can be of order x_t / b = e^{y_t} / b. A created cell that stayed large
for all later steps would cost about x_t times a polylog, and no polylog gain
p_0(g_t) pays that. This is why Balaban needs R: a component must stop
costing after a wait of order R-check_t, polylogarithmic in x_t. It is also
why the outline's site budget is C M^4 R-check_t^5 log x_t (wait times
volume times site cost) against p_0(g_t). Healing and joining are the only
genuinely new ingredients beyond Dimock III and YM3_I.

**Proof accessible?** Dimock III and YM3_I: yes, complete for monotone
regions. Balaban 122b: not from here. Raw account: located, partly labelled
incomplete by its authors.

**What it changes about the lane.**
- (a) **Port, don't rebuild, the monotone part.** YM3_I Lemma II-75-82
  (entropy) and Prop II-75-45 (volume to creations) are dimension-generic up to
  constants: 48^3 becomes (44L/(L-1))^4 < 48^4, and the six bonds per site
  become eight. They can be re-derived in `library/` with credit for d = 4.
  The lane's own work then reduces to **the healing and joining case**: a
  bound on the number and the cost of renewed waits per created cell,
  uniform in the number of joins.
- (b) The kill test of sa-map Lane 4 (two old regions that join repeatedly
  with no new creation) is exactly the case that raw II l. 103387 and 106818
  leave open. The lane should read those two statements first, since they are
  the authors' own nearest attempt.
- (c) The arithmetic C M^4 R-check_t^5 log x_t <= (1/2) c p_0(g_t) is a
  polylog-against-polylog inequality: with R-check_t ~ y_t^r it needs
  p_0 > 5r + 1 in the exponents. It belongs in S3's table.

## 6. Summary per lane

| Lane | Closest published | Closest written by SA | How close | Proof accessible here | Change to the lane |
|---|---|---|---|---|---|
| S1 `sa-floor` | None for renewed tests. Balaban 122a pp. 181-183 removes failed components instead (via the outline). Dimock II Sec. 3.1.6 decouples by buffer (scalar); Dimock QED_3 (abelian) | Outline l. 18334-18415 only (a sketch) | Analytic core: scalar and abelian analogue. Renewed-test logic: nothing | Dimock: yes. Balaban: no | Restate the screening as a Dimock-type decoupled background plus remainder; run the Z_2 vortex-sheet kill test first, since no source touches it |
| S2 `sa-seam-response` | Balaban CMP 95, 96 (multiscale propagators on nested regions), 99, 102b (background, variational); Dimock 1712.10029 Sec. 3.7, (301)-(303) for U(1), d = 3 | Outline (1b) Thms 3-4; Remark: Landau pair = comb pair at V_0 = 1 | Linear flat statement: essentially published (Balaban 96), with a readable d = 3 abelian proof | Dimock: yes. Balaban: no | Prove the flat linear statement by porting Dimock Sec. 3.7 to d = 4; move the kill effort to the curved nonlinear response and to gauge choice (Example E) |
| S3 `sa-order` | Dimock II Thm 3.1 (order without R); Balaban's per-paper orders | Raw I Lemma 2.4 (no cycle) and Prop 2.4 (conditions can be met), conditional on (A1), (A2), both "proof incomplete"; YM3_I Prop II-202-29 | Same statement, already written, with two named holes | Yes (SA texts) | Start from raw I Sec. 2.4; check the inventory against the outline's conditions; attack (A2), local M-independence of random-walk constants |
| S4 `sa-count` | Dimock III Sec. 3 (sum over creation sets P, Q, R; monotone); Balaban 122b pp. 384-387 (joins with healing, via the outline) | YM3_I Props II-75-45, II-75-106, Lemma II-75-82 (complete, 3D, monotone); raw I Sec. 4.15; raw II Sec. 8.6 (healed islands, survival: "proof outstanding") | Monotone part: complete in 3D and transfers; healing and joins: only Balaban, and he relies on the p. 387 sentence | Dimock and YM3: yes. Balaban: no | Port the monotone count to d = 4 with credit; the lane is then only the renewed-wait count under repeated joins; read raw II l. 103387 and 106818 first |

**One-line reading for `route-compare`** (row 73), not a decision. Of the four
outline obligations, S2's linear part and S4's monotone part have published
or written proofs to port. S3 has an SA-written statement with two named
holes. S1, and the healing and joining half of S4, have no published proof
except Balaban 122a/b. So on the outline's route the large-field position
stands or falls on the R operation itself. The literature offers no
alternative: every complete published large-field analysis (Dimock I-III,
Dimock QED_3, SA YM3_I, MRS with IR cutoff) is superrenormalizable or
IR-cut-off, which is exactly the case where R is not needed.

**Side finding for row 67 (`annular-reset`, our (AR)).** This is method
only, not part of this item. The continuum analogue of (AR) is the
small-energy theory of Yang-Mills connections on annuli: Uhlenbeck's gauge
and removable singularities (CMP 83, 1982), and the Donaldson and Råde annulus
decay estimates, as cited in arXiv math/9903021. Those are for critical
points. (AR) is for an arbitrary connection of small action, so only
Uhlenbeck's gauge-fixing half applies. Our `library/lattice-uhlenbeck.md` is
the lattice version of that half. Not searched further.

## 7. What was read, what was not, limits

Read (as text, by grep and section): Dimock II Sections 1, 3.1 (pp. 1-24),
Theorem 2.2, Theorem 3.1 with remarks (pp. 30-31); Dimock III Section 3
heads (pp. 19-23); Dimock 1712.10029 Introduction, Lemmas 5, 6, 11, 12,
Section 3.7.2, Theorem 1 statement; Dimock 2009.01156 abstract, end of the
paper and Appendix A; BFKT 1609.00968 via search summary only; MRS 92-38 TeX
l. 120-170, 525-590, 955-990. In the SA repository at `31a47c543775`: README;
outline l. 9055-9075, 9599, 9625, 9693-9745, 17288-17316, 17566, 17656-17662,
17784-17790, 18334-18415, 26141, the bibliography; YM3_I l. 755-800, 940-962,
62325-62706, 63071-63110; raw I l. 1126-2345 (parts), 19375-19449,
51129-51200, 51845-51870, and grep lists of statements; raw II
l. 14600-14640 and grep lists. In this folder: FINISH.md, GOAL.md,
`library/sa-map.md` (Sections 0, Package C, 4, 5, 6).

Not read: Balaban CMP 95-122 and 198 (bot check at Project Euclid, paywall
at Springer; the rules say stop there). Dimock I; YM3_II; QED3; QCD3;
Aronow-Lopatto; Goldstein; Federbush; Gawedzki-Kupiainen; BCGNOPS; Råde;
Uhlenbeck. The raw account beyond the lines listed.

Limits. This is a search, not a check. No statement here was re-derived. Every
claim about the inside of Balaban 122a/b is the outline's, not ours, and
should be checked first by anyone with library access. "Transfers to d = 4"
in S2 and S4 is my reading of the arguments' dimension dependence, not a
proof. No numerics were run (memory was 59 percent free at the start; no job
needed). Scratch copies of papers and of the SA repository are in /tmp,
outside the repository; nothing was committed.

Status: finished 2026-11-02.
