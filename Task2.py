import requests
from pprint import pprint


class YaUploader:
    URL = 'https://cloud-api.yandex.net:443'

    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_link = f'{self.URL}/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(upload_link, params=params, headers=headers)
        return response.json().get('href')

    def upload_file(self, file_path, file_name):
        upload_link = self.upload(file_path)
        header = {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}
        response = requests.put(upload_link, data=open(file_name, 'rb'), headers=header)
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл сохранен')

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = '/Task2.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    uploader.upload_file(path_to_file, 'Task2.txt')
