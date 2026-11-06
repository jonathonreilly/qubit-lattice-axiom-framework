lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:13Z

# p20-gate: referee of b109.md Lemma P20 (depth-uniform quadratic-radius tower estimate (110))

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, branch claude/ym4d-hard-route at 285da4077. One line-by-line reading by one model. Not an audit, not human review.

Status: in progress. Sections are written as the check proceeds.

## 1. Scope and what P20 reads

Refereed: `library/b109.md` P19 (lines 3312-3338) and P20 (lines 3340-3456), with premises (104)-(105) (lines 3200-3215) and the ceilings at lines 3342, 3440-3443, 3646-3649.

P20's proof reads these inputs. None of P1-P18 is read by P20.

- P19 (109), the real-point Taylor inequality.
- (86), the perturbed-plaquette expansion of P16 (line 2676), for (111).
- (107), the one-step relative-angle inequality of section 11.2 (a1-balaban section 3.5, actual-mean form section 7.6), for the raw datum increment.
- `a1-balaban.md` (8.2), the real critical-orbit theorem, linear in the datum radius, conditional on F0.
- `a1-balaban.md` (9.1)-(9.2), the uniform datum ball and the holomorphic axial representative, with the second-order (Euler-equation) estimate.
- `a1-balaban.md` (3.6) and section 7, the plaquette-averaging recursion, for the datum radius of a real field.
- `flat-port.md` sections 4-9, which supply F0.
- CA-I 34178-34189 and CA-I (4.8:eq-tower-rules-b), the collar bound, for the interior.

The outline treats the same statement. SA Theorem 5(a), lines 9746-9753, states (110) with K^sharp(alpha_0' + alpha_1'^2). SA mechanism 8, lines 9899-9911, sketches the proof: the P19 inequality without its constant, the plaquette formula (111) as a display, and "Theorem 1 is linear in the datum". So P20 is a proof of a step the outline sketches. It is not a correction of their text.

Source pins: SA `YM4_sketch_500.tex` and CA-I `theorem_0_complete_account_raw_I.tex` at 31a47c543775, fetched to a scratch folder; CMP 109 OCR at `~/ym4d-papers/cmp109.txt`, pp. 262-263.
