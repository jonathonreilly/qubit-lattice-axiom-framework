lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-08T01:45Z

# out-pi-check: faithfulness of library/out-pi.md

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, mac-mini-worker, fresh session, commit b9b7e0318. One reading by one model. Not an audit; grants no status. No computation; finite arithmetic is displayed.

**Checked text.** `library/out-pi.md`, 1708 lines, SHA-256 `495eeb50d937f91edf2b563d8139f562d6288d340346114125c3caafdb107581` (Codex, row 432).

**Sources.** `library/print-inverse-r2.md` ("r2"), 1260 lines, SHA-256 `fabe51d6…aa0343`, with its §13 repairs; `gates/pi-r2-gate.md` ("the gate"); `library/flat-port.md`, SHA-256 `329371416b74…b920cc` (the identity the gate recorded), §§2–9.2 and 12; `gates/flat-port-gate.md`. The account lines that out-pi.md quotes or cites anew were re-read at `31a47c543775` in a scratch copy: CA-I SHA-256 `4cb5cb5e…10e6e93` (equal to `library/prior/print-inverse.md:21-26`), CA-II `6a1f74b0…b2b8f`. New Balaban page numbers were placed with the page markers of the local OCR (`~/ym4d-papers/cmp95.txt`, `cmp96.txt`, `cmp99b.txt`). The OCR was used only to place equations, propositions and pages. No formula was transcribed from it, and no page image was rendered.

**Credit.** Tadeusz Balaban for the averages, projections, inverse operators and walk method. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the account. Codex for out-pi.md and flat-port.md; Claude for r2.

## Result

out-pi.md matches the checked texts in every statement, constant, hypothesis and proof step of Theorem PI, Propositions 3.1–3.3, Lemmas 4.1–7.1 and §§8–11. Every repair of the gate is present. Appendix A matches flat-port §§2–9.2 and 12, with seven NEW steps, each checked below. **First failing step in the main proof: none.**

Defects (ranked below, D1–D8): the flat inverse lemma's statement in §4.4 claims its cutoff clause for cutoffs not tied to the local scale, and omits the torus room that its proof chooses (D1; its uses are unaffected). The CMP 95 proposition number is wrong in three places (D2). One new sentence on the background domain conflicts with the settings of §3.4 (D3). Provenance, one quotation, one citation and some wording need small fixes (D4–D7). D8 is a gap shared with r2, not a mismatch. Corrected text is given for each.

## Verdict per statement

"MATCHES" means: same statement, constants, hypotheses and proof steps as the checked source, up to wording. Line numbers: out-pi.md first, then the source.

