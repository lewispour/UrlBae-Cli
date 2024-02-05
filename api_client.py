import requests
import os
from config import API_KEY, BASE_URL
from tabulate import tabulate 

def create_short_url(long_url, custom=None, type=None, password=None):
    endpoint = f'{BASE_URL}/url/add'
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    data = {
        'url': long_url,
        'custom': custom,
        'type': type,
        'password': password
    }
    # Remove None values from data
    data = {k: v for k, v in data.items() if v is not None}
    response = requests.post(endpoint, headers=headers, json=data)
    return response.json() if response.status_code in [200, 201] else response.raise_for_status()

def list_urls(limit=10, page=1, order='date'):
    endpoint = f'{BASE_URL}/urls?limit={limit}&page={page}&order={order}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        urls_data = data.get('data', {}).get('urls', [])
        parsed_urls = [{'Short URL': url['shorturl'], 'Long URL': url['longurl'], 'ID': url['id']} for url in urls_data]
        table = tabulate(parsed_urls, headers="keys", tablefmt="pretty")  # Format as a pretty table
        return table
    else:
        response.raise_for_status()
        
def get_single_url_details(url_id):
    endpoint = f'{BASE_URL}/url/{url_id}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        url_data = response.json().get('details', {})
        data = response.json().get('data', {})
        parsed_url_data = {
            'ID': url_data.get('id', ''),
            'Short URL': url_data.get('shorturl', ''),
            'Long URL': url_data.get('longurl', ''),
            'Title': url_data.get('title', ''),
            'Description': url_data.get('description', ''),
            'Clicks': data.get('clicks', ''),
            'Unique Clicks': data.get('uniqueClicks', ''),
            'Date': url_data.get('date', ''),
        }
        table = tabulate([parsed_url_data], headers="keys", tablefmt="pretty")  # Format as a pretty table
        return table
    else:
        response.raise_for_status()

def delete_url(url_id):
    endpoint = f'{BASE_URL}/url/{url_id}/delete'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.delete(endpoint, headers=headers)
    return response.json() if response.status_code == 200 else response.raise_for_status()

def list_files(limit=10, page=1, name=None):
    endpoint = f'{BASE_URL}/files?limit={limit}&page={page}'
    if name:
        endpoint += f'&name={name}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        files_data = data.get('list', [])
        parsed_files = [
            {
                'ID': file['id'],
                'Name': file['name'],
                'Downloads': file['downloads'],
                'Short URL': file['shorturl'],
                'Date': file['date'],
            }
            for file in files_data
        ]
        table = tabulate(parsed_files, headers="keys", tablefmt="pretty")  # Format as a pretty table
        return table
    else:
        response.raise_for_status()

def list_qr_codes(limit=10, page=1):
    endpoint = f'{BASE_URL}/qr?limit={limit}&page={page}'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data', {})
        qr_data = data.get('qrs', [])
        parsed_qr = [
            {
                'ID': qr['id'],
                'Link': qr['link'],
                'Scans': qr['scans'],
                'Name': qr['name'],
                'Date': qr['date'],
            }
            for qr in qr_data
        ]
        table = tabulate(parsed_qr, headers="keys", tablefmt="pretty")
        return table
    else:
        response.raise_for_status()

def create_qr_code(type, data, background=None, foreground=None, logo=None):
    endpoint = f'{BASE_URL}/qr/add'
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    body = {
        'type': type,
        'data': data,
        'background': background,
        'foreground': foreground,
        'logo': logo
    }
    body = {k: v for k, v in body.items() if v is not None}
    response = requests.post(endpoint, headers=headers, json=body)
    return response.json() if response.status_code == 200 else response.raise_for_status()

def update_qr_code(qr_id, data, background=None, foreground=None, logo=None):
    endpoint = f'{BASE_URL}/qr/{qr_id}/update'
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    body = {
        'data': data,
        'background': background,
        'foreground': foreground,
        'logo': logo
    }
    body = {k: v for k, v in body.items() if v is not None}
    response = requests.put(endpoint, headers=headers, json=body)
    return response.json() if response.status_code == 200 else response.raise_for_status()

def delete_qr_code(qr_id):
    endpoint = f'{BASE_URL}/qr/{qr_id}/delete'
    headers = {'Authorization': f'Bearer {API_KEY}'}
    response = requests.delete(endpoint, headers=headers)
    return response.json() if response.status_code == 200 else response.raise_for_status()

def upload_file(filename, name=None, custom=None, domain=None, password=None, expiry=None, maxdownloads=None):
    # Check if file exists in the current directory
    if not os.path.isfile(filename):
        # If not found, prompt the user for the full path
        full_path = input("File not found. Please provide the full path: ")
        if not os.path.isfile(full_path):
            print("File still not found. Exiting.")
            return
        filepath = full_path
    else:
        filepath = filename
    endpoint = f'{BASE_URL}/files/upload/{filename}'
    if name or custom or domain or password or expiry or maxdownloads:
        params = []
        if name:
            params.append(f'name={name}')
        if custom:
            params.append(f'custom={custom}')
        if domain:
            params.append(f'domain={domain}')
        if password:
            params.append(f'password={password}')
        if expiry:
            params.append(f'expiry={expiry}')
        if maxdownloads:
            params.append(f'maxdownloads={maxdownloads}')
        query_string = '&'.join(params)
        endpoint += f'?{query_string}'

    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}

    with open(filepath, 'rb') as file:
        data = file.read()

    response = requests.post(endpoint, headers=headers, data=data)
    return response.json() if response.status_code == 200 else response.raise_for_status()

