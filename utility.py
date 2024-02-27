def calc_wer(df, group_by=None, suffix=''):
    if suffix:
        if group_by:
            wer = (df.groupby(group_by)['num_del'+suffix].sum() + df.groupby(group_by)['num_ins'+suffix].sum() + df.groupby(group_by)['num_sub'+suffix].sum()) / df.groupby(group_by)['num_words'+suffix].sum()
        else:
            wer = (df['num_del'+suffix].sum() + df['num_ins'+suffix].sum() + df['num_sub'+suffix].sum()) / df['num_words'+suffix].sum()
    else:
        if group_by:
            wer = (df.groupby(group_by)['num_del'].sum() + df.groupby(group_by)['num_ins'].sum() + df.groupby(group_by)['num_sub'].sum()) / df.groupby(group_by)['len_ref'].sum()
        else:
            wer = (df['num_del'].sum() + df['num_ins'].sum() + df['num_sub'].sum()) / df['len_ref'].sum()
    return wer
