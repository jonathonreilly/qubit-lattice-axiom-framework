# Collective corner response: focused source review

Disposition: PASS for this conditional-support source block after the portability correction below. No unresolved material science finding. This is not a formal audit, retained-grade certification, or integration/landing PASS.

Scope: complete note and main runner; supplied candidate JSON (all arrays loaded, dimensions/finiteness inspected); complete 18-row result and independent output/checker; all five pack files. Frozen base is f389e89fe84e2584ee85047f08da88c1443eb163. The note, primary runner and candidate were hashed at review entry and remained unchanged. Supplied upstream provenance is PR9671 head a96cefd1901938c6e4b6155a3576477d78ed6c87; this review validates the stored numerical candidate conditionally, not an independent derivation or re-extraction of that upstream model. No repository edits, audits, commits, pushes or merges performed by this reviewer.

## Finding and resolution

The first independent checker hardcoded the author's temporary checkout and temporary output path. That prevented portable replay. The author changed its root to Path(__file__).resolve().parents[2] and output to the sibling independent.json. I reread the corrected complete checker and executed it from a relocated temporary copy: all eight checks passed, producing byte-identical independent.json. This finding is resolved in this same reviewer session.

## Scientific assessment

The grand-canonical free-fermion Hessian has the stated sign and all-ordered-pair normalization. Its coincident-energy limit is beta f(1-f); retaining the complete degenerate block makes the expression basis independent. The staggered operator connects k and k+Q. Counting the full-zone 12-band Kubo sum once per original cell is correct; the full-zone 24-band folded free energy requires the extra half. The independent checker instead uses 32 representatives of the 64-point mesh and correctly omits that half.

The nonzero imaginary-frequency expression follows by pairing the two ordered spectral terms. Exact degeneracies have zero isolated dynamical contribution; they retain an equilibrium divided-difference contribution. The finite-grid relation between the two limits is correct with the stated numerical degeneracy convention. This does not assert a continuum limit or relaxation mechanism.

The four node levels give sum(lambda_i^2)/(2 T N^3), which reduces to lambda^2/(T N^3) for the equal singular values. The source vertex is explicitly normalization dependent. The proposed mean-field curvature is G^-1-chi, with G explicitly absent from the free model; the text does not promote the curvature crossing to a phase, propagating scalar, local interaction or canonical Yukawa coupling. Conserved uniform H0 has zero isolated commutator response even where its isothermal variance response is nonzero. This narrow identity is not a global no-go. Temperature, chemical potential, finite meshes, chosen matrix/flux and pseudoscalar-channel identification remain supplied inputs. The one-qubit/block and cosmological bridges are expressly unproved.

## Checks

- Exact temporary-copy main runner replay: 44/44 controls; result.json byte-identical to submitted output.
- Relocated corrected independent checker: 8/8 controls; independent.json byte-identical.
- Independent frequency formula check: directly summed (f_a-f_b)|M_ba|^2/(E_b-E_a-i omega), rather than the runner's real paired expression, at all five recorded frequencies for N=4,T=.03. Real parts agree to displayed floating precision; residual imaginary part at most 4.6e-13.
- Manual verification of the divided-difference sign, folded/full-zone normalization, complete degenerate-block contribution, four-node Curie factor, conditional threshold, and conserved-operator distinction.
- Input arrays have shapes (7,3), (7,12,12), and (12,12), with finite entries; all 18 recorded state/mesh rows were inspected. No certified error bound or thermodynamic convergence was inferred.

Review covers the final source identities below. Later combined mechanical validation and current-main preservation remain separate coordinator gates. No formal audit was requested or performed.

## SHA-256 identities

```text
2d248272c10c663808b2b998115167cfb008d18e3c0a9db36a98bfb1a57e58f9  .claude/science/physics-loops/collective-corner-response-20261017/HANDOFF.md
aa4b80bf4569411a365ff07be6eabc1c1f92165b16a854e0d6742c73747a5ae8  .claude/science/physics-loops/collective-corner-response-20261017/INDEPENDENT_MATRIX_CHECK.md
9fa59634b6f392d43125a6874979b65f9f5ad6de4aefa26782d1778e7997dfc3  .claude/science/physics-loops/collective-corner-response-20261017/INDEPENDENT_RESPONSE_MATH.md
a8cc3122c7a172d20d155378a559a3d21e67bd85fafb4e5f151db9035c2f75bd  .claude/science/physics-loops/collective-corner-response-20261017/STATE.yaml
07c7a2a6602a9d18a8c97fb6160f63141adf6ee330b11d274972dc31da9cbf2e  .claude/science/physics-loops/collective-corner-response-20261017/UPSTREAM_REPLAY.txt
b4c2bc8c25dafa7c529a96f3109331924eb428d2b363ec765f66fd1efc1e0588  data/collective_corner_response/candidate.json
2999a80428c6adf26119d0512f7fe855ea1adb1b0741e69e8608e82535fc9916  docs/COLLECTIVE_CORNER_RESPONSE_NOTE_2026-10-17.md
4fca3461b39844d4eaf342e67732bd34a5d9017b935a9dda4d6f1b040d4868d9  outputs/collective_corner_response/independent.json
b9d4b814c5b9c6e57b4cc882068a8a7f3a70c8bdc07e8e59deac58f889f17d5b  outputs/collective_corner_response/independent_check.py
4ff4f1d7e822c2a827a5f40c07a4948b1a48e3a586b6781348af81f49ed7900f  outputs/collective_corner_response/mutation_check.py
5c2a601f62f4e70e5b0b55b1eade5c73e5ed432ea27ac74ec8d1d35b2df943ed  outputs/collective_corner_response/mutations.json
3d5db9eb01c3b614ffe5dcae8242c57d1114c0b9d580594e98907d3b8f80b697  outputs/collective_corner_response/result.json
50d5e6149515d710509e1fc71a10c50ff50cea187211bd64a8254b972ecef83f  scripts/collective_corner_response.py
```
