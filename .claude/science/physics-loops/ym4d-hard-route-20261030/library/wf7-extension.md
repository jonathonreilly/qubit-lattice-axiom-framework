# WF7: testing the old-projection-first window extension (row 145)
Provenance: OpenAI Codex, GPT-6 family (exact deployment identifier and runtime effort not exposed; requested effort: max); checkout `93bad75ee32e50d58bd4703280d43cc648ee7693`; Sussman–Alpoge source commit `31a47c543775`. Research text, not an audit; no status is granted.

## 1. Scope, sources, and the two different continuations

This note concerns rank 4's removed-window estimate (SA 15850–15866). Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, for the window, its nonlinear averages, pair domains, response systems, and formation estimates. SA line numbers refer to `YM4_sketch_500.tex` at the pinned commit, fetched once to `/tmp/sa_ym4.tex`. Credit Tadeusz Balaban for composing background maps and restricting a critical background at its own averages (CMP **109**, 249–301, and **119**, 243–285). The local notes and their readers retain their authorship: `old-depth.md`, `removed-fix.md`, and `wf-room.md` are Codex's; `old-depth-gate.md`, `wf-room-2.md`, and `o1-decoupled.md` are Claude's. Codex's gates of the last two notes qualify their premises.

The requested queue rows are 113, 116, 125, 126, 129, 131, 136, 137, 141, and 145. In particular row 136 is pending at this source revision: the repaired removed-map theorems are conditional inputs, not independently established facts. Row 144's separate check of Proposition V is also pending. Neither a gate label nor this note upgrades an input. All proof steps below are written mathematics; searches, extraction, and file editing are bookkeeping only. The workflow and no-go-discipline sources were read from this commit's Git objects; they are absent from the sparse working tree. The user's one-file, no-commit, no-audit instructions govern this research note.

Write \(\sigma=\sigma_j=L^{j-k}\). Let \(q\) be the assigned step pair, \(V\) its underlying shifted configuration, \(p=\Pi_j(V)\) the pair consisting of the global old constrained critical projection and its actual current, and \(p_R\) the actual old box pair (WF4). The symbol \(\Pi_j\) includes the nonlinear determining datum and an explicitly chosen representative. A difference of pairs is taken only in a common admitted chart. There are two distinct proposals:

* retain \(q\), and use the exact decomposition \(q-p_R=(q-p)+(p-p_R)\);
* replace the interpolating action by its evaluation on \(p\), using critical-endpoint identities to recover the physical action difference, and then localize this new interpolation.

The second proposal need not agree with the first away from the physical locus. Conversely, an endpoint identity alone does not prove the fine-parameter restriction or locality of the new interpolation. These distinctions are retained throughout.

## 2. Counterexample first, and the decision between the two proposals

At the flat pair, put \(\mathscr L=D^{\mathsf T}D\), let \(K\) be the raw straightened determining derivative, and choose the real constrained lift \(h=Hb\), \(Kh=b\), \(\mathscr Lh=K^{\mathsf T}\lambda=f\). At a single active parameter with the one-cube version of Definition D, \(H(z)=zH\). R9 has quadratic remainder at zero, so its first field coefficient is \(zh\). Current-I then gives
\[
 \dot j_z=K^{\mathsf T}H(z)^{\mathsf T}\mathscr L(zh)=z^2f,
 \qquad \dot J(e^{i\eta A_z})=zf.                 \tag{2.1}
\]
These are bilinear transposes; complex conjugation does not change the degree. At the flat base, derivatives of the anchor and of the local chart conversion that multiply the zero field/current contribute zero. An assigned gauge has the same property: differentiating \(gJg^{-1}\) adds a commutator with the base current, which is zero.

The exact Cartan family in `old-depth.md` Sections 4–5 has \(\|b\|_\infty\le8\), a next-step average equal to one, and \(|f(b_*)|=1\) at every mesh. Its first-rule old box has only a distant collar correction at the tested bond. Thus its direct replacement by WF4 has mixed coefficient
\[
 \partial_\epsilon\partial_\nu(q-p_R)_J(b_*)
   =(z^2-z)\sigma_1^3 f(b_*)
        +O(\sigma_1^{-3}e^{-a/\sigma_1}).            \tag{2.2}
\]
Here the named inputs are exactly that note's **Flat lift, D, R9-local, Current-I, old T4, and Domain room**. At \(z=1/2\) the coefficient is at least \(\sigma_1^3/8\) for sufficiently old windows. Indeed \(e^x\ge x^8/8!\) makes the error \(O(\sigma_1^5)\). An alleged \(C\sigma_1e^{-cM/\sigma_1}\) bound would imply \(\sigma_1^2e^{cM/\sigma_1}\le8C\), contradicted by \(e^x\ge x^3/6\). This preserves the scope of the prior result; it does not identify the unspecified old box reduced readout with the actual current.

Claude's Proposition V in `old-depth-gate.md` moves this test to a many-cube grid using the flat walk-support and energy-decay inputs. Its conclusion has \(1/16\) instead of \(1/8\). It remains a separately supplied conditional result here: no completion of its row-144 check is claimed. The new example in Section 5 below uses an ordinary large torus and no one-cube parameter partition.

For proposal (b), the exact revised estimate is
\[
 \|\Delta_\nu(q-p_R)\|_{j,X}
 \le \|\Delta_\nu E_j\|_{j,X}
       +C|\nu|\delta_k\sigma_j e^{-cM/\sigma_j},
 \qquad E_j=q-\Pi_j(V).                              \tag{2.3}
\]
Its second term requires the old-to-old collar hypotheses, proved conditionally in Section 4 below. The first term is retained, including any change of assigned representative. Cauchy's inequality on an actual member core, with room \(c\alpha_j\), gives the additional window majorant
\[
 C{g_j\over\alpha_j}
       \sum_{z\text{ in window}}\|\partial_\nu E_{j,z}(0)\|.
                                                               \tag{2.4}
\]
Replacing \(g_j\) by \(d_j\) gives the vacuum-only version. Neither the identity (2.3) nor Cauchy's inequality supplies a spatial tail for this new term.

