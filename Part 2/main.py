from bs4 import BeautifulSoup
import requests
import time


print('input some skill that you are not familiar')
unfamiliar_skill = input('>')
print(f'Filtering out {unfamiliar_skill}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=data+science&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:
            company = job.find('h3', class_="joblist-comp-name").text.replace('', '')
            skill = job.find('span', class_="srp-skills").text.replace('', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skill:
                with open('posts/{index}.txt', 'w') as f:

                    f.write(f"Company Name: {company.strip()} /n")
                    f.write(f"Required Skill: {skill.strip()} /n")
                    f.write(f"More Info: {more_info}")
                print(f'File saved: {index}')

if __name__ == '__main__' :
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} seconds....')
        time.sleep(time_wait * 0.2
        )

