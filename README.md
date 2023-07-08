# osu_historic_pp_graph
Can draw a graph of your pp over time. It uses McOsu for pp calculation.

How to use it?
1) Install McOsu - https://store.steampowered.com/app/607260/McOsu/
2) Launch McOsu and select your main profile
3) Open profile top ranks
4) Press on gear and select `Import osu! Scores of ...`
5) Press Shift+F1 and type `osu_scores_export` in the console
6) Go to the McOsu folder, find exported scores file, and copy it into some folder
7) Download my Python scripts and throw them into the same folder
8) Open `full_script.py` with notepad
9) Change lines with `filename` and `playername` accordingly
10) (Optional) Change the line with `current_bonus_pp` with your bonus pp. You can find it here - https://pp.huismetbenen.nl/rankings/players/live
11) Install Python (if you didn't)
12) Install numpy, matplotlib and pandas with Pip (if you didn't). If you don't know how - google `how to install python libraries`
13) Launch `full_script.py` to calculate and visualize graph
14) Launch `only_plot.py` to only visualize graph
