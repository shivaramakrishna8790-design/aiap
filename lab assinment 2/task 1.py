import random
import csv
from statistics import mean
def create_sample_csv(filename):
    """Create a CSV file with random numbers"""
    data = [[i, random.randint(1, 100)] for i in range(1, 21)]
    # Write to CSV file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Value'])  # Header
        writer.writerows(data)
    return filename
def analyze_csv(filename):
    """Analyze the CSV file and return statistics"""
    values = []
    # Read the CSV file
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values.append(int(row['Value']))
    # Calculate statistics
    stats = {
        'mean': mean(values),
        'min': min(values),
        'max': max(values)
    }
    return stats
def main():
    # Create the CSV file
    filename = 'data.csv'
    print(f"Creating CSV file: {filename}")
    create_sample_csv(filename)
    # Analyze the data
    print("\nAnalyzing data...")
    stats = analyze_csv(filename)
    # Display results
    print("\nResults:")
    print(f"Mean value: {stats['mean']:.2f}")
    print(f"Minimum value: {stats['min']}")
    print(f"Maximum value: {stats['max']}")
if __name__ == "__main__":
    main()