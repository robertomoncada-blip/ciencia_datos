def crear_features(df):
    # índice de habilidades
    skill_cols = [col for col in df.columns if 'Skill_' in col]
    df['Skill_Index'] = df[skill_cols].mean(axis=1)

    # variable target binaria (ejemplo)
    df['High_Risk'] = (df['Automation_Probability_2030'] > 0.7).astype(int)

    return df