import pandas as pd

def consulta_na(dataframe: pd.DataFrame):
    """ 
    lista todos os registros que possuem dados faltantes do dataframe.
    
    Parâmetros
    ___
    dados: um dataframe

    Retorno
    ___
    Return: lista os registros com dados faltantes
    """
    ausentes = dataframe.isna().sum()
    return print(f'{ausentes}')


