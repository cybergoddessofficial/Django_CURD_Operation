
from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('displaystudent',views.displaystudent,name="displaystudent"),
    path('editstudent/<int:dataid>',views.editstudent,name="editstudent"),
    path('deletestudent/<int:dataid>',views.deletestudent,name="deletestudent"),
    path('addadmin',views.addadmin,name="addadmin"),
    path('displayadmin',views.displayadmin,name="displayadmin"),
    path('editadmin/<int:dataid>',views.editadmin,name="editadmin"),
    path('deleteadmin/<int:dataid>',views.deleteadmin,name="deleteadmin"),
    path('addcategory',views.addcategory,name="addcategory"),
    path('displaycategory',views.displaycategory,name="displaycategory"),
    path('editcategory/<int:dataid>', views.editcategory, name="editcategory"),
    path('deletecategory/<int:dataid>', views.deletecategory, name="deletecategory"),

]
