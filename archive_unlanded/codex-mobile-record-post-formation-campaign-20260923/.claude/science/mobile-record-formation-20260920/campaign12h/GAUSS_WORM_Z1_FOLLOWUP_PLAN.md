# Targeted follow-up of the fugacity-one signal

Written before follow-up production. Selection is explicitly adaptive: the first
18-case screen showed nearly flat low-mode spectra and agreement of empty/full
starts at z=1, while z=4 had severe sector trapping and z=.2 lacked the planned
minimum blocks. The old cases remain unchanged and separately reported.

Reuse the exact sampler implementation, changing only the job list and seeds.
Single A species, z=1; L=17,25,33,49; empty and fully +e1 starts; eight jobs.
Seeds20260921400 through20260921407 in ascending L then initialization.
Burn100,000,000 attempted head moves and production1,000,000,000 per job.
Eight threads maximum; every closed-state visit is sampled. The initial plan's
exact Gauss/content checks and four mode definitions are unchanged.

Analyze each initialization separately, with the original128-sample block
bootstrap and a declared sensitivity check at1024 samples. Fewer than16 full
blocks at either size is flagged. Report occupation, both spectral ratios,
flux changes, run lengths, block lag dependence and first/last-half means.
No pooling, extrapolated exponent, equilibrium certification, phase transition,
formation-selected state or quantum-vacuum identification. A flat finite-size
signal cannot exclude a correlation length larger than these boxes. Independent
sampler review is still pending when this plan is written.
