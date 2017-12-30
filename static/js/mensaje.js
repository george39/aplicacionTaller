

{% load staticfiles %}

<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Inventario{% endblock %}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <link rel="stylesheet" href="{% static 'css/bootstrap.css' %}" media="screen">
    <link rel="stylesheet" href="{% static 'css/custom.min.css' %}">
    

    <!-- HTML5 shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="../bower_components/html5shiv/dist/html5shiv.js"></script>
      <script src="../bower_components/respond/dest/respond.min.js"></script>
    <![endif]-->
    
  </head>
  <body>
  {% block header %}
  <!--<div align="center"><IMG src="{% static 'registro/css/matrix.jpg' %}" WIDTH=178 HEIGHT=180></div> -->
  
    <!--<input type="submit" value="Registrar" /> -->
  </form >
    <div class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <a href="../" class="navbar-brand">Inicio</a>
          <button class="navbar-toggle" type="button" data-toggle="collapse" data-target="#navbar-main">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
        </div>
       
        <div class="navbar-collapse collapse" id="navbar-main">
          <ul class="nav navbar-nav">
            <li class="dropdown">
         <!--      <a class="dropdown-toggle" data-toggle="dropdown" href="registro" id="themes">Registro <span class="caret"></span></a>
        -->  
            <li>
              <a href="registros">Salidas</a>
            </li> 

            <li>
              <a href="compras">Compras</a>
            </li>  
            
            <li>
              <a href="productos">Productos</a>
            </li>
            <li>
              <a href="proveedor">Proveedores</a>
            </li>
            <li>
              <a href="ventas">Ventas</a>
            </li>

            
            
          </ul>
          <!--
          <form class="navbar-search pull-left" action="compra/listar">
              <input class="form-control mr-sm-2" type="text" placeholder="Buscar" aria-label="Search">
              <button class="btn btn-outline-success " type="submit">Buscar</button>
            </form>
          -->
        </div>
      </div>
    </div>


    <div class="container">

      
        <div class="row">
          <div class="col-lg-8 col-md-7 col-sm-6">
           
         
          </div>
          <div class="col-lg-4 col-md-5 col-sm-6">
            
            </div>
          </div>
        

    <script src="https://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/custom.js' %}"></script>
  </body>
</html>




<div class="row">
	<div class="col-md-4">
		<div class="alert alert-success">
		<button class="close" data-dismiss="alert"><span>&times;</span> </button>
		Los datos fueron guardados con exito
		</div>
			
		
		
	</div>
	
</div>