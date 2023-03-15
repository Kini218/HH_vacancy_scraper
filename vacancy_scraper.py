import requests
import pandas as pd


def get_raw_vacancies(search_term, amount):
    """
    Retrieve raw vacancy data from the HeadHunter API.

    Parameters:
    search_term (str): The search term to use when querying vacancies.
    amount (int): The number of vacancies to retrieve.

    Returns:
    List: A list of dictionaries containing raw vacancy data.
    """
    raw_vacancies_data = []
    url = 'https://api.hh.ru/vacancies'

    for i in range(amount // 10):  # 10 vacancies on one page
        params = {
            'text': search_term,
            'area': '113',  # area 113 == Russia
            'per_page': '10',
            'page': i
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception if the request failed
        raw_vacancies_data.append(response.json())

    return raw_vacancies_data


def extract_salary(vacancy):
    """
    Extract the salary information from a vacancy dictionary.

    Parameters:
    vacancy (dict): A dictionary containing vacancy data.

    Returns:
    Tuple: A tuple containing the salary from and to values.
    """
    if vacancy['salary'] is not None:
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
    else:
        salary_from = None
        salary_to = None
    return salary_from, salary_to


def extract_address(vacancy):
    """
    Extract the address information from a vacancy dictionary.

    Parameters:
    vacancy (dict): A dictionary containing vacancy data.

    Returns:
    str: The address string.
    """
    if vacancy['address'] is not None:
        address_raw = vacancy['address']['raw']
    else:
        address_raw = None
    return address_raw


def save_to_excel(data, filename):
    """
    Save the extracted vacancy data to an Excel file.

    Parameters:
    data (list): A list of lists containing vacancy data.
    filename (str): The filename to save the Excel file to.
    """
    columns = [
        'Job Title',
        'Company Name',
        'Salary From',
        'Salary To',
        'Region',
        'Full Address',
        'Apply URL',
        'Vacancy URL',
        'Publication Time',
        'Archived',
        'Requirements',
        'Responsibilities'
    ]
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(filename)


def extract_information(search_term, amount):
    """
    Extract the necessary information from the raw vacancy data.

    Parameters:
    search_term (str): The search term to use when querying vacancies.
    amount (int): The number of vacancies to retrieve.

    Returns:
    List: A list of lists containing the extracted vacancy data.
    """
    clear_data = []
    for elem in get_raw_vacancies(search_term, amount):
        page = elem['items']
        for vacancy in page:
            salary_from, salary_to = extract_salary(vacancy)
            address_raw = extract_address(vacancy)

            clear_data.append([
                vacancy['name'],
                vacancy['employer']['name'],
                salary_from,
                salary_to,
                vacancy['area']['name'],
                address_raw,
                vacancy['apply_alternate_url'],
                vacancy['alternate_url'],
                vacancy['published_at'],
                vacancy['archived'],
                vacancy['snippet']['requirement'],
                vacancy['snippet']['responsibility']
            ])

    return clear_data


if __name__ == '__main__':
    # Retrieve raw data and extract necessary information
    print('Please enter vacancy name:')
    search_term = input()
    print('Please enter amount:')
    amount = int(input())
    extracted_data = extract_information(search_term, amount)
    # Save extracted data to an Excel file
    filename = f'{search_term}_{amount}.xlsx'
    save_to_excel(extracted_data, filename)
    print(f'Successfully saved {len(extracted_data)} vacancies to {filename}')
