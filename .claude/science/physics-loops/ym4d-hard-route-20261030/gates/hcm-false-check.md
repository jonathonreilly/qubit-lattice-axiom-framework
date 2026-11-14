# Check of library/hcm-false.md (H-C-MARK, assignment 502)

Checker: Claude (Opus 5.5), one line-by-line reading, 2026-11-08.
Clone at `43f13c7ea` on `claude/ym4d-hard-route`.
Research text. Not an audit. Grants no status.

## Verdict: FIX

Section 2 is correct. Every cited source line says what the note uses.
The horizon bound (3) and the majorant lemma (4) are correct.
The arithmetic in (6) and (8)-(10) is correct.
The note is right that finding 9 does not prove the divergence.
It is also right that finding 9's "terminal level to infinity at fixed birth" is ill-posed.

Two things need repair.
First, the rejection of finding 9 puts the gap in the wrong place.
The conditional failure rate is not the open part.
At a fixed exterior it is deterministic (route 3 already uses this).
In the measure layer a standard small-amplitude shift bounds it (finding 7).
The open part is one normalization clause of RIM-LB (finding 8).
Second, the order of choice for the price c is reversed at note 210 and 217 (finding 6).

## Findings

**1. Note 56-71, (1). Y 72324-72338, Y 63876 / SA 17624. CONFIRMED.**
Y 72332-72334: the bare plaquette variable "is exactly the level-m plaquette variable of V_m".
Y 63876: adjacent to X^c the localized background is constrained bond by bond on the bare lattice.
So at fixed top rows the stage variables and the inner minimization cannot change (1).
Y 72335-72338: the first-member collar still leaves bare determining bonds. Correct.

**2. Note 73-81. Y 63862 = SA 17610, Y 78408-78435. CONFIRMED.**
Y 63862: a failure "can happen to the same component repeatedly"; the operation has no exception for a renewal.
Y 78429-78431: old reads lie in the floor; the preparation "modifies only higher layers".
So a renewed operation that reaches its final stage runs the same rim test. The note keeps the quiet-box condition. Correct.
"An operation which stops earlier never executes it" is correct and matters.

**3. Note 83-92. Y 72416-72419, Y 63876, SA 17624. CONFIRMED.**
Y 72416-72419: earlier stage tests read away from the outer joining collar.
Y 63876: "the carried tests provide only 2ε_k" against a demand Cε_kη_k² on the block field.
Y 72318-72322 says the same for the collar. No earlier passed test pays the rim. Finding 9 point (ii) holds.

**4. Note 94-148 (§2 end, §3). CONFIRMED, with finding 7.**
(2) is correct when the four top rows are fixed exterior data.
Y 63836: no frame sum for a component leaving during the stages. Y 63856: the reference law comes at (4). So note 124-126 is correct.
(3): IN1 (1) with i=h, j=K and θ_K ≥ X_0 gives λ(K-h) ≤ θ_h - X_0 + c_5. Correct.
This invalidates finding 9 line 79 ("F grows without bound in the terminal level while e^{B_h} is fixed"). Good catch.

**5. Note 150-185, (4). hc-mark.md (3a), (4). CONFIRMED.**
HCM-R requires H_ρ to dominate the complete integrands (hc-mark 165-166). So H_ρ ≥ |J_ρ| at a compatible evaluation.
w_ρ ≥ e^{(c+c_ent)ΔV}; the κ_1 factor is ≥ 1; terminal reward 1. Iteration of a+TF ≤ F over a finite horizon is valid.
Using |J_ρ| makes the lower bound easier, not harder. The lemma is uniform in H_ρ. Correct.

**6. Note 208-217, (5)-(6). in1.md row 7 (line 233), Theorem 10. MISMATCH (quantifier).**
(6) matches hc-mark (11). B_h ≥ (c+c_ent-C_*)v and B_h ≤ C_0P_h² contradict (6). Correct as an implication.
But the refuter does not choose c. IN1 row 7 fixes c = C_v c_r. A larger c only makes HCM-R harder.
A defender of HCM-R uses the smallest c that IN1 allows.
Finding 9 line 81 makes the same reversal ("c can be taken large").
Repair: state RIM-LB with C_* < c + c_ent for the c of IN1 row 7. Or state the conclusion "for every c > C_* - c_ent".
q_t at note 237 matches in1.md 518-522. CONFIRMED.

