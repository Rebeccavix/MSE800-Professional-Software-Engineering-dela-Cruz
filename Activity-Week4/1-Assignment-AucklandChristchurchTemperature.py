'''
Activity W4-1: - https://data.niwa.co.nz/pages/clidb-on-datahub
Due date : 9 May 2025 - Load a data for Auckland and Christchurch and compare the temperature between two cities in a year monthly basis -  See Link: https://data.niwa.co.nz/pages/clidb-on-datahub
'''

import pandas as pd
import matplotlib.pyplot as plt


class TemperatureData:
    def __init__(self):
        self.auckland = None
        self.christchurch = None
        self.combined = None

    def load_data(self):
        """Load temperature data from CSV files."""
        self.auckland = pd.read_csv('Activity-Week4\Auckland_temperature.csv')
        self.auckland['City'] = 'Auckland'

        self.christchurch = pd.read_csv(
            'Activity-Week4\Christchurch_temperature.csv')
        self.christchurch['City'] = 'Christchurch'

        self.combined = pd.concat([self.auckland, self.christchurch])

    def show_plot(self):
        for city in self.combined['City'].unique():
            city_data = self.combined[self.combined['City'] == city]
            plt.plot(city_data['Month'],
                     city_data['Temperature'], label=city)

        plt.title('Monthly Temperature: Auckland vs Christchurch')
        plt.xlabel('Month')
        plt.ylabel('Mean Temp (°C)')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


comparison = TemperatureData()
comparison.load_data()
comparison.show_plot()
