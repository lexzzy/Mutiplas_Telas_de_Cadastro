from PyQt5 import uic,QtWidgets
import mysql.connector
import getpass

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd= '',
    database='cadastro_usuarios'
)

def Logar_CUsuario():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Usuario.LogarEdit.text()
    Senha = Tela_de_Login_Usuario.SenhaEdit.text()

    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Usuarios.show()
        Tela_de_Login_Usuario.LogarEdit.setText('')
        Tela_de_Login_Usuario.SenhaEdit.setText('')
        Tela_de_Login_Usuario.close()
    else:
        print('')

def Logar_CVendedor():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Vendedor.LogarEdit.text()
    Senha = Tela_de_Login_Vendedor.SenhaEdit.text( )

    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Vendedor.show()
        Tela_de_Login_Vendedor.close()
    else:
        print('')

def Logar_CAssociados():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Associados.LogarEdit.text()
    Senha = Tela_de_Login_Associados.SenhaEdit.text( )
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Associados.show()
        Tela_de_Login_Associados.close()
    else:
        print('')

def Logar_CProduto():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Produtos.LogarEdit.text()
    Senha = Tela_de_Login_Produtos.SenhaEdit.text( )

    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Produtos.show()
        Tela_de_Login_Produtos.close()
    else:
        print('')

def Logar_CCliente():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Cliente.LogarEdit.text()
    Senha = Tela_de_Login_Cliente.SenhaEdit.text( )

    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Cliente.show()
        Tela_de_Login_Cliente.close()
    else:
        print('')

def Logar_CFuncionario():
    usuarios = str('admin')
    senhas = str('admin')
    
    logar = Tela_de_Login_Funcionario.LogarEdit.text()
    Senha = Tela_de_Login_Funcionario.SenhaEdit.text( )

    if Senha == senhas and logar == usuarios:
        Tela_Cadastro_de_Funcionario.show()
        Tela_de_Login_Funcionario.close()
    else:
        print('')

def Finalizar_Usuario():
    Nome = Tela_Cadastro_de_Usuarios.NomeEdit.text()
    Sobrenome = Tela_Cadastro_de_Usuarios.SobrenomeEdit.text()
    Idade = Tela_Cadastro_de_Usuarios.IdadeEdit.text()
    data = Tela_Cadastro_de_Usuarios.DataNEdit.text()
    usuario = Tela_Cadastro_de_Usuarios.UsuarioEdit.text()
    senha = Tela_Cadastro_de_Usuarios.SenhaEdit.text()

    Genero = ''

    if Tela_Cadastro_de_Usuarios.radioFeminino.isChecked() :
        Genero = str('feminino')
    else:
        Genero = str('masculino')


    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO usuarios (nome,sobrenome,idade,data_de_nascimento,usuario, senha, genero) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    dados = (str(Nome), str(Sobrenome), str(Idade), str(data), str(usuario), str(senha), Genero)
    cursor.execute(comando_SQL,dados)
    banco.commit()

    Tela_Cadastro_de_Usuarios.NomeEdit.setText('')
    Tela_Cadastro_de_Usuarios.SobrenomeEdit.setText('')
    Tela_Cadastro_de_Usuarios.IdadeEdit.setText('')
    Tela_Cadastro_de_Usuarios.DataNEdit.setText('')
    Tela_Cadastro_de_Usuarios.UsuarioEdit.setText('')
    Tela_Cadastro_de_Usuarios.SenhaEdit.setText('')

def Finalizar_Produto():
    Nome_Prod = Tela_Cadastro_de_Produtos.ProdutoE.text()
    Desc_Prod = Tela_Cadastro_de_Produtos.DescricaoE.text()
    Valor_Prod = Tela_Cadastro_de_Produtos.VProdutoE.text()
    Fabri_Prod = Tela_Cadastro_de_Produtos.FabricanteE.text()
    Uni_Prod = Tela_Cadastro_de_Produtos.UnidadesE.text()
    CodB_Prod = Tela_Cadastro_de_Produtos.CodigoBarraE.text()

    Tipo_Prod = ''

    if Tela_Cadastro_de_Produtos.R_Eletronico.isChecked():
        Tipo_Prod = str('Eletronico')
    elif Tela_Cadastro_de_Produtos.R_Informatica.isChecked():
        Tipo_Prod = str('Informatica')
    elif Tela_Cadastro_de_Produtos.R_Objeto.isChecked():
        Tipo_Prod = str('Objeto')
    elif Tela_Cadastro_de_Produtos.R_Educativo.isChecked():
        Tipo_Prod = str('Educativo')
    else:
        Tipo_Prod = str('')

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO Produtos (Nome_Prod, Desc_Prod, Valor_Prod, Fabri_Prod, Tipo_Prod, Uni_Prod, CodB_Prod) VALUES (%s, %s, %s, %s, %s, %s, %s)'

    dados = (str(Nome_Prod), str(Desc_Prod), str(Valor_Prod), str(Fabri_Prod), str(Tipo_Prod), str(Uni_Prod), str(CodB_Prod))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    Tela_Cadastro_de_Produtos.ProdutoE.setText('')
    Tela_Cadastro_de_Produtos.DescricaoE.setText('')
    Tela_Cadastro_de_Produtos.VProdutoE.setText('')
    Tela_Cadastro_de_Produtos.FabricanteE.setText('')
    Tela_Cadastro_de_Produtos.UnidadesE.setText('')
    Tela_Cadastro_de_Produtos.CodigoBarraE.setText('')

