import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
import os

# Create cache directory if it doesn't exist
cache_dir = 'cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)

# Enable cache for faster data retrieval
fastf1.Cache.enable_cache(cache_dir)

# Load the race session
session = fastf1.get_session(2024, 'Italy', 'R')
session.load()

# Get all Leclerc's laps
lec_laps = session.laps.pick_driver("LEC")

# Print all Leclerc's laps to identify the pit stop lap
print(lec_laps[['LapNumber', 'PitInTime', 'PitOutTime']])

# Identify Leclerc's pit stop lap
lec_pit_lap = lec_laps[lec_laps['PitInTime'].notna()].iloc[0]

# Print the identified pit stop lap
print(f"Leclerc's pit stop lap: {lec_pit_lap['LapNumber']}")

# Get laps in his second stint (after his pit stop)
lec_second_stint = lec_laps[lec_laps['LapNumber'] > lec_pit_lap['LapNumber']]

# Select a lap where Leclerc was managing tires (e.g., mid-stint)
lec_tire_saving_lap = lec_second_stint[lec_second_stint['LapNumber'] == 39].iloc[0]

# Select Leclerc's fastest lap (lap 53)
lec_fastest_lap = lec_laps[lec_laps['LapNumber'] == 33].iloc[0]

# Get telemetry for the tire-saving lap
lec_tire_saving_tel = lec_tire_saving_lap.get_car_data().add_distance()

# Get telemetry for the fastest lap
lec_fastest_tel = lec_fastest_lap.get_car_data().add_distance()

plt.figure(figsize=(10,5))

# Plot speed telemetry for tire-saving lap
plt.plot(lec_tire_saving_tel['Distance'], lec_tire_saving_tel['Speed'], 
         label=f"Leclerc Tire Saving - Lap {lec_tire_saving_lap['LapNumber']}", color='blue')

# Plot speed telemetry for fastest lap
plt.plot(lec_fastest_tel['Distance'], lec_fastest_tel['Speed'], 
         label=f"Leclerc Fastest - Lap {lec_fastest_lap['LapNumber']}", color='red')

plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Leclerc Speed Trace Comparison - 2024 Italian GP")
plt.legend()
plt.show()

# Get all Norris's laps
nor_laps = session.laps.pick_driver("NOR")

# Print all Norris's laps to identify the pit stop lap
print(nor_laps[['LapNumber', 'PitInTime', 'PitOutTime']])

# Identify Norris's pit stop lap
nor_pit_lap = nor_laps[nor_laps['PitInTime'].notna()].iloc[0]

# Print the identified pit stop lap
print(f"Norris's pit stop lap: {nor_pit_lap['LapNumber']}")

# Get laps in his second stint (after his pit stop)
nor_second_stint = nor_laps[nor_laps['LapNumber'] > nor_pit_lap['LapNumber']]

# Select a lap where Norris was managing tires (e.g., mid-stint)
nor_tire_saving_lap = nor_second_stint[nor_second_stint['LapNumber'] == 37].iloc[0]

# Select Norris's fastest lap (lap 53)
nor_fastest_lap = nor_laps[nor_laps['LapNumber'] == 53].iloc[0]

# Get telemetry for the tire-saving lap
nor_tire_saving_tel = nor_tire_saving_lap.get_car_data().add_distance()

# Get telemetry for the fastest lap
nor_fastest_tel = nor_fastest_lap.get_car_data().add_distance()

plt.figure(figsize=(10,5))

# Plot speed telemetry for tire-saving lap
plt.plot(nor_tire_saving_tel['Distance'], nor_tire_saving_tel['Speed'], 
         label=f"Norris Tire Saving - Lap {nor_tire_saving_lap['LapNumber']}", color='blue')

# Plot speed telemetry for fastest lap
plt.plot(nor_fastest_tel['Distance'], nor_fastest_tel['Speed'], 
         label=f"Norris Fastest - Lap {nor_fastest_lap['LapNumber']}", color='red')

plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Norris Speed Trace Comparison")
plt.legend()
plt.show()

# Compare Leclerc's Lap 30 to Norris lap 25
# Select Leclerc's lap 30
lec_lap_30 = lec_laps[lec_laps['LapNumber'] == 32].iloc[0]

# Select Norris's lap 25
nor_lap_25 = nor_laps[nor_laps['LapNumber'] == 32].iloc[0]

