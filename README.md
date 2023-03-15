# Vacancy Scraper

This Python script allows you to retrieve job vacancies from the HeadHunter job board API and extract key information such as job titles, company names, salaries, addresses, and requirements/responsibilities. The extracted data is then saved to an Excel file for further analysis.

## Dependencies

- Python 3.x
- Requests library
- Pandas library

## How to Use

1. Clone the repository to your local machine.
2. Open the command prompt or terminal and navigate to the directory containing the script.
3. Run the script using the command `python vacancy_scraper.py`.
4. Enter the search term and amount of vacancies you wish to retrieve.
5. The script will retrieve the raw data from the HeadHunter API, extract the necessary information, and save it to an Excel file with a filename based on the search term and amount.
6. The script will output a message indicating how many vacancies were successfully saved to the Excel file.

## Additional Notes

- The script uses area code `113` to specify that the vacancies should be retrieved from Russia. You can modify this code in the `get_raw_vacancies` function to retrieve vacancies from other regions.
- The script saves the extracted data to an Excel file with columns for job title, company name, salary from/to, region, full address, apply URL, vacancy URL, publication time, archived status, requirements, and responsibilities. You can modify the `save_to_excel` function to customize the columns or output format as needed.
- The script uses the `extract_salary` and `extract_address` functions to extract salary and address information from the raw vacancy data. You can modify these functions or add additional functions to extract other types of data.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