def Finalizar_Funcionario():
    Nome = Tela_Cadastro_de_Funcionario.Nome_CompletoE.text()
    rg = Tela_Cadastro_de_Funcionario.rgE.text()
    Endereco = Tela_Cadastro_de_Funcionario.EnderecoE.text()
    cep = Tela_Cadastro_de_Funcionario.cepE.text()
    Nacionalidade = Tela_Cadastro_de_Funcionario.NacionalidadeE.text()
    EstadoCivil = ''
    Raca = ''
    Cargo = ''
    Salario = Tela_Cadastro_de_Funcionario.SalarioE.text()
    vr = Tela_Cadastro_de_Funcionario.vrE.text()
    vt = Tela_Cadastro_de_Funcionario.vtE.text()

    if Tela_Cadastro_de_Funcionario.SolteiroR.isChecked():
        EstadoCivil = str('Solteiro')
    elif Tela_Cadastro_de_Funcionario.CasadoR.isChecked():
        EstadoCivil = str('Casado')
    elif Tela_Cadastro_de_Funcionario.ViuvoR.isChecked():
        EstadoCivil = str('Viuvo')

    if Tela_Cadastro_de_Funcionario.NegroR.isChecked():
        Raca = str('Negro')
    elif Tela_Cadastro_de_Funcionario.PardoR.isChecked():
        Raca = str('Pardo')
    elif Tela_Cadastro_de_Funcionario.BrancoR.isChecked():
        Raca = str('Branco')
    elif Tela_Cadastro_de_Funcionario.AmareloR.isChecked():
        Raca = str('Amarelo')
    elif Tela_Cadastro_de_Funcionario.IndigenaR.isChecked():
        Raca = str('Indigena')

    if Tela_Cadastro_de_Funcionario.tiR.isChecked():
        Cargo = str('TI')
    elif Tela_Cadastro_de_Funcionario.EstoqueR.isChecked():
        Cargo = str('Estoque')
    elif Tela_Cadastro_de_Funcionario.VendasR.isChecked():
        Cargo = str('Vendas')
    elif Tela_Cadastro_de_Funcionario.MarketingR.isChecked():
        Cargo = str('Marketing')
    elif Tela_Cadastro_de_Funcionario.FinanceiroR.isChecked():
        Cargo = str('Financeiro')

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO Funcionario (Nome,RG,Endereco,CEP,Nacionalidade,EstadoCivil,Raca,Cargo,Salario,VR,VT) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    dados = (str(Nome), str(rg), str(Endereco), str(cep), str(Nacionalidade), str(EstadoCivil), str(Raca), str(Cargo), str(Salario), str(vr), str(vt))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    Tela_Cadastro_de_Funcionario.Nome_CompletoE.setText('')
    Tela_Cadastro_de_Funcionario.rgE.setText('')
    Tela_Cadastro_de_Funcionario.EnderecoE.setText('')
    Tela_Cadastro_de_Funcionario.cepE.setText('')
    Tela_Cadastro_de_Funcionario.NacionalidadeE.setText('')
    Tela_Cadastro_de_Funcionario.SalarioE.setText('')
    Tela_Cadastro_de_Funcionario.vrE.setText('')
    Tela_Cadastro_de_Funcionario.vtE.setText('')

def Finalizar_Associados():
    Nome_Empresa = Tela_Cadastro_de_Associados.NomeEmpresaE.text()
    cnpj = Tela_Cadastro_de_Associados.cnpjE.text()
    Numero_Gerente = Tela_Cadastro_de_Associados.NGerenteE.text()
    Ender_Empresa = Tela_Cadastro_de_Associados.EnderEmpresaE.text()
    acoes = Tela_Cadastro_de_Associados.AcoesE.text()

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO Associados (Nome_Empresa, CNPJ, Numero_Gerente,Endereco_da_Empresa,Acoes) VALUES (%s,%s,%s,%s,%s)'
    dados = (str(Nome_Empresa), str(cnpj), str(Numero_Gerente), str(Ender_Empresa), str(acoes))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    Tela_Cadastro_de_Associados.NomeEmpresaE.setText('')
    Tela_Cadastro_de_Associados.cnpjE.setText('')
    Tela_Cadastro_de_Associados.NGerenteE.setText('')
    Tela_Cadastro_de_Associados.EnderEmpresaE.setText('')
    Tela_Cadastro_de_Associados.AcoesE.setText('')

