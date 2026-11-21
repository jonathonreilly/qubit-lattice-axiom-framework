# GEOH: the actual-history geometry (critical path item 3, owner LF1(2)) — pass 1 draft

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-05. Pass 1 (long draft) of the draft → distil → referee → freeze process. Not checked by another model. Research text, not an audit; it grants no status. No computer-assisted step: every argument below is a finite hand argument (set inclusions, integer counts, geometric series), meant to be Lean-formalizable.

Credit. The region rules, tests, fates, marks, genealogy count, volume convention, coding and entropy argument are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text ("SA" = `ym4.tex` at revision `31a47c543775`, line numbers of that file; "CA-I" = `ca_I.tex`, its complete account I). The large-field regions, the prepared sequence, the boxes and the counting by creations follow Tadeusz Bałaban (CMP 119 (1988) 243; CMP 122 (1989) 175 and 355); the gauge-field renormalization-group framework is Bałaban's, with the later expositions of Jonathan Dimock. "geo5c-count" is Claude's ungated note `geo5c-count.md`; I re-derive the one step of it that I use (§11.3).

Files read (bounded ranges): `assembly-status.md` (whole); `in1.md` L1–240, L419–560, L635–699; `ag1.md` L1–177, L360–430; `st1-r4.md` L1–257, L650–668, L700–810, L811–925, L1025–1110, L1505–1530; `cls.md` L1–150; `geo5c-count.md` (whole); `f-meas.md` L30–48; `nl1-L.md` L128–140; `cp12-draft.md` L228–295; `descent.md` (grep only); SA 6095–6140, 17300–17460, 17494, 17575–17585, 17719–17762, 18416–18720, 23315–23330; CA-I 53735–53810, 74290–74330, 80915–80930, 159060–159082.

## 0. Results

| # | Statement (§1 gives the exact text) | Status in this draft | Where |
|---|---|---|---|
| S1 | IN1 H-G: (14), the waiting rule, leaves/cut islands, volume convention (6) with the source-volume comparison, and the coding hypotheses of Lemma 9 | **proved** for the actual history (§§2–5), with explicit constants (§10) | Theorems G1–G4 |
| S2 | AG1 (ANC) | **proved**, in both readings of "live at level \(j\)" (§3) | Theorem A |
| S3 | ST1 GEO-mark | **proved**, all six clauses, with one stated reading of SA's quarantine (§6) | Theorem M |
| S4 | ST1 GEO-box | **proved** for an explicit specification of the affected loop family \(\mathcal B_t\) (§7) | Theorem B |
| S5 | ST1 GEO-slot | **Outstanding**: one precise lemma (convention identity at two interfaces), after three attacks (§8). Under CA-I's own bond-count convention it is false at the outer interface (conditional counterexample) | Lemma S♮ |
| S6 | cls Lift | **proved** on admissible tori with an explicit floor (§9) | Theorem L |

