import random



SEED = 1234


def generate_companies(companies_count):


    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)

    companies = []

    for i in range(companies_count):
        companies.append({
            "id": ids[i],
            "name": 'all_company',
            "phone": 'number-55555',
        })

    return companies

companies = generate_companies(10)
print(companies)
id = 5
for dictionary in companies:
    if dictionary['id'] == id:
        print('YES')
    else:
        print('NO')

