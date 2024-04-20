# importaciones
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Task, Facturation
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# vista añadir vegetal
@login_required
def task_create(request):

    """
    Añade un nuevo vegetal.

    Esta vista maneja la creación de un nuevo vegetal.
    se valida el formulario del vegetal y, si es válido, se guarda el vegetal en la base de datos
    y se redirige a la lista de vegetales.

    Args:
        request: La solicitud recibida.

    Returns:
        La respuesta con el formulario de creación de vegetales renderizado.
    """

    if request.method == "POST":
         # Si la solicitud es POST, se crea un formulario de tarea con los datos recibidos
        form = TaskForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, se guarda la tarea en la base de datos
            form.save()
            # Se redirige a la lista de tareas
            return redirect(reverse("tasks:task_list"))
    else:
        # Si la solicitud es GET, se crea un formulario de tarea vacío
        form = TaskForm()
    # Se renderiza el template 'tasks/task_form.html' con el formulario de vegetales
    return render(request, "tasks/task_form.html", { "form": form, })

# vista listar vegetales
@login_required
def task_list(request):

    """
    Muestra una lista de todas laos vegetales.

    Esta vista realiza una consulta a la base de datos para obtener todas los vegetales
    y las pasa al template 'tasks/task_list.html' para ser renderizadas.

    Args:
        request: una solicitud recibida.

    Returns:
        la respuesta con la lista de vegetales renderizada.
    """

    # Obtiene todas las tareas de la base de datos
    tasks = Task.objects.all()
    # Renderiza el template 'tasks/task_list.html' con los vegetales consultados
    return render(request, "tasks/task_list.html", { "tasks": tasks,})

# vista de facturacion
@login_required
def task_purchase(request):

    """
    Vista que muestra la página de facturacion de vegetales.

    Parameters:
        request: una solicitud recibida.

    Returns:
        Respuesta que renderiza la página de facturacion de vegetales.

    """

    # Obtiene todos los vegetales disponibles
    tasks = Task.objects.all()
    # Obtiene todos los elementos del carrito de compras (facturación)
    cart_items = Facturation.objects.all() 
    # Renderiza la plantilla HTML de facturacion, pasando los vegetales y los elementos del carrito como contexto
    return render(request, "tasks/task_purchase.html", {"tasks": tasks, "cart_items": cart_items})

# vista de detalles de un vegetal
@login_required
def task_detail(request, pk):

    """
    Vista que muestra los detalles de un vegetal en específico.

    Parameters:
        request: La solicitud recibida.
        pk (int): El identificador único del vegetal que se desea visualizar.

    Returns:
        Respuesta que renderiza la página de detalles del vegetal.

    """

    # Obtiene lel vegetal correspondiente al identificador único (pk) proporcionado, o devuelve un error 404 si no existe
    task = get_object_or_404(Task, pk=pk)

    # Renderiza la plantilla HTML de detalle del vegetal
    return render(request, "tasks/task_detail.html", { "task": task, })

# vista de inicio
def index(request):

    """
    Vista que muestra la página de inicio del sitio web.

    Parameters:
        request: La solicitud recibida.

    Returns:
        Respuesta que renderiza la página de inicio del sitio web

    """

    # Renderiza la plantilla HTML de la página de inicio del sitio web
    return render(request, "tasks/index.html")

# vista de salida / logout del usuario
def exit(request):

    """
    Vista que maneja la salida de un usuario del sistema.

    Parameters:
        request: La solicitud recibida.

    Returns:
        Redirecciona al usuario a la página de inicio después de cerrar sesión.

    """

    # Cierra la sesión del usuario actual
    logout(request)
    # Redirecciona al usuario a la página de inicio
    return redirect('/')

# vista de actualizacion de un vegetal
@login_required
def task_update(request, pk):

    """
    Vista que maneja la actualización de un vegetal existente.

    Parameters:
        request: La solicitud recibida.
        pk (int): El identificador único del vegetal que se desea actualizar.

    Returns:
        Respuesta que renderiza el formulario de actualización del vegetal o redirecciona a los detalles de la tarea.

    """

    # Obtiene la instancia del vegetal correspondiente al identificador único (pk) proporcionado, o devuelve un error 404 si no existe
    task_obj = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # Si la solicitud es POST, crea un formulario con los datos proporcionados por el usuario y la instancia del vegetal
        form = TaskForm(instance=task_obj, data=request.POST)
        if form.is_valid():
            # Si el formulario es válido, guarda los cambios
            form.save()
            # Redirecciona al usuario a la página de detalles del vegetal actualizado
            return redirect(reverse("tasks:task_detail", args=[pk,]))
    else:
        # Si la solicitud no es POST, crea un formulario con la instancia del vegetal
        form = TaskForm(instance=task_obj)
    # Renderiza la plantilla HTML del formulario del vegetal
    return render(request, "tasks/task_form.html", { "form": form, "object": task_obj})

# vista de eliminar vegetales
def task_delete(request, pk):

    """
    Vista que maneja la eliminación de un vegetal existente.

    Parameters:
        request: La solicitud recibida.
        pk (int): El identificador único del vegetal que se desea eliminar.

    Returns:
        Redirecciona al usuario a la lista de vegetales después de eliminarlo.

    """

    # Obtiene la instancia del vegetal correspondiente al identificador único (pk) proporcionado, o devuelve un error 404 si no existe
    task_obj = get_object_or_404(Task, pk=pk)
    # Elimina el vegetal
    task_obj.delete()
    # Redirecciona al usuario a la lista de vegetales
    return redirect(reverse("tasks:task_list"))



