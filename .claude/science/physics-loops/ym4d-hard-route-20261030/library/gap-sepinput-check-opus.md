lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T19:04Z

# Check of row 996 (`library/gap-sepinput-max.md`), queue row 997

Row 997, `gap-sepinput-check-opus`. Checker: Claude Opus 5.5 max, Mac mini worker 3. Pinned at commit 011ea3c56 on `claude/ym4d-hard-route`. The note under check was written by Claude Fable 5.2 (row 996). This is a same-provider check (Anthropic model, different model), not an independent check in the sense of the working rules; a gpt-6-astra check is held.

Scope (row 997): check line by line 5.1 (Identity MIX, v = 8 beta_A/3), 5.2 and 5.3 (Proposition TILT and its corollaries; Brascamp-Lieb with hypotheses; non-compact domain with F smooth), 5.5 (Lemma SHEET: Haar-preserving change of variables on the open tube, m at most n - 2), Proposition MF, 6.3 (Proposition ELL), 6.4 (Proposition 4F: interval J and second derivative). Verdicts: HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.

## Plan (one step per response, appended here as it finishes)

1. Read the note in full and the K7 definition it reads (`library/gap-constraints-max.md` L73, `library/gap-mid-max.md`). Record the exact statements under check with line numbers.
2. Check 5.1, Identity MIX, including the variance v = 8 beta_A/3 and the sign and normalisation conventions.
3. Check 5.2 and 5.3, Proposition TILT and Corollary LIP and any other corollary; state Brascamp-Lieb with its hypotheses; decide whether a non-compact domain with F smooth meets them.
4. Check 5.5, Lemma SHEET: the frozen tube, the Haar-preserving change of variables on the open tube, the count m at most n - 2, the bound R_Lambda(0) at most 4/(n-1).
5. Check Proposition MF.
6. Check 6.3, Proposition ELL.
7. Check 6.4, Proposition 4F: the interval J and the second derivative.
8. Verdict table and RESULT line.

## Step results

(Appended below as each step finishes.)

### Step 1 (07:20Z): what is under check

Read in full: `library/gap-sepinput-max.md` (571 lines, file as at 011ea3c56). Read for the K7 definition: `gap-mid-max.md` L48 (one-plaquette weight exp(beta_F x + beta_A (4 x^2 - 1)/3), x = (1/2) tr U_p) and `gap-constraints-max.md` L73. The Sussman-Alpoge account is not read: no item under check cites it.

Items and lines (all line numbers are in `gap-sepinput-max.md`):

| Item | Lines | Claim |
|---|---|---|
| 5.0 setting | L256-267 | mu_(b,v) proportional to exp(sum_p (b_p x_p + (v/2) x_p^2)) dU; C = Hess_b F; Sigma^2(v) = sup_b lambda_max C(b,v); R = 1/Sigma^2; 0 < Sigma^2 <= abs(P) |
| 5.1 Identity MIX | L269-290 | (a) Z(b,v+w) = int gamma_w(ds) Z(b+s,v); (b) mixture law, s = w x(U) + sqrt(w) xi; (c) hidden-field density exp(-H), Hess H = 1/w - C(b+s,v); K7 = mu_(beta_F 1, 8 beta_A/3); heat equation; Remark MIX |
| 5.2 Proposition TILT | L292-305 | w Sigma^2(v) < 1 gives C(b,v+w) <= Sigma^2(v)/(1 - w Sigma^2(v)) and R(v+w) >= R(v) - w; uses Brascamp-Lieb |
| 5.3 Corollaries | L307-336 | LIP; K7-A; K7-B; Reading; Remark POL (marked ARGUED) |
| 5.5 Lemma SHEET | L358-390 | frozen side plaquettes of an open tube; Cov(x_(p_i), x_(p_j)) -> 1/4; Sigma^2_Lambda(0) >= (n-1)/4; consequence for TILT |
| Proposition MF | L392-402 | one global Gaussian shift; Var(E)/abs(P) <= X/(1 - w X); converse; "the same statement as" |
| 6.3 Proposition ELL | L419-428 | (Re g_1, Re g_2, Re g_1 g_2) uniform on the elliptope E_3, density 2/pi^2 |
| 6.4 Proposition 4F | L430-445 | rho_4 = (2/pi^3) abs(J); J; rho_4 not log-concave at theta = (0.5, 0.4, 0.4, 0.4) |

Method: each step is redone by hand from the definitions. No numeric run is used for any verdict. The GUIDE controls of the note (5.4, 5.5 remark 3, 6.4 control, 6.5) are not checked and carry no weight here.
