# sca-day-2-project
 Rendering a Basic HTML Page

 - after setting up your app, reate the html page inside the 'templates' folder of each app

 - define your view function in the views.py file of each app
 return render(request, 'html_page', {optional_parameter_object})

 - create a urls.py file in each app folder and define your urlpatterns (URLConfig)
  path('', views.name_of_function) 

- add all paths to the core urls.py under urlpatterns
path('prefered_path', include('filename'))