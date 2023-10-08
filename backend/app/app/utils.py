from datetime import datetime, timedelta
from typing import Optional

from app.core.config import settings
from app.schemas.response import OkResponse
from jose import jwt


def generate_password_reset_token(email: str) -> str:
    delta = timedelta(hours=settings.EMAIL_RESET_TOKEN_EXPIRE_HOURS)
    now = datetime.utcnow()
    expires = now + delta
    exp = expires.timestamp()
    encoded_jwt = jwt.encode(
        {"exp": exp, "nbf": now, "sub": email},
        settings.SECRET_KEY,
        algorithm="HS256",
    )
    return encoded_jwt


def verify_password_reset_token(token: str) -> Optional[str]:
    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, algorithms=["HS256"])
        return decoded_token["email"]
    except jwt.JWTError:
        return None


def get_responses_description_by_codes(
        codes: list[int],
):
    all_titles = {
        400: "Переданы невалидные данные",
        401: "Ошибка авторизации",
        403: "Отказано в доступе",
        404: "Не найдено",
        422: "Переданы некорректные данные",
        500: "Ошибка сервера",
        502: "Ошибка прокси"
    }

    codes.append(422)
    codes.append(500)
    codes.append(502)

    codes = list(set(codes))

    responses = {}

    for code in codes:
        responses[code] = {
            'model': OkResponse,
            'description': all_titles.get(code, f"Error {code}")
        }

    return responses
