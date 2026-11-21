# Cls: the collared-hub family in IN1's class — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05, one session, in a clone of the planning folder. Pass 1 of (Cls), the amendment check on frozen IN1 that `drlocp-draft.md` §6.2 left as the first Outstanding statement on CI's path. Research text. It is not an audit and grants no status. No other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen. No frozen file was edited; §9 is a *proposed* Amendment 2 to IN1.

No step rests on a computation. Every argument is a finite union or inclusion of cube sets in a graph metric, a floor/ceiling inequality, a geometric series, a rooted tree count (a depth-first traversal code, as in IN1 Lemma 9), or a comparison of explicit numbers. Each is meant to be Lean-formalisable.

Credit. The relative length with an exempt family, the class bound (R23), the class rule with its nested boxes, the running-minimum radius with its drop rule, the three fates of a component, and the "no circle" and "no growth" arguments of the closed induction are the work of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the outline `ym4.tex` ("SA"), revision `31a47c543775`. The large-field induction they follow is Tadeusz Balaban's (CMP 116, 119, 122); Jonathan Dimock's expositions are the readable versions. Library notes keep their authors: `in1.md`, `td.md`, `td2.md`, `ci-form.md` (Codex distillations of Claude drafts); `ag1.md`, `tp1.md`, `st1-r4.md` (frozen); `drlocp-draft.md` (Claude).

Line references. SA L = `scratchpad/sa/ym4.tex`. Library notes by short name: IN1 = `in1.md` (frozen, with Amendment 1); TD = `td.md`; TD2 = `td2.md`; CI = `ci-form.md`; AG1 = `ag1.md` (frozen); TP1 = `tp1.md` (frozen); ST1 = `st1-r4.md` (frozen); DRL = `drlocp-draft.md`. I give the line before I say what a source states. "States" means that the text at those lines says so; it does not mean that the source proves it. SA is paraphrased, not quoted.

Status words: **[P]** proved here, not checked; **[I]** import, with owner; **[R]** reading of a source, flagged; **[O]** Outstanding; **[CE-route]** a counterexample to an implication used by a proof route (not to the statement); **[design]** a choice we are free to make.

Notation clash, fixed here. DRL's collar ratio is \(\eta=4\lambda_P/(a/2-6)\). TD2 74 uses \(\eta\) for \(1+C_{\rm isl}/10\); I write that one \(\eta_o\). TD2's integer collar width \(c\) is DRL's \(c_{\rm col}\); I write \(c\).

---

## 0. Result

**(Cls) as stated is not proved.** It replaces SA's hulls by the fixed collared hubs \(\widehat H_i^+=N_{\lceil\eta s_H\rceil+3}(\widetilde H_i^+)\), formed afresh at each step from the current hub. Two defects block it, each with an exact mechanism (§7):

- **(D1) The fixed collar does not iterate** [CE-route]. DRL Theorem 3 at step \(t+1\) needs every read of an old exempt term that lies near a hub to lie in the *hub* \(\widetilde H^+_{t+1}\) (TD2 76–80, X°). A term filed at step \(t\) reads the pair on its whole member \(\widehat H_t^+\) (DRL Proposition 5.1′). After a scale drop (SA 17334), the level-\((t+1)\) cells have the same physical size as the level-\(t\) cells, so the coarsened old collar is again a full collar of the current hub: the old reads reach within \(c+7\) cubes of the boundary of the step-\((t+1)\) base (Proposition 7.1). An attachment there pays root weight at most \(c+8\). Its connector through the hub still costs about \(s_H\), and the literal relative length charges that. DRL's payment \(l_c\ge\eta s_H\) fails, and the Theorem 3 majorant diverges as \(\gamma\downarrow0\). This is the precise sense in which fixed collars accumulate.
- **(D2) Replacement removes an exemption that old producers use** [R]. Under replacement, a slot \(X\) that contains a hull \(H\) but not its collared hub loses its exemption, so the old bound \(e^{-\kappa d^\natural_{\rm old}(X)}\) no longer implies the new one. Re-filing such slots at \(X\cup\widehat H^+\) merges distinct slots, so the fixed \(\mathsf B\) would have to grow with the collar (§7.3).

**The repaired statement (Cls⁺) is proved** [P, conditional on the imports that IN1, TD, TD2 and DRL already name, and on no new import]. It changes the family in two ways:

1. *Add members to SA's hulls; do not replace them:* \(\mathsf H^+_j=\{H_j(\alpha)\}\cup\{M_j(\alpha)\}\).
2. *Members are recursive.* Each member is built around a core \(R_j(\alpha)\) that contains the coarsened member of the previous step: \(R_{j+1}=\widetilde H^+_{j+1}\cup\pi(M_j)\), \(\rho_j=\lceil\eta\,s(R_j)\rceil\), \(M_j=N_{\rho_j+3}(R_j)\). At an island's first standing step, \(R=\widetilde H^+\) and \(M\) is exactly (Cls)'s collared hub.

Theorem C (§6) proves that IN1's class \(\mathfrak L_k(\theta)\), with the boundary bound (12) and the oscillation clause (18) taken with \(d^+_j(\mathcal S;X):=d^\natural_{j,\mathsf H^+_j}(X)\) (SA's literal relative length, crossings charged), satisfies IN1's induction: Theorems 10–12 and the step. The proof has four parts.

- **Monotonicity** (Lemma 2.2): \(d^+_j\le d^\natural_j\) for every \(X\). Every producer that returns SA's bound returns the new one, and no slot is moved.
- **No accumulation** (Lemma 3.2): the width \(e_j\) of the core over the hub obeys \(e_j\le1.16\,\eta(D_H(j)+2c)+1.32\) at every step. The bound is uniform in the island's age. The reason is that after a scale drop the old collar is absorbed into the core, and a coarsening by \(L\) then shrinks it at every step without a drop.
- **Member geometry with \(2C_{\rm isl}\)** (Lemma 3.3): members lie in non-wrapping boxes of side \(2C_{\rm isl}L\check R_j+6\), are mutually separated by \(\check R_j/2\), and sit within \(\check R_j/(6(C_{\rm isl}+1))+c+12\) of their hubs.
- **Every use of the excused family survives.** There are 17 uses (§1, table U1–U17); §4–§6 handle each.

**Constants.** \(C_{\rm isl}\) is doubled only where it bounds the excused sets (member boxes in AG1 Lemma 2, Lemma LD, the entropy count). Every independent constant in IN1 rows 1–10 is unchanged. The changes are these:

- DRL's ceiling (F3) \(\eta\le1/(16(C_{\rm isl}+1)L)\) is strengthened to **(F3♯)** \(\eta\le\eta_\sharp:=\min\{1/(16(C_{\rm isl}+1)^2L),\,1/(4+2c)\}\). This is a floor on \(\bar\kappa\) depending on \(\lambda_P,C_{\rm isl},L,c\), all of which come earlier.
- AG1's floor \(\bar\kappa\ge4\kappa_PC_0^{\rm isl}\) becomes \(\bar\kappa\ge8\kappa_PC_0^{\rm isl}\), and its derived \(c_g\) is recomputed.
- Two new \(\gamma\)-ceilings appear: \(\check R\ge\check R_\sharp\) and (8♯).
- If one derives the per-cube entropy prefactors \(C_B^{\rm ent}\) and \(C_{\rm ex}(M)\) from the class bound alone, they grow by a factor of at most 40. Both are late and are read only through \(\gamma\)-ceilings.
- TD2's \(\eta_o=1+C_{\rm isl}/10\), its floor (14), and G's \(s_0,G_0\) are unchanged.

The order stays acyclic (§8).

**First remaining Outstanding statement.** Nothing new on (Cls⁺). The imports it uses were already Outstanding. Lemma 4.1 discharges one part of TD2 82 ("read-collar coverage") for the new family. What remains of TD2 82 is the scale conversion and the containment of excused sets in current cores. Containment is now the hull statement (Mon) of §2.3, which is TD2 82's own containment import with its old margin. For the literal (Cls), the first Outstanding statement is (D1). §7 gives the three attacks on it and why each fails.

**Line count**: reported in the session reply.

---

## 1. Sources and the uses of the excused family

### 1.1 SA

- *The relative length* (SA 6191–6198). For a finite family of nonempty regions, SA defines \(d^\natural_{j,\mathsf H}(X)\) as \(M^{-1}\) times a minimal tree length. The minimum is over subfamilies whose members are contained in \(X\). The tree must meet every cube outside the chosen members and must meet each chosen member, but need not fill it (6191–6195). For a label, SA takes the level-\(j\) hulls of the label's standing islands as the family (6196–6197). SA notes that the result is at most \(d_j(X)\) and gives no decay across an exempt island (6198).
- *The class bound* (SA 6199–6205): \(|B_{\mathcal S}(j,X,o)|\le\mathsf Be^{-\kappa d_j^\natural(\mathcal S;X)}\) (R23). A slot \((j,X,o)\) keeps its formation domain at later steps (SA 6187–6189).
- *Hulls are taken in level-\(t\) cells* (SA 17317). The boxing map replaces a small component by its bounding box. Free evolution coarsens, adds a 10-cell margin and boxes (SA 17325–17334).
- *The running-minimum radius* (SA 17334). \(\check R_k\) is the least power of \(L\) not below the \(r\)-th power of the log of the running minimum. Because it is a power of \(L\), the partitions are nested. It is non-increasing, \(\check R_k\le L\check R_{k+1}\), and two consecutive drops never occur. I write this as **(Drop)**: \(\check R_{t-k}\le L^{\lceil k/2\rceil}\check R_t\) for \(k\ge0\). *Proof* [P from SA 17334]: among \(k\) consecutive steps at most \(\lceil k/2\rceil\) are drops, and each drop is by a factor \(L\).
- *Class rule and boxes* (SA 17575–17583). The class components are small, quiet and quarantined. \(H_i\) is the level-\(i\) hull of \(X\cap Z_{i-1}\), and \(\Omega_i^c\cap X=H_i^{[8]}\), \(Z_i\cap X=H_i^{[10]}\). The boxes are nested, and no box or neighbourhood of a box wraps (17583).
- *Three fates* (SA 17415–17433). Healed, island, or drop-out. An island stays in \(Z_t\) as a component without inner regions, and its operation is kept (17418). A mark persists until a later healed component or island swallows it (17433).
- *The closed induction* (SA 19408–19523). Old terms enter a step in one of three ways: unchanged; through a difference with a small factor; or, in the main step of \(\mathbf R\), either with a domain stretching across \(c\check R_kL^{k-j}\) cubes of its own level (so its decay makes it small) or inside an enlarged component, where only a volume bound is used (19495–19499). The four ways boundary data enter, and why \(\mathsf B\) does not depend on itself, are at 19515–19520. A carried term is literally unchanged, and a standing island's bounds refer to its creation level (19523).

