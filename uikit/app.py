from slinn import Dispatcher, LinkFilter, HttpResponse
from ntml.ntmlc import ntml_compile

meals = {
	'Button': {'tag': 'button', 'props':({'class': 'Button Button-animation'}, [])},
	'CButton': {'tag': 'button', 'props':({'class': 'CButton Button-animation'}, [])},
	'MButton': {'tag': 'button', 'props':({'class': 'MButton Button-animation'}, [])},
	'SButton': {'tag': 'button', 'props':({'class': 'SButton Button-animation'}, [])},
	'CalculatorInput': {'tag': 'input', 'props': ({'class': 'CalculatorInput'}, [])},
	'ThreeDots': {'tag': 'button', 'props': ({'class': 'ThreeDots Button-animation'}, [])},
	'Container': {'tag': 'div', 'props': ({'class': 'Container'}, [])}
}
 
dp = Dispatcher()

# Write your code down here   
@dp(LinkFilter('m3uikit.css'))
def styles(request):
	return render('m3uikit.css')

@dp(LinkFilter('m3uikit_color.css'))
def styles(request):
	return render('m3uikit_color.css')

@dp(LinkFilter('styles.css'))
def styles(request):
	return render('styles.css')

@dp(LinkFilter(''))
def index(request):
	return render('index.ntml')



def render(path):
	try:
		extension = path.split('.')[-1]
		match extension:
			case 'html':
				with open(path, 'r') as f:
					return HttpResponse(f.read(), content_type='text/html')
			case 'ntml':
				with open(path, 'r') as f:
					return HttpResponse(ntml_compile(f.read(), path, meals), content_type='text/html')
			case 'css':
				with open(path, 'r') as f:
					return HttpResponse(f.read(), content_type='text/css')
	except FileNotFoundError:
		return '404 Not Found'
