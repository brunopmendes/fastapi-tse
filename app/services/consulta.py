from models.candidate import Candidate
import pandas as pd


def read_data_and_convert_all_columns_to_string(data_path):

    df = pd.read_csv(data_path, encoding='latin1', delimiter=';')
    df = df.astype(str)
    return df


def query_candidates(year: int, uf: str, municipality: str, position: str):

    df = read_data_and_convert_all_columns_to_string('data/AC_1T.csv')
    df_candidates = df[
        (df['ANO_ELEICAO'] == year) & 
        (df['SG_UF'] == uf) & 
        (df['NM_MUNICIPIO'] == municipality) & 
        (df['DS_CARGO_PERGUNTA'] == position)
    ]
    return df_candidates


def filter_df(list_filter: list, year: int, uf: str, municipality: str, position: str):
    
    df = query_candidates(year, uf, municipality, position)
    if list_filter:
        df_filtered = df[list_filter]
    else:
        df_filtered = df
    
    return df_filtered


def get_candidates(year: int, uf: str, municipality: str, position: str):
    
    filter_list = ["NM_VOTAVEL", "NM_PARTIDO", "ANO_ELEICAO", "QT_VOTOS", "NM_MUNICIPIO", "DS_CARGO_PERGUNTA", "SG_UF"]
    df = filter_df(filter_list, year, uf, municipality, position)

    df['QT_VOTOS'] = pd.to_numeric(df['QT_VOTOS'])
    df_grouped = df.groupby(["NM_VOTAVEL", "NM_PARTIDO", "ANO_ELEICAO", "NM_MUNICIPIO", "DS_CARGO_PERGUNTA", "SG_UF"], as_index=False).agg({"QT_VOTOS": "sum"})

    candidates = []
    for _, row in df_grouped.iterrows():
        candidate = Candidate(
            name = row["NM_VOTAVEL"],
            political_party=row["NM_PARTIDO"],
            election_year=row["ANO_ELEICAO"],
            municipality=row["NM_MUNICIPIO"],
            position=row["DS_CARGO_PERGUNTA"],
            qttVotes=row["QT_VOTOS"],
            uf=row["SG_UF"]
        )
        candidates.append(candidate)
    return candidates

