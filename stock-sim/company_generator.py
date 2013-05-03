from econsim.companies import Ceo, Company
from econsim.wordgen import generate_word

import random

company_set = []
name_set = []

# Make them companies
for i in xrange(8420):
    try_name = generate_word(4)
    while try_name in name_set:
        try_name = generate_word(4)

    name_set.append(try_name)
    company_set.append(Company(try_name))

#print company_set

test_vol = 4.0
for company in company_set[:]:
    company.progress(test_vol)

#print company_set

#print map(lambda x: x.current_ceo(), company_set)

bankrupts = map(Company.is_bankrupt, company_set) 

while False in bankrupts:
    for company in company_set:
        if not company.is_bankrupt():
            company.progress(test_vol)
            """
        else:
            new_company = Company(generate_word(4))
            new_company.progress(test_vol)
            company_set.append(new_company)
            """
    bankrupts = map(Company.is_bankrupt, company_set) 

    alive = 0
    for is_broke in bankrupts:
        if not is_broke:
            alive += 1

    print alive

#print company_set
