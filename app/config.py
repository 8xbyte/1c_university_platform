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
            cls.guid_regular = str(json_config.get("guidRegular"))

            messages_json: dict = dict(json_config.get("messages") or {})

            cls.start_command = str(messages_json.get("startCommand"))
            cls.get_user_error = str(messages_json.get("getUserError"))
            cls.arguments_not_specified = str(messages_json.get("argumentsNotSpecified"))
            cls.not_enough_arguments = str(messages_json.get("notEnoughArguments"))
            cls.line_is_not_email = str(messages_json.get("lineIsNotEmail"))
            cls.line_is_not_guid = str(messages_json.get("lineIsNotGuid"))
            cls.binding_error = str(messages_json.get("bindingError"))
            cls.wrong_guid = str(messages_json.get("wrongGuid"))
