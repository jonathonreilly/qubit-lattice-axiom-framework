"""Finalize existing research only after verified deadline/heartbeat closure."""
import datetime
import hashlib
import json
from pathlib import Path
import shutil

R = Path(__file__).resolve().parent
W = Path('/Users/jonBridger/.codex/worktrees/observations-backward-24h-20261014/New Axioms Lets Go')
P = W / '.claude/science/physics-loops/observations-backward-24h-20261014'
C = P / 'closing'
now = datetime.datetime.now(datetime.timezone.utc)
assert now >= datetime.datetime.fromisoformat('2026-10-15T21:48:44+00:00')
shutdown = json.loads((R / 'DEADLINE_SHUTDOWN_v1.json').read_text())
retirement = json.loads((R / 'HEARTBEAT_RETIREMENT_v1.json').read_text())
assert shutdown['status'] == 'no_owned_research_process_found_matching_lock_released'
assert shutdown['matching_processes'] == []
remaining = shutdown['lock_after'].get('lock') or {}
assert not (remaining.get('owner') == 'direct-author-observations-backward' and remaining.get('holder_id') == '01a130f9-fd7f-7d31-9f8f-ac05cdf2c617')
assert retirement['confirmed_deleted'] is True
assert retirement['automation_id'] == 'observations-backward-24-hour-campaign'
for name in ['DEADLINE_SHUTDOWN_v1.json', 'HEARTBEAT_RETIREMENT_v1.json']:
    shutil.copyfile(R / name, C / name)

report = P / 'FINAL_REPORT.md'
text = report.read_text()
old_opening = text.split('\n\n', 2)[1]
assert 'deadline shutdown verification remains pending' in old_opening
opening = ('The fixed 24-hour campaign has ended. It ran from 2026-10-14 21:48:44 UTC '
           'to 2026-10-15 21:48:44 UTC (5:48:44 PM America/New_York). Scientific discovery '
           'was frozen before the final packaging period; no new discovery was begun after '
           '21:33:44 UTC. The actual shutdown check at ' + shutdown['checked_at'] +
           ' found no campaign-marked research process outside the administrative process '
           'and its ancestors. The matching cooperative lock was released, the three previous '
           'campaigns remain stopped, and the completed campaign heartbeat was deleted. '
           'Closing documentation and delivery checks are administrative work after the fixed '
           'research window; the clock was not extended.')
text = text.replace(old_opening, opening, 1)
start = text.index('## Deadline closure — pending final process check')
end = text.index('## Closing source receipts', start)
closure = ('## Deadline closure\n\n'
           'All 18 campaign PR heads matched the saved inventory at 2026-10-15T21:32:59Z '
           'and all were open. PR #9620 and its full 91-path scientific diff were checked, '
           'and its attachment to this chat was confirmed. The table freezes scientific '
           'delivery heads; later closing-document commits may advance PR #9620 without '
           'changing scientific source. The earlier read-only inventory comparison failed '
           'on an absent baseRefOid metadata key; that failure and the corrected head-only '
           'comparison are preserved.\n\n'
           'The at-or-after-deadline process check found no campaign-marked worker to stop. '
           'The three prior saved statuses are completed/cancelled and retain no worker or '
           'supervisor PID. The cooperative lock release checked both owner and holder ID. '
           'The app confirmed deletion of the completed heartbeat at ' + retirement['recorded_at'] +
           '. See [the shutdown receipt](closing/DEADLINE_SHUTDOWN_v1.json) and '
           '[the app retirement receipt](closing/HEARTBEAT_RETIREMENT_v1.json). '
           'These operational checks do not establish physical validity of the theory. '
           'The timed campaign is complete; the fundamental scientific objective remains unresolved.\n\n')
text = text[:start] + closure + text[end:]
text = text.replace('Actual deadline closure remains pending.',
                    'Actual deadline closure is recorded above; no subsequent scientific calculation is claimed.')
text += ('\nThe displayed M20 equations and inventory wording received a separate narrow '
         '[presentation check](closing/FINAL_EQUATION_DISPLAY_REVIEW_v1.md). The complete '
         'scientific report had already received the scoped synthesis reviews v1/v2; '
         'the final shutdown delta is checked separately. Historical drafts and pending '
         'receipts remain preserved as time-stamped history.\n')
report.write_text(text)
(R / 'FINAL_REPORT_AT_DEADLINE_v1.md').write_text(text)