| out-pi.md | Checked source | Verdict |
|---|---|---|
| §1 scope, bare vs corrected, (3.132) display, 3–52 | r2 §1.1 69–94; gate §1 | MATCHES; D4, D5 |
| §2 lattices, towers (T), cube class, rows, Hessian, (S1), (S2), (S2+), (S1-loc), metric, 55–157 | r2 §§1.3, 2 138–219; gate §1 | MATCHES; D3, D7(a) |
| §3.1–3.2 operators, pairings, M_5, Schur objects, norms, (E), 161–228 | r2 §§3.1–3.2 223–276 | MATCHES; D6 |
| §3.3 constants, items 1–8, 230–259 | r2 §3.3 277–304 | MATCHES (same values, same order) |
| §3.4 tiles, exterior tiles, footprints, walks, settings, Theorem PI (a)–(e), 261–323 | r2 §3.4 306–368; gate §§1, 4, 7 | MATCHES |
| Props. 3.1–3.3, 325–350 | r2 §§3.5–3.6 370–401; gate §3 | MATCHES (3.3 has ∅ ≠ Ω_0 ≠ T_η; 3.1 keeps thickness and interior scope) |
| Lemma 4.1, 361–389 | r2 425–441 | MATCHES |
| Def. 4.2, Lemma 4.2, 391–494 | r2 443–504; gate §2 | MATCHES |
| Def. 4.3, (3.15), Lemma 4.4, 496–617 | r2 506–597; gate §2 | MATCHES |
| Lemma 4.5, 621–645 | r2 601–618; gate §4 repair | MATCHES |
| Flat inverse lemma, 647–669 | r2 [F] 619–637; flat-port (8.5)–(8.12), §9.2, §12 | **MISMATCH** D1, D2 |
| Lemma 5.1, 671–756 | r2 640–695; gate §5 | MATCHES |
| §5.2 tiles, cutoffs, two levels, models, agreement, diameter, overlap, 758–859 | r2 697–781; gate §§4, 5 | MATCHES; D7(b) |
| Lemmas 5.2–5.3, 861–911 | r2 783–818; gate §5 | MATCHES |
| Lemmas 6.1–6.3 and remark, 913–998 | r2 820–884; gate §6 | MATCHES |
| Lemma 7.1, PI(a), 1000–1042 | r2 886–925; gate §6 | MATCHES |
| §8 (8.1)–(8.3), PI(b)–(d), 1044–1105 | r2 927–974; gate §7 | MATCHES |
| §9 PI(e), C1 limit, 1107–1144 | r2 976–1031; gate §§7, 8 | MATCHES |
| §10 proofs, 1146–1226 | r2 1032–1100; gate §3 | MATCHES; D8 |
| §11 table, K10 geometry, not proved, 1228–1284 | r2 1101–1153, 1190–1205; gate §8 | MATCHES |
| A.1, 1296–1376 | flat-port §2.1 28–41, §3 79–127, §4.0 136–142, §5 (5.1)–(5.2) 237–258, §8.1 520–525 | MATCHES; NEW N1, N2, N7 |
| A.2, 1377–1453 | flat-port §6.1 286–356 | MATCHES; D2 |
| A.3, 1454–1574 | flat-port §6.2 357–418, §7 419–458, §9.2 657–664 | MATCHES; D7(c) |
| A.4, 1575–1611 | flat-port §8.1 511–539, §9.2 666–668 | MATCHES; NEW N3, N4 |
| A.5, 1613–1708 | flat-port §§8.2–8.3 541–609, §12 814–820 | MATCHES; D1; NEW N5, N6 |

Points checked with care, all MATCHES:

- Theorem PI's hypotheses are r2's: fixed constants, box side ≥ (2r̂+2)ℓ_k, (T) with R ≥ R_1, (S1-loc) with a_0 ≤ a_0^*, (S2) and (S2+) with a_1 ≤ a_1^*, literal rows. Parts (a)–(e) carry the same constants: C_q, δ_q, D_X, θ^{|ω|/2}, the 4/3 summation factor, the spare (4D_*)^{-|ω|}, 2·4C_q in (b).
- PI(e): r2 363 says the margin is (2L+1)M_tℓ_{j_{τ_0}} "at the first end, and the same at the last". out-pi 317 writes ℓ_{j_{τ_n}} at the last end. That is the correct reading: r2's proof (1021–1023) takes the margin as the difference of the half-widths of F_τ and supp h_τ at each end.
- The gate's repairs are all in place: common background domain (272–273), base-point support convention (317–318), ∅ ≠ Ω_0 ≠ T_η (341, 1210), Ω_n = ∅ for every n > k (77), run-of-sites centre (266), Lemma 4.5's separate row relabelling (621–645), corner-block reading of the flat lemma (666–669), the min{…} intersection bound (853–855), the one-bond exterior test in §9 (1126), the C1 limitation (1141–1144, 1253), the boundary real-gauge wording (1225–1226), K10 rate δ_q/17 and endpoint construction (1260–1279), 8δ_1 ≤ δ_q (1255).
- §2.1 adds "Distances in T are Euclidean" (80). r2's proofs use Euclidean distance (r2 723, 1035), and a Euclidean gap is the weaker hypothesis, so this states what the proofs use.
- §3.5 adds "Both constructions also satisfy (S2+)" (346). True: 𝔞 = 0 (gate 169).
- Lemma 5.3 cites covariance as CMP 99b (3.28)–(3.32) (896), where r2 810 has (3.31)–(3.34). out-pi follows the gate's image reading (gate 21). The OCR places the displays (3.28)–(3.32) on p. 395, inside the cited pp. 394–395.

