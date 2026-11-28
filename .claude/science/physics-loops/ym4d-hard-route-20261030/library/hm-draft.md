# H-M: the actual Gaussian matrix envelope (pass 1, long draft)

Provenance: Claude (Opus 5.5, `claude-opus-5-5`), pass 1 of the draft / distil / referee cycle, 2026-11-04, written in the clone at `57d99099f97c`. Sussman–Alpoge sources at `31a47c543775`; the local copy of the outline has SHA-256 `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f`, which matches the pin. Research text, not an audit; it grants no status. Not distilled, not refereed, not checked by the other model.

Credits. **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**: the collared Gaussian and its reference (SA 14160–14210), the local Gaussian comparison FG1–FG12 (SA 13894–14270), the unmarked majorant UM1–UM30 (SA 14276–14816), the hereditary core R4–R8 (SA 5663–5755), and the three-dimensional actual-structure theorem with its local resolvents, strings and localization (YM3 39839–40569) and its early cost choice (YM3 43564–43604). **Tadeusz Balaban**: the background-field method, cut-down local inverses and random-walk expansions, used through `h-walk.md`. **Jonathan Dimock**: the parametrix template used in `h-walk.md`. **Codex**: the grouped resolvent / inverse-root series of `inv-root.md`, reused here in local form, and `um-envelope.md`, `pr-lay.md`. **Claude**: `h-walk.md`, `carrier-adopt.md`.

SA = the pinned outline `YM4_sketch_500.tex` (local copy `ym4.tex`); YM3 = `YM3/YM3_I.tex`. Line numbers are those of the pinned raw files. All arguments are hand proofs. No step uses a computation.

---

## 0. Result in brief

**What is proved here.** Theorem HM (§9–§10) proves every clause of IN1's H-M for the actual collared matrices of the step: the matrices of SA 14164–14170, with the precision decoupled by hull tags and the inverse root given by the explicit grouped series of Definition 7.4. The estimate holds on every triple of the declared hereditary core (SA R4), with **local** real factor and **local** complex potential and current; it does not assume a global field. The constants \(K_0,H_0,d,C_\tau\) are fixed before \(\kappa,\bar\kappa,M\); \(b=32\); \(H_p\equiv L^3\) is a constant. Heredity, wall factorization, normalization, holomorphy on \(|s_\Delta|\le e^{\bar\kappa}\), the local dimension bound and the Schur identity at \(s=1\) are proved (Theorem C).

**Status of each piece.**

| Piece | Status |
|---|---|
| Lemma 0 (core radii to local-class radii) | Proved here (unit bookkeeping). |
| Lemma 1 (local-class form of h-walk (H2)) | Proved conditionally, **by reading** h-walk's chain proofs; h-walk states (H2) only at global regular pairs. |
| Lemma 2 (complex line, Lipschitz) | Proved here; the cited pr-lay proof is plaquette-local. |
| Lemma 3 (box extension of a local real field) | Proved here, from the import (I2) and the reading (Ax) of "block axial". |
| Lemma 4 (real gap at a local real factor) | Proved here, from R, Lemmas 1 and 3 and a localization (IMS) identity. |
| Lemma 5 (complex gap, ball gaps) | Proved here. |
| Theorem A (local inverse-root series) | Proved here; local form of inv-root §§3–4. |
| Theorem B (the envelope (9)) | Proved here. |
| Theorem C (structure) | Proved here; the physical clause uses the import G-ID. |
| Consequence for UM (§13) | IN1 Lemma 3 applies: (UM4)–(UM6), (UM14) and \(C_0^{\rm UM}\le1\), with \(W_0\) fixed before \(M\). |

**Imports retained (not proved here).** R (the real layered gap of pr-lay §2, from a2-layers Theorem A); h-walk Theorem H with its inputs (I1)–(I3); Balaban's gauge covariance of the averages (I2); the reading (Ax) that the step's representative condition is a blockwise axial gauge; G-ID, the identification of the step's Gaussian precision with \(\mathsf A(P_W)\) (SA 14108–14118, sketched there; pr-lay (9) keeps it separate).

