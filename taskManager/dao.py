from .models import *
from .forms import *
    
class taskDao:
    def registerTask(self, resquet, user):        
        form = TaskForm(resquet.POST)
        if form.is_valid():
            task = form.save(commit=False)            
            member = Member.objects.get(user=user) 
            task.member = member
            self.save(form.cleaned_data, member)
            return task
        
    def listTask(self, user):
        member = Member.objects.get(user=user)      
        return Task.objects.filter(member=member).order_by('completed', '-created_at')
    
    def deleteTask(self, pk):
        try:
            obj = Task.objects.get(pk=pk)
            obj.delete()
            return 0
        except Task.DoesNotExist:
            return 1
        
    def getTask(self, pk):
        return Task.objects.get(pk=pk)
    
    def updateTask(self, form, task):
        if form.is_valid():                
                task.title = form.cleaned_data['title']
                task.description = form.cleaned_data['description']
                task.completed = form.cleaned_data['completed']
                task.updated_at = timezone.now()
                task.save()
                return task
        
    def save(self, cleaned_data, m):
        title = cleaned_data['title']
        description = cleaned_data['description']

        task = Task.objects.create(
            title=title,
            description=description,
            member=m,
        )
        return task