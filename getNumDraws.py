import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_page(year, page):
    url = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={page}'
    response = requests.get(url).json()
    return response.get('data', [])

def getNumDraws(year):
    # Initialize the variable to count matches
    matches = 0

    # Retrieve the total number of pages and items per page
    r = requests.get(f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&page=1').json()
    total_pages = r['total_pages']
    per_page = r['per_page']

    # Use ThreadPoolExecutor to fetch pages in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Fetch all pages in parallel
        pages_data = list(executor.map(lambda page: fetch_page(year, page), range(1, total_pages + 1)))

    # Loop through matches on all pages
    for page_data in pages_data:
        for match in page_data:
            team1_goals = int(match['team1goals'])
            team2_goals = int(match['team2goals'])

            # Check if it's a draw
            if team1_goals == team2_goals:
                matches += 1

    return matches
