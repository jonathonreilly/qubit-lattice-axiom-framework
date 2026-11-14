lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T01:57Z

# gap-avgcurv-max (row 968): averaged curvature against (LSI-J-seed)

Author: Claude Fable 5.2 (max), Mac mini worker, pinned at commit 4a2be4ba1. Started 2026-11-14T13:57Z.
Research-stage working state. Nothing here is a public claim. No statement below rests on a run; runs are labelled GUIDE.

## 0. Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Inputs and duplicate check.** Read rows 941, 947, 957, 958, 960 and `library/prior/gap-lit-bridge-lsi.md`.
   Grep `library/open-core.md` and the FINISH rows (rule 0a). Restate (LSI-J-seed) exactly, with the box and constants.
2. **Sources.** Bauerschmidt-Bodineau-Dagallier 2024 (Polchinski flow, Theorem 3.6), Chen-Eldan localization schemes.
   For each: the exact hypothesis, and whether it is an average or a supremum for J.
3. **Fact tests of the candidate criteria.** Compact U(1) Coulomb phase, frozen Q_8 / 2T, SMALL-BOX, K7, FT-FK.
4. **Attack 1.** Integrated or averaged Bakry-Emery criterion applied to J.
5. **Attack 2.** Ricci curvature of SU(2) against the averaged negative part of the Wilson Hessian
   (exponential-family form of log Omega, Brownian-bridge structure of Theorem BR).
6. **Attack 3.** Splitting: the large negative eigenvalues on a set of small J-measure (RARE-P).
7. **If not closed.** The smallest unproved averaged-curvature inequality and one GUIDE test that could refute it.
8. **Status table and RESULT line.**

Status log (UTC times read from `date -u`):

- 13:57 file created; reading inputs.
- 14:10 inputs read: FINISH rows 941, 947, 954, 957, 958, 960, 968; `gap-fc-max.md` L39-282, L487-586; `gap-lsivac-max.md` L84-222;
  `gap-ps-disint-max.md` L46-95, L163-180, L371-486; check 958 finding 5; `prior/gap-lit-bridge-lsi.md` in full;
  `prior/gap-fullread-2.md` Section 3 (BBD Theorem 3.6 digest). Duplicate check done (Section 1.3).

## 1. Inputs, target, duplicate check (READ; no new claim)

**1.1 Objects (rows 941, 947, 957; quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L in R^N,
N = 4L. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) (temporal gauge). Omega its top
eigenfunction, nu = Omega^2 dx, m(dw) = e^(-V(w)/2) Omega(w) dw. Lambda(theta) = log integral of e^(<theta, w>) m(dw) on R^N,
pi_theta(dw) = e^(<theta, w> - Lambda(theta)) m(dw); the one-step law is pi_(beta x); Hess Lambda(theta) = Cov_(pi_theta)(w)
(row 941 (A2)). J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z is the two-slice vacuum law. Elitzur (row 941 (A5)):
Cov_m(w) = Id/4. The bridge marginal (row 947 (B1)-(B4)): nu_s = law of y = (1 - lam) x + lam w + (lam (1 - lam)/beta)^(1/2) xi,
lam = beta s, s' = 1/beta - s, with density h_s h_(s')/Z on R^N, h_s = g_s * m.

**1.2 Target.** (LSI-J)_(alpha_J): Ent_J(Phi^2) <= (2/alpha_J) E_J[|grad_x Phi|^2 + |grad_w Phi|^2] for gauge-invariant Phi.
(LSI-J-seed)_a: alpha_J >= 2 beta K_a on one box, K_a = (C_beta + 3 log a)/(a - 2). Row 960 (unchecked): on the box
(a; (4a)^3), C_beta = 12.51 at beta 2.3 and 12.63 at 2.6, so K_30 = 0.811, K_40 = 0.621, K_60 = 0.427. Row 954
(Lemma GAP-R, conditional): the route needs m_G >= K_a. Theorem BR and Corollary BR-J (row 947; HOLD by check 949)
turn (LSI-J-seed)_a, or the weaker (LSI-br-seed)_a: (1/2) integral over (0, 1/beta) of alpha_s ds >= K_a (alpha_s the
gauge-invariant log-Sobolev constant of nu_s), into (HC-vac)_(K_a) and the seed. Row 957 (T1): any bound with
b alpha_J(b)/log b -> infinity along box sides b gives the seed for some a.

**1.3 Duplicate check (rule 0a).** `grep -n -i -E "LSI-J|polchinski|stochastic locali|localization scheme|chen-eldan|eldan|averaged curv|integrated bakry|DEF-ABS|entropic stab|bakry"`
on `library/open-core.md`, `library/l17c.md`, `library/open-registry.md`: no hit. FINISH rows: Polchinski 689, 690, 813,
915 (reading rows; 689: Bauerschmidt-Bodineau Theorem 1.2 "needs a lower bound at every scale ... no gauge
application"), 719 (BBD Theorem 3.6 read; digest `prior/gap-fullread-2.md` Section 3); Eldan 689, 690, 787 (reading);
"averaged curvature" 958 (the check that left the route open) and 968 (this row); (DEF-ABS) 957, 958. No row attacks
an averaged-curvature or Polchinski-flow criterion for J. Row 941 has the one-scale forms (Theorem MID, (COV)_kbar,
three ceilings at beta 1, 2, 3/2). I proceed, and I do not re-attack (SG-step), (SC), (FC), (MAC).

**1.4 What check 958 left open, in its words (finding 5).** Sampling the top eigenvalue of Hess H tests only the
pointwise tensor criterion. An averaged inequality may keep the term E[f |Hess log f|^2], which can compensate a
negative tensor term. So "no averaged form exists" was not established by row 957.

**Credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the transfer frame
and temporal-gauge setting of the account. Rows 941, 947 (Claude Fable 5.2): exponential family, Theorem BR.
Bauerschmidt, Bodineau, Dagallier; Chen, Eldan; Piazza, Shen: named where used below.
