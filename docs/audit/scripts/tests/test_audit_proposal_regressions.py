"""Synthetic repair regressions; no auditor, API, or production ledger writes."""
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace as NS
from unittest import mock

ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(ROOT/'scripts'), str(ROOT/'docs/audit/scripts'), str(Path(__file__).parent)]
import codex_audit_runner as runner
import audit_science_fingerprint as science
from test_audit_science_fingerprint import PremiseScopedFingerprintTest


class PremiseGrammarRepairs(PremiseScopedFingerprintTest):
    def test_indented_and_deep_unmapped_prefixes_reject(self):
        original = (self.root/'docs/AXIOM.md').read_text()
        for heading in (' ### Extra', '   #### Extra', '###### Extra'):
            with self.subTest(heading=heading):
                self._write('docs/AXIOM.md', original.replace('### Alpha', heading+'\n\nNormative condition.\n\n### Alpha'))
                with self.assertRaises(science.ScienceFingerprintError):
                    science.build_science_fingerprint(self._declared_target(['axiom:beta']), self.rows, self.root)

    def test_preamble_is_bound_but_history_is_not(self):
        row = self._declared_target(['axiom:beta'])
        self.assertEqual(self._change_after(row, lambda: self._edit_memo('## Axioms\n', '## Axioms\n\nAll clauses require P.\n')), 'science_changed:premise_unit:axiom:beta')

    def test_default_policy_does_not_scope_a_declaration(self):
        with mock.patch.object(science, 'SCOPED_PREMISE_FINGERPRINTS_ENABLED', False):
            fp = science.build_science_fingerprint(self._declared_target(['axiom:beta']), self.rows, self.root)
            self.assertEqual(fp['schema'], science.SCIENCE_FINGERPRINT_SCHEMA)
            self.assertIsNotNone(fp['framework_premise_epoch'])


class BackendRepairs(unittest.TestCase):
    def backend(self, message, cap=None):
        self.calls = []
        class Stream:
            def __enter__(inner): return inner
            def __exit__(inner, *args): return False
            def get_final_message(inner): return message
        def stream(**kwargs):
            self.calls.append(kwargs)
            return Stream()
        factory = lambda *args: NS(beta=NS(messages=NS(stream=stream)))
        return runner.ClaudeAuditBackend(runner.ClaudeKeyPool(['TEST'], {'TEST':'synthetic'}), runner.ClaudeSpend(cap), client_factory=factory)

    def invoke(self, backend):
        # Transport exception types only; the fake client does not use an SDK.
        fake_sdk = NS(AuthenticationError=type('Auth', (Exception,), {}), APIStatusError=type('Status', (Exception,), {}), APIConnectionError=type('Connection', (Exception,), {}))
        with mock.patch.dict(sys.modules, {'anthropic': fake_sdk}):
            return backend.run('fixture', None, 1, model='claude-opus-5-5')

    def message(self):
        return NS(id='synthetic', model='claude-opus-5-5', stop_reason='end_turn', usage={'input_tokens':1000,'output_tokens':1000}, content=[{'type':'text','text':'{"answer":1}'}])

    def test_stream_continuation_and_actual_serving_identity(self):
        m=self.message()
        m.content=[{'type':'text','text':'{"answer":'}, {'type':'fallback','from':{'model':'claude-opus-5-5'},'to':{'model':'claude-opus-4-8'}}, {'type':'text','text':'1}'}]
        m.usage['iterations']=[{'type':'message','model':'claude-opus-5-5','input_tokens':1000,'output_tokens':1000}, {'type':'fallback_message','model':'claude-opus-4-8','input_tokens':1000,'output_tokens':1000}]
        b=self.backend(m);ok,reply,error=self.invoke(b)
        self.assertTrue(ok,error);self.assertEqual(json.loads(reply),{'answer':1})
        self.assertEqual(b.last_call['served_model'],'claude-opus-4-8')
        self.assertEqual(len(b.last_call['usage']['iterations']),2)
        self.assertAlmostEqual(b.spend.spent_usd,0.054)
        with mock.patch.object(runner,'CLAUDE_AUDIT_ENABLED',True):
            row={'audit_status':'audit_in_progress','cross_confirmation':{'status':'awaiting_second','first_audit':{'auditor_family':'claude-opus-4.8'}}}
            self.assertEqual(runner.determine_audit_role(row,runner.claude_family_for_model(b.last_call['served_model'])),('second','fresh_context'))

    def test_ambiguous_restarted_json_and_inconsistent_chain_reject(self):
        m=self.message();m.content.append({'type':'text','text':'{"answer":2}'})
        self.assertFalse(self.invoke(self.backend(m))[0])
        m=self.message();m.content.insert(0,{'type':'fallback','from':{'model':'unrelated'},'to':{'model':'claude-opus-4-8'}})
        self.assertFalse(self.invoke(self.backend(m))[0])

    def test_repeat_and_repair_cannot_cross_exhausted_threshold(self):
        b=self.backend(self.message(),cap=0.001)
        self.assertTrue(self.invoke(b)[0])
        with self.assertRaises(runner.ClaudeCreditsExhausted): self.invoke(b)
        self.assertEqual(len(self.calls),1)
        b=self.backend(self.message(),cap=0)
        with self.assertRaises(runner.ClaudeCreditsExhausted): self.invoke(b)
        self.assertEqual(self.calls,[])

    def test_sdk_reserved_field_alias_and_unknown_identity(self):
        self.assertEqual(runner._claude_value(NS(from_={"model":"m"}), "from"), {"model":"m"})
        m=self.message();m.model=None
        self.assertFalse(self.invoke(self.backend(m))[0])

    def test_threshold_is_rechecked_before_key_rotation(self):
        b=self.backend(self.message(),cap=1)
        fake_sdk=NS(AuthenticationError=type('Auth',(Exception,),{}), APIStatusError=type('Status',(Exception,),{}), APIConnectionError=type('Connection',(Exception,),{}))
        class Stream:
            def __enter__(self): raise fake_sdk.AuthenticationError()
            def __exit__(self,*args): return False
        requests=[]
        def stream(**kwargs): requests.append(kwargs);return Stream()
        b.client_factory=lambda *args:NS(beta=NS(messages=NS(stream=stream)))
        with mock.patch.dict(sys.modules, {'anthropic':fake_sdk}), mock.patch.object(b.spend,'exhausted',side_effect=[False,True]):
            with self.assertRaisesRegex(runner.ClaudeCreditsExhausted,'threshold'):
                b.run('fixture',None,1)
        self.assertEqual(len(requests),1)

    def test_iteration_cost_excludes_top_level_duplicate(self):
        spend=runner.ClaudeSpend(None)
        usage={'input_tokens':999999,'output_tokens':999999,'iterations':[{'model':'claude-opus-5-5','input_tokens':1000,'output_tokens':1000}]*2}
        self.assertAlmostEqual(spend.add('claude-opus-5-5','claude-opus-5-5',usage),0.048)

    def test_production_transport_and_role_stay_inactive(self):
        self.assertFalse(runner.CLAUDE_AUDIT_ENABLED)
        self.assertEqual(runner.determine_audit_role({'audit_status':'unaudited'},'claude-opus-5.5')[0],'skip')
        with self.assertRaisesRegex(RuntimeError,'unactivated'):
            runner._default_claude_client('never-used',1)


if __name__ == '__main__': unittest.main()
