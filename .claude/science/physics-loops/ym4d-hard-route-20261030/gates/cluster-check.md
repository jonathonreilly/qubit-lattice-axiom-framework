lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T16:27Z

# cluster-check (queue row 187): line-by-line check of `library/cluster-port.md` and `library/growth-qf3.md`

Worker: Claude Opus 5.5 at max effort, Mac mini worker session, started 2026-11-04T04:27Z, pinned at commit 3c53a7772. Same model family as the lead; this is not an independent-model check.

Provenance: Claude Opus 5.5, max effort, Mac mini worker, commit 3c53a7772; one reading by one model, not an audit. The two notes are by Codex. Sussman–Alpoge sources read at `31a47c543775` (SA = `YM4_sketch_500.tex`, Y3 = `YM3/YM3_I.tex`), credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No numeric run was used; every check below is by hand.

Status: Part A finished. Part B in progress.

## Part A. `library/cluster-port.md`

**Verdict: checked line by line by Claude, first failing step none.** Every statement is a correct implication from its named premises, S1g (`am1-port.md`) and, from Section 8 on, S3. ADVANCE for skeleton nodes S12–S14, conditional on S1g and S3.

**Kind (FINISH item 9): check of their proof.** The outline already proves the same statements in four dimensions, with the same constants and the same rate:

- PL3 with rate \((r/n)^2+(r/n)^3\), threshold and momentum density \(Cr^3\): SA L3238–3750 (Theorem "Uniform plateau bound", (PL4)–(PL16), and the closedness corollary).
- Conditional kernel on a compact metric space: SA L30875 (Theorem "Compact-metric conditional law").
- Fixed-spacing decomposition, components and uniform \(|v|^{-2}\) clustering: SA L31112–31385 (Theorem "Conditional canonical decomposition").
- PV4: SA L31442. There it is proved under the hypotheses (PV1)–(PV3), which that section does not derive (SA L31438–31440).

So Sections 2–8 rebuild proofs that the outline gives in detail at d = 4. Section 9 also derives (PV3) from the limit's bounds, RP and translation invariance. SA's PV4 section assumes (PV3); the derivation agrees with the H2 step that `s4-s6.md` covers (row 205 checks it).

### A1. The d = 4 changes, each redone

