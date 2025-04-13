import pandas as pd
import os

# Get the absolute paths to important directories
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.dirname(current_dir)
data_dir = os.path.join(base_dir, 'data')
results_dir = os.path.join(base_dir, 'results')

# Create results directory if it doesn't exist
os.makedirs(results_dir, exist_ok=True)

file_path = os.path.join(data_dir, "Copy of dataset.xlsx")
df = pd.read_excel(file_path)

sample = df.sample(20, random_state=42)

sample.to_excel(os.path.join(results_dir, "sample_test_data.xlsx"), index=False)
print(f"Created sample test data with {len(sample)} rows")
print(f"Saved as '{os.path.join(results_dir, 'sample_test_data.xlsx')}'") 