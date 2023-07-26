from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_valor_23(self):
        entrada = "13/03/2000"  # Given - contexto
        esperado = 23

        funcionario_teste = Funcionario("Lucas Carvalho", entrada, 1000)

        resultado = funcionario_teste.idade()  # When - ação

        assert resultado == esperado  # Then - resultado

    def test_quando_sobrenome_recebe_lucas_carvalho_deve_retornar_carvalho(self):
        entrada = "Lucas Carvalho"
        esperado = "Carvalho"

        lucas = Funcionario(entrada, "11/11/2000", 1111)  # Given - contexto

        resultado = lucas.sobrenome()  # When - ação

        assert resultado == esperado  # Then - resultado

    def test_quando_decrescimo_de_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100_000  # Given - contexto
        entrada_nome = "Paulo Bragança"
        esperado = 90_000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)
        funcionario_teste.decrescimo_salario()  # When - ação
        resultado = funcionario_teste.salario

        assert resultado == esperado  # Then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
        resultado = funcionario_teste.calcular_bonus()  # when

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1_000_000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 1_000_000  # given

            funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then

    def test_retorno_str(self):
        nome, data_nascimento, salario = 'teste','12/03/2000',1000  # given
        esperado = "Funcionario(teste, 12/03/2000, 1000)"

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() # when

        assert resultado == esperado  # then