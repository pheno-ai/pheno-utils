# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/13_questionnaire_handler.ipynb.

# %% auto 0
__all__ = ['convert_to_string', 'tranform_answers']

# %% ../nbs/13_questionnaire_handler.ipynb 3
import pandas as pd
import numpy as np

# %% ../nbs/13_questionnaire_handler.ipynb 4
# Here is a function that can convert a column to string, removing '.0' from floats

def convert_to_string(x):
    return str(int(x)) if isinstance(x, float) and x.is_integer() else str(x)

# Usage:
# df['column_name'] = convert_to_string(df['column_name'])


def tranform_answers(tab_field_name: str, orig_answer: pd.Series, transform_from: str, transform_to: str, 
                     dict_df: pd.DataFrame, mapping_df: pd.DataFrame) -> pd.Series:
    code_from = transform_from.lower()
    code_to = transform_to.lower()
    assert code_from in ['hebrew', 'english', 'coding']
    assert code_to in ['hebrew', 'english', 'coding']
    
    # the index of the dict_df is the tabular_field_name
    if isinstance(dict_df.loc[tab_field_name]['data_coding'], pd.Series):
        code_string = convert_to_string(dict_df.loc[tab_field_name]['data_coding'][0] )
    else: 
        code_string = convert_to_string(dict_df.loc[tab_field_name]['data_coding'])
    code_df = mapping_df[mapping_df['code_number'] == code_string].copy()
    coding = dict(zip(code_df[code_from].astype(int).astype(str), code_df[code_to]))
    return orig_answer.astype(str).replace(coding)

