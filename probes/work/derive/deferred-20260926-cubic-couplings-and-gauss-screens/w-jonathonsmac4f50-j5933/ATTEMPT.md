# Proper-cubic eleven couplings and the five-versus-eleven classification, refereed

- **Task:** `J:derive:deferred-20260926-cubic-couplings-and-gauss-screens:a1`
- **Worker:** `w-jonathonsmac4f50-j5933`
- **Model:** Claude Opus 5.5 (`claude-opus-5-5`)
- **Provenance.** The sources are Codex files: campaign12h, and frozen #8569 at `508722df2e`. This is a cross-family referee. Codex's own independent check (`proper_cubic_extension_independent/`) is same-family.
- **Prior attempts.** None existed on `ai/probes` for this problem at claim time.
- **Obligation chosen** (one per attempt). Referee, with disjoint machinery, the proper-cubic eleven-coupling extension (`PROPER_CUBIC_ELEVEN_COUPLINGS_AND_VECTOR_SELECTION.md`). With it, recover #8569's five-versus-eleven classification and the distinction between raw-vector Gauss closure and derivative-curl closure.

## Sources

**Packet** `probes/work/deferred-science-20260926/mobile-record-formation-20260920/campaign12h/`, with SHA256:
- `PROPER_CUBIC_ELEVEN_COUPLINGS_AND_VECTOR_SELECTION.md`: `d7833106…4070`;
- `proper_cubic_extension_independent/REPORT.md`: `4b16425c…b39`.

**Frozen #8569** (at `508722df2e`). The note was read in full for the definitions:
- `docs/MOBILE_RECORDS_CUBIC_SYMBOL_SELECTION_AND_GAUSS_CLOSURE_BOUNDED_THEOREM_NOTE_2026-09-21.md`: `a1e8be3e…76f1`;
- its runner: `3807ae95…536e`.

Both hashes match `SOURCE_MAP.json`. The runners were not used.

No `correction_ack` exists for this packet.

## (1) Statement

**The setting.**
- Take the 15-state alphabet (vacancy, 6 polar axis labels, 8 axial cube labels), linearised at the uniform law on its 14-dimensional tangent.
- Use the note's orthonormal observables `(E; s1, s2, B, d1, d2, t12, t13, t23, w)`.
- Consider real symmetric first-order symbols `A(q) = Σ q_i A_i` satisfying `R(Q)A(q)R(Q)ᵀ = A(Qq)`.

**What holds.**
- Such symbols form a space of dimension **11** under the 24 proper signed permutations, and **5** under all 48.
- The author's eleven explicit maps (#8569's five plus `b1, b2, b_u, b_v, d, g`) are a basis of the proper space.
- **Raw closure.** Closure of the six raw-vector observables for arbitrary other moments, and preservation of `q·E = q·B = 0`, are each equivalent to `a1 = a2 = u = v = b1 = b2 = b_u = b_v = 0`.
- **Derivative-curl closure.** Closure of the pair `([q]×B, [q]×E)` is equivalent to `u = v = b_u = b_v = 0`.
- **The remaining statements hold as the note states them:**
  - the `d, g` block and its determinant;
  - the reversal parities;
  - the rank-10 spectrum;
  - #8569's Gram formula;
  - the `15/2` current normalisation.

## (2) Steps (all CHECKED exactly by `check.py`)

1. **K0.** The alphabet, the 24- and 48-element signed-permutation actions (with `b → det(Q)Qb`), and the orthonormal tangent observables are rebuilt from the note's text.
2. **K1 (disjoint from character sums).** Write symbols in species space: `S_i = Uᵀ A_i U`, symmetric with zero row sums. Covariance then becomes `P(Q) S_i P(Q)ᵀ = Σ_j Q_{ji} S_j`, a rational linear system. It is imposed for the generators, the 90° rotations about `z` and `x`, and for inversion.
   - The exact nullspaces over ℚ have dimensions 11 (proper) and 5 (full).
   - The author and #8569's independent report counted these with character sums. This route does not use them.
3. **K2.** All eleven explicit maps satisfy `R(Q)A(q)R(Q)ᵀ = A(Qq)` exactly, with `R = U P(Q) Uᵀ`.
   - Their coefficient vectors have rank 11, so by K1 they span the space.
   - Exactly `a1, a2, m, u, v` are also inversion covariant.
4. **K3.** The closure conditions are polynomial identities in `q`, solved for all eleven coefficients at once.
   - (a) Vector rows vanishing on nonvector columns.
   - (b) The Gauss constraints preserved on the subspace `q·E = q·B = 0`, with arbitrary other moments.
   - Both (a) and (b) give the same eight zeros; `m`, `d` and `g` stay free.
   - (c) `[q]×` of the vector rows kills the nonvector columns and the longitudinal `E` and `B` inputs. This gives only `u = v = b_u = b_v = 0`.
   - Specialised to #8569's five, (a) and (b) leave only `m`. (c) removes only the two tensor couplings `u` and `v`, as #8569 states.
5. **K4.** The `(t12, t13, t23) × (d1, d2, w)` block equals the note's matrix, with determinant `−6√3 d² g q1 q2 q3`.
6. **K5.** `T = diag(−I3, I11)` is odd on the original five and even on the six additions.
7. **K6.** With only `m`, `d`, `g` nonzero, at `q = (1, 2, 3)`, the rank is 10: ten nonzero speeds and four zeros.
8. **K7.** #8569's `K Kᵀ` formula holds as a polynomial identity.
9. **K8.** At the uniform law, `J_a = 2p_a[(Sp)_a − pᵀSp]` has tangent derivative `(2/15)S` whenever `S1 = 0`, so `S = (15/2) U A Uᵀ` realises `A`.

## (3) Where it stops

- **No defect was found.** The extension's statements and #8569's classification hold as written.
- **Not refereed here:** the positivity of the four-site local context-exchange generator realising every map. K8 checks only the normalisation.
- **Frozen #8565 was not addressed:**
  - the reachable-background birth-locality counterexample;
  - the low-fugacity polymer assumptions;
  - the loop ensemble.
- **Not addressed:** the Gram-kernel cubic formation response, the centred-Gauss staggered sectors, and the Gauss-worm screens.
- **The research target is open:** a local formation or transport mechanism that selects the raw constraints.

## (4) What would finish it

- **(i)** Referee #8565's birth-locality counterexample and the polymer premises.
- **(ii)** Construct, or rule out, a local irreversible formation law whose stationary sector keeps `q·E = q·B = 0`. By K3, such a law would have to switch off the eight couplings.

## ASSUMED

The supplied model of #8569: the alphabet, the uniform law, entropy compatibility and first order. Nothing else is imported.

## Reproduce

```bash
python3 probes/work/derive/deferred-20260926-cubic-couplings-and-gauss-screens/w-jonathonsmac4f50-j5933/check.py
```

The run takes about 3 s.
