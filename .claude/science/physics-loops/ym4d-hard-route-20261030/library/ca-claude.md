lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:43Z

# CA, completion-collar admission: Claude proof attack (FINISH row 347)

Provenance: Claude Opus 5.5, max effort, Mac mini worker; checkout pinned at `98d2f9435`; 2026-11-06. Research text, not an audit, no status. Proved by Claude, not yet checked by the other model. No computer-assisted step and no numerical run was used.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text (complete account CA-I, CA-II, CA-III and outline at upstream `31a47c543775`), for every statement, construction and bound cited with a line number below; Tadeusz Balaban for the multiscale construction (CMP 89-122). Earlier lanes in this repository: `arr.md` (two rounds), `crca.md`, `prior/ca-claude.md`.

Kind of result (How we work, item 9): proof of steps the account assumes (its collar corollary, I:142283-142291, in the weaker CA form), by reduction. One step stays open and is stated as one lemma.

## 0. Summary

1. **Seed, pinned part: proved (Lemma A).** On every stratum bond of a removed collar, the completion seed equals the raw real datum, exactly. The rows come from Balaban's splice formula and a separation the account proves. So at b2 the plaquette entries are below 0.04 r1(0), and A' = 0. This settles, for stratum bonds, the datum identification that ARR section 15.2 left open.
2. **Seed, side plaquettes, current and cubes: proved as an implication (Lemma B)** from one account input, the base bound on the core (I:136724-136733, I:138438-138450), used only at cells of level at least one. The account prints no statement or proof of that bound. Result: the seed current is at most 0.48 r3(0), and the index-zero cube clause holds.
3. **Sharpened criterion (Proposition C).** Lemmas A, B and the collar layer bound (CL) imply CA. The layer budget in (CL) is 48 times weaker than ARR (18.4).
4. **(CL) stays open.** Three new attacks fail at stated points (section 6). The account's own layer bounds give (CL) only for completion densities k up to a ceiling k*(gamma). The reason is structural: the old raw radius scales with the bare coupling g0, and the layer sources scale with gk. A proof needs a decay that grows with h = k - Nk; the account's k-independent separation does not give it (section 6.4).

## 1. Sources and scope

- Read first: `library/prior/ca-claude.md`; `library/arr.md` sections 2-3, 10-18 and Result; `library/crca.md` section 3; `library/open-core.md` sections 1 and 7; the CA row of `library/open-registry.md` (owner `ca-claude`, state open, so no duplicate lane).
- Account sources: fetched by URL from the Sussman-Alpoge repository into a scratch folder of this lane. SHA-256 values agree with `arr.md` section 1. Line numbers below are of those raw TeX files.
- Balaban CMP 122a and 122b are not in `~/ym4d-papers`. Project Euclid answered with a bot check (Incapsula), so the fetch stopped there, as the rules require. CMP 122a/b statements are used only as the account quotes them.
- The level-zero chain proposition and the collar corollary of I:142269-142291, and the cube admission of I:142950, are not used anywhere below.

## 2. Consumer strategy

**Who reads CA.** The consumers are listed in `crca.md` sections 3.2-3.3: clause (e4)' of `4.27:thm-collar-rigidity`, newborn continuation and old-term composition, the arrest uses K1, K2, K7, and the frozen leftovers of the correlation induction (II:25188-25200). Each needs image membership in the old dated raw clause at every removed collar point, for every source, parameter and segment, with the cube clause.

**No entry can be dropped.** A stored term whose domain meets a completed component is absorbed into Balaban's term V(Y) at that completion (I:132301-132303). The absorption evaluates the term on the presented chain at b2, b3, b4. So the old clause is read on the full chain, seed and layers together. No consumer reads only the real seed, a real slice, or a subset of the five entries. I agree with the digest: no weaker all-consumer statement than CA exists.

**What the consumers' threshold buys.** CA's threshold is f0(d^t) r_a(0) with f0 > 3.65 (ARR (10.3)), not the 1/16 that the account assumes. Sections 3-4 show that the seed uses at most 0.04 of r1(0), r5(0) and 0.48 of r3(0). The room left for the two layers is therefore large. Section 5 turns this into the layer budget

  epsilon := F3 + F4 <= min{ 1/85 , (3/Kcur) alpha_{*,0} },   Kcur = 3 + 18d + 2.2 KJ,

where ARR (18.4) asked for min{1/160, alpha_{*,0}/(16 K*)} with K* = Kcur. This weaker statement (CL) is the one attacked in section 6.

Status: sections 3-6 are being written.
