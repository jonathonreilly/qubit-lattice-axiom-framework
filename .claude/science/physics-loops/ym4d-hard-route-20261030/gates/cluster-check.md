lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T16:27Z

# cluster-check (queue row 187): line-by-line check of `library/cluster-port.md` and `library/growth-qf3.md`

Provenance: Claude Opus 5.5, max effort, Mac mini worker, started 2026-11-04T04:27Z, commit 3c53a7772; one reading by one model, not an audit. The two notes are by Codex, so this is the other-model check of FINISH item 5. Sussman–Alpoge sources read at `31a47c543775` (SA = `YM4_sketch_500.tex`, Y3 = `YM3/YM3_I.tex`), credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. No numeric run was used; every check below is by hand.

Status: Parts A and B finished.

## Part A. `library/cluster-port.md`

**Verdict: checked line by line by Claude, first failing step none.** Every statement is a correct implication from its named premises, S1g (`am1-port.md`) and, from Section 8 on, S3. ADVANCE for skeleton nodes S12–S14, conditional on S1g and S3.

**Kind (FINISH item 9): check of their proof.** The outline already proves the same statements in four dimensions, with the same constants and the same rate:

- PL3 with rate \((r/n)^2+(r/n)^3\), threshold and momentum density \(Cr^3\): SA L3238–3750 (Theorem "Uniform plateau bound", (PL4)–(PL16), and the closedness corollary).
- Conditional kernel on a compact metric space: SA L30875 (Theorem "Compact-metric conditional law").
- Fixed-spacing decomposition, components and uniform \(|v|^{-2}\) clustering: SA L31112–31385 (Theorem "Conditional canonical decomposition").
- PV4: SA L31442. There it is proved under the hypotheses (PV1)–(PV3), which that section does not derive (SA L31438–31440).

So Sections 2–8 rebuild proofs that the outline gives in detail at d = 4. Section 9 also derives (PV3) from the limit's bounds, RP and translation invariance. SA's PV4 section assumes (PV3); SA treats that step as H2 (L4600, L25491), and `s4-s6.md` ports it (row 205 checks it). I checked the note's own derivation in A2 below.

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


## Part B. `library/growth-qf3.md`

**Verdict: checked line by line by Claude, first failing step none.** D2 implies (1): \(\lvert S_n(\varphi)\rvert\le C^n(n!)^{k+32}p_{20n}(\varphi)\) on \(\mathcal S_{\Delta,n}\), with a unique extension, constrained tensor density (positive-time boundary included), and RP transfer under compact RP. ADVANCE for skeleton S5 and O3 (E0′), conditional on D2 (S2).

**Kind (FINISH item 9): check of their proof.** SA L24915–25420 (Theorem "Quantitative diagonal-flat extension", (QF1)–(QF22)) proves the same theorem at d = 4 for a general exponent \(\alpha\): \(k_*=\lceil\alpha\rceil+15\), factorial exponent \(\kappa+32\). SA H1 (L4572–4590) states \(k_{\rm E}=20\), \(\kappa_{\rm E}=k+32\) at \(\alpha=5\). The note is that proof at \(\alpha=5\).

### B1. The d = 4 changes, each redone