### 1.2 Library

- **IN1** (frozen). Line 44: the boundary hull length \(d^\natural_j(\mathcal S;X)\) is supplied. Lines 131–136: H-SF returns \(|B^{(k+1)}(X)|\le\mathsf Be^{-\kappa d^\natural_{k+1}(\mathcal S;X)}\). The boundary-origin bounds do not depend on \(\mathsf B\), and old boundary data enter only through a vanishing difference factor, a long-domain exponential, or a volume cost chosen after \(\mathsf B\) (136). Lines 197–204: H-O (18), the oscillation of island factors with \(e^{-\kappa d_i^\natural(\mathcal S;R)}\). Line 217: the class requires (12) and (18). Line 228: row 2 fixes the geometric and hull constants. Line 233: row 7 chooses \(\mathsf B\), then the volume costs, and \(c_1\ge\dots+c_{\mathsf B}\). Line 417 (Lemma 5): the boundary maximum is chosen first, and its difference, long-domain and volume parts are handled later. Lines 540–633: Theorems 10–12. Lines 649–674: change log and Amendment 1.
- **TD** 65–71: X, with boundary lengths as SA relative lengths and the per-cube sum (6). TD 73: G, with standing-island hulls \(H\), \(\widetilde H=N_2(H)\), separation \(s_0=\check R_i-4\), box side \(D_H\), gap \(G_0=10L\check R_i-2\). TD 75–90: the contracted graph \(\Gamma^\natural\), (7), (8). TD 443–445: Proposition 11, the literal reading.
- **TD2** 35: G with \(D_H=C_{\rm isl}L\check R_i+6\). TD2 73–74: G-ord, with \(\eta_o=1+C_{\rm isl}/10\). TD2 76–80: X°. TD2 82: Outstanding supply of X° (scale conversion, read-collar coverage, containment of each excused hull in a current hub). TD2 86–158: Lemmas 1–2 and Theorem 3. TD2 162–182: the order. TD2 365: the filing inputs, including the scale/hull comparison.
- **CI** 30: a term is exempt if its carrier meets the live set or its boundary-hull definition exempts an island. CI 352: filing into IN1's slots uses the scale and hull comparison.
- **AG1** 333–361: (L-B), (N-B), the read hull as a tree plus exempt hulls, and the island geometry inputs. AG1 463–482: Lemma 2's exempt-hull path argument.
- **DRL** 383–472: §5, with the collared hubs, Lemma 5.0, Lemma 5.2 and Theorem 3. DRL 503–517: §6.2, the (Cls) statement and three attacks.
- **TP1, ST1**: a search of both (TP1 87–651; ST1 146, 191, 223) finds no use of the excused family. ST1 146 (GEO-mark) concerns standing marks and windows, not hulls; it is unaffected.

### 1.3 The uses (task 1)

| # | Where | What it reads of the family | Handled in |
|---|---|---|---|
| U1 | IN1 44 | definition of \(d^\natural_j\) | §2, Definition F |
| U2 | IN1 131–134, 217 | (12) as H-SF output and class clause | Lemma 2.2, Theorem C |
| U3 | IN1 136; SA 19517 | vanishing difference factor for old data | §5.1 |
| U4 | IN1 136; SA 19499, 19519 | long-domain exponential | Lemma 5.2 (LD) |
| U5 | IN1 136; SA 19520; IN1 233, 417 | volume cost \(c_{\mathsf B}\) inside enlarged components | Lemma 5.3 (ENT), §5.3 |
| U6 | IN1 197–204, 217 | (18), the oscillation of island factors | Lemma 2.2, §5.4 |
| U7 | IN1 228 (row 2) | geometric/hull constants (\(C_{\rm isl}\)) | §8 |
| U8 | IN1 666–674 (Amendment 1) | natural-window floors (TD♮) | §5.6 |
| U9 | TD 65–71 (X) | \(d_f^{\rm old}\) as the SA relative length; per-cube sum (6) | §4.3 |
| U10 | TD 73 (G); TD2 35 | hub geometry | Lemma 3.3 |
| U11 | TD2 73–80 (G-ord, X°) | \(C_{\rm isl}\), \(\eta_o\); reads near hubs | Lemma 4.1, Theorem B |
| U12 | TD2 86–158 | Lemma 1 (crossings), Lemma 2 (gap), Theorem 3 | Theorem B |
| U13 | TD 75–90, 174–200 | contracted \(\Gamma^\natural\), TD-natural | §5.6 |
| U14 | CI 30, 352 | exempt classification; scale/hull comparison | §5.5 |
| U15 | AG1 333–361, 463–482 | island-hull geometry, (L-B), (N-B), Lemma 2 | Lemma 5.4 |
| U16 | DRL §5 | collared hubs, Lemma 5.0, 5.2, Theorem 3 | Theorem A |
| U17 | SA 19523; DRL 507 | standing islands across steps (non-accumulation) | Lemma 3.2 |

IN1 also has a "creation-domain hull" \(\widetilde X\) in (7) (IN1 82, change log F2). It is a hull of a domain, not a member of the exempt family, and nothing here touches it.

---

## 2. Definitions

### 2.1 Graphs and coarsening

For each level \(j\), let \(\mathcal C_j\) be the graph of level-\(j\) \(M\)-cubes with corner adjacency (degree \(\le80\)). Its distance \(d\) is the sup-norm of integer cube indices, read on a non-wrapping lift (SA 17583). Write \(N_r(A)=\{x:d(x,A)\le r\}\), and \(s(A)\) for the side, in cubes, of the least axis-parallel box containing \(A\). A slot of level \(j\) measures its length in \(\mathcal C_j\): \(d^\natural_j\) counts tree edges in \(\mathcal C_j\) (SA 6192: \(M^{-1}\) times tree length). The step that forms level-\(j\) slots works in \(\mathcal C_j\). Any other unit convention is the scale conversion of TD2 82, which is unchanged here.

**(Nest)** [R: SA 17334, partitions nested]. Every cube of \(\mathcal C_{j+1}\) is a union of \(L^4\) cubes of \(\mathcal C_j\). Let \(\pi=\pi_j:\mathcal C_j\to\mathcal C_{j+1}\) send a cube to the coarse cube containing it, and extend it to sets.

**Lemma 2.1 (coarsening)** [P].

- (a) \(d(\pi x,\pi y)\le\lceil d(x,y)/L\rceil\).
- (b) \(\pi(N_r(A))\subset N_{\lceil r/L\rceil}(\pi A)\).
- (c) If \(T\) is a tree in \(\mathcal C_j\), then \(\pi(V(T))\) spans a connected subgraph of \(\mathcal C_{j+1}\) that has a spanning tree with at most \(|E(T)|\) edges.
- (d) \(s(\pi A)\le\lceil s(A)/L\rceil+1\), and \(s(A)\le L\,s(\pi A)\).

*Proof.* (a) Take one coordinate, with \(a-b=r\ge0\) and \(b=qL+u\), \(0\le u<L\). Then \(\lfloor a/L\rfloor-\lfloor b/L\rfloor=\lfloor(u+r)/L\rfloor\le\lfloor(L-1+r)/L\rfloor=\lceil r/L\rceil\); take the maximum over coordinates. (b) follows from (a). (c) Consecutive vertices of a tree path are adjacent (sup-distance 1), so by (a) their images are equal or adjacent. Hence \(\pi(V(T))\) is connected through images of edges, and those images number at most \(|E(T)|\); delete cycle edges. (d) The first part is (a) applied to the two extreme coordinates. For the second, a box of \(n\) coarse cubes per side covers \(nL\) fine cubes per side. ∎

### 2.2 Hulls and hubs

At level \(j\) the standing islands \(\alpha\) of the label have level-\(j\) hulls \(H_j(\alpha)\subset\mathcal C_j\) (SA 6196, 17317). The hub is \(\widetilde H_j=N_2(H_j)\) and the collared hub is \(\widetilde H_j^+=N_c(\widetilde H_j)=N_{c+2}(H_j)\). Put \(h_j=s(\widetilde H^+_j)\).

**G** [I, LF1 geometry; TD 73, TD2 35]: \(s(\widetilde H_j)\le D_H(j):=C_{\rm isl}L\check R_j+6\), so \(h_j\le D_H(j)+2c\) and \(s(H_j)\le C_{\rm isl}L\check R_j+2\). Distinct hubs are at distance \(\ge s_0(j)=\check R_j-4\). Gas cubes and the live set are at distance \(\ge G_0(j)=10L\check R_j-2\) from every hub. Boxes and their collars do not wrap.

### 2.3 Standing islands across steps

