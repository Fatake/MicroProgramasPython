def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
  for i in range(len(alumnos)):
    if alumnos[i] == alumno_buscado:
      print alumno_buscado, nota[i]
      return
  print 'El alumno %s no pertenece al grupo' % alumno_buscado
