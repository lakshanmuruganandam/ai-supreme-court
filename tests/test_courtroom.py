import pytest
from src.agents.courtroom import SupremeCourtSwarm, LegalCase

@pytest.mark.asyncio
async def test_courtroom_adjudication():
    swarm = SupremeCourtSwarm()
    case = LegalCase(case_id="TX-2026-99", description="Software theft", evidence=["Logged IP", "Copied Code"])
    
    verdict = await swarm.adjudicate(case)
    
    assert verdict.case_id == "TX-2026-99"
    assert "NOT GUILTY" in verdict.judge_ruling
    assert "Logged IP" in verdict.prosecutor_argument