**(Mon)** [I, LF1 geometry: TD2 82's containment of each excused hull in a current hub; R: SA 17418, 17433, 19523]. If \(\alpha\) stands at level \(j\), then exactly one of three things holds at level \(j+1\):

- (i) \(\alpha\) stands, and \(\pi(H_j(\alpha))\subset N_2(H_{j+1}(\alpha))\);
- (ii) \(\alpha\) has been swallowed by an island \(\beta\) standing at \(j+1\), and \(\pi(H_j(\alpha))\subset N_2(H_{j+1}(\beta))\);
- (iii) \(\alpha\) has been swallowed by a healed component.

Write \(\alpha'=\alpha\) in case (i) and \(\alpha'=\beta\) in case (ii).

*Reading.* An island's region is fixed after creation (SA 19523), and hulls are unions of cells of nested partitions (SA 17317, 17334). The level-\((j+1)\) hull of a fixed set is a union of level-\((j+1)\) cells and contains the set, so it contains every level-\(j\) cell meeting the set. Hence \(\pi(H_j)\subset H_{j+1}\) when the hull is the cell cover or its bounding box. This is stronger than (i)/(ii) by two layers. I use only the weaker form, which is literally TD2 82's import ("containment of each excused hull in a current hub", with the hub \(N_2(H)\)). A swallowing island's region contains the swallowed one (SA 17433), which gives (ii). Case (iii) is SA's healed case and is treated in §5.3.

### 2.4 The recursive members — Definition M [design]

Fix \(\eta\in(0,\eta_\sharp]\), with
\[
 \eta_\sharp:=\min\Big\{\frac1{16(C_{\rm isl}+1)^2L},\ \frac1{4+2c}\Big\}.
\]
For an island \(\alpha\) at its first standing level \(j_0\), put \(R_{j_0}(\alpha)=\widetilde H^+_{j_0}(\alpha)\). Recursively,
\[
 \rho_j(\alpha)=\lceil\eta\,s(R_j(\alpha))\rceil,\qquad
 M_j(\alpha)=N_{\rho_j(\alpha)+3}(R_j(\alpha)),\qquad
 R_{j+1}(\beta)=\widetilde H^+_{j+1}(\beta)\ \cup\bigcup_{\alpha:\ \alpha'=\beta}\pi\big(M_j(\alpha)\big).
\]
The union runs over \(\beta\) itself (if it stood at \(j\)) and over the islands it swallowed at \(j+1\). The **base collar** around \(\alpha\) is \(\widehat R_j(\alpha):=N_{\rho_j(\alpha)+2}(R_j(\alpha))\), so \(N_1(\widehat R_j)=M_j\).

At \(j=j_0\), \(M_{j_0}=N_{\lceil\eta h_{j_0}\rceil+3}(\widetilde H^+_{j_0})\), which is DRL's \(\widehat H^+\) (DRL 389). Members depend only on the island's own hull record and on \(\eta\). They are formed from the history alone (SA 19410: regions and histories depend on \(\theta\) only).

### 2.5 The family and the length — Definition F [design]

\[
 \mathsf H^+_j:=\{H_j(\alpha)\}_\alpha\cup\{M_j(\alpha)\}_\alpha,\qquad
 d^+_j(\mathcal S;X):=d^\natural_{j,\mathsf H^+_j}(X),
\]
with SA's literal rule (SA 6191–6195): chosen elements must be contained in \(X\), the tree meets every cube of \(X\) outside the chosen elements and each chosen element, and crossings are charged (TD 443–445).

**Lemma 2.2 (monotonicity)** [P]. For every \(X\), \(d^+_j(\mathcal S;X)\le d^\natural_j(\mathcal S;X)\le d_j(X)\). Hence every bound \(|B|\le\mathsf Be^{-\kappa d^\natural_j}\) implies \(|B|\le\mathsf Be^{-\kappa d^+_j}\), on the same slot and with the same \(\mathsf B\).

*Proof.* SA's family \(\{H_j(\alpha)\}\) is a subfamily of \(\mathsf H^+_j\), so every admissible pair for \(d^\natural_j\) is admissible for \(d^+_j\). The empty subfamily gives \(\le d_j\) (SA 6198). ∎

**Lemma 2.3 (normal form)** [P]. Every value of \(d^+_j(X)\) is attained by a pair \((\mathsf F,T)\) in which \(\mathsf F\) contains at most one element per island, and the chosen elements are pairwise disjoint.

*Proof.* If both \(H(\alpha)\) and \(M(\alpha)\) are chosen, drop \(H(\alpha)\). \(T\) still meets \(M(\alpha)\supset H(\alpha)\), and the set of cubes outside the chosen elements does not change, since \(H\subset M\). Elements of distinct islands are disjoint by Lemma 3.3(iii). ∎

*Why add members rather than replace hulls.* See (D2), §7.3. Adding keeps Lemma 2.2. Replacing does not: a slot containing \(H(\alpha)\) but not \(M(\alpha)\) would lose its exemption.

---

## 3. Non-accumulation and member geometry

### 3.1 The width recursion

Let \(e_j(\alpha)\) be the least integer \(e\ge0\) with \(R_j(\alpha)\subset N_e(\widetilde H^+_j(\alpha))\). So \(e_{j_0}=0\), and
\[
 s(R_j)\le h_j+2e_j,\qquad M_j\subset N_{e_j+\rho_j+3}(\widetilde H_j^+)=N_{e_j+\rho_j+c+5}(H_j).                          \tag{3.1}
\]

**Lemma 3.1 (one step)** [P from Lemma 2.1, (Mon)]. If \(\alpha'=\beta\) at level \(j+1\), then
\[
 e_{j+1}(\beta)\le\max_{\alpha:\alpha'=\beta}\frac{(1+2\eta)e_j(\alpha)+\eta\,(D_H(j)+2c)+1}{L}+1.2,                                            \tag{3.2}
\]
where the maximum includes \(\alpha=\beta\) if \(\beta\) stood at \(j\). The term is absent for a newly created \(\beta\) that swallowed nothing; then \(e_{j+1}(\beta)=0\).

*Proof.* By (3.1) and Lemma 2.1(b),
\(\pi(M_j(\alpha))\subset N_{\lceil(e_j+\rho_j+c+5)/L\rceil}(\pi H_j(\alpha))\).
By (Mon) this lies in \(N_{\lceil(e_j+\rho_j+c+5)/L\rceil+2}(H_{j+1}(\beta))\).
Since \(\widetilde H^+_{j+1}=N_{c+2}(H_{j+1})\), it follows that \(\pi(M_j(\alpha))\subset N_{e'}(\widetilde H^+_{j+1}(\beta))\) with
\(e'=\max\{0,\lceil(e_j+\rho_j+c+5)/L\rceil-c\}\).
Using \(\lceil x\rceil<x+1\) and \(c(1/L-1)\le0\), we get \(e'<(e_j+\rho_j)/L+1+5/L\le(e_j+\rho_j)/L+1.2\), since \(L\ge27\).
Next, \(\rho_j\le\eta s(R_j)+1\le\eta(h_j+2e_j)+1\le\eta(D_H(j)+2c)+2\eta e_j+1\) by (3.1) and G.
Finally, \(R_{j+1}(\beta)\) is the union of \(\widetilde H^+_{j+1}(\beta)\) (width 0) and these images. ∎

### 3.2 The uniform bound

**Lemma 3.2 (no accumulation)** [P from Lemma 3.1, G at every level, (Drop)]. For every island and every level \(j\) at which it stands,
\[
 e_j\le1.16\,\eta\,(D_H(j)+2c)+1.32 .                                                   \tag{3.3}
\]
The bound does not depend on the island's age, on its history of swallowings, or on the number of steps.

*Proof.* Follow any chain of predecessors \(\alpha_{j-1},\alpha_{j-2},\dots\) back to a creation level, choosing at each step one index that attains the maximum in (3.2). Write \(q=(1+2\eta)/L\) and \(b_i=[\eta(D_H(i)+2c)+1]/L+1.2\). Then (3.2) reads \(e_{i+1}\le qe_i+b_i\) along the chain, with \(e=0\) at the start. By induction on the length of the chain,
\[
 e_j\le\sum_{k\ge1}q^{k-1}b_{j-k}.
\]
By G and (Drop), \(D_H(j-k)+2c=C_{\rm isl}L\check R_{j-k}+6+2c\le L^{\lceil k/2\rceil}(D_H(j)+2c)\). Hence
\[
 e_j\le\eta(D_H(j)+2c)\sum_{k\ge1}(1+2\eta)^{k-1}L^{\lceil k/2\rceil-k}+\Big(\frac1L+1.2\Big)\sum_{k\ge1}q^{k-1}.
\]
Since \(\eta\le\eta_\sharp\le1/4\), \(1+2\eta\le3/2\). Group the first sum in pairs \(k=2m,2m+1\):
\[
 \sum_{k\ge1}(\tfrac32)^{k-1}L^{-\lfloor k/2\rfloor}
 =1+\sum_{m\ge1}L^{-m}\big[(\tfrac32)^{2m-1}+(\tfrac32)^{2m}\big]
 =1+\tfrac53\sum_{m\ge1}\Big(\frac{9/4}{L}\Big)^m
 \le1+\tfrac53\cdot\frac{1/12}{11/12}<1.16
\]
for \(L\ge27\). The second sum is at most \(1/(1-1.5/L)\le1.06\), and \((1/L+1.2)\cdot1.06<1.32\). ∎

*Why this is the right notion of "collars do not accumulate".* After a scale drop the coarsened old collar is a full collar of the current hub (Proposition 7.1). The recursion puts it into the core \(R\) and adds a fresh collar \(\rho\) beyond it, which is the margin DRL's payment needs (Theorem A). At the next step without a drop, coarsening shrinks the old part by \(L\). Since no two drops are consecutive, the old parts form a geometric series dominated by the current \(D_H\). The *absolute* width is therefore bounded by a small multiple of \(D_H(j)\), uniformly in the age.

### 3.3 Member geometry

Write \(K_w:=c+12\) and define the ceiling
\[
 \check R_j\ge\check R_\sharp:=\max\{10K_w,\ 64+8c\}.                                          \tag{3.4}
\]
By RUN (TD2 36: \(\check R_i\ge(\ell-1)^r\)) this is a ceiling on \(\gamma\).

**Lemma 3.3 (G♯: hub geometry with \(2C_{\rm isl}\))** [P from G, Lemma 3.2, (3.4), \(\eta\le\eta_\sharp\)]. At every level \(j\) and for every standing island:

- (i) *Widths.* \(e_j\le\check R_j/(13(C_{\rm isl}+1))+4\) and \(\rho_j\le\check R_j/(15(C_{\rm isl}+1))+3\), so \(M_j\subset N_{w_j}(H_j)\) with
  \[
   w_j:=e_j+\rho_j+c+5\le w_{\max}(j):=\frac{\check R_j}{6(C_{\rm isl}+1)}+K_w .
  \]
  Also \(\rho_j\ge\eta\,s(R_j)\).
- (ii) *Boxes.* \(s(R_j)\le D_H(j)+2c+2e_j\) and \(s(M_j)\le D_H^\sharp(j):=2C_{\rm isl}L\check R_j+6\), the box side of G with \(C_{\rm isl}\) doubled. Neither box wraps.
- (iii) *Separation.* Members of distinct islands are at distance \(\ge\check R_j/2\).
- (iv) *Gap.* Gas cubes and the live set are at distance \(\ge G_0(j)-w_{\max}(j)\) from every member, and \(\ge G_0(j)-e_j-c\) from every core \(R_j\).
- (v) *Persistence.* \(\pi(M_j(\alpha))\subset R_{j+1}(\alpha')\subset M_{j+1}(\alpha')\) in cases (i)–(ii) of (Mon). Iterating, \(\pi^m(M_j(\alpha))\subset R_{j+m}(\alpha^{(m)})\) for every chain that avoids case (iii).

*Proof.* First, \(\eta(D_H+2c)\le\dfrac{C_{\rm isl}L\check R}{16(C_{\rm isl}+1)^2L}+\dfrac{6+2c}{4+2c}\le\dfrac{\check R}{16(C_{\rm isl}+1)}+\dfrac32\), using \(C_{\rm isl}/(C_{\rm isl}+1)^2\le1/(C_{\rm isl}+1)\).

(i) Lemma 3.2 gives \(e\le1.16(\check R/(16(C_{\rm isl}+1))+1.5)+1.32\le\check R/(13(C_{\rm isl}+1))+4\).
Next, \(\rho\le\eta(D_H+2c)+2\eta e+1\). Here \(\eta\le\eta_\sharp\le1/(16\cdot4\cdot27)=1/1728\), so \(2\eta e\le\check R/(11232(C_{\rm isl}+1))+0.005\). Hence \(\rho\le\check R/(15(C_{\rm isl}+1))+3\).
Summing, \(w\le\check R(1/13+1/15)/(C_{\rm isl}+1)+c+12\le\check R/(6(C_{\rm isl}+1))+K_w\), since \(1/13+1/15=28/195<1/6\).
The lower bound on \(\rho\) is the definition of the ceiling.

(ii) The first bound is (3.1). For the second, \(s(M)\le s(H)+2w\le C_{\rm isl}L\check R+2+\check R/3+2K_w\). This is \(\le2C_{\rm isl}L\check R+6\) when \((C_{\rm isl}L-1/3)\check R\ge2K_w-4\), which holds by (3.4) since \(L\ge27\). No wrap: SA 17583 excludes wrapping for every box and neighbourhood of a box of side \(O(M\check R)\) in cells [R]. Members lie in a box of side \(\le2D_H\), inside G's non-wrapping lift doubled. *Status of "no wrap"* [R]: SA's sentence covers boxes of \(O(1)\) cells. A box of side \(2D_H\) fine cubes is \(O(1)\) cells, since a cell is \(L\check R\) fine cubes on the reading of TD 73 that \(G_0+2\) is ten cells.

(iii) Hubs \(\widetilde H(\alpha),\widetilde H(\beta)\) are at distance \(\ge\check R-4\). Since \(M\subset N_{w-2}(\widetilde H)\), the members are at distance \(\ge\check R-4-2(w_{\max}-2)\ge\frac56\check R-2K_w\ge\check R/2\) by (3.4), since \(\check R\ge10K_w\ge6K_w\).

(iv) \(M\subset N_{w-2}(\widetilde H)\) and \(R\subset N_{e+c}(\widetilde H)\); apply G's gap.

(v) This is the definition of \(R_{j+1}\), plus \(R\subset M\) and induction. ∎

So **hub geometry holds with \(2C_{\rm isl}\)**: every element of \(\mathsf H^+_j\) lies in a non-wrapping box of side \(D_H^\sharp=2C_{\rm isl}L\check R_j+6\). The separation is \(s_0/2\) up to a ceiling, and the gap loses only \(w_{\max}\le\check R_j/6+K_w\le G_0/1600+K_w\).

---

## 4. The consumer side: reads, ordinary decay, and the filing bound

### 4.1 X°♯: reads near hubs lie in cores

**X°♯** [replaces TD2 76–80]. Each exempt \(f\) consumed at step (level) \(t\) has a tree \(T_f\) in \(\mathcal C_t\) with \(|E(T_f)|\le C_{\rm pr}(1+d_f^{\rm old})\), such that every \(x\in X_f\) either lies within \(c\) of \(T_f\), or lies in \(R_t(\alpha)\) for an island whose core \(T_f\) meets. Also \(X_f\) meets a hub or the live set. Put \(\operatorname{Hub}(f):=\{\alpha:T_f\cap R_t(\alpha)\ne\varnothing\}\).

The only change from X° is "lies in \(R_t(\alpha)\)" in place of "lies in \(\widetilde H^+\)". At an island's first standing step, \(R=\widetilde H^+\).

**Lemma 4.1 (supply of the member part of X°♯)** [P from Lemma 2.1(c), Lemma 3.3(v), Definition F; scale conversion I, TD2 82].

Let \(f\) be a slot of level \(j<t\), with carrier \(X\) and supplied length \(d_f^{\rm old}\ge d^+_j(X)\), whose islands avoid case (iii) of (Mon) through level \(t\). Let \((\mathsf F,T)\) be a minimizer for \(d^+_j(X)\) in normal form (Lemma 2.3). Put \(T_f:=\) a spanning tree of \(\pi^{t-j}(V(T))\). Then:

- \(|E(T_f)|\le|E(T)|=d^+_j(X)\le d^{\rm old}_f\) (in edge units of \(\mathcal C_j\));
- every read cube of \(f\) at step \(t\) lies in \(\pi^{t-j}(X)\);
- every cube of \(\pi^{t-j}(X)\) either lies on \(T_f\) or lies in some \(R_t(\alpha^{(t-j)})\) that \(T_f\) meets.

*Proof.* Lemma 2.1(c) gives the edge bound. Reads: a carried slot keeps its carrier and function (SA 19523), and its step-\(t\) reads are the coarse cubes of its carrier (TD 51–61, A's complete reads).

Let \(y\in X\). If \(y\notin\bigcup\mathsf F\), then \(T\) meets \(y\), so \(T_f\) contains \(\pi^{t-j}(y)\). If \(y\in F\in\mathsf F\), then \(F\in\{H_j(\alpha),M_j(\alpha)\}\subset M_j(\alpha)\). By Lemma 3.3(v), \(\pi^{t-j}(y)\in R_t(\alpha^{(t-j)})\). Also \(T\) meets \(F\subset M_j(\alpha)\), so \(T_f\) meets \(\pi^{t-j}(M_j(\alpha))\subset R_t(\alpha^{(t-j)})\). ∎

*What this discharges.* TD2 82 lists three obligations for supplying X°: scale conversion, read-collar coverage, and containment of each excused hull in a current hub. For the new family, read-collar coverage is proved (every carrier cube is on the projected tree or in a met core), and containment is Lemma 3.3(v) from (Mon). The scale conversion (edge units of \(\mathcal C_j\) against \(d_f^{\rm old}\) in SA's units, and \(C_{\rm pr}\)) remains TD2 82's import, unchanged. Slots whose islands meet case (iii) are SA's healed case (§5.3).

### 4.2 Ordinary decay with X°♯ — Theorem B

**Theorem B (TD2 Theorem 3 under X°♯)** [P from TD2's R, A, X, G, RUN, X°♯, G-ord unchanged, Lemma 3.3].

Replace TD2 (8) by
\[
 (10L-\tfrac3{13})\check R_i\ge18+2c+(1+C_{\rm isl}/10)(2+c)+0.4C_{\rm isl}\qquad\text{(8♯, a ceiling on }\gamma\text{)}.
\]
Replace TD2 (10) by \(m_{X(f)}(W)+C_{\rm pr}(1+d_f^{\rm old})+2c+e_{\max}\ge G_0\), where \(e_{\max}\le\check R_i/(13(C_{\rm isl}+1))+4\).
Then TD2 Lemma 1 (9) holds with the **same** \(\eta_o=1+C_{\rm isl}/10\). TD2 Theorem 3 holds with \(a_T(\ell)=2e^{\kappa/4}N_{\rm ex}\vartheta_Te^{-\nu(G_0-C_{\rm pr}-2c-e_{\max})}\), which still tends to zero. The conditions (11) and (14) are unchanged.

*Proof.*

*Lemma 1.* Follow TD2 96–102. A root point \(x_{c_0}\) is either within \(c\) of \(T_f\) (connector \(\le c\)) or lies in \(R_i(\alpha)\) with \(T_f\) meeting \(R_i(\alpha)\). In the second case both ends of the connector lie in the box of \(R_i(\alpha)\), so the connector has at most \(s(R)\le D_H+2c+2e\) edges (Lemma 3.3(ii)). The root edge costs at least \(G_0-e-c\) (Lemma 3.3(iv)). So the number of such connectors is at most \(m/(G_0-e-c)\), and their total cost is at most \(\eta_om\) provided \(D_H+2c+2e\le\eta_o(G_0-c-e)\). Expand:
\[
 \eta_o(G_0-c-e)=10L\check R+C_{\rm isl}L\check R-(1+C_{\rm isl}/10)(2+c+e).
\]
The requirement becomes \(10L\check R\ge6+2c+(1+C_{\rm isl}/10)(2+c)+(3+C_{\rm isl}/10)e\). Since \((3+C_{\rm isl}/10)/(C_{\rm isl}+1)\le3\), Lemma 3.3(i) gives \((3+C_{\rm isl}/10)e\le\frac3{13}\check R+12+0.4C_{\rm isl}\). That is (8♯).

*Lemma 2.* Follow TD2 109. From a root point in \(R(\alpha)\), another \(e+c\) edges reach \(\widetilde H(\alpha)\), since \(R\subset N_{e+c}(\widetilde H)\). This adds \(e_{\max}\) to the walk.

*Theorem 3.* TD2 130–158 verbatim, with (10) replaced. Since \(e_{\max}\le\check R_i/26+4\le G_0/(260L)+5\), the tail argument at TD2 156–158 is unchanged. ∎

So the doubled \(C_{\rm isl}\) is **not** needed in \(\eta_o\). The connector crosses the core box, which exceeds the hub box only by \(2e\), and \(e\) is small.

### 4.3 X: lengths and per-cube sums (U9)

TD 65–71 requires \(\widetilde\omega_f\le\widehat\omega_fe^{-\kappa d_f^{\rm old}}\) and \(\sup_c\sum_{f:X(f)\ni c}\widehat\omega_fe^{-(\kappa/2)d_f^{\rm old}}\le N_{\rm ex}\).

**Lemma 4.2 (X is unchanged for old-route terms)** [P from Lemma 2.2]. Consider a term whose producer supplies \(d^\natural_j\). One may use either \(d_f^{\rm old}=d^\natural_j(X)\) (its old length, \(\ge d^+_j(X)\)) or \(d_f^{\rm old}=d^+_j(X)\) with \(\widehat\omega_f:=\widetilde\omega_fe^{\kappa d^+_j}\). In both cases (6) holds with the same \(N_{\rm ex}\).

*Proof.* In the first case nothing changes, and every consumer below needs only \(d_f^{\rm old}\ge d^+_j(X)\). In the second case,
\[
 \widehat\omega_fe^{-(\kappa/2)d^+}=\widetilde\omega_fe^{(\kappa/2)d^+}\le\widehat\omega^{\rm old}_fe^{-\kappa d^\natural+(\kappa/2)d^+}\le\widehat\omega^{\rm old}_fe^{-(\kappa/2)d^\natural},
\]
using \(d^+\le d^\natural\). Read sets are unchanged. ∎

For terms produced by Theorem A (new pieces), (6) at the next step is the producer's bookkeeping, as in DRL: Proposition 5.1′ with the regrouping of TD2 Corollary 4. If one derives (6) from the class bound alone (counting slots), Lemma 5.3(b) gives a prefactor at most 40 times the one obtained with SA's family.

### 4.4 The filing bound with recursive members — Theorem A (U16)

DRL §5 is re-run with the base \(N_f:=X_f\cup\bigcup_{\alpha\in\operatorname{Hub}(f)}\widehat R_i(\alpha)\), \(\widehat R=N_{\rho+2}(R)\), and members \(M_i(\alpha)=N_1(\widehat R_i(\alpha))\).

**Theorem A ((File-P°) with \(\mathsf H^+\))** [P from DRL Theorem 2 with \(\tau=a\), Lemma 4.3, Lemma 5.1, Proposition 5.1′, X°♯, G, Lemma 3.3]. Assume DRL's (F1), (F2) and (F4), the ceilings listed in DRL Theorem 3, (3.4), and

- **(F3♯)** \(\eta\le\eta_\sharp\), i.e. \(r=a/2-6\ge4\lambda_P\max\{16(C_{\rm isl}+1)^2L,\,4+2c\}\).

Then for every nonempty gas set \(W\), every \(P\in\mathcal O_\sigma(U)\) and every \(|\zeta|_c\le\mathfrak b\),
\[
 \sum_{f}\sum_{V\subset\mathcal P\setminus N_f}\sup|f_{W,V}|\,e^{\lambda_P\ell^{+}(Y_{f,V})}\le a_P^\sharp e^{-\lambda_Td_f(W)},\qquad
 a_P^\sharp=6e^{\kappa/2}\vartheta_PN_{\rm ex}e^{-\nu_g(G_0-C_{\rm pr}-2c-e_{\max})},
\]
with \(\ell^+=d^+_i\) on \(Y_{f,V}=N_1(N_f\cup V)\), and \(a_P^\sharp\to0\) under RUN.

*Proof.* Follow DRL 454–472 and change only what reads the hubs.

1. *Lemma 5.0 becomes Lemma 3.3.* Members are disjoint and separated (iii). Gas is far from them (iv). Boxes are bounded (ii). (F3♯) implies DRL's (F3), since \(\eta_\sharp\le1/(16(C_{\rm isl}+1)L)\).

2. *Proposition 5.1′* is unchanged. The base is any set containing \(X_f\) (DRL 397–399).

3. *Lemma 5.2 (carrier length)*, with \(\mathsf F=\{M_i(\alpha):\alpha\in\operatorname{Hub}(f)\}\). Each \(M_i(\alpha)=N_1(\widehat R)\subset N_1(N_f)\subset Y_{f,V}\).
   - Items 1, 2 and 5 of DRL 429–433 are verbatim. Item 2 uses X°♯ in place of (X°)(a): every cube of \(N_1(X_f)\) outside \(\bigcup\mathsf F\) is within \(c+1\) of \(T_f\). A cube of \(X_f\) in \(R(\alpha)\), \(\alpha\in\operatorname{Hub}(f)\), has \(N_1\) inside \(\widehat R\subset M\).
   - Item 4, Case 2: \(x_c\in R_i(\alpha)\) and \(T_f\) meets \(R_i(\alpha)\). The connector runs inside the box of \(R_i(\alpha)\) with at most \(s(R_i(\alpha))\) edges. The parent cost is \(l_c=d(c,x_c)\ge\rho_i(\alpha)+3\ge\eta\,s(R_i(\alpha))\). If \(c\in V\), this holds because \(c\notin\widehat R\). If \(c\in W\), it holds because \(d(c,R)\ge G_0-e-c\ge\rho+3\) by Lemma 3.3(iv) and (i). So Case 2 costs at most \(m/\eta\) in total, as in DRL.
   - Connectivity and coverage follow DRL 435, with \(N_1(\widehat R)=M\in\mathsf F\).
   - The minimizer for \(d^+_i(Y)\) may choose more elements, for instance members or hulls of other islands contained in \(Y\). This only lowers the length, so DRL's tree gives an upper bound.

   Hence \(\ell^+(Y_{f,V})\le C_4(1+d_f)+(81+c+1/\eta)m+c|W|\), with DRL's \(C_4\).

4. *Theorem 3 (i), shell sum.* Split \(X(f)=X_1\cup X_2\) with \(X_2\subset\bigcup_{\operatorname{Hub}(f)}R(\alpha)\) (X°♯). A cube \(v\notin N_f\) has \(d(v,R(\alpha))\ge\rho+3\). The cubes at distance \(n\) from the box of \(R\) number at most \(8(s(R)+2n)^3\). Each hub therefore contributes at most \(16(s(R)+2\rho+6)^3e^{-12(\rho+3)}\le16\Theta_\eta\). This is DRL's \(\Theta_\eta\), read at \(x=s(R)\), since \(\eta x\le\rho\le\eta x+1\). The number of hubs is \(|\operatorname{Hub}(f)|\le|V(T_f)|\le(C_{\rm pr}+1)(1+d_f)\), since the cores are disjoint. (F4) is unchanged.

5. *Theorem 3 (ii), gap.* TD2d Lemma 3.2 gains \(e_{\max}\), exactly as in Theorem B.

6. *Theorem 3 (iii), the sum over \(f\)*, and the collection of factors are verbatim.

The limit follows as in DRL 472, since \(e_{\max}\ll G_0\). ∎

*Iteration.* At step \(i+1\) the new terms \(f_{W,V}\) (and their cluster logarithms, DRL Proposition 5.4) are slots with carrier \(Y\supset M_i(\alpha)\) and \(d^+_i(Y)\) as supplied length. By Lemma 4.1 they satisfy X°♯ at step \(i+1\), with reads near \(\alpha\) in \(\pi(M_i(\alpha))\subset R_{i+1}(\alpha')\). The step-\((i+1)\) base \(\widehat R_{i+1}(\alpha')\) contains these reads with margin \(\rho_{i+1}+2\), which is what Case 2 needs. By Lemma 3.2 the widths stay below (3.3) at every step. **The induction closes with bounded collars.**

DRL Proposition 5.4 [P, as there]. The cubes of \(N_{c_G}(X)\) are at distance \(\ge G_0-w_{\max}-c_G\) from every element of \(\mathsf H^+\) (Lemma 3.3(iv)), so they lie outside every element, as DRL needs.

---

## 5. The remaining uses

### 5.1 U3: vanishing differences

SA 19517–19518 and IN1 136. Old boundary data enter \(\mathbf T\) and the stages as differences in the fluctuation or collar field, carrying a factor \(C\mathsf Bs_k\le1\), or a negative power of \(\log\theta_k\) per switched-off block. A difference of \(B(X)\) is a function on the same carrier \(X\), bounded by the same \(e^{-\kappa d(X)}\) times the factor. No property of the family enters except through \(d(X)\) on the same slot.

[P] Under Definition F the difference inherits \(e^{-\kappa d^+_j(X)}\) on the same slot. If the step files the result at a new level, the scale/hull comparison of CI 352 and TD2 365 is needed. That comparison is unchanged in status (§5.5).

### 5.2 U4: the long-domain exponential

SA 19499 and 19519 describe old terms that enter the main step of \(\mathbf R\) undifferenced, outside the enlarged components. Their domain must extend over \(c\check R_kL^{k-j}\) cubes of its own level, and then \(\mathsf Be^{-c\check R_k}\le1\). IN1 136 records this as one of the three ways old data enter. Neither SA nor IN1 proves the underlying lower bound on the relative length of such a domain. It is part of H-SF.

**Lemma 5.2 (LD: long domains)** [P]. Let \(\mathsf H\) be any finite family, and let \(\delta(\mathsf H)\) be the largest graph diameter of its elements. If \(p,q\in X\), then
\[
 d^\natural_{j,\mathsf H}(X)\ge d(p,q)-2\delta(\mathsf H).
\]
In particular:

- with SA's family, \(d_j^\natural(X)\ge d(p,q)-2(C_{\rm isl}L\check R_j+1)\);
- with \(\mathsf H^+_j\), \(d^+_j(X)\ge d(p,q)-2(2C_{\rm isl}L\check R_j+5)\).

*Proof.* Let \((\mathsf F,T)\) be admissible. If \(p\notin\bigcup\mathsf F\), then \(T\) meets \(p\); put \(p'=p\). Otherwise \(p\in F_1\in\mathsf F\), and \(T\) meets \(F_1\) at some \(p'\) with \(d(p,p')\le\operatorname{diam}F_1\le\delta\). Choose \(q'\) in the same way. \(T\) is connected and contains \(p',q'\), so \(|E(T)|\ge d(p',q')\ge d(p,q)-2\delta\). For the two families: \(\operatorname{diam}(H)\le s(H)-1\le C_{\rm isl}L\check R+1\), and \(\operatorname{diam}(M)\le D^\sharp_H-1\) (Lemma 3.3(ii)). ∎

So any long-domain inequality \(d^\natural_j(X)\ge c'\check R_k\), derived from an extension \(D\ge c\check R_kL^{k-j}\) by subtracting excused diameters, holds for \(d^+_j\) with \(C_{\rm isl}\) replaced by \(2C_{\rm isl}\) in the subtracted term. **This is the only place where IN1's own H-SF clause reads the size of excused sets, and there the change is exactly "\(C_{\rm isl}\) doubled".**

*Status.* The source inequality remains part of H-SF [I, NL1/ST1/OL1/SC1], with SA's \(c\) and the doubled \(C_{\rm isl}\). By (Drop), \(\check R_j\le L^{\lceil(k-j)/2\rceil}\check R_k\). The requirement is \(c>2\cdot2C_{\rm isl}/L^{\lfloor(k-j)/2\rfloor}\), with the worst case at \(k-j=1\): \(c>4C_{\rm isl}\), against \(c>2C_{\rm isl}\) for SA's family. If SA's \(c\) is a free-upward geometric constant fixed with the enlarged-component construction (2d), after \(C_{\rm isl}\), this is a floor on it, and no cycle arises. **[R]**: SA does not state where its \(c\) sits in the order (SA 19469–19470 lists no such letter), so this placement is a reading.

### 5.3 U5: the volume cost and the healed case

SA 19520 and IN1 136, 233, 417. Inside an enlarged component, old data enter only through \(V(X^\sim)\), at a cost per cube \(c_{\mathsf B}\) chosen after \(\mathsf B\).

**Lemma 5.3 (ENT: rooted entropy)** [P]. Let \(\mathsf H\) be a family in which every cube lies in at most two elements, and the elements form chains \(H(\alpha)\subset M(\alpha)\) with disjoint \(M\)'s. If \(e^{\kappa}\ge76800\), then:

- (a) for every finite set \(A\) of cubes, \(\sum_{\varnothing\ne X\subset A}e^{-\kappa d^\natural_{j,\mathsf H}(X)}\le36|A|\);
- (b) for every cube \(z\), \(\sum_{X\ni z}e^{-(\kappa/2)\,d^\natural_{j,\mathsf H}(X)}\le C_\kappa(1+2V_{\max})\), where \(V_{\max}\) is the largest element volume and \(C_\kappa=18\sum_n(38400e^{-\kappa/2})^n\le36\) when \(e^{\kappa/2}\ge76800\).

*Proof.* For each \(X\) fix a minimizer \((\mathsf F,T)\) in normal form (Lemma 2.3). Every \(X\) has an **anchor**:

- if \(X\setminus\bigcup\mathsf F\ne\varnothing\), the anchor is its least cube \(a\), which \(T\) contains;
- otherwise \(X=\bigcup\mathsf F\), and the anchor is the pair \((F_1,b)\), where \(F_1\) is the element containing the least cube of \(X\) and \(b\) is the least cube of \(F_1\cap V(T)\).

Fix the anchor and \(n=|E(T)|\). Encode \(T\) by a depth-first traversal from \(a\) (or \(b\)): at most \(80^{2n}=6400^n\) codes, as in IN1 Lemma 9. Given \(T\):

- the islands met by \(T\) have disjoint \(M\)'s, each containing a vertex of \(T\), so there are at most \(n+1\) of them, and \(\mathsf F\) picks none, \(H\) or \(M\) for each: at most \(3^{n+1}\) choices;
- \(X\setminus\bigcup\mathsf F\subset V(T)\): at most \(2^{n+1}\) choices.

Anchors inside \(A\) number at most \(|A|+\sum_{F\subset A}|F|\le3|A|\), since each cube lies in at most two elements. Hence
\[
 \sum_{X\subset A}e^{-\kappa d}\le3|A|\sum_n6400^n3^{n+1}2^{n+1}e^{-\kappa n}=18|A|\sum_n(38400e^{-\kappa})^n\le36|A|.
\]
For (b), anchor \(X\ni z\) at \(z\) if \(z\notin\bigcup\mathsf F\). Otherwise \(z\in F_1\), and \(T\) meets \(F_1\) at one of at most \(V_{\max}\) cubes; there are at most two such \(F_1\). ∎

So the volume-type sum over slots inside \(X^\sim\) has a constant independent of member sizes. Only the numerical factor changes: 36 against 16 for SA's family (there each cube lies in at most one element: anchors \(\le2|A|\), two choices per island), a constant fixed in row 7 after \(\mathsf B\). So \(c_{\mathsf B}\) is *recomputed by its rule* and does not move in the order. The per-cube prefactor (b) grows from \(1+V_{\max}(H)\) to \(1+2V_{\max}(M)\). With \(V_{\max}(M)\le(D^\sharp_H)^4\le16(C_{\rm isl}L\check R+3)^4\), the ratio of the worst-case prefactors is at most 40.

*The healed case of (Mon).* When an island \(\alpha\) is swallowed by a healed component \(X\) at level \(k\), slots excusing \(\alpha\)'s elements fall into case (iii). The member then has to lie inside the enlarged component \(X^\sim\), so that those slots enter only through the volume bound. Here \(M_j(\alpha)\subset N_{w_{\max}}(H_j(\alpha))\), with \(w_{\max}\le\check R_j/6+K_w\) fine cubes, which is less than one cell. The component \(X\) contains \(\alpha\)'s region with SA's margins of 8–10 cells (SA 17325–17330, 17575–17580). **[R]**: this gives \(M\subset X\subset X^\sim\) once one reads "cell = \(L\check R\) fine cubes" (TD 73) and the nesting of SA 17579. The containment is the same kind of statement that SA's family needs for its hull, with a margin smaller than one cell added. I do not count it as new.

### 5.4 U6: the oscillation clause (18)

IN1 197–204 and 217. SA 17564 states the oscillation bound of a kept-form piece with carrier \(R\) as measured in the hull length of the carrier. By Lemma 2.2, any supply of (18) with \(d^\natural_i(\mathcal S;R)\) gives it with \(d^+_i(\mathcal S;R)\), on the same carriers and with the same \(B_\Phi\) [P]. Its consumers (LF1/ST1 at later evaluations) read it through decay and through per-carrier sums. These are §4.3 and Lemma 5.3. H-O remains Outstanding as before (IN1 204).

### 5.5 U14: CI's exempt classification and the scale/hull comparison

- *Classification* (CI 30). Call a term exempt if its carrier meets the live set or contains an element of \(\mathsf H^+_j\). Since \(H\subset M\), this is the same as containing a hull. Then a term is exempt under Definition F if and only if it is exempt under SA's family. A carrier containing no hull contains no member, so its \(d^+=d^\natural=d_j\) [P]. **Non-exempt terms are untouched.**
- *Scale/hull comparison* (CI 352, TD2 365, DRL §6.1 item 6) [O, owner NL1-L/LF1, unchanged]. This is filing a fine-level carrier into a slot of the next level. With Definition F there are two cases. If \(Y\supset M_j(\alpha)\), then \(\pi(Y)\supset\pi(M_j(\alpha))\), and the core of the next level is \(R_{j+1}\supset\pi(M_j)\) (Lemma 3.3(v)). If the comparison is made at a level whose family contains \(\pi(M_j)\) or a subset of \(\pi(Y)\) containing it, the projected tree is admissible (Lemma 2.1(c)). For SA's family the same question arises: the hull \(H_{j+1}\) may stick out of \(\pi(Y)\). The amendment does not make it harder, by Lemma 2.2, but it does not settle it either.

### 5.6 U8, U13: Amendment 1 and the contracted route

- Amendment 1 (IN1 670): \(L_0^\natural=\max\{4C_h^{\rm WF},8C_{\rm pr}\}[c^\natural_2+2C_h(c^\natural_1+5)](1+4\beta_s)\) and \(\kappa\ge\kappa_0^\natural(L)\). Neither reads \(C_{\rm isl}\) or the family. **Unchanged** [P].
- TD-natural (TD 75–90, 174–200) contracts each entire hub \(\widetilde H\) in \(\Gamma^\natural\). With supplied lengths \(d^+\), TD (8) would need \(\Gamma^\natural\) to contract cores or members instead. Otherwise the cubes of a member's collar inside \(X_f\) are uncontracted and unpaid. TD-natural is off the current route: TD2 Theorem 3 and DRL use ordinary TD, and TD 421 and 482 keep TD-natural as a separate valid conditional construction. The geometric constants \(c^\natural_1,c^\natural_2\) of TD (23) with contracted members were **not checked** here [O, off-route].

### 5.7 U15: AG1 Lemma 2

AG1 343–346 asks for these island geometry inputs: hull diameter \(\le C_0^{\rm isl}LR_i+2\); distinct hulls at distance \(\ge R_i\); distance \(\ge10LR_i-2\) from a cube meeting \(I\). The read hull is \(T_f\) together with the exempt hulls, with \(|T_f|\le C_{\rm tr}(d^\natural_f+1)\) (AG1 337–339).

**Lemma 5.4 (AG1 Lemma 2 with \(\mathsf H^+\))** [P from AG1 463–482 and Lemma 3.3, with \(R_i=\check R_i\)]. Use the read hull \(T_f\cup\{\text{chosen elements}\}\) of a minimizer for \(d^+\). If \(\check R_i\ge\max\{10,\check R_\sharp\}\) and \(0.1L\check R_i\ge w_{\max}+4\) (a \(\gamma\)-ceiling), then
\[
 \operatorname{diam}_cX_f\le c^\sharp_g(d^+_f+1)+\frac{2C_0^{\rm isl}}{9.9}\,d_c(\Delta,X_f),\qquad c^\sharp_g=(2+6C_0^{\rm isl}L)C_{\rm tr}+7 .
\]
AG1's conclusions then hold with \(\kappa_P\le\kappa/(2c^\sharp_g)\) and \(\bar\kappa\ge8\kappa_PC_0^{\rm isl}\).

*Proof.* Follow AG1 463–475. Elements have diameter \(\le2C_0^{\rm isl}LR_i+5\) and pairwise distance \(\ge R_i/2\) (Lemma 3.3(ii), (iii)). A simple path through the read hull uses tree cubes between elements, at least \(R_i/2-1\) of them, so it meets at most \(1+|T_f|/(R_i/2-1)\) elements. Its length is at most
\[
 |T_f|+\Big(1+\frac{|T_f|}{R_i/2-1}\Big)(2C_0^{\rm isl}LR_i+7)\le A^\sharp_g|T_f|+2C_0^{\rm isl}LR_i+7,
\]
with \(A^\sharp_g=1+(2C_0^{\rm isl}LR_i+7)/(R_i/2-1)\le2+5C_0^{\rm isl}L\) for \(R_i\ge10\).

Gap: stop at the first element along a path from \(X_f\) toward \(\Delta\). Before it the path uses only tree cubes. Elements are at distance \(\ge10LR_i-2-w_{\max}\) from \(\Delta\) (Lemma 3.3(iv)). So \(10LR_i-2-w_{\max}\le d_c(\Delta,X_f)+|T_f|+2\), and \(9.9LR_i\le d_c+|T_f|\) under the ceiling. Combine: \(2C_0^{\rm isl}LR_i\le\frac{2C_0^{\rm isl}}{9.9}(d_c+|T_f|)\). Then \(\operatorname{diam}\le(A_g^\sharp+2C_0^{\rm isl}/9.9)|T_f|+7+\frac{2C_0^{\rm isl}}{9.9}d_c\), and \(A_g^\sharp+2C_0^{\rm isl}/9.9\le2+6C_0^{\rm isl}L\). Use \(|T_f|\le C_{\rm tr}(d^+_f+1)\).

The rest is AG1 476–481. Multiplying by \(2\mathsf Be^{-\kappa d}\) and using \(\kappa_Pc_g^\sharp\le\kappa/2\) gives \(e^{-\kappa d/2}\). The \(d_c\) term needs \(\kappa_P\cdot2C_0^{\rm isl}/9.9\le\bar\kappa/4\), which \(\bar\kappa\ge8\kappa_PC_0^{\rm isl}\) implies. (N-B) is used with the supplied lengths (Lemma 4.2), or with prefactor \(\le40\,C_B^{\rm ent}\) if one derives it from the class bound (Lemma 5.3(b)). ∎

*Constants.* \(c^\sharp_g\) is a derived geometric constant (rows 1–2: \(C_0^{\rm isl},L,C_{\rm tr}\)). \(\kappa_P\) is a ceiling fixed after \(\kappa\). The \(\bar\kappa\) floor doubles. All are acyclic.

---

## 6. IN1's class induction with the new family (task 3)

**Theorem C ((Cls⁺))** [P, conditional on IN1's imports H-M, H-OL, H-SF, H-LF, H-G, H-C, H-E, H-O, H-SUM with the order of §8; on TD2's R, A, X, G, RUN; on G-ord unchanged; on DRL's DR-lane imports; on (Mon); and on the scale conversion of TD2 82]. Make the following changes:

- in IN1 44, (12), (18) and the class clause (IN1 217), replace \(d^\natural_j(\mathcal S;\cdot)\) by \(d^+_j(\mathcal S;\cdot)\) of Definition F;
- in TD's X and G and TD2's X°, use Definitions M and F, with X°♯;
- add (F3♯), (3.4) and (8♯) to the order as in §8.

Then:

- (a) the bare presentation is in \(\mathfrak L_0(\theta)\);
- (b) Theorem 10 (component mass), Theorem 11 (class step and floor) and Theorem 12 (first passage) hold with their statements unchanged and all constants of IN1 rows 1–10 unchanged;
- (c) the boundary and oscillation clauses are returned with \(d^+\) and the same \(\mathsf B,B_\Phi\);
- (d) at every level, every element of \(\mathsf H^+_j\) lies in a non-wrapping box of side \(2C_{\rm isl}L\check R_j+6\), and the collar widths obey (3.3) uniformly in the step.

*Proof.*

(a) At level zero there are no islands. Then \(\mathsf H^+_0=\varnothing\) and \(d^+_0=d^\natural_0=d_0\), and IN1 573 applies verbatim.

(b) *Theorem 10* (IN1 540–560) reads H-LF, H-G, H-C, H-E, (6), (7), (16), (32) and (33). None of them reads the exempt family or the boundary length. Its statement and proof are unchanged.

*Theorem 12* (IN1 583–633) reads Theorem 11, Lemma 4, the scalar recursion and the torus choice. The torus choice reads only \(2L^{11}MR_j\), which is not the family. It is unchanged.

*Theorem 11* (IN1 562–581). Its proof assigns each class clause to an import (IN1 571). The boundary clause (12) and the oscillation clause (18) are the only clauses that read the family. I check that their supply and their uses survive.

- *Supply of (12).* The step's boundary terms come from five origins (SA 6185–6187). Every origin whose producer returns SA's bound returns the new one on the same slot with the same \(\mathsf B\) (Lemma 2.2). The exempt-term origin on CI's path returns the new bound through Theorem A, DRL Proposition 5.4 and the regrouping of DRL §5.5/TD2 Corollary 4. Under SA's family it has no valid supply (DRL Attack A, DRL 511). For the passage from the filing bound at rate \(\lambda_P\) to the class rate \(\kappa\) on IN1's slots, the scale/hull comparison is unchanged (§5.5).
- *Supply of (18).* Lemma 2.2, as in §5.4.
- *The bound \(\mathsf B\) does not depend on itself.* IN1 136 and SA 19515–19520 name three ways old boundary data enter. Vanishing differences need no change (§5.1). The long-domain exponential holds with \(C_{\rm isl}\) doubled in the subtracted diameter (Lemma 5.2). The volume cost has the same structure and its constant is recomputed by its rule (Lemma 5.3). None of the three makes an origin bound depend on \(\mathsf B\). So Lemma 5 (IN1 389–417), "the boundary maximum is chosen first", is unchanged.
- *Uses at later steps.* An old slot is consumed by TD's X (Lemma 4.2), by X°♯ (Lemma 4.1), by ordinary TD (Theorem B), by DRL's filing (Theorem A), and by AG1 (Lemma 5.4). Each was checked above under the same imports.
- *Non-accumulation.* Lemma 3.2 bounds every width at every level by (3.3). The bound depends only on \(D_H(j)\), \(c\) and \(\eta\), never on the number of earlier steps. So the floors and ceilings above are finitely many, are fixed once, and hold at every step. This is the meaning of IN1 565's "with unchanged constants" here.
- *Remaining clauses.* Analyticity, reality, gauge invariance, covariance and coherence of the class (IN1 217; SA 19420–19423) do not read the family. Members enter only as index sets of lengths. They are formed covariantly: \(N_r\), \(\pi\) and least axis-parallel boxes commute with hypercubic lattice isometries. They are local in the history, since each member is a function of its island's own hull record (Definition M). So coherence (SA 19423(v)) transports them with the island [P].

(c) This is the supply step above.

(d) Lemma 3.3(ii) and Lemma 3.2. ∎

*What Theorem C does not do.* It does not prove any import. It does not discharge H-SF's long-domain inequality, which is now stated with \(2C_{\rm isl}\). It does not discharge the scale/hull comparison, the scale conversion of TD2 82, (Mon), or the healed-case containment (§5.3, [R]). Each of these was already Outstanding or imported in the same form for SA's family.

---

## 7. The literal (Cls): what fails, and three attacks

### 7.1 (D1): fixed collars after a scale drop

**Proposition 7.1** [P from SA 17334, (Nest), G; CE-route]. Suppose island \(\alpha\) stands at levels \(t\) and \(t+1\), and \(\check R_{t+1}=\check R_t/L\) (a drop). Use (Cls)'s fixed members \(\widehat H^+_t=N_{\rho_t+3}(\widetilde H^+_t)\), \(\rho_t=\lceil\eta h_t\rceil\), with DRL's base at step \(t+1\), \(N_{f'}=X_{f'}\cup N_{\rho_{t+1}+2}(\widetilde H^+_{t+1})\). Then a term \(f'\) filed at step \(t\), with carrier containing \(\widehat H^+_t\), has reads within distance \(c+7\) of the complement of its step-\((t+1)\) base. An attachment cube there has parent cost \(l_c\le c+8\). DRL's Case-2 payment \(l_c\ge\eta s_H\) fails once \(\eta h_{t+1}>c+8\), which RUN forces as \(\gamma\downarrow0\).

*Proof.* At a drop the cell side \(L\check R_t\) of level \(t\), measured in the units of level \(t+1\), is \(\check R_t=L\check R_{t+1}\) cubes of \(\mathcal C_{t+1}\). That is the cell side of level \(t+1\) [R: a cell is \(L\check R\) cubes, TD 73]. The partitions are nested (SA 17334), so the cells coincide. The level-\((t+1)\) hull of the fixed region is the level-\(t\) hull, and \(H_{t+1}=\pi(H_t)\) with \(s(H_{t+1})=s(H_t)/L\).

The carrier of \(f'\) contains \(\widehat H^+_t=N_{\rho_t+c+5}(H_t)\), and \(f'\) reads the pair there (DRL Proposition 5.1′: the base piece's response reads every component of the base). The coarse neighbourhood is contained in the image: \(N_{\lfloor(\rho_t+c+5)/L\rfloor}(\pi H_t)\subset\pi(N_{\rho_t+c+5}(H_t))\). A coarse cube at coarse distance \(k\) from \(\pi H_t\) contains a fine cube at fine distance \(\le kL\) from \(H_t\), since the grids are aligned.

Now \(\lfloor(\rho_t+c+5)/L\rfloor\ge\eta h_t/L-1\ge\eta s(H_t)/L-1=\eta s(H_{t+1})-1\). Also \(\rho_{t+1}\le\eta(s(H_{t+1})+2c+4)+1\le\eta s(H_{t+1})+2\), using \(\eta(2c+4)\le1\). Hence the reads reach \(N_{\rho_{t+1}-3}(H_{t+1})=N_{\rho_{t+1}-c-5}(\widetilde H^+_{t+1})\). The base boundary is at \(N_{\rho_{t+1}+2}(\widetilde H^+_{t+1})\), at most \(c+7\) further out. ∎

*Why this is the divergence.* For an attachment \(v\) on the far side of the hub from \(T_{f'}\), the literal \(\ell^{\rm rel}\) of \(N_1(N_{f'}\cup\{v\})\) is at least about \(h_{t+1}/2\): the tree must join \(N_1(v)\setminus\widehat H^+_{t+1}\) to \(T_{f'}\) through or around the member. Theorem 2 of DRL gives the piece the factor \(q\,e^{-r(c+8)}\), with no \(h\)-dependence. The shell just outside the base has about \(h^3\) cubes. So the Theorem 3 majorant contains \(\gtrsim h^3qe^{-r(c+8)}e^{\lambda_Ph/2}\), which is unbounded as \(\check R\to\infty\). This refutes the proof route, not (File-P°) itself. A lower bound on the actual pieces, as in DRL Proposition 3.2, is not attempted.

### 7.2 Three attacks on the literal (Cls), and why each fails

**Attack 1 — DRL's base with the fixed family, as written.** This is Proposition 7.1. *Exact reason:* after a drop the coarsened old collar is again a full current collar, because the hull does not grow while the cubes do. The base therefore has no margin beyond the old reads.

**Attack 2 — a larger fixed collar, \(\rho=\lceil K\eta s_H\rceil\) for a fixed \(K\ge2\), with base at width \(K\rho-1\).** *Fails for the same reason.* Proposition 7.1's computation scales: at a drop \(\lfloor K\rho_t/L\rfloor\ge K\eta s(H_{t+1})-1\), so the old reads again reach within \(O(c)\) of the new base. No fixed multiple escapes the scale invariance of a collar proportional to the hub. *Exact reason:* the collar and the hub shrink by the same factor \(L\) at a drop, so any rule \(\rho=F(s_H)\) with \(F\) linear reproduces itself. A collar proportional to the *level* \(D_H(j)\) instead of the hub has the same defect at a drop, since \(D_H\) also scales by \(L\) in current units there.

**Attack 3 — keep fixed members, and re-file old terms read in an old collar at carriers containing the current member.** *Fails* for two reasons. First, it does not change the reads: the step-\((t+1)\) base must contain a \(\rho\)-margin beyond the *reads*, wherever the term is filed. Second, filing distinct old slots \(X'\) at one carrier \(X'\cup\widehat H^+\) merges them (§7.3). *Exact reason:* the payment in DRL Case 2 is measured from the reads, and slots are indexed by carrier.

The repair in Definition M is to put the old reads into the core \(R\) and measure the new collar from there. It is the least change that removes the defect in all three attacks, and Lemma 3.2 shows it costs a bounded width.

### 7.3 (D2): replacing hulls by collared hubs

Under replacement, consider a slot \(X\) with \(H(\alpha)\subset X\) and \(\widehat H^+(\alpha)\not\subset X\). Its length is no longer exempted at \(\alpha\). The tree must meet every cube of \(X\cap\widehat H^+\setminus H\), so \(d_{\rm rep}(X)\) can exceed \(d^\natural(X)\) by up to \(|X\cap(\widehat H^+\setminus H)|-1\). Lemma 2.2 fails, and an old-route producer's bound no longer implies the class bound.

The obvious remedy is to file \(B(X')\) at \(X'\cup\widehat H^+\). It sends every slot \(X'\subset\widehat H^+\) with \(X'\supset H\) to the same slot \(\widehat H^+\), whose new length is \(0\). Their sum is bounded only by \(\mathsf B\) times the number of attachment places on \(\partial H\), as in Lemma 5.3(b). That number is of order \(s_H^3\). **[R]**: a rigorous lower bound needs actual terms. A capacity count shows that any filing of \(\sim s_H^3\) collar-supported old terms of size \(\sim\mathsf Be^{-\kappa O(1)}\) into slots of new length \(O(1)\) forces \(\mathsf B\) to grow at least like the collar width. Adding members (Definition F) avoids the question: each old slot keeps its own exemption.

---

## 8. Constant order

"Early" means fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\). Rows are IN1's (IN1 225–236) with Amendment 1.

| Constant or condition | Row | Kind | Reads | Change |
|---|---|---|---|---|
| \(C_{\rm isl}\), \(c\), \(C_{\rm pr}\) (G-ord, TD2 73) | 2 | geometric, early | — | unchanged; members bounded by \(2C_{\rm isl}\) (Lemma 3.3(ii)) |
| \(\eta_o=1+C_{\rm isl}/10\) | 2 | determined | \(C_{\rm isl}\) | unchanged (Theorem B) |
| \(L\) floors (TD2 168, Amendment 1) | 2 | floors | early constants | unchanged |
| \(c_g^\sharp=(2+6C_0^{\rm isl}L)C_{\rm tr}+7\) (AG1) | 2 | determined | \(C_0^{\rm isl},L,C_{\rm tr}\) | recomputed |
| \(\kappa\), with \(\kappa\ge\log76800\) for Lemma 5.3 | 4 | floor | numbers | within IN1 row 7's entropy floor on \(\kappa\) |
| \(\lambda_P=\min\{\kappa/(16C_4),(4(2c_G+1)^4)^{-1}\}\) (DRL) | after 4 | determined | \(\kappa,C_4,c_G\) | unchanged |
| \(\kappa_P\le\kappa/(2c^\sharp_g)\) (AG1) | after 4 | ceiling | \(\kappa,c_g^\sharp\) | recomputed |
| **(F3♯)** \(a/2-6\ge4\lambda_P\max\{16(C_{\rm isl}+1)^2L,4+2c\}\) | 5 | floor on \(\bar\kappa\) | \(\lambda_P,C_{\rm isl},L,c\) | replaces DRL (F3) |
| AG1: \(\bar\kappa\ge8\kappa_PC_0^{\rm isl}\) | 5 | floor on \(\bar\kappa\) | \(\kappa_P,C_0^{\rm isl}\) | doubled |
| TD2 (14), DRL (F2), (F4) | 5 | floors on \(\bar\kappa\) | as before | unchanged |
| \(\eta=4\lambda_P/(a/2-6)\), \(\rho_j\), \(R_j\), \(M_j\) | after 5 | determined by history | \(\eta\), hulls | new objects; no earlier constant reads them |
| \(\mathsf B\), then \(c_{\mathsf B}\) (36 per cube in Lemma 5.3), then \(c_1\) | 7 | as IN1 | as IN1 | \(c_{\mathsf B}\) recomputed by its rule |
| \(C_{\rm ex}(M)\), \(C_B^{\rm ent}\) | after \(M\) | amplitudes | — | \(\times\le40\) only if derived from the class bound |
| (3.4) \(\check R\ge\check R_\sharp\); (8♯); AG1's \(0.1L\check R\ge w_{\max}+4\) | 9 | ceilings on \(\gamma\) | early constants | new |
| SA's long-domain \(c\) vs \(2C_{\rm isl}\) (Lemma 5.2) | (2d) | floor on SA's \(c\) | \(C_{\rm isl}\) | [R] placement |

**No cycle.** Each new or changed condition is assigned to the last constant it reads, as in SA 19453–19460, and is of an allowed kind there. (F3♯) and the AG1 floor are floors on \(\bar\kappa\), which comes after \(\kappa,\lambda_P,L,C_{\rm isl},c\). The \(\check R\) conditions are ceilings on \(\gamma\) (SA 19485, the supremum form) under RUN. No early constant reads \(\eta\), the members, or the widths (3.3). Lemma 3.2's bound uses only \(D_H\), \(c\) and \(\eta\le1/4\).

---

## 9. Proposed Amendment 2 to frozen IN1 (task 4)

*Not applied. Text for the lead.* Each item gives the change and why it is safe.

1. **IN1 44.** Replace "The supplied boundary hull length is \(d_j^\natural(\mathcal S;X)\)." with:
   > The supplied boundary hull length is \(d^+_j(\mathcal S;X)\): SA's \(d^\natural_{j,\mathsf H}(X)\) (SA 6191–6195, literal reading, crossings charged, chosen elements contained in \(X\)) for the family \(\mathsf H^+_j=\{H_j(\alpha)\}\cup\{M_j(\alpha)\}\) over the label's standing islands. Here \(H_j\) is SA's level-\(j\) hull and \(M_j\) is the recursive collared hub of `cls-draft.md` Definition M: \(R=\widetilde H^+\) at creation, \(\rho_j=\lceil\eta s(R_j)\rceil\), \(M_j=N_{\rho_j+3}(R_j)\), \(R_{j+1}=\widetilde H^+_{j+1}\cup\pi(M_j)\), with \(\eta=4\lambda_P/(a/2-6)\le\eta_\sharp\).

   *Safe because* \(d^+\le d^\natural\) for every \(X\) (Lemma 2.2), and non-exempt carriers are unchanged (§5.5).
2. **IN1 133 (12), 201 (18), 217.** Read \(d^\natural\) as \(d^+\). *Safe:* by Lemma 2.2, every existing supply passes. The new exempt supply is Theorem A.
3. **IN1 136 (H-SF), after "a long-domain exponential".** Add:
   > with excused diameters at most \(2C_{\rm isl}L\check R_j+5\) (`cls-draft.md` Lemma LD).

   *Safe:* this is the only place where H-SF reads the size of excused sets, and the change is "\(C_{\rm isl}\) doubled" (Lemma 5.2).
4. **IN1 147–159 (H-G), new sentence.** Add:
   > The members satisfy G♯: non-wrapping boxes of side \(2C_{\rm isl}L\check R_j+6\), mutual distance \(\ge\check R_j/2\), distance from gas and the live set \(\ge G_0-\check R_j/(6(C_{\rm isl}+1))-c-12\), and persistence \(\pi(M_j)\subset R_{j+1}\). These follow from G, (Mon) and (Drop) (`cls-draft.md` Lemmas 3.2–3.3).
   
   *Safe:* proved from existing G and SA 17334, and (Mon) is TD2 82's existing containment import.
5. **Row 2.** After "geometric and hull constants", add "including \(C_{\rm isl}\) (TD2 G-ord); excused members are bounded with \(2C_{\rm isl}\)." *Safe:* no new early constant.
6. **Row 5.** Add:
   > (Amendment 2) \(\bar\kappa\) also satisfies (F3♯), \(a/2-6\ge4\lambda_P\max\{16(C_{\rm isl}+1)^2L,4+2c\}\), and AG1's \(\bar\kappa\ge8\kappa_PC_0^{\rm isl}\).
   
   *Safe:* both are floors on \(\bar\kappa\) in earlier constants.
7. **Row 9.** Add:
   > (Amendment 2) \(\check R\ge\check R_\sharp=\max\{10(c+12),64+8c\}\), (8♯), and \(0.1L\check R\ge w_{\max}+4\).

   *Safe:* \(\gamma\)-ceilings under RUN.
8. **Change log.** Add:
   > Amendment 2 (lead, date): excused family enlarged by recursive collared hubs, per `cls-draft.md` Theorem C. Theorems 10–12 unchanged; constants unchanged except the floors and ceilings in rows 5 and 9. Conditional on `cls-draft.md` surviving distillation and referee.

**What is not proposed.** Replacing SA's hulls (D2). Fixed per-step collars (D1). Any change to \(\eta_o\), \(s_0\), \(G_0\), \(\mathsf B\), \(E_0\), \(N_*\), or any row-1–4 constant.

**Companion corrections (not made; no frozen file edited).**

- *TD2 76–82:* X° becomes X°♯ (cores, not collared hubs). TD2 82's "read-collar coverage" is discharged by Lemma 4.1 for the new family. (8) becomes (8♯), and (10) gains \(e_{\max}\).
- *DRL §5:* the base is \(N_{\rho+2}(R)\); (F3) becomes (F3♯); Lemma 5.0 becomes Lemma 3.3. DRL's non-accumulation sketch (DRL 507) is corrected. Hub sides do not shrink by \(L\) per step in general (hulls are in cells), and fixed collars fail at drops (Proposition 7.1). The recursive cores are needed.
- *AG1 343–346 and Lemma 2:* the geometry inputs are read for \(\mathsf H^+\) as in Lemma 5.4.

---

## 10. Status

| Statement | Status |
|---|---|
| Lemma 2.1 (coarsening) | [P] |
| Lemma 2.2 (monotonicity), 2.3 (normal form) | [P] |
| (Drop) from SA 17334 | [P] from the source's stated rule |
| (Mon) | [I, LF1, = TD2 82's containment], with [R] derivation of the stronger form |
| Lemma 3.1, **Lemma 3.2 (no accumulation)** | **[P]** |
| **Lemma 3.3 (G♯, \(2C_{\rm isl}\))** | **[P]**; "no wrap" [R] |
| Lemma 4.1 (X°♯ member part) | [P]; scale conversion [I, TD2 82] |
| Lemma 4.2 (X per-cube sums) | [P] |
| **Theorem A (filing with recursive members)** | **[P]** from DRL's imports |
| **Theorem B (ordinary TD under X°♯, same \(\eta_o\))** | **[P]** from TD2's imports |
| Lemma 5.2 (LD) | [P]; the source inequality stays in H-SF [I], with placement [R] |
| Lemma 5.3 (ENT) | [P] |
| Healed-case containment (§5.3) | [R] |
| Lemma 5.4 (AG1 Lemma 2♯) | [P] |
| TD-natural with members (§5.6) | [O, off-route, not checked] |
| Scale/hull comparison (§5.5) | [O, unchanged owner NL1-L/LF1] |
| **Theorem C ((Cls⁺))** | **[P]**, conditional as stated |
| Literal (Cls) | **not proved**; (D1) [CE-route] Proposition 7.1; (D2) [R] |

### Checks this draft needs (for the referee)

1. Lemma 3.1: the ceiling arithmetic \(e'<(e+\rho)/L+1.2\), and the use of the weak (Mon) with \(N_2\).
2. Lemma 3.2: the paired geometric sum \(<1.16\) for \(L\ge27\), and the claim that maximizing chains through swallowings obey the same recursion.
3. Lemma 3.3(i)–(iii): the numbers under \(\eta\le\eta_\sharp\) and (3.4).
4. Theorem A, Case 2: the parent cost \(\ge\rho+3\) for attachments, measured from the core rather than the hub, and the shell sum read at \(x=s(R)\).
5. Theorem B: (8♯) with the original \(\eta_o\).
6. Proposition 7.1: cell coincidence at a drop, and the reach of the old reads.
7. Lemma 5.3: the anchor count \(\le3|A|\) and the normal-form choice.
8. Lemma 5.4: \(A_g^\sharp\) and the gap with \(w_{\max}\).

Only `library/cls-draft.md` is written. Retrieval, searches and file bookkeeping discharge no mathematical step. The text is not refereed, is not an audit and grants no status.
