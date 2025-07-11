import pandas as pd

def limpa_dados_NAN(dataframe: pd.DataFrame):
    """Remove todas as linhas que contêm valores NaN de um DataFrame.

    Args:
        dataframe (pd.DataFrame): O DataFrame de entrada que será limpo.

    Returns:
        pd.DataFrame: O DataFrame com todas as linhas contendo valores NaN removidas.

    Notes:
        - A remoção é feita inplace, ou seja, o DataFrame original é modificado.
        - Não há tratamento adicional para outros tipos de valores ausentes (ex.: None, strings vazias).
    """
    dataframe.dropna(inplace=True)
    return dataframe