| Change (note's §6) | Check |
|---|---|
| A literal YM3_I port fails at its Fourier majorant. | Correct. Y3 IV-25-55 (L74807–74900) integrates by parts to total order \(k=4n+1\) in one coordinate. After the tensor norms \(\prod(1+\lvert\omega\rvert_\infty)\), the summand is \((1+\lvert\omega\rvert_\infty)^{-(3n+1)}\). The shell \(\lvert\omega\rvert_\infty=r\) has order \(r^{dn-1}\) points. That gives \(\sum r^{-2}\) at d = 3 and \(\sum r^{n-2}=\infty\) at d = 4. |
| Repair: \(8n\) slotwise derivatives, (6). | Correct. \((1-\pi^{-2}\Delta_{y_i})^4\) gives \(\prod_i(1+\lvert v_i\rvert^2)^{-4}\). Each slot sum \(\sum_{v\in\mathbb Z^4}(1+\lvert v\rvert)(1+\lvert v\rvert^2)^{-4}\) is finite (shell \(Cr^3\cdot r^{-7}\)). |
| YM3_I's weight \((1+\lvert u\rvert^2)^{-2}\) is not integrable on \(\mathbb R^4\). | Correct (logarithmic divergence). (12) uses \((1+\lvert x_i\rvert^2)^{-10}\), and \((1+\sum\lvert x_i\rvert^2)^{-10n}\le\prod_i(1+\lvert x_i\rvert^2)^{-10}\). |
| Powers of \(h\): D2 \(h^{-5n}\), tensor norms \(h^{-n}\), grid \(h^{-4n}\), Taylor \(h^{10n+2}\). | Correct. \(\max(1,(h/2)^{-5n})=32^nh^{-5n}\); \(\ell^{-n}=64^nh^{-n}\); \(\sum_z\le C^n\ell_j^{-4n}\). Net power \(h_j^2\), summable over \(j\). Derivative order \(8n+10n+2\le20n\) for \(n\ge1\). |
| Factorial loss \((Cn^2)^{8n}((8n)!)^2\le C^n(n!)^{32}\), (9). | Correct. \(n^{n}\le e^nn!\), and \((8n)!/(n!)^8\le8^{8n}\) (a multinomial coefficient). No \(e^{cn^2}\): undifferentiated cutoffs cost one in (5). |

### B2. Other steps redone

- §1, (3). \(\sum_{\pi:\,m\text{ blocks}}\prod_D\lvert D\rvert!=\frac{n!}{m!}\binom{n-1}{m-1}\) (Lah numbers). With \(\prod_D\lvert D\rvert!\le n!\) and \(k\ge1\), the sum is at most \(2^{n-1}(n!)^k\). With \(\prod_D\max(1,\delta^{-5\lvert D\rvert})\le\max(1,\delta^{-5n})\) this gives (4).
- §2. \(\operatorname{Re}(1/z)\ge2/(9t)\) on \(\lvert z-t\rvert=t/2\); Cauchy gives \(\lvert a^{(q)}\rvert\le9^q(q!)^2\). The reciprocal induction closes: with \(L=B(1+2A/d_0)\), \((A/d_0)\sum_{r\ge1}(B/L)^r=1/2\). Leibniz bound (5) is correct. Tensor consistency: a pair of slot sets closer than \(\delta/2\) forces a zero factor, since otherwise two supports would be closer than \(\delta/2+\delta/4<\delta\).
- §3. Coefficient bound (6), sharp norms \(C\ell^{-1}(1+\lvert v_i\rvert)\), and (7) with \(h^{-6n}\) are correct. The cutoff \(\chi^+\) is one on \(\operatorname{supp}u\) and vanishes outside \(Q\), so the expansion equals \(u\) everywhere. Fejér bound \(F_N\le[N\sin^2(\pi\varepsilon/2)]^{-1}\) is correct.
- §4. Layer support (8) is correct, also with \(P_hB_h\). Retained boxes have expanded-cube separation \(h_j-6\ell_j=\frac{58}{64}h_j>h_j/2\). Taylor: \(\lvert x-y\rvert\le2\lvert x_i-x_l\rvert_\infty\le8h_j\); \(\ell^1\) displacement \(\le16h_j\); weight transfer \(1+\lvert x\rvert^2\le3(1+\lvert w\rvert^2)\) costs \(3^{10n}\).
- §5. (15), (16) and the positive-time version are correct. The cross-diagonal flatness of \(\theta\bar f\otimes g\) and \(p_r(f\otimes g)\le p_r(f)p_r(g)\) are correct; RP transfer needs compact RP, as the note says.

### B3. Input match (not a defect)

The note's D2 form (2) at radius one, with the one-point clause, is what `d2-d4.md` (20)–(22) delivers "for every pair of periodic Wilson states". The S3 form read by Part A is `d2-d4.md` (8) and (10). So the three notes fit as written. Row 205 checks `d2-d4.md` itself.

### B4. What Part B does not show

D2 stays a premise. The bound is for moments centered at the common reference state, on diagonal-flat tests only. No contact terms and no extension across the diagonals follow.

## Summary for the lead

- Both notes: checked line by line by Claude, first failing step none. Each is a correct implication from its named premises.
- Both rebuild proofs that SA gives in detail at d = 4 (Part A: SA L3238–3750, L30875–31530; Part B: SA L24915–25420). So this lane is a check of their proof, not a new proof. Each d = 4 change the notes list is confirmed. Where YM3_I would fail at d = 4, the failure is real, and the repair the notes use is SA's.
- Skeleton lines this moves (lead to edit `t0-skeleton.md`): S12, S13, S14 from "cited" to "proved by Codex, checked by Claude, first failing step none; conditional on S1g and S3"; S5 the same, conditional on S2 (D2). O3 (E0′) and O8 follow as implications from those nodes.
- Still open on these nodes: S1g (`am1-port.md`, row 206), S2/S3 (`d2-d4.md`, row 205) and, upstream, D1.