| Change (note's list) | Where | Check |
|---|---|---|
| three tangential momenta, carrier \(E\ge\kappa\lvert\eta\rvert_\infty\), \(\kappa=\frac2\pi\log(1+\sqrt2)\) | §2, (4) | Correct. The disc lemma works in one coordinate plane. \(E\ge 2\operatorname{arsinh}\sin(\lvert\eta_\lambda\rvert/2)\) follows from \(\cosh E+\cos\eta_\lambda\ge2\). That function is concave on \([0,\pi]\), so it lies above the chord \(\kappa u\). The fourth direction adds one more carrier to intersect. |
| sixteen sign changes in \(\mathcal N_r\) | §4, (7) | Correct. \(\Gamma_{16}\) is a group, so \(\mathcal N_r(\theta_\mu A)=\mathcal N_r(A)\) and \(\mathcal N_r(A_\pm)\le\mathcal N_r(A)\). |
| shell count \(24k^2+2\) in \(\mathbb Z^3\), density \(0\le h_A\le Cr^3\mathcal N_r(A)\) | §4, (10)–(11) | Correct. \((2k+1)^3-(2k-1)^3=24k^2+2\). With \((2r+j)^2\le 8r^2+2j^2\) and the two displayed sums, \(\sum_w\lvert K(w)\rvert\le Cr^3\mathcal N_r(A)\) for \(r\ge1\). The bound \(\sum_{j\ge1}j^2e^{-hj}\le\int_0^\infty(x+1)^2e^{-hx}dx\) holds because \(j^2e^{-hj}\le\int_{j-1}^{j}(x+1)^2e^{-hx}dx\). |
| shell volume \(24u^2du\), leading power \((r/n)^2\) | §5, (12) | Correct. \(Cr^3[2/(n\kappa)^3+1/(2r\kappa(n\kappa)^2)]=C[(r/n)^3+(r/n)^2]\). The two-sided Cauchy–Schwarz keeps the order. |
| Euclidean threshold \(8ra\) | §5, (13) | Correct. In \(\mathbb R^4\), \(\lvert y\rvert_\infty\ge\lvert y\rvert_2/2\). Then \(n\ge\lvert y\rvert_2/(4a)\), \(r/n\le\frac12\), and the bound is at most \(24C(ra/\lvert y\rvert_2)^2\). |
| \(C(Q)^5\), \(W_4\), decay in (18) | §8 | Correct. The reflection moments in \(\mathcal N_{r_j}(F_j)\) are moments of \(2k\) tests with mutual separation \(\min(\delta(F),2\epsilon)\), since \(r_ja_j\ge R_0\). |
| time coordinate \(x_4\) | §9 | Correct; dimension-free otherwise. |

### A2. Other steps redone

- §2. Disc lemma: \(\lvert\cos(u+iv)\rvert^2=\cos^2u+\sinh^2v\); the radial limit of \(\varphi\) is \(\pi/2\) on the circle except at \(1\); both identities for \(\tan\varphi\) and \(\lvert1+\zeta^2\rvert^2-4\lvert\zeta\rvert^2\) verified by expansion. The diagonal identity has displacement \((2R+k+l)e_\mu+(k-l)e_\lambda\) on both sides. Positivity of \(T_+\) uses the diagonal mirror at height \(R+1\) (\(\theta_{R+1}\tau_{d_+}=\theta_R\)). \(T_\mu\ge0\) uses the bond mirror at \(-1/2\).
- §3. Positive involution on \(L^2(\mathcal I_\mu)\) is the identity; the isometry \(\Pi_\mu[F]\mapsto P_\mu F\) intertwines tangential translations, so \(\mathcal I_\mu=\mathcal I\).
- §4. \(b_m\), \(\sum\lvert z_m\rvert b_m=b(0)-b(\pi/2)=8\), the three-shift formula for \(q\), and the Poisson representation of \(t\Psi(t)\) are correct. The lower bound \(\Psi(t)\ge\frac{1-t^2}{1+t^2}\frac{\sqrt2}{1+t^2+\sqrt2t}\ge c_\Psi\tanh x\) is correct, with \(c_\Psi=(1+\sqrt2)^{-1}\).
- §5. Removal of the filter needs zero mass on \(\{0<E<\infty,\eta=0\}\) only for the filtered measure; (11) gives it. Closedness of the ergodic class is correct.
- §6. Kernel construction: Borel representatives stay \(\mathcal H\)-measurable because \(\mathcal N_\mu\subset\mathcal H\); measurability of \(x\mapsto k(x)\) follows from the countable coordinate embedding; monotone class extension is correct.
- §7. Invariant densities keep DLR; ergodic components lie in \(\mathcal G_{a,\beta}\), so S1g applies to them; (15) and the variance argument give ergodicity; uniqueness of \(D_\nu\) by iterated far-translation limits is correct.
- §8. The partition formula with singleton blocks as differences of means gives (16). The order of choice "\(v_q\) first, …, \(v_2\) last" is correct for the nested limit (20): \(v_2\) separates \(F^2\) from the union fixed by \(v_3,\dots,v_q\). Support points, barycenters, uniqueness of the representation, RP of components (lattice mirrors \(\to\) continuum mirror) are correct.
- §9. The form is positive; \(\lVert[\tau_sF]\rVert\) is bounded uniformly in \(s\ge0\) by (16) with separation \(\min(\delta,2d_0)\); iterated Cauchy–Schwarz gives contraction; \(\ker T_1=\{0\}\) and positive roots give \(T_t=e^{-tH}\); (21) and Stone–Weierstrass give PV4.

### A3. Reading needed (not a defect)

Section 1 does not say where the centering state \(\nu_j\) lives. Section 8 uses its decomposition \(D_{\nu_j}\) and its symmetry ("S1g ensures covariance also for the common centering"). So the note needs \(\nu_j\in\mathcal G_{a_j,\beta_j}\). SA fixes this choice (SA L31143: "a centering state \(\nu_j\in\mathcal G_j\) is fixed"). With that reading nothing changes.

### A4. What Part A does not show

S1g and S3 stay premises. Rows 206 and 205 check `am1-port.md` and `d2-d4.md`. No spectral gap follows, and PV4 is on the separated positive-time domain only.

