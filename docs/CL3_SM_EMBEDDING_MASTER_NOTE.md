# Cl(3) carrier synthesis: algebra, supplied normalization and physical boundaries

**Date:** 2026-04-19; correction 2026-10-21
**Type:** bounded_theorem
**Primary runner:** `scripts/verify_cl3_sm_embedding.py`
**Status authority:** independent audit lane only.

This synthesis consumes the explicit finite carrier and corrected proof in
[the carrier note](CL3_SM_EMBEDDING_THEOREM.md). It does not derive the Standard
Model from a single axiom or supersede the
[current four-axiom memo](MINIMAL_AXIOMS_2026-06-29.md).

| Result on supplied matrices | Limit |
|---|---|
| Real even Clifford algebra H, dimension4; central omega gives an independent fifth vector | These are vector-space counts, not gauge coupling values |
| Chosen g2²=1/4, gY²=1/5 gives ratio4/9 | Reciprocal-dimension normalization is supplied; physical coefficient and matching remain open |
| Base SU(3), fiber SU(2) and selected Y commute | Their physical gauge interpretation and carrier realization are additional bridges |
| Y has multiplicities6 and2, values1/3 and−1, trace zero | Tracelessness alone is not anomaly cancellation or a species assignment |
| S3 action and a three-state cyclic orbit | The orbit is not three physical generations; its restricted Y spectrum is not uniform |
| Fierz identity and adjoint dimension fraction8/9 | A dimension fraction is not a universal current amplitude or an electroweak correction |
| det(aI+sum biJi)=(a²−|b|²/4)² on the explicit four-dimensional even block | Restricted algebraic result, not positivity of every Hermitian operator or physical A-BCC selection |

The last identity follows from the Clifford anticommutators and trace, as proved
in the linked carrier note. The old argument omitted Kramers' T-invariance
hypothesis; normalized T=2J2K squares to−I but sends J2 to−J2. The result survives
by a different, explicit algebraic proof, not by claiming every H is invariant.

The [taste-orbit note](CL3_TASTE_GENERATION_THEOREM.md) and
[color-action note](CL3_COLOR_AUTOMORPHISM_THEOREM.md) carry their own conditions.
Neither a spatial dimension nor the dimension of a selected symmetric square
alone identifies physical color or generations. The symmetric square of the
fundamental SU(2) module is spin1; an SU(3) action on that underlying complex
three-space is separately supplied.

The historical95-check table is superseded by the actual current runner output.
It was not a proof of the withdrawn physical claims. The previous source is
recoverable at `f24d17d97d372df977476e4a69674577f31af575`.

Related prior work and bibliographic links are recorded in the carrier note,
including Susskind's lattice-fermion construction and the Clifford-algebra
constructions of Furey and Stoica. No novelty, physical equivalence or full
Standard Model closure is established here.
