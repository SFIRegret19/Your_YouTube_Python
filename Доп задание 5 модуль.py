from time import sleep


class UrTube:
    """
    Класс UrTube, содержащий атрибуты: 
    """
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname in i and password in i:
                self.current_user = nickname

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        flag = True
        for i in self.users:
            if nickname.__eq__(i[0]):
                print(f'Пользователь {nickname} уже существует')
                flag = False
                break

        if flag.__eq__(True):
            new_user = User(nickname, password, age)

            self.nickname = new_user.nickname
            self.password = new_user.password
            self.age = new_user.age

            info = [self.nickname, self.password, self.age]

            self.users.append(info)
            self.current_user = self.nickname

    def add(self, *args):
        videos_list = [*args]
        for i in videos_list:
            if isinstance(i, Video):
                title = i.title
                if title in self.videos:
                    continue
                else:
                    self.videos.append(i)

    def get_videos(self, search_word):
        videos_list = []
        for i in self.videos:
            if isinstance(i, Video):
                title = i.title
                if search_word.upper() in title.upper():
                    videos_list.append(title)
            else:
                continue
        return videos_list

    def watch_video(self, video_name):

        flag = False
        age = 0
        for i in self.users:
            if self.current_user.__eq__(i[0]):
                age = i[2]
                flag = True
            else:
                flag = False

        if flag.__eq__(True):
            for i in self.videos:
                if isinstance(i, Video):
                    title = i.title
                    if video_name.__eq__(title):
                        if i.adult_mode and age.__lt__(18):
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                            break
                        else:
                            for j in range(1, i.duration + 1):
                                sleep(1)
                                if j.__eq__(i.duration):
                                    print(f'{j} Конец видео')
                                else:
                                    print(j, end=' ')
                            i.duration = 0
                else:
                    continue
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


class Video:
    """
    Класс Video, содержащий атрибуты: заголовок, продолжительность, секунда остановки,
    ограничение по возрасту
    """
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    """
    Класс User, содержащий атрибуты: никнейм, пароль, возраст
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

if __name__ == "__main__":
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')