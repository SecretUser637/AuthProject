import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from config import settings


class AuthHandler:
    # настройки для хеширования пароля
    security = HTTPBearer()
    pwd_context = CryptContext(
        schemes=['bcrypt'],
        deprecated='auto'
    )
    # Секретный ключ, на его основе генерируется JWT токен
    secret = settings.SECRET_KEY

    # функция получения хеша из пароля
    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    # сверка пароля и хеша
    def verify_password(self, input_pass, hash_pass):
        return self.pwd_context.verify(input_pass, hash_pass)

    # создание JWT токена, с временем жизни 30 минут
    def encode_token(self, user_id):
        payload = {
            'exp': datetime.now(timezone.utc).replace(tzinfo=timezone.utc) + timedelta(seconds=1),
            'iat': datetime.now(timezone.utc).replace(tzinfo=timezone.utc),
            'user_id': user_id
        }
        return {
            'exp': int(payload['exp'].timestamp()),
            'token': jwt.encode(
                payload,
                self.secret,
                algorithm='HS256'
            )
        }

    # декодирование JWT токена
    def decode_token(self, token):
        try:
            payload = jwt.decode(
                token,
                self.secret,
                algorithms=['HS256']
            )
            return payload['user_id']
        except jwt.ExpiredSignatureError:
            raise HTTPException(401, 'Просрочено')
        except jwt.InvalidTokenError as e:
            raise HTTPException(401, 'Плохой токен')

    # мидлваре для защиты маршрутов
    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)


auth = AuthHandler()
