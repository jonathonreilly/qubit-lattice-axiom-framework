# Tensor Network Connection Note

**Status:** support - structural or confirmatory support note
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The runner reproduces the finite numerical gates, but it does not derive the note's broader bridge to AdS/CFT, Ryu-Takayanagi, and holographic-principle language. In particular, the runner reports the S vs 1/g RT fit as R^2=0.6465 while the linea"*

with repair: *"missing_bridge_theorem: Re-audit after either removing/marking the holographic and RT language as explicitly interpretive, or adding a retained bridge theorem that derives the claimed AdS/CFT/RT/holographic connection from the finite transf"*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The four runner-verified computational gates: propagator-as-MPO bond dimension equals Ny on tested 2D lattices (Test 1); CFT central charge `c=1.09` with `R^2=0.9997` and 2D area-law fit `R^2=0.9996` (Test 2); gravitational bond dimension drop 8→7 at `f=20` (Test 3); monotonic entropy decrease with gravitational coupling (Test 4) — all finite numerical results exactly reproduced by the runner.
- **NON-load-bearing (split off / admitted):** The broader interpretive bridge connecting these finite numerical results to AdS/CFT, Swingle 2012, Pastawski et al. 2015, Ryu-Takayanagi, and the holographic principle is not derived by the runner; those identifications are explicitly interpretive and remain admitted, non-load-bearing language until a retained bridge theorem derives the connection from the finite transfer-matrix structure.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

**Primary runner:** `scripts/frontier_tensor_network_connection.py`

**Audit-conditional perimeter (2026-05-11):**
The current generated audit ledger records this row `audited_conditional` with
`auditor_confidence = high`, `chain_closes = false`, and audited
`claim_type = bounded_theorem`. The audit chain-closure explanation is exact:
"The runner reproduces the finite numerical gates, but it does not derive the
note's broader bridge to AdS/CFT, Ryu-Takayanagi, or the holographic principle.
In particular, the runner reports the S vs 1/g RT fit as R^2=0.6465 while the
linear S vs g fit has R^2=0.9745, so the RT-labeled gate is only monotone
entropy decrease, not an RT formula derivation." This repair removes the
load-bearing holographic/RT interpretation and keeps only the finite
computational theorem produced by the registered runner
[`scripts/frontier_tensor_network_connection.py`](../scripts/frontier_tensor_network_connection.py):
Test 1 (propagator-as-MPO bond dimension equals Ny on tested 2D
lattices), Test 2 (CFT scaling `S = (c/6) ln(L), c=1.09, R^2=0.9997`;
2D area law `S = 0.82 * boundary - 0.47, R^2=0.9996`; mutual
information `~d^{-0.86}`), Test 3 (gravitational bond dimension drop
8 → 7 at f=20), and Test 4 (entropy decreases monotonically with
gravitational coupling, approximately linear `S ~ -0.36 g + 5.77,
R^2=0.975`, with the inverse-coupling fit failing as an RT formula
derivation). The words AdS/CFT, Ryu-Takayanagi, MERA, and holographic
principle are retained only as outside-context analogies and rejected as
derived claims in this row.

## Result

The path-sum propagator on the tested layered graphs factors through a finite
Matrix Product Operator (MPO)-style transfer-matrix product. The toy
gravitational potential modifies the singular value spectrum of the transfer
matrices and reduces the center effective bond dimension from 8 to 7 at
`f=20`. All four finite computational checks pass. No continuum AdS/CFT, RT,
MERA, or holographic-gravity theorem is claimed.

## Key findings

### Test 1: Propagator as MPO (PASS)
On a 2D lattice (Nx x Ny), the propagator from layer 0 to Nx-1
decomposes as a product of Ny x Ny transfer matrices. Bond dimension
equals Ny for all lattice sizes tested (4, 6, 8). Gravity changes
matrix elements but not the formal bond dimension.

### Test 2: Entanglement structure (PASS)
- 1D CFT scaling confirmed: S = (c/6) ln(L) with c = 1.09 (expect 1.0
  for free fermion CFT with open boundaries). R^2 = 0.9997.
- 2D area law: S = 0.82 * boundary - 0.47, R^2 = 0.9996.
- Mutual information decays as d^{-0.86} between separated regions.

### Test 3: Gravitational bond dimension (PASS)
At strong gravity (f=20), the effective bond dimension at the center
drops from 8 to 7 and the singular value condition number grows from
112 to 641507. This is a finite strong-field singular-spectrum compression
diagnostic only; it is not a derivation of the holographic principle.

### Test 4: Entropy coupling sweep (PASS as monotone diagnostic)
Entropy decreases monotonically with gravitational coupling: from
S=6.07 at g=0 to S=2.43 at g=10. The relationship is approximately
linear (S ~ -0.36*g + 5.77, R^2 = 0.975) rather than S ~ 1/g.
This explicitly fails as an RT formula derivation on the tested sweep:
the inverse-coupling fit has only R^2 = 0.6465, while the direct linear
fit has R^2 = 0.9745.

## Interpretation

The retained content proposed by this note is the finite computational
diagnostic package above. These readouts can be compared with tensor-network
and holography vocabulary, but this row does not derive a bridge to AdS/CFT,
Ryu-Takayanagi, MERA, the continuum, or physical holographic gravity. A future
bridge theorem would have to define the dictionary and prove that the finite
transfer-matrix quantities instantiate it.

## Scope repair and re-audit boundary (2026-05-27)

This repair answers the audit blocker by choosing the narrowing route, not by
adding a new bridge theorem. The row should be re-audited only as a bounded
finite-runner theorem:

- The propagator factors as the runner's tested transfer-matrix product with
  bond dimension bounded by `Ny`.
- The free-fermion entanglement calculations reproduce the stated 1D log
  scaling and 2D area-law fits on the sampled finite lattices.
- The toy gravitational potential changes the singular spectrum and reduces
  the center effective bond dimension at the strongest tested coupling.
- The entropy sweep is a monotone finite diagnostic; it is not an RT
  `S = Area/(4G)` derivation.
- No AdS/CFT, MERA, continuum, or physical-gravity claim is promoted by this
  row.

Branch-local checker:

```bash
PYTHONPATH=scripts python3 scripts/frontier_tensor_network_connection_scope_repair.py
```

## Script
`scripts/frontier_tensor_network_connection.py`
