import pytest
from src.agents.courtroom import SupremeCourtSwarm, LegalCase

@pytest.mark.asyncio
async def test_courtroom_guilty_verdict():
    swarm = SupremeCourtSwarm()
    case = LegalCase(
        case_id="TX-2026-99", 
        description="Software theft", 
        evidence=["Logged IP", "Copied Code"],
        defendant_name="John Doe",
        severity_level=5
    )
    
    verdict = await swarm.adjudicate(case)
    
    assert verdict.case_id == "TX-2026-99"
    assert verdict.is_guilty is True
    assert verdict.sentencing is not None
    assert verdict.prosecutor_argument.agent_role == "Prosecutor"

@pytest.mark.asyncio
async def test_courtroom_not_guilty_verdict():
    swarm = SupremeCourtSwarm()
    case = LegalCase(
        case_id="NY-2026-12", 
        description="Minor infraction", 
        evidence=["Hearsay"],
        defendant_name="Jane Doe",
        severity_level=2
    )
    
    verdict = await swarm.adjudicate(case)
    
    assert verdict.is_guilty is False
    assert verdict.sentencing is None
    assert "dismissed" in verdict.judge_ruling.lower()
