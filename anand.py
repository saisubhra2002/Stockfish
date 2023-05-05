import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2023, 5, 1)  # Starting date in April
end_date = datetime(2023, 6, 1)    # Ending date in May

for i in range(1, 11):
    for j in range(0, randint(1, 10)):
        random_days = randint(0, (end_date - start_date).days)
        random_date = start_date + timedelta(days=random_days)
        formatted_date = random_date.strftime('%Y-%m-%d %H:%M:%S')

        with open('data.txt', 'a') as data:
            data.write(formatted_date)

        os.system('git add .')
        os.system(f'git commit --date="{formatted_date}" -m "commit"')

os.system('git push -u origin main')