for path in [P / 'STATE.yaml', R / 'STATUS.json', R / 'DIRECT_AUTHOR.json']:
    state = json.loads(path.read_text())
    state.update(status='completed', phase='completed_fixed_deadline', completed_at=now.isoformat(),
                 updated_at=now.isoformat(), last_checkpoint_at=now.isoformat(),
                 fixed_deadline='2026-10-15T21:48:44Z', research_window_extended=False,
                 scientific_objective_complete=False,
                 scientific_outcome='Conditional reconstruction/consistency results; no TOE or independent empirical validation of the scalar action.',
                 current_block_status='published_conditional_result_campaign_closed',
                 active_route=None, next_working_block=None, next_milestone=None,
                 next_action='No automatic research remains. Preserve results and unresolved physical/theoretical suppliers for a future explicitly requested campaign.',
                 worker_pid=None, supervisor_pid=None, owned_research_processes=[], owned_processes=[],
                 lock_status='matching_lock_released', heartbeat_status='DELETED',
                 closing_draft=str(report), closing_draft_scope='Completed campaign report; scientific objective remains unresolved.',
                 last_published_head_scope='Last scientific delivery; closing-document Git HEAD is recorded separately in runtime FINAL_DELIVERY_v1.json.',
                 checkpoint_scope='Fixed-deadline closure with process/lock/app receipts; no new discovery or scientific execution.',
                 shutdown_receipt='closing/DEADLINE_SHUTDOWN_v1.json',
                 retirement_receipt='closing/HEARTBEAT_RETIREMENT_v1.json')
    path.write_text(json.dumps(state, indent=2) + '\n')
with (P / 'HANDOFF.md').open('a') as handle:
    handle.write('\n## Campaign closed at its fixed deadline — ' + now.isoformat() +
                 '\n\nNo new discovery after21:33:44Z. The original21:48:44Z research window has ended. '
                 'Fresh process inventory found no campaign-marked research worker; the matching owner/holder '
                 'lock was released and the completed heartbeat deleted through the app. All three prior '
                 'campaigns remain stopped. FINAL_REPORT.md and closing receipts preserve the observation '
                 'comparisons, strongest conditional mathematics, real failures and surviving assumptions. '
                 'The timed campaign is complete; action selection, actual initial state/history, absolute '
                 'scales and physical measurement/environment suppliers remain unresolved. No TOE or independent '
                 'empirical validation is claimed. Closing-document verification/delivery only remains.\n')
with (P / 'REVIEW_HISTORY.md').open('a') as handle:
    handle.write('\n## Closing scientific synthesis\n\nComplete synthesis reviews v1/v2, packaging delivery '
                 'check174/0 and final equation-display report read by root. The final equation display is a '
                 'presentation of already checked M20 equations, not new discovery. The930path content '
                 'inventory pins the scientific delta. Final operational shutdown delta receives a separate '
                 'narrow check; no scientific rerun or formal audit.\n')
with (P / 'PR_BACKLOG.md').open('a') as handle:
    handle.write('\nCampaign research window ended2026-10-15T21:48:44Z. No additional scientific PR is '
                 'queued by this campaign. Closing report/receipts will be added to existing PR9620; '
                 'all earlier scientific units remain preserved. No merge or main push.\n')
automation = json.loads((R / 'AUTOMATION.json').read_text())
automation.update(status='DELETED', retired_at=retirement['recorded_at'],
                  retirement_action='delete', retirement_receipt='HEARTBEAT_RETIREMENT_v1.json',
                  retirement_reason='Fixed 24-hour campaign complete; no scheduled research continuation.')
(R / 'AUTOMATION.json').write_text(json.dumps(automation, indent=2) + '\n')
receipt = {'created_at': now.isoformat(), 'science_commit': '414856e9c2195680af563678a0844af71de3ddfb',
           'fixed_deadline': '2026-10-15T21:48:44Z', 'report_sha256': hashlib.sha256(report.read_bytes()).hexdigest(),
           'scope': 'Existing scientific report finalized with actual deadline closure; narrow final-delta review and document delivery remain.',
           'closure_receipts': {name: hashlib.sha256((C / name).read_bytes()).hexdigest()
                                for name in ['DEADLINE_SHUTDOWN_v1.json', 'HEARTBEAT_RETIREMENT_v1.json']}}
(R / 'FINAL_REPORT_CLOSURE_v1.json').write_text(json.dumps(receipt, indent=2) + '\n')
(C / 'FINAL_REPORT_CLOSURE_v1.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt, indent=2))
