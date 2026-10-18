# Focused pole-component envelope review

Disposition: mathematical/source scope PASS subject to one narrow displayed Parseval correction sent to root. The canonical time-dependent norm equality omitted exp[2t Im E_lambda(p)]; it must include that damping factor or be explicitly restricted to t=0. The later decay formula and proofs already use the correct damping, so this is a local formula fix rather than a failed envelope argument.

The fourth-order endpoint-to-COM conversion is correct. One-end changes h=1,2 shift the center by +/-h/2, giving 2a_h cos(hp/2). The resulting coefficients (19/32)gamma and -(13/128)cos p, and zero-relative-momentum symbol c(p)=29/192+19gamma/16-13cos(p)/64 agree with the independent native K4 check. The linked support classification excludes missing rigid long-interval translations at order four and confines short-interval corrections to boundary matrices. The existing canonical/local gauge transfer applies between these external ker K1 states in each momentum fiber. c(0)=109/96 is recovered.

The refined real-p expansion and uniform normalized-residue convergence are the prior complete fixed-order coefficient results, not newly selected effective dynamics. At lifetime time T0/(Jz lambda^4), the uniform O(Jz lambda^(14/3)) pole error yields O(lambda^(2/3)) phase error. Outgoing damping bounds both multipliers. Parseval then gives the L2 envelope comparison without differentiating the exact error. The weaker fast correction contributes only lambda log(1/lambda) phase error. The failed fixed-complex-momentum fast-arm argument remains open and is not silently assumed.

For integer readout displacement x, Fourier translation by k lambda² produces the displayed positive sign in exp[ik T0 sin(p/2)]. L2 translation continuity suffices for a general fixed L2 profile f; derivatives are taken only of the smooth approximation. Twice Im e4 gives the mass factor exp[-T0 g], so neither a factor of two nor an energy-unit factor is missing. The characteristic transform is explicitly an unnormalized positive measure of the squared defined kernel. Its normalization, if later chosen, would still not make it a physical particle probability.

The helper is a finite FFT control of the smooth approximation with T0=1. It removes only momentum-independent real phases, which do not change intensity. The leading momentum phase, Airy phase, complex e4 damping, and scaled position factor are consistent with the theorem. Its interpolated host data are development inputs computed from the supplied outgoing host. Two-grid agreement and small edge mass test resolution/aliasing for the reported controls; they are not rigorous continuum error bounds. The artificial rapid-phase stress is plainly labeled as such and tests only the multiplier inequality, not a demonstrated native correction. The runner's native JSON checks and its binding of the proof, helper, host and original coefficient data are consistent.

The canonical scope is appropriate: a defined outgoing pole component of the fixed-order response, not proof of pole dominance, full-H resonance, a microscopic ballistic particle, or physical scalar coupling. The complete background remains an explicit obstacle. Current-main audit-only changes and unrelated PR9761 do not alter this source result and were not treated as science inputs or as retirement of the native bridge. No audit, landing, or repository edits performed. Existing independent native and Fourier-lemma reports were reused; no redundant FFT rerun required.

## Reviewed source hashes before narrow formula fix

- `docs/NATIVE_COMPOSITE_POLE_ENVELOPE_NOTE_2026-10-18.md`: `e3280733a5f7093bdf3b64981065fc0a15b900232ca8ef811d669dbc7c723c25`
- `scripts/native_pole_envelope.py`: `42e5db87ba8fa2ee3de1892455459ff9f19f944043cbdd96f059e409089a916e`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLE_ENVELOPE_PROOF.md`: `4cb2897c3b9f87de57ecc279dd9491eb697ce41358bdf7a30bfa2ef027e9dab3`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_COM_FOURTH.md`: `2f1dcf3baff595a07fa1e7b920defac35134923d685e0d72961fa454bc53d64b`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_POLE_ENVELOPE.md`: `259c550379331388fe9382f45ce5277df9f3b468b831bed3cd896e2085ca5633`
- `.claude/science/physics-loops/neutral-composite-24h-20261018/native/neutral_envelope_model.py`: `aae00ba68cf3276c4be79e37ff4cafbf5981295e6533c4fa87de896dbb4ee25b`

## Final affected-fix confirmation

PASS: the canonical Parseval equality now includes exp[2t Im E(p)], correctly accounting for outgoing damping. This resolves the sole material finding above; all previously reviewed scope and mathematics remain unchanged. No broader rereview or repository edits performed.

Final canonical note SHA256: `e3280733a5f7093bdf3b64981065fc0a15b900232ca8ef811d669dbc7c723c25`.
