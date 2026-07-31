# Review History

## Initial checkpoint

Review disposition: `pending`.

Pre-review risks already identified:

1. deriving the invariant measure by assuming it rather than calculating the
   lattice pole residue;
2. calling an assumed tensor product a consequence of the Qubit axiom;
3. confusing CAR relabelling under a given CAR algebra with statistics
   selection;
4. silently upgrading a Euclidean pole limit to OS/Wightman reconstruction;
5. relabelling existing P1-P8 checks as a new theorem;
6. overusing kinetic isotropy beyond its exact `c_t=c_s` boundary.

No PR may open while the disposition is pending.

## Checkpoint 1 — adversarial pre-review

Review disposition: `pending`; narrow fixes required.

- `SEMANTIC_BRIDGE`: an arbitrary measurable projector frame would leave a
  textbook choice inside the alleged carrier derivation. Fixed by deriving the
  explicit finite-spacing partial isometry `T_a` from the Clifford symbol and
  rest projector.
- `IMPORTED_VALUE / SEMANTIC_BRIDGE`: the first draft named a standard boost
  without exhibiting it. Fixed by giving `L(p)` explicitly and checking both
  `L^T eta L=eta` and `L(m,0)=(E,p)`.
- `REPO_GOVERNANCE`: the minimal-axiom memo was initially a graph dependency
  even though it supplies no dynamics or composition. Fixed by retaining it as
  plain boundary context only.
- `IMPORT_SUPPORT`: the retained parity theorem assumes a finite tensor product
  and supplies neither its physical existence nor cross-mode CAR. Because the
  new note re-derives every needed Pauli/Jordan-Wigner identity, the decorative
  graph edge was removed and the parity row retained as plain comparison
  context.
- `AUDIT_COMPATIBILITY`: the heuristic classifier read the boundary phrase
  containing the word `observed` as class D. Fixed without weakening the
  scientific boundary; the source still forbids fitted inputs and literature
  proof inputs, and the classifier now reports `D=0`.
- `LABELING_CONVENTION`: the Pauli ladder convention could be inferred in two
  ways. Fixed by displaying `sigma_+` and the associated occupation matrix.
- `BUG / SEMANTIC_BRIDGE`: the first finite CAR draft used `omega_a` as the
  occupation weight even though the analytically continued pole location is
  `E_a`. The projectors still use the exact `+/-omega_a` spectral split, while
  the raw and normal-ordered finite-mode occupation operators use the pole
  weight `E_a`; the runner checks that corrected identity without promoting it
  to physical Hamiltonian energy.
- `SEMANTIC_BRIDGE`: the target note's old trailing methodology paragraph
  still listed the invariant measure and CAR relabelling as free textbook
  inputs. Fixed so those objects are sourced only from the new candidate edge;
  general Lie/Clifford and induced-representation machinery remains non-graph
  mathematical infrastructure.
- `REPO_GOVERNANCE`: added `AUDIT_TIMEOUT_SEC=120` and a canonical SHA-pinned
  runner cache.

The affected note, runner/cache, import ledger, and certificate require a
focused second review after the final disposable pipeline run.

## Checkpoint 2 — focused re-review after the 90-minute deep block

Review disposition: `pass`.

Additional workers were forbidden, so the repo-native reviewer roles were
emulated sequentially on the final staged surface.

### Code / runner — PASS

The new deterministic runner passes `11/11`; the unchanged target runner
passes `8/8`; the retained Clifford-parent runner passes `12/12`; and the
non-graph parity comparison passes `47/47`. The new cache pins the live runner
SHA-256 `2df622445a8d5c592de4b375a19982bf14fd21215dc2f6b2845642471fc09ba1`.
`py_compile` and `git diff --cached --check` pass.

### Physics claim boundary — BOUNDED

The source derives a compact-momentum pole carrier with four spectator tastes
and a finite given-CAR relabelling. It does not claim selection of the free
action, physical global composition, CAR statistics, a single taste,
OS/Wightman reconstruction, interacting covariance, or generator-domain
closure. Those exclusions match the downstream target's existing bounded
scope rather than changing it.

### Imports / support — DISCLOSED

The graph has exactly two load-bearing parents: the `retained_bounded` ABJ
finite Clifford core and the registered kinetic-isotropy primitive. The final
review found and fixed a possible custody ambiguity: the ABJ parent supplies
the symmetric four-label Euclidean formula as a finite algebraic surface,
while the primitive alone licenses temporal graining in the same kinetic
normalization as `Z^3`; it does not turn the analytic pole parameter into
physically reconstructed transfer energy. The minimal axioms and parity theorem
remain boundary/comparison context, not decorative graph dependencies.

