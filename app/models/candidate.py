from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    position: str
    politicalParty: str
    electionYear: str
    qttVotes: int
    uf: str
    municipality : str
