from fastapi import FastAPI
from src.agents.courtroom import SupremeCourtSwarm, LegalCase, CourtVerdict

app = FastAPI(title="AI Supreme Court", version="1.0.0")
swarm = SupremeCourtSwarm()

@app.post("/trial", response_model=CourtVerdict)
async def run_trial(case: LegalCase):
    """
    Submits a case to the AI Supreme Court.
    The swarm of LLM agents will debate and issue a ruling.
    """
    verdict = await swarm.adjudicate(case)
    return verdict

@app.get("/health")
def health_check():
    return {"status": "The court is in session"}
