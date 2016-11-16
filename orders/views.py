from django.shortcuts import render, loader
from .models import Client
from .models import Provider
from .models import Region
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.template import RequestContext



def home(request):
    return render(request, 'index.html', {})

def page_provider(request, name):
	provider = Provider.objects.get(provider_name=name)
	regions = provider.regions_provider.all()
	context = {
		'name': name,
		'regions': regions,
	}
	return render(request, 'page_provider.html', context)
	
def  search(request):	
	form = {}
	errors = []
	
	try:
		if request.method=='POST':
			form['client'] = request.POST.get('client')
			if not form['client']:
				errors.append('Errors')
				return home(request)
			

			client = Client.objects.get(client_name=form['client']) 
			providers_list = set()
			providers_all = Provider.objects.all()
			for region in client.regions_client.all():
				for provider in providers_all:
					if provider.regions_provider.filter(region_id=region.region_id):
						providers_list.add(provider)
			
			template = loader.get_template('index.html')
			context = RequestContext(request, {'providers_list': providers_list,})
			return HttpResponse(template.render(context))
		return home(request)
		
	except Client.DoesNotExist:
		return home(request)
