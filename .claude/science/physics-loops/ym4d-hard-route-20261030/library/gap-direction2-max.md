lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T03:45Z

# Row 970, gap-direction2-max: direction on the crux after row 968

Author: Claude Fable 5.2 (max), Mac mini worker, as AUTHOR (direction). Pinned at commit 61049a444.
Research-stage working state. Nothing here is checked by another model. Nothing here is a public claim.
Labels used: PROVED (written argument, not yet checked), CONDITIONAL (on named inputs), GUIDE (numeric, no proof weight), OPEN.

## Status log (newest last; times from `date -u`)

- 2026-11-14 15:45Z. File created. Plan below. No result yet.

## Plan (eight steps, one per response)

1. Inputs. Read rows 947, 954, 960, 965, 968 and `library/gap-status-1113.md`. Write the exact statements of
   (LSI-J-seed), (TILT-COV-sup), (LOC-COV) and what consumes them. Section 1.
2. Question (1), port or new input. Search the Sussman-Alpoge text (sa-index, outline copy) for small-field cluster
   bounds and one-block decay that would give (TILT-COV-sup) or (LOC-COV) at the seed scale. Quote lines. Section 2.
3. Question (2), circularity. Does (LOC-COV) on the seed box need the gap of a larger box? Proof or counterexample
   of the dependence. Section 3.
4. Question (3), ranking. At most three attacks, each with fact test and refutation test, cheapest first. Section 4.
5. Question (4), stage 1 of the top attack. Section 5.
6. Question (4), stage 2. Section 6.
7. Question (4), stage 3, or the refutation test if a stage fails. Section 7.
8. Summary table of verdicts, what stays open, RESULT line. Section 8.

## 1. Inputs, exact statements, duplicate check (READ; no new claim)

**1.1 Read.** FINISH rows 947, 954, 960, 965, 968 in full. `gap-avgcurv-max.md` (row 968) Sections 1-8 in full.
`gap-status-1113.md` Sections 1 and 6. Rows 969 (check of 968, HELD) and 971 (literature on the tilted covariance,
queued, no output at this commit).

**1.2 Objects (row 968, 1.1 and 3.1; quoted in short).** B is a periodic spatial box with L links. M = (S^3)^L in R^N,
N = 4L. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) in temporal gauge. Omega is its top
eigenfunction. m(dw) = e^(-V(w)/2) Omega(w) dw. pi_theta(dw) = e^(<theta, w> - Lambda(theta)) m(dw) for theta in R^N; the one-step law
of the vacuum chain is pi_(beta x). J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z is the two-slice vacuum law. For s in (0, 1/beta):
s' = 1/beta - s, c = s s'/(s + s'), q~ = x/s + w/s', and for 0 <= b <= beta, phi in R^N:
  J_(b,phi)(dx, dw) = e^(b <x, w> + <phi, q~>) m(dx) m(dw)/Z_b(phi).
At b = 0 this is the product pi_(phi/s) x pi_(phi/s').

**1.3 The three statements of the row.**
- (LSI-J-seed)_a (row 947): the log-Sobolev constant of J on gauge-invariant functions obeys alpha_J >= 2 beta K_a on
  one box, K_a = (C_beta + 3 log a)/(a - 2). On the box (a; (4a)^3) of row 960: K_30 = 0.811.
- (TILT-COV-sup) (row 968, 3.3): Var_(J_(b_t,phi))(<z, q~>) <= kbar_(s,t) |z|^2 for every phi in R^N and every z orthogonal to
  the gauge orbit of phi, with b_t = t/(s s'), 0 <= t <= c. A bound kbar that is uniform in the box gives the seed for
  some a (Theorem POL-BR, CONDITIONAL on BBD Theorem 3.6 and Theorem BR).
- (LOC-COV) (row 968, 6.3): K_s(y) >= diag_l(k_l(y)) on horizontal vectors, with k_l >= rho off a set Bad_l and
  k_l >= -D on it. Here K_s(y)(z, z) = |z|^2/c - Var_(pi_(y/s))(<z, x>)/s^2 - Var_(pi_(y/s'))(<z, w>)/s'^2. So (LOC-COV) is a bound
  of the covariance of the tilted law pi_theta by a diagonal form, at typical tilts with rare exceptions. With the
  capacity bound (CAP)_l it gives a gauge-invariant Poincare constant of nu_s.
Reading used below. m is the law of the boundary slice of the half-infinite cylinder B x {0, 1, 2, ...} (half
weight on the boundary plaquettes). pi_theta is that law with a linear field theta on the boundary links.

**1.4 Chain to the consumer (rows 931, 947, 960, 968).** (TILT-COV-sup) box-uniform -> (LSI-br)_s -> (HC-vac)_alpha ->
X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m) -> the seed on (a; (4a)^3) when alpha >= K_a -> Theorem S. Necessary sizes: m_G >= K_a (row
954), and kbar >= 2 beta log(1/E_1(B)) (Lemma NEC, row 968).

**1.5 Duplicate check (rule 0a).** `grep -n -i -E "TILT-COV|LOC-COV|ABS-flow"` on `open-core.md`, `l17c.md`,
`open-registry.md`: no hit. FINISH rows with a hit: 968 (source), 969 (its check, HELD), 970 (this row), 971
(literature, reading only). Library files with a hit: `gap-avgcurv-max.md` only. So no other row attacks
(TILT-COV-sup) or (LOC-COV). Row 971 reads the literature on them; this row does not repeat its search.
Prior GUIDE evidence that bears on the supremum form, found in the lane notes: rows 950 and 952 report that the
one-step law at a frozen pi-flux slice orders its colour direction near beta 2.4 to 2.5. Section 4 reads them.

**Credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the account, its
transfer frame and its renormalisation-group bounds, read in Section 2. Rows 931, 941, 947, 950, 952, 954, 960, 965,
968 (Claude Fable 5.2 and Claude Opus 5.5): the statements above. Bauerschmidt, Bodineau, Dagallier; Chen, Eldan:
the criteria behind Theorem POL-BR.

