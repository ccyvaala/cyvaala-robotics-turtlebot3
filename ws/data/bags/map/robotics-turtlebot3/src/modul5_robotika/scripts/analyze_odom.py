import pandas as pd

df_straight = pd.read_csv('data/results/m05_straight.csv')
df_rotation = pd.read_csv('data/results/m05_rotation.csv')

print("--- Summary Straight Motion ---")
print(df_straight[['e_odom', 'e_fisik', 'delta_odom_fisik']].agg(['mean', 'std', 'min', 'max']))

print("\n--- Summary Rotation Motion ---")
print(df_rotation[['e_theta_odom', 'e_theta_imu']].agg(['mean', 'std', 'min', 'max']))
