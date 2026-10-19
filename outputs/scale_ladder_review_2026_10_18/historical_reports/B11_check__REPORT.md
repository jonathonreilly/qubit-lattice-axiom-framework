# B11 check

Provenance: a fresh-context checker of the same model family. Its circuit build is its own: a Clements on-site mesh, R_L plaquette blocks with 2-colouring matchings, and its own S = D·S_B·S_A. The reference is the runner's Ws(k), rebuilt from `B18_check/chk_model.py`. Saved by the supervisor from the hand-back.

**Runs:** `chk_b11.py` PASS=17 (two first-run checker bugs fixed). B11's own scripts re-run at 11/11, 4/4 and 8/8.

## Verdicts

- **Circuit identity: confirmed.**
  - The circuit equals the real-space step to 2.3e−15.
  - Its Bloch transform equals Ws(k) at all 64 momenta to 2.7e−15.
  - Every gate acts on ≤ 2 modes within sup-distance 1.
- **Depth.** The "~25" is specific to the Reck order. A Clements mesh gives 2-mode depth 16 (17 with the phase layer). The minimal depth is not determined.
- **The 5³ block-embedding claim is unsupported; removed.**
- **Clifford wording.** These are statements about the many-body Γ(U).
  - Γ(S) is Clifford.
  - Γ(R_L) is Clifford plus π/8 rotations, with T-count ≤ 12 per site.
- **On-site obstruction: confirmed by a Galois test.** Add "exact, measurement-free, clean ancillas". Approximate synthesis is always possible.
- **Context.** W is a matchgate circuit, so it is classically efficiently simulable.
- **Follow-up overreach corrected.** No on-site Clifford choice in this search gives a Weyl doublet; exact Clifford+T on-site factors remain open. `clifford_family.py` execs a scratchpad file.
