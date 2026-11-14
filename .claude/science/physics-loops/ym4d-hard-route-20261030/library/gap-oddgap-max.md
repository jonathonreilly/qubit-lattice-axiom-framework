lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:17Z

# gap-oddgap-max (FINISH row 930): the odd-gap form of the flux half

Worker: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit edc2c18b3 on
`claude/ym4d-hard-route`. Author item. No commit, no push (relay copies this file).
Research-stage working state; nothing here is a public claim.

Status labels used below: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric or heuristic,
carries no proof weight), OPEN.

## Plan (at most eight steps; one step per response; each appended before the next)

1. **Read the inputs in full**: row 922 `library/gap-fr-opus.md`, its check row 927
   `library/gap-fr-check-astra.md`, rows 899/901 (VAR-SLAB), and Step A of row 929
   `library/gap-seam-max.md` if present. Grep `library/open-core.md` and the FINISH rows for
   the lemma names before any attack. Record the exact statements used (p, R, FR, lambda_odd,
   ODD-0, the ceilings 2/3, 0.775, 4G_3 = 1.0109).
2. **STEP A, U(1) fact test, exact**: Gaussian U(1) (Villain or noncompact) on the same box and
   time extent, pi twist in place of the centre twist. Compute p, FR and lambda_odd in closed
   form and say which factor of `p <= FR/(2 lambda_odd)` carries the U(1) failure.
3. **STEP A, frozen groups**: the same three quantities for frozen Q_8 and 2T at the level of
   a sound estimate (a domain wall should cost nothing).
4. **Verdict of Step A**: either name the failing factor, or declare the odd-gap form the wrong
   target and give the form that does fail for U(1).
5. **STEP B, statement**: the exact SU(2) Wilson statement to attack (beta about 2.3-2.6, the
   size the flux half needs), with the property U(1) lacks written into the hypothesis.
6. **STEP B, attack 1** on the failing factor, as a real proof; mark the step where the photon
   breaks it.
7. **STEP B, attack 2 or repair**, and consistency with the ceilings 2/3, 0.775, 4G_3 = 1.0109.
8. **Result table and RESULT line**: every statement marked PROVED / CONDITIONAL / GUIDE / OPEN,
   what failed, what is left.

## Log

- 2026-11-14T04:17Z: file created; reading inputs (step 1).
