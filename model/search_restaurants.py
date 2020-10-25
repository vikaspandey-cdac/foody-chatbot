from  model.zomato_slots import results

class SearchRestaurants:
    def search_restaurants(self, loc, cuisine, budgetmin, budgetmax):

        print("location ::", loc, " cuisine ::", cuisine, "price ::", budgetmax)

        global restaurants

        restaurants = results(loc, cuisine, budgetmin, budgetmax)
        restaurants.drop_duplicates(inplace=True)
        restaurants_length = len(restaurants)
        top5 = restaurants.head(5)
        #print(restaurants)
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

