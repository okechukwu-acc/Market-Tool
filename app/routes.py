from flask import Blueprint, render_template, request, jsonify
from .utils.data_retrieval import fetch_historical_data
from .utils.technical_analysis import calculate_indicators
from .utils.predictive_modeling import predict_stock_prices
from .utils.visualization import plot_stock_data
from .utils.report_generation import generate_report

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        symbol = request.form.get('symbol')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        data = fetch_historical_data(symbol, start_date, end_date)
        indicators = calculate_indicators(data)
        predictions = predict_stock_prices(data)
        plots = plot_stock_data(data, indicators, predictions)
        
        return render_template('dashboard.html', data=data, indicators=indicators, predictions=predictions, plots=plots)
    return render_template('dashboard.html')

@main_bp.route('/report', methods=['POST'])
def report():
    symbol = request.form.get('symbol')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    
    report = generate_report(symbol, start_date, end_date)
    
    return render_template('report.html', report=report)
