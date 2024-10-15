from pydantic import BaseModel

class Candidate(BaseModel):
    name: str
    position: str
    political_party: str
    election_year: str
    qttVotes: int
    uf: str
    municipality : str
