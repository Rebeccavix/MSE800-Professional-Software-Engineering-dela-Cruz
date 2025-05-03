import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a more professional style
# sns.set_style("whitegrid")
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial']

# Load data with error handling
try:
    auckland_data = pd.read_csv("auckland_temperature.csv")
    christchurch_data = pd.read_csv("christchurch_temperature.csv")
except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please check that the CSV files exist in the current directory")
    exit()

# Ensure both datasets have required columns
required_columns = ['Month', 'Temperature']
for dataset, name in [(auckland_data, 'Auckland'), (christchurch_data, 'Christchurch')]:
    if not all(col in dataset.columns for col in required_columns):
        print(
            f"Error: {name} dataset is missing required columns. Expected: {required_columns}")
        print(f"Found: {dataset.columns.tolist()}")
        exit()

# Convert Month to datetime if it's not already for proper ordering
for dataset in [auckland_data, christchurch_data]:
    if not pd.api.types.is_datetime64_dtype(dataset['Month']):
        try:
            dataset['Month'] = pd.to_datetime(
                dataset['Month'], format='%b')  # Assumes month abbreviations
            # Sort by month to ensure chronological order
            dataset.sort_values('Month', inplace=True)
            # Format month names for display
            dataset['Month_Display'] = dataset['Month'].dt.strftime('%b')
        except Exception:
            # If specific format fails, try automatic parsing
            dataset['Month'] = pd.to_datetime(
                dataset['Month'], errors='coerce')
            dataset.sort_values('Month', inplace=True)
            dataset['Month_Display'] = dataset['Month'].dt.strftime('%b')

# Create figure and axes with better sizing ratio
fig, ax = plt.subplots(figsize=(12, 7))

# Plot with improved styling
ax.plot(auckland_data['Month_Display'] if 'Month_Display' in auckland_data else auckland_data['Month'],
        auckland_data['Temperature'],
        label='Auckland',
        marker='o',
        linewidth=2.5,
        markersize=8,
        color='#1f77b4')  # Blue

ax.plot(christchurch_data['Month_Display'] if 'Month_Display' in christchurch_data else christchurch_data['Month'],
        christchurch_data['Temperature'],
        label='Christchurch',
        marker='s',
        linewidth=2.5,
        markersize=8,
        color='#ff7f0e')  # Orange

# Add mean temperature lines
auck_mean = auckland_data['Temperature'].mean()
chch_mean = christchurch_data['Temperature'].mean()
ax.axhline(y=auck_mean, color='#1f77b4',
           linestyle='--', alpha=0.7, linewidth=1.5)
ax.axhline(y=chch_mean, color='#ff7f0e',
           linestyle='--', alpha=0.7, linewidth=1.5)

# Add annotations for mean temperatures
ax.text(len(auckland_data) - 1, auck_mean + 0.3, f'Auckland Mean: {auck_mean:.1f}°C',
        color='#1f77b4', fontweight='bold', ha='right')
ax.text(0, chch_mean + 0.3, f'Christchurch Mean: {chch_mean:.1f}°C',
        color='#ff7f0e', fontweight='bold')

# Enhance the plot appearance
ax.set_xlabel('Month', fontsize=12, fontweight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
ax.set_title('Monthly Temperature Comparison: Auckland vs Christchurch',
             fontsize=16, fontweight='bold', pad=20)

# Improve legend
ax.legend(loc='best', frameon=True, shadow=True, fontsize=12)

# Add temperature range and difference information
temp_diff = abs(auckland_data['Temperature'].max() -
                christchurch_data['Temperature'].max())
plt.figtext(0.5, 0.01,
            f"Auckland Temperature Range: {auckland_data['Temperature'].min():.1f}°C to {auckland_data['Temperature'].max():.1f}°C\n"
            f"Christchurch Temperature Range: {christchurch_data['Temperature'].min():.1f}°C to {christchurch_data['Temperature'].max():.1f}°C\n"
            f"Maximum Temperature Difference: {temp_diff:.1f}°C",
            ha='center', fontsize=10)

# Adjust layout and display
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.grid(True, alpha=0.3)
plt.show()

# Optional: Save the figure with high resolution
# plt.savefig('nz_temperature_comparison.png', dpi=300, bbox_inches='tight')
