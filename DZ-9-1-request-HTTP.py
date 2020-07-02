import os

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _get_files_from_folder(self) -> list:
        """Метод получает списко файлов из каталога по пути self.file_path и возвращает список файлов для дальнейшей работы"""
        files_names = os.path.split(self.file_path)[-1]
        print(files_names)
        return 'Вернуть список файлов из каталога'

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""
        file_list = self._get_files_from_folder()
        # Тут ваша логика
        return 'Вернуть ответ об успешной загрузке'

    def create_folder(self):
        """метод создает папку на яндекс.диске с таким же именем как и в self.file_path"""
        # Тут ваша логика


if __name__ == '__main__':
    uploader = YaUploader('c:\my_folder') #создать папку, разобраться с путем!!!
    result = uploader.upload()

    print('examp')