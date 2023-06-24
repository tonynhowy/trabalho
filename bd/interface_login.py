import customtkinter as ctk
import PIL
from tkinter import *
from pagina_usuario import JanelaUsuario
from database.database import DataBase
              
class JanelaLogin(ctk.CTk, DataBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.aparencia_programa()
        self.frame_principal_login()
        self.criar_tabela()
        self.toplevel_window = None
 
    @staticmethod
    def aparencia_temas(setar_dark_light_mode):
        ctk.set_appearance_mode(setar_dark_light_mode)
    
    def abrir_janela_usuario(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            # esconde a janela principal
            self.withdraw()
            
            self.toplevel_window = JanelaUsuario(
                self)  # cria uma janela se não existe nenhuma ou destroi
            self.toplevel_window.protocol("WM_DELETE_WINDOW", self.fechar_janela_usuario)
        else:
            self.toplevel_window.focus()  # se a janela existe, foca nela

    def fechar_janela_usuario(self):
        if self.toplevel_window and self.toplevel_window.winfo_exists():
            self.deiconify()
            self.toplevel_window.destroy()
    
    def aparencia_programa(self):   
        self.tema_aparencia = ctk.CTkLabel(
            self, text='Tema',
            bg_color='#A567BB',
            fg_color='#A567BB',
            text_color=('#A567BB', '#A567BB')
        )
        
        self.opcao_tema = ctk.CTkOptionMenu(
            self,
            width=20,
            height=20,
            fg_color='#A567BB',
            button_color='#A567BB',
            button_hover_color='#A567BB',
            values=['Dark', 'Light'],
            corner_radius=15,
            command=self.aparencia_temas,
            font=('Berlin Sans FB', 14),
        )
        self.opcao_tema.place(x=5, y=400)
        
    def mostrar_senha_login(self):
        if self.ver_senha._check_state == True:
            self.entrada_senha_login.configure(show='')
        else:
            self.entrada_senha_login.configure(show='*')
            
    def frame_principal_login(self):
        self.title('Login')
        self.geometry('700x450')
        self.resizable(False, False)
        
        # IMAGEM PRINCIPAL USADA NA "MAIN FRAME"
        self.imagem_principal = ctk.CTkImage(PIL.Image.open('imagens\logo_login.png'),
                                             size=(200, 200))
        self.label_imagem = ctk.CTkLabel(self, text='', image=self.imagem_principal)
        self.label_imagem.grid(row=0, column=0, padx=80, pady=220)
        
        # FRAME DE BOAS VINDAS
        self.frame_boas_vindas = ctk.CTkFrame(self, width=200, height=100)
        self.frame_boas_vindas.place(x=15, y=15)
        
        # TÍTULO DE BOAS VINDAS
        self.titulo_boas_vindas = ctk.CTkLabel(
            self.frame_boas_vindas,
            text='Olá, seja bem vindo(a)! \nFaça o seu login ou cadastre-se \nna nossa '
                 'plataforma para acessar \nos nossos serviços!',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_boas_vindas.grid(row=0, column=0, padx=20, pady=35)
        
        # MAIN FRAME - QUADRO PRINCIPAL
        self.frame_login = ctk.CTkFrame(self, width=350, height=380)
        self.frame_login.place(x=350, y=15)
       
        # widgets no frame - forms
        self.label_login = ctk.CTkLabel(
            self.frame_login,
            text=' \nfaça o seu login:',
            font=('Berlin Sans FB', 24)
        )
        self.label_login.grid(row=0, column=0, pady=10)
        
        self.entrada_login_username = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Seu nome de usuário:',
            font=('Berlin Sans FB', 16),
            corner_radius=15
        )
        self.entrada_login_username.grid(row=1, column=0, pady=10, padx=20)
        
        self.entrada_senha_login = ctk.CTkEntry(
            self.frame_login,
            width=300,
            placeholder_text='Sua senha de usuário:',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            show='*'
        )
        self.entrada_senha_login.grid(row=2, column=0, pady=10, padx=10)
        
        self.ver_senha = ctk.CTkCheckBox(
            self.frame_login,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='Clique para ver a senha.',
            font=('Berlin Sans FB', 14),
            corner_radius=40,
            command=self.mostrar_senha_login
        )
        self.ver_senha.grid(row=3, column=0, pady=10, padx=10)
        
        # BOTÃO DE ENTRAR
        self.botao_entrar = ctk.CTkButton(
            self.frame_login,
            width=300,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='ENTRAR',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            command=self.abrir_janela_usuario
        )
        self.botao_entrar.grid(row=4, column=0, pady=10, padx=10)
        
        self.msg_fazer_cadastro = ctk.CTkLabel(
            self.frame_login,
            text='\nNão tem cadastro?!'
                 '\nClique em baixo para se juntar à comunidade! \n💜',
            font=('Berlin Sans FB', 14)
        )
        self.msg_fazer_cadastro.grid(row=5, column=0, pady=10)
        
        self.button_cadastro = ctk.CTkButton(
            self.frame_login, width=300,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='CADASTRE-SE',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            command=self.frame_principal_cadastro
        )
        self.button_cadastro.grid(row=6, column=0, pady=10, padx=10)
        
    def mostrar_senha_cadastro(self):
        if self.ver_senha_cadastro._check_state == True:
            self.entrada_senha_cadastro.configure(show='')
            self.entrada_confirmar_senha_cadastro.configure(show='')
        else:
            self.entrada_senha_cadastro.configure(show='*')
            self.entrada_confirmar_senha_cadastro.configure(show='*')
            
    def frame_principal_cadastro(self):
        # limpar tela de login
        self.frame_login.place_forget()
        self.frame_boas_vindas.place_forget
        
        # frame dos widgets
        self.frame_cadastro = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro.place(x=350, y=15)
        
        # texto explicativo
        self.frame_cadastro_txt = ctk.CTkFrame(self, width=200, height=100)
        self.frame_cadastro_txt.place(x=15, y=15)
    
        self.titulo_explica_cadastro = ctk.CTkLabel(
            self.frame_cadastro_txt,
            text='faça o seu cadastro de forma rápida:',
            font=('Berlin Sans FB', 20)
        )
        self.titulo_explica_cadastro.grid(row=0, column=0, padx=10, pady=10)
        
        self.explicar_cadastro = ctk.CTkLabel(
            self.frame_cadastro_txt,
            text='1: preencha os seus dados.' 
                '\n2: verifique a disponibilidade do '
                '\nnome de usuário escolhido.'
                '\n 3: é só finalizar e aproveitar!',
            font=('Berlin Sans FB', 20)
        )
        self.explicar_cadastro.grid(row=1, column=0, padx=10, pady=10)
        
        # botão voltar
        self.button_voltar_login = ctk.CTkImage(
            PIL.Image.open('imagens/btn_voltar.png'), size=(26, 26)
        )
        self.button_voltar_login = ctk.CTkButton(
            self.frame_cadastro,
            image=self.button_voltar_login,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='',
            height=30,
            width=30,
            corner_radius=5,
            command=self.frame_principal_login
        )
        self.button_voltar_login.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        # titulo do cadastro
        self.cadastro_title = ctk.CTkLabel(
            self.frame_cadastro,
            text='insira seus dados:',
            font=('Berlin Sans FB', 24)
        )
        self.cadastro_title.grid(row=1, column=0, pady=10)
        
        # widgets da tela de cadastro
        self.entrada_nome_cadastro = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Seu nome:',
            font=('Berlin Sans FB', 16),
            corner_radius=15
        )
        self.entrada_nome_cadastro.grid(row=2, column=0, pady=5, padx=20)
        
        self.entrada_username_cadastro = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Nome de usuário:',
            font=('Berlin Sans FB', 16),
            corner_radius=15
        )
        self.entrada_username_cadastro.grid(row=3, column=0, pady=5, padx=10)
        
        self.verificar_username = ctk.CTkButton(
            self.frame_cadastro,
            width=150,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='VERFICAR NOME DE USUÁRIO',
            font=('Berlin Sans FB', 16),
            corner_radius=15
        )
        self.verificar_username.grid(row=4, column=0, pady=5, padx=10)
        
        self.entrada_numero_cadastro = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Número de telefone (xx) xxxxx-xxxx',
            font=('Berlin Sans FB', 16),
            corner_radius=15
        )
        self.entrada_numero_cadastro.grid(row=5, column=0, pady=5, padx=10)
                
        self.entrada_senha_cadastro = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Senha de usuário:',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            show='*'
        )
        self.entrada_senha_cadastro.grid(row=6, column=0, pady=5, padx=10)

        self.entrada_confirmar_senha_cadastro = ctk.CTkEntry(
            self.frame_cadastro,
            width=300,
            placeholder_text='Confirmar senha de usuário:',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            show='*'
        )
        self.entrada_confirmar_senha_cadastro.grid(row=7, column=0, pady=5, padx=10)
                
        self.ver_senha_cadastro = ctk.CTkCheckBox(
            self.frame_cadastro,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='Clique para ver a senha.',
            font=('Berlin Sans FB', 14),
            corner_radius=30,
            command=self.mostrar_senha_cadastro
        )
        self.ver_senha_cadastro.grid(row=8, column=0, pady=5, padx=10)
        
        # botão da proxima estapa
        self.button_cadastro = ctk.CTkButton(
            self.frame_cadastro,
            width=300,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='FINALIZAR CADASTRO',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            command= self.cadastrar_usuario
        )
        self.button_cadastro.grid(row=9, column=0, pady=10, padx=10)
    
    def cadastro_finalizado(self):
        self.frame_cadastro.place_forget()
        self.frame_cadastro_txt.place_forget()
 
        
        self.frame_cadastro_finalizado = ctk.CTkFrame(self, width=350, height=380)
        self.frame_cadastro_finalizado.place(x=350, y=15)
        
        self.cadastro_concluido = ctk.CTkLabel(
            self.frame_cadastro_finalizado,
            text='cadastro concluído! \nseja bem vindo(a)!',
            font=('Berlin Sans FB', 24)
        )
        self.cadastro_concluido.grid(row=1, column=0, pady=60)
        
        self.img_hands = ctk.CTkImage(
            PIL.Image.open('imagens\img_welcome.png'), size=(115, 100)
        )
        self.welcome_img = ctk.CTkLabel(
            self.frame_cadastro_finalizado,
            text='', image=self.img_hands)
        self.welcome_img.grid(row=2, column=0, padx=0, pady=0)
        
        self.ir_ao_login = ctk.CTkButton(
            self.frame_cadastro_finalizado,
            width=300,
            fg_color='#A567BB',
            hover_color='#bc91e6',
            text='IR PARA O LOGIN',
            font=('Berlin Sans FB', 16),
            corner_radius=15,
            command=self.frame_principal_login
        )
        self.ir_ao_login.grid(row=3, column=0, pady=60, padx=20)

    def limpar_entrada_login(self):
        self.entrada_login_username.delete(0, END)
        self.entrada_senha_login.delete(0, END)
    
    def limpar_entrada_cadastro(self):
        self.entrada_nome_cadastro.delete(0, END)
        self.entrada_username_cadastro.delete(0, END) 
        self.entrada_numero_cadastro.delete(0, END)
        self.entrada_senha_cadastro.delete(0, END)
        self.entrada_confirmar_senha_cadastro.delete(0, END)
    
janela = JanelaLogin()
janela.mainloop()