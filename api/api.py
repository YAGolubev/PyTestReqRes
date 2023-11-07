import allure
import requests
from jsonschema import validate
from helper.parser import get_data
from helper.load import load_json_schema
from helper.logger import log


class Api:
    """Основной класс для работы с API"""
    _HEADERS = {'Content-Type': 'application/json; charset=utf-8'}
    _TIMEOUT = 10
    base_url = {}

    def __init__(self):
        self.response = None

    @allure.step("Отправить POST-запрос")
    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None):
        with allure.step(f"POST-запрос на url: {url}{endpoint}"
                         f"\n тело запроса: \n {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=self._HEADERS,
                                          params=params,
                                          json=json_body,
                                          timeout=self._TIMEOUT)
        log(response=self.response, request_body=json_body)
        return self

    @allure.step("Статус-код ответа равен {expected_code}")
    def status_code_should_be(self, expected_code: int):
        """Проверяем статус-код ответа actual_code на соответствие expected_code"""
        actual_code = self.response.status_code
        assert expected_code == actual_code, f"\nОжидаемый результат: {expected_code} " \
                                             f"\nФактический результат: {actual_code}"
        return self

    @allure.step("ОР: Cхема ответа json валидна")
    def json_schema_should_be_valid(self, path_json_schema: str,
                                    name_json_schema: str = 'schema'):
        """Проверяем полученный ответ на соответствие json-схеме"""
        json_schema = load_json_schema(path_json_schema, name_json_schema)
        validate(self.response.json(), json_schema)
        return self

    @allure.step("ОР: Объекты равны")
    def objects_should_be(self, expected_object, actual_object):
        """Сравниваем два объекта"""
        assert expected_object == actual_object, f"\nОжидаемый результат: {expected_object} " \
                                                 f"\nФактический результат: {actual_object}"
        return self

    @allure.step("ОР: В поле ответа содержится искомое значение")
    def have_value_in_response_parameter(self, keys: list, value: str):
        """Сравниваем значение необходимого параметра"""
        payload = self.get_payload(keys)
        assert value == payload, f"\nОжидаемый результат: {value} " \
                                 f"\nФактический результат: {payload}"
        return self

    def get_payload(self, keys: list):
        """Получаем payload, переходя по ключам,
        возвращаем полученный payload"""
        response = self.response.json()
        # payload = self.json_parser.find_json_vertex(response, keys)
        payload = get_data(keys, response)
        return payload
