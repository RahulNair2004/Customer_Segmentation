# Customer Segmentation

Customer segmentation is the process of dividing customers into distinct groups based on common characteristics such as demographics, behavior, or purchasing patterns. This project uses machine learning techniques to perform customer segmentation.

## 🚀 Features
- **Data Preprocessing**: Handles missing values, outliers, and feature scaling.
- **Clustering Models**: Implements K-Means, DBSCAN, and Hierarchical Clustering.
- **Dimensionality Reduction**: Uses PCA for feature reduction and visualization.
- **Visualization**: Generates cluster plots for better understanding.

## 📂 Dataset
The dataset should contain customer attributes like:
- Age
- Annual Income
- Spending Score
- Purchase Behavior

You can use datasets like [Mall Customers Dataset](https://www.kaggle.com/datasets) or any customer-related dataset.

## 🛠 Installation
Clone the repository and install dependencies:
```bash
# Clone the repo
git clone https://github.com/your-username/customer-segmentation.git
cd customer-segmentation

# Create a virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🏃‍♂️ Usage
Run the customer segmentation script:
```bash
python customer_segmentation.py
```
This will perform clustering and generate visualizations.

## 📊 Results
- Clusters are visualized using scatter plots.
- PCA helps in reducing dimensionality for better cluster representation.

## 📌 Models Used
- **K-Means Clustering**: Assigns customers to clusters based on similarity.
- **DBSCAN**: Identifies dense regions for clustering.
- **Hierarchical Clustering**: Forms clusters in a hierarchical manner.


## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Feel free to submit issues or pull requests.
