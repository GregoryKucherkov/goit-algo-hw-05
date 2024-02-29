import requests

def download_google_docs(url):
    # Find the index of '/edit' in the URL
    edit_index = url.find('/edit')

    # Replace '/edit' with '/export?format=txt'
    export_url = url[:edit_index] + '/export?format=txt'
    response = requests.get(export_url)

    #checking that the request was successful, and the server has returned the requested data
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error downloading file from {export_url}. Status code: {response.status_code}")
        return None
        

if __name__ == '__main__':
    download_google_docs()

