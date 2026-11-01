lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-01T19:34Z

# Excess: Lemma EX, Lemma EX2, (COMP)(ii)

Queue item 7 of `FINISH.md`, mapped side, frozen at commit `d9d4496f1`. Research-stage working state. Grants no status.

Status: started 2026-11-01T07:34Z. Sections appear below as they are written.

## 0. Working summary (updated as sections land)

**Frozen statements.** Lemma EX, Lemma EX2, (COMP) as printed in `library/sector-values.md` at `d9d4496f1`, read with `gates/lemma-ex-7c12c6981.md` and `gates/closure-bad958abb.md`.

**New route for Lemma EX (under test in this file): no symbol, no IMS, no gauge patch.** The one-level excess is, up to second-order remainders, an exact sum of local variances:

    E_j(U) - E_{j+1}(M U) = sum_{y, p} L^4 Var_{chi_y^p}(F^{(y)}_p) - remainders,

because the coarse plaquette angle is L^2 times an average of fine plaquette angles against a tent-tent-box-box kernel chi_y^p, and these kernels are a partition of unity on fine plaquettes. Overlapping tents control the in-plane coarse gradient, and a discrete Bianchi identity bounds the transverse gradient by exactly twice the in-plane one (sharp at p = (1,1,1,0), a = e_4, which is the gate's minimiser of c_e). Nothing global is read, so sectors and torons do not enter.
