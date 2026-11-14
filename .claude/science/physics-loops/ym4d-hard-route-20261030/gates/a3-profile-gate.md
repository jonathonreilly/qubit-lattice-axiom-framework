lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T04:23Z

# Gate: `library/a3-profile.md` (row 86)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, statement pinned at d5ee4fb43 on `claude/ym4d-hard-route`. The note was written by Codex. This is one hand read by a reader from another provider: not an audit, and it grants no status. Sources: the Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once into a scratch folder (SA line numbers as in the note), and T. Balaban, CMP 102 (1985) 277–309 (OCR in `~/ym4d-papers/`, not copied here). I used no numerics and no subagents.

Labels, as in `gates/share-check-199fac1cb.md`: **ADVANCE**, the proof stands at the level of its steps and any defect is local with a repair in hand. **CORRECT-NO-ADVANCE**, no counterexample, but a step as written fails and its repair is not done. **WRONG**, false as written.

## Verdicts

| Step | Verdict | First failure / scope |
|---|---|---|
| §3 explicit localized family (kill attempt) | ADVANCE | None. A closed test: the slow plateau is not a counterexample. It proves nothing for general data, as the note says. |
| §4 input list P81, P82 | ADVANCE after one addition | Not quite "exactly" the pending list (§9): the flat column bound for \(K^*\), used in §6.2, is missing (D1). Every other input used is listed. |
| §5.1 geometry, auxiliary sequence, restriction is critical | ADVANCE | None. Induction rechecked; the constants absorb a factor \(L\) in the read-cube size. |
| §5.2 datum gauge, (14)–(16) | ADVANCE (given P81) | None. This is Balaban's (145)–(146), (151), (155), (160), localized. |
| §6.1 force and curvature expansions (17)–(20) | ADVANCE | None. Elementary; rechecked term by term. |
| §6.2 near/far split (21)–(22) | ADVANCE (given P81, P82) | None. |
| §6.2 multiplier (23)–(25) and current return | ADVANCE (given P81, P82, D1) | None. The identity \(H^*\partial^*\partial\mathcal G=0\) holds; it reads \(Rd^*H=0\), stated in P82. |
| (26) local inequality | ADVANCE (given the above) | None. The proof gives \(\sigma^2 r_R^2\); the boxed \(\sigma^4\) is a harmless enlargement. |
| §7 slowly varying maximum, (27)–(30) | ADVANCE | None. Depth uniformity survives the seams (§3 below). Typo in (29) (D2). |
| §8 consumer statements | ADVANCE | None. (31) follows from (30); the limits on floor screening and on 2.8 (L) are correct. |

