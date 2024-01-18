import pandas as pd

fileName = ''

df = pd.read_excel(fileName, skiprows=1)

def getPredecessors(df, activity, main=None):
    print('now on ' + activity.strip())

    if main is None:
        main = [[activity]]

    predec_row = df[df['Activity ID'] == activity]

    if predec_row.empty:
        print(activity.strip() + ' is empty')
        return main

    predecessors = predec_row['(*)Predecessors'].iloc[0]

    if pd.isna(predecessors):
        print(activity.strip() + ' has no predecessors')
        return main

    predecessors = predecessors.split(',')

    new_main = []  # Create a new list to store updated branches

    for m in main:
        for predecessor in predecessors:
            new_branch = m.copy()  # Create a new list for each branch
            new_branch.append(predecessor.strip())
            print('added ' + predecessor.strip() + ' to ' + str(new_branch))
            new_main.append(new_branch)
            new_main.extend(getPredecessors(df, predecessor.strip(), [new_branch]))
        print('done with ' + predecessor.strip() + ' now on ' + activity.strip() + '\n')

    return new_main

def cleanup(main):
    # Use a set to store unique sublists
    unique_sublists = set(tuple(sublist) for sublist in main)

    # Create a new list with unique sublists
    unique_list = [list(sublist) for sublist in unique_sublists]

    for i in unique_list.copy():
        for j in unique_list.copy():
            if set(i).issubset(set(j)) and i != j:
                if i in unique_list:
                    unique_list.remove(i)

    # Print the result
    for sublist in unique_list:
        print(sublist)

if __name__ == '__main__':
    main = getPredecessors(df, 'CGS9663858')
    cleanup(main)