## Defects, ranked by what each breaks

**D1. Flat inverse lemma: the cutoff clause is not tied to the local scale, and the torus room is missing (out-pi 647–660; proof 1636–1639, 1689).** Sources: flat-port (8.6) at 544–546 is stated for the cutoffs h_i of level-i tiles, |Dh_i| ≤ C_L/(Ms_i); (8.8) at 571; flat-port 582 and §12 818 fix a torus floor for the read sets; r2 282–283, 635, 719 take C_88 and c_h from (8.8), (8.6) "with M = M_t".
- *Mismatch.* out-pi states the multiplier and commutator bounds for "a smooth cutoff on scale Mℓ" with ℓ undefined and C unquantified. Its proof (A.23) needs the local scale on the cutoff's read to be at most L times the cutoff's level scale: the oscillation over a pillar or double block of scale m is m·|Dh|, which is C_L/M only when m ≤ Lℓ.
- *Failure if ℓ is read as a fixed lattice scale.* Take Ω'_0 = ⋯ = Ω'_k = T, so m = ℓ_k = L^kη everywhere, and take ℓ = η, M = L^{k−1}. Let h have its transition zone of width Mη, and let λ equal 1 on that zone and fall off over 10Mη. Then ‖[A_s,h]λ‖_2 contains (Δ_s h)λ, of order (Mη)^{-2} times the root volume of the zone, while ‖λ‖_{H²_m} is of the same order (its ‖D_αD_βλ‖ term dominates, since m ≥ LMη). The ratio is bounded below independently of M and k, not by C_88/M = C_88L^{1−k}.
- *Torus.* A.5 chooses "the torus room for its reads" (1689) and uses it (1637), but the stated lemma has no box-size hypothesis.
- *What it breaks.* Nothing downstream. Lemma 6.1 applies the clause to h_τ and Lemma 6.2 to χ_τ. Both have scale M_tℓ_{j_τ}, and their reads meet only levels j_τ−1, j_τ, j_τ+1 (§5.2, Two levels), so the adapted clause applies. For the torus, the uses in Lemma 5.3 are on model geometries 𝒢_τ. There I see no wrap: tiles whose enlargement meets the Dirichlet edge are bare (A.5, 1630), so interior reads stay inside Ω^τ_0, which lies in a cube of side 12M_tℓ_{j_τ}, smaller than the box side ((4L+4)M_t+2)ℓ_k. The global use in §10 (Δ_a(1) > 0) needs the room on T_η. That PI's floor (2r̂+2)ℓ_k always covers it is not checked here.
- *Corrected text (replace 647–660; unproved repair only in its torus clause, which restates flat-port 582):* "**Flat inverse lemma.** There are M_F, ρ_F, t_F and B_F ≥ 1, depending only on L, and for each C_φ there are c_h ≥ 1 and C_88, depending only on L and C_φ, such that the following holds. Let the periodic box have side at least t_F M_F ℓ_k. Let Ω'_0 ⊃ ⋯ ⊃ Ω'_k be nested unions of blocks of side M_Fℓ_n in a nested block grid, with ℓ_n^{-1}dist((Ω'_n)^c, Ω'_{n+1}) ≥ ρ_F. Use §2's rows, corner blocks and Dirichlet conventions, with empty terminal regions allowed. Then M_r(1), r ∈ {1,3,4,5}, is invertible and ‖M_r(1)^{-1}‖_{Y_r→X_r} ≤ B_F. Its vector Schur complement is positive and controls the squared energy norm. Let M ≥ 1 and 0 ≤ n ≤ k, and let h take values in [0,1], with |Dh| ≤ C_φ/(Mℓ_n), |D²h| ≤ C_φ/(Mℓ_n)², and local scale at most Lℓ_n on the read closure of supp h. Then multiplication by h has norm at most c_h on X_r and on Y_r, and ‖[M_r(1),h]X‖_{Y_r} ≤ (C_88/M)‖X‖_{X_r}." In A.5 at 1689, name the torus room t_F. In §10 at 1193, add "on a box with the room of the flat inverse lemma".

