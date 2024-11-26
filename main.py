import pandas as pd
import matplotlib.pyplot as plt
import random

data = pd.read_csv('data.csv')

def plot_bar(column_name, title):
    counts = data[column_name].value_counts()
    counts.plot(kind='bar', figsize=(8, 6), color='skyblue', edgecolor='black')
    plt.title(title, fontsize=14)
    plt.ylabel('Количество', fontsize=12)
    plt.xlabel('Ответы', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_pie(column_name, title):
    counts = data[column_name].value_counts()
    counts.plot(kind='pie', figsize=(8, 6), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title(title, fontsize=14)
    plt.ylabel('')  
    plt.tight_layout()
    plt.show()

def plot_horizontal_bar(column_name, title):
    counts = data[column_name].value_counts()
    counts.plot(kind='barh', figsize=(8, 6), color='lightgreen', edgecolor='black')
    plt.title(title, fontsize=14)
    plt.xlabel('Количество', fontsize=12)
    plt.ylabel('Ответы', fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_line(column_name, title):
    counts = data[column_name].value_counts().sort_index()
    counts.plot(kind='line', figsize=(8, 6), marker='o', color='red')
    plt.title(title, fontsize=14)
    plt.ylabel('Количество', fontsize=12)
    plt.xlabel('Ответы', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.show()

def plot_density(column_name, title):
    try:
        data[column_name].plot(kind='density', figsize=(8, 6), color='purple')
        plt.title(title, fontsize=14)
        plt.xlabel('Значения', fontsize=12)
        plt.ylabel('Плотность', fontsize=12)
        plt.tight_layout()
        plt.show()
    except TypeError:
        print(f"Диаграмма плотности недоступна для вопроса: {column_name}")

plot_types = {
    'bar': plot_bar,
    'pie': plot_pie,
    'horizontal_bar': plot_horizontal_bar,
    'line': plot_line,
    'density': plot_density
}

questions = data.columns[1:]  
for question in questions:
    plot_type = random.choice(list(plot_types.keys()))
    plot_types[plot_type](question, f'Распределение ответов: {question}')
