lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T11:55Z

# gap-cr-tomboulis-max (queue row 1025): the decimation line against Theorem CR and the vortex containers

Worker result file, research-stage working state. It grants no status and is no public claim. Pinned at commit
fe79776a6 of `claude/ym4d-hard-route`. Started 2026-11-15T23:55Z (`date -u`). Marks used: PROVED, ARGUED, OPEN,
FAILS. Nothing here is checked by a second reader yet.

Credit, by name, for everything this row builds on: E. T. Tomboulis (the decimation / vortex-free-energy argument,
arXiv:0707.2179 and the 2008-2009 follow-ups); T. Kanazawa (the comparison form of the same line); K. R. Ito and
E. Seiler (arXiv:0711.4930, the two obligations); G. Mack and V. B. Petkova (vortex containers and the 't Hooft
loop bound); N. Sussman and L. Alpoge (the complete account this lane ports). The lane's own rows used are named
where used.

## 0. Plan (at most eight steps; one step per response; each appended before the next)

1. Read `parts/gap.md`, the exercise skill (main 8b11ae2bb9), and the five named inputs with their checks. Log
   one line per source below as it is read.
2. Question (1): write Ito and Seiler's two obligations and the 2008 repair's trapping-domain / endpoint-bracket
   statement exactly, in the lane's notation.
3. Registry grep before any attack: `library/open-core.md`, FINISH rows, the idea digests. Name every match.
4. Question (4) first, as the row orders: run the tests (Lemma PT, Proposition NP, Theorem D2, Lemma SHEET,
   compact U(1), frozen Q_8 and 2T, the five-dimensional test) against the combination before building on it.
5. Question (2): does the compactness of Theorem CR / Proposition OM supply the common interpolation parameter
   or the trapping domain; test against Proposition SI.
6. Question (3): does (K-RESP) follow from Lemma PAR and Corollary MP on vortex containers, or reduce to (SER)
   and (SPR).
7. The first surviving piece: prove it by hand or build the counterexample.
8. Re-read of every PROVED item, verdict table, RESULT line.

## Status log (times from `date -u`)

- 23:55Z file created; GOAL.md and queue row 1025 read.
- 23:56Z read in full: `parts/gap.md`; exercise skill and `proof-search-governance.md` (main 8b11ae2bb9, fetched to
  /tmp/row1025-skill); `library/gap-tomboulis-read.md` (row 797, gpt-6-astra). Notes from row 797 kept for Step 2:
  T = Tomboulis 0707.2179; Z^+ = (Z + Z^-)/2; upper bound (3.1)-(3.4) Z_(m-1) <= (F_0^U)^(N_m) Z_m(c^U(r));
  interpolation alpha(t, r) per partition function (3.12)-(3.24); A = (N_m log F_0^U)^(-1) d/dalpha log Z_m,
  alpha_t = - h_t/(h_alpha + A); the disputed step is Appendix C (C.8)-(C.10): one t_* with
  alpha(t_*) = alpha^+(t_*); row 797 2.1: Psi(1, t) = 0 is exactly Z_c^+(alpha(t))/Z_c(alpha(t)) = Z_f^+/Z_f,
  and Psi_t = h_t (A - lambda A^+)/(h_alpha + A); Kanazawa v3 Theorem 4 (bounding flow reaches the small-coefficient
  basin for connected groups, U(1) included, b large, r = 1 - b^-2); Kanazawa v3 Theorem 1 (mismatched ratio,
  |alpha_Lambda - alpha| <= C/|Lambda_c|); 2008 repair = PoS Confinement8 020, (4.5)-(4.6) r_m adaptive,
  (4.9)-(4.11) Meyer's monotone iteration needing F(x_0) < 0, entrywise non-negative inverse, a bounded invariant
  domain with a boundary sign.