**First failing step: none.** What stands is the implication P81 ∧ P82 ∧ (D1's flat column bound) ⇒ (30) for real, no-inward-bond, regular critical fields on separated sequences with \(\mathfrak M,\rho\ge C_L\sigma\) and the first torus floor, uniformly in depth. None of the three inputs is discharged here. Row 84 counts as this conditional theorem, not as closed A3.

## 1. What was redone, step by step

**§3, ADVANCE (closed test).** Rechecked: (5) holds across block ends, since the last value in block \(j-1\) is \(tq_j/s^2\). Composing one-step means of a Cartan field adds the angles of the \(L\) child columns, so \(b_j=\sum_{B_j}a_i\). The site factors and the direction-1 averages vanish because the contour angle is odd in the direction-2 displacement. In (7) each \(r\in B_j\) has multiplicity exactly \(s\) in \(T_{j-1}+T_j\). Also \(\sum_u p=(t/s)[q_j(s-1)/(2s)+q_{j+1}(s+1)/(2s)]\ge t\max(q_j,q_{j+1})/(3s)\) for \(s\ge3\), which gives (8) and the factor 24. For criticality, the action derivative is constant on blocks, the straight-mean adjoint gives \(L\cdot L^{-4}\) per step, and the site-factor terms pair with \(\partial_2\omega=0\). Perpendicular colour directions vanish on both sides by \(U(1)\) covariance, and the direction-1 current vanishes because its paired staples carry equal angles.

**§5.1, ADVANCE.** The dichotomy holds: a read cube about a point of layer \(j\ge1\) lies at distance \(>\rho\xi_{j-1}\) from \(\Omega_0^c\), and inside layer 0 every bond is a row, so the direct bound \(r\le6v_R\) applies there. Two scales at most: the note writes the cube diameter as \(C\sigma\xi_j\) but then takes \(C_J\) of half-side "comparable to \(\sigma s\)" with \(s\) possibly \(L\xi_j\). This is consistent once that comparability constant depends on \(L\), with \(\rho\ge C L^2\sigma\). Restriction: the claim "\(\mathcal M^i\tilde U'=\mathcal M^iU\) on every \(\mathbb T^{(i)}\) bond with no end in \(O_{i+1}\)" holds by induction:
- Base: the collar \(\Gamma_0^{\rm aux}\) is prescribed.
- Step, neither end of \(c\) in \(O_{i+1}\): its double block misses \(O_{i+1}\), a union of \((i+1)\)-blocks.
- Step, one end in \(O_{i+1}\): then \(c\in\Gamma^{\rm aux}_{i+1}\), with its double block inside \(O_0\).

For \(i\ge J\), \(O_{i+1}=\varnothing\), so every original row at every level is preserved. Plaquettes crossing \(\partial O_0\) see only prescribed collar bonds. The auxiliary regularity uses \(\mathsf L_{\rm aux}\le\mathsf L\), with truncated currents at most six plaquettes at \(\xi=\eta\). This is the outline's mechanism 9 (SA 9913).

**§5.2, ADVANCE given P81.** Every coarse plaquette of the completed grid is a test, or the one-step mean of tests: the four blocks of an all-fine coarse plaquette avoid \(\Omega_J\), so all their bonds are \(\Gamma_{J-1}\) rows and none is inward. The comb strip has area at most \(3m\), because the combs to \(y\) and \(y+e_\mu\) agree before direction \(\mu\). The descent (14) has coefficient one, the bootstrap for \(u\mapsto L^2u+C_Lu^2\) is correct, and \(\sum_{n<J}(\xi_n/s)^2\le(1-L^{-2})^{-1}\). This is Balaban's CMP 102 §F, localized: (145)–(146) and (151) for the axial-gauge datum, (155) for the far rows at \(18d^2L^3M\varepsilon_0\), and (160) for the central rows at \((8d^2L^2+4L^2|x-y|)\varepsilon_1\), with \(\varepsilon_1,\varepsilon_0\) replaced by \(v_R,r_R\). Then (16) is P81(2) with \(r=C_Lr_R\) and \(b=C_L\sigma r_R\).

**§6.1, ADVANCE.** In (18) the linear displaced terms are \(\nabla_\mu A_\nu-\nabla_\nu A_\mu\). \(R_0\) is \(\eta^{-2}\) times the Hermitian part of the commutator of \(e^{i\eta A_\mu(z)},e^{i\eta A_\nu(z)}\); for \(\eta a_*\le1\), \(|R_0|\le Ca_*^2\) with Lipschitz constant \(Ca_*\). In (19):
- the \(R_0\) difference costs \(Ca_*g_*\);
- \(R_1\) at two sites costs \(C(a_*g_*+\eta g_*^2)\);
- the transport costs \(Ca_*(g_*+a_*^2)\);
- \(T_A-I=O(\eta a_*)\) multiplies \(|\partial^*\partial A|\le Cg_*/\eta\).

The scale check \(\xi^3(a_*g_*+a_*^3+\eta g_*^2)\le3\|A\|_1^2\) needs \(\|A\|_1\le1\) and \(\eta\le\xi\). At an auxiliary seam the stencil spans two scales, which costs \(L^3\). For boundary staples at layer 0, \(\eta^3(a_*^2/\eta+a_*g_*+a_*^3)\le C\|A\|_1^2\). (20) is the same expansion without the divergence.

**§6.2 near/far, ADVANCE given P81, P82.** \(\sup_{t\ge0}(1+t)e^{-at}\le1+a^{-1}\) (the maximum is at \(t=a^{-1}-1\) when \(a<1\)), so the coefficient of \(v_R\) is \(C_L(1+a^{-1})\), free of \(\sigma\). Rows off the central cube have tops at physical distance \(\ge c\sigma s\), and auxiliary scales are \(\le s\), so \(d_*\ge c\sigma\). In (22) only \(H\beta\) needs a weighted bound; both quadratic remainders enter unweighted, since \(w\le1\).

**§6.2 multiplier, ADVANCE given P81, P82 and D1.** I rederived (23). \(H^*F'(A)=H^*\partial^*\partial A+H^*M(A)\), and \(H^*\partial^*\partial A=E\beta-ED(Z)\), using \(H^*\partial^*\partial H=E\) and \(H^*\partial^*\partial\mathcal G=0\). The last identity is the first-order optimality of \(H\beta\) for \(\|\partial A\|^2\) on \(\{KA=\beta\}\cap\) slice, tested against \(\mathcal Gf\in\ker K\cap\) slice. Equivalently \(\partial^*\partial H=K^*E\), from \(G_0^{-1}H=K^*(KG_0K^*)^{-1}\), \(KH=I\) and \(Rd^*H=0\); the last reads \(Kd\lambda=0\) for \(Q'\lambda=0\) and \(\partial d=0\) on inner plaquettes. The right side is \((KH)^*\omega+H^*C'(A)^*\omega\). The Neumann series, (24) and (25) are correct. Moving \(H^*C'^*\omega\) into the unweighted error \(\mathcal E\) means no weighted inverse of \(I+H^*C'^*\) is needed. Current return: \(J=(T_A^*)^{-1}(K+C'(A))^*\omega\). The rows whose supports contain a central bare bond have tops at bounded \(d_*\) and lie at levels \(J-1,J\) only. This replaces Balaban's sup bounds on \(\partial^*\partial H,\partial^*\partial\mathcal G\) in (164)–(165), which the note rightly does not assume (the CMP 99b Theorems 3.12–3.13 exception). The substitution is sound.

