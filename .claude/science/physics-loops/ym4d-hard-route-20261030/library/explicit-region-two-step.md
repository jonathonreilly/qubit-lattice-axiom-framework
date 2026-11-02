lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T12:16Z

# Explicit-region two-step test (queue item 32, `explicit-region`, neutral)

Pinned at `eda9debc5`. Status: in progress. Sections are appended as they are finished.

**Provenance.** Anthropic, claude-opus-5-5, effort max, one session, no subagents. Same-model research text, not an audit, and it grants no status. Labels: *discharged* (proof here, by hand), *implication* (proof here, given named inputs), *gap* (no proof), *memory* (recalled, not read and not proved). Dimock's papers were read in the open arXiv text; Balaban only through open abstracts. Nothing from either carries weight until rebuilt here.

## 0. Criteria, registered before the derivation

The question: on the two examples of `library/heavy-wall.md` and `library/seam-nlpay.md` (identity-parent pairs at a wall; locked pairs in frozen bricks), does an explicit large-field region price the fine energy that stops (HW) and (PATCH)?

- **R1, the region must be rare.** A region is priced only if its test marks the pack and is rare at typical fields. A test that fires at typical fields prices nothing. *Fail:* the test marks the pack only because it marks everything.
- **R2, retained data.** With the pack on the boundary of a retained region, every term of the conditional partition function must be bounded with no small l^2 energy on a patch larger than a block. *Fail:* a term that grows with the pack size M, other than the common classical term.
- **R3, no relative gauge.** *Fail:* a step that compares two independently given global fields, as (PATCH) does.
- **R4, column.** Sum the history cost at d = 4 on the flow x_j = x_K + b(K - j). *Fail:* a region that must persist to the top, with total cost above its own price.
- **R5, insertions.** Two separated insertions through two steps. *Fail:* a step that needs a generated current under a mixture law.
- **R6, mandatory examples.** The commutator square of `gates/energy-stages-codex-b87de884f.md` and the locked pair, for any new statement.
- **R7, sectors.** A retained boundary with nonzero winding. *Fail:* a comparison of values across sectors by a path.

A pass here is a two-step statement. It does not prove all-depth closure.

## 1. The heavy field is the typical field (R1)

Write A(U) = sum_p (1 - (1/2) tr U_p) and weight exp(-x A). This is the normalization of `parts/hard-core--mapped.md`: its slope c_0 = (11 N^2 / 12 pi^2) log L is the one-loop slope of x = 4/g^2 at N = 2.

**Lemma TYP (discharged).** *Let x >= 1. Let B be a set of links, no two in one plaquette. Given all links off B, with any values, the links of B are independent, and e_b := sum_(p containing b) (1 - (1/2) tr U_p) obeys 0 <= e_b <= 12 and E[e_b | rest] >= 1/(8x). Hence, with n = |B|, sum_b e_b <= A(B^+), the action of the plaquettes meeting B, and P(A(B^+) <= n/(16x) | rest) <= 9216 x^2 / n.*

*Proof.* Independence: no plaquette reads two links of B. Fix b. Its six plaquettes are U_b S_p with S_p in SU(2). A real sum of unit quaternions is a real multiple of a unit quaternion, so sum_p S_p = s R with 0 <= s <= 6, R in SU(2). Put u = (1/2) tr(U_b R). Then e_b = 6 - s u. Under Haar measure u has density (2/pi)(1 - u^2)^(1/2) on [-1, 1], so given the rest, w = 1 - u has density proportional to (w(2 - w))^(1/2) exp(-k w) on [0, 2], with k = x s.
Case k >= 1. On [0, 1/(2k)] the density is at most (2w)^(1/2), with integral 1/(3 k^(3/2)). On [1/(2k), 1/k] it is at least (2k)^(-1/2) e^-1, with integral at least 0.13 k^(-3/2). So P(w >= 1/(2k)) >= 0.13/(0.13 + 0.334) >= 1/4, and E w >= 1/(8k). Thus E[e_b | rest] >= s E w >= 1/(8x).
Case k < 1. Then s < 1/x <= 1 and e_b >= 5.
Each plaquette holds at most one link of B, which gives sum_b e_b <= A(B^+). Each e_b has variance at most 36, so Chebyshev at distance n/(16x) gives the tail. QED

Take the direction-1 links with base points in (2Z)^4 inside a level-j cell, side L^j, so n >= L^(4j)/16:

    fine action on a level-j cell >= L^(4j) / (256 x_0), with probability >= 1 - 147456 x_0^2 / L^(4j).        (1.1)

