from pandas import read_csv
from numpy import mean
from pandas import DataFrame

def update_csv(method,eplained_inertia):
    df = read_csv("../results/results.csv",index_col=[0])
    df.loc[method]=eplained_inertia
    df.to_csv("../results/results.csv")

repeats = 5
end_step = 100
def remake_dfs(dataset_len):
    df = DataFrame(columns=[int(dataset_len*i/end_step) for i in range(1,end_step+1)])
    df.to_csv("../results/tranform_time_results.csv",mode='w+')
    df.to_csv("../results/fit_time_results.csv",mode='w+')

import time
def measure_time(f):
    start = time.time()
    f()
    return time.time()-start

def measure_fit_time(method,fit,dataset):
    # measure fit time
    df = read_csv("../results/fit_time_results.csv",index_col=[0])
    df.loc[method] = [mean([measure_time(lambda: fit(dataset[:int(dataset.shape[0]*modifier/end_step)])) for _ in range(repeats)]) for modifier in range(1,end_step+1)]
    # measure transform time
    df.to_csv("../results/fit_time_results.csv")
    
def measure_transform_time(method,transform,dataset):
    # measure transform time
    df = read_csv("../results/tranform_time_results.csv",index_col=[0])
    df.loc[method] = [mean([measure_time(lambda: transform(dataset[:int(dataset.shape[0]*modifier/end_step)])) for _ in range(repeats)]) for modifier in range(1,end_step+1)]
    # measure transform time
    df.to_csv("../results/tranform_time_results.csv")
    
    