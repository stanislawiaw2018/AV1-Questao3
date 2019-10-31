from django.db import models


class Item(models.Model):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Itens"

    nome = models.CharField("Nome do Item",null=False,blank=False)
    descricao = models.TextField("Descrição",null=False,blank=False)

    def __str__(self):
        self.nome

class Tema(models.Model):
    class Meta:
        verbose_name_plural = "Temas"
        verbose_name = "Tema"

    TIPO_CORES = [
        ("1","Vermelho"),
        ("2","Verde"),
        ("3","Amarelo"),
        ("4","Azul"),
        ("5","Rosa"),
        ("6","Laranja"),
    ]
    nome = models.CharField("Título do Tema",max_length=50,null=False,blank=False)
    valor = models.DecimalField("Valor do Aluguel",max_digits=6,decimal_places=2,null=False,blank=False)
    cor = models.CharField("Cor da mesa", max_length=1,choices=TIPO_CORES,default="1")
    item1 = models.ForeignKey("Item 1",Item,on_delete=models.CASCADE,null=True,blank=True)
    item2 = models.ForeignKey("Item 2", Item,on_delete=models.CASCADE, null=True, blank=True)
    item3 = models.ForeignKey("Item 3", Item,on_delete=models.CASCADE, null=True, blank=True)
    item4 = models.ForeignKey("Item 4", Item,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        self.nome


class Endereco(models.Model):
    ESTADOS = [
        ("SP","São Paulo"),
        ("PI","Piauí"),
        ("MT","Mato Grosso"),
        ("MS","Mato Grosso do Sul"),
        ("MG","Minas Gerais"),
    ]
    logradouro = models.CharField("Logradouro",max_length=50,null=False,blank=False)
    numero = models.CharField("Número",max_length=4,null=False,blank=False)
    complemento = models.CharField("Complemento", max_length=50,null=True,blank=True)
    bairro = models.CharField("Bairro", max_length=50,null=False,blank=False)
    cidade = models.CharField("Cidade", max_length=50,null=False,blank=False)
    uf = models.CharField("UF", max_length=2,choices=ESTADOS,default="",null=False,blank=False)
    cep = models.CharField("CEP", max_length=10,null=False,blank=False)


class Aluguel(models.Model):
    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"

    data_festa = models.DateField("Data da Festa",null=False,blank=False)
    horai = models.TimeField("Hora Inicial",null=False,blank=False)
    horat= models.TimeField("Hora Término",null=False,blank=False)
    valor = models.DecimalField("Valor Cobrado", max_digits=8,decimal_places=2,null=False,blank=False)
    tema = models.ForeignKey("Título do Tema",Tema,null=True,blank=True,default="")
    endereco = models.OneToOneField("Endereço",Endereco,on_delete='CASCADE')
    def __str__(self):
        return self.data_festa

class Cliente(models.Model):
    nome = models.CharField("Nome Cliente",max_length=50,null=False,blank=False)
    telefone = models.CharField("Telefone",max_length=12,null=False,blank=False)
    aluguel = models.ForeignKey("Aluguel",Aluguel,on_delete=models.CASCADE,null=True,blank=True)


