from pandas import read_csv
def update_csv(method,eplained_inertia):
    df = read_csv("../results/results.csv",index_col=[0])
    df.loc[method]=eplained_inertia
    df.to_csv("../results/results.csv")
    