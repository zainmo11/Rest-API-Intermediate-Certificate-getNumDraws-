import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_page(year, page, i):
    url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&page={page}'
    response = requests.get(url).json()
    return response.get('data', [])

def getNumDraws(year):
    # Initialize the variable to count matches
    matches = 0

    # Retrieve the total number of pages and items per page
    r = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&page=1').json()
    total_pages = r['total_pages']
    per_page = r['per_page']

    # Use ThreadPoolExecutor to fetch pages and team1 goals in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Fetch all pages and team1 goals in parallel
        futures = []
        for page in range(1, total_pages + 1):
            for i in range(11):
                future = executor.submit(fetch_page, year, page, i)
                futures.append(future)

        # Wait for all futures to complete
        for future in futures:
            response = future.result()

            # Check if the request was successful
            if response:
                # Loop through matches on the page
                for match in response:
                    team1_goals = int(match['team1goals'])
                    team2_goals = int(match['team2goals'])

                    # Check if it's a draw
                    if team1_goals == team2_goals:
                        matches += 1

    return matches
