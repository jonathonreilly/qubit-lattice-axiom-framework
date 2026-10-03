You are lane A41, the final small lane of an overnight exploration ("Campaign 8"). Time box: 40 minutes. Topic: **does charged "vector" matter, hopping through light's links that carry a uniform π flux, move like light?**

## Context (read only what you need)
Scratch root: SP=/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad
- A40's layout "S1": matter sits on the vertex places of the 2×2×2 role cell (a coarse cubic lattice of spacing 2), and light's links sit on the edge places between them. See `SP/c8/A40/REPORT.md`, especially §3.8 T5, and its ERRATA.
- The fourth review, round 8 (`SP/c8/A34/REVIEW4.md`, C134), found the following:
  - No glued covariant hop exists for one-component charged matter through a light link. Under a quarter turn about its own axis, a link's raising operator picks up a phase of −i.
  - A 2-real-parameter family of covariant hops exists for a charged TRIPLET over an empty singlet. These hops are helicity-changing matrices.
  - Its exploratory band scan (`SP/c8/A34/c14_vector_matter_bands.py`, c13) was inconclusive.
  - Neutral vector matter with the hop i S^a has isotropic touchings at k = 0 (slopes −2, 0, +2) plus a flat middle band.
- `SP/c8/A34/c13_glued_link_hops.py` builds the covariant hop family. Reuse it and cite what you reuse.

## Task
1. Take the 2-parameter covariant charged-triplet hop family through links. Treat light's links as a fixed classical background:
   - (a) zero flux;
   - (b) a uniform π flux through every square. KS gauge on the coarse lattice: the link phase multiplies the triplet hop matrix.
2. Build the single-particle Bloch Hamiltonian. That is 3 internal states times the magnetic unit cell, i.e. 3×8 = 24 bands for π flux in KS gauge. Scan the parameters.
3. Answer:
   - Are there band touchings at zero energy? Linear? Isotropic?
   - How many cones, and with what slopes?
   - Are there flat or heavy bands beside them?
   - Is the spectrum symmetric about zero, so that negative energies exist (A39's positivity lemma)?
   - Compare (a) with (b): does light's π flux create cones that zero flux lacks, or does the matrix holonomy of the triplet hop already twist things?
4. Grade everything (EXACT / CHECKED / ARGUED / COMPARATOR). Single-particle numerics on Bloch matrices are CHECKED. Analytic statements are EXACT.

## Rules
- Use `nice -n 10` with the four BLAS thread caps set to 1. Each run must take under 40 s and 200 MB. Check `uptime` first and only run if the load is below 6.
- No git, no repo edits.
- Never present anything as adopted, and never use "read" for possibilities.
- Put scripts in `SP/c8/A41/`. If your sandbox blocks REPORT.md, return the report as your final message.

## Output
A short report with these sections:
1. Question
2. Answer: graded
3. Derivation and checks: the numbers
4. Open edges
5. A 3–4 sentence plain-language summary for the owner
