from Tools.tavily_tool import travily_search 
from Tools.flight_tool import search_flights

res2 = search_flights(" plan e ticket from New York to Los Angeles on July 15th, 2023 for 2 adults and 1 child, with a budget of $500 per person. Please provide the best available options and include details such as airline, flight duration, layovers, and total cost. Additionally, if there are any special promotions or discounts available for this route, please highlight them in the results. Thank you!")
print(res2)