import tabula

lista_tabelas = tabula.read_pdf("Pellegrini.pdf", pages="all")
print(len(lista_tabelas))