def Finalizar_Cliente():
    Nome = Tela_Cadastro_de_Cliente.NomeE.text()
    Endereco = Tela_Cadastro_de_Cliente.EnderecoE.text()
    cnpj = Tela_Cadastro_de_Cliente.cnpjE.text()
    tell = Tela_Cadastro_de_Cliente.TellE.text()
    codigo = Tela_Cadastro_de_Cliente.CodigoE.text()

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO Clientes (Nome, Endereco, cpf_cnpj, Tell, Codigo) VALUES (%s,%s,%s,%s,%s)'
    dados = (str(Nome), str(Endereco), str(cnpj), str(tell), str(codigo))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    Tela_Cadastro_de_Cliente.NomeE.setText('')
    Tela_Cadastro_de_Cliente.EnderecoE.setText('')
    Tela_Cadastro_de_Cliente.cnpjE.setText('')
    Tela_Cadastro_de_Cliente.TellE.setText('')
    Tela_Cadastro_de_Cliente.CodigoE.setText('')

def Finalizar_Vendedor():
    Nome = Tela_Cadastro_de_Vendedor.NomeE.text()
    Endereco = Tela_Cadastro_de_Vendedor.EnderecoE.text()
    cnpj = Tela_Cadastro_de_Vendedor.cnpjE.text()
    tell = Tela_Cadastro_de_Vendedor.TellE.text()
    codigo = Tela_Cadastro_de_Vendedor.CodigoE.text()

    tipo_vend = str('')

    if Tela_Cadastro_de_Vendedor.InternoR.isChecked():
        tipo_vend = str('Interno')
    elif Tela_Cadastro_de_Vendedor.ExternoR.isChecked():
        tipo_vend = str('Externo')

    cursor = banco.cursor()
    comando_SQL = 'INSERT INTO Vendedor (Nome, Endereco, cpf_cnpj, Tell, Codigo, Tipo_de_Vendedor) VALUES (%s,%s,%s,%s,%s,%s)'
    dados = (str(Nome), str(Endereco), str(cnpj), str(tell), str(codigo), str(tipo_vend))
    cursor.execute(comando_SQL, dados)
    banco.commit()
    
    Tela_Cadastro_de_Vendedor.NomeE.setText('')
    Tela_Cadastro_de_Vendedor.EnderecoE.setText('')
    Tela_Cadastro_de_Vendedor.cnpjE.setText('')
    Tela_Cadastro_de_Vendedor.TellE.setText('')
    Tela_Cadastro_de_Vendedor.CodigoE.setText('')

def Chama_Logar_Usuarios():
    Tela_de_Login_Usuario.show()

def Chama_Logar_Produtos():
    Tela_de_Login_Produtos.show()

def Chama_Logar_Funcionario():
    Tela_de_Login_Funcionario.show()

def Chama_Logar_Associados():
    Tela_de_Login_Associados.show()

def Chama_Logar_Cliente():
    Tela_de_Login_Cliente.show()

def Chama_Logar_Vendedor():
    Tela_de_Login_Vendedor.show()

app=QtWidgets.QApplication([])

##### Chamando Telas UI #####
Cadastro_Principal=uic.loadUi('Cadastro_Principal.ui')
Tela_Cadastro_de_Produtos=uic.loadUi('Tela_Cadastro_de_Produtos.ui')
Tela_Cadastro_de_Usuarios=uic.loadUi('Tela_Cadastro_de_Usuarios.ui')
Tela_Cadastro_de_Funcionario=uic.loadUi('Tela_Cadastro_de_Funcionario.ui')
Tela_Cadastro_de_Associados=uic.loadUi('Tela_Cadastro_de_Associados.ui')
Tela_Cadastro_de_Cliente=uic.loadUi('Tela_Cadastro_de_Cliente.ui')
Tela_Cadastro_de_Vendedor=uic.loadUi('Tela_Cadastro_de_Vendedor.ui')

### Chamando Tela de Login ###

Tela_de_Login_Usuario=uic.loadUi('Tela_de_Login_Usuario.ui')
Tela_de_Login_Vendedor=uic.loadUi('Tela_de_Login_Vendedor.ui')
Tela_de_Login_Associados=uic.loadUi('Tela_de_Login_Associados.ui')
Tela_de_Login_Cliente=uic.loadUi('Tela_de_Login_Cliente.ui')
Tela_de_Login_Produtos=uic.loadUi('Tela_de_Login_Produtos.ui')
Tela_de_Login_Funcionario=uic.loadUi('Tela_de_Login_Funcionario.ui')

