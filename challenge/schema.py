import graphene
from graphene_django.types import DjangoObjectType
import requests


class Price(graphene.ObjectType):
    price = graphene.String()



class Query(object):    

    ### Important
    ### I used typeC instead of type because 'type' is a keyword
    calculatePrice = graphene.Field(Price, typeC=graphene.String(), margin=graphene.Float(), exchangeRate=graphene.Float())


    def resolve_calculatePrice(self, info, typeC, margin, exchangeRate):

        ### Send get request to CoinDesk to get rate of Bitcoin in real time
        url = 'http://api.coindesk.com/v1/bpi/currentprice/USD.json'
        response = requests.get(url)

        #Convert the response to json to be accessed
        content = response.json()


        ##Toggle the type to allow for only buy or sell arguments
        if typeC == 'buy' : 

            ## Get the rate of bitcoin, it's quite deeply nested in the api
            rate = content['bpi']['USD']['rate']

            ##Convert the returned string value to float, by first substiting for
            ##extra spaces that might cause irregularities.
            rate = float(rate.replace(',',''))


            ##get the margin_value by multiplying the margin by the rate and
            ##dividing by 100, since its in percentage.
            calculate_value = rate * margin / 100

            ##Add the current rate by the calulated margin value
            substracted_value = rate + calculate_value

            ##Convert the value to NGN, by converting to the exchangeRate
            price = substracted_value * exchangeRate



        elif typeC == 'sell': 

            ##The same logic Apply here
        
            rate = content['bpi']['USD']['rate']
            rate = float(rate.replace(',',''))


            calculate_value = rate * margin / 100
            substracted_value = rate - calculate_value

            price = substracted_value * exchangeRate



        else:

            price = 'Invalid arguments'
        

        return Price(price=price)
        