The source search for `WF7` finds its definition at SA 15861 and exactly two explicit references: SA 16102 and 16270. Searching `WF11`, `WF12`, the removed exponential, and `removed field` also locates the following uses. This table separates a failed inference from a counterexample to an entire formation theorem.

| Reader | What it needs | Effect of (2.3) |
|---|---|---|
| SA 15947–15959, identification of the two removed substitutions | Exponential comparison for the fixed assigned maps, on their own discs | A bulk term is an extra origin; it cannot be renamed a boundary difference. |
| SA 16100–16114, WF11 | One member Cauchy factor, then up to \(C_M\sigma_j^{-4}\) old bases | Adds (2.4). A per-base bound \(C\delta_k\sigma_j^3\), even if proved, gives only \(Cs_kg_j\rho_j\sigma_j^{-1}\) by this argument. |
| SA 16115–16132, WF12 | Absorb \(\rho_j\sigma_j^{-3}e^{-cM/\sigma_j}\) into the regular or vacuum-only age weight | The replacement inequalities \(\rho\sigma^{-1}\le C\rho^3\sigma^{\alpha_H}\) and \(\rho\sigma^{-1}\le C\rho^2\) both fail under the actual ordinary age bound; see the quotient calculation below. |
| SA 16260–16280, rate allocation citing WF7–WF12 | A long-domain exponential and a retained spatial rate | The old long-domain tail remains valid; (2.3) gives no corresponding tree or distance factor for its new bulk origin. |
| SA 16299–16343, WF14–WF15 and first source derivatives | The summable regular age weight \((1+a)^{3/2}L^{-\alpha_Ha}\), and the vacuum-only weight | The extra \(\rho\sigma^{-1}\) majorant cannot be inserted with these weights. Differentiating origins does not supply the missing estimate. |
| SA 16826–16856, OA7 and the following wall restriction | The assigned exponential response factors and exact restriction on active components | Smallness of a bulk defect proves neither property. |

For that consumer calculation set \(a=k-j\), \(\sigma=L^{-a}\), and retain WF1's actual bound \(1\le\rho\le C_0\sqrt{1+a}\). The ratios of the proposed bulk majorant to the regular and vacuum-only weights are respectively at least
\[
 {\rho\sigma^{-1}\over\rho^3\sigma^{\alpha_H}}
 \ge {L^{(1+\alpha_H)a}\over C_0^2(1+a)},\qquad
 {\rho\sigma^{-1}\over\rho^2}
 \ge {L^a\over C_0\sqrt{1+a}}.
\]
Both are unbounded: apply \(e^x\ge x^3/6\) with \(x=a\log L\). This tests the consumer on its stated age regime, without prescribing an unrelated radius ratio.

The lower coefficient (2.2) does **not** by itself prove a lower bound on a summed gauge-invariant activity. For example its first derivative at the flat pair can vanish, and a current-square member has an extra current factor. It would be incorrect to turn the worst-case Cauchy majorant in (2.4) into an actual lower bound without constructing such an activity and its substituted pair. What is decided is narrower and sufficient for choosing the next attack: **(b) with (7.11) alone does not pass the outline's existing consumers.** A new cancellation or stronger bulk estimate would be a different proof. I therefore pursue (a); no impossibility result for an improved version of (b) is claimed.

## 3. What composition and restriction prove, with the gauges retained

The primary passages read in the supplied paper folder were CMP 109 pp. 255–256, 260–263, 273–280, especially (3.18)–(3.28), (3.38), and (3.48)–(3.53); and CMP 119 pp. 256–261, 275–276, 279–280, especially (2.14)–(2.15) and (3.48)–(3.49). The OCR is used to locate the argument, not as a theorem import. Balaban first composes with an old background, removes collar data through the old response, and transports both the current and fluctuation datum when changing gauge. CMP 109 p. 276 explicitly leaves a **final localization** of these analytic functions to a later construction. CMP 119 p. 276 likewise performs localization after the Section 3–5 operations. Neither passage identifies small nonlocal tails with exact locality. The layered domains retain old determining rows as well as new collar rows.