**D2. Wrong CMP 95 proposition (out-pi 664, 1290, 1379).** The three places attribute the energy bound (1.89)–(1.90) to Proposition 1.2. In CMP 95, (1.89)–(1.90) belong to Proposition 1.1 (OCR page 17, journal p. 33); Proposition 1.2 (p. 35) is the decay and Hölder package, which Appendix A does not use. flat-port 77 and 284 and flat-port-gate 45 say Proposition 1.1. Breaks: a citation only. *Corrected text:* 664 "CMP 95, Proposition 1.1, (1.89)–(1.90)"; 1290 "CMP 95 (1984), pp. 17–40, Proposition 1.1, (1.89)–(1.90)"; 1379 "This rebuilds the energy argument of Balaban, CMP 95 p. 33, Proposition 1.1, (1.89)–(1.90)."

**D3. New sentence on the background domain (out-pi 111).** "The local-gauge hypothesis below supplies the background and its gauge representation on every local read where it is invoked." r2 has no such sentence. r2 225 puts U on the bonds of Ω_0^+, and §3.4 of out-pi (272–273), with the gate's repair (gate 23), compares settings on that common domain. Read literally, the sentence lets (S1-loc) supply U off Ω_0^+, since N(x) reaches 7M_tη past the boundary at level 0; then two settings could differ on reads that §9 does not compare. The proof needs no such reads: every read lies in Ω_0^+. *Corrected text:* replace 111 by "Read (S1-loc) below on the bonds of N(x) in this domain. Every coefficient read lies there: field bonds touch Ω_0, plaquettes through them stay within 2η of Ω_0, and a row of level j ≥ 1 reads only bonds inside Ω_0." At 137 write "on its bonds in Ω_0^+".

**D4. Provenance of Appendix A and of the page images (out-pi 48–52).**
- The paragraph says who wrote and checked the main proof. It does not say that the flat argument was written by Codex (flat-port line 2) and checked line by line by Claude (flat-port-gate 6–8), or that this version was checked here.
- The CMP 95 p. 18 and CMP 96 p. 231 displays had one reader. The checking model could not see those pages (gate 17). The lead's pending edit may already cover this.
- "outward version" (51) is our process word.
- *Corrected text for 48–51:* "Balaban's displays were read from page images of the journal pages: CMP 99b and CMP 98 by Codex and Claude; CMP 95 p. 18, (1.6)–(1.7), and CMP 96 p. 231, (2.46), by Claude only. **Who wrote and checked.** The main proof was written by Claude (Opus 5.5) and checked line by line by Codex (gpt-6-astra); the repairs from that check are applied. The flat argument of Appendix A was written by Codex and checked line by line by Claude. Codex prepared this text from those two; Claude checked it line by line against them." Adjust the first sentence to what the lead actually read.

**D5. The CA-II quotation is not exact (out-pi 43).** CA-II 54617–54619 reads: "For $y$, $y'$ in one layer $\Lambda_{j}$ the exponential factor in the bound of \cite[(3.132)--(3.133)]{B-CMP99b} for $C_{Q}$ does not depend on $d(y,y')$;". out-pi renders the citation as "[CMP 99b, (3.132)–(3.133)]" and ends with a full stop. The words are otherwise exact, and the line numbers are right. *Corrected text:* quote the source verbatim, ending "…does not depend on $d(y,y')$; …", or keep the rendering and add "(citation key rendered)". This is on the lead's pending list.

**D6. Citation of (3.8) (out-pi 167).** "This is Balaban's covariant difference, CMP 99b p. 391, (3.8)." By the OCR, (3.8) is printed on p. 392 and displays the adjoint D^*. The covariant derivatives are introduced on p. 391. r2 227 attributes (3.8) to the transpose. *Corrected text:* "This is Balaban's covariant difference, CMP 99b pp. 391–392; its adjoint is his (3.8)."

