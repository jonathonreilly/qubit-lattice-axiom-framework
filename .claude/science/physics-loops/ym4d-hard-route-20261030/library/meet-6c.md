lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T12:46Z

# meet-6c: P81, P82° and Theorem 6(c) on the meet localisations W1-W4 of 2.8, with (SEP)

Queue row 104. Pinned at a86c38fba (branch `claude/ym4d-hard-route`). Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session. Same-model research text, not gated, not an audit; grants no status. Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once by URL into a private scratch folder (SHA-256 `d7f77d4d...b4d6f`, matching `gates/a3-derivative-gate.md`). No numeric job was run (Section 2.7 says why none could help); every step is written by hand.

**Credits.** Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for every definition read here: separated sequences and their floors (SA 9593-9600, 9661), Theorem 6 (a)-(c) with the localisation as a cube-wise meet of a tower with a separated sequence (SA 9783-9789), Proposition 2.3 and the operation's nests, shells and core (SA 17398-17437, 17576-17598), the label's first member (SA 17317). T. Balaban for the architecture behind the inputs: CMP 102 Theorem 1 (the orbit), CMP 99 (389-434) (background propagators by cell gauges and flat parametrices), CMP 95, 96, 89 (the flat package). OpenAI Codex for `a1-balaban.md`, `flat-port.md`, `a3-balaban.md`, `a3-derivative.md` Sections 1-6 and the gates of rows 89 and 100. Claude for `sa-2.8-terms.md` (Lemma MJ), `a3-close.md` (Lemma J, Section 1), `a3-derivative.md` Sections 6.1-10, `p82-curved.md`.

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

(Sections 3-8 follow.)
