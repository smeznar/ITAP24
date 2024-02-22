import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def height_weight_dataset(path):
    male_heights = np.random.normal(177, 7.11, 700) / 100
    woman_heights = np.random.normal(162.57, 6, 300) / 100
    heights = np.concatenate((male_heights, woman_heights))
    bmi_percentage = np.array([0.018, 0.319, 0.672, 0.945])
    bmi_scale = [(11, 18.4), (18.5, 24.9), (25, 29.9), (30, 39.9), (40, 45)]
    bmi_scale = [(h-l, l) for l, h in bmi_scale]
    weight = []
    for i in range(1000):
        s = np.sum(bmi_percentage < np.random.random())
        weight.append((np.random.random()*bmi_scale[s][0]+bmi_scale[s][1])*heights[i]**2)
    weights = np.array(weight)
    sex = ["Male" for i in range(700)] + ["Female" for i in range(300)]
    df = pd.DataFrame(data={"Height": heights, "Weight": weights, "Sex": sex})
    df.to_csv(path, index=False)


def weight_dataset(path):
    height = np.random.normal(170, 6.5, 1000) / 100
    bmi = np.random.normal(23.5, 2, 1000)
    weight = bmi * height**2
    df = pd.DataFrame(data={"Height": height, "Weight": weight})
    df.to_csv(path, index=False)


if __name__ == '__main__':
    height_weight_dataset("../Podatki/vaje1_train.csv")
    a = pd.read_csv("../Podatki/vaje1a_train.csv")
    sns.scatterplot(a, y="Height", x="Weight", hue="Sex")
    plt.show()
      
    height_weight_dataset("../Podatki/vaje1_test.csv")
    a = pd.read_csv("../Podatki/vaje1a_test.csv")
    sns.scatterplot(a, y="Height", x="Weight", hue="Sex")
    plt.show()
  
    weight_dataset("../Podatki/vaje1b_train.csv")
    a = pd.read_csv("../Podatki/vaje1b_train.csv")
    sns.scatterplot(a, y="Height", x="Weight")
    plt.show()
  
    weight_dataset("../Podatki/vaje1b_test.csv")
    a = pd.read_csv("../Podatki/vaje1b_test.csv")
    sns.scatterplot(a, y="Height", x="Weight")
    plt.show()