### Nature retention — BOUNDED

V1-V5 all pass. The marginal result is the finite-spacing pole/residue route
to the mass shell, density, exact spectral-fiber trivialization, spin/taste
carrier, and finite hole relabelling. It is neither the target's existing
continuum identity packet nor a Pattern-A rescope.

### No-go discipline — NOT APPLICABLE

No negative theorem or named universal wall is proposed. The temporal-coefficient
and string-omission checks perturb only the displayed constructions and do not
foreclose alternative parametrizations or equivalent CAR presentations, so
N1-N8 is not substantively triggered on the narrowed source surface.

### Labeling convention — PASS

The Pauli ladder convention, occupation projector, positive/negative spectral
labels, distinction between `omega_a` and the pole weight `E_a`, taste
multiplicity, and principal time patch are explicit.

### Repository governance — PASS

No audit worker, audit-verdict tool, ledger/status edit, publication output,
or `MISSING_DERIVATION_PROMPTS.md` edit is present. The shared-lock permission
failure is recorded and the branch-local lock remains untracked. No active
cl3-to-cl31, PMNS, Koide, or Record-worker file is touched.

### Audit compatibility — PASS

The full 18-stage audit pipeline passed in a disposable worktree against
`origin/main=1932972cb7d9d21693d70b7c74c3a206b77d1211`. Strict audit lint had no
errors; generated audit/publication outputs were discarded. Fresh queue
inspection classified the candidate as `bounded_theorem` / `unaudited`, ready
for independent audit with two allowed dependencies, and reset the target to
`unaudited` behind that new parent as expected. No generated output remains in
the science worktree.

### Independent checks — PASS

- symbolic expansion independently reproduces the `E_a` and `rho_a` terms;
- 200 random pole/frame cases have worst residuals below `5e-15`;
- compact-convergence ratios approach four under halving of `a`;
- the anisotropic temporal coefficient changes the target shell;
- the Jordan-Wigner and hole-shift identities close exactly;
- 200 independent standard-boost/Wigner tests give cocycle, rest-fixing, and
  Lorentz residuals below `1.3e-14`; and
- an independent cover check confirms that the spin-one-half action must be
  stated on `Spin^+(1,3) ~= SL(2,C)`, not as an ordinary representation of
  `SO^+(1,3)`.

Overall local review-loop disposition: `pass`. Independent audit remains
required and no effective status is authored here.

## Checkpoint 3 — cycle 2 restricted-packet transport repair

Review disposition: `pass`.

The scoped repair gives only the target-to-authority edge a 22,000-character
authority budget. The default remains 10,000 characters, the prior unrelated
override is unchanged, and the authority source itself is unchanged. The new
regression renders the real target packet and proves that the manifest contains
the authority byte-for-byte, includes all requested Sections 2–5, and carries
no load-bearing clipping marker. The authority's independent formula runner
passes `11/11`; the target runner passes `8/8`.

The first review iteration added a dated packet-readiness record to the target
note as an explicit re-audit trigger. On frozen current main,
`audited_conditional` is already non-terminal and audit-pending, and the row is
dispatch-open because its recorded policy fingerprint moved; the source-hash
change additionally takes the supported reset path on the next seed. A
sibling-pin sweep then exposed one exact wording guard in the Wigner companion;
the existing invariant measure statement was reconciled to the expected
`Lorentz-invariant mass-shell density` wording without changing the claim. The
self-adjointness companion passes `21/21` and the Wigner companion passes
`48/48`; those runner results are source evidence, not audit grades.

The complete 18-stage audit pipeline passed in a disposable clean clone at
`b377240587dc9cb0640cb4424e4ea25261687e7a`. Strict audit lint reported no
errors. The regenerated ledger classified the target as `bounded_theorem` /
`unaudited`, and the target was present in the audit queue. Generated audit,
publication, and front-door files were confined to the disposable clone and
were not copied into the source worktree.

Claim-boundary, import, and Nature-retention review remain bounded: no premise,
formula, dependency edge, negative claim, or scientific scope changed. The
repair closes the named runner-artifact obstruction and exposes the already
existing derivation for independent checking. It does not predict or apply the
fresh audit verdict. The target's negative-looking prose is only a set of
non-foreclosing scope exclusions, so no N1-N8 pass or named-wall certification
is asserted.
