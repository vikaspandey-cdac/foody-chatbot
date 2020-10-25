## happy path
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_verify_location
    - slot{"location_ok": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_verify_cuisine
    - slot{"cuisine_ok": true}
    - utter_ask_budget
* restaurant_search{"budgetmin":"300", "budgetmax": "700"}
    - slot{"budgetmax": "700"}
    - slot{"budgetmin": "300"}
    - action_verify_budget
    - slot{"budget_ok": true}
    - action_search_restaurants
    - slot{"restaurant_exist": true}    
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"emailid": "abc@abc.com"}
    - slot{"emailid": "abc@abc.com"}
    - action_send_email
    - utter_goodbye
        - action_restart

## Story from conversation with 751c7388109e46458398bc8da15c0dd8 on October 25th 2020

* greet
    - utter_greet
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budgetmax":"700"}
    - slot{"budgetmax":"700"}
    - slot{"budgetmax":"700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - slot{"restaurant_exists":true}
    - utter_ask_email
* affirm
    - utter_ask_emailid
* ask_email{"email":"asdf@ldf.com"}
    - action_send_email
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - slot{"budgetmax":"700"}

## Story from conversation with d361c52c747649aa9b0db69828f40323 on October 25th 2020

* greet
    - utter_greet
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - action_verify_location
    - slot{"location_ok":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - action_verify_cuisine
    - slot{"cuisine_ok":true}
    - utter_ask_budget
* restaurant_search{"budgetmax":"700"}
    - slot{"budgetmax":"700"}
    - slot{"budgetmax":"700"}
    - action_verify_budget
    - slot{"budget_ok":true}
    - action_search_restaurants
    - slot{"restaurant_exists":true}
    - utter_ask_email
* deny
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - slot{"budgetmax":"700"}
    - utter_goodbye
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"South Indian"}
    - slot{"budgetmax":"700"}
