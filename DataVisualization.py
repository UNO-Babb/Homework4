import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inputFile = "output.csv"
outputGraph = "graph.png"

def main():

    df = pd.read_csv(inputFile)
    df['Arrive'] = df['Arrive'].values // 3600 # convert to hours
    #dataset =  df.groupby('Arrive')['Car_Number'].count()
    dataset = df.groupby('Arrive')['Wait'].mean()
    print(dataset)
    #wait = data['Wait'].values
    plt.style.use('fivethirtyeight')
    dataset.plot.bar()
    plt.savefig(outputGraph)

if __name__ == '__main__':
    main()