### conectando BTN ###

### PRINCIPAL ###

Cadastro_Principal.UsuariosButton.clicked.connect(Chama_Logar_Usuarios)
Cadastro_Principal.ProdutosButton.clicked.connect(Chama_Logar_Produtos)
Cadastro_Principal.AssociadosButton.clicked.connect(Chama_Logar_Associados)
Cadastro_Principal.FuncionariosButton.clicked.connect(Chama_Logar_Funcionario)
Cadastro_Principal.ClienteButton.clicked.connect(Chama_Logar_Cliente)
Cadastro_Principal.VendedorButton.clicked.connect(Chama_Logar_Vendedor)

### TELA_CADASTRO ###


Tela_Cadastro_de_Produtos.FinalizarB.clicked.connect(Finalizar_Produto)
Tela_Cadastro_de_Usuarios.FinalizarButton.clicked.connect(Finalizar_Usuario)
Tela_Cadastro_de_Associados.FinalizarBT.clicked.connect(Finalizar_Associados)
Tela_Cadastro_de_Funcionario.FinalizarBT.clicked.connect(Finalizar_Funcionario)
Tela_Cadastro_de_Cliente.FinalizarBT.clicked.connect(Finalizar_Cliente)
Tela_Cadastro_de_Vendedor.FinalizarBT.clicked.connect(Finalizar_Vendedor)

### TELA_LOGIN ###

Tela_de_Login_Usuario.LogarButton.clicked.connect(Logar_CUsuario)
Tela_de_Login_Vendedor.LogarButton.clicked.connect(Logar_CVendedor)
Tela_de_Login_Cliente.LogarButton.clicked.connect(Logar_CCliente)
Tela_de_Login_Associados.LogarButton.clicked.connect(Logar_CAssociados)
Tela_de_Login_Produtos.LogarButton.clicked.connect(Logar_CProduto)
Tela_de_Login_Funcionario.LogarButton.clicked.connect(Logar_CFuncionario)

###
Cadastro_Principal.show()
app.exec()

### Tabela para criar variaveis de Login ###

'''
create table login (
id INT NOT NULL AUTO_INCREMENT,
usuario VARCHAR(10),
senha VARCHAR(15),
PRIMARY KEY (id)
)
'''

# Tabela para criar as variaveis de Usuarios

'''
create table usuarios (
id INT NOT NULL AUTO_INCREMENT,
nome VARCHAR(15),
sobrenome VARCHAR(20),
idade VARCHAR(3),
data_de_nascimento VARCHAR(10),
usuario VARCHAR(10),
genero VARCHAR(20),
senha VARCHAR(18),
PRIMARY KEY (id)
);
'''

# Tabela para criar as variaveis de produto

'''
create table Produtos (
id INT NOT NULL AUTO_INCREMENT,
Nome_Prod VARCHAR(20),
Desc_Prod VARCHAR(30),
Valor_Prod DOUBLE,
Fabri_Prod VARCHAR(20),
Tipo_Prod VARCHAR(15),
Uni_Prod INT,
CodB_Prod INT,
PRIMARY KEY (id)
);
'''

# Tabela para criar as Variaveis de Funcionario

'''
create table Funcionario (
id INT NOT NULL AUTO_INCREMENT,
Nome VARCHAR(20),
RG VARCHAR(14),
Endereco VARCHAR(35),
CEP VARCHAR(9),
Nacionalidade VARCHAR(15),
EstadoCivil VARCHAR(20),
Raca VARCHAR(20),
Cargo VARCHAR(20),
Salario DOUBLE,
VR DOUBLE,
VT DOUBLE,
PRIMARY KEY (id)
);
'''

# Tabela para criar as Variaveis de Associados

'''
create table Associados (
id INT NOT NULL AUTO_INCREMENT,
Nome_Empresa VARCHAR(15),
CNPJ VARCHAR(20),
Numero_Gerente INT,
Endereco_da_Empresa VARCHAR(30),
Acoes DOUBLE,
PRIMARY KEY (id)
);
'''

# Tabela para criar as Variaveis de Clientes

'''
create table Clientes (
id INT NOT NULL AUTO_INCREMENT,
Nome varchar(35),
Endereco varchar(25),
cpf_cnpj int,
Tell int,
Codigo int,
primary key (id)
);
'''

# Tabela para criar as Variaveis de Vendedor

'''
create table Vendedor (
id INT NOT NULL AUTO_INCREMENT,
Nome varchar(35),
Endereco varchar(25),
cpf_cnpj int,
Tell int,
Codigo int,
Tipo_de_Vendedor varchar(12),
primary key (id)
);
'''