import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create visualization folder if not exists
vis_dir = r"c:\Users\Godwin Akachukwu\Downloads\Covid Dataset\visualization"
if not os.path.exists(vis_dir):
    os.makedirs(vis_dir)

# Load data
df = pd.read_csv(r"c:\Users\Godwin Akachukwu\Downloads\Covid Dataset\covid_dataset.csv")

# Set aesthetic style
sns.set_theme(style="darkgrid")
plt.rcParams['figure.facecolor'] = '#121212'
plt.rcParams['axes.facecolor'] = '#1e1e1e'
plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

# 1. Covid Status Distribution
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Has_Covid', palette='viridis')
plt.title('Covid Status Distribution')
plt.savefig(os.path.join(vis_dir, 'covid_status_distribution.png'))
plt.close()

# 2. Cases by City
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='City', hue='Has_Covid', palette='magma')
plt.title('Covid Cases by City')
plt.savefig(os.path.join(vis_dir, 'cases_by_city.png'))
plt.close()

# 3. Age Distribution by Covid Status
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Has_Covid', kde=True, palette='coolwarm')
plt.title('Age Distribution by Covid Status')
plt.savefig(os.path.join(vis_dir, 'age_distribution.png'))
plt.close()

# 4. Fever vs Age
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Age', y='Fever', hue='Has_Covid', palette='plasma')
plt.title('Fever vs Age (Colored by Covid Status)')
plt.savefig(os.path.join(vis_dir, 'fever_vs_age.png'))
plt.close()

# 5. Symptom (Cough) vs Covid
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x='Cough', hue='Has_Covid', palette='rocket')
plt.title('Cough Severity vs Covid Status')
plt.savefig(os.path.join(vis_dir, 'cough_vs_covid.png'))
plt.close()

# Summary Analysis
summary = {
    'Total Records': len(df),
    'Positive Cases': len(df[df['Has_Covid'] == 'Yes']),
    'Negative Cases': len(df[df['Has_Covid'] == 'No']),
    'Positivity Rate': f"{(len(df[df['Has_Covid'] == 'Yes']) / len(df)) * 100:.2f}%",
    'Average Fever (Positive)': df[df['Has_Covid'] == 'Yes']['Fever'].mean(),
    'Average Fever (Negative)': df[df['Has_Covid'] == 'No']['Fever'].mean()
}

with open(os.path.join(vis_dir, 'analysis_summary.txt'), 'w') as f:
    for key, value in summary.items():
        f.write(f"{key}: {value}\n")

print("Analysis and visualizations completed successfully.")
