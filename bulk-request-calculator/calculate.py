
import requests
import json
from dotenv import load_dotenv
import os


load_dotenv()


FIRST_YEAR = 1900
CUR_YEAR = 2023


def get_agencies_for_year(year, api_key):
	url = 'https://api.regulations.gov/v4/documents'
	params = {
		'api_key': api_key,
		'filter[agencyId]': '*',
		'filter[postedDate][le]': f'{year}-12-31',
		'filter[postedDate][ge]': f'{year}-01-01'
	}
	return requests.get(url, params=params)


def get_years_per_agency(api_key):
	years = {}

	for year in range(FIRST_YEAR, CUR_YEAR+1):
		response = get_agencies_for_year(year, api_key)
		print(f'Received response for year {year}.')

		response = json.loads(response.text)
		elements = response['meta']['aggregations']['agencyId']

		for elm in elements:
			agency = elm['value']
			if agency in years:
				years[agency].append(year)
			else:
				years[agency] = [year]

		print(f'Current Years Per Agency: {get_num_years_per_agency(years)}')

	return years


def get_num_years_per_agency(years):
	return sum([len(years[key]) for key in years])


def main():
	api_key = os.getenv('key')
	years = get_years_per_agency(api_key)
	print(f'Total Bulk Requests Required: {get_num_years_per_agency(years)}')


if __name__ == '__main__':
	main()
