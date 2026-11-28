# Ladder PS: planar stability of the master-field equation (the order-one crossing)

Target (row 1708 section 7): at one order-one beta, a master field W_beta exists and the linearised planar Schwinger-Dyson operator has a bounded inverse in the norm sup_l |delta(l)| e^(-m r(l)) a^(-|l|), with constant kappa.

| Rung | Statement | Status | Row | Gate |
|---|---|---|---|---|
| PS1 | Exact specification of a Newton-Kantorovich certificate (finite loop set, exact arithmetic, inequalities) whose pass proves (PS) at one beta | done (unchecked): Theorem C | 1716 | written spec, checked |
| PS2 | Tail lemma closing the truncation (reflection positivity or other) | OPEN in 4D; row-sum form needs 6 beta a^4 < 1; FALSE in the one-plaquette twin weak phase | 1716 | proof by hand, checked |
| PS3 | First exact instance at small beta, matched to the strong-coupling expansion | done (unchecked): twin certificate at beta = 9/10; 4D W(p) = u + 4u^5 | 1716 | exact output |
| PS4 | Certificate at an order-one beta, Lean-checked | open; cost about 1e14 rational operations at Lambda = 16, beyond direct Lean: needs a smarter certificate | | Lean kernel, axioms printed |
| PS7 | Restate (PS) for the weak side (row 1716: as stated it fails in the twin weak phase): smaller perturbation class, other norm, or a modified action without a bulk transition | open | 1720 (in part) | statement that the twin does not refute |
| PS5 | U(N) twin: the same certificate fails where U(N) is Coulomb (the SU(N) last term is the selective line) | open | | twin test |
| PS6 = GPU | Joint rung with ladder LD (row 1717 Lemma I): planar uniqueness in a ball with free boundary; (PS) is its linear infinite-volume form | in progress | 1720 | see LD.md |
