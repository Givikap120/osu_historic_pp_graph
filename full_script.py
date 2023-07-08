import pandas as pd
import numpy as np
import math

# ENTER SCORES FILENAME AND PLAYER NICKNAME HERE
filename ='Scores.csv'
playername = 'Givikap120'

# Enter your bonus pp for more accurate results
current_bonus_pp = 231.324
ranked_scores_count = round(math.log(1 - current_bonus_pp / 416.6667, 0.9994))
print(f'Estimated amount of ranked scores - {ranked_scores_count}')
# It calculates approximation of your bonus pp

#filename = input('Enter filename: ')
#playername = input('Enter playername: ')

df = pd.read_csv(filename)
df = df[df.playerName == playername] # only certain player
df = df[df.beatmapID != 0] # only submitted maps
df = df[df.beatmapSetID != -1] # only submitted mapsets
df = df.sort_values('unixTimestamp') # sort from oldest to newest
df = df[(df.modsLegacy & 128) == 0] # remove relax
df = df[(df.modsLegacy & 8192) == 0] # remove autopilot
df['timestamp'] = pd.to_datetime(df['unixTimestamp'], unit='s') # add formatted time
df = df[['timestamp', 'pp']] # remove unnecessary

# Scores lower than {precision} will be ignored, significiant performance boost with pisslow accuracy reduce
precision = 250

# osu! pp system use 0.95 as weighting coefficient
coef = 0.95

scores_pp = np.empty((0, 2), dtype=np.float64)

input_array = df.to_numpy()
output_array = []
bonus_pp_modifier = ranked_scores_count / len(df)

for i, row in enumerate(input_array):
    pp = row[1]

    if scores_pp.shape[0]:
        scores_pp_temp = scores_pp[:,0]
        index = np.searchsorted(-scores_pp_temp, -pp, side='left')
        if index > precision:
            continue
    else:
        index = 0
        

    pp_weighted = pp * math.pow(coef, index)
        
    scores_pp = np.insert(scores_pp, index, [pp, pp_weighted], axis=0)
    scores_pp[index + 1:,1] *= coef

    pp_sum = scores_pp[:,1].sum()
    bonus_pp = 416.6667 * (1 - 0.9994 ** (i * bonus_pp_modifier))
    total_pp = pp_sum + bonus_pp
    
    output_array.append([row[0], pp, pp_sum, bonus_pp, total_pp])

    if i % 100 == 0:
        print(total_pp)
print(total_pp)
print('Calculations done!')

output_filename = 'scores_result.csv'
output_df = pd.DataFrame(output_array, columns=['timestamp', 'pp', 'pp_sum', 'bonus_pp', 'total_pp'])
output_df.to_csv(output_filename, index=False)
print(f'Saved into file {output_filename}')

import matplotlib.pyplot as plt
output_df.plot(x='timestamp',y='total_pp')
plt.grid(True)
plt.show()
