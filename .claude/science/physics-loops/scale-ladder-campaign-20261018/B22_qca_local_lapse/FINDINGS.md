# B22 findings: does a unitary step have a local lapse, and does it close like the Hamiltonian?

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back.

| Runner | Result |
|---|---|
| `b22_cut_1d.py` | PASS=6 (6 s) |
| `b22_generator_1d.py` | PASS=7 (132 s) |
| `b22_generator_3d.py` | PASS=6 (207 s) |
| first 3D run | PASS=2 FAIL=4 with preset thresholds; log kept |

Disclosures: the 3D thresholds were rewritten as scaling checks after the first run; nothing was fitted. A cut-test bug in runner 1 was fixed, and that log was overwritten.

**Short answer.** "Local lapse for a step" has two inequivalent definitions.
- **A**, the step's own causal timing, does not reduce to the Hamiltonian bracket.
- **B**, a smooth lapse built from the step's generator, does: the shift is ξ = g·w, with g the node's cone metric.

So B17's premise (a) can be met for steps, but only through B. That is a choice; the circuit does not force it.

## Definition A: causal cuts

- **C1 (exact, trivial).** Path independence holds for any layered circuit (6e−16), because causally unordered gates act on disjoint wires. It carries no bracket information.
- **C2 (exact).** Row j of W_F equals row j of the uniform evolution by λ_j layers.
- **C3.** The fixed-operator commutator is far from 1: ‖C − 1‖ = 2.
- **C4 (exact defect lemma).** A cut whose total count changes by T has at least T odd-count wires. In the massless walk each of them flips chirality. So lattice-scale defects appear at a density ∝ |∇N|, the same order as the v²w term.
- **C5.** Packet displacements miss the Dirac-algebra value:
  - right-movers: −0.77, −2.46, −8.84;
  - left-movers: +0.90, +2.18, +8.56;
  - against −0.39, −1.57, −6.28.

  Interband loss is 5–16%. Smooth real lapses fail grossly. The massive walk gives no clean limit.

## Definition B: generator lapse

Take H_F = i log W, H(N) = ½{N̂, H_F} and W_N = exp(−iH(N)). For integer constant N this is exactly W^n.

- **Prediction, declared before running (first-order Moyal).** [H(N), H(M)] = −i G[g·w] near a node, with g = Hess(ω²/2). The sign is Lorentzian automatically.
- **1D.**
  - The symbol residual is 1e−12 (massless) and 9e−7 to 3e−4 (massive), scaling as q².
  - The speed that enters is the node's cone, v² = θ cot θ, within 6e−5 to 5e−4. The light-cone speed 1 is excluded.
  - Packets are displaced by −w g(k0) within 2.4% (A = 32) and 1% (A = 16).
- **3D, 64³ and 96³.**
  - **Isotropic step** W_iso = e^{−ik_xσ_x}e^{−ik_yσ_y}e^{−ik_zσ_z}, which has the minimal automaton's dispersion; the matrices were not compared with D'Ariano–Perinotti. Its bracket tends to −i v² G[w]. The deviations, 6.0% to 17.8% over kc = 0.13–0.45, are roughly linear, consistent with the automaton's linear anisotropy.
  - **Uniaxial toy** with metric diag(1, 1, 4). The bracket is the direction-weighted shift g^{jj}w_j, B17's derivative part. The best-fit κ is (1.0025, 3.9994), so there is no common κ.
  - **Exponentiated packets.** The ratio −w g^{aa} is matched below 0.1% at Lx = 8192. Along z on the uniaxial step the ratio is 3.997.

## Obstacles

1. **The node must sit at quasi-energy 0.**
   - An offset E adds a lapse-weighted current, not a translation (P2).
   - The walk's species at quasi-energy π misses the form by a factor of 6.2.
   - The generator of W² (lapse in two-step units) works for both.
   - Inference, not computed: the corner step, with nodes at ±π/2, needs −W².
2. **Gaplessness.** A branch cut through a band makes H_F non-local, |H_r| ~ 1/r. The low-energy bracket is unaffected, but W_N is then only quasi-local.
3. **The density is not unique.** Improvements leave the band-projected leading bracket unchanged, but change the interband part. A and B are themselves inequivalent.
4. **Definition B is not path independent.** That is expected; closure with gravity takes over that role.

## Status of B17's premise

- It holds for steps under Definition B at leading order, with the caveats above.
- The uniaxial doublers get direction-weighted shifts, so B17's rejection carries over. For the corner step this is an inference from the symbol identity plus the measured cone metrics; its circuit was not run.
- The premise is not realised by causal timing (Definition A).

## Not tested

The spin term, non-uniform w, interband parts for 12-band steps, interacting steps, and whether any other identification of cut data avoids the defect lemma.

## Prior art (unverified)

- Arrighi–Facchini–Forets 2014 (their re-encodings plausibly correspond to the defect lemma).
- Bisio–D'Ariano–Tosini 2015; D'Ariano–Perinotti 2014; Bisio–D'Ariano–Perinotti 2016.
- Di Molfetta–Brachet–Debbasch 2013; Arnault–Debbasch; Mlodinow–Brun 2018.
- Tomonaga–Schwinger; Kuchař; HKT; Torre–Varadarajan 1999.
- Gambini–Pullin; Destri–de Vega; GNVW.
