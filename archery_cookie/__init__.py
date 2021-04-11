from dotenv import load_dotenv
from os import getenv
from json import loads, dumps
from redis import Redis
from archery_secret import Secret


load_dotenv()


class CookieNotFound(Exception):
    def __init__(
        self: object,
        cookie: str
    ) -> None:
        self.cookie = cookie

    def __str__(self) -> str:
        return '\033[1;31mCookie ' +\
            self.cookie +\
            ' not found!\033[m'


class Cookie:
    """
        Responsible for manage cookies.

    """
    __redis = Redis(
        host=getenv(
            'ARCHERY_PERSON_REDIS_HOST'
        ),
        port=getenv(
            'ARCHERY_PERSON_REDIS_PORT'
        ),
        db=getenv(
            'ARCHERY_PERSON_SESSION_DB'
        )
    )
    __secret = Secret()

    def get(
        self: object,
        cookie: str
    ) -> dict:
        try:
            person = loads(
                self.__secret.decrypt(
                    self.__redis.get(
                        str(
                            cookie
                        )
                    ).decode()
                )
            )
            return person
        except AttributeError:
            raise CookieNotFound(
                cookie
            )

    def new(
        self: object,
        person: dict
    ) -> str:
        return self.__set(
            person
        )

    def __set(
        self: object,
        person: dict
    ) -> str:
        cookie = self.__secret.randomic
        self.__redis.set(
            cookie,
            self.__secret.encrypt(
                dumps(person)
            ),
            ex=getenv(
                'ARCHERY_PERSON_SESSION_TIME'
            )
        )
        return cookie

    def renew(
        self: object,
        cookie: str
    ) -> dict:
        data = self.get(
            cookie
        )
        self.__redis.delete(
            cookie
        )
        return self.__set(
            data
        )
