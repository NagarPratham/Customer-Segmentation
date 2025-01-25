# Customer Segmentation Project

This repository contains a Python script that implements customer segmentation using the K-Means clustering algorithm. The script processes customer data stored in a SQLite database, performs clustering, and visualizes the results.

## Features

- **SQLite Integration**: The script creates a SQLite database (`customer_data.db`) to store customer data.
- **Data Preprocessing**: Prepares data by standardizing numerical features using `StandardScaler`.
- **K-Means Clustering**: Groups customers into clusters based on their spending behavior and other attributes.
- **Visualization**: Generates a scatter plot to visualize the clustering results.

## Prerequisites

Ensure you have the following libraries installed:

- `sqlite3`
- `pandas`
- `matplotlib`
- `scikit-learn`

You can install the required libraries using pip:

```bash
pip install pandas matplotlib scikit-learn
```

## Usage

1. **Set Up Database**: The script creates and populates the `purchases` table in the `customer_data.db` database with sample customer data.
2. **Run the Script**: Execute the script to perform clustering and generate visualizations.

```bash
python customer_segmentation_updated.py
```

3. **View Output**:
   - A scatter plot displaying the customer clusters.
   - Console output with detailed information, including customer IDs and their respective clusters.
![image](https://github.com/user-attachments/assets/bae4b209-42a7-4458-82cf-39792e49c1b9)

## Data Schema

The `purchases` table in the SQLite database has the following columns:

- `customer_id` (INTEGER, PRIMARY KEY)
- `age` (INTEGER)
- `spending_score` (INTEGER)
- `gender` (TEXT)
- `number_of_purchases` (INTEGER)
- `customer_loyalty_score` (INTEGER)
- `purchase_frequency` (INTEGER)
- `average_purchase_value` (REAL)
- `last_purchase_date` (TEXT)

## Clustering Variables

The clustering algorithm uses the following features:

- `age`
- `spending_score`
- `number_of_purchases`
- `customer_loyalty_score`
- `purchase_frequency`
- `average_purchase_value`

## Visualization

The script generates a scatter plot with the following details:

- **X-axis**: Spending Score
- **Y-axis**: Number of Purchases
- **Color**: Represents the cluster assignment

## Customization

- Adjust the number of clusters by modifying the `n_clusters` parameter in the `KMeans` initialization:

  ```python
  kmeans = KMeans(n_clusters=4, random_state=42)
  ```

- Add or modify customer data in the `customer_data` list to test with different datasets.

## Limitations

- The dataset provided is sample data for demonstration purposes.
- The clustering algorithm may need fine-tuning for larger or more complex datasets.