**(26), ADVANCE.** The constants are \(C_0=C_L(1+a^{-1})\), \(C_1\) from the far rows' factor \(\sigma\), and \(C_2\) from \((\sigma r_R)^2\), all fixed before \(\sigma\). The proof gives \(\sigma^2r_R^2\); the boxed \(\sigma^4\) is weaker.

**§7, ADVANCE.** \(C_1\sigma^2e^{-ca\sigma}\le48C_1(ca)^{-3}\sigma^{-1}e^{-ca\sigma/2}\to0\). With \(C_2\sigma^4\varepsilon_*\le1/8\) this gives (27). (28) is the triangle inequality for the path metric \(d_{\mathbf B}\), applied in both directions. The algebra of (29), the zero-datum case and (30) are correct.

**§8, ADVANCE.** (31) is (30) with the maximum bounded by the sum. Its rate is \(\delta\), not \(\delta_0\), and it gives no two-background (L). Both limits are stated correctly, and agree with `gates/floor-screen-gate.md` §5.

## 2. Does §4 list every input taken from rows 81 and 82?

Yes, with one exception, D1. I traced every use back to its source.

| Input used | Where used | In §4? | Source named |
|---|---|---|---|
| One-step mean: local, covariant, analytic; coarse plaquette \(\le L^2u+C_Lu^2\) | §5.1 induction; §5.2 completed grid and (14) | P81(1) | CMP 98; SA 9808–9823 |
| Reconstruction with coefficient one in block axial gauge; no coarse term inside a block | §5.2, (14), (15) | P81(1) | CMP 99a Lemma 1, as CMP 102 (160) uses it |
| Outward-row reduction reads one finer block and is Lipschitz | (15) | P81(1) | SA reduced datum; CMP 102 (154) |
| Representative and straightened coordinate, unweighted bound (9) | (16) | P81(2) | CMP 102 (152) via CMP 99a Thm 2; (157)–(159) |
| Quadratic bounds (10) on \(D,N\) | (22), (24) | P81(2) | CMP 102 (55), (97)–(98) (located in the OCR) |
| Euler equation with multiplier \(F'(A)=(K+C'(A))^*\omega\) | (23), current return | P81(2) | CMP 102 (178) |
| Column bound for \(C'(A)^*\) | (23), (24), current return | P81(2) | SA 9808–9821 |
| **Column bound for the flat \(K^*\): \(\sum_c|K(c,b)|\le C_L\eta^4\mathsf L(b)^{-3}\)** | current return, §6.2 | **no (D1)** | SA 9811–9812 at \(A=0\), \(U_0=1\) |
| \(KH=I\), \(Rd^*H=0\) (flat W1, \(\partial d=0\)), \(K\mathcal G=0\), \(Rd^*\mathcal G=0\) | (23) | P82 (text) | outline 1b.3; Balaban |
| Weighted \(H\): rows \(\to\|\cdot\|_{1,w}\) | (22) | P82 (11) | \(H=G_0K^*(KG_0K^*)^{-1}\) is CMP 99b (3.126) = CMP 95 (1.103); the weighted row sum as in CMP 102 (161)–(162), from CMP 96 (2.47)–(2.51) |
| \(\mathcal G\): \((-3)\to\|\cdot\|_1\), unweighted suffices | (22) | P82 (11) | CMP 99b (3.42)–(3.47) at \(U=1\), as the note cites |
| \(H^*\): \((-3)\to\) rows, unweighted suffices | (23), (24) | P82 | transpose of the \(H\) kernel bounds (Schur) |
| \(E\): rows \(\to\) rows, unweighted and weighted | (23)–(25) | P82 | \(E=(KG_0K^*)^{-1}-I\) is Balaban's \(\Delta_k\) at \(a=1\), flat (CMP 99b (3.156)). CMP 99b p. 421 only says its analysis is "very similar" to that of \((Q'G'^2Q'^*)^{-1}\), so this is a port item, not a printed bound |

