import json
import os
import requests

class YaUploader():
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_files_from_folder(self) -> list:
        """Метод получает список файлов из каталога по пути self.file_path и возвращает список файлов для дальнейшей работы"""

        #создаем папку на яндексе
    def create_folder(self):
        common_path = 'https://cloud-api.yandex.net:443/v1/disk/resources?path='
        print('Токен headers СЛОВАРЬ: ', headers_token)
        requests.put(common_path+self.file_path, headers=headers_token)

        #Запрос УНИКАЛЬНОЙ URL для загрузки
    def get_meta_info(self, path):
        common_path_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path='
        upload_postfix = '%2F' + self.file_path + '%2F' + path
        print('Путь для запроса ссылки ВВЕРХ: ', common_path_upload + upload_postfix)
        r = requests.get(common_path_upload + upload_postfix, headers=headers_token)
        url_upload = json.loads(r.content)['href']
        print(url_upload)
        return r

        #загрузка файла ВВЕРХ
    def upload(self, url_upload):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        ###file_list = self._get_files_from_folder()
        common_path_upload = 'https://cloud-api.yandex.net/v1/disk/resources/upload?path='
        upload_postfix2 = loc_folder_path + '&url=' + url_upload
        print('Полная строка загрузки файла ВВЕРХ: ', common_path_upload + upload_postfix2)
        requests.put(common_path_upload + upload_postfix2)  # OAuth-токен для загрузки в хранилище не нужен
        return print('Загрузка файла/ов успешно завершена!')#'Вернуть ответ об успешной загрузке'


if __name__ == '__main__':
    token = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'  # получен копированием по ссылке на "Полигоне" https://yandex.ru/dev/disk/poligon/#!//v1/disk/resources/CreateResource
    headers_token = {'Authorization': f'OAuth {token}'}
    real = r'/home/ubuntu-user/PycharmProjects/DZ-9-1-request-HTTP/4upload/'
    print('Реальный путь к загружаемым файлам: ', real)
    loc_folder_path = os.path.basename(real)

    uploader = YaUploader(loc_folder_path)
    r = uploader.get_meta_info('presentation-1-9.pdf')
    print(json.loads(r.content)['href'])

YaUploader(loc_folder_path).get_meta_info()

# if __name__ == '__main__':
#     token = 'AgAAAAA16yaTAADLW8lKRwrYhUimmUWQ4zu39e4'   #токен Нетологии!
#     #token = 'AgAAAAAy_UpkAADLW4DINWqLNUrUml_SsYrvX7U'  # получен копированием по ссылке на "Полигоне" https://yandex.ru/dev/disk/poligon/#!//v1/disk/resources/CreateResource
#     headers_token = {'Authorization': f'OAuth {token}'}
#     real_folder_path = '/home/ubuntu-user/PycharmProjects/DZ-9-1-request-HTTP/4upload/' #задать ЛОКАЛЬНУЮ папку с файлами
#     print('Реальный путь к загружаемым файлам: ', real_folder_path)
#     loc_folder_path = real_folder_path.split('/')[-2]
#     print('Короткий путь к загружаемым файлам: ', loc_folder_path)
#     files_names = os.listdir(loc_folder_path)
#     print('Файлы для загрузки', files_names)  # 'Вернуть список файлов из каталога'
#     uploader = YaUploader(loc_folder_path)
#     result = uploader.upload()
#

