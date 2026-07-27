# Route portfolio

| Route | Claim-state movement | Trace | Artifactability | Overclaim risk | Decision |
|---|---:|---:|---:|---:|---|
| Class-A inequalities over two SHA-pinned artifacts, with source runners included as static helpers | 3 | direct blocker closure | 3 | low | selected |
| Read current sharded audit grades before parsing | 0 | mutable governance state, not proof | 2 | high | rejected; the certificate must not depend on an audit verdict |
| Re-run both expensive family computations inside the synthesis runner | 2 | duplicates source computations | 0 within the short fix budget | medium | rejected as unnecessary duplication |
| Derive the magnitudes and the `H`/seed selector from `Cl(3)` on `Z^3` | 3 if solved | structural extension, not the quoted bounded blocker | 0 | very high | excluded from this claim and short closure |
| Keep a hard-coded expected-value matcher and add prose | 0 | does not retire class G | 3 | high | rejected |

The selected route keeps the load-bearing object as a class-A inequality over
two exact artifact inputs. Static imports expose the complete source runners to
the restricted packet, SHA checks bind the transcripts, and the primary runner
recomputes the finite summaries without reading a mutable audit verdict.

## Prior-art sweep

- Searched commit: `460e7ed266f25b32e7a184ed0c768b5623dc2dcb` (`origin/main`; remote
  refresh was permission-blocked, and the existing snapshot equals `HEAD`).
- Searches: both noun orders for seed-0/cross-family and Fam1/Fam2; both noun
  orders for `delta_hist`/ordering and weak-field/family; Wave Direct-dM title
  inventory; audit obligation and ledger hits for the claim id.
- Matching hit: this note already contains the bounded two-row theorem, and its
  latest archived audit on matching premises was clean. The current primary
  runner nevertheless crashes because it reads the removed monolithic ledger.
- Classification: theorem already proven on matching premises; proceed only
  with the non-duplicative artifact-chain repair.
