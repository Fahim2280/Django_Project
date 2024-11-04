import json
from django.core.management.base import BaseCommand
from MainApp.models import Person

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **kwargs):
        with open('stock_market_data.json', 'r') as file:
            data = json.load(file)
            for item in data:
                Person.objects.create(date=item['date'], trade_code=item['trade_code'], high=item['high'], low=item['low'], open=item['open'], close=item['close'], volume=item['volume'])
                
