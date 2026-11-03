lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T12:46Z

# meet-6c: P81, P82° and Theorem 6(c) on the meet localisations W1-W4 of 2.8, with (SEP)

Queue row 104. Pinned at a86c38fba (branch `claude/ym4d-hard-route`). Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Same-model research text, not gated, not an audit; grants no status. Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (SHA-256 `d7f77d4d...b4d6f`, matching `gates/a3-derivative-gate.md`). No numeric job was run (Section 2.7 says why none could help); every step is written by hand.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for every definition read here: separated sequences and their floors (SA 9593-9600, 9661), Theorem 6 (a)-(c) with the localisation as a cube-wise meet of a tower with a separated sequence (SA 9783-9789), Proposition 2.3 and the operation's nests, shells and core (SA 17398-17437, 17576-17598), the label's first member (SA 17317). T. Balaban for the architecture behind the inputs: CMP 102 Theorem 1 (the orbit), CMP 99 (389-434) (background propagators by cell gauges and flat parametrices), CMP 95, 96, 89 (the flat package). OpenAI Codex for `a1-balaban.md`, `flat-port.md`, `a3-balaban.md`, `a3-derivative.md` Sections 1-6 and the gates of rows 89 and 100. Claude for `sa-2.8-terms.md` (Lemma MJ), `a3-close.md` (Lemma J, Section 1), `a3-derivative.md` Sections 6.1-10, `p82-curved.md`.

## 0. Result

**P81, P82° and Theorem 6(c) hold on the four meet localisations W1-W4, as implications; (SEP) and (SEP-L) hold for the outline's localisations given its Proposition 2.3. No counterexample.**
- *Hole boundaries are harmless.* In every separated sequence a hole of \(\Omega_0\) is surrounded by bare layer 0. Theorem P, the A1 port and the flat package all treat \(\partial\Omega_0\) by shape-free bare cells, and the outline admits any shape (SA 9596).
- *The meets are separated sequences.* Lemma J\* proves this, with (G1)-(G3), alignment and mismatch sets in the collars. So [A1], [Reg] and [P°] apply verbatim (Proposition 5.1).
- *Theorem M* gives the comparison in the form 2.8 needs: decay from \((X^-)^c\), \(C\) or \(\Lambda\), uniformly in level, depth, torus and history.
- *One defect, essential for \(R_1\) and repaired here (D1).* I1 measured decay from \(W^c\). Since the label's first member is \(\Omega_1^\sim\ne\mathbb T\) (SA 17317), that set contains the label's holes, and \(R_1\)'s global sum would then not be small.
- *Remaining inputs:* the same-model `a3-close.md` §1 and Lemma J, the outline's geometry (Proposition 2.3, EXT), and I5 on the global datum.

## 1. Statement and inputs

**Moves:** `library/sa-2.8-terms.md` Section 8, open item 1, "the input where 2.8 would fail": I1 (Theorem 6(c)) on the four comparisons W1-W4, with P81 and P82° on their meet sequences, and (SEP).

**Setting.** As in `sa-2.8-terms.md` Sections 1 and 3: level-\(k\) units, \(\eta=L^{-k}\), \(\xi_j=L^{j-k}\); \(X\) a class component; \(\Lambda=\Lambda^{\rm pr}\); \(C=C_{k_\flat}=X\cap Z_{k_\flat}\); the shells; \(\mathcal O^p,\mathcal O^h\) the global prepared and healed determining sequences; \(\mathcal L_X\) the outline's localisation in \(X\); \(\mathbf D_{pX}=\mathcal L_X\mathcal O^p\); the backgrounds \(P,P_X,H,R(b),S=R(0),T(B)\); \(\theta=\delta_0/8\). The lengths \(\mathfrak M=M_1\) (cube size), \(\rho=R_1\mathfrak M\) (gap), \(\mu=M_1'\ge\rho\) (collar unit), \(M\) (localisation cube side) and \(\check R=\check R_k\) are powers of the odd integer \(L\) (SA 5585-5591, 6029, 9596). Every cube used below is therefore a block of some lattice \(\mathbb T^{(m)}\), and the partitions are nested; "aligned" means this.

**The four comparisons**, with the part \(A_i\) and collar level \(j_i\) fixed here (the table of `sa-2.8-terms.md` I1 leaves them implicit):

| | pair and sequences | part \(A_i\) | \(j_i\) | term |
|---|---|---|---|---|
| W1 | \(P\) on \(\mathcal O^p\); \(P_X\) on \(\mathcal L_X\mathcal O^p\) | \(X^-\): the union of the aligned \(\mu\)-cubes \(Q\subset X\) with \(\operatorname{dist}_\infty(Q,X^c)\ge\frac14M\check R\) | \(k\) | \(R_6\) |
| W2 | \(H\) on \(\mathcal O^h\); \(R(b)\) on \(\mathcal L_X\mathcal O^h\) | \(X^-\) | \(k\) | \(R_3\) |
| W3 | \(T(B)\), \(P_X\), both on \(\mathbf D_{pX}\) | \(\mathbb T\setminus C\) | \(k_\flat\) | \(R_7\) |
| W4 | \(P\) on \(\mathcal O^p\); \(H\) on \(\mathcal O^h\) | \(\mathbb T\setminus\Lambda\) | \(k\) | \(R_1\) |

