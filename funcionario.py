#AGORA ESSE ARQUIVO É UM MÓDULO
#RESPONSÁVEL POR FUNCIONALIDADES REFERENTES A FUNCIONÁRIO

#listar conexão
from database import conectar


def listar_funcionarios():
#Abrir conexão
    conexao = conectar()

    #Criar cursor

    cursor = conexao.cursor()

    #sql da consulta

    sql = """
    SELECT 
        f.id_funcionario,
        f.nome,
        f.cargo,
        s.nome AS setor
    from funcionario f
    join setor s on f.id_setor = s.id_setor
    """
    #executa sql
    cursor.execute(sql)

    #recuperar dados
    dados = cursor.fetchall()


    #exibir dados
    for funcionario in dados: 
        print(funcionario)

    #fechar a conexao

    cursor.close()
    conexao.close()

def cadastrar_funcionario(nome,cargo,id_setor):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO funcionario (nome, cargo, id_setor)
    VALUES (%s, %s, %s)
    """
    valores = (nome, cargo, id_setor)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Funcionário cadastrado com sucesso!")

    cursor.close()
    conexao.close()

def atualizar_cargo(id_funcionario, novo_cargo):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = """
    UPDATE funcionario
    SET cargo = %s
    WHERE id_funcionario = %s
    """
    valores = (novo_cargo, id_funcionario)
    cursor.execute(sql, valores)
    conexao.commit()

    print("Cargo do funcionário atualizado com sucesso!")

    cursor.close()
    conexao.close()
    