Here is the part used below, re-proved as an implication from **BG** (the regular real critical orbit's existence and uniqueness, and the specified holomorphic branch), **AV** (the actual local nonlinear average), and **AX** (the fixed residual axial recursion). These names mean the corresponding inputs of `old-depth.md` Section 2 and `wf-room-2.md` Section 1, with their stated qualifications.

**Restriction lemma.** Let \(S'\subset S\) memberwise be separated, aligned determining sequences, including level-zero boundary rows. If \(W\) is a regular critical background for \(S\), then its restriction is critical at its **own** \(S'\)-averages. Its canonical representative equals that restriction after the prescribed residual transformation. This identity extends on a connected common holomorphic critical-datum chart.

*Proof.* A constraint-preserving variation for \(S'\) fixes the level-zero collar. Extend it by zero outside its first member. Induct upwards through the actual iterated averages. A smaller exterior coarse bond is either a prescribed determining row, or its two aligned blocks miss the smaller member, so its finer inputs are unchanged. Consequently all original determining rows are unchanged; a row of \(S\) has no endpoint in \(\Omega_{q+1}\supset\Omega'_{q+1}\). Crossing plaquettes see only fixed collar bonds. The first variation of the smaller inner-plaquette action therefore equals the larger first variation and vanishes. BG identifies the regular critical orbit. AX fixes its representative by finite contour recursions with node values fixed. Both sides, including this recursion, are holomorphic on the admitted datum chart. Their difference vanishes on its real open ball; all real derivatives there vanish, hence all complex Taylor coefficients vanish. Overlapping balls continue the identity. This continuation varies the critical datum; it does not free variables that were fixed in the real identity. At an interior bond the incident plaquettes are the same, so differentiating their products gives the same adjoint identity for the actual current. \(\square\)

If \(W(v)\) is such a branch, differentiation retains the full chain
\[
 D\Phi_{S'}\,DM_{S'}\,\rho DW
                  =D((\rho W)^g),
 \qquad
 \dot W^g_b=a_-W^g_b+g_-\dot W_bg_+^{-1}-W^g_ba_+,
 \quad a=\dot g g^{-1}.                              \tag{3.1}
\]
For the current the extra term is \([a_-,J(W^g)_b]\). In this convention \((W^u)^v=W^{vu}\), so the raw-to-lower-tower factor is \(g_Zu^{-1}\widetilde v^{-1}\). These formulas follow by the product rule and \(\partial g^{-1}=-g^{-1}(\partial g)g^{-1}\); no factors commute.

Let \(V(t)=e^{i\eta_k t\mathbf H_k}U_+\) join two physical critical endpoints whose sequences contain the old truncation. On an admitted projected path, the lemma and gauge invariance give
\[
 G(P_1)-G(P_0)=\int_0^1 {d\over dt}G(\Pi_j(V(t)))\,dt. \tag{3.2}
\]
The chain rule is linear in the direction of \(V\). Inserting \(\sum_\square\zeta_\square=1\) gives the WF3 direction \((t+\nu\zeta_\square)\mathbf H_k\), with the **nonlinear** average still inside \(\Pi_j\). This proves the physical endpoint identity and its window decomposition before final localization. It does not assert equality with Current-I at independent parameters. In particular \(\Pi_j\) reads the independent current only through the specified \(\mathbf H_k(P;s,B')\); this is a permissible holomorphic dependence wherever the composition exists.

For a first-rule box tower \(T\) contained in the old truncation, put \(W=\Pi_j(V)_U\). In raw constraint coordinates, \(M_TW-M_TV\) vanishes on every common old determining row; only the new collar rows can differ. Applying the restriction lemma to \(W\) gives the comparison through one old box map. For a layered region the statement is first about the **meet** with the old sequence. Its identification with a prescribed pure WF4 tower is a separate geometric requirement; it is automatic in a constant top layer containing the enlarged window, and is not automatic at a seam. The current-depth sequence may never be substituted for the old one in this argument.

## 4. The weighted collar bounds and the assigned-node calculation

This section sharpens the conditional positive result. It does not assume the fine-bracket restriction which Section 5 tests. All constants below are independent of depth when the named response/counting inputs are uniform.

Use **T4, AX, AV, MS** as stated in `wf-room-2.md` Section 1, with its gate's radius repairs. Write \(d\) for the old box metric. Each native cell meets at most \(N_L\) determining-row carriers. The MS count implies, for sufficiently small fixed \(\gamma>0\) below the response rate and above its counting threshold,
\[
 S_\gamma:=\sup_x\sum_c e^{-\gamma d(x,c)}<\infty.       \tag{4.1}
\]
Indeed the shell \(n\le d<n+1\) has at most \(C_L(n+2)^q e^{bn}\) rows for a fixed integer \(q\) and \(b<\gamma\). The ratio of successive summands tends to \(e^{b-\gamma}<1\), so their sum is finite. Equivalently choose a positive surplus and absorb the fixed polynomial by the exponential series. Counts are in the **old map's native cells**, including its finer collar layers. An exterior count from the current-depth map is not used.

Let \(F_R\) be a single old box pair map in the specified common output chart. Include its Landau response and node factors in the following hypothesis, on the entire \(r\)-neighbourhood of the datum segments:
\[
 \|DF_R(u)e_c\|_x\le K e^{-2\gamma d(x,c)}.             \tag{4.2}
\]
The neighbourhood clause is the W1 repair in `old-depth-gate.md`. Suppose the actual raw data \(v(\nu)=M_TV(\nu)\), \(w(\nu)=M_TW(\nu)\) lie in that chart, and \(\beta=w-v\) and \(\partial_\nu\beta\) are supported on the fixed new collar \(C\). Define the **weighted** quantities
\[
 B_x=\sup_\nu\sum_{c\in C}e^{-\gamma d(x,c)}|\beta_c|,
 \quad b_x=\sup_\nu\sum_{c\in C}e^{-\gamma d(x,c)}|\partial_\nu\beta_c|,
 \quad a=\sup_\nu\max(\|v'\|_\infty,\|w'\|_\infty).
                                                               \tag{4.3}
\]
The following proves (7.10) in its justified weighted form whenever the two actual maps have the common chart just stated.

**Datum lemma.** Suppose the step field derivative has current-unit first-order supremum at most \(C\delta_k\) on its declared fine-parameter and multiplier discs. Suppose all old scales are at most \(\sigma_j\), both background branches are admitted on the common datum neighbourhood, and \(\|v\|_\infty,\|w\|_\infty\le C_0r\) there. Then
\[
 a\le C\delta_k\sigma_j,\qquad
 b_x\le C\delta_k\sigma_j,
 \qquad B_x\le Cr.                                  \tag{4.4}
\]

*Proof.* The local derivative of the actual average on a row of scale \(\xi_c\) is at most \(C\xi_c\) times the physical potential derivative on its carrier (AV, or the gated Lemma A′). Thus \(|v'_c|\le C\delta_k\sigma_j\). Apply the old T4 response to the global old datum. For a cell \(Q\), its scale-normalized field derivative is at most
\(C\sum_c e^{-\theta d_S(Q,c)}|v'_{S,c}|\le C\delta_k\sigma_j\),
using the native count for \(S^{\le j}\). The same bound holds on the carriers of the smaller rows, with adjacent-scale constants retained. AV applied to \(W\) now gives \(|w'_c|\le C\delta_k\sigma_j\). This proves the estimate for \(a\). Since \(|\beta'_c|\le|v'_c|+|w'_c|\), (4.1) gives the bound for \(b_x\). Finally \(|\beta_c|\le2C_0r\), and (4.1) gives the bound for \(B_x\). No unweighted cardinality of the collar has been declared uniformly bounded. \(\square\)

The assumed common chart includes the real-reference/datum transport; it is not supplied by the supremum estimate alone. The first-system bound in this lemma is the named **PW** input (the first-order R9 bound left in `o1-decoupled.md` Section 5), not a consequence of (O1). For the actual WF discs, zero-field room, the repaired running radii and PW/AV give the displacement \(C|\nu|\delta_k\sigma_j/\alpha_j\). Choosing \(c_\nu\) below the fixed room gives \(|\nu|<c_\nu/s_k\). At young ages one must retain the actual core chart; the global half-datum-ball estimate is not asserted there. This keeps the two endpoint radii and the separate inner/removed discs of `removed-fix.md` Section 6.

**Collar estimate.** Under (4.2)–(4.4), with \(D=d(x,C)\),
\[
 \|\Delta_\nu(F_R(w)-F_R(v))\|_x
       \le C K|\nu|\delta_k\sigma_j e^{-\gamma D}.    \tag{4.5}
\]
*Proof.* Write the difference as \(\int_0^1DF_R(v+t\beta)\beta\,dt\). Its derivative in \(\nu\) contains \(DF_R\beta'\) and
\(D^2F_R[(1-t)v'+tw',\beta]\). Cauchy's formula in a direction of supremum norm one, on the stated \(r\)-neighbourhood, bounds the latter kernel by \((K/r)e^{-2\gamma d(x,c)}\) for its collar leg \(e_c\). For \(c\in C\),
\(e^{-2\gamma d(x,c)}\le e^{-\gamma D}e^{-\gamma d(x,c)}\).
Summing the collar leg gives \(K e^{-\gamma D}(b_x+aB_x/r)\). Integrate from zero to \(\nu\) along its straight segment and apply (4.4). This proof works for complex \(\nu\) and independent fine parameters, provided the same admitted neighbourhood is available throughout. \(\square\)

**What the node hypothesis in (4.2) means.** For a common old map, T4 bounds its node derivative and its Landau field/gradient derivative. AX extends the node derivative down a pillar. If a contour factor at level \(q\) has length \(O_L(\xi_q)\), its relative first variation is bounded by \(C_L(\xi_q/\xi_n)\|\dot a\|\) in the containing pillar of scale \(\xi_n\). The sum of these length ratios is at most \(C_L/(1-L^{-1})\). For ordered products \(g=T_1\cdots T_N\),
\[
 \dot g=\sum_{r=1}^N T_1\cdots T_{r-1}\dot T_rT_{r+1}\cdots T_N.
                                                               \tag{4.6}
\]
The products have bounded condition numbers by the same geometric sum. A pillar has bounded old metric diameter; moving its anchor changes an exponential by a fixed factor. Thus the all-site node derivative has the same exponential as T4, up to a fixed constant. Cauchy's formula gives its mixed derivative on a smaller common ball. Integrating (4.6) for the collar data gives (4.5) for the **relative node change**, too. For the current, differentiate \(gJg^{-1}\); the extra term is the commutator in (3.1), bounded by the node derivative times the existing current bound. These calculations prove the assigned-node estimate when both sides have first been identified with **this same** \(F_R\). Two unrelated bounded Landau gauges do not meet that premise merely because both condition numbers are bounded.

The collar geometry is also elementary. For the first rule,
\[
 e_j=\sum_{q<j}(\rho\xi_q+\mathfrak M\xi_{q+1}),
 \qquad {e_j\over\xi_j}\le{\rho+L\mathfrak M\over L-1}.
                                                               \tag{4.7}
\]
After the fixed sharp-read-set loss \(b_*\xi_j\), a member at physical depth \(d_0M\xi_k\) has
\(D\ge d_0M/\sigma_j-e_j/\xi_j-b_*\).
For a pure tower, use the constant-top hypothesis; otherwise take the actual old meet and retain the identification requirement. Choose \(M\) after the fixed collar/read-set sizes. Equations (4.5)–(4.7) give
\[
 \|\Delta_\nu(p-p_R)\|_{j,X}
       \le C_R|\nu|\delta_k\sigma_j e^{-cM/\sigma_j}. \tag{4.8}
\]
This is an old-to-old estimate with its datum, chart, representative, and PW premises visible. It establishes the quantitative collar implication and the weighted (7.10) mechanism. It is **not** yet a filing of a global composite as the local functions in WF13a–WF13b. That issue has an additional exact requirement, tested next.

## 5. A hand counterexample to leaving the old projection undecoupled

The extension tested here is precise: keep Definition D and R9 for the step response, replace the interpolating pair by
\[
 \Pi_j\!\left(e^{i\eta_k(t+\nu\zeta)\mathbf H_k(s;P,B')}\mathbf U\right),
                                                               \tag{5.1}
\]
and put **no fine parameters into the global old projection**. Here the assigned background is explicitly the direct R8/R9 choice \(U_+(P)=\mathbf U\): the shifted potential is formed over the bare configuration of the input pair (SA 5747–5759). Thus (5.1) is one precise realization of (7.14), with \(s\) entering only through the step response. WF3's phrase “configuration in the assigned background evaluation” does not uniquely impose this choice on every alternative extension. The counterexample tests this choice; it does not concern a new expansion that also localizes the old projection or replaces its baseline first.

In particular a rule that replaces the baseline outside \(R_z\) by fixed data is a different map and evades the two-completion test below. It must then restore the physical endpoint identity through its own removed origins. A rule that projects a local box but retains the original field outside that box still feeds the remote data to the global old projection. Neither convention may be silently substituted for (5.1). This distinction is necessary when using the example against the **actual** window filing.

### 5.1 Exact old linear response on a periodic Cartan slice

Fix odd \(L\ge5\), old depth \(j=1\), and a finite torus with an even number \(n\) of old blocks in direction 1. Take \(n\) large and divisible by the required lattice periods; all floors and room for the fine-parameter grid can be met. Other directions can have the same length. At the flat background consider fields with only direction-2 potential, in the colour \(T=\operatorname{diag}(1,-1)\), independent of coordinates 2, 3, 4. Label the fine sites in direction 1 by \(i\) modulo \(nL\), and old blocks by \(B_m=\{mL,\ldots,mL+L-1\}\). A translation gives the centred convention used for odd \(L\).

On this slice the old average is the arithmetic block average of the potential, up to its fixed row-length factor. Indeed all link factors commute; the defining mean equation is solved by the mean angle, and the site contours cancel in pairs under reversal of the direction-2 displacement. Write the normalized old datum as
\(u_m=L^{-1}\sum_{i\in B_m}a_i\).
The flat old constrained response minimizes the quadratic Wilson action
\(\tfrac12\sum_i(a_{i+1}-a_i)^2\) at these means. Its equations are
\[
 2a_i-a_{i-1}-a_{i+1}=\lambda_m\quad(i\in B_m),
 \qquad L^{-1}\sum_{i\in B_m}a_i=u_m.                 \tag{5.2}
\]
The omitted positive action and unit factors do not affect any zero or nonzero assertion below.

These are also the full four-dimensional flat saddle equations on this datum, not just restricted Euler equations. The row multiplier has only direction 2 and is independent of that coordinate, so it annihilates the site-gradient part of the averaging derivative. The action force is the same direction-2 discrete Laplacian. All other components vanish, and the field is divergence free. Thus it is in the Landau slice and satisfies every saddle equation. The **Flat lift/BG** input identifies it with the derivative of the old nonlinear background. Alternatively, uniqueness of this scalar part follows because a difference with zero block means has zero quadratic energy only if it is constant, hence zero.

For completeness solve (5.2) by hand. Put
\(y_m=a_{mL-1}\) and \(s_m=a_{mL}-a_{mL-1}\).
Inside block \(m\),
\[
 a_{mL+r}=y_m+(r+1)s_m-\tfrac12\lambda_m r(r+1),
 \quad s_{m+1}=s_m-L\lambda_m,\quad 0\le r<L.
                                                               \tag{5.3}
\]
Summing these finite arithmetic progressions gives
\[
 u_m=y_m+{L+1\over2}s_m-{L^2-1\over6}\lambda_m,
 \quad y_{m+1}=y_m+Ls_m-{L(L-1)\over2}\lambda_m.
\]
Eliminate \(y,\lambda\), and set
\[
 A={L^2-1\over6L}>0,\qquad B=L-2A,
 \qquad B-2A={L^2+2\over3L}>0.
\]
One obtains
\[
 u_{m+1}-u_m=A s_m+B s_{m+1}+A s_{m+2}.              \tag{5.4}
\]
There is a unique \(r\in(0,1)\) with \(A(r+r^{-1})=B\): the left side decreases continuously from infinity to \(2A<B\). Define, for \(0\le m<n\), periodically,
\[
 g_m={(-1)^m(r^m+r^{n-m})\over
              A(r^{-1}-r)(1-r^n)}.                   \tag{5.5}
\]
Direct substitution gives
\(Bg_m+A(g_{m-1}+g_{m+1})=0\) for \(m\ne0\).
At zero the numerator of the left side before the denominator is
\[
 B(1+r^n)-2A(r+r^{n-1})
       =A(r^{-1}-r)(1-r^n),
\]
so that left side is one. The cyclic operator is invertible: for a real vector \(v\), its quadratic form is at least \((B-2A)\sum v_m^2>0\), using \(2|v_mv_{m+1}|\le v_m^2+v_{m+1}^2\). The same inverse exists over the complex numbers.

Take \(u_m=\mathbf1_{m=0}\). Equation (5.4) then has
\[
 s_{m+1}=g_{m+1}-g_m,
 \qquad
 \lambda_m={2g_m-g_{m-1}-g_{m+1}\over L}
           ={g_m\over A}\ne0\quad(m\ne0).           \tag{5.6}
\]
The last equality uses \(2A+B=L\). The slopes sum to zero, so (5.3) gives a periodic potential. Equation (5.4) fixes successive differences of its block means; its additive constant fixes the remaining common mean. This verifies all constraints, including the constant mode.

Thus a datum supported on one old block produces a nonzero old actual-current response on **every** other old block. The effect decays exponentially and is never exactly zero. This is an explicit finite formula, not a numerical Green-function observation.

### 5.2 Two ambient completions of the same local pair

Choose a current window \(R_z\) disjoint from the direction-1 slab of block 0, and put a real Cartan potential \(a_i=1\) on that block and zero on the other blocks. Its exact nonlinear old normalized datum at small amplitude \(\epsilon\) is \(u_m=\epsilon\mathbf1_{m=0}\). Let \(\mathbf U_\epsilon\) be this fine field, with independent input current zero and real reference factor one. It agrees with \(\mathbf U_0=1\) on every bond of \(R_z\). At each fixed finite mesh, choose \(\epsilon\) small enough for all simple and hereditary clauses and all logarithm branches: the family is finite, the inequalities are strict at one, and the supplied background branches are holomorphic there. No mesh-independent lower bound on this amplitude is needed to test an exact identity.

The local WF4 pair at the datum on \(R_z\) is identically \((1,0)\) for both completions. The global \(\Pi_1(\mathbf U_\epsilon)\), however, has the nonzero derivative (5.6) at a direction-2 bond based at \(z\). Hence the bare map \(\Pi_1\) cannot be evaluated as a function of a pair defined only on \(R_z\). This already refutes replacing the local map in WF13a by the global map without further localization. Since (a) could instead keep WF13a and put the difference into a removed origin, the next test checks that origin's anchored derivative as well.

### 5.3 The obstruction survives the anchor and an actual R9 direction

Take a slab of current parameter cubes containing block 0, outside a large neighbourhood of \(R_z\). Put their parameters equal to zero and every other parameter equal to one. Let \(Y\) be the surviving cubes. The grid has room for at least three cubes in every direction and may be arbitrarily large. The two input pairs \(P_\epsilon,P_0\) agree on \(Y\); the perturbation lies strictly inside the deleted slab.

By Definition D, every surviving step walk reads its pair only on \(Y\); walks reaching the deleted cubes have zero monomial. R9 splitting and the zero-datum anchor therefore give the **same** step response for \(P_\epsilon\) and \(P_0\), zero on the removed slab. This uses the corrected fixed-region field-locality in `o1-decoupled.md` Theorem B and its gate, not the disputed comparison of two different sequences.

Write \(h_s=\partial_a\mathbf H_k(s;P_0,B'(a))|_{a=0}\), with \(b=\partial_aB'(a)|_0\). R9-local gives \(h_s=H_1(s)b\), since its remaining terms are quadratic at the flat base. The flat walk estimate used below applies to this **actual** tangent. To check this identification at the level of its specified expansion, use Claude's `h-walk.md` Section 7: every branch coefficient is \(j_\beta=H_\beta^{\mathsf T}\mathbf J\). At \(\mathbf J=0\) each is zero, hence every inserted vertex \(V_\beta\), which is linear in \(j_\beta\), is zero. The zero-branch local systems have \(j^{(0)}=0\) and are the original W systems. Thus the nonzero coefficients of \(H_1(s)\) have the flat W bounds. Retain their full declared read hulls; any extra enlargement is fixed in current units. This argument needs no identity \(H_1(s)=H(s)\) between two decoupled specifications with possibly different hull conventions. At all parameters one, both equal the flat constrained lift.

There is an admitted fluctuation direction for which
\[
 \left[D(J\circ\Pi_1)(1)[\zeta h_s]\right]_2(z)
                         \ne0.                       \tag{5.7}
\]
Here is a quantitative existence proof, retaining all its inputs. Use the exact flat-based family of `old-depth.md` Section 4, whose tangent satisfies \(h_1=H_1(1)b=h\), \(\|b\|_\infty\le8\), and \((\mathscr Lh)_2=-T\) on a current block containing \(R_z\)'s tested old site. Its nonlinear datum is an actual next-fibre fluctuation; using its free-coordinate curve gives this same tangent. The restriction lemma yields
\(D(J\circ\Pi_1)(1)h=\mathscr Lh\).
Choose the grouped cutoff with \(\zeta=1\) around the test, and support in \(R_z\), as in WF13a. For the tail \((1-\zeta)h\), AV bounds every old raw datum component by \(C\sigma_1\). T4 and the native old cell count give, in old current units,
\[
 \left|D(J\circ\Pi_1)(1)[(1-\zeta)h](z)\right|
          \le C\sigma_1 e^{-cM/\sigma_1}.             \tag{5.8}
\]
Fix the geometric constants and \(M\), then take \(k\) large enough that this is smaller than \(\sigma_1^3/4\). The exponential-series argument in Section 2 proves that such an integer exists.

Now move the deleted parameter slab a distance \(D\) from \(R_z\). The difference \(h_s-h\) consists of walks whose enlarged hull reaches that slab. The flat **W** absolute walk bound, at parameters zero or one, implies
\[
 \sup_{R_z}|h_s-h|\le C_k e^{-\vartheta D},           \tag{5.9}
\]
with \(C_k<\infty\) independent of the torus size; dependence on this fixed mesh is allowed. To check this use explicitly, reserve one part of each walk exponent for its distance from \(R_z\) to the slab, losing only the fixed hull enlargement. Reserve a second part for the distance to its input row. Sum those input rows in current units, where their polynomial shell count is uniform. Sum the remaining transition factor \(\sum_n(\nu_1C_W/M_1)^n\le2\). Finally convert local physical \(L^2\) energy to a value at a **fixed** fine bond: its mass term gives \(|A_b|\le C\eta_k^{-2}\|A\|_E\). This costs a finite factor in \(C_k\), and proves (5.9) without a mesh-uniform pointwise upgrade. This is why the counterexample does not consume the unresolved general PW theorem.

Apply AV and T4 to \(\zeta(h_s-h)\); their old native row sum is finite uniformly in volume. Its contribution to the left side of (5.7) is at most \(C'_k e^{-\vartheta D}\). Choose a finite integer number of parameter cubes making this smaller than \(\sigma_1^3/4\), then choose a torus large enough for this slab and all periods. Equations (5.8)–(5.9) show that the direction-2 component in (5.7), in old units and along \(T\), has magnitude at least \(\sigma_1^3/2\). The flat operators preserve colour, so there is no uncontrolled perpendicular colour component. Nearby forward/backward direction-2 tests can be placed in the same constant-current part of the current block; the same bounds apply to them. This proves (5.7) by inequalities and the exact flat family.

Use the vacuum-only pointed member
\[
 G_z(P)={\mathfrak d_j e^{-\kappa d_j(X)}\over C_J\alpha_j^2}
            \sum_{b\in\mathcal S_z}\tfrac12\operatorname{tr}J(b)^2,
                                                               \tag{5.10}
\]
where \(\mathfrak d_j>0\) is the member norm allowance, \(\mathcal S_z\) is the set of the forward and backward fine bonds in all four directions at the old site \(z\), and \(X\) is a fixed old cube containing their stencils. Use based currents at their initial sites; a reversed bond can equivalently be transported to its initial site before taking the trace. The finite constant \(C_J\) bounds this sum on the current ball \(|J|<\alpha_j\). The member is holomorphic, gauge invariant, invariant under the hypercubic stabilizer of \(z\), vacuum normalized, and has no fixed colour spectator. It meets the vacuum-only structural hypotheses at SA 13859–13880 and 16056–16067. Its pointed translates give a Euclidean family as well. Its spatial weight is a fixed nonzero constant for this fixed \(X\).

Let the fluctuation coordinate curve have amplitude \(a\), tangent \(b\), and set \(t=0\). Define
\[
 \Psi_\epsilon(a,\nu;s)=
 G_z\!\left(\Pi_1(e^{i\eta_k\nu\zeta\mathbf H_k(s;P_\epsilon,B'(a))}
                                         \mathbf U_\epsilon)\right).
                                                               \tag{5.11}
\]
Let \(A_b\) be the old actual-current derivative in \(\epsilon\) from (5.6), including the fixed unit factors, and let \(C_b\) be the old current response in (5.7). At the flat base the projected current is zero. The product rule therefore gives exactly
\[
 \partial_\epsilon\partial_a\partial_\nu\Psi_\epsilon(0,0;s)|_{\epsilon=0}
 = {2\mathfrak d_j e^{-\kappa d_j(X)}\over C_J\alpha_j^2}
             \sum_{b\in\mathcal S_z}\tfrac12\operatorname{tr}(A_bC_b)
 \ne0.                                                       \tag{5.12}
\]
Only the two direction-2 terms of \(A_b\) are nonzero; their coefficients are the same nonzero block value (5.6), with the matching orientation signs in both factors. The corresponding \(C_b\)'s have the same sign along \(T\), by the \(\sigma_1^3/2\) bound. Thus their products cannot cancel. Terms involving a second derivative of the projected current multiply its zero base value and vanish. All assigned transports give the same coefficient: the member is gauge invariant, and a first derivative of conjugation at zero current adds zero.

Subtracting \(\Psi_\epsilon(a,0;s)\) does not change (5.12). At general \(t\), the coefficient of \(\epsilon a\) in \(\partial_\nu|_0\Psi\) is still the same: \(t\) appears in the other first-order fluctuation direction but not in the \(a\nu\) direction, and the zero base current eliminates the additional terms. Its integral over \(0\le t\le1\) is therefore nonzero as well. Finite-dimensional holomorphy turns this unequal Taylor coefficient into unequal values for sufficiently small nonzero inputs. A common small nonzero fluctuation radius on the full fine-parameter polydisc follows from R9-local and the supplied convergent walk data exactly as in `old-depth.md` Section 5.3; no uniform lower bound on that radius is needed here.

Consequently the anchored projected window function, even after its \(t\)-integral, depends on \(P\) in the deleted slab although the step response and \(P|_Y\) are unchanged. The actual WF4 inner window is unchanged: its datum and background read only \(R_z\subset Y\). The projected-minus-inner removed origin inherits (5.12).

This contradicts the **exact** hereditary restriction needed at SA 16194–16209, 16216–16238 and OA7–OA8: setting parameters outside \(Y\) to zero must give the same function of the pair on \(Y\). The undecoupled old map still reads the remote data. Increasing a collar only makes its nonzero response smaller; (5.5) shows that no fixed finite collar makes it vanish. An exponential error is compatible with (4.8), but is incompatible with this exact identity.

**Scope of the counterexample.** It refutes (5.1), with its explicitly declared direct background, as a complete fine-parameter extension with the step's existing decoupling alone. It does not refute the physical endpoint formula (3.2), the collar estimate (4.8), or a construction that also localizes the old projection and assigns its connecting read sets to new origins. It also does not assert that a global projection is part of WF13a as originally printed: WF13a deliberately uses the local box map. The failure occurs when the proposed global projection is inserted upstream and its remaining removed origin is claimed to inherit the original fine-bracket restriction without another construction.

## 6. A finite algebraic repair, and the estimate it still owes

There is a concrete counter-route to any claim that projection-first is impossible. On a **fixed finite lattice**, it can be made local by an additional interpolation. The following algebra proves this much; it does not establish a uniform formation bound.

Let \(B=B_z\) be connected and contain the full fixed inner box and all its prescribed read collars. For each set \(A\supset B\) of current cubes, let \(f_A(P;s)\) be the projected window evaluation obtained by doing the old problem on the component of \(A\) containing \(B\), with its actual boundary rows, and using the step response restricted to that component. Include the \(\nu\) anchor and, if desired, its derivative and \(t\)-integral. For this construction take as explicit premises that all these finite problems exist on a common small chart, that disconnected extra components are ignored, and that their local formulas are consistent under adding such components. These are definition choices for new maps, not properties assigned retroactively to (5.1). Provided each assigned determining problem meets BG's separation and boundary hypotheses, BG and R9-local near the flat field give a common small neighbourhood on a fixed finite lattice by taking the minimum of the finitely many radii. This observation neither verifies those geometric hypotheses for arbitrary cut-downs nor gives a uniform lower bound on the radii.

With \(Q=\mathcal P\setminus B\), introduce extra flags \(\theta\) and define
\[
 \mathcal F(\theta,s;P)=
 \sum_{C\subset Q}
   \left(\prod_{\Delta\in C}\theta_\Delta\right)
   \left(\prod_{\Delta\in Q\setminus C}(1-\theta_\Delta)\right)
                      f_{B\cup C}(P;s).               \tag{6.1}
\]
It is holomorphic on the common chart and polynomial in \(\theta\). At \(\theta=1\) it equals \(f_\Lambda\). If \(\theta=0\) off \(Y\supset B\), terms using a cube off \(Y\) vanish; hence it reads only the pair on \(Y\). If an active component misses \(B\), the function \(f_{B\cup C}\) is independent of its choices there. Summing those choices gives a factor \(\prod_\Delta(\theta_\Delta+1-\theta_\Delta)=1\). Thus a derivative belonging to that disconnected component is zero. Set \(\theta=s\); restriction of the step response gives the same conclusions for one set of fine parameters. Finite fundamental theorem of calculus then gives the bracket sum and its physical completeness. Joint holomorphy commutes with the \(\nu\) derivative and the finite \(t\)-integral. These are exact finite identities.

The uniform estimate is a different statement. A bound \(\sup_A|f_A|\le H\) gives on \(|s_\Delta|\le R\) only
\[
 |\mathcal F(s,s;P)|\le H(1+2R)^{\#Q}.              \tag{6.2}
\]
This follows by taking absolute values in (6.1) and multiplying \(|s|+|1-s|\le1+2R\) over all flags. It is unusable uniformly in volume. The same loss multiplies a uniform single-collar bound for \(f_A-f_B\). Small nonzero tails at individual deleted cubes, as in (5.5), cannot be set to zero to avoid this issue.

One possible completion is a connected expansion of the old projection (or of these domain differences), with the **old** response distance paying for each added current cube, uniformly on the joint fine-parameter discs, including node transport. Its coefficients must have enough tree decay to sum the absolute values in a norm suitable for WF13, while retaining the \(\delta_k\sigma_j e^{-cM/\sigma_j}\) amplitude for the removed origins. Its physical value must be the old projection in (3.2), and its inner term must remain the common local map WF13a. The current-depth walk expansion by itself does not prove this new statement: Section 5 is a counterexample to precisely that inference. Formula (6.1) proves the finite locality/identity part and isolates the missing **uniform analytic bound**; it is not proposed as a completed uniform construction.

## 7. Scope checks and recovery checkpoint

The checks below apply the repository's no-go-discipline questions at the pinned revision. They are research scope checks, with no packet PASS, landing, runner, or audit claim. The user forbids those actions and all other file writes.

* **N1, alternatives.** Three actual approach families were examined: assigned-pair comparison with an explicit bulk term (Section 2); old projection and a common old box response (Sections 3–5); and an additional domain interpolation/connected localization of the composed action (Section 6). The first does not pass the printed consumer inequalities with its present estimate; the literal undecoupled version of the second fails exact fine restriction; the third remains live. These are not five exhausted routes. No procedural completeness or universal negative follows.
* **N2, dependencies.** Let L denote a quantitatively controlled joint localization of the old projection, and C the common-chart/collar comparison. Neither implication L ⇒ C nor C ⇒ L is established in general. Section 5 does prove that a collar estimate does not imply exact restriction for the literal composite. No claim that these form a minimal set of independent obstructions is made. The existing PW and background premises remain attached to each positive implication.
* **N3, hidden premises.** BG/Flat lift identify nonlinear derivatives with constrained saddle solutions; AV supplies the actual averaging carriers; T4/AX supply the old response and representative; W/D and R9-local supply the flat masked response and its local dependence; MS supplies native counts; the datum neighbourhood and common-map identification in Section 4 are explicit. Finite-dimensional continuity supplies radii only at each fixed lattice. None is silently promoted to a uniform theorem.
* **N4, residual match.** `old-depth.md` Sections 4–6 and its gate concern Current-I versus WF4's actual pair; they support (2.1)–(2.2), not the new locality obstruction. `removed-fix.md` Section 7 concerns same-depth agreement and the old/current distance distinction; it supports the geometric comparison, not global fine restriction. The present (5.2)–(5.12) concern only the undecoupled old composite (5.1). Proposition V is credited and left at its stated conditional standing, not used as a proof of (5.12).
* **N5, resolutions.** Equation (5.6) proves a nonzero current response on each non-source block, and hence at a fine bond within it. Equation (5.12) tests one actual pointed, gauge-invariant window derivative and its \(t\)-integral. No lower bound for the full sum of all output origins or for a physical fibre integral is claimed. No per-mode or universal-program impossibility is claimed.
* **N6, partial closure.** The weighted (7.10) calculation and common-map node comparison in Section 4 are valid implications. Section 6 repairs exact finite locality by changing the extension; it requires no new physical axiom. Its uniform bound is open.
* **N7, strongest counterargument.** Balaban explicitly localizes the composed functions after his Section 3 transformations, and SA allows different off-physical extensions. One should therefore put parameters into the old projection's connected expansion as well, with a collar around the fixed inner base, and use old-scale propagation to pay the additional cubes. That construction could retain WF4 and produce WF7 on the full discs. The terminal obligation is a uniform, jointly holomorphic, rooted expansion of the projected removed origin with the old exponential and assigned-node control. The present counterexample does not rule it out; (6.1) already supplies a finite algebraic version. Accordingly the result is a partial narrowing, not a no-go for route (a).
* **N8, prior echoes.** The prescribed local notes already separate critical restriction from independent-parameter continuation. `gates/h-walk-fix-gate.md` Sections 3–5 similarly distinguishes term locality from a consumer's full rooted-domain filing. Enlarging read sets repairs missing finite reads there; here (5.5) shows that a fixed enlargement alone cannot remove the global old projection's tail. Adding its own connecting read sets is the remaining analogue of that repair.

Recovery state: source checkout `93bad75ee32e50d58bd4703280d43cc648ee7693`, SA `31a47c543775`; all cited local sources are at that checkout. The decisive new calculation is (5.3)–(5.6), checked within the text by direct substitution into the positive cyclic operator, and then inserted into the anchored derivative (5.12). This is a second hand calculation, not an independent review. No calculation was machine-assisted. Next decision: construct the additional joint localization suggested by (6.1), or prove stronger structured bulk estimates for (2.3); do not retry the direct assigned-pair identity, change an exponent by a unit conversion, or infer exact restriction from a boundary estimate.

## Result

**WF7 is not closed by this note.** What is proved, as implications from the named inputs, is:

1. From **BG, AV, AX**, admitted critical-datum charts and aligned nested sequences: critical restriction with its actual current and ordered node transport, and the physical projected endpoint/window identity (3.2).
2. From **T4, AX, AV, MS**, the explicit common datum neighbourhood and common old-map identification, and **PW** for the step derivative: the weighted (7.10) bounds (4.4), the assigned-node collar comparison, and the old-depth exponential (4.8). No unweighted collar count or mixed native norm is used.
3. From **Flat lift/BG**, the actual flat average, **W/D, R9-local**, old **T4**, fixed-lattice domain room, and the direct-background assignment declared in Section 5: the projection-first extension (5.1), with parameters only in the step response, fails the exact restriction required by the fine brackets. The failure occurs for the gauge-invariant vacuum-only member (5.10) and survives both the \(\nu\) anchor and the \(t\)-integral. It is compatible with an exponentially small collar error.
4. Exact algebra gives (2.3). The explicit consumer inequality in Section 2 fails, so this defect estimate alone cannot be carried through WF11–WF15/OA7 by the printed norm argument. This is not a refutation of every possible improved bulk estimate. Finite algebra gives (6.1)'s additional localization and completeness, conditional on the stated finite local maps; its volume-uniform complex bound remains unproved.

**Where rank 4 stops:** after the named first-system bounds, a projection-first completion still needs a joint old-projection/step-response localization with a uniform rooted fine-bracket bound, the declared local pair domains, and the actual node conventions. In layered applications it must also identify the old meet with the prescribed box problem where that is used. Improving the collar estimate alone cannot supply the missing exact restriction. The literal extension (5.1) must change; route (a) with the additional localization of Section 6 remains open. No rank-4 completion, independent check of the whole dependency chain, retained status, or Yang–Mills existence result is asserted.
