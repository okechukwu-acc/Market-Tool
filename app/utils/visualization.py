import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def plot_stock_data(data, indicators, predictions):
    plt.figure(figsize=(14, 7))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.plot(data['Date'], indicators['MA50'], label='50-Day MA')
    plt.plot(data['Date'], indicators['MA200'], label='200-Day MA')
    plt.fill_between(data['Date'], indicators['Bollinger Low'], indicators['Bollinger High'], alpha=0.3, label='Bollinger Bands')
    
    for model, prediction in predictions.items():
        plt.plot(data['Date'].iloc[-len(prediction):], prediction, label=f'{model} Prediction')
    
    plt.legend()
    plt.title('Stock Price and Indicators')
    plt.xlabel('Date')
    plt.ylabel('Price')
    
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return plot_url