**D7. Wording (breaks nothing).**
- (a) (S1-loc), 139–143: z is not defined. r2 203 has "at every point z of N(x)". *Corrected text:* add "at both endpoints z of each bond of N(x)". Lemma 5.2 uses the bound at the larger endpoint scale, and Proposition 3.1 proves it at every z ∈ N(x).
- (b) §5.2, 815: "Its read set X_τ contains its field bonds, …". r2 742 has "consists of the bonds read by their coefficients". The bound on X_τ needs "consists of".
- (c) A.3, 1522–1525: the face argument does not say how bonds with neither endpoint in a marked block enter (A.16). flat-port 445 does: "Internal unmarked bonds are already controlled by the bare part of M_U". *Corrected text:* add "Bonds with neither endpoint marked are retained bare bonds; there B_ax = B, and their squared norm is part of M_U(B)."
- (d) The constant name C_88 (234, 250, 647, 660, 930–936, 1696) is a residue of flat-port's label (8.8). For a reader outside the repository, rename it, e.g. C_com.

**D8. Shared gap, not a mismatch: Proposition 3.3's appeal to Theorem PI (out-pi 344 and 1223–1224; r2 393–395).** The last inference applies Theorem PI. PI also asks for a box of side at least (2r̂+2)ℓ_k, which Proposition 3.3 does not assume. *Corrected text:* "If T_η has side at least (2r̂+2)ℓ_k, then by Theorem PI, (S1-loc) with a_0 ≤ a_0^* must fail at a site whose box contains that bond." The singularity of Δ_a itself is unaffected.

## Appendix A: steps with no counterpart in a checked text (NEW), with a proof check

- **N1. Proof of (A.4), 1338–1344.** flat-port 136–139 averages coordinate paths. out-pi uses the variance identity Σ_x|u_x−ū|² = (2n)^{-1}Σ_{x,y}|u_x−u_y|² on a line of n sites. Check: |u_x−u_y|² ≤ n Σ_{e∈[x,y]}|δu_e|², and an edge lies in at most n² ordered pairs, so Σ_x|u_x−ū|² ≤ (n²/2)Σ_e|δu_e|². Write u − Av u = (u−E_1u) + E_1(u−E_2u) + E_1E_2(u−E_3u) + E_1E_2E_3(u−E_4u). Each E_i is an orthogonal projection, so the triangle inequality gives ‖u−Av u‖ ≤ (n/√2)Σ_i‖δ_iu‖ ≤ √2·n‖δu‖. With δu = ηDu and nη = s, (A.4) holds with C = √2. **Correct.**
- **N2. Small pillars, 1359–1360.** The added reason "each second-difference stencil has at most four entries" is right: for the central point field n⁴δ, with n < 33, |D_αD_βF| ≤ 4n⁴η^{-2} = 4n⁶s^{-2} < 4·33⁶s^{-2}. **Correct.**
- **N3. Bare model of M_5, 1603–1611.** Here T = C^TC + η^{-2}I with η^{-2} ≤ T ≤ Cη^{-2}, K = ηI and K^T = η^{-3}I (counting against η⁴ pairing). So ⟨ν,Γν⟩_count is comparable to Σ|ν|². This agrees with flat-port 664 (T_b = b/η). **Correct.**
- **N4. 1600.** "The block factorization in Lemma 7.1 is a finite algebraic identity; it does not require the main inverse theorem." The LDU factorization needs only an invertible lower-right block. **Correct.**
- **N5. 1639.** "If a whole periodic component is itself used as the local model, the same periodic estimates apply." (A.11), (A.18) and (A.20) hold on every periodic box, uniformly in its size. **Correct**, but it does not replace the torus room (D1).
- **N6. 1618.** Only the bare exterior tiles needed for initial points of crossing field bonds are included, where flat-port 544 tiles the whole exterior. Cutoffs are read only at active reference points, and these tiles cover every exterior initial point (§5.2). **Correct.**
- **N7. New attributions in A.1, A.4, A.5** (CMP 98 (124)–(125) at 1303; CMP 96 (2.17) and CMP 99b pp. 398–399, (3.48)–(3.49) at 1375; CMP 99b p. 394, (3.25) at 1578; CMP 96 pp. 247–248, (2.141), Proposition 2.6 at 1615). They agree with r2 Lemma 4.4(iii), the gate §1 and the OCR page markers ((3.48) p. 398, (3.49) p. 399, (3.25) p. 394, (2.141) and Proposition 2.6 p. 247). **Consistent.**

