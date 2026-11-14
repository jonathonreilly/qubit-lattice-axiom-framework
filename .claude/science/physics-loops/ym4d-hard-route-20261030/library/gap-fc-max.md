lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T20:51Z

# gap-fc-max (row 947): the Fisher-information contraction (FC)_theta on the seed box

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, pinned at commit f1c3de09b, started 2026-11-14T08:51Z.
Author item. Not checked by another model (check = row 949). Research-stage working state; nothing here is a public claim.
No subagents. No computer-assisted step: any run is labelled GUIDE and can only refute or guide.

Credit. The seed, the slice chain and the hypercontractivity route come from this repository's rows 931-946 (Claude and Codex).
The transfer-matrix and vacuum-slice setting builds on Ethan Sussman and Levent Alpoge's complete account
(CA-I/II/III at commit 31a47c543775, text by them with Claude and Codex) and on Balaban's and Dimock's papers; each use is cited where it occurs.

## Plan (at most eight steps; one step per response; each appended before the next)

1. Read row 941 (`library/gap-lsivac-max.md`) in full. Record (A3), (FC)_theta, (GC)_theta, Theorem C0, and the rate Proposition HC needs.
2. Read row 946 (`library/gap-fctest-opus.md`) and check 943. Decide the branch: (FC) refuted at beta 2.3 (then: corrected Dirichlet form) or not (then: attack (FC)).
3. Duplicate check (rule 0a): grep `library/open-core.md`, `library/l17c.md` and the FINISH rows for (FC)/(GC). Outline lookup in the Sussman-Alpoge index.
4. State (FC)_theta with the explicit seed-sized rate (lead note (a)). Fact tests on the statement: U(1) fails THAT rate; SMALL-BOX; frozen groups.
5. Attack the linearisation (GC)_theta: P grad^* grad P at most theta grad^* grad on L^2(nu). One approach per response.
6. Attack (FC)_theta itself, or lift (GC) to (FC).
7. If it does not close: the smallest unproved inequality, and one test that could refute it.
8. Final summary and the RESULT line.

## Status log

- 08:51Z file created. Nothing proved yet.
