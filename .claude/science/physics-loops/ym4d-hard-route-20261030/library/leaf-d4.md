## Repo search

The lead searched main and PRs #10114, #10133, #10134 and #10141.
Its record is [prior/repo-search-2026-11-08.md](prior/repo-search-2026-11-08.md), especially section 13.
There is no `prior/leaf-d4.md` at this pin.
This note reuses that search; it does not claim a new exhaustive search.

The closest result is [loc-4.md](loc-4.md), sections 4–7.
It proves one-move admission and Theorem W conditional on D4.
Its section 5 leaves the full carried compositions open.
[src-array.md](src-array.md), 222–226, retains exactly that input.
[gates/ho-collar-check.md](../gates/ho-collar-check.md), finding 1, specifies the missing radius \(2/a_R\).
These results are prior work and are not re-derived here.
The complete requested r2-heal, loc-4 and lfi-ho notes and both requested checks were read.

Main was fetched at `43a1fcc374711ca50626eca667441d3ca575c7d1`, the lead's final search revision.
PR #10141 was fetched at `c73ad7b177d94f89ff37b77386936e3d52b48b05`.
Its `research/ym4d/library/in1.md`, 66–74 and 205–216, retains the genealogy convention and healing hypotheses.
Its `library/st1-r4.md`, 1703–1707, retains the separate coordinate, transport, constraint and pivot match.
These are snapshot copies, not independent admission proofs.
That snapshot has no `library/loc-4.md`.
PR #10114 was fetched at `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
Its soft-route `SOFTHARD.md`, 584–598, requires a representation on the actual joint support.
It does not provide this hard-route complex core inclusion.

The registry assigns D4-CARRIED to DOM; FINISH row 544 assigns this first reader.
The older D4-BUDGET, D4-TRANSITION and D4-REAL-RECORD rows retain their separate targets.
Their general budget, eventual drop-out transition and real record extension are not reopened here.
The requested first pinned outer reader is not recorded as closed.

# D4-PINNED-CORE: first old outer reader

Codex, 2026-11-08. Checkout `a85478ecbecfed1121fd6921af7e5040fd9bf7c4`.
Research text, not an audit. Grants no status.
All calculations below are written mathematics. No numerical run is used.
The branch reference moved during this session.
A final comparison found the GOAL, library and gate inputs unchanged from the requested pin.
Only this note was written by this lane.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Credit Tadeusz Bałaban for the background, preparation and kept-form method.
Source line numbers use these fixed files:

- **SA:** `YM4_sketch_500.tex`, commit `31a47c543775`.
- **Y:** `YM4_1400.tex`, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
- **I:** `theorem_0_complete_account_raw_I.tex`, commit `31a47c543775`.

The requested `/tmp` copies already existed and were reused.
The SA index, neighbouring rows and obligations were consulted before the source excerpts.
SA 5663–5760 defines the pair core and its shifts.
SA 5813–5825 assumes enlarged-disc inclusion.
SA 17558–17564 sketches the actual kept-form carriage.
Y 73373–73559 supplies the pinned-profile route examined below.

## 1. Kill test, before the proof attempt

**Outcome.** A potential-only budget fails. A main-level-only tower budget also fails.
Neither test refutes the actual pinned map, which claims both current and tower control.
The tests therefore require a full certificate; they do not end this lane with a Yang–Mills counterexample.

### 1.1 Opposite potentials, equal-sign current increments