**Outstanding inside H-M:** none beyond these imports. **Outside H-M:** admission of the program's actual chain domains into SA cores with the small radii used here is pr-lay's D (Outstanding there; it is not part of H-M's statement).

---

## 1. The target as frozen IN1 imports it

IN1 states H-M at `in1.md` lines 99–106 and its Outstanding note at line 108. I restate it in clauses, without change of content.

For the actual localized Gaussian functional and its actual carriers, on every disc \(|s_\Delta|<e^{\bar\kappa}\):

- **(M1)** the covariance datum \(C\) is complex symmetric and \(\Gamma\) is rectangular;
- **(M2)** there are real \(C_*,\Gamma_*\), \(C_*\) symmetric positive definite, with \(\|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0\);
- **(M3)** \(\|C-C_*\|+\|\Gamma-\Gamma_*\|\le H_0\{e^{b\bar\kappa-dM}+H_p(M)(a_0+a_1+j_0)\}+C_\tau|\tau-1|\) (IN1 (9)), where \(K_0\ge1\) and \(H_0,b,d,C_\tau>0\) precede \(\bar\kappa,M\), and \(0\le H_p(M)<\infty\) may follow \(M\);
- **(M4)** the functional is normalized;
- **(M5)** it is hereditary in its declared carriers;
- **(M6)** it is wall-factorizing;
- **(M7)** it is holomorphic on these discs;
- **(M8)** it agrees at physical parameters with the actual fluctuation law;
- **(M9)** its local dimension is at most \(c_m(LM)^4\) per cube.

H-M also imports FG1–FG11 (SA 13904–14089) and the UM counts (SA 14276–14811); those are SA's theorems and are not reproved here.

The Outstanding note (line 108) says: Lemma 2 of IN1 proves (9) for an auxiliary path-weighted construction under a **global** gap, but it does not identify that construction with H-M or prove heredity; and the enlarged-disc estimate with early constants remains an actual-construction obligation. The note points at `carrier-adopt.md` §6 and `inv-root.md`. IN1 lines 329–334 give a three-site chain on which Lemma 2's local covariance depends on an exterior edge.

The task is therefore: define the actual collared family exactly, and prove (M1)–(M9) for it, on the declared cores, with the stated constant order.

---

## 2. What the sources prove and assume

Each entry quotes at most a few words and gives the lines read.

| Lines read | Content | Status there |
|---|---|---|
| SA 13894–13990 (FG1–FG6) and IN1's citation 13904–14089 | Abstract comparison: real references, \(\|C-C_0\|+\|\Gamma-\Gamma_0\|\le\varepsilon\), \(D=C+C\Gamma\Gamma^{\mathsf T}C\), \({\cal J}[F]=\int F\,d\mu_D\), \({\cal J}[1]=1\), cost \(e^{A_K(\varepsilon+\rho)m}\) independent of the auxiliary dimension. | Proved in SA (a theorem with proof). Used here as an import, as IN1 does. |
| SA 14091–14118 | Defines \(\mathsf A(P)\) (14096–14102). At the background pair the form is "the Hessian on the fibre"; "the Gaussian of the step is \(C^{(k)}=\mathsf A(P_W)^{-1}\)" (14117–14118). | Sketched. This is G-ID. |
| SA 14120–14157 | Flat bound, local real gauge with \(a_{\rm w}=CLMa_0\) (14129), localization formula with double commutator (14133–14140), gap \(\tfrac12\gamma_0\) (14146), "Every compression inherits this gap" (14149–14150), inverse root by the resolvent integral (14152–14157). | Sketched. The comparison with the flat operator "in this gauge" (14130–14131) uses gauge covariance of the form, which the 4D precision lacks (h-walk (H3); §11 below). |
| SA 14158–14210 | \(C(Z_0;s)=(\chi\mathsf A(s)\chi)^{-1}\), \(\Gamma(Z_0;s)=-\chi\mathsf A(s)(1-\chi)\mathsf r(s)\) (14164–14166); \(\mathsf r(s)\) is "the decoupled inverse-root series" and not \(\mathsf A(s)^{-1/2}\) (14168–14169); references at \(s=0\), \((U,0)\) (14175–14176); perturbation \(C(e^{-cM}+LMa_0+a_1)\) (14187–14190); \(\tau\) adds \(C|\tau-1|\) (14196–14198); "Far from \(Z_0\) the mutilated form need not have a gap" (14202–14203); Schur identity at \(s=1\) (14207–14210). | Sketched; the decoupled series is not written. |
| SA 14219–14270 | FG12 failed-test tail; Fubini–Morera holomorphy (14237–14243); "The matrix gap and kernel closeness are the actual A2–A3 obligations, which we must prove" (14258–14259); completeness only on complete physical pairs (14262–14270). | FG12 proved; the actual matrix inputs named open. |
| SA 14276–14412 | UM1–UM6. "All bounds below are local" (14286–14287); "No global Gaussian on an arbitrary independent-current pair is assumed" (14288–14290); UM3 terms; UM4 discs \(|s_\Delta|<R_s\); UM5 dimension; UM6 marginal estimate; structural hypotheses "heredity, normalized-functional and wall-factorization identities" (14406–14412). | UM4–UM6 and the structural identities assumed; UM6 follows conditionally from FG. |
| SA 14518–14560 | UM15 cost \(C_0=C_pW_0L^4+A_Kc_m(LM)^4(\varepsilon+C_pW_0M^{-4}+\gamma/2)\) (14524–14528). | Proved conditionally. |
| SA 14659–14816 | Supremum "over the declared local core of \(Z\), not over restrictions of one global field" (14678–14679); hereditary restrictions (14680–14682); the choice paragraph "does not assert them for a matrix family whose constants have not been controlled" (14789–14791). | Proved conditionally; the matrix supply named open. |
| SA 5663–5755 | Triples \((U,A',\mathbf J)\) on \(X\) with \(U\) real; R4 (curvature \(<a_0\eta_j^2\), \(|A'|,|\nabla_UA'|<a_1\), \(|\mathbf J|<a_2\), real gauges with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\) on every box of side \(\le C_{\rm box}LM\)); R5–R6 towers; restriction "without extending them across the boundary" (5738–5739). | Definitions. |
| YM3 39839–39905 | The 3D collared structure (II-38-15) with coefficients tagged "once by each parameter in its domain"; "These expressions require the background only on the union of the surviving domains." | Definition and theorem statement II-38-61. |
| YM3 40140–40300 | Gap transferred "to local backgrounds"; inverse root built "without extending those backgrounds beyond their domains"; Schwarz on a complex disc; cosine partition with \(\sum h^2=1\) and the double-commutator loss; local resolvents \(g_\square\) and strings \(r_\omega\). | Proved in detail in 3D. The transfer of the flat gap uses unitary gauge covariance of the 3D form. |
| YM3 40377–40400; 43564–43604 | Parameters and Schwarz differences of coefficients and strings; \(c_v,c_w\) independent of \(M\). | Proved in 3D; the literal 3D cost has an additive constant, not the bound one. |

Local files read: `in1.md` 1–380 and 640–696; `um-novelty.md` (all); `um-envelope.md` (all); `inv-root.md` (all); `carrier-adopt.md` 1–60 and 160–207; `gates/carrier-check.md` (all); `pr-lay.md` (all); `ci-form.md` 1–60, 129–160, 218–240; `h-walk.md` 10–120, 223–232, 243–345, 354–458; `st1-r3.md` 50–70; `c4-order.md` table rows. `p82.md` is not used: its Theorem P concerns the real constrained inverse \(S_q^\circ\) (pr-lay §5 records this), not the step precision.

Two facts from the local files frame the work.

- `inv-root.md` §§3–5 constructs exactly the needed series and proves um-envelope (6), but its premise is the **global** gap of the full precision at a regular pair (inv-root (10)–(11), "Retain the repaired A2 bounds \(\operatorname{Re}A\ge aI\)"). `carrier-check.md` §6 checks that implication; it does not check local cores.
- `pr-lay.md` Theorem 3 proves the global gap and the Lipschitz bound at **global** regular pairs, and its closing Outstanding note says it does not supply H-M.

So the new content needed is the passage from global pairs to the declared **local** cores, plus the structural clauses. That is what §§3–10 do.

---

## 3. Setting, cores and imports

### 3.1 Geometry

Work at one regular step from level \(k\), in level-\(k\) units on a periodic four-torus \(\mathbb T\). The fine field lives on the bare lattice of mesh \(\eta=L^{-k}\). The step's longer sequence \(\mathbf S=(\Omega_0,\dots,\Omega_{k+1})\) and its layer scales \(\xi_j=L^{j-k}\) are those of pr-lay §1; the point scale of a bond is at most \(\xi_{k+1}=L\), and is \(\eta\) outside \(\Omega_0\).

**Free coordinates.** \(I\) is the set of free coordinates of the step (pr-lay §1: positively stored, non-pivot level-\(k\) bonds touching \(\Omega_{k+1}\), three real colour coordinates each). Each \(x\in I\) has a base point \(\hat x\) in the level-\(k\) unit lattice, and at most \(n_c=12\) coordinates share a base point. Write \(d(x,y)\) for the periodic \(\ell^\infty\) distance of base points. It is an integer, and
\[
 \#\{y\in I: d(x,y)\le t\}\le n_c(2t+1)^4 .                    \tag{3.1}
\]

**Cubes.** Fine cubes have side \(M\) and coarse cubes side \(\ell:=LM\), both aligned half-open blocks in level-\(k\) units, \(M\) a power of \(L\), tiling \(\mathbb T\). A coarse cube is identified with the set of bare sites in it. \(\Lambda\) is the set of coarse cubes. (If UM measures \(M\) in level-\((k+1)\) units, every cube side below is multiplied by \(L\); all floors on \(M\) remain floors and all distances only increase.)

**Collar.** For a union \(Z_0\) of fine cubes let \(\mathcal N_f(Z_0)\) be \(Z_0\) together with every fine cube that shares at least a corner with a fine cube of \(Z_0\). Let \(Z_0^\sharp\) be the union of coarse cubes containing a fine cube of \(\mathcal N_f(Z_0)\). This is SA's collar (SA 14338–14347) with the first layer taken in corner adjacency. SA 14344–14347 allows a fixed number of extra neighbouring layers; the corner layer lies inside four wall layers.

*Remark (why corner adjacency).* With wall adjacency only, a fine cube at a coarse corner has a diagonal fine neighbour whose coarse cube contains no fine cube of the first wall layer. Then sites outside \(Z_0^\sharp\) can lie at distance \(1\) from \(Z_0\), and (G1) below fails.

**(G1)** \(\operatorname{dist}_\infty(Z_0,\mathbb T\setminus Z_0^\sharp)\ge M\).

*Proof.* Let \(p\in Z_0\) lie in the fine cube \(Q\) and \(q\notin Z_0^\sharp\) in \(Q'\). Then \(Q'\notin\mathcal N_f(Z_0)\), since otherwise its coarse cube lies in \(Z_0^\sharp\). So \(Q'\) shares no corner with \(Q\), and the fine indices differ by at least two in some coordinate \(\mu\). Then \(|p_\mu-q_\mu|>M\). \(\square\)

**(G2)** Let \(Z\) be a union of coarse cubes and \(H\subset Z\) a set of bare sites that is nearest-neighbour connected. Then \(H\) lies in one wall-component of \(Z\).

*Proof.* A nearest-neighbour step changes one coordinate by \(\eta\). The coarse cube index then changes by at most one in that coordinate. So consecutive sites lie in equal or wall-adjacent coarse cubes, both in \(Z\). \(\square\)

**(G3)** If \(Y\subset Z_0\) is a corner-connected union of fine cubes, then \(Y\) lies in one wall-component of \(Z_0^\sharp\).

*Proof.* Let \(Q_1,Q_2\subset Y\) share a corner. The fine cubes on a coordinate path from \(Q_1\) to \(Q_2\) inside the \(3^4\) block around \(Q_1\) are consecutive wall neighbours, and all lie in \(\mathcal N_f(Z_0)\). Their coarse cubes lie in \(Z_0^\sharp\), and consecutive ones are equal or wall-adjacent. Induct along a corner path in \(Y\). \(\square\)

**(G4) Tag count.** Let \(T\) be a connected union of straight segments with total \(\ell^\infty\)-length \(l\), let \(R\ge0\) with \(\ell\ge8R\), and let \(H\) lie in the closed \(R\)-neighbourhood \(\mathcal N_R(T)\). Then the number of coarse cubes meeting \(H\) is at most \(16+128\,l/\ell\).

*Proof.* Doubling every segment gives a closed walk covering \(T\) with length at most \(2l\). Cut it into at most \(1+8l/\ell\) pieces of length at most \(\ell/4\); if \(l=0\) take one piece, a point. The \(R\)-neighbourhood of a piece has \(\ell^\infty\)-diameter at most \(\ell/4+2R\le\ell/2<\ell\). A set of \(\ell^\infty\)-diameter less than \(\ell\) meets at most two grid intervals in each coordinate, hence at most \(2^4=16\) coarse cubes. So the count is at most \(16(1+8l/\ell)\). \(\square\)

This is inv-root (18), rebuilt there after SA 10558, with side \(\ell\) in place of \(M\).

### 3.2 The declared cores

**Definition 3.1 (core).** For a union \(Z\) of coarse cubes and radii \(a_0,a_1,a_2>0\), let \(\mathcal K(Z)=\mathcal K_k(Z;a_0,a_1,a_2)\) be the set of triples \(P=(U,A',\mathbf J)\) on the bare bonds of \(Z\), with \(U\) real (\(SU(2)\)) and \(A',\mathbf J\) complex Lie-algebra-valued, such that:

1. SA R4 holds on every read contained in \(Z\), at level \(k\): \(|\partial U-\mathbf1|,|\partial\mathbf U-\mathbf1|<a_0\eta^2\), \(|A'|,|\nabla_UA'|<a_1\), \(|\mathbf J|<a_2\); and every cubical box contained in \(Z\) with side at most \(C_{\rm box}\ell\) carries a real gauge \(g\) with \(U^g=e^{i\eta A}\) and \(|A|,|\nabla A|<C_{\rm pot}Ma_0\) (SA 5671–5690);
2. **(Rep)** \(U\) satisfies the step's representative condition \(\mathrm{Ax}_b\) (§3.4) on every active level-\((k+1)\) block \(b\) whose \(r_M\)-neighbourhood lies in \(Z\).

IN1's radii are \((a_0,a_1,j_0)=(a_0,a_1,a_2)\). SA's hereditary core \(\mathcal U^\circ_k(Z;a_0,a_1,a_2)\) (SA 5722–5726) adds R5–R6; IN1's \(\mathcal D_k(Z)\) adds further data. Both are subsets of the set in item 1. A bound on \(\mathcal K(Z)\) therefore bounds the supremum over those cores.

*Status of (Rep).* SA R4 does not state it. It is needed to define the step's matrices at \(U\) at all, because the precision depends on the gauge representative (pr-lay §1, "Fix the step's real representative"; h-walk (H3), covariance of \(A^{\rm loc}_\kappa\) only under block-constant transformations). Activities are gauge invariant (SA 5729–5733), so the supremum over a core equals the supremum over its triples in the representative. This is a convention, not a new estimate.

Restriction: if \(Z'\subset Z\) is a union of coarse cubes, restriction maps \(\mathcal K(Z)\) into \(\mathcal K(Z')\), because every condition in Definition 3.1 is imposed on reads, boxes or blocks inside the set.

### 3.3 The local class and radius conversion

**Definition 3.2 (local class).** For a set \(Y\) of bare sites and radii \(\alpha=(\alpha_0,\alpha_1,\gamma_0)\), \(\mathcal R_{\rm loc}(Y;\alpha)\) is the set of triples on the bonds of \(Y\) for which the clauses of pr-lay's regular class (pr-lay §1, after (4)) hold on every read contained in \(Y\): \(\eta^{-2}l_p^2|\partial U-I|,\ \eta^{-2}l_p^2|\partial\mathbf U-I|<\alpha_0\) on inner plaquettes, \(l_b|A'|,\ l_b^2|\nabla^UA'|<\alpha_1\), \(l_b^3|\mathbf J|<\gamma_0\); and every cube of side at most \(c_gM_1\xi_j\) contained in \(Y\cap\Omega_0\cap(\mathcal L_j\cup\mathcal L_{j+1})\) carries a real gauge with \(\xi_j|A|,\xi_j^2|\nabla A|<\alpha_0\). Write \(r_Y(P)\) for the maximum of pr-lay (4) over reads in \(Y\).

This is the "local class on a set" of h-walk (C4) and (H3) (h-walk 111, 378), made explicit.

**Lemma 0 (conversion).** Assume \(c_gM_1\le C_{\rm box}M\). If \(P\in\mathcal K(Z;a_0,a_1,a_2)\), then \(P\in\mathcal R_{\rm loc}(Z;\alpha)\) for every \(\alpha\) with
\[
 \alpha_0>L^2(1+C_{\rm pot}M)a_0,\qquad \alpha_1>L^2a_1,\qquad \gamma_0>L^3a_2,
\]
and \(r_Z(P)\le L^3(a_1+a_2)\).

*Proof.* Every point scale is at most \(L\). Hence \(\eta^{-2}l_p^2|\partial U-I|<L^2a_0\), and likewise for \(\mathbf U\); \(l_b|A'|<La_1\), \(l_b^2|\nabla^UA'|<L^2a_1\), \(l_b^3|\mathbf J|<L^3a_2\). A cube of side at most \(c_gM_1\xi_j\le c_gM_1L\le C_{\rm box}\ell\) is a box of Definition 3.1, so it carries a gauge with \(|A|,|\nabla A|<C_{\rm pot}Ma_0\); multiply by \(\xi_j\le L\) and \(\xi_j^2\le L^2\). The bound on \(r_Z\) is the maximum of the three normalized quantities. \(\square\)

*Status.* Proved, provided SA's "level-\(k\) units with bare mesh \(\eta_k\)" (SA 5665–5666) are pr-lay's level-\(k\) units with \(\eta=L^{-k}\) (pr-lay §1). Both texts say so. If the real-gauge clause uses the \(U\)-covariant difference in place of the plain one, the two differ by at most \(2|A|^2\), since \(\eta^{-1}|\operatorname{Ad}(e^{i\eta A})-1|\le2|A|\); the constants change by a factor \(2\).

### 3.4 Imports

**R (real gap; pr-lay §2).** There are \(c_L,a_R>0\), fixed with the early constants, such that for every real \(U\) on \(\mathbb T\) in the step's axial representative with real bound \(<a_R\), \(\mathsf A(U,0,0)\) exists, is real symmetric and \(\ge c_LI\) on \(\ell^2(I)\). pr-lay states it uniform over admissible sequences and larger gaps (pr-lay §2, "uniform in depth, volume, region shape and larger admissible gaps").

**W (walk package; h-walk Theorem H).** At every regular pair below \(a_h(L)\): \(\mathsf A=\sum_\omega A_\omega\) (H1), with \(|A_\omega(b,b')|\le C_h(C_hM_1^{-1/3})^{|\omega|}e^{-\delta_hd_B(\omega;b,b')}\) (H2), and each \(A_\omega\) holomorphic on the local class on its hull, real at real pairs, depending on the pair and on the regions only on its hull (H3). h-walk's own inputs (I1)–(I3) are retained.

**Hull and length conventions (from h-walk and inv-root §2).** For each label \(\omega\) let \(H(\omega)\) be its full read hull together with the base sites of its two arguments, and let \(l_\omega\) be the infimum of \(\ell^\infty\)-lengths of trees through the two arguments meeting all cells of \(\omega\). Then:

- **(P-hull)** \(H(\omega)\subset\mathcal N_{R_h}(T)\) for every such tree \(T\), with \(R_h=C_LM_1\) fixed (inv-root §2; `gates/h-walk-gate.md` §§8–9; carrier-adopt note (a));
- **(P-conn)** \(H(\omega)\) is nearest-neighbour connected: it is the union of the boxes \(\kappa_i^{(4)}\) along a walk whose consecutive cells intersect (h-walk 263–264, Theorem T(d)), enlarged by fixed read ranges and joined to the arguments, which lie within \(O(1)\) of the root cell (h-walk (H2));
- **(P-mom)** with \(\eta_W:=\delta_h/2\) as in inv-root (11) ("take \(\eta\le\delta_h/2\)"), there is \(W\) such that the \(P\)-independent majorants \(\bar m_\omega(x,y):=C_h(C_hM_1^{-1/3})^{|\omega|}e^{-\delta_hd_B(\omega;x,y)}\) satisfy
\[
 \max\Bigl\{\sup_x\sum_{y,\omega},\ \sup_y\sum_{x,\omega}\Bigr\}
   e^{\eta_Wl_\omega}\,\tfrac12\bigl(\bar m_\omega(x,y)+\bar m_\omega(y,x)\bigr)\le W. \tag{3.2}
\]
This is inv-root (11), whose proof uses only (H2), the root count and \(d_B\ge\ell^\infty\)-length (pr-lay Lemma 1's proof). Below I write \(\eta\) for \(\eta_W\) when no confusion with the mesh can arise; the mesh appears only in Lemma 3 and Definition 3.2. The constants \(W,\eta_W,R_h,C_h\) depend only on \(L,M_1\) (h-walk, "Order of constants").

**(I2) (gauge covariance of the averages).** For every gauge transformation \(u\) of the fine field, \(\mathcal M^k(U^u)=(\mathcal M^kU)^{u_\flat}\), where \(u_\flat\) is \(u\) evaluated at the level-\(k\) block centres. This is h-walk's (I2) (h-walk 358), Balaban's covariance of his averaging. h-walk uses it only for covariance; Lemma 3 uses it for an existence statement. The averaging \(\mathcal M^k\) on a level-\(k\) link reads the fine field within a fixed range \(r_M\) (h-walk (I3): finite stencils).

**(Ax) (reading of "block axial").** pr-lay §1 fixes the step's representative "with \(\mathcal M^kU\) block axial on the active blocks". I read this as: for each active level-\((k+1)\) block \(b\) there is a fixed spanning tree \(T_b\) of the level-\(k\) lattice of \(b\), and \(\mathrm{Ax}_b(U)\) means \(V(\ell)=\mathbf1\) for \(\ell\in T_b\), where \(V=\mathcal M^kU\). It reads only links of \(V\) inside \(b\). Any other per-block condition that a gauge transformation on the level-\(k\) sites of \(b\) can achieve works the same way below.

**G-ID (identification of the step's Gaussian).** At a complete physical pair \(P_W=(U_+,J(U_+))\), the Gaussian part of the step has covariance \(\mathsf A(P_W)^{-1}\) on \(I\). SA 14108–14118 sketches this; pr-lay (9) records that the identification "additionally requires the physical-current and background-branch identities". If the step uses pr-lay's completed form \(\mathsf A_{\rm full}\), read \(\mathsf A_{\rm full}\) throughout (Remark 9.4).

---

## 4. Lemma 1: the walk terms on the local class

**Lemma 1 (local-class form of (H2)).** Let \(Y\) be a set of bare sites and \(P\in\mathcal R_{\rm loc}(Y;\alpha)\) with \(\alpha\) below h-walk's ceiling \(a_h(L)\). For every label \(\omega\) with \(H(\omega)\subset Y\), the term \(A_\omega(P)\), defined by h-walk's formulas with every local inverse taken on the cut-down at the restriction of \(P\), is defined; it is holomorphic in \((A',\mathbf J)\) at fixed \(U\) on \(\mathcal R_{\rm loc}(Y;\alpha)\), real at real pairs, and depends only on \(P|_{H(\omega)}\); and \(|A_\omega(P)(b,b')|\le\bar m_\omega(b,b')\). If \(P\) is the restriction of a regular pair \(\widetilde P\), then \(A_\omega(P)=A_\omega(\widetilde P)\).

*Proof, by reading h-walk.* Each term is a finite product of the following factors.

1. Local inverses \(S_\kappa=K_\kappa^{-1}\), \(K_\kappa=K[\mathbf S^\kappa,P^\kappa,j^\kappa]\), on the cut-down sequence \(\mathbf S^\kappa\) of Lemma C (h-walk 245–248). Here \(P^\kappa\) is the restriction of \(P\) to \(\Omega^\kappa_0\subset\kappa^{(4)}\). Lemma C (C4) states that the restriction of a pair in the local class on a set containing \(\kappa^{(4)}\) is a regular pair for \(\mathbf S^\kappa\) (h-walk 111; its proof at 116 checks the pointwise and gauge clauses at points of \(\Omega^\kappa_0\) only). Lemma L (h-walk 223–226) holds "for every separated sequence ... (the actual sequence and every cut-down), every regular pair". So each \(S_\kappa\) is defined and obeys (5.1) of h-walk.
2. Commutators \([K,\tilde h_\kappa]=[K_\kappa,\tilde h_\kappa]\), which "read data within \(\kappa^{(5/2)}\)" (h-walk 281–283, proof of Theorem W(c),(d)). At a local pair take the right side as the definition.
3. Coefficient vertices \(V_\beta\) with \(j_\beta\) from Lemma J; \(j_\beta\) "depends on the data only on \([[\beta]]\)" and obeys (7.1), whose proof uses (6.2) and \(\|\chi_y\mathbf J\|\le2\gamma_0\) (h-walk 289–297); the vertex bound (7.2) is the localized coefficient bound of a2-curved (h-walk 301–305).
4. The finite stencils \(C_V,G^{(2)}_V,\mathsf a,E^{(2)}\) of (I3).

The chain bounds (6.2) and (7.3) are proved by iterating Lemma L for the successive \(K_{\kappa_i}\), Lemma K for the commutators and (7.1)–(7.2) for the vertices, then summing intermediate pillars (h-walk 269–280 and 331–336). None of these steps uses the global operator \(K\) or its inverse; the global objects enter only Theorem W(a) and Theorem T(a), the identities \(K^{-1}=\sum_\omega T_\omega\) and \(K_1^{-1}=\sum_\omega T^{(1)}_\omega\). The bounds for \(A^G_\omega,A^E_\omega,A^{\rm loc}_\kappa\) in the proof of Theorem H (h-walk 381–387) are then (7.3), (7.4) and the finite stencils. Holomorphy and reality are factorwise (Theorem W(c), T(d)). At a restriction of a regular pair all factors coincide with the global ones, since each reads only its own hull. \(\square\)

*Status.* Proved conditionally, by inspection of h-walk's proofs. It adds no estimate. The new statement is that h-walk's per-term bounds hold on the local class, while h-walk states them at regular pairs of the whole sequence. A referee should check the four items above against h-walk §§5–8.

---

## 5. Lemma 2: complex lines and Lipschitz bounds

Fix \(h:=\min\{a_R,a_h,1/2\}\) and put \(H_1:=16L^2W/h\).

**Lemma 2.** Let \(Y\) be a set of bare sites and \(P=(U,A',\mathbf J)\) a triple on \(Y\) whose real factor has real bound \(r_0<h/2\) on \(Y\) (pointwise and gauge clauses of Definition 3.2 on reads in \(Y\)). Put \(r=r_Y(P)\) and \(P_z=(U,zA',z\mathbf J)\).

(a) If \(r>0\), then \(P_z\in\mathcal R_{\rm loc}(Y;(h,h,h))\) for \(|z|<h/(8L^2r)\).

(b) If \(r\le h/(16L^2)\), then for every family \(\mathcal F\) of labels with \(H(\omega)\subset Y\),
\[
 \max\Bigl\{\sup_x\sum_{y,\,\omega\in\mathcal F},\ \sup_y\sum_{x,\,\omega\in\mathcal F}\Bigr\}
 e^{\eta l_\omega}|\bar A_\omega(P)(x,y)-\bar A_\omega(P_0)(x,y)|\le H_1r,
 \qquad P_0=(U,0,0).                                             \tag{5.1}
\]
Here \(\bar A_\omega=\tfrac12(A_\omega+A_\omega^{\mathsf T})\) (Definition 7.1).

*Proof.* (a) This is pr-lay Lemma 2. Its proof treats one plaquette at a time: the curvature bound (14) uses only the four links and two derivative readings of that plaquette, and (5) is a statement about a single plaquette stencil, which cannot cross two layer boundaries. The real gauges are unchanged. So the proof applies verbatim on reads in \(Y\).

(b) Fix \(\omega\in\mathcal F\), \(x,y\). By (a) and Lemma 1, \(f(z)=\bar A_\omega(P_z)(x,y)\) is holomorphic on \(|z|<R:=h/(8L^2r)\ge2\), with \(|f|\le\bar m:=\tfrac12(\bar m_\omega(x,y)+\bar m_\omega(y,x))\). The function \(g=(f-f(0))/(2\bar m)\) maps the disc into the unit disc with \(g(0)=0\). Schwarz's lemma gives \(|g(1)|\le1/R\), so \(|f(1)-f(0)|\le2\bar m/R=16L^2\bar m\,r/h\). Multiply by \(e^{\eta l_\omega}\), sum and use (3.2). \(\square\)

*Status.* Proved here.

Define the working ceilings
\[
 r_{\rm LG}:=\min\Bigl\{\frac h{16L^2},\ \frac{c_L}{8H_1}\Bigr\},\qquad
 a_\natural:=\min\Bigl\{a_h,\ \frac h2,\ \frac{a_R}{8},\ \frac1{16}\Bigr\}.   \tag{5.2}
\]

---

## 6. Gaps at local triples

### 6.1 Lemma 3: box extension of a local real field

**Lemma 3.** Let \(B^+\) be a box (a product of intervals) that is a union of level-\((k+1)\) blocks. Let \(U\) be real on the bare bonds of \(B^+\), with a real gauge \(g\) on the sites of \(B^+\) such that \(U^g=e^{i\eta A}\) on the bonds of \(B^+\), and
\[
 \alpha_U:=\max\{\sup|A|,\ \sup|\nabla A|\}\le1/16
\]
(level-\(k\) units, over reads in \(B^+\)). Assume \(U\) satisfies \(\mathrm{Ax}_b\) for every active block \(b\) with \(\mathcal N_{r_M}(b)\subset B^+\). Let \(F'\) be the union of the level-\((k+1)\) blocks \(b\subset B^+\) with \(\mathcal N_{r_M}(b)\subset B^+\). Then there is a real field \(\widetilde U\) on all bare bonds of \(\mathbb T\) such that:

(a) \(\widetilde U=U\) on every bond with both endpoints in \(F'\);

(b) \(\widetilde U\) satisfies \(\mathrm{Ax}_b\) on every active block;

(c) \(\widetilde U\) has real bound at most \(8L^2\alpha_U\) in the sense of pr-lay §1.

*Proof.* *Step 1 (clamp).* For a direction \(\mu\) let \(B^+_\mu=\{x\in B^+:x+\eta e_\mu\in B^+\}\), again a box of bare sites. Let \(\pi_\mu\) clamp each coordinate of a bare site to the corresponding interval of \(B^+_\mu\). Then \(\pi_\mu\) is the identity on \(B^+_\mu\). For a nearest neighbour \(x'=x+\eta e_\nu\), \(\pi_\mu(x')\) equals \(\pi_\mu(x)\) or \(\pi_\mu(x)+\eta e_\nu\): clamping in coordinate \(\nu\) is monotone and changes by \(0\) or \(\eta\), and the other coordinates do not change.

*Step 2 (cutoff).* Put \(\chi(x)=\max\{0,1-\operatorname{dist}_\infty(x,B^+)\}\). Then \(\chi=1\) on \(B^+\), \(\chi=0\) outside \(\mathcal N_1(B^+)\), and \(|\chi(x')-\chi(x)|\le\eta\) for nearest neighbours.

*Step 3 (extended potential).* Set \(A^{\rm ext}_\mu(x)=\chi(x)A_\mu(\pi_\mu(x))\). For bonds in \(B^+\) this is \(A\). Clearly \(|A^{\rm ext}|\le\alpha_U\). For \(x'=x+\eta e_\nu\),
\[
 \eta^{-1}|A^{\rm ext}_\mu(x')-A^{\rm ext}_\mu(x)|
 \le\eta^{-1}|\chi(x')-\chi(x)|\,|A_\mu(\pi_\mu x')|
     +\chi(x)\,\eta^{-1}|A_\mu(\pi_\mu x')-A_\mu(\pi_\mu x)|
 \le\alpha_U+\alpha_U .
\]
The last difference is zero or a difference of \(A_\mu\) along a bond in direction \(\nu\) with both base points in \(B^+_\mu\), a read inside \(B^+\). So \(|\nabla A^{\rm ext}|\le2\alpha_U\).

*Step 4 (curvature).* Let \(U'=e^{i\eta A^{\rm ext}}\) on all bonds. At a plaquette in the \(\mu\nu\)-plane, \(\partial U'(p)=\prod_{l=1}^4e^{iX_l}\) with \(X_l=\pm\eta A^{\rm ext}\) at its four links. Expanding the product, every term of total degree at least two is dominated by the matching term of \(e^{t}\), \(t=\sum|X_l|\le4\eta\alpha_U\le1\). So \(|\partial U'(p)-I-i\sum X_l|\le e^t-1-t\le t^2\). The signed sum is \(\eta^2\) times the lattice curl, at most \(4\eta^2\alpha_U\). Hence \(|\partial U'(p)-I|\le4\eta^2\alpha_U+16\eta^2\alpha_U^2\le5\eta^2\alpha_U\).

*Step 5 (back to \(U\) on \(B^+\)).* Let \(\hat g=g\) on the sites of \(B^+\) and \(\hat g=\mathbf1\) elsewhere. Put \(U''=(U')^{\hat g^{-1}}\). On bonds of \(B^+\), \(U''=(U^g)^{g^{-1}}=U\).

*Step 6 (representative).* For each active block \(b\not\subset F'\), choose \(u_\flat\) on the level-\(k\) sites of \(b\) by propagating along \(T_b\) from its root with \(u_\flat(\text{root})=\mathbf1\), so that \((\mathcal M^kU'')^{u_\flat}\) is \(\mathbf1\) on \(T_b\). Each level-\(k\) site lies in exactly one level-\((k+1)\) block, so these choices are independent. Put \(u_\flat=\mathbf1\) on all other level-\(k\) sites. Let \(u\) be \(u_\flat\) at the level-\(k\) block centres and \(\mathbf1\) at all other bare sites. Set \(\widetilde U=(U'')^u\).

(a): \(u\ne\mathbf1\) only at centres of level-\(k\) sites in blocks not contained in \(F'\). A bond with both endpoints in \(F'\) is therefore unchanged, and \(U''=U\) there.

(b): by (I2), \(\mathcal M^k\widetilde U=(\mathcal M^kU'')^{u_\flat}\). For \(b\not\subset F'\) this is \(\mathrm{Ax}_b\) by construction. For \(b\subset F'\), both endpoints of every link of \(T_b\) have \(u_\flat=\mathbf1\), so the link value is that of \(\mathcal M^kU''\), which reads \(U''\) within \(\mathcal N_{r_M}(b)\subset B^+\), where \(U''=U\); it equals \(\mathcal M^kU\), which satisfies \(\mathrm{Ax}_b\) by hypothesis.

(c): \(\widetilde U\) is a gauge transform of \(U'\). Curvature is conjugated, so Step 4 and \(l_p\le L\) give \(\eta^{-2}l_p^2|\partial\widetilde U-I|\le5L^2\alpha_U\). For the gauge clause, the single global gauge \((\hat g^{-1}u)^{-1}\) maps \(\widetilde U\) to \(U'=e^{i\eta A^{\rm ext}}\) on every cube, with \(\xi|A^{\rm ext}|\le L\alpha_U\) and \(\xi^2|\nabla A^{\rm ext}|\le2L^2\alpha_U\), since every scale is at most \(L\). Hence the real bound is at most \(5L^2\alpha_U\le8L^2\alpha_U\). \(\square\)

*Status.* Proved here, from (I2) and (Ax). Note what the lemma does not use: it does not extend the field from a long or non-convex set. Section 11.3 shows that extension from a general union of cubes can be impossible.

### 6.2 Lemma 4: the real gap at a local real factor

For a union \(Y\) of coarse cubes and a triple \(P\) on \(Y\), put
\[
 \mathsf A^Y(P):=\sum_{\omega:\,H(\omega)\subset Y}\bar A_\omega(P),         \tag{6.1}
\]
the hull-restricted (symmetrized) precision. By Lemma 1 it is defined on \(\mathcal R_{\rm loc}(Y)\) and depends only on \(P|_Y\).

Choose, in this order and depending only on \(L,M_1,c_L,W,\eta,R_h,r_M\):
\[
\begin{gathered}
 \ell_0 \text{ a power of } L \text{ with } \frac{c_{\rm IMS}W}{\eta^2\ell_0^2}\le\frac{c_L}8,\quad c_{\rm IMS}:=16\cdot400^2\cdot\frac4{e^2};\\
 \rho' \text{ with } 2We^{-\eta(\rho'-R_h)}\le\frac{c_L}8;\qquad
 \rho_G:=2\ell_0+\rho'+r_M+4L .
\end{gathered}                                                      \tag{6.2}
\]

**Lemma 4.** Let \(Y\) be a union of coarse cubes, \(P=(U,A',\mathbf J)\in\mathcal K(Y;a_0,a_1,a_2)\) with \(L^2(1+C_{\rm pot}M)a_0<a_\natural\), and assume the floor \(C_{\rm box}\ell\ge2\ell_0+2\rho_G\). Let \(S\subset I\) be a set of free coordinates with base points in \(Y\) and \(\operatorname{dist}_\infty(S,\mathbb T\setminus Y)\ge\rho_G\). Then \(\mathsf A^Y(U,0,0)\) is real symmetric and
\[
 \langle v,\mathsf A^Y(U,0,0)v\rangle\ge\tfrac34c_L|v|^2\qquad(v\in\ell^2(S)\ \text{real}). \tag{6.3}
\]

*Proof.* *Symmetry and reality.* Each \(\bar A_\omega\) is symmetric by construction and real at real pairs (Lemma 1), and the restriction in (6.1) depends only on hulls.

*Localization.* Let \(\varphi_c(x)=\prod_{\mu=1}^4(1-|\hat x_\mu-c_\mu|/\ell_0)_+\) for \(c\in\ell_0\mathbb Z^4\) (periodic; \(\ell_0\) divides the torus side because both are powers of \(L\) and \(\ell_0\le M\)). Then \(\sum_c\varphi_c=1\), at most \(16\) are nonzero at a point, and \(\psi:=(\sum_c\varphi_c^2)^{1/2}\ge(\sum_c\varphi_c)/4=1/4\). Put \(h_c=\varphi_c/\psi\), so \(\sum_ch_c^2=1\). Each \(\varphi_c\) is \(4/\ell_0\)-Lipschitz in \(d\) (a product of four \(1/\ell_0\)-Lipschitz factors bounded by one). At most \(32\) indices are nonzero at \(x\) or \(y\), so \(|\psi(x)-\psi(y)|\le\sqrt{32}\cdot4d(x,y)/\ell_0\le23d(x,y)/\ell_0\), and
\[
 |h_c(x)-h_c(y)|\le\frac{|\varphi_c(x)-\varphi_c(y)|}{\psi(x)}
   +\varphi_c(y)\frac{|\psi(y)-\psi(x)|}{\psi(x)\psi(y)}\le\frac{400\,d(x,y)}{\ell_0}.
\]
On \(\ell^2(S)\) let \(\mathsf A_S=\chi_S\mathsf A^Y(U,0,0)\chi_S\). The identity \([h,[h,\mathsf A]]=h^2\mathsf A-2h\mathsf Ah+\mathsf Ah^2\) and \(\sum_ch_c^2=1\) give
\[
 \mathsf A_S=\sum_ch_c\mathsf A_Sh_c+\tfrac12\sum_c[h_c,[h_c,\mathsf A_S]],\qquad
 \Bigl(\sum_c[h_c,[h_c,\mathsf A_S]]\Bigr)(x,y)=\sum_c(h_c(x)-h_c(y))^2\mathsf A_S(x,y).
\]
Since \(\sum_c(h_c(x)-h_c(y))^2\le32\cdot400^2d(x,y)^2/\ell_0^2\), \(d(x,y)\le l_\omega\) for every label with arguments \(x,y\), and \(\sup_{t\ge0}t^2e^{-\eta t}=4/(e\eta)^2\), the Schur test and (3.2) give
\[
 \tfrac12\Bigl\|\sum_c[h_c,[h_c,\mathsf A_S]]\Bigr\|\le\frac{c_{\rm IMS}W}{\eta^2\ell_0^2}\le\frac{c_L}8 .
\]

*One cell.* Fix \(c\) with \(h_c\ne0\) on \(S\), let \(Q_c\) be the closed cube of side \(2\ell_0\) centred at \(c\), and let \(B_c^+\) be the smallest union of level-\((k+1)\) blocks containing \(\mathcal N_{\rho'+r_M+2L}(Q_c)\). It is a box, contained in \(\mathcal N_{\rho_G}(S)\subset Y\), with side at most \(2\ell_0+2\rho_G\le C_{\rm box}\ell\). By Definition 3.1 it carries a real gauge with \(\alpha_U<C_{\rm pot}Ma_0\le a_\natural\le1/16\), and (Rep) gives \(\mathrm{Ax}_b\) on its interior blocks. The set \(F'_c\) of Lemma 3 contains \(\mathcal N_{\rho'}(Q_c)\). Lemma 3 gives \(\widetilde U_c\), equal to \(U\) on \(F'_c\), axial, with real bound \(\le8L^2\alpha_U<a_R\). By R, \(\langle u,\mathsf A(\widetilde U_c,0,0)u\rangle\ge c_L|u|^2\) for real \(u\in\ell^2(I)\).

Now let \(u\) be real and supported in \(S\cap Q_c\). Compare the two quadratic forms term by term. A label \(\omega\) with \(H(\omega)\subset F'_c\) has the same value in \(\mathsf A^Y(U,0,0)\) and in \(\mathsf A(\widetilde U_c,0,0)\), because its value depends only on the data on its hull (Lemma 1), the fields agree there (Lemma 3(a)), and the regions are the step's. Every other label with an argument in \(Q_c\) has a hull site at distance \(>\rho'\) from \(Q_c\); by (P-hull) its tree has length \(l_\omega\ge\rho'-R_h\). Using the \(P\)-independent majorants, the two remaining sums have Schur norms at most \(We^{-\eta(\rho'-R_h)}\) each. So
\[
 \langle u,\mathsf A^Y(U,0,0)u\rangle\ge\bigl(c_L-2We^{-\eta(\rho'-R_h)}\bigr)|u|^2\ge\tfrac78c_L|u|^2 .
\]

*Sum.* With \(u=h_cv\), \(\sum_c|h_cv|^2=|v|^2\), so \(\langle v,\mathsf A_Sv\rangle\ge(\tfrac78-\tfrac18)c_L|v|^2\). \(\square\)

*Status.* Proved here, from R, Lemmas 0, 1, 3, (I2), (Ax) and (Rep). This is the four-dimensional replacement for YM3's transfer of the flat gap to local backgrounds (YM3 40217–40250). The difference: YM3 compares a local form with the flat form in a real mesh gauge, using gauge covariance; the 4D soft axial term is covariant only under block-constant transformations (h-walk (H3)), so here the comparison is with the global operator at an extended axial field.

### 6.3 Lemma 5: complex gaps

**Lemma 5.** Under the hypotheses of Lemma 4, assume also \(r_Y(P)\le r_{\rm LG}\).

(a) For complex \(v\in\ell^2(S)\), \(\operatorname{Re}\langle v,\mathsf A^Y(P)v\rangle_H\ge\tfrac58c_L|v|^2\).

(b) Let \(r\ge1\) satisfy \(We^{-\eta r}\le c_L/8\), and let \(\mathsf A_<(P)=\sum_{l_\omega\le r}\bar A_\omega(P)\) be the short part, untagged. If \(B\subset I\) has \(\operatorname{dist}_\infty(B,\mathbb T\setminus Y)\ge\rho_G+r+R_h\), then the compression \(\mathsf A_B=\chi_B\mathsf A_<(P)\chi_B\) is defined from data in \(Y\), and
\[
 \operatorname{Re}\langle v,\mathsf A_Bv\rangle_H\ge\tfrac12c_L|v|^2,\qquad \|\mathsf A_B\|\le W .  \tag{6.4}
\]

*Proof.* (a) For real symmetric \(\mathsf A^Y(P_0)\) and \(v=v_1+iv_2\), \(\langle v,\mathsf A^Y(P_0)v\rangle_H=\langle v_1,\cdot\,v_1\rangle+\langle v_2,\cdot\,v_2\rangle\ge\tfrac34c_L|v|^2\) by (6.3). By Lemma 0 the real factor has real bound \(<h/2\), so Lemma 2(b) applies and \(\|\mathsf A^Y(P)-\mathsf A^Y(P_0)\|\le H_1r_Y(P)\le c_L/8\).

(b) A short label with an argument in \(B\) has its hull within \(r+R_h\) of that argument, hence inside \(Y\); so on \(B\times B\), \(\mathsf A_<=\mathsf A^Y-\mathsf E^Y\), where \(\mathsf E^Y\) sums the labels with \(l_\omega>r\) and \(H(\omega)\subset Y\). By (3.2), \(\|\chi_B\mathsf E^Y\chi_B\|\le We^{-\eta r}\le c_L/8\). Apply (a) with \(S=B\) (its distance to the complement exceeds \(\rho_G\)). The norm bound is the Schur bound from (3.2). \(\square\)

*Status.* Proved here.

---

## 7. The actual collared family

**Definition 7.1 (symmetrized precision labels).** For each h-walk label \(\omega\) put \(\bar A_\omega=\tfrac12(A_\omega+A_\omega^{\mathsf T})\), with the same hull \(H(\omega)\) and length \(l_\omega\). Since \(H(\omega)\) contains both arguments and is symmetric under exchanging them, the transposed half reads the same data. At a regular pair, \(\sum_\omega\bar A_\omega=\tfrac12(\mathsf A+\mathsf A^{\mathsf T})=\mathsf A\), because \(\mathsf A\) is symmetric (pr-lay Theorem 3). The majorant of \(\bar A_\omega\) is the symmetrized majorant in (3.2).

**Definition 7.2 (tags).** For a set \(H\) of bare sites and \(s\in\mathbb C^\Lambda\) put \(P_\Lambda(H)=\{\Delta\in\Lambda:\Delta\cap H\ne\varnothing\}\) and \(s^{(H)}=\prod_{\Delta\in P_\Lambda(H)}s_\Delta\). A labelled term with hull \(H\) is multiplied by \(s^{(H)}\), once per cube. **Convention:** if \(s_\Delta=0\) for some \(\Delta\in P_\Lambda(H)\), the tagged term is \(0\), whether or not the untagged term is defined. The UM assignment for a polymer \(Z\supset Z_0^\sharp\) is
\[
 s_Z:\quad s_\Delta=1\ (\Delta\subset Z_0^\sharp),\qquad
 s_\Delta\ \text{free}\ (\Delta\subset Z\setminus Z_0^\sharp),\qquad
 s_\Delta=0\ (\Delta\not\subset Z),                               \tag{7.1}
\]
as in UM3 (SA 14353–14364). The reference assignment \(s_0\) has \(s_\Delta=1\) on \(Z_0^\sharp\) and \(0\) elsewhere. A tagged term **survives** if its tag is not forced to zero, that is, if its hull lies in \(Z\); it is **varied** if its hull meets \(Z\setminus Z_0^\sharp\).

Then
\[
 \mathsf A(s;P):=\sum_\omega s^{(H(\omega))}\bar A_\omega(P).      \tag{7.2}
\]
At \(s=s_Z\) only labels with \(H(\omega)\subset Z\) occur, so \(\mathsf A(s_Z;P)\) is defined for every triple on \(Z\) in the local class (Lemma 1). At \(s=s_0\), \(\mathsf A(s_0;P)=\mathsf A^{Z_0^\sharp}(P)\) of (6.1).

**Definition 7.3 (grouped coefficients).** Fix the constants of §8.1: \(a_s,b_s,\lambda,\varrho,r,\theta,n,R_*\). Let \(\mathsf A_<\) be the untagged short part (Lemma 5(b)) and, for \(t\ge0\), \(N_t=(\lambda I-\mathsf A_<)/(\lambda+t)\). For coordinates \(x,y\) define
\[
 P_t(x,y)=\frac1{\lambda+t}\sum_{j=0}^{n-1}N_t^j(x,y),\qquad Q_t(x,y)=N_t^n(x,y).
\]
Each entry is one labelled coefficient, with hull \(\bar B(x,R_*)\cup\bar B(y,R_*)\) (closed \(\ell^\infty\) balls of bare sites) and length \(d(x,y)\). \(P_t(x,y)=0\) unless \(d(x,y)\le(n-1)r\), and \(Q_t(x,y)=0\) unless \(d(x,y)\le nr\). The coefficients are grouped **before** tags are inserted; the short terms inside a grouped coefficient carry no tags.

Every short term used in \(N_t^j(x,y)\), \(j\le n\), has its arguments within \(nr\) of \(x\) and its hull within \(nr+r+R_h\le R_*\) of \(x\). So the grouped coefficient depends only on the data in its hull.

**Definition 7.4 (chains and the decoupled inverse root).** A chain \(\alpha\) is a finite sequence of labelled factors \(F_0F_1\cdots F_m\) (\(m\ge0\)) with contracted intermediate coordinates kept as labels, where \(F_0\) is a \(P_t\)-entry and each \(F_i\), \(i\ge1\), is either a \(Q_t\)-entry or a pair \((-\bar A_\omega\text{-entry},\,P_t\text{-entry})\) with \(l_\omega>r\). Its value \(R_\alpha(t;x,y)\) is the product of the entries. Its hull \(H(\alpha)\) is the union of the factor hulls, and its length \(l(\alpha)\) is the sum of factor lengths (\(d\) for grouped entries, \(l_\omega\) for long precision terms). Put
\[
 r_\alpha=\frac1\pi\int_0^\infty t^{-1/2}R_\alpha(t)\,dt,\qquad
 \mathsf r(s;P)=\sum_\alpha s^{(H(\alpha))}\,r_\alpha(P).          \tag{7.3}
\]
This is the series of inv-root (14)–(17), with three changes: coarse cubes of side \(\ell=LM\) carry the tags; the grouped hull radius \(R_*\) includes the gap margin; and the majorants are uniform in the pair (§8).

*Connectivity and tree.* Each factor hull lies within \(R_*\) of a factor tree: the segment from \(x\) to \(y\) for grouped entries, an admitted tree for \(\bar A_\omega\) (P-hull, \(R_h\le R_*\)). Consecutive factors share their contracted coordinate, which lies on both factor trees. So the union \(T(\alpha)\) of factor trees is connected, has \(\ell^\infty\)-length \(l(\alpha)\), and \(H(\alpha)\subset\mathcal N_{R_*}(T(\alpha))\). Each factor hull is nearest-neighbour connected (balls; P-conn), and consecutive hulls share a site, so \(H(\alpha)\) is nearest-neighbour connected.

**Definition 7.5 (the collared matrices).** Let \(Z_0\) be the fine support of an index \(\iota\) (SA 14349–14351), \(I_0=\{x\in I:\hat x\in Z_0\}\), \(\chi=\mathbf1_{I_0}\), and let \(Z\supset Z_0^\sharp\) be a union of coarse cubes. For \(s=s_Z\) and a triple \(P\) on \(Z\):
\[
 C(s;P)=\bigl(\chi\,\mathsf A(s;P)\,\chi\bigr)^{-1}\ \text{on}\ \ell^2(I_0),\qquad
 X(s;P)=\chi\,\mathsf A(s;P)(1-\chi),\qquad
 \Gamma(s;P)=-X(s;P)\,\mathsf r(s;P),                             \tag{7.4}
\]
\(\Gamma\) being an \(I_0\times I\) matrix (only columns with base points in \(Z\) are nonzero). The references are \(C_*=C(s_0;P_0)\), \(\Gamma_*=\Gamma(s_0;P_0)\), \(P_0=(U,0,0)\). For a coefficient ratio \(\tau\), the structure is \((\tau^{-1}C,\tau^{1/2}\Gamma)\) (SA 14196–14198). The functional is SA FG4:
\[
 {\cal J}(Z_0;s;P)[F]={\cal J}_{C(s;P),\Gamma(s;P)}[F]=\int F\,d\mu_{D(s;P)},\qquad
 D=C+C\Gamma\Gamma^{\mathsf T}C .                                 \tag{7.5}
\]

These are SA's matrices (SA 14164–14166) with "the precision and its inverse root ... by their respective expansions" (SA 14161–14162) specified: the precision by the hull-tagged walk series (7.2), the inverse root by (7.3).

---

## 8. Theorem A: the local inverse-root series

### 8.1 Constants

All of the following depend only on \(L,M_1\) and the imports R, W; they precede \(\kappa,\bar\kappa,M\).
\[
\begin{gathered}
 a_s=\tfrac12c_L,\quad b_s=\max(W,c_L),\quad \lambda=\frac{2b_s^2}{a_s},\quad
 \varrho=\Bigl(1-\frac{3a_s^2}{4b_s^2}\Bigr)^{1/2}<1,\\
 \hat p_r=16n_cr^4\sum_{j\ge0}(j+1)^4\varrho^{j/2}.
\end{gathered}                                                     \tag{8.1}
\]
Choose \(r\ge1\) with \(We^{-\eta r}\le c_L/8\) and \(We^{-\eta r/2}\hat p_r/\lambda\le1/4\); this is possible since \(\hat p_r\) is a fixed multiple of \(r^4\) and \(e^{\eta r/2}\ge(\eta r/2)^5/5!\). Then
\[
 \theta=\min\Bigl\{\frac\eta2,\ \frac{-\log\varrho}{2r}\Bigr\},\qquad
 n\ \text{with}\ n_c(2nr+1)^4\varrho^{n/2}\le\tfrac14,\qquad
 R_*=nr+r+R_h+\rho_G,\qquad U_r=\frac{2\hat p_r}{\sqrt\lambda}.  \tag{8.2}
\]
The choice of \(n\) is possible by the same exponential-series argument. For a working region, put
\[
 \mathcal W(Y)=\{P=(U,A',\mathbf J):\ U\ \text{is the real factor of a triple in}\ \mathcal K(Y)\ \text{with}\ L^2(1+C_{\rm pot}M)a_0<a_\natural,\ r_Y(P)\le r_{\rm LG}\}. \tag{8.3}
\]
Every triple of \(\mathcal K(Y)\) with \(L^2(1+C_{\rm pot}M)a_0<a_\natural\) and \(L^3(a_1+a_2)\le r_{\rm LG}\) lies in \(\mathcal W(Y)\) (Lemma 0). \(\mathcal W(Y)\) is closed under \(P\mapsto P_z\) for \(|z|\le r_{\rm LG}/r_Y(P)\), since \(r_Y(P_z)=|z|r_Y(P)\): \(r_Y\) is homogeneous of degree one in \((A',\mathbf J)\) at fixed \(U\).

### 8.2 Statement

A chain is a \(Y\)-chain if \(H(\alpha)\subset Y\).

**Theorem A.** Let \(Y\) be a union of coarse cubes and \(P\in\mathcal W(Y)\).

(i) For every \(Y\)-chain, \(r_\alpha(P)\) is defined by an absolutely convergent integral, depends only on \(P|_{H(\alpha)}\), is holomorphic in \((A',\mathbf J)\) on \(\mathcal W(Y)\) at fixed \(U\), and is real at real pairs.

(ii) There are nonnegative numbers \(m_\alpha(x,y)\), independent of \(P\in\mathcal W(Y)\), with \(|r_\alpha(P)(x,y)|\le m_\alpha(x,y)\) and
\[
 \max\Bigl\{\sup_x\sum_{y,\alpha},\ \sup_y\sum_{x,\alpha}\Bigr\}e^{\theta l(\alpha)}m_\alpha(x,y)\le U_r,
\]
the sum running over all chains (a fortiori over \(Y\)-chains).

(iii) If \(r_Y(P)\le r_{\rm LG}/2\), then for every family \(\mathcal F\) of \(Y\)-chains
\[
 \max\{\text{row},\text{column}\}\sum_{\alpha\in\mathcal F}e^{\theta l(\alpha)}|r_\alpha(P)-r_\alpha(P_0)|\le\frac{2U_r}{r_{\rm LG}}\,r_Y(P).
\]

(iv) If \(P\in\mathcal W(\mathbb T)\) is a triple on the whole torus, then \(\sum_\alpha r_\alpha(P)=\mathsf A(P)^{-1/2}\), the principal inverse root, symmetric, with absolute convergence.

### 8.3 Proof

*Factor bounds.* Let \(x\) be a coordinate with \(\bar B(x,R_*)\subset Y\). For \(j\le n\) put \(B_j=I\cap\bar B(x,jr)\). In \(N_t^j(x,y)=\sum N_t(x,z_1)\cdots N_t(z_{j-1},y)\) every nonzero term has \(z_i\in\bar B(x,ir)\), since \(\mathsf A_<\) has range at most \(r\). So \(N_t^j(x,y)=((\chi_{B_j}N_t\chi_{B_j})^j)(x,y)\). The set \(B_j\) has distance at least \(R_*-nr\ge\rho_G+r+R_h\) from \(\mathbb T\setminus Y\). By Lemma 5(b), \(\mathsf A_{B_j}=\chi_{B_j}\mathsf A_<\chi_{B_j}\) has \(\operatorname{Re}\ge a_s\) and norm \(\le W\le b_s\). Then for \(v\in\ell^2(B_j)\)
\[
 |(\lambda-\mathsf A_{B_j})v|^2=\lambda^2|v|^2-2\lambda\operatorname{Re}\langle v,\mathsf A_{B_j}v\rangle_H+|\mathsf A_{B_j}v|^2
 \le(\lambda^2-2\lambda a_s+b_s^2)|v|^2=\lambda^2\varrho^2|v|^2 .
\]
Hence \(\|\chi_{B_j}N_t\chi_{B_j}\|\le\varrho\lambda/(\lambda+t)\) and
\[
 |N_t^j(x,y)|\le\Bigl(\frac{\varrho\lambda}{\lambda+t}\Bigr)^j\mathbf1\{d(x,y)\le jr\}. \tag{8.4}
\]
The same bound holds if instead \(\bar B(y,R_*)\subset Y\), by the same argument with balls about \(y\). For a grouped coefficient whose hull lies in \(Y\), both balls lie in \(Y\).

Define the \(P\)-independent majorants
\[
 m^P_t(x,y)=\frac1{\lambda+t}\sum_{j=0}^{n-1}\Bigl(\frac{\varrho\lambda}{\lambda+t}\Bigr)^j\mathbf1\{d\le jr\},\qquad
 m^Q_t(x,y)=\varrho^n\mathbf1\{d\le nr\}.
\]
They are symmetric in \(x,y\). By (3.1), \(2jr+1\le2r(j+1)\), and \(e^{\theta jr}\le\varrho^{-j/2}\),
\[
 \sum_ye^{\theta d(x,y)}m^P_t(x,y)\le\frac1{\lambda+t}\sum_{j\ge0}n_c(2jr+1)^4\varrho^{j}e^{\theta jr}\le\frac{\hat p_r}{\lambda+t},\qquad
 \sum_ye^{\theta d(x,y)}m^Q_t(x,y)\le n_c(2nr+1)^4\varrho^{n/2}\le\tfrac14 .
\]
For long precision factors use \(\bar m_\omega\) of (3.2). Since \(\theta\le\eta/2\) and \(l_\omega>r\),
\[
 \sum_{y,\ l_\omega>r}e^{\theta l_\omega}\bar m_\omega(x,y)\le e^{-(\eta-\theta)r}W\le We^{-\eta r/2}.
\]
All three hold with rows and columns exchanged.

*Chains.* For a labelled family write \(|\cdot|_\theta\) for the maximum of the row and column sums of \(e^{\theta\cdot\text{length}}\times\)majorant. Summing an intermediate coordinate over a product (Tonelli) shows that lengths add and \(|UV|_\theta\le|U|_\theta|V|_\theta\) (inv-root (12)). A \(K\)-factor (a \(Q_t\)-entry or a long term followed by a \(P_t\)-entry) therefore has
\[
 |K_t|_\theta\le\tfrac14+We^{-\eta r/2}\frac{\hat p_r}{\lambda+t}\le\tfrac14+\tfrac14=\tfrac12 ,
\]
by the choice of \(r\). Set \(m_\alpha(t)\) to be the product of the factor majorants and \(m_\alpha=\pi^{-1}\int_0^\infty t^{-1/2}m_\alpha(t)\,dt\). Summing over \(m\ge0\),
\[
 \Bigl|\{m_\alpha(t)\}_\alpha\Bigr|_\theta\le\frac{\hat p_r}{\lambda+t}\sum_{m\ge0}2^{-m}=\frac{2\hat p_r}{\lambda+t},\qquad
 \frac1\pi\int_0^\infty\frac{t^{-1/2}\,2\hat p_r}{\lambda+t}\,dt=\frac{2\hat p_r}{\sqrt\lambda}=U_r .
\]
Tonelli exchanges the integral with the sums. This proves (ii), once (i) gives \(|r_\alpha|\le m_\alpha\).

*(i).* For a \(Y\)-chain every factor hull lies in \(Y\), so (8.4) and Lemma 1 apply to every factor, and \(|R_\alpha(t)|\le m_\alpha(t)\). The first factor is a \(P_t\)-entry, so \(m_\alpha(t)\le C_\alpha/(\lambda+t)\) and \(t^{-1/2}m_\alpha(t)\) is integrable. Each factor is a polynomial in finitely many short and long precision terms, divided by powers of \(\lambda+t\); it depends only on the data in its hull and is holomorphic at fixed \(U\) (Lemma 1). The integrand is dominated uniformly in \(P\in\mathcal W(Y)\), so the integral is holomorphic (differentiate under the integral, or Fubini and Morera). Reality at real pairs is factorwise.

*(iii).* Fix \(\alpha\), \(x,y\) and put \(f(z)=r_\alpha(P_z)(x,y)\), \(R=r_{\rm LG}/r_Y(P)\ge2\). For \(|z|<R\), \(P_z\in\mathcal W(Y)\), so \(f\) is holomorphic there with \(|f|\le m_\alpha(x,y)\). Schwarz's lemma applied to \((f-f(0))/(2m_\alpha)\) gives \(|f(1)-f(0)|\le2m_\alpha/R\). Sum with weights and use (ii).

*(iv).* On the whole torus every chain is a \(\mathbb T\)-chain. The algebraic identity \((\lambda+t)(I-N_t)\cdot(\lambda+t)^{-1}\sum_{j<n}N_t^j=I-N_t^n\) gives \((\mathsf A_<+t)P_t=I-Q_t\), and so \((\mathsf A+t)P_t=I-K_t\) with \(K_t=Q_t-(\mathsf A-\mathsf A_<)P_t\). The Schur norm is at most the weighted norm, so \(\|K_t\|\le\tfrac12\). Then \((\mathsf A+t)P_t\sum_mK_t^m=I\). In finite dimension a right inverse is the inverse, so \((\mathsf A+t)^{-1}=P_t\sum_mK_t^m=\sum_\alpha R_\alpha(t)\), absolutely. Lemma 5(a) with \(Y=\mathbb T\) gives \(\operatorname{Re}\mathsf A\ge\tfrac58c_L\) on \(\ell^2(I)\). For such \(\mathsf A\), \(\mathsf A^{-1/2}=\pi^{-1}\int_0^\infty t^{-1/2}(\mathsf A+t)^{-1}dt\) (inv-root §4: the scalar identity on \(\operatorname{Re}z>0\) and its Jordan-block extension). Tonelli with the majorant \(2\hat p_r/(\lambda+t)\) exchanges the integral and the chain sum. Each \((\mathsf A+t)^{-1}\) is symmetric because \(\mathsf A\) is, so the root is symmetric. \(\square\)

*Status.* Proved here. Compared with inv-root, the only new premise is local: (8.4) uses the ball gaps of Lemma 5(b), not a global gap. The global gap enters only (iv), at whole-torus triples.

---

## 9. Theorem B: the envelope (9)

### 9.1 Statement

Put \(d=\theta/4\), \(b=32\), \(\varepsilon_M=e^{32\bar\kappa-dM}\), and
\[
\begin{gathered}
 K_0=1+\frac4{3c_L}+W+WU_r,\qquad
 H_0=\Bigl(\frac8{3c_L^2}+U_r\Bigr)\bigl(e^{3\eta R_h/4}W+H_1\bigr)+e^{\theta R_*/2}WU_r+\frac{4WU_r}{r_{\rm LG}},\\
 C_\tau=\frac4{c_L}+K_0+1 .
\end{gathered}                                                     \tag{9.1}
\]

Floors on \(M\) (after \(\bar\kappa\)):
\[
\begin{gathered}
 \text{(F1)}\ \ell\ge8R_*;\qquad \text{(F2)}\ M\ge\max(\rho_G,2R_*);\qquad
 \text{(F3)}\ \frac{128\bar\kappa}{\ell}\le\frac\theta2;\\
 \text{(F4)}\ e^{3\eta R_h/4}W\varepsilon_M\le\frac{c_L}8\ \text{and}\ H_0\varepsilon_M\le\frac12;\qquad
 \text{(F5)}\ c_gM_1\le C_{\rm box}M,\ \ 2\ell_0+2\rho_G\le C_{\rm box}\ell .
\end{gathered}                                                     \tag{9.2}
\]
Ceilings on the radii (after \(M\)):
\[
 \text{(C1)}\ L^2(1+C_{\rm pot}M)a_0<a_\natural;\qquad
 \text{(C2)}\ L^3(a_1+a_2)\le\min\Bigl\{\frac{r_{\rm LG}}2,\frac1{2H_0}\Bigr\};\qquad
 \text{(C3)}\ |\tau-1|\le\tfrac12 .                               \tag{9.3}
\]

**Theorem B.** Assume R, W, (I2), (Ax), (Rep), (9.2) and (9.3). Let \(Z_0\), \(Z\supset Z_0^\sharp\) be as in Definition 7.5 and \(P\in\mathcal K(Z;a_0,a_1,a_2)\). Then for every \(s=s_Z\) with \(|s_\Delta|\le e^{\bar\kappa}\) on \(Z\setminus Z_0^\sharp\):

(B1) \(C_*\) is real symmetric positive definite and \(\Gamma_*\) is real, with \(\|C_*\|\le4/(3c_L)\), \(\|C_*^{-1}\|\le W\), \(\|\Gamma_*\|\le WU_r\); so \(\|C_*\|+\|C_*^{-1}\|+\|\Gamma_*\|\le K_0\).

(B2) \(\chi\mathsf A(s;P)\chi\) is complex symmetric with \(\operatorname{Re}\ge c_L/2\) on \(\ell^2(I_0)\); \(C\) exists, is complex symmetric, and \(\|C\|\le2/c_L\).

(B3) \(\|C-C_*\|+\|\Gamma-\Gamma_*\|\le H_0\{\varepsilon_M+L^3(a_1+a_2)\}\).

(B4) For the \(\tau\)-structure, \(\|\tau^{-1}C-C_*\|+\|\tau^{1/2}\Gamma-\Gamma_*\|\le H_0\{\varepsilon_M+L^3(a_1+a_2)\}+C_\tau|\tau-1|\).

This is IN1 (9) with \(b=32\), \(d=\theta/4\), \(H_p(M)\equiv L^3\), and with the \(a_0\)-term absent (it is allowed with coefficient zero). The constants \(K_0,H_0,d,C_\tau\) depend only on \(L,M_1\) and R, W.

### 9.2 Proof

Throughout, \(r:=r_Z(P)\le L^3(a_1+a_2)\le r_{\rm LG}/2\) (Lemma 0, (C2)), and \(P|_{Y}\in\mathcal W(Y)\) for every union \(Y\subset Z\) of coarse cubes (restriction, (C1)).

*Step 1: parameter weights.* For a surviving tagged term with hull \(H\) and tree length \(l\), the factors \(s_\Delta\) with \(\Delta\subset Z_0^\sharp\) equal one, and the others have modulus at most \(e^{\bar\kappa}\). By (G4) and (F1), \(|s^{(H)}|\le e^{\bar\kappa\#P_\Lambda(H)}\le e^{16\bar\kappa}e^{128\bar\kappa l/\ell}\le e^{16\bar\kappa}e^{\theta l/2}\), using (F3). For a product of two separately tagged terms (as in \(\Gamma\)) the bound is \(e^{32\bar\kappa}e^{\theta(l_1+l_2)/2}\).

*Step 2: varied terms cross the collar.* Let a varied term have an argument \(x\in I_0\). Its hull contains a site outside \(Z_0^\sharp\), at distance at least \(M\) from \(\hat x\) by (G1). By (P-hull) its tree, which contains \(\hat x\), has length \(l\ge M-R_h\). For a product \(X_\omega(x,y)r_\alpha(y,z)\) in which \(\alpha\) is varied, the union of the two hulls is within \(R_*\) of the connected union of the two trees, which contains \(\hat x\); so \(l_1+l_2\ge M-R_*\). The same holds if \(\omega\) is varied.

*Step 3: the varied precision.* Let \(\mathsf V(s;P)=\chi\mathsf A(s;P)-\chi\mathsf A(s_0;P)\), the sum of varied surviving labels with left argument in \(I_0\). By Steps 1–2 and (3.2), its Schur norm satisfies
\[
 \|\mathsf V\|\le e^{16\bar\kappa}\sum e^{\theta l/2}\bar m
 \le e^{16\bar\kappa}e^{-(3\eta/4)(M-R_h)}W\le e^{3\eta R_h/4}W\varepsilon_M .
\]
Here I used \(e^{\theta l/2}\le e^{\eta l/4}=e^{\eta l}e^{-3\eta l/4}\), \(l\ge M-R_h\), and \(3\eta/4\ge d\), \(16\bar\kappa\le32\bar\kappa\). The same bound holds for \(\mathsf V(1-\chi)\) and for \(\chi\mathsf V^{\mathsf T}\).

*(B1).* \(C_*^{-1}=\chi\mathsf A^{Z_0^\sharp}(P_0)\chi\). It is real symmetric (Lemma 4). By (G1) and (F2), \(\operatorname{dist}_\infty(I_0,\mathbb T\setminus Z_0^\sharp)\ge M\ge\rho_G\), so Lemma 4 with \(Y=Z_0^\sharp\), \(S=I_0\) gives \(C_*^{-1}\ge\tfrac34c_L\). Hence \(C_*>0\) and \(\|C_*\|\le4/(3c_L)\). The Schur bound gives \(\|C_*^{-1}\|\le W\). Next, \(\Gamma_*=-X(s_0;P_0)\mathsf r(s_0;P_0)\), where \(X(s_0;P_0)\) has Schur norm \(\le W\) and \(\mathsf r(s_0;P_0)=\sum_{H(\alpha)\subset Z_0^\sharp}r_\alpha(P_0)\) has Schur norm \(\le U_r\) (Theorem A(ii) with \(Y=Z_0^\sharp\)). Both are real (Lemma 1, Theorem A(i)).

*(B2).* \(\chi\mathsf A(s;P)\chi=\chi\mathsf A^{Z_0^\sharp}(P)\chi+\chi\mathsf V\chi\). It is complex symmetric, since every \(\bar A_\omega\) is symmetric and the tag depends only on the hull. Lemma 5(a) with \(Y=Z_0^\sharp\), \(S=I_0\) gives \(\operatorname{Re}\ge\tfrac58c_L\) for the first part; Step 3 and (F4) bound the second by \(c_L/8\). So \(\operatorname{Re}\ge c_L/2\), the matrix is invertible, \(\|C\|\le2/c_L\), and \(C=C^{\mathsf T}\).

*(B3), the \(C\) part.* \(C-C_*=C\,(C_*^{-1}-C^{-1})\,C_*\), and
\[
 \|C^{-1}-C_*^{-1}\|\le\|\chi\mathsf V\chi\|+\|\chi(\mathsf A^{Z_0^\sharp}(P)-\mathsf A^{Z_0^\sharp}(P_0))\chi\|
 \le e^{3\eta R_h/4}W\varepsilon_M+H_1r ,
\]
by Step 3 and Lemma 2(b). Multiply by \(\|C\|\|C_*\|\le8/(3c_L^2)\).

*(B3), the \(\Gamma\) part.* Write \(X=X(s;P)\), \(X_0=X(s_0;P)\), \(X_{00}=X(s_0;P_0)\), \(\mathsf r=\mathsf r(s;P)\), \(\mathsf r_0=\mathsf r(s_0;P)\), \(\mathsf r_{00}=\mathsf r(s_0;P_0)\). Then
\[
 \Gamma_*-\Gamma=(X-X_0)\mathsf r_{00}+(X_0-X_{00})\mathsf r_{00}+X(\mathsf r-\mathsf r_0)+X(\mathsf r_0-\mathsf r_{00}).
\]
- First term: \(X-X_0=\mathsf V(1-\chi)\), norm \(\le e^{3\eta R_h/4}W\varepsilon_M\) (Step 3); \(\|\mathsf r_{00}\|\le U_r\).
- Second term: Lemma 2(b) gives \(\|X_0-X_{00}\|\le H_1r\); times \(U_r\).
- Third term: every product \(X_\omega(x,y)\,s^{(H(\alpha))}r_\alpha(y,z)\) has \(\alpha\) varied. By Steps 1–2 its weight is at most \(e^{32\bar\kappa}e^{\theta(l_1+l_2)/2}\) with \(l_1+l_2\ge M-R_*\). Write \(e^{\theta(l_1+l_2)/2}=e^{\theta(l_1+l_2)}e^{-\theta(l_1+l_2)/2}\), use \(e^{\theta l_1}\le e^{\eta l_1}\), and sum with (3.2) and Theorem A(ii):
\[
 \|X(\mathsf r-\mathsf r_0)\|\le e^{32\bar\kappa}e^{-\theta(M-R_*)/2}WU_r\le e^{\theta R_*/2}WU_r\,\varepsilon_M ,
\]
since \(\theta/2\ge d\). This includes products in which \(\omega\) is varied too: Step 1 covers both tags.
- Fourth term: \(\|X\|\le W+e^{3\eta R_h/4}W\varepsilon_M\le2W\) by (F4), and Theorem A(iii) with \(Y=Z_0^\sharp\) gives \(\|\mathsf r_0-\mathsf r_{00}\|\le2U_rr/r_{\rm LG}\).

Adding the four terms and the \(C\) part gives (B3) with \(H_0\) of (9.1), using \(r\le L^3(a_1+a_2)\).

*(B4).* By (B3), (F4) and (C2), \(\|\Gamma\|\le\|\Gamma_*\|+1\le K_0+1\). For \(|\tau-1|\le\tfrac12\), \(|\tau^{-1}-1|=|\tau-1|/|\tau|\le2|\tau-1|\), and \(|\tau^{1/2}-1|=|\tau-1|/|\tau^{1/2}+1|\le|\tau-1|\), since the principal root has positive real part. So \(\|\tau^{-1}C-C\|+\|\tau^{1/2}\Gamma-\Gamma\|\le(2\|C\|+\|\Gamma\|)|\tau-1|\le C_\tau|\tau-1|\). Add (B3). \(\square\)

*Status.* Proved here, as an implication from the imports listed in the hypothesis.

**Remark 9.1 (the open disc).** IN1 asks for \(|s_\Delta|<e^{\bar\kappa}\). Theorem B gives the closed disc, which is stronger.

**Remark 9.2 (no \(a_0\) term).** The reference is taken at the actual real factor \(U\), not at the flat field. So the curvature radius \(a_0\) enters only the admissibility ceiling (C1), not the perturbation. SA's \(LMa_0\) term (SA 14189) comes from comparing with the flat operator, which is not done here.

**Remark 9.3 (where the global gap went).** The real gap R is used only inside Lemma 4, for the global operator at a box-extended axial field, and inside Theorem A(iv) at whole-torus triples. The hull-restricted form is never inverted away from the collar, as SA 14202–14205 require.

**Remark 9.4 (completed gauge form).** If the step uses \(\mathsf A_{\rm full}=\mathsf A-E_{\rm free}[J_{\rm GF}]\) (pr-lay (9)), add the entries of \(-E_{\rm free}\) as short labels with hull the ball of radius \(r_F+O(1)\) about each argument. They vanish at \(P_0\) and have entries at most \(C_Fr(P)\) (pr-lay F). Lemma 4 is unchanged; Lemmas 2(b) and 5 change \(H_1\) to \(H_1+E_FV\) with \(E_F,V\) as in pr-lay Lemma 4, and the ceiling \(r_{\rm LG}\) shrinks by a fixed factor. Nothing else changes.

---

## 10. Theorem C: the structural clauses

**Theorem C.** Under the hypotheses of Theorem B:

**(C-hol) Holomorphy and reality (M7).** \(C(s;P)\), \(\Gamma(s;P)\) and \(D(s;P)\) are jointly holomorphic in \((s_\Delta)_{\Delta\subset Z\setminus Z_0^\sharp}\) on \(|s_\Delta|<e^{\bar\kappa}\) and in \((A',\mathbf J)\) at fixed \(U\) on the core, and real at real \(s\) and real pairs.

*Proof.* Each tagged term is a polynomial in finitely many \(s_\Delta\) times a function holomorphic in \((A',\mathbf J)\). By Step 1 of §9.2, (3.2) and Theorem A(ii), the series (7.2) and (7.3) converge normally on the closed polydisc and uniformly on the core. A normally convergent series of jointly holomorphic functions is jointly holomorphic. \(C\) is the inverse of a holomorphic matrix with \(\operatorname{Re}\ge c_L/2\), hence holomorphic; \(\Gamma\) and \(D\) are products. Reality is termwise. \(\square\)

**(C-norm) Normalization (M4).** If \(H_0\{\varepsilon_M+L^3(a_1+a_2)\}+C_\tau|\tau-1|\le\varepsilon_0(K_0)\), then \({\cal J}(Z_0;s;P)[1]=1\) and \({\cal J}[F]=\int F\,d\mu_D\).

*Proof.* (B1)–(B4) give FG1 with \(K=K_0\) and \(\varepsilon\le\varepsilon_0(K_0)\). Apply FG6 (SA 13961–13967). \(\square\)

**(C-her) Heredity (M5).** Let \(Z\subset Z'\) be unions of coarse cubes, \(P'\in\mathcal K(Z')\) and \(P=P'|_Z\). With \(s_Z\) extended by zero to \(Z'\), \(C(s_Z;P')=C(s_Z;P)\) and \(\Gamma(s_Z;P')=\Gamma(s_Z;P)\). Hence \(D\), \({\cal J}(Z_0;s_Z;\cdot)[F]\) and the UM term \(T(Z,\iota)\) of SA (UM3) are functions of \(P|_Z\) alone, and the value at \(P'\) is the value at its restriction.

*Proof.* At \(s_Z\) the surviving labels are those with hull in \(Z\) (Definition 7.2), and each depends only on the data on its hull (Lemma 1; Theorem A(i)). The UM term integrates \(\partial_{s_\Delta}\) over \(s_\Delta\in[0,1]\) for \(\Delta\subset Z\setminus Z_0^\sharp\); the derivatives exist by (C-hol). The integrand \(F_{\mathbf D,P_0}\) of UM2 is supported in \(Z_0\) and its potentials are UM1's local potentials. \(\square\)

This is the statement SA uses at 14680–14682 ("values obtained by the assigned hereditary restrictions") and 14712–14713.

**(C-wall) Wall factorization (M6).** Let \(Z\supset Z_0^\sharp\) and let \(Z_1,\dots,Z_q\) be the wall-components of \(Z\).

(a) If some \(Z_i\) is disjoint from \(Z_0^\sharp\), then \(C,\Gamma\) do not depend on \((s_\Delta)_{\Delta\subset Z_i}\), and \(T(Z,\iota)=0\).

(b) If each \(Z_i\) meets \(Z_0^\sharp\), put \(Z_{0,i}=Z_0\cap Z_i\). Then \(D(s_Z;P)=\bigoplus_iD(s_{Z_i};P|_{Z_i})\) relative to \(I_0=\bigsqcup_iI_{0,i}\), where the \(i\)-th summand is built from \((Z_{0,i},Z_i)\) by Definition 7.5. If \(F=\prod_iF_i\) with \(F_i\) depending only on the coordinates of \(I_{0,i}\), then \({\cal J}(Z_0;s_Z)[F]=\prod_i{\cal J}(Z_{0,i};s_{Z_i})[F_i]\), and \(T(Z,\iota)=\prod_iT(Z_i,\iota_i)\).

*Proof.* Every surviving hull lies in \(Z\) and is nearest-neighbour connected (P-conn; §7, connectivity), so by (G2) it lies in one wall-component.

(a) A label of \(\chi\mathsf A\chi\) has an argument in \(I_0\), so its hull meets \(Z_0\subset Z_0^\sharp\) and lies in a component meeting \(Z_0^\sharp\). For \(\Gamma(x,z)=-\sum_yX(x,y)\mathsf r(y,z)\), the hull of the \(X\)-label contains \(\hat x\) and \(\hat y\), and the hull of the \(\mathsf r\)-label contains \(\hat y\) and \(\hat z\); both lie in the component of \(\hat x\). So no surviving term of \(C\) or \(\Gamma\) has a hull meeting \(Z_i\), and no \(s_\Delta\), \(\Delta\subset Z_i\), occurs. Then \(\partial_{s_\Delta}{\cal J}=0\) for such \(\Delta\), and the UM term vanishes.

(b) By the same argument, \(\chi\mathsf A(s_Z)\chi\) has no entry between \(I_{0,i}\) and \(I_{0,j}\), \(i\ne j\), and is block diagonal; so is its inverse \(C\). In \((\Gamma\Gamma^{\mathsf T})(x,x')=\sum_z\Gamma(x,z)\Gamma(x',z)\), a nonzero summand needs \(\hat z\) in the component of \(\hat x\) and in that of \(\hat x'\); so \(\Gamma\Gamma^{\mathsf T}\) is block diagonal and \(D\) is block diagonal. The \(i\)-th block equals the construction for \((Z_{0,i},Z_i)\): its surviving labels are those with hull in \(Z_i\); the collar of \(Z_{0,i}\) is \(Z_0^\sharp\cap Z_i\), by (G3) applied to each corner-component of \(Z_0\) and the chain argument in its proof; and in \(X\) the condition \(\hat y\notin Z_0\) reduces to \(\hat y\notin Z_{0,i}\) for \(\hat y\in Z_i\). A normalized Gaussian with block-diagonal covariance is the product of its block marginals: the density factorizes, and the branch of \((\det D)^{-1/2}\), continued from the positive reference (FG3), is the product of the block branches, because both are continuous along the segment from the reference, agree there and have the same square. The UM index \(\iota=(\mathbf D,P_0)\) splits accordingly: each selected tagged domain is corner-connected, hence (G3) in one component, and each failed bond lies in one fine cube. The derivative-integrals in UM3 factor over components. \(\square\)

This is SA's "Disconnected regions factor into their wall-components" (SA 14370–14371) and the structural hypothesis of SA 14406–14412.

**(C-dim) Local dimension (M9).** \(m=|I_0|\le n_c\ell^4\,\#\{\Delta\subset Z_0^\sharp\}\le12(LM)^4N\), \(N=\#Z\).

*Proof.* \(I_0\) consists of coordinates with base points in \(Z_0\subset Z_0^\sharp\); a coarse cube has \(\ell^4\) base points and each carries at most \(n_c=12\) coordinates. \(\square\)

**(C-gas) The finite decoupling identity.** For each index \(\iota\), with \(\Lambda\) all coarse cubes and \(\mathbf1\) the all-ones assignment,
\[
 {\cal J}(Z_0;\mathbf1;P)[F_\iota]=\sum_{Z\supset Z_0^\sharp}T(Z,\iota),               \tag{10.1}
\]
for every triple \(P\) on \(\mathbb T\) for which Theorem B holds with \(Z=\mathbb T\).

*Proof.* Put \(f(s)={\cal J}(Z_0;s;P)[F_\iota]\) for \(s\in[0,1]^{\Lambda\setminus Z_0^\sharp}\), with \(s=1\) on \(Z_0^\sharp\). By (C-hol) and (C-norm) \(f\) is \(C^1\) on a neighbourhood of the cube (the polydisc has radius \(e^{\bar\kappa}>1\)). For one variable, \(f(s)=f(s|_{s_\Delta=0})+\int_0^1\partial_{s_\Delta}f\,ds_\Delta\). Iterating over the finitely many cubes gives
\(f(\mathbf1)=\sum_{S\subset\Lambda\setminus Z_0^\sharp}\prod_{\Delta\in S}\int_0^1ds_\Delta\,\partial_{s_\Delta}f(s_S,0)\). The summand for \(S\) is \(T(Z_0^\sharp\cup S,\iota)\). By (C-wall)(a) the terms with a wall-component disjoint from \(Z_0^\sharp\) vanish. \(\square\)

**(C-phys) Physical identification (M8).** Let \(P_W\) be a complete physical pair admitted by pr-lay Theorem 8, with \(r(P_W)\le r_{\rm LG}/2\). Then
\[
 D(\mathbf1;P_W)=\chi\,\mathsf A(P_W)^{-1}\chi ,                     \tag{10.2}
\]
so \({\cal J}(Z_0;\mathbf1;P_W)[F]\) is the expectation of \(F(b|_{I_0})\) under the centred Gaussian on \(\mathbb R^I\) with covariance \(\mathsf A(P_W)^{-1}\). Under G-ID this is the marginal on \(I_0\) of the step's actual Gaussian fluctuation law, and by (10.1) the UM gas reproduces it.

*Proof.* At \(s=\mathbf1\) all labels survive with weight one, so \(\mathsf A(\mathbf1)=\sum_\omega\bar A_\omega=\mathsf A\) (Definition 7.1) and \(\mathsf r(\mathbf1)=\mathsf A^{-1/2}=:\mathsf R\), symmetric (Theorem A(iv)). Write \(\mathsf A=\begin{pmatrix}a&\beta\\ \beta^{\mathsf T}&\delta\end{pmatrix}\) relative to \(I=I_0\sqcup I_0^c\). Then \(C=a^{-1}\), \(X=(0\ \ \beta)\), \(\Gamma=-\beta\mathsf R_{2\cdot}\), where \(\mathsf R_{2\cdot}\) is the block of rows of \(\mathsf R\) in \(I_0^c\). Since \(\mathsf R\mathsf R^{\mathsf T}=\mathsf R^2=\mathsf A^{-1}\),
\(\Gamma\Gamma^{\mathsf T}=\beta(\mathsf A^{-1})_{22}\beta^{\mathsf T}\). With the Schur complement \(\sigma=\delta-\beta^{\mathsf T}a^{-1}\beta\), block inversion gives \((\mathsf A^{-1})_{22}=\sigma^{-1}\) and \((\mathsf A^{-1})_{11}=a^{-1}+a^{-1}\beta\sigma^{-1}\beta^{\mathsf T}a^{-1}\). Hence \(D=C+C\Gamma\Gamma^{\mathsf T}C=(\mathsf A^{-1})_{11}\). (Here \(a\) is invertible by (B2) and \(\sigma\) is invertible because \(\mathsf A\) is.) The marginal of a centred Gaussian on a coordinate subset has the corresponding block of the covariance. \(\square\)

*Status of Theorem C.* Proved here. (C-phys) rests on the import G-ID for the words "actual fluctuation law"; the matrix identity (10.2) itself is proved.

---

## 11. Relation to IN1 Lemma 2, to SA's formula, and why local cores need Lemma 1

### 11.1 IN1 Lemma 2 and its chain example

IN1 Lemma 2 (in1.md 276–327) uses path weights \(B^s_{xy}=B_{xy}\prod_{\Delta\in D(x,y)}s_\Delta\) on a fixed geodesic, and the **global** root \(R(A(P))\), weighted afterwards: \(\Gamma=-\chi A(P)^s(1-\chi)R(A(P))^s\). The present family differs in three ways.

1. Tags are assigned by the **full read hull** of each labelled coefficient, not by a geodesic between its arguments.
2. The root coefficients are **grouped local polynomials** (Definition 7.3) integrated in \(t\), not entries of the global functional calculus \(R(A)\).
3. The premises are local (Lemmas 4–5), not a global gap at the pair.

So this family is **not** identified with Lemma 2's at \(s\ne\mathbf1\), and no such identification is needed: Theorem B proves IN1 (9) for the actual family directly. At \(s=\mathbf1\) and a whole-torus pair both give \(D=\chi\mathsf A^{-1}\chi\) (IN1 Lemma 2's last line; (10.2) here). IN1's estimate (21) is neither used nor implied.

*The chain example (in1.md 329–334).* There \(A=I-T\) on sites \(1,2,3\), \(T_{12}=t\), \(T_{23}=u\), \(Z_0=\{1\}\), collar \(\{1,2\}\), site \(3\) cut. In the present construction the cut means \(s_\Delta=0\) on the cube \(\Delta\ni3\). Every labelled coefficient whose hull contains site \(3\) is then zero by Definition 7.2, in particular every coefficient that reads \(T_{23}=u\). The surviving grouped coefficients are polynomials in entries whose hulls avoid site \(3\). So \(u\) enters no surviving term, and \(D\) does not depend on \(u\). The dependence found in IN1 comes from \(R_{22}=((I-T)^{-1/2})_{22}\), a coefficient of the global functional calculus; the present construction never forms it at \(s\ne\mathbf1\). This is the content of (C-her). In the real step, hulls have radius \(R_*\) rather than one site, so "contains site 3" reads "meets the cut cube"; the argument is the same.

### 11.2 SA's formula and the carrier-check caveat

The matrices (7.4) are SA's (SA 14164–14166) with SA's two unwritten expansions specified: the precision by the hull-tagged walk series (7.2), the inverse root by (7.3). `gates/carrier-check.md` §2 marks as wrong the claim that the outline "constructs none for the covariance", citing SA 10533–10550 and 10311–10338 as a construction scheme; its §6 passes the inv-root series as satisfying um-envelope (6), and adds: "Equality with another series at \(s\ne1\) is neither proved nor needed for these readers." The same holds here. Definition 7.4 is an explicit specification, a replacement for the outline's scheme, not a proof about another series. Its readers are SA 14160–14243 and UM1–UM30; they read only (M1)–(M9), which Theorems B and C supply.

Differences from `inv-root.md` §§3–5, all deliberate:

- the premise of (8.4) is the local ball gap of Lemma 5(b), not a global gap;
- tags live on coarse cubes of side \(LM\), as UM requires (SA 14160–14161, UM4);
- the grouped hull radius \(R_*\) contains the gap margin \(\rho_G+r+R_h\);
- majorants are uniform in the pair (entry \(\le\) operator norm, (8.4)), which makes Schwarz's lemma directly applicable in Theorem A(iii);
- the precision labels are symmetrized (Definition 7.1), so \(C\) is complex symmetric as FG1 requires;
- the collar is taken in corner adjacency (§3.1, Remark).

### 11.3 Why extension cannot replace Lemma 1

A tempting route is to extend each local core triple to a regular pair on the whole torus and apply h-walk and pr-lay there. This fails for general unions of coarse cubes.

*Example.* Let \(\Delta_1=[0,\ell)^4\) and \(\Delta_2=\Delta_1+\ell(e_1+e_2)\); they share a two-dimensional face and no wall. Let \(Z\) consist of \(\Delta_1,\Delta_1+\ell e_3,\Delta_1+\ell(e_1+e_3),\Delta_1+\ell(e_1+e_2+e_3),\Delta_2\). It is wall-connected; the cubes \(\Delta_1+\ell e_1\) and \(\Delta_1+\ell e_2\) are not in \(Z\). Take \(U=\mathbf1\), \(\mathbf J=0\), and \(A'_3=\varphi X\) with a fixed unit colour vector \(X\), \(\varphi=c\) on \(\Delta_1\), \(\varphi=-c\) on \(\Delta_2\), and \(\varphi\) interpolating linearly along the three intermediate cubes, other components zero. A plaquette or difference stencil with sites in both \(\Delta_1\) and \(\Delta_2\) has a site in \(\Delta_1+\ell e_1\) or \(\Delta_1+\ell e_2\), so it is not a read in \(Z\). On reads in \(Z\), \(|A'|\le c\) and \(|\nabla_UA'|\le2c/\ell\). So R4 holds with \(a_0\) arbitrary, \(a_1>c\). (R5–R6 concern towers of averages of this smooth configuration; I have not checked them for this example. It is an illustration, not a load-bearing step.)

Suppose \(\widetilde P=(\widetilde U,\widetilde A',\widetilde{\mathbf J})\) is a regular pair on \(\mathbb T\) agreeing with \(P\) on the bonds of \(Z\), with real bound \(r_0\) and \(r(\widetilde P)<r_*\). Let \(p_1=(\ell-\eta,\ell-\eta,0,0)\in\Delta_1\), \(p_2=(\ell,\ell,0,0)\in\Delta_2\), and let \(g\) be the transport of \(\widetilde U\) along the two bare links \(p_1\to p_1+\eta e_1\to p_2\). The loop formed by these two links and a lattice path back from \(p_2\) to \(p_1\) through the three intermediate cubes (where \(\widetilde U=\mathbf1\)) bounds a ladder of at most \(4\ell/\eta+4\) plaquettes. Non-abelian Stokes for unitary fields (telescoping, as in pr-lay Lemma 6) gives \(|g-\mathbf1|\le(4\ell/\eta+4)\,r_0\eta^2\le8r_0\ell\eta\). Two covariant difference steps give
\[
 |\widetilde A'_3(p_1)-\operatorname{Ad}(g)\widetilde A'_3(p_2)|\le2\eta\max|\nabla^{\widetilde U}\widetilde A'|,
\]
while the left side is \(c|X+\operatorname{Ad}(g)X|\ge c(2-2|g-\mathbf1|)\ge c(2-16r_0\ell\eta)\). For \(16r_0\ell\eta\le1\) this forces \(\max l^2|\nabla\widetilde A'|\ge c/(2\eta)\) at scale \(l\ge1\) near \(\Omega_{k+1}\), which exceeds \(r_*\) once \(\eta<c/(2r_*)\). Since \(\eta=L^{-k}\), at deep levels no regular extension exists, although the local triple is admissible.

A walk hull inside \(Z\) can contain the corner bonds at \(p_1\) and at \(p_2\), reached through the detour. So the term bound at this local triple cannot be obtained by evaluating a global term at an extension. Lemma 1 avoids extension: it evaluates each factor on its own cut-down box, and no box meets both corners without meeting a missing cube. Lemma 3 extends only from a box, where clamping works.

---

## 12. Constant order

Rows refer to frozen IN1's constant table (in1.md 225–236) and, inside it, to `c4-order.md`.

| Order | Choice | Depends on |
|---|---|---|
| IN1 rows 1–3 (c4 rows 1–6) | \(L\); walk constants and ceilings \(C_h,\delta_h,a_h\); \(M_1\), then \(R_1\), \(\rho=R_1M_1\) | unchanged |
| IN1 row 3 (c4 row 7) | A2 gap \(c_L\), ceiling \(a_R\) (import R); \(W,\eta,R_h\) (3.2); \(r_M\); then \(h,H_1,r_{\rm LG},a_\natural\) (5.2); \(\ell_0,\rho',\rho_G\) (6.2); \(a_s,b_s,\lambda,\varrho,r,\theta,n,\hat p_r,U_r,R_*\) (8.1)–(8.2) | \(L,M_1\), R, W only |
| IN1 row 4 | H-M's early constants: \(K_0,H_0,C_\tau\) (9.1), \(d=\theta/4\), \(b=32\); then FG constants \(A_{K_0},\varepsilon_0(K_0),\rho_0(K_0)\); then IN1 Lemma 3's \(W_0\); then \(\kappa,\Theta,\lambda\) | the row above |
| IN1 row 5 | \(\bar\kappa\); then \(M\) a power of \(L\) with (F1)–(F5) of (9.2), besides IN1's own floors | \(\bar\kappa\) and the early constants |
| IN1 row 6 | ceilings (C1)–(C3) of (9.3) on \(a_0,a_1,a_2=j_0,|\tau-1|\), besides IN1 (23) | \(M\) and the early constants |

No constant of H-M depends on a later one. (F3) and (F4) are the only places where \(\bar\kappa\) enters, and both are floors on \(M\). (C1) is the only place where \(M\) enters a ceiling; it is the ceiling SA 14148–14149 already imposes ("then the radii with \(CLMa_0\le a_{\rm w}\)"). The constants are uniform in depth, torus, cutoff, the region shapes and the core, because they depend only on \(L,M_1\) and the uniform imports.

---

## 13. Consequences for UM and for IN1

**Corollary 13.1 (UM4–UM6 and the cost).** Assume the imports of Theorem B, UM1's potential bounds, and IN1 Lemma 3's other displayed constraints. Then for every polymer \(Z\), every index \(\iota\) and every triple of the declared core of \(Z\) within the ceilings (9.3):

- (UM4) holds on the discs \(|s_\Delta|<R_s=e^{\bar\kappa}\), \(R_s>2\), with matrix perturbation \(\varepsilon\le\varepsilon_*\) and gap constant \(K=K_0\);
- (UM5) holds with \(c_m=12\);
- (UM6) holds by FG6 and FG12;
- (UM14) holds and \(C_0^{\rm UM}\le1\), with \(W_0\) fixed before \(M\).

*Proof.* Theorem B gives IN1 (9) with early \(K_0,H_0,b,d,C_\tau\) and \(H_p\equiv L^3\). This is exactly the hypothesis H-M uses in IN1 Lemma 3 (in1.md 336–371). That lemma fixes \(W_0\) by (22) before \(M\), imposes the floor \(H_0e^{b\bar\kappa-dM}\le\varepsilon_*/2\) on \(M\), which is a floor because \(M^4e^{-dM}\to0\), and the later ceiling \(H_0H_p(a_0+a_1+j_0)+C_\tau|\tau-1|\le\varepsilon_*/2\); it concludes UM14 and \(C_0^{\rm UM}\le1\). (UM5) is (C-dim). The structural hypotheses of SA 14406–14412 (heredity, normalized functional, wall factorization) are (C-her), (C-norm), (C-wall), and the identification with the finite expansion on complete physical pairs is (C-gas) with (C-phys). \(\square\)

**What this gives FINISH row 274.** The exact four-dimensional claim recorded in `um-novelty.md` (all declared complex pairs, UM15 cost at most one fixed before \(M\)) now has a written supply, conditional on the imports R, W (with h-walk's inputs), (I2), (Ax), (Rep), and G-ID for the physical clause. "All declared complex pairs" here means every triple of SA's core R4 on the polymer's domain, with local real factor and local independent current, within the ceilings (9.3). The abstract Gaussian comparison, the hull-tagging idea and the local-resolvent method are Sussman–Alpoge's (SA 13894–14089; YM3 39839–40569); the four-dimensional parts written here are Lemmas 1, 3 and 4 (local precision bounds and the local real gap without gauge covariance), Theorem A's local series, and the explicit early constants. Whether this is a contribution worth sending is for the owner; nothing outward follows from this draft.

**IN1's Outstanding note (line 108).** If this draft survives distil and referee, the note can be replaced by: "H-M is proved in `hm-draft.md` for the actual collared family on the R4 cores, conditional on R, W, (I2), (Ax), (Rep) and, for the physical clause, G-ID." That is a lead decision, not made here.

---

## 14. Hostile check of the newest steps

I attacked each new step as a skeptic. Findings:

1. **Lemma 1 is a reading, not a proof.** The bounds (6.2), (7.1), (7.3) of h-walk are proved by chaining cut-down inverses. I read those proofs (h-walk 243–345, 381–389) and found no use of the global \(K^{-1}\) in the per-term bounds. But h-walk states them only at regular pairs of the whole sequence, and Lemma L's proof (h-walk 223–242, not read in full) uses (I1) "on every separated sequence"; I rely on h-walk's sentence that the cut-downs are such sequences and on (C4)'s local clause. **Believed, checked by reading only.** A referee should verify Lemma L at cut-downs with only local data.
2. **(I2) for non-smooth \(u\).** Lemma 3 uses a gauge transformation equal to \(u_\flat\) at block centres and \(\mathbf1\) elsewhere. Balaban's covariance is an algebraic identity for any \(u\) (the average transports to centres), so I believe (I2) applies. h-walk imports (I2) without proof. **Import.**
3. **(Ax) reading.** If the step's representative were a global gauge condition linking blocks, Lemma 3(b) would fail as written. pr-lay §1 says "block axial on the active blocks", and h-walk (H3) records covariance of \(A^{\rm loc}_\kappa\) under block-constant transformations, the residual freedom of a blockwise gauge. **Reading, well supported; flagged.**
4. **Units.** I took SA's level-\(k\) units with mesh \(\eta_k\) equal to pr-lay's. If they differed by a fixed power of \(L\), Lemma 0 changes by that power. **Bookkeeping risk only.**
5. **R at extended fields.** R is stated for every axial real \(U\) with real bound below \(a_R\) (pr-lay §2 and Theorem 3's hypothesis "every axial real \(U\) with real bound \(r_0<h/2\)"). \(\widetilde U_c\) is such a field. It need not be a critical background, and R does not ask for one. **Checked against the statement.**
6. **Is the collar distance used correctly?** (G1) needs corner adjacency; with SA's wall adjacency a second layer is needed. I made this explicit (§3.1). Without it, (B1) would fail at coarse corners. **Repaired in the definition.**
7. **Two tags in \(\Gamma\).** The product of a varied \(\mathsf r\)-label with an \(X\)-label carries two tag sets. I bounded both by Step 1 (\(e^{32\bar\kappa}\)), which is why \(b=32\). The single-tag bound \(16\) would be wrong for \(\Gamma\). **Checked.**
8. **Holomorphy of \(r_\alpha\) needs a pair-uniform majorant.** The Cauchy–Schwarz row bound of inv-root (14) is pair-dependent through the operator norm only; I replaced it by the entrywise bound (8.4), uniform on \(\mathcal W(Y)\). The cost is the power \(r^4\) in \(\hat p_r\) instead of \(r^2\). **Checked.**
9. **Does Lemma 4 need the box to sit in a two-scale zone?** No: every point scale is at most \(L\), so \(\xi|A^{\rm ext}|\le L\alpha_U\) holds everywhere, including finer layers and the bare layer. An earlier version of this argument imposed an extra floor on \(R_1\); it is not needed. **Removed.**
10. **The example of §11.3 uses R4 only.** It is not load-bearing; it explains why extension is avoided. **Flagged as illustration.**
11. **Symbols.** \(\eta\) denotes both the bare mesh (§3.1, Lemma 3, Definition 3.2) and the moment rate \(\eta_W\) of (3.2); \(\rho\) is the layer gap and \(\varrho\) the contraction factor. The distiller should rename.

What I derived: every lemma and theorem in §§3–10 and the example in §11.3, step by step as written. What I only believe: item 1 (that h-walk's per-term proofs are local, beyond what I read) and item 2 (that (I2) holds for the transformations used).

---

## 15. Status summary

- **H-M for the actual collared family:** proved here (Theorems B and C), as an implication from R, W (with h-walk's inputs (I1)–(I3)), (I2), (Ax), (Rep), and G-ID for the words "actual fluctuation law" in (M8). The quantifier covers every triple of SA's core R4 on the polymer's domain, with local real factor and local complex pair.
- **Identification with IN1 Lemma 2:** not made and not needed; the direct proof replaces it (§11.1).
- **Heredity, wall factorization, enlarged discs, physical identification:** proved (Theorem C; Theorem B on the closed polydisc \(|s_\Delta|\le e^{\bar\kappa}\); (10.2)).
- **Constants:** \(K_0,H_0,d=\theta/4,C_\tau\) and \(b=32\) depend only on \(L,M_1\) and the uniform imports, so they precede \(\kappa,\bar\kappa,M\); \(H_p\equiv L^3\).
- **First remaining Outstanding inside H-M:** none. The physical clause rests on G-ID, an existing import (SA 14108–14118 sketched; pr-lay (9)). Admission of the program's actual chain domains into R4 cores with the ceilings (9.3) is pr-lay's D, Outstanding there and outside H-M.
- **UM:** (UM4)–(UM6), (UM14) and \(C_0^{\rm UM}\le1\) with \(W_0\) fixed before \(M\) follow by IN1 Lemma 3 (Corollary 13.1), given UM1's potentials.
- **Checks still needed:** Codex distillation; a fresh-session referee, looking hardest at Lemma 1 (item 1 of §14), Lemma 3(b) and Lemma 4.

This is research text. It grants no status. No computer-assisted step is used; every step is a written inequality or identity intended to be formalizable.
