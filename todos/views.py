from django.shortcuts import render, redirect 
from django.contrib import messages 

## import todo form and models 

from .forms import todosform
from .models import Work

############################################### 

def index(request): 

	item_list = Work.objects.all() 
	if request.method == "POST": 
		form = todosform(request.POST) 
		if form.is_valid(): 
			form.save() 
			return redirect("/") 
	form = todosform() 

	page = { 
			"forms" : form, 
			"list" : item_list, 
			"name" : "TODO LIST", 
		} 
	return render(request, 'index.html', page) 



### function to remove item, it recive todo item id from url ## 
def remove(request, item_id): 
    item = Work.objects.get(id=item_id) 
    item.delete()
    messages.info(request," Deleted succesfully!...Please add more work")
    return redirect("/")
