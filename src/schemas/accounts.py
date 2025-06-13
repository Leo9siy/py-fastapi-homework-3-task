from pydantic import BaseModel, field_validator



class EmailSchema(BaseModel):
    email: str


class PasswordSchema(BaseModel):
    password: str


class UserRegisterSchema(EmailSchema, PasswordSchema):

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Password must contain at least 8 characters.")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit.")
        if not any(c.islower() for c in v):
            raise ValueError("Password must contain at least one lower letter.")
        if not any(c in "@$!%*?#&" for c in v):
            raise ValueError("Password must contain at least one special character: @, $, !, %, *, ?, #, &.")
        return v


class UserLoginSchema(UserRegisterSchema):
    pass


class UserRegisterResponse(EmailSchema):
    id: int


class UserActivationRequestSchema(EmailSchema):
    token: str


class ResponseSchema(BaseModel):
    message: str


class UserResetPasswordCoplete(EmailSchema, PasswordSchema):
    token: str


class UserLoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str