Task 4 (drop-outs, §11). The drop-out windows do not change the genealogy count or the coding (14). Moreover, the drop-out configuration that `cp12-draft.md` Proposition 8.6 needs does **not** occur in the actual history above a coupling floor: inside a drop-out the action level of a site is at least its determining level minus \(w\le 1+\log_L(2(11+b_{\rm bx})C_1')+\log_L(1+\mathsf N_t)\), not minus \(\mathsf N_t\) (Proposition D3).

The first remaining Outstanding statement is Lemma S♮ (GEO-slot). It feeds only ST1's FM6 and the CA-I identification (Outstanding FM-match); no other ST1 proof reads it (§8.4).

## 1. The six statements, exactly as the frozen consumers use them

### 1.1 S1 = IN1 H-G (frozen `in1.md`)

`in1.md` L147–157 (quoted in full, display (14) included):

> **H-G (geometry and coding, LF1(2)).** For each outer genealogy let \(o_n,l_n,n_t^{\rm cr},n_t^{\rm mk}\) count occupied cells, light nodes, created cells and marked nodes (excluding the root mark). There are fixed \(C_g\ge1,s_0\ge1,C_T\ge1\) such that
> \[ |C(u)|\le C_g(1+o(u)),\qquad o_n\le\tfrac12o_{n-s_0}+C_g l_{n-s_0}+C_g\sum_{n-s_0<t\le n}n_t^{\rm cr}. \tag{14}\]
> Counts below the initial level vanish. A node is light if and only if \(o(u)\le C_g\), i.e. it has at most \(C_g\) occupied cells (SA 17744). A chain beginning at an event and continuing through nodes with exactly one predecessor, no new cell and no intervening mark has at most \(T_t=C_TR_t\) light nodes if it begins at \(t\). Every leaf has a created cell; predecessors have lower levels and successors are unique. Cut islands are leaves with at most \(N_{\rm cut}\) cells.
>
> The outer record has a connected set of active addresses in a graph of fixed degree bound \(D\ge1\), with root fixed by \(X\); an address includes its level and spatial cell. Its volume (6) is determined by that set and is at least its cardinality. At each fixed address set the number of non-frame codes is at most \(e^{b_{\rm code}V^\circ}\). Every free frame choice is accompanied by its factor \(w^{-1}\). These are the coding hypotheses needed for Lemma 9 […]. The source-volume comparison following (6) is also part of H-G.

The source-volume comparison, `in1.md` L74: "The geometry import must bound the source reserve volume \(v\) by \(C_vv^\natural\)". The volume (6), L68–73: \(V^\circ(\omega^\circ)=\sum_{(n,C)\ {\rm outer}}(1+\log x_n)(MR_n)^4|C|_n\), \(v^\natural=V^\circ+\sum_yv^\natural(\omega_y)\); "each uncut node occurs once and each cut boundary at most twice". The Outstanding note, L159: "The supplied local geometry and [geo5c-count.md] do not verify (14), the waiting rule and this coding map for all actual histories. The relevant SA arguments are 17719–17762 and 18416–18715".

Consumers: Lemma 8 (L484–527) reads (14), the chain bound, "Every leaf has a created cell", the cut-leaf bound and H-C; Lemma 9 (L529–538) reads the coding hypotheses; Theorem 10 (L540) reads H-G through both. The constants are placed at row 7 (L233): "\(c_{\rm lin}\) and the H-C certificate constants, then \(C_g,s_0,C_T,N_{\rm cut},c_w\), then \(c_G\); \(C_{\rm env},C_{\rm int},b_{\rm code},D\), then \(c_{\rm ent}\); the source-volume factor \(C_v\)".

The SA sources: the count SA 17732–17762 (Proposition 2.6); the skeleton (SA 18479), the coarse count (SA 18493), the occupied recurrence (SA 18522), the light wait (SA 18570), the genealogy count (SA 18593), the volume multiplicity (SA 18437), the read and label volumes (SA 18449, 18458), the address degree (SA 18680) and the entropy (SA 18707).

### 1.2 S2 = AG1 (ANC) (frozen `ag1.md`)

`ag1.md` L72: "**(ANC), LF1(2):** if a cell is live at levels \(j-1\) and \(j\), its live component at level \(j-1\) lies inside its live component at level \(j\). SA 23328 states this ("At every one of these levels it belongs to the lineage of the component that is live at level \(k\) and contains it"); it is not among (R0)–(R3) and is used by Lemma 1 (lines 412–413). **Outstanding** as an LF1 verification."

Definitions it reads, L35–41: "\(Z_j^{\rm pre}=\Lambda_j^{\rm pre,c}\) is the large-field region before healing; \(\mathcal Z_j\) is its live part after healing. Initially \(\mathcal Z_0=\varnothing\). For a component \(C\subset\mathcal Z_k\), put \(\mathsf Z_k(C)=C\), and recursively let \(\mathsf Z_{j-1}(C)\) be the union of the live components at \(j-1\) contained in \(\mathsf Z_j(C)\)." Event (2), L47: \(E_z^{(n)}(q)=\{z\subset\mathcal Z_j\text{ for every }n\le j\le q\}\).

Line pointer. The use is in Lemma 1's last paragraph, L414–415 ("Every designated surviving cell is counted by a terminal or a designated healed lineage, once at each paid level"), not L412–413 (which end the merger charge). Wording only.

### 1.3 S3 = ST1 GEO-mark (frozen `st1-r4.md`)

`st1-r4.md` L146: "**GEO-mark.** A standing mark of level \(s\) contained in a class component of level \(t\) has \(s<t-N_t\); standing windows sharing a point are disjoint. A mark disappears only when contained in a healed component or island at that operation's output. Its recorded number \(\nu\) of completed stages never decreases while it stands. Islands contribute no remake levels. A point belongs to at most one class component per operation level. These are hypotheses about the actual history (SA 6111–6115, 17433–17449)."

I split it into six clauses M(a)–M(f) in that order. Consumers: Lemma 1′/M2 (L202–225); Theorem 14 hypothesis 1 (L1541); `nl1-L.md` L137 ("Round 3's all-transition admission additionally reads GEO-mark, GEO-box, …"). SA's own text: SA 6111–6115 "Their waiting windows are required to be disjoint at a point, and old marks disappear when swallowed by a healed component or an island. These geometric facts require verification for the actual operation." SA 17440: "*Marks wait*: a mark of level \(s\) lying inside a class component of level \(t\) satisfies \(s<t_\flat\). Hence standing marks that share a part are nested, their windows \((s_\flat,s]\) are disjoint, and at any one place and level at most one drop-out mark is active."

### 1.4 S4 = ST1 GEO-box (frozen `st1-r4.md`)

`st1-r4.md` L148: "**GEO-box.** Specify the affected output-loop family \(\mathcal B_t\). Every corner of each such loop lies in the old \(\Omega_{k_\sharp+1}^c\) and is newly healed into output layer \(t\). The box response carrier lies in that top layer, up to the fixed endpoint/stencil enlargement used in Lemma B2. The prepared-box inclusion of CA-I 53786–53804 does not alone prove this assertion for an arbitrary enlarged loop family. This full carrier condition is assumed, including the required metric width of layers."

Here \(k_\sharp=t-N_t^0\) with \(L^{N_t^0-1}=R_{k_\sharp+1}\), \(N_t^0\ge2\) (RUN-low, L147). Consumers: Lemma B1 (L722–728: "On the affected loops GEO-box gives \(\mathcal E=N_t^0-1\)"), Lemma B2 (L1505–1523: "If the source lies exactly in layer \(t\), (20) gives \(d_+(b,S)\ge\rho_0(t-m-1)_+\). … For GEO-box's fixed carrier enlargement, replace \(\nu-1\) by \(\nu-1-c_{\rm bx}\)").

### 1.5 S5 = ST1 GEO-slot (frozen `st1-r4.md`; same in distilled `f-meas.md`)

`st1-r4.md` L153: "**GEO-slot (new input).** The independent collar bonds of CA-I 74314–74316 correspond exactly to the free removed rows of F2. Its rim bonds in 74317–74320 are exactly the recorded rim slots integrated at the stage. Orientations, units, fixed parameters and stored transports are matched. This does not identify densities or quadratic forms." `f-meas.md` L40–43 states the same with "are exactly \(F\)". Consumers: FM6 (`st1-r4.md` L1031–1041); Corollary 14′ (L1587, "GEO-slot for the specified stored Haar/delta stages"). L1105: "GEO-slot alone does not do it either" (FM-match).

CA-I 74314–74320: "The bonds of integration are the bonds of the set \((\Omega^c_{j+1}\setminus Z''_{j+1})^{(j)*}\), which carry the integration variables \(B_j\), and the bonds of the rim \(Z_{j+1}\cap\Omega_{j+1}\cap Z\), which carry the integration variables \(A_j\)."

### 1.6 S6 = cls Lift (distilled `cls.md`, not frozen; proposed for IN1 Amendment 2)

`cls.md` L22: "**Lift:** every box and neighbourhood used below embeds with its read margins. This is a torus condition for the enlarged sets, not a consequence of a side bound alone." Uses: Lemma 4 (L128, "Nonwrapping uses Lift"); Amendment 2, A4 (L451) and row 10 (L462: "the admissible torus/grid must satisfy Lift for the enlarged members, their constructed carriers and complete read margins").

### 1.7 One name, two or more statements

1. **"Lift" / "lift" has three meanings.** (i) cls's Lift: a torus-embedding condition (above), the same kind as SA 17583 ("no cell, no box, no neighbourhood of a box wraps around the torus"), IN1 Lemma 6's "consistent lifts on an admissible torus" (`in1.md` L419) and AG1's admissible-tori alternative (`ag1.md` L118–121). (ii) The radius lift factor of records: `st1-r4.md` L89 "Set \(\lambda_\tau\equiv1\)", Definition R1 "with unit lift" (L91), Lemma 10 "formation with unit lift" (L652); `nl1-L.md` L691 withdraws "the Tq-with-lifts branch". The task's phrase "with no lift" (Tq0) is meaning (ii). (iii) Companions "agreeing on common collared lifts" (`in1.md` L50). Only (i) is S6.
2. **\(C_g\).** IN1 (14) uses one \(C_g\) both as the multiplicative constant and as the light threshold (L155); that is one constant, and §4 chooses it to serve both. `st1-r4.md` row 5 (L166) uses \(C_g\) for "Fixed formation comparison constants \(C_U,C_g\) of Lemma 10" — a different constant. A distil should rename one.
3. **\(N\).** \(N_t=\mathsf N_t=R_t\) (operation depth; `in1.md` L25 "\(N_j=R_j\)", SA 17575); \(N_t^0\) (CA-I's prepared depth, \(L^{N_0-1}=R_{k_0+1}\), CA-I 53765–53773; `st1-r4.md` L147); \(N_{\rm cut}\) (IN1) = SA's \(N_*\) in SA 18530 ("\(|Y|_m\le N_*\)"), which is not IN1's list-size \(N_*\) (`in1.md` L233); \(N_k^{\rm site}\) (`in1.md` L213). They are distinct; §§4–7 keep the subscripts.
4. **"Mark", "collar", "window".** SA 17432 gives "mark" three meanings and SA 17356 (collar paragraph) gives "collar" four. "Window" means the stage-level window \((t_\flat,t_\flat+n]\) of a drop-out (SA 6098–6105) and also the trace window \(W_i^+\) (SA 17453). Here "window" is always the first.
5. **(ANC) and SA 23328.** They are one statement (AG1's reading), not two; §3 proves the form AG1 states, in both readings of "live".
6. **GEO-mark and SA's "Marks wait".** M(a) is SA 17440's first sentence with \(t_\flat=t-\mathsf N_t\); M(b) is its second. Same statements.

## 2. The actual geometric history

### 2.1 What "actual" means here, and why the analytic changes do not matter

The actual step is SA's step with four analytic changes: the Y3 relative soft-gauge Hessian (frozen `descent.md`), chart-free intrinsic domains and the radius table (Tq0) with \(\lambda_\tau\equiv1\) (frozen `st1-r4.md` L82–89), and Amendment CV's averaged-contour representative (`st1-r4.md` L41).

**Lemma 2.0 (outcome-driven geometry).** The geometric record of a history (cells, regions \(\Omega_l,\Lambda_l,S_l\), components, created cells, class components, fates, stage counts, marks, nest boxes) is a deterministic function of the sequence of test outcomes and the region rules (G1)–(G9) below. None of the four analytic changes enters (G1)–(G9).

*Proof.* (G1)–(G9) are quoted below with their SA lines; each is a set-valued rule whose inputs are earlier regions and the failure sets of tests (which cubes or bonds failed). The four changes enter as follows. `descent.md` L7: "For each fixed admitted region sequence, replacing its ambient gauge Hessian by Y3's relative form …"; L188: "Cut-down regions, cutoffs and boundary spaces depend only on fixed geometry". So descent takes the region sequence as input. (Tq0) and R1 define record radii and domains (`st1-r4.md` L82–118), not regions. CV changes the background representative used inside a test (`st1-r4.md` L41: "Changing the convention defines revised passing tests"). Thus the changes alter which outcomes occur and their weights, never the maps (G1)–(G9). Every statement S1–S6 is universally quantified over outcome sequences, so it is unaffected. ∎

Consequence. All results below hold for every outcome sequence, hence for every history the actual construction can produce, whatever the field.

### 2.2 The rules

Units: level-\(n\) quantities are in level-\(n\) lattice units unless said otherwise. A **level-\(n\) cell** is an aligned cube of side \(M\check R_n\) (level-\(n\) units); cell distance is the sup-distance between cell indices; two cells are adjacent iff their closures meet (distance \(\le1\)). \(N_rA\) is the set of cells at cell distance \(\le r\) from \(A\); \(A^{\sim r}\) is \(A\) with \(r\) layers of cells of the stated level (for a set of cells, \(A^{\sim r}=N_rA\)).

- **(G1) Cell sizes** (SA 17333). \(\check R_k\) is the least power of \(L\) not below \((\log\min_{i\le k}x_i)^r\), \(r\ge2\). It is non-increasing; \(\check R_k/\check R_{k+1}\in\{1,L\}\). A *drop* at \(k+1\) means \(\check R_k=L\check R_{k+1}\); then the level-\(k\) and level-\((k+1)\) cell partitions coincide as point sets. Otherwise one level-\((k+1)\) cell is the union of \(L^4\) level-\(k\) cells. Write \(R_k=\check R_k\) and \(\mathsf N_k=R_k\) (`in1.md` L25; SA 6035).
- **(G2) Step \(t=k+1\)** (SA 17317–17325). With \(Y=\mathcal Z_k\) the live region, hulls \(\widehat\cdot,{}'\) and layers in level-\(t\) cells:
  \(\Omega_t^c=Q_t'^{\sim2}\cup P_t'^{\sim4}\cup\widehat Y^{\sim8}\), \(Z^{[0]}=\mathsf{bx}((\Omega_t^c)^{\sim2}\cup R_t'^{\sim1})\), \(Z^{[n+1]}=\mathsf{bx}(Z^{[n]}\cup F_n^{\sim1})\) with \(F_n\) the cells of the failures of round \(n\); \(Z_t=\Lambda_t^c\) is the final \(Z^{[n]}\).
- **(G3) Creations** (SA 17325, 17407). The created cells of step \(t\) are the cells of \(\mathcal W^\wedge_t\), the union of the hulls of all failures of the step (\(P_t',Q_t',R_t'\), failing collar-bond cells, failing rim cells). They are level-\(t\) cells.
- **(G4) Boxing** (SA 17317). \(\mathsf{bx}\) "replaces each component contained in a cube of \(O(1)\) cells by its bounding box, and repeats this until nothing changes". The \(O(1)\) is a fixed design integer \(b_{\rm bx}\ge1\) (cube side in cells).
- **(G5) Rounds terminate** (SA 17356: "Every round examines bonds and cubes that no earlier round examined").
- **(G6) The class** (SA 17575–17583). With \(k_\flat=k-\mathsf N_k\ge1\), a component \(X\) of \(Z_k\) is in the class iff: (single boxes, size) for \(k_\flat\le i\le k\), \(X\cap Z_i\) is a single component of \(Z_i\) contained in a cube of \(b_{\rm cl}\) level-\(i\) cells; (quiet) for \(k_\flat<i\le k\), step \(i\) creates nothing in it and \(X\cap Z_i=\Phi_i(X\cap Z_{i-1})\), \(\Phi_i(V)=\mathsf{bx}(\widehat V^{\sim10})\); (quarantine) it "has not been acted on by any operation whose level lies in \([k_\flat,k)\)". The class-size integer is \(b_{\rm cl}=100\) (CA-I 53749: "contained in a cube of the size \(100MR_k\)").
- **(G7) Fates** (SA 17415–17430). Healed: \(\Omega_l,\Lambda_l,S_l\mapsto\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\) for \(l\le t\). Island: the same for \(l<t\) and for \(\Omega_t,S_t\); \(\Lambda_t\) unchanged, so \(X\subset Z_t\) remains. Drop-out after \(n\le\mathsf N_t\) stages: \(X\) remains in \(Z_t\); \(\Omega_l\cap X=X\setminus Z''_l(X)\) for \(t_\flat<l\le t_\flat+n\); \(\Lambda_l\cap X=X\setminus Z''_l(X)\) and \(S_l\cap X=\varnothing\) for the same \(l\) with \(l<t\); all other entries unchanged, so \(\Lambda_t\cap X=\varnothing\) (the top entry \(\Lambda_t\) is never replaced).
- **(G8) Marks** (SA 17432; SA 6098–6115). Islands and drop-outs are marks. "A mark persists until a later healed component or island swallows it." A drop-out mark keeps its former regions \(\Omega^\circ_l\cap X\), and the sequences \(\Omega^{\boldsymbol\nu}\) of (R21) are defined for \(0\le\boldsymbol\nu(X)\le n(X)\); \(\boldsymbol\nu=0\) is the action sequence, \(\boldsymbol\nu=n\) the determining sequence (SA 17440).
- **(G9) The nest and the box** (SA 17415, 17585; CA-I 53776–53802). In a class component \(X\) at level \(t\), with \(h=t_\flat\), \(N^0=N^0_t\), \(k_0=t-N^0\): \(Z''_i=Z_i\cap X\) for \(i\le h\); \(Z''_i=(\Omega_i^{\sim5})^c\cap X\) for \(h<i\le k_0\); for \(k_0<i\le t\), \(Z''_i\) is a union of level-\(i\) \(M\)-cubes, nested, consecutive members "separated by one layer" of level-\(i\) \(M\)-cubes, and \(Z''_t=(\Omega^{\sim5}_{k_0+1})^c\cap X\). The main-step box is \(\Lambda^{\rm pr}=(\Omega^{\sim4}_{k_0+1})^c\cap X\). Here \(\Omega\) is the label in force at the start of the operation, and in (G9) "\(\sim\)" counts layers of \(M\)-cubes of the stated level (CA-I 53742–53743).

Two facts from the frame are used. (Frame) \(\underline\lambda(j-i)-c_5\le\theta_i-\theta_j\le\overline B(j-i)\) for \(i\le j\), \(\theta\ge X_0>e\) (`in1.md` (1)); on the run \(\theta=x\). (Tube) \(|x_j-\theta_j|\le\theta_j/4\) (`in1.md` (3)).

### 2.3 Elementary lemmas

**Lemma 2.1 (no consecutive drops).** If \(X_0\ge X_0^{\rm dr}(L,r,\overline B)\), defined by \((1-4\overline B/(X_0\log X_0))^{-r}<L\), then no two consecutive levels are drops, and \(\check R_i\le L^{\lceil(k-i)/2\rceil}\check R_k\) for \(i\le k\).

*Proof.* Let \(m_k=\min_{i\le k}\theta_i\). Drops at \(k\) and \(k+1\) give \((\log m_{k+1})^r\le\check R_{k-1}/L^2<(\log m_{k-1})^r/L\). By (Frame), \(\theta_{k+1}\ge\theta_{k-1}-2\overline B\) and \(\theta_k\ge\theta_{k-1}-\overline B\), so \(m_{k+1}\ge m_{k-1}-2\overline B\). (SA defines \(\check R\) with \(x\); on the run \(\theta=x\).) Since \(m_{k-1}\ge X_0\), \(\log m_{k+1}\ge\log m_{k-1}+\log(1-2\overline B/m_{k-1})\ge\log m_{k-1}-4\overline B/m_{k-1}\) once \(2\overline B/X_0\le1/2\). So \((\log m_{k-1}/\log m_{k+1})^r\le(1-4\overline B/(m_{k-1}\log m_{k-1}))^{-r}<L\), a contradiction. The second claim: among \(k-i\) consecutive levels at most \(\lceil(k-i)/2\rceil\) are drops, and each drop multiplies \(\check R\) by \(L\) going down. ∎

**Lemma 2.2 (boxing reach).** For any set \(B\) of level-\(t\) cells, \(B\subset\mathsf{bx}(B)\subset N_{b_{\rm bx}}B\). The map adds no component that does not contain a component of \(B\). A component of \(B\) that is not contained in a cube of \(b_{\rm bx}\) cells is not changed except by merging with boxes.

*Proof.* Induction on the boxing operations. Invariant: each component of the current set contains a cell of \(B\), and each added cell is in a cube of side \(b_{\rm bx}\) that contains a cell of \(B\). A boxing replaces a component \(K\), contained in a cube \(Q\) of side \(b_{\rm bx}\), by its bounding box \(\subset Q\); \(K\) contains a cell \(c\in B\) by the invariant, and every cell of \(Q\) is within cell distance \(b_{\rm bx}-1<b_{\rm bx}\) of \(c\). The union of boxes and old components is again a union of components each containing a cell of \(B\). The set strictly grows at each change and the torus is finite, so the process stops (as SA states). The same invariant holds across the rounds of (G2): if \(B_{\rm tot}=(\Omega_t^c)^{\sim2}\cup R_t'^{\sim1}\cup\bigcup_nF_n^{\sim1}\) is the unboxed union of all material entering the step, then by induction over rounds every component of \(Z^{[n]}\) contains a cell of \(B_{\rm tot}\), and every cell of \(Z_t\) is within cell distance \(b_{\rm bx}\) of \(B_{\rm tot}\). So boxing reach does not accumulate over rounds. ∎

**Lemma 2.3 (regions as made are nested).** Write \(Z_n^{\rm m}\) for \(Z_n\) at the end of step \(n\) and \(\mathcal Z_n^{\rm m}\) for its live part after the level-\(n\) operation (healed components removed). Then \(\mathcal Z^{\rm m}_{n-1}\subset Z_n^{\rm m}\), and \(\mathcal Z^{\rm m}_n\subset Z^{\rm m}_n\).

*Proof.* \(Y=\mathcal Z^{\rm m}_{n-1}\subset\widehat Y\subset\widehat Y^{\sim8}\subset\Omega_n^c\subset(\Omega_n^c)^{\sim2}\subset Z^{[0]}\subset Z_n^{\rm m}\), by (G2) and Lemma 2.2. Healing removes components. ∎

**Lemma 2.4 (current label regions are nested).** Fix a time \(k\) and a value of \(\boldsymbol\nu\) on each standing drop-out. Let \(Z_l^{\boldsymbol\nu}(k)\), \(l\le k\), be the complements of the \(\Lambda^{\boldsymbol\nu}_l\) of the label at time \(k\), and \(\mathcal Z_l^{\boldsymbol\nu}(k)\) their live parts. Then \(Z_{l}^{\boldsymbol\nu}(k)\subset Z^{\boldsymbol\nu}_{l+1}(k)\) for \(l<k\).

*Proof.* Induction over the operations up to \(k\). After a step the new top entry contains the old live region (Lemma 2.3). A healing removes \(X\) from every \(Z_l\), \(l\le t\): \(Z_l\setminus X\subset Z_{l+1}\setminus X\). An island removes \(X\) from \(Z_l\), \(l<t\), and keeps \(X\subset Z_t\): \(Z_{t-1}\setminus X\subset Z_t\). A drop-out with parameter \(\nu\le n\) sets \(Z_l\cap X=Z''_l(X)\) for \(t_\flat<l\le t_\flat+\nu\), \(l<t\), and leaves the pre-operation entries \(Z_l^\circ\cap X\) for the other levels. Inside \(X\) we need: (i) \(Z_{t_\flat}^\circ\cap X\subset Z''_{t_\flat+1}\); (ii) \(Z''_l\subset Z''_{l+1}\); (iii) \(Z''_{t_\flat+\nu}\subset Z^\circ_{t_\flat+\nu+1}\cap X\). (i) and (ii) are (G9): \(Z''_{h}=Z_h\cap X\) and nestedness ("\(Z''_{h+1}\supset Z_h\)", CA-I 53795). (iii): \(Z''_l\subset\Omega_l^{\circ c}\cap X\) (SA 17415, "increasing boxes in \(\Omega_l^c\cap X\)"); \(\Omega^{\circ c}_l\subset Z^\circ_l\) because \(\Lambda_l\subset\Omega_l\); and \(Z^\circ_l\subset Z^\circ_{l+1}\) by induction. Outside \(X\) nothing changes. ∎

Remark. Lemma 2.4 for \(\boldsymbol\nu=0\), \(\boldsymbol\nu=n\) and every intermediate \(\boldsymbol\nu\) agrees with SA 17440: "each \(\Omega^{\boldsymbol\nu}\) is the label of an actual history, the one in which the operations stop after \(\boldsymbol\nu\) stages".

### 2.4 Nodes, predecessors, genealogy

**Definition 2.5.** A *node* is \(u=(n,C)\) with \(C\) a component of \(Z^{\rm m}_n\). A node \((n-1,C')\) with \(C'\subset\mathcal Z^{\rm m}_{n-1}\) (not healed at operation \(n-1\)) is a *predecessor* of the node \((n,C)\) with \(C\supset\widehat{C'}\) (hull in level-\(n\) cells). This is SA 17732: "An unhealed component of level \(n-1\) is a predecessor of the component \((n,C)\) of \(Z_n\) that contains its hull." \(\operatorname{Gen}(u_*)\) is the tree of \(u_*\) and its iterated predecessors. The *outer genealogy* \(\mathcal G^\circ(x)\) cuts \(\operatorname{Gen}(x)\) at inner islands: an island node \(y\ne x\) of \(\operatorname{Gen}(x)\) is kept as a leaf and its predecessors are removed (SA 18417–18422). A node is a *mark node* if it is an island or a drop-out at its own level.

**Lemma 2.6 (tree facts).** (a) Every unhealed node has exactly one successor (if the history continues). (b) Predecessors of a node are disjoint and have level one less. (c) A node with no predecessor contains a created cell of its own level. (d) The predecessor relation lowers the level by one, so \(\operatorname{Gen}(u_*)\) is a finite rooted tree.

*Proof.* (a) \(\widehat{C'}\) is connected (a union of level-\(n\) cells, each meeting the connected \(C'\), with consecutive cells adjacent) and lies in \(Z_n^{\rm m}\) (Lemma 2.3), so it lies in exactly one component. (b) Distinct components of \(Z_{n-1}^{\rm m}\) are disjoint. (c) Let \(C\) have no predecessor. Then \(C\) does not meet \(\widehat Y^{\sim10}\): each component of \(\widehat Y^{\sim10}\) contains the hull of a component of \(Y\) and is connected, so if it met \(C\) it would lie in \(C\) and give a predecessor. By (G2), every cell of \(Z_n^{\rm m}\setminus\widehat Y^{\sim10}\) before boxing lies in \(Q'^{\sim4}\cup P'^{\sim6}\cup R'^{\sim1}\cup\bigcup_nF_n^{\sim1}\). Boxing adds no component without an original one (Lemma 2.2). Each component of a layer set \(A^{\sim r}=N_rA\) meets \(A\) (a cell of \(N_rA\) is joined to \(A\) by a path of adjacent cells inside \(N_rA\)). So \(C\) contains a cell of \(Q'\cup P'\cup R'\cup\bigcup_nF_n\subset\mathcal W^\wedge_n\), i.e. a created cell. (d) Levels strictly decrease along predecessors. ∎

(Lemma 2.6(c) is IN1's "Every leaf has a created cell" for ordinary leaves; cut leaves are treated in §4.4.)

## 3. (ANC)

AG1 does not say whether "live at level \(j\)" means live in the region as made at time \(j\), or live in the label at the stopping time \(k\). Both readings are covered.

**Theorem A ((ANC) for the actual history).** Let \(z\) be a level-\(n\) cell (any \(n\le j-1\)) and \(n<j\le k\).
(i) *As-made reading.* If \(z\subset\mathcal Z^{\rm m}_{j-1}\) and \(z\subset\mathcal Z^{\rm m}_j\), the component of \(\mathcal Z^{\rm m}_{j-1}\) containing \(z\) lies in the component of \(\mathcal Z^{\rm m}_j\) containing \(z\).
(ii) *Current-label reading.* Fix the time \(k\) and any \(\boldsymbol\nu\). If \(z\subset\mathcal Z^{\boldsymbol\nu}_{j-1}(k)\cap\mathcal Z^{\boldsymbol\nu}_{j}(k)\), the same conclusion holds for the components of \(\mathcal Z^{\boldsymbol\nu}_{j-1}(k)\) and \(\mathcal Z^{\boldsymbol\nu}_j(k)\).
Consequently, along \(E^{(n)}_z(q)\) the components containing \(z\) form an increasing chain, and \(z\subset\mathsf Z_j(C_q)\) for every \(n\le j\le q\), where \(C_q\) is the live component at \(q\) containing \(z\).

*Proof.* (i) Let \(A\) be the component of \(\mathcal Z^{\rm m}_{j-1}\) containing \(z\). By Lemma 2.3, \(A\subset Z^{\rm m}_j\); \(A\) is connected, so it lies in one component \(W\) of \(Z^{\rm m}_j\), and \(z\subset W\). Components of \(Z_j^{\rm m}\) are either healed at operation \(j\) (and then removed entirely, (G7)) or kept entirely. Since \(z\subset\mathcal Z^{\rm m}_j\), \(W\) is kept, so \(W\) is the component of \(\mathcal Z^{\rm m}_j\) containing \(z\), and \(A\subset W\).
(ii) Lemma 2.4 gives \(\mathcal Z^{\boldsymbol\nu}_{j-1}(k)\subset\mathcal Z^{\boldsymbol\nu}_{j}(k)\): the live parts are the complements of healed areas, and a healed area is removed at all levels \(\le\) its level, so the inclusion survives. Then argue as in (i) with "kept" replaced by inclusion.
The consequence follows by induction on \(j\) downward from \(q\): \(\mathsf Z_q(C_q)=C_q\ni z\); if the component \(A_j\ni z\) at level \(j\) lies in \(\mathsf Z_{j}(C_q)\), then \(A_{j-1}\subset A_j\) by (ANC), and \(A_{j-1}\) is a live component at \(j-1\) contained in \(\mathsf Z_j(C_q)\), hence in \(\mathsf Z_{j-1}(C_q)\). ∎

Remarks. (1) The two readings must not be mixed: in a drop-out the determining entries \(Z^{\boldsymbol\nu=n}_l\cap X=Z''_l(X)\) are smaller than the as-made entries, so a cell can be live at \(l\) as made and not live at \(l\) in the determining label at time \(k\) (§11). Each reading is internally consistent. (2) AG1's L52 ("nestedness proves this directly") is the consequence above. (3) Status: **proved**; inputs (G2), (G4), (G7), (G9) only.

## 4. The genealogy count (14) and the waiting rule

### 4.1 Occupied cells and the reach

**Definition 4.1.** For a node \(u=(n,C)\) of an outer genealogy, \(O(u)\) is the set of level-\(n\) cells that contain a created cell of a node of \(\mathcal G^\circ(u)\) (the subtree below \(u\)), where cut-island cells count as created cells (artificial creations, `in1.md` L171 and SA 18530). \(o(u)=|O(u)|\). For the outer genealogy of a root, \(o_n=\sum_{u\ {\rm at\ level}\ n}o(u)\), \(l_n\) = number of light nodes at level \(n\), \(n^{\rm cr}_t\) = number of created (including artificial) cells of level \(t\) in it, \(n^{\rm mk}_t\) = number of mark nodes of level \(t\) other than the root.

**Lemma 4.2 (skeleton inclusion).** \(O(u)\subset C(u)\).

*Proof.* A created cell \(c\) of level \(t\) lies in a node \(v\) at level \(t\) of the subtree; the successor chain \(v=v_t,v_{t+1},\dots,v_n=u\) has \(v_{s+1}\supset\widehat{v_s}\), and the level-\(s+1\) cell containing \(c\) is in \(\widehat{v_s}\). Induction gives that the level-\(n\) cell containing \(c\) is in \(C(u)\). For an artificial cell of a cut island the same chain starts at the island node. ∎

**Lemma 4.3 (bounded reach).** Put \(e:=32+3b_{\rm bx}\). If \(L\ge27\) and Lemma 2.1 holds, then \(C(u)\subset N_eO(u)\) for every node of every outer genealogy.

*Proof.* Let \(e(u)\) be the least integer with \(C(u)\subset N_{e(u)}O(u)\). Put \(E_1=2(11+b_{\rm bx})\). Claim: \(e(u)\le E_1\) if level \(n(u)\) is not a drop, and \(e(u)\le E_1+10+b_{\rm bx}=e\) if it is.

Take \(u=(n,C)\). Every cell of \(C\) is within \(b_{\rm bx}\) of a cell of \(B_{\rm tot}\cap C\) (Lemma 2.2, across rounds), and every cell of \(B_{\rm tot}\) is either in \(\widehat{v}^{\sim10}\) for a predecessor \(v\), or in \(Q'^{\sim4}\cup P'^{\sim6}\cup R'^{\sim1}\cup\bigcup F_m^{\sim1}\) inside \(C\) (by (G2); \((A^{\sim2}\cup B^{\sim4}\cup D^{\sim8})^{\sim2}=A^{\sim4}\cup B^{\sim6}\cup D^{\sim10}\)). Boxing then adds at most \(b_{\rm bx}\) (Lemma 2.2). Cells of the second kind are within \(6\) of a created cell of level \(n\), which is in \(O(u)\). For the first kind: \(v\subset N_{e(v)}O(v)\) in level-\(n-1\) cells. Coarsening by the ratio \(\rho\in\{1,L\}\) maps cell distance \(d\) to at most \(\lceil d/\rho\rceil\) (each coordinate: \(\lfloor(b+d)/\rho\rfloor-\lfloor b/\rho\rfloor\le\lceil d/\rho\rceil\)). The level-\(n\) cells containing \(O(v)\) are in \(O(u)\). So \(\widehat v\subset N_{\lceil e(v)/\rho\rceil}O(u)\), and
\[ e(u)\le\max\{\lceil e(v)/\rho\rceil+10,\ 6\}+b_{\rm bx}\le\max_v\lceil e(v)/\rho\rceil+10+b_{\rm bx}. \]
At a leaf (no predecessor) \(e(u)\le6+b_{\rm bx}\le E_1\). At a cut leaf \(O(u)=C(u)\), \(e(u)=0\). At a drop (\(\rho=1\)) the previous level is not a drop (Lemma 2.1), so \(e(v)\le E_1\) and \(e(u)\le E_1+10+b_{\rm bx}\). At a non-drop (\(\rho=L\)), \(e(v)\le E_1+10+b_{\rm bx}\), so \(e(u)\le(E_1+10+b_{\rm bx})/L+1+10+b_{\rm bx}\). This is \(\le E_1\) iff \(E_1(1-1/L)\ge(10+b_{\rm bx})/L+11+b_{\rm bx}\). With \(E_1=2(11+b_{\rm bx})\) and \(L\ge27\): \(E_1\cdot\frac{26}{27}\ge\frac{52}{27}(11+b_{\rm bx})\ge\frac{10+b_{\rm bx}}{27}+(11+b_{\rm bx})\), since \(25(11+b_{\rm bx})\ge10+b_{\rm bx}\). Mergers take the maximum over predecessors. Induction over levels proves the claim, and \(e(u)\le e\). ∎

**Lemma 4.4 (connected skeleton).** \(O(u)\) is \(h_0\)-connected, \(h_0:=2e+1\): the graph on \(O(u)\) joining cells at cell distance \(\le h_0\) is connected.

*Proof.* Suppose \(O(u)=A\sqcup B\), both nonempty, with cell distance \(d(A,B)>h_0\). Then \(N_eA\) and \(N_eB\) are at cell distance \(\ge d(A,B)-2e\ge2\), so no cell of \(N_eA\) is adjacent to a cell of \(N_eB\). By Lemmas 4.2–4.3, \(C(u)\subset N_eA\cup N_eB\) and \(C(u)\) meets both (it contains \(A\) and \(B\)). This contradicts the connectedness of \(C(u)\). ∎

**Theorem G1 (first line of (14)).** With \(C_g:=\max\{h_0^4,64\}=h_0^4\) (as \(h_0=2e+1\ge71\)), \(|C(u)|\le(2e+1)^4o(u)\le C_g(1+o(u))\).

*Proof.* \(C(u)\subset N_eO(u)\), and \(|N_eA|\le(2e+1)^4|A|\). ∎

### 4.2 The coarse count and the contraction recurrence

**Lemma 4.5 (coarse count).** Let \(A\) be an \(h_0\)-connected set of \(N\) cells, and \(\pi\) a coarsening of ratio \(q\) (a power of \(L\)) with \(q\ge2h_0\). Then \(|\pi A|\le16+64h_0N/q\).

*Proof.* A spanning tree of the \(h_0\)-graph traversed in both directions gives a closed walk through all of \(A\) with \(2(N-1)\) steps, each of cell distance \(\le h_0\). Cut it into consecutive pieces of \(m:=\lfloor q/h_0\rfloor\ge q/(2h_0)\) steps. There are at most \(1+2(N-1)/m\le1+4h_0N/q\) pieces. The cells visited by one piece have index span \(\le mh_0\le q\) in each coordinate, so they occupy at most \(q+1\) consecutive fine cells per coordinate. An interval of \(q+1\) consecutive fine cells meets at most \(2\) coarse intervals of length \(q\). So one piece meets at most \(2^4=16\) coarse cells. Multiply. ∎

(SA 18493 states \(C_0(1+h_0N/q)\) "including a fixed coarse collar"; Lemma 4.5 is that bound with \(C_0=64\), and no collar is needed for \(O\).)

**Theorem G2 (second line of (14)).** Put \(s_0:=2\lceil\log_L(256h_0)\rceil\). For the outer genealogy of any root and every level \(n\),
\[ o_n\le\tfrac12o_{n-s_0}+C_gl_{n-s_0}+\sum_{n-s_0<t\le n}n^{\rm cr}_t, \]
with all quantities at levels \(\le0\) equal to zero. Hence (14) holds with this \(C_g\) (the last coefficient \(1\le C_g\)).

*Proof.* Every node of the outer genealogy at level \(\le n-s_0\) lies below exactly one node at level \(n-s_0\) (successor chains pass through every level). So for a node \(u\) at level \(n\),
\(O(u)=\bigcup_{v}\pi_{s_0}O(v)\cup\{\text{cells of }u\text{'s level containing creations of levels }n-s_0<t\le n\}\), where \(v\) runs over the level-\((n-s_0)\) nodes below \(u\) and \(\pi_{s_0}\) is coarsening from level \(n-s_0\) to level \(n\). A created cell of level \(t\le n\) is contained in exactly one level-\(n\) cell (nested partitions). Summing over \(u\),
\(o_n\le\sum_{v\ {\rm at}\ n-s_0}|\pi_{s_0}O(v)|+\sum_{n-s_0<t\le n}n^{\rm cr}_t\).
Among the \(s_0\) levels at most \(s_0/2\) are drops (Lemma 2.1), so the ratio is \(q\ge L^{s_0/2}\ge256h_0\). By Lemmas 4.4–4.5, \(|\pi_{s_0}O(v)|\le16+o(v)/4\). If \(o(v)>C_g\ge64\), this is \(<o(v)/2\). If \(v\) is light (\(o(v)\le C_g\)), it is \(\le16+C_g/4\le C_g\). Sum. If \(n-s_0\le0\) the first two sums are empty. Cut leaves are nodes with \(O=C\); they obey the same bounds. ∎

(SA 18522 has \(C_1\) on all three terms; IN1 (14) has \(C_g\) on the last two; Theorem G2 gives \(1\) on the last, which is stronger.)

### 4.3 The waiting rule (light chains)

**Lemma 4.6 (quiet contraction).** Let \(\alpha_i\) be the side, in level-\(i\) cells, of the least cell box containing a node \(v_i\) on a chain in which each node is the only predecessor of the next and no step creates anything in it. Then \(\alpha_{i+1}\le\alpha_i/\rho_{i+1}+22\) and \(\alpha_{i+2}\le\alpha_i/L+44\) (for \(L\ge27\), given Lemma 2.1).

*Proof.* On such a chain \(v_{i+1}=\mathsf{bx}(\widehat{v_i}^{\sim10})\) restricted to its component (G2 with no failure in it: the failure terms are empty there, and the rounds add nothing since a round failure is a creation). The hull of a set of side \(\alpha\) in a grid coarser by \(\rho\) has side \(\le\lceil\alpha/\rho\rceil+1\le\alpha/\rho+2\); ten layers add \(20\); boxing of a single component replaces it by its bounding box, which does not change the side (no other component joins, by the chain condition). So \(\alpha_{i+1}\le\alpha_i/\rho+22\). Over two levels at most one is a drop: the three cases give \(\alpha/L^2+22/L+22\), \((\alpha+22)/L+22\), \(\alpha/L+44\), all \(\le\alpha/L+44\). ∎

**Theorem G3 (waiting rule).** Put \(\alpha_L:=h_0C_g+2e\), \(b_0:=2\lceil\log_L\alpha_L\rceil\), \(C_T:=b_0+2\) and \(T_t:=b_0+1+R_t\le C_TR_t\). A chain that begins at an event of level \(t\) (a node with a created cell of its level, or the successor of a mark node, or a node with \(\ge2\) predecessors) and continues through nodes with exactly one predecessor, no new cell and no intervening mark, has at most \(T_t\) light nodes. \(T_t\) is non-increasing in \(t\).

*Proof.* Along the chain no creation enters, so \(O(v_{i+1})=\pi O(v_i)\) and \(o\) is non-increasing; once a node is light, all later nodes on the chain are light. Let \(\ell_1\ge t\) be the level of the first light node. A light node has \(o\le C_g\); \(O\) is \(h_0\)-connected (Lemma 4.4), so its side is \(\le h_0(C_g-1)+1\), and the node's side is \(\le\alpha_L\) (Lemma 4.3). By Lemma 4.6, after \(2m\) further levels, \(m=\lceil\log_L\alpha_L\rceil\), the side is \(\le\alpha_L/L^m+44L/(L-1)\le47\), and the two-step bound keeps every later side \(\le47+22=69\) (if \(\alpha_i\le69\) then \(\alpha_{i+2}\le69/27+44<47\) and \(\alpha_{i+1}\le69\)). So for every level \(i\ge\ell_1+b_0\) on the chain the node is a single component of side \(\le69<b_{\rm cl}=100\).

Let \(k:=\ell_1+b_0+\mathsf N_{\ell_1}\). Since \(\mathsf N\) is non-increasing, \(k_\flat=k-\mathsf N_k\ge\ell_1+b_0>t\). If the chain is still running at level \(k\), its node \(X=v_k\) satisfies (G6): single boxes and size for \(k_\flat\le i\le k\) (just shown; \(X\cap Z_i=v_i\) because \(v_i\) is the only node below \(X\) at level \(i\), and no operation has acted on these nodes, so the label entries inside \(X\) are the as-made entries); quiet for \(k_\flat<i\le k\) (chain condition, as \(i>t\)); quarantine, since an operation that acted on a chain node would have healed it (ending the chain, as healed nodes leave the genealogy) or marked it (ending the chain by definition). Also \(k_\flat\ge1\). So \(X\) is in the class at \(k\); the operation heals it or marks it; either way \(v_k\) has no chain successor (a healed node has no successor; a marked node ends the chain by definition). Hence the chain has no node beyond level \(k\), and its light nodes lie at levels \(\ell_1,\dots,k\): at most \(b_0+\mathsf N_{\ell_1}+1\le b_0+1+R_t=T_t\) of them (\(\mathsf N=R\) non-increasing, \(\ell_1\ge t\)). If the history stops before \(k\), the chain is shorter. Finally \(T_t\le(b_0+1)R_t+R_t=C_TR_t\) since \(R_t\ge1\). ∎

Remarks. (1) Chains after a mark: a drop-out \(X\) at level \(s\) stays live; its successor starts a new chain (an event). The re-entry level \(k'\) has \(k'_\flat>\ell_1\ge s+1\), so the old mark is outside \([k'_\flat,k')\) and quarantine allows re-entry. This is SA 17610 ("followed by a wait of at most \(\mathsf N_k+1\) steps"). (2) SA 18598 treats tori too small for the class box; on admissible tori (§9) the box embeds, and a chain cut by the terminal level is shorter. No terminal-level term is needed. (3) SA 18570 has \(T_t=b_0+\overline N_t+3\); Theorem G3's \(b_0+1+R_t\) is the same bound with \(\overline N=R\).

### 4.4 Leaves, successors, cut islands

**Theorem G4(a).** Every leaf of an outer genealogy contains a created cell (an ordinary leaf by Lemma 2.6(c); a cut leaf by the artificial-creation convention). Predecessors have level one less, and successors are unique (Lemma 2.6). A cut island \((m,Y)\) has \(|Y|_m\le N_{\rm cut}:=b_{\rm cl}^4=10^8\).

*Proof of the last claim.* An island is a class component at its level \(m\) (G7), so \(Y=Y\cap Z_m\) is contained in a cube of \(b_{\rm cl}\) level-\(m\) cells (G6, size at \(i=m\)). ∎

### 4.5 The volume convention and the source-volume comparison

**Theorem G4(b) (multiplicity).** In \(v^\natural=V^\circ+\sum_yv^\natural(\omega_y)\), each node of the full genealogy that is not a non-root island occurs in exactly one \(V^\circ\) term; a non-root island occurs in exactly two (as a cut leaf of the outer tree of its successor and as the root of its own inner tree). Hence \(\mathsf V\le v^\natural\le2\mathsf V\) (SA 18437).

*Proof.* The cutting partitions the full genealogy into trees whose roots are \(x\) and the islands; each node belongs to the tree of the nearest island (or \(x\)) on or above it, except that a cut island also appears as a leaf of the tree above it. An island has one successor, so it is a leaf of exactly one outer tree. ∎

**Theorem G4(c) (source-volume comparison).** Let \(\mathsf V_{\rm in}(i,X;\mathcal S)=\sum_{j<i}\mathsf l_j\#_j(Z_j^{\rm a}\cap X)\) with \(Z^{\rm a}\) the action regions of the current label and \(\#_j\) the number of level-\(j\) sites (SA 18458). Then \(\mathsf V_{\rm in}\le v^\natural(\omega_X)\). If every stored or owned read site lies within a read collar of \(c_{\rm rd}\) level-\(j\) \(M\)-cubes of the cell owning it, and \(R_j\ge2c_{\rm rd}/(2^{1/4}-1)\), then the number of stored and owned read sites satisfies \(n^\sharp\le(2/\mathsf l_{\min})v^\natural\). So \(v\le C_vv^\natural\) holds with \(C_v:=2\) for \(v=\max\{\mathsf V_{\rm in},n^\sharp\}\), since \(\mathsf l_{\min}\ge1\).

*Proof.* A site of \(Z^{\rm a}_j\cap X\), \(j<i\), lies in a component \(C'\) of \(Z^{\rm a}_j\). The action label keeps the as-made entries except where an operation healed (removing the area at all levels \(\le\) its level) or made an island (removing the area below the island level); \(\boldsymbol\nu=0\) keeps the pre-operation drop-out entries (G8). So \(C'\) is a component of \(Z^{\rm m}_j\) none of whose successors up to level \(i\) was healed, and none of whose successors below level \(i\) was an island removed from the label; by nesting (Lemma 2.3) and connectedness its successor chain ends in \(X\), so \((j,C')\) is a node of \(\operatorname{Gen}(i,X)\), outer or inner. A level-\(j\) cell has \((MR_j)^4\) sites and \(\mathsf l_j(MR_j)^4\) is its volume weight. Summing, \(\mathsf V_{\rm in}\le\mathsf V\le v^\natural\). For \(n^\sharp\): a cell with its read collar has at most \((MR_j+2c_{\rm rd}M)^4=(MR_j)^4(1+2c_{\rm rd}/R_j)^4\le2(MR_j)^4\) sites; overlaps only reduce the union; divide by \(\mathsf l_j\ge\mathsf l_{\min}\). ∎

Status of §4: **proved**. Inputs: (G1)–(G7), Lemma 2.1, and for \(n^\sharp\) the read-collar locality (the same GEO locality requirement as ST1 Lemma F7, `st1-r4.md` L918). The determining regions are not used (they are subsets, §11).

## 5. The coding hypotheses of IN1 Lemma 9

**Definition 5.1 (address graph).** Vertices are addresses \((n,c)\), \(c\) a level-\(n\) cell, \(0\le n\le K\). Edges join adjacent cells of one level, and a cell to its parent (the level-\((n+1)\) cell containing it). Degree: \(3^4-1=80\) neighbours, one parent, and \(L^4\) children (one at a drop). So \(D:=L^4+82\) bounds the degree (SA 18680 has \(L^4+3^4+2\), the same number).

The **active set** of an outer record \(\omega^\circ\) rooted at \(x=(i,X)\) is \(\mathcal A(\omega^\circ)=\{(n,c):c\subset C(u)\text{ for an outer node }u\text{ at level }n\}\). Its root address is the lexicographically least cell of \(X\) at level \(i\), so it is fixed by \(X\).

**Theorem G5 (coding).** (a) \(\mathcal A(\omega^\circ)\) is connected and contains the root address. (b) \(V^\circ(\omega^\circ)=\sum_{(n,c)\in\mathcal A}\mathsf l_n(MR_n)^4\), so \(V^\circ\) is determined by \(\mathcal A\) (and the fixed frame), and \(V^\circ\ge|\mathcal A|\). (c) At a fixed active set the number of outer records with that set, counted without frame choices, is at most \(e^{b_{\rm code}V^\circ}\), with
\[ b_{\rm code}:=\log2+K_s\log K_o+\log K_{\rm st}+\log(3K_f)+(2+p_f)(\log(2L)+r), \]
where \(K_s\) is the number of test objects (bonds, plaquettes, test cubes, collar and rim bonds) based at one level-\(n\) site, including those based at the \(L^4\) level-\((n-1)\) sites of its block (so \(K_s\le c_sL^4\) with a design integer \(c_s\)), \(K_o\) the number of outcomes of one test object, \(K_{\rm st}\) the number of stored-variable and seam types at one site, and \(K_f(R+1)^{p_f}\) bounds the number of (failure type, stage position) pairs of an operation (SA 18698–18701: "a fixed power of \(R_j+1\) choices"). (d) Every free frame choice carries \(w^{-1}\).

*Proof.* (a) Each \(C(u)\) is connected in the same-level adjacency. If \(v\) is a predecessor of \(u\), every cell of \(v\) has its parent in \(\widehat v\subset C(u)\); so the parent edges join \(v\)'s addresses to \(u\)'s. The outer genealogy is a tree rooted at \(x\). Hence \(\mathcal A\) is connected.
(b) Distinct nodes of one level are disjoint, so each address is counted once; each address weighs \(\mathsf l_n(MR_n)^4\ge1\).
(c) Given \(\mathcal A\): the nodes at level \(n\) are the components of its level-\(n\) slice (distinct components of \(Z^{\rm m}_n\) are not adjacent); predecessor links are determined by hull containment; cut leaves are the slice components that the record marks as islands. The remaining record is local. Per address \((n,c)\): one bit (created or not); the outcome of each of the \(\le K_s(MR_n)^4\) test objects based in \(c\) (\(K_o\) values each); the stored-variable and seam type of each of its \((MR_n)^4\) sites; and, if \(c\) is the least cell of a class component, its fate (3 values), its stage count \(n(X)\in\{0,\dots,\mathsf N_n\}\) (\(\le R_n+1\) values) and its (failure type, stage position) (\(\le K_f(R_n+1)^{p_f}\)). The rounds need no code: round \(m\) examines the bonds not examined before (G5), and its failures are the recorded failures among them, so the round index of each failure is determined. The nest boxes \(Z''_l\) are determined by the label and (G9). The parameter \(\boldsymbol\nu\) is a structure parameter, not a history datum (§6.2). So the logarithm of the number of choices at \((n,c)\) is at most
\(\log2+(MR_n)^4(K_s\log K_o+\log K_{\rm st})+\log(3K_f)+(1+p_f)\log(R_n+1)\).
Now \(R_n\le L\mathsf l_n^r\), so \(\log(R_n+1)\le\log(2L)+r\log\mathsf l_n\le(\log(2L)+r)\mathsf l_n\); and \(\mathsf l_n(MR_n)^4\ge\max\{\mathsf l_n,(MR_n)^4,1\}\). So the logarithm is at most \(b_{\rm code}\,\mathsf l_n(MR_n)^4\). Multiply over \(\mathcal A\) and use (b).
(d) The operation inserts \(1=|W_4|^{-1}\sum_{r\in W_4}1\) per class component (SA 17585). So each frame summand carries \(w^{-1}\), \(w=|W_4|\). ∎

Status: **proved**, given the finite local alphabets \(K_s,K_o,K_{\rm st},K_f,p_f\) of the step's specification. These are design integers: they count objects the step defines, and SA 18696–18703 lists them. They do not depend on \(M\), \(\kappa\), \(\bar\kappa\) or the level. IN1 Lemma 9 then gives \(c_{\rm ent}\ge b_{\rm code}+2\log D+\log2\).

Injectivity. The record is, by IN1's definition (`in1.md` L66), the finite record of regions, tests, created cells, marks and operations. The code above lists exactly these data or data determined by them. So distinct records have distinct codes.

## 6. GEO-mark

### 6.1 The reading of quarantine

SA 17575 says the class component "has not been acted on by any operation whose level lies in \([k_\flat,k)\)". At level \(i<k\) the component \(X\) of \(Z_k\) did not exist; the clause must refer to its pieces. I use:

**(Q)** For every \(i\in[k_\flat,k)\), no standing mark of level \(i\) lies in \(X\).

This is the only reading under which the clause restricts anything: an operation at level \(i\) acts on class components of \(Z_i\); a healed one is removed from all levels \(\le i\) (G7), so it cannot lie inside \(X\) later; an island or a drop-out becomes a standing mark. So "a piece of \(X\) was acted on at level \(i\)" is equivalent to "a mark of level \(i\) lies in \(X\)", given that marks persist until swallowed (G8) and a swallowed mark lies in a healed component or island at a later level, hence is not inside the quiet \(X\) at levels \(\ge k_\flat\) (quiet forbids creations; swallowing happens only at class components, whose fates are recorded).

### 6.2 The theorem

**Theorem M (GEO-mark for the actual history).** Under (G1)–(G9) and (Q):
- M(a) A standing mark \((s,X')\) contained in a class component \(X\) of level \(t\) has \(s<t_\flat=t-\mathsf N_t\).
- M(b) Two standing marks sharing a point are nested, and their windows \((s_\flat,s]\), \((s'_\flat,s']\) are disjoint.
- M(c) A mark disappears only when it is contained in a healed component or an island at that operation's output.
- M(d) For each standing drop-out \(C\), \(\boldsymbol\nu(C)\) never decreases along the compared transitions of the actual history.
- M(e) Islands contribute no remake levels.
- M(f) A point belongs to at most one class component per operation level.

*Proof.* M(f): class components at level \(t\) are distinct components of \(Z_t\), hence disjoint.

M(a). \(X'\) is a component of \(Z_s\) in the label at the time of operation \(t\): an island keeps \(X'\subset Z_s\) ((G7), \(\Lambda_s\) unchanged) and a drop-out keeps \(X'\subset Z_s\) ("\(\Lambda_s\cap X'=\varnothing\)"). Since \(X'\) is standing at time \(t\), it was made at an operation \(s\le t\); a mark made at operation \(t\) itself is a fate of a class component of level \(t\), not a standing mark inside one, so \(s<t\). If \(t_\flat\le s<t\), then \(X'\) is a standing mark of level \(s\in[t_\flat,t)\) inside \(X\), contradicting (Q). So \(s<t_\flat\).

M(b). Let \((s,X')\), \((s',X'')\) be standing and share a point \(p\). Distinct components of one level are disjoint, so \(s\ne s'\); say \(s<s'\). By Lemma 2.4 (current label, any \(\boldsymbol\nu\)), \(X'\subset Z_s\subset Z_{s'}\); \(X'\) is connected and meets \(X''\) at \(p\), so \(X'\subset X''\). At operation \(s'\), \(X''\) was a class component and \(X'\) was standing then (marks never reappear after swallowing, so a mark standing now was standing at every earlier time since its birth). By M(a) at level \(s'\), \(s<s'_\flat\). So \(s\le s'_\flat\) and \((s_\flat,s]\cap(s'_\flat,s']=\varnothing\).

M(c). This is the record rule (G8): the update at operation \(t\) removes exactly the standing marks contained in a class component with fate healed or island. A mark meeting such a component \(X\) lies in it (nesting and connectedness as in M(b)). A drop-out does not remove older marks inside it. Marks outside class components are untouched.

M(d). Two families of \(\boldsymbol\nu\) occur. (i) The record of the history: the determining structure uses \(\boldsymbol\nu(C)=n(C)\), fixed when \(C\) is born (its stages are completed then); while \(C\) stands, no later operation changes \(n(C)\) (a later operation on a component containing \(C\) is a new mark with its own \(n\)). So \(\boldsymbol\nu(C)\) is constant. (ii) SA 17440's interpolating structures \(\boldsymbol\nu_\mu\): \(\boldsymbol\nu_\mu=n\) on marks older than \(\mu\) and \(0\) on later marks. As \(\mu\) increases, a mark moves from the second class to the first and never back; so \(\boldsymbol\nu_\mu(C)\) is non-decreasing in \(\mu\). SA 6120 orders structures so that "A structure precedes another if it counts no more completed stages"; for that order to be the order of compared transitions, it must be read per mark, and then (i)–(ii) are the two cases. In both, \(\boldsymbol\nu(C)\) never decreases.

M(e). An island replaces \(\Omega_l,\Lambda_l,S_l\) by \(\Omega_l\cup X,\Lambda_l\cup X,S_l\setminus X\) for \(l<t\) and \(\Omega_t,S_t\) likewise (G7). This is the same in every \(\boldsymbol\nu\)-sequence: (R21) defines the \(\boldsymbol\nu\)-dependence only on drop-outs. So an island has no level where the action and determining sequences differ, i.e. no remake level. ∎

Corollary (ST1 Lemma 1′'s use). The stage-level sets \(\{s-\mathsf N_s,\dots,s-\mathsf N_s+n-1\}\) of standing drop-outs containing a fixed point are pairwise disjoint (by M(b), since they lie in the windows), and the ledger (M1) is increasing (by M(c)–M(d)). This is exactly what `st1-r4.md` L223 uses.

Status: **proved**, with (Q) as the stated reading of SA 17575's quarantine clause. If the actual specification of the class uses a different quarantine rule, M(a) must be re-proved for it; M(b)–M(f) then follow as above.

## 7. GEO-box

### 7.1 The specification of \(\mathcal B_t\)

At a healed class component \(X\) of level \(t\), the main step integrates the level-\(t\) field over \(\Lambda^{\rm pr}=(\Omega^{\sim4}_{k_0+1})^c\cap X\), \(k_0=t-N^0_t\) (G9; SA 17585 "\(V_k\) is integrated over \(\Lambda^{\rm pr}\)"). Here \(k_\sharp=k_0\): both are defined by \(L^{N^0-1}=R_{k_0+1}\), the least such positive integer (`st1-r4.md` L147; CA-I 53765–53769).

**Definition 7.1.** \(\mathcal B_t(X)\) is the set of output datum loops all of whose corners lie in \(\Lambda^{\rm pr}\). \(\mathcal B_t\) is the union over healed class components of level \(t\). The box response source \(S_{\rm bx}\) is the set of output rows that read a variable changed by the main step.

### 7.2 Geometry of the quiet class

**Lemma 7.2.** Let \(X\) be a class component at level \(t\), and \(H_i\) the hull in level-\(i\) cells of \(X\cap Z_{i-1}\) (label in force). For \(t_\flat<i\le t\): \(\Omega^c_i\cap X=N_8H_i\) and \(N_{10}H_i\subset Z_i\cap X\subset X\). Hence \(\operatorname{dist}_\infty(\Omega^c_i\cap X,X^c)\ge2s_i\), \(s_i\) the level-\(i\) cell side. Also \(2\le N^0_t\le R_t-1<\mathsf N_t\), so \(t_\flat<k_0+1<t\).

*Proof.* By quiet, step \(i\) creates nothing in \(X\) and absorbs no second component. So inside \(X\) the failure terms of (G2) are empty, and \(\Omega_i^c\cap X=\widehat{(X\cap Z_{i-1})}^{\sim8}=N_8H_i\) and \(Z_i\cap X=\mathsf{bx}(N_{10}H_i)\supset N_{10}H_i\) (Lemma 2.2). By quarantine no operation has changed these entries since step \(i\). Lemma 2.4 gives \(Z_i\cap X\subset Z_t\cap X=X\). A cell of \(N_8H_i\) and a cell outside \(N_{10}H_i\) have index distance \(\ge3\), so their closures are at sup-distance \(\ge2s_i\). Finally CA-I 53773 gives \(2\le N_0\le R_t-1\), and \(\mathsf N_t=R_t\). ∎

This is SA 17578 (\(\Omega_i^c\cap X=H_i^{[8]}\), \(Z_i\cap X=H_i^{[10]}\)), written with neighbourhoods so that no box shape is needed.

### 7.3 The theorem

**Theorem B (GEO-box for the actual history).** Let \(X\) be healed at operation \(t\), with \(\mathcal B_t(X)\), \(S_{\rm bx}\) as in Definition 7.1. Assume the fixed floor \(M\ge c_{\rm bx}+1\), where \(c_{\rm bx}\) is the read reach (in level-\(t\) bonds) of an output row (its double block and stencil). Then:
(i) every corner of every loop of \(\mathcal B_t(X)\) lies in the old \(\Omega^c_{k_\sharp+1}\), hence in old layer \(\le k_\sharp\);
(ii) every such corner is newly healed into output layer \(t\);
(iii) \(S_{\rm bx}\subset N^{\rm lat}_{c_{\rm bx}}(\Lambda^{\rm pr})\subset X\), where \(N^{\rm lat}_r\) is the \(r\)-neighbourhood in level-\(t\) lattice units; so the box response carrier lies in output layer \(t\) up to the fixed enlargement \(c_{\rm bx}\);
(iv) \(\operatorname{dist}_\infty(S_{\rm bx},X^c)\ge2M-c_{\rm bx}\ge M\) in level-\(t\) units;
(v) on \(\mathcal B_t(X)\) the formation exponent of `st1-r4.md` Lemma 10 is \(\mathcal E=N^0_t-1\).

*Proof.* (i) \(\Lambda^{\rm pr}=(\Omega^{\sim4}_{k_0+1})^c\cap X\subset\Omega^c_{k_0+1}\cap X\), since \(\Omega\subset\Omega^{\sim4}\). This is the definition, with \(\Omega\) the label in force (old). A point of \(\Omega^c_{k_0+1}\) has old layer \(m(x)=\max\{q:x\in\Omega_q\}\le k_0\) (nesting of \(\Omega\)).
(ii) At the output of a healing, \(\Omega_l\cap X=X\) for all \(l\le t\) (G7), and \(t\) is the top level of the output label. So every point of \(X\) has output layer \(t\). Since the old layer was \(\le k_0<t\), the point is newly raised; it is raised by the healing.
(iii)–(iv) The main step changes only the variables of \(\Lambda^{\rm pr}\) (SA 17585: "Integrals against any bounded \(F\) that is independent of \(V_k\) on the box are left unchanged by it"). A row reading a changed variable lies within \(c_{\rm bx}\) of \(\Lambda^{\rm pr}\). By Lemma 7.2 with \(i=k_0+1\in(t_\flat,t]\): \(\Lambda^{\rm pr}\subset\Omega^c_{k_0+1}\cap X\), whose distance to \(X^c\) is at least \(2s_{k_0+1}=2a_{k_0+1}=2M\) level-\(t\) units (CA-I 53769: \(a_{k_0+1}=M\)). Subtract \(c_{\rm bx}\).
(v) For \(x\) with old layer \(l(x)\le k_\sharp\), raised at healing, Lemma 10 sets \(\mathcal E=e_{t-1}(x)+1=(t-1-k_\sharp-1)+1=N^0_t-1\) (`st1-r4.md` L654–660). ∎

What Theorem B does not prove. It fixes \(\mathcal B_t\) as the loops *inside* the box. Loops with some corners in \(\Lambda^{\rm pr}\) and some outside are not in \(\mathcal B_t\); BOX-bg (`st1-r4.md` L149) must then give them "the inherited (58), converted to their output levels". That is BOX's analytic content, owned by ST1, and is not a geometric fact. If instead \(\mathcal B_t\) is enlarged to all loops reading a changed variable, (i) can fail: the 4 layers in \(\Lambda^{\rm pr}\)'s definition are level-\((k_0+1)\) \(M\)-cube layers, of width \(4M/R_{k_0+1}\) level-\(t\) units, which is below one level-\(t\) bond when \(R_{k_0+1}>4M\). This is the precise sense of `st1-r4.md` L148: "The prepared-box inclusion … does not alone prove this assertion for an arbitrary enlarged loop family." The metric-width clause of GEO-box ("including the required metric width of layers") is used in Lemma B2 only through (20), which needs the output determining sequence to be \(\rho_0\)-separated (3); that is `st1-r4.md` Lemma 2 under GEO-prep (19), a separate GEO item, plus (iv) here.

Status: **proved** for Definition 7.1. The floor \(M\ge c_{\rm bx}+1\) is a fixed locality floor on \(M\) (IN1 row 5; ST1 row 8), independent of \(\kappa,\bar\kappa\).

## 8. GEO-slot

### 8.1 What ST1's own sets are (proved)

Fix a class component \(X\) at operation level \(t\), \(h=t_\flat\), and stage \(n+1\), \(j=h+n\), \(0\le n<\mathsf N_t\). Entries \(\Omega_q\) are those in force just before this stage. Put
\[ Y_j:=(\Omega^c_{j+1}\setminus Z''_{j+1})\cap X. \]
`st1-r4.md` L22–26 defines rows: \(\Gamma_q\) = level-\(q\) bonds with both endpoints in \(\Omega_0\), an endpoint in \(\Omega_q\) and no endpoint in \(\Omega_{q+1}\). Lemma 12 (L781) defines the stage by "enlarging member \(j+1\)"; with (G7)/(G9) the new member is \(\Omega^{\rm new}_{j+1}\cap X=X\setminus Z''_{j+1}\).

**Lemma 8.1.** (a) \(\Omega^{\rm new}_{j+1}=\Omega_{j+1}\cup Y_j\), and \(Y_j\subset\Omega_j\). (b) The removed rows are \(\mathfrak E=\Gamma^{\rm rm}=\{\text{level-}j\text{ bonds with an endpoint in }Y_j\text{ and no endpoint in }\Omega_{j+1}\}\). (c) The added rows are \(\mathfrak C=\Gamma^{\rm ad}=\{\text{level-}(j+1)\text{ bonds with an endpoint in }Y_j\text{ and no endpoint in }\Omega_{j+1}\}\). (d) \(\mathfrak F=\mathfrak E\setminus\{b_0(c):c\in\mathfrak C\}\) and \(|\mathfrak F|=|\mathfrak E|-|\mathfrak C|\).

*Proof.* (a) \(Z''_{j+1}\subset\Omega^c_{j+1}\cap X\) (SA 17415), so \(X\setminus Z''_{j+1}=(\Omega_{j+1}\cap X)\cup Y_j\). For \(n=0\): \(Z''_{h+1}\supset Z_h\cap X\) (G9), so \(Y_j\subset X\setminus Z_h=\Lambda_h\cap X\subset\Omega_h\). For \(n\ge1\): the previous stage set \(\Omega_j\cap X=X\setminus Z''_j\supset X\setminus Z''_{j+1}\supset Y_j\) (nest increasing). (b) A level-\(j\) row before the stage has an endpoint in \(\Omega_j\) and none in \(\Omega_{j+1}\); after it, it is a row iff it has no endpoint in \(\Omega^{\rm new}_{j+1}\). Removed rows are those with an endpoint in \(Y_j\) and none in \(\Omega_{j+1}\); conversely such a bond was a row (its \(Y_j\) endpoint is in \(\Omega_j\) by (a); \(\Omega_0\) contains everything here). Rows of other levels are unchanged, since only member \(j+1\) changes and the level-\((j+1)\) condition "no endpoint in \(\Omega_{j+2}\)" is not affected. (c) A level-\((j+1)\) bond becomes a row iff it gains an endpoint in \(\Omega^{\rm new}_{j+1}\), had none in \(\Omega_{j+1}\), and has none in \(\Omega_{j+2}\); the last holds automatically, because \(\operatorname{dist}(\Omega_{j+2},\Omega^c_{j+1})>\rho_0\xi_{j+1}>\xi_{j+1}\) by (3). (d) is F2's definition, with one pivot per added row (CH, `st1-r4.md` L836–841). ∎

### 8.2 CA-I's sets

CA-I 74314–74320: the stage integrates \(B_j\) on "the bonds of the set \((\Omega^c_{j+1}\setminus Z''_{j+1})^{(j)*}\)" and \(A_j\) on "the bonds of the rim \(Z_{j+1}\cap\Omega_{j+1}\cap Z\)". CA-I 159071–159075 defines, for \(Y\) a union of \((j+1)\)-cells: "\(\mathfrak b_i(Y)\) [is] the number of bonds of \(\mathbb T^{(i)}\) with at least one end-point in \(Y\). Let \(Y^{(j)*}\) be the set of \(j\)-bonds of \(Y\) from which, for every \((j+1)\)-bond \(c\) of \(Y\), the one \(j\)-bond that [B-CMP119 (1.9)] associates with \(c\) has been removed. In this notation \(|Y^{(j)*}|=\mathfrak b_j(Y)-\mathfrak b_{j+1}(Y)\)."

GEO-slot's first sentence says \(Y_j^{(j)*}=\mathfrak F\) (with orientations, units, parameters, transports). By Lemma 8.1 this is the statement:

> **Lemma S♮ (Outstanding).** (1) In CA-I 74315 the "\(j\)-bonds of \(Y_j\)" are the level-\(j\) bonds with an endpoint in \(Y_j\) and no endpoint in \(\Omega_{j+1}\) (label in force), and the "\((j+1)\)-bonds of \(Y_j\)" are the level-\((j+1)\) bonds with the same property; (2) the bond that B-CMP119 (1.9) associates with a \((j+1)\)-bond \(c\) is F2's pivot \(b_0(c)\); (3) the bonds of the rim \(Z_{j+1}\cap\Omega_{j+1}\cap X\) carrying \(A_j\) are exactly the stored level-\(j\) slots of \(X\) whose collar is integrated at stage \(n+1\) under the rule of GEO (`st1-r4.md` L126).

Given Lemma S♮, GEO-slot's two set identities follow from Lemma 8.1 and the definitions. Orientation and units are then F2's (`st1-r4.md` L830–850) by construction; the transport match is FM6's own claim (L1031–1041).

### 8.3 Three attacks on Lemma S♮(1), and why each fails

Facts used: the outer interface (sites of \(Y_j\) adjacent to sites of \(\Omega_{j+1}\cap X\)) and the inner interface (sites of \(Y_j\) adjacent to \(Z''_{j+1}\)) are both nonempty at every stage. Inner: \(Y_j\cup Z''_{j+1}=\Omega^c_{j+1}\cap X=N_8H_{j+1}\) is connected (Lemma 7.2) and both parts are nonempty (\(Z''_{j+1}\supset Z_h\cap X\ne\varnothing\); \(Y_j\) contains the boundary layer below). Outer: for \(j+1\le k_0\), \(Z''_{j+1}=(\Omega_{j+1}^{\sim5})^c\cap X\) omits the five \(M\)-cube layers of \(\Omega^c_{j+1}\) next to \(\Omega_{j+1}\), so those layers are in \(Y_j\); for \(j+1>k_0\), \(Z''_{j+1}\subset Z''_t\subset\Omega^c_{k_0+1}\cap X\), which is at positive distance from \(\Omega_{j+1}\cap X\)'s boundary with \(N_8H_{j+1}\) (Lemma 7.2 at two levels), so the boundary sites of \(N_8H_{j+1}\) lie in \(Y_j\). Per coarse boundary site \(y\) the face of its block carries \(L^3\) level-\(j\) bonds crossing the interface, while at most \(8\) pivots lie in the block of \(y\) (one per \((j+1)\)-bond at \(y\)).

**Attack 1 (CA-I's own count convention).** Read "\(j\)-bonds of \(Y\)" as the bonds counted by \(\mathfrak b_j(Y)\): at least one endpoint in \(Y\). This is the reading that makes CA-I's identity \(|Y^{(j)*}|=\mathfrak b_j(Y)-\mathfrak b_{j+1}(Y)\) true. *Failure:* it contradicts S♮(1). The outer-interface \(j\)-bonds have an endpoint in \(\Omega_{j+1}\), so they are not in \(\mathfrak E\) (Lemma 8.1(b)), but they are in CA-I's set unless they are associated bonds; at least \(L^3-8>0\) per coarse boundary site are not. Moreover the cardinalities differ: \(|Y_j^{(j)*}|-|\mathfrak F|=(\#\text{outer-interface }j\text{-bonds})-(\#\text{outer-interface }(j+1)\text{-bonds})\ge(L^3-1)\cdot\#\{\text{coarse boundary sites}\}>0\). So under this reading **GEO-slot is false** (a conditional counterexample: it is conditional on 74315 using 159071's convention). The two stages would integrate different numbers of variables.

**Attack 2 (both endpoints in \(Y\)).** *Failure:* the inner-interface \(j\)-bonds have one endpoint in \(Y_j\) and one in \(Z''_{j+1}\subset\Omega^c_{j+1}\); by Lemma 8.1(b) they are in \(\mathfrak E\), and all but \(\le8\) per coarse site are free. They are not in CA-I's set under this reading. Also this reading makes \(\mathfrak b_j\)-identity false. So S♮(1) fails under it.

**Attack 3 (exactness: every variable integrated once).** H-LF (`in1.md` L145) requires each variable to be "retained or integrated exactly once". In ST1's convention an outer-interface \(j\)-bond has an endpoint in \(\Omega_{j+1}\); its level-\(j\) variable is integrated by the small-field integration of level \(j+1\) on \(\Omega_{j+1}\), before the operation. If CA-I's presentation is also exact, it cannot integrate that variable again at the stage; so CA-I's stage set cannot contain outer-interface bonds that its own small-field step already integrated. This would force S♮(1)'s outer half, *if* CA-I's small-field step at level \(j+1\) integrates exactly the \(j\)-bonds with an endpoint in \(\Omega_{j+1}\). *Failure:* that is a statement about CA-I's small-field bond convention, which I have not read (it is not in the ranges the consumers cite), and exactness of CA-I's presentation is itself what FM-match would test. The attack reduces S♮(1) to an equally unread convention; it does not prove it.

Exact reason S♮ stays open: it is a statement about the meaning of a notation in another text (CA-I's bond-of-a-set convention at 74315 and B-CMP119 (1.9)), not about the history. The only convention CA-I states explicitly (159071) refutes it; a consistent exact reading would support it. Deciding needs CA-I's small-field-step bond convention and B-CMP119 (1.9).

### 8.4 What depends on GEO-slot

`st1-r4.md` names GEO-slot at L153 (statement), L924 (import list of the folded F-measure text), L1031 (FM6), L1105 (FM-match: "GEO-slot alone does not do it either") and L1587 (Corollary 14′). The proofs of F1–F4, Theorem FM, (FMg), Lemma 12 and Theorem 14 use ST1's own rows \(\mathfrak E,\mathfrak C,\mathfrak F\) and do not read CA-I's index sets. So only FM6 and the CA-I clause of Corollary 14′ depend on S♮; both serve FM-match, which the assembly lists as needed "only for a CA-I presentation" (`assembly-status.md` §2.3). No frozen proof uses GEO-slot wrongly; FM6 is a correct implication from it. If Attack 1's reading is CA-I's, then FM6's premise is false, and FM-match must also reconcile the outer-interface variables (a real dimension mismatch, not a relabelling).

## 9. Lift

### 9.1 What must embed

`cls.md` uses, at level \(j\) in level-\(j\) \(M\)-cube units (cls D1): hubs \(U_j=N_2H_j\) with \(s(U_j)\le D_j=C L\check R_j+6\) (G, L19); members \(M_j\) with \(s(M_j)\le D_j^*=2CL\check R_j+6\) and \(M_j\subset N_{w_j^*}H_j\) (Lemma 4, L120); and read margins of at most \(c+c_{\rm rd}\) cubes around a member (L22, L147). The distances \(G_j=10L\check R_j-2\) and \(\check R_j/2\) in (8) are torus distances; they need no lift. Trees \(T_f\) are used through edge counts and adjacency only (L53, L143); they need no lift.

**Definition 9.1.** A set \(A\) on the torus *embeds with margin \(m\)* if there is a coordinate box \(\widetilde Q\subset\mathbb Z^4\) of side \(\le T/2\), \(T\) the torus side in the same units, whose image contains \(N_mA\). Then the covering map is injective on \(\widetilde Q\) and preserves sup-distances between points of \(N_mA\) (all lifted differences are \(\le T/2\)).

### 9.2 The theorem

**Theorem L (Lift on admissible tori).** Put \(C_{\rm tor}:=2CL+8+2c+2c_{\rm rd}\) (cls's \(C=C_{\rm isl}\), \(c=c_{\rm col}\)). Call a torus of side \(\ell\) (final-level units) at final level \(K\) *admissible* if
\[ \tfrac12\ell\ \ge\ C_{\rm tor}\,M\,\check R_K. \tag{AT} \]
Then on every admissible torus, at every level \(j\le K\), every hub, member and their read margins embed with margin \(c+c_{\rm rd}\), provided the side bounds \(s(U_j)\le D_j\), \(s(M_j)\le D^*_j\) hold for their path-lifts (as cls Lemma 4 computes them).

*Proof.* At level \(j\) the torus side in level-\(j\) units is \(\ell L^{K-j}\), i.e. \(\ell L^{K-j}/M\) level-\(j\) \(M\)-cubes. A member's path-lift lies in a box of side \(D^*_j\) cubes, so \(N_{c+c_{\rm rd}}M_j\) lies in a box of side \(D^*_j+2(c+c_{\rm rd})\le(2CL+6+2c+2c_{\rm rd})\check R_j\le C_{\rm tor}\check R_j\) cubes (\(\check R_j\ge1\)). Hubs are smaller. By Lemma 2.1, \(\check R_j\le L^{\lceil(K-j)/2\rceil}\check R_K\le L^{K-j}\check R_K\). So (AT) gives \(\tfrac12\ell L^{K-j}/M\ge C_{\rm tor}\check R_KL^{K-j}\ge C_{\rm tor}\check R_j\). Thus the box has side \(\le\) half the torus side, and Definition 9.1 applies. A path-lift of a connected union of cubes is well defined on a box of side \(<T\): the covering map is injective there. ∎

Consistency with SA 17583. SA's condition "\(\tfrac12\ell L^{K-i}\ge CM\check R_i\) for \(i\le k\)" is (AT) with \(C=C_{\rm tor}\), via the same Lemma 2.1 bound (SA writes \(\check R_i\le L^{K-i}\check R_K\)). For a first-passage datum, \(x_K\le g^{-2}+B_\sharp\), so \(\check R_K\le L(\log(g^{-2}+B_\sharp))^r\) and (AT) is a lower bound on \(\ell\) given \(g\) and \(M\). The torus is chosen at IN1 row 10, after all constants; so (AT) creates no cycle. IN1 Lemma 6's cones (site boxes of side \(2L^{t-l}\) in level-\(l\) units, i.e. 2 level-\(t\) units) and the class boxes (\(\le b_{\rm cl}\) cells) are far smaller and embed under the same (AT).

Status: **proved** on admissible tori, given cls's own side bounds (cls D2's G and Lemma 4, which are cls's lemmas, distilled and not refereed). The hub bound G is an LF1 geometry input of cls, not one of the six statements here; for a standing hull at its birth level it is the class size \(b_{\rm cl}=100\) cells \(=100\check R_j\) cubes, which is \(\le CL\check R_j+6\) once \(C\ge100/L\). Its persistence under Mon is cls Lemmas 3–4.

## 10. Order of the constants

IN1's rule (`in1.md` L223): "A returned constant must precede every choice it bounds", with Amendment 1 (\(L>L_0^\natural\) at row 2, \(\kappa\ge\kappa_0^\natural(L)\) at row 4). Every constant of §§2–9 is fixed at row 2 (after \(r\) at row 1 and \(L\) at row 2), from design integers and \(L,r,\overline B\) only. None reads \(\kappa,\bar\kappa,M,X_0,\gamma\), the torus, or any activity amplitude. IN1 row 7 lists \(C_g,s_0,C_T,N_{\rm cut},b_{\rm code},D,C_v\) after \(c_{\rm lin}\); a constant fixed at row 2 may be listed later without change, so row 7 is consistent (it only says that \(c_G\) and \(c_{\rm ent}\) come after them).

| Constant | Value | Depends on | Fixed at (IN1 row) | Used in |
|---|---|---|---|---|
| \(b_{\rm bx}\) | boxing cube side, design integer | — | 2 | G4, Lemma 2.2 |
| \(b_{\rm cl}\) | \(100\) (CA-I 53749) | — | 2 | G6, Theorems G3, G4(a) |
| layer integers | \(2,4,8,10\) and round layer \(1\) (SA 17320–17322) | — | 2 | (G2) |
| \(e\) | \(32+3b_{\rm bx}\) | \(b_{\rm bx}\) (\(L\ge27\)) | 2 | Lemma 4.3 |
| \(h_0\) | \(2e+1\) | \(e\) | 2 | Lemma 4.4 |
| \(C_g\) | \(h_0^4\) | \(h_0\) | 2 | (14), light threshold |
| \(s_0\) | \(2\lceil\log_L(256h_0)\rceil\) | \(h_0,L\) | 2 | (14) |
| \(\alpha_L,b_0\) | \(h_0C_g+2e\); \(2\lceil\log_L\alpha_L\rceil\) | \(h_0,e,L\) | 2 | Theorem G3 |
| \(C_T\) | \(b_0+2\) | \(b_0\) | 2 | waiting rule |
| \(N_{\rm cut}\) | \(b_{\rm cl}^4=10^8\) | — | 2 | cut leaves; H-C's \(c_G\le c_w/(2N_{\rm cut})\) at row 7 |
| \(D\) | \(L^4+82\) | \(L\) | 2 | Lemma 9 |
| \(b_{\rm code}\) | §5 formula | \(K_s,K_o,K_{\rm st},K_f,p_f,L,r\) | 2 | Lemma 9 |
| \(C_v\) | \(2\) | — (needs \(R_j\ge2c_{\rm rd}/(2^{1/4}-1)\), an \(X_0\) floor, row 9) | 2 | source volume |
| \(c_{\rm bx}\) | read reach of an output row, design integer | — | 2 | GEO-box; floor \(M\ge c_{\rm bx}+1\) at row 5 |
| \(C_{\rm tor}\) | \(2C_{\rm isl}L+8+2c_{\rm col}+2c_{\rm rd}\) | cls's \(C,c\) (cls: before \(\kappa\)), \(L\) | 2 | (AT); the torus itself at row 10 |
| \(X_0^{\rm dr}\) | Lemma 2.1 | \(L,r,\overline B\) | 9 (a floor on \(X_0\)) | no consecutive drops |
| \(w\), \(N_{\rm crit}\) | Proposition D3 | \(L,r,\overline B,b_{\rm bx}\) | 9 (floor \(R\ge N_{\rm crit}\)) | §11 |

Independence. \(M\) enters only through the volume weights \((MR_n)^4\) inside \(V^\circ\) and \(b_{\rm code}V^\circ\) (where it cancels against per-site counts) and through the GEO-box floor \(M\ge c_{\rm bx}+1\). \(\kappa,\bar\kappa\) do not enter. So all of S1–S4, S6 hold with constants fixed before \(\kappa\), independent of \(M\) and \(\bar\kappa\), as IN1 requires (`in1.md` L147: "fixed \(C_g\ge1,s_0\ge1,C_T\ge1\)"; row 7).

Lemma 8's constant. With these values, IN1's \(C_{\rm cnt}=2C_g(5C_g+1)+4C_g^2s_0\) (L488) is fixed at row 2 as well. Lemma 8's coupling ceiling (\(c_GP_n^2\ge2P_n+C_{\rm cnt}T_n\widehat r_n\), \(P_n/2\ge C_{\rm cnt}T_n\widehat r_n\)) is imposed at row 9, after \(c_1\); it uses \(T_n\le C_TR_n\) and \(p_0>6r\). Nothing here changes that order.

## 11. Drop-outs (Task 4)

`cp12-draft.md` Proposition 8.6 (L275–283): "Suppose an admitted history has, at step \(k\), a standing drop-out mark \((t,X)\) with \(k-t=m\), \(n(X)=\mathsf N_t\), and a plaquette \(p\) in \(X\) with \(p\in\Omega^\circ_{t_\flat}\setminus\Omega^\circ_{t_\flat+1}\) and \(p\in X\setminus Z''_t(X)\). Then \(n_{\rm d}(p)=m\) and \(x_k(p)-x_k\ge\tfrac{c_0}2(m+\mathsf N_t)-2c_2-B_b\)." L283: "I did not prove that such histories exist; that is a statement about the history construction (H-G)."

### 11.1 The genealogy count and the coding are unaffected

**Proposition D1.** (a) The nodes, predecessor links, occupied sets and cell counts of §4 are as made (Definition 2.5); a drop-out at operation \(t\) changes label entries only at levels \(l\le t\) inside its own node \(X\), after the nodes of those levels were made. So (14), Theorems G1–G4 and their constants are the same with or without drop-outs. (b) The drop-out node \((t,X)\) itself is a mark node: it is counted in \(n^{\rm mk}_t\), its successor starts a new chain (Theorem G3, Remark 1), and it creates no copy of its older nodes (SA 18443: "Keeping a drop-out does not make another copy of all its older nodes"). (c) If one reads the genealogy from the current label instead: the action label (\(\boldsymbol\nu=0\)) keeps the pre-operation entries inside drop-outs (G8), so inside drop-outs it gives the as-made components. The determining label gives \(Z_l^{\rm d}\cap X=Z''_l(X)\subset\Omega_l^{\circ c}\cap X\subset Z_l^\circ\cap X\) at window levels; at these levels \(X\cap Z^\circ_l\) is a single component (class condition at \(l\ge t_\flat\)) and \(Z''_l\) is a single box, so the tree has the same shape and fewer cells. Hence every count of §4 read on the determining label is at most the as-made count. SA 18461 fixes the as-made (action) reading for the volume: "The determining regions may have redone some of these levels and cannot replace them in this count."

*Proof.* (a) is (G7)–(G9) plus Definition 2.5. (b) is Definition 2.5 and Theorem G3. (c) is (G8) and Lemma 2.4. ∎

**Proposition D2 (coding).** A drop-out adds to the code only its stage count \(n(X)\in\{0,\dots,\mathsf N_t\}\) and its failure data, already included in \(b_{\rm code}\) (§5). The nest boxes are determined by (G9); \(\boldsymbol\nu\) is not a history datum. So the coding (Lemma 9's hypotheses) is unchanged. The stage count difference of Proposition 8.6 (\(\le\mathsf N_t\) levels) is paid by the mark credit: each mark pays \(T_t\widehat r_t\) with \(T_t\ge\mathsf N_t\) (Theorem G3), which is IN1 Lemma 8's "\(P_n/2\ge C_{\rm cnt}T_n\widehat r_n\)". ∎

Where the discrepancy does enter. The profile coupling \(x_k(p)\) reads the action sequence; the backgrounds read the determining one (SA 17440). This is an H-E/H-SF matter (per-site normalizers and the signed profile), not a geometry one. IN1's (6) charges \(\mathsf l_n=1+\log x_n\) per site at the node level \(n\). If H-E's per-site normalizer at a site \(p\) reads \(\log x_n(p)\) rather than \(\log x_n\), then H-E must bound the difference. That is outside GEOH; I record it for the H-E owner. The bound of Proposition D3 below makes it logarithmically small inside drop-outs.

### 11.2 The nest gap

**Lemma D0 (nest gap).** Let \(X\) be a class component at level \(t\), \(m_u=M\xi_u\) the level-\(u\) \(M\)-cube side (level-\(t\) units). For \(t_\flat<u\le t\), \(\operatorname{dist}_\infty(Z''_{u-1},(Z''_u)^c\cap X)\ge m_u\), and \(Z''_{t_\flat}=Z_{t_\flat}\cap X=:C\) (the core).

*Proof.* \(Z''_{t_\flat}=Z_{t_\flat}\cap X\) is (G9) with \(h=t_\flat\). For \(u\in I_M=(k_0,t]\), consecutive members are "separated by one layer" of level-\(u\) \(M\)-cubes (G9), so the gap is \(\ge m_u\). For \(t_\flat<u\le k_0\): \(Z''_u=(\Omega_u^{\sim5})^c\cap X\) contains every point of \(X\) at distance \(\ge6m_u\) from \(\Omega_u\cap X\) (five layers, plus one cube of rounding). By Lemma 7.2, \(\Omega_u\cap X=X\setminus N_8H_u\) and \(H_u\supset Z_{u-1}\cap X\supset Z''_{u-1}\). A point of \(H_u\) is at distance \(\ge8s_u\ge8m_u\) from \(X\setminus N_8H_u\). So a point within \(m_u\) of \(Z''_{u-1}\) is at distance \(\ge7m_u\ge6m_u\) from \(\Omega_u\cap X\), hence in \(Z''_u\). ∎

### 11.3 The action level inside a drop-out

**Proposition D3.** Let \((t,X)\) be a drop-out with \(n\) completed stages, standing at time \(k\ge t\). Let \(p\in X\), and let \(j\in(t_\flat,t_\flat+n]\) with \(p\notin Z''_j(X)\) (so \(p\in\Omega^{\rm d}_j\)). Put
\[ w:=\big\lceil\log_L\big(2(11+b_{\rm bx})\check R_{t_\flat}\big)\big\rceil . \]
Then \(p\in\Omega^\circ_l\) for every \(l\le j-w\). Hence \(j_{\rm a}(p)\ge j_{\rm d}(p)-w\) and \(n_{\rm a}(p)\le n_{\rm d}(p)+w\) whenever \(j_{\rm d}(p)\) lies in that window. Moreover
\[ \check R_{t_\flat}\le C_1'(1+\mathsf N_t),\quad C_1':=L2^{r-1}\big(1+r^r(1+\overline B)\big),\qquad w\le1+\log_L\!\big(2(11+b_{\rm bx})C_1'\big)+\log_L(1+\mathsf N_t). \]
Consequently, if \(\mathsf N_t\ge N_{\rm crit}\), where \(N_{\rm crit}\) is the least integer \(N\) with \(N\ge2+\log_L(2(11+b_{\rm bx})C_1')+\log_L(1+N)\), the hypotheses of `cp12-draft.md` Proposition 8.6 cannot all hold: \(p\notin Z''_t\) with \(n=\mathsf N_t\) forces \(p\in\Omega^\circ_{t_\flat+1}\).

*Proof.* Write \(C=Z_{t_\flat}\cap X\), \(A_l=X\cap\Omega_l^{\circ c}\), \(B_l=X\cap Z^\circ_l\), pre-operation entries, \(t_\flat\le l\le t\). By Lemma 7.2, for \(t_\flat<l\le t\), \(A_l=N_8H_l\subset N_{10}H_l\subset B_l\), \(H_l\) the level-\(l\) hull of \(B_{l-1}\), and \(B_l=\mathsf{bx}(N_{10}H_l)\cap X\). A cell hull lies within one cell side \(s_l\) of its set, ten layers add \(10s_l\), and boxing adds \(\le b_{\rm bx}s_l\) (Lemma 2.2). So \(B_l\subset\{x:d(x,B_{l-1})\le(11+b_{\rm bx})s_l\}\), and by induction from \(B_{t_\flat}=C\),
\[ A_l\subset B_l\subset\{x:d(x,C)\le\tau_l\},\qquad \tau_l:=(11+b_{\rm bx})\sum_{u=t_\flat+1}^{l}s_u. \]
Here \(s_u=\check R_um_u\le\check R_{t_\flat}m_u\) (\(\check R\) non-increasing) and \(\sum_{u\le l}m_u\le m_lL/(L-1)\). So \(\tau_l\le(11+b_{\rm bx})\tfrac{L}{L-1}\check R_{t_\flat}m_l<2(11+b_{\rm bx})\check R_{t_\flat}m_l\).
By Lemma D0, \(Z''_j\supset\{x\in X:d(x,C)<\sigma_j\}\) with \(\sigma_j=\sum_{u=t_\flat+1}^jm_u\ge m_j\). If \(j-l\ge w\), then \(m_j=L^{j-l}m_l\ge L^wm_l\ge2(11+b_{\rm bx})\check R_{t_\flat}m_l>\tau_l\), so \(A_l\subset Z''_j\). Since \(p\notin Z''_j\), \(p\notin A_l\), i.e. \(p\in\Omega^\circ_l\). For \(l\le t_\flat\): \(p\notin Z''_j\supset C=Z_{t_\flat}\cap X\supset\Omega^{\circ c}_{t_\flat}\cap X\supset\Omega^{\circ c}_l\cap X\), so again \(p\in\Omega^\circ_l\).
Frame bound. Let \(m_\cdot\) now denote running minima of \(\theta\). If \(\min_{i\le t}\theta_i\) is attained at \(v\le t_\flat\), then \(\min_{i\le t_\flat}\theta_i=\min_{i\le t}\theta_i\). Otherwise it is attained at \(v\in(t_\flat,t]\) and \(\min_{i\le t_\flat}\theta_i\le\theta_{t_\flat}\le\theta_v+\overline B(v-t_\flat)\le\min_{i\le t}\theta_i+\overline B\mathsf N_t\) (Frame). As \(\min\theta\ge1\), \(\log\min_{i\le t_\flat}\theta_i\le\log\min_{i\le t}\theta_i+\log(1+\overline B\mathsf N_t)\). With \((a+b)^r\le2^{r-1}(a^r+b^r)\), \((\log(1+y))^r\le r^r(1+y)\) (`cp12-draft.md` Lemma 8.4's inequality), and \(\check R\le L(\log\min\theta)^r\), \((\log\min_{i\le t}\theta_i)^r\le\check R_t=\mathsf N_t\):
\(\check R_{t_\flat}\le L2^{r-1}[\mathsf N_t+r^r(1+\overline B\mathsf N_t)]\le C_1'(1+\mathsf N_t)\). Take \(\log_L\).
Last claim: with \(n=\mathsf N_t\), \(j=t=t_\flat+\mathsf N_t\), and \(l=t_\flat+1\le t-w\) iff \(\mathsf N_t-1\ge w\), which holds when \(\mathsf N_t\ge N_{\rm crit}\). Then \(p\in\Omega^\circ_{t_\flat+1}\), contradicting Proposition 8.6's \(p\notin\Omega^\circ_{t_\flat+1}\). ∎

Since \(\mathsf N_t=R_t\ge(\log X_0)^r\), the condition \(\mathsf N_t\ge N_{\rm crit}\) is a floor on \(X_0\) (IN1 row 9), fixed after \(L,r,\overline B,b_{\rm bx}\).

Credit and difference. This is `geo5c-count.md` (F3) Case 2 with two changes: boxing reach \(b_{\rm bx}\) is included (geo5c used SA's \(H^{[10]}\) without it), and the frame bound is linear in \(\mathsf N_t\) instead of quadratic (geo5c (F4) gives \(C_1(1+\check R_k)(1+k-u)\), here \(k=t\), \(k-u=\mathsf N_t\)). The nest gap Lemma D0 is derived here from CA-I's prepared sequence (53776–53784) and Lemma 7.2, not from `geo-5.md`.

### 11.4 What this means for the consumers

1. The genealogy count (14) and the coding are not affected by drop-out windows (D1, D2).
2. Proposition 8.6's configuration does not occur in the actual history above the floor \(\mathsf N_t\ge N_{\rm crit}\) (D3). Proposition 8.6 is a correct implication, but its existence hypothesis is false for the actual history. So the literal (H-prof) is **not refuted** by it.
3. D3 gives a sharper corrected profile bound than (H-prof♯). Inside windows \(n_{\rm a}\le n_{\rm d}+w\), so `cp12-draft.md` Lemma 8.2 gives \(|x_k(p)-x_k|\le B_b(1+n_{\rm d}(p)+w)\). By cp12 (8.2) and \(k-t\le n_{\rm d}\), \(\mathsf N_t\le L2^{r-1}[(\log\theta_k)^r+r^r(1+\overline Bn_{\rm d})]\), so \(w\le C_w+r\log_L\log\theta_k+\log_L(1+n_{\rm d})\) with \(C_w\) fixed after \(L,r,\overline B,b_{\rm bx}\). This replaces \(C'_x(\log\theta_k)^r\) by \(B_br\log_L\log\theta_k\). Whether the literal (H-prof) with a constant \(C_x\) holds needs a lower-bound configuration with \(j_{\rm d}-j_{\rm a}\) unbounded; D3 neither gives nor excludes one. Corollary 8.7's consumer closes a fortiori.

## 12. Status, inputs, and uses of the six statements by frozen texts

### 12.1 What is proved, from what

All proofs above are implications from the rules (G1)–(G9) of the actual step, each quoted with its SA or CA-I line, plus:
- the frame (1) and tube (3) of IN1, and the floors \(X_0\ge X_0^{\rm dr}\), \(R\ge N_{\rm crit}\), \(R\ge2c_{\rm rd}/(2^{1/4}-1)\) (IN1 row 9);
- the design integers \(b_{\rm bx},b_{\rm cl}=100\), the layer integers, \(K_s,K_o,K_{\rm st},K_f,p_f\), the read collar \(c_{\rm rd}\) and the output read reach \(c_{\rm bx}\). These are parts of the step's specification (they count objects the step defines). They are not physics; fixing them is a design choice, and every bound above holds for any fixed values;
- for GEO-mark, the reading (Q) of SA 17575's quarantine clause (§6.1);
- for GEO-box, Definition 7.1 of \(\mathcal B_t\);
- for Lift, cls's side bounds (cls D2's G and Lemma 4) and the admissible-torus floor (AT).

(G9) is CA-I's description of Bałaban's prepared sequence (CA-I 53776–53802, quoting B-CMP122a §1). I use it as the specification of the actual operation's nest and box. If the actual operation is specified differently, Lemma 2.4 (i)–(iii), Lemma 7.2's use, Theorem B and Lemma D0 must be re-checked against the new nest; the other results do not read (G9).

| Statement | Status |
|---|---|
| S1 (14), waiting rule, leaves, cut islands, (6) multiplicity, source volume, coding | **proved** (Theorems G1–G5) |
| S2 (ANC) | **proved** (Theorem A) |
| S3 GEO-mark | **proved** (Theorem M), under (Q) |
| S4 GEO-box | **proved** (Theorem B), for Definition 7.1 |
| S5 GEO-slot | **Outstanding**: Lemma S♮ (§8.2); three attacks failed (§8.3); conditionally false under CA-I 159071's convention |
| S6 Lift | **proved** (Theorem L), on admissible tori (AT) |

### 12.2 The first remaining Outstanding statement

**Lemma S♮.** (1) In CA-I 74315 the "\(j\)-bonds of \(Y_j\)", \(Y_j=(\Omega^c_{j+1}\setminus Z''_{j+1})\cap Z\), are the level-\(j\) bonds with an endpoint in \(Y_j\) and no endpoint in \(\Omega_{j+1}\) (label in force), and likewise for \((j+1)\)-bonds; (2) the bond B-CMP119 (1.9) associates with a \((j+1)\)-bond \(c\) is F2's pivot \(b_0(c)\); (3) the rim bonds of \(Z_{j+1}\cap\Omega_{j+1}\cap Z\) carrying \(A_j\) are exactly the stored level-\(j\) slots whose collar is integrated at that stage.

Attacks and reasons (§8.3): (1) CA-I's explicit count convention (159071, "at least one end-point") makes S♮(1) false at the outer interface, with a dimension excess \((L^3-1)\) per coarse interface face; (2) the both-endpoint reading excludes inner-interface removed rows, which are in \(\mathfrak F\); (3) the exactness argument (each variable integrated once) reduces S♮(1) to CA-I's small-field-step bond convention, which is unread and is itself what FM-match tests. S♮ is a statement about another text's notation, not about the history. It feeds only FM6 and the CA-I clause of Corollary 14′ (§8.4).

### 12.3 Uses of the six statements in frozen texts

No frozen proof uses one of the six statements beyond what is proved here, except through GEO-slot (open). Specific points:
1. `ag1.md` L72 cites "Lemma 1 (lines 412–413)" as the use of (ANC); the use is L414–415. Wording only.
2. `st1-r4.md` GEO-slot (L153) and `f-meas.md` L40: "correspond exactly" is false under CA-I's own stated bond convention (Attack 1). FM6 (L1031) is a correct implication from it. If Attack 1's reading is CA-I's, FM-match must reconcile a dimension mismatch at the outer interface. Not a defect of any other ST1 proof (§8.4).
3. `in1.md` row 7 lists \(C_g,s_0,C_T,N_{\rm cut},b_{\rm code},D,C_v\) after \(c_{\rm lin}\). They can be fixed at row 2. The listing is harmless.
4. `in1.md` (14) is true with the stronger coefficient \(1\) on the creation sum (Theorem G2).
5. `st1-r4.md` row 5 (L166) uses \(C_g\) for a formation constant; IN1 uses \(C_g\) for the geometry constant. Two constants, one name.
6. `st1-r4.md` GEO-box's wording "Specify the affected output-loop family" is met by Definition 7.1. With that choice the analytic burden for loops straddling \(\partial\Lambda^{\rm pr}\) is on BOX-bg (§7.3), which `st1-r4.md` keeps as a hypothesis. No frozen text claims otherwise.
7. Not frozen: `cp12-draft.md` Proposition 8.6's existence hypothesis is false for the actual history above \(\mathsf N_t\ge N_{\rm crit}\) (Proposition D3). Its "refuted conditionally" verdict on the literal (H-prof) (L16, L295) should become "not refuted; corrected form (H-prof♯) proved, and sharpened by D3".

### 12.4 What a distil should check first

- Lemma 4.3's two-level reach invariant, and that boxing reach does not accumulate across rounds (Lemma 2.2's last sentence).
- Theorem G3's class-entry argument: that the chain node at level \(k=\ell_1+b_0+\mathsf N_{\ell_1}\) meets all three class conditions, in particular quarantine via (Q).
- Theorem G4(c): that action-label components are whole as-made components (healing and islands remove whole components, by nesting and connectedness).
- Lemma D0's distance arithmetic for \(t_\flat<u\le k_0\) (units of \(\sim5\) layers).
- §8.3 Attack 1's interface count \(I_j=L^3I_{j+1}\).

## Result

For the actual multiscale history (SA's step with the Y3 relative form, chart-free intrinsic domains, the (Tq0) table without radius lift, and CV's averaged-contour representative), five of the six GEOH statements are proved here as hand implications from the quoted region rules: IN1's H-G in full ((14), the waiting rule, leaves and cut islands, the volume multiplicity, the source-volume comparison, and the coding hypotheses of Lemma 9), AG1's (ANC), ST1's GEO-mark (under the stated quarantine reading), ST1's GEO-box (for an explicit \(\mathcal B_t\)), and cls's Lift (on admissible tori). All their constants are fixed at IN1 row 2, before \(\kappa\), independent of \(M\) and \(\bar\kappa\); the only later items are \(X_0\) floors at row 9, the \(M\) floor \(M\ge c_{\rm bx}+1\) at row 5, and the torus at row 10. ST1's GEO-slot remains Outstanding as Lemma S♮, a notation-identity statement about CA-I; under CA-I's own stated bond convention it is false at the outer interface. Drop-out windows do not affect the genealogy count or the coding (14); and the drop-out configuration of `cp12-draft.md` Proposition 8.6 does not occur in the actual history above a coupling floor, because inside a drop-out the action and determining levels differ by at most \(w=O(\log_L(1+\mathsf N_t))\).

This is pass 1. It is not refereed and grants no status.