x_0 grows linearly in the depth K, and L^(4j) exponentially in j. So above j_* := log_(L^4)(10^7 x_0^2) = O(log K), **every level-j cell of a typical field carries fine energy above any fixed multiple of T^2.** The pair pack of (HW) with amplitude about x_0^(-1/2) and M about L^(4j) is the typical field, not a corner. The triggers of `library/energy-by-stages.md` (A_c(U) > kappa T^2, dense boxes) fire on typical fields at every level above j_*, and the hypothesis ||theta(U)||_P <= epsilon_0 of Lemma U fails there on the field being integrated. An excess over a minimal lift does no better: the lift of a class top has energy at most C T_2^2 on a cell, so the excess of a typical field is still of the size (1.1).

**R1, verdict on raw fine energy: FAIL.** No region defined by fine energy at a fixed threshold can be rare, so none can price that energy. Sections 3 to 5 show what replaces it: the test has to be read at the field's own level, with everything finer already integrated.

## 2. Persistent regions cannot work at d = 4 (R4)

Dimock's induction, rebuilt from the printed statements of arXiv 1212.5562 (Theorem 3.1) and 1304.0705: the regions decrease, Omega_1 > Omega_2 > ... (each Omega_(j+1)^c holds the rounded and buffered Omega_j^c), so a large-field cube found at level i removes one cube of every coarser level, up to the top. The sum over histories is closed at 1304.0705 (205): a level-i cube pays, for its column, sum_(j >= i) C (-log lambda_j) r_j^3, and this is bounded by C (-log lambda_i)^(3r + 2), **using N - i <= -log lambda_i**. That inequality says the column height is at most the logarithm of the inverse coupling. It is the superrenormalizable fact lambda_k = L^(k-N) lambda, and it has no analogue on the flow x_j = x_K + b(K - j), where the height K - i is about x_i/b. The open abstract of Balaban's CMP 119 (1988) says the same in its own terms: the inductive description of the densities with large-field domains completes the analysis for superrenormalizable models. The abstract of CMP 122 (1989) names the R operation as what removes the main obstacle in four dimensions.

This is not only a loss in an estimate. The holes really are everywhere.

**Lemma RARE (discharged).** *Let 0 < T <= 1/2, x >= 1. For a link b and any values of the other links, P(some plaquette at b has angle > T | rest) >= q := (T^3/12) exp(-12 x T^2).*

*Proof.* With the notation of Lemma TYP write u = cos phi, phi in [0, pi], the angle of U_b R. If all six angles are at most T then s u = sum_p (1/2) tr(U_b S_p) >= 6 cos T, so s >= 6 cos T and u >= cos T, that is phi <= T. So the event contains {phi > T}. Given the rest, phi has density proportional to sin^2(phi) exp(k cos phi), with k = x s <= 6x. Let k >= 1. On [T, 2T] the density is at least (4 T^2/pi^2) exp(k(1 - 2T^2)), using sin phi >= 2 phi/pi and cos phi >= 1 - phi^2/2. The full integral is at most exp(k) times the integral over [0, infinity) of phi^2 exp(-2 k phi^2/pi^2), using sin phi <= phi and 1 - cos phi >= 2 phi^2/pi^2. Evaluating, P(phi > T) >= (16/pi^(5/2)) (2/pi^2)^(3/2) k^(3/2) T^3 exp(-2 k T^2) >= (T^3/12) exp(-12 x T^2). For k < 1 the density is within e^2 of Haar, and P(phi > T) >= e^-2 (1 - 2 T^3/(3 pi)) >= q. QED

**Proposition HOLES (discharged, given the flow's upper bound).** *Let x_0 <= x_K + B K, with 12 B T^2 <= 2 log L. Then a level-K cell contains no level-0 plaquette of angle above T with probability at most exp(-n q), with n >= L^(4K)/16, and*

    n q >= (T^3/192) exp( 2 K log L - 12 x_K T^2 ).        (2.1)

*Proof.* Take B as in (1.1). Given the rest the events are independent with probability at least q. Insert the flow. QED

The hypothesis holds for T <= 1/2 at the actual slope B about 0.372 log L. Any smaller threshold only makes more holes, so this covers Balaban's thresholds g p(g), and the fixed T of both attempts. So for K >= K_0 := (6 x_K T^2 + log(192/T^3))/log L, every top cell holds a rough fine plaquette, except with doubly exponentially small probability, and a union bound over the fixed number of top cells keeps that. **In any induction where a large-field cell removes its ancestors at all later levels, the small-field region at the top is empty for K >= K_0.** In phi^4_3 the same count is L^(3(N-j)) exp(-c (N-j)^(2p)) and it is summable, which is why Dimock needs no R. Explicit regions at d = 4 must be absorbed after finitely many levels, or there is nothing left to run the induction on. The same count appears, as a recorded difficulty, in the mapped part's reading of Balaban's R (`parts/hard-core--mapped.md`, Text 2) and it is what its positive gas answers.

**R4, verdict on persistent regions: FAIL, by (2.1).** The state cannot be "regions with histories" in the form of Dimock's Theorem 3.1. Only regions of bounded age can be carried.
