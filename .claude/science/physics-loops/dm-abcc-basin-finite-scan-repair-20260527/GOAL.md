# Goal

Repair `dm_abcc_basin_finite_search_support_note_2026-04-30` enough to make it
reauditable without importing the old retained basin chart as a proof input.

The audit blocker was that the prior primary runner hard-coded the five
archived basin coordinates and expected signature labels. This block adds a
new primary runner that derives the active-chamber finite-scan representatives
from the Hermitian pencil, PMNS angle residuals, retained sigma set, coordinate
box, and active chamber inequality.

Non-goal: prove global A-BCC chart exhaustiveness. The branch keeps that as an
open interval/root-isolation problem.