**7. Note 94-100, §5 route 1 (246-287). UNCLEAR: the rejection of finding 9 is right in its conclusion, overstated in its reason.**
Finding 9's "typical size g_m" is not an argument. The note is right there.
The mixture countermodel (273-283) is valid. It refutes the inference from support and energy only.
But a standard argument gives the conditional pass rate without any density bound or the scale g_m.
It uses quasi-invariance of the actual measure under a small shift, which the mixture lacks.

Sketch (measure layer, bare Wilson law ν_0 of SA 17499-17514).
Use Y's affine commuting field (Y 72340-72367) with top angle a, near the rim, away from the old core.
Left-multiply the bare links by exp(iη_m A). Haar measure is invariant, so the Jacobian is 1.
The quadratic action cost is Cθ_0a². Pair the shifts ±a; the linear term cancels in the sum, as in a spin-wave argument.
Take a in a grid of K³ points, spacing > 2τ_m, with Kτ_m ≤ ε_m/4. The images of the passing set are disjoint and fail.
Then the pass probability, given the other outcomes, is at most C/K³ plus a margin term.
The cost is uniform in absolute level: θ_0τ_m²K² ≤ (1+B̄m/θ_m)P_m²L^{-4m}·C → 0.
So the pass rate is O((τ_m/ε_m)³) = O(L^{-6m}), essentially (7).
Bare plaquettes move by O(aη_m²) ≪ every bare threshold. Lifted layers move by at most a ≪ ε_j.
Open in this sketch: a margin lemma. Configurations within Kτ_m of another test threshold must carry small mass relative to the passing set.
This is a fourth route. The note does not try it. Route 1's "first failed step" is not a real obstruction for the normalized rate.
Caveat: a shift at a = g_m would cost θ_0g_m², which is not uniform in absolute level. Only the small amplitude works.

**8. Note 360-405 (route 3), 117-126. CONFIRMED; this is the real open point.**
(12) is correct. A normalized estimate does not bound an unnormalized mass. Correct.
SA 18040-18042: Gaussian normalizers, gauge normalizers and elimination determinants stay in the integrand.
Y 77548-77549 (not cited by the note) helps: a stop at the prospective test has "no normalizer from the interrupted stage".
So the failed final stage adds no normalizer of its own. Only the waiting levels' factors remain.
Repair: narrow RIM-LB to RIM-N. The formula-layer prefix mass, per unit of IN1 volume, is at least e^{-C_*} times the measure-layer probability, with C_* < c + c_ent.
Together with finding 7 this would give (5). Name RIM-N as the first open input.
Also note: v carries the factor 1+log x per cell (in1.md 513). If the normalizer loss has no such factor, C_* is o(1) per unit v. Check this first.

**9. Note 289-358 (route 2), (8)-(11). CONFIRMED.**
(9): a_ℓ = 16e_*L^{2m_ℓ-4m_0}. (10) needs m_ℓ ≥ m_0, e_* ≥ ε_{m_ℓ}, a_ℓ ≤ a_* ≤ 1, and 8 > 3(1-β_s/2). All hold.
Common translation b sends a_* → 0 at fixed differences. Correct.
Y 77526-77552 does keep the old guards at a failed prospective test (Y 77529-77537). Correct citation.
The loss proportional to m_0 for a small ball (349-353) is plausible and stated as such.

**10. Distinctness of routes (§5). CONFIRMED.**
Conditional density, single field plus open ball, exterior supremum. They are distinct. Each fails where stated, as written.
They differ from the three payment routes of hc-mark.md. But see finding 7: a fourth route passes route 1's failed step.

**11. Scope (§6, table). CONFIRMED.**
The note claims no counterexample of its own. It credits Y 72340-72432 for the mismatch and the example.
It does not treat finding 10 as proved. It changes no test. No closure claimed.
Repair: the table row "Low energy, support, or conditional failure probability alone implies (5)" should say the countermodel refutes the support-and-energy inference only, not a quasi-invariance argument.

## Repairs

1. Note 94-100 and route 1: say the conditional pass rate follows from a small-amplitude shift (finding 7), modulo a margin lemma. Add it as route 4 or as the fix of route 1.
2. Rename the open input RIM-N: the formula-layer prefix mass against the measure-layer probability (finding 8). Cite Y 77548-77549.
3. Note 210 and 217: fix the order of c (finding 6).
4. Table row at 450: narrow as in finding 11.
