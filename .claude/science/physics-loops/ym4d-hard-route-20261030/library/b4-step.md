# B4: the complex small-field step (row 172)
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed; requested effort max); checkout `b1388bfbddc5c20f5ccb2e7fbb14a0560ebfcafe`; Sussman–Alpoge source `31a47c543775`. Research text, not an audit; no status granted.

## 1. Target and sources

The target is B4, SA 4006–4037, including the small-field map used at SA 22879.
SA denotes `YM4_sketch_500.tex` at the commit above, fetched once to `/tmp/sa_ym4.tex`.
Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for that formulation.
Credit Tadeusz Bałaban for the background and small-field constructions.

The step must admit complex data throughout its product box, with constants independent of depth, volume and label count.
Its finer derivatives require their own stated domains.
The real result in `one-step-closure.md` does not supply either assertion.
This note follows the first unresolved input before attempting the cluster expansion.

## 2. The first input to establish

**The first input left unproved here is the actual complex box package in SA 15745–15833, before WF8.**
It concerns WF4's constrained box background and its own current.
It must hold for every allowed outer pair, including independent currents, and throughout
\[
 |s_\Delta|<e^{\bar\kappa},\qquad 0\le t\le1,
 \qquad |\nu|<c_\nu/s_k.                                      \tag{1}
\]
The package includes common datum/core room and compatible boundary comparison with the prescribed node factors.
Individual holomorphic background charts do not state that package.

The relevant source limits are these. Library paths are relative to this folder; checks are in `../gates/`.

| Input | What can be read at this revision |
|---|---|
| A1–A3 | `a1-balaban.md` Section 9 supplies datum charts. `a3-profile.md` supplies the real profile. `a3-derivative.md` supplies complex datum response, but its Section 10 collar proof starts with real data. Their checks, `a3-balaban-reads-gate.md` and `a3-close-meet-gate.md` retain these scopes and repairs. `a3-clauses.md` and its check extend the specified inverse/pair system, without matching WF4's entire family. |
| A2 | `a2-full.md` and its check give a corrected conditional half-gap, retaining the formation premise H-ct. That premise is not a proof of formation. |
| WF room and response | `wf-room-2.md` and `o1-decoupled.md`, with their checks, supply conditional room, (O1), and inner admission with explicit endpoint inequalities. `pw-bridge.md`, `nl-r9.md` and `pw-bridge-gate.md` supply conditional [PW] and [NL] for the adopted maps. That check leaves complex box localisation and the Landau comparison open. |
| Box first and Rule W | `wf7-bf.md`, checked in `cond-c.md` Section 1, avoids the removed-map comparison. Section 3 still assumes T4 on the whole datum paths and the WF3–WF6 domains. Rule W supplies geometry, not those analytic premises. Its new proofs are not yet checked by the other model at this pin. |
| Reference chart and B1 | `ref-chart.md` Theorem 2.4 and Section 8, with `ref-chart-regate.md`, give a conditional reference chart, without matching every WF4 datum. SA 1191–1310 proves the abstract tree majorant; B1 still requires the actual complex activities. |

Thus the old removed-map comparison is not used as a reason to reject the box-first route.
The stopping point is supplying that route's own complex box input.

## 3. Where the continuation argument stops

Here is the precise missing step in the direct continuation of the checked collar proof.
Let \(V^U\) be the restricted datum and \(V^J\) the joined datum, after the prescribed node gauges.
On every instance of (1), one must place them in a common admitted background chart:
\[
 V^U=e^{ib_U}V_*,\quad V^J=e^{ib_J}V_*,\quad
 \|b_U\|_\infty,\|b_J\|_\infty<r_B/2,
 \quad \operatorname{supp}(b_U-b_J)\subset\mathcal C,
 \quad \|b_U-b_J\|_\infty\le C a.                       \tag{2}
\]
Here \(V_*\) is a real regular reference datum, \(\mathcal C\) the actual collar, and \(a\) its regularity radius.
The constants, chart margin and gauge bounds must be independent of depth and volume.
The resulting Landau pair must also satisfy the inner-admission inequalities of `o1-decoupled.md` Theorem I.
Equation (2) is a sufficient input for this continuation route, not a claimed necessary condition for every possible proof of B4.