# Get telemetry for Leclerc's lap 30
lec_lap_30_tel = lec_lap_30.get_car_data().add_distance()

# Get telemetry for Norris's lap 25
nor_lap_25_tel = nor_lap_25.get_car_data().add_distance()

plt.figure(figsize=(10,5))

# Plot speed telemetry for Leclerc's lap 30
plt.plot(lec_lap_30_tel['Distance'], lec_lap_30_tel['Speed'], 
         label=f"Leclerc Lap 32 - Lap {lec_lap_30['LapNumber']}", color='red')

# Plot speed telemetry for Norris's lap 25
plt.plot(nor_lap_25_tel['Distance'], nor_lap_25_tel['Speed'], 
         label=f"Norris Lap 32 - Lap {nor_lap_25['LapNumber']}", color='blue')

plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Leclerc vs. Norris Speed Trace Comparison")
plt.legend()
plt.show()

#PIT INTERVAL
# Calculate the total lap time for Leclerc up to lap 14
lec_total_time = lec_laps[lec_laps['LapNumber'] <= 13]['LapTime'].sum()

# Calculate the total lap time for Norris up to lap 14
nor_total_time = nor_laps[nor_laps['LapNumber'] <= 13]['LapTime'].sum()

# Calculate the difference in seconds
time_difference = nor_total_time - lec_total_time

print(f"Norris was {time_difference.total_seconds()} seconds ahead of Leclerc before pitting on lap 14")

# Plot the lap times for the first 13 laps of Lando Norris
first_13_laps_norris = nor_laps[nor_laps['LapNumber'] <= 13]

plt.figure(figsize=(10, 5))

# Plot lap times for the first 13 laps of Norris
plt.plot(first_13_laps_norris['LapNumber'], first_13_laps_norris['LapTime'], label='Norris', color='blue', marker='o', linestyle='-')

plt.xlabel("Lap Number")
plt.ylabel("Lap Time")
plt.title("Norris Lap Times - First 13 Laps")
plt.legend()
plt.show()


#Norris Having Front Grip Issue
# Select Norris's lap 31
nor_lap_31 = nor_laps[nor_laps['LapNumber'] == 31].iloc[0]

# Get telemetry for Norris's lap 31
nor_lap_31_tel = nor_lap_31.get_car_data().add_distance()

# Get telemetry for Norris's lap 53 (already selected as nor_fastest_lap)
nor_lap_53_tel = nor_fastest_lap.get_car_data().add_distance()

plt.figure(figsize=(10,5))

# Plot speed telemetry for Norris's lap 31
plt.plot(nor_lap_31_tel['Distance'], nor_lap_31_tel['Speed'], 
         label=f"Norris Lap 31 - Lap {nor_lap_31['LapNumber']}", color='blue')

# Plot speed telemetry for Norris's lap 53
plt.plot(nor_lap_53_tel['Distance'], nor_lap_53_tel['Speed'], 
         label=f"Norris Lap 53 - Lap {nor_fastest_lap['LapNumber']}", color='red')

plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Norris Speed Trace Comparison - Lap 31 vs Lap 53")
plt.legend()
plt.show()

# Select Leclerc's lap 30
lec_lap_30 = lec_laps[lec_laps['LapNumber'] == 30].iloc[0]

# Select Norris's lap 30
nor_lap_30 = nor_laps[nor_laps['LapNumber'] == 30].iloc[0]

# Get telemetry for Leclerc's lap 30
lec_lap_30_tel = lec_lap_30.get_car_data().add_distance()

# Get telemetry for Norris's lap 30
nor_lap_30_tel = nor_lap_30.get_car_data().add_distance()

plt.figure(figsize=(10,5))

# Plot braking telemetry for Leclerc's lap 30
plt.plot(lec_lap_30_tel['Distance'], lec_lap_30_tel['Brake'], 
         label=f"Leclerc Lap 30 - Brake", color='blue')

# Plot braking telemetry for Norris's lap 30
plt.plot(nor_lap_30_tel['Distance'], nor_lap_30_tel['Brake'], 
         label=f"Norris Lap 30 - Brake", color='red')

plt.xlabel("Distance (m)")
plt.ylabel("Brake (%)")
plt.title("Leclerc vs. Norris Brake Trace - Lap 30")
plt.legend()
plt.show()


