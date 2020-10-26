import json
import pandas as pd

from actions.zomato import zomatopy

config = {"user_key": "be2cfee4af568158abde9eae6c636ca6"}
zomato = zomatopy.initialize_app(config)


class SearchRestaurants:
    def search_restaurants(self, loc, cuisine, budgetmin, budgetmax):

        print("location ::", loc, " cuisine ::", cuisine, "price ::", budgetmax)

        global restaurants

        restaurants = list_restaurants(loc, cuisine, budgetmin, budgetmax)
        restaurants.drop_duplicates(inplace=True)
        restaurants_length = len(restaurants)
        top5 = restaurants.head(5)
        # print(restaurants)
        # top 5 results to display
        if restaurants_length > 0:
            response = 'Showing you top results:' + "\n"
            for index, row in top5.iterrows():
                response = response + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + \
                           row['restaurant_address'] + ' and the average budget for two people ' + str(
                    row['budget_for2people']) + "\n"
        else:
            response = 'No restaurants found'
        return restaurants_length, response


def list_restaurants(loc, cuisine, minBudget, maxBudget):
    location_detail = zomato.get_location(loc, 1)
    location_json = json.loads(location_detail)

    lat = location_json["location_suggestions"][0]["latitude"]
    lon = location_json["location_suggestions"][0]["longitude"]
    cuisines_dict = {'american': 1, 'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85,
                     'thai': 95}
    budgets = [minBudget, maxBudget]

    list1 = [0, 20, 40, 60, 80]
    d = []
    df = pd.DataFrame()
    for i in list1:
        print(" parameters to request restaurant search :: ", lat, lon, "cuisine :: " + cuisine,
              str(cuisines_dict.get(cuisine)), i)
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), limit=i)
        d1 = json.loads(results)
        d = d1['restaurants']
        df1 = pd.DataFrame([{'restaurant_name': x['restaurant']['name'],
                             'restaurant_rating': x['restaurant']['user_rating']['aggregate_rating'],
                             'restaurant_address': x['restaurant']['location']['address'],
                             'budget_for2people': x['restaurant']['average_cost_for_two'],
                             'restaurant_photo': x['restaurant']['featured_image'],
                             'restaurant_url': x['restaurant']['url']} for x in d])
        df = df.append(df1)

    restaurant_df = df[(df.budget_for2people.isin(budgets))]
    restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)

    return restaurant_df