As the note states, the proof does not use:
- existence or uniqueness from Theorem 1;
- any curved or complex inverse;
- sup bounds on \(\partial^*\partial\mathcal G\) or \(\Delta\mathcal G\);
- Balaban's Proposition 9 or (189)–(190).

Outside rows 81 and 82 it reads the outline's definitions, its first torus floor and its order of constants (SA 9916).

**For row 82: the weighted package needed here is smaller than P82 lists.** Weighted bounds are needed only for \(H\) (rows to \(\|\cdot\|_{1,w}\)) and \(E\) (rows to rows). For \(\mathcal G\) and \(H^*\) the unweighted bounds suffice, because \(w\le1\) and those terms are only quadratic errors. P82 is still stronger than what the old `a3-response.md` supplied: its gated \(L^2\) estimates do not give (11) (gate b2c312b2e, Lemma S(iii)).

**For row 81: P81 is the toolkit of Balaban's own §F.** CMP 102 §F proves the global version of this theorem: Proposition 8, \(r\le\max\{B_3\varepsilon_1,\varepsilon_0/2\}\), iterated. It does so on the same kind of nested auxiliary cubes, (144) and (148)–(150), with the same near/far split (161)–(167). So a faithful row-81 port of §F delivers P81 as the note uses it. The note's two own additions to §F stand: the current through the multiplier in place of sup bounds on \(\partial^*\partial\mathcal G\), and the localization with a slowly varying maximum in place of the global halving. The profile form remains absent from Balaban, as `library/lit-balaban.md` §3 says.

**For both ports: they must share one row family.** Rows 81 and 82 have different workers, so the lead should check this when they land. The identity (23) needs one row family \(K\) in four places: the Euler equation of P81(2), the straightening (9), \(KH=I\), and \(K\mathcal G=0\). An invertible local rotation of the rows is harmless, since \(\ker K\) is unchanged; this is the outline's "up to a rotation of the rows", SA mechanism 2. At the flat reference the Landau slice may differ between the ports by gauge directions \(d\lambda\) with \(Kd\lambda=0\), because \(\partial d\lambda=0\). What breaks (23) is pairing Balaban's corner-based rows in one port with the outline's centred rows in the other: then \(K\mathcal G\neq0\) and \(H^*\partial^*\partial\mathcal G\neq0\) in general. This is a consistency condition on the pending ports, not a defect of the note, which already requires the outline's mean in both.

