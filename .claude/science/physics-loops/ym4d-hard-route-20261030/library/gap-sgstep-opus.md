lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-14T18:47Z

# gap-sgstep-opus (queue row 944): the one-step sub-Gaussian score (SG-step) for the SU(2) Wilson slice chain

Started 2026-11-14T06:47Z on the Mac mini worker, Claude Opus 5.5 at max effort, as AUTHOR. Pinned at commit
a90db3999 on branch claude/ym4d-hard-route. Research-stage working state; no status is granted by this file.
Labels: PROVED, CONDITIONAL (on named inputs), GUIDE (a run or a heuristic; refutes or guides only), OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Inputs. Read `library/gap-direction-max.md` Steps 5-7, `library/gap-etohc-opus.md` (definition of (SG-step),
   Corollary HC2) and `library/gap-etohc-check-astra.md` (the SGC correction). Record the exact statement of
   (SG-step)_sigma, the slice chain, pi_u, the score, and which form (supremum over u, averaged, normalized z)
   Proposition HC and (E-to-HC) really consume. Duplicate check: grep `library/open-core.md` and the FINISH rows.
2. Structure of the score. Write phi_(u,z) explicitly for the Wilson slice chain on (24a)^3: a sum over the links
   of the slice of bounded one-link forces, coupled through the spatial plaquettes of the next slice. Fact test on
   the free photon (sigma^2 = beta e^(-omega) at most beta per mode).
3. Key question. Is sigma necessarily volume-free? Decide whether sub-Gaussianity at a volume-free sigma follows
   from compactness and the one-link bound alone (Hoeffding type plus a decoupling or martingale argument), or
   fails; if it fails, give the volume growth and say whether a normalized z or the averaged form repairs it.
4. Attack. Prove the strongest form reachable (supremum form, or the averaged form, or the pair of Corollary HC2),
   with sigma explicit; or isolate the exact missing input.
5. Fact tests. U(1) and the frozen groups: (SG-step) is group-blind, so it must hold for them and must not imply a
   gap on its own.
6. GUIDE run if memory allows (one job, machine lock): sample the score on a small box to test the constants.
7. Literature and credit: Sussman-Alpoge account and library on the Mini, and any published inequality used.
8. Verdicts, what stays open, RESULT line.

## 1. Inputs and the exact statement (step 1)

(in progress)