**What (2) would give, by hand.** Put \(b_u=b_J+u(b_U-b_J)\), \(0\le u\le1\).
Convexity keeps this segment in the datum ball.
For the normalized field, gradient and current coordinates \(Z_y\) in that same Landau chart, T4 gives
\[
 Z_y(b_U)-Z_y(b_J)=\int_0^1 DZ_y(b_u)[b_U-b_J]\,du.
\]
Choose the weight \(w(y)=e^{\theta d(y,W^c)}\), below the allowed response rate.
Memberwise containment gives \(d\le d'\), so this is also an allowed weight for the joined sequence.
If every collar row has \(d(c,W^c)\le c_1\mu\), the weighted response bound yields
\[
 |Z_y(b_U)-Z_y(b_J)|
 \le C a e^{\theta c_1\mu}e^{-\theta d(y,W^c)}.          \tag{3}
\]
The operator bound already includes the row sum. There is no factor counting rows or levels.
This proves the comparison implication; it does not establish (2) for WF4.

**First failed application.** Section 10 of `a3-derivative.md` obtains its collar datum from real fields.
Its Lemma 10.3 uses unitary transports; its check explicitly retains that restriction.
For complex transports, write the surface product as \(\prod_{r=1}^N T_rP_r^{\pm1}T_r^{-1}\).
If \(\|P_r-I\|\le a<1/2\) and \(\|T_r\|\|T_r^{-1}\|\le K\), telescoping gives
\[
 \left\|\prod_{r=1}^N T_rP_r^{\pm1}T_r^{-1}-I\right\|
 \le(1+2Ka)^N-1\le e^{2NKa}-1.                         \tag{4}
\]
Indeed \(\|P_r^{-1}-I\|\le a/(1-a)\le2a\), and each conjugated factor differs from identity by at most \(2Ka\).
Thus the real proof's estimate needs control of the actual complex transports and node gauges.
Separate chart existence, or complex bounds for a specified inverse, does not perform this matching.
I have not established (2), with those gauges and the core margins, for the full family (1).
The attempt stops at this input. No complex Wilson counterexample is claimed.

## 4. Literature and scope at the stop

Bałaban CMP **109**, pp. 273–279, separates local analyticity of (3.25) from the core inclusion (3.36).
I read those excerpts and checked pp. 275–278 against the scan.
His construction retains the box background's current and transports the current and fluctuation with the gauge.
The paper's own complex spaces cannot be identified with (1) by citation.
No additional Balaban theorem is assumed here; (3)–(4) are the written conditional estimates used in this attempt.

In particular, SA 7569 requires, for each radius component,
\[
 (1+\beta_s)^{-1}\le
 \frac{\alpha_{i,k+1}}{\alpha_{i,j}}
 \le(1+\beta_s)\sqrt{k+2-j},\qquad
 CM\alpha_0<\alpha_1,\quad \alpha_1^2\le C\alpha_0.       \tag{5}
\]
These size comparisons do not verify the nonlinear datum and core inclusions in (2).
I have not rebuilt Balaban's inclusion on this full running family.
CMP **116** is absent from the permitted paper folder and was not read.
The QED3 and YM3 manuscripts are also absent from the permitted local sources.
No missing source is counted as evidence.

## Result

**B4 and the holomorphic one-step theorem 1.6 remain unproved in this attempt.**
The first unproved input is the actual complex WF4 box package, specifically the common collar-chart and core admission in Section 3.
The proof stops before the actual B1 majorant and before the finer potential, zone and mixed derivatives.
Equations (3)–(4) are hand arguments with explicit premises, not a closure of that input.
No refutation of B4, new independent check or scientific status is claimed.
