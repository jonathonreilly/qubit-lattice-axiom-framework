# GOAL — block 15: the formation-unit clause witness — when sequential formation of a unit reproduces its joint law (2026-09-15)

**Owner directive (2026-09-15):** don't stop; assess the next lane at each conclusion; no subagents; derivations over computation.

**Why this block.** The derivation campaign's verdict table (#8093) lists "Formation unit" as *to compute*: single-site formation ("for each site") against joint formation on a covariant set, with the expected witness "the joint law on a covariant set differs from every sequential law" on the star (a site and its six neighbours), and the clause candidates "for each site" against "for each admissible set of sites". Nobody has opened it. `main`'s joint-formation notes (2026-09-03/04) live in the unitary-tick setting; the classical definition is stated here.

**Object.** A unit `U ⊂ Z³` (finite), its outside neighbours `O = N(U) \ U` carrying fixed records `v_O` (possibly empty: the isolated unit); the six-axis menu with the product rule `(p, q, r)`, executed at `(3,1,2)`. *Joint formation* of `U`: the records of `U` are drawn from the unique positive law on `U` whose one-site conditionals, given all neighbours inside and outside, are the rule — the Gibbs conditional `Π_{edges in U and U–O} φ / Z_U(v_O)`. *Sequential formation* along an order: `Π_x r(v_x | v_{A_x})` with `A_x` the outside neighbours of `x` together with the inside neighbours recorded before `x`.

**Contract.**
- U1 (uniqueness lemma, re-proved): a positive law on a finite set is determined by its one-site conditionals; hence the joint law is well defined.
- U2 (the criterion): sequential formation of `U` in the environment `v_O` equals the joint law **iff** no site records an inside neighbour together with a second recorded neighbour (inside or outside); proved for every non-constant rule via the lemma `K_k(b, b, …, b) ≠ K_k(−b, b, …, b)` for `p ≠ q` (closed form `((p−q)/Z_1)[(p/Z_1)^{k−1} − (q/Z_1)^{k−1}]`) and `K_k(b, …) ≠ K_k(c, …)`, `c ⊥ b`, for `p = q ≠ r`.
- U3 (the star, corrected): in isolation the star's sequential law equals its joint law iff at most one leaf precedes the center (executed: the seven classes by `k`, total variations for `k = 2..6`); the campaign's expected witness fails on the isolated star and holds on the isolated plaquette (every order differs; executed).
- U4 (units in a recorded environment): every connected unit with at least two sites differs from its joint law under every order (the last site records all its neighbours); executed on the star, a domino and a path in two environments; a single site agrees.
- U5 (the clause reading): "for each site" is the sequential reading; "for each admissible set" with the whole window as the set is the static reading; intermediate units in an environment never coincide with sequential formation. Recorded, not adopted.
- N-gate for the negatives (U2's "only if"; U4).

**Lens pass (self-run panel).**
- *"Joint formation is undefined for a classical rule."* Defined as the rule-consistent law on the set (U1 makes it unique); this is the only reading under which "for each site … determined by the nearest-neighbour conditions" applies to every site of the set at once.
- *"The star was supposed to be the witness."* It is not, in isolation: Theorem B (block 01) makes center-first formation reproduce the joint law. The environment restores the witness (U4), and the criterion says exactly why.
- *"Is U2 just block 01 again?"* Block 01 treats isolated windows without an environment; U2 adds the environment and gives the iff in terms of recorded neighbours; the environment case is what a unit inside a growing record field sees.
- *"Only small units."* The theorems are general; the executions are on the star, the plaquette, a domino, a path and a single site.

**Forbidden phrases (beyond the lane's standing list):** "the unit clause is adopted", "selects the unit", "converge", "emergent", "certified".

**Prior-art search at `origin/main`.** `git grep -n -iE "joint(ly)? (formation|forms|record)|forms? (all )?at once|formation unit"` → the census note (names joint formation on covariant sets as an owner decision), the unitary-tick notes of 2026-09-03/04 (commuting projectors; a different setting); no classical criterion. Open PRs: none on the unit seam.
