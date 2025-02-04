import matplotlib.pyplot as plt
import pandas as pd
import base64
import io

class VisualizatoinHandler:

    @staticmethod
    def generate_bar_chart(df, column, title):
        plt.figure(figsize=(8, 5))
        df[column].value_counts().plot(kind='bar')
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel('Count')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode('utf-8')
    
    @staticmethod
    def generate_pie_chart(df, column, title):
        plt.figure(figsize=(6, 6))
        df[column].value_counts().plot(kind='pie', autopct='%1.1f%%')
        plt.title(title)
        plt.ylabel('')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode('utf-8')