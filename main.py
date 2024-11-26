import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

def plot_data_distribution(column_name, title):
    counts = data[column_name].value_counts()
    counts.plot(kind='bar', figsize=(8, 6), color='skyblue', edgecolor='black')
    plt.title(title, fontsize=14)
    plt.ylabel('Количество', fontsize=12)
    plt.xlabel('Ответы', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.show()

questions = data.columns[1:]  
for question in questions:
    plot_data_distribution(question, f'Распределение ответов: {question}')
