# Interface: a mass gap and NT1, NT2 (the later target)

Status: neutral interface note, 2026-11-01, author-side, not reviewed. It is not on the critical path (`GOAL.md`: the mass gap is a later target) and it changes no status here. It proves nothing new: each step is two lines from a statement already in this folder or in PR #10114. **Independent-side workers skip this file.** It cites #10114, an AI-written account of the soft-kernel route. Mapped-side and neutral readers may use it.

## Objects

- Reconstruction: Theorem 10.2(d) of `parts/upper-chain.md`, giving a Hilbert space with vacuum Omega and H >= 0, exp(-s H) Omega = Omega, on the bounded family B.
- NT1, NT2: `GOAL.md`. (WIT), (WIT+): `parts/upper-chain.md`, Text 10. Theorem 4.1 and Corollary 4.2: `parts/witness.md`.
- Gap (G): ker H = span{Omega} and spec(H) on Omega-perp lies in [m_*, infinity), m_* > 0. This is the form of rows MG1 and MG3 of `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_TARGET.md` on branch `claude/ym4d-proof-draft` (#10114). Row MG4 there asks separately for Omega-perp != {0}.

## Statements

**I1 (gap with a non-empty excited sector gives NT1).** If (G) holds and Omega-perp != {0}, then H != 0 on Omega-perp, since H >= m_* > 0 there. []

(G) alone does not give NT1: a gap on Omega-perp = {0} is vacuous. Hence the order below.

**I2 (the witness gives a non-empty excited sector, MG4).** (WIT) gives Omega-perp != {0}. Proof: Text 10 of `parts/upper-chain.md`, after (WIT+). A non-zero connected correlator gives, by Cauchy-Schwarz with the reflection, a non-zero [A]_perp. Theorem 4.1's hypothesis c(x) != c(x') already contains a non-zero connected correlator, so (WIT+) or Corollary 4.2 does as well. []

**I3 (the converse fails).** NT1 gives no gap. Theorem 4.1 already says this: spectral measure at 0 on Omega-perp is not excluded, and NT1 does not imply a unique vacuum. The quantitative remark after Theorem 4.1 bounds the top of the spectrum on a cyclic subspace, not the bottom.

**I4 (a gap excludes the gate's static law).** The static random constant field of `gates/net-tier-upper-chain-c3242879df.md`, D1, has a reflected connected correlator independent of time, hence a non-zero spectral weight at 0 on Omega-perp. It therefore violates ker H = span{Omega}. Any law with (G) and a non-empty excited sector passes the NT1 test that D1 fails. []

**I5 (where NT2 enters).** I1, I2 give only a non-empty, dynamical excited sector, which a free (Gaussian) limit also has. The non-freeness and identification asked by #10114 (rows MG4 "non-trivial" and MG5, Yang-Mills identification) are what NT2 supplies: the three-gluon-vertex part at leading order, with g_r running. A gap theorem does not replace NT2, and NT2 does not give a gap.

## Conditions for combining

The two routes combine only on a common hierarchy: same group (SU(2) here), same trajectory beta_i, same blocking or a proved comparison (hard constraint here, soft kernel in #10114), and an observable family containing B, or dense in the same reconstruction. #10114's gap is conditional. `MASS_GAP_CROSSOVER_REDUCTION.md` on `claude/ym4d-proof-draft` reduces it to one open crossover estimate (CW) plus source transport (MG2), and closes no MG row. Nothing here is a claim of a gap.

Compatibility check: (G) and the scale-r Gaussian value of Theorem 10.7 do not conflict, since r is far below 1/m_* along the trajectory, where decay at rate m_* is invisible.
