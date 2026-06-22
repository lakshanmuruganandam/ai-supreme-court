from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import asyncio

class LegalCase(BaseModel):
    case_id: str
    description: str
    evidence: List[str]
    defendant_name: str
    severity_level: int = Field(..., ge=1, le=5)

class Argument(BaseModel):
    agent_role: str
    statement: str
    confidence_score: float

class CourtVerdict(BaseModel):
    case_id: str
    prosecutor_argument: Argument
    defense_argument: Argument
    judge_ruling: str
    is_guilty: bool
    sentencing: Optional[str] = None

class SupremeCourtSwarm:
    def __init__(self):
        self.court_name = "AI Supreme Court - Autonomous Division"

    async def _run_prosecutor(self, case: LegalCase) -> Argument:
        await asyncio.sleep(0.1) # Simulate LLM thinking
        base = f"The defendant, {case.defendant_name}, is unequivocally liable."
        ev_str = f"The evidence ({', '.join(case.evidence)}) proves this beyond a reasonable doubt."
        return Argument(agent_role="Prosecutor", statement=f"{base} {ev_str}", confidence_score=0.92)

    async def _run_defense(self, case: LegalCase) -> Argument:
        await asyncio.sleep(0.1) # Simulate LLM thinking
        base = f"The prosecution's claims against {case.defendant_name} are entirely circumstantial."
        return Argument(agent_role="Defense", statement=base, confidence_score=0.85)

    async def adjudicate(self, case: LegalCase) -> CourtVerdict:
        # Agents run their analysis concurrently
        prosecutor, defense = await asyncio.gather(
            self._run_prosecutor(case),
            self._run_defense(case)
        )
        
        await asyncio.sleep(0.2) # Simulate Judge LLM reviewing
        
        # Judge logic
        if case.severity_level >= 4 and len(case.evidence) > 1:
            is_guilty = True
            ruling = "The court finds the evidence overwhelming. The prosecution's argument holds."
            sentencing = "Maximum penalty simulated."
        else:
            is_guilty = False
            ruling = "The defense has successfully established reasonable doubt. Case dismissed."
            sentencing = None
            
        return CourtVerdict(
            case_id=case.case_id,
            prosecutor_argument=prosecutor,
            defense_argument=defense,
            judge_ruling=ruling,
            is_guilty=is_guilty,
            sentencing=sentencing
        )
