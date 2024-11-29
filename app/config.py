import json


class Config:
    @classmethod
    def load_config(cls) -> None:
        with open("config.json", encoding="utf8") as file:
            json_config: dict = json.loads(file.read())

            cls.bot_token = str(json_config.get("botToken"))
            cls.student_url = str(json_config.get("studentUrl"))
            cls.user_authorization = str(json_config.get("userAuthorization"))
            cls.email_regular = str(json_config.get("emailRegular"))

            messages_json: dict = dict(json_config.get("messages") or {})

            cls.start_command = str(messages_json.get("startCommand"))
            cls.get_user_error = str(messages_json.get("getUserError"))
            cls.email_not_specified = str(messages_json.get("emailNotSpecified"))
            cls.line_is_not_email = str(messages_json.get("lineIsNotEmail"))
            cls.binding_error = str(messages_json.get("bindingError"))