Fix an old kept Gaussian reader, with its original independent-current ceiling \(r_J>0\).
Suppress its fixed stored coordinate \(a'\), mask and pivot data.
Its quadratic contribution has the form

\[
 F_R(P;a')=-\tfrac12\langle a',K_R(\mathbf U,\mathbf J)a'\rangle.
 \tag{1}
\]

Its original domain requires \(\|\mathbf J\|<r_J\), irrespective of the reader's value at a given \(a'\).
The carried elimination factor has to keep its own domain too.
This is the construction of SA 17558–17564, not a newly chosen Gaussian.

Here is the test of a proposed domain argument.
On one current component choose \(T\) with \(\|T\|=1\), and put
\[
 \mathbf J_0=\tfrac34r_JT,\qquad
 h_1=(\varepsilon T,\tfrac18r_JT),\qquad
 h_2=(-\varepsilon T,\tfrac18r_JT).
 \tag{2}
\]
Take \(\varepsilon>0\) small enough for the potential logarithms in this test.
The two link multipliers commute and cancel:
\[
 e^{-i\eta\varepsilon T}e^{i\eta\varepsilon T}=1.
\]
But the independent currents add, by SA (R8), 5748–5760:
\[
 \mathbf J_1=\tfrac78r_JT,\qquad \mathbf J_2=r_JT.
 \tag{3}
\]
Each separate increment at the initial current fits the current clause.
Their composition reaches its excluded boundary.
Its potential displacement is zero; its current displacement is \(r_JT/4\).
Replacing that current by the current of the final link would change the prescribed complex pair.
Thus a zero potential budget cannot admit (1) after these two carries.
This is a clause test, not a claim that (2) is produced by an actual history.

### 1.2 One subordinate level and the amplified disc

Take the old core at level \(j\ge2\), with radius \(a_0\).
For \(p=n=j-1\), SA (R6), 5696–5720, requires
\[
 \frac{\|\partial U_{j-1}-1\|}{\eta_{j-1}^{\,2}}<a_0/L,
 \qquad \|J_{j-1}(U_{j-1})\|<a_0/L.
 \tag{4}
\]
The second current is in level-\(j-1\) units.
It is not the independent main-level current.
Both erosion assignments and all allowed subdomains remain quantified.

Put \(Q=4L^8\), \(u_R=1\), and
\[
 a_R=C_*\ell_t^{-(q-p_1-r/2)}Q^{-1},\qquad \rho_R=2/a_R.
 \tag{5}
\]
Suppose one only bounded a tower-current displacement, already in its own units, by
\[
 |\lambda|a_R a_0/2.
\]
At \(\lambda=(2/a_R)(1-\epsilon)\) this permits \((1-\epsilon)a_0\).
It exceeds the tower ceiling in (4) whenever \(0<\epsilon<1-1/L\).
An actual bound must divide by \(a_0/L\), and by the remaining fraction of that radius.
The potential, curvature and current unit changes must precede this comparison.
SA (R7), 5738–5746, gives the potential and current factors \(L^{-1}\) and \(L^{-3}\).
It does not identify the nonlinear tower current with a rescaled independent current.

There is a second loss if the age factor is omitted.
Writing \(a_{\rm base}=C_*\ell_t^{-(q-p_1-r/2)}\), the required disc has radius \(2Q/a_{\rm base}\).
A normalized bound \(|\lambda|a_{\rm base}/2\) then permits \(Q(1-\epsilon)\), not a number below one.
Y 73508–73556 explicitly claims to pay both losses.
The proof attempt must check that claim on the complete old read.

## 2. The reader, its birth core, and the source's proposed map

Fix a retained strip Gaussian at its first subsequent outer preparation.
Choose one of its original kept-chain carriers \(R\).
Let \(\sigma_b\) be its recorded formation structure and \(j\) its fluctuation level.
Keep its original free rows, stored coordinate \(a'\), chain mask and elimination factor \(z^{(j)}\).
The Gaussian's argument level and its fluctuation level are not silently identified.
SA 17558–17564 fixes the functions once; only their evaluations subsequently change.

Its pair domain is the original formation section on its complete read, with its stored-variable domain.
It is not the current output core on \(X^\sim\).
SA 6117–6173 specifies the birth section as \(\widetilde U^c_{\sigma_b}\), with its assigned radii and stored-field extensions.
In particular it retains:

- Every simple clause (R4), including the independent current.
- Every old determining set and (R5) continuation, for both erosion rules and all truncations.
- The tower curvature and recomputed-current clauses (R6), in their own units.
- The predecessor structures, their (R22) coefficients, radius lifts and old real-gauge clauses.
- The actual logarithms, inverse matrices, node maps and stored transports used to define this reader.
- Its original far-field discs and scalar switches. Near variables remain real Borel parameters.

For the last two items, the definedness of a formula is part of its domain.
An already specialized contour parameter is not restored as a new free parameter.
This is also the convention of [d4-chart.md](d4-chart.md), 72–102.
Lifting a filed carrier does not replace any of these domains.
Y 68773–68838 and 68988–69036 explicitly retain the original formation reads.

Here is the pinned construction of Sussman and Alpoge, Y 73387–73555.
Use \(\mathbf V_\star=(\mathbf1,V_X^{\rm in})\) on the component's determining rows.
Let \(U_\star\) be its adapted real critical background and \(q(\xi)=(U_\star,J(U_\star))\).
The stored rows are fixed. The exterior rows of this reference are identity rows.
The new datum \(\mathbf V\) uses the following four row types:

| Row type | Entry in \(\mathbf V\) |
|---|---|
| Tower row at level \(m\) | \(e^{i\gamma}\mathcal M^m(\mathbf U)\), with both combs and node factors |
| Other exterior row | \(\mathcal M^t(\mathbf U)\) |
| Box row | The formed box average with its left multiplier \(e^{ig_tB}\) |
| Inner stored row | \(V_X^{\rm in}\) |

The exterior comb gauge \(\hat w\) is identity at the core nodes.
In the fixed reference chart put
\[
 B^\natural=\frac1i\Log(\mathbf V^{\hat w}\mathbf V_\star^{-1}),\qquad
 (H_\star,j_\star)=
 \bigl(\mathcal H_\star(B^\natural),
 J(e^{i\eta\mathcal H_\star(B^\natural)}U_\star)-J(U_\star)\bigr).
 \tag{6}
\]
The source's proposed pair substitution is
\[
 \widehat S_R(\lambda)=
 \mathfrak p[U_\star]|_R\dotplus
          (\lambda H_\star,\lambda j_\star)^\delta|_R.
 \tag{7}
\]
The superscript denotes levelling at the original stored pins.
Both increments are multiplied *before* levelling.
The hat here distinguishes this displayed pair map from its full evaluation through the old reader's defining calls.
It does not propose a different substitution.

At zero, (7) is \(q(\xi)|_R\) and does not depend on the output pair.
Y 73546–73555 identifies its full real endpoint with the prepared datum and the original pinned stored values.
It then identifies the factor value by the tie.
Neither that endpoint identity nor the notation in (7) independently admits the defining calls at complex parameters.

The source obtains the profile
\[
 s_\star(x)=C\left[
 \delta'_t e^{-\theta_\flat D_{h_t}(x)}
 +a_C\sum_{m=h_t}^{t-1}L^{m-t}e^{-\theta_\flat D_m(x)}
 +\epsilon_{\rm out}e^{-\theta_\flat D_t(x)}\right],
 \tag{8}
\]
where \(a_C=\max_\iota\alpha_{\iota,t}\).
Y 73482–73506 bounds this by \(C\delta'_t e^{-\theta_\flat\varrho_0(h_t-1-l(x))_+}\) on the retained carriers.
Y 73508–73556 then compares it with the target radii and claims cost \(|\lambda|a_R/2\).
This is the existing profile estimate; it is not re-derived here.
The geometric, response and radius constants precede the coupling ceiling.

Y 73501–73510 says that the anchor has half of every target radius.
It uses criticality over its own averages to identify subordinate anchor towers.
This is the assertion to apply to the *old* determining rows and defining calls.
Replacing them by the new component rows would assume the required inclusion.

The exterior-strip result at Y 63569–63677 is a useful but different application.
Its carriers lie outside the enlargement of the region being healed.
It assumes the served target's lower-clause gap \(\mathsf{gp}(m')\).
Here the retained inner carriers lie inside \(Z''_{h_t+2}\), by Y 73373–73386.
The exterior theorem therefore does not already prove this leaf.

## 3. The precise remaining lemma

The attempt stops at the old continuation-entry estimate in the proposed profile proof.
Call it **D4-OLD-TOWER-ENTRY**, for this first outer reader only.
This is a substatement of D4-CARRIED, owner DOM, not a new registry row.

Unfold the actual reader just far enough to reach one of its original (R5) calls.
Let \(e=(Z,p,n,\text{erosion rule})\) name that call in its birth structure.
Already one subordinate level is included: \(p=n=j_R-1\), when the argument level \(j_R\ge2\).
Retain its determining rows \(\mathbf B'_e\), real factor \(U_e\), branch and assigned continuation domain \(\mathcal B_e\).
The real factor is fixed throughout the complex parameters.
Let \(W_e(\lambda;\mathfrak z,s,\zeta,\xi)\) be the link argument actually delivered to that call.
It includes every retained earlier substitution and its prescribed transport.
Here \(\zeta\) collects exactly the earlier parameters and spectators still present in that formula.
The next raw datum is
\[
 b_e(\lambda)=\frac1i\Log\left[
 M_{\mathbf B'_e}(W_e(\lambda))
 M_{\mathbf B'_e}(U_e)^{-1}\right].
 \tag{9}
\]
This is (R5), not the component datum \(B^\natural\) in (6).

**Lemma required.** At every such call of this first reader, the actual anchor lies in \(\mathcal B_e\).
Supply \(\sigma_e>0\) such that
\[
 b_e(0)+\{v:\|v\|<\sigma_e\}\subset\mathcal B_e.
 \tag{10}
\]
The margin must be uniform in the permitted inputs in the following quantitative sense:
on continuation up to first exit,
\[
 \sup_{\mathfrak z,s,\zeta,\xi}
 \frac{\|b_e(\lambda)-b_e(0)\|}{\sigma_e}
 \le \frac{|\lambda|a_R}{4},\qquad |\lambda|<2/a_R.
 \tag{11}
\]
The supremum uses the entire prescribed cube polydisc and spectator range.
If the chosen margin depends on the fixed real fibre, the quotient is taken on that same fibre.
The fixed constant \(C_*\) in \(a_R\) must cover all these fibres and old calls.
The raw means, their node maps and the old logarithm must be defined during this continuation.

The factor \(1/4\) reserves half the datum margin at the edge of the requested disc.
It is the requested \(|\lambda|a_R/2\) cost measured against the safe allowance \(\sigma_e/2\).
Changing this fixed fraction only changes \(C_*\); it must not change \(Q^{-u_R}\).
This lemma addresses old continuation entry only. It supplies no final current, Gram or Gaussian bound.
Those other clauses would still need their certificate after this one is supplied.

The source's first-exit proof is already available at Y 13520–13573.
It applies once the actual clause margins and continuation bounds are supplied.
It does not provide (10)–(11).
In particular, a bound on the last pair alone cannot be entered as a bound for (9).

## 4. Three routes to D4-OLD-TOWER-ENTRY

### Route 1: apply the weighted profile in the original chart

This is the direct route proposed in hstep-tree section 8.
The useful tower theorem already exists in Y 36699–37176.
It must be ported, not replaced by a new tower argument.
It fixes the determining sequence, requires its memberwise containment in the ambient sequence, and retains the complete row reads.
For a fixed real factor \(U_e\), its input norm is
\[
 n_e(w)=\max_b\max\{l_e(x_b)|w(b)|,
                   l_e(x_b)^2|\nabla_{U_e}w(b)|\}.
 \tag{12}
\]
Y 36859–36896 gives existence on \(n_e(w)<a\), with a fixed \(a>0\).
Y 37070–37176 treats the settled full stencils, both allowed erosions, and multiplicative shifts.
This supplies nonlinear tower control. It is stronger than a bound on the independent current alone.

To apply it here, write the actual argument of (9) in its original frame:
\[
 W_e(\lambda;b)=v_e(\lambda;b_-)\widehat W_e(\lambda;b)
                         v_e(\lambda;b_+)^{-1},\qquad
 w_e(\lambda)=(i\eta_e)^{-1}\Log(W_e(\lambda)U_e^{-1}).
 \tag{13}
\]
The symbols in (13) denote the literal carried argument and assigned transport, not freely chosen gauges.
For an uncomposed native call they reduce to the restriction and pinning in (7).
If earlier substitutions remain in the formula, they remain in \(\widehat W_e\) and \(v_e\).
One must not insert substitutions that were already eliminated by an exact filing identity.

The fixed-chart estimates in d4-chart, 104–184, already bound (13) from complete link and transport bounds.
They explicitly need the covariant difference of \(v_e\), not only its condition number.
Their averaging estimate has the form
\[
 \|b_e(w)\|\le C_{A,e}\|w\|_{*,e},\qquad
 C_{A,e}R_e<r_{B,e},
 \tag{14}
\]
on an admitted old potential ball of radius \(R_e\).
Here \(r_{B,e}\) is a radius inside the old continuation domain.
Use that existing conditional estimate; no second proof of it is needed.

Thus the direct attempt asks whether (8) gives the corresponding bound for the complete \(w_e(\lambda)-w_e(0)\).
At a matched native tower it does, through the source's weighted norm and pinning estimates.
For the full old call, differentiating (9) also differentiates every retained node map and transport in (13).
Those are evaluated at their original arguments and branches.
The required estimate must be in the old norm (12), on its full first member and endpoint blocks.
The final value of \(s_\star\) on \(R\) is not a bound on this composite derivative by itself.

The same issue affects the centre of the disc.
The assertion about \(q(\xi)\) in Y 73501–73510 describes the prepared anchor and its subordinate towers.
Applying it to (9) requires identifying the original rows, real frame and retained spectator arguments there.
Their equality cannot be assumed from equality of a final pair.
Y 69111–69134 retains exactly this check on the complete turn polydisc.
Its instruction is to check the pin estimate against every earlier reader's room.

**Where this route stops.** I did not establish that the literal old read in (13), uniformly in \(\zeta\), satisfies these antecedents.
In particular, I obtained no margin (10) and no normalized datum estimate (11) for that read.
The fixed-tower theorem and the one-move estimates remain available.
This failure does not assert that their antecedents are false on an actual history.

### Route 2: collapse the old read to the prepared critical representative

Try to avoid the missing composite estimate by identifying the entire old argument with the pinned prepared representative.
Then the source's anchor/profile calculation could be applied directly, with the original masks.
At full physical parameters the kept form is indeed evaluated at the current background, by SA 17558–17564.
Y 73546–73555 identifies the prepared endpoint and its stored pins.

The attempted extension to the whole complex pair domain needs more than that identity.
The independent current is an independent coordinate, by SA 5665–5671 and 5757–5760.
Successive shifts and pinning transport it additively and by conjugation.
Even in common units, two retained shifts give
\[
 K_2=\operatorname{Ad}(u_2u_1)(K_0+\nu_1j_1)
                     +\operatorname{Ad}(u_2)(\nu_2j_2).
 \tag{15}
\]
Each \(j_m\) has its actual earlier arguments.
Replacing (15) by the current of the final link requires a separate identity.
The test in section 1 shows why cancellation of link increments does not give it.

Holomorphic uniqueness does not establish this identity from agreement on physical pairs alone.
On a small link chart the physical current \(J_{\rm ph}(W)\) is holomorphic.
The holomorphic, gauge-invariant pair function
\[
 G(W,K)=\operatorname{tr}\bigl[(K(b)-J_{\rm ph}(W)(b))^2\bigr]
 \tag{16}
\]
vanishes on every physical pair \(K=J_{\rm ph}(W)\).
It is not identically zero on the independent-current domain.
For \(W=1\), take \(K(b)=z\operatorname{diag}(1,-1)\), with small nonzero \(z\), and all other current components zero.
Then \(J_{\rm ph}(1)=0\) and \(G=2z^2\ne0\).
This example respects the pair tie and shows the precise failure of the proposed identity-theorem inference.
It is not a counterexample to the actual carried maps.

Agreement on an open real slice in *all* independent coordinates would suffice locally.
Alternatively, an identity from the actual equations and original stored transports could suffice.
Neither is supplied by equality on the physical graph alone.
Nor would an endpoint identity admit the intermediate logarithms used to construct it.

**Where this route stops.** It does not replace the complete read in (9) by the simple prepared read on the required parameter set.
Consequently it does not supply (10)–(11).
I retain the physical identification as prior work, without promoting it to an all-parameter domain theorem.

### Route 3: port the complete account's inherited-domain theorem

The CA index has several close results. Their proofs are real prior work.
The following comparison uses their actual hypotheses, not the index label alone.

| Account result | What it supplies | Why it does not finish (10)–(11) here |
|---|---|---|
| I 62245–62325, `4.21:prop-link-containment` | Containment in a stored domain under its threshold arithmetic and tube assumptions | Hypothesis (a) retains containment at Bałaban's family; (c) retains the dilated-clause bound; (d) retains descendant tube containment. They must be matched to this reader. |
| I 62856–62935, `4.21:cor-radius-loss` | One-reading costs and allocation of the existing chart allowances | It reads the named link and dilation hypotheses. Its allowance bookkeeping does not construct this old datum or its anchor. |
| I 124189–124325, `4.26:prop-source-image` | The stage source enters the inherited domain at real slot data | It uses the supplied source, increments, older-piece clauses and inherited room. None is identified there with (9) for this H-O reader. |
| I 125926–126046, `4.26:lem-analyticity-membership` | A stage space lies in a broad analyticity class by a finite maximum of frozen weights and radii | Inclusion in that larger class is not inclusion in this reader's original birth core. |

The source-image proof has a particularly useful quantitative refinement.
I 124330–124400 asks that each amplified layer increment spend at most one quarter of inherited room.
It uses a source radius \(\mathsf w_L\) bounded by a fixed power of \(\log g_k^{-2}\).
The layer factor \(2^{-(k-1-m)}\) pays the room factor \(2^{-(k-m)}\).
This is a proved conditional comparison, which should be reused on that source.

For this reader, the requested radius instead contains \(Q^{u_R}\), with unbounded retained age \(u_R\).
Substituting \(2/a_R\) for \(\mathsf w_L\) in that proof requires the additional \(Q^{-u_R}\) estimate in the *same old clauses*.
Y's final-pair profile provides a candidate for it, but this substitution returns to the unmatched old datum (9).
There is no inference from a polynomial source-radius ceiling alone to this age-dependent disc.
The account also separates complex slot analyticity at I 124348.
It is not supplied by its real-slot pair inclusion.
The extra-parameter corollary, I 124108–124187, retains two explicit hypotheses.
Its input families must already be holomorphic on the same domains with the same majorants.
Its Gaussian integrals, stage layer, current slot and listed operators must remain independent of that extra parameter.
Thus it cannot supply missing spectator admission merely by treating \(\zeta\) as another parameter.

The birth-radius alternative at I 128186–128339 was also inspected.
It proves half-room for its real reference under a uniform assignment of levels and units.
It requires corresponding changes to the tube, shell, source and kernel statements.
It does not identify that reference with the literal old datum (9).
Its warning about mixing birth-level factors with frozen-level units supports the unit test in section 1.
No change to the prescribed reader or its birth core is made here.

I 49495–49546 separately identifies background-space inclusion as an application condition of the operator theorem.
That remark is not used to deny the later conditional proofs.
It prevents importing the operator theorem as an unconditional replacement for their input matching.
The permitted Balaban paper directory was absent here; the argument did not stop for that reason.
The account's quoted statements and the expanded outline were available.

**Where this route stops.** No identification of its supplied inherited source and slot domain with the full source of (9) was obtained.
No admitted disc of radius \(2/a_R\) for that old datum follows from this port.
Thus this route also leaves the same lemma (10)–(11) unproved.

## 5. Result and handoff

**Stop (c): D4-OLD-TOWER-ENTRY remains unproved after the three routes above.**
This is failure of these proof attempts, not a proof that the lemma is false.
No actual Yang–Mills history violating D4 has been constructed.
The written kill tests refute two weaker budget arguments only.

The leaf does not yet supply D4-CARRIED to loc-4 Theorem W or the radius required by H-O (11a).
It leaves their existing input unchanged.
The later-island requirement H-O (11b) remains H-E's separate input.
The next leaf in hstep-tree is persistence of the certificate at later outer preparations.
It cannot start from a completed certificate here.
No separate registry item, audit result or scientific status is created.
This note has not been checked by another model.

| Item | Status in this note |
|---|---|
| Repository and source prior work | Cited statements inspected at the recorded ranges; no duplicate proof claimed |
| Opposite-potential, equal-current test | Potential-only budget refuted by hand |
| One-level tower and age-one radius test | Main-radius-only and age-free budgets rejected by hand |
| Pinned pair construction and profile | Ported from Sussman–Alpoge, Y 73373–73559, with their inputs |
| Fixed-tower response and product chart | Existing source results retained with their fixed-sequence hypotheses |
| Full original datum, anchor margin and amplified estimate (10)–(11) | **Open: D4-OLD-TOWER-ENTRY; three routes unsuccessful** |
| Physical agreement extended by holomorphic uniqueness alone | Inference refuted by (16); actual maps not refuted |
| Complete-account inherited-domain results | Conditional proofs retained; source and radius match not established |
| D4-PINNED-CORE for the first old outer reader | **Not proved; stop (c)** |
| Later outer-preparation stability | Next leaf only after the first certificate is supplied |

**First open input:** D4-OLD-TOWER-ENTRY, (9)–(11), on the literal first old reader's complete source.
The required work is to match its original determining rows, fixed real frame, retained substitutions and spectator ranges, then prove the quantitative anchor and displacement bounds.
The existing owner remains DOM under D4-CARRIED.
