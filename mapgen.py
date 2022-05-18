import random
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

mape = [[0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
print(mape)
for i in range (0, 10):
    for j in range (0, 10):
        mape[i][j] = random.randrange(1, 101)
for i in range (0, 10):
    for j in range (0, 10):
        if mape[i][j] < 11:
            mape[i][j] = 5 #enemy
        elif 11 <= mape[i][j] < 20:
            mape[i][j] = 15 #water
        elif 20 <= mape[i][j] <40:
            mape[i][j] = 30 #forest
        elif 40 <= mape[i][j] <50:
            mape[i][j] = 45 #path
        elif 60 <= mape[i][j] <70:
            mape[i][j] = 65 #wall
        elif 70 <= mape[i][j] <75:
            mape[i][j] = 72 #cave
        elif 75 <= mape[i][j] <80:
            mape[i][j] = 77 #dungeon
        elif 80 <= mape[i][j] <95:
            mape[i][j] = 87 #soil
        elif 95 <= mape[i][j] <100:
            mape[i][j] = 97 #town
df = pd.DataFrame(mape)
print(df)
myColors = ('r', 'b', 'g', '#bd8d7b', '#697689', '#673ab7', '#9f0500', '#795548', 'c')
cmap = LinearSegmentedColormap.from_list('Custom', myColors, len(myColors))
mapy = sns.heatmap(df, cmap=cmap)
colorbar = mapy.collections[0].colorbar
colorbar.set_ticks([7, 18, 29, 40, 51, 62, 73, 84, 95])
colorbar.set_ticklabels(['Enemy', 'Water', 'Forest', 'Path', 'Wall', 'Cave', 'Dungeon', 'Soil', 'Town'])
plt.show()