- 23:56Z read in full: `library/gap-tomboulis-check-opus.md` (row 799) and `library/gap-kanazawa-astra.md` (row 800).
  Kept for Step 2: check 799 B2: by the intermediate value theorem Psi(1, .) has a zero iff the fine ratio
  Z_f^+/Z_f lies in the range of alpha -> Z_c^+(alpha)/Z_c(alpha) over the alpha values the level curve reaches,
  "Appendix C therefore needs an endpoint bracket of the fine ratio by coarse ratios", which is T (5.23); check 799
  B5: the 2008 sign condition (ii) is met after t -> -t, "the substantive unproved hypotheses of the 2008 repair
  are (i) and the bounded invariant domain with a boundary sign, which amount to the endpoint bracket of B2".
  Row 800: (K1)-(K8) exact (D = log Q_c(alpha) - log Q_f; D = int_0^beta G_f - int_0^alpha G_c; G = -d/ds log Q;
  (K6) G_f = (2<WY> - Cov(W, H_m))/(1 + R)); (K17) inverse branch trapped in J for EVERY q in [1/2, 1] (so the
  mismatched representation encodes any ratio); (K-RESP) = [int_0^beta G_f ds - int_0^alpha G_c du]_+ <=
  (1/8) min{1/96, K(a) eta_*^(a/2)/4}, i.e. by (K21) up to 2N e^(-l^2): H_f = -log((1 + R_f)/2) small at the scale
  of the consumer (FQ) (or area-small for (V)).
- 23:56Z read: `library/gap-compact-rigidity-max.md` (row 1017) Sections 1-6 in full (L1-403). Kept for Steps 4-5:
  datum (E1)-(E3), eternal datum, admissible sequence (H1), (H2), critical element (3.1); Theorem CE (limit keeps the
  spectral form in four directions, the engine's non-strict finite inequalities, the centre grading (e); loses the
  ultraviolet data, the group, the action); Proposition OM (Omega compact, sigma a homeomorphism; stall (c),
  recurrence (d), monotone gives stationarity (e)); Theorem CR ((W) iff Omega empty iff no uniformly recurrent
  element iff for one continuous Lambda no element has Lambda(sigma E) >= Lambda(E), GIVEN (BDD-Delta)); Lemma
  PT-inf (the blow-down forgets every seeded factor); Proposition NR (constants log m are critical elements);
  Proposition SI (a kept property is sigma-invariant: no condition at one end of the scale axis is kept); Remark
  MON (a non-increasing continuous Lambda passes the ultraviolet data as one inequality Lambda(E) <= Lambda_UV).
- 23:56Z read: row 1017 Sections 7-8; check `library/gap-compact-rigidity-check-opus.md` (row 1019) Steps 6-8 and RESULT
  (L145-256; Steps 1-5 not read: they re-derive UF, CE, OM line by line). Repairs that bind this row: D2 (Omega =
  Omega(D_0) with D_0 a (BDD-Delta) bound), D4 ("no element of Omega(D_0)", not "no critical element"), D14 (SI
  says nothing on asymptotic conditions as b -> 0; what keeps the ultraviolet growth out of Omega is CE (d)), and
  6.5 (i): "by compactness a strict decrease on every element of Omega is automatically uniform".