## 3. Depth uniformity across seams

I tried to break it at original seams and at the artificial seams of the auxiliary sequence. It survives both.

1. **One original seam per read cube.** A read cube about \(x\) meets at most two consecutive layers once \(\rho\ge CL^2\sigma\); the gap is chosen after \(\sigma\), in the outline's order. Its \(d_{\mathbf B}\)-diameter is at most \(CL^2\sigma\le R\), so (28) applies with \(e^{\delta R}=2\).
2. **No comb-through-a-slab failure.** The comb and every test it reads stay in a cube with two scales, \(s/L\) and \(s\). Auxiliary scales there are \(\le s\), so the comb's coarse length is at most \(C(1+d_*(x,y_c))\), and the weight pays for its linear growth. No profile is evaluated along a comb, so the slab failure the floor-screen gate found in (OS-loc) (§6 there) cannot occur here. The far rows are bounded unweighted, by \(C_L\sigma r_R\).
3. **Seam tests are counted.** Mixed seam plaquettes are tests; all-fine coarse plaquettes are one-step means of tests, costing \(L^2\) once; central outward rows read one finer block. All of this is inside the read cube, and the constants grow only through \(C_L\).
4. **Artificial seams.** The \(J\) seams in the shells enter only through the depth-uniform constants of P81 and P82, and through the descent (14). The descent has coefficient one and a geometric series, so the number of artificial layers never multiplies an error. Balaban's §F runs the same descent, (146) and (151).
5. **No dependence on depth.** \(C_0,C_1,C_2,a,c\) depend on \(L\) through P81 and P82. \(\sigma\), \(\varepsilon_*\), \(R=C_L\sigma\) and \(\delta=\log2/R\) are chosen from those, and nothing in (26)–(30) counts layers, seams or tests.

## 4. Defects

**D1. Unlisted flat column bound.** This breaks the sentence "The pending list is exactly §4" (§9), and nothing else. §6.2 returns from \(\omega\) to the current through "the column sum of \(K\) ... is \(C_L\xi^{-3}\)". P81 lists only the column bound for \(C'(A)^*\), which vanishes at \(A=0\) and says nothing about \(K\). None of P82's operators \(H,\mathcal G,H^*,E\) gives \(K^*:\sup\to(-3)\). Without this bound, (25) controls \(\omega\) but not the current at the centre. Repair, unproved here: add \(\sum_c|K(c,b)|\le C_L\eta^4\mathsf L(b)^{-3}\) to P81(1), with the identification of the outline's mean. It is the \(A=0\), \(U_0=1\) case of SA 9811–9812. Its straight part is computed in the note's own §3, at \(L\cdot L^{-4}\) per step. The block-factor and outward-row parts must come with the row-81 identification.

**D2. Typo, rendering only.** In (29), lines 646–647 of the note, the "\t" of "\tfrac12" became a literal tab on both lines, so they render as "\(2C_0+\) frac12 \(Q\)". Restore "\tfrac12".

No other defect found. The note's wording "a cube of diameter \(C\sigma\xi_j\)" in §5.1 needs its constant to carry a factor \(L\) (step notes, §5.1). That is not a defect.

## 5. What stays open

- P81, P82 and D1's flat column bound: all pending ports, rows 81 and 82; none is discharged in this checkout.
- The kept-inward-bond variant and the complex (Theorem 4 / 6(c)) response: not in this note.
- Admission of an arbitrary floor: row 88.
- The two-background comparison (L) of 2.8: rows 85 and 89. The profile does not supply it, as §8 of the note says.

Credit: the outline's definitions, Theorem 2's statement, mechanism 5 and the maximum-principle proposal are due to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text (`31a47c543775`). The flat coordinate reduction, the axial-gauge descent and the near/far improvement are T. Balaban's (CMP 102 §F; CMP 96, 98, 99). The localization, the multiplier route to the current and the write-up under gate are Codex's (`library/a3-profile.md`).
