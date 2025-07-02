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

def consulta_na_porcentagem(dataframe: pd.DataFrame):
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
    ausentes = round(((ausentes / len(dataframe)) * 100),2)

    return print(f'{ausentes}')



