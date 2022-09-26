# sca-day-2-project

 Rendering a Basic HTML Page

1. Create an app called courses, students, profile

2. Register the apps in your settings.

3. Create a custom page for each app and render a basic html page for each app with each having a h1 heading corresponding to their app name and a body of any random text... (You can be creative)

Note : the three apps will have their separate routes.
E.g Courses app will be on http://localhost:8000/courses
etc 


 - after setting up your app, reate the html page inside the 'templates' folder of each app

 - define your view function in the views.py file of each app
 return render(request, 'html_page', {optional_parameter_object})

 - create a urls.py file in each app folder and define your urlpatterns (URLConfig)
  path('', views.name_of_function) 

- add all paths to the core urls.py under urlpatterns
path('prefered_path', include('filename'))