**The meet** of a separated sequence \(\Omega\) with a part \(A\) of level \(j\) (first erosion rule, cut at depth \(j\); SA 9646, 9783):
\[
 \Omega'_q:=\Omega_q\cap T^A_{\min(q,j)},\qquad T^A_0=A,\quad T^A_{q+1}=\bigcup\{Q\ \text{aligned }\mathfrak M\xi_{q+1}\text{-cube}:\ \operatorname{dist}_\infty(Q,(T^A_q)^c)>\rho\xi_q\}.
\tag{1.1}
\]
So \(\Omega'_0=\Omega_0\cap A\). The joined datum \(\mathbf V^J\) is \(\mathbf V\) on the rows of \(\Omega'\) that are rows of \(\Omega\), and the lift of \(V_j\) on the others. \(\mathbf B'_i\) denotes the meet of W\(i\), \(U^\circ_i\) its background with datum \(\mathbf V^J_i\).

**Target (Theorem M, Section 6).** For each \(i\) and each background \(U\) of the pair, \(U|_{\Omega'_0}=(e^{i\eta f}U^\circ_i)^w\), with
\[
 \xi'_y|f|,\ \xi_y'^2|\nabla f|,\ \xi_y'^3|D^{\mathsf T}Df|\ \le\ E\,e^{-\theta d_{\mathbf B}(y,A_i^c)}
\tag{1.2}
\]
over every top \(y\) of \(\mathbf B'_i\) (scale \(\xi'_y\) in \(\mathbf B'_i\)). Here \(U^\circ_i\) is the same for both members of the pair, \(E=C_E\varepsilon_1\) with \(C_E\) depending on \(L,\rho,\mu\) only, and \(d_{\mathbf B}\) is the original metric of either sequence; the two metrics agree here (Lemma C(e)). The decay is measured from \(A_i^c\), that is from \((X^-)^c\), \(C\) or \(\Lambda\), and not from \((\Omega'_0)^c\). Section 8, D1 explains why that matters for W4.

**Inputs, with their labels.**
- [A1] `a1-balaban.md` Sections 7.3, 7.9, 8, 9 (Codex), gated ADVANCE conditional on F0 (`gates/a1-balaban-gate.md`, row 91). F0 is `flat-port.md` (Codex), gated with first failing step none (`gates/flat-port-gate.md`, row 99). For every separated sequence (cube size and gap above fixed thresholds, first floor) and every real \(\varepsilon\)-regular datum with \(\varepsilon\le\bar\varepsilon\), [A1] gives one regular critical orbit, (8.2), the holomorphic datum ball (9.2) and restriction (9.3). The first member is arbitrary: §7.3 and §7.9 build a bare boundary layer whose estimates are "independent of the shape of the intersection".
- [P°] `p82-curved.md` Theorem P (Claude), with the repairs D1-D3 of `gates/p82-curved-gate.md` (Codex, row 100): an ADVANCE as an implication. It holds for every separated sequence with \(\rho\ge\rho_0\), "of any depth, mesh, volume and region shape above the torus floors", and every real \(U\in\mathrm{Reg}_\alpha\) with \(\alpha\le\alpha_*\).
- [Reg] `a3-close.md` Section 1 (Claude; same-model, ungated): the A1 background of any separated sequence with gap \(\rho\ge\rho_0'=\max\{\rho_0,4LW+2L\}\) lies in \(\mathrm{Reg}_\alpha\), \(\alpha=C_LM'\varepsilon\).
- [10.1] `a3-derivative.md` Lemmas 10.1-10.4 (Claude), gated ADVANCE with the repairs of `gates/a3-derivative-gate.md` Section 10 (repaired 10.2, rebuilt 10.3-10.4, datum admission), including its consumer-check variant with a mismatch-set weight.
- [J] `a3-close.md` Lemma J (Claude; same-model, ungated). The parts used are re-derived in Section 3. [MJ] is `sa-2.8-terms.md` Lemma MJ.
- [SA] Outline assertions, not checked against a construction here: Proposition 2.3 (nest gaps; boxes are unions of \(M\)-cubes; large-field regions are unions of cells), the class geometry (SA 17576-17583), (2b) (\(\Lambda^{\rm pr}\), core, shells), the healed and prepared formulas (SA 17423-17437), Theorem 6(a).
- [I5] As in `sa-2.8-terms.md`: the data of every sequence used are \(\varepsilon_1\)-regular, \(\varepsilon_1=4L^2C_F\check R^2\varepsilon_k\). This is (D-F), gated for every case (rows 88, 94, 96, 97) given Proposition 2.4 and H1-H4. W1, W2 and W4 read it for the global label datum (Section 2.6).

## 2. Counterexample first

**Target failure** (queue row): a meet background in the class at which P82°'s curved inverse, or P81, loses uniformity at a hole boundary; or a meet that is not in the class at all. W3's meet has a hole (\(C\)); W4's is global and has the hole \(\Lambda\), together with the holes of the label's own first member, \(\Omega_0=\Omega_1^\sim\ne\mathbb T\) (SA 17317).

**2.1 A hole boundary is a bare boundary component.** In every separated sequence \(\operatorname{dist}_\infty(\Omega_0^c,\Omega_1)>\rho\eta\), so every point within \(\rho\eta\) of a hole lies in layer 0. The proofs treat \(\partial\Omega_0\) through cells that meet \(\Omega_0^c\), and none of them distinguishes an inner component of \(\partial\Omega_0\) from an outer one:
- in Theorem P every cell meeting \(\Omega_0^c\) is bare once \(\rho>c_LM_{\rm P}\), and Lemma 5.0 inverts the bare model at any unitary \(U\), for any shape of \(Z_i\cap\Omega_0\);
- [A1] §7.9 gives the boundary cubes (7.24)-(7.26), "independent of the shape of the intersection";
- `flat-port.md` §8.1 proves the bare model's inverse "uniformly over shapes";
- SA 9596 itself admits any shape: "no condition is imposed on the shape or the connectivity of the members".

So a failure has to come from one of four other places: (i) the meet is not a separated sequence (thin or misaligned layers near the hole); (ii) the topology of the hole is seen by a global step; (iii) the reference \(U^\circ_i\) is not in Reg near the hole; (iv) the joined datum is not regular near the hole. Each is tested below.

**2.2 (i) Thin layers: none.** The tower is built by maximal erosion, so \(\operatorname{dist}_\infty((T^A_q)^c,T^A_{q+1})>\rho\xi_q\) at every level, reentrant corners of \(A=\mathbb T\setminus C\) or \(\mathbb T\setminus\Lambda\) included. The construction is a statement about \(\ell^\infty\)-distance from a union of aligned cubes, and it never asks for convexity. Where the cut tower meets the old sequence, the gap is \((n_{\rm col}\mu-\rho)\xi_j\ge4\rho\xi_j\) (Lemma J(b), re-derived in Section 3). At the hole of W3 the \(k_\flat\) tower levels are compressed into a strip of width \(e_{k_\flat}\le\rho\xi_{k_\flat}\). Each of them still has a layer wider than \(\rho\xi_q\), and that is all Theorem P uses: with \(\rho>C_LM_{\rm P}L\) every cell, and every enlarged gauge cube of the gate's repair, meets only two adjacent layers. *No failure.*

**2.3 (ii) Holonomy: invisible.** W3's meet domain \(\Omega_0(\mathbf D_{pX})\setminus C\) is a box minus a box in four dimensions, hence simply connected. W4's domain \(\Omega_0\setminus\Lambda\) carries the loops of the torus and of the label's holes. A flat connection with non-trivial holonomy around such a loop has every plaquette equal to \(\mathbf 1\), and it lies in Reg with \(\alpha=0\) (`p82-curved.md` 2.3, gate: CORRECT-NO-ADVANCE, no reason to fail). No proof step forms a global gauge. Theorem P uses cell gauges; [A1] uses pillar-wise recursive gauges (§9.1) and gauges on cubes (§3.8); the flat local models are periodic copies of single cells. *No failure.*

**2.4 (iii) Reg near the hole: holds, in the meet's own units, and only there.** The meet background is genuinely rougher than either member of the pair near the collar. Take the collar of \(A\) in layer \(j\ge1\), and a bare plaquette \(p\) of the meet's layer 0 that lies in a coordinate 2-plane at the common corner of four level-\(j\) blocks \(B(y),B(y+e_\alpha),B(y+e_\alpha+e_\beta),B(y+e_\beta)\subset A\). Such corners reach to within \(\eta\) of \(\partial A\), because \(\partial A\) is a union of block faces. The four bonds of \(p\) are level-0 rows of \(\mathbf B'\) with the lifted data, so \(U^\circ\) equals the lift on them, and
\[
 \partial U^\circ(p)=\partial V_j(P),\qquad P=\text{the level-}j\text{ plaquette at }y\text{ in the }(\alpha,\beta)\text{ plane}.
\]
This can be of size \(\varepsilon\). The background \(U\) of the given sequence has \(|\partial U(p)-\mathbf 1|\le B\varepsilon(\eta/\xi_j)^2\) at the same \(p\), since \(p\) lies in its layer \(j\). So the curvature of \(U^\circ\) exceeds that of \(U\) there by up to \((\xi_j/\eta)^2=L^{2j}\), a factor that grows with the depth.

This is no counterexample. Regularity of \(U^\circ\) is required, and holds by (8.2), in the meet's local scale \(\mathsf L'(p)=\eta\), where the bound is \(B\varepsilon\). [Reg] derives the gauges from (8.2) in exactly those units: steps (ii)-(iv) of `a3-close.md` §1 use only \(Z\subset\mathcal L'_j\cup\mathcal L'_{j+1}\), the gap \(\rho\ge\rho'_0\), and the class conditions on \(\tilde\square\subset\Omega'_{j-1}\). The depth factor is confined to the collar. There (1.2) makes no small claim: \(e^{-\theta d}\) is \(O(1)\) on the collar, with \(d\) measured from the mismatch set. The example shows that a version of 6(c) measuring the collar in the original sequence's units would be false. The outline's 6(c) does not do that: "in the collar it is the scale of the tower".

**2.5 (iv) The datum near the hole: as regular as \(\mathbf V\).** Every test of \(\mathbf V^J\) is \(\mathbf 1\), or a level-\(j\) plaquette of \(V_j\) in the collar, or a test of \(\mathbf V\) (Lemma D). The reason is that \(\mathcal M\) of a lift is the lift one level up, so mixed tests at the tower's seams reduce to plaquettes of a single lift. *No failure.*

**2.6 The global comparisons: the only global premise is the datum.** W1, W2 and W4 involve the global \(P\) and \(H\), backgrounds of the global label sequences, which have arbitrary shape and many holes. [A1] and [P°] are uniform over shape (2.1), so the only way these comparisons can fail globally is that the global datum is not regular somewhere. That does happen without (D-F): a bare determining bond with \(V(b)=-1\) (`floor-screen.md` Example 1) has \(|\partial U(p)-\mathbf 1|=2\) for every compatible \(U\), so the global regular orbit is empty and \(P\) does not exist. So W1, W2 and W4 rest on I5 for the whole label datum, at every level and in every component, and not only near \(X\). W3 reads I5 only on \(\mathbf D_{pX}\). This is a scope statement about an input already on 2.8's list, not a new gap.

A second global point is the decay set. For W4, \(\Omega'_0=\Omega_0\setminus\Lambda\) with \(\Omega_0=\Omega_1^\sim\). A comparison stated with decay from \((\Omega'_0)^c\) would give no decay near the label's other holes, and the sum over all tops in \(R_1\) (`sa-2.8-terms.md` 5.5) would not be small. Near those holes \(P\) and \(H\) have the same sequence and the same data (Lemma C), and the mismatch of the comparison sits only at \(\partial\Lambda\). The mismatch-set form (1.2) gives decay from \(\Lambda\) alone (Theorem M; Section 8, D1).

**2.7 No run.** A failure of uniformity at a hole would need depth, so at least two layers and a tower, on a four-dimensional lattice. That is out of reach, and a two-dimensional one-layer run would only re-test the flat constants, which `gates/flat-port-gate.md` already kill-tested. No numeric job was started, and memory was not tested.

**Verdict.** No counterexample. A hole boundary is a bare boundary component, and the meets are separated sequences (Section 3). The reference is in Reg in the meet's own units, and the depth factor of 2.4 is confined to the collar, where (1.2) claims nothing small. The one global premise is I5 for the global datum.

## 3. The four meets are separated sequences

Fix \(n_{\rm col}:=5\). (This is the collar count of `a3-close.md` Lemma J, there called \(n_c\). It is not the margin \(n_{\rm c}=\lfloor\mathsf N/2\rfloor\) of `sa-2.8-terms.md` (1.1).) Assume \(M\ge16n_{\rm col}\mu\), \(M\ge\rho+L\mathfrak M\) and \(\check R\ge2\). For a part \(A\) of level \(j\) put
\[
 \mathrm{col}^+(A):=\{x\in A:\operatorname{dist}_\infty(x,A^c)<(n_{\rm col}\mu+2)\xi_j\}.
\]

**Lemma G (geometry of the parts; reads [SA]).** For \(i=1,\dots,4\):
- (G-a) \(A_i\) is a union of aligned \(\mu\xi_{j_i}\)-cubes;
- (G-b) \(\mathrm{col}^+(A_i)\) lies in \(\Omega_0\), in layer \(j_i\) of each sequence of the pair;
- (G-c) \(\mathcal O^p,\mathcal O^h\) are separated with cube size \(\mathfrak M\) and gap \(\rho\), and so are \(\mathcal L_X\mathcal O^p=\mathbf D_{pX}\) and \(\mathcal L_X\mathcal O^h\) (Proposition 7.1).

*Proof.*

(G-a). For W1 and W2 this holds by definition (\(\xi_k=1\)). For W3: \(C=X\cap Z_{k_\flat}\). \(Z_{k_\flat}\) is a union of level-\(k_\flat\) cells (Proposition 2.3: "every large-field region ... is a union of cells of its own level"), that is of aligned \(M\check R_{k_\flat}\xi_{k_\flat}\)-cubes. \(X\) is a union of level-\(k\) cells, aligned \(M\check R_k\)-cubes. These are unions of level-\(k_\flat\) cells because \(\check R_kL^{\mathsf N}/\check R_{k_\flat}\) is a power of \(L\) at least 1: (R19) iterated gives \(\check R_{k_\flat}\le L^{\mathsf N}\check R_k\), and all three numbers are powers of \(L\) (SA 6029). So \(\mathbb T\setminus C\) is a union of aligned level-\(k_\flat\) cells, hence of aligned \(\mu\xi_{k_\flat}\)-cubes, since \(\mu\le M\le M\check R_{k_\flat}\). For W4: \(\Lambda\) is \(Z''_k(X)\) enlarged by one layer of level-\(k\) \(M\)-cubes (SA 17598), and "the boxes are only unions of \(M\)-cubes" (Proposition 2.3). So \(\mathbb T\setminus\Lambda\) is a union of aligned \(\mu\)-cubes.

(G-b), W1, W2 and W4. Every point of these thickened collars lies in \(X\setminus\Lambda\). For W1 and W2 such a point has \(\frac14M\check R\le\operatorname{dist}(x,X^c)<\frac14M\check R+(n_{\rm col}+1)\mu+2\). For W4 it lies within \(n_{\rm col}\mu+2\) of \(\Lambda\). And \(\operatorname{dist}_\infty(\Lambda,X^c)\ge2M\check R-M\) (GEO1, from SA 17578 and 17598), which exceeds both bounds. In \(X\setminus\Lambda\) the prepared formula \(\Omega''_l\cap X=X\setminus Z''_l(X)\) (\(k_\flat<l\le k\), SA 17423-17437 with \(\boldsymbol\nu=n=\mathsf N\)) gives \(X\setminus\Lambda\subset\Omega''_k\). The healed formula \(\Omega_l\mapsto\Omega_l\cup X\) (\(l\le k\)) gives \(X\subset\Omega^h_k\). Both sequences have depth \(k\). So \(X\setminus\Lambda\) lies in layer \(k\) of \(\mathcal O^p\) and of \(\mathcal O^h\). The localisations agree with these sequences at those points, by Proposition 7.1(c). Every point of the three collars is at distance at least \(\frac14M\check R>3\mu+4\) from \(X^c\).

(G-b), W3. Let \(x\notin C\) with \(\operatorname{dist}_\infty(x,C)<(n_{\rm col}\mu+2)\xi_{k_\flat}\).
- \(x\notin\Omega''_{k_\flat+1}\): Proposition 2.3 for the prepared nest gives \(\operatorname{dist}_\infty(Z_{k_\flat},\Omega''_{k_\flat+1})\ge LM\xi_{k_\flat}>(n_{\rm col}\mu+2)\xi_{k_\flat}\). Here \(Z''_{k_\flat}=Z_{k_\flat}\), since the operation changes only levels \(k_\flat<l\le k\) ("all other entries unchanged").
- \(x\in\Omega''_{k_\flat}\): the chain \(\Omega_{k_\flat}\supset\Lambda_{k_\flat}\) of Proposition 2.3 gives \(\Omega_{k_\flat}^c\subset\Lambda_{k_\flat}^c=Z_{k_\flat}\). Hence \(X\cap\Omega_{k_\flat}^c\subset C\), and the operation leaves \(\Omega_{k_\flat}\cap X\) unchanged.
- \(x\) lies deep inside \(X\), because \(C\subset\Lambda\). The localisation \(\mathbf D_{pX}\) agrees with \(\mathcal O^p\) there (Proposition 7.1(c)).

(G-c). Proposition 2.3 gives label gaps of at least \(cM\check R_j\) between consecutive regions of \(\Omega_1\supset\Lambda_1\supset\Omega_2\supset\cdots\), and prepared gaps \(\operatorname{dist}_\infty(Z_j,\Omega_{j+1})\ge LM\) in level-\(j\) units, with \(Z_j=\Lambda_j^c\supset\Omega_j^c\). So \(\operatorname{dist}_\infty(\Omega_j^c,\Omega_{j+1})\ge\min(LM,2cM\check R_j)\,\xi_j>\rho\xi_j\). Members are unions of \(M\)-cubes or of cells, hence of aligned \(\mathfrak M\xi_j\)-cubes (\(\mathfrak M\le M\)). Theorem 6(a) asserts the same. For the localisations see Proposition 7.1. \(\square\)

**Lemma J\* (meet with one part; `a3-close.md` Lemma J, re-derived with \(\Omega'_0=\Omega_0\cap A\)).** Let \(\Omega\) be separated, with cube size \(\mathfrak M\), gap \(\rho=R_1\mathfrak M\) and \(R_1\ge L\ge3\). Let \(A\) be a part of level \(j\ge1\) satisfying (G-a) and (G-b), with \(\mu\ge\rho\) and \(n_{\rm col}=5\). Let \(\Omega'\) be the meet (1.1), and put
\[
 e_q:=\textstyle\sum_{i<q}(\rho\xi_i+\mathfrak M\xi_{i+1}),\qquad
 S:=\{x\in A:\operatorname{dist}_\infty(x,A^c)\le e_j\},\qquad
 S^+:=\{x\in A:\operatorname{dist}_\infty(x,A^c)\le e_j+3\xi_j\}.
\]
Then:
- (a) \(\{x\in A:\operatorname{dist}_\infty(x,A^c)>e_q\}\subset T^A_q\), and \(e_q\le\rho\xi_q\).
- (b) \(\Omega'\) is a separated sequence with cube size \(\mathfrak M\) and gap \(\rho\). Moreover \(\Omega'_0=\Omega_0\cap A\) and \(\Omega'_q\subset\Omega_q\) (G1); members are unions of aligned \(\mathfrak M\xi_q\)-cubes (G2); \(\operatorname{dist}_\infty((\Omega'_0)^c,\Omega'_1)>\rho\eta\) (G3).
- (c) For \(x\in\Omega'_0\setminus S\) and every \(q\): \(x\in\Omega'_q\iff x\in\Omega_q\).
- (d) Consider the rows of \(\Omega\) or of \(\Omega'\) that lie in \(\Omega'_0\). Those with an end point in \(S\) have level at most \(j\) and lie in \(\mathrm{col}(A)\). The rows of \(\Omega\) that are dropped are the level-\(j\) bonds with no end point in \(T^A_j\); the rows that are added are the rows of \(\Omega'\) of levels \(q<j\). Both kinds have both end points in \(S\). Every other row is a row of both sequences, with the same datum.
- (e) The mismatch set \(\mathcal C_A\), the union of the double blocks of the dropped and added rows, lies in \(S^+\subset\mathrm{col}(A)\).

*Proof.*

(a) Induction on \(q\). Suppose \(\operatorname{dist}(x,A^c)>e_{q+1}\), and let \(Q\ni x\) be the aligned \(\mathfrak M\xi_{q+1}\)-cube. Every \(z\in Q\) has \(\operatorname{dist}(z,A^c)>e_q+\rho\xi_q\). By the induction hypothesis every \(w\notin T^A_q\) has \(\operatorname{dist}(w,A^c)\le e_q\). Since the distance function is 1-Lipschitz, \(|z-w|_\infty>\rho\xi_q\); on the finite lattice the infimum is attained, so \(\operatorname{dist}(Q,(T^A_q)^c)>\rho\xi_q\) and \(Q\subset T^A_{q+1}\). For the bound, \(\sum_{i<q}\xi_i\le\xi_q/(L-1)\) and \(\sum_{1\le i\le q}\xi_i\le L\xi_q/(L-1)\) give \(e_q\le(\rho+L\mathfrak M)\xi_q/(L-1)\le2\rho\xi_q/(L-1)\le\rho\xi_q\).

*Key inclusion.* Let \(q>j\). Then \(\Omega_q\cap\mathrm{col}=\emptyset\), because \(\mathrm{col}\) lies in layer \(j\). So \(x\in\Omega_q\cap A\) has \(\operatorname{dist}(x,A^c)\ge n_{\rm col}\mu\xi_j\), while points of \(A^c\cup S\) are within \(e_j\le\rho\xi_j\) of \(A^c\). Hence \(\operatorname{dist}(\Omega_q\cap A,A^c\cup S)\ge(n_{\rm col}\mu-\rho)\xi_j\ge4\rho\xi_j\). If \(q\ge j+2\) the distance is also \(>\rho\xi_{q-1}\): a segment from \(x\) to such a point crosses \(\mathrm{col}\subset\Omega_{j+1}^c\subset\Omega_{q-1}^c\), and \(x\in\Omega_q\).

(b) (G1) holds by definition.

*Cubes.* For \(q\le j\), \(\Omega_q\), \(T^A_q\) and \(A\) are unions of aligned \(\mathfrak M\xi_q\)-cubes; for \(A\) this uses (G-a) and nesting. For \(q>j\) we have \(\Omega'_q=\Omega_q\cap T^A_j=\Omega_q\cap A\), by the key inclusion and (a). An \(\mathfrak M\xi_q\)-cube in \(\Omega_q\) that meets both \(A\) and \(A^c\) would meet \(\mathrm{col}\subset\Omega_q^c\). So \(\Omega_q\cap A\) is a union of such cubes.

*Gaps.* \((\Omega'_q)^c=\Omega_q^c\cup(T^A_{\min(q,j)})^c\), and the distance from a union is the minimum of the distances. First, \(\operatorname{dist}(\Omega_q^c,\Omega'_{q+1})\ge\operatorname{dist}(\Omega_q^c,\Omega_{q+1})>\rho\xi_q\). Second, for \(q<j\), \(\operatorname{dist}((T^A_q)^c,T^A_{q+1})>\rho\xi_q\) by construction. Third, for \(q\ge j\): \((T^A_j)^c\subset A^c\cup S\) by (a), and \(\Omega'_{q+1}\subset\Omega_{q+1}\cap A\). The key inclusion then gives a distance of at least \(4\rho\xi_j\) when \(q=j\), and more than \(\rho\xi_q\) when \(q>j\). (G3) is the case \(q=0\).

(c) By (a), \(x\in T^A_{\min(q,j)}\) for every \(q\), because \(e_{\min(q,j)}\le e_j\).

(d), (e) These are `a3-close.md` Lemma J (d), (e), word for word, with \(W\) read as \(\Omega'_0\). The inputs are (c); the fact that \(\Omega_q\supset\mathrm{col}\) for \(q\le j\) and \(\Omega_{j+1}\cap\mathrm{col}=\emptyset\); and, for \(q>j\), that a row with an end point in \(S\) would need its other end point in \(\Omega_q\cap A\). That point is at distance at least \(4\rho\xi_j\ge\xi_{j+1}\), or more than \(\rho\xi_{q-1}\ge\xi_q\), from \(S\). Finally \(e_j+3\xi_j\le(\rho+3)\xi_j<n_{\rm col}\mu\xi_j\). \(\square\)

**Corollary 3.1.** Each meet \(\mathbf B'_i\) is a separated sequence with cube size \(\mathfrak M\) and gap \(\rho\), with (G1)-(G3). Its mismatch set \(\mathcal C_i\) lies in \(S^+_i\), within \((\rho+3)\xi_{j_i}\) of \(A_i^c\) inside the collar. Taking for \(\Omega\) either sequence of the pair gives the same meet (Lemma C).

**Lemma 3.2 (distances).** Let \(d_{\mathbf B}\), \(d_{\mathbf B'}\) be the metrics of the given sequence and of its meet.
- (a) \(d_{\mathbf B}\le d_{\mathbf B'}\).
- (b) Every \(z\in S^+\) has \(d_{\mathbf B}(z,A^c)\le2\rho+8\).
- (c) Hence \(d_{\mathbf B}(y,\mathcal C_A)\ge d_{\mathbf B}(y,A^c)-2\rho-8\) for every \(y\).

*Proof.* (a) By (G1) the local scale of the meet is at most that of the given sequence at every point. So its path weight is at least as large, and infima preserve the inequality. (b) Pick \(a\in A^c\) with \(|z-a|_\infty\le(\rho+3)\xi_j\). The segment \([z,a]\) has Euclidean length at most \(2(\rho+3)\xi_j\). Up to its first point of \(A^c\) it runs in \(\{x\in A:\operatorname{dist}_\infty(x,A^c)\le(\rho+3)\xi_j\}\subset\mathrm{col}\), which lies in layer \(j\ge1\), where the weight is \(\xi_j^{-1}\). (c) is the triangle inequality. \(\square\)

## 4. The pairs coincide on the parts; the joined data

**Lemma C (coincidence).**
- (a) W1: \(\mathcal O^p\) and \(\mathcal L_X\mathcal O^p\) have the same members on \(X^-\), the same rows with both end points in \(X^-\), and the same data there, namely \(P\)'s.
- (b) W2: the same holds for \(\mathcal O^h\), \(\mathcal L_X\mathcal O^h\) and \(H\)'s data.
- (c) W3: \(T(B)\) and \(P_X\) are backgrounds of the one sequence \(\mathbf D_{pX}\), and their data agree on every row of \(\mathbf D_{pX}\) with both end points in \(\mathbb T\setminus C\).
- (d) W4: \(\mathcal O^p\) and \(\mathcal O^h\) have the same members on \(\mathbb T\setminus\Lambda\), and \(P\), \(H\) the same data on the rows there.
- (e) Hence, for each pair, the two meets with \(T^{A_i}\) coincide, with one joined datum ([MJ] (iii)). For \(y\in\Omega'_0\) the two original metrics give the same \(d(y,A_i^c)\).

*Proof.*

(a), (b) By Proposition 7.1(c), the localisation agrees with the given sequence (members, rows and data) off \(S_X^+\). \(S_X^+\) lies within \(3\mu+3\) of \(X^c\), and \(X^-\) is at distance at least \(\frac14M\check R\) from \(X^c\). The joined datum is \(\mathbf V\) on old rows (SA 9786).

(c) The rows of \(\mathbf D_{pX}\) with both end points in \(\mathbb T\setminus C\) are of three kinds:
- shell rows: \(\Lambda\setminus C\) consists of the shells (SA 17598). Both data are \(e^{ig_kB}V_0\) there: SA (2b), \(V''=e^{ig_kB}V_0\) on \(\mathbb B_0=\mathbf B''\cap\)shells, and the definition of \(T(B)\);
- level-\(k\) rows of \(X\setminus\Lambda\);
- collar rows of \(X\).

On the last two kinds, \(T(B)\) carries the averages of \(S\). These are \(S\)'s own data: \(S\)'s sequence \(\mathcal L_X\mathcal O^h\) has the same members there, by (d) and Proposition 7.1. \(S\)'s data there are the exterior field and its lift, and so are \(P_X\)'s (EXT; `sa-2.8-terms.md` Section 1, from SA 17598-17604; an assertion).

(d) In \(X\setminus\Lambda\) both sequences contain every member up to depth \(k\) (proof of (G-b)). Outside \(X\) both are the label of the history, because the operation changes regions only inside \(X\) (SA 17421-17437). The data outside \(\Lambda\) are the exterior field \(V_k\) and the history's, for both (SA 17598-17604; EXT).

(e) For the meets: \(T^A_q\subset A\). For the metrics: the weight of \(d_{\mathbf B}\) at a point depends only on its layer, which agrees on \(A\). A path from \(y\) to \(A^c\) may be stopped at its first point of \(A^c\); before that it runs in \(A\). \(\square\)

**Lemma D (joined data).** If \(\mathbf V\) is \(\varepsilon\)-regular, so is \(\mathbf V^J\). The interpolations \(e^{itB_0}\mathbf V^J\), \(0\le t\le1\), of Section 6 are \(C_L\varepsilon\)-regular.

*Proof.* A test of \(\mathbf V^J\) built only from old rows away from the collar is a test of \(\mathbf V\). A new row of level \(q<j\) lies inside one level-\(j\) block, or crosses exactly one face between two adjacent blocks. In the second case the level-\(j\) bond \(c\) joining their centres lies in \(\mathrm{col}^+\), in layer \(j\), so it is a row of \(\mathbf V\).

A level-\(q\) plaquette of the lift has one of three values:
- \(\mathbf 1\), inside one block;
- \(V_j(c)\mathbf 1V_j(c)^{-1}\mathbf 1=\mathbf 1\), across one face;
- \(\partial V_j(P)\), with \(P\) a level-\(j\) plaquette of the collar, at a corner of four blocks.

The last is a test of \(\mathbf V\). Mixed tests, at the tower's seams and at the old outward rows of level \(j\), use \(\mathcal M\) of the finer datum on the bonds of the finer layer. For the lift, \(\mathcal M(\mathrm{lift}_{q-1})=\mathrm{lift}_q\): inside a block every contour stays in the block, where the lift is \(\mathbf 1\); across a face every contour crosses it exactly once, and the mean returns \(V_j(c)\) (SA 7072-7080; `gates/a1-balaban-gate.md` 7.2, "the actual mean returns \(V_k(c)\) exactly"). So each mixed test reduces to one of the previous cases. The interpolation statement is the admission paragraph of `gates/a3-derivative-gate.md` Section 10: each test reads four rows and one finite average, hence is Lipschitz in the row logarithm, and \(|B_0|\le C_L\varepsilon\). \(\square\)

## 5. P81, Reg and P82° on the meets

**Order of constants.** Nothing below depends on \(k\), \(\mathsf N\), the torus, the history or \(i\).
1. \(L\) and \(\alpha_{\rm H}\).
2. The flat constants (F0). Theorem P's walk size \(M_{\rm P}\), \(c_{\rm reg}\), \(\alpha_*\), \(\theta_0=\delta_w/2\), \(\rho_0\). [A1]'s four gap lengths (`gates/a1-balaban-gate.md` D2). The walk length \(W\) of [Reg].
3. \(\mathfrak M=M_1\ge M_{\rm P}\), a power of \(L\) ("the size of the walks", SA 9596), and \(\rho=R_1\mathfrak M\), with \(R_1\ge L\) and \(\rho\ge\rho_*:=\max\{\rho_0,\ 4LW+2L,\ \rho_{\rm A1}\}\).
4. \(\mu=M_1'\ge\rho\), a power of \(L\); \(n_{\rm col}=5\).
5. \(M\ge\max\{C_c\mu,\ 16n_{\rm col}\mu,\ \rho+L\mathfrak M\}\), a power of \(L\), and the later lengths of `sa-2.8-terms.md` Section 6.
6. The coupling ceiling, under which \(C_L\varepsilon_1\le\min\{\bar\varepsilon,\ \alpha_*/(C_LM'),\ \mathsf a(L,\rho,\mu),\ r_{\rm B}/C_L\}\).

This is the order of SA 9916 (propagator constants, then \(\mathfrak M\) and \(\rho\), then radii, then \(M\)), with `gates/a1-balaban-gate.md` D2 and `a3-close.md` §1 included.

**Proposition 5.1.** For \(i=1,\dots,4\), under I5:
- (a) \(\mathbf B'_i\) is a separated sequence with cube size \(\mathfrak M\) and gap \(\rho\ge\rho_*\), above the three floors of SA 9661.
- (b) (P81) [A1] applies to \((\mathbf B'_i,\mathbf V^J_i)\). \(U^\circ_i\) is the unique regular critical orbit, with (8.2) at radius \(BC_L\varepsilon_1\), the holomorphic datum ball (9.2) and the restriction identity (9.3).
- (c) (Reg) \(U^\circ_i\in\mathrm{Reg}_\alpha\) with \(\alpha=C_LM'\varepsilon_1\le\alpha_*\).
- (d) (P82°) Theorem P (a)-(f), with the repairs D1-D3 of its gate, holds at \(U^\circ_i\), with constants depending on \(L\) and \(\alpha_{\rm H}\) only.
- (e) Each background \(U\) of the pair is the regular critical background of its own sequence. Its restriction \(U|_{\Omega'_0}\) is critical and regular, at a fixed enlarged radius, for \((\mathbf B'_i,M_{\mathbf B'_i}(U|_{\Omega'_0}))\).

*Proof.* Every clause is an instance of a theorem proved for all separated sequences. Only the hypotheses need checking.

(a) Corollary 3.1. The floors: the torus is admissible, \(\frac12\ell L^{K-i}\ge CM\check R_i\) for \(i\le k\) (SA 17583). So it has many more than \(O(\rho)\) sites of \(\mathbb T^{(k)}\) in every direction, and every gauge cube used, of side \(O(M_{\rm P}+W+\mu)\) local units enlarged by \(O(\rho)\), stays shorter than half the torus. The third floor holds for all depths on the tori of the Notation (SA 9661).

(b) [A1]'s hypotheses are a separated sequence with gap above the four lengths (step 3), F0 (gated, row 99), and an \(\varepsilon\)-regular datum with \(\varepsilon\le\bar\varepsilon\) (Lemma D, I5, step 6). The first member is arbitrary (§7.3 and §7.9, shape-free).

(c) [Reg] needs only a separated sequence with gap \(\rho\ge4LW+2L\) and the bounds (8.2) of its background. The steps of `a3-close.md` §1 read nothing else. Holes enter only through \(\Omega'^c_{j-1}\) in step (ii), and only as distance.

(d) [P°] needs a separated sequence with \(\rho\ge\rho_0\) and a real reference in \(\mathrm{Reg}_\alpha\), \(\alpha\le\alpha_*\).

(e) The given sequences are separated (G-c), and their data are \(\varepsilon_1\)-regular: I5, and Lemma D for the joined data of \(P_X\) and \(R(b)\). So [A1] applies to each of them. (9.3) needs \(\Omega'_q\subset\Omega_q\) and separatedness of the meet, which are Lemma J\*(b). Regularity at the new action boundary \(\partial\Omega'_0\cap\Omega_0\) is the gate-repaired Lemma 10.2: \(|J_W|\le C\varepsilon_1\eta^{-3}\), a fixed enlarged radius. \(\square\)

## 6. Theorem 6(c) on W1-W4

**Theorem M.** Assume Proposition 5.1. Let \(i\in\{1,2,3,4\}\) and let \(U\) be either background of the pair of W\(i\). Then \(U|_{\Omega'_0}=(e^{i\eta f}U^\circ_i)^w\), where \(w=v_q[f]^{-1}\) at the tops of \(\mathbf B'_i\) away from the collar and is unrestricted elsewhere, and at every top \(y\) of \(\mathbf B'_i\)
\[
 \xi'_y|f|,\ \xi_y'^2|\nabla f|,\ \xi_y'^3|D^{\mathsf T}Df|\ \le\ E\,e^{-\theta d_{\mathbf B}(y,A_i^c)},\qquad E:=C\,e^{\theta(2\rho+8+D_L)}C_L\varepsilon_1 .
\tag{6.1}
\]
The background \(U^\circ_i\) is the same for both members of the pair.

*Proof.* Apply `a3-derivative.md` Lemma 10.1 to \(U\), its sequence and the meet \(\mathbf B'_i\), as repaired in `gates/a3-derivative-gate.md` Section 10. Use the gate's consumer-check weight, the distance to the mismatch set. Its premises:
1. P81 and P82° for \(\mathbf B'_i\) at \(U^\circ_i\): Proposition 5.1 (b)-(d).
2. (G1)-(G3) and separatedness of \(\mathbf B'_i\): Lemma J\*(b). This is the gate's eligibility point.
3. (R1), restriction: Proposition 5.1(e).
4. (R2), collar datum: rebuilt Corollary 10.4, which needs the collar in the single layer \(j_i\), complete level-\(j_i\) blocks over the collar rows inside that layer (Lemma G (G-b), the "+2" in \(\mathrm{col}^+\)), and a gauge equal to \(\mathbf 1\) at old nodes. It gives \(\mathbf V^U=e^{iB_0}\mathbf V^J\) with \(|B_0|\le C_L\varepsilon_1\le r_{\rm B}\). \(B_0\) is supported on the added rows, because old rows carry \(\mathbf V\) in both data (Lemma J\*(d)).
5. Admission of \(\mathbf V^J\) and of \(e^{itB_0}\mathbf V^J\): Lemma D.
6. Weight: \(w(y)=e^{\theta d_{\mathbf B}(y,\mathcal C_{A_i})}\). It lies in \(\mathcal W_\theta\) for the joined metric, by Lemma 3.2(a) and the 1-Lipschitz property of distance functions. The forcing \(D\mathsf b(tB_0)B_0\) is supported within \(D_L\) of the added rows (\(\mathsf b\) is local), so \(\|D\mathsf b(tB_0)B_0\|_{Y,w}\le C_be^{\theta D_L}C_L\varepsilon_1\).

The all-weights bound (4) for \(S^{\circ-1}\) at \(U^\circ_i\) (Lemma 8.2, row sums) and the \(4/3\) Neumann bound give the first two members with \(e^{-\theta d(y,\mathcal C_{A_i})}\). The third member comes from (39) at each \(t\), before integration. Lemma 3.2(c) converts the decay to \(e^{-\theta d(y,A_i^c)}\), at the cost \(e^{\theta(2\rho+8)}\). The meets and joined data of the two members coincide (Lemma C(e)), so they have the same \(U^\circ_i\), and the two original metrics give the same \(d(y,A_i^c)\). \(\square\)

**Corollary 6.1 (I1 as 2.8 reads it).** `sa-2.8-terms.md` 5.2-5.5 hold with its \(E\) replaced by (6.1)'s \(E\), and with the following distances at the tops it sums over. Each of these tops lies away from the collar of its meet, where the tops of \(\mathbf B'_i\) are those of the given sequence (Lemma J\*(c)):
- \(R_3\), \(R_6\): \(d(y,(X^-)^c)\ge\frac12M\check R-\mu-2\), because \((X^-)^c\subset\{\operatorname{dist}(\cdot,X^c)<\frac14M\check R+\mu\}\);
- \(R_7\): \(d(y,C)\ge LMn_{\rm c}\ge Mn_{\rm c}\), crossing \(n_{\rm c}\) margin shells, each of width at least \(LM\xi_j\) in its own layer \(j\) (Proposition 2.3);
- \(R_1\): \(d(y,\Lambda)\ge M\check R\) (GEO1).

So (6.1) of `sa-2.8-terms.md` stands with a changed constant: the extra factors \(e^{\theta(\mu+2)}\) and \(e^{\theta(2\rho+8+D_L)}\) depend only on the constants of steps 1-4.

## 7. (SEP) for the outline's localisations

**Proposition 7.1.** Let \(\Omega\in\{\mathcal O^p,\mathcal O^h\}\), and let \(\mathcal L_X\Omega\) be its meet with the tower of the part \(X\) (level \(k\), second rule, \(\mu=M_1'\)). This is the outline's localisation: SA 9783 describes "the localisations, which are cube-wise meets of the tower of a region with a separated sequence"; SA 9786 describes one part on one lattice with \(\mu=M_1'\); and the cut at depth \(k\) is vacuous. Then:
- (a) \(\mathcal L_X\Omega\) is a separated sequence with cube size \(\mathfrak M\) and gap \(\rho\), above the floors.
- (b) (G1)-(G3) hold relative to \(\Omega\).
- (c) Off \(S_X^+:=\{x\in X:\operatorname{dist}_\infty(x,X^c)\le3\mu+3\}\), the sequences \(\mathcal L_X\Omega\) and \(\Omega\) coincide: members, rows and data. This is (SEP-L), and (a) is (SEP), for both localisations.

*Proof.* This is Lemma J\* with part \(X\), \(j=k\), and the second rule. Under the second rule, members are unions of aligned \(M_1'\xi_q\)-cubes, which are multiples of \(\mathfrak M\xi_q\). Tower gaps are at least \(M_1'\xi_{q+1}=LM_1'\xi_q>\rho\xi_q\). Erosion depths are \(e'_q=2M_1'\sum_{i=1}^q\xi_i\le3M_1'\xi_q\), and the key-inclusion gap is \((n_{\rm col}-3)M_1'\xi_k=2\mu>\rho\). These are the bracketed second-rule cases of `a3-close.md` Lemma J (a), (b), with the same proofs.

The hypotheses hold:
- (G-a): \(X\) is a union of level-\(k\) cells, aligned \(M\check R\)-cubes, hence of \(\mu\)-cubes.
- (G-b): points of \(X\) within \((5\mu+2)\) of \(X^c\) lie in the outer two cell layers \(X\setminus H_k^{[8]}\). These lie in \(\Omega_k\), since \(\Omega_k^c\cap X=H_k^{[8]}\) and \(X=H_k^{[10]}\) (SA 17578). For \(\mathcal O^p\) they lie in \(\Omega''_k\) because \(Z''_k\subset H_k^{[8]}\). For \(\mathcal O^h\), \(X\subset\Omega^h_k\). Both sequences have depth \(k\), so these points lie in layer \(k\).
- (G-c) for \(\Omega\) is Proposition 2.3 (Lemma G).

The floors hold as in Proposition 5.1(a). \(\square\)

So (SEP) and (SEP-L) are proved for \(\mathcal L_X\mathcal O^p=\mathbf D_{pX}\) and \(\mathcal L_X\mathcal O^h\), given Proposition 2.3 for \(\mathcal O^p\) and \(\mathcal O^h\). The towers and the four auxiliary meets are separated by Lemma J\*(b).

## 8. Verdicts, defects, what changes, open items

| Statement | Verdict (one same-model session, ungated) | Reads |
|---|---|---|
| Counterexample: P82° or P81 loses uniformity at a hole boundary of a meet | **none** (Section 2). A hole boundary is a bare boundary component, and the meets are separated. The meet background is rougher than either member near the collar, by up to \(L^{2j}\) in curvature (2.4), but only there and only in the original units. | - |
| The four meets \(\mathbf B'_1,\dots,\mathbf B'_4\) are separated sequences with (G1)-(G3), alignment, floors, mismatch sets in the collars | **proved** (Lemma G, Lemma J\*, Corollary 3.1, Proposition 5.1(a)) | [SA] |
| P81 on the meets (orbit, (8.2), (9.2), (9.3)), and for the given sequences with restriction | **implication** (Proposition 5.1 (b), (e)) | [A1], F0, I5 |
| \(U^\circ_i\in\mathrm{Reg}_\alpha\), \(\alpha=C_LM'\varepsilon_1\) | **implication** (Proposition 5.1(c)) | [Reg] |
| P82° at \(U^\circ_i\) | **implication** (Proposition 5.1(d)) | [P°] |
| Theorem 6(c) on W1-W4, in the form (6.1) with decay from \(A_i^c\), and I1 as `sa-2.8-terms.md` 5.2-5.5 read it | **implication** (Theorem M, Corollary 6.1) | [10.1] and the above |
| (SEP), (SEP-L) for \(\mathcal L_X\mathcal O^p=\mathbf D_{pX}\) and \(\mathcal L_X\mathcal O^h\) | **proved, given Proposition 2.3** (Proposition 7.1) | [SA], [J] |

**Defects, ranked by what each breaks.** None breaks a conclusion after its repair.
- **D1. Decay set of I1** (`sa-2.8-terms.md` Section 3, table W3 and W4; breaks \(R_1\) as literally stated). I1 states decay from \(W^c\). In the outline's 6(c), \(W\) is a cube-wise meet of parts inside the sequence, and a label's first member is \(\Omega_0=\Omega_1^\sim\ne\mathbb T\) (SA 17317). So W4 \(=\Omega_0\setminus\Lambda\), and \(W_4^c\) contains the label's holes. Decay measured from there gives no smallness at tops near those holes, and the global sum of 5.5 would not be small. *Repair, proved:* Theorem M measures decay from \(A_i^c\) (\(\Lambda\) for W4, \(C\) for W3), through the mismatch-set weight. Then 5.5 holds as written, with \(d_y=d(y,\Lambda)\). For W3 the literal \(W_3^c\supset X^c\) is harmless, since \(\operatorname{supp}\phi\) is far from \(X^c\), but the clean statement is decay from \(C\). Lemma 10.1's premise "\(\Omega'_0=W\)" should read \(\Omega'_0=\Omega_0\cap W\), with \(W\) allowed to leave \(\Omega_0\); its proof is unchanged.
- **D2.** `a3-close.md` Lemma J assumes \(W=\bigcap_bA_b\subset\Omega_0\). The parts of W3 and W4 are not inside \(\Omega_0\). Lemma J\*, with \(\Omega'_0=\Omega_0\cap A\), is the form needed, with the same proof.
- **D3.** \(X^-=\{d(\cdot,X^c)\ge\frac14M\check R\}\) is not a union of \(\mu\)-cubes, as a part must be (SA 9786). Use the \(\mu\)-cube version of Section 1; the distances shift by \(\mu\) (Corollary 6.1).
- **D4.** Notation: `a3-close.md`'s collar count \(n_c\ge5\) clashes with `sa-2.8-terms.md`'s margin \(n_{\rm c}=\lfloor\mathsf N/2\rfloor\). It is renamed \(n_{\rm col}\) here.
- **D5 (scope).** W1, W2 and W4 read I5 for the global label datum, at every level and in every component (2.6), not only near \(X\). Without it the global orbit can be empty (`floor-screen.md` Example 1).

**What changes for consumers (evidence for the lead; no other file was edited).**
- `sa-2.8-terms.md` Section 3, I1: the standing becomes "implication: `meet-6c.md` Theorem M", with decay from \(A_i^c\) (D1) and parts as in Section 1 here (D3).
- `sa-2.8-terms.md` Section 8, item 1 ("where 2.8 would fail") is closed as an implication, modulo the inputs below. The (G1) identification is not read (Lemma MJ), and (SEP), (SEP-L) are Proposition 7.1.
- `a3-close.md` Section 3, Consequence 3 is confirmed, with D1-D2.
- Reversal test 4.3, second bullet, does not fire. Its honest form, a failure of 6(c) on these comparisons, has no counterexample.

**Open, hardest first.**
1. The same-model inputs: `a3-close.md` Section 1 ([Reg]) and Lemma J (re-derived here as Lemma J\*). Gating them, together with this note, is the next step. The other analytic inputs are gated implications: [A1] on F0, [P°], [10.1].
2. The outline's geometry, read off its definitions and not checked against a construction: Proposition 2.3 (gaps, cube unions), the prepared and healed formulas, EXT, and the coincidence of \(P\) and \(H\) outside \(\Lambda\).
3. I5 on the global label datum: (D-F) given Proposition 2.4 (Balaban CMP 122 Proposition 1, not in hand) and H1-H4.
4. Not touched: `sa-2.8-terms.md` Section 8, items 2 and 4-6. \(\mathbf D_{pX}\) is separated (Proposition 7.1), so [A1] (9.2) applies to it. Whether that closes item 2 (the complex chart radius in Lemma TQ) is not checked here.

**What moved.** The input named as the place 2.8 would fail is now an implication from inputs already on the A3 list. No counterexample was found at hole boundaries. One statement defect (D1) was found and repaired; without the repair \(R_1\) has no bound. Nothing here is waste for the next lane: the gate of `a3-close.md` §1 and Lemma J now also carries 2.8's I1.

**Method.** No numeric job was run (2.7) and no subagent was used. The outline was fetched once into a private scratch folder. Balaban's papers were not needed in this session and were not opened. Only this file was written.
