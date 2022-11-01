class Validator:
    @staticmethod
    def raises_if_string_is_empty(string, error_message):
        if string.strip() == '':
            raise ValueError(error_message)

    @staticmethod
    def if_number_is_less_than(number, min_number, message):
        if number < min_number:
            raise ValueError(message)

    @staticmethod
    def raises_if_string_is_less_than(string, min_value, message):
        if len(string) < min_value:
            raise ValueError(message)

    @staticmethod
    def raises_if_string_not_in_list(string, message):
        valid_types = ["Winter", "Spring", "Autumn", "Summer"]
        if string not in valid_types:
            raise ValueError(message)
