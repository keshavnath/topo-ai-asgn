from flask import Flask, jsonify, render_template
import pandas as pd

from AppFunctions import DataProcessor
from AppVisualization import VisualizatoinHandler

app = Flask(__name__)

data_processor = DataProcessor()

@app.route('/api/data', methods=['GET'])
def get_all_data():
    data = data_processor.get_unified_data()
    return jsonify(data)

@app.route('/api/data/<file_type>', methods=['GET'])
def get_file_type_data(file_type):
    data = data_processor.get_type_data(file_type)
    if data is None:
        return jsonify({"error": f"File type '{file_type}' not found"}), 404
    return jsonify(data)

@app.route('/visualization')
def visualization():
    csv_data = data_processor.get_type_data('csv')
    if not csv_data:
        return "No CSV data available"
    df = pd.DataFrame(csv_data)
    
    membership_chart = VisualizatoinHandler.generate_bar_chart(df, 'Membership_Type', 'Membership Types Distribution')
    activity_chart = VisualizatoinHandler.generate_bar_chart(df, 'Activity', 'Activity Distribution')
    revenue_pie_chart = VisualizatoinHandler.generate_pie_chart(df, 'Membership_Type', 'Revenue Distribution by Membership Type')
    
    return render_template('./visuals.html', 
                           membership_chart=membership_chart, 
                           activity_chart=activity_chart, 
                           revenue_pie_chart=revenue_pie_chart)

if __name__ == '__main__':
    app.run(debug=True)