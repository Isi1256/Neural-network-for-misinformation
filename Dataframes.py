import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the JSON file into a Pandas DataFrame
df_LOCO = pd.read_json("LOCO.json")

df_LOCO_LFs = pd.read_json("LOCO_LFs.json")

seeds_stats = df_LOCO["seeds"].value_counts()

print(type(seeds_stats))

conspiracy_names = seeds_stats.index[:30]
counts = seeds_stats.values[:30]

# Create a horizontal bar chart
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
plt.barh(conspiracy_names, counts, color='skyblue')
plt.xlabel('Count')
plt.title('Conspiracy Name Counts')
plt.gca().invert_yaxis()  # Invert y-axis to display the highest count at the top
output_folder = 'plots'
os.makedirs(output_folder, exist_ok=True)
plt.savefig(os.path.join(output_folder, 'my_plot.png'))
plt.show()

pass
