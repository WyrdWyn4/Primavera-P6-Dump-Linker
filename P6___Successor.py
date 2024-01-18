import pandas as pd

fileName = ''
df = pd.read_excel(fileName, skiprows=1)

def getSuccessors(df, activity):
    print('now on ' + activity.strip())

    predec_row = df[df['Activity ID'] == activity]

    if predec_row.empty:
        print(activity.strip() + ' is empty')
        return

    Successors = predec_row['(*)Successors'].iloc[0]

    if pd.isna(Successors):
        print(activity.strip() + ' has no Successors')
        return

    Successors = Successors.split(',')
    for i, successor in enumerate(Successors.copy()):
        for j, success2or in enumerate(Successors.copy()):
            if i == j: continue
            if i in SetOfSuccessors(j):
                Successors.remove(i)
    return

def SetOfSuccessors(df, activity, succ=set()):
    predec_row = df[df['Activity ID'] == activity]

    if predec_row.empty:
        print(activity.strip() + ' is empty')
        return succ

    Successors = predec_row['(*)Successors'].iloc[0]

    if pd.isna(Successors):
        print(activity.strip() + ' has no Successors')
        return succ
    
    Successors = Successors.split(',')

    for successor in Successors:
        succ.add(successor.strip())
        succ.update(SetOfSuccessors(df, successor.strip(), succ))
    
    return succ

successors = SetOfSuccessors(df,'MS-S-20')
print(successors)