## Other additions to the main text, checked

- New Balaban page numbers, placed by the OCR page markers: CMP 95 (1.6)–(1.7) p. 18; CMP 96 (2.46) p. 231, (2.123)–(2.128) pp. 244–245, Lemma 2.4 p. 245, Proposition 2.5 p. 246, (2.141) p. 247, (2.152)–(2.157) pp. 249–250; CMP 99b (3.10) p. 392, (3.21)–(3.27) pp. 394–395, (3.35) p. 396, (3.42)–(3.47) pp. 397–398, (3.87) p. 409, (3.93) p. 410, (3.98) p. 413, (3.108) p. 416, (3.130) p. 421, (3.132) p. 422. All agree with out-pi.md, except (3.8) (D6).
- Account lines re-read at 31a47c543775: CA-I 12949–12957 and 12953–12955 ((S1), the size number 12), 12968–12973 (plaquette bound 4(a_0+a_1)η²ℓ_j^{-2}), 12738–12748 (the norm N, read as out-pi 122–127 states it), 13142–13173 (the remark), 13150–13152 (G_0 is "the Green's operator of this chapter at vanishing current J, which is the operator G of [CMP 99b §3]", that is the bare operator), 5126–5130 (footprints are closures of open sets with connected interior), 15276–15464 (cites CMP 116 (1.6), (1.7), (1.11), (1.12)–(1.18), as out-pi 1260 says), CA-II 54617–54619 (D5). All as stated, apart from D5.
- r2 material left out of out-pi.md, harmlessly: §0 and §§12–13 (history and status), "What r1 got wrong" in §9, and the §3.7 remark on the symmetric rows. §4's opening keeps the distinction from the symmetric rows in one sentence.

## Internal names and credit

- No row number, lane, gate, registry, BP07, [F], file path or internal label occurs in out-pi.md. Two residues remain: "outward version" (51; D4) and the constant name C_88 (D7(d)). The labels 4.5:rem-covariance-inverse-walks, J3, J4, J8, K3, K10 and C1 are the account's own.
- No sentence credits Ethan Sussman and Levent Alpoge for their own work. The note addresses them as "you" and credits Balaban for his constructions.

## What this check does not do

It is not a new proof review. It does not re-check r2's mathematics beyond the comparison, and it does not re-read Balaban's displays from page images. The torus coverage in D1 and the repair in D8 are stated, not proved here.

RESULT: out-pi.md is faithful to the checked print-inverse-r2.md, pi-r2-gate.md and flat-port.md in every statement, constant, hypothesis and proof step of Theorem PI, Propositions 3.1–3.3, Lemmas 4.1–7.1, §§8–11 and Appendix A; first failing step in the main proof: none. Eight defects with corrected text: D1, the flat inverse lemma's statement overreaches (cutoff clause not tied to the local scale, false if read literally; torus room omitted), uses unaffected; D2, CMP 95 Proposition 1.2 should be 1.1 (three places); D3, a new background-domain sentence at line 111 conflicts with §3.4; D4–D7, provenance, the CA-II quotation, the (3.8) citation and wording; D8, a gap shared with r2 (Proposition 3.3 needs PI's box floor). Seven NEW Appendix A steps checked, all correct. Open: whether PI's floor (2r̂+2)ℓ_k covers the flat lemma's torus room in the global use in §10.

Checked line by line by Claude (Opus 5.5).
