import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

conn = sqlite3.connect('customer_data.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS purchases')
cursor.execute('''
    CREATE TABLE purchases (
        customer_id INTEGER PRIMARY KEY,
        age INTEGER,
        spending_score INTEGER,
        gender TEXT,
        number_of_purchases INTEGER,
        customer_loyalty_score INTEGER,
        purchase_frequency INTEGER,
        average_purchase_value REAL,
        last_purchase_date TEXT
    )
''')

customer_data = [
    (1, 25, 60, 'Female', 15, 75, 10, 200.5, '2024-09-01'),
    (2, 30, 90, 'Male', 25, 90, 15, 150.0, '2024-08-25'),
    (3, 35, 80, 'Female', 30, 85, 20, 175.75, '2024-09-10'),
    (4, 40, 30, 'Male', 10, 50, 5, 220.3, '2024-09-15'),
    (5, 45, 50, 'Female', 5, 60, 3, 300.6, '2024-08-30'),
    (6, 50, 40, 'Male', 20, 70, 12, 185.9, '2024-09-20'),
    (7, 22, 70, 'Female', 12, 80, 8, 250.0, '2024-09-05'),
    (8, 27, 20, 'Male', 8, 40, 4, 130.2, '2024-09-12'),
    (9, 32, 75, 'Female', 18, 78, 12, 215.7, '2024-08-28'),
    (10, 38, 85, 'Male', 22, 88, 18, 195.6, '2024-09-18')
]
cursor.executemany('''
    INSERT INTO purchases (customer_id, age, spending_score, gender, number_of_purchases, customer_loyalty_score, purchase_frequency, average_purchase_value, last_purchase_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
''', customer_data)
conn.commit()
df = pd.read_sql_query('SELECT * FROM purchases', conn)
X = df[['age', 'spending_score', 'number_of_purchases', 'customer_loyalty_score', 'purchase_frequency', 'average_purchase_value']]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)
df['cluster'] = kmeans.labels_
plt.figure(figsize=(10, 6))
plt.scatter(df['spending_score'], df['number_of_purchases'], c=df['cluster'], cmap='plasma', marker='o')
plt.title('Customer Segmentation using K-Means Clustering')
plt.xlabel('Spending Score')
plt.ylabel('Number of Purchases')
plt.colorbar(label='Cluster')
plt.grid()
plt.show()

print(df[['customer_id', 'age', 'spending_score', 'number_of_purchases', 'customer_loyalty_score', 'purchase_frequency', 'average_purchase_value', 'cluster']])
conn.close()