- 23:57Z read: `library/gap-short-step-max.md` (row 1018) Sections 2-3, 5.2-5.3, 6.2, 7 (L70-212, L289-305, L389-443);
  not read: Sections 4, 5.1, 5.4-5.6, 6.1 (route (ii), Lemma NAB, the control run), which this row does not use.
  Check `library/gap-short-step-check-opus.md` (row 1022): headings and RESULT only (no WRONG; Lemma PAR (i)-(iii)
  and Corollary MP confirmed, MP against Mack and Petkova's (2.16), (2.19)-(2.21)). Kept for Step 6: Lemma PAR
  setting (sub-containers Lam_i with disjoint plaquette sets, twist system (H1), (H2), rho = Z(sigma Om)/Z(Om),
  r_i, a_i = tanh(v_i/2)); (i) E[prod_S r_i] = rho or 1 by parity of |S|; (ii) Etilde[a_1 ... a_n] = tanh(V/2), all
  proper sub-products vanish; (iii) |tanh(V/2)| <= prod_i tanh(xi_i/2); Corollary MP: E[O] = Etilde[O a_1 ... a_n]
  for O odd under each tau_i; (T-vor) open half O2: (SER) xi(Sigma_2l, D) <= kappa xi(Sigma_l, D), (SPR)
  xi(Sigma, D_2l) <= phi xi(Sigma, D_l), kappa phi < 1; Lemma PAR holds verbatim in frozen Z_2, Q_8, 2T and in five
  dimensions.
- 00:09Z primary sources fetched once into /tmp/row1025-lit (one folder each; PyMuPDF text; nothing executed) and read at
  the pages named in 1.2: Tomboulis 0707.2179v1; Ito and Seiler 0711.4930v1 (in full), 0803.3019v1; PoS
  Confinement8 020. Step 1 done. Step 2 next.

## 1. Step 1 result: what was read, what is pinned

### 1.1 Header in the form the exercise skill asks

Writer: Claude Fable 5.2 (Anthropic), max effort, Mac mini worker 1, one session, no subagents. Commit fe79776a6.
Date 2026-11-15/16. **Nothing in this file is checked by another model.** This is a standalone proof target, so
`GOAL.md` and the FINISH rules replace the skill's framework refresher read (the skill allows this and asks that
it is said). The row's brief names the files to read first, so the skill's "closed list" is empty here: the brief
wins. The wall has had five exercises (rows 878, 998, 1003, 1011, 1017); by skill step 0 their inventory,
assumption tables and set-aside lists are reused, not rewritten. This row runs the skill on one combination.

What this run did not cover is listed in Section 9.4.

### 1.2 Sources, with how each was read

| Source | Read | Used for |
|---|---|---|
| `parts/gap.md` (lead, 2026-11-15) | in full | the wall (W), lead rule W2, test table, registry |
| `library/gap-tomboulis-read.md` (row 797, gpt-6-astra) | in full | the reading of Tomboulis, Kanazawa, Ito and Seiler |
| `library/gap-tomboulis-check-opus.md` (row 799) | in full | B2 (bracket form), B5 (the 2008 sign is a convention) |
| `library/gap-kanazawa-astra.md` (row 800, gpt-6-astra) | in full | (K1)-(K8), (K17), (K21), (K-RESP) |
| `library/gap-compact-rigidity-max.md` (row 1017) | L1-480 | Theorems CE, CR, Propositions OM, NR, SI, Lemma PT-inf |
| `library/gap-compact-rigidity-check-opus.md` (row 1019) | L145-256 (Steps 6-8, RESULT) | repairs D2, D4, D14 |
| `library/gap-short-step-max.md` (row 1018) | L70-212, L289-305, L389-443 | Lemma PAR, Corollary MP, (T-vor), (SER), (SPR) |
| `library/gap-short-step-check-opus.md` (row 1022) | headings and RESULT | no WRONG on PAR, MP |
| E. T. Tomboulis, arXiv:0707.2179v1 | pp. 7-8, 10, 12-14, 24-28, 43-46 (text layer) | (2.18)-(2.22), (3.12)-(3.29), (5.1)-(5.24), Appendix C |
| K. R. Ito and E. Seiler, arXiv:0711.4930v1 | in full (10 pp.) | Claim 2.1, Theorem 2.1 (flow at r = 1), (3.1)-(3.11) |
| K. R. Ito and E. Seiler, arXiv:0803.3019v1 | pp. 6-7, 12-16 | Theorem 2.2, Problems 1-3, Section 3.3 |
| E. T. Tomboulis, PoS(Confinement8)020 | pp. 6-9 | (4.2)-(4.13), the 2008 repair |
| T. Kanazawa, arXiv:0805.2742v3 | fetched; not re-read (rows 797, 799, 800 read it) | - |
| G. Mack and V. B. Petkova, Ann. Phys. 125 (1980) 117 | not fetched; as rebuilt in row 1018 7.4 and confirmed by check 1022 | Corollary MP |
| Sussman and Alpoge's account (with Claude and Codex as authors of their text) | not opened in this row: rows 797 and 800 searched its index for Tomboulis, Migdal-Kadanoff, Kanazawa and found no entry | - |

