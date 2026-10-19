# C1c WORKLOG — long production with C1b's validated finite-T PT QMC (cubic spin-1/2 link ring model)

## RESUME (read first after a container restart)
- Raw data and checkpoints live OUTSIDE the block in /tmp/claude-0/c1c_raw/{raw,ckpt,locks}
  (NOT durable; `blocks/C1c/data/raw` and `data/ckpt` are symlinks to them). If /tmp was wiped, the runs
  cannot resume; C1b's originals of the seeded continuations are in blocks/C1b/data/{ckpt,raw}.
- Relaunch all workers (idempotent; flock prevents running a tag twice; run_pt.py resumes from ckpt):
    cd blocks/C1c/scripts && ./launch.sh 1635
  (argument = UTC HHMM after which no new 15-min chunk is started).
- Status of each tag: `ls /tmp/claude-0/c1c_raw/raw | sed 's/_c.*//' | sort | uniq -c`; per-chunk JSON in
  logs/prod_chunks.jsonl (written by run_pt.py), worker logs logs/queue_w{1,2,3}.log.

## Provenance
- scripts/*.py and scripts/queue.sh copied UNCHANGED from blocks/C1b/scripts (sha256 in
  data/source_hashes_C1b.sha256, verified identical after copy). data/ladders/ copied unchanged.
- New thin wrappers only: scripts/worker.sh (dynamic 3-worker queue, flock per tag), scripts/launch.sh,
  scripts/jobs_C1c.txt. No change to the kernel, driver, measurement, or analysis code.
- Seeded continuations: C1b ckpt+raw chunks of L4_s3, L4_s4, L6_s4, L8E_s3 copied (hashes recorded) into
  /tmp/claude-0/c1c_raw/; those runs continue with the same tag (chunk index continues). These are the
  C1b *clean* runs (loops off at beta>1 for the first 2000 sweeps). New runs: L6_s3 (canonical, seed 203),
  L8E_s5 (start mixW_rot with one replica = axis-rotated canonical state, W=0, seed 305). NOLOOP_SWEEPS=2000
  for all (irrelevant for continuations, which are past 2000 sweeps).

## Plan and criteria (declared 08:57 UTC 2026-10-19, before any C1c data)
- Criteria: C1b's pre-declared criteria UNCHANGED (C1b WORKLOG 01:32/03:35/03:40; C1b NOTE §4):
  EQ (>=2 starts, E, <W^2>, S_T(q1) agree within 2.5 sigma, >=10 round trips), C-W/X-W on a(L)=L*dF1 at
  beta=L with K(L)=<W_a^2>, TI-vs-direct agreement, S_T exponent windows, 20% discard, 20 bins,
  combined error = max(binned, seed scatter). Analysis with C1b's analyze_prod.py / ti.py / drift.py /
  energy_L8.py unchanged; each tag's FULL series (C1b chunks + C1c chunks) is one run.
- Supplementary (reported, not a verdict input; from C1b NOTE §9.2 recommendation): per-chunk P1(beta=L)
  drift table for both starts; the user's stopping target "z<2 between starts" is reported alongside the
  declared 2.5-sigma rule.
- L=8 energy: declared criterion from C1's review: combined error <= 0.15 needed to discriminate
  C1's -443.83(14) from repo -443.364(31). E(beta=16) >= E0 one-sidedly; a value significantly (>2 sigma)
  below -443.364 would indicate the repo value lies above E0. Error = max(binned, scatter of the 2 starts).
- Fixed schedule (no data-dependent stopping): L4_s3/L4_s4: 14 new 15-min chunks each (target 17 total);
  L6_s3/L6_s4 and L8E_s3/L8E_s5: as many chunks as the budget allows (targets 40+). Priority tiers
  L4 > L6 > L8E, 3 workers; no chunk starts after 16:35 UTC; analysis 16:55-17:30.

## Log
- 08:56 launched workers w1 (L4_s3), w2 (L4_s4), w3 (L6_s3/L6_s4 alternating; after L4 finishes the
  workers move to L6 and then L8E per